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

Just push to `master` (or your active working branch):
```powershell
git add .
git commit -m "Add <post name>"
GitHub Actions (`quarto_publish.yml`) automatically builds, converts LaTeX images to SVG, checks for dead links, and seamlessly overrides the gh-pages branch to deploy the site natively.

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
| Global Theme & Typography | `styles.scss` (Primary color, font families) | No |
| LaTeX Link Colors | `styles.scss` (RoyalBlue/ForestGreen/NavyBlue logic) | No |
| Homepage Dashboard (Grids, Tiles) | `assets/css/dashboard.css` (Handles dark mode natively via `[data-bs-theme="dark"]`) | No |
| Latex-style theorem boxes | `custom_theorems.css` | No |
| Dashboard spacing/Title hiding | `index.qmd` (header-includes) | No |
| Global MathJax config (delimiters, macros) | `_quarto.yml` | No |
| How LaTeX is converted (equation labels, figure syntax, cross-refs) | `latex2qmd.py` | **Yes** — `py latex2qmd.py posts --all` |
| Post-specific macros | Edit `preamble.sty`, then re-run converter | **Yes**, on affected posts |
| Equation Labels (names instead of numbers) | Use `\tag{label}` inside math envs | **Yes** |
| Post tags/categories | Use `\posttags{...}` in `main.tex` | **Yes** |
| Post subtitle | Use `\postsubtitle{...}` in `main.tex` | **Yes** |
| Cross-post references | Use `\postref{...}{...}{...}` in `main.tex` | **Yes** — must use `--all` |
| Checking for broken links | Run `py check_links.py` entirely locally after generating the `_site` directory to view the report | **No** |

---

## Design & Customization

The site uses a layered CSS/SCSS architecture to replicate a high-end mathematical typesetting aesthetic:

### 1. Global Styling (`styles.scss`)
This is where the "Terence Tao" aesthetic is defined. It overrides Quarto's default Bootstrap variables and implements the LaTeX-style link coloring:
- **Primary Color:** Set to a deep navy (`#1E3A8A`).
- **Typography:** Uses serif fonts (*Merriweather*, *Georgia*) for article content and sans-serif (*Inter*) for UI elements.
- **Link Logic:** 
  - **Internal Refs (Theorems, Eqs):** `RoyalBlue` (#4169E1) — *scoped to article content*.
  - **Citations:** `ForestGreen` (#228B22).
  - **External Links:** `NavyBlue` (#000080).

### 2. Homepage Listing (`assets/css/dashboard.css`)
Controls the layout of the homepage grid and cards. 
- Edit the `.featured-pane .pane-label` and `.recent-list-pane .pane-label` to change the colors of the "Latest Post" and "Most recent posts" header bars.
- Controls the hover effects and tile shadows.

### 3. Homepage Layout Overrides (`index.qmd`)
The homepage title block ("NoWhere Differentiable Math") is hidden via a CSS block in the `header-includes` section. It also manages the top padding between the navbar and the dashboard.

---

## Cross-post references (`\postref`)

Use `\postref` to link from one post to another, optionally targeting a specific theorem, equation, or definition.

### Syntax

```latex
\postref{folder-path}{label}{display text}
```

| Argument | Description |
|---|---|
| `folder-path` | Relative path from `posts/` to the target folder, e.g. `Stochastic Calculus/Martingales` |
| `label` | LaTeX label in the target post (e.g. `thm:doobs`). Leave empty `{}` to link to the post without an anchor. |
| `display text` | What the reader sees, e.g. `Theorem 3.2` or `the Martingales post` |

### Examples

**Link to a specific theorem in another post:**
```latex
By \postref{Stochastic Calculus/Martingales}{thm:doobs-hilbert}{Doob's maximal inequality}, we obtain...
```

**Link to another post (no specific anchor):**
```latex
As shown in \postref{Analysis on Banach spaces/Bochner_integral}{}{the Bochner integral post}, ...
```

### How it renders

| Environment | What happens |
|---|---|
| **pdflatex** | Renders as an `\href` linking to the live blog URL (`nowheredifferentiable.com/posts/...`). The label argument is ignored by LaTeX — it only uses the folder path and display text. Compiles without error. |
| **Quarto (via `latex2qmd.py --all`)** | The converter resolves the label via a global registry to compute the correct relative `.qmd` path and anchor (e.g. `../../Martingales/index.qmd#thm-doobs-hilbert`). If the label is not found, it emits a **warning** and links to the post without an anchor. |
| **Quarto (single-folder mode)** | Without `--all`, no registry is built. The converter falls back to an absolute URL to the live site. |

### Important notes

- **You must use `--all` mode** (`py latex2qmd.py posts --all`) for cross-post labels to resolve. Single-folder mode has no access to labels in other posts.
- **Folder paths must match exactly.** If you rename or move a post folder, update all `\postref` commands pointing to it. The converter will emit a warning if a referenced label is not found.
- **The command is already defined** in all `preamble.sty` files. No setup needed — just use it in your `main.tex`.