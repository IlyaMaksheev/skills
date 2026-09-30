# Temporary artifacts

# Writable locations

Write artifacts only within locations authorized by the assignment or direct human request. This module grants no implicit write permission. If operational files are necessary but no writable location is authorized, obtain permission before creating them.

For disposable files, prefer an explicitly approved `/tmp/pi-workers/<session-name>/`; resolve the name from the harness or assignment and create the directory before use. Artifact permission does not authorize source/product edits, dependency changes, Git mutation, or task-status updates. Project artifacts require permission covering their location and purpose.

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

Report `Artifacts` with retained or requested paths and their purpose; omit deleted temporary files and `Artifacts: n/a`.
