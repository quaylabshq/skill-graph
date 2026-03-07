# Rule: Use `useEffectEvent` for Latest-Value Callbacks in Effects

**ID:** advanced-use-latest
**Category:** Advanced Patterns (Priority 8 — LOW)

## Explanation

When an effect sets up a long-lived connection (WebSocket, EventSource, Intersection Observer, etc.) and invokes a callback on each message or event, adding that callback to the dependency array causes the effect to tear down and reconnect every time the callback identity changes. This is wasteful and can cause dropped messages during reconnection.

React's experimental `useEffectEvent` hook solves this by creating a stable function identity that always reads the latest closure values when called. The returned function is never added to the dependency array, so the effect runs only when its true dependencies (like a URL) change, while still invoking the most up-to-date callback.

Until `useEffectEvent` is stable, the manual ref pattern (see [event-handler-refs.md](event-handler-refs.md)) achieves the same result.

## Incorrect

```tsx
import { useEffect } from "react";

interface ChatProps {
  roomId: string;
  onMessage: (msg: { user: string; text: string }) => void;
}

function Chat({ roomId, onMessage }: ChatProps) {
  useEffect(() => {
    // Opens a new WebSocket connection
    const ws = new WebSocket(`wss://chat.example.com/${roomId}`);

    ws.addEventListener("message", (event) => {
      const msg = JSON.parse(event.data);
      onMessage(msg);
    });

    return () => ws.close();
  }, [roomId, onMessage]);
  //         ^^^^^^^^^^
  // onMessage changes on every parent render if passed as an inline arrow,
  // causing the WebSocket to disconnect and reconnect each time.

  return <div>Connected to {roomId}</div>;
}
```

Problem: the parent renders `<Chat roomId="general" onMessage={(msg) => setMessages(prev => [...prev, msg])} />`. The inline arrow creates a new reference each render, so `onMessage` is a new value every time. The effect re-runs, closing the WebSocket and opening a fresh one -- dropping any in-flight messages.

## Correct

```tsx
import {
  useEffect,
  experimental_useEffectEvent as useEffectEvent,
} from "react";

interface ChatProps {
  roomId: string;
  onMessage: (msg: { user: string; text: string }) => void;
}

function Chat({ roomId, onMessage }: ChatProps) {
  // Stable identity — always calls the latest `onMessage` when invoked
  const onMsg = useEffectEvent(onMessage);

  useEffect(() => {
    const ws = new WebSocket(`wss://chat.example.com/${roomId}`);

    ws.addEventListener("message", (event) => {
      const msg = JSON.parse(event.data);
      onMsg(msg); // latest onMessage, stable reference
    });

    return () => ws.close();
  }, [roomId]);
  // Only reconnects when roomId changes — exactly the right behavior.

  return <div>Connected to {roomId}</div>;
}
```

Benefit: the WebSocket connection is stable for a given `roomId`. When the parent re-renders and provides a new `onMessage` arrow, `onMsg` still has a stable identity so the effect does not re-run. When a message arrives, `onMsg` delegates to whatever `onMessage` is at that moment -- always the latest version.

### Fallback: Manual Ref Pattern (Stable React)

If `useEffectEvent` is not available in your React version, use a ref:

```tsx
import { useEffect, useRef } from "react";

function Chat({ roomId, onMessage }: ChatProps) {
  const onMessageRef = useRef(onMessage);
  onMessageRef.current = onMessage;

  useEffect(() => {
    const ws = new WebSocket(`wss://chat.example.com/${roomId}`);

    ws.addEventListener("message", (event) => {
      const msg = JSON.parse(event.data);
      onMessageRef.current(msg);
    });

    return () => ws.close();
  }, [roomId]);

  return <div>Connected to {roomId}</div>;
}
```

Same result: the effect only depends on `roomId`, and the ref always points to the latest callback.

## When to Apply

- WebSocket, Server-Sent Events, or long-polling effects where a handler prop changes frequently.
- Intersection Observer or Mutation Observer callbacks derived from component state or props.
- Any `useEffect` where a callback dependency causes unnecessary teardown/setup cycles, but the subscription target (URL, element, channel) has not changed.

## Back to

- [overview.md](overview.md)

## See Also

- [event-handler-refs.md](event-handler-refs.md) — the manual ref approach for stable callbacks (works without experimental APIs)
- [../rerender-optimization/memo.md](../rerender-optimization/memo.md) — memoize parent components to stabilize callback prop identities
- [../rerender-optimization/defer-reads.md](../rerender-optimization/defer-reads.md) — avoid subscribing to state that is only needed in event handlers
