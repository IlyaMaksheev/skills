# Local Wayfinder Format

## Planning directory

For a new map, derive a concise lowercase kebab-case feature name, state `./.agent-docs/<feature-name>/`, and inspect it before writing. Reuse an existing directory only when it clearly represents the same effort.

Place every artifact directly in that directory.

## Map

`WAYFINDER.md` is the canonical low-resolution index and workflow state:

```markdown
# Wayfinder: <effort name>

Status: active
Closure audit: pending

## Destination

<What reaching the end of this map means.>

## Destination invariants

- <One testable destination-level condition.>

## Notes

<Domain, standing constraints, relevant skills, and explicit execution overrides.>

## Decision bank

| ID | Decision | Type | Status | Depends on | Claimed by | Claimed at |
|---|---|---|---|---|---|---|
| 001 | [<decision title>](decision-001-<slug>.md) | brainstorm | open | None | — | — |

## Decisions so far

- [<resolved decision title>](decision-NNN-<slug>.md) — <one-line bounded gist>

## Not yet specified

<In-scope fog that cannot yet be expressed as a precise question, or `None`.>

## Out of scope

<Excluded work, with a linked decision and reason when applicable, or `None`.>
```

Map statuses:

- `active` — closure has not passed for the current route
- `ready` — closure has passed for the current route

Closure-audit states:

- `pending` — the current route has not passed closure
- `auditing — <owner>, <ISO-8601 UTC timestamp>` — the named session owns the audit
- `passed` — the current route passed closure

Only `Status: ready` with `Closure audit: passed` represents completion. Every substantive change to the destination, invariants, route-constraining notes, bank, accepted decisions, fog, or scope sets the map to `active` and closure to `pending`. When an invocation discovers or receives changed evidence used by a current decision, invalidate closure before other work and open revalidation where needed. Evidence invalidation is discovery-driven; external evidence between invocations remains outside Wayfinder's observation. Formatting and link repairs preserve closure.

Write each destination invariant as one testable destination-level condition. Add an invariant directly only when the destination, accepted scope, or standing constraints already entail it. A change that broadens, narrows, or reinterprets the destination requires a brainstorm decision. Keep implementation choices in the bank and conditions not yet expressible in `Not yet specified`.

The decision bank owns all workflow metadata. `Decisions so far` is the narrative index of current accepted results, not workflow state.

## Decision bank

Allowed types:

- `brainstorm`
- `research`

Allowed status forms:

- `blocked` — at least one permanent dependency is not a current `resolved` decision
- `open` — every dependency is current and the decision is available to claim
- `claimed` — a session owns the decision
- `resolved` — the resolution and claim boundary are current and accepted
- `needs-review → NNN` — the resolution is quarantined while the linked higher-ID decision controls its review; it has no accepted current answer or `Decisions so far` gist
- `out-of-scope` — the decision sits beyond the destination
- `superseded → NNN` — the immutable historical resolution was replaced by the linked successor

Use `—` for empty claim fields. Only `claimed` rows fill both claim fields.

`Depends on` is `None` or a comma-separated list of zero-padded bank IDs, such as `001, 002`. Add an edge when the dependent question cannot yet be responsibly resolved or when its eventual answer's validity relies on the upstream answer. Every edge remains a continuing-validity edge after resolution, so use bank order—not a convenience-only edge—for preferred scheduling between independent decisions. Every ID must identify an existing row; retain the IDs after the dependent opens or resolves. A row may be `open`, `claimed`, or `resolved` only when every dependency row is exactly `resolved`; `out-of-scope`, `needs-review`, and historical `superseded` rows cannot satisfy a dependency. Keep the graph acyclic.

A `needs-review` link names the single active review controlling whether the quarantined resolution can return to the route or needs its own successor; several quarantined decisions may point to that review. A `superseded` link names the actual successor. The linked ID must be higher than the historical ID. Each historical decision has one active review path, and later revalidation starts from the current successor rather than branching from an older decision.

The frontier is every `open` row. Automatic selection takes the lowest ID.

The bank is the sole authority for selection, accepted state, dependency traversal, and readiness. Scan sibling decision files only during explicit migration or consistency repair.

