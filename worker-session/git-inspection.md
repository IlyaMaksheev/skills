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

Keep inspection within the requested evidence. If the expected result requires mutation outside the authority envelope, report an assignment mismatch in delegated mode or ask for authorization in direct mode.

# Report contribution

When relevant, append:

```text
Git inspection:
- <finding with commit, path, or ref anchor>
```

Include only findings needed by the expected result.
