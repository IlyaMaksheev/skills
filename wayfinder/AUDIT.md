# Closure Audit

Load this workflow only when `WORKFLOWS.md` reaches closure. The audit tries to falsify the assembled route; ticket exhaustion alone cannot establish readiness.

## Candidate gate

After a fresh map reread, begin only when:

- the map is `active` and closure is `pending`;
- no bank row is `open`, `blocked`, `claimed`, or `needs-review`;
- every dependency of a current `resolved` row points directly to a current `resolved` row;
- every superseded chain reaches a current resolved successor;
- all dependency and successor references exist, increase where required, and form acyclic graphs;
- `Decisions so far` contains exactly the current resolved decisions, with every gist inside its claim boundary;
- every current resolved decision has the required context analysis;
- every `Route context` row points to a current resolved source, stays inside its claim boundary, and contains a reusable conclusion with a bounded applicability scope;
- `Not yet specified` is empty (`None.` is acceptable);
- every material prototype or manual prerequisite has been handled;
- the destination and its invariants remain valid.

Report every failing condition and return to the applicable workflow. A passing gate authorizes investigation, not readiness.

## Claim and investigate

1. Exact-edit closure from `pending` to `auditing — <owner>, <timestamp>`, then reread. Continue when the claim is yours.
2. Build an audit manifest containing every current `resolved` row and the decision file, context analysis, claim boundary, evidence, promoted route context, and relevant lineage it requires. Map gists and route-context rows provide navigation rather than audit evidence. Complete the audit only after every manifest row has been inspected in full and included in global synthesis.
3. Inspect the manifest directly when it fits one reliable context. Otherwise read `/skill:master-session` and delegate bounded inspection passes to fresh utility workers. Give each worker explicit decision IDs, files, lenses, and factual checks. Require a compact report of claims, assumptions, dependencies, evidence currency, and material findings. Workers inspect; the parent owns Wayfinder mutations, product judgment, and closure.
4. Verify that bounded passes cover every manifest row. Resolve overlap or conflicting reports and inspect source material where verification requires it. The parent traces invariants and performs the final cross-route compatibility and composition judgment. Local agreement is not global closure.
5. When full coverage and one global synthesis cannot be completed in the claimed invocation, return closure to `pending`, report the limitation, and stop. Partial passes cannot establish readiness.
6. Trace every destination invariant to a current accepted route and support. Every accepted decision must support an invariant or a necessary route element.
7. Attempt falsification through every lens:
   - **Coverage:** Find material destination concerns absent from the invariants, decisions, and fog.
   - **Compatibility:** Compare definitions, populations, time boundaries, contracts, artifact and representation identities, versions, and execution models.
   - **Claims and evidence:** Keep each decision and gist inside its claim boundary. Distinguish mechanical, bounded, population, and semantic validity where applicable; verify that support is current and permitted. Artifact presence is not execution evidence. Missing evidence is unproven and becomes a finding when the destination requires that proof.
   - **Propagation:** Trace transitive effects through permanent dependencies and successor chains. Check semantic reliance as well as declared edges.
   - **Context continuity:** Find reusable conclusions omitted from `Route context`, local detail promoted without need, stale or duplicate entries, materially applicable context absent from downstream context analysis, and downstream answers that silently contradict promoted context.
   - **Composition:** Assemble one end-to-end route, including material prerequisites, handoffs, resources, execution limits, stopping behavior, manual ownership, recovery or resume behavior, and intermediate artifact identities.
   - **Boundary integrity:** Verify that excluded work is not an implicit prerequisite and prohibited evidence or artifacts do not enter accepted conclusions.
8. Treat a finding as material when leaving it unresolved could change invariant satisfaction, invalidate or materially narrow an accepted decision or gist, break end-to-end feasibility, or introduce an implicit prerequisite, prohibited dependency, or scope violation. Improvements and post-destination optimizations remain outside closure.

## Finish

### Material finding

A material finding fails the current audit.

1. Route a precise finding into an ordinary decision or review path.
2. For a material problem whose resolution question is still imprecise, add actionable fog stating the contradiction or omission, its destination impact, and what must become clearer.
3. Add an omitted invariant directly only when the current destination already entails it; route a changed destination meaning into brainstorming.
4. Return closure to `pending`, keep the map `active`, and apply the complete finding set through **Coherent mutations** in `WORKFLOWS.md`.
5. Commit when safe and stop. A later fresh invocation resolves the new work and audits the repaired route.

### No material finding

1. Reread the map and verify that the claimed candidate state is unchanged.
2. Reverify each artifact, revision, or external evidence identity on which the audit relied when the map does not guarantee its currentness.
3. Exact-edit map status to `ready` and the owned audit state to `passed`.
4. Reread, commit when safe, report the completed map, and stop.

Persist only the current binary audit result. Any route repair requires a later fresh audit.
