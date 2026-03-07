# ChatInput

Auto-resizing textarea with file upload support, drag-and-drop, command menu, and send/stop toggle.

**File:** `components/infsh/agent/chat-input.tsx`

## Props

| Prop | Type | Description |
|------|------|-------------|
| `placeholder` | `string?` | Input placeholder text |
| `className` | `string?` | Additional CSS classes |
| `allowAttachments` | `boolean?` | Enable file attachments |
| `allowFiles` | `boolean?` | Enable general file uploads |
| `allowImages` | `boolean?` | Enable image uploads |
| `onFilesChange` | `(files: File[]) => void` | Callback when files change |

## Basic Usage

```tsx
import { ChatInput } from "@/registry/blocks/chat/chat-input"

<ChatInput
  placeholder="Type a message..."
  allowAttachments
  allowImages
/>
```

## Features

### Auto-Resizing Textarea
Grows vertically as the user types. No fixed height.

### Send / Stop Toggle
- **Send button** when idle — triggers `sendMessage()` via `useAgentActions()`
- **Stop button** during generation — triggers `stopGeneration()`
- Automatically toggles based on chat state

### File Upload Integration
When `allowAttachments`, `allowFiles`, or `allowImages` is enabled:

- **Drag-and-drop** — Visual `DragOverlay` component appears on drag
- **Command menu** — Popover for file selection triggered via UI
- **`@filename` references** — Uploaded files can be referenced in messages
- **Upload status** — Error notifications for failed uploads

### Hooks Used

| Hook | Purpose |
|------|---------|
| `useAgentChat()` | Chat state (loading, messages) |
| `useAgentActions()` | `sendMessage()`, `stopGeneration()`, `uploadFile()` |
| `useFileUploadManager()` | Upload state tracking |

## Minimal Example

```tsx
import { ChatContainer } from "@/registry/blocks/chat/chat-container"
import { ChatMessages } from "@/registry/blocks/chat/chat-messages"
import { ChatInput } from "@/registry/blocks/chat/chat-input"

<ChatContainer>
  <ChatMessages>{({ messages }) => /* render messages */}</ChatMessages>
  <ChatInput placeholder="Ask anything..." />
</ChatContainer>
```

## With File Uploads

```tsx
<ChatInput
  placeholder="Type or drop files..."
  allowAttachments
  allowFiles
  allowImages
  onFilesChange={(files) => console.log('Files:', files)}
/>
```

For the full file upload system (hooks, types, previews), see [file-uploads.md](../integration/file-uploads.md).

## Back to

- [Components overview](overview.md)
- See also: [File uploads](../integration/file-uploads.md) — upload manager hook and file type handling
- See also: [Hooks & State](../integration/hooks-and-state.md) — useAgentActions for send/stop
