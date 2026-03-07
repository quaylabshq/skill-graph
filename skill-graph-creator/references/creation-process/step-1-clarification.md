# Step 1: Clarification

**Status: MANDATORY — never skip this step.**

Before any implementation, ask extensive clarifying questions. This is the most critical step in the entire process. Think like a senior staff engineer approaching a new problem from first principles.

## Why Clarification Is Non-Negotiable

Implementation is easy. Understanding the requirement correctly is the hard part. A skill graph built on misunderstood requirements is worse than no skill graph at all — it actively misleads.

## When to Ask Questions

- **At the very beginning** — Before any other work happens
- **During research** — When findings raise new questions
- **During planning** — When decomposition decisions require domain insight
- **During implementation** — When ambiguity is discovered in reference content
- **During iteration** — When user feedback reveals gaps in understanding

Questions are not limited to step 1. They can and should happen at any point.

## How to Ask

Apply [domain classification](domain-classification.md) first, then the [questionnaire framework](../questionnaire-framework/overview.md):

1. Classify the domain — determine the subjectivity, technical depth, scope, novelty, and coding density
2. For high-subjectivity domains: ask for examples, references, taste preferences BEFORE technical stack questions
3. Use the [subjective-vs-objective framework](../questionnaire-framework/subjective-vs-objective.md) to decide question depth per area
4. Start with scope and boundaries — what is in and out of scope
5. Identify technical constraints — what tools, languages, platforms are involved
6. Understand quality requirements — what level of detail, correctness, coverage is expected
7. Probe for implicit requirements — what the user assumes but hasn't stated
8. Challenge your own assumptions — what do you think you know that might be wrong

## Rules

1. Do not ask more than 3–5 questions in a single message — avoid overwhelming the user
2. Start with the most critical questions first
3. Follow up based on answers — each answer may reveal new questions
4. Continue until all relevant uncertainties are resolved
5. Document answers as they will inform the graph structure
6. Never ask only technical questions for a design-heavy project — this is an anti-pattern

## Back to

- [Creation process overview](overview.md)
- See also: [Questionnaire framework](../questionnaire-framework/overview.md) — detailed thinking model for question generation
