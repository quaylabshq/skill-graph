# Step 6: Implement the Skill Graph

Write the skill's content following graph architecture principles. Remember: the skill is being created for another instance of Claude to use. Include information that would be beneficial and non-obvious.

## Implementation Order

1. **Write SKILL.md first** — The navigation index. Define all sections and links even before detail files exist. This serves as the blueprint.
2. **Write hub files** — `overview.md` files for each reference category. These establish the navigation within each category.
3. **Write detail files** — Individual reference files for each topic, feature, or step.
4. **Write scripts** — Executable code for deterministic tasks.
5. **Verify interlinking** — Every file must link back to its hub and across to related files.

## Writing Guidelines

- Use imperative/infinitive form throughout
- Apply [conciseness principles](../core-principles/conciseness.md) — only include what Claude doesn't already know
- Follow [degrees of freedom](../core-principles/degrees-of-freedom.md) — match specificity to task fragility
- Consult design patterns as needed:
  - **Multi-step processes**: See [workflows.md](../workflows.md)
  - **Specific output formats**: See [output-patterns.md](../output-patterns.md)

## SKILL.md Frontmatter

Write the YAML frontmatter with `name` and `description`:

- `name`: kebab-case skill name
- `description`: Primary triggering mechanism. Include both what the skill does AND specific triggers/contexts for when to use it. All "when to use" information goes here — not in the body.

Do not include any other fields in YAML frontmatter.

## Script Requirements

- Added scripts must be tested by running them
- If there are many similar scripts, test a representative sample
- Delete any example files not needed for the skill

## Context Delegation

For research-heavy implementation, delegate exploration to sub-contexts rather than loading everything into the main thread:

- Use targeted tool calls (searches, reads) to gather specific information
- Bring back synthesized findings — not raw results
- Keep the main implementation context focused on writing files
- See [context management](../graph-architecture/context-management.md) for delegation strategies

For subjective domains: show early output (first reference file, first design decision) to the user for direction validation before completing all files. See [feedback checkpoints](feedback-checkpoints.md).

## Graph Integrity Checks

Before moving to packaging, verify:

- Every file in `references/` is linked from SKILL.md or a hub file
- Every hub file links to all files in its directory
- Every detail file has a "Back to" section
- SKILL.md is under 100 lines
- No duplicate content across files
- **One-shot test**: For each reference file, verify that loading only this file + SKILL.md is sufficient to complete the related subtask. See [one-shot design](../core-principles/one-shot-design.md).

## User Input

This step may require user input. Examples:

- Brand assets to store in `assets/`
- API documentation to store in `references/`
- Configuration templates or schemas

If new questions arise during implementation, return to [step 1: clarification](step-1-clarification.md).

## Back to

- [Creation process overview](overview.md)
- See also: [Graph architecture](../graph-architecture/overview.md) — structural principles
- See also: [Index design](../graph-architecture/index-design.md) — how to write the navigation index
- See also: [Interlinking](../graph-architecture/interlinking.md) — how to connect files
