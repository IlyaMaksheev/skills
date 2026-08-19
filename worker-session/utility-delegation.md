# Utility delegation

Delegate when isolation materially protects implementation context, such as context-heavy research, foreign-codebase mapping, monitoring loops, or bounded performance analysis.

Keep work local when it requires the controlling session's continuous judgment or is cheaper than the handoff. Batch related routine work into one utility assignment.

# Resource check

Before spawning, consider runtime, CPU/process count, RAM, disk I/O, log growth, shared artifacts, and duplicate side effects. Spawn only one resource-heavy utility job unless the controlling instruction explicitly approves parallel heavy work.

# Spawn contract

Use the same merged worker skill; never reference the removed utility skill.

Defaults:

- `mode: "fresh"`;
- `persistent: false`;
- `reportToSelf: true`;
- `cwd`: the current relevant repo/worktree or task directory;
- `thinkingLevel: "low"`;
- name: `<controlling-session-name>-sub-<purpose>`.

Explicit placement instructions override this default. With non-empty inherited `$NVIM`, use `placement: "neovim-tab"`; with missing or empty `$NVIM`, use `niri-ghostty`. If the tab launch reports an invalid or unreachable inherited server, preserve every other spawn option and fall back to `niri-ghostty`. Use the tool error directly; do not probe for or discover another Neovim server.

The sparse plaintext prompt must include:

```text
First read and follow: /home/korvin/.pi/agent/skills/worker-session/SKILL.md
Worker name: <same as utility session name>
Worker type: utility
Parent name: <controlling session name>
Task:
- <exact bounded routine task>

Expected result:
- <acceptance/output returned only to the immediate parent>
```

Add only relevant positive sections: useful context, input files, search hints, constraints, resource limits, or approved artifact paths. Do not add Git lifecycle or task-bank mutation authority.

# Controlling-session ownership

The controlling implementation worker or direct session retains implementation, architecture, acceptance, and final-delivery ownership. After the utility report, read the returned relevant files or evidence before implementing. Do not repeat the delegated search unless the result is insufficient, contradictory, or blocked; if needed, send a correction or spawn one corrected bounded investigation.

# Report contribution

When useful, append:

```text
Delegation:
- <utility worker>: <result used by this task>
```

Do not reproduce the child's full report.
