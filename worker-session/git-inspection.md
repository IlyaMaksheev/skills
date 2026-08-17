# Read-only Git inspection

# Boundary

This file grants no Git mutation authority. Use read-only operations such as:

- `git status`;
- `git log`;
- `git show`;
- `git diff`;
- `git grep`;
- `git blame`;
- `git ls-files`;
- `git branch --show-current`;
- `git worktree list`.

Do not stage, commit, checkout, switch, merge, rebase, reset, clean, create/delete branches or worktrees, or otherwise change repository state.

Finding a Git repository does not justify broader inspection than the task requires and never activates `git-lifecycle.md`.

If an implementation worker later needs Git delivery, the parent must have supplied the structured Git lifecycle fields. If a utility worker discovers that mutation is required, report a worker-type mismatch or blocker.

# Report contribution

When relevant, append:

```text
Git inspection:
- <finding with commit, path, or ref anchor>
```

Include only findings needed by the expected result.
