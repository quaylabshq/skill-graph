# Step 5: Initialize the Skill Graph

Skip this step only if the skill being developed already exists and iteration or packaging is needed.

## Running the Initializer

When creating a new skill graph from scratch, always run the `init_skill_graph.py` script:

```bash
scripts/init_skill_graph.py <skill-name> --path <output-directory>
```

The script:

- Creates the skill graph directory at the specified path
- Generates a navigation-only SKILL.md template with TODO table placeholders
- Creates `references/` directory with a starter `overview.md`
- Creates `scripts/` directory with an example script
- Adds TODO markers indicating where to add feature references, script links, etc.

## After Initialization

1. Review the generated template structure
2. Compare against the plan from step 4
3. Add or remove directories as needed to match the planned graph structure
4. Delete any example files that don't apply

## Back to

- [Creation process overview](overview.md)
