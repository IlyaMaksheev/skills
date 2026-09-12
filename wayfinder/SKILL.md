---
name: wayfinder
description: Map and resolve decisions for an effort too large or uncertain to plan in one session.
disable-model-invocation: true
---

# Wayfinder

Wayfinder turns a loose effort into an audited route of decisions. Use it to discover what must be settled before downstream work begins, not to implement that work. `Notes` may explicitly authorize execution inside a particular effort.

A route starts from a named **destination** and its testable invariants. Its **frontier** contains precise questions available now; less precise in-scope uncertainty remains **fog** until it can become a decision. The map is the route index and workflow authority: its compact **route context** exposes reusable conclusions from previous decisions so each selected question can preflight against them without loading the whole history. Decision files hold detailed answers.

Map and decision files live flat in `./.agent-docs/<feature-name>/`; prototype evidence lives in a decision-owned subdirectory described in [FORMAT.md](./FORMAT.md). Before creating or modifying them in Git, load and follow `/skill:agent-docs-lifecycle`; read-only map inspection does not activate that lifecycle.

- `WAYFINDER.md` — destination, route index, and canonical workflow state
- `decision-NNN-<slug>.md` — one precise question and its resolution
- later artifacts such as `SPEC.md` and task files may coexist beside them

Decision tickets are not implementation tasks. Reserve `task-NNN-*` for downstream tracer-bullet work.

Resolve choices through `/skill:brainstorm`, facts through delegated research, and questions needing a concrete artifact through `/skill:prototype`. A prototype decision is a HITL session: its owning Wayfinder session builds and evaluates the artifact with the human.

## Invocation

Use Pi skill-command syntax in instructions and handoffs:

```text
/skill:wayfinder <loose idea>
/skill:wayfinder ./.agent-docs/<feature-name>/WAYFINDER.md
/skill:wayfinder ./.agent-docs/<feature-name>/decision-NNN-<slug>.md
```

- A loose idea charts a new map.
- A map path works its frontier. When ordinary work is exhausted, a fresh invocation performs closure.
- A decision path works that decision and finds its sibling map. Historical decisions route through the bank's current review or successor lineage.

Read [FORMAT.md](./FORMAT.md), then follow the matching branch in [WORKFLOWS.md](./WORKFLOWS.md). Those files are authoritative for schema and procedure.

## Completion

A map is complete only when a fresh closure audit finds one coherent current route covering the destination and every invariant. `ready` attests to that route, not to unknown facts outside the audit.

Wayfinder ends at the cleared destination. Invoke downstream skills only when the user requests them. When the destination calls for a spec, offer:

```text
/skill:to-spec ./.agent-docs/<feature-name>/WAYFINDER.md
```
