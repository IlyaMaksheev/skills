---
name: worker-session
description: "Worker-session router for direct human-guided tasks and structured delegated assignments."
---
Use this session as a bounded worker. Select the invocation mode, establish its authority envelope, load the smallest applicable module set, and execute the active task.

# Invocation mode

Select exactly one mode before loading modules.

## Delegated mode

The presence of any structured assignment field selects delegated mode. Recognized fields are `Worker name`, `Worker type`, `Parent name`, `Task`, `Expected result`, `Git lifecycle`, `Target branch`, `Task bank`, `Task artifact`.

Require `Worker name`, `Worker type`, `Parent name`, `Task`, and `Expected result`. Valid worker types are exactly `implementation` and `utility`. If a required value is missing or unknown, report `blocked` to the immediate parent before starting work.

## Direct mode

When no structured assignment field is present, derive the task, expected result, and constraints from the human conversation. Human instructions define the authority envelope under normal coding-agent safety rules. If no actionable task is available, ask the human what to work on.

# Authority envelope

The invocation establishes the session's **authority envelope**. Modules and runtime discoveries may narrow the envelope, never widen it.

In delegated mode, worker type sets the baseline and structured activation fields grant privileged workflows. Structured fields take precedence over incidental task prose.

- `implementation` may modify project or product state within the task. Git lifecycle and task-state mutation also require their registry fields.
- `utility` performs bounded research, reconnaissance, inspection, checks, launching, or monitoring. It may write approved temporary artifacts. Source/product files, Git state, task state, dependencies, environment, final architecture and acceptance decisions, and session delegation remain with an implementation worker.

In direct mode, explicit human instructions authorize project changes, Git delivery, task handling, or delegation. Discovery alone grants none of them.

Report an assignment mismatch when a delegated expected result falls outside its authority envelope. In direct mode, ask for clarification when the requested authority is ambiguous.

# Module registry

This registry is the single source of truth for module activation. Compare the active task and runtime evidence with every row before planning, then again whenever the task's operational profile changes. Read each applicable module once; do not peek into modules to decide whether they apply.

| File | Capability and activation hook |
|---|---|
| `implementation-work.md` | Planning, implementation, checks, and detailed decomposition. Load for delegated `implementation` work and direct tasks that modify project or product state. |
| `git-lifecycle.md` | Git worktree creation, commits, linear integration, verification, and cleanup. Load in delegated mode with both `Git lifecycle` and `Target branch`; in direct mode, load when the human explicitly requests worker-owned Git delivery and identifies the target branch. |
| `git-inspection.md` | Read-only Git status, history, diff, provenance, or repository-state evidence. Load when the task or expected result explicitly requests Git-derived inspection. |
| `task-bank.md` | Selected task inspection and state handling. Load in delegated mode with both `Task bank` and `Task artifact`; in direct mode, load when the human explicitly identifies the task bank and selected task. Delegated utility access remains read-only. |
| `long-running-jobs.md` | Safe background launch, bounded monitoring, terminal detection, and cleanup. Load before starting a process expected to outlive a normal tool call, or when runtime evidence requires repeated or prolonged monitoring. |
| `utility-delegation.md` | Fresh utility-child spawning and handoff. Load before a delegated implementation worker or direct session delegates a bounded routine subtask whose isolation materially protects implementation context. |
| `web-research.md` | Session-specific authority and reporting for external research. Load when the task requires internet discovery or evidence from external sources. |
| `repository-recon.md` | Broad codebase discovery and an anchored file/symbol map. Load when the task requires wide repository mapping rather than a targeted read or search. |
| `temporary-artifacts.md` | Writable-path ownership, safety, retention, and cleanup. Load before creating temporary scripts, logs, PID files, caches, or research artifacts. |
| `resource-intensive-work.md` | Resource bounds, feasibility, and performance-work composition. Load when substantial CPU, RAM, I/O, concurrency, or runtime is expected or observed. |
| `reporting-recovery.md` | Immediate-parent lookup and fallback delivery. Load in delegated mode only after `message_session({ parent: true })` fails. |

Operational evidence may activate modules during execution. In delegated mode, privileged workflows remain field-gated. In direct mode, they require explicit human authorization and identified targets. Repository presence, discovered artifact banks, and incidental prose do not activate them. Read only selected task artifacts, and never read backup files.

# Specialized skill hooks

Compose specialized skills with the worker modules rather than reproducing their procedures here:

- load `web-research` with `web-research.md` for internet discovery;
- load `test-driven-development` when the implementation task or repository requires test-first work;
- load `script-performance-design` before designing or implementing a resource-intensive script or workflow;
- load `script-performance-refinement` after such an implementation and before full-scale execution.

The worker modules retain authority, composition, and completion rules; specialized skills supply their domain procedure.

# Execution

Read task inputs and the smallest relevant project context before materializing a visible plan. Respect every file/path limit and forbidden action, then execute the plan immediately.

When runtime evidence activates another module, pause the affected action, record the addition in the session, read the module, amend the plan as needed, and continue within the original authority envelope. Module loading is additive.

A delegated implementation worker or direct session may spawn only utility workers and only under `utility-delegation.md`. A delegated utility worker executes directly without delegation.

# Completion and reporting

Loaded modules may contribute their named sections only when they produced evidence relevant to the terminal result. Omit unloaded, empty, irrelevant, and placeholder sections.

## Delegated mode

Send only completion, terminal failure, or a hard blocker to the immediate parent; keep routine progress in the child session. A running job with a clear completion path is not a blocker.

Use sparse plaintext. Always include:

```text
Status: done | blocked | failed
Summary:
- <concise terminal result>
```

`blocked` means external input or a decision is required, or no safe path remains. `failed` means in-scope recovery ended without the expected result.

Before the final response, attempt `message_session({ parent: true })`. If delivery fails, load `reporting-recovery.md` and follow it. Report only to the immediate parent.

## Direct mode

Interact with and report to the human in the current session. Use normal concise progress and completion responses; the delegated plaintext schema and parent-delivery procedure do not apply.
