---
name: agent-docs-lifecycle
description: Establish separated Git history for `.agent-docs` artifacts when creating or modifying them, integrating worker changes, or delivering their associated feature.
---

# Agent-docs lifecycle

Keep one **mixed feature branch** for active work and construct a **product projection** for delivery. The mixed branch may interleave persistent project commits with ephemeral `agent-docs:` commits; the target receives the persistent commits only.

This skill governs Git state associated with `.agent-docs/**`. Merely reading, searching, or reviewing those artifacts does not activate it. Remote operations and retrospective cleanup of `.plans` or earlier history are outside this lifecycle.

## Establish the mixed branch

Before the first `.agent-docs` write in a Git repository:

1. Inspect repository instructions, status, current branch, worktrees, and relevant recent history. Preserve unrelated changes; use no automatic stash, reset, or clean.
2. Determine whether the current branch is an existing feature branch or the likely mainline target from ancestry, conventional target names, and history. Ask only when the evidence remains ambiguous.
3. Use an existing feature branch as the mixed branch. From a mainline target, create an ordinary feature branch named from the feature's lowercase kebab-case name unless the user supplied a name.
4. Confirm the intended write and branch switch are safe before creating `.agent-docs/<feature-name>/`.

Several feature directories may coexist on one mixed branch. Git is the source of branch and divergence evidence; create no lifecycle metadata artifact.

## Classify commits

Make stable changes promptly as path-pure commits. Transient claims, audit ownership, and incomplete edits remain uncommitted until resolved or reverted.

- An `agent-docs: <description>` commit changes only `.agent-docs/**`.
- Every other commit changes only persistent project paths.
- Persistent documentation uses the repository's normal documentation commit type.
- Agent-doc and product commits may be interleaved.
- Create an agent-doc commit only when an agent artifact actually changed.

Choose commit messages in this order: explicit repository instructions; a clearly consistent convention in relevant recent history; Conventional Commits as fallback. `agent-docs:` is the reserved ephemeral type under every convention.

Stage exact intended paths and verify the staged diff before committing. A policy-governed mixed commit must be split on the feature branch before delivery. The lifecycle neither scans nor rewrites history predating this policy.

## Compose workers

A delegated implementation worker receives all three fields when it handles a mixed branch:

```text
Git lifecycle: enabled
Target branch: <mixed-feature-branch>
Agent-docs lifecycle: enabled
```

Add `Task bank` and `Task artifact` only when task-state mutation is authorized. Workers branch and create worktrees from the mixed branch, commit product and agent-doc changes separately, and use the ordinary worker Git lifecycle to rebase, fast-forward integrate, verify, and clean their worktree and integrated branch. A worker that changes no agent artifact creates no `agent-docs:` commit.

The mixed feature branch is the workers' integration target. The mainline target is reserved for explicit clean delivery.

## Deliver the product projection

Begin delivery only on explicit human request and after concurrent feature work has settled. Reuse the primary checkout and its established development environment; worker isolation does not imply a delivery worktree.

1. Inspect status and preserve unrelated work. Proceed when branch switching and reconstruction are safe.
2. Infer the likely mainline target from ancestry, conventional target names, and history. Ask for confirmation when several candidates remain plausible.
3. Find the divergence with `git merge-base <target> <mixed-branch>`. This identifies history; it performs no merge. Require linear feature history and inspect the ordered commits after that base.
4. Classify every policy-governed commit by both subject and changed paths. The product projection contains each non-`agent-docs:` commit in order; each selected commit changes persistent project paths only.
5. Create a temporary delivery branch from the latest target in the primary checkout. Cherry-pick each selected product commit individually, preserving its subject, author, and order. Resolve ordinary product conflicts with the repository's normal Git workflow and rerun affected checks.
6. Run applicable validation and review the reconstructed product diff. Verify that delivered commits change persistent paths and the resulting tree consists exclusively of persistent project content.
7. Switch to the target and integrate the temporary delivery branch with `git merge --ff-only`. Verify the target history is linear and points to the validated result; if the target advanced, reconstruct on its latest head before retrying.
8. Remove the successful temporary delivery branch. Retain the mixed feature branch and report it with the target and delivered commits. The final checked-out branch is not a lifecycle requirement.

When reconstruction cannot safely complete, preserve the mixed branch and any useful conflict-resolution branch, return to a stable checkout, and report the concrete Git or validation evidence. Apply ordinary repository recovery rather than inventing agent-doc-specific repair.

## Completion

The lifecycle operation is complete when its current phase is checkable:

- artifact mutation: the stable `.agent-docs` change is in a path-pure `agent-docs:` commit on the mixed branch;
- worker integration: product and agent-doc commits are separate, fast-forwarded into the mixed branch, and the worker worktree and integrated branch are cleaned up;
- delivery: the target contains the validated product projection in linear history, while the retained mixed branch remains the home of `.agent-docs` history.
