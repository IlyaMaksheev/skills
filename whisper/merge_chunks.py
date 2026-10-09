#!/usr/bin/env python3
"""Validate Whisper JSON and write timestamped artifacts for a single file or WAV chunks."""

import argparse
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import wave


class InputError(ValueError):
    pass


def positive_number(value):
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError("expected a positive finite number")
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("expected a positive finite number")
    return number


def positive_integer(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("expected a positive integer")
    return number


def timestamp(seconds, comma=False):
    # Round before splitting, including carry across second/minute/hour boundaries.
    millis = int(round(seconds * 1000))
    hours, remainder = divmod(millis, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    secs, millis = divmod(remainder, 1000)
    return "{:02d}:{:02d}:{:02d}{}{:03d}".format(hours, minutes, secs, "," if comma else ".", millis)


def number(value, context):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise InputError("{} must be a finite numeric timestamp".format(context))
    return float(value)


def indexed_files(directory, suffix, limit):
    if not directory.is_dir():
        raise InputError("Not a directory: {}".format(directory))
    pattern = re.compile(r"part_(\d+)\." + re.escape(suffix) + r"$")
    files = {}
    for path in directory.glob("part_*." + suffix):
        match = pattern.fullmatch(path.name)
        if not match or not path.is_file():
            raise InputError("Invalid chunk file: {}".format(path))
        index = int(match.group(1))
        if index in files:
            raise InputError("Duplicate chunk index {} in {}".format(index, directory))
        files[index] = path.resolve()
        if len(files) > limit:
            raise InputError("Chunk count exceeds --max-chunks={}".format(limit))
    if not files:
        raise InputError("No part_*.{} files in {}".format(suffix, directory))
    return files


def inputs(args):
    if args.input_json:
        path = args.input_json.resolve()
        if not path.is_file():
            raise InputError("JSON file missing: {}".format(path))
        return [(path, 0.0, args.duration, None)]
    audio = indexed_files(args.audio_dir, "wav", args.max_chunks)
    results = indexed_files(args.input_dir, "json", args.max_chunks)
    if sorted(audio) != list(range(len(audio))):
        raise InputError("WAV chunk indices must be contiguous and start at zero")
    if set(audio) != set(results):
        missing = sorted(set(audio) - set(results))
        extra = sorted(set(results) - set(audio))
        raise InputError("Incomplete/mismatched JSON chunks; missing={}, extra={}".format(missing[:20], extra[:20]))
    offset = 0.0
    planned = []
    for index in range(len(audio)):
        try:
            with wave.open(str(audio[index]), "rb") as wav:
                duration = wav.getnframes() / wav.getframerate()
        except (OSError, EOFError, wave.Error, ZeroDivisionError) as exc:
            raise InputError("Cannot inspect WAV {}: {}".format(audio[index], exc))
        if not math.isfinite(duration) or duration <= 0:
            raise InputError("Empty/invalid WAV: {}".format(audio[index]))
        planned.append((results[index], offset, duration, audio[index]))
        offset += duration
    return planned


def reject_constant(value):
    raise InputError("Non-finite JSON constant: {}".format(value))


def finite_float(value):
    result = float(value)
    if not math.isfinite(result):
        raise InputError("Non-finite JSON number: {}".format(value))
    return result


def load_results(planned, args):
    byte_limit = int(args.max_total_mb * 1024 * 1024)
    file_limit = int(args.max_json_mb * 1024 * 1024)
    sizes = [path.stat().st_size for path, _, _, _ in planned]
    if any(size > file_limit for size in sizes) or sum(sizes) > byte_limit:
        raise InputError("JSON size exceeds configured limits; inspect input or explicitly raise --max-json-mb/--max-total-mb")
    segments, sources, paragraphs = [], [], []
    trimmed = dropped = actual_bytes = 0
    previous_start = -1.0
    for chunk_index, (path, offset, duration, audio_path) in enumerate(planned):
        # A bounded read also handles a source file growing after the size check.
        with path.open("rb") as handle:
            raw = handle.read(file_limit + 1)
        actual_bytes += len(raw)
        if len(raw) > file_limit or actual_bytes > byte_limit:
            raise InputError("JSON grew past configured input limits: {}".format(path))
        data = json.loads(raw, parse_constant=reject_constant, parse_float=finite_float)
        if not isinstance(data, dict) or not isinstance(data.get("segments"), list):
            raise InputError("{} requires an object with a segments list".format(path))
        language = data.get("language")
        if language is not None and not isinstance(language, str):
            raise InputError("{} language must be a string or null".format(path))
        if not isinstance(data.get("text", ""), str):
            raise InputError("{} text must be a string".format(path))
        if not data["segments"] and data.get("text", "").strip():
            raise InputError("{} has text but no timestamped segments".format(path))
        sources.append({"json": str(path), "audio": str(audio_path) if audio_path else None,
                        "offset": offset, "duration": duration, "language": language})
        chunk_text = []
        for local_index, source in enumerate(data["segments"]):
            context = "{} segment {}".format(path.name, local_index)
            if not isinstance(source, dict) or not isinstance(source.get("text"), str):
                raise InputError("{} needs string text".format(context))
            start = number(source.get("start"), context + " start")
            end = number(source.get("end"), context + " end")
            if end < start:
                raise InputError("{} ends before it starts".format(context))
            clipped_start = max(0.0, start)
            clipped_end = min(end, duration) if duration is not None else end
            if clipped_end <= clipped_start:
                dropped += 1
                continue
            trimmed += int(start != clipped_start or end != clipped_end)
            global_start = round(offset + clipped_start, 3)
            global_end = round(offset + clipped_end, 3)
            if global_end <= global_start:
                dropped += 1
                continue
            if global_start < previous_start:
                raise InputError("{} starts before the preceding segment".format(context))
            previous_start = global_start
            segment = dict(source)
            segment.update(id=len(segments), start=global_start, end=global_end, source_chunk=chunk_index)
            if "words" in source:
                if not isinstance(source["words"], list):
                    raise InputError("{} words must be a list".format(context))
                words = []
                for word in source["words"]:
                    if not isinstance(word, dict) or not isinstance(word.get("word"), str):
                        raise InputError("{} contains an invalid word".format(context))
                    ws = number(word.get("start"), context + " word start")
                    we = number(word.get("end"), context + " word end")
                    if we < ws:
                        raise InputError("{} word ends before it starts".format(context))
                    ws, we = max(clipped_start, ws), min(clipped_end, we)
                    if we > ws:
                        adjusted = dict(word)
                        adjusted.update(start=round(offset + ws, 3), end=round(offset + we, 3))
                        if adjusted["end"] > adjusted["start"]:
                            words.append(adjusted)
                segment["words"] = words
            segments.append(segment)
            if source["text"].strip():
                chunk_text.append(source["text"].strip())
        if chunk_text:
            paragraphs.append(" ".join(chunk_text))
        if chunk_index == 0 or (chunk_index + 1) % 100 == 0 or chunk_index + 1 == len(planned):
            print("Validated {}/{} inputs, {} segments".format(chunk_index + 1, len(planned), len(segments)), file=sys.stderr, flush=True)
    languages = sorted({source["language"] for source in sources if source["language"]})
    merged = {"text": "\n\n".join(paragraphs), "segments": segments,
              "language": languages[0] if len(languages) == 1 else None,
              "languages": languages, "model": args.model, "task": args.task,
              "output_language": "en" if args.task == "translate" else (languages[0] if len(languages) == 1 else None),
              "source_chunks": sources}
    return merged, {"input_bytes": actual_bytes, "trimmed_segments": trimmed, "dropped_segments": dropped}


def cue_text(text):
    return " ".join(text.strip().splitlines()).replace("-->", "->")


def write_artifact(handle, kind, merged, name, summary):
    segments = merged["segments"]
    if kind in ("json", "run"):
        json.dump(merged if kind == "json" else summary, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    elif kind == "txt":
        handle.write(merged["text"] + "\n")
    elif kind == "md":
        handle.write("# Transcript: {}\n\nModel: {} | Task: {} | Source languages: {}\n\n".format(
            name, merged["model"], merged["task"], ", ".join(merged["languages"]) or "unknown"))
        for segment in segments:
            handle.write("[{}] {}\n".format(timestamp(segment["start"]), cue_text(segment["text"])))
    elif kind in ("srt", "vtt"):
        if kind == "vtt":
            handle.write("WEBVTT\n\n")
        for index, segment in enumerate(segments, 1):
            if kind == "srt":
                handle.write(str(index) + "\n")
            handle.write("{} --> {}\n{}\n\n".format(
                timestamp(segment["start"], kind == "srt"), timestamp(segment["end"], kind == "srt"), cue_text(segment["text"])))
    elif kind == "tsv":
        handle.write("start\tend\ttext\n")
        for segment in segments:
            handle.write("{}\t{}\t{}\n".format(round(segment["start"] * 1000), round(segment["end"] * 1000),
                                                cue_text(segment["text"]).replace("\t", " ")))


def outputs(args, name):
    root = args.output_dir.resolve()
    stem = name + (".merged" if args.input_dir else "")
    paths = {kind: root / (stem + "." + kind) for kind in ("txt", "json", "srt", "vtt", "tsv")}
    paths.update(md=root / (name + ".timestamped.md"), run=root / (name + ".run.json"))
    return paths


def write_outputs(paths, merged, name, summary, overwrite):
    staged = []
    try:
        for kind, path in paths.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                             prefix=".whisper-", suffix=".tmp", delete=False) as handle:
                staged.append((Path(handle.name), path))
                write_artifact(handle, kind, merged, name, summary)
        for temporary, final in staged:
            if overwrite:
                os.replace(temporary, final)
            else:
                # Atomic no-clobber publication on the same filesystem, including races.
                os.link(temporary, final)
                temporary.unlink()
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input-json", type=Path, help="One ordinary Whisper JSON")
    group.add_argument("--input-dir", type=Path, help="Directory of part_NNN.json results")
    parser.add_argument("--audio-dir", type=Path, help="Required for chunks: directory of matching part_NNN.wav files")
    parser.add_argument("--duration", type=positive_number, help="Optional single-file duration in seconds for end trimming")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--name", help="Output stem (dots preserved); defaults to JSON stem or transcript")
    parser.add_argument("--model", required=True, help="Actual model used; Whisper JSON does not record it")
    parser.add_argument("--task", choices=("transcribe", "translate"), default="transcribe")
    parser.add_argument("--dry-run", action="store_true", help="Validate all inputs and report planned outputs without writing")
    parser.add_argument("--overwrite", action="store_true", help="Explicitly permit replacing existing final artifacts")
    parser.add_argument("--max-chunks", type=positive_integer, default=10000)
    parser.add_argument("--max-json-mb", type=positive_number, default=16, help="Per-file byte limit in MiB (default 16)")
    parser.add_argument("--max-total-mb", type=positive_number, default=64, help="Total JSON byte limit in MiB (default 64)")
    args = parser.parse_args(argv)
    if args.input_dir and (not args.audio_dir or args.duration is not None):
        parser.error("--input-dir requires --audio-dir and does not accept --duration")
    if args.input_json and args.audio_dir:
        parser.error("--audio-dir is only valid with --input-dir")
    name = args.name if args.name is not None else (args.input_json.stem if args.input_json else "transcript")
    if not name or name in (".", "..") or any(c in name for c in "/\\") or any(ord(c) < 32 for c in name):
        parser.error("--name must be a nonempty filename stem without separators or control characters")
    started = time.monotonic()
    try:
        planned = inputs(args)
        paths = outputs(args, name)
        input_paths = {path for path, _, _, _ in planned}
        input_paths.update(audio for _, _, _, audio in planned if audio)
        for path in paths.values():
            if path.resolve() in input_paths:
                raise InputError("Output would replace a source file: {}".format(path))
            if path.is_dir():
                raise InputError("Output path is a directory: {}".format(path))
            if (path.exists() or path.is_symlink()) and not args.overwrite:
                raise InputError("Output exists (use another name or --overwrite): {}".format(path))
        merged, stats = load_results(planned, args)
        total_duration = planned[-1][1] + planned[-1][2] if planned[-1][2] is not None else None
        summary = dict(stats, model=args.model, task=args.task, languages=merged["languages"],
                       input_count=len(planned), segment_count=len(merged["segments"]),
                       total_duration=total_duration, final_timestamp=max((s["end"] for s in merged["segments"]), default=None),
                       dry_run=args.dry_run, outputs={kind: str(path) for kind, path in paths.items()},
                       sources=merged["source_chunks"], validation_seconds=round(time.monotonic() - started, 3))
        if not args.dry_run:
            write_outputs(paths, merged, name, summary, args.overwrite)
        summary["elapsed_seconds"] = round(time.monotonic() - started, 3)
        print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (InputError, OSError, ValueError, OverflowError, RecursionError) as exc:
        print("Merge failed: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
