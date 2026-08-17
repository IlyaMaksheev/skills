# Resource-intensive work

# Bound before scale

Assess and state the applicable bounds:

- input size and selection;
- expected algorithmic or grid size;
- process/thread count;
- memory and temporary-disk needs;
- output/log growth;
- runtime estimate or stopping condition;
- shared-resource and duplicate-run risks.

Run a bounded feasibility or representative sample before full-scale execution when practical. Do not launch an unbounded grid, full data scan, or high-concurrency workload merely because the code permits it.

When the task matches their descriptions:

- load `script-performance-design` before implementing the heavy script/workflow;
- load `script-performance-refinement` after implementation and before full-scale execution.

Those specialized skills provide detailed design and refinement guidance; do not duplicate them here.

# Composition

Load `long-running-jobs.md` separately when execution needs background launch or monitoring. An implementation worker may load `utility-delegation.md` when execution/monitoring should be isolated.

Permit only one resource-heavy utility job at a time unless the immediate-parent prompt explicitly approves parallel resource use. If safe bounds cannot be established, report a blocker rather than consuming uncontrolled resources.

# Report contribution

When relevant, append:

```text
Resources:
- Bounds: <input/process/memory/runtime limits actually used>
- Feasibility: <concise result>
```

Report only measured or intentionally enforced bounds; distinguish estimates from observations.
