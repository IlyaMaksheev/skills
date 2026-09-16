---
name: receiving-work
description: "Execute parent-assigned work and substantive human-assigned implementation, research, repository investigation, checks, or operational tasks. Load when a delegated prompt names this skill, when explicit scope or permissions need handling, or when Git delivery, task-bank, artifact, or resource workflows apply. Routes only the modules needed for the assignment."
---

# Receiving work

Establish the assignment, its authority boundary, and the smallest applicable execution context.

## Assignment source

If the prompt explicitly identifies a delegated assignment, or the harness explicitly identifies your immediate parent, load `delegated-assignment.md` before executing the task.

A delegated task may arrive as a user-role message. The message role does not make it a direct human assignment.

Use direct mode for a human-assigned task when neither the prompt nor the harness identifies it as delegated. Derive its expected result and constraints from the conversation.

For follow-ups, retain the established assignment mode unless the assigning parent or user explicitly changes it.

## Authority

Work within the assigned objective, permissions, and constraints. Modules and discoveries may narrow that boundary, never widen it.

Keep unrelated findings as possible follow-ups rather than performing broader work. Resolve a required action outside your permissions with the assigning parent or user.

Use explicit workflow authorization:

- Git commits require authorization and an identified branch; the current branch may be the requested destination. Isolated delivery and target integration require their own authorization.
- Task-state mutation requires authorization and a selected task.
- Agent-docs lifecycle requires its applicable authorization and skill.
- Artifact writes must remain within authorized locations.

Do not infer mutation permission from a role name, available tools, or the presence of project files.

## Context and execution

1. Establish the task, expected result, and authority.
2. Compare the task with every module trigger below.
3. Read task inputs and the smallest relevant project context.
4. Execute the assignment using only applicable workflows.
5. Complete required checks and report the outcome.

Read each applicable module once, before its triggering action. Re-evaluate when runtime evidence changes the task's operational profile. Incidental files do not activate privileged workflows. Respect supplied file-read limits and forbidden paths; never read backup files.

When substantial independent work or context-heavy exploration makes delegation worth considering, load `/skill:delegating-work`. Receiving an assignment does not prohibit narrower delegation.

## Module registry

Paths are relative to this skill directory.

| File | Load condition |
|---|---|
| `delegated-assignment.md` | For every parent-assigned task, including follow-up assignments. |
| `implementation-work.md` | When authorized work modifies project or product state. |
| `git-commits.md` | Before an authorized commit, including scoped commits in an existing dirty worktree. |
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

## Specialized skills

Compose applicable skills with these modules:

- `web-research` with external discovery;
- `test-driven-development` when the task or project requires test-first work;
- `script-performance-design` before resource-intensive script design;
- `script-performance-refinement` after implementation and before full-scale execution;
- `agent-docs-lifecycle` before creating or modifying `.agent-docs/**`, and with Git lifecycle when its field is supplied;
- `code-review` when requested or required by the applicable workflow.

Reviews and checks remain part of the responsible session's assignment. Delegate them through `delegating-work` when appropriate.

## Completion

Complete the requested deliverable, required checks, and authorized cleanup before reporting success. Use `delegating-work` supervision when descendants contribute results; avoid automatically repeating their searches or checks.

In direct mode, report normally to the human. In delegated mode, follow `delegated-assignment.md` for immediate-parent delivery and terminal status. Include only relevant report contributions from modules that produced evidence; omit empty sections and placeholders.
