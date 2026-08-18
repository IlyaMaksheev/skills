# Resource-intensive orchestration

# Before spawning

Define useful bounds in the child prompt when known:

- input scope or sample limits;
- CPU/process limit;
- memory or disk constraints;
- expected artifacts and log location;
- timeout or stopping condition;
- whether parallel heavy jobs are allowed.

Run one resource-heavy job at a time unless the parent explicitly approves parallel resource use. Keep implementation and monitoring behind the delegation boundary with the responsible worker.

Ask the responsible worker to load its `resource-intensive-work.md` module. When the task matches their descriptions, direct it to use `script-performance-design` before implementation and `script-performance-refinement` after implementation and before full-scale execution.

If the workload is also long-running, the worker decides whether to load long-job guidance and isolate execution in a utility child.

# Dispatch criterion

Before dispatch, produce one of three outcomes: applicable resource bounds with a stopping condition, a bounded feasibility run, or a hard blocker explaining why safe bounds cannot yet be established.
