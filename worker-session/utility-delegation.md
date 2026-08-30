# Utility delegation

Use **research escalation**: keep one or two targeted fetches, searches, or known-file reads local; delegate when the task is already substantial or the investigation grows iterative, branching, broad, or context-heavy. Substantial work includes multi-source web research, open-ended discovery, foreign-codebase mapping, and broad repository or folder reconnaissance. Treat call count as guidance: scope and context growth decide the handoff.

Delegate other bounded read-only work when isolation materially protects the controlling context, such as monitoring loops or bounded performance analysis. Keep work local when it requires the controlling session's continuous judgment or is cheaper than the handoff.

A direct session or delegated implementation worker may spawn multiple utility children without activating master orchestration merely because of their count. Give each child a distinct bounded question, batch related routine work, avoid overlapping investigations, and stop when more research is unlikely to change the result. When escalating work already begun locally, pass the useful findings and open questions so the child does not repeat discovery.

# Resource check

Before spawning, consider runtime, CPU/process count, RAM, disk I/O, log growth, shared artifacts, and duplicate side effects. Match concurrent fan-out to genuine parallelism and available resources. Spawn only one resource-heavy utility job unless the controlling instruction explicitly approves parallel heavy work.

# Spawn contract

Use the same merged worker skill; never reference the removed utility skill.

Defaults:

- `mode: "fresh"`;
- `persistent: false`;
- `reportToSelf: true`;
- `cwd`: the current relevant repo/worktree or task directory;
- `thinkingLevel: "low"`;
- name: `<controlling-session-name>-sub-<purpose>`.

Explicit placement instructions override this default. Use `placement: "neovim-tab"`. If that placement reports an invalid or unreachable server, preserve every other spawn option and fall back to `niri-ghostty`. Use the tool error directly; do not inspect the environment or probe for another Neovim server.

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

The controlling implementation worker or direct session retains implementation, architecture, acceptance, and final-delivery ownership. Briefly disclose substantial delegation to the human in direct mode. After dispatch, wait for the utility child's authored report without elapsed-time or silence-driven pings; act only on its report, an actionable runtime event, or a human request. Then synthesize the result and read the returned relevant files or evidence before implementing. Repeat delegated searches only when a result is insufficient, contradictory, or blocked; if needed, send a correction or spawn one corrected bounded investigation.

# Report contribution

When useful, append:

```text
Delegation:
- <utility worker>: <result used by this task>
```

Do not reproduce the child's full report.
