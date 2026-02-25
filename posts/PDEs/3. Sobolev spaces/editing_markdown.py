# %% [markdown]
# # Pandoc Markdown → Blog Post Converter
# Converts the `post.txt` output from pandoc into a blog-ready `.md` file.
# Run cell-by-cell in VS Code (Ctrl+Shift+P → "Run Cell") or as a script.

# %% Stage 0: Configuration
import re
import os
import sys
import json
import io
from pathlib import Path

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ─── Post metadata ───────────────────────────────────────────────────────────
CONFIG = {
    "title":       "Sobolev spaces",
    "subtitle":    "Density, trace and embeddings",
    "tags":        "[PDEs]",
    "date":        "2023-07-12",
    "number":      3,
    "pdftitle":    "Sobolev spaces",
    "img":         "sobolev_leoni.jpg",
    "author":      "L.Llamazares-Elias",
    # Where the final .md file is saved (your Jekyll _posts folder)
    "posts_path":  r"C:\Users\liaml\Documentos\LiamLlamazares.github.io\_posts",
}

# Derived paths (relative to this script)
SCRIPT_DIR = Path(__file__).resolve().parent if "__file__" in dir() else Path.cwd()
POST_PATH  = SCRIPT_DIR / "post.txt"
BIB_PATH   = SCRIPT_DIR / "biblio.txt"

# Derived filename for the blog post
tag = CONFIG["tags"].strip("[]").split(",")[0]
post_filename = (
    f"{CONFIG['date']}-{tag}-{CONFIG['number']}-"
    f"{CONFIG['title'].replace(' ', '_')}.md"
)
OUTPUT_BLOG   = SCRIPT_DIR / "blog.txt"
OUTPUT_POST   = Path(CONFIG["posts_path"]) / post_filename

print(f"Post file:   {POST_PATH}")
print(f"Bib file:    {BIB_PATH}")
print(f"Output blog: {OUTPUT_BLOG}")
print(f"Output post: {OUTPUT_POST}")

# %% Stage 1: Load files
e = POST_PATH.read_text(encoding="utf-8")
bib = BIB_PATH.read_text(encoding="utf-8")

print(f"Post length: {len(e)} chars, {e.count(chr(10))} lines")
print(f"Bib length:  {len(bib)} chars")

# %% Stage 2: Extract citations
# Find all [@...] patterns in the post. 
# The original Mathematica code searched for "[@" and "]" separately,
# which produced mismatched counts. This regex handles it correctly,
# including citations with newlines like [@taylor2013partial\npage 241].
citation_pattern = re.compile(r'\[@([^\]]+)\]')
citation_matches = list(citation_pattern.finditer(e))

# Full match text (e.g. "[@leoni2017first]") and inner key (e.g. "leoni2017first")
citations_full = [m.group(0) for m in citation_matches]
citations_keys = [m.group(1) for m in citation_matches]
citation_spans = [(m.start(), m.end()) for m in citation_matches]

print(f"Found {len(citation_matches)} citations:")
for i, (full, key) in enumerate(zip(citations_full, citations_keys)):
    print(f"  {i+1}. {full!r}  →  key={key!r}")

# %% Stage 3: Format citations as "Author, Year"
def format_citation(key: str) -> str:
    """Extract author surname and year from a citation key like 'leoni2017first'."""
    # Clean up: the key might contain extra text like "taylor2013partial\npage 241"
    clean_key = re.split(r'\s', key)[0]  # take first word before any whitespace
    letters = re.findall(r'[a-zA-Z]+', clean_key)
    digits  = re.findall(r'\d+', clean_key)
    author = letters[0].capitalize() if letters else "?"
    year   = digits[0] if digits else "?"
    return f"{author}, {year}"

citations_formatted = [format_citation(k) for k in citations_keys]
print("Formatted citations:")
for cf in citations_formatted:
    print(f"  {cf}")

