# Implementation work

# Context before plan

Read the task-provided files and the smallest relevant project context before writing the plan. Respect file-read limits and forbidden paths. Do not duplicate context already supplied by files.

After context is loaded, write a visible plan in the current session and execute it immediately. The plan should cover only applicable items:

- scope and ordered approach;
- likely touched files;
- expected checks or acceptance evidence;
- activated optional workflows such as Git or task-bank handling;
- reporting target and requested artifacts.

Do not add Git, task-bank, or other absent workflows merely to fill out the plan.

# Implementation

Follow project conventions and existing contracts. Keep changes limited to the assigned scope. Prefer cohesive, reviewable changes over unrelated cleanup.

When other agents share the working directory, preserve their changes and commit only attributable task changes. Stage explicit paths or hunks, inspect the staged diff, and leave unrelated tracked and untracked files in place. If changes overlap so attribution cannot be established safely, report the overlap instead of rearranging another agent's work.

For complex code or script work, make the implementation decomposition visible before coding. Include target files, ordered chunks, verification after major chunks, and final checks or execution. Build in reviewable phases such as contracts/skeleton, configuration or CLI, schema/input audit, bounded feasibility, core logic, aggregation/reporting, and orchestration when those phases apply.

Build non-trivial scripts and large features in reviewable phases. Implement one cohesive phase or function group at a time, prefer appropriately split modules over a monolith, and check each major phase before continuing.

# Checks and completion

Run the smallest checks that establish the expected result, plus required project checks. Do not claim success when checks fail, required artifacts are missing, or acceptance criteria remain incomplete.

If a fix is feasible within scope, make it and rerun the relevant check. If no safe in-scope path remains or an external decision is needed, report a blocker.

# Report contribution

When relevant, append a plaintext section such as:

```text
Checks:
- <command or check>: passed | failed, with concise evidence

Changes:
- <important changed path or behavior>
```

Include only performed checks and material changes. Do not add empty sections or `n/a` values.
