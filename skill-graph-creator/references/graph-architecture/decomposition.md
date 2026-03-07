# Content Decomposition

How to break monolithic content into graph nodes. This is the key skill for transforming existing skills or designing new ones.

## When to Split

Split content into a separate file when:

1. **Logical independence** — The topic can stand alone and be understood without the surrounding context
2. **Conditional loading** — The content is only relevant to specific tasks or domains
3. **Size threshold** — A single file approaches 200 lines
4. **Feature boundary** — The content describes a distinct feature, tool, or capability

## When to Keep Together

Keep content in one file when:

1. **Tightly coupled** — The topics cannot be understood independently
2. **Sequential dependency** — The reader must process them in order
3. **Small scope** — Splitting would create files under 20 lines

## Decomposition Strategies

### By Feature

Each feature or capability gets its own file:

```
references/
├── authentication.md
├── authorization.md
├── session-management.md
└── password-policy.md
```

### By Domain

Each domain or audience gets its own file:

```
references/
├── finance.md
├── sales.md
├── product.md
└── marketing.md
```

### By Process Step

Each step in a workflow gets its own file:

```
references/creation-process/
├── step-1-clarification.md
├── step-2-research.md
├── step-3-understand.md
└── ...
```

### By Variant

Each framework, provider, or option gets its own file:

```
references/
├── aws.md
├── gcp.md
└── azure.md
```

## Sizing Guidelines

| File Type | Target Size | Maximum |
|-----------|-------------|---------|
| SKILL.md (index) | 50–80 lines | 100 lines |
| Hub files (overview.md) | 30–60 lines | 100 lines |
| Detail files | 50–150 lines | 200 lines |

If a detail file exceeds 200 lines, it likely covers multiple topics and should be split further.

## Recursive Decomposition Heuristic

For every component, ask: "Can this be split into 2+ independent parts?"

- If yes → split and repeat the question on each part
- If no → the component is atomic
- Stop when: the file would be <20 lines, the topic is tightly coupled with its parent, or splitting would require duplicating content

## Complexity Assessment

Count the depth of decomposition to assess complexity:

| Depth | Complexity | Graph Implication |
|-------|------------|-------------------|
| 1-2 levels | Simple | Flat references, single hub |
| 3-4 levels | Moderate | Sub-hubs needed, more reference files |
| 5+ levels | Complex | Additional reference layers, aggressive sub-categorization |

## Problem-to-Graph Mapping

- Subproblems become graph nodes (reference files)
- Dependencies between subproblems become links between files
- Independent subproblems become parallel reference files that can be worked independently
- The decomposition tree maps directly to the hub-and-spoke architecture

## Back to

- [Graph architecture overview](overview.md)
- See also: [Creation process — step 4: plan](../creation-process/step-4-plan.md) — where decomposition decisions are made
