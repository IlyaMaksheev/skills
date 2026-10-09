# Whisper model selection

Read before execution. The default is `large-v3`; an explicit `--model` takes precedence. The table guides alternatives, not automatic downgrades. If the requested/default model is impractical, explain why and agree on an alternative.

## Trade-offs

Approximate upstream memory guidance is for GPU VRAM, not guaranteed peak use or CPU RAM. Desktop activity, precision, torch build, and decoding options affect headroom. Relative speed depends strongly on hardware; benchmark a short representative sample when uncertain.

| Model family | Approx. VRAM | Practical use |
|---|---:|---|
| `tiny`, `tiny.en` | ~1 GB | Very fast rough drafts, quick audio checks; lowest accuracy |
| `base`, `base.en` | ~1 GB | Lightweight drafts on constrained hardware |
| `small`, `small.en` | ~2 GB | Better balance for clear speech and limited resources |
| `medium`, `medium.en` | ~5 GB | Stronger accuracy, slower; useful middle ground |
| `large-v1`, `large-v2`, `large-v3` | ~10 GB | Quality-first multilingual work; costly on CPU or tight GPUs |
| `turbo` (optimized large-v3) | ~6 GB | Fast, strong transcription; not suitable for translation |

These are tendencies, not a universal accuracy ordering. Noise, accents, jargon, and overlapping speech can defeat any model. For CPU-only work, smaller models can be much more practical than large-v3. A nominal 12 GB GPU can still run out of memory while desktop applications are using it.

`.en` variants are English-only; select them only for known English transcription. Multilingual variants support Whisper's supported languages with uneven accuracy. For the installed runtime's exact names, inspect `whisper --help`; `large` and turbo aliases may vary by release. Existing cached weights can avoid a download but do not override an explicitly selected model.

## Source language and task

- **Transcription:** output remains in the spoken language. Omit `--language` for detection, or pass the source language supplied by the user.
- **Translation:** `--task translate` translates supported speech into **English only**. Use a multilingual model, such as medium or large-v3.
- **Invalid combination:** turbo and English-only models are not appropriate for translation. Explain the conflict and agree on a multilingual alternative before running.
- **Mixed-language input:** detection usually relies on the opening audio; a misleading opening or forced source language can distort later passages. Chunk-level detection can also differ between chunks. Investigate only when results or the request warrant it.

`--language ru` means Russian source speech, not Russian translated output. Non-English translation destinations are outside this skill.

## Choosing an alternative

Offer tiny/base for preview speed, small for constrained machines, medium for a quality/resource compromise, or turbo for fast transcription with enough GPU headroom. Reserve large-v3's default for a feasible quality-first run. For important results, compare a representative short segment against the audio rather than treating a model-size label as proof of accuracy.

Whisper does not assign speaker identities. Names, numbers, abbreviations, silence hallucinations, and technical vocabulary require human verification; subtitles and timestamped Markdown help locate questionable passages.
