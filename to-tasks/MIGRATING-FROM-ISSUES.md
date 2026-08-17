# Migrating from Issues to Tasks

Use this guide only when the user explicitly asks to migrate legacy issue artifacts. Normal `/to-tasks` operation does not consume `ISSUE-BANK.md` or `issue-*.md` files.

Migration is mechanical and lossless. Do not reinterpret acceptance criteria, improve the breakdown, merge or split slices, change dependencies, or otherwise alter behavior.

## Tasks-only migration

1. Identify the legacy feature directory and select `./.plans/<feature-name>/` as the target.
2. Build the complete target manifest before writing:
   - `ISSUE-BANK.md` → `TASK-BANK.md`
   - `issue-NNN-<description>.md` → `task-NNN-<description>.md`
   - `issue-NNN-<description>-plan.md` → `task-NNN-<description>-plan.md`
3. Preserve numbering, zero padding, slugs, types, statuses, dependency order, acceptance criteria, parent relationships, and all substantive content.
4. Mechanically update structural terminology and links:
   - issue bank → task bank
   - issue used as the work-unit name → task
   - `ISSUE-BANK.md` → `TASK-BANK.md`
   - `issue-NNN-*.md` → `task-NNN-*.md`
   - issue-specific plan references → task-specific plan references
5. Do not globally replace words inside quoted material, historical notes, external titles, or content where `issue` is not naming a migrated work unit.
6. Preflight every target path. If any target exists, stop without writing anything. Report all collisions and ask whether the user wants to replace them, merge manually, or choose another destination.
7. Once the complete target set is safe, write all task artifacts.
8. Leave every legacy source file untouched.

## Complete feature-bundle migration

When the user asks to migrate the PRD and issues together:

1. Also load `../to-spec/MIGRATING-FROM-PRD.md` through the `/to-spec` skill.
2. Build one combined manifest containing `SPEC.md`, all task artifacts, all task-plan companions, and an existing `IMPLEMENTATION-CONTEXT.md`.
3. Preflight the combined target set before writing. If any target collides, write nothing.
4. Carry an existing `IMPLEMENTATION-CONTEXT.md` forward without reinterpretation. Only rewrite links and structural references to renamed planning artifacts.
5. Write the complete migrated bundle only after the whole preflight succeeds.
6. Leave every legacy source file untouched.
