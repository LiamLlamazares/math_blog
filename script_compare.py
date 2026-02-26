import re
import sys

md_file = r"c:\Users\liaml\Documents\GitHub\Research\math_blog\_posts\2023-07-12-PDEs-3-Sobolev_spaces.md"
tex_file = r"c:\Users\liaml\Documents\GitHub\Research\math_blog\posts\PDEs\3. Sobolev spaces\Sobolev spaces.tex"

def parse_md(filepath):
    struct = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if line.startswith('#'):
                struct.append((i+1, "HEADER", line.strip()))
            elif re.match(r'^\*\*(Theorem|Lemma|Proposition|Definition|Exercise|Example|Observation|Corollary)', line):
                match = re.search(r'^\*\*(.*?)\*\*', line)
                if match:
                    struct.append((i+1, "ENV", match.group(1)))
    return struct

def parse_tex(filepath):
    struct = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if '\\section{' in line or '\\subsection{' in line:
                match = re.search(r'\\(sub)?section\{(.*?)\}', line)
                if match:
                    struct.append((i+1, "HEADER", match.group(2)))
            elif '\\begin{theorem}' in line or '\\begin{lemma}' in line or '\\begin{proposition}' in line or '\\begin{definition}' in line or '\\begin{exercise}' in line or '\\begin{example}' in line or '\\begin{observation}' in line or '\\begin{corollary}' in line:
                match = re.search(r'\\begin\{(.*?)\}', line)
                if match:
                    struct.append((i+1, "ENV", match.group(1)))
    return struct

md_struct = parse_md(md_file)
tex_struct = parse_tex(tex_file)

print("Markdown Structure:")
for l, t, content in md_struct:
    print(f"{l}: {t} - {content}")

print("\n\nTex Structure:")
for l, t, content in tex_struct:
    print(f"{l}: {t} - {content}")
