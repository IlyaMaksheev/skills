# Legacy issue-bank handling

Load only for explicit legacy `Issue bank` and `Issue` fields. Current task banks use `task-bank.md`.

## Read scope

Read the supplied issue entry, its stated blockers/dependents, and only the surrounding conventions needed to update or inspect it. Keep unrelated issues unchanged.

## Worker-type behavior

An implementation worker owns its issue-state update:

- do not mark the issue done until the expected result, required checks, and requested artifacts are complete;
- update the current issue using the bank's existing status convention;
- unblock a dependent only when every recorded blocker is done;
- preserve newer statuses from other workers when resolving concurrent changes;
- when `git-lifecycle.md` is active, include the issue-bank update with the same feature history before integration;
- without Git lifecycle, still complete the explicitly requested issue-bank edit as part of the implementation task.

A utility worker may inspect the explicitly supplied issue context when required, but must not change status, blockers, or dependencies.

If the bank's conventions or dependency state are ambiguous, do not invent a transition. Report the exact ambiguity as a blocker.

## Report contribution

After an actual update, append:

```text
Issue bank:
- <issue>: <status transition>
- Dependents: <only actual unblock changes>
```

For read-only inspection, report only findings required by the task. Omit this section when no issue-bank result is relevant.
