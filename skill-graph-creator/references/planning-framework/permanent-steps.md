# Permanent Steps

These are non-negotiable process steps that must be followed for every skill graph creation. They cannot be skipped, shortened, or reordered.

## The Nine Steps

| # | Step | Status | Skippable? |
|---|------|--------|------------|
| 0.5 | [Domain Classification](../creation-process/domain-classification.md) | **Mandatory** | Never |
| 1 | [Clarification](../creation-process/step-1-clarification.md) | **Mandatory** | Never |
| 2 | [Research](../creation-process/step-2-research.md) | **Mandatory** | Never |
| 3 | [Understand](../creation-process/step-3-understand.md) | Required | Only if usage patterns are already clearly understood |
| 4 | [Plan](../creation-process/step-4-plan.md) | Required | Never |
| 5 | [Initialize](../creation-process/step-5-initialize.md) | Required | Only if updating an existing skill |
| 6 | [Implement](../creation-process/step-6-implement.md) | Required | Never |
| 7 | [Package](../creation-process/step-7-package.md) | Required | Never |
| 8 | [Iterate](../creation-process/step-8-iterate.md) | Ongoing | Triggered by usage feedback |
| 9 | [Final Eval](../creation-process/step-9-final-eval.md) | **Mandatory** | Never |

### Cross-Cutting Layers

| Layer | Purpose | Reference |
|-------|---------|-----------|
| Pre/Post Eval | Evaluation gates wrapping every step | [pre-post-eval.md](../creation-process/pre-post-eval.md) |
| Feedback Checkpoints | Structured user validation loops | [feedback-checkpoints.md](../creation-process/feedback-checkpoints.md) |

## Mandatory Behaviors

Throughout all steps:

1. **Classify the domain first** — Before any questions are asked. See [domain classification](../creation-process/domain-classification.md).
2. **Ask questions when uncertain** — See [questionnaire framework](../questionnaire-framework/overview.md)
3. **Maintain a todo list** — See [todo structure](todo-structure.md)
4. **Follow graph architecture** — See [graph architecture](../graph-architecture/overview.md)
5. **Run pre-eval before each step** — Challenge whether the approach is right before executing. See [pre-post eval](../creation-process/pre-post-eval.md).
6. **Run post-eval after each step** — Verify the decision was correct after executing. See [pre-post eval](../creation-process/pre-post-eval.md).
7. **Maintain feedback checkpoints** — Validate understanding with the user at prescribed points. See [feedback checkpoints](../creation-process/feedback-checkpoints.md).
8. **Apply recursive decomposition** — Break problems into atomic subproblems. See [problem decomposition](../core-principles/problem-decomposition.md).
9. **Validate before packaging** — Run `validate_graph.py`
10. **Never assume** — If information is missing, ask for it
11. **Always run final eval (step 9)** — Never deliver without a bird's-eye review.

## Pre-Packaging Checklist

Before running `package_skill.py`, verify:

- [ ] Domain classification performed and validated with user
- [ ] Clarifying questions were asked and answered
- [ ] Research was performed
- [ ] Concrete usage examples were identified
- [ ] Graph structure was planned
- [ ] SKILL.md is navigation-only and under 100 lines
- [ ] All reference files are written and interlinked
- [ ] All hub files link to all files in their directory
- [ ] All detail files have "Back to" sections
- [ ] No orphan files exist
- [ ] No duplicate content across files
- [ ] Scripts are tested
- [ ] Pre-eval performed before each step
- [ ] Post-eval performed after each step
- [ ] Feedback checkpoint after clarification completed
- [ ] Feedback checkpoint after research completed
- [ ] Feedback checkpoint after plan completed
- [ ] Subjective decisions gathered from user (not defaulted)
- [ ] One-shot test passed for all reference files
- [ ] `validate_graph.py` passes
- [ ] Final eval (step 9) completed with bird's-eye review

## Back to

- [Planning framework overview](overview.md)
- See also: [Creation process overview](../creation-process/overview.md)
