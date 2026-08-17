---
name: script-performance-design
description: Design resource-aware long-running scripts before implementation, with bounded inputs, progress logs, safe parallelism, and scalable data handling. Use before creating scripts that may process large data, parquet, grids, multiprocessing, backtests, or long research workloads.
---

# Script Performance Design

## When to use

Use before writing script/code.
Use when workload may be long, large, parallel, or resource-heavy.

## Checklist discipline

Before coding, write visible checklist in session.
Do not keep checklist only in hidden reasoning.
Do not stop after showing checklist.
Execute implementation immediately after checklist.

Checklist should cover:

- input bounds and dry-run mode;
- phases and timing;
- resource model;
- parallelism design;
- progress logging;
- output size;
- correctness check;
- post-implementation refinement handoff.

## Design checklist

Define before coding:

- expected input size, groups, configs, and output size;
- bounded dry-run mode from start;
- phases: load, prep, compute, aggregate, write;
- memory and disk projection;
- parallelism boundary and worker count;
- correctness checks for small deterministic input.

## Data handling

- Do not load full big data unless proven safe.
- Prefer lazy scans, projections, filters, and chunks.
- Avoid huge joins.
- Keep data columnar where possible.
- Avoid repeated reread of just-written outputs.
- Estimate output size before full run.

## Parallelism

- Pick boundary that preserves state semantics.
- Do not shard by item count when work is skewed.
- Prefer weighted sharding or dynamic work queue.
- Estimate RAM per worker before choosing worker count.
- Watch for slowest-worker barrier.
- Log per-worker progress when run is long.

## Hot-path code shape

- Avoid object creation inside per-row/per-event loops.
- Avoid tiny DataFrame/Series creation in hot path.
- Avoid repeated collect/sort/group inside loops.
- Avoid scanning all known keys per event.
- Batch model calls when possible.
- Precompute constants and indexes.

## Logging

Logs must prove liveness without becoming huge.

Log periodically:

- phase name;
- processed rows/events/jobs;
- elapsed time;
- throughput;
- ETA if possible;
- active/finished workers;
- RSS or memory when cheap;
- output rows/size when relevant.

Flush important long-run lines.
Do not log per row/event.

## Built-in observability

Add:

- `--limit` / bounded input option;
- `--dry-run` or sample mode;
- phase timing summary;
- JSON run summary under `tmp/`;
- optional profile flag if practical.

## Handoff

After script logic is implemented, load `script-performance-refinement`.
Do not load `script-performance-refinement` before implementation.
