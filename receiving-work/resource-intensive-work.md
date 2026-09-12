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

Use the loaded performance skills for detailed design and refinement; this module owns bounds, feasibility, and worker-level resource composition.

# Concurrency

Permit only one resource-heavy job across your local and delegated assignment at a time unless the controlling instruction explicitly approves parallel resource use. Pass this restriction and any shared budget to children; nesting does not multiply the allowed budget. If safe bounds cannot be established, report a blocker rather than consuming uncontrolled resources.

# Report contribution

When relevant, append:

```text
Resources:
- Bounds: <input/process/memory/runtime limits actually used>
- Feasibility: <concise result>
```

Report only measured or intentionally enforced bounds; distinguish estimates from observations.
