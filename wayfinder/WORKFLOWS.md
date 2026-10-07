# Wayfinder Workflows

Use the branch selected by the invocation. `FORMAT.md` remains authoritative for states, schemas, identity, and claims.

## Chart a map

1. **Establish facts.** Inspect available repository context before asking factual questions.
2. **Name the destination and visible invariants.** Use `/skill:brainstorm` to settle the destination and its entailed testable conditions rather than route decisions.
3. **Map breadth-first.** Propose distinct precise questions visible now and coarse in-scope fog beyond them. Keep implementation choices out of invariants and investigative phases within their problem question.
4. **Take the no-map exit.** When the route is clear and fits one session, create nothing. Ask whether the user wants ordinary brainstorming, an appropriate downstream workflow, or to stop.
5. **Approve the chart.** Present the proposed map and question set. Apply `FORMAT.md`'s **Decision creation approval** gate to the initial decisions.
6. **Establish and create the route.** In Git, follow `/skill:agent-docs-lifecycle` before the first write; use the active feature branch or create the derived feature branch from the inferred mainline target. Preflight the directory and every approved path, preserving any existing map. Write the active map with closure `pending`, then only approved decision files. Add complete permanent dependencies and set each row to `open` or `blocked`; retain fog and unapproved distinct proposals under `Not yet specified`.
7. **Commit the chart** as a path-pure `agent-docs:` commit when Git can do so safely.
8. **Complete the chart.** Report the created map, its open frontier, and the applicable Wayfinder commands for subsequent work. The charting invocation ends with the committed route.

## Work a map or named decision

1. Read `WAYFINDER.md`. When `FORMAT.md` identifies legacy structure, read [MIGRATION.md](./MIGRATION.md) and migrate only after explicit confirmation.
2. Reread immediately before selection. Another session's closure claim pauses frontier work.
3. When the invocation discovers or receives changed evidence used by a current decision, return the map to `active` and closure to `pending` before other work, then follow **Revalidate and propagate** where needed. Otherwise, report a map already at `ready` with closure `passed` and offer its applicable downstream handoff.
4. Select work:
   - A supplied current decision must be `open` or already `claimed` by this session; resume an owned investigation rather than replacing it.
   - For bare `needs-review`, report its pending review-creation proposal and request approval.
   - For `needs-review → NNN`, follow the controlling review. Work it when `open` or owned by this session; otherwise report its blockers or owner.
   - For `superseded → NNN`, follow the bank lineage to the current successor and load the history needed to understand it.
   - Without a supplied decision, choose the lowest-ID `open` row.
5. When no frontier exists, read [AUDIT.md](./AUDIT.md) if its candidate gate can pass. Otherwise report every state preventing closure: blocked or claimed decisions, reviews, fog, or unsupported prerequisites.
6. Claim an open selected row through `FORMAT.md`, or retain this session's existing claim; reread and verify ownership.
7. Perform **Decision preflight**.
8. Perform **Pursue the answer** until `FORMAT.md`'s completion criterion holds. A paused investigation ends with progress, not resolution.
9. When the answer is established, perform **Refresh before acceptance**.
10. Apply **Resolve and advance the frontier**, including propagation, only after the refreshed answer meets the completion criterion.
11. Stop after settling one decision requiring human evaluation. Independent research may run in parallel. A fresh invocation audits after the final ordinary resolution.

## Decision preflight

Preflight is the bounded context check for one claimed decision, not a closure audit.

1. Read the selected question against the map's destination, invariants, notes, complete bank, accepted gists, route context, fog, and scope.
2. Load every current transitive dependency and required review or successor lineage in full.
3. Compare every compact `Route context` entry with the selected question. Load a source decision in full only when its reusable conclusion plausibly affects the question; inspect additional accepted decisions when their gists expose overlap.
4. Identify the previous decisions that materially preserve, narrow, or already answer the question. Add a permanent dependency when changing a reused conclusion could invalidate or materially alter the eventual answer.
5. Carry the effective question and materially applied sources into its resolution. A context conflict follows **Revalidate and propagate**; a scope conflict follows the existing out-of-scope flow.
6. Retain the applied context and a snapshot of the compact route context through resolution.

Preflight is complete only when the remaining question can be handled without silently reopening or contradicting a current accepted conclusion.

## Pursue the answer

