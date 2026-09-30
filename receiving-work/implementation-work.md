# Implementation work

# Context before plan

Read task-provided files and the smallest relevant project context before planning, respecting read limits and forbidden paths. Reference supplied context rather than repeating it.

After context is loaded, write a visible plan in the current session and execute it immediately. The plan should cover only applicable items:

- scope and ordered approach;
- likely touched files;
- expected checks or acceptance evidence;
- activated optional workflows such as Git or task-bank handling;
- reporting target and requested artifacts.

Do not add Git, task-bank, or other absent workflows merely to fill out the plan.

# Implementation

Follow project conventions and existing contracts. Keep changes limited to the assigned scope. Prefer cohesive, reviewable changes over unrelated cleanup.

Before editing, distinguish existing changes from task changes. Preserve pre-existing and newly appearing unrelated state; it does not block implementation. Report only overlaps whose ownership cannot be established safely. When commits are authorized, read `git-commits.md` before editing for baseline and task-only commit handling.

For complex code/scripts, show target files, ordered reviewable phases, per-phase verification, and final checks before coding. Applicable phases include contracts/skeleton, configuration/CLI, schema/input audit, bounded feasibility, core logic, aggregation/reporting, and orchestration. Implement one cohesive phase or function group at a time, split modules appropriately, and check each major phase before continuing.

# Checks and completion

Run the smallest checks that establish the expected result, plus required project checks. Do not claim success when checks fail, required artifacts are missing, or acceptance criteria remain incomplete.

If a fix is feasible within scope, make it and rerun the relevant check. If no safe in-scope path remains or an external decision is needed, report a blocker.

# Report contribution

Report `Checks` with performed commands/checks, pass/fail outcomes, and concise evidence; report `Changes` with material paths or behavior. Omit empty sections and `n/a` values.
