# Domain Classification

The first action before any planning begins. Classify the task's domain profile to drive all downstream behavior — which questions to ask, what to research, how detailed the plan should be.

## Domain Profile Axes

Classify each as high, medium, or low:

| Axis | Question | High | Low |
|------|----------|------|-----|
| Technical depth | How much engineering complexity? | Complex systems, many constraints | Straightforward, well-known patterns |
| Subjectivity | How much depends on user taste? | Design, UX, aesthetics matter | Correct answers exist |
| Scope | How many distinct areas? | Broad, many components | Narrow, focused |
| Novelty | Established or emerging domain? | Few known patterns | Mature, known solutions |
| Codebase relevance | Is there existing code to understand? | Deep existing codebase | Greenfield or non-code |

## Profile Drives Behavior

| Profile | Effect on Planning |
|---------|-------------------|
| High-technical | Deep codebase exploration, architecture-focused plan, dependency mapping |
| High-subjectivity | Extensive preference gathering, example-driven questioning, design validation |
| High-scope | Aggressive decomposition, phased plan, more subtasks |
| High-novelty | Extended research phase, more exploratory questions, fewer assumptions |
| Low codebase-relevance | Web research replaces codebase exploration |

## Complexity Assessment

The classification also determines **plan depth**:

| Complexity | Indicators | Plan Depth |
|------------|------------|------------|
| Simple | 1-2 files, clear approach, known pattern | Lightweight — summary + steps list |
| Moderate | 3-10 files, some decisions needed, known domain | Standard — full core template |
| Complex | 10+ files, architectural decisions, multiple approaches | Detailed — core template + all adaptive sections |

## Classification Process

1. Read the user's initial request
2. Identify signals: keywords, implied complexity, domain indicators
3. Rate each axis (high/medium/low)
4. Determine complexity tier (simple/moderate/complex)
5. Present classification to the user: "Based on your request, I'm classifying this as [profile]. Does that match?"
6. Adjust based on feedback

## Rules

- Classification happens BEFORE any questions are asked
- The classification determines WHICH question categories get deep probing
- Always validate the classification with the user
- Reclassify if new information changes the profile

## Back to

- [Planning process overview](overview.md)
- See also: [Domain adaptation](../questionnaire-framework/domain-adaptation.md)
