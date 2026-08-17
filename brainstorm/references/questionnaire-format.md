# Questionnaire source format

The model writes questionnaire content as JSON. The compiler owns all HTML, JavaScript, form behavior, persistence, and answer export behavior.

The authoritative machine-readable contract is [`../schemas/questionnaire.schema.json`](../schemas/questionnaire.schema.json). Unknown properties are rejected.

## Complete shape

```json
{
  "questionnaireId": "topic-round-1",
  "title": "Questionnaire title",
  "description": "Optional questionnaire description.",
  "sections": [
    {
      "sectionId": "direction",
      "title": "Direction",
      "description": "Optional section description.",
      "questions": [
        {
          "questionId": "primary-approach",
          "prompt": "Which approach is most appropriate?",
          "description": "Optional clarification for the question.",
          "selection": "single",
          "options": [
            {
              "optionId": "approach-alpha",
              "label": "Approach Alpha",
              "description": "Optional explanation of this option.",
              "recommended": true
            },
            {
              "optionId": "approach-beta",
              "label": "Approach Beta"
            }
          ]
        }
      ]
    }
  ]
}
```

See [`../examples/example-questionnaire.json`](../examples/example-questionnaire.json) for both single-choice and multiple-choice questions.

## Fields

### Questionnaire

- `questionnaireId` — required stable ID. Give every round a different ID so browser persistence cannot collide.
- `title` — required plain-text title.
- `description` — optional plain-text introduction.
- `sections` — required non-empty ordered array.

### Section

- `sectionId` — required and unique across the questionnaire.
- `title` — required plain-text heading.
- `description` — optional plain-text context.
- `questions` — required non-empty ordered array.

The renderer adds one general section-comment textarea automatically.

### Question

- `questionId` — required and unique across the entire questionnaire.
- `prompt` — required plain-text question.
- `description` — optional plain-text clarification.
- `selection` — required; only `single` or `multiple` is accepted.
- `options` — required array containing at least two predefined answers.

The renderer adds selection guidance and one general-purpose textarea automatically. Options are never preselected, including recommended options. User answers are never required. Selecting an already chosen single-choice option again clears it.

### Option

- `optionId` — required and unique within its question.
- `label` — required plain-text answer.
- `description` — optional plain-text explanation.
- `recommended` — optional boolean. Omission means not recommended.

A `single` question must have exactly one recommended option. A `multiple` question must have one or more recommended options.

## ID rules

IDs contain lowercase ASCII letters, digits, and single hyphens. They cannot begin or end with a hyphen. Examples:

- `deployment-round-1`
- `hosting-model`
- `self-hosted`

Section IDs must be unique within the questionnaire. Question IDs must be globally unique. Option IDs must be unique within their question.

## Content rules

- All displayed content is plain text. Do not provide HTML or Markdown.
- Do not add branching, dependencies, required-answer flags, layout settings, or JavaScript fields.
- Include only questions relevant in the current round.
- Put possible manual answers, qualifications, or comments in the automatically supplied textarea; do not add an `other` option solely to enable manual input.
- Recommendations guide the user but never select an answer for them.

## Validation and compilation

Resolve `scripts/compile` relative to the skill directory.

```bash
scripts/compile --validate path/to/round-01.questionnaire.json
scripts/compile path/to/round-01.questionnaire.json path/to/round-01.questionnaire.html
```

Validation reports JSON paths and exits nonzero. Repair only the source JSON and rerun validation. Never repair or hand-edit generated HTML.

## Exported answers

The generated page downloads an independently understandable answer file named `<questionnaireId>-answers.json`. A nearby button copies this exact suggested filename; browser security prevents the page from discovering or copying the download's full filesystem path.

```json
{
  "questionnaireId": "topic-round-1",
  "title": "Questionnaire title",
  "sections": [
    {
      "sectionId": "direction",
      "title": "Direction",
      "comment": "Optional section context.",
      "answers": [
        {
          "questionId": "primary-approach",
          "prompt": "Which approach is most appropriate?",
          "selectedOptions": [
            {
              "optionId": "approach-alpha",
              "label": "Approach Alpha"
            }
          ],
          "textAnswer": "Optional written answer, explanation, or comment."
        }
      ]
    }
  ]
}
```

Every presented question appears in the answer file. An unanswered question has an empty `selectedOptions` array and an empty `textAnswer` string.
