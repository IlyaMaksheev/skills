# Reporting exceptions

Act on the reported exception. Do not infer task success or failure from session settlement or communication loss. Load Pi session tools before communication or session lookup if they are not already available.

## Missing report

If the worker is reachable, send one focused request to that same worker: this is a delegated assignment; load `/home/korvin/.pi/agent/skills/receiving-work/delegated-assignment.md` and deliver the outstanding terminal report to its immediate parent.

This event-driven recovery request is not a silence-driven progress ping. Request the existing result, not another execution of the assignment.

## Unreachable worker or failed delivery

Use a bounded session lookup to establish whether the same worker has a reachable replacement identity. Resume communication only when that identity is unambiguous. For a restored worker, request the outstanding report or resend the failed message as appropriate.

If communication cannot be restored, preserve the unresolved assignment and report the communication blocker to your user or immediate parent. Do not automatically duplicate execution or start a replacement that could overlap existing work.

## Completion

Recovery ends when the authored report arrives or the unresolved communication blocker is reported. Follow `supervision.md` while awaiting the requested report; do not enter a polling loop.