# %% Stage 4: Look up URLs from bibliography
def find_bib_url(bib_text: str, citation_key: str) -> str:
    """Find the URL for a citation key in the BibTeX file."""
    # Clean the key (remove page references etc.)
    clean_key = re.split(r'\s', citation_key)[0]
    
    # Find the bib entry that starts with @type{clean_key,
    pattern = re.compile(
        r'@\w+\{' + re.escape(clean_key) + r'\s*,',
        re.IGNORECASE
    )
    match = pattern.search(bib_text)
    if not match:
        print(f"  WARNING: No bib entry found for '{clean_key}'")
        return ""
    
    # Find the closing } of this entry (track brace depth)
    start = match.start()
    depth = 0
    end = start
    for i in range(start, len(bib_text)):
        if bib_text[i] == '{':
            depth += 1
        elif bib_text[i] == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    
    entry = bib_text[start:end]
    
    # Extract URL from the entry
    url_match = re.search(r'url\s*=\s*\{([^}]+)\}', entry)
    if url_match:
        return url_match.group(1).strip().strip('"')
    
    # Some entries have url={...} with quotes inside
    url_match = re.search(r'url\s*=\s*\{"([^"]+)"\}', entry)
    if url_match:
        return url_match.group(1).strip()
    
    print(f"  WARNING: No URL found in bib entry for '{clean_key}'")
    return ""

websites = [find_bib_url(bib, k) for k in citations_keys]
print("\nURLs found:")
for i, (cf, url) in enumerate(zip(citations_formatted, websites)):
    print(f"  {i+1}. {cf}: {url[:60]}{'...' if len(url) > 60 else ''}")

# %% Stage 5: Replace citations in text
# Build replacement strings: [Author, Year](url)
# Use zzx/zzy as temporary placeholders for [ ] to avoid conflicts
# with other bracket processing later.
e0 = e
for i in range(len(citation_matches) - 1, -1, -1):
    # Replace in reverse order to preserve positions
    start, end = citation_spans[i]
    if websites[i]:
        replacement = f"zzx{citations_formatted[i]}zzy({websites[i]})"
    else:
        replacement = f"zzx{citations_formatted[i]}zzy"
    e0 = e0[:start] + replacement + e0[end:]

print(f"Replaced {len(citation_matches)} citations")
# Verify a sample
sample = e0[citation_spans[0][0]:citation_spans[0][0]+80] if citation_spans else ""
print(f"Sample: ...{sample}...")

# %% Stage 6: Equation label replacement  
# Pattern: [\[label\]](#label){reference-type="eqref" reference="label"}
# Replace with: (\ref{label})
eq_ref_pattern = re.compile(
    r'\[\\?\[([^\]]+)\\?\]\]'  # [\[label\]] or [[label]]
    r'\(#[^)]+\)'              # (#label)
    r'\{reference-type="eqref"\s+reference="[^"]+"\}',  # {reference-type=...}
    re.DOTALL
)

def replace_eq_ref(m):
    label = m.group(1)
    return f"(\\\\ref{{{label}}})"

e00_count = len(eq_ref_pattern.findall(e0))
e00 = eq_ref_pattern.sub(replace_eq_ref, e0)
print(f"Replaced {e00_count} equation references")

# Also try the slightly different format pandoc sometimes produces
eq_ref_pattern2 = re.compile(
    r'\[\\?\[([^\]]+)\\?\]\]'
    r'\(#[^)]+\)'
    r'\{reference-type="eqref"\s+reference="[^"]+"\s*\}',
    re.DOTALL
)
# Already handled above if the first pattern is general enough.

# %% Stage 7: Aligned → Align for labeled equations
# When \label{} appears inside \begin{aligned}...\end{aligned}, 
# change to \begin{align}...\end{align} so MathJax numbers them.

