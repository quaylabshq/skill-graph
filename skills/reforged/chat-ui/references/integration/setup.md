# Installation & Provider Setup

How to install chat-ui components and configure the SDK provider that all components depend on.

## Installation

```bash
# Chat components only
npx shadcn@latest add https://ui.inference.sh/r/chat.json

# Full agent experience (chat + tools + widgets)
npx shadcn@latest add https://ui.inference.sh/r/agent.json
```

**Required NPM dependency:** `@inferencesh/sdk`

```bash
npm install @inferencesh/sdk
```

## Provider Setup

All chat components require `AgentChatProvider` wrapping them. Components will not function without it.

```tsx
import { useMemo } from "react"
import { Inference } from "@inferencesh/sdk"
import { AgentChatProvider } from "@inferencesh/sdk/agent"

function App() {
  const client = useMemo(
    () => new Inference({ proxyUrl: '/api/inference/proxy' }),
    []
  )

  return (
    <AgentChatProvider client={client} agentConfig={config}>
      <ChatUI />
    </AgentChatProvider>
  )
}
```

### Client Options

| Option | Type | Description |
|--------|------|-------------|
| `proxyUrl` | `string?` | Proxy URL for API calls (recommended for production) |
| `apiKey` | `string?` | Direct API key (use for development only) |
| `baseUrl` | `string?` | Custom API base URL |

### AgentChatProvider Props

| Prop | Type | Description |
|------|------|-------------|
| `client` | `Inference` | SDK client instance |
| `agentConfig` | `AgentOptions` | Agent configuration (model, tools, etc.) |
| `chatId` | `string?` | For chat persistence across sessions |
| `onChatCreated` | `(chatId: string) => void` | Callback when new chat is created |

## Proxy API Route (Next.js)

For production, create a proxy route to avoid exposing API keys:

```tsx
// app/api/inference/proxy/route.ts
import { Inference } from "@inferencesh/sdk"

const client = new Inference({ apiKey: process.env.INFERENCE_API_KEY })

export async function POST(req: Request) {
  // Proxy the request to inference.sh
  return client.proxy(req)
}
```

## Back to

- [Integration overview](overview.md)
- See also: [Hooks & State](hooks-and-state.md) — hooks provided by the provider
- See also: [Full Agent Assembly](../patterns/full-agent.md) — complete setup example
