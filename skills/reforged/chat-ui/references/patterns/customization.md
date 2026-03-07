# Customization & Styling

Patterns for customizing message rendering, markdown output, and visual styling.

## Custom Message Rendering

### Using Render Props

`ChatMessages` uses a render prop — replace the default rendering entirely:

```tsx
<ChatMessages>
  {({ messages }) =>
    messages.map((msg) => (
      <div key={msg.id} className="my-custom-message">
        <Avatar role={msg.role} />
        <MessageContent message={msg} />
        <Timestamp time={msg.createdAt} />
      </div>
    ))
  }
</ChatMessages>
```

### Composing Message Components

Mix individual components for custom layouts:

```tsx
// Custom: bubble + content, no reasoning display
<MessageBubble message={msg}>
  <MessageContent message={msg} truncate />
</MessageBubble>

// Custom: full display with reasoning
<MessageBubble message={msg}>
  {msg.reasoning && (
    <MessageReasoning
      reasoning={msg.reasoning}
      isReasoning={!isTerminalStatus(msg.status)}
    />
  )}
  <MessageContent message={msg} />
</MessageBubble>
```

### vs. Pre-Composed Message

| Approach | When to Use |
|----------|-------------|
| `<Message />` | Default layout is sufficient, quick setup |
| Individual components | Custom layout, selective features, additional elements |

## Custom Markdown

Override the markdown renderer in MessageContent:

```tsx
<MessageContent
  message={msg}
  renderMarkdown={(content) => (
    <MyCustomMarkdown content={content} theme="dark" />
  )}
/>
```

The default Markdown component supports custom renderers for cloud.inference.sh URLs:

```tsx
<Markdown
  content={text}
  renderFilePreview={(url) => <CustomFileCard url={url} />}
  renderCloudImage={(url) => <CustomImage src={url} />}
/>
```

## Tailwind Styling

All components accept `className` for Tailwind overrides:

```tsx
<ChatContainer className="max-w-2xl mx-auto">
  <ChatMessages className="p-4">
    {({ messages }) =>
      messages.map((msg) => (
        <MessageBubble key={msg.id} message={msg} className="rounded-2xl">
          <MessageContent message={msg} className="text-sm" />
        </MessageBubble>
      ))
    }
  </ChatMessages>
  <ChatInput className="border-t" />
</ChatContainer>
```

## Design Tokens

Components use shadcn/ui design tokens. Override via CSS variables:

| Token | Usage |
|-------|-------|
| `--background` | Container backgrounds |
| `--foreground` | Text color |
| `--muted` | System message backgrounds |
| `--primary` | Send button, links |
| `--border` | Input borders, dividers |

## Compact Mode

For dense chat UIs (sidebars, embedded widgets):

```tsx
<Markdown content={text} compact />
```

Compact mode reduces text to `text-xs` and disables media embeds (YouTube, file previews).

## Back to

- [Patterns overview](overview.md)
- See also: [Message display](../components/message-display.md) — component props for customization
- See also: [Markdown](../components/markdown.md) — markdown renderer options
