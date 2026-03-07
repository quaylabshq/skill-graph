# File Upload System

Complete file upload pipeline: manager hook, drag-and-drop, previews, and type detection.

**File:** `components/infsh/agent/file-upload.tsx`

## useFileUploadManager Hook

```tsx
import { useFileUploadManager } from "@/registry/blocks/chat/file-upload"

const {
  uploads,            // FileUpload[] — current upload state
  addFiles,           // (files: File[]) => void — start uploads
  removeUpload,       // (id: string) => void — remove by ID
  clearAll,           // () => void — clear all uploads
  getUploadedFiles,   // () => UploadedFile[] — get completed files
  hasPendingUploads,  // boolean — any in-progress uploads
  hasCompletedUploads // boolean — any finished uploads
} = useFileUploadManager()
```

## FileUpload Interface

```typescript
interface FileUpload {
  id: string
  file: File
  status: 'pending' | 'uploading' | 'completed' | 'failed'
  uploadedFile?: UploadedFile
  error?: string
}
```

## File Type Detection

| Type | Extensions / Detection |
|------|----------------------|
| Image | MIME `image/*` + jpg, jpeg, png, gif, webp, svg, bmp |
| Video | mp4, webm, mov, avi, mkv |
| Text | txt, md, csv, json, xml, yaml, yml |
| Generic | Fallback for unrecognized types |

## Sub-Components

### FileUploadPreview

Renders individual file preview cards:
- **Image thumbnails** — generated from file data
- **Video thumbnails** — first frame capture
- **Text preview** — first 100 characters
- **Extension badge** — file type indicator
- **Formatted size** — human-readable file size
- **Upload status overlay** — progress/error state

### FileUploadList

Renders a list of `FileUploadPreview` items. Used internally by ChatInput.

### showFileUploadDialog

```tsx
import { showFileUploadDialog } from "@/registry/blocks/chat/file-upload"

// Open native file picker with optional accept filter
const files = await showFileUploadDialog("image/*")
```

## Drag-and-Drop

ChatInput includes a `DragOverlay` sub-component that:
1. Detects drag events over the input area
2. Shows a visual overlay indicating drop is available
3. Handles file drop and passes to `useFileUploadManager`

## @filename References

After upload, files can be referenced in messages using `@filename` syntax. The ChatInput command menu (popover) helps users select from uploaded files.

## Back to

- [Integration overview](overview.md)
- See also: [ChatInput](../components/chat-input.md) — UI component that integrates file uploads
- See also: [Message display](../components/message-display.md) — FileAttachment and ImageAttachment rendering
