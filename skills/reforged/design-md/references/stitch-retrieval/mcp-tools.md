# Stitch MCP Tool Reference

Detailed signatures and usage for each Stitch MCP Server tool used in the retrieval workflow.

## Tool Discovery

```
list_tools
```
Returns all available MCP tools. Look for the Stitch prefix (e.g., `mcp_stitch:`, `stitch:`). This prefix varies by installation.

## list_projects

```
[prefix]:list_projects(filter: "view=owned")
```

- **Purpose**: Retrieve all user-owned projects
- **Key fields**: `name` (contains Project ID), `title`, `description`
- **ID extraction**: Parse numeric ID from `name` field: `projects/13534454087919359824` → `13534454087919359824`

## list_screens

```
[prefix]:list_screens(projectId: "<numeric_id>")
```

- **Purpose**: List all screens in a project
- **Input**: Numeric project ID only (not full path)
- **Key fields**: `name` (contains Screen ID), `title`, `width`, `height`

## get_screen

```
[prefix]:get_screen(projectId: "<numeric_id>", screenId: "<numeric_id>")
```

- **Purpose**: Get complete screen object with download URLs
- **Input**: Both IDs as numeric strings only
- **Returns**:
  - `screenshot.downloadUrl` — Visual reference image
  - `htmlCode.downloadUrl` — Full HTML/CSS source code
  - `width`, `height` — Screen dimensions
  - `deviceType` — Target platform (mobile, tablet, desktop)

## get_project

```
[prefix]:get_project(name: "projects/<numeric_id>")
```

- **Purpose**: Get project-level metadata and design theme
- **Input**: Full path format (`projects/{id}`), not just numeric ID
- **Returns**:
  - `designTheme.colorMode` — Light/dark mode
  - `designTheme.fonts` — Font family definitions
  - `designTheme.roundness` — Corner radius settings
  - `designTheme.customColors` — Brand color definitions
  - `description` — Project-level design guidelines

## Asset Download

```
web_fetch(url: "<downloadUrl>")
```

Use `web_fetch` or `read_url_content` to download HTML from `htmlCode.downloadUrl`. Parse the returned HTML for:
- Tailwind utility classes (colors, spacing, typography, borders)
- Custom CSS properties and variables
- Component structure and nesting patterns
- Inline styles and overrides

## Back to

- [Retrieval overview](overview.md)
