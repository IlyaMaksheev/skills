# Briefing and dispatch

## Worker selection

Choose reuse or a fresh session before assigning follow-up work, including review corrections and blocker resolution.

Reuse a reachable worker for small, bounded corrections, clarification, or omissions when the fix direction is clear and the worker has sufficient context headroom.

Spawn a fresh worker for substantial corrections, renewed investigation, revisions that reconsider implementation assumptions, or follow-up work that would substantially burden the original worker's remaining context. The correction may remain within the original task; related scope alone does not justify reuse.

Assess the reasoning and implementation required, not just the number of findings or changed files. Use available reports and known context state; a numeric context threshold is not required.

Assess availability from known worker identity and authored reports. A completed assignment does not make the worker unavailable. Missing availability information calls for discovery, not polling an active reporting worker.

Independent work, materially different scope, unavailable prior workers, and explicitly requested independent assessment also warrant a fresh session.

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

Keep the assignment readable and bounded: objective, expected result, permissions, relevant inputs, and requested reporting checkpoints. Inline decisions and constraints needed before execution. Reference detailed policy and historical evidence by exact path; identify which material is authoritative. Include useful findings, ruled-out approaches, and unresolved questions only when they affect this assignment. Investigations need a bounded question, not a speculative search sequence or whole workspace.

For read-only work, explicitly prohibit project, dependency, Git, task-state, and environment mutation. Allow temporary writes only when needed and permitted: supply an approved path, such as `/tmp/pi-workers/<session-name>/`, and require `../receiving-work/temporary-artifacts.md` (resolve the path before prompting). Otherwise omit the allowance.

For code changes, specify allowed files/modules and checks. Editing permission does not authorize commits, integration, dependency installation, or task-state updates.

Include optional fields only when they carry active instructions or authorization:

- `Input files`, useful context, output limits, resource bounds, approved artifact paths;
- explicit commit permission and destination branch for scoped commits in the supplied worktree; unrelated dirty state is allowed under `../receiving-work/git-commits.md`;
- `Git lifecycle` and `Target branch` together for isolated-worktree delivery and target integration; state whether integration is required for completion;
- `Agent-docs lifecycle` with those Git fields for delivery into a mixed feature branch, following `agent-docs-lifecycle`;
- `Task bank` and `Task artifact` for selected task context, with explicit permission for any task-state mutation;
- `Parent name` or stable identity when harness routing is insufficient;
- `Human interaction: direct in this worker session` when human decisions or acceptance are required; include the decision to obtain and its completion criterion. Also supply `Parent reporting: automatic` and `Parent session ID` with the assigning session's stable ID, so the human can guide outcome delivery if automatic reporting is incomplete.

When the human requests intermediate updates, include `Reporting checkpoints`: the observable events the child must report, such as preparation ready or each execution attempt ending successfully or unsuccessfully. Define what counts as an attempt when multiple retry layers exist. The parent delivers requested orchestration updates. For direct HITL, the worker owns the human discussion.

The receiving skill owns validation and reporting. Do not repeat its entire instructions in each prompt.

## Follow-up contract

Send related follow-ups with `message_session` in triggering mode. Include the bounded task, expected result, and any changed constraints. State that prior restrictions remain in force when unchanged. Updated permissions must remain within your own authority. An extension must still fit the assigning session's scope.

If the worker was created under an older or different contract, explicitly bootstrap `receiving-work` and supply the full assignment contract for the new task.

## Successor handoff

When a fresh worker takes over unfinished work or substantial corrections, provide:

- the governing requirements, accepted findings, and expected corrected result;
- exact code-state anchors, including relevant revisions, worktree paths, and inherited uncommitted changes;
- attempted fixes, their observed outcomes, and unresolved questions;
- explicit permissions, restrictions, and transferred execution ownership.

Reference detailed evidence by exact path rather than copying the previous session's transcript. Distinguish authoritative requirements from the previous worker's hypotheses.

Require the successor to evaluate inherited assumptions against the governing requirements and evidence before extending the implementation.

Transfer exclusive execution ownership before the successor starts mutating shared state. Preserve inherited work and its attribution.

## Spawn defaults

Before creating a new session, read [model-routing](../model-routing/SKILL.md) for its model and thinking level; keep existing workers' configurations unchanged. Load Pi session tools before dispatch. Use:

- `mode: "fresh"`; use `fork` only when inherited history was explicitly requested;
- `reportToSelf: true` for stable immediate-parent routing;
- `autoReport: "both"` for ordinary assignments; use `autoReport: "done"` for direct-HITL workers with automatic parent reporting;
- `cwd`: the task-relevant repository, worktree, or directory;
- `sessionName`: a distinct, meaningful task name;
- non-HITL research/checking without product changes: `persistent: false`;
- state-changing execution or direct HITL: `persistent: true`;
- explicit `model` and `thinkingLevel` selected through model-routing.

The terminal-report promise makes settlement without an authored parent report observable as `report-missing`. Omitting `autoReport` defaults to readiness-only reporting and does not establish that promise. Ordinary assignments still require the child's `message_session` report.

For direct HITL, retain `reportToSelf: true` for parent identity and use automatic reporting without routine manual parent-message instructions. Automatic completion delivery is not guaranteed by the current extension; provide the stable parent session ID for human-guided delivery. Have the worker write its outcome locally under `../receiving-work/delegated-assignment.md`. Readiness for human discussion is not task completion.

These execution defaults do not define authority. Explicit user instructions override them.

Use `placement: "neovim-tab"` unless explicitly directed otherwise. If that placement reports an invalid or unreachable server, preserve every other option and fall back to `niri-ghostty`. Use the tool error directly; do not probe for another Neovim server.

For concurrent assignments, read `multi-worker-coordination.md` and give distinct write scopes. Parallel Git delivery requires `Git lifecycle` and `Target branch`, plus an assigned isolated worktree or instructions to create one. Scoped commits alone do not activate isolated delivery.

Before dispatch, read `supervision.md`. Briefly disclose substantial delegation to the human in direct mode. Dispatch is complete when the child or follow-up is accepted, its scope is recorded, and responsibility for the assigned execution has passed to that child. After spawning a direct-HITL worker, tell the user to enter its named session and provide its stable session ID.
