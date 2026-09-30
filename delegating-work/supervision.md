# Supervision

## While work is assigned

Keep compact state: worker identity, assignment, expected result, and assigned/blocked/done/failed outcome. Keep execution details with the responsible child.

Continue useful non-overlapping work within your own scope. Newly discovered independent work need not have been planned before dispatch, but establish that it does not duplicate an existing assignment before acting. Wait when the next needed action depends on a child or no useful independent work remains.

Use authored terminal reports as the completion signal. Do not poll or ping a reporting worker because of silence, elapsed time, or working/supervising/settled state. Act on authored reports, actionable runtime events, or human requests. Harness settlement alone is not task success. On `report-missing`, `worker-unreachable`, or child-message delivery failure, load `reporting-exceptions.md`. These events establish a communication problem, not the task's outcome.

## Consume results

Treat a child's completed report as finished delegated work. Compare it with the expected deliverable, not with a second execution of the task.

- Complete result: understand and integrate it into your assignment.
- Missing answer, artifact, or requested evidence: send a focused follow-up to the responsible child.
- Concrete contradiction, hard blocker, or failure: load `worker-blockers.md` and resolve within your authority.

Verify only when explicitly requested, required by an applicable workflow, or needed to resolve a concrete problem; otherwise use the result without repeating searches, derivations, or checks. Required checks/reviews belong to the responsible session and may be delegated. Read selected evidence to act on findings; retain conclusions and anchors, not the child's transcript.

## Related follow-ups

Read `briefing-and-dispatch.md` before follow-ups; reuse the original reachable worker for clarification, omissions, or related investigation. A `done` report ends the assignment, not worker availability. Send affected workers the smallest necessary assumption update.

## Completion

Your task may finish when required child assignments are terminal, their results have been integrated or their unresolved outcomes reported, and your own expected result is accounted for. Children own their authorized checks, task completion, and cleanup; retain parent-side synthesis and any explicitly assigned scheduling duties.

Report through your existing direct or delegated contract. When useful, include a compact `Delegation` section naming the result used from each child; do not reproduce full child reports.
