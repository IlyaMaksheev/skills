# Multi-worker coordination

## Partitioning

Split into bounded, independently deliverable assignments with one owner per mutable scope; prefer vertical tasks with non-overlapping writes. Parallel Git delivery needs distinct branches and isolated worktrees, created by parent or worker, with serialized target updates. Unrelated target-worktree changes are protected state, not a dispatch blocker; `../receiving-work/git-lifecycle.md` owns integration safety.

If assignments explicitly share a working directory, partition edits and serialize index mutation and commits. Disjoint files alone do not isolate a shared Git index. Pass these constraints in the briefs rather than relying on workers to discover each other.

Identify dependencies before dispatch:

- assign independent or currently unblocked work;
- assign each investigation once unless independent corroboration is explicitly requested;
- serialize shared-state updates and resource-heavy work unless authorized safe concurrency is established;
- preserve useful local work when available, without requiring parallelism for context-isolating delegation.

Use `briefing-and-dispatch.md` for every assignment. Keep names, scopes, and expected results distinct. A child coordinating descendants remains responsible for its own bounded result, not unrelated sibling work.

## Supervision

Follow `supervision.md` for report handling, waiting, reuse, and assumption updates; keep compact assignment/dependency state. Read `worker-blockers.md` for hard blockers. For requested graph-backed scheduling with an explicitly supplied bank or one selected through `../receiving-work/workspace-artifacts.md`, read `task-bank-orchestration.md`.

## Completion

Coordination is complete when every required child assignment is terminal, dependency-relevant results have reached affected workers, and unresolved outcomes are accounted for in your own result. Aggregate useful conclusions without reproducing child contexts.
