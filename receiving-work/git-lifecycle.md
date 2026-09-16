# Git lifecycle

# Ownership

Own the complete feature lifecycle: isolated worktree/branch, implementation history, synchronization, fast-forward integration, verification, and cleanup. The immediate parent should not need to perform routine Git cleanup.

Resolve the worker's session name from the harness or explicit assignment metadata. Use that name as the branch name unless the prompt supplies another exact branch. If no usable identity is available, obtain a branch name before creating the worktree. Create a dedicated worktree from the latest target branch, or use the isolated worktree explicitly assigned by the parent. Use the canonical target worktree only for integration, preserving any existing foreign state there. A new worktree contains committed target state, not its uncommitted edits; resolve any task dependency on those edits explicitly.

Load `git-commits.md` before implementation; it owns protected-state handling and task-only commits. Keep task changes cohesive. When task-bank handling is active, include its required update with the feature history.

When `Agent-docs lifecycle` is active, the supplied target is the mixed feature branch. Follow `/skill:agent-docs-lifecycle`: product commits contain persistent project paths, stable `.agent-docs/**` updates use separate path-pure `agent-docs:` commits, and a worker with no agent-doc change creates no such commit. Clean delivery to the mainline target remains outside an individual worker's routine integration.

# Environment reuse

A new worktree does not carry untracked environments such as installed dependencies. Reuse a compatible existing project environment through the repository's supported mechanism before downloading or rebuilding it. Confirm compatibility from the relevant manifests and lockfiles; when the task changes them, the project requires isolation, or reuse is unavailable, use the project's lockfile-safe installation procedure. Keep another session's environment unchanged and report a blocker when neither reuse nor an authorized safe installation is available.

# Linear integration

History must remain linear:

- no merge commits;
- no non-fast-forward integration;
- no force pushes, forced resets, or force-deleting branches;
- no ordinary merge fallback after `--ff-only` fails.

Before integration:

1. Complete implementation and checks in the worker worktree.
2. Commit all intended task changes.
3. Rebase onto the latest target branch.
4. Resolve only in-scope conflicts carefully.
5. Rerun checks affected by the rebase.

# Concurrent workers

Serialize only the final target-branch update with the shared advisory lock:

```text
$(git rev-parse --git-common-dir)/pi-worker-integration.lock
```

Use `flock` or an equivalent OS advisory lock on that exact path so every worker coordinates through the same lock. If no safe locking mechanism is available, report a blocker. Keep implementation, rebase, and checks outside the lock.

Use this bounded optimistic flow:

1. Record the target commit used for the successful rebase/checks.
2. Acquire the shared integration lock.
3. Confirm the target branch still points to that commit. Inspect the canonical worktree's staged, unstaged, and untracked state against the paths changed by the incoming commits, including file/directory collisions. Unrelated dirt is permitted; preserve its content and staging. Defer integration if incoming changes overlap protected state or observed concurrent writes to the integration paths cannot be coordinated.
4. Fast-forward integrate with `git merge --ff-only --no-autostash` from the canonical target worktree. Honor Git's refusal if it cannot preserve local state; do not force the update or enable autostash.
5. Verify the integrated commit and preservation of protected state, then release the lock immediately.
6. If the target advanced before integration, release the lock, rebase, rerun affected checks, and retry.

Default to at most three integration attempts unless the parent gives a different bound. Dirty state alone is not a blocker. If a safe shared lock is unavailable, protected state would be affected, Git refuses the update, conflicts cannot be resolved in scope, or bounded retries are exhausted, retain the committed worker branch and report the specific integration obstacle. Report `blocked` when integration is required by the assignment; a committed result is `done` only when it satisfies the agreed deliverable. Do not bypass serialization.

# Verification and cleanup

After successful integration:

- verify the target points to the intended commit;
- inspect `git log --oneline --graph` for accidental merge commits;
- verify no intended task changes remain uncommitted; unrelated dirty state may remain;
- remove the worker worktree when safe;
- decide branch cleanup separately from worktree removal;
- delete a temporary merged worker branch with `git branch -d`;
- retain any branch whose requested role continues after worktree removal;
- keep unmerged branches and report any cleanup item that could not safely be completed.

Run cleanup from outside the worktree being removed.

# Report contribution

Append only applicable plaintext details:

```text
Git:
- Commit: <hash>
- Target: <branch>
- Integration: fast-forward complete | pending, with specific obstacle
- Cleanup: <worktree/branch result>
```

Add conflict or retry details only when they occurred. Never emit Git fields when this file was not loaded.
