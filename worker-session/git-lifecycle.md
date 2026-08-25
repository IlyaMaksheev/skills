# Git lifecycle

# Ownership

Own the complete feature lifecycle: isolated worktree/branch, implementation history, synchronization, fast-forward integration, verification, and cleanup. The immediate parent should not need to perform routine Git cleanup.

Use the worker name as the branch name unless the prompt supplies another exact branch. Create a dedicated worktree from the latest target branch. Never overwrite, stash, reset, or clean another session's changes.

Follow explicit repository instructions, then a clearly consistent convention in relevant recent history; default to Conventional Commits when neither establishes one. Include the worker name on its own line in the commit message. Keep task changes cohesive. When task-bank handling is active, include its required update with the feature history.

When `Agent-docs lifecycle` is active, the supplied target is the mixed feature branch. Follow `/skill:agent-docs-lifecycle`: product commits contain persistent project paths, stable `.agent-docs/**` updates use separate path-pure `agent-docs:` commits, and a worker with no agent-doc change creates no such commit. Clean delivery to the mainline target remains outside an individual worker's routine integration.

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
3. Confirm the target branch still points to that commit and its canonical worktree has no unintended tracked changes.
4. Fast-forward integrate with `git merge --ff-only` from the canonical target worktree.
5. Release the lock immediately.
6. If the target advanced before integration, release the lock, rebase, rerun affected checks, and retry.

Default to at most three integration attempts unless the parent gives a different bound. If a safe shared lock is unavailable, the target worktree is dirty, conflicts cannot be resolved in scope, or bounded retries are exhausted, report a hard blocker. Do not bypass serialization.

# Verification and cleanup

After successful integration:

- verify the target points to the intended commit;
- inspect `git log --oneline --graph` for accidental merge commits;
- verify no intended tracked changes remain;
- remove the worker worktree when safe;
- delete the merged local worker branch with `git branch -d`;
- never force-delete an unmerged branch;
- report any cleanup item that could not safely be completed.

Run cleanup from outside the worktree being removed.

# Report contribution

Append only applicable plaintext details:

```text
Git:
- Commit: <hash>
- Target: <branch>
- Integration: fast-forward complete
- Cleanup: <worktree/branch result>
```

Add conflict or retry details only when they occurred. Never emit Git fields when this file was not loaded.
