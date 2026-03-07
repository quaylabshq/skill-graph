# Step 9: Final Evaluation

A mandatory bird's-eye review of the entire skill graph. This is the LAST step before delivering to the user.

## When

After step 8 (iterate) or after step 7 (package) if no iteration was needed.

## Bird's-Eye Review

1. List all original requirements from step 1 (clarification)
2. For each requirement, verify: "Is this covered in the skill graph? Where specifically?"
3. Identify any requirements that were mentioned but not implemented
4. Identify any features that were implemented but not requested (scope creep)

## Decision Audit

Review every major decision made during creation:

- For each: "Was this the right call? Given what I know now, would I decide differently?"
- If wrong and fixable at reasonable cost → fix it
- If wrong but fixing requires major restructuring → document as a known limitation

## Completeness Checklist

- [ ] All clarification answers are reflected in the skill graph
- [ ] Research findings are incorporated (not just gathered and forgotten)
- [ ] Domain classification drove actual behavior differences (not just documented)
- [ ] Subjective preferences (if any) are captured in reference files
- [ ] Graph structure matches the plan (or deviations are justified)
- [ ] All reference files are self-contained for their subtask (one-shot test)
- [ ] Extension points are documented for future growth
- [ ] Feedback from checkpoints was incorporated
- [ ] Pre/post evals were performed at each step

## Quality Assessment

Ask these questions honestly:

- "If another Claude instance loads this skill graph, can it execute the intended tasks effectively?"
- "Are there gaps where Claude would need to guess or make assumptions?"
- "Does the skill graph match the user's stated taste/preferences (for subjective domains)?"
- "Would a senior engineer reviewing this graph find obvious improvements?"

## Final Output

Present a summary to the user:

1. **What was built** — high-level structure and capabilities
2. **Key decisions** — what was decided and why
3. **Coverage** — what is covered vs. what is marked as future extensions
4. **Known limitations** — any gaps or areas for improvement
5. **Recommendation** — suggested first iteration if applicable

## Rules

- This step is MANDATORY — never skip
- Be honest about gaps — do not hide known issues
- If the final eval reveals significant problems, return to the relevant step rather than delivering a flawed skill graph
- The final eval is the last chance to catch mistakes — treat it seriously

## Back to

- [Creation process overview](overview.md)
- See also: [Pre/post evaluation](pre-post-eval.md)
- See also: [Permanent steps](../planning-framework/permanent-steps.md)
