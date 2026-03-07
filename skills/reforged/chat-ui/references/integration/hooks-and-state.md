# Hooks & State Management

Core hooks provided by `AgentChatProvider` context. These drive all component behavior.

## useAgentChat

Access chat state and message history.

```tsx
import { useAgentChat } from "@inferencesh/sdk/agent"

const { messages, status, chatId } = useAgentChat()
```

| Return Value | Type | Description |
|-------------|------|-------------|
| `messages` | `ChatMessageDTO[]` | Array of all messages in the conversation |
| `status` | `string` | Current chat status |
| `chatId` | `string?` | Active chat ID |

### ChatMessageDTO

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique message identifier |
| `role` | `string` | `ChatMessageRoleUser` or `ChatMessageRoleAssistant` |
| `content` | `MessageContent[]` | Array of content parts (text, image, file) |
| `status` | `string` | Message status (ready, failed, cancelled) |
| `reasoning` | `string?` | AI reasoning/thinking text |

### Message Roles

| Constant | Value |
|----------|-------|
| `ChatMessageRoleUser` | User message |
| `ChatMessageRoleAssistant` | Assistant message |

### Message Statuses

| Constant | Terminal? | Description |
|----------|-----------|-------------|
| `ChatMessageStatusReady` | Yes | Message complete |
| `ChatMessageStatusFailed` | Yes | Message failed |
| `ChatMessageStatusCancelled` | Yes | Message cancelled |

Use `isTerminalStatus(status)` helper to check if generation is complete.

### Content Types

| Constant | Description |
|----------|-------------|
| `ChatMessageContentTypeText` | Plain text content |
| `ChatMessageContentTypeImage` | Image content |
| `ChatMessageContentTypeFile` | File attachment |
| `ChatMessageContentTypeReasoning` | Reasoning/thinking block |

## useAgentActions

Access action dispatchers for sending messages and controlling generation.

```tsx
import { useAgentActions } from "@inferencesh/sdk/agent"

const { sendMessage, stopGeneration, uploadFile } = useAgentActions()
```

| Action | Signature | Description |
|--------|-----------|-------------|
| `sendMessage` | `(content: string, files?: UploadedFile[]) => void` | Send a user message |
| `stopGeneration` | `() => void` | Stop in-progress AI generation |
| `uploadFile` | `(file: File) => Promise<UploadedFile>` | Upload a file to the server |

## Streaming Pattern

Messages update in real-time during generation. Check terminal status to know when complete:

```tsx
import { isTerminalStatus } from "@inferencesh/sdk/agent"

const { messages } = useAgentChat()
const lastMessage = messages[messages.length - 1]
const isGenerating = lastMessage && !isTerminalStatus(lastMessage.status)
```

## Back to

- [Integration overview](overview.md)
- See also: [Setup](setup.md) — provider must be configured first
- See also: [ChatMessages](../components/chat-messages.md) — consumes messages from useAgentChat
- See also: [ChatInput](../components/chat-input.md) — uses useAgentActions for send/stop
