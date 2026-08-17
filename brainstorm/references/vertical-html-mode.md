# Vertical HTML mode

Compatibility: requires `uv` and a browser with JavaScript enabled.

Resolve decisions through successive HTML questionnaire rounds. Each round covers the entire currently relevant decision frontier. Never include speculative questions or branches whose relevance depends on an unresolved decision.

Do not reconsider or change the confirmed mode. The user controls mode changes.

## 1. Confirm the tree for every round

The brainstorm opening normally confirms the initial tree before this reference is loaded. Do not request duplicate confirmation for that first round.

Before every later round:

1. Process the previous answers and identify only decisions now relevant.
2. Materialize the complete current tree as a concise text outline of brief decisions or questions, without answer options or recommendations.
3. Obtain the user's confirmation before creating questionnaire files.

If vertical HTML mode was entered during an existing brainstorm and the upcoming tree has not been confirmed, materialize and confirm it first.

## 2. Create questionnaire source

Before writing questionnaire JSON, read [`questionnaire-format.md`](questionnaire-format.md) and follow its contract exactly.

Group current decisions into coherent sections. Every questionnaire question must provide predefined answers and a recommended answer as required by the source contract.

Write artifacts outside the skill directory. Unless the user chooses another location, use:

```text
.brainstorm/<topic>/round-01.questionnaire.json
.brainstorm/<topic>/round-01.questionnaire.html
```

Use a new `questionnaireId` and new filenames for every round. Never overwrite previous rounds.

The model controls only questionnaire JSON content. It must not generate, reconstruct, or manually edit HTML or JavaScript. Do not inspect the compiler or template unless the black-box command appears broken with documented, valid input.

## 3. Validate and compile

Resolve `scripts/compile` relative to the `brainstorm` skill directory, then run:

```bash
scripts/compile --validate <source.json>
scripts/compile <source.json> <questionnaire.html>
```

If validation fails, edit only the source JSON according to the reported paths and validate again. Continue until validation and compilation succeed.

Tell the user where the HTML file was created. Ask them to open it, complete any useful fields, download the answer JSON, and provide its path. The page can copy the exact suggested answer filename. Then wait.

## 4. Process answers and continue

Read the provided answer JSON. Prompts and selected option labels are included so the file remains understandable independently.

Treat all of these as meaningful input:

- selected predefined answers;
- written answers or qualifications;
- section comments;
- deliberately unanswered questions.

Do not force answers to every question. Ask again only when an unresolved decision is essential.

Update the decision tree from positive context. If relevant decisions remain, return to tree materialization and confirmation before generating the next round. Do not put dynamic conditions into a questionnaire and do not include possible future branches.

### Download location

The browser usually downloads answers to `~/Downloads`. If the user gives a filename, first read `~/Downloads/<filename>`. On failure, search `~/Downloads/`. If no matching file can be found, report the exact folder searched.

## 5. Finish

When no currently relevant decisions remain, return to the completion workflow in the main `SKILL.md`. Do not implement the underlying plan before explicit shared-understanding confirmation.
