---
name: to-tasks
description: Break a plan or spec into independently grabbable tasks using tracer-bullet vertical slices. Use when the user wants to convert a plan into tasks, create implementation tasks, or break down work into tasks.
disable-model-invocation: true
---

# To Tasks

Break a plan into independently grabbable tasks using vertical slices (tracer bullets).

The task bank format is [TASK-BANK-FORMAT.md](./TASK-BANK-FORMAT.md).

Legacy issue artifacts are not normal inputs to this skill. If the user explicitly asks to migrate an issue bank or issue files to the new task standard, read [MIGRATING-FROM-ISSUES.md](./MIGRATING-FROM-ISSUES.md) and follow it instead.

## Output location

When the user provides a spec path, use that spec's feature directory. Otherwise, use the active `./.plans/<feature-name>/` directory when one has already been established. If neither exists, derive a concise lowercase kebab-case feature name from the current context, state the selected path, and create the directory.

Write `TASK-BANK.md` and each `task-NNN-<short-description>.md` in that feature directory. Inspect existing artifacts and do not overwrite them without user confirmation.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a task reference as an argument, fetch it from the task bank and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Task titles and descriptions should use the project's domain glossary vocabulary and respect ADRs in the area you're touching.

### 3. Draft vertical slices

Break the plan into **tracer-bullet** tasks. Each task is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Slices may be `HITL` or `AFK`. HITL slices require human interaction, such as an architectural decision or design review. AFK slices can be implemented and merged without human interaction. Prefer AFK over HITL where possible.

<vertical-slice-rules>
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Prefer many thin slices over few thick ones
</vertical-slice-rules>

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each slice, show:

- **Title**: short descriptive name
- **Type**: HITL / AFK
- **Blocked by**: which other tasks (if any) must complete first
- **User stories covered**: which user stories this addresses (if the source material has them)

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the dependency relationships correct?
- Should any slices be merged or split further?
- Are the correct slices marked as HITL and AFK?

Iterate until the user approves the breakdown.

### 5. Add the tasks to the task bank

For each approved slice, publish a new task to the task bank. Use the task body template below.

Publish tasks in dependency order (blockers first) so you can reference real task identifiers in the `Blocked by` field.

## Task template

```md
## Parent

A reference to the parent task in the task bank (if the source was an existing task; otherwise omit this section).

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

- A reference to the blocking task (if any)

Or `None - can start immediately` if there are no blockers.
```

Do NOT close or modify any parent task.

File name template: `task-<number>-<short-descriptive-name>.md`.
