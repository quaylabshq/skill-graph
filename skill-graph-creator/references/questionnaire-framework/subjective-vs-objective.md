# Subjective vs Objective Decisions

Not all decisions are equal. Some have correct answers. Some depend entirely on taste. The questioning strategy must differ for each type.

## Decision Types

### Objective Decisions

Have a correct or commonly accepted answer. Safe to default if user has no preference.

Examples: file formats, API protocols, data structures, security patterns, error handling strategies, database choices for known workloads.

Question template: "Should we use X or Y?" — offer best practice as default.

### Subjective Decisions

No single correct answer. Depends entirely on user taste, context, and preference. MUST gather user preferences. Never default.

Examples: visual style, interaction patterns, naming aesthetics, content tone, layout choices, color palettes, typography selection, animation behavior, brand voice.

Question templates:
- "Can you show me examples of what you like?"
- "Describe the feeling you want this to evoke."
- "What existing products match your taste?"
- "What should this NOT look like?"

### Mixed Decisions

Have technical constraints but also taste components. Present the constraints, then ask for preference within those bounds.

Examples: color schemes (accessibility constraints + preference), typography (readability + style), animation (performance + feel), component density (usability + aesthetic).

Question template: "Here's what works technically — which direction matches your preference?"

## Rules

1. For any decision classified as subjective, asking "which framework?" is insufficient — ask "what should it look/feel/read like?"
2. Never assume subjective preferences — always ask
3. For objective decisions with no user preference, default to best practice and move on
4. For mixed decisions, present the constraint boundary first, then ask for taste within it
5. When uncertain whether a decision is subjective or objective, treat it as subjective and ask

## Back to

- [Questionnaire framework overview](overview.md)
- See also: [Domain adaptation](domain-adaptation.md)
