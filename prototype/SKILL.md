---
name: prototype
description: Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. Propose the question and artifact before starting unless the user already requested the prototype.
---

# Prototype

A prototype is **throwaway code that answers a question**. The question decides the shape.

## Entry and approval

An explicit `/skill:prototype` invocation or request to build a prototype authorizes the work. When reaching for it automatically, propose the question, artifact, and bounded scope, then wait for approval before writing files or dispatching work. A suggestion that prototyping might help is not yet approval to build.

Standalone use runs in the current session. When a Wayfinder parent delegates an approved prototype, build it in the dedicated worker without spawning another prototype worker. The parent owns the decision, human evaluation, and map mutations; the worker owns only the assigned prototype artifacts. Follow `/skill:receiving-work` for the assignment and `/skill:agent-docs-lifecycle` for worker integration. Building the artifact never authorizes resolving the decision.

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding code, or by asking if the user is around:

- **"Does this logic / state model feel right?"** → [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"What should this look like?"** → [UI.md](UI.md). Generate several radically different UI variations on a single prototype route, switchable via a URL search param and a floating bottom bar.

The two branches produce very different artifacts, so getting this wrong wastes the whole prototype. If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch better matches the surrounding code (a backend module → logic; a page or component → UI) and state the assumption at the top of the prototype. This inference chooses a branch only after approval to build; it does not supply a human verdict.

## Workspace and environment

Before the first artifact write, load and follow `/skill:agent-docs-lifecycle`. Infer the feature or prototype name from context and inspect the intended paths; preserve existing artifacts and ask when ownership or reuse is ambiguous.

- **Standalone:** `.agent-docs/<prototype-name>/prototype/` holds the runnable files; `.agent-docs/<prototype-name>/RESULT.md` holds the result. No Wayfinder map is required or created.
- **Wayfinder:** use the assigned `.agent-docs/<feature>/prototypes/decision-NNN-<slug>/` directory, with `RESULT.md` beside its runnable files. The existing decision file remains the route-facing authority.

These are paths in the target project, not in this installed skill directory. Keep every authored file, prototype dependency manifest, generated output, and prototype configuration inside the designated `.agent-docs` directory. Production paths, project dependency manifests, and shared environments remain unchanged.

A **worktree isolates source, not the environment**. Inspect project instructions, established run commands, the primary checkout, and existing compatible environments, installed dependencies, toolchains, and caches before provisioning anything. Reuse them through supported paths or commands instead of duplicating large downloads. Check that commands run the intended worktree source rather than a package bound to the primary checkout. Shared environments are reused read-only; tools that would install, sync, or rebuild them need an isolated alternative. If compatible reuse fails, explain the missing dependency and obtain approval before new installation or environment creation, keeping prototype-specific provisioning within its artifact directory.

Production code may be read or imported where this works without changing production files, configuration, dependencies, or external state. Stub mutations and avoid imports with application-startup side effects. When reuse is impractical, copy the minimum representative behavior or UI into the prototype and record the fidelity limitation in `RESULT.md`.

## Rules that apply to both

1. **Throwaway from day one, and clearly marked as such.** Keep the question and the production module or page being explored identifiable from the prototype, while all prototype files stay in its artifact directory.
2. **Trivial to run.** A UI prototype starts with one documented command using the existing environment, or opens as self-contained HTML. A logic demo is a single HTML file the user double-clicks. Either way, no thinking required to start it.
3. **No persistence by default.** State lives in memory. Persistence is the thing the prototype is checking, not something it should depend on. If the question explicitly involves persistence, use a clearly named scratch file inside the artifact directory or an explicitly approved scratch service, never production data stores.
4. **Skip the polish.** No maintained test suite, no error handling beyond what makes the prototype runnable, no speculative abstractions. The point is to learn something fast. This does not exempt the runnable checks in the branch guide.
5. **Surface the state.** After every action (logic) or on every variant switch (UI), print or render the full relevant state so the user can see what changed.
6. **Preserve the primary source.** Keep the runnable prototype and its result on the mixed feature branch in path-pure `agent-docs:` commits under the existing lifecycle. No permanent branch per prototype, no `agent-prototype:` commit type, and no automatic production implementation. Product delivery excludes these artifacts; the retained mixed branch preserves their evidence.

## Capture and evaluate

Create `RESULT.md` using [RESULT-TEMPLATE.md](RESULT-TEMPLATE.md). Start with the question, artifact links, run instructions, observations, and known fidelity limitations; keep the verdict at `Pending human evaluation`. Record the runtime checks actually performed. If tools or access prevent a required check, state exactly what remains unverified and request the missing check rather than claiming the artifact is verified.

Present the artifact for the human to drive. A delegated builder returns a runnable artifact and enough information to open it, leaving the verdict pending. There is no fixed worker report format; follow the assignment's reporting and Git integration workflow.

A **human verdict** is required even when the result seems obvious. The human may accept, combine, reject, request revisions, change the investigation method, or leave the question unresolved. Use `/skill:brainstorm` when discussion of the concrete artifact is needed. Iterate on revisions and verify affected walkthroughs or variants before presenting again. Until the human settles the question, keep the result pending; rejection resolves it only when that rejection itself answers the question.

After an explicit verdict, record the answer and what it does and does not establish in `RESULT.md`, then preserve the stable update through `/skill:agent-docs-lifecycle`. Under Wayfinder, the parent records the route-facing resolution and claim boundary in the decision file, links `RESULT.md` as evidence instead of copying it, and routes remaining uncertainty into decisions or fog through Wayfinder's normal workflow. The worker never marks the decision resolved.

The validated idea is input to later implementation. Prototyping stops at the answer and its evidence; production changes require a separate authorized implementation task.
