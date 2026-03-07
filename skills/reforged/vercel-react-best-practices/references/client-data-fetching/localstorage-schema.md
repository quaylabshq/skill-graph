# Rule: Version and Minimize localStorage Data

**ID:** client-localstorage-schema
**Category:** Client-Side Data Fetching (Priority 4 — MEDIUM-HIGH)

## Explanation

localStorage persists across sessions, but its data has no built-in schema or versioning. Without discipline, apps accumulate stale keys, store overly large objects, and crash when the data shape changes between deployments. Three rules prevent these problems:

1. **Version-prefix keys** — include a version number in the key (e.g., `v1:user-prefs`) so you can migrate or discard stale data when the schema changes.
2. **Store only needed fields** — pick the minimal set of fields instead of dumping entire API responses. localStorage has a ~5MB limit per origin, and large payloads slow down `getItem`/`setItem` because they run on the main thread synchronously.
3. **Always wrap in try-catch** — localStorage throws in private browsing mode (some Safari versions), when the quota is exceeded, or when storage is disabled by policy. Unhandled exceptions here break the entire component.

## Incorrect

```tsx
import { useEffect, useState } from "react";

interface User {
  id: string;
  name: string;
  email: string;
  avatarUrl: string;
  role: string;
  permissions: string[];
  preferences: Record<string, unknown>;
  loginHistory: { date: string; ip: string }[];
  metadata: Record<string, unknown>;
}

function useUser() {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    // No try-catch — crashes in Safari private mode or when quota is exceeded
    const cached = localStorage.getItem("user");
    if (cached) {
      // No version check — breaks if User shape changes between deploys
      setUser(JSON.parse(cached));
      return;
    }

    fetch("/api/user")
      .then((res) => res.json())
      .then((data: User) => {
        // Stores the entire object including loginHistory, metadata, etc.
        // Wastes storage and slows down synchronous getItem/setItem
        localStorage.setItem("user", JSON.stringify(data));
        setUser(data);
      });
  }, []);

  return user;
}
```

Problems: no try-catch around localStorage access, no versioning so schema changes cause runtime errors on returning users, and the full user object (including large arrays like `loginHistory`) is stored unnecessarily.

## Correct

```tsx
import { useEffect, useState, useCallback } from "react";

// --- Storage schema types ---

const STORAGE_VERSION = "v2";

interface CachedUserData {
  id: string;
  name: string;
  avatarUrl: string;
}

interface StorageEnvelope<T> {
  version: string;
  timestamp: number;
  data: T;
}

// --- Safe localStorage helpers ---

function storageGet<T>(key: string): T | null {
  try {
    const raw = localStorage.getItem(`${STORAGE_VERSION}:${key}`);
    if (!raw) return null;

    const envelope: StorageEnvelope<T> = JSON.parse(raw);

    // Reject data from a different version
    if (envelope.version !== STORAGE_VERSION) {
      localStorage.removeItem(`${STORAGE_VERSION}:${key}`);
      return null;
    }

    // Reject stale data (e.g., older than 1 hour)
    const ONE_HOUR = 60 * 60 * 1000;
    if (Date.now() - envelope.timestamp > ONE_HOUR) {
      localStorage.removeItem(`${STORAGE_VERSION}:${key}`);
      return null;
    }

    return envelope.data;
  } catch {
    // localStorage unavailable, corrupt JSON, or quota error
    return null;
  }
}

function storageSet<T>(key: string, data: T): void {
  try {
    const envelope: StorageEnvelope<T> = {
      version: STORAGE_VERSION,
      timestamp: Date.now(),
      data,
    };
    localStorage.setItem(`${STORAGE_VERSION}:${key}`, JSON.stringify(envelope));
  } catch {
    // Quota exceeded or storage unavailable — fail silently
    // The app continues to work; it just won't cache this value
  }
}

// --- Migration logic ---

function migrateStorage(): void {
  try {
    // Clean up keys from previous versions
    const previousVersions = ["v1"];
    for (const oldVersion of previousVersions) {
      const keysToRemove: string[] = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key?.startsWith(`${oldVersion}:`)) {
          keysToRemove.push(key);
        }
      }
      keysToRemove.forEach((key) => localStorage.removeItem(key));
    }
  } catch {
    // Storage unavailable — nothing to migrate
  }
}

// --- Hook ---

interface User {
  id: string;
  name: string;
  email: string;
  avatarUrl: string;
  role: string;
  permissions: string[];
  preferences: Record<string, unknown>;
  loginHistory: { date: string; ip: string }[];
  metadata: Record<string, unknown>;
}

function useUser() {
  const [user, setUser] = useState<CachedUserData | null>(() => {
    // Run migration on first load
    migrateStorage();
    // Read from cache synchronously to avoid flash of loading state
    return storageGet<CachedUserData>("user");
  });

  useEffect(() => {
    // Always revalidate from the server
    fetch("/api/user")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((fullUser: User) => {
        // Store only the fields the UI actually needs
        const minimal: CachedUserData = {
          id: fullUser.id,
          name: fullUser.name,
          avatarUrl: fullUser.avatarUrl,
        };
        storageSet("user", minimal);
        setUser(minimal);
      })
      .catch((err) => {
        console.error("Failed to fetch user:", err);
        // Cached data (if any) remains in state as a fallback
      });
  }, []);

  return user;
}
```

Benefits:
- **Versioned keys** (`v2:user`) prevent shape mismatches after deploys.
- **Minimal data** (3 fields instead of the full object) respects the 5MB quota and keeps synchronous `getItem` fast.
- **try-catch everywhere** ensures the app works in private browsing, with storage disabled, or when quota is exceeded.
- **Migration function** cleans up keys from previous versions so stale data does not accumulate.
- **TTL check** discards data older than one hour so users do not see dangerously stale information.

## When to Apply

- Caching user preferences, theme settings, or recently viewed items in localStorage.
- Any `localStorage.getItem` / `setItem` call in client components.
- Apps that have been deployed multiple times and may have old-format data on returning users' devices.

## Back to

- [overview.md](overview.md)

## See Also

- [swr-dedup.md](swr-dedup.md) — for in-memory caching and deduplication, prefer SWR over manual localStorage caching
