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

Return a bounded file/anchor map the parent can use without repeating discovery; selected file reads to act on findings are not a second investigation.

# Report contribution

When reconnaissance is part of the expected result, report a bounded `Repository map` of paths/symbols and their role/relevance, `Recommended reads` as a small selected path list, and unresolved `Uncertainties`. Omit empty sections and raw search dumps.
