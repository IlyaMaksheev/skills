# Delegated assignment

## Establish the contract

Require `Task`, `Expected result`, and `Permissions and constraints`. Resolve immediate-parent routing from the harness; use explicit parent metadata when provided. Session name and parent name need not be duplicated in every prompt when the harness supplies reliable identity.

If required assignment information is missing, or the expected result exceeds the supplied authority, report `blocked` to the immediate parent before execution. Do not silently choose broader permissions. If parent identity is unavailable, ask for clarification locally rather than guessing another session.

Interpret a follow-up within the existing assignment context. Explicit task and expected-result updates define the new deliverable; unchanged restrictions continue to apply. A new tool or discovered opportunity does not grant additional authority.

Optional workflow fields authorize only their stated workflow. `Task bank` and `Task artifact` provide selected context, not implicit task-state mutation permission. `Git lifecycle` requires `Target branch`. Compose `Agent-docs lifecycle` with its specialized skill and Git fields for mixed-feature delivery.

After validation, return to `SKILL.md` and select execution modules from the actual task. Delegate only after loading `/skill:delegating-work` when its consideration triggers apply.

## Execution ownership

Own execution, required checks, authorized task-state completion, and cleanup. Do not report success with required deliverables or checks outstanding. A running job with a clear completion path is not a blocker.

Keep routine progress in this session. Communicate completion, terminal failure, or a hard blocker to the immediate parent. If descendants contribute work, integrate their results before reporting your own outcome.

## Parent reporting

Your terminal result belongs to your immediate parent. A local final response alone does not satisfy this contract.

Use sparse plaintext:

```text
Status: done | blocked | failed
Summary:
- <concise terminal outcome>
```

- `done`: the expected result and required checks are complete.
- `blocked`: external input or a decision is required, or no safe path remains.
- `failed`: in-scope recovery ended without the expected result.

Add only relevant sections from modules that produced evidence. Include requested paths, citations, or check outcomes; omit unloaded, empty, irrelevant, and placeholder sections. Acknowledge unresolved limitations rather than presenting them as completed work.

Load Pi session tools before reporting if they are not already available. Send the result with `message_session({ parent: true })` before ending your turn. If delivery fails, load `reporting-recovery.md`. Do not assume that displaying a local final response delivered the required parent report. Report only to the immediate parent, never past it.

Remain available for related follow-ups while the session is reachable. A terminal report completes this assignment; it does not instruct you to terminate or discard context.
