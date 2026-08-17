# Resource-intensive orchestration

# Before spawning

Define useful bounds in the child prompt when known:

- input scope or sample limits;
- CPU/process limit;
- memory or disk constraints;
- expected artifacts and log location;
- timeout or stopping condition;
- whether parallel heavy jobs are allowed.

Prefer one resource-heavy job at a time unless the parent explicitly approves parallel resource use. Do not spend master context implementing or monitoring the workload directly.

Ask the responsible worker to load its `resource-intensive-work.md` module. When the task matches their descriptions, direct it to use `script-performance-design` before implementation and `script-performance-refinement` after implementation and before full-scale execution.

If the workload is also long-running, the worker decides whether to load long-job guidance and isolate execution in a utility child.

# Blockers

If safe resource bounds cannot be established, obtain a smaller feasibility run or report a hard blocker rather than launching an unbounded workload.
