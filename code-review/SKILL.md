---
name: code-review
description: Review a bounded code change through independent Spec, Correctness, and Design utility reviewers. Use when a completed task, committed diff, branch, or integrated feature would benefit from evidence-backed review against its governing requirements, runtime behavior, and changed design.
---

# Code review

Orchestrate a read-only review of one selected change. The caller owns the review scope, adjudication, remediation, and final reporting. Three isolated utility reviewers examine separate axes so one kind of evidence cannot mask another:

- **Spec**: does the selected change implement its governing requirements without omissions or added scope?
- **Correctness**: does changed behavior work across concrete execution and failure paths?
- **Design**: do structural choices introduced or materially altered by the change follow available repository guidance and avoid meaningful code smells?

The same procedure applies at different scopes. An implementation worker may review its assigned change. A master may review an integrated feature or another meaningful bounded change. A direct human-guided session may review a selected diff or branch.

# Authority and composition

This skill supplies review procedure, not session authority or generic delegation mechanics.

- In a master session, retain `master-session` as the governing contract. Load `multi-worker-coordination.md` before dispatching the parallel axis reviewers.
- In a worker session, retain `worker-session` as the governing contract. An implementation worker or direct session loads `utility-delegation.md` before dispatching axis reviewers.
- When neither session contract is active, first read `/home/korvin/.pi/agent/skills/worker-session/SKILL.md` and operate in direct mode.
- A utility worker executes only its assigned axis. Its authority does not permit invoking this orchestration skill or spawning sessions.

All review work is read-only. Axis reviewers return evidence to their immediate parent. The caller checks that evidence, decides each finding's disposition, and handles corrections through its existing authority and workflow.

# Review module registry

`SKILL.md` is the entrypoint. Axis reviewers do not discover modules themselves. Put exactly one applicable module path in each utility assignment.

| File | Purpose and exact load condition |
|---|---|
| `spec-review.md` | Compare the selected change with the caller-supplied governing task or specification. Load when a governing artifact is available. |
| `correctness-review.md` | Trace behavior changed by the selected diff through concrete execution and failure paths. Load for every review. |
| `design-review.md` | Evaluate changed design against available repository guidance and the smell baseline. Load for every review. |

# Process

## 1. Select the change

Establish one explicit, bounded review target before dispatch:

- For task-local review, use the task's known before and after revisions, commit range, or exact diff command.
- For integrated feature review, use the feature branch point and integrated feature head.
- For direct review, use the fixed point supplied by the human. Ask for it when absent.

For a branch-style comparison, capture `git diff <fixed-point>...HEAD` and `git log <fixed-point>..HEAD --oneline`. Confirm each selected revision resolves and the diff is non-empty before spawning reviewers.

When `/skill:agent-docs-lifecycle` governs a mixed feature branch, select the product projection: review the ordered non-`agent-docs:` commits and persistent-path diff. `.agent-docs` artifacts may remain governing Spec inputs, but their textual changes are outside the delivered product diff. Inspect their workflow consistency separately only when requested.

Check whether staged or working-tree changes fall outside the selected boundary. State that mismatch before review. Include uncommitted changes only when the caller explicitly selects a command or snapshot that contains them. Give every axis reviewer the same diff command or immutable review input.

## 2. Select governing inputs

The caller supplies the task, specification, or other governing artifact. Pipeline reviews use artifacts already held by the worker or master rather than rediscovering them through commit messages, issue trackers, or broad repository searches.

In direct mode, ask the human for an optional spec path when none was supplied. When no governing artifact exists, skip the Spec axis and record that it was unavailable. Correctness and Design remain applicable.

Use repository guidance already supplied or clearly applicable in the active repository context. Its absence is normal. Design review falls back to its smell baseline without requiring standards files or setup infrastructure.

## 3. Dispatch isolated axis reviewers

Launch applicable reviewers in parallel using the sparse utility-worker prompt required by the governing session contract. Give each reviewer:

- the path to `/home/korvin/.pi/agent/skills/worker-session/SKILL.md`;
- a unique worker name, utility type, immediate parent, bounded task, and checkable expected result;
- exactly one review module path from the registry;
- the selected diff command or immutable diff input;
- the commit list when applicable;
- the governing artifact for Spec, or relevant repository guidance for Design;
- the instruction to perform the assigned review directly within utility authority.

Keep all three reviewers anchored to the same selected change. They may read the minimum surrounding implementation needed to establish a finding in that change.

## 4. Consume and adjudicate

Wait for every dispatched reviewer to return a terminal report. Keep Spec, Correctness, and Design findings separate, including when two axes identify the same underlying problem.

For each finding, check its cited location, evidence, and impact. Reject unsupported claims. Resolve straightforward findings with the caller's existing context and leave genuinely ambiguous cases for caller judgement. Severity may inform this analysis, but it is not a mandatory field in reviewer output.

The caller decides whether accepted findings require correction, deferral, clarification, or no action. The review procedure does not modify files. An implementation worker may correct accepted findings within its assignment. A master may delegate corrections. Choose between the original implementation worker and a fresh worker based on change complexity, whether the implementation approach is being preserved, and session availability.

Rerun an affected axis when the correction materially changes what that axis evaluated. Use caller judgement rather than repeating review until no heuristic finding appears.

## 5. Complete in the governing workflow

Review is complete when:

- the selected boundary was validated and was non-empty;
- every applicable axis returned a completed report;
- reported findings were checked against their evidence;
- the caller decided the disposition of each established finding.

Then resume the governing workflow:

- an implementation worker completes its assigned work and sends its normal result, without narrating internal review investigations;
- a master continues orchestration and reports only under `master-session` rules;
- a direct session presents the scoped review result to the human.

When an axis identifies no issue, its reviewer states that no findings were identified for that axis in the selected change. Exact wording follows the existing worker reporting contract.
