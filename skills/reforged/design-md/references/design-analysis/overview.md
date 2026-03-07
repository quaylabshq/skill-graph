# Design Analysis Process

After retrieving Stitch project data, analyze the design elements and synthesize them into a semantic design system. The goal: translate technical implementation into descriptive, designer-friendly language.

## Analysis Pipeline

1. **Extract project identity** — Project title and ID from the JSON metadata
2. **Define the atmosphere** — Evaluate screenshot + HTML structure to capture the overall "vibe" using evocative adjectives (e.g., "Airy," "Minimalist," "Dense," "Utilitarian")
3. **Map the color palette** — Extract colors from Tailwind config, designTheme, and HTML. Assign descriptive names, hex codes, and functional roles
4. **Catalog typography** — Identify font families, weight hierarchy, letter-spacing patterns, and line-height conventions
5. **Document component styles** — Analyze buttons, cards, forms, navigation for shape, color, hover states, and layout behavior
6. **Describe layout principles** — Capture grid structure, whitespace strategy, responsive breakpoints, and alignment rules

## Core Principle

Stitch interprets design through **visual descriptions** supported by specific color values. Every analysis must produce language that Stitch can act on — descriptive prose paired with exact hex codes.

## What Makes Good Analysis

- Captures the "why" behind design decisions, not just the "what"
- Uses evocative, specific language (not generic terms)
- Includes exact values (hex codes, pixel values) alongside descriptions
- Identifies patterns and consistency across components
- Notes hierarchy and visual weight relationships

For the translation methodology, see [design-language.md](design-language.md).
For per-section guidance, see [section-guides.md](section-guides.md).

## Back to

- [SKILL.md](../../SKILL.md)
- See also: [Stitch retrieval](../stitch-retrieval/overview.md) — how to get the data for analysis
- See also: [Output format](../output/overview.md) — how to structure the final output
