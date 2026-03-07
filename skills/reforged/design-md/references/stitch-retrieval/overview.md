# Stitch Retrieval Workflow

To analyze a Stitch project, retrieve screen metadata and design assets via the Stitch MCP Server in this order:

## Workflow Steps

1. **Namespace discovery** — Run `list_tools` to find the Stitch MCP prefix (e.g., `mcp_stitch:`). Use this prefix for all subsequent calls.

2. **Project lookup** (if Project ID not provided) — Call `[prefix]:list_projects` with `filter: "view=owned"`. Identify the target by title or URL. Extract the Project ID from the `name` field (e.g., `projects/13534454087919359824`).

3. **Screen lookup** (if Screen ID not provided) — Call `[prefix]:list_screens` with the numeric `projectId`. Review screen titles to find the target. Extract the Screen ID from the screen's `name` field.

4. **Metadata fetch** — Call `[prefix]:get_screen` with both `projectId` and `screenId` (numeric IDs only). Returns: `screenshot.downloadUrl`, `htmlCode.downloadUrl`, dimensions, device type, and project metadata including `designTheme`.

5. **Asset download** — Use `web_fetch` to download HTML code from `htmlCode.downloadUrl`. Optionally download the screenshot. Parse the HTML to extract Tailwind classes, custom CSS, and component patterns.

6. **Project metadata extraction** — Call `[prefix]:get_project` with full path (`projects/{id}`) to get `designTheme` object with color mode, fonts, roundness, custom colors, and project-level design guidelines.

## Key Data Points to Extract

- **From screen**: HTML/CSS source, screenshot, dimensions, device type
- **From designTheme**: Color mode, font families, roundness values, custom color definitions
- **From HTML parsing**: Tailwind utility classes, custom CSS properties, component structure

For detailed MCP tool signatures, see [mcp-tools.md](mcp-tools.md).

## Back to

- [SKILL.md](../../SKILL.md)
- See also: [Design analysis overview](../design-analysis/overview.md) — what to do with the retrieved data
