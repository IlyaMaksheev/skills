# Worker blocker handling

# Triage

Classify the blocker before acting:

- missing external input or decision;
- assignment/authority mismatch;
- conflicting requirements;
- shared-state or Git integration conflict;
- unavailable dependency/service;
- unsafe resource requirement;
- insufficient or contradictory investigation result.

A long-running job that still has a clear completion path is not a blocker.

# Response

Maintain the delegation boundary: return the resolution to the original worker unless its authority or assigned scope cannot contain it.

1. Send the smallest clarification, authorized permission, corrected input, or changed constraint; ask the worker to retry or finish cleanup.
2. Reassign only when scope, availability, or capability makes reuse unsuitable, within your authority. Use `briefing-and-dispatch.md` for follow-up or reassignment.
3. Delegate narrower read-only investigation only when isolated evidence warrants the handoff.
4. Ask the immediate parent/user when an external decision is genuinely required.

For Git or task-bank blockers, return the decision to the implementation worker so it can finish integration and cleanup. Preserve repository and unrelated state: never authorize a non-fast-forward merge, force deletion, destructive reset, or unrelated-state overwrite as a shortcut.

Blocker handling is complete when the original worker resumes with sufficient authority and input, the work is reassigned with explicit scope and permissions, or an unresolved external decision is reported to the immediate parent. Report only that terminal resolution or unresolved hard blocker.
