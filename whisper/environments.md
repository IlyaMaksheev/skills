# Runtime reuse and installation

Read before selecting or changing a Python environment. uv is a machine-level tool; a directory may contain a uv-managed project. Its presence alone is not a reason to initialize a project.

## Discovery: inspect, then reuse

Use bounded local discovery, not a home-directory scan. Check the active virtual environment, the invocation directory's `.venv`, its containing project/workspace, and Python/Whisper on PATH. Also reuse a known compatible environment supplied by the user. Resolve interpreter paths before changing directories.

Run the bundled inspector with each plausible interpreter:

```bash
"$PYTHON_PATH" "$SKILL_DIR/inspect_runtime.py"
```

It emits JSON without installing packages or loading a speech model. Inspect `openai-whisper` distribution/module availability, torch/device support, tool paths, and cached-model candidates. A package merely named `whisper` is not sufficient. Use `--require-whisper` to demand an importable runtime and ffmpeg/ffprobe. Read `--help` for optional cache/inspection flags.

Prefer a working invocation-project environment, then an active or known existing environment, then a working PATH environment. Reuse its actual interpreter; avoid accidentally running another project's `uv run`.

For an existing venv:
```bash
PYTHON=("/absolute/path/to/.venv/bin/python")
WHISPER=("/absolute/path/to/.venv/bin/whisper")
```
Verify both come from the same environment. An absolute interpreter and launcher work without activation. For an installed uv project, `uv run --project "$PROJECT" --no-sync python …` / `whisper …` are alternatives; inspection should not trigger a dependency sync.

## Compatible existing uv project: add if necessary

If no reusable runtime has Whisper, but the invocation directory belongs to a compatible uv project, adding `openai-whisper` is authorized by this skill invocation. Inspect `pyproject.toml`, `uv.lock`, Python constraints, workspace ownership, and existing dependency changes first.

```bash
uv add --project "$PROJECT" openai-whisper
```

Then rerun the inspector and `whisper --help` in that environment. uv add resolves and syncs; a separate uv sync is normally unnecessary. Report changed dependency files. If resolution fails or requires unrelated dependency upgrades, a Python-version change, or new CUDA packaging policy, stop and propose isolation rather than force changes. Never reinitialize an existing project.

## No suitable environment: propose, then wait

Offer the smallest appropriate choice; install only after the user selects it:

1. **Dedicated uv project**, useful for repeated transcription:
   ```bash
   uv init --bare --python 3.11 --name whisper-runtime "$RUNTIME_DIR"
   uv add --project "$RUNTIME_DIR" openai-whisper
   ```
   Choose a new, user-approved directory, not the media folder or skill directory by default.
2. **Isolated uv-managed run**, no project files changed:
   ```bash
   PYTHON=(uv run --no-project --isolated --python 3.11 --with openai-whisper python)
   WHISPER=(uv run --no-project --isolated --python 3.11 --with openai-whisper whisper)
   ```
   uv may download Python and dependencies into its managed cache. Use matching requirements/options for inspection and transcription.
3. **Dedicated Python venv**, if uv is unavailable:
   ```bash
   python3 -m venv "$RUNTIME_DIR"
   "$RUNTIME_DIR/bin/python" -m pip install openai-whisper
   ```
   Use a supported available Python, inspecting compatibility first. Install into the selected venv, not system Python.

If a compatible active non-uv venv lacks Whisper, propose installing there or isolation; choose neither silently. Do not install uv, OS packages, GPU drivers, or a different PyTorch build without approval. A missing ffmpeg/ffprobe is a blocker even when Python packages are present.

## GPU, cache, and failures

The inspector reports torch CUDA/MPS availability and bounded NVIDIA memory information when possible. Prefer CUDA when available. Select CPU if CUDA is unavailable; use MPS only when explicitly selected and tested with this runtime. On CPU use `--fp16 False`. GPU failures and CPU retries are covered in [long-recordings.md](long-recordings.md).

Model weights normally live in `${XDG_CACHE_HOME:-$HOME/.cache}/whisper`, independently of transcript output. Cached filenames are candidates, not proof that downloads are complete; Whisper validates weights. Check disk and download cost before a first use. Temporary transcript output does not imply temporary environment/model storage.

Use the helper scripts with any Python 3.9+ interpreter; they require only the standard library. Whisper itself has additional package/Python compatibility requirements determined by the selected release.
