# Step 4: Generate Plan

Turn the research findings and decomposed subtasks into a structured implementation plan. Use the [core template](../output-format/core-template.md) as the foundation and add [adaptive sections](../output-format/adaptive-sections.md) based on the domain.

## Plan Generation Process

1. **Select plan depth** based on [domain classification](domain-classification.md):
   - Simple → summary + steps list only
   - Moderate → full core template
   - Complex → core template + all relevant adaptive sections

2. **Fill core template sections** (see [core-template.md](../output-format/core-template.md)):
   - Summary: one-paragraph overview of approach
   - Approach: key decisions and rationale
   - Implementation steps: ordered from decomposition
   - Files affected: from codebase research (if applicable)

3. **Add adaptive sections** as needed (see [adaptive-sections.md](../output-format/adaptive-sections.md)):
   - Architecture decisions for complex systems
   - Risk assessment for high-stakes tasks
   - Testing strategy for code tasks
   - Alternatives considered for novel domains

4. **Map dependencies** into the step ordering:
   - Independent steps can be labeled as parallelizable
   - Dependent steps are sequenced with explicit dependencies noted

5. **Estimate complexity signals** (not time):
   - Mark steps as "straightforward", "needs investigation", or "high-risk"
   - This helps the user understand where challenges are, without guessing duration

## Quality Checks

Before moving to presentation:

- Does every decomposed subtask appear in the plan?
- Does the plan address every concern raised during clarification?
- Does the plan incorporate research findings?
- Are the steps ordered correctly given dependencies?
- Is the detail level appropriate for the task complexity?

## Rules

1. Never generate a plan without completing steps 1-3 first
2. Use the output format framework — don't invent ad-hoc structures
3. If generating the plan reveals ambiguity, return to [step 1](step-1-clarification.md)
4. Do not include time estimates — use complexity signals instead

## Back to

- [Planning process overview](overview.md)
- See also: [Output format overview](../output-format/overview.md)
- See also: [Core template](../output-format/core-template.md)
- See also: [Adaptive sections](../output-format/adaptive-sections.md)