## Decision ticket

```markdown
# <Decision title>

## Question

<One precise question sized for one agent session.>
```

When resolved, append:

```markdown
## Resolution

<Answer and important reasoning.>

## Claim boundary

- **Applies to:** <Population, artifact or revision, environment, time range, semantic interpretation, or other covered scope.>
- **Assumes:** <Conditions that must remain true.>
- **Leaves open:** <Material destination-relevant conclusions not established, or `None`.>

## Evidence

<Relevant source, report, or research links; omit the section when empty.>
```

The claim boundary states how far the answer may safely be used. Express it in structured plain language rather than one validity label. Use `Assumes` for external or domain conditions and to explain the semantic meaning of dependency assumptions. When another decision establishes or controls an assumption, also add that decision to permanent `Depends on`; the edge carries propagation. Route every material item under `Leaves open` into a new decision or `Not yet specified` in the same coherent update; move excluded limitations to `Out of scope`. A `Decisions so far` gist must fit entirely inside this boundary.

Evidence remains optional when the reasoning is self-contained. Put the answer's important factual basis in the resolution; research decisions normally cite the sources or artifacts they inspected.

Decision files contain no type, status, dependency, claim, or successor metadata. After resolution, preserve their substantive contents. Later facts revalidate them through new decisions rather than rewriting accepted history.

## Links and identity

The filename is persistent identity, but human-facing prose uses the linked title:

```markdown
[Choose the storage model](decision-001-choose-storage-model.md)
```

Use relative links. Human-facing prose names each item through its linked title; structured bank fields use IDs.

## Cooperative claims

Local Markdown does not guarantee atomic assignment. Use optimistic exact-state edits:

1. Reread `WAYFINDER.md` immediately before selection.
2. Replace only the selected row, changing `open` to `claimed` and filling `Claimed by` and `Claimed at`.
3. Reread `WAYFINDER.md`; continue only if the claim is yours.
4. On edit failure or conflicting ownership, reread and select again.
5. Treat existing ownership as authoritative.
6. Release or reassign a stale claim only with explicit user confirmation.

Claim closure similarly by exact-editing `Closure audit: pending` to `Closure audit: auditing — <owner>, <timestamp>`, then reread and verify ownership. Another session seeing `auditing` stops. Release a stale audit claim only with explicit user confirmation.

After initial creation, mutate `WAYFINDER.md` with targeted exact-text edits. Keep cooperative claim state in the map.

## Creation safety and numbering

- When the target `WAYFINDER.md` already exists, preserve it and ask whether to work it or choose another feature name.
- Preflight the map and every initial decision path. A collision pauses creation before any write.
- Allocate each ID once, monotonically above the highest bank ID, including terminal rows.
- Create new decision files before adding their bank rows. Add each row with its complete `Depends on` value and correct initial `blocked` or `open` status.
- A substantive revalidation decision links the prior decision and changed evidence in its question and receives a higher ID.
- Explicit work-mode invocation authorizes state updates to that map and its decisions, not replacement of unrelated artifacts.

A map requires explicit migration before work when it lacks a decision bank or any current required structure: `Destination invariants`, `Closure audit`, `Depends on`, current status forms, or claim boundaries on accepted decisions. Follow [MIGRATION.md](./MIGRATION.md); it owns the normalization procedure and the sole exception to substantive resolved-file immutability.

## Git persistence

When Git is configured, follow `/skill:agent-docs-lifecycle`: establish the mixed feature branch before the first artifact write, keep stable artifact updates in path-pure `agent-docs:` commits, and preserve unrelated changes.

- commit the initial map and decisions after charting;
- commit each completed resolution together with its coherent map, fog, dependency, propagation, and successor updates;
- commit an approved migration;
- commit a failed audit together with the decisions or fog it surfaced;
- commit a passed audit together with the readiness transition;
- follow the project's proven commit-message convention, using Conventional Commits as fallback and the reserved `agent-docs:` type for these artifacts;
- stage only the Wayfinder planning files changed by this operation.

Leave unrelated changes unstaged. When repository state makes a safe scoped commit uncertain, stop and ask. Stable commits exclude decision claims and the transient `auditing` state.
