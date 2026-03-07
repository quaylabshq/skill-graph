# Rule: Deduplicate Global Event Listeners with `useSWRSubscription`

**ID:** client-event-listeners
**Category:** Client-Side Data Fetching (Priority 4 — MEDIUM-HIGH)

## Explanation

When multiple component instances each register their own global event listener (e.g., WebSocket `onmessage`, `window.onresize`, `document.onvisibilitychange`), you end up with N listeners doing the same work. This wastes memory, causes redundant processing, and risks memory leaks if cleanup is missed.

`useSWRSubscription()` from the `swr/subscription` package solves this by sharing a single subscription across all component instances that use the same key. SWR manages the lifecycle: the underlying listener is created when the first subscriber mounts and torn down when the last one unmounts. Every subscriber receives the same data through SWR's shared cache.

## Incorrect

```tsx
// StockPrice.tsx — each instance opens its own WebSocket
import { useState, useEffect } from "react";

function StockPrice({ symbol }: { symbol: string }) {
  const [price, setPrice] = useState<number | null>(null);

  useEffect(() => {
    // N instances of <StockPrice symbol="AAPL" /> = N WebSocket connections
    const ws = new WebSocket(`wss://api.example.com/stocks/${symbol}`);

    ws.addEventListener("message", (event) => {
      const data = JSON.parse(event.data);
      setPrice(data.price);
    });

    ws.addEventListener("error", (event) => {
      console.error("WebSocket error:", event);
    });

    return () => {
      ws.close();
    };
  }, [symbol]);

  if (price === null) return <span>Loading {symbol}...</span>;
  return <span>{symbol}: ${price.toFixed(2)}</span>;
}

// Dashboard.tsx — 3 instances = 3 WebSocket connections to the same endpoint
export default function Dashboard() {
  return (
    <div>
      <header><StockPrice symbol="AAPL" /></header>
      <aside><StockPrice symbol="AAPL" /></aside>
      <main><StockPrice symbol="AAPL" /></main>
    </div>
  );
}
```

Problem: three `<StockPrice symbol="AAPL" />` instances open three separate WebSocket connections to the same endpoint, tripling resource usage on both client and server.

## Correct

```tsx
// StockPrice.tsx — all instances share one WebSocket per symbol
import useSWRSubscription from "swr/subscription";
import type { SWRSubscription } from "swr/subscription";

interface StockMessage {
  price: number;
}

const subscribe: SWRSubscription<string, number, Error> = (key, { next }) => {
  const symbol = key.replace("stock-", "");
  const ws = new WebSocket(`wss://api.example.com/stocks/${symbol}`);

  ws.addEventListener("message", (event: MessageEvent) => {
    try {
      const data: StockMessage = JSON.parse(event.data);
      next(null, data.price);
    } catch (err) {
      next(err as Error);
    }
  });

  ws.addEventListener("error", () => {
    next(new Error(`WebSocket error for ${symbol}`));
  });

  // SWR calls this cleanup when the last subscriber unmounts
  return () => {
    ws.close();
  };
};

function StockPrice({ symbol }: { symbol: string }) {
  // SWR deduplicates: N instances with key "stock-AAPL" = 1 WebSocket
  const { data: price, error } = useSWRSubscription(
    `stock-${symbol}`,
    subscribe
  );

  if (error) return <span>Error: {error.message}</span>;
  if (price === undefined) return <span>Loading {symbol}...</span>;
  return <span>{symbol}: ${price.toFixed(2)}</span>;
}

// Dashboard.tsx — 3 instances = 1 WebSocket connection, shared data
export default function Dashboard() {
  return (
    <div>
      <header><StockPrice symbol="AAPL" /></header>
      <aside><StockPrice symbol="AAPL" /></aside>
      <main><StockPrice symbol="AAPL" /></main>
    </div>
  );
}
```

Benefit: one WebSocket connection per unique symbol, regardless of how many component instances subscribe. SWR handles lifecycle management -- the connection opens on first mount and closes when the last subscriber unmounts.

## When to Apply

- WebSocket connections shared across multiple components.
- `EventSource` / Server-Sent Events listeners.
- Global DOM event listeners (`resize`, `scroll`, `visibilitychange`) where multiple components react to the same event.
- Any subscription-based data source where N components should share 1 connection.

## Back to

- [overview.md](overview.md)

## See Also

- [swr-dedup.md](swr-dedup.md) — the same deduplication principle applied to HTTP requests
- [passive-event-listeners.md](passive-event-listeners.md) — optimizing the event listeners you do register
