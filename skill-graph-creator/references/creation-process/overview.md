# Creation Process

Building a skill graph follows nine steps plus cross-cutting evaluation layers. Steps 0.5, 1–2, and 9 are **mandatory** and must never be skipped.

## Process Summary

| Step | Name | Status | Reference |
|------|------|--------|-----------|
| 0.5 | Domain Classification | **Mandatory** | [domain-classification.md](domain-classification.md) |
| 1 | Clarification | **Mandatory** | [step-1-clarification.md](step-1-clarification.md) |
| 2 | Research | **Mandatory** | [step-2-research.md](step-2-research.md) |
| 3 | Understand | Required | [step-3-understand.md](step-3-understand.md) |
| 4 | Plan | Required | [step-4-plan.md](step-4-plan.md) |
| 5 | Initialize | Required (new skills) | [step-5-initialize.md](step-5-initialize.md) |
| 6 | Implement | Required | [step-6-implement.md](step-6-implement.md) |
| 7 | Package | Required | [step-7-package.md](step-7-package.md) |
| 8 | Iterate | Ongoing | [step-8-iterate.md](step-8-iterate.md) |
| 9 | Final Eval | **Mandatory** | [step-9-final-eval.md](step-9-final-eval.md) |

### Cross-Cutting Layers

| Layer | Purpose | Reference |
|-------|---------|-----------|
| Pre/Post Eval | Evaluation gates wrapping every step | [pre-post-eval.md](pre-post-eval.md) |
| Feedback Checkpoints | Structured user validation loops | [feedback-checkpoints.md](feedback-checkpoints.md) |

## Critical Rules

1. **Classify the domain first** — Before any questions are asked
2. **Always start with clarification** — Do not begin implementation before exhausting all questions
3. **Always research** — Implementation is the easy part; understanding requirements is the hard part
4. **Apply pre-eval before each step and post-eval after** — See [pre-post-eval.md](pre-post-eval.md)
5. **Maintain feedback checkpoints throughout** — See [feedback-checkpoints.md](feedback-checkpoints.md)
6. **Always create a todo list** — Every step must be tracked. See [planning framework](../planning-framework/overview.md)
7. **Follow the order** — Steps are sequential; skipping ahead results in rework
8. **Questions can happen at any step** — If ambiguity is discovered mid-process, return to clarification
9. **For subjective domains** — Do not proceed past step 4 without validating design direction with user
10. **Always perform final eval (step 9)** — Never skip, never deliver without it

## Permanent Steps Checklist

These steps are non-negotiable. Before packaging any skill graph, verify:

- [ ] Clarifying questions were asked and answered
- [ ] Research was performed on best practices and standards
- [ ] Concrete usage examples were identified
- [ ] Graph structure was planned (index, references, scripts)
- [ ] Skill was initialized with proper template
- [ ] All reference files are written and interlinked
- [ ] Validation passes (run validate_graph.py)
- [ ] Package was created successfully

## See Also

- [Questionnaire framework](../questionnaire-framework/overview.md) — drives steps 1 and ongoing questioning
- [Research framework](../research-framework/overview.md) — drives step 2
- [Planning framework](../planning-framework/overview.md) — drives todo tracking throughout
- [Graph architecture](../graph-architecture/overview.md) — structural principles applied in step 6
