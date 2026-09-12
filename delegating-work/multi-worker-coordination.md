# Multi-worker coordination

## Partitioning

Split work into bounded, independently deliverable assignments. Give each mutable scope a single owner. Prefer vertical tasks with non-overlapping writes; give every Git-delivery assignment its own isolated worktree and reserve the canonical target worktree for serialized integration.

Identify dependencies before dispatch:

- assign independent or currently unblocked work;
- assign each investigation once unless independent corroboration is explicitly requested;
- serialize shared-state updates and resource-heavy work unless authorized safe concurrency is established;
- preserve useful local work when available, without requiring parallelism for context-isolating delegation.

Use `briefing-and-dispatch.md` for every assignment. Keep names, scopes, and expected results distinct. A child coordinating descendants remains responsible for its own bounded result, not unrelated sibling work.

## Supervision

Follow `supervision.md` for reports, non-overlapping local work, waiting, reuse, and result handling. Keep only compact assignment and dependency state here.

When one result changes another worker's assumptions, send that worker the smallest necessary update. Load `worker-blockers.md` for hard blockers. Use `task-bank-orchestration.md` only when requested work has a relevant persisted scheduling graph.

## Completion

Coordination is complete when every required child assignment is terminal, dependency-relevant results have reached affected workers, and unresolved outcomes are accounted for in your own result. Aggregate useful conclusions without reproducing child contexts.
