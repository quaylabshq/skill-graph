# Message Display

Four components for rendering individual messages: MessageBubble (alignment/styling), MessageContent (text/media), MessageReasoning (thinking blocks), and MessageStatusIndicator (typing spinner). Plus a pre-composed `Message` convenience component.

## MessageBubble

Role-based alignment and visual styling wrapper.

**File:** `components/infsh/agent/message-bubble.tsx`

| Prop | Type | Description |
|------|------|-------------|
| `message` | `ChatMessageDTO` | Message data object |
| `children` | `ReactNode?` | Content inside the bubble |
| `className` | `string?` | Additional CSS classes |

**Role-Based Styling:**

| Role | Alignment | Background | Max Width |
|------|-----------|------------|-----------|
| `user` | Right-aligned | Background fill | ~70% |
| `assistant` | Left-aligned | No background | Full |
| `system` | Centered | Muted | Full |

```tsx
<MessageBubble message={msg}>
  <MessageContent message={msg} />
</MessageBubble>
```

## MessageContent

Renders text, images, files, and markdown within a message bubble.

**File:** `components/infsh/agent/message-content.tsx`

| Prop | Type | Description |
|------|------|-------------|
| `message` | `ChatMessageDTO` | Message data object |
| `className` | `string?` | Additional CSS classes |
| `truncate` | `boolean?` | Truncate long user messages with expand/collapse |
| `renderMarkdown` | `(content: string) => ReactNode` | Custom markdown renderer override |

**Content Types Handled:**
- Plain text → rendered via Markdown component
- Images → clickable image previews
- Videos → thumbnail display (mp4, webm, mov, avi, mkv)
- Files → file preview with extension badge and size

**Helper Functions:**

| Function | Purpose |
|----------|---------|
| `getTextContent(message)` | Extract plain text from message parts |
| `getImageUrls(message)` | Extract image URLs from content |
| `getFileUrls(message)` | Extract file URLs from content |
| `getFileName(url)` | Parse filename from URL |
| `getFileExtension(url)` | Parse extension from URL |
| `isImageUrl(url)` | Check if URL is an image |
| `isVideoUrl(url)` | Check if URL is a video |

**Sub-Components:**
- `FileAttachment` — thumbnail + extension badge + formatted size
- `ImageAttachment` — clickable image with rounded corners

## MessageReasoning

Collapsible reasoning/thinking block for AI thought process display.

**File:** `components/infsh/agent/message-reasoning.tsx`

| Prop | Type | Description |
|------|------|-------------|
| `reasoning` | `string` | The reasoning/thinking text |
| `isReasoning` | `boolean?` | Whether reasoning is still in progress |
| `className` | `string?` | Additional CSS classes |

**Features:**
- **Collapsed preview** — shows last line when collapsed
- **Pulsing animation** — active when `isReasoning=true`
- **Markdown rendering** inside the reasoning block

```tsx
{msg.reasoning && (
  <MessageReasoning
    reasoning={msg.reasoning}
    isReasoning={!isTerminalStatus(msg.status)}
  />
)}
```

## MessageStatusIndicator

Spinner shown during AI generation.

**File:** `components/infsh/agent/message-status-indicator.tsx`

| Prop | Type | Description |
|------|------|-------------|
| `className` | `string?` | Additional CSS classes |
| `size` | `number?` | Icon size in pixels |
| `showLabel` | `boolean?` | Show text label alongside spinner |
| `label` | `string?` | Custom label (default: "thinking...") |

```tsx
{isGenerating && <MessageStatusIndicator showLabel label="Thinking..." />}
```

## Message (Pre-Composed)

Convenience component combining all display components into a default message row.

**File:** `components/infsh/agent/message.tsx`

| Prop | Type | Description |
|------|------|-------------|
| `message` | `ChatMessageDTO` | Message data object |
| `truncateUser` | `boolean?` | Truncate long user messages |

Internally combines: `MessageBubble` + `MessageContent` + `MessageReasoning` + `ToolInvocations`.

```tsx
import { Message } from "@/registry/blocks/chat/message"

<Message message={msg} truncateUser />
```

Use `Message` for quick default rendering. Use the individual components for custom layouts.

## Back to

- [Components overview](overview.md)
- See also: [ChatMessages](chat-messages.md) — the scroll container that wraps message display
- See also: [Markdown renderer](markdown.md) — how text content is rendered
- See also: [Customization](../patterns/customization.md) — custom rendering overrides
