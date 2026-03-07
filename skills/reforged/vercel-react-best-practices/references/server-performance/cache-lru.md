# Rule: Use LRU Cache for Cross-Request Data Sharing

**ID:** server-cache-lru
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

`React.cache()` only deduplicates within a single request. Once the response is sent, the cached data is discarded. For data that is expensive to compute and rarely changes (e.g., global config, popular product listings, shared metadata), you need a cache that persists across sequential requests.

An LRU (Least Recently Used) cache lives in the Node.js process memory and survives between requests. This is especially effective on **Vercel Fluid Compute**, where a single serverless function instance can handle multiple sequential requests before being evicted -- meaning the in-memory cache is reused across those requests.

Use `lru-cache` (or a similar library) with a TTL to avoid serving stale data indefinitely.

## Incorrect

```tsx
// lib/config.ts
import { cache } from "react";
import { db } from "@/lib/db";

// React.cache only deduplicates within ONE request.
// Every new request re-fetches from the database.
export const getSiteConfig = cache(async () => {
  console.log("Fetching site config from DB"); // logs on EVERY request
  return db.siteConfig.findFirst();
});

// 100 requests/second = 100 identical DB queries/second
// for data that changes once a day
```

Problem: site config rarely changes, but every single request pays the full database latency.

## Correct

```tsx
// lib/config.ts
import { LRUCache } from "lru-cache";
import { cache } from "react";
import { db } from "@/lib/db";

// Cross-request cache: persists in process memory between requests.
// max: number of entries, ttl: time-to-live in milliseconds.
const configCache = new LRUCache<string, SiteConfig>({
  max: 50,
  ttl: 1000 * 60 * 5, // 5 minutes
});

async function fetchSiteConfig(): Promise<SiteConfig> {
  const cached = configCache.get("site-config");
  if (cached) return cached;

  const config = await db.siteConfig.findFirst();
  if (config) {
    configCache.set("site-config", config);
  }
  return config!;
}

// Wrap in React.cache for per-request deduplication ON TOP of the LRU cache.
// This prevents multiple components in the same render from triggering
// even the LRU lookup multiple times.
export const getSiteConfig = cache(fetchSiteConfig);
```

## Practical Example: Popular Products

```tsx
// lib/products.ts
import { LRUCache } from "lru-cache";
import { cache } from "react";
import { db } from "@/lib/db";

type Product = {
  id: string;
  name: string;
  price: number;
  imageUrl: string;
};

const productCache = new LRUCache<string, Product>({
  max: 500,           // cache up to 500 products
  ttl: 1000 * 60 * 2, // 2-minute TTL
});

async function fetchProduct(id: string): Promise<Product | null> {
  const cached = productCache.get(id);
  if (cached) return cached;

  const product = await db.product.findUnique({ where: { id } });
  if (product) {
    productCache.set(id, product);
  }
  return product;
}

// Layer 1: LRU (cross-request) + Layer 2: React.cache (per-request)
export const getProduct = cache(fetchProduct);
```

## When to Apply

- Data that is read far more often than it is written (config, feature flags, popular entities).
- Expensive computations or aggregations (leaderboards, category trees).
- Deployments using Vercel Fluid Compute or long-lived Node.js servers where the process handles many sequential requests.
- Always pair with `React.cache()` so you get both cross-request **and** per-request deduplication.

## Caveats

- LRU caches are per-process. In a multi-instance deployment, each instance has its own cache. For globally shared state, use Redis or a similar external store.
- Always set a `ttl` to prevent serving stale data indefinitely.

## Back to

- [overview.md](overview.md)

## See Also

- [cache-react.md](cache-react.md) — per-request deduplication (use together with LRU)
- [hoist-static-io.md](hoist-static-io.md) — another module-level caching pattern for static assets
