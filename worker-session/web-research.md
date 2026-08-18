# Web research

Follow the loaded `web-research` skill for discovery, source selection, and evidence handling. This module defines the worker-specific authority boundary and terminal report.

# Authority

Research stays within the session's authority envelope. A delegated utility worker returns findings and writes only approved temporary or research artifacts. A delegated implementation worker or direct session may apply findings within its authorized implementation scope.

# Report contribution

When web findings form part of the expected result, append:

```text
Research:
- <concise finding>

Sources:
- <title or authority>: <URL>

Gaps:
- <only unresolved or weakly supported points>
```

Omit `Gaps` when the evidence has no material gap. Summarize evidence rather than reproducing source content.
