---
name: model-routing
description: Select a model and thinking level for a new Pi worker session.
---

# Model routing

Match model and thinking effort to execution and judgment demands. Optimize completed-work quality, latency, verification, and coordination overhead; apply user-supplied budgets.

## Scope

Recommend configurations for **new sessions** inline in the conversation or an existing dispatch brief; produce no files or persistent artifacts. Honor explicit user model and thinking choices. Recommendations do not authorize delegation, session creation, implementation, or changes to existing sessions or account defaults.

## Model

**GPT-6.1 Sol Low is the general-execution default.** Choose alternatives prospectively when better suited; no prior failure is required.

- **Sol** (`gpt-6.1-sol`): general execution and judgment, including implementation, multi-file investigation, debugging, review, architecture, planning, synthesis, orchestration, and continuing design decisions. Usually Low; task length or file count alone does not justify higher effort.
- **Luna** (`gpt-6-luna`): focused, verifiable discovery, extraction, deterministic transformations, known checks, and localized implementation or debugging with explicit requirements. Usually Low; consider Medium or High for well-specified, reasoning-intensive work. Favor Sol or Astra for hidden constraints, ambiguity, or cross-system design decisions.
- **Astra** (`gpt-6-astra`): optional higher-cost, higher-latency alternative when documented evaluations or observed results support a workload-specific advantage over Sol at appropriate effort. Consider difficult science, demanding computer use, exacting factuality or instruction adherence, or independent assessment of consequential decisions. Architecture, ambiguity, debugging, review, and synthesis default to Sol.

Route by required decisions, not read-only versus coding work. Luna fits explicit scope, acceptance criteria, and independent verification; a settled plan helps when remaining decisions are local and integration assumptions are checkable.

Unsuccessful Sol attempts can inform selection: distinguish missing inputs from capability limits using available diagnostics. Ask users for preferences or authorization only they can provide.

## Thinking

Choose prospectively from the assignment, independently of model tier, using previous results when available. No lower-effort trial is required.

- **Low:** clear objectives, bounded decisions, ordinary implementation, investigation, review, and tool use. Normal for Sol and Luna; useful for focused Astra judgments.
- **Medium:** significant comparison or substantial synthesis when it meets the quality bar with less latency than High. Optional; not a prerequisite to High.
- **High:** Sol's primary deeper-thinking option for sustained reasoning across interacting constraints, competing explanations, or difficult failure modes. Use a task-specific reason, not size or importance alone.
- **Higher supported settings:** explicit request or task-specific evidence of benefit over High. Verify model, provider, and session-tool support before dispatch.

Higher effort can increase latency, unnecessary checking, and complexity. Consequential work may need stronger verification instead. Compare model and effort together; choose alternatives for expected workload benefits.

## Recommendation

1. Select model and effort together. Briefly justify nondefault choices for this task; explicit user selection suffices.
2. Resolve unknown model/provider identifiers with `list_models`; visibility does not prove account access. Preserve the configured provider rather than silently switching to separately billed API access.
3. Include explicit `model` and `thinkingLevel` values inline.
4. If unavailable, report the limitation and propose an available, task-appropriate alternative while preserving explicit user requirements.

## Calibration

These are workflow routes, not universal capability rankings. Sol Low is the chosen default, not a claim of Astra-level capability at Low. Launch evaluations support improved lower-effort capability and quality per dollar; broader reliability and effort choices need workflow calibration.

Refine routes from representative outcomes: acceptance checks, missed constraints, rework, completion time, and observable usage. Prefer outcomes over blanket capability claims; published high-effort results suggest routing hypotheses, not Low-effort reliability. Compare costs with provider-specific billing, distinguishing API prices, subscription consumption, and remaining allowance.
