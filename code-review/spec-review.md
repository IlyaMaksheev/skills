# Spec review

Review the selected change only against the caller-supplied governing task or specification. Own this bounded read-only review and return evidence to the immediate parent. Use `delegating-work` only when a narrower subtask warrants delegation.

# Method

1. Read the governing artifact and identify every requirement applicable to the selected change.
2. Compare those requirements with behavior added, altered, or omitted by the diff.
3. Look for:
   - requirements that are missing or only partially implemented;
   - behavior that conflicts with a requirement;
   - behavior added without support from the governing scope;
   - behavior that appears to implement a requirement but does so incorrectly.
4. Read the minimum surrounding implementation needed to establish how a changed behavior relates to a requirement.
5. Report only findings anchored to the selected change. Preserve distinct requirements as distinct evidence even when one correction may resolve several findings.

# Finding evidence

Each finding includes:

- **Finding**: the concrete divergence from the governing artifact.
- **Location**: the changed file and lines or diff hunk.
- **Evidence**: the quoted requirement and the changed behavior that diverges from it.
- **Impact**: the observable requirement or acceptance outcome affected.
- **Suggested direction**: optional, when a correction direction follows clearly from the evidence.

When essential information prevents evaluation of an applicable requirement, identify the missing evidence and why it matters as a blocked evaluation rather than a defect.

# Completion

The review is complete when every applicable requirement has been compared with the selected change, including missing behavior and added scope, and every reported finding carries the required evidence.

When complete without findings, state that no Spec findings were identified in the selected change. Keep the report concise, evidence-backed, and free of summaries of correctly implemented requirements.
