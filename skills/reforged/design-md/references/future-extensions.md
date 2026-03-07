# Future Extensions

Planned capabilities that can extend the design-md skill graph.

## Planned

### 1. Multi-Screen Analysis
- **Type**: Reference + workflow extension
- **Purpose**: Analyze multiple screens from a project simultaneously to build a more comprehensive design system
- **Operations**: Batch screen retrieval, cross-screen pattern detection, component consistency verification
- **Implementation**: Add `references/multi-screen-analysis.md` and update retrieval workflow

### 2. Design Diff
- **Type**: Tool skill (script)
- **Purpose**: Compare two versions of a design or two screens to highlight differences
- **Operations**: Color delta detection, typography changes, layout shifts
- **Implementation**: Add `scripts/diff_designs.py`, create `references/design-diff.md`

### 3. Figma/Screenshot Source
- **Type**: Reference + alternative retrieval workflow
- **Purpose**: Generate DESIGN.md from non-Stitch sources (Figma exports, screenshots, raw HTML)
- **Operations**: Image analysis, CSS extraction from static files, manual color picking
- **Implementation**: Add `references/alternative-sources/` hub with per-source retrieval guides

### 4. Design Token Export
- **Type**: Tool skill (script)
- **Purpose**: Export the semantic design system as machine-readable design tokens (JSON/CSS custom properties)
- **Operations**: Parse DESIGN.md, generate tokens file, validate token completeness
- **Implementation**: Add `scripts/export_tokens.py`

### 5. Component Library Integration
- **Type**: Reference extension
- **Purpose**: Map design system to specific component library implementations (shadcn/ui, Material, etc.)
- **Operations**: Component mapping, prop translation, theme configuration generation
- **Implementation**: Add `references/component-libraries/` hub

## Implementation Pattern

Each extension should follow this structure:
- `scripts/<name>.py` (if tool skill)
- `references/<name>.md` or `references/<name>/overview.md` (if reference needed)
- Update `SKILL.md` index to include new links
- Validate with `validate_graph.py` after adding

## Back to

- [SKILL.md](../SKILL.md)
