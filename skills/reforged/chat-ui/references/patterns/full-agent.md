# Full Agent Assembly

Complete pattern for building an AI agent chat interface from scratch. Combines provider setup, layout, messages, and input into a working agent.

## Agent Component

The top-level `Agent` component wraps everything:

**File:** `components/infsh/agent/agent.tsx`

### AgentProps

| Prop | Type | Description |
|------|------|-------------|
| `proxyUrl` | `string?` | API proxy URL (e.g., `/api/inference/proxy`) |
| `apiKey` | `string?` | Direct API key (dev only) |
| `baseUrl` | `string?` | Custom API base URL |
| `config` | `AgentOptions` | Agent configuration (model, tools, etc.) |
| `name` | `string?` | Agent display name |
| `chatId` | `string?` | For chat persistence |
| `className` | `string?` | Additional CSS classes |
| `compact` | `boolean?` | Dense UI mode |
| `allowFiles` | `boolean?` | Enable file uploads |
| `allowImages` | `boolean?` | Enable image uploads |
| `onChatCreated` | `(chatId: string) => void` | Chat creation callback |
| `description` | `string?` | Agent description shown in empty state |
| `examplePrompts` | `string[]?` | Clickable prompt suggestions |

## Minimal Assembly

```tsx
import { useMemo } from "react"
import { Inference } from "@inferencesh/sdk"
import { AgentChatProvider } from "@inferencesh/sdk/agent"
import { ChatContainer } from "@/registry/blocks/chat/chat-container"
import { ChatMessages } from "@/registry/blocks/chat/chat-messages"
import { ChatInput } from "@/registry/blocks/chat/chat-input"
import { Message } from "@/registry/blocks/chat/message"
import { MessageStatusIndicator } from "@/registry/blocks/chat/message-status-indicator"
import { isTerminalStatus } from "@inferencesh/sdk/agent"
import { useAgentChat } from "@inferencesh/sdk/agent"

function AgentChat() {
  const client = useMemo(
    () => new Inference({ proxyUrl: '/api/inference/proxy' }),
    []
  )

  return (
    <AgentChatProvider client={client} agentConfig={{ model: "gpt-4" }}>
      <ChatContainer>
        <AgentMessages />
        <ChatInput placeholder="Ask anything..." />
      </ChatContainer>
    </AgentChatProvider>
  )
}

function AgentMessages() {
  const { messages } = useAgentChat()
  const lastMsg = messages[messages.length - 1]
  const isGenerating = lastMsg && !isTerminalStatus(lastMsg.status)

  return (
    <ChatMessages>
      {({ messages }) => (
        <>
          {messages.map((msg) => (
            <Message key={msg.id} message={msg} />
          ))}
          {isGenerating && <MessageStatusIndicator showLabel />}
        </>
      )}
    </ChatMessages>
  )
}
```

## Internal Sub-Components

The pre-built Agent component includes:

| Sub-Component | Purpose |
|---------------|---------|
| `DefaultHeader` | Bot icon + agent name label |
| `ExamplePrompts` | Clickable prompt suggestion buttons |
| `EmptyState` | Initial UI with description + example prompts |
| `MessageRow` | Individual message + reasoning + tool invocations |
| `MessageList` | All messages + typing indicator |
| `AgentContent` | Full layout assembly |

## Assembly Order

1. Create `Inference` client with `useMemo`
2. Wrap with `AgentChatProvider` — passes client + config to context
3. `ChatContainer` — CSS Grid layout
4. `ChatMessages` — scrollable area with auto-scroll
5. Message rendering — use `Message` (default) or custom `MessageBubble` + `MessageContent`
6. `ChatInput` — input area at bottom

## Back to

- [Patterns overview](overview.md)
- See also: [Setup](../integration/setup.md) — provider and client configuration
- See also: [Hooks & State](../integration/hooks-and-state.md) — hooks used in assembly
- See also: [Components overview](../components/overview.md) — individual component APIs
