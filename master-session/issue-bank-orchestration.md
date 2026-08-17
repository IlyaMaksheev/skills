# Legacy issue-bank orchestration

Load only for an explicitly supplied legacy `ISSUE-BANK.md`. Current `TASK-BANK.md` workflows use `task-bank-orchestration.md`.

## Scheduling

Read only the supplied issue bank and issue files needed to understand dependencies. Track blockers and spawn only work that is currently unblocked.

Every applicable implementation-worker prompt must positively include:

```text
Issue bank: <path>
Issue: <identifier>
```

Do not add these fields to unrelated workers.

## Ownership

The implementation worker owns its issue-state changes:

- mark its issue done only after acceptance requirements and checks pass;
- unblock dependents only when all recorded blockers are done;
- keep unrelated entries unchanged;
- include issue-bank changes with the implementation work and, when Git lifecycle is active, in the same feature history.

Utility workers may inspect an explicitly supplied issue bank when their task requires it, but may not modify status.

The master schedules from worker reports and intervenes only when a worker cannot safely complete its own update. Do not routinely clean up issue status on workers' behalf.
