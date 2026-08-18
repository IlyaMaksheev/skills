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

# Delegated recon

A utility worker returns a bounded file/anchor map that the implementation worker can consume without repeating the broad search. The implementation worker reads the selected relevant files before acting on the map.

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
