# Wayfinder Workflows

Use the branch selected by the invocation. `FORMAT.md` remains authoritative for states, schemas, identity, and claims.

## Chart a map

1. **Establish facts.** Inspect available repository context before asking factual questions.
2. **Name the destination and visible invariants.** Use `/skill:brainstorm` to settle the destination and its entailed testable conditions rather than route decisions.
3. **Map breadth-first.** Surface precise decisions visible now and coarse in-scope fog beyond them. Keep implementation choices out of invariants. The test is precision: create a decision when its question can be stated now, even if it cannot be answered; keep the rest as fog.
4. **Take the no-map exit.** When the route is clear and fits one session, create nothing. Ask whether the user wants ordinary brainstorming, an appropriate downstream workflow, or to stop.
5. **Choose and preflight the directory.** Follow `FORMAT.md` and preserve any existing map.
6. **Create the route.** Write the active map with closure `pending`, then the currently precise decision files. Add complete permanent dependencies and set each row to `open` or `blocked`. Keep imprecise in-scope uncertainty under `Not yet specified`.
7. **Commit the chart** when Git can do so safely.
8. **Delegate open research** through **Delegate research**. Leave blocked research in the bank.
9. **Stop after charting.** A later invocation works the frontier.

## Work a map or named decision

1. Read `WAYFINDER.md`. When `FORMAT.md` identifies legacy structure, read [MIGRATION.md](./MIGRATION.md) and migrate only after explicit confirmation.
2. Reread immediately before selection. Another session's closure claim pauses frontier work.
3. When the invocation discovers or receives changed evidence used by a current decision, return the map to `active` and closure to `pending` before other work, then follow **Revalidate and propagate** where needed. Otherwise, report a map already at `ready` with closure `passed` and offer its applicable downstream handoff.
4. Select work:
   - A supplied current decision must be `open`; otherwise report its state.
   - For `needs-review → NNN`, follow the controlling review. Work it when `open`; otherwise report its blockers or owner.
   - For `superseded → NNN`, follow the bank lineage to the current successor and load the history needed to understand it.
   - Without a supplied decision, choose the lowest-ID `open` row.
5. When no frontier exists, read [AUDIT.md](./AUDIT.md) if its candidate gate can pass. Otherwise report every state preventing closure: blocked or claimed decisions, reviews, fog, or unsupported prerequisites.
6. Claim the selected row through `FORMAT.md`, then reread and verify ownership.
7. Zoom into the selected decision and every related item required by its question. Revalidation includes the prior resolution and boundary, changed evidence, dependencies, affected decisions, and successor lineage.
8. Resolve by type:
   - `brainstorm`: use `/skill:brainstorm`.
   - `research`: use **Delegate research**. Factual research supplies evidence rather than agent-made product judgment.
9. Apply **Resolve and advance the frontier**, including propagation.
10. Stop after one brainstorm decision. Independent research may run in parallel. A fresh invocation audits after the final ordinary resolution.

## Delegate research

Read and follow `/skill:master-session`, including its worker-prompt and spawn rules.

For each independent open research decision:

1. Claim the bank row in the parent session.
2. Spawn a fresh `utility` worker with the current project as `cwd` and reporting to the parent.
3. Supply the map path, decision path, bounded factual question, constraints, and expected evidence. Keep issue-bank and Git mutation authority in the parent.
4. Let the worker select applicable research or repository-inspection modules.
5. Verify the returned evidence, then record the resolution and all Wayfinder mutations in the parent.

Independent research decisions may run in parallel. When evidence exposes a human choice, resolve the factual question and create a blocked or open `brainstorm` decision for that choice.

## Resolve and advance the frontier

