# Step 8: Iterate

After testing the skill graph, users may request improvements. Iteration often happens right after using the skill, with fresh context of how it performed.

## Iteration Workflow

1. Use the skill graph on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md, reference files, or scripts should be updated
4. Implement changes
5. Re-validate and re-package

## Common Iteration Patterns

- **Missing reference**: A topic came up that isn't covered → add a new reference file and link it
- **Overly broad reference**: A reference file covers too much → split it using [decomposition](../graph-architecture/decomposition.md)
- **Broken interlinking**: Related files don't cross-reference each other → add "See also" links
- **New extension**: A new capability is needed → implement from [extension points](../graph-architecture/extension-points.md)
- **Stale content**: Information is outdated → update the specific reference file

## Rules

1. Every change must maintain graph integrity — run `validate_graph.py` after changes
2. New files must be linked from existing hubs or the index
3. If iteration reveals misunderstood requirements, return to [step 1: clarification](step-1-clarification.md)

## Back to

- [Creation process overview](overview.md)
- See also: [Extension points](../graph-architecture/extension-points.md)
