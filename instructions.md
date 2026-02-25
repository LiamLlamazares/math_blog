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
   \subtitle{One sentence description of the post.}
   \tags{Analysis, Measure Theory}   % optional — defaults to collection folder name
   ```
   Add to your shared `preamble.sty` (once only):
   ```latex
   \newcommand{\subtitle}[1]{}
   \newcommand{\tags}[1]{}
   ```

3. Copy `latex2qmd.py` into the post folder (done once per post). Then from inside the folder run:
   ```powershell
   py .\latex2qmd.py
   ```
   This writes `index.qmd` in the same folder.

---

## Previewing locally

Start a live preview server (hot-reloads on file changes):
```powershell
quarto preview index.qmd
```
Then open **http://127.0.0.1:4256/** in your browser.

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
- Tags come from `\tags{}` in `main.tex`, or default to the parent collection folder name.
- The featured post (large card) is always the most recent post.
- To hide a post from the site, place it inside `posts/Future/` — this folder is excluded from rendering.