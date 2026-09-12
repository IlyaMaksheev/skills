# Task-bank orchestration

## Activation

Load only for requested graph-backed scheduling when the user or parent explicitly supplies a task-bank path, or `../receiving-work/workspace-artifacts.md` selects a relevant `TASK-BANK.md` for requested graph-backed implementation. A discovered bank does not activate this module for unrelated work. Prompt-derived work without a persisted bank uses `multi-worker-coordination.md` when coordination is needed.

## Scheduling

Read the supplied bank in full and only the task files needed to select or dispatch work. Use its recorded type, status, ownership, and blockers; do not invent missing conventions.

The frontier is every unfinished, unclaimed task whose recorded blockers are complete. Apply `SKILL.md` delegation judgment to independent AFK frontier tasks. Dispatch worthwhile assignments when their writes and resources can safely overlap; execute suitable local work under `/skill:receiving-work`. Present HITL frontier tasks to the parent/user; never assign the human side of a decision to an autonomous worker. Load `multi-worker-coordination.md` when coordinating multiple children.

Before spawning, reserve the task using the bank's claim/owner convention when one exists and reservation is authorized; otherwise track assignment in compact session state. If persisted reservation is required but unauthorized, obtain permission before dispatch. Dispatch each task once from this session and respect every recorded blocker and existing owner.

Every applicable task-backed prompt must include:

```text
Task bank: <path>
Task artifact: <path-or-identifier>
```

When the bank is under `.agent-docs/**` and the worker targets its mixed feature branch, also pass the positive `Agent-docs lifecycle` field together with `Git lifecycle` and `Target branch`. The worker commits stable task-state changes separately from product changes.

Add relevant selected artifacts under `Input files`; do not pass the workspace directory as worker context. Explicitly state whether task-state mutation is authorized. Supplying task paths alone permits no mutation.

## Ownership

The assigned session owns its authorized task-state completion under the bank's existing convention:

- mark completion only after acceptance requirements, checks, and requested artifacts succeed;
- keep unrelated rows and tasks unchanged;
- unblock a dependent only when every recorded blocker is complete;
- preserve newer concurrent state;
- include the state update with feature history when Git lifecycle is active; under `Agent-docs lifecycle`, use a separate path-pure `agent-docs:` commit.

The assigning session owns selection, scheduling, and compact orchestration state. It performs authorized persisted reservation, spawn-failure recovery, and hard-exception updates; the assigned session owns authorized routine completion updates. With nested scheduling, allocate distinct task scopes and state ownership so a parent and child do not both reserve or complete the same task.

## Completion

A reservation is settled when its task is completed, terminally failed or blocked, or safely released after spawn failure. Schedule from terminal worker reports. Report completed tasks, remaining frontier work, HITL items, blockers, and failures without reproducing task bodies or worker context.
