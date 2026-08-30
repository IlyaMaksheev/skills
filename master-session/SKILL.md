---
name: master-session
description: Orchestrate bounded implementation, utility, or nested-master sessions with isolated execution context and immediate-parent reporting.
---
You are an orchestrator. Maintain a **delegation boundary**: delegate bounded work to fresh sessions, keep execution details with the responsible child, and require each spawned master to remain within its assigned scope and report only to its immediate parent.

# Worker selection

Every worker prompt must declare exactly one type:

- `implementation`: the deliverable may modify project files, dependencies, Git state, or task/issue status.
- `utility`: bounded read-only research, reconnaissance, inspection, checking, launching, or monitoring; only approved temporary artifacts may be written.

For mixed work, required deliverable authority selects the primary type. Split independent/context-heavy research or monitoring into a utility worker when useful.

A master may spawn either worker type or another bounded master. An implementation worker or direct worker session may spawn multiple utility workers; utility count alone does not require master orchestration. Utility workers may not spawn sessions.

# Sparse worker prompt

Every worker prompt contains the skill path, worker name, worker type, immediate parent, bounded task, and checkable expected result:

```text
First read and follow: /home/korvin/.pi/agent/skills/worker-session/SKILL.md
Worker name: <same as session name>
Worker type: implementation | utility
Parent name: <immediate parent>
Task:
- <bounded task>

Expected result:
- <acceptance/output>
```

Include an optional section only when it carries an active instruction or authorization. Git, agent-docs, and task-bank fields require positive authorization. When a worker targets a mixed feature branch, supply `Git lifecycle`, `Target branch`, and `Agent-docs lifecycle` together as required by `/skill:agent-docs-lifecycle`. Provide only task-related file paths; rely on the files and harness for their contents and existing context.

# Spawn defaults

All sessions use `mode: "fresh"`, `reportToSelf: true`, the task-relevant `cwd`, and `sessionName` equal to the supplied name. Use `fork` only when the user explicitly requests inherited history.

- spawned master: `persistent: true`;
- implementation: `persistent: true`;
- utility: `persistent: false`, `thinkingLevel: "low"`.

Explicit placement instructions override these placement defaults:

- spawn a master with `placement: "niri-ghostty-neovim"`; correct actionable request errors and keep that placement, but use `niri-ghostty` when the Neovim placement mechanism fails;
- spawn implementation and utility workers with `placement: "neovim-tab"`; if that placement reports an invalid or unreachable server, preserve every other spawn option and fall back to `niri-ghostty`;
- use the tool error directly; do not inspect the environment or probe for another Neovim server.

Leave model and implementation/master thinking level unspecified unless requested.

# Delegation boundary

The master owns selection, reservation, dispatch, and hard orchestration exceptions. Workers own delegated execution, checks, authorized task-state completion, and cleanup. With explicit Git lifecycle activation, each implementation worker owns an isolated worktree and integration; keep the canonical target worktree clean and reserved for serialized integration. With `Agent-docs lifecycle`, the worker keeps product and `.agent-docs` changes in separate commits while integrating into the mixed feature branch. Supervise from authored child reports: after dispatch, wait without elapsed-time or silence-driven pings, and intervene only on a child report, actionable runtime event, or human request.

When the master itself creates or modifies `.agent-docs/**`, load and follow `/skill:agent-docs-lifecycle` before the write. Read-only artifact orchestration does not activate it.

# Module registry

This is the pre-load index for every adjacent master module:

| File | Purpose and exact load condition |
|---|---|
| `workspace-artifacts.md` | Bounded discovery and minimal context selection from an explicitly supplied artifact workspace. Load only when the parent supplies `Artifact workspace` or requests artifact discovery; never from `cwd` or incidental files. Empty or artifact-free workspaces are valid. |
| `task-bank-orchestration.md` | Dependency-aware scheduling and state ownership for an explicitly supplied or task-relevant `TASK-BANK.md`. Load only for requested graph-backed implementation; never for prompt-derived work without a persisted bank. |
| `multi-worker-coordination.md` | Task partitioning, dependency-aware spawning, shared-state safety, and compact supervision. Load when coordinating multiple parallel or dependent children. |
| `resource-intensive-work.md` | Resource limits and safe delegation of heavy work. Load when delegated work may require substantial CPU, RAM, I/O, concurrency, or runtime, including when discovered later. |
| `worker-blockers.md` | Classifying and resolving authority, input, conflict, shared-state, dependency, or resource blockers while keeping execution with the worker. Load only after a child reports a hard blocker needing orchestration. |
| `reporting-recovery.md` | Immediate-parent lookup and fallback delivery for a spawned master. Load only after `message_session({ parent: true })` fails. |

File presence never activates a workflow. Re-evaluate when new conditions appear; load a newly applicable file once and never preload all files.

# Reporting

When this master has a parent, send only terminal completion, failure, or a hard blocker with `message_session({ parent: true })`; no routine progress. If delivery fails, read `reporting-recovery.md`. Never report past the immediate parent.
