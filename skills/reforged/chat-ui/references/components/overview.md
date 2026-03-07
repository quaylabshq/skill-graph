# Components Overview

Chat UI provides composable React primitives installed via the shadcn registry. All components use Tailwind CSS and shadcn/ui design tokens.

## Component Map

| Component | File | Purpose | Reference |
|-----------|------|---------|-----------|
| ChatContainer | `components/infsh/agent/chat-container.tsx` | CSS Grid layout wrapper | Below |
| ChatMessages | `components/infsh/agent/chat-messages.tsx` | Scrollable message list | [chat-messages.md](chat-messages.md) |
| ChatInput | `components/infsh/agent/chat-input.tsx` | Auto-resizing textarea + uploads | [chat-input.md](chat-input.md) |
| MessageBubble | `components/infsh/agent/message-bubble.tsx` | Role-based message alignment | [message-display.md](message-display.md) |
| MessageContent | `components/infsh/agent/message-content.tsx` | Text, images, files rendering | [message-display.md](message-display.md) |
| MessageReasoning | `components/infsh/agent/message-reasoning.tsx` | Collapsible thinking blocks | [message-display.md](message-display.md) |
| MessageStatusIndicator | `components/infsh/agent/message-status-indicator.tsx` | Typing/thinking spinner | [message-display.md](message-display.md) |
| Message | `components/infsh/agent/message.tsx` | Pre-composed default message row | [message-display.md](message-display.md) |
| Markdown | Via `markdown.json` registry | Rich markdown rendering | [markdown.md](markdown.md) |

## ChatContainer

Simplest component — a CSS Grid wrapper creating three layout zones.

**Props:**

| Prop | Type | Description |
|------|------|-------------|
| `children` | `ReactNode` | Header, messages, and input components |
| `className` | `string?` | Additional CSS classes |

**Layout:** CSS Grid with `grid-template-rows: auto 1fr auto` → `[header] [messages] [input]`.

```tsx
import { ChatContainer } from "@/registry/blocks/chat/chat-container"

<ChatContainer>
  <Header />        {/* auto — top zone */}
  <ChatMessages />  {/* 1fr — scrollable middle zone */}
  <ChatInput />     {/* auto — bottom zone */}
</ChatContainer>
```

Supports `forwardRef` for external ref access. Full width, max height container.

## Back to

- [SKILL.md](../../SKILL.md)
