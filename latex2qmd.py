#!/usr/bin/env python3
"""
latex2qmd.py — Convert a LaTeX project folder into a Quarto blog post.

Usage:
    python latex2qmd.py /path/to/latex/folder [--blog-dir /path/to/blog]

Input folder must contain:
    - main.tex (or specified .tex file)
    - preamble.sty (or specified .sty file)
    - biblio.bib (optional)
    - cover.jpg/png (optional, used as post image)

Metadata is extracted from:
    - \title{}, \author{}, \date{} — standard LaTeX commands
    - \description{} — becomes the post subtitle
    - Parent folder name — becomes the default tag
    - cover.* — auto-detected as post image

Output:
    - index.qmd written into the folder
    - If --blog-dir is given, copies entire folder into blog/posts/
"""

import argparse
import re
import sys
import os
import shutil
import textwrap
from datetime import date
from pathlib import Path


# ---------------------------------------------------------------------------
# 1. FOLDER-BASED METADATA (replaces info.txt)
# ---------------------------------------------------------------------------

def detect_cover_image(folder: Path) -> str | None:
    """Look for cover.jpg, cover.png, etc. in the folder."""
    for ext in ('jpg', 'jpeg', 'png', 'svg', 'webp'):
        candidates = list(folder.glob(f'cover.{ext}')) + list(folder.glob(f'Cover.{ext}'))
        if candidates:
            return candidates[0].name
    return None


def infer_tags(folder: Path) -> list[str]:
    """Default tag = parent folder name (e.g. 'analysis' from latex/analysis/MyPost)."""
    parent = folder.parent.name
    # Don't use 'latex' or the repo root as a tag
    if parent.lower() in ('latex', '.', ''):
        return []
    # Convert underscores to spaces, title-case
    tag = parent.replace('_', ' ').title()
    return [tag]


# ---------------------------------------------------------------------------
# 2. PARSE main.tex METADATA
# ---------------------------------------------------------------------------

def _extract_braced(text: str, cmd: str) -> str | None:
    """Extract content of \\cmd{...}, handling nested braces."""
    pattern = re.compile(r'\\' + cmd + r'\s*\{')
    m = pattern.search(text)
    if not m:
        return None
    start = m.end()
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
        i += 1
    return text[start:i - 1].strip()


def parse_tex_metadata(tex: str) -> dict:
    """Extract title, author, date, description from LaTeX source."""
    meta = {}
    title = _extract_braced(tex, 'title')
    if title:
        meta['title'] = title

    author = _extract_braced(tex, 'author')
    if author:
        meta['author'] = author

    date_str = _extract_braced(tex, 'date')
    if date_str:
        if '\\today' in date_str:
            meta['date'] = date.today().isoformat()
        else:
            meta['date'] = date_str
    else:
        meta['date'] = date.today().isoformat()

    # Extract \subtitle{...} → subtitle
    desc = _extract_braced(tex, 'subtitle')
    if desc:
        meta['subtitle'] = desc

    # Extract \tags{...} → tags override (comma-separated)
    posttags = _extract_braced(tex, 'tags')
    if posttags:
        meta['tags'] = [t.strip() for t in posttags.split(',')]

    # Check for bibliography
    bib_match = re.search(r'\\bibliography\{([^}]+)\}', tex)
    if bib_match:
        bib_name = bib_match.group(1)
        if not bib_name.endswith('.bib'):
            bib_name += '.bib'
        meta['bibliography'] = bib_name

    return meta


def extract_body(tex: str) -> str:
    """Extract content between \\begin{document} and \\end{document}."""
    begin = re.search(r'\\begin\{document\}', tex)
    end = re.search(r'\\end\{document\}', tex)
    if not begin or not end:
        print("ERROR: Could not find \\begin{document} or \\end{document}")
        sys.exit(1)
    body = tex[begin.end():end.start()]
    # Strip structural commands
    body = re.sub(r'\\maketitle', '', body)
    body = re.sub(r'\\tableofcontents', '', body)
    body = re.sub(r'\\bibliography\{[^}]*\}', '', body)
    # Strip \title{...}, \author{...}, \date{...} from the body
    for cmd in ['title', 'author', 'date']:
        pat = re.compile(r'\\' + cmd + r'\s*\{', re.DOTALL)
        m = pat.search(body)
        if m:
            depth = 1
            i = m.end()
            while i < len(body) and depth > 0:
                if body[i] == '{':
                    depth += 1
                elif body[i] == '}':
                    depth -= 1
                i += 1
            body = body[:m.start()] + body[i:]
    return body


