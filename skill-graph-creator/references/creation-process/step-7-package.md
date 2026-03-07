# Step 7: Package the Skill Graph

Once development is complete, package the skill graph into a distributable .skill file.

## Running the Packager

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Optional output directory:

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

## What the Packager Does

1. **Validates** the skill graph automatically by running `validate_graph.py`, checking:
   - YAML frontmatter format and required fields
   - Naming conventions and directory structure
   - Description completeness
   - Graph structure: link integrity, orphan detection, index size
2. **Packages** the skill if validation passes, creating a `.skill` file (zip with .skill extension) that includes all files and maintains proper directory structure

## If Validation Fails

The script reports errors and exits without creating a package. Fix validation errors and run the command again.

## Back to

- [Creation process overview](overview.md)
