---
name: design-md
description: Analyze Stitch projects via MCP Server and synthesize semantic design systems into DESIGN.md files. Use when creating a DESIGN.md to capture an existing Stitch project's visual language — colors, typography, component styles, layout principles — in descriptive, designer-friendly prose with exact hex values. Requires access to Stitch MCP Server. Produces a single DESIGN.md that serves as the source of truth for prompting Stitch to generate new screens aligned with the existing design language.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
  - "web_fetch"
---

# Stitch DESIGN.md Skill Graph

This skill provides a navigable reference graph for creating semantic design system documentation from Stitch projects. All detailed content lives in reference files — this file contains only navigation.

## Stitch Retrieval

How to fetch project data from the Stitch MCP Server:

| Topic | Reference |
|-------|-----------|
| Retrieval workflow overview | [references/stitch-retrieval/overview.md](references/stitch-retrieval/overview.md) |
| MCP tool signatures & usage | [references/stitch-retrieval/mcp-tools.md](references/stitch-retrieval/mcp-tools.md) |

## Design Analysis

How to analyze and translate design elements into descriptive language:

| Topic | Reference |
|-------|-----------|
| Analysis process overview | [references/design-analysis/overview.md](references/design-analysis/overview.md) |
| Technical-to-descriptive translation | [references/design-analysis/design-language.md](references/design-analysis/design-language.md) |
| Per-section analysis guidance | [references/design-analysis/section-guides.md](references/design-analysis/section-guides.md) |

## Output Format

How to structure and write the DESIGN.md output:

| Topic | Reference |
|-------|-----------|
| Output format & template | [references/output/overview.md](references/output/overview.md) |
| Writing rules & anti-patterns | [references/output/writing-rules.md](references/output/writing-rules.md) |

## Example Output

| Asset | Purpose |
|-------|---------|
| [assets/example-design.md](assets/example-design.md) | Complete DESIGN.md example (furniture collection project) |

## Tool Scripts

| Tool | Script | Purpose |
|------|--------|---------|
| Validate | [scripts/validate_design_md.py](scripts/validate_design_md.py) | Validate DESIGN.md structure and completeness |

## Future Extensions

See [references/future-extensions.md](references/future-extensions.md) for planned capabilities.
