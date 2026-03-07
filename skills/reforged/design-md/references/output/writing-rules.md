# Writing Rules & Anti-Patterns

Language guidelines for DESIGN.md output. These rules ensure the document serves as an effective prompting reference for Stitch.

## Language Principles

1. **Be descriptive** — Use evocative, specific language. "Ocean-deep Cerulean (#0077B6)" not "blue"
2. **Be functional** — Always explain what each element is used for, not just what it looks like
3. **Be consistent** — Use the same terminology throughout the entire document
4. **Be visual** — Help readers visualize the design through descriptions alone
5. **Be precise** — Include exact values (hex codes, pixel values) in parentheses after natural language

## Anti-Patterns

| Instead of... | Write... |
|---------------|----------|
| "blue" or "rounded" | "Ocean-deep Cerulean (#0077B6)" or "Gently curved edges" |
| `rounded-xl` | "Generously rounded corners" |
| `shadow-sm` | "Whisper-soft diffused shadow" |
| `tracking-wide` | "Expanded letter-spacing for refined elegance" |
| "some space between sections" | "Generous 5-8rem vertical breathing room between major sections" |
| "the main color" | "Deep Muted Teal-Navy (#294056) — the sole vibrant accent, used exclusively for primary CTAs" |

## Best Practices

- **Start with the big picture** — Understand the overall aesthetic before diving into component details
- **Look for patterns** — Identify consistent spacing, sizing, and styling patterns across the design
- **Think semantically** — Name colors by their purpose and character, not just appearance
- **Consider hierarchy** — Document how visual weight and importance are communicated
- **Explain the "why"** — Go beyond listing values to explain design decisions and relationships

## Tips for Stitch-Optimized Language

- Stitch interprets "Visual Descriptions" — prefer natural language over technical specs
- Color descriptions should pair a mood-word with the hex: "Warm Barely-There Cream (#FCFAFA)"
- Component descriptions should include shape, color role, and interaction feel
- Atmosphere descriptions anchor the entire generation — invest time here

## Completeness Checklist

Before finalizing a DESIGN.md, verify:

- [ ] Every color has a descriptive name + hex code + functional role
- [ ] Typography describes font character, not just font name
- [ ] Component styles include shape, color, and interaction states
- [ ] Layout describes whitespace strategy, not just grid specs
- [ ] Atmosphere section uses evocative, specific adjectives
- [ ] No raw CSS class names appear without descriptive translation
- [ ] Consistent terminology used throughout

## Back to

- [Output overview](overview.md)
- See also: [Design language translation](../design-analysis/design-language.md) — translation reference tables