1. Put the detailed answer and important reasoning under `## Resolution`.
2. Add the complete claim boundary required by `FORMAT.md`; include `## Evidence` when useful.
3. Route every material `Leaves open` item into a new decision or `Not yet specified`. Put excluded limitations in `Out of scope`. The route, rather than a resolved file alone, must expose every material uncertainty.
4. Compare the result with the destination, invariants, current resolutions, and reverse dependency graph. When it challenges a current answer, include **Revalidate and propagate** in the same coherent update.
5. Exact-edit its bank row from `claimed` to `resolved` and clear both claim fields.
6. Append one linked title and bounded one-line gist under `Decisions so far`.
7. Create newly visible decision files, then add their rows with complete permanent dependencies and correct `open` or `blocked` states.
8. Graduate newly precise fog into decisions and remove that material from `Not yet specified`.
9. Move work beyond the destination to `out-of-scope`, clear its claim, remove its accepted gist, add a linked reason under `Out of scope`, and propagate the lost dependency.
10. Open a `blocked` row only when every retained dependency is exactly `resolved`.
11. Set the map to `active` and closure to `pending` for every substantive route change.
12. Apply existing-map changes through targeted edits, verify the coherent result, and commit when safe.

## Revalidate and propagate

A later fact triggers revalidation when it challenges a current answer, assumption, claim boundary, evidence currency, or permitted use. Preserve the resolved file; the bank determines currentness.

### Open a review path

1. Reread the map and identify the challenged decision, changed fact, and every transitive descendant in the reverse dependency graph. Add semantic edges exposed by the changed fact.
2. Coordinate before mutation when another session owns an affected row or closure. Merge a new fact into the existing unclaimed review path; one historical decision has one active path.
3. Allocate a higher ID and preflight a controlling review. Its question links the prior decision and changed fact and identifies the answer, assumptions, reusable findings, and possible confirmation, narrowing, or replacement under review.
4. Create the review file and bank row with every permanent dependency it awaits. Set it to `open` only when all dependencies are current `resolved` rows; otherwise use `blocked`.
5. Conservatively quarantine the challenged resolution and every accepted transitive descendant: remove their gists and set each to `needs-review → NNN`, naming its controlling review. Block affected open work and preserve every dependency edge. Restore an unchanged descendant only after review shows that its answer, assumptions, boundary, gist, and permitted use fit the current upstream boundary.
6. Set the map to `active` and closure to `pending`, then use **Coherent mutations**.

### Resolve a review path

1. State what the successor preserves, changes, and discards. Its claim boundary becomes the sole current boundary.
2. When the controlling review supplies the new answer, set the historical decision to `superseded → NNN` and accept the successor. When it supplies only a prerequisite fact, create the precise successor and repoint `needs-review` to it.
3. Reconsider quarantined descendants in topological order:
   - Restore an unchanged answer only after rewiring historical dependencies to current successor IDs and confirming its boundary and gist still fit.
   - Create one successor path when a new answer is required.
   - Move work beyond the destination to `out-of-scope` and reconcile its descendants.
4. Re-evaluate blocked rows after each current answer; open only those whose permanent dependencies are exactly `resolved`.
5. Continue successor chains from the current resolution with increasing IDs, no cycles, and one active lineage.
6. Keep the map active with closure pending until every review and descendant is reconciled and a later fresh audit passes.

## Coherent mutations

Use this optimistic transaction for propagation, successors, migrations, and failed-audit findings:

1. Reread and preflight the complete affected set, including every new path and exact map edit.
2. Coordinate when another session owns an affected decision or closure.
3. Create all collision-free new decision files.
4. Apply one targeted map edit containing rows, state transitions, dependency rewiring, gist changes, fog or scope changes, and audit invalidation.
5. Reread and verify the complete resulting state.
6. On conflict, remove only files created by this operation that remain unreferenced and are certainly safe to remove; otherwise report them and stop. Reread before retrying.
7. Commit the verified stable result. Claims and transient `auditing` states remain uncommitted.

## Completion report

Only an invocation that resolved a decision or completed closure ends with the applicable continuation footer:

```text
Decision: `decision-NNN-<slug>`
Next command: `/skill:wayfinder ./.plans/<feature-name>/WAYFINDER.md`
```

List each resolved decision by exact filename stem, in completion order and separated by `, `. Omit `Decision` when closure resolved no decision. A failed audit resumes through the map. A passed audit may offer `/skill:to-spec <map-path>` when the destination calls for a spec. Omit inapplicable lines and placeholders.
