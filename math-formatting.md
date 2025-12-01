---
layout: page
title: Comment Formatting
subtitle: How to write mathematics in the comments
---

### 1. Inline Math

To write math inside a sentence, use single dollar signs `$`.
**Crucial:** You must **not** put spaces next to the dollar signs.

- **Correct:** `Let $\epsilon > 0$ be given.` $\rightarrow$ Let $\epsilon > 0$ be given.
- **Incorrect:** `Let $ \epsilon > 0 $ be given.` $\rightarrow$ (Will render as raw text)

### 2. Block Math (Centered Equations)

To write large equations on their own line, use double dollar signs `$$`.
**Crucial:** You must leave a **blank line** above the equation for it to render correctly.

**Incorrect (No blank line):**

```text
The formula is
$$
\int f(x) dx
$$
```

**Correct (With blank line):**

```text
The formula is

$$
\int f(x) dx
$$
```

### 3. Editing Comments

You cannot edit comments directly on this blog page.

1. Look at your posted comment.
2. Click the timestamp (e.g., "5 minutes ago") next to your name.
3. This takes you to GitHub, where you can click the three dots (...) to Edit or Delete.
