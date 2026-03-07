# Extension Points

Every skill graph must explicitly document where and how it can be extended. This ensures future capabilities are planned for rather than hacked in.

## What Is an Extension Point

An extension point is any place where:

- New features can be added
- New scripts can be introduced
- New reference files can be created
- New domains or variants can be supported

## How to Document Extensions

Create a `future-skills.md` or `extensions.md` reference file listing planned or potential extensions:

```markdown
# Future Extensions

## Planned

### 1. Feature Name
- **Type**: Tool skill (script) / Prompt skill / Reference
- **Purpose**: What this extension would add
- **Operations**: Key capabilities
- **Reference**: Link to related existing reference files
- **Implementation pattern**: Brief description of how to add it

### 2. Another Feature
...

## Implementation Pattern

Each extension should follow this structure:
- scripts/<name>.py (if tool skill)
- references/<name>.md (if reference needed)
- Update SKILL.md index to include new links
```

## Rules

1. Every hub file should note which extensions are possible for its category
2. Extension files follow the same graph structure — new files must be linked from existing hubs or the index
3. When an extension is implemented, move it from the future file to the main graph and remove the future entry
4. Scripts and references for extensions follow the same naming and structural conventions

## Back to

- [Graph architecture overview](overview.md)
- See also: [Creation process — step 8: iterate](../creation-process/step-8-iterate.md) — iteration often involves implementing extensions
