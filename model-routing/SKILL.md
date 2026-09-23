---
name: model-routing
description: Select a model and thinking level when creating a Pi worker session.
---

# Model routing

Match the model and thinking level to the assignment's execution and judgment demands. Optimize for useful completed work: quality, latency, verification needs, and coordination overhead. Apply budget constraints when the user supplies them.

## Scope

This skill selects configuration for **new sessions**; it does not authorize changing existing sessions or account defaults. Honor explicit user model and thinking choices.

Routing is separate from deciding whether to delegate. Use [delegating-work](../delegating-work/SKILL.md) for delegation judgment, worker reuse, authority, and dispatch. Reuse skill contents already available in context, including complete contents supplied by the user or harness. Read a referenced skill only when its contents are missing or there is reason to believe they changed; retrieve only a missing section when that suffices.

## Choose the model

**Sol Low is the default for general execution.** Choose another model and effort directly when they better fit the assignment; no prior failure is required.

| Model | Best fit | Boundaries and tradeoffs |
| --- | --- | --- |
| **Sol** (`gpt-6-sol`) | General execution: implementation, multi-file investigation, debugging, review, planning, and orchestration. | Usually Low. Increase effort for competing hypotheses or interacting constraints; task length and file count alone do not establish that need. |
| **Luna** (`gpt-6-luna`) | Focused, verifiable work: bounded discovery, extraction, deterministic transformations, known checks, and localized implementation or debugging with explicit requirements. | Usually Low. Consider Medium or High when the task is well specified but reasoning-intensive. Favor Sol or Astra when success depends on discovering hidden constraints, resolving ambiguity, or making cross-system design decisions. |
| **Astra** (`gpt-6-astra`) | Stronger judgment: architecture, ambiguity, difficult diagnosis, conflicting evidence, complex synthesis, and work requiring continuing design decisions. | Low or Medium according to the reasoning demands below. Identify the concrete benefit over Sol; novelty, prestige, or automatic final approval is not a reason. |
| **Terra** (`gpt-5.6-terra`) | Optional alternative for a recurring bounded workload with demonstrated reliability, latency, or efficiency advantages. | No prescribed role in this workflow. Use when requested or supported by observed results. |

Route by the decisions the worker must make, not by whether the task is read-only or involves code. For Luna assignments, specify the scope, acceptance criteria, and independent verification. A settled plan supports a Luna handoff when the remaining decisions are local and its integration assumptions can be checked.

## Choose thinking

Choose effort prospectively from the assignment, independently of model tier. Use previous results when available; no trial at a lower level is required.

- **Low:** clear objectives, bounded decisions, ordinary implementation, investigation, review, and tool use. The normal Sol and Luna setting; also useful for focused Astra judgments.
- **Medium:** significant comparison, competing hypotheses, interacting constraints, or substantial synthesis. Suitable for difficult Sol analysis and complex Astra planning or investigation.
- **High:** deeply coupled reasoning or difficult failure-mode analysis where further deliberation is likely to improve the result. Use a task-specific reason rather than task size or importance alone.
- **Higher supported settings:** choose them when explicitly requested or when task-specific evidence supports a benefit over High. Verify what the selected model, provider, and session tool expose before dispatch.

Higher effort can add latency, unnecessary checking, and complexity. Consequential work may need stronger verification rather than more thinking. Select model capability and effort together; there is no required ladder through Sol Medium before Astra.

## When Astra adds value

Choose Astra at the outset when stronger judgment is likely to materially improve the outcome, for example:

- Interpreting ambiguous requirements or comparing architectures before implementation.
- Identifying hidden invariants or failure modes across subsystem boundaries.
- Reconciling contradictory observations, competing explanations, or reviewer findings.
- Synthesizing research across domains or many independently gathered findings.
- Assessing uncertain, costly-to-reverse decisions involving security, data integrity, or operations.
- Implementing work where design choices remain tightly intertwined with execution.

Repeated unsuccessful Sol attempts are another useful signal, not an admission requirement. First obtain missing files, logs, or tests when they can settle the question directly; ask the user for preferences or authorization only they can provide.

In the dispatch brief, state the expected benefit and deliverable:

> Astra is appropriate because <specific judgment demand>; stronger judgment should improve <outcome>. Return <bounded deliverable>.

Supply the relevant evidence, alternatives, constraints, and uncertainty, distinguishing observations from interpretations so Astra can challenge the current explanation.

Use an advisory handoff when judgment separates cleanly from execution: Astra settles the decision, then Sol implements. Let Astra own authorized implementation when repeated handoffs would lose essential reasoning or context. Model choice does not change permissions.

Routine lookups, extraction, formatting, known tests, boilerplate, and settled mechanical edits usually benefit more from Luna or Sol. Likewise, final review warrants Astra when it contains a substantive judgment question, rather than merely being the last step.

## Dispatch

1. Select the model and effort together with a bounded assignment. For a nondefault choice, include a brief task-specific reason; explicit user selection is sufficient.
2. Use the loaded Pi session tools. Resolve unknown model/provider identifiers with `list_models`; catalog visibility does not establish account access. Preserve the configured provider rather than silently switching to separately billed API access.
3. Pass explicit `model` and `thinkingLevel` values to `new_session`. Follow delegating-work for the remaining dispatch settings, reusing its instructions if already loaded.
4. If the requested configuration is unavailable, report the limitation and propose an available alternative appropriate to the assignment. Preserve explicit user requirements.

Workers report capability limits to their parent rather than spawning a replacement merely to continue the same assignment on another model. Narrower delegation remains governed by the assigned authority and delegating-work.

## Calibration

These routes are workflow guidance, not universal capability rankings. Sol Low was established with GPT‑5.6 Sol; carrying that default to GPT‑6 Sol and expanding Luna to bounded coding work are provisional choices.

Calibrate using representative assignments: acceptance checks passed, missed constraints, rework, completion time, and usage where observable. Compare model and effort together. Published high-effort results motivate trials; they do not establish Low-effort reliability.

Prefer observed task outcomes over blanket capability claims. Use provider-specific billing information for cost comparisons; distinguish API prices, subscription consumption, and remaining allowance.