def replace_aligned_with_label(text):
    """Replace aligned with align when the block contains a \\label."""
    result = text
    
    # Find all \label positions
    label_positions = [m.start() for m in re.finditer(r'\\label\{', result)]
    
    if not label_positions:
        print("No \\label found, skipping aligned→align")
        return result
    
    # For each \label, check if the containing environment is "aligned"
    # and if this is the FIRST label in that block (for multi-label support)
    begin_aligned_positions = [m.start() for m in re.finditer(r'\\begin\{aligned\}', result)]
    end_aligned_positions   = [m.start() for m in re.finditer(r'\\end\{aligned\}',   result)]
    
    # Track which aligned environments contain a label (use the first label only)
    blocks_to_convert = set()
    for lp in label_positions:
        # Find the most recent \begin{aligned} before this label
        prev_begins = [b for b in begin_aligned_positions if b < lp]
        if not prev_begins:
            continue
        block_start = max(prev_begins)
        
        # Check if there's already a label between block_start and this label
        labels_between = [l for l in label_positions if block_start < l < lp]
        if len(labels_between) == 0:
            blocks_to_convert.add(block_start)
    
    # Also find the corresponding \end{aligned} for each block
    ends_to_convert = set()
    for bs in blocks_to_convert:
        next_ends = [e for e in end_aligned_positions if e > bs]
        if next_ends:
            ends_to_convert.add(min(next_ends))
    
    # Do replacements (in reverse order to preserve positions)
    all_replacements = []
    for pos in sorted(blocks_to_convert, reverse=True):
        all_replacements.append((pos, r'\begin{aligned}', r'\begin{align}'))
    for pos in sorted(ends_to_convert, reverse=True):
        all_replacements.append((pos, r'\end{aligned}', r'\end{align}'))
    
    all_replacements.sort(key=lambda x: x[0], reverse=True)
    for pos, old, new in all_replacements:
        idx = result.find(old, pos)
        if idx == pos:
            result = result[:idx] + new + result[idx + len(old):]
    
    print(f"Converted {len(blocks_to_convert)} aligned→align blocks")
    return result

e01 = replace_aligned_with_label(e00)

# %% Stage 8: Figure HTML generation
# Input:  ![alt text](path){width="X%" ...}
# Output: <figure><img src="..."><figcaption>alt</figcaption></figure>

def convert_figure(match):
    description = match.group(1)
    path = match.group(2)
    options = match.group(3) if match.group(3) else ""
    
    # Normalize \[ and \] to ( and ) in description
    description = description.replace("\\[", "(").replace("\\]", ")")
    
    # Convert .pdf to .svg for web
    web_path = re.sub(r'\.pdf$', '.svg', path)
    
    # Extract width from options
    width_match = re.search(r'width="([^"]+)"', options)
    width = width_match.group(1) if width_match else "90%"
    
    # Build ID from file basename
    basename = Path(path).stem.replace("_", "-")
    
    # Clean alt text (remove $ for alt attribute)
    clean_alt = description.replace("$", "")
    
    html = (
        f'<figure style="text-align: center;">'
        f'<img src="{{{{\'assets/img/Figures/{web_path}\' | relative_url }}}}" '
        f'alt="{clean_alt}" width="{width}" id="fig:{basename}">'
        f'<figcaption style="text-align: center;">{description}</figcaption>'
        f'</figure>'
    )
    return html

fig_pattern = re.compile(
    r'!\[([^\]]*)\]'       # ![alt text]
    r'\(([^)]+)\)'          # (path)
    r'(?:\{([^}]+)\})?',    # {options} (optional)
    re.DOTALL
)

fig_count = len(fig_pattern.findall(e01))
e01 = fig_pattern.sub(convert_figure, e01)
print(f"Converted {fig_count} figures")

# %% Stage 9: Theorem/proposition label anchoring
# Input:  ::: {#name .theorem}
#         **Theorem N** ...
# Output: <a name="name"> **Theorem N** </a> ...
# The ::: {#...} line is replaced with an anchor tag.

