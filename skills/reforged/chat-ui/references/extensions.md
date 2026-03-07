# Future Extensions & Related Skills

Planned extension points and related skills in the inference.sh ecosystem.

## Related Skills

Install alongside chat-ui for expanded functionality:

```bash
# Full agent component (chat + tools + widgets combined)
npx skills add inference-sh/skills@agent-ui

# Tool invocation UI (function calling display)
npx skills add inference-sh/skills@tools-ui

# Declarative widgets (charts, tables, forms)
npx skills add inference-sh/skills@widgets-ui

# Standalone markdown rendering
npx skills add inference-sh/skills@markdown-ui
```

## Extension Points

### 1. Tool Invocations Display
- **Type**: Component reference
- **Purpose**: Render tool/function call results inline in messages
- **Status**: Available via `tools-ui` skill
- **Integration**: `Message` component already includes `ToolInvocations` when tools-ui is installed

### 2. Voice Input
- **Type**: Input extension
- **Purpose**: Speech-to-text input for ChatInput
- **Implementation**: Add a voice button to ChatInput, integrate Web Speech API
- **Files needed**: `references/components/voice-input.md`, component code

### 3. Message Actions
- **Type**: Component extension
- **Purpose**: Copy, retry, edit, delete actions on messages
- **Implementation**: Action bar overlay on MessageBubble hover
- **Files needed**: `references/components/message-actions.md`

### 4. Multi-Modal Input
- **Type**: Input extension
- **Purpose**: Camera capture, screen recording, drawing input
- **Implementation**: Extend ChatInput attachment system
- **Files needed**: `references/integration/multi-modal.md`

### 5. Chat Persistence
- **Type**: Integration reference
- **Purpose**: Save/restore chat history across sessions
- **Implementation**: Use `chatId` prop + backend storage
- **Files needed**: `references/integration/persistence.md`

### 6. Platform Integrations
- **Type**: Reference
- **Purpose**: Connect chat agents to Slack, Discord, Telegram, WhatsApp
- **Note**: Configured at platform level, not component library

## Implementation Pattern

To add an extension:
1. Create reference file in appropriate `references/` subdirectory
2. Link from the relevant hub `overview.md`
3. Add entry to SKILL.md navigation table
4. Remove the extension entry from this file

## Documentation

- [Chatting with Agents](https://inference.sh/docs/agents/chatting) — building chat interfaces
- [Agent UX Patterns](https://inference.sh/blog/ux/agent-ux-patterns) — chat UX best practices
- [Real-Time Streaming](https://inference.sh/blog/observability/streaming) — streaming responses
- Component docs: [ui.inference.sh/blocks/chat](https://ui.inference.sh/blocks/chat)

## Back to

- [SKILL.md](../SKILL.md)
- See also: [Components overview](components/overview.md)
- See also: [Integration overview](integration/overview.md)
