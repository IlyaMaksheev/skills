# Prototype result template

Use this shape for the finalized `RESULT.md` after evaluation is complete, following [SKILL.md](SKILL.md)'s capture-and-evaluate sequence. Keep entries bounded to the question and evidence; omit empty Adopt or Reject sections. Links are relative to the result file. Record commands with the working directory and any reused environment needed to reproduce the run, without credentials.

```markdown
# Prototype result: <short name>

## Question

<The exact question this prototype was built to answer.>

## Artifact

<Relative links to entry points, the working directory, and how to open or run them.>

## Verification

<Checks actually performed and their outcomes; identify anything still unverified.>

## Verdict

<The human's settled verdict, identifying the evaluated artifact or revision and the scope of approval.>

## Observations

- <What the artifact exposed; distinguish observed behavior from interpretation.>

## Fidelity and limitations

<What was reused, represented, or stubbed, and how that limits conclusions.>

## Adopt

- <After human evaluation: validated behavior, structure, or idea for later implementation.>

## Reject

- <After human evaluation: variants or assumptions explicitly rejected.>

## Leaves open

- <Remaining uncertainty, or `None`.>
```

Record which variant or behavior the human accepted or rejected and why. Recommendations and a successful runtime check are not a verdict. Under Wayfinder, the parent uses this result as evidence for the decision's resolution and claim boundary; the result carries no decision-bank state.
