# Interlinking

All components in a skill graph must be interlinked. This ensures traceability between features, scripts, references, and extension points.

## Hub-and-Spoke Pattern

The primary linking structure:

```
SKILL.md (root)
├── references/category-a/overview.md (hub)
│   ├── references/category-a/detail-1.md (spoke)
│   ├── references/category-a/detail-2.md (spoke)
│   └── references/category-a/detail-3.md (spoke)
├── references/category-b/overview.md (hub)
│   └── ...
└── scripts/tool.py (leaf)
```

## Linking Rules

### Downward Links (hub → detail)

Every hub file (`overview.md`) must link to ALL files in its directory. Use a table:

```markdown
| Topic | Reference |
|-------|-----------|
| Detail 1 | [detail-1.md](detail-1.md) |
| Detail 2 | [detail-2.md](detail-2.md) |
```

### Upward Links (detail → hub)

Every detail file must include a "Back to" section linking to its parent hub:

```markdown
## Back to

- [Category overview](overview.md)
```

### Cross Links (detail → related detail)

When files reference related content in other directories, use "See also" links:

```markdown
## See Also

- [Related topic](../other-category/related-file.md)
```

### Root Links (SKILL.md → hubs)

SKILL.md links to every hub file and directly to scripts. It does NOT link to individual detail files — those are reached via their hub.

## Reachability Requirement

Every file must be reachable from SKILL.md within 2 hops:

- **Hop 1**: SKILL.md → hub file (overview.md)
- **Hop 2**: hub file → detail file

This means no nested subdirectories beyond one level within `references/`.

## Avoiding Orphans

An orphan is a file that exists in the directory but isn't linked from any other file. Orphans violate graph integrity. The `validate_graph.py` script checks for orphans automatically.

## Back to

- [Graph architecture overview](overview.md)
- See also: [Progressive disclosure](../core-principles/progressive-disclosure.md) — loading patterns that interlinking enables
