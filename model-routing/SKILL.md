---
name: model-routing
description: Choose a model and thinking level before creating a new Pi session. Use for worker creation, model-specific delegation, or planning an escalation into a new session. Defaults to Sol Low with selective Luna delegation and justified Astra escalation.
---

# Model routing

Select the model, thinking level, and bounded assignment together before creating a session. This policy applies regardless of the model making the selection. It optimizes a constrained ChatGPT Plus subscription for useful completed work rather than lowest token price.

## Scope

Apply routing only to **new sessions**. Keep existing sessions on their current model and thinking level; this skill does not authorize changing session configuration or account defaults. Honor explicit user model and thinking choices over these defaults.

Routing does not itself justify spawning. Load and follow [delegating-work](../delegating-work/SKILL.md) to decide whether delegation is worthwhile and to handle briefing, authority, dispatch, and reporting. Prefer a suitable existing worker when its retained context helps; needing this skill is not a reason to replace it.

## Select a route

Start with **Sol Low**. Choose another route only when the assignment meets its criteria below.

| Model | Role and strengths | Selection rule |
| --- | --- | --- |
| **Sol** (`gpt-5.6-sol`) | Dependable general worker: implementation, multi-file reasoning, investigation, debugging, review, planning, and orchestration. Strong follow-through; higher effort can add unnecessary checking or complexity. | **Low by default**, including substantive research and state-changing work. Task length or file count alone does not warrant escalation. |
| **Luna** (`gpt-5.6-luna`) | Economical scout for file/symbol discovery, fact extraction, known-file summaries, deterministic transformations, and known check execution. Less reliable on hidden invariants and cross-file judgment. | **Low** for narrow work with cheap independent verification. Specify the search boundary, output contract, and checks. Keep architectural interpretation and final synthesis with the parent. |
| **Astra** (`gpt-6-astra`) | Scarce specialist for ambiguity, difficult diagnosis, conflicting evidence, and consequential decisions. Promising stronger judgment at Low, but subscription usage can be expensive. | **Low**, only with an explicit justification under the escalation gate below. Prefer a bounded advisory assignment, returning implementation to Sol when the decision is settled. |
| **Terra** (`gpt-5.6-terra`) | Balanced worker, but its lower token price can be offset by longer output or retries. No default role in this workflow. | **Low or Medium** only for an explicit request or a recurring bounded workload with measured end-to-end savings over Sol and sufficient reliability beyond Luna. |

A read-only assignment is not automatically a Luna assignment. Broad research synthesis, security analysis, and architectural investigation usually belong on Sol. Even a Sol-authored plan or reference implementation does not remove Luna's risk of missing integration constraints.

## Select thinking

Use **Low** unless the assignment supplies a concrete reason for more reasoning. Apply the choice at creation, not mid-session.

- **Low:** ordinary execution, analysis, planning, review, and tool use; the normal setting for all selected models.
- **Medium:** additional comparison or checking when evidence shows Low left a shallow plan, unresolved hypotheses, or incomplete multi-file reasoning. Prefer Sol Medium for deeper analysis within Sol's capability before treating extra thinking as an Astra justification.
- **High:** unusually difficult reasoning or consequential analysis where the expected benefit outweighs additional usage. Astra Medium/High is exceptional: for example, a potential data-loss migration with unresolved competing explanations.
- **Higher settings:** use only when explicitly requested or when task-specific evidence justifies the additional usage and the loaded session tool and selected model support the value. They are not routine escalation steps.

Higher Luna thinking is not a substitute for a stronger model when judgment or hidden invariants are the bottleneck. Account for retries and cleanup, not just token counts. API prices and subscription allowance consumption are different; do not infer remaining allowance or exact usage multipliers from token prices.

## Astra escalation gate

Before choosing Astra, identify a specific unresolved judgment question and at least one concrete trigger:

- Requirements have materially different interpretations, and choosing wrong would cause broad rework. Ask the user when only they can supply the missing preference or authorization.
- Sol has made two well-instrumented attempts without resolution, fixes move the failure elsewhere, or observed evidence contradicts the current explanation.
- An important decision combines subsystem boundaries with security, data integrity, product, or operational consequences that Sol has not reconciled.
- Reviewers disagree about an important invariant or whether behavior is intentional.
- A costly-to-reverse decision still has uncertain failure modes or conflicting evidence.

These are reasons to consider Astra, not automatic triggers to spawn it. First check whether a missing file, test, log, or user answer would resolve the question more cheaply. Sol remains suitable for routine decisions and reviews.

Put a short justification in the dispatch brief:

> Astra is warranted because <unresolved question and consequence>; available evidence is <findings>; return <bounded decision and supporting evidence>.

Include relevant facts and source paths, attempted approaches and outcomes, alternatives, constraints, and remaining uncertainty. Clearly separate observed evidence from the parent's interpretation. Give the child enough context to challenge the current explanation, rather than merely endorse it.

A useful deliverable is: recommendation, decisive evidence, unresolved questions, and implementation constraints. Bound access to the assigned decision; use read-only authority for advisory work. Explicitly authorized implementation may use Astra when the same gate warrants it, but calling a session Astra does not broaden its permissions.

File lookup, summaries, boilerplate, known tests, settled mechanical edits, routine status reporting, and automatic final approval do not justify Astra. A large task with a settled plan usually stays on Sol Low.

## Dispatch

1. Resolve the assignment and route above. For a nondefault route or thinking above Low, record the task-specific reason in the brief; explicit user selection is sufficient justification.
2. Load Pi session tools. Use `list_models` when the provider/model identifier is unknown or availability is uncertain. Select the configured subscription provider; catalog visibility is not proof of account access. Avoid silently switching to separately billed API access.
3. Pass explicit `model` and `thinkingLevel` values to `new_session`, using the loaded tool's schema. Do not rely on inheritance from the parent or an unspecified model default. Preserve the remaining dispatch settings from delegating-work.
4. If the model or effort is unavailable, report the limitation. Offer Sol Low as the normal fallback when it can satisfy the task; preserve explicit user requirements rather than silently substituting an unsupported or more expensive route.

Delegated workers should complete their assigned role and report material uncertainty or capability limits to their parent. They should not create a replacement session merely to continue the same assignment on a different model; any permitted narrower delegation follows the same routing and delegation rules. An Astra advisor should return its decision rather than expand into an unassigned implementation run.

## Evidence basis

These are user workflow preferences informed by early, subjective reports, not universal capability rankings. Sol Low is an established successful default for this user. Reports favor Sol's reliability, Luna's bounded-task economy, and Astra's judgment, but disagree on task-level efficiency; Terra can still win on particular workloads.

Supporting sources for revisiting the policy (no web lookup required for ordinary routing):
- [User reports of Luna/Terra retries versus Sol](https://community.openai.com/t/sol-is-expensive-but-luna-terra-retries-can-cost-even-more/1394943)
- [CodeRabbit hands-on Sol/Terra evaluation](https://www.coderabbit.ai/blog/gpt-5-6-sol-and-terra-benchmark)
- [Astra-as-advisor discussion](https://www.reddit.com/r/codex/comments/1wag9vf/for_plus_users_use_astra_as_an_advisor/) — early anecdotal evidence; research access was limited to indexed excerpts.

Most community evidence comes from Codex users, so harness behavior and opaque subscription accounting may not transfer to Pi. Prefer observed results from this workflow over generalized claims such as “Astra Low always beats Sol High.”
