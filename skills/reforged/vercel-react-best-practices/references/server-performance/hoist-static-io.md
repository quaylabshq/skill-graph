# Rule: Hoist Static Asset Loading to Module Level

**ID:** server-hoist-static-io
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

Static assets -- fonts, logos, configuration files, templates -- do not change between requests. If you read them inside a request handler or component function, the I/O happens on every single request. By hoisting the read to module scope (top level of the file), the I/O runs once when the module is first imported, and all subsequent requests reuse the result from memory.

This is especially important for **OG image generation** with `next/og` `ImageResponse`, where font files and logo images are commonly loaded. Reading a 200KB font file from the filesystem on every OG image request adds unnecessary latency and disk I/O.

## Incorrect

```tsx
// app/api/og/route.tsx
import { ImageResponse } from "next/og";

export async function GET(request: Request) {
  // BAD: reads the font file from disk on EVERY request
  const fontData = await fetch(
    new URL("../../../public/fonts/Inter-Bold.ttf", import.meta.url)
  ).then((res) => res.arrayBuffer());

  // BAD: reads the logo on every request
  const logoData = await fetch(
    new URL("../../../public/logo.png", import.meta.url)
  ).then((res) => res.arrayBuffer());

  return new ImageResponse(
    (
      <div style={{ display: "flex", fontSize: 48 }}>
        <img src={logoData as any} width={64} height={64} />
        <span>My Site</span>
      </div>
    ),
    {
      width: 1200,
      height: 630,
      fonts: [{ name: "Inter", data: fontData, style: "normal" }],
    }
  );
}
```

Problem: two filesystem reads on every request for files that never change.

## Correct

```tsx
// app/api/og/route.tsx
import { ImageResponse } from "next/og";

// Hoisted to module level — runs ONCE when the module loads,
// then every request reuses the result from memory.
const fontData = fetch(
  new URL("../../../public/fonts/Inter-Bold.ttf", import.meta.url)
).then((res) => res.arrayBuffer());

const logoData = fetch(
  new URL("../../../public/logo.png", import.meta.url)
).then((res) => res.arrayBuffer());

export async function GET(request: Request) {
  // Await the already-resolved (or in-flight) promises
  const [font, logo] = await Promise.all([fontData, logoData]);

  return new ImageResponse(
    (
      <div style={{ display: "flex", fontSize: 48 }}>
        <img src={logo as any} width={64} height={64} />
        <span>My Site</span>
      </div>
    ),
    {
      width: 1200,
      height: 630,
      fonts: [{ name: "Inter", data: font, style: "normal" }],
    }
  );
}
```

## Also Works: `fs.readFileSync` at Module Level

```tsx
// lib/templates.ts
import { readFileSync } from "node:fs";
import { join } from "node:path";

// Synchronous read at module level — runs once at startup
const emailTemplate = readFileSync(
  join(process.cwd(), "templates/welcome.html"),
  "utf-8"
);

export function getWelcomeEmail(name: string): string {
  return emailTemplate.replace("{{name}}", name);
}
```

## Pattern: Config Files

```tsx
// lib/config.ts
import { readFileSync } from "node:fs";
import { join } from "node:path";

// Parse once at module load, reuse across all requests
const rawConfig = readFileSync(
  join(process.cwd(), "config/features.json"),
  "utf-8"
);
export const featureFlags: Record<string, boolean> = JSON.parse(rawConfig);
```

## When to Apply

- Font loading for `ImageResponse` / OG image routes.
- Logo or icon files used in server-rendered images or PDFs.
- Static templates (HTML email templates, PDF templates).
- Configuration files (JSON, YAML) that do not change at runtime.
- Any `readFile` / `fetch` for a file that ships with the deployment.

## Back to

- [overview.md](overview.md)

## See Also

- [cache-lru.md](cache-lru.md) — for dynamic data that changes but should persist across requests
- [../bundle-size/overview.md](../bundle-size/overview.md) — keeping static assets out of client bundles
