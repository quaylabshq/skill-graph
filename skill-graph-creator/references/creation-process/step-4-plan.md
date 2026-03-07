# Step 4: Plan the Graph Structure & Resources

Turn concrete examples into a structured plan. This step determines both the reusable resources AND the graph architecture.

## Planning Reusable Resources

Analyze each concrete example by:

1. Considering how to execute the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Examples of this analysis:

- Rotating PDFs requires re-writing the same code → `scripts/rotate_pdf.py`
- Building frontend apps requires the same boilerplate → `assets/hello-world/`
- Querying BigQuery requires re-discovering schemas → `references/schema.md`

## Planning the Graph Structure

Using the [decomposition principles](../graph-architecture/decomposition.md), determine:

1. **What goes in the index** — Feature categories, script listings, reference links
2. **How to organize references** — By feature, domain, process step, or variant
3. **What becomes a hub** — Groupings that need their own overview file
4. **What becomes a detail file** — Individual features, steps, or topics
5. **What scripts are needed** — Deterministic, reusable code
6. **What extension points exist** — Planned future capabilities

## Decomposition Depth Assessment

Apply [recursive decomposition](../core-principles/problem-decomposition.md) to the planned structure:

1. For each planned reference file, ask: "Does this contain 2+ independent topics?" If yes, split.
2. Count decomposition levels. Use the [complexity assessment](../graph-architecture/decomposition.md) to gauge skill complexity:
   - 1–2 levels → simple skill, flat references
   - 3–4 levels → moderate, hub-and-spoke per category
   - 5+ levels → complex, consider sub-hubs or additional reference layers
3. Verify each planned file is atomic — it addresses one topic that can be understood independently.

## Context Budget Planning

Estimate context usage for common execution paths:

- SKILL.md (~100 lines) + 1 hub (~50 lines) + 2–3 detail files (~150 lines each) ≈ 600 lines — leaves ample room for conversation.
- If a common task requires loading 5+ detail files simultaneously, restructure to make files more self-contained.
- Apply the [one-shot test](../core-principles/one-shot-design.md): for each planned reference file, verify that loading only that file + SKILL.md is sufficient to complete the related subtask.
- See [context management](../graph-architecture/context-management.md) for delegation strategies when context budget is tight.

## Creating the Todo List

Use the [planning framework](../planning-framework/overview.md) to create a structured todo list:

1. List every file that needs to be created
2. List every script that needs to be written
3. Define the interlinking structure
4. Set completion criteria for each item

## Output

This step produces:

- A file tree of the planned skill graph
- A description of what each file contains
- A list of scripts with their purposes
- A todo list for implementation

## Rules

1. Plan the graph structure BEFORE writing any files
2. Verify the planned structure follows [graph invariants](../graph-architecture/overview.md)
3. Check that every planned file is reachable from SKILL.md within 2 hops
4. The plan may trigger return to step 1 if new questions arise

## Back to

- [Creation process overview](overview.md)
- See also: [Graph architecture — decomposition](../graph-architecture/decomposition.md)
- See also: [Planning framework](../planning-framework/overview.md)