# ---------------------------------------------------------------------------
# 3. PARSE preamble.sty FOR MATHJAX MACROS
# ---------------------------------------------------------------------------

def parse_preamble_macros(sty_path: Path) -> dict:
    """
    Extract \\newcommand and \\renewcommand definitions from preamble.sty.
    Returns a dict: macro_name -> (replacement, num_args).
    Only extracts simple macros suitable for MathJax.
    """
    macros = {}
    if not sty_path.exists():
        print(f"WARNING: {sty_path} not found. No custom macros will be injected.")
        return macros

    with open(sty_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match \newcommand{\name}[n]{...} or \newcommand{\name}{...}
    # Also \renewcommand
    # We need to handle nested braces in the replacement body
    pattern = re.compile(
        r'\\(?:new|renew)command\{\\([a-zA-Z]+)\}'
        r'(?:\[(\d)\])?'  # optional [n] for number of args
    )

    pos = 0
    while pos < len(content):
        m = pattern.search(content, pos)
        if not m:
            break

        name = m.group(1)
        num_args = int(m.group(2)) if m.group(2) else 0

        # Now extract the braced body after the match
        body_start = m.end()
        # Skip whitespace
        while body_start < len(content) and content[body_start] in ' \t\n\r':
            body_start += 1

        if body_start >= len(content) or content[body_start] != '{':
            pos = m.end()
            continue

        # Extract balanced braces
        depth = 0
        i = body_start
        while i < len(content):
            if content[i] == '{':
                depth += 1
            elif content[i] == '}':
                depth -= 1
                if depth == 0:
                    break
            i += 1

        replacement = content[body_start + 1:i]

        # Skip macros that use LaTeX-only packages or are too complex
        skip_patterns = [
            r'\\RequirePackage', r'\\ProvidesPackage', r'\\usepackage',
            r'\\newtheorem', r'\\theoremstyle', r'\\newaliascnt',
            r'\\aliascntresetthe', r'\\crefname', r'\\Crefname',
            r'\\DeclareMathOperator', r'\\xqed',
            r'\\todo', r'\\newenvironment',
            r'\\leavevmode', r'\\microtypesetup',
            r'\\faEnvelopeO', r'\\textcolor',
        ]
        skip = False
        for sp in skip_patterns:
            if re.search(sp, replacement):
                skip = True
                break
        # Also skip if the name itself is a structural command
        structural = {
            'ProvidesPackage', 'RequirePackage',
            'theoremstyle', 'newtheorem', 'newaliascnt',
            'tableofcontents', 'summaryname',
        }
        if name in structural:
            skip = True

        # Skip macros with newlines in the body (multi-line = too complex for MathJax)
        if '\n' in replacement:
            skip = True

        if not skip and replacement:
            macros[name] = (replacement, num_args)

        pos = i + 1

    # Physics-package macros: \qty is handled at Python level via _expand_qty().
    # \bm is provided as a macro fallback since the MathJax bm extension
    # is not available on all CDN builds.
    if 'bm' not in macros:
        macros['bm'] = (r'\boldsymbol{#1}', 1)

    return macros


def format_mathjax_macros(macros: dict) -> str:
    """Format macros dict into a MathJax JS configuration block."""
    lines = []
    for name, (repl, nargs) in sorted(macros.items()):
        # Escape backslashes for JS string
        js_repl = repl.replace('\\', '\\\\')
        # Escape quotes
        js_repl = js_repl.replace('"', '\\"')
        if nargs > 0:
            lines.append(f'              {name}: ["{js_repl}", {nargs}]')
        else:
            lines.append(f'              {name}: "{js_repl}"')
    return ',\n'.join(lines)


# ---------------------------------------------------------------------------
# 4. BODY CONVERSION: LaTeX → Quarto Markdown
# ---------------------------------------------------------------------------

# Environment types and their Quarto div classes
THEOREM_ENVS = {
    'theorem': 'thm',
    'proposition': 'prp',
    'lemma': 'lem',
    'corollary': 'cor',
    'definition': 'def',
    'example': 'exm',
    'exercise': 'exr',
    'remark': 'rem',
    'conjecture': 'cnj',
}


def _find_matching_end(text: str, env_name: str, start: int) -> int:
    """Find the position of the matching \\end{env_name} for a \\begin at start."""
    depth = 1
    pattern = re.compile(
        r'\\(begin|end)\{' + re.escape(env_name) + r'\}'
    )
    pos = start
    while depth > 0:
        m = pattern.search(text, pos)
        if not m:
            return len(text)
        if m.group(1) == 'begin':
            depth += 1
        else:
            depth -= 1
        pos = m.end()
    return pos


def _expand_qty(text: str) -> str:
    """Convert \\qty(expr) -> \\left(expr\\right), \\qty[...] -> \\left[...\\right], \\qty{...} -> \\left\\{...\\right\\}.
    Uses balanced-delimiter matching so nested \\qty calls work correctly.
    """
    OPEN  = {'(': ')', '[': ']', '{': '}'}
    LATEX = {'(': ('\\left(', '\\right)'),
              '[': ('\\left[', '\\right]'),
              '{': ('\\left\\{', '\\right\\}')}
    result = []
    i = 0
    while i < len(text):
        if text[i:i+4] == '\\qty' and (i + 4) < len(text) and text[i+4] in OPEN:
            delim = text[i+4]
            close = OPEN[delim]
            latex_open, latex_close = LATEX[delim]
            depth = 1
            j = i + 5
            while j < len(text) and depth > 0:
                if text[j] == delim:
                    depth += 1
                elif text[j] == close:
                    depth -= 1
                j += 1
            inner = text[i+5:j-1]
            result.append(latex_open)
            result.append(_expand_qty(inner))  # recurse for nested \qty
            result.append(latex_close)
            i = j
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)


def convert_body(body: str) -> str:
    """Apply all mechanical transformations to the LaTeX body."""
    text = body

    # Map of LaTeX labels to generated Quarto IDs, populated during conversion
    label_map = {}  # e.g. {'density': 'eq-density', 'independence': 'prp-1', ...}
    # For item-level labels: label -> (parent_qid, item_name)
    item_label_map = {}  # e.g. {'inversion': ('prp-1', 'Inversion')}

    # --- Pass 0: Strip TODO notes, end-of-theorem symbols, expand \qty,
    #             and strip blog metadata commands from body ---
    text = re.sub(r'\\liam\{[^}]*\}', '', text)
    text = re.sub(r'\\exampleSymbol', '', text)
    text = re.sub(r'\\exerciseSymbol', '', text)
    # Strip blog metadata commands that should only appear in front matter
    text = re.sub(r'\\subtitle\{[^}]*\}', '', text)
    text = re.sub(r'\\tags\{[^}]*\}', '', text)
    text = _expand_qty(text)

    # --- Pass 1: Sections ---
    text = re.sub(r'\\section\{([^}]*)\}', r'## \1', text)
    text = re.sub(r'\\subsection\{([^}]*)\}', r'### \1', text)
    text = re.sub(r'\\subsubsection\{([^}]*)\}', r'#### \1', text)

    # --- Pass 2: Theorem-like environments ---
    # Process from innermost out: we iterate until no more matches
    env_counter = {}  # running counter per type for auto-generated IDs

    def replace_theorem_env(m):
        env_name = m.group(1)
        label = m.group(2)  # may be None
        opt_name = m.group(3)  # may be None (optional [Name])

        prefix = THEOREM_ENVS.get(env_name, env_name[:3])

        if label:
            # Sanitize label for use as ID
            label_id = label.replace(':', '-').replace(' ', '-').replace('_', '-').lower()
            div_id = f"#{prefix}-{label_id}"
        else:
            # Auto-generate an ID
            env_counter[env_name] = env_counter.get(env_name, 0) + 1
            div_id = f"#{prefix}-{env_counter[env_name]}"

        attrs = [div_id]
        if opt_name:
            attrs.append(f'name="{opt_name}"')

        return f'\n::: {{{" ".join(attrs)}}}\n'

    # Match \begin{theorem}\label{X}, \begin{theorem}[Name]\label{X}, etc.
    for env_name in THEOREM_ENVS:
        # Pattern: \begin{env}[optional name]\label{optional label} ... \end{env}
        pattern = re.compile(
            r'\\begin\{' + env_name + r'\}'
            r'(?:\[([^\]]*)\])?'       # optional [Name]
            r'(?:\\label\{([^}]*)\})?'  # optional \label{X}
            r'[ \t]*\n?'                # consume spaces and up to one newline
            r'(.*?)'                    # inner content
            r'\\end\{' + env_name + r'\}',
            re.DOTALL
        )
        def make_replacer(env):
            def replacer(m):
                opt_name = m.group(1)  # [Name] or None
                label = m.group(2)     # \label{X} or None
                inner = m.group(3)     # inner content
                
                prefix = THEOREM_ENVS[env]
                if label:
                    label_id = label.replace(':', '-').replace(' ', '-').replace('_', '-').lower()
                    div_id = f"#{prefix}-{label_id}"
                    label_map[label] = f"{prefix}-{label_id}"
                else:
                    env_counter[env] = env_counter.get(env, 0) + 1
                    div_id = f"#{prefix}-{env_counter[env]}"
                
                # Map orphan \label{X} (not inside \begin{aligneq}...\end{aligneq})
                # to this env's div ID. Labels inside math envs are handled by Pass 3.
                qid = div_id.lstrip('#')
                # Find labels NOT inside a math env by stripping math envs first
                stripped = re.sub(r'\\begin\{aligneq\*?\}.*?\\end\{aligneq\*?\}', '', inner, flags=re.DOTALL)
                # For labels on \item lines, extract the item name (first word after \item)
                for il_m in re.finditer(r'\\item\s+(\w+).*?\\label\{([^}]*)\}', stripped):

                    item_name = il_m.group(1)
                    il = il_m.group(2)
                    label_map[il] = qid
                    item_label_map[il] = (qid, item_name)
                # Also map any remaining orphan labels (not on \item lines)
                for il in re.findall(r'\\label\{([^}]*)\}', stripped):
                    if il not in label_map:
                        label_map[il] = qid
                # Only strip orphan labels (outside math envs)
                inner = re.sub(r'(?<!\\end\{aligneq\})\\label\{([^}]*)\}', lambda lm: '' if lm.group(1) in label_map and label_map[lm.group(1)] == qid else lm.group(0), inner)
                
                attrs = [div_id]
                if opt_name:
                    attrs.append(f'name="{opt_name}"')
                
                # Dedent inner content to prevent 4-space markdown indents parsing as code blocks
                dedented = textwrap.dedent(inner.strip('\n'))
                # Force-lstrip each line to avoid 4-space code block parsing
                lines_d = dedented.split('\n')
                lines_d = [l.lstrip() if l.strip() else l for l in lines_d]
                dedented = '\n'.join(lines_d)
                # Pandoc requires blank lines after the opening fence and before the closing fence
                return f'\n::: {{{" ".join(attrs)}}}\n\n{dedented}\n\n:::\n'
            return replacer

        text = pattern.sub(make_replacer(env_name), text)

    # --- Pass 2b: Proof environment ---
    def dedent_proof(m):
        inner = m.group(1)
        dedented = textwrap.dedent(inner.strip('\n'))
        return f'\n::: {{.proof}}\n\n{dedented}\n\n:::\n'

    text = re.sub(r'\\begin\{proof\}[ \t]*\n?(.*?)\\end\{proof\}', dedent_proof, text, flags=re.DOTALL)

    # --- Pass 2c: Hint environment ---
    def dedent_hint(m):
        inner = m.group(1)
        dedented = textwrap.dedent(inner.strip('\n'))
        return f'\n::: {{.callout-tip collapse="true" title="Hint"}}\n\n{dedented}\n\n:::\n'

    text = re.sub(r'\\begin\{hint\}[ \t]*\n?(.*?)\\end\{hint\}', dedent_hint, text, flags=re.DOTALL)

    # --- Pass 3: Display math environments ---
    # aligneq = equation + aligned, aligneq* = equation* + aligned
    # We convert to $$\begin{aligned}...\end{aligned}$$ so MathJax renders natively.
    # For non-aligneq envs (align, equation), we just use $$ fences.

    def replace_display_math(text, env_name, starred=False, wrap_aligned=False):
        begin_pat = r'\\begin\{' + env_name + r'\}'
        if not starred:
            pattern = re.compile(
                begin_pat + r'\s*(?:\\label\{([^}]*)\})?',
                re.DOTALL
            )
        else:
            pattern = re.compile(begin_pat)

        end_pat = r'\\end\{' + env_name + r'\}'

        result = []
        last_end = 0

        for m in pattern.finditer(text):
            result.append(text[last_end:m.start()])

            label = None
            if not starred and m.group(1):
                label = m.group(1)

            # Find matching \end
            end_m = re.search(end_pat, text[m.end():])
            if end_m:
                inner = text[m.end():m.end() + end_m.start()]
                end_pos = m.end() + end_m.end()
            else:
                inner = text[m.end():]
                end_pos = len(text)

            # Check for \label inside the block if we haven't found one yet
            if not label and not starred:
                inner_label = re.search(r'\\label\{([^}]*)\}', inner)
                if inner_label:
                    label = inner_label.group(1)
                    inner = inner[:inner_label.start()] + inner[inner_label.end():]

            # Build the output block
            if wrap_aligned:
                result.append('\n$$\n\\begin{aligned}\n')
                result.append(inner.strip())
                result.append('\n\\end{aligned}')
            else:
                result.append('\n$$\n')
                result.append(inner.strip())

            if label:
                label_id = label.replace(':', '-').replace(' ', '-').replace('_', '-').lower()
                label_map[label] = f"eq-{label_id}"
                result.append(f'\n$$ {{#eq-{label_id}}}\n')
            else:
                result.append('\n$$\n')

            last_end = end_pos

        result.append(text[last_end:])
        return ''.join(result)

    # aligneq → wrap in \begin{aligned}...\end{aligned}
    text = replace_display_math(text, 'aligneq', wrap_aligned=True)
    text = replace_display_math(text, 'aligneq\\*', starred=True, wrap_aligned=True)
    # align → already an alignment env, just fence with $$
    text = replace_display_math(text, 'align', starred=False)
    text = replace_display_math(text, 'align\\*', starred=True)
    # equation → just fence with $$
    text = replace_display_math(text, 'equation', starred=False)
    text = replace_display_math(text, 'equation\\*', starred=True)

    # --- Pass 4: Enumerate / Itemize ---
    def convert_enumerate(m):
        inner = m.group(1)
        items = re.split(r'\\item\s*', inner)
        items = [it.strip() for it in items if it.strip()]
        lines = []
        for idx, item in enumerate(items, 1):
            # Strip trailing \label{...} from items
            item = re.sub(r'\\label\{[^}]*\}', '', item).strip()
            lines.append(f'{idx}. {item}')
        return '\n'.join(lines)

    text = re.sub(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}',
                  convert_enumerate, text, flags=re.DOTALL)

    def convert_itemize(m):
        inner = m.group(1)
        items = re.split(r'\\item\s*', inner)
        items = [it.strip() for it in items if it.strip()]
        lines = []
        for item in items:
            lines.append(f'- {item}')
        return '\n'.join(lines)

    text = re.sub(r'\\begin\{itemize\}(.*?)\\end\{itemize\}',
                  convert_itemize, text, flags=re.DOTALL)

    # --- Pass 5: Citations ---
    # \cite[options]{key1,key2} → [@key1; @key2]
    def convert_cite(m):
        opt = m.group(1)  # optional [...]
        keys = m.group(2)
        key_list = [k.strip() for k in keys.split(',')]
        formatted = '; '.join(f'@{k}' for k in key_list)
        if opt:
            return f'[{formatted}, {opt}]'
        return f'[{formatted}]'

    text = re.sub(r'\\cite\[([^\]]*)\]\{([^}]*)\}', convert_cite, text)

    def convert_cite_no_opt(m):
        keys = m.group(1)
        key_list = [k.strip() for k in keys.split(',')]
        formatted = '; '.join(f'@{k}' for k in key_list)
        return f'[{formatted}]'

    text = re.sub(r'\\cite\{([^}]*)\}', convert_cite_no_opt, text)

    # --- Pass 6: Cross-references ---
    # \eqref{X} → @eq-X
    def convert_eqref(m):
        label = m.group(1).replace(':', '-').replace(' ', '-').replace('_', '-').lower()
        return f'@eq-{label}'

    text = re.sub(r'\\eqref\{([^}]*)\}', convert_eqref, text)

    # \Cref{X} and \cref{X} → @prefix-X  (best effort)
    def convert_cref(m):
        raw_label = m.group(1)
        label = raw_label.replace(':', '-').replace(' ', '-').replace('_', '-').lower()
        # First check if this is an item-level label (emit descriptive text)
        if raw_label in item_label_map:
            parent_qid, item_name = item_label_map[raw_label]
            return f'@{parent_qid} ({item_name})'
        # Then check if this label was mapped during theorem/equation conversion
        if raw_label in label_map:
            return f'@{label_map[raw_label]}'
        # Try to guess the prefix from the label convention
        if label.startswith('def'):
            return f'@def-{label}'
        elif label.startswith('thm'):
            return f'@thm-{label}'
        elif label.startswith('lem'):
            return f'@lem-{label}'
        elif label.startswith('prp') or label.startswith('prop'):
            return f'@prp-{label}'
        elif label.startswith('cor'):
            return f'@cor-{label}'
        elif label.startswith('eq'):
            return f'@eq-{label}'
        else:
            # Fallback: just reference by label
            return f'@{label}'

    text = re.sub(r'\\[Cc]ref\{([^}]*)\}', convert_cref, text)

    # Also fix plain @rawlabel references emitted by earlier passes
    # If a label in label_map appears as @label (without prefix), replace it.
    def fix_raw_at_ref(m):
        raw = m.group(1)
        if raw in label_map:
            return f'@{label_map[raw]}'
        return m.group(0)  # leave as-is (likely a real Quarto ref or cite key)

    text = re.sub(r'@([A-Za-z][\w:-]*)', fix_raw_at_ref, text)

    # --- Pass 7: Inline formatting ---
    # \href{url}{text} → [text](url)
    text = re.sub(r'\\href\{([^}]*)\}\{([^}]*)\}', r'[\2](\1)', text)

    # \emph{X} → *X*  (only outside math mode — simple heuristic)
    text = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', text)

    # \textbf{X} → **X**
    text = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', text)

    # \textit{X} → *X*
    text = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', text)

    # --- Pass 8: Clean up ---
    # Remove stray \label{} that weren't consumed
    text = re.sub(r'\\label\{[^}]*\}', '', text)

    # Strip whitespace inside inline $...$ delimiters
    # Pandoc requires no space adjacent to $ for inline math.
    # Character-level scan to properly skip $$ display math boundaries.
    def _fix_inline_math_spaces(text):
        result = []
        i = 0
        while i < len(text):
            if text[i] == '$':
                # Check for $$ (display math) — skip it entirely
                if i + 1 < len(text) and text[i + 1] == '$':
                    # Find closing $$
                    end = text.find('$$', i + 2)
                    if end == -1:
                        result.append(text[i:])
                        break
                    result.append(text[i:end + 2])
                    i = end + 2
                    continue
                # Single $ — inline math. Find matching closing $
                j = i + 1
                while j < len(text):
                    if text[j] == '$':
                        break
                    if text[j] == '\n':
                        # Inline math can't span newlines in Pandoc
                        break
                    j += 1
                if j < len(text) and text[j] == '$':
                    inner = text[i + 1:j]
                    result.append('$' + inner.strip() + '$')
                    i = j + 1
                else:
                    # No matching $ on same line — not inline math
                    result.append(text[i])
                    i += 1
            else:
                result.append(text[i])
                i += 1
        return ''.join(result)
    text = _fix_inline_math_spaces(text)

    # Remove multiple blank lines (keep max 2)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


# ---------------------------------------------------------------------------
# 5. ASSEMBLE index.qmd
# ---------------------------------------------------------------------------

def build_qmd(meta: dict, body: str, mathjax_macros: str) -> str:
    """Assemble the final index.qmd content."""
    lines = ['---']

    # Title
    title = meta.get('title', 'Untitled')
    lines.append(f'title: "{title}"')

    # Author
    author = meta.get('author', '')
    if author:
        lines.append(f'author: "{author}"')

    # Date
    lines.append(f'date: "{meta.get("date", date.today().isoformat())}"')

    # Tags (was 'categories')
    tags = meta.get('tags', [])
    if tags:
        tag_str = ', '.join(tags)
        lines.append(f'categories: [{tag_str}]')

    # Subtitle (was 'description')
    subtitle = meta.get('subtitle', '')
    if subtitle:
        lines.append(f'description: "{subtitle}"')

    # Image (auto-detected cover)
    img = meta.get('image', '')
    if img:
        lines.append(f'image: "{img}"')

    # Bibliography
    bib = meta.get('bibliography', '')
    if bib:
        lines.append(f'bibliography: {bib}')

    # Format block with MathJax
    lines.append('format:')
    lines.append('  html:')
    lines.append('    css: custom_theorems.css')
    lines.append('    toc: true')
    lines.append('    number-sections: true')
    lines.append('    html-math-method: mathjax')

    if mathjax_macros:
        lines.append('    include-in-header:')
        lines.append('      text: |')
        lines.append('        <script>')
        lines.append('        window.MathJax = {')
        lines.append('          tex: {')
        lines.append('            tags: "ams",')
        lines.append('            macros: {')
        lines.append(mathjax_macros)
        lines.append('            }')
        lines.append('          }')
        lines.append('        };')
        lines.append('        </script>')

    lines.append('---')
    lines.append('')
    lines.append(body)
    lines.append('')
    lines.append('## References')
    lines.append('')
    lines.append('::: {#refs}')
    lines.append(':::')
    lines.append('')

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# 6. MAIN
# ---------------------------------------------------------------------------

