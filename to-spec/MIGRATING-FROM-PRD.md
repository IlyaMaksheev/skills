# Migrating from PRD to Spec

Use this guide only when the user explicitly asks to migrate a legacy PRD. Normal `/to-spec` operation does not consume PRD artifacts.

Migration is mechanical and lossless. Do not reinterpret requirements, improve the document, add missing decisions, or otherwise change its behavior.

## Spec-only migration

1. Identify the legacy `PRD.md` and its feature name.
2. Select `./.plans/<feature-name>/SPEC.md` as the target.
3. Preflight the complete target set before writing.
4. If `SPEC.md` already exists, stop without writing anything. Report the collision and ask whether the user wants to replace it, merge manually, or choose another destination.
5. Create `SPEC.md` while preserving the legacy document's section order and content.
6. Mechanically update structural terminology and links:
   - `PRD` used as the artifact name becomes `spec` or `SPEC.md`, as appropriate.
   - Links to `PRD.md` become links to `SPEC.md`.
   - PRD-specific template labels become their spec equivalents.
7. Do not globally replace words inside quoted material, historical notes, external titles, or other content where `PRD` is not naming the migrated artifact.
8. Leave the source `PRD.md` untouched.

## Complete feature-bundle migration

When the user asks to migrate both the PRD and its legacy issues:

1. Also load `../to-tasks/MIGRATING-FROM-ISSUES.md` through the `/to-tasks` skill.
2. Build one combined manifest of every target file before writing.
3. Include `SPEC.md`, `TASK-BANK.md`, every `task-NNN-*.md`, every `task-NNN-*-plan.md`, and an existing `IMPLEMENTATION-CONTEXT.md` in the preflight.
4. If any target collides, write nothing.
5. Once the complete target is safe, write the whole migrated bundle.
6. Carry an existing `IMPLEMENTATION-CONTEXT.md` forward without reinterpretation. Only rewrite links and structural references to the renamed planning artifacts.
7. Leave every legacy source file untouched.
