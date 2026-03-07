# Rule: Put Interaction Logic in Event Handlers, Not Effects

**ID:** rerender-move-effect-to-event
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When a side effect is a direct response to a user action (click, submit, toggle), run it in the event handler. Do not model it as a state change that triggers a `useEffect`. The effect pattern adds indirection: set state, re-render, effect fires, potentially set more state, re-render again. The event handler pattern is direct: user acts, code runs, done.

Effects should synchronize with external systems, not orchestrate interaction flows.

## Incorrect

```tsx
import { useState, useEffect } from "react";

function ContactForm() {
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });
  const [submitted, setSubmitted] = useState(false);

  // Side effect modeled as state change + effect
  useEffect(() => {
    if (submitted) {
      sendAnalytics("form_submitted", formData);
      showToast("Message sent!");
      setSubmitted(false); // reset flag — yet another render
    }
  }, [submitted, formData]);

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    submitForm(formData);
    setSubmitted(true); // triggers effect on next render
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={formData.name}
        onChange={(e) => setFormData((d) => ({ ...d, name: e.target.value }))}
      />
      <input
        value={formData.email}
        onChange={(e) => setFormData((d) => ({ ...d, email: e.target.value }))}
      />
      <textarea
        value={formData.message}
        onChange={(e) => setFormData((d) => ({ ...d, message: e.target.value }))}
      />
      <button type="submit">Send</button>
    </form>
  );
}
```

Problem: three render cycles per submit (setFormData, setSubmitted true, setSubmitted false). The analytics and toast are delayed until after the re-render. The `submitted` state is boilerplate that exists only to trigger the effect.

## Correct

```tsx
import { useState } from "react";

function ContactForm() {
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    // All side effects run directly in the event handler
    submitForm(formData);
    sendAnalytics("form_submitted", formData);
    showToast("Message sent!");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={formData.name}
        onChange={(e) => setFormData((d) => ({ ...d, name: e.target.value }))}
      />
      <input
        value={formData.email}
        onChange={(e) => setFormData((d) => ({ ...d, email: e.target.value }))}
      />
      <textarea
        value={formData.message}
        onChange={(e) => setFormData((d) => ({ ...d, message: e.target.value }))}
      />
      <button type="submit">Send</button>
    </form>
  );
}
```

Benefit: no extra state, no extra renders, no timing ambiguity. The side effects execute synchronously in response to the user action.

## When to Apply

- Analytics tracking triggered by user clicks or form submissions.
- Toast notifications shown after an action.
- Navigation triggered by a button click (use `router.push()` in the handler).
- Any "do X when user does Y" pattern — if you can point to a specific user action, use the event handler.

## When Effects ARE Appropriate

- Synchronizing with external systems on mount/unmount (WebSocket connections, event listeners).
- Reacting to prop/state changes that are NOT caused by a single user interaction (e.g., data fetched by a parent).
- Setting up subscriptions that should persist across the component lifecycle.

## Back to

- [overview.md](overview.md)

## See Also

- [derived-state-no-effect.md](derived-state-no-effect.md) — another common case of effect misuse
