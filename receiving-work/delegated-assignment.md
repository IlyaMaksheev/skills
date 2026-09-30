# Delegated assignment

## Establish the contract

Require `Task`, `Expected result`, and `Permissions and constraints`. Resolve immediate-parent routing from the harness; use explicit parent metadata when provided. Session name and parent name need not be duplicated in every prompt when the harness supplies reliable identity.

If required assignment information is missing, or the expected result exceeds the supplied authority, report `blocked` to the immediate parent before execution. Do not silently choose broader permissions. If parent identity is unavailable, ask for clarification locally rather than guessing another session.

Interpret a follow-up within the existing assignment context. Explicit task and expected-result updates define the new deliverable; unchanged restrictions continue to apply. A new tool or discovered opportunity does not grant additional authority.

Optional fields authorize only their stated workflow. `Task bank` and `Task artifact` provide context, not mutation permission. `Git lifecycle` requires `Target branch`; with `Agent-docs lifecycle`, also read `../agent-docs-lifecycle/SKILL.md` for mixed-feature delivery.

After validation, return to `SKILL.md` and select execution modules from the actual task. Delegate only after loading `/skill:delegating-work` when its consideration triggers apply.

## Execution ownership

Own execution, checks, authorized task-state completion, and cleanup; finish required deliverables and checks before success. Integrate descendant results before reporting. A running job with a clear completion path is not a blocker.

Keep routine progress local; report completion, terminal failure, or hard blockers to the immediate parent.

## Parent reporting

Deliver your terminal result to the immediate parent using sparse plaintext:

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
