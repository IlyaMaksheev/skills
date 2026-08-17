---
name: script-performance-refinement
description: Refine newly created long-running scripts with bounded profiling and resource checks before full-scale execution. Use (load) after script logic has already been implemented, when script may process large data, grids, multiprocessing, parquet, or long research workloads.
---

# Script Performance Refinement

## When to use

Use only after script/code logic exists.
Use before full-scale run if script may take long time, use large data, spawn workers, or write large outputs.

## Required loop

1. Verify code correctness first.
2. Run bounded representative dry run.
3. Capture profile, phase timings, logs, and resource usage.
4. Inspect bottlenecks and system behavior.
5. Rewrite script logic only where evidence points.
6. Re-run same bounded check.
7. Repeat until no sane measured refinement remains.

## Dry run requirements

- Must finish quickly, not hours.
- Use real data slice when possible.
- Else use representative synthetic/possible input.
- Must exercise same code paths as full run.
- Persist command, logs, config, and profile artifacts under `tmp/`.

## Measurements

Use cProfile for Python hot paths and OS-level observation for worker, CPU, RAM, and disk behavior.

Capture:

- wall time and rows/events/jobs per second;
- cProfile or equivalent hot-path profile;
- phase timing breakdown;
- worker count vs active CPU use;
- RSS / memory trend / peak;
- disk output size and projected full-run size;
- progress logging quality.

## Investigation rules

- Do not optimize guesses.
- Normalize by unit of work.
- Check resource limits before scaling.
- If workers idle, investigate sharding/scheduling.
- If memory/disk projection is unsafe, change design before full run.
- Preserve semantics with small deterministic checks.

## Stop criteria

Stop when:

- bounded run is acceptable;
- major bottlenecks are understood or fixed;
- resource usage projects safely;
- progress logs are useful;
- further changes would be speculative or high-risk.

## Finish

Record final evidence and changed files.
Commit when requested or project workflow requires it.
