# NoWhere Differentiable Math — Site Instructions

## Converting a LaTeX post to Quarto

1. Place your LaTeX folder inside `posts/<collection>/`, e.g.:
   ```
   posts/Analysis on Banach spaces/My_Post/
       main.tex
       preamble.sty
       biblio.bib
       cover.jpg          ← optional, shown as the post image
   ```

2. Add blog metadata to your `main.tex` (alongside `\title`, `\author`, `\date`):
   ```latex
   \postsubtitle{One sentence description of the post.}
   \posttags{Analysis, Measure Theory}   % optional — defaults to collection folder name
   ```
   Add to your shared `preamble.sty` (once only):
   ```latex
   \providecommand{\postsubtitle}[1]{}
   \providecommand{\posttags}[1]{}
   ```

3. Run the converter. From inside the post folder:
   ```powershell
   py .\latex2qmd.py
   ```
   This writes `index.qmd` in the same folder. The file is named `index.qmd` (not `main.qmd`) so Quarto generates clean URLs like `/posts/.../My_Post/` instead of `/posts/.../My_Post/main.html`.

4. **Batch mode** — regenerate all posts at once from the blog root:
   ```powershell
   py latex2qmd.py posts --all
   ```
   This finds every folder containing `main.tex` under `posts/`, skips `Future/`, and converts them all.

---

## Previewing locally

Start a live preview server (hot-reloads on file changes):
```powershell
quarto preview index.qmd
```
Then open the URL shown in the terminal.

To do a full site build without the server:
```powershell
quarto render
```

---

## Deploying to GitHub Pages

Just push to `main`:
```powershell
git add .
git commit -m "Add <post name>"
git push
```
GitHub Actions (`ci.yml`) builds and deploys the site automatically.

The `fetch-comments.yml` workflow runs every hour to update the recent comments sidebar.

---

## Dashboard tags and ordering

- Posts are ordered by `date` (newest first) on the homepage.
- Tags come from `\posttags{}` in `main.tex`, or default to the parent collection folder name.
- The featured post (large card) is always the most recent post.
- To hide a post from the site, place it inside `posts/Future/` — this folder is excluded from rendering.

---

## What to change

| Goal | Edit | Re-run converter? |
|---|---|---|
| Visual styling (colors, spacing, theorem boxes) | `custom_theorems.css` or `assets/css/dashboard.css` | No |
| Global MathJax config (delimiters, macros) | `_quarto.yml` | No |
| How LaTeX is converted (equation labels, figure syntax, cross-refs) | `latex2qmd.py` | **Yes** — `py latex2qmd.py posts --all` |
| Post-specific macros | Edit `preamble.sty`, then re-run converter | **Yes**, on affected posts |
| Equation Labels (names instead of numbers) | Use `\tag{label}` inside math envs | **Yes** |
| Post tags/categories | Use `\posttags{...}` in `main.tex` | **Yes** |
| Post subtitle | Use `\postsubtitle{...}` in `main.tex` | **Yes** |