#!/usr/bin/env python3
"""
latex2qmd.py — Convert a LaTeX project folder into a Quarto blog post.

Usage:
    python latex2qmd.py /path/to/latex/folder [--blog-dir /path/to/blog]

Input folder must contain:
    - main.tex (or specified .tex file)
    - preamble.sty (or specified .sty file)
    - info.txt (categories, description)
    - biblio.bib (optional)

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
# 1. PARSE info.txt
# ---------------------------------------------------------------------------

def parse_info(folder: Path) -> dict:
    """Read info.txt and return a dict of key-value pairs."""
    info_path = folder / "info.txt"
    info = {}
    if not info_path.exists():
        print(f"WARNING: {info_path} not found. categories/description will be empty.")
        return info
    with open(info_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                info[key.strip().lower()] = val.strip()
    return info


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
    """Extract title, author, date from LaTeX source."""
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

    # Inject physics-package macros that come from LaTeX \usepackage{physics}
    # and can't be extracted from preamble.sty via \newcommand parsing.
    physics_fallbacks = {
        # \bm{x} → \boldsymbol{x}  (bm package, no MathJax extension needed)
        'bm': (r'\boldsymbol{#1}', 1),
        # \qty is handled at the Python level via _expand_qty(), not as a macro
    }
    for name, val in physics_fallbacks.items():
        if name not in macros:
            macros[name] = val

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

    # --- Pass 0: Strip TODO notes, end-of-theorem symbols, and expand \qty ---
    text = re.sub(r'\\liam\{[^}]*\}', '', text)
    text = re.sub(r'\\exampleSymbol', '', text)
    text = re.sub(r'\\exerciseSymbol', '', text)
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
                else:
                    env_counter[env] = env_counter.get(env, 0) + 1
                    div_id = f"#{prefix}-{env_counter[env]}"
                
                attrs = [div_id]
                if opt_name:
                    attrs.append(f'name="{opt_name}"')
                
                # Dedent inner content to prevent 4-space markdown indents parsing as code blocks
                dedented = textwrap.dedent(inner.strip('\n'))
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
        label = m.group(1).replace(':', '-').replace(' ', '-').replace('_', '-').lower()
        # Try to guess the prefix from the label convention
        # Common patterns: "def:X", "thm:X", "GM def", "covariance-space-lemma"
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

    # Remove multiple blank lines (keep max 2)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


# ---------------------------------------------------------------------------
# 5. ASSEMBLE index.qmd
# ---------------------------------------------------------------------------

def build_qmd(meta: dict, info: dict, body: str, mathjax_macros: str) -> str:
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

    # Categories
    cats = info.get('categories', '')
    if cats:
        cat_list = [c.strip() for c in cats.split(',')]
        cat_str = ', '.join(cat_list)
        lines.append(f'categories: [{cat_str}]')

    # Description
    desc = info.get('description', '')
    if desc:
        lines.append(f'description: "{desc}"')

    # Image
    img = info.get('image', '')
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
        # Ensure physics-package macros are always available as fallbacks
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

def main():
    parser = argparse.ArgumentParser(
        description='Convert a LaTeX folder into a Quarto blog post.'
    )
    parser.add_argument('folder', type=str, help='Path to the LaTeX folder')
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

    tex_path = folder / args.tex
    if not tex_path.exists():
        print(f"ERROR: {tex_path} not found.")
        sys.exit(1)

    # Read LaTeX source
    with open(tex_path, "r", encoding="utf-8") as f:
        tex_content = f.read()

    # Parse metadata
    meta = parse_tex_metadata(tex_content)
    print(f"  Title:  {meta.get('title', '???')}")
    print(f"  Author: {meta.get('author', '???')}")
    print(f"  Date:   {meta.get('date', '???')}")

    # Parse info.txt
    info = parse_info(folder)
    print(f"  Categories:  {info.get('categories', '(none)')}")
    print(f"  Description: {info.get('description', '(none)')}")

    # Parse preamble for MathJax macros
    sty_path = folder / args.preamble
    macros = parse_preamble_macros(sty_path)
    print(f"  Extracted {len(macros)} macros from {args.preamble}")
    mathjax_macros = format_mathjax_macros(macros)

    # Extract and convert body
    body = extract_body(tex_content)
    converted_body = convert_body(body)

    # Assemble output
    qmd = build_qmd(meta, info, converted_body, mathjax_macros)

    # Write index.qmd into the source folder
    out_path = folder / args.output
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(qmd)
    print(f"\n  Output written to: {out_path}")

    # Auto-copy to blog posts/ directory if --blog-dir is given
    if args.blog_dir:
        blog_dir = Path(args.blog_dir).resolve()
        posts_dir = blog_dir / 'posts'
        dest = posts_dir / folder.name

        if dest.exists():
            print(f"  Updating existing post at: {dest}")
            # Copy only the key files, preserving the destination
            for item in folder.iterdir():
                src_item = folder / item.name
                dst_item = dest / item.name
                if src_item.is_file():
                    shutil.copy2(src_item, dst_item)
        else:
            print(f"  Copying folder to: {dest}")
            shutil.copytree(folder, dest)

        # Also copy custom_theorems.css if not already present
        css_src = blog_dir / 'Intro_Gaussian_Measures' / 'custom_theorems.css'
        css_dest = dest / 'custom_theorems.css'
        if not css_dest.exists():
            # Create a default one
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
        print(f"  Run 'quarto preview' in {blog_dir} to see it.")
    else:
        print(f"  To deploy: copy this folder into your blog's posts/ directory.")
        print(f"  Or re-run with: --blog-dir /path/to/blog")


if __name__ == '__main__':
    main()
