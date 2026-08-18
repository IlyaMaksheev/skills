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

Maintain the delegation boundary: return the resolution to the original worker unless its authority or assigned scope cannot contain it.

1. Send the smallest clarification, permission, corrected input, or changed constraint needed.
2. Ask the worker to retry or finish its own cleanup.
3. Reassign to a correctly typed worker only when authority or scope was wrong.
4. Spawn a separate utility investigation only when isolated evidence is needed.
5. Ask the immediate parent/user only when an external decision is genuinely required.

For Git or task-bank blockers, return the decision to the implementation worker so it can finish integration and cleanup. Preserve repository and unrelated state: never authorize a non-fast-forward merge, force deletion, destructive reset, or unrelated-state overwrite as a shortcut.

Blocker handling is complete when the original worker resumes with sufficient authority and input, the work is reassigned to a correctly typed worker, or an unresolved external decision is reported to the immediate parent. Report only that terminal resolution or unresolved hard blocker.
