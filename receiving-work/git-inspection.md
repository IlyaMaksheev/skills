# Read-only Git inspection

# Boundary

This file grants no Git mutation authority. Read-only examples: `git status`, `log`, `show`, `diff`, `grep`, `blame`, `ls-files`, `branch --show-current`, and `worktree list`.

Do not stage, commit, checkout, switch, merge, rebase, reset, clean, create/delete branches or worktrees, or otherwise change repository state.

Keep inspection within the requested evidence. If the expected result requires mutation outside the authority envelope, report an assignment mismatch in delegated mode or ask for authorization in direct mode.

# Report contribution

Report `Git inspection` findings needed by the expected result, with commit, path, or ref anchors.
