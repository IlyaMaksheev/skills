---
name: to-implementation-context
description: Create implementation context from concrete repository and coding discoveries for a future agent that will modify, debug, or test software. Use only when the destination session will perform software implementation. Generic handoffs, web research, interview preparation, and other non-coding context transfers do not qualify.
disable-model-invocation: true
---

# To Implementation Context

Extract usable implementation context from the current conversation and the codebase understanding already accumulated in this session.

## Invocation boundary

Use this skill only when the receiving agent will implement, modify, debug, or test software in the repository. The session must already contain at least one concrete implementation discovery:

- relevant modules, interfaces, or integration points;
- existing implementation patterns or tests;
- build, validation, or debugging commands;
- technical constraints or code-level hazards.

A request for a handoff, context file, or document for another agent does not qualify by itself. Use a purpose-specific artifact for web or company research, interview and job-application preparation, general conversation summaries, product requirements, task decomposition, and other non-coding handoffs.

This is a synthesis step. Work only from knowledge already present in the session. Do not interview the user, perform additional repository exploration, or load a spec, task bank, or task files to discover more context.

## How this artifact differs

- A **spec** defines what and why.
- A **task** defines an executable slice, its acceptance criteria, and its dependencies.
- **Implementation context** preserves shared, codebase-specific knowledge that would help a future agent avoid repeating discovery.
- A **task plan** contains detailed implementation steps for one task.

Do not duplicate product requirements, user stories, task decomposition, acceptance criteria, dependency information, or unresolved product decisions.

## Output location

Before selecting a path, verify that the session contains at least one concrete codebase integration point, implementation pattern, command, or technical hazard distinct from requirements and tasks. If none is available, create neither a file nor an empty planning directory; state that the request needs a different handoff format.

When useful context exists, use the active `./.plans/<feature-name>/` directory if one has already been established. Otherwise, derive a concise lowercase kebab-case feature name from the current session, state the selected path, and create the directory.

Write the result to `./.plans/<feature-name>/IMPLEMENTATION-CONTEXT.md`. If that file already exists, inspect it and do not overwrite it without user confirmation.

## Content rules

- Include only concrete facts and discoveries already present in the session.
- Be concise and implementation-oriented.
- Use repository-relative paths.
- Link to existing project documentation instead of duplicating it.
- Omit empty sections and placeholders.
- Do not speculate or invent missing context.

## Template

```md
# Implementation Context

## Relevant code and integration points

<Repository-relative paths, modules, interfaces, and boundaries already discovered.>

## Existing patterns and prior art

<Implementations, tests, or conventions worth following.>

## Commands and tooling

<Relevant setup, validation, test, build, or debugging commands.>

## Technical constraints and hazards

<Non-obvious limitations, compatibility concerns, operational constraints, and known traps.>

## Useful implementation findings

<Other concrete technical facts from the session that would prevent repeated discovery.>
```
