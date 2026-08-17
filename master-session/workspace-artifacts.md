# Workspace artifacts

## Activation

Load only when the parent supplies `Artifact workspace: <path>` or explicitly requests bounded planning-artifact discovery. Spawn `cwd`, repository presence, and incidental files do not activate this module. A readable empty workspace or one without recognized artifacts is valid: use the assignment and other explicit inputs, and do not activate artifact-backed workflows.

## Discovery

1. Resolve the supplied directory without searching other workspaces.
2. List direct children; do not recursively read the tree.
3. Classify recognized names before opening files.
4. Select artifacts by assignment relevance, not presence.
5. Ignore unknown files unless explicitly supplied or linked by a selected artifact.

| Pattern | Role | Read policy |
|---|---|---|
| `WAYFINDER.md` | Low-resolution decision provenance and readiness | Read fully only when the assignment concerns its effort. |
| `decision-NNN-*.md` | Detailed decision history and evidence | Never bulk-read; open one resolved decision only for a concrete ambiguity, conflict, or explicit link. |
| `SPEC.md` | Implementation contract | Read fully when relevant. |
| `TASK-BANK.md` | Persisted scheduling graph and state | Read fully only for requested graph-backed work; then load `task-bank-orchestration.md`. |
| `IMPLEMENTATION-CONTEXT.md` | Shared codebase-specific findings | Read fully when relevant; it informs but does not override requirements. |
| `task-NNN-*-plan.md` | Task-specific execution guidance | Read only with its matching selected task. |
| `task-NNN-*.md`, excluding plans | Executable task scope | Read only selected frontier or explicitly named tasks. |

Recognized artifacts are optional. Do not require Wayfinder, a spec, a task bank, or implementation context for generic orchestration.

## Wayfinder use

For work derived from a map, use `WAYFINDER.md` for destination, notes, boundary, readiness, and provenance; use `SPEC.md` as the implementation contract. Do not reconstruct implementation requirements from decision files. If the relevant map is `active`, treat downstream implementation as unstable unless its `Notes` or the parent explicitly authorizes execution within the selected scope. A `ready` map permits normal downstream validation but does not itself activate implementation.

Do not import `out-of-scope` or `superseded` decisions. If a current artifact conflicts with a resolved decision, report the exact conflict rather than choosing silently.

## Authority and coherence

- Project instructions govern execution.
- The selected task defines bounded deliverables and acceptance criteria; `SPEC.md` defines feature requirements and settled implementation decisions. A conflict between them is a blocker.
- `TASK-BANK.md` owns persisted scheduling state under its existing convention.
- A task plan is subordinate to its task and spec.
- `IMPLEMENTATION-CONTEXT.md` supplies technical facts and pointers, not requirements.
- Wayfinder artifacts preserve provenance; they are not the default worker interface after spec creation.

Validate only relationships needed by the assignment: selected paths exist, selected task references resolve, blockers are known, and explicitly required parents are coherent. Artifact absence alone is not an error.

## Worker projection

Pass the smallest sufficient set. For a bank-backed implementation worker, normally provide the selected task, relevant `SPEC.md`, optional `IMPLEMENTATION-CONTEXT.md`, matching task plan when present, and structured task-bank fields. Add a specific resolved decision only when its detail is necessary. Never pass the whole workspace, every task, every plan, or every decision by default.