def process_theorem_labels(text):
    """Convert ::: {#name .type} blocks to <a name="name"> anchored headings."""
    # Find all ::: {#label .type} patterns
    label_pattern = re.compile(r'::: \{#([^ ]+) \.(\w+)\}')
    matches = list(label_pattern.finditer(text))
    
    if not matches:
        print("No theorem labels found")
        return text
    
    result = text
    # Process in reverse to preserve positions
    for m in reversed(matches):
        label_name = m.group(1)
        label_type = m.group(2)
        full_match = m.group(0)
        
        # Find the **Type N** or **Type N** (text) that follows
        # It should appear shortly after the ::: {#...} line
        after = result[m.end():]
        bold_match = re.search(r'\*\*(.+?)\*\*', after)
        
        if bold_match:
            # The name from the label (e.g., "complement theorem") 
            name_slug = label_name
            
            # Replace the ::: {#...} with empty string
            # And wrap the **bold** text with an anchor
            old_bold = f"**{bold_match.group(1)}**"
            new_bold = f'<a name="{name_slug}"> **{bold_match.group(1)}** </a>'
            
            # First remove the ::: {#...} line
            result = result[:m.start()] + result[m.end():]
            
            # Now find and replace the first occurrence of **...** after the removal point
            idx = result.find(old_bold, m.start())
            if idx >= 0:
                result = result[:idx] + new_bold + result[idx + len(old_bold):]
        else:
            # Just remove the ::: {#...} line
            result = result[:m.start()] + result[m.end():]
    
    print(f"Processed {len(matches)} theorem labels")
    return result

e02 = process_theorem_labels(e01)

# %% Stage 10: Theorem/section reference links
# Input:  [N](#name){reference-type="ref" reference="name"}
# Output: <a href="#name">N</a>
ref_pattern = re.compile(
    r'\[(\d+)\]'                    # [N]
    r'\(#([^)]+)\)'                 # (#name)
    r'\{reference-type="ref"\s+'    # {reference-type="ref" 
    r'reference="([^"]+)"\}',       # reference="name"}
    re.DOTALL
)

def replace_ref(m):
    num = m.group(1)
    link = m.group(2)
    return f'<a href="#{link}">{num}</a>'

ref_count = len(ref_pattern.findall(e02))
e03 = ref_pattern.sub(replace_ref, e02)
print(f"Replaced {ref_count} theorem/section references")

# Also handle reference-type="eqref" that might have been missed
eqref_remaining = re.compile(
    r'\[([^\]]+)\]'
    r'\(#([^)]+)\)'
    r'\{reference-type="eqref"\s+'
    r'reference="([^"]+)"\}',
    re.DOTALL
)
eqref_remaining_count = len(eqref_remaining.findall(e03))
e03 = eqref_remaining.sub(lambda m: f'(\\\\ref{{{m.group(3)}}})', e03)
if eqref_remaining_count:
    print(f"Also replaced {eqref_remaining_count} remaining eqref references")

# %% Stage 11: Section label handling
# Input:  # Title {#section-name}
# Output: # <a name="section-name"> Title </a>
section_label_pattern = re.compile(
    r'^(#{1,6})\s+(.+?)\s+\{#([^}]+)\}\s*$',
    re.MULTILINE
)

def replace_section_label(m):
    hashes = m.group(1)
    title = m.group(2)
    name = m.group(3)
    return f'{hashes} <a name="{name}"> {title} </a>'

section_count = len(section_label_pattern.findall(e03))
e04 = section_label_pattern.sub(replace_section_label, e03)
print(f"Processed {section_count} section labels")

# %% Stage 12: Equation div wrapping
# Wrap display math $$...$$ in <div>...</div> for proper rendering.
# First $$ gets \n\n<div>\n $$, second $$ gets $$\n</div>\n\n

def wrap_display_math(text):
    """Wrap pairs of $$ in <div> tags."""
    # Find all $$ positions
    positions = [m.start() for m in re.finditer(r'\$\$', text)]
    if len(positions) % 2 != 0:
        print(f"WARNING: Odd number of $$ found ({len(positions)}), skipping div wrapping")
        return text
    
    result = text
    # Process pairs in reverse
    for i in range(len(positions) - 2, -1, -2):
        open_pos = positions[i]
        close_pos = positions[i + 1]
        
        # Replace closing $$
        result = result[:close_pos] + '$$\n</div>\n\n ' + result[close_pos + 2:]
        # Replace opening $$
        result = result[:open_pos] + '\n\n<div>\n $$' + result[open_pos + 2:]
    
    print(f"Wrapped {len(positions)//2} display math blocks in <div> tags")
    return result

