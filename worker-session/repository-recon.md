# Repository reconnaissance

# Discovery

Begin with bounded structural searches such as `find`, `rg --files`, targeted `rg`, and read-only project metadata. Use known anchors and task terms to narrow candidates before opening files.

Read only files that are plausibly relevant. Respect all forbidden paths, file-count limits, size limits, generated-data restrictions, and project trust boundaries. Search hints guide discovery but do not become hard limits unless the prompt says `only`.

Map useful relationships rather than dumping search output:

- entry points and ownership boundaries;
- relevant modules, contracts, callers, and tests;
- configuration and artifact paths;
- likely files for later implementation;
- uncertainties or conflicting implementations.

Repository presence does not activate Git inspection. Load `git-inspection.md` only when the task explicitly requests history, diff, provenance, or status information.

# Delegated recon

When this file is loaded by a utility worker, return a concise file/anchor map to the immediate parent. The parent should consume that map and read the selected relevant files rather than repeating the broad search.

When loaded by an implementation worker and the recon would materially pollute context, load `utility-delegation.md` and delegate the bounded mapping task.

# Report contribution

When reconnaissance is itself part of the expected result, append:

```text
Repository map:
- <path or symbol>: <role/relevance>

Recommended reads:
- <small selected path list>

Uncertainties:
- <only unresolved items>
```

Omit empty sections and large raw search listings.
