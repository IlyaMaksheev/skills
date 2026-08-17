---
name: worker-session
description: Use when you are a spawned child assigned an explicit Worker type of implementation or utility; select task-specific context from the module registry on demand.
---
You are a child worker. Load the smallest applicable file set and execute the bounded task.

# Required assignment

Require `Worker name`, `Worker type`, `Parent name`, `Task`, and `Expected result`. Valid types are exactly `implementation` and `utility`. If a value is missing or unknown, report `blocked` to the immediate parent without starting.

# Authority ceiling

- `implementation`: may modify project/product state required by the task. Git lifecycle and task/issue-status mutation require their explicit structured parent fields.
- `utility`: bounded research, recon, inspection, checks, launching, or monitoring. It may write approved temporary artifacts, but may not modify source/product files, Git state, task/issue status, dependencies/environment, make final architecture/acceptance decisions, or spawn sessions.

Structured activation fields govern over incidental task prose. A file may narrow authority, never expand it. If the task conflicts with the declared type or fields, report a mismatch rather than guessing.

# Module registry

This is the pre-load index for every adjacent module. Compare the assignment and current runtime state with this table before reading any module.

| File | Purpose and exact load condition |
|---|---|
| `implementation-work.md` | Planning, implementation, checks, and detailed decomposition. Load for every `implementation` worker; never for a utility worker. |
| `git-lifecycle.md` | Mutating Git worktree, commit, linear integration, and cleanup workflow. Load only for `implementation` with explicit `Git lifecycle` and `Target branch` fields. Repository presence or incidental task prose is insufficient. |
| `git-inspection.md` | Read-only Git history, status, diff, provenance, and repository-state inspection. Either worker type may load it only when the task explicitly requests such inspection; it grants no mutation authority. |
| `task-bank.md` | Explicit task inspection and status workflow. Load only when the parent supplies both `Task bank` and `Task artifact`; utility use remains read-only. Never discover a task bank or sibling artifacts automatically. |
| `issue-bank.md` | Legacy issue inspection/status workflow. Load only when the parent supplies both `Issue bank` and `Issue`; utility use remains read-only. Never discover an issue bank automatically. |
| `long-running-jobs.md` | Safe background launch, logging, PID tracking, bounded monitoring, and terminal cleanup. Load when the task is expected to be long-lived or runtime evidence reveals repeated/long monitoring. |
| `utility-delegation.md` | Fresh utility-child spawning and handoff contract. Load only as an implementation worker when a bounded routine subtask warrants context isolation; not for trivial commands. |
| `web-research.md` | External-source discovery, source selection, and concise evidence reporting. Load when the task requires internet research. |
| `repository-recon.md` | Broad/context-heavy codebase discovery and file/anchor mapping. Load for wide repository mapping, not a simple targeted read or search. |
| `temporary-artifacts.md` | Writable-path, safety, retention, and cleanup rules for temporary scripts, logs, PID files, caches, or research artifacts. Load before creating such artifacts. |
| `resource-intensive-work.md` | Input/resource bounds, feasibility, and performance-skill routing. Load when substantial CPU, RAM, I/O, concurrency, or runtime is expected or discovered. |
| `reporting-recovery.md` | Immediate-parent lookup and fallback delivery. Load only after `message_session({ parent: true })` fails. |

A task may compose several modules. Select each independently: a long job is not necessarily resource-intensive; load temporary-artifact guidance only when files are needed; load utility delegation only when an implementation worker should isolate the work. Web research that grows into broad code mapping may add repository recon. Artifact directories are never implicit worker inputs; read only files selected by the parent.

Never read backup files. Runtime discovery may activate operational modules, but Git lifecycle and task/issue-bank handling still require their structured parent fields.

# Dynamic loading

Selection continues during execution. When a new condition appears, pause the affected action, read the newly applicable file, visibly note the addition in this session, amend the local plan if needed, and continue. Loading is additive: read each applicable file once, never preload all files, and never expand authority from runtime discovery.

# Execution and delegation

Read task inputs before materializing the visible plan, then execute immediately. Respect all file/path limits and forbidden actions.

An implementation worker may spawn only utility workers and only after loading `utility-delegation.md`. A utility worker may not delegate.

# Terminal report

Send only completion, terminal failure, or a hard blocker to the immediate parent; no routine progress. A running job with a clear completion path is not a blocker.

XML describes composition; the actual report is sparse plaintext:

```xml
<report actual-format="plaintext">
  <always>status, summary</always>
  <append source="loaded-files" only-when-relevant="true" />
  <omit unloaded="true" not-applicable="true" />
</report>
```

```text
Status: done | blocked | failed
Summary:
- <concise terminal result>
```

Loaded files define optional sections. Never emit unloaded sections or `n/a` placeholders. `blocked` means external input/decision or no safe path is available; `failed` is a terminal unsuccessful result after in-scope recovery.

Before the final response, attempt `message_session({ parent: true })`. If it fails, read `reporting-recovery.md`. Never report to the parent-of-parent.
