#!/usr/bin/env python3
r"""
latex2qmd.py — Convert a folder containing LaTeX (.tex) and preamble (.sty) into a Quarto blog post.

Usage:
    python latex2qmd.py /path/to/latex/folder [--blog-dir /path/to/blog]

Input folder must contain:
    - main.tex (or specified .tex file)
    - preamble.sty (or specified .sty file)
    - biblio.bib (optional)
    - cover.jpg/png (optional, used as post image)

Metadata is extracted from:
    - \title{}, \author{}, \date{} — standard LaTeX commands
    - \postsubtitle{} — becomes the post subtitle
    - \posttags{} — becomes the post tags
    - Parent folder name — becomes the default tag
    - cover.* — auto-detected as post image

Output:
    - index.qmd written into the folder
    - If --blog-dir is given, copies entire folder into blog/posts/
"""

import argparse
import json
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


def _normalize_date(date_str: str) -> str:
    """Normalize a date string to ISO 8601 (YYYY-MM-DD).

    Handles: YYYY-MM-DD (passthrough), DD-MM-YYYY, MM/DD/YYYY, M/DD/YYYY,
    MM-DD-YYYY, DD/MM/YYYY. Disambiguates by checking if either component > 12.
    """
    date_str = date_str.strip()

    # Already ISO?
    iso_m = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})$', date_str)
    if iso_m:
        return date_str

    # Try patterns with / or - separator
    m = re.match(r'^(\d{1,2})[/\-](\d{1,2})[/\-](\d{4})$', date_str)
    if m:
        a, b, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
        # Disambiguate: if a > 12, it must be day (DD-MM-YYYY)
        if a > 12:
            day, month = a, b
        elif b > 12:
            month, day = a, b
        else:
            # Ambiguous: assume MM/DD/YYYY for / separator, DD-MM-YYYY for - separator
            sep = date_str[len(m.group(1))]
            if sep == '/':
                month, day = a, b
            else:
                day, month = a, b
        return f"{year}-{month:02d}-{day:02d}"

    # Fallback: return as-is
    return date_str


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
            meta['date'] = _normalize_date(date_str)
    else:
        meta['date'] = date.today().isoformat()

    # Extract \postsubtitle{...} → subtitle
    desc = _extract_braced(tex, 'postsubtitle')
    if desc:
        meta['subtitle'] = desc

    # Extract \posttags{...} → tags override (comma-separated)
    posttags = _extract_braced(tex, 'posttags')
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


