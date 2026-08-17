# Reporting recovery

1. Call `list_sessions`.
2. Match the prompt's `Parent name` against live sessions.
3. If exactly one clear immediate parent exists, send the same sparse plaintext report with `message_session({ to: "<session>" })`.
4. If the result is missing or ambiguous, do not report to a guessed master or parent-of-parent.
5. End locally with only:

```text
Status: blocked
Summary:
- Cannot identify the immediate parent session for terminal reporting.

Sessions:
- <compact session list>
```

Do not loop through repeated delivery attempts. Do not add sections from unrelated modules merely because reporting failed, and do not give a normal final summary after ambiguous routing.
