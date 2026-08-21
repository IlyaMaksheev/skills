# Correctness review

Review runtime behavior introduced or materially changed by the selected diff. Execute directly as a utility worker and return evidence to the immediate parent.

# Method

1. Identify materially changed behavior in the selected diff.
2. Trace its inputs, state transitions, outputs, and failure handling through concrete execution paths.
3. Examine assumptions where changed behavior crosses an interface, state boundary, or error boundary.
4. Use relevant tests as evidence while evaluating the behavior itself. Passing tests do not establish correctness outside what they exercise.
5. Deepen the investigation where the change presents a plausible defect with a concrete trigger and consequence.
6. Read the minimum surrounding implementation, interface, caller, or test needed to establish a finding in the selected change.

A correctness finding describes an actual failing path. General suspicion, hypothetical fragility without a trigger, and unrelated pre-existing problems do not establish findings.

# Finding evidence

Each finding includes:

- **Finding**: the concrete incorrect behavior.
- **Location**: the changed file and lines or diff hunk.
- **Evidence**: the triggering conditions, execution path, and relevant changed code.
- **Impact**: the resulting incorrect state, output, failure, or externally visible consequence.
- **Suggested direction**: optional, when a correction direction follows clearly from the evidence.

When missing information prevents evaluation of a materially changed path, identify the missing evidence and why it matters as a blocked evaluation rather than a defect.

# Completion

The review is complete when materially changed behavior has been considered through its normal and failure paths, deeper investigation has covered every plausible defect surfaced by that pass, and every reported finding carries the required evidence.

When complete without findings, state that no Correctness findings were identified in the selected change. Keep the report concise and omit praise, unchanged-code summaries, and unsupported possibilities.
