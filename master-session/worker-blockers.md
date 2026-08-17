# Worker blocker handling

# Triage

Classify the blocker before acting:

- missing external input or decision;
- authority/type mismatch;
- conflicting requirements;
- shared-state or Git integration conflict;
- unavailable dependency/service;
- unsafe resource requirement;
- insufficient or contradictory investigation result.

A long-running job that still has a clear completion path is not a blocker.

# Response

Keep ownership with the original worker whenever possible:

1. Send the smallest clarification, permission, corrected input, or changed constraint needed.
2. Ask the worker to retry or finish its own cleanup.
3. Reassign to a correctly typed worker only when authority or scope was wrong.
4. Spawn a separate utility investigation only when isolated evidence is needed.
5. Ask the immediate parent/user only when an external decision is genuinely required.

For Git or task/issue-bank blockers, do not absorb routine execution into the master. Return the decision to the implementation worker so it can finish integration and cleanup. Never authorize a non-fast-forward merge, force deletion, destructive reset, or unrelated-state overwrite as a shortcut.

Report only the terminal resolution or unresolved hard blocker to this master's immediate parent.
