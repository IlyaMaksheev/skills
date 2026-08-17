# Multi-worker coordination

# Partitioning

Split work into bounded deliverables with clear ownership and non-overlapping write scopes where practical. Prefer vertical, independently verifiable tasks over layers that all modify the same files.

Identify dependencies before spawning:

- spawn independent or currently unblocked work;
- do not duplicate the same investigation in multiple sessions without a reason;
- do not ask multiple workers to mutate the same shared state concurrently;
- keep resource-heavy jobs serialized unless the parent explicitly approves parallel resource use.

Each child prompt must use the sparse prompt contract in `SKILL.md`. Give every child a unique name and exact expected result.

# Supervision

Use terminal child reports rather than routine polling or progress messages. Track only compact orchestration state: assigned, blocked, done, or failed.

Workers retain execution ownership, including their checks and any explicitly authorized Git integration and cleanup. If one worker's result changes another worker's assumptions, send the smallest necessary correction to the affected worker.

Load `worker-blockers.md` only when a reported blocker needs intervention. Load `task-bank-orchestration.md` or legacy `issue-bank-orchestration.md` only when its corresponding bank workflow was explicitly activated.

# Completion

Aggregate child outcomes without reproducing their full context. Report relevant results, unresolved blockers, and requested artifacts to the immediate parent.
