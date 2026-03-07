# Codebase Exploration

How to explore an existing codebase before planning. This is the research mode for tasks involving existing code.

## What to Explore

### 1. Architecture & Structure

- Directory structure and organization patterns
- Key entry points (main files, routers, controllers)
- Module boundaries and how components interact
- Configuration files and build setup

### 2. Relevant Code Areas

- Files and functions directly related to the task
- Adjacent code that the task will interact with
- Test files for the relevant areas
- Type definitions and interfaces

### 3. Patterns & Conventions

- Naming conventions used in the codebase
- Error handling patterns
- State management approach
- API design patterns (REST, GraphQL, etc.)
- Testing patterns (what framework, what style)

### 4. Dependencies & Integration Points

- External libraries and their versions
- Internal module dependencies
- API contracts (both consumed and exposed)
- Database schemas and migrations

## How to Explore

Use the Task tool with `subagent_type=Explore` to delegate exploration:

1. **Start broad**: "Explore the project structure and identify the architecture pattern"
2. **Then narrow**: "Find all files related to [feature area] and understand how they interact"
3. **Then specific**: "Read [specific file] and summarize the API contract"

### Exploration Prompts by Task Type

| Task Type | Exploration Focus |
|-----------|-------------------|
| New feature | Architecture, related features, patterns to follow |
| Bug fix | Error flow, related tests, recent changes to the area |
| Refactor | Current structure, dependencies, test coverage |
| Migration | Data model, integration points, rollback paths |
| Performance | Hot paths, database queries, caching patterns |

## Synthesizing Findings

Bring back to the main context:

- **Architecture summary** — 3-5 sentences on how the codebase is organized
- **Relevant files** — list of files the task will likely touch
- **Patterns to follow** — conventions discovered that the plan should respect
- **Constraints** — hard requirements from the codebase (e.g., "auth middleware must wrap all API routes")
- **Risks** — fragile areas or technical debt that could complicate the task

Do NOT bring back: raw file contents, full directory listings, or unfiltered search results.

## Rules

1. Always explore before planning code tasks — never plan from description alone
2. Delegate to sub-agents — keep main context clean
3. Synthesize findings into actionable summaries
4. If exploration reveals the task is different than described, return to clarification

## Back to

- [Research framework overview](overview.md)
- See also: [Context management](../context-management.md)