e1 = wrap_display_math(e04)

# %% Stage 13: Bracket escaping in inline math
# Inside $...$ (but not $$...$$), escape \{ → \\{ and \} → \\}
def escape_brackets_in_inline_math(text):
    """Escape curly braces inside inline math $...$ environments."""
    # Find positions of $$ (display math) so we exclude them
    double_dollar_positions = set()
    for m in re.finditer(r'\$\$', text):
        double_dollar_positions.add(m.start())
        double_dollar_positions.add(m.start() + 1)
    
    # Find all single $ positions (not part of $$)
    single_positions = []
    for m in re.finditer(r'\$', text):
        if m.start() not in double_dollar_positions:
            single_positions.append(m.start())
    
    if len(single_positions) % 2 != 0:
        print(f"WARNING: Odd number of single $ found ({len(single_positions)})")
        return text
    
    # Process pairs in reverse
    result = text
    count = 0
    for i in range(len(single_positions) - 2, -1, -2):
        start = single_positions[i]
        end = single_positions[i + 1] + 1
        segment = result[start:end]
        new_segment = segment.replace("\\{", "\\\\{").replace("\\}", "\\\\}")
        if new_segment != segment:
            count += 1
        result = result[:start] + new_segment + result[end:]
    
    print(f"Escaped brackets in {count} inline math spans")
    return result

e2 = escape_brackets_in_inline_math(e1)

# %% Stage 14: Hints → toggle buttons
def convert_hints(text):
    """Convert ::: hint ... ::: blocks to HTML toggle buttons."""
    hint_pattern = re.compile(
        r'::: hint\n(.*?)\n:::',
        re.DOTALL
    )
    
    matches = list(hint_pattern.finditer(text))
    if not matches:
        print("No hints found")
        return text
    
    result = text
    for m in reversed(matches):
        # Extract the content (skip the **Hint N**. line and get the rest)
        content = m.group(1).strip()
        
        # Find the actual hint content after the **Hint N**. line
        content_match = re.search(r'\*\*.*?\*\*\.?\s*(.*)', content, re.DOTALL)
        if content_match:
            hint_content = content_match.group(1).strip()
        else:
            hint_content = content
        
        html = (
            '<div class="exercise-container">\n'
            '<button class="exercise-button" onclick="toggleExercise(this)">Hint</button>\n'
            '<div class="exercise-text">\n'
            f'{hint_content}\n'
            '</div>\n'
            '</div>'
        )
        result = result[:m.start()] + html + result[m.end():]
    
    print(f"Converted {len(matches)} hints to toggle buttons")
    return result

e20 = convert_hints(e2)

# %% Stage 15: Math symbol escaping (* → \star, _ → \U in math)
def escape_math_symbols(text):
    """Replace * with \\star and _ with \\U inside math environments."""
    
    def replace_in_match(m):
        s = m.group(0)
        s = s.replace("*", "\\star ")
        s = s.replace("_", "\\U ")
        return s
    
    # Apply to inline math $...$
    result = re.sub(r'(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)', replace_in_match, text, flags=re.DOTALL)
    
    # Apply to display math $$...$$
    result = re.sub(r'\$\$.*?\$\$', replace_in_match, result, flags=re.DOTALL)
    
    # Apply to \begin{...}...\end{...} environments
    result = re.sub(r'\\begin\{.*?\}.*?\\end\{.*?\}', replace_in_match, result, flags=re.DOTALL)
    
    return result

e200 = escape_math_symbols(e20)

# Trim trailing whitespace from lines
lines = e200.split("\n")
trimmed = [line.rstrip() for line in lines]
e21 = "\n".join(trimmed)

