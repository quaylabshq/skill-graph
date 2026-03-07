# Per-Section Analysis Guidance

Each section of the DESIGN.md requires a different analysis focus. This guide covers what to extract and how to describe each section.

## 1. Visual Theme & Atmosphere

**Source**: Screenshot + overall HTML structure
**Analysis focus**: Mood, density, aesthetic philosophy

- Evaluate the screenshot holistically before diving into details
- Use evocative adjective pairs: "Airy yet grounded", "Sophisticated minimalist", "Dense and utilitarian"
- Describe the space: gallery-like, information-dense, editorial, playful
- Note the photography-to-UI ratio and how content is prioritized
- Capture what emotional response the design evokes

## 2. Color Palette & Roles

**Source**: `designTheme.customColors`, Tailwind classes, inline styles
**Analysis focus**: Descriptive naming, hex precision, functional mapping

- Group colors by function: foundation, accent/interactive, text hierarchy, functional states
- Assign evocative descriptive names (not "primary blue" but "Deep Muted Teal-Navy")
- Always pair descriptive names with exact hex codes
- Document each color's specific functional role in the UI
- Note color relationships (complementary, analogous, monochromatic)

## 3. Typography Rules

**Source**: `designTheme.fonts`, CSS font declarations, Tailwind typography classes
**Analysis focus**: Font character, weight hierarchy, spacing patterns

- Describe the font family's visual character, not just its name
- Map the full weight hierarchy: display → headers → body → small text → CTAs
- Document letter-spacing and line-height conventions per level
- Note vertical rhythm patterns between text blocks

## 4. Component Stylings

**Source**: HTML component structure, Tailwind utility classes, CSS
**Analysis focus**: Shape, color, interaction states, composition

Cover these components (when present):
- **Buttons**: Shape (using [design-language.md](design-language.md) translations), color assignment, padding, hover/focus states
- **Cards/Containers**: Corner style, background, shadow behavior, internal padding, image treatment
- **Navigation**: Layout, typography treatment, active/hover states, mobile behavior
- **Inputs/Forms**: Border style, background, focus states, padding, placeholder treatment
- **Specific patterns**: Product cards, hero sections, or other domain-specific components

## 5. Layout Principles

**Source**: CSS grid/flexbox, Tailwind layout classes, responsive breakpoints
**Analysis focus**: Grid structure, whitespace strategy, responsive behavior

- Document the max content width and grid column count
- Describe the whitespace strategy using descriptive language (see [design-language.md](design-language.md))
- Map responsive breakpoints and how layout adapts
- Note alignment conventions (left/center/right) and when each is used
- Document the base spacing unit and vertical rhythm

## 6. Stitch Generation Notes (Optional)

**Purpose**: Translate the design system into reusable Stitch prompting snippets
**When to include**: When the DESIGN.md will be actively used to prompt Stitch for new screens

- Provide ready-to-use language snippets for common components
- Reference the descriptive names with hex codes consistently
- Include atmosphere keywords for overall screen generation
- Document incremental iteration patterns

## Back to

- [Design analysis overview](overview.md)
- See also: [Output format template](../output/overview.md) — how these sections map to the output
