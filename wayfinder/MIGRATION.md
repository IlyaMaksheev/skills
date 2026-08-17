# Migrate a Legacy Map

Load this workflow when `FORMAT.md` identifies missing current structures. Migration requires explicit user confirmation and ends with an active, unaudited map.

1. Report the missing structures and obtain confirmation.
2. Reread and preflight the complete migration set. For a map without a bank, map every legacy decision title, filename, ID, and blocker reference to one zero-padded bank ID before editing. Ask about ambiguous mappings. For a map with a bank, treat that bank as canonical.
3. Move legacy type, effective status, dependencies, and active claim ownership into the bank. Remove legacy `Type`, `Status`, `Blocked by`, `Claimed by`, and `Claimed at` metadata from decision files. This normalization is the explicit migration exception to resolved-file immutability.
4. Establish testable destination invariants already entailed by the destination and accepted scope. Route any reinterpretation of the destination into brainstorming.
5. Add `Closure audit: pending`. Rename the bank's `Blocked by` column to permanent `Depends on`, translate legacy links to bank IDs, preserve those edges, and set rows with unresolved dependencies to `blocked` while retaining terminal history.
6. For each accepted legacy decision, append a claim boundary only when it follows directly from the existing resolution. Preserve the resolution. Put an ambiguous or over-broad answer into revalidation and remove its gist.
7. Reconcile every gist, dependency, claim, scope entry, successor, and fog item under `FORMAT.md`.
8. Set the map to `active` with closure `pending`, then verify the complete result through **Coherent mutations** in `WORKFLOWS.md`.
9. Commit when safe and stop. The next `/skill:wayfinder <map-path>` resumes ordinary work or performs the fresh audit.
