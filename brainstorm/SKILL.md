---
name: brainstorm
description: Interview the user relentlessly about a plan or design. Use when the user wants to brainstorm or stress-test an idea.
---

# Brainstorm

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you have not heard yet.

Adapt each round to its frontier:

- **Linear**: when the frontier contains one decision, ask that question and give your recommended answer.
- **Vertical**: when the frontier contains multiple independent decisions, ask the whole frontier as a numbered text round and give your recommended answer for each question.

Then wait for the user's answers before the next round.

Format each question like so:

```
❓ **Q1** - **<question title>**: <question body, which may include multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one. If questions believed independent turn out to interact, reopen the affected branch.

## Vertical HTML mode

Use vertical HTML mode only when the user explicitly requests a `vertical HTML` brainstorm or questionnaire. Before entering it, materialize the current design tree as a concise text outline and obtain the user's confirmation. Then read [`references/vertical-html-mode.md`](references/vertical-html-mode.md) and follow it. Vertical HTML presents the whole frontier through successive HTML questionnaire rounds.

## Facts and decisions

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment, investigate it with the filesystem, available tools, or a sub-agent rather than asking the user. Do not block the rest of the frontier on that investigation: treat it as an unsettled prerequisite, hold only the questions downstream of it, and ask the rest now. The _decisions_ are the user's: put each to them and wait.

## Completion

The session is done when the frontier is empty: every relevant branch of the design tree has been visited and nothing remains silently assumed. Summarize the agreed decisions, constraints, explicit deferrals, and any uncertainty that still blocks action. Do not act on the underlying plan until the user confirms you have reached a shared understanding.
