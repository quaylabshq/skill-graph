# Output Format & Template

The DESIGN.md output follows a fixed structure. Every generated file must use this template.

## DESIGN.md Template

```markdown
# Design System: [Project Title]
**Project ID:** [Numeric Project ID]

## 1. Visual Theme & Atmosphere
[Mood, density, aesthetic philosophy. Evocative adjectives. Space description.]

## 2. Color Palette & Roles
[Colors grouped by function. Each entry: Descriptive Name + (Hex Code) + Functional Role.]

### Primary Foundation
- **[Name]** ([hex]) — [role]

### Accent & Interactive
- **[Name]** ([hex]) — [role]

### Typography & Text Hierarchy
- **[Name]** ([hex]) — [role]

### Functional States
- **[Name]** ([hex]) — [role]

## 3. Typography Rules
[Font family character description. Weight hierarchy. Letter-spacing. Line-height. Vertical rhythm.]

## 4. Component Stylings
* **Buttons:** [Shape, color, padding, hover/focus states]
* **Cards/Containers:** [Corners, background, shadow, padding, image treatment]
* **Navigation:** [Layout, typography, states, mobile behavior]
* **Inputs/Forms:** [Border, background, focus, padding]
* **[Domain-specific components]:** [As needed]

## 5. Layout Principles
[Grid structure. Whitespace strategy. Responsive breakpoints. Alignment. Spacing units.]

## 6. Design System Notes for Stitch Generation (Optional)
[Ready-to-use language snippets. Atmosphere keywords. Component prompts. Iteration patterns.]
```

## Output Rules

1. **File name**: Always `DESIGN.md`
2. **Location**: Project root directory
3. **Sections 1-5**: Required for every output
4. **Section 6**: Include when the DESIGN.md will be used for ongoing Stitch generation
5. **Color subsections**: Group by function (foundation, accent, text, states)
6. **Component list**: Include all components found; omit sections for absent components

## Reference Example

See [assets/example-design.md](../../assets/example-design.md) for a complete output example (furniture collection project).

For language and writing guidelines, see [writing-rules.md](writing-rules.md).

## Back to

- [SKILL.md](../../SKILL.md)
- See also: [Section guides](../design-analysis/section-guides.md) — how to analyze content for each section
