# Markdown Renderer

Rich markdown rendering component for chat messages. Installed via separate registry entry. Supports GFM, syntax highlighting, media embeds, and compact mode for dense chat UIs.

**Registry:** `https://ui.inference.sh/r/markdown.json`
**Dependencies:** `react-markdown`, `remark-gfm`

## Props

| Prop | Type | Description |
|------|------|-------------|
| `content` | `string` | Markdown text to render |
| `className` | `string?` | CSS classes for wrapper |
| `compact` | `boolean?` | Dense UI mode — reduces text to `text-xs`, disables media |
| `renderFilePreview` | `function?` | Custom renderer for cloud.inference.sh file URLs |
| `renderCloudImage` | `function?` | Custom image renderer for cloud URLs |

## Rendering Features

| Feature | Detail |
|---------|--------|
| Headings | h1–h6 with appropriate sizing |
| Text formatting | Bold, italic, strikethrough |
| Code | Inline code (pink background) + fenced code blocks with syntax highlighting |
| Links | Open in new tab (`target="_blank"`) |
| Lists | Ordered and unordered |
| Blockquotes | Styled quote blocks |
| Tables | With horizontal scroll overflow |
| Images | Zoomable with rounded corners |
| YouTube | Auto-detected embeds from youtube.com/youtu.be links |
| HTML comments | Stripped automatically |

## Compact Mode

When `compact={true}`:
- All text reduced to `text-xs`
- YouTube embeds disabled
- File preview rendering disabled
- Optimized for dense chat bubble display

```tsx
<Markdown content={message.content} compact />
```

## Helper Functions

From `lib/markdown-helpers.ts`:

| Function | Purpose |
|----------|---------|
| `isCloudInferenceUrl(url)` | Check if URL is from cloud.inference.sh |
| `getYouTubeVideoId(url)` | Extract video ID from YouTube URLs |
| `stripHtmlComments(text)` | Remove HTML comments from content |
| `isLikelyMarkdown(text)` | Heuristic scoring — detect if text contains markdown |

## Custom Markdown Override

`MessageContent` accepts a `renderMarkdown` prop to override the default renderer:

```tsx
<MessageContent
  message={msg}
  renderMarkdown={(content) => <MyCustomRenderer content={content} />}
/>
```

## Back to

- [Components overview](overview.md)
- See also: [Message display](message-display.md) — MessageContent uses this renderer
- See also: [Customization](../patterns/customization.md) — overriding the markdown renderer
