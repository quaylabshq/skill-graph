# Integration Overview

How to install, configure, and connect chat-ui components with the inference.sh SDK and your application.

## Integration Topics

| Topic | What It Covers | Reference |
|-------|---------------|-----------|
| Setup | Installation, provider wrapping, SDK client | [setup.md](setup.md) |
| Hooks & State | useAgentChat, useAgentActions, streaming lifecycle | [hooks-and-state.md](hooks-and-state.md) |
| File Uploads | Upload manager, drag-and-drop, file types | [file-uploads.md](file-uploads.md) |

## Dependency Chain

```
@inferencesh/sdk (required)
  └── AgentChatProvider (wraps your app)
        ├── useAgentChat()     → messages, chat state
        ├── useAgentActions()  → sendMessage, stopGeneration, uploadFile
        └── Components read from provider context
```

Components do not function without `AgentChatProvider`. See [setup.md](setup.md) for provider configuration.

## Registry Dependencies

```
chat.json
  ├── button, scroll-area, textarea, tooltip, spinner (shadcn primitives)
  ├── command, popover (for input command menu)
  └── markdown.json
        ├── react-markdown, remark-gfm
        ├── zoomable-image, youtube-embed, code-block
```

## Back to

- [SKILL.md](../../SKILL.md)
- See also: [Components overview](../components/overview.md)
