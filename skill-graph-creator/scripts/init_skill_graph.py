#!/usr/bin/env python3
"""
Skill Graph Initializer - Creates a new skill graph from template

Usage:
    init_skill_graph.py <skill-name> --path <path>

Examples:
    init_skill_graph.py my-api-skill --path skills/public
    init_skill_graph.py data-pipeline --path skills/private
    init_skill_graph.py custom-skill --path /custom/location
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

This skill provides a navigable reference graph for [TODO: domain]. All detailed content lives in reference files and tool scripts — this file contains only navigation.

## [TODO: Feature Category 1]

[TODO: Short contextual sentence about this category.]

| Topic | Reference |
|-------|-----------|
| [TODO: Feature A] | [references/feature-a.md](references/feature-a.md) |
| [TODO: Feature B] | [references/feature-b.md](references/feature-b.md) |

## [TODO: Feature Category 2]

| Topic | Reference |
|-------|-----------|
| [TODO: Feature C] | [references/feature-c.md](references/feature-c.md) |

## Tool Scripts

| Tool | Script | Purpose |
|------|--------|---------|
| [TODO: Tool name] | [scripts/example.py](scripts/example.py) | [TODO: One-line purpose] |

## [TODO: Extensions / Future Skills]

See [references/extensions.md](references/extensions.md) for planned capabilities.
"""

EXAMPLE_OVERVIEW = """# [TODO: Category] Overview

[TODO: Short description of this category and what it covers.]

## Topics

| Topic | Summary | Reference |
|-------|---------|-----------|
| [TODO: Topic A] | [TODO: One-line summary] | [feature-a.md](feature-a.md) |
| [TODO: Topic B] | [TODO: One-line summary] | [feature-b.md](feature-b.md) |

## See Also

- [TODO: Link to related category overview]
"""

EXAMPLE_REFERENCE = """# [TODO: Feature Name]

[TODO: Detailed content for this feature. This is where implementation details, examples, and guidance live.]

## [TODO: Section 1]

[TODO: Content]

## [TODO: Section 2]

[TODO: Content]

## Back to

- [Category overview](overview.md)
"""

EXAMPLE_EXTENSIONS = """# Future Extensions

Planned capabilities that can be implemented as additional reference files or tool scripts.

## Planned

### 1. [TODO: Extension Name]
- **Type**: [TODO: Tool skill (script) / Reference / Asset]
- **Purpose**: [TODO: What this extension would add]
- **Implementation pattern**: Add `scripts/<name>.py` and/or `references/<name>.md`, then update SKILL.md index

## Implementation Pattern

Each extension should follow this structure:
```
scripts/<name>.py       # Executable tool script (if needed)
references/<name>.md    # Reference documentation (if needed)
```

Update SKILL.md to include new links when implementing an extension.
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example helper script for {skill_name}

This is a placeholder script. Replace with actual implementation or delete if not needed.
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here

if __name__ == "__main__":
    main()
'''


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill_graph(skill_name, path):
    """
    Initialize a new skill graph directory with graph-structured templates.

    Args:
        skill_name: Name of the skill (kebab-case)
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"Error: Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

    # Create SKILL.md (navigation-only index)
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("Created SKILL.md (navigation index)")
    except Exception as e:
        print(f"Error creating SKILL.md: {e}")
        return None

    # Create graph-structured references
    try:
        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)

        # Create hub overview file
        overview_path = references_dir / 'overview.md'
        overview_path.write_text(EXAMPLE_OVERVIEW)
        print("Created references/overview.md (hub)")

        # Create example detail file
        feature_path = references_dir / 'feature-a.md'
        feature_path.write_text(EXAMPLE_REFERENCE)
        print("Created references/feature-a.md (example detail)")

        # Create extensions file
        extensions_path = references_dir / 'extensions.md'
        extensions_path.write_text(EXAMPLE_EXTENSIONS)
        print("Created references/extensions.md (extension points)")

    except Exception as e:
        print(f"Error creating references: {e}")
        return None

    # Create scripts directory with example
    try:
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)

        example_script = scripts_dir / 'example.py'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("Created scripts/example.py")
    except Exception as e:
        print(f"Error creating scripts: {e}")
        return None

    print(f"\nSkill graph '{skill_name}' initialized at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md to replace TODO items with actual feature categories and links")
    print("2. Create reference files for each feature (one file per topic)")
    print("3. Create hub overview.md files if grouping references into subdirectories")
    print("4. Ensure all files are interlinked (hubs link down, details link back up)")
    print("5. Delete example files that don't apply")
    print("6. Run validate_graph.py to check graph integrity")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill_graph.py <skill-name> --path <path>")
        print("\nSkill name requirements:")
        print("  - Kebab-case identifier (e.g., 'my-data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 64 characters")
        print("\nExamples:")
        print("  init_skill_graph.py my-new-skill --path skills/public")
        print("  init_skill_graph.py my-api-helper --path skills/private")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"Initializing skill graph: {skill_name}")
    print(f"   Location: {path}")
    print()

    result = init_skill_graph(skill_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
