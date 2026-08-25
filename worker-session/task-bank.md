# Task-bank handling

## Read scope

Read the supplied bank, the selected task, its recorded blockers and dependents, and only the surrounding convention needed for the authorized operation. Keep sibling tasks outside the read scope.

## Authority

A delegated implementation worker or direct session may update only its selected task state under the bank's existing convention:

- verify the task is assigned to this worker when ownership is recorded;
- do not mark it complete until the expected result, acceptance criteria, checks, and requested artifacts succeed;
- preserve newer concurrent state and unrelated entries;
- unblock a dependent only when every recorded blocker is complete;
- include the state update with feature history when Git lifecycle is active;
- under `Agent-docs lifecycle`, commit a stable task-state update separately as a path-pure `agent-docs:` commit;
- without Git lifecycle, still perform the explicitly authorized task-state update.

A delegated utility worker may inspect supplied task context but must not mutate status, ownership, blockers, or dependencies. If conventions, assignment, or dependency state are ambiguous, report the exact blocker rather than inventing a transition.

## Report contribution

After an actual update, append:

```text
Task bank:
- <task>: <status transition>
- Dependents: <only actual unblock changes>
```

For read-only inspection, report only requested findings. Omit this section when no task-bank result exists.
