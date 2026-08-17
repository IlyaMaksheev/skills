# Reporting recovery

1. Call `list_sessions`.
2. Match the prompt's immediate parent name against the live sessions.
3. If exactly one clear parent exists, send the same sparse terminal report with `message_session({ to: "<session>" })`.
4. If no clear parent exists or the result is ambiguous, do not report to a guessed master or parent-of-parent.
5. End with plaintext only:

```text
Status: blocked
Summary:
- Cannot identify the immediate parent session for terminal reporting.

Sessions:
- <compact session list>
```

Do not loop through repeated delivery attempts and do not add unrelated report sections.
