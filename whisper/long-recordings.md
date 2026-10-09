# Long recordings, recovery, and merge

Read before a long run, for resume, or after an execution failure. Whisper already processes audio in internal windows; external chunking is mainly for bounded retries and progress, not a guarantee of lower model VRAM. Independent chunks lose cross-boundary context and may split words.

## Plan and extract

For a long recording (roughly 30 minutes or more), prefer the existing ten-minute chunk workflow unless the user requests a single pass. Estimate disk: mono 16 kHz signed 16-bit PCM uses about 115 MB/hour; keeping both full WAV and copied chunks roughly doubles that. Model weights and transcript artifacts are additional. Run one GPU transcription at a time.

Use a unique work directory. With INPUT and WORK resolved:
```bash
mkdir -p "$WORK/audio" "$WORK/chunks" "$WORK/results" "$WORK/logs"
ffmpeg -nostdin -n -i "$INPUT" -vn -ac 1 -ar 16000 -c:a pcm_s16le \
  "$WORK/audio/source.wav"
ffmpeg -nostdin -n -i "$WORK/audio/source.wav" -f segment \
  -segment_time 600 -c copy "$WORK/chunks/part_%03d.wav"
```
Continue only after each command succeeds. This retains the existing ffmpeg default stream behavior. Keep chunks non-overlapping. Changed chunk sizes are fine: the merger reads each WAV's actual duration and computes cumulative offsets, including the final short chunk.

Before inference, save a small run record in WORK: resolved source identity (path, size, modification time, duration), model, task, source-language setting, device, chunking options, runtime version, and complete expected chunk list. A completed run is not inferred merely from a filename.

## Transcribe sequentially and resume

For each numerically ordered WAV:
- Print its index/count and elapsed time.
- Invoke the same runner/options as the main workflow, with output in WORK/results.
- Save stdout/stderr in its own WORK/logs file and inspect the exit status.
- After success, confirm parseable JSON and the requested txt/srt/vtt/tsv artifacts, then record completion in the run record.
- Stop on failure; report the failed chunk and preserve completed artifacts. Avoid unattended infinite retries.

On resume, reuse chunks only after matching the source identity and settings. Skip only explicitly completed, validated chunks. A JSON file alone is not a completion marker. Changing model, task, source-language setting, source audio, or chunk boundaries requires a separate compatible run; do not silently combine unlike results.

Process one chunk at a time rather than launching parallel GPU workers. A CLI call per chunk reloads the model, trading speed for simple failure isolation. Keep per-chunk logs rather than sending unbounded output into agent context.

## Recovery

Check the actual error. For CUDA memory pressure, inspect current free memory and suggest closing GPU-heavy applications; chunking does not make model weights smaller. Retry the failed chunk once after an agreed remediation. Offer:
- the same model on CPU with `--device cpu --fp16 False` (potentially much slower), or
- a smaller task-compatible model after approval, restarting in a separate run to keep model metadata consistent.

Changing only device can resume the same model/task run; record the per-chunk device change. Dependency/tool failures need environment repair, not arbitrary retries.

## Merge and verify

When every expected chunk is complete:
```bash
"${PYTHON[@]}" "$SKILL_DIR/merge_chunks.py" \
  --input-dir "$WORK/results" --audio-dir "$WORK/chunks" \
  --output-dir "$OUTPUT" --name "$NAME" --model "$MODEL" --task "$TASK" \
  --dry-run
# If validation succeeds, repeat without --dry-run.
```

For a single Whisper JSON, use `--input-json` instead of the two directory options. Supply `--duration` from ffprobe when known to trim decoding beyond the recording end.

The helper:
- requires contiguous, zero-based part indices and exactly one JSON per expected WAV;
- validates JSON schema, finite timestamps, and configured input-size limits before writing;
- derives chunk offsets from actual WAV duration, trimming padded segments and adjusting optional word timestamps;
- writes consistent text, JSON, timestamped Markdown, SRT, VTT, TSV, and a JSON run summary;
- refuses existing output names unless `--overwrite` is explicit; stages writes before replacing final files.

Final stems retain embedded dots. Chunk outputs use `.merged.*`, single-file outputs use their ordinary extensions, and Markdown uses `.timestamped.md`. Read `--help` for exact names and resource-limit options.

The merged JSON records the actual model/task, per-input source language, and source paths. Mixed detected languages remain a list rather than being mislabeled English. Decoding metadata such as seek/token positions remains local to its source chunk; segment and word start/end timestamps are global.

Inspect the run summary, final timestamp range, and transcript around chunk boundaries. Complete files do not prove accurate speech recognition. Keep work/logs for recovery until the user elects to remove them, and identify temporary outputs as disposable.
