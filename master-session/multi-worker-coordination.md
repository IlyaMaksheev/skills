# Multi-worker coordination

# Partitioning

Split work into bounded, independently verifiable deliverables. Maintain **write isolation** with clear ownership and non-overlapping write scopes where practical; prefer vertical tasks over layers that all modify the same files. Give every Git-lifecycle implementation worker its own worktree, and reserve the canonical target worktree for the brief serialized integration step.

Identify dependencies before spawning:

- spawn independent or currently unblocked work;
- assign each investigation once unless independent corroboration is part of the expected result;
- give concurrently mutable shared state a single writer;
- serialize resource-heavy jobs unless the parent explicitly approves parallel resource use.

Each child prompt must use the sparse prompt contract in `SKILL.md`. Give every child a unique name and exact expected result.

# Supervision

Use authored terminal child reports as the completion signal. After dispatch, wait without elapsed-time or silence-driven pings; act only on a child report, actionable runtime event, or human request. Track only compact orchestration state: assigned, blocked, done, or failed.

Maintain the delegation boundary from `SKILL.md`: workers retain execution ownership, including their checks and any explicitly authorized Git integration and cleanup. If one worker's result changes another worker's assumptions, send the smallest necessary correction to the affected worker.

Load `worker-blockers.md` only when a reported blocker needs intervention. Load `task-bank-orchestration.md` only when its bank workflow was explicitly activated.

# Completion

Coordination is complete when every dispatched child is terminal, dependency-relevant results have reached affected children, and every unresolved blocker is represented in the immediate-parent report. Aggregate outcomes without reproducing child context; include relevant results and requested artifacts.
