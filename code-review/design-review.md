# Design review

Review structural choices introduced or materially altered by the selected diff. Own this bounded read-only review and return evidence to the immediate parent. Use `delegating-work` only when a narrower subtask warrants delegation.

Apply clearly relevant repository guidance when the caller supplies it or it is already available in the active repository context. Its absence is normal. Use the smell baseline below in every Design review. Repository guidance takes precedence when it deliberately endorses a choice the baseline might otherwise question.

Treat every smell as a heuristic. Establish a concrete maintenance, comprehension, or change cost before reporting it. A named smell is not itself proof that refactoring is warranted. Keep suggested directions proportional to the selected change and skip concerns already decided mechanically by formatter, linter, or typechecker configuration.

# Smell baseline

- **Mysterious Name**: a changed name obscures what a value, function, or type represents. Consider a name that exposes the role; difficulty naming it may reveal a muddled responsibility.
- **Duplicated Code**: the change introduces repeated logic whose copies are likely to evolve together. Consider sharing the stable concept when doing so reduces future coordinated edits rather than merely removing similar lines.
- **Feature Envy**: changed behavior depends more on another module's data or decisions than on its own responsibility. Consider moving behavior toward the knowledge it uses or exposing a focused operation there.
- **Data Clumps**: the change repeatedly moves a related group of values together and their relationship carries domain meaning. Consider representing that relationship explicitly when it improves invariants or communication.
- **Primitive Obsession**: a changed primitive stands in for a domain concept with behavior or constraints that callers must repeatedly remember. Consider a focused type when it centralizes meaningful rules.
- **Repeated Switches**: the change repeats branching over the same distinction in several places, creating coordinated edit points. Consider centralizing the decision or moving behavior behind the varying concept.
- **Shotgun Surgery**: one conceptual change requires scattered edits because the relevant responsibility is dispersed. Consider gathering the changing knowledge behind a focused module or interface.
- **Divergent Change**: the modified module now changes for several unrelated reasons, making its responsibility harder to explain. Consider separating responsibilities where they evolve independently.
- **Speculative Generality**: the change adds abstraction, parameters, or extension points without a current requirement or demonstrated use. Consider the simplest structure that serves the selected scope.
- **Message Chains**: changed code navigates through a sequence of collaborators and becomes coupled to their structure. Consider placing a focused operation at the boundary that owns the navigation.
- **Middle Man**: a changed abstraction mostly forwards calls without adding a stable boundary, policy, or simplification. Consider using the underlying collaborator directly when the layer provides no leverage.
- **Refused Bequest**: changed inheritance forces an implementation to ignore or neutralize behavior it does not meaningfully support. Consider composition or a narrower contract that represents the actual relationship.

# Method

1. Read the selected diff and identify structural choices introduced or materially altered by it.
2. Evaluate those choices against applicable repository guidance and the smell baseline.
3. Read the minimum surrounding implementation needed to establish the cost of a changed design choice.
4. Report a finding only when the evidence shows a meaningful cost in the selected change. State heuristic findings as design judgement, not hard violations. A cited repository rule may establish a hard violation when its wording supports that conclusion.

# Finding evidence

Each finding includes:

- **Finding**: the repository-guidance breach or named smell and the concrete design problem.
- **Location**: the changed file and lines or diff hunk.
- **Evidence**: the applicable guidance or smell, the changed structure, and the demonstrated cost.
- **Impact**: the maintenance, comprehension, or future-change consequence.
- **Suggested direction**: optional and proportional, not a mandatory refactoring prescription.

When missing information prevents evaluation of a materially changed design choice, identify the missing evidence and why it matters as a blocked evaluation rather than a defect.

# Completion

The review is complete when structural choices introduced or materially altered by the selected change have been evaluated against applicable repository guidance and the smell baseline, and every reported finding carries the required evidence.

When complete without findings, state that no Design findings were identified in the selected change. Keep the report concise and omit praise, unchanged-code summaries, and unsupported design preferences.
