---
name: to-spec
description: Turn the current conversation context or a completed local Wayfinder map into a spec. Use when the user wants to synthesize settled feature understanding into a spec.
disable-model-invocation: true
---

# To Spec

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user — just synthesize what you already know.

A legacy PRD is not a normal input to this skill. If the user explicitly asks to migrate a PRD to the new spec standard, read [MIGRATING-FROM-PRD.md](./MIGRATING-FROM-PRD.md) and follow it instead.

## Wayfinder source

When the user explicitly provides a local `WAYFINDER.md` path:

1. Read the map and require `Status: ready`. If it is still `active`, scan sibling `decision-NNN-*.md` metadata, report the remaining open or claimed decisions and fog, create nothing, and direct the user back to `/skill:wayfinder <map-path>`.
2. Follow every decision linked under `Decisions so far` and read the resolution and relevant evidence. Use `Out of scope` to preserve the agreed boundary, but never import `out-of-scope` or `superseded` decisions as accepted implementation decisions.
3. Collapse the accepted resolutions into a self-contained spec. The spec must be usable by `/skill:to-tasks` and implementation sessions without reopening every decision file; summarize rationale rather than reproducing the full discussions.
4. Use the map's feature directory for `SPEC.md`. Link `WAYFINDER.md` and the material resolved decision files under `Parent Documents` to preserve provenance.

This is an explicit input adapter only. Do not invoke Wayfinder or any downstream workflow automatically. Normal conversation-to-spec behavior is unchanged when no Wayfinder path is supplied.

## Output location

Use the active `./.plans/<feature-name>/` directory when one has already been established. Otherwise, derive a concise lowercase kebab-case feature name from the current context, state the selected path, and create the directory.

Write the result to `./.plans/<feature-name>/SPEC.md`. If `SPEC.md` already exists, inspect it and do not overwrite it without user confirmation.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation.

A deep module (as opposed to a shallow module) is one which encapsulates a lot of functionality in a simple, testable interface which rarely changes.

Check with the user that these modules match their expectations. Check with the user which modules they want tests written for.

3. Write `SPEC.md` using the template below.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

<user-story-template>
As an <actor>, I want to:
1. <feature-1>, so that <benefit>
...
n. <feature-n>, so that <benefit>
</user-story-template>

<user-story-example>
As a mobile bank customer, I want to:
1. see the balance on my accounts, so that I can make better-informed decisions about my spending
2. ...
...
n. ...
</user-story-example>

This list of user stories should be extremely extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built or modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may become outdated very quickly.

## Technology Stack

A list of libraries, packages, or technologies that should be used to solve the problem. Some technologies should be taken from the current context. If none were mentioned, do not add any.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

## Parent Documents

A list of documents that played an important role in creating this spec, if there are any.

</spec-template>
