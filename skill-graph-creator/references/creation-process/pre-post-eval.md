# Pre/Post Evaluation Gates

Every step in the creation process has a pre-gate and a post-gate. These are not separate steps — they are evaluation layers that wrap each step.

## Pre-Execution Eval (Before Each Step)

Before executing any step, pause and evaluate:

| Question | Purpose |
|----------|---------|
| "Is this the right approach? Is there a better way?" | Challenge the current plan |
| "Given what I know now, would I make the same decision?" | Check for stale assumptions |
| "What are 2-3 alternatives? Why is the chosen way better?" | Consider options |
| "Do I have everything I need to execute this well?" | Check dependencies |

**If the pre-eval reveals:**
- A better approach → revise the plan before proceeding
- Missing information → return to clarification or research
- Changed assumptions → update the plan to reflect current understanding

## Post-Execution Eval (After Each Step)

After completing a step, evaluate:

| Question | Purpose |
|----------|---------|
| "Did I achieve what this step was supposed to achieve?" | Goal verification |
| "Is the output good enough for the next step?" | Quality gate |
| "Did any assumptions prove wrong during execution?" | Assumption audit |
| "Did I cover everything, or skip/miss something?" | Completeness check |

**If the post-eval reveals:**
- Gaps → fix before moving to the next step
- Wrong assumptions → return to relevant earlier step
- Quality issues → redo or refine the current step

## Step-by-Step Application

| Step | Pre-Eval Focus | Post-Eval Focus |
|------|----------------|-----------------|
| 0.5 Domain Classification | "Am I classifying based on enough information?" | "Does the classification feel right given what the user said?" |
| 1 Clarification | "Am I asking the right kinds of questions for this domain?" | "Do I genuinely understand the requirements?" |
| 2 Research | "Am I researching the right things?" | "Did research confirm or change my understanding?" |
| 3 Understand | "Do I have enough examples to proceed?" | "Do the examples cover the full scope?" |
| 4 Plan | "Is this the right graph structure for this domain?" | "Does the plan cover all requirements?" |
| 5 Initialize | "Is the template appropriate for this graph?" | "Does the generated structure match the plan?" |
| 6 Implement | "Am I building the right thing?" | "Does the implementation match plan and requirements?" |
| 7 Package | "Is the graph ready for packaging?" | "Did packaging succeed without issues?" |
| 8 Iterate | "Are the requested changes the right changes?" | "Did iteration improve the skill graph?" |

## Anti-Patterns

- **Rubber-stamping**: Going through eval motions without genuine reflection
- **Confirmation bias**: Only looking for evidence that the current approach is correct
- **Sunk cost**: Continuing a bad approach because work has already been done — it is always cheaper to fix now than later

## Back to

- [Creation process overview](overview.md)
- See also: [Feedback checkpoints](feedback-checkpoints.md)
- See also: [Permanent steps](../planning-framework/permanent-steps.md)
