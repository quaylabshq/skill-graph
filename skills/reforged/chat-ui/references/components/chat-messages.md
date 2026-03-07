# ChatMessages

Scrollable message list with auto-scroll behavior, scroll-to-bottom button, and render prop pattern for flexible message rendering.

**File:** `components/infsh/agent/chat-messages.tsx`

## Props

| Prop | Type | Description |
|------|------|-------------|
| `children` | `(props: { messages: ChatMessageDTO[] }) => ReactNode` | **Render prop** — you control how each message renders |
| `className` | `string?` | Additional CSS classes |
| `scrollToTopPadding` | `boolean?` | Add padding at top for scroll behavior |

## Render Prop Pattern

ChatMessages uses a **render prop** instead of mapping internally. This gives full control over message layout:

```tsx
import { ChatMessages } from "@/registry/blocks/chat/chat-messages"
import { MessageBubble } from "@/registry/blocks/chat/message-bubble"
import { MessageContent } from "@/registry/blocks/chat/message-content"

<ChatMessages>
  {({ messages }) =>
    messages.map((msg) => (
      <MessageBubble key={msg.id} message={msg}>
        <MessageContent message={msg} />
      </MessageBubble>
    ))
  }
</ChatMessages>
```

## Auto-Scroll Behavior

Uses the `useAutoScroll()` hook internally:

| Behavior | Detail |
|----------|--------|
| Auto-scroll on new messages | Scrolls to bottom when new content arrives |
| Deliberate scroll-up detection | Disables auto-scroll when user scrolls up >10px |
| Re-activation threshold | Re-enables auto-scroll when within 50px of bottom |
| Scroll-to-bottom button | Appears when user has scrolled up |
| Safari rubber-band handling | Detects and ignores rubber-band bounce |
| Content resize detection | `ResizeObserver` tracks content height changes |
| Touch support | Mobile-friendly touch event handling |

### useAutoScroll Hook

```typescript
const {
  containerRef,    // Attach to scroll container
  scrollToBottom,  // Programmatic scroll
  handleScroll,    // Scroll event handler
  shouldAutoScroll, // Current auto-scroll state
  handleTouchStart // Touch event handler
} = useAutoScroll()
```

**Constants:**
- `ACTIVATION_THRESHOLD: 50` — pixels from bottom to re-enable auto-scroll
- `MIN_SCROLL_UP_THRESHOLD: 10` — minimum upward scroll to disable auto-scroll

## Data Source

Messages come from the `useAgentChat()` hook via provider context. See [hooks-and-state.md](../integration/hooks-and-state.md).

## Back to

- [Components overview](overview.md)
- See also: [Message display](message-display.md) — how individual messages render inside ChatMessages
- See also: [Hooks & State](../integration/hooks-and-state.md) — useAgentChat provides the messages array
