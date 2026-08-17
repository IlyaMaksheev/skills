# Task-bank orchestration

## Activation

Load only when the parent explicitly supplies a task-bank path, or `workspace-artifacts.md` selects a relevant `TASK-BANK.md` for requested graph-backed implementation. A discovered bank does not activate this module for unrelated work. Prompt-derived work without a persisted bank uses `multi-worker-coordination.md` when coordination is needed.

## Scheduling

Read the supplied bank in full and only the task files needed to select or dispatch work. Use its recorded type, status, ownership, and blockers; do not invent missing conventions.

The frontier is every unfinished, unclaimed task whose recorded blockers are complete. Spawn independent AFK frontier tasks when their writes and resources can safely overlap. Present HITL frontier tasks to the parent/user; never assign the human side of a decision to an autonomous worker. Load `multi-worker-coordination.md` when coordinating multiple children.

Before spawning, reserve the task using the bank's claim/owner convention when one exists; otherwise track assignment in compact master state and never dispatch it twice from this session. Do not bypass blockers or another owner.

Every applicable implementation-worker prompt must include:

```text
Task bank: <path>
Task artifact: <path-or-identifier>
```

Add relevant selected artifacts under `Input files`; do not pass the workspace directory as worker context. Utility workers may inspect explicitly supplied task context when required but remain read-only.

## Ownership

An implementation worker owns its authorized task-state completion under the bank's existing convention:

- mark completion only after acceptance requirements, checks, and requested artifacts succeed;
- keep unrelated rows and tasks unchanged;
- unblock a dependent only when every recorded blocker is complete;
- preserve newer concurrent state;
- include the state update with feature history when Git lifecycle is active.

The master owns selection, reservation, scheduling, and compact orchestration state. It updates task state only for reservation, spawn failure recovery, or a hard exception the worker cannot safely resolve. Do not routinely duplicate worker updates.

## Completion

Schedule from terminal worker reports. Report completed tasks, remaining frontier work, HITL items, blockers, and failures without reproducing task bodies or worker context.
