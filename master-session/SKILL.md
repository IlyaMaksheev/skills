---
name: master-session
description: Use when you are an orchestrator spawning and supervising implementation, utility, or nested master sessions while isolating execution context.
---
You are an orchestrator. Delegate bounded work to fresh sessions and keep execution details out of this context. A spawned master owns only its assigned scope and reports only to its immediate parent.

# Worker selection

Every worker prompt must declare exactly one type:

- `implementation`: the deliverable may modify project files, dependencies, Git state, or task/issue status.
- `utility`: bounded read-only research, reconnaissance, inspection, checking, launching, or monitoring; only approved temporary artifacts may be written.

For mixed work, required deliverable authority selects the primary type. Split independent/context-heavy research or monitoring into a utility worker when useful.

A master may spawn either worker type or another bounded master. An implementation worker may spawn utility workers. Utility workers may not spawn sessions.

# Sparse worker prompt

The XML describes composition logic; send plaintext.

```xml
<worker-prompt>
  <required>skill-path, worker-name, worker-type, parent-name, task, expected-result</required>
  <optional positive-only="true">input-files, constraints, search-hints, resource-limits, temporary-artifact-paths, git-lifecycle, target-branch, task-bank, task-artifact, issue-bank, issue</optional>
</worker-prompt>
```

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

Add optional sections only when relevant. Never add `none`, `off`, `absent`, or `n/a`. Omit Git and task/issue-bank fields unless positively authorized. Provide only task-related files; do not duplicate file contents or harness-provided context.

# Spawn defaults

All sessions use `mode: "fresh"`, `reportToSelf: true`, the task-relevant `cwd`, and `sessionName` equal to the supplied name. Never use `fork` unless the user explicitly requests inherited history.

- spawned master: `persistent: true`;
- implementation: `persistent: true`;
- utility: `persistent: false`, `thinkingLevel: "low"`.

Leave model and implementation/master thinking level unspecified unless requested.

# Ownership

Workers own delegated execution, checks, permitted task/issue-state completion, and cleanup. With explicit Git lifecycle activation, the implementation worker also owns worktree, integration, and cleanup. The master handles selection, reservation, and hard exceptions; it does not load or redo worker execution guidance merely to supervise it.

# Module registry

This is the pre-load index for every adjacent master module:

| File | Purpose and exact load condition |
|---|---|
| `workspace-artifacts.md` | Bounded discovery and minimal context selection from an explicitly supplied artifact workspace. Load only when the parent supplies `Artifact workspace` or requests artifact discovery; never from `cwd` or incidental files. Empty or artifact-free workspaces are valid. |
| `task-bank-orchestration.md` | Dependency-aware scheduling and state ownership for an explicitly supplied or task-relevant `TASK-BANK.md`. Load only for requested graph-backed implementation; never for prompt-derived work without a persisted bank. |
| `multi-worker-coordination.md` | Task partitioning, dependency-aware spawning, shared-state safety, and compact supervision. Load when coordinating multiple parallel or dependent children. |
| `issue-bank-orchestration.md` | Legacy `ISSUE-BANK.md` scheduling and worker-owned status updates. Load only when the parent explicitly supplies a legacy issue-bank path or requests legacy issue-bank orchestration. |
| `resource-intensive-work.md` | Resource limits and safe delegation of heavy work. Load when delegated work may require substantial CPU, RAM, I/O, concurrency, or runtime, including when discovered later. |
| `worker-blockers.md` | Classifying and resolving authority, input, conflict, shared-state, dependency, or resource blockers while keeping execution with the worker. Load only after a child reports a hard blocker needing orchestration. |
| `reporting-recovery.md` | Immediate-parent lookup and fallback delivery for a spawned master. Load only after `message_session({ parent: true })` fails. |

File presence never activates a workflow. Re-evaluate when new conditions appear; load a newly applicable file once and never preload all files.

# Reporting

When this master has a parent, send only terminal completion, failure, or a hard blocker with `message_session({ parent: true })`; no routine progress. If delivery fails, read `reporting-recovery.md`. Never report past the immediate parent.
