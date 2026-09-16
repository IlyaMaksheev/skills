# Scoped commits

## Protected state

Unrelated staged, unstaged, and untracked changes are protected state, not a reason to block an authorized commit. A scoped commit in the supplied worktree does not require creating a branch or worktree, rebasing, or integrating elsewhere.

Before editing, inspect the current branch, `HEAD`, status, staged and unstaged diffs, and relevant untracked content. Establish which changes predate the task and which paths or hunks belong to it. A filename list alone cannot establish ownership within an already-modified file.

Preserve foreign content and its staged/unstaged disposition. Leave newly appearing unrelated changes alone too. Reinspect owned paths before staging and committing; reconcile unexpected edits only when attribution remains clear. Block only the affected operation when attribution or preservation cannot be established. Never stash, reset, discard, or commit foreign changes to obtain a clean workspace.

## Commit procedure

1. Confirm commit authorization, destination branch, and attributable task changes. Complete the required checks. If another actor shares this worktree's index, serialize selection through verification; separate tool calls are not a concurrency boundary.
2. Select only owned paths or hunks. Stage explicit paths only when their entire diff belongs to the task; otherwise select attributable hunks. Avoid broad staging and `git commit -a`.
3. Inspect the exact proposed commit diff against `HEAD`. A normal commit includes the entire index, so inspecting only your staged paths is insufficient. When foreign changes are staged, use a path-limited commit (`git commit --only -- <paths>`) only for wholly owned file diffs, or prepare a task-only temporary index for hunk-level selection. If no safe selection is available, report the specific overlap.
4. Commit the inspected task-only content. After using a temporary index, reconcile only task hunks in the original index against the new `HEAD`, preserving foreign entries and their staging.
5. Inspect the resulting commit and remaining status/diffs. Confirm that the commit contains only task changes and that protected content and staging are preserved. Remaining unrelated dirt is an expected successful outcome.

Follow explicit repository commit conventions, then consistent relevant recent history; otherwise use Conventional Commits. Include the worker name on its own message line when an identity is supplied by the assignment or harness. Report the commit hash and branch. A commit does not imply integration or a remote push; perform those only when authorized.