def extract_balanced(text: str, start_pos: int) -> tuple[str, int]:
    """Helper to extract balanced {...} starting at start_pos.
    Returns (content_inside, end_pos_after_closing_brace)."""
    if start_pos >= len(text) or text[start_pos] != '{':
        return "", start_pos
    
    depth = 0
    i = start_pos
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start_pos+1:i], i + 1
        i += 1
    return text[start_pos+1:], i


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

    # Match \newcommand{\name}[n]{...}, \newcommand{\name}{...}, \newcommand\name[n]{...}, \newcommand\name{...}
    # Also \renewcommand
    # We need to handle nested braces in the replacement body
    pattern = re.compile(
        r'\\(?:new|renew)command(?:\{|\s*)\\([a-zA-Z]+)(?:\}|\s*)'
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
    
    # Fallbacks for indicator functions from bbm/dsfont packages
    if 'mathbbm' not in macros:
        macros['mathbbm'] = (r'\mathbb{#1}', 1)
    if 'mathds' not in macros:
        macros['mathds'] = (r'\mathbb{#1}', 1)
    if 'supp' not in macros:
        macros['supp'] = (r'\operatorname{supp}', 0)

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
# 3b. GLOBAL LABEL REGISTRY (two-pass cross-post references)
# ---------------------------------------------------------------------------

def find_main_tex(folder: Path, preferred_name: str = 'main.tex') -> Path | None:
    """Find the likely main LaTeX file in a folder."""
    # 1. Try preferred_name
    if (folder / preferred_name).exists():
        return folder / preferred_name
    # 2. Try [foldername].tex
    if (folder / (folder.name + '.tex')).exists():
        return folder / (folder.name + '.tex')
    
    # 3. Look for files with \title
    tex_files = list(folder.glob('*.tex'))
    valid_files = [f for f in tex_files if f.name.lower() not in ['preamble.tex', 'style.tex']]
    
    candidates_with_title = []
    candidates_with_doc = []
    
    for f in valid_files:
        try:
            content = f.read_text(encoding='utf-8')
            if r'\title{' in content:
                candidates_with_title.append(f)
            elif r'\begin{document}' in content or r'\documentclass' in content:
                candidates_with_doc.append(f)
        except Exception:
            pass
            
    # Priority: 1. Has \title, 2. Has \begin{document}, 3. Any valid tex file
    if candidates_with_title:
        return candidates_with_title[0]
    if candidates_with_doc:
        return candidates_with_doc[0]
    if valid_files:
        return valid_files[0]
        
    return None


def build_label_registry(posts_root: Path, tex_name: str = 'main.tex') -> dict:
    r"""
    Phase 1: Scan all posts and extract every \label{X}, mapping each to
    its Quarto ID, organized by folder.

    Returns a dict: folder_path -> {label: qid}
    where folder_path is relative to posts_root (e.g. "Stochastic Calculus/Martingales").
    """
    registry = {}  # folder -> {label -> qid}

    def sanitize(l):
        return l.replace(':', '-').replace(' ', '-').replace('_', '-').lower()

    # Find all direct subfolders of posts_root as potential "post collections"
    # Actually, we want to find leaf folders that contain a .tex file.
    for root, dirs, files in os.walk(posts_root):
        # Skip hidden dirs or __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        folder = Path(root)
        tex_file = find_main_tex(folder, preferred_name=tex_name)
        if not tex_file:
            continue
            
        rel = folder.relative_to(posts_root)
        # Skip Future/ folders
        if any(part.lower() == 'future' for part in rel.parts):
            continue

        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract body between \begin{document} and \end{document}
        begin_m = re.search(r'\\begin\{document\}', content)
        end_m = re.search(r'\\end\{document\}', content)
        if not begin_m or not end_m:
            continue
        body = content[begin_m.end():end_m.start()]

        folder_str = str(rel).replace('\\', '/')
        registry[folder_str] = {}
        env_counter = {}  # for auto-numbering

        # Scan theorem-like environments for labels
        for env_name, prefix in THEOREM_ENVS.items():
            pattern = re.compile(
                r'\\begin\{' + env_name + r'\}'
                r'(?:\[([^\]]*)\])?'       # optional [Name]
                r'(?:\\label\{([^}]*)\})?'  # optional \label{X}
                r'[ \t]*\n?'
                r'(.*?)'
                r'\\end\{' + env_name + r'}',
                re.DOTALL
            )
            for m in pattern.finditer(body):
                label = m.group(2)  # from \begin{env}\label{X}
                inner = m.group(3)

                if label:
                    label_id = sanitize(label)
                    qid = f"{prefix}-{label_id}"
                    registry[folder_str][label] = qid
                    registry[folder_str][qid] = qid # Map QID to itself for direct access
                else:
                    env_counter[env_name] = env_counter.get(env_name, 0) + 1
                    qid = f"{prefix}-{env_counter[env_name]}"
                    registry[folder_str][qid] = qid # Auto-numbered ID maps to itself

                # Also scan labels inside the inner content (orphan labels)
                for inner_label in re.findall(r'\\label\{([^}]*)\}', inner):
                    if inner_label not in registry[folder_str]:
                        registry[folder_str][inner_label] = qid

        # Scan math environments for labels (equation, aligneq, align)
        for env_name in ['equation', 'aligneq', 'align']:
            pattern = re.compile(
                r'\\begin\{' + env_name + r'\}'
                r'\s*(?:\\label\{([^}]*)\})?',
                re.DOTALL
            )
            end_pat = r'\\end\{' + env_name + r'}'
            for m in pattern.finditer(body):
                label = m.group(1)
                # Also check for labels inside the block
                end_m2 = re.search(end_pat, body[m.end():])
                if end_m2:
                    inner = body[m.end():m.end() + end_m2.start()]
                else:
                    inner = ''

                if not label:
                    inner_label_m = re.search(r'\\label\{([^}]*)\}', inner)
                    if inner_label_m:
                        label = inner_label_m.group(1)

                if label:
                    label_id = sanitize(label)
                    qid = f"eq-{label_id}"
                    registry[folder_str][label] = qid
                    registry[folder_str][qid] = qid

        # Scan sections for labels (including starred versions)
        sec_pattern = re.compile(r'\\(?:section|subsection|subsubsection)(\*?)\{([^}]*)\}(?:\s*\\label\{([^}]*)\})?')
        for m in sec_pattern.finditer(body):
            label = m.group(3)
            if label:
                label_id = sanitize(label)
                if not label_id.startswith('sec-'):
                    label_id = f"sec-{label_id}"
                registry[folder_str][label] = label_id
                registry[folder_str][label_id] = label_id

    return registry


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
    'observation': 'rem',
    'note': 'rem',
    'assumption': 'thm',
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


def convert_body(body: str, label_registry: dict | None = None,
                 current_folder: str | None = None,
                 pdf_filename: str | None = None) -> str:
    r"""Apply all mechanical transformations to the LaTeX body.
    """
    # --- Pass 0a: Structural Normalization ---
    # Strip unescaped LaTeX comments %...
    body = re.sub(r'(?<!\\)%.*', '', body)
    
    # Replace escaped percentages \% with plain %
    body = body.replace(r'\%', '%')

    # Split, lstrip, and rejoin to prevent 4-space/tab indented code blocks in Markdown.
    # We do this first because LaTeX source indentation is purely cosmetic,
    # but Markdown indentation is semantic.
    lines = [l.lstrip() for l in body.split('\n')]
    text = '\n'.join(lines)

    # Insert PDF Link data at the top if available
    if pdf_filename:
        text = f'<div id="quarto-post-pdf-url" data-url="{pdf_filename}" style="display:none;"></div>\n\n' + text

    # Strip legacy "outdated PDF" disclaimers and spacing commands
    text = re.sub(r'(?i)link to a (?:possibly )?outdated PDF content.*?\.', '', text)
    text = re.sub(r'(?i)a possibly outdated version of the PDF.*?\.', '', text)
    
    # Clean up LaTeX specific spacing markers
    text = re.sub(r'\\(?:bigbreak|medbreak|smallbreak|noindent|hfill)', '', text)
    text = re.sub(r'\\hspace\{[^}]*\}', '', text)
    text = re.sub(r'\\vspace\{[^}]*\}', '', text)

    # Map of LaTeX labels to generated Quarto IDs, populated during conversion
    label_map = {}  # e.g. {'density': 'eq-density', 'independence': 'prp-1', ...}
    # For item-level labels: label -> (parent_qid, item_name)
    item_label_map = {}  # e.g. {'inversion': ('prp-1', 'Inversion')}

    def sanitize_label(l):
        # Replace all non-alphanumeric (except hyphens and colons) with hyphens
        s = re.sub(r'[^a-zA-Z0-9:-]', '-', l)
        # Replace multiple hyphens with one
        s = re.sub(r'-+', '-', s)
        return s.strip('-').lower()

    # --- Pass 0: Strip TODO notes, end-of-theorem symbols, expand \qty,
    #             and strip blog metadata commands from body ---
    text = re.sub(r'\\liam\{[^}]*\}', '', text)
    text = re.sub(r'\\exampleSymbol', '', text)
    text = re.sub(r'\\exerciseSymbol', '', text)
    # Strip blog metadata commands that should only appear in front matter
    text = re.sub(r'\\postsubtitle\{[^}]*\}', '', text)
    text = re.sub(r'\\posttags\{[^}]*\}', '', text)
    text = _expand_qty(text)

    # --- Pass 1: Sections ---
    def replace_sections(m):
        level = m.group(1)
        is_starred = m.group(2) == '*'
        title = m.group(3).strip()
        label = m.group(4)
        hashes = '##' if level == 'section' else '###' if level == 'subsection' else '####'
        if label:
            label_id = sanitize_label(label)
            if not label_id.startswith('sec-'):
                label_id = f"sec-{label_id}"
            label_map[label] = label_id
            return f'\n\n{hashes} {title} {{#{label_id}}}\n\n'
        if is_starred:
            return f'\n\n{hashes} {title} {{.unnumbered}}\n\n'
        return f'\n\n{hashes} {title}\n\n'

    text = re.sub(r'\\(section|subsection|subsubsection)(\*?)\{([^}]*)\}(?:\s*\\label\{([^}]*)\})?', replace_sections, text)

    # --- Pass 1b: Convert \[ ... \] to $$ ... $$ ---
    # We do this before theorem processing so internal math is standardized
    text = re.sub(r'\\\[(.*?)\\\]', r'\n\n$$\1$$\n\n', text, flags=re.DOTALL)

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
        # Handles nested braces in [Name] by using a non-greedy balance check
        pattern = re.compile(
            r'\\begin\{' + env_name + r'\}'
            r'(?:\[((?:\{[^{}]*\}|[^\]])*)\])?'  # optional [Name], supporting one level of {braces}
            r'(?:\\label\{([^}]*)\})?'            # optional \label{X}
            r'[ \t]*'                             # consume spaces
            r'(?:%.*?\n)?'                        # consume optional comment
            r'\s*'                                # consume remaining whitespace/newlines
            r'(.*?)'                              # inner content
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
                    label_id = sanitize_label(label)
                    div_id = f"#{prefix}-{label_id}"
                    label_map[label] = f"{prefix}-{label_id}"
                    label_map[label_id] = f"{prefix}-{label_id}" # Also map sanitized version
                else:
                    env_counter[env] = env_counter.get(env, 0) + 1
                    div_id = f"#{prefix}-{env_counter[env]}"
                
                # Map orphan \label{X} (not inside \begin{aligneq}...\end{aligneq})
                # to this env's div ID. Labels inside math envs are handled by Pass 3.
                qid = div_id.lstrip('#')
                # Find labels NOT inside a math env by stripping math envs first
                math_envs_pat = re.compile(r'\\begin\{(aligneq\*?|align\*?|equation\*?)\}.*?\\end\{\1\}', re.DOTALL)
                stripped = math_envs_pat.sub('', inner)
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
                # Only strip orphan labels (captured by Pass 2) if they match this div's qid
                # (Avoid stripping labels meant for math blocks or other environments)
                text_label_pat = re.compile(r'\\label\{([^}]*)\}')
                def strip_if_mapped_to_us(lm):
                    l = lm.group(1)
                    if l in label_map and label_map[l] == qid:
                        return ''
                    return lm.group(0)
                
                inner = text_label_pat.sub(strip_if_mapped_to_us, inner)
                
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
                # Pandoc requires blank lines after the opening fence and before the closing fence
                # Use 3 colons as standard, but ensure blank lines for block separation
                return f'\n\n::: {{{" ".join(attrs)}}}\n\n{dedented}\n\n:::\n\n'
            return replacer

        text = pattern.sub(make_replacer(env_name), text)

    # --- Pass 2b: Proof environment ---
    def dedent_proof(m):
        inner = m.group(1)
        dedented = textwrap.dedent(inner.strip('\n'))
        return f'\n\n::: {{.proof}}\n\n{dedented}\n\n:::\n\n'

    text = re.sub(r'\\begin\{proof\}[ \t]*\n?(.*?)\\end\{proof\}', dedent_proof, text, flags=re.DOTALL)

    # --- Pass 2c: Hint environment ---
    def dedent_hint(m):
        inner = m.group(1)
        dedented = textwrap.dedent(inner.strip('\n'))
        return f'\n\n::: {{.callout-tip collapse="true" title="Hint"}}\n\n{dedented}\n\n:::\n\n'

    text = re.sub(r'\\begin\{hint\}[ \t]*\n?(.*?)\\end\{hint\}', dedent_hint, text, flags=re.DOTALL)

    # --- Pass 2d: Center environment ---
    def dedent_center(m):
        inner = m.group(1)
        dedented = textwrap.dedent(inner.strip('\n'))
        return f'\n\n<div style="text-align: center;">\n\n{dedented}\n\n</div>\n\n'

    text = re.sub(r'\\begin\{center\}[ \t]*\n?(.*?)\\end\{center\}', dedent_center, text, flags=re.DOTALL)

    # --- Pass 2e: Figures and standalone images ---
    def convert_figure_env(m):
        inner = m.group(1)
        # Extract \includegraphics[opts]{path}
        img_m = re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', inner)
        
        # Robust caption extraction: handle balanced braces for one level (e.g. \eqref{...})
        # This matches \caption{ followed by:
        #   - any char that isn't { or }
        #   - OR a { ... } group
        # repeated, until }
        cap_m = re.search(r'\\caption\{((?:[^{}]|\{[^{}]*\})*)\}', inner)
        
        # Extract \label{...}
        lab_m = re.search(r'\\label\{([^}]*)\}', inner)

        if not img_m:
            return inner

        path = img_m.group(1).strip()
        # Swap .pdf to .svg for web rendering
        if path.lower().endswith('.pdf'):
            path = path[:-4] + '.svg'
        
        caption = cap_m.group(1).strip() if cap_m else ""
        
        attr = '{fig-align="center" width="80%"}'
        if lab_m:
            raw_lab = lab_m.group(1)
            qid = sanitize_label(raw_lab)
            # Quarto figure labels must start with fig-
            fig_id = qid if qid.startswith('fig-') else f"fig-{qid}"
            attr = f"{{#{fig_id} fig-align=\"center\" width=\"80%\"}}"
            label_map[raw_lab] = fig_id
        
        return f'\n\n![{caption}]({path}){attr}\n\n'

    text = re.sub(r'\\begin\{figure\}(?:\[[^\]]*\])?(.*?)\\end\{figure\}', convert_figure_env, text, flags=re.DOTALL)

    def convert_standalone_graphics(m):
        path = m.group(1).strip()
        if path.lower().endswith('.pdf'):
            path = path[:-4] + '.svg'
        return f'\n\n![]({path}){{fig-align="center" width="80%"}}\n\n'
    
    text = re.sub(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', convert_standalone_graphics, text)

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

            # Move ALL labels to the global label map, associating them with the block ID
            # This ensures @eq-secondary-label works (pointing to the same block)
            # and removes them from the math text to avoid MathJax/Quarto conflicts
            inner_labels = list(re.finditer(r'\\label\{([^}]*)\}', inner))
            
            # Remove ALL labels from internal text for display
            clean_inner = re.sub(r'\\label\{([^}]*)\}', '', inner).strip()

            # Build the output block
            if wrap_aligned:
                result.append('\n$$\n\\begin{aligned}\n')
                result.append(clean_inner)
                result.append('\n\\end{aligned}')
            else:
                result.append('\n$$\n')
                result.append(clean_inner)

            if label:
                label_id = sanitize_label(label)
                qid = f"eq-{label_id}"
                label_map[label] = qid
                label_map[label_id] = qid
                # Also map any secondary labels in the same block to this qid
                for il in inner_labels:
                    l = il.group(1)
                    if l != label:
                        label_map[l] = qid
                
                result.append(f'\n$$ {{#{qid}}}\n')
            else:
                # Still register any secondary labels if they exist
                for il in inner_labels:
                    l = il.group(1)
                    # We need a qid here. If no primary label, use the first secondary one.
                    secondary_label_id = sanitize_label(il.group(1))
                    qid = f"eq-{secondary_label_id}"
                    label_map[l] = qid
                    result.append(f'\n$$ {{#{qid}}}\n')
                    break # Only one qid allowed per block
                else:
                    result.append('\n$$\n')

            last_end = end_pos

        result.append(text[last_end:])
        return ''.join(result)

    # aligneq → wrap in \begin{aligned}...\end{aligned}
    text = replace_display_math(text, 'aligneq', wrap_aligned=True)
    text = replace_display_math(text, 'aligneq\\*', starred=True, wrap_aligned=True)
    # align → already an alignment env, but Quarto mathjax needs aligned wrap for raw & and \\
    text = replace_display_math(text, 'align', starred=False, wrap_aligned=True)
    text = replace_display_math(text, 'align\\*', starred=True, wrap_aligned=True)
    # equation → just fence with $$
    text = replace_display_math(text, 'equation', starred=False)
    text = replace_display_math(text, 'equation\\*', starred=True)

    # --- Pass 4: Enumerate / Itemize ---
    def roman(n):
        val = [10, 9, 5, 4, 1]
        syb = ["x", "ix", "v", "iv", "i"]
        res = ""
        i = 0
        while n > 0:
            for _ in range(n // val[i]):
                res += syb[i]
                n -= val[i]
            i += 1
        return res

    def convert_enumerate(m):
        opt_arg = m.group(1)
        inner = m.group(2)
        items = re.split(r'\\item\s*', inner)
        items = [it.strip() for it in items if it.strip()]
        lines = []
        for idx, item in enumerate(items, 1):
            marker = f'{idx}.'
            if opt_arg:
                if 'a' in opt_arg:
                    marker = f'{chr(96+idx)}.' if idx <= 26 else f'{idx}.'
                elif 'A' in opt_arg:
                    marker = f'{chr(64+idx)}.' if idx <= 26 else f'{idx}.'
                elif 'i' in opt_arg:
                    marker = f'{roman(idx)}.'
                elif 'I' in opt_arg:
                    marker = f'{roman(idx).upper()}.'
            
            # Strip trailing \label{...} from items
            item = re.sub(r'\\label\{[^}]*\}', '', item).strip()
            item_lines = item.split('\n')
            indented = item_lines[0].lstrip()
            if len(item_lines) > 1:
                subsequent = []
                for l in item_lines[1:]:
                    if l.strip():
                        subsequent.append('    ' + l.lstrip())
                    else:
                        subsequent.append('')
                indented += '\n' + '\n'.join(subsequent)
            lines.append(f'{marker} {indented}')
        return '\n\n' + '\n\n'.join(lines) + '\n\n'

    text = re.sub(r'\\begin\{enumerate\}(?:\[(.*?)\])?(.*?)\\end\{enumerate\}',
                  convert_enumerate, text, flags=re.DOTALL)

    def convert_itemize(m):
        opt_arg = m.group(1) # just in case
        inner = m.group(2)
        items = re.split(r'\\item\s*', inner)
        items = [it.strip() for it in items if it.strip()]
        lines = []
        for item in items:
            item_lines = item.split('\n')
            indented = item_lines[0].lstrip()
            if len(item_lines) > 1:
                subsequent = []
                for l in item_lines[1:]:
                    if l.strip():
                        subsequent.append('    ' + l.lstrip())
                    else:
                        subsequent.append('')
                indented += '\n' + '\n'.join(subsequent)
            lines.append(f'- {indented}')
        return '\n\n' + '\n\n'.join(lines) + '\n\n'

    text = re.sub(r'\\begin\{itemize\}(?:\[(.*?)\])?(.*?)\\end\{itemize\}',
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
        raw_label = m.group(2)
        label = sanitize_label(raw_label)
        
        # Check label_map first (handles aliases in align blocks)
        if raw_label in label_map:
            return f'@{label_map[raw_label]}'
        if label in label_map:
            return f'@{label_map[label]}'
            
        # ensure eq- prefix
        if label.startswith('eq-'):
            return f'@{label}'
        return f'@eq-{label}'

    # \Cref{X} and \cref{X} → @prefix-X  (best effort)
    def convert_cref(m):
        raw_label = m.group(2)
        label = sanitize_label(raw_label)
        
        target = f'@{label}'
        # First check if this is an item-level label (emit descriptive text)
        if raw_label in item_label_map:
            parent_qid, item_name = item_label_map[raw_label]
            target = f'@{parent_qid} ({item_name})'
        # Then check if this label was mapped during theorem/equation conversion
        elif raw_label in label_map:
            target = f'@{label_map[raw_label]}'
        elif label in label_map:
            target = f'@{label_map[label]}'
        # Try to guess the prefix from the label convention
        elif label.startswith('def'):
            target = f'@def-{label}'
        elif label.startswith('thm'):
            target = f'@thm-{label}'
        elif label.startswith('lem'):
            target = f'@lem-{label}'
        elif label.startswith('prp') or label.startswith('prop'):
            target = f'@prp-{label}'
        elif label.startswith('cor'):
            target = f'@cor-{label}'
        elif label.startswith('eq'):
            target = f'@eq-{label}'
        else:
            # Fallback: assume it's a theorem if no prefix
            target = f'@thm-{label}'
        return target

    def convert_cref_wrapper(text, cmd_pattern):
        def repl(m):
            res = convert_cref(m)
            following = m.group(3) if m.group(3) else ""
            # If followed by a word character or a dot+word character, add a space to aid Pandoc/Quarto
            # We want to keep the dot but add a space after it IF it's followed by a letter
            if following == ".":
                return f"{res}. "
            elif following and re.match(r'\w', following):
                return f"{res} {following}"
            return f"{res}{following}"
        
        # Use a lookahead to see if a dot is followed by a non-whitespace character (like a letter)
        # Or just be aggressive and add space after ref if not followed by whitespace.
        pattern = re.compile(cmd_pattern + r'(\.?)')
        return pattern.sub(repl, text)

    text = convert_cref_wrapper(text, r'(\\[Cc]ref\{([^}]*)\})')
    text = convert_cref_wrapper(text, r'(\\ref\{([^}]*)\})')
    
    # \eqref specific replacer: output ([-@eq-X]) to suppress "Equation" prefix
    def repl_eqref(m):
        res = convert_eqref(m) # returns @eq-label or @label
        # Strip the @ to create the suppressed format [-@label]
        bare_ref = res[1:] if res.startswith('@') else res
        following = m.group(3) if m.group(3) else ""
        if following == ".": 
            return f"([-@{bare_ref}]). "
        return f"([-@{bare_ref}]){following}"
    text = re.sub(r'(\\eqref\{([^}]*)\})(\.?)', repl_eqref, text)

    # Also fix plain @rawlabel references emitted by earlier passes
    # If a label in label_map appears as @label (without prefix), replace it.
    def fix_raw_at_ref(m):
        raw = m.group(1)
        if raw in label_map:
            return f'@{label_map[raw]}'
        return m.group(0)  # leave as-is (likely a real Quarto ref or cite key)

    text = re.sub(r'@([A-Za-z][\w:-]*)', fix_raw_at_ref, text)

    # Pass 7: Inline formatting (using balanced brace extraction)
    for cmd, md_wrap in [('emph', '*'), ('textbf', '**'), ('textit', '*')]:
        cmd_pat = re.compile(r'\\' + cmd + r'\{')
        while True:
            m = cmd_pat.search(text)
            if not m:
                break
            inner, end_pos = extract_balanced(text, m.end() - 1)
            text = text[:m.start()] + f'{md_wrap}{inner}{md_wrap}' + text[end_pos:]

    # \href{url}{text} → [text](<url>)
    href_pat = re.compile(r'\\href\{')
    while True:
        m = href_pat.search(text)
        if not m:
            break
        url, mid_pos = extract_balanced(text, m.end() - 1)
        if mid_pos < len(text) and text[mid_pos] == '{':
            display, end_pos = extract_balanced(text, mid_pos)
            text = text[:m.start()] + f'[{display}](<{url}>)' + text[end_pos:]
        else:
            text = text[:m.start()] + f'<{url}>' + text[mid_pos:]

    # --- Pass 7b: Cross-post references (\postref) ---
    def convert_postref(m):
        folder_arg = re.sub(r'\s+', ' ', m.group(1).strip())   # Normalize whitespace
        label_arg = m.group(2).strip()    # e.g. "thm:doobs" or ""
        display = m.group(3).strip()      # e.g. "Theorem 3.2"

        # Expand display math/linebreaks inside the display text just in case
        display = re.sub(r'\s+', ' ', display)

        # Attempt anchor resolution via registry
        anchor = ''
        if label_registry and folder_arg in label_registry and label_arg:
            if label_arg in label_registry[folder_arg]:
                anchor = '#' + label_registry[folder_arg][label_arg]
            else:
                print(f"  WARNING: \\postref label '{label_arg}' not found in folder '{folder_arg}'")
        elif label_registry and folder_arg not in label_registry:
            print(f"  WARNING: \\postref folder '{folder_arg}' not found in registry")

        # Use absolute path from project root for maximum reliability in Quarto
        # Quarto resolves paths starting with / relative to the project root.
        dst_clean = folder_arg.replace('\\', '/')
        target = f"/posts/{dst_clean}/index.qmd"
        return f'[{display}](<{target}{anchor}>)'

    # --- Pass 7c: Internal References (\ref, \eqref, \Cref) ---
    def convert_refs(m):
        label = m.group(1)
        qid = label_map.get(label, sanitize_label(label))
        # Ensure we point to the right prefix if it's a known environment
        if qid.startswith('eq-'):
            return f'(@{qid})'
        return f'@{qid}'

    text = re.sub(r'\\(?:eqref|ref|Cref)\{([^}]*)\}', convert_refs, text)

    text = re.sub(
        r'\\postref\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}',
        convert_postref, text
    )

    # --- Pass 8: Clean up ---
    # Convert LaTeX double quotes to standard curly quotes
    text = re.sub(r'``', r'“', text)
    text = re.sub(r"''", r'”', text)

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

    # Resources (PDF and Image) so Quarto copies them
    resources = []
    if img:
        resources.append(f'"{img}"')
    pdf_file = meta.get('pdf', '')
    if pdf_file:
        lines.append(f'pdf: "{pdf_file}"') # Inject pdf into YAML for dashboard
        resources.append(f'"{pdf_file}"')
    
    if resources:
        lines.append('resources:')
        for res in resources:
            lines.append(f'  - {res}')

    # Format block with MathJax
    lines.append('format:')
    lines.append('  html:')
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
                   output_name='index.qmd', blog_dir=None,
                   label_registry: dict | None = None,
                   posts_root: Path | None = None):
    r"""Convert a single LaTeX folder to a Quarto post.

    If label_registry and posts_root are provided, cross-post \postref
    commands are resolved to relative Quarto links with anchors.
    """
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
        
    # Determine if a PDF version exists to provide a link
    pdf_file = tex_path.with_suffix('.pdf')
    pdf_filename = pdf_file.name if pdf_file.exists() else None
    
    if pdf_filename:
        meta['pdf'] = pdf_filename
        print(f"  PDF:      {pdf_filename}")
    else:
        print(f"  PDF:      (none)")

    # Compute current folder path relative to posts/ for cross-post resolution
    current_folder = None
    if posts_root and label_registry:
        try:
            current_folder = str(folder.relative_to(posts_root)).replace('\\', '/')
        except ValueError:
            pass  # folder is not under posts_root

    # Parse preamble for MathJax macros
    sty_path = folder / preamble_name
    macros = parse_preamble_macros(sty_path)
    print(f"  Extracted {len(macros)} macros from {preamble_name}")
    mathjax_macros = format_mathjax_macros(macros)

    # Extract and convert body
    body = extract_body(tex_content)
    converted_body = convert_body(body, label_registry=label_registry,
                                  current_folder=current_folder,
                                  pdf_filename=pdf_filename)

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
        # Phase 1: Build global label registry
        print("Phase 1: Building cross-post label registry...")
        registry = build_label_registry(folder, args.tex)
        print(f"  Indexed {sum(len(v) for v in registry.values())} labels across {len(registry)} posts.\n")

        # Phase 2: Convert each post found in registry
        print(f"Found {len(registry)} post(s) to convert:\n")
        for folder_rel_path in sorted(registry.keys()):
            post_folder = folder / folder_rel_path
            print("=" * 60)
            print(f"  Converting: {folder_rel_path}")
            print("=" * 60)
            
            # Find the best tex file for this folder as well
            current_tex = find_main_tex(post_folder, preferred_name=args.tex)
            if not current_tex:
                print(f"  SKIP: No .tex file found in {folder_rel_path}")
                continue

            convert_folder(
                post_folder, current_tex.name, args.preamble, args.output, args.blog_dir,
                label_registry=registry, posts_root=folder
            )
    else:
        # Single folder mode
        convert_folder(folder, args.tex, args.preamble, args.output, args.blog_dir)


if __name__ == '__main__':
    main()

