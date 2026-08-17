# Long-running jobs

# Transition from normal execution

Pause before beginning another blocking call. If a process is already running unexpectedly, determine whether it can safely continue, be interrupted, or be relaunched without duplicating side effects. Do not blindly launch a second copy.

Load `temporary-artifacts.md` when logs, PID files, or helper scripts are needed. Load `resource-intensive-work.md` separately when CPU, memory, I/O, or concurrency may be substantial. An implementation worker may load `utility-delegation.md` when monitoring would occupy its context unnecessarily.

# Launch

Do not run long-lived code as a foreground/blocking tool call.

- launch with `nohup`, an equivalent background mechanism, or the project's approved runner;
- redirect stdout and stderr to a bounded log path;
- record the PID in a PID file;
- record enough invocation metadata to avoid duplicate launches;
- use only approved artifact paths and resource bounds.

Unless the expected result explicitly requests launch-only handoff, remain responsible for monitoring until the process reaches a terminal outcome.

# Monitoring

Use bounded short checks:

- inspect the PID with `ps` or `kill -0`;
- prefer a compact structured progress/status file;
- otherwise inspect a small tail such as 20 lines or fewer;
- capture elapsed time and latest useful heartbeat;
- use bounded sleeps between checks.

Do not use `tail -f`, `wait <pid>`, an unbounded foreground command, or full-log reads/pastes. Do not send parent messages merely because the process is still running.

On failure, decide whether an in-scope fix and safe retry exist. Retry only when duplicate effects are controlled. A running process with a clear completion path is not a blocker.

# Completion and cleanup

Confirm the terminal exit state and requested artifacts. Remove stale PID files and disposable helpers when safe. Preserve requested or diagnostically necessary logs and report their paths. Follow `temporary-artifacts.md` for remaining cleanup.

# Report contribution

Append only relevant terminal information:

```text
Long job:
- Result: <completed or failed outcome>
- Runtime: <concise duration>
- Artifacts: <only retained paths>
```

Do not report a nonterminal `running` status as the final result unless the task explicitly requested launch-only handoff.
