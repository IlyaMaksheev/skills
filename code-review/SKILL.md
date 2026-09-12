---
name: code-review
description: Review a bounded code change through independent read-only Spec, Correctness, and Design reviewers. Use when a completed task, committed diff, branch, or integrated feature would benefit from evidence-backed review against its governing requirements, runtime behavior, and changed design.
---

# Code review

Orchestrate a read-only review of one selected change. The caller owns the review scope, adjudication, remediation, and final reporting. Three isolated read-only reviewers examine separate axes so one kind of evidence cannot mask another:

- **Spec**: does the selected change implement its governing requirements without omissions or added scope?
- **Correctness**: does changed behavior work across concrete execution and failure paths?
- **Design**: do structural choices introduced or materially altered by the change follow available repository guidance and avoid meaningful code smells?

The same procedure applies to an assigned change, an integrated feature, or a human-selected diff or branch. Any session may arrange review within its assignment and authority.

# Authority and composition

This skill supplies review procedure, not session authority or generic delegation mechanics.

- Load `/skill:receiving-work` for assignment authority and the applicable execution modules.
- Load `/skill:delegating-work` and its `multi-worker-coordination.md` before dispatching parallel axis reviewers.
- Give reviewers explicit read-only constraints. A reviewer owns its assigned axis and may delegate only narrower subtasks when delegation is worthwhile; it must not forward the entire axis unchanged.

All review work is read-only. Axis reviewers return evidence to their immediate parent. The caller checks that evidence, decides each finding's disposition, and handles corrections through its existing authority and workflow.

# Review module registry

`SKILL.md` is the entrypoint. Axis reviewers do not discover modules themselves. Put exactly one applicable module path in each review assignment.

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

The caller supplies the task, specification, or other governing artifact. Pipeline reviews use artifacts already held by the assigning session rather than rediscovering them through commit messages, issue trackers, or broad repository searches.

In direct mode, ask the human for an optional spec path when none was supplied. When no governing artifact exists, skip the Spec axis and record that it was unavailable. Correctness and Design remain applicable.

Use repository guidance already supplied or clearly applicable in the active repository context. Its absence is normal. Design review falls back to its smell baseline without requiring standards files or setup infrastructure.

## 3. Dispatch isolated axis reviewers

Launch applicable reviewers in parallel using the assignment contract in `../delegating-work/briefing-and-dispatch.md`. Give each reviewer:

- the instruction to load `/skill:receiving-work`;
- a bounded task, checkable expected result, and explicit read-only constraints forbidding project, dependency, Git, task-state, and environment mutations;
- exactly one review module path from the registry;
- the selected diff command or immutable diff input;
- the commit list when applicable;
- the governing artifact for Spec, or relevant repository guidance for Design;
- responsibility for completing the assigned axis and returning evidence to its immediate parent.

Keep all three reviewers anchored to the same selected change. They may read the minimum surrounding implementation needed to establish a finding in that change.

## 4. Consume and adjudicate

Wait for every dispatched reviewer to return a terminal report. Keep Spec, Correctness, and Design findings separate, including when two axes identify the same underlying problem.

For each finding, check its cited location, evidence, and impact. Reject unsupported claims. Resolve straightforward findings with the caller's existing context and leave genuinely ambiguous cases for caller judgement. Severity may inform this analysis, but it is not a mandatory field in reviewer output.

The caller decides whether accepted findings require correction, deferral, clarification, or no action. The review procedure does not modify files. A session may correct accepted findings within its authorized assignment or delegate bounded corrections. Prefer the original reachable implementation worker for related corrections; use a new worker when a materially different scope or unavailable session makes reuse unsuitable.

Rerun an affected axis when the correction materially changes what that axis evaluated. Use caller judgement rather than repeating review until no heuristic finding appears.

## 5. Complete in the governing workflow

Review is complete when:

- the selected boundary was validated and was non-empty;
- every applicable axis returned a completed report;
- reported findings were checked against their evidence;
- the caller decided the disposition of each established finding.

Then resume the governing workflow:

- a delegated session integrates the review into its assigned result and reports under `receiving-work` rules;
- a session with other assigned children continues applicable supervision through `delegating-work`;
- a direct session presents the scoped review result to the human.

When an axis identifies no issue, its reviewer states that no findings were identified for that axis in the selected change. Exact wording follows the existing worker reporting contract.
