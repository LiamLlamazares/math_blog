import re
import argparse

def expand_macros(content):
    """
    Expands custom LaTeX macros.
    """
    macros = {
        # Zero-argument macros
        r'\\eps': r'\\varepsilon',
        r'\\Th': r'\\bm{\\theta}',
        r'\\Thh': r'\\bm{\\Theta}',
        r'\\xxi': r'\\bm{\\xi}',
        r'\\om': r'\\bm{\\om}',
        r'\\Id': r'\\bm{I}',
        r'\\ker': r'\\bm{ker}', # Renamed
        r'\\star': r'*', # Renamed
        r'\\Im': r'\\bm{Im}', # Renamed
        r'\\iso': r'\\xrightarrow{\\sim}',
        r'\\d ': r'\\,\\mathrm{d} ',
        r'\\dx': r'\\,\\mathrm{d}x',
        r'\\dy': r'\\,\\mathrm{d}y',
        r'\\vol': r'\\mathrm{vol}',
        r'\\x': r'\\bm{x}',
        r'\\y': r'\\bm{y}',
        r'\\A': r'\\mathbb{A}',
        r'\\C': r'\\mathbb{C}',
        r'\\E': r'\\mathbb{E}',
        r'\\F': r'\\mathbb{F}',
        r'\\N': r'\\mathbb{N}',
        r'\\Q': r'\\mathbb{Q}',
        r'\\R': r'\\mathbb{R}',
        r'\\Z': r'\\mathbb{Z}',
        r'\\Aa': r'\\mathcal{A}',
        r'\\Bb': r'\\mathcal{B}',
        r'\\Cc': r'\\mathcal{C}',
        r'\\Dd': r'\\mathcal{D}',
        r'\\Ee': r'\\mathcal{E}',
        r'\\Ff': r'\\mathcal{F}',
        r'\\Gg': r'\\mathcal{G}',
        r'\\Hh': r'\\mathcal{H}',
        r'\\Kk': r'\\mathcal{K}',
        r'\\Ll': r'\\mathcal{L}',
        r'\\Mm': r'\\mathcal{M}',
        r'\\Nn': r'\\mathcal{N}',
        r'\\Oo': r'\\mathcal{O}',
        r'\\Pp': r'\\mathcal{P}',
        r'\\Qq': r'\\mathcal{Q}',
        r'\\Rr': r'\\mathcal{R}',
        r'\\Ss': r'\\mathcal{S}',
        r'\\Tt': r'\\mathcal{T}',
        r'\\Uu': r'\\mathcal{U}',
        r'\\Vv': r'\\mathcal{V}',
        r'\\Ww': r'\\mathcal{W}',
        r'\\Xx': r'\\mathcal{X}',
        r'\\Yy': r'\\mathcal{Y}',
        r'\\Zz': r'\\mathcal{Z}',
    }

    # One-argument macros (regex patterns and their replacements)
    # Order matters for some, e.g., \b should be after \Thh if \Thh uses \b
    # For simplicity, we'll apply them in a fixed order and iterate.
    arg_macros = [
        (r'\\b\{(.*?)\}', r'{{\\bm{\1}}}'), # Renamed
        (r'\\red\{(.*?)\}', r'{{\\color{red}\1}}'),
        (r'\\diag\{(.*?)\}', r'\\operatorname{diag}\\left(\1\\right)'),
        (r'\\fk\{(.*?)\}', r'\\mathfrak{\1}'),
        (r'\\wh\{(.*?)\}', r'\\widehat{\1}'),
        (r'\\tl\{(.*?)\}', r'\\widetilde{\1}'),
        (r'\\br\{(.*?)\}', r'\\left\\langle\1\\right\\rangle'),
        (r'\\set\{(.*?)\}', r'\\left\\{\\1\\right\\}'),
        (r'\\qp\{(.*?)\}', r'\\left(\1\\right)'),
        (r'\\qb\{(.*?)\}', r'\\left[\1\\right]'),
        (r'\\qt\{(.*?)\}', r'\\left(\1\\right)'),
        (r'\\supp\{(.*?)\}', r'\\bm{supp}(\1)'),
        (r'\\tr\{(.*?)\}', r'\\mathrm{tr}\\left(\1\\right)'), # Renamed
        (r'\\norm\{(.*?)\}', r'\\left\\lVert \1 \\right\\rVert'), # Renamed
        (r'\\abs\{(.*?)\}', r'\\left| \1 \\right|'), # Renamed
        (r'\\rmm\{(.*?)\}', r'\\mathrm{\1}'),
        (r'\\mat\{(.*?)\}', r'\\begin{bmatrix}{\1}\\end{bmatrix}'),
        # Two-argument macros
        (r'\\restr\{(.*?)\}\{(.*?)\}', r'\\left.\1\\right|{\2}'),
    ]

    # Apply zero-argument macros first
    for pattern, replacement in macros.items():
        content = re.sub(pattern, replacement, content)

    # Apply argument-based macros iteratively to handle potential nesting
    for _ in range(5): # Iterate a few times to catch nested macros
        for pattern, replacement in arg_macros:
            content = re.sub(pattern, replacement, content)

    # Handle specific complex macros that are not simple replacements
    content = re.sub(r'\\td', r'TODO', content) # Simplified
    content = re.sub(r'\\liam', r'', content) # Remove color command
    content = re.sub(r'\\liamtodo\{(.*?)\}', r'TODO: \1', content)

    return content

