# Skill Anatomy

Every skill graph consists of a required SKILL.md file and optional bundled resources.

## Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   ├── description: (required)
│   │   └── compatibility: (optional, rarely needed)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

## SKILL.md

Every SKILL.md consists of:

- **Frontmatter** (YAML): Contains `name` and `description` fields (required), plus optional `license`, `metadata`, and `compatibility`. Only `name` and `description` are read by Claude to determine when the skill triggers — be clear and comprehensive about what the skill is and when it should be used.
- **Body** (Markdown): In a skill graph, this is navigation-only — tables linking to reference files, scripts, and frameworks. No detailed content lives here.

### Frontmatter Rules

- `name`: kebab-case identifier (lowercase, digits, hyphens only, max 64 chars)
- `description`: Max 1024 chars. Must include both what the skill does AND specific triggers/contexts for when to use it. All "when to use" information goes here — not in the body.
- Do not include fields beyond `name`, `description`, `license`, `metadata`, and `compatibility`.

## Bundled Resources

### Scripts (`scripts/`)

Executable code for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by Claude for patching or environment-specific adjustments

### References (`references/`)

Documentation loaded as needed into context to inform Claude's process and thinking.

- **When to include**: For documentation that Claude should reference while working
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when Claude determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both

### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output Claude produces.

- **When to include**: When the skill needs files used in the final output
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents
- **Benefits**: Separates output resources from documentation

## What NOT to Include

A skill should only contain essential files. Do NOT create extraneous documentation:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md

The skill should only contain information needed for an AI agent to do the job. No auxiliary context about the creation process, setup procedures, or user-facing documentation.

## Back to

- [Core principles overview](overview.md)
- See also: [Graph architecture — index design](../graph-architecture/index-design.md)