def convert_folder(folder: Path, tex_name='main.tex', preamble_name='preamble.sty',
                   output_name='index.qmd', blog_dir=None):
    """Convert a single LaTeX folder to a Quarto post."""
    tex_path = folder / tex_name
    if not tex_path.exists():
        print(f"  SKIP: {tex_path} not found.")
        return False

    # Read LaTeX source
    with open(tex_path, "r", encoding="utf-8") as f:
        tex_content = f.read()

    # Parse metadata
    meta = parse_tex_metadata(tex_content)
    print(f"  Title:  {meta.get('title', '???')}")
    print(f"  Author: {meta.get('author', '???')}")
    print(f"  Date:   {meta.get('date', '???')}")
    print(f"  Subtitle: {meta.get('subtitle', '(none)')}")

    # Infer tags from parent folder
    if 'tags' not in meta:
        meta['tags'] = infer_tags(folder)
    print(f"  Tags:     {meta.get('tags', '(none)')}")

    # Auto-detect cover image
    cover = detect_cover_image(folder)
    if cover:
        meta['image'] = cover
        print(f"  Image:    {cover}")
    else:
        print(f"  Image:    (none)")

    # Parse preamble for MathJax macros
    sty_path = folder / preamble_name
    macros = parse_preamble_macros(sty_path)
    print(f"  Extracted {len(macros)} macros from {preamble_name}")
    mathjax_macros = format_mathjax_macros(macros)

    # Extract and convert body
    body = extract_body(tex_content)
    converted_body = convert_body(body)

    # Assemble output
    qmd = build_qmd(meta, converted_body, mathjax_macros)

    # Determine output location
    if blog_dir:
        blog_dir = Path(blog_dir).resolve()
        posts_dir = blog_dir / 'posts'
        dest = posts_dir / folder.name
        dest.mkdir(parents=True, exist_ok=True)
        out_path = dest / output_name
    else:
        out_path = folder / output_name

    # Write index.qmd
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(qmd)
    print(f"  Output written to: {out_path}")

    # Auto-copy to blog posts/ directory if --blog-dir is given
    if blog_dir:
        EXCLUDE_SUFFIXES = {'.tex', '.sty', '.aux', '.log', '.out', '.toc',
                            '.synctex', '.gz', '.blg', '.bbl', '.fls', '.fdb_latexmk'}
        EXCLUDE_NAMES = {'info.txt'}

        dest.mkdir(parents=True, exist_ok=True)
        for src_item in folder.rglob('*'):
            if src_item.is_dir():
                continue
            rel = src_item.relative_to(folder)
            if src_item.suffix.lower() in EXCLUDE_SUFFIXES:
                continue
            if src_item.name in EXCLUDE_NAMES:
                continue
            dst_item = dest / rel
            dst_item.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_item, dst_item)

        # Ensure custom_theorems.css exists
        css_dest = dest / 'custom_theorems.css'
        if not css_dest.exists():
            css_content = '''/* LaTeX-style theorem environments */
.theorem, .lemma, .corollary, .proposition, .conjecture, .definition, .example, .remark {
  border: none !important;
  background-color: transparent !important;
  padding: 0 !important;
  margin-top: 1em;
  margin-bottom: 1em;
}
.theorem-title, .lemma-title, .corollary-title, .proposition-title,
.conjecture-title, .definition-title, .example-title, .remark-title {
  display: inline !important;
  font-weight: bold;
  color: inherit !important;
  margin-right: 0.5em;
}
.theorem-title::after, .lemma-title::after, .corollary-title::after,
.proposition-title::after, .definition-title::after { content: "."; }
.theorem-body, .lemma-body, .corollary-body, .proposition-body { font-style: italic; }
.definition-body, .example-body, .remark-body { font-style: normal; }
'''
            with open(css_dest, 'w') as f:
                f.write(css_content)

        print(f"  Post deployed to: {dest}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Convert a LaTeX folder into a Quarto blog post. '
                    'If run with no arguments, converts the current directory.'
    )
    parser.add_argument('folder', type=str, nargs='?', default='.',
                        help='Path to the LaTeX folder (default: current directory)')
    parser.add_argument('--all', action='store_true',
                        help='Batch mode: find all folders containing main.tex '
                             'under the given path (excluding Future/) and convert them all.')
    parser.add_argument('--tex', type=str, default='main.tex',
                        help='Name of the .tex file (default: main.tex)')
    parser.add_argument('--preamble', type=str, default='preamble.sty',
                        help='Name of the .sty file (default: preamble.sty)')
    parser.add_argument('--output', type=str, default='index.qmd',
                        help='Output filename (default: index.qmd)')
    parser.add_argument('--blog-dir', type=str, default=None,
                        help='Path to the Quarto blog repo. '
                             'If given, copies the folder into blog/posts/<folder-name>/')

    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        print(f"ERROR: {folder} is not a directory.")
        sys.exit(1)

    if args.all:
        # Batch mode: find all folders with main.tex, excluding Future/
        targets = []
        for tex_file in folder.rglob(args.tex):
            post_folder = tex_file.parent
            # Skip Future/ folders
            rel = post_folder.relative_to(folder)
            if any(part.lower() == 'future' for part in rel.parts):
                continue
            targets.append(post_folder)

        if not targets:
            print(f"No folders with {args.tex} found under {folder}")
            sys.exit(1)

        print(f"Found {len(targets)} post(s) to convert:\n")
        ok, fail = 0, 0
        for t in sorted(targets):
            print(f"{'='*60}")
            print(f"  Converting: {t.relative_to(folder)}")
            print(f"{'='*60}")
            if convert_folder(t, args.tex, args.preamble, args.output, args.blog_dir):
                ok += 1
            else:
                fail += 1
            print()

        print(f"\nDone. {ok} converted, {fail} skipped.")
    else:
        # Single folder mode
        convert_folder(folder, args.tex, args.preamble, args.output, args.blog_dir)


if __name__ == '__main__':
    main()

