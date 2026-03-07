# Questionnaire Framework

This framework governs how and when to ask clarifying questions during skill graph creation. It is a **permanent step** — referenced from [step 1: clarification](../creation-process/step-1-clarification.md) and applicable throughout the entire creation process.

## Philosophy

Think like a senior staff engineer approaching a problem from first principles. Never assume. Never proceed with uncertainty. The cost of asking one more question is negligible compared to the cost of building on a misunderstanding.

## Core Rules

1. **Always ask before building** — No implementation begins before critical questions are answered
2. **Questions are not limited to the beginning** — They can and should happen at any point in the process
3. **3–5 questions per message** — Avoid overwhelming the user; start with the most critical
4. **Follow up on answers** — Each answer may reveal new questions
5. **Continue until uncertainty is resolved** — There is no "good enough" understanding

## Framework Components

| Component | Purpose | Reference |
|-----------|---------|-----------|
| Initial questions | General thinking model for upfront question generation | [initial-questions.md](initial-questions.md) |
| Mid-process questions | Identifying and addressing gaps discovered during work | [mid-process-questions.md](mid-process-questions.md) |
| First-principles thinking | The mental model that drives all question generation | [first-principles.md](first-principles.md) |
| Domain adaptation | Classify domain profile and adapt question strategy | [domain-adaptation.md](domain-adaptation.md) |
| Subjective vs objective | Distinguish taste decisions from engineering decisions | [subjective-vs-objective.md](subjective-vs-objective.md) |

## Core Rules (continued)

6. **Classify the domain BEFORE asking questions** — Classification drives question type and depth
7. **For subjective domains, ask 2-3x more preference/taste questions** than technical questions
8. **Never default on subjective decisions** — Always gather user preference

## When This Framework Activates

- **Step 1 (Clarification)** — Primary activation. Full upfront questioning.
- **Step 2 (Research)** — Research findings may raise new questions.
- **Step 3 (Understand)** — Gathering examples may reveal gaps.
- **Step 4 (Plan)** — Decomposition decisions may require domain insight.
- **Step 6 (Implement)** — Implementation may surface ambiguity.
- **Step 8 (Iterate)** — User feedback may reveal misunderstandings.

## See Also

- [Creation process — step 1](../creation-process/step-1-clarification.md) — where this framework is first invoked
- [First-principles thinking](first-principles.md) — the engine behind question generation