1. Keep the preflight's effective question and completion criterion in view. When accepted prior decisions already establish the answer, derive it by reference rather than reopening a settled choice.
2. Choose the method needed now, using the bank type as the starting point: **Delegate research** for missing facts, `/skill:brainstorm` for human choices, and **Work a prototype** for questions needing a concrete artifact. Combine or revisit methods within the same decision; factual evidence does not grant agent-made product judgment or execution authority.
3. Assess each result against the effective question. Verify findings, test credible competing explanations where relevant, and identify the next evidence-producing step when the answer remains unsupported. A completed worker assignment or diagnostic pass is not decision completion. Record findings and remaining work in `Progress`, then repeat the appropriate method for useful authorized work.
4. When the next step needs permission, propose its bounded scope in the current conversation and wait for approval, retaining the claim. A missing permission, unavailable evidence, or exhausted safe path is a concrete blocker to report, not an answer to invent or a reason to manufacture a new ticket. Use `FORMAT.md`'s creation gate only for genuinely distinct questions.

## Delegate research

Read and follow `/skill:delegating-work`, including its assignment and dispatch rules.

For each bounded factual investigation within an owned decision:

1. Ensure the parent owns the bank claim and has completed **Decision preflight** for that claim.
2. Assign a bounded read-only investigation through `delegating-work`, preferring a reachable worker with related context. For a new session, use the current project as `cwd` and immediate-parent reporting.
3. Supply the map path, decision path, bounded factual question, applicable prior conclusions, constraints, and expected evidence. Keep decision-bank, context-classification, product-judgment, and Git mutation authority in the parent.
4. Let the worker select applicable research or repository-inspection modules.
5. Verify the returned evidence and record progress in the parent, then return to **Pursue the answer**. The parent owns completion assessment, resolution, and all Wayfinder mutations.

Independent research decisions may run in parallel. When evidence exposes a human choice serving the current question, discuss it in this session or obtain scoped approval for the needed prototype or diagnostic. Propose a separate decision only through `FORMAT.md`'s creation gate.

## Work a prototype

The claimed decision's session is the prototype session, not a dispatcher. Keep artifact construction and human evaluation in this session.

1. Carry the preflight's effective question, applicable prior conclusions, constraints, and decision-owned artifact directory into `/skill:prototype`. Follow its approval gate before building; charting a `prototype` row alone is not approval to build it.
2. Build, verify, and present the artifact through that skill. Keep the claim while the human evaluates it. Revisions and further observations answering the same question reuse the directory and claim; propose a materially different question through `FORMAT.md`'s creation gate.
3. Use `/skill:brainstorm` when discussion of the artifact is needed. Record the human's explicit verdict in `RESULT.md`; revisions or an undecided response keep evaluation pending. A verdict on an intermediate artifact may still leave the effective question unanswered.
4. Return to **Pursue the answer** and assess the verdict against the effective question before refresh or resolution. Apply `FORMAT.md`'s prototype evidence requirements; if refreshed context invalidates an evaluated answer, resume evaluation and obtain a revised verdict before acceptance.

## Refresh before acceptance

Reread `WAYFINDER.md` immediately before recording the resolution and compare its compact route context with the preflight snapshot. Load only a new or changed source whose conclusion plausibly affects the answer. When fresh context materially changes the effective question or answer, retain the claim and resume the applicable resolution workflow from that conflict. Refresh is complete when the answer fits both the preflight context and every relevant concurrent addition.

## Resolve and advance the frontier

1. Write `## Context analysis` naming only previous decisions materially applied during preflight and how each preserved, narrowed, or answered the question; record the required no-context statement when none did.
2. Put the detailed answer and important reasoning under `## Resolution`.
3. Add the complete claim boundary required by `FORMAT.md`; include `## Evidence` when useful.
4. Expose every material `Leaves open` item through `FORMAT.md`'s claim-boundary and creation rules. If it is still needed to answer the effective question, return to **Pursue the answer** unless the user explicitly accepted a narrower boundary. Put excluded limitations in `Out of scope`.
5. Classify each material conclusion by reach. Keep local conclusions in the resolution. Promote every conclusion that meets `FORMAT.md`'s `Route context` criteria, giving targeted conclusions a semantic applicability scope and reserving `Route-wide` for conclusions that apply to every decision.
6. Compare the result with the destination, invariants, applied route context, current resolutions, and reverse dependency graph. When it challenges a current answer, include **Revalidate and propagate** in the same coherent update.
7. Exact-edit its bank row from `claimed` to `resolved` and clear both claim fields.
8. Append one linked title and bounded one-line gist under `Decisions so far`.
9. Create only approved distinct decision files, then add their rows with complete permanent dependencies and correct `open` or `blocked` states. Preserve unapproved proposals under `Not yet specified`. Lazy reconciliation leaves other unresolved questions for their own preflights rather than scanning or closing them here.
10. Remove fog or pending proposals from `Not yet specified` only after their approved decisions exist or the user explicitly settles their disposition.
11. Move work beyond the destination to `out-of-scope`, clear its claim, remove its accepted gist and sourced route context, add a linked reason under `Out of scope`, and propagate the lost dependency.
12. Open a `blocked` row only when every retained dependency is exactly `resolved`.
13. Set the map to `active` and closure to `pending` for every substantive route change.
14. Apply existing-map changes through targeted edits, verify the coherent result, and commit the stable artifact update under `/skill:agent-docs-lifecycle` when safe.

