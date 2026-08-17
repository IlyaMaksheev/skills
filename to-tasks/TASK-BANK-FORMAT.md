---
description: The structure of the task bank
---

# Task Bank Format

The task bank is a collection of files representing the global and local state of available tasks.

## Tasks global state

`TASK-BANK.md` template:

```md
# Tasks

| ID | Task | Type | Status | Blocked by |
```

### Parent section

If there is a parent `TASK-BANK.md` file, reference it in the local bank:

```md
# Parent

- [Parent task bank](__file_link__)
```

## Tasks

Each task has its own file in the same directory as `TASK-BANK.md`.

Structure:

```text
./.plans/<feature-name>/
├── SPEC.md
├── TASK-BANK.md
├── IMPLEMENTATION-CONTEXT.md
├── task-001-<short-description>.md
├── task-002-<short-description>.md
└── task-00n-<short-description>.md
```

`IMPLEMENTATION-CONTEXT.md` is optional and is owned by `/to-implementation-context`, not `/to-tasks`.

The default root directory is `./.plans/`. Use one lowercase kebab-case subdirectory per feature.
