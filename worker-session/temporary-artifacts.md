# Temporary artifacts

# Writable locations

A utility worker may implicitly create operational artifacts only under:

```text
/tmp/pi-workers/<worker-name>/
```

Create that worker-specific directory before use. Any other utility write location must be explicitly supplied by the immediate parent as an approved artifact path. Such approval does not permit source/product edits, dependency changes, Git mutation, or issue-status updates.

Implementation workers may write task-authorized project artifacts within their implementation scope. Prefer the worker-specific `/tmp` directory for disposable operational files unless the project or parent requires another location.

# Safety

- use unique, descriptive paths under the worker directory;
- do not overwrite pre-existing files outside owned paths;
- do not follow an unexpected symlink into an unapproved location;
- keep logs and caches bounded;
- record PID and invocation metadata for launched processes;
- do not use broad destructive cleanup commands.

# Lifecycle

Delete disposable helpers, stale PID files, and unneeded intermediate data when safe. Retain artifacts required by the expected result or needed to diagnose a terminal failure. Never delete another session's artifacts.

# Report contribution

Append only retained or requested artifacts:

```text
Artifacts:
- <path>: <purpose>
```

Do not list deleted temporary files or emit `Artifacts: n/a`.
