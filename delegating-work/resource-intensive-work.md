# Resource-intensive orchestration

# Before spawning

Define useful bounds in the child prompt when known:

- input scope or sample limits;
- CPU/process limit;
- memory or disk constraints;
- expected artifacts and log location;
- timeout or stopping condition;
- whether parallel heavy jobs are allowed.

Run one resource-heavy job across your local and delegated assignment at a time unless the controlling instruction explicitly approves parallel resource use. Pass shared budgets and concurrency restrictions down the assignment tree; nesting does not multiply resources. Keep implementation and monitoring with the responsible worker.

Ask the responsible worker to load `../receiving-work/resource-intensive-work.md` (resolve the path against this module's directory before putting it in a prompt). When the task matches their descriptions, direct it to use `script-performance-design` before implementation and `script-performance-refinement` after implementation and before full-scale execution.

If the workload is also long-running, the worker loads the receiving skill's long-job guidance. It may consider narrower delegated monitoring through `delegating-work` while retaining responsibility for the job's result.

# Dispatch criterion

Before dispatch, produce one of three outcomes: applicable resource bounds with a stopping condition, a bounded feasibility run, or a hard blocker explaining why safe bounds cannot yet be established.