def convert_latex_to_markdown(latex_content, list_style='numbered'):
    # Extract content between \begin{document} and \end{document}
    try:
        content = re.search(r'\\begin{document}(.*?)\\end{document}', latex_content, re.DOTALL).group(1)
    except AttributeError:
        print("No \\begin{document} found. Processing the whole file.")
        content = latex_content

    # First, expand all the custom macros
    content = expand_macros(content)

    # Remove title, author, date, maketitle
    content = re.sub(r'\\title\{(.*?)\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\author\{(.*?)\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\date\{(.*?)\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\maketitle', '', content, flags=re.DOTALL)

    # Sections and subsections
    content = re.sub(r'\\section\{(.*?)\}', r'# \1', content)
    content = re.sub(r'\\subsection\{(.*?)\}', r'## \1', content)

    # Bold and italics
    content = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', content)
    content = re.sub(r'\\emph\{(.*?)\}', r'*\1*', content)

    # Citations
    content = re.sub(r'\\cite\{(.*?)\}', r'[[\1]]', content)

    # Numbered lists
    def replace_enum(match):
        items = match.group(1).strip().split('\\item')
        processed_items = []
        for i, item in enumerate(items):
            if item.strip():
                if list_style == 'todo':
                    processed_items.append(f"- [ ] {item.strip()}")
                else:
                    processed_items.append(f"{i}. {item.strip()}")
        return '\n'.join(processed_items)

    content = re.sub(r'\\begin{enumerate}(.*?)\\end{enumerate}', replace_enum, content, flags=re.DOTALL)
    
    # Remove bibliography
    content = re.sub(r'\\bibliography\{.*?\}', '', content)

    # Basic cleanup
    content = content.strip()

    return content

def main():
    parser = argparse.ArgumentParser(description='Convert LaTeX to Markdown.')
    parser.add_argument('input_file', help='The input LaTeX file.')
    parser.add_argument('output_file', help='The output Markdown file.')
    parser.add_argument('--list-style', choices=['numbered', 'todo'], default='numbered',
                        help='The style for numbered lists (default: numbered).')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            latex_content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found.")
        return

    markdown_content = convert_latex_to_markdown(latex_content, args.list_style)

    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Successfully converted '{args.input_file}' to '{args.output_file}'.")

if __name__ == '__main__':
    main()
