# Domain Classification

The first action in any skill graph creation. Classify the task's domain profile to drive all downstream behavior — which questions to ask, how deeply to probe, and what to prioritize.

## Domain Profile Axes

Classify each as high, medium, or low:

| Axis | Question | High | Low |
|------|----------|------|-----|
| Technical depth | How much engineering complexity? | Complex systems, many constraints | Straightforward, well-known patterns |
| Subjectivity | How much depends on user taste? | Visual style, tone, aesthetics matter | Correct answers exist |
| Scope | How many distinct feature areas? | Broad, many capabilities | Narrow, focused |
| Novelty | Established or emerging domain? | Few known patterns, custom solutions | Mature, known best practices |
| Coding density | Primarily code, or broader? | Almost entirely code | Includes design, content, workflow |

## Profile Drives Behavior

| Profile | Downstream Effect |
|---------|-------------------|
| High-subjectivity | Deep preference gathering, example-driven questioning, show-and-validate workflow at checkpoints |
| High-technical | Best-practice defaults, focus on constraints and integration, less preference probing |
| High-scope | Aggressive decomposition, more reference files, sub-hubs likely |
| High-novelty | Extended research phase, more exploratory questions, fewer assumptions |
| Low coding-density | Workflow-focused references, not just code scripts; include design and content guidance |

## Classification Process

1. Read the user's initial request
2. Identify signals: keywords, implied complexity, domain indicators
3. Rate each axis (high/medium/low)
4. Present the classification to the user: "Based on your request, I'm classifying this as [profile]. Does that match?"
5. Adjust based on user feedback

## Rules

- Classification happens BEFORE any questions are asked
- The classification determines WHICH question categories get deep probing vs. light touch
- Always validate the classification with the user — they may see their task differently
- Reclassify if new information changes the profile (mid-process reclassification is valid)

## Back to

- [Creation process overview](overview.md)
- See also: [Domain adaptation](../questionnaire-framework/domain-adaptation.md)
