# Conciseness

The context window is a public good. Skills share the context window with everything else Claude needs: system prompt, conversation history, other skills' metadata, and the actual user request.

## Default Assumption

Claude is already very smart. Only add context Claude doesn't already have.

Challenge each piece of information:

- "Does Claude really need this explanation?"
- "Does this paragraph justify its token cost?"

## Rules

1. Prefer concise examples over verbose explanations
2. Never duplicate information across files — content lives in exactly one place
3. If Claude can infer it, don't spell it out
4. Reference files should be loaded on demand, not preloaded

## In Graph Context

The graph architecture naturally enforces conciseness:

- SKILL.md is pure navigation — no detailed content
- Each reference file covers one focused topic
- Claude loads only the reference files relevant to the current task
- No file should contain content that belongs in a different file

## Back to

- [Core principles overview](overview.md)
