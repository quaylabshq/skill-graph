# Domain Adaptation

Adapt question depth, type, and strategy based on the domain profile of the task. Generic questions produce generic skill graphs.

## Domain Classification Model

Every task has a domain profile along these axes (classify each as high/medium/low):

| Axis | High | Low |
|------|------|-----|
| Technical depth | Complex engineering, many constraints | Straightforward, well-known patterns |
| Subjectivity | Taste, aesthetics, style matter heavily | Correct answers exist, preferences secondary |
| Scope | Many distinct feature areas | Narrow, focused capability |
| Novelty | Emerging domain, few established patterns | Mature domain, known solutions |
| Coding density | Primarily code-driven | Includes design, content, workflow |

## Adaptation Rules

### High-Subjectivity Domains (design, UX, branding, content)

Ask taste/preference/example questions BEFORE any technical questions:

- "Can you show me examples of what you like?"
- "What existing products match your taste?"
- "What aesthetic direction — minimal, bold, playful, corporate?"
- "What should it feel like to use?"
- "What should it NOT look like?"

Subjective domains require 2-3x more questions in the preference/taste category than technical domains.

### High-Technical Domains (backend, infrastructure, data pipelines)

Lean on established best-practice defaults but still offer preference input:

- "The standard approach for this is X — do you have a different preference?"
- Present defaults with the option to override

### Mixed Domains (full-stack, product builds)

Interleave both subjective and technical questions. Don't front-load one category — alternate to build a complete picture.

## Concrete Signals

If the user mentions any of these words, immediately classify as high-subjectivity and shift questioning strategy:

- "design", "look", "feel", "style", "brand", "beautiful", "clean", "modern", "aesthetic", "vibe", "tone", "elegant", "minimal", "bold"

## Anti-Patterns

- Asking only stack/tooling questions for a design-heavy project
- Defaulting on subjective decisions without asking the user
- Treating all domains identically regardless of subjectivity level
- Asking "which framework?" when you should ask "what should it feel like?"

## Back to

- [Questionnaire framework overview](overview.md)
- See also: [Subjective vs objective](subjective-vs-objective.md)
- See also: [Domain classification step](../creation-process/domain-classification.md)
