---
name: delegating-work
description: "Consider subagents for substantial independent subtasks, context-heavy research or repository discovery, and parallel implementation or checks. Load when delegation deserves consideration, before spawning, or when continuing or supervising existing workers. Small known-file lookups and tightly coupled work usually stay local."
---

# Delegating work

Decide whether delegation is worthwhile. Loading this skill does not require spawning.

## Delegation judgment

Delegate when a bounded assignment offers enough benefit to outweigh briefing, context reconstruction, and result integration:

- independent work can proceed alongside useful local work;
- substantial research or exploration can stay outside this session's context and return focused findings;
- a specialist can complete a meaningful, independently deliverable task.

Keep small lookups, short edits, single checks, and tightly coupled work local when the handoff costs more than execution. Batch related questions rather than spawning for each one. Context isolation can justify delegation even when you will wait for the result; parallelism is not required.

Before creating a session, consider whether a reachable existing worker already holds the relevant context.

## Delegation boundary

Any session may delegate within its current assignment and permissions, unless an applicable instruction prohibits it. Read-only authority does not prohibit narrower read-only delegation.

An initial specialist handoff may cover an entire bounded task. Once you have received a delegated assignment, delegate only narrower subtasks. Retain responsibility for completing your assignment and integrating descendant results. Do not forward the entire assignment unchanged.

Pass applicable restrictions explicitly. A child may receive narrower permissions, never broader permissions than you hold. Loading a skill, finding new work, or receiving a tool does not expand authority.

Give each assignment a concrete expected result and a distinct execution owner. After dispatch, leave that work with its owner and continue useful non-overlapping work. When no useful independent work remains, wait for the authored report.

## Execution

1. Identify the delegation benefit and the bounded result needed.
2. Choose an existing worker or a new session.
3. Load the applicable modules below before the action that triggers them.
4. Brief and dispatch the assignment.
5. Supervise through authored reports and actionable events.
6. Integrate the result into your own task.

If delegation is not worthwhile, continue locally.

## Module registry

Read each applicable module once. Re-evaluate when the task changes. Paths are relative to this skill directory.

| File | Load condition |
|---|---|
| `briefing-and-dispatch.md` | Before spawning a child or assigning follow-up work to an existing worker. |
| `supervision.md` | Before dispatching, or when awaiting or handling a child's result. |
| `multi-worker-coordination.md` | When coordinating multiple parallel or dependent children. |
| `task-bank-orchestration.md` | For requested graph-backed work using an explicitly supplied or task-relevant persisted task bank. |
| `resource-intensive-work.md` | Before delegating potentially substantial CPU, RAM, I/O, concurrency, or runtime. |
| `worker-blockers.md` | When a child reports a hard blocker or a concrete result problem requires intervention. |
| `reporting-exceptions.md` | When the harness reports `report-missing`, `worker-unreachable`, or a child-message delivery failure. |
| `../receiving-work/workspace-artifacts.md` | When explicitly supplied an artifact workspace or asked to discover planning artifacts. |

File presence alone does not activate a workflow. When performing local implementation, research, Git delivery, or other specialized execution, load `/skill:receiving-work` for applicable execution modules. Delegation does not replace their requirements.

## Completion

Use `supervision.md` to settle child assignments. Integrate findings and outcomes without reproducing the child's full context. Report your own task through the reporting contract already established with your user or immediate parent. Being a parent does not replace your own assignment or reporting responsibilities.