## Revalidate and propagate

A later fact triggers revalidation when it challenges a current answer, assumption, claim boundary, evidence currency, or permitted use. Preserve the resolved file; the bank determines currentness.

### Open a review path

1. Reread the map and identify the challenged decision, changed fact, and every transitive descendant in the reverse dependency graph. Add semantic edges exposed by the changed fact.
2. Coordinate before mutation when another session owns an affected row or closure. Reuse an existing unresolved controlling review or pending proposal for the same question; one historical decision has one active path.
3. When no controlling review exists, propose it through `FORMAT.md`'s creation gate. Its question links the prior decision and changed fact and identifies the answer, assumptions, reusable findings, and possible confirmation, narrowing, or replacement under review.
4. Quarantine the challenged resolution and every accepted transitive descendant even while approval is pending: remove their gists and sourced route context, set them to `needs-review → NNN` when a controlling review exists or bare `needs-review` while creation awaits approval. Record the changed fact and affected IDs in the existing review's `Progress` or, while creation awaits approval, in the pending proposal under `Not yet specified`. Block affected open work and preserve every dependency edge. Coordinate a pause for affected claimed work before changing its state.
5. For an approved new review, allocate a higher ID, preflight its path, and create the review file and row with every permanent dependency it awaits. Set it to `open` only when all dependencies are current `resolved` rows; otherwise use `blocked`. Point quarantined rows to `needs-review → NNN` and remove the matching pending proposal. Restore an unchanged descendant only after review shows that its answer, assumptions, boundary, gist, route context, and permitted use fit the current upstream boundary.
6. Set the map to `active` and closure to `pending`, then use **Coherent mutations** for the pending or approved update.

### Resolve a review path

1. State what the successor preserves, changes, and discards. Its claim boundary becomes the sole current boundary.
2. Pursue the full review question in the controlling review, including further investigation after prerequisite findings. When it supplies the new answer, set the historical decision to `superseded → NNN` and accept the successor. A genuinely distinct successor requires `FORMAT.md`'s creation approval before creation or repointing; a prerequisite fact alone does not require another ticket.
3. Reconsider quarantined descendants in topological order:
   - Restore an unchanged answer only after rewiring historical dependencies to current successor IDs and confirming its boundary, gist, context analysis, and promoted route context still fit.
   - Propose one successor path through the creation gate when a distinct new answer is required; keep the descendant quarantined while approval is pending.
   - Move work beyond the destination to `out-of-scope` and reconcile its descendants.
4. Re-evaluate blocked rows after each current answer; open only those whose permanent dependencies are exactly `resolved`.
5. Continue successor chains from the current resolution with increasing IDs, no cycles, and one active lineage.
6. Keep the map active with closure pending until every review and descendant is reconciled and a later fresh audit passes.

## Coherent mutations

Use this optimistic transaction for propagation, successors, migrations, and failed-audit findings:

1. Reread and preflight the complete affected set, including every new path and exact map edit.
2. Coordinate when another session owns an affected decision or closure.
3. Verify explicit approval covers every proposed new decision; create only those approved, collision-free files. Pending updates use existing rows and `Not yet specified` without allocating IDs.
4. Apply one targeted map edit containing rows, state transitions, dependency rewiring, gist and route-context changes, fog or scope changes, and audit invalidation.
5. Reread and verify the complete resulting state.
6. On conflict, remove only files created by this operation that remain unreferenced and are certainly safe to remove; otherwise report them and stop. Reread before retrying.
7. Commit the verified stable result as a path-pure `agent-docs:` commit. Claims and transient `auditing` states remain uncommitted.

## Completion report

Only an invocation that resolved a decision or completed closure ends with the applicable continuation footer:

```text
Decision: `decision-NNN-<slug>`
Next command: `/skill:wayfinder ./.agent-docs/<feature-name>/WAYFINDER.md`
```

List each resolved decision by exact filename stem, in completion order and separated by `, `. Omit `Decision` when closure resolved no decision. A failed audit resumes through the map. A passed audit may offer `/skill:to-spec <map-path>` when the destination calls for a spec. Omit inapplicable lines and placeholders.
