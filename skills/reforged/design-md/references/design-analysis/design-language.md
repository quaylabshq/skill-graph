# Design Language Translation

The core value of this skill: converting technical CSS/Tailwind values into descriptive, designer-friendly prose that Stitch can interpret.

## Translation Rules

### Geometry & Shape

| Technical Value | Descriptive Translation |
|-----------------|------------------------|
| `rounded-full` | "Pill-shaped" or "Fully circular" |
| `rounded-xl` / `rounded-2xl` | "Generously rounded corners" |
| `rounded-lg` | "Subtly rounded corners" |
| `rounded-md` | "Gently softened corners" |
| `rounded-sm` | "Barely perceptible rounding" |
| `rounded-none` | "Sharp, squared-off edges" |

### Shadows & Depth

| Technical Value | Descriptive Translation |
|-----------------|------------------------|
| No shadow | "Flat, shadowless" |
| `shadow-sm` | "Whisper-soft diffused shadow" |
| `shadow` / `shadow-md` | "Gentle depth shadow" |
| `shadow-lg` | "Pronounced floating shadow" |
| `shadow-xl` / `shadow-2xl` | "Heavy, high-contrast drop shadow" |

### Spacing & Whitespace

| Pattern | Descriptive Translation |
|---------|------------------------|
| Tight spacing (4-8px) | "Compact, information-dense" |
| Moderate spacing (16-24px) | "Comfortable breathing room" |
| Generous spacing (32-64px) | "Expansive whitespace, gallery-like" |
| Section gaps (80-128px) | "Dramatic breathing room between sections" |

### Color Naming Convention

Never use bare color names. Always combine three elements:

1. **Descriptive name** — evocative, conveying character: "Deep Muted Teal-Navy", "Warm Barely-There Cream"
2. **Hex code** — exact value in parentheses: (#294056)
3. **Functional role** — what it's used for: "Used for primary call-to-action buttons"

**Example**: "Deep Muted Teal-Navy (#294056) — Used exclusively for primary call-to-action buttons and active navigation states"

### Typography Description

Describe fonts by their visual character, not just their name:
- "Modern geometric sans-serif with gentle humanist warmth" (not just "Manrope")
- "Semi-bold weight (600) with subtle letter-spacing for refined elegance" (not just "font-semibold tracking-wide")

## Anti-Patterns

- "Blue button" → "Ocean-deep Cerulean (#0077B6) button with pill-shaped edges"
- "rounded corners" → "Subtly rounded corners creating approachable, modern edges"
- "some shadow" → "Whisper-soft diffused shadow appearing on hover (0 2px 8px rgba(0,0,0,0.06))"
- "large gap" → "Generous 5-8rem vertical breathing room between major sections"

## Back to

- [Design analysis overview](overview.md)
- See also: [Writing rules](../output/writing-rules.md) — output-level language guidelines
