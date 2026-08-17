# Web research

# Search and source selection

Start with narrow discovery queries and follow relevant results to primary or authoritative sources. Prefer current official documentation, specifications, original publications, and direct project sources over unsourced summaries.

Use the configured search/fetch guidance and tools from higher-priority instructions. Do not duplicate large fetched pages in context. Extract only the evidence needed for the expected result, keeping source URLs, titles, dates, and important limitations.

Broaden queries only when initial results are insufficient or contradictory. Distinguish sourced facts from inference. For time-sensitive claims, record the source date and verify that it is current enough for the task.

# Authority

Research does not grant project mutation authority. A utility worker returns findings and may write only approved temporary/research artifacts. An implementation worker may use findings in its authorized implementation scope.

If research reveals a need for substantial codebase mapping, load `repository-recon.md`. If it becomes long-running or resource-intensive, load the corresponding files dynamically.

# Report contribution

Append only when web findings are part of the expected result:

```text
Research:
- <concise finding>

Sources:
- <title or authority>: <URL>

Gaps:
- <only unresolved or weakly supported points>
```

Omit `Gaps` when there are none. Do not paste full source content.