print("Math symbols escaped and lines trimmed")

# %% Stage 16: Cleanup — remove pandoc environments, fix formatting
# Remove pandoc div markers
env_removals = [
    "::: example", "::: hint", "::: exercise", "::: proof",
    "::: proposition", "::: lemma", "::: theorem", "::: observation",
    "::: corollary", "::: definition", ":::"
]

e3 = e21
for env in env_removals:
    e3 = e3.replace(env, "")

# Replace ^* with ^\star (outside of already-processed math)
e3 = e3.replace("^*", "^\\star ")

# Temporarily protect ** (bold markers) by replacing with zzz
e3 = e3.replace("**", "zzz")

# Remove stray single * (pandoc italic markers from environments)
e3 = re.sub(r'(?<!\*)(?<!\w)\*(?!\*)(?!\w)', '', e3)

# Build the YAML front matter
yaml_header = (
    "---\n"
    "layout: post\n"
    f"title: {CONFIG['title']}\n"
    f"subtitle: {CONFIG['subtitle']}\n"
    f"thumbnail-img: /assets/img/{CONFIG['img']}\n"
    f"share-img: /assets/img/{CONFIG['img']}\n"
    f"tags: {CONFIG['tags']}\n"
    f"author: {CONFIG['author']}\n"
    "---"
)

# Replace the pandoc YAML header (between --- ... ---)
e3 = re.sub(r'---.*?---', yaml_header, e3, count=1, flags=re.DOTALL)

# Restore ** from zzz
e4 = e3.replace("zzz", "**")

# Restore [ ] from zzx/zzy (citation brackets)
e4 = e4.replace("zzx", "[").replace("zzy", "]")

print("Cleanup complete")

# %% Stage 17: Additional fixes

# PDF link
if CONFIG["pdftitle"]:
    pdf_link = (
        f"\n\nA (possibly not updated) pdf version of this page is provided "
        f"[here](/assets/pdfs/{tag}/{CONFIG['pdftitle']}.pdf)."
    )
else:
    pdf_link = ""

e6 = e4 + pdf_link

# Fix \left| and \right| (remove \left and \right before |)
e7 = e6.replace("\\left\\|", "\\|").replace("\\right\\|", "\\|")

# Fix CJK artifacts
e8 = e7.replace(" CJK\nUTF8gbsn", "")

# Fix aligalign bug (from label replacement)
e9 = e8.replace("aligalign", "align}")

# Replace \bm with \mathbf (MathJax compatibility)
e10 = e9.replace("\\bm", "\\mathbf")

# Convert **bold** to <b> tags for theorem statements etc.
e11 = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', e10)

# Also make "Proof." bold
e11 = e11.replace("Proof.", "<b>Proof.</b>")

print("Additional fixes applied")

# %% Stage 18: Markdown links → HTML links
# Convert [text](http...) to <a href="...">text</a>

def convert_markdown_links(text):
    """Convert markdown links [text](url) to HTML <a> tags."""
    # Find links that start with http
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')
    
    matches = list(link_pattern.finditer(text))
    if not matches:
        print("No markdown links to convert")
        return text
    
    result = text
    for m in reversed(matches):
        link_text = m.group(1)
        url = m.group(2)
        html = f'<a href="{url}">{link_text}</a>'
        result = result[:m.start()] + html + result[m.end():]
    
    print(f"Converted {len(matches)} markdown links to HTML")
    return result

e12 = convert_markdown_links(e11)

# %% Stage 19: Export
OUTPUT_BLOG.write_text(e12, encoding="utf-8")
print(f"Written to {OUTPUT_BLOG}")

try:
    OUTPUT_POST.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_POST.write_text(e12, encoding="utf-8")
    print(f"Written to {OUTPUT_POST}")
except Exception as ex:
    print(f"Could not write to posts path: {ex}")
    print("(This is expected if the posts directory doesn't exist locally)")

print(f"\nFinal output: {len(e12)} chars, {e12.count(chr(10))} lines")
print("Done.")
