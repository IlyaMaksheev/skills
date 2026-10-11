# Supervision

## While work is assigned

Keep compact state: worker identity, assignment, expected result, and assigned/blocked/done/failed outcome. Keep execution details with the responsible child.

Continue useful non-overlapping work within your own scope. Newly discovered independent work need not have been planned before dispatch, but establish that it does not duplicate an existing assignment before acting. Wait when the next needed action depends on a child or no useful independent work remains.

When the human requested checkpoint updates, relay each corresponding child report concisely. Identify the phase or attempt, outcome, and next authorized action. A checkpoint report is not a terminal assignment report; keep the assignment active unless its expected result or terminal condition has been reached.

Use explicit terminal task outcomes as the completion signal; ordinary assignments require authored parent reports. Do not poll or ping a reporting worker because of silence, elapsed time, or working/supervising/settled state. Act on authored reports, actionable runtime events, or human requests. Harness settlement alone is not task success. A worker awaiting local HITL remains assigned; direct the user to its named session and stable ID. Technical readiness or runtime settlement alone does not complete HITL. On `report-missing`, `worker-unreachable`, or child-message delivery failure, load `reporting-exceptions.md`. These events establish a communication problem, not the task's outcome.

## Consume results

Treat a child's completed report as finished delegated work. Compare it with the expected deliverable, not with a second execution of the task.

- Complete result: understand and integrate it into your assignment.
- Missing answer, artifact, or requested evidence: define the missing deliverable and select its owner through `briefing-and-dispatch.md`.
- Concrete contradiction, hard blocker, or failure: load `worker-blockers.md` and resolve within your authority.

Verify only when explicitly requested, required by an applicable workflow, or needed to resolve a concrete problem; otherwise use the result without repeating searches, derivations, or checks. Required checks/reviews belong to the responsible session and may be delegated. Read selected evidence to act on findings; retain conclusions and anchors, not the child's transcript.

## Related follow-ups

Read `briefing-and-dispatch.md` before follow-ups and apply its Worker selection guidance. A `done` report ends the assignment, not worker availability. Send affected workers the smallest necessary assumption update.

## Session cleanup

Track every child created for the assignment by exact session ID. After accepting a child's terminal report and completing required integration and checks, call `remove_session` unless a concrete pending follow-up requires its context. Required HITL decisions, human review, and resulting revisions must be settled before removal. Retain the responsible worker while that interaction is pending. The parent owns child-session removal; Git worktree cleanup is a separate obligation.

Before final delivery or acknowledging task closure, account for every child:

- **Removed:** `remove_session` confirmed `status: "complete"`.
- **Retained:** name the pending follow-up requiring its context.
- **Blocked:** report why cleanup could not complete, including partial or rejected tool results.

Use explicit task outcomes delivered through the agreed reporting mode; settlement alone does not establish acceptance or readiness for removal.

## Completion

Your task may finish when required child assignments are terminal, their results have been integrated or their unresolved outcomes reported, every child session is accounted for under Session cleanup, and your own expected result is accounted for. Children own their authorized checks and task artifacts; retain parent-side synthesis, session cleanup, and any explicitly assigned scheduling duties.

Report through your existing direct or delegated contract. When useful, include a compact `Delegation` section naming the result used from each child; do not reproduce full child reports.
