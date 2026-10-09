#!/usr/bin/env python3
"""Inspect the selected interpreter without installing packages or loading models."""

import argparse
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time


def package_version(name):
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def inspect_runtime(model_cache=None, skip_imports=False):
    started = time.monotonic()
    tools = {name: shutil.which(name) for name in ("uv", "ffmpeg", "ffprobe", "whisper", "nvidia-smi")}
    report = {
        "python": {"executable": sys.executable, "version": sys.version.split()[0],
                   "prefix": sys.prefix, "base_prefix": sys.base_prefix},
        "cwd": str(Path.cwd()),
        "virtual_env": os.environ.get("VIRTUAL_ENV"),
        "tools": tools,
        "packages": {"openai-whisper": package_version("openai-whisper"), "torch": package_version("torch")},
        "whisper_importable": None,
        "torch": {"importable": None, "cuda_available": False, "mps_available": False},
        "errors": [],
    }
    if not skip_imports:
        if report["packages"]["openai-whisper"]:
            try:
                whisper = importlib.import_module("whisper")
                report["whisper_importable"] = callable(getattr(whisper, "load_model", None))
                report["whisper_module"] = getattr(whisper, "__file__", None)
            except Exception as exc:
                report["whisper_importable"] = False
                report["errors"].append("Whisper import: {}: {}".format(type(exc).__name__, exc))
        else:
            report["whisper_importable"] = False
        if report["packages"]["torch"]:
            try:
                torch = importlib.import_module("torch")
                report["torch"].update(importable=True, version=torch.__version__,
                                       cuda_build=torch.version.cuda,
                                       cuda_available=torch.cuda.is_available())
                mps = getattr(torch.backends, "mps", None)
                report["torch"]["mps_available"] = bool(mps and mps.is_available())
                if report["torch"]["cuda_available"]:
                    props = torch.cuda.get_device_properties(0)
                    report["torch"].update(cuda_device=props.name, cuda_total_bytes=props.total_memory)
            except Exception as exc:
                report["torch"]["importable"] = False
                report["errors"].append("Torch inspection: {}: {}".format(type(exc).__name__, exc))
        else:
            report["torch"]["importable"] = False
    if tools["nvidia-smi"]:
        try:
            result = subprocess.run(
                [tools["nvidia-smi"], "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=5, check=True,
            )
            report["nvidia_memory_csv"] = result.stdout.strip()[:4096]
        except (OSError, subprocess.SubprocessError) as exc:
            report["errors"].append("nvidia-smi: {}".format(exc))
    cache = Path(model_cache) if model_cache else Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "whisper"
    report["model_cache"] = str(cache.expanduser().resolve())
    report["cached_model_candidates"] = []
    try:
        if cache.expanduser().is_dir():
            # The model family is small; cap listing for unexpectedly crowded directories.
            for index, path in enumerate(cache.expanduser().glob("*.pt")):
                if index >= 100:
                    report["errors"].append("Model cache listing truncated at 100 candidates")
                    break
                if path.is_file():
                    report["cached_model_candidates"].append({"name": path.name, "bytes": path.stat().st_size})
    except OSError as exc:
        report["errors"].append("Model cache: {}".format(exc))
    report["ready"] = bool(report["whisper_importable"] and report["torch"]["importable"] and tools["ffmpeg"] and tools["ffprobe"])
    report["elapsed_seconds"] = round(time.monotonic() - started, 3)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-cache", help="Inspect this cache instead of the default Whisper cache")
    parser.add_argument("--skip-imports", action="store_true", help="Fast package/tool inspection only; cannot establish readiness")
    parser.add_argument("--require-whisper", action="store_true", help="Exit 2 unless Whisper, torch, ffmpeg and ffprobe are usable")
    args = parser.parse_args()
    if args.skip_imports and args.require_whisper:
        parser.error("--skip-imports cannot establish --require-whisper readiness")
    report = inspect_runtime(args.model_cache, args.skip_imports)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if args.require_whisper and not report["ready"] else 0


if __name__ == "__main__":
    sys.exit(main())
