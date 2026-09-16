# Briefing and dispatch

## Reuse before spawn

Prefer a reachable existing worker for related clarification, missing deliverables, or an extension of the same investigation. Use its retained context rather than asking a new worker to rediscover it. A completed assignment does not make the session unavailable.

Use known live identity or `list_sessions` when reachability is unknown or names are ambiguous. This is a dispatch lookup, not permission to poll an active reporting worker. Spawn a new session for independent work, materially different scope, unavailable prior workers, or explicitly requested independent assessment.

## Assignment contract

Every new child prompt contains:

```text
This is a delegated assignment from your immediate parent session.
First load and follow: /skill:receiving-work

Task:
- <bounded objective>

Expected result:
- <checkable deliverable>

Permissions and constraints:
- <explicit mutation scope or read-only restriction>
- <applicable inherited restrictions>
```

Use a compact but sufficient brief. Include purpose, useful prior findings, ruled-out approaches, and unresolved questions when the child needs them for judgment. Pass selected file paths rather than entire workspaces or repeated file contents. Investigations need a bounded question, not a speculative sequence of searches. State output bounds when useful.

Read-only example:

```text
Permissions and constraints:
- Read-only investigation. Do not modify project files, dependencies,
  Git state, task state, or the environment.
- Temporary operational artifacts may be written only under
  /tmp/pi-workers/<session-name>/ and must follow temporary-artifacts.md.
```

Omit the temporary-write allowance when writes are unnecessary or forbidden. For code changes, identify allowed files or modules and the expected checks. Distinguish permission to edit from authorization to commit, integrate, install dependencies, or update task state.

Include optional fields only when they carry active instructions or authorization:

- `Input files`, useful context, output limits, resource bounds, approved artifact paths;
- explicit commit permission and destination branch for scoped commits in the supplied worktree; unrelated dirty state is allowed under `../receiving-work/git-commits.md`;
- `Git lifecycle` and `Target branch` together for isolated-worktree delivery and target integration; state whether integration is required for completion;
- `Agent-docs lifecycle` with those Git fields for delivery into a mixed feature branch, following `agent-docs-lifecycle`;
- `Task bank` and `Task artifact` for selected task context, with explicit permission for any task-state mutation;
- `Parent name` or stable identity when harness routing is insufficient.

The receiving skill owns validation and reporting. Do not repeat its entire instructions in each prompt.

## Follow-up contract

Send related follow-ups with `message_session` in triggering mode. Include the bounded task, expected result, and any changed constraints. State that prior restrictions remain in force when unchanged. Updated permissions must remain within your own authority. An extension must still fit the assigning session's scope.

If the worker was created under an older or different contract, explicitly bootstrap `receiving-work` and supply the full assignment contract for the new task.

## Spawn defaults

Before creating a new session, load and follow [model-routing](../model-routing/SKILL.md) to select its model and thinking level. That skill owns these choices for every parent model; keep existing workers' configurations unchanged. Load Pi session tools before dispatch. Use:

- `mode: "fresh"`; use `fork` only when inherited history was explicitly requested;
- `reportToSelf: true` for stable immediate-parent routing;
- `autoReport: "both"` to preserve startup notification and establish the terminal-report promise;
- `cwd`: the task-relevant repository, worktree, or directory;
- `sessionName`: a distinct, meaningful task name;
- research/checking without product changes: `persistent: false`;
- state-changing execution: `persistent: true`;
- explicit `model` and `thinkingLevel` selected through model-routing.

The terminal-report promise makes settlement without an authored parent report observable as `report-missing`. Omitting `autoReport` defaults to readiness-only reporting and does not establish that promise. It does not replace the child's required `message_session` report.

These execution defaults do not define authority. Explicit user instructions override them.

Use `placement: "neovim-tab"` unless explicitly directed otherwise. If that placement reports an invalid or unreachable server, preserve every other option and fall back to `niri-ghostty`. Use the tool error directly; do not probe for another Neovim server.

Give concurrent assignments distinct write scopes. For parallel Git-delivery assignments, authorize isolated delivery through `Git lifecycle` and `Target branch`; either assign an existing worker-specific worktree or instruct the child to create one. Use `multi-worker-coordination.md` for ownership and integration coordination. A scoped commit request alone does not activate isolated delivery.

Before dispatch, read `supervision.md`. Briefly disclose substantial delegation to the human in direct mode. Dispatch is complete when the child or follow-up is accepted, its scope is recorded, and responsibility for the assigned execution has passed to that child.
