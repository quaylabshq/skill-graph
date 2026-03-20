# Step 1: Clarification

**Status: MANDATORY — never skip this step.**

Before any planning work, ask extensive clarifying questions. This is the most critical step. Think like a senior staff engineer approaching a new problem from first principles.

## Why Clarification Is Non-Negotiable

Planning without understanding leads to wrong plans. A plan built on misunderstood requirements wastes more time than no plan at all — it sends implementation in the wrong direction.

## When to Ask Questions

- **At the very beginning** — before any other work happens
- **During research** — when findings raise new questions
- **During decomposition** — when breakdown decisions require domain insight
- **During plan generation** — when ambiguity surfaces in the plan structure

Questions are not limited to step 1. They can and should happen at any point.

## How to Ask

Apply [domain classification](domain-classification.md) first, then the [questionnaire framework](../questionnaire-framework/overview.md):

1. Classify the domain — determine the subjectivity, technical depth, scope, novelty, and codebase relevance
2. **Validate the problem first** — ask at least one question challenging the premise: "Is this the right problem? What happens if we don't do this?" (see [initial questions — category 0](../questionnaire-framework/initial-questions.md))
3. For high-subjectivity domains: ask for examples, references, preferences BEFORE technical questions
4. Start with scope and boundaries — what is in and out of scope
5. **Uncover success criteria** — for every requirement, ask "how will you know this is done?" This feeds the [goal-driven methodology](../goal-driven-methodology/overview.md).
6. Identify constraints — what tools, languages, platforms, existing patterns are involved
7. Understand quality requirements — what level of detail, correctness, coverage
8. Probe for implicit requirements — what the user assumes but hasn't stated
9. Challenge your own assumptions — what do you think you know that might be wrong
10. **Detect conflicting requirements** — see [mid-process questions](../questionnaire-framework/mid-process-questions.md)

## Rules

1. Ask 3–5 questions per message — avoid overwhelming the user
2. Start with the most critical questions first
3. Follow up based on answers — each answer may reveal new questions
4. Continue until all relevant uncertainties are resolved
5. For complex tasks, expect 2-3 rounds of questioning before proceeding

## Back to

- [Planning process overview](overview.md)
- See also: [Questionnaire framework](../questionnaire-framework/overview.md) — detailed thinking model for question generation
