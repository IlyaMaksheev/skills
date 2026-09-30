---
name: receiving-work
description: "Execute substantive human- or parent-assigned implementation, research, repository investigation, checks, or operations. Load for delegated prompts, explicit scope/permissions, or Git delivery, task-bank, artifact, or resource workflows."
---

# Receiving work

Establish the assignment, its authority boundary, and the smallest applicable execution context.

## Assignment source

If the prompt identifies a delegated assignment or the harness identifies your immediate parent, use delegated mode and read `delegated-assignment.md` before execution—even for user-role messages. Otherwise use direct mode, deriving the expected result and constraints from the human conversation. Retain the established mode for follow-ups unless the assigning parent or user explicitly changes it.

## Authority

Work within the assigned objective, permissions, and constraints; modules, tools, and discoveries do not expand them. Keep unrelated findings as follow-ups. Resolve required out-of-scope actions with the assigning parent or user.

Use explicit workflow authorization:

- Git commits require authorization and an identified branch; the current branch may be the requested destination. Isolated delivery and target integration require their own authorization.
- Task-state mutation requires authorization and a selected task.
- Agent-docs lifecycle requires its applicable authorization and skill.
- Artifact writes must remain within authorized locations.

Roles and incidental files grant no mutation permission or workflow activation.

## Context and execution

1. Establish the task, expected result, and authority.
2. Evaluate every module trigger below; read each applicable module once, before its triggering action.
3. Read task inputs and the smallest relevant project context, then execute applicable workflows.
4. Complete required checks, authorized cleanup, and reporting.

Re-evaluate triggers when runtime evidence changes the operational profile. Respect supplied file-read limits and forbidden paths; never read backup files.

When substantial independent work or context-heavy exploration makes delegation worth considering, load `/skill:delegating-work`. Receiving an assignment does not prohibit narrower delegation.

## Module registry

Paths are relative to this skill directory.

| File | Load condition |
|---|---|
| `delegated-assignment.md` | For every parent-assigned task, including follow-up assignments. |
| `implementation-work.md` | When authorized work modifies project or product state. |
| `git-commits.md` | When commits are authorized, before editing; also before committing existing attributable task changes, including in dirty worktrees. |
| `git-lifecycle.md` | When isolated-worktree delivery or target-branch integration is authorized and the target branch is identified. |
| `git-inspection.md` | When the expected result requires read-only Git-derived evidence. |
| `task-bank.md` | When a task bank and selected task are explicitly identified; mutations require separate authorization. |
| `workspace-artifacts.md` | When an artifact workspace is explicitly supplied or artifact discovery is requested. |
| `web-research.md` | When internet discovery or external-source evidence is required. |
| `repository-recon.md` | For broad repository mapping rather than a targeted known-file read or search. |
| `long-running-jobs.md` | Before a process expected to outlive a normal tool call, or when prolonged monitoring becomes necessary. |
| `temporary-artifacts.md` | Before creating temporary scripts, logs, PID files, caches, or research artifacts. |
| `resource-intensive-work.md` | When substantial CPU, RAM, I/O, concurrency, or runtime is expected or observed. |
| `reporting-recovery.md` | Only after immediate-parent report delivery fails. |

## Completion

Own the deliverable, required checks/reviews, and authorized cleanup; complete them before reporting success. For descendant contributions, use `delegating-work` supervision rather than automatically repeating their work.

Report to the human in direct mode; follow `delegated-assignment.md` for immediate-parent delivery and terminal status in delegated mode. Include relevant module evidence only; omit empty sections and placeholders.
