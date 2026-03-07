# One-Shot Design

Every skill graph should be designed so that Claude can load the right context and execute the task in one turn, without requiring the user to re-prompt.

## Design for One-Shot

- **Frontmatter description** must be precise enough to trigger correctly — false negatives waste user turns
- **SKILL.md index** must make it obvious which reference to load for any given task
- **Reference files** must be self-contained — once loaded, Claude should not need to load another file to complete a subtask
- **Scripts** must handle common variations without requiring user adjustment

## Information Completeness Test

For each reference file, ask:

> "If Claude loads only this file and the index, can it complete the related task?"

If the answer is no, the file is incomplete. Add the missing information or restructure.

## Fallback Design

When one-shot is not possible (task too complex, requires user input):

1. Design for MINIMUM clarification roundtrips — 1 roundtrip if not 0
2. Batch questions to reduce roundtrips — don't ask one question per turn
3. Provide sensible defaults for non-critical decisions so the user only needs to answer what matters

## Context Loading Strategy

For complex tasks requiring multiple reference files:

1. Load high-value, broadly-applicable references first
2. Load specialized references only when the specific subtask requires them
3. Never load all references simultaneously — this defeats progressive disclosure

## One-Shot Checklist (for skill graph creators)

- [ ] Every reference file passes the information completeness test
- [ ] SKILL.md index clearly maps task types to reference files
- [ ] Frontmatter description covers all trigger scenarios
- [ ] Scripts have sensible defaults for common parameters
- [ ] No reference file requires loading another reference file to be useful

## Back to

- [Core principles overview](overview.md)
- See also: [Context management](../graph-architecture/context-management.md)
