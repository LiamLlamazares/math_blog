import os
import re

search_dir = r"c:\Users\liaml\Documents\GitHub\Research\math_blog\posts"
pattern1 = re.compile(r'\(link\)')
pattern2 = re.compile(r'\\(?:href|HREF)\{(https?://(?:www\.)?nowheredifferentiable\.com[^}]*)\}')

matches = []

for root, _, files in os.walk(search_dir):
    for file in files:
        if file.endswith(('.tex', '.qmd')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        m1 = pattern1.findall(line)
                        if m1:
                            matches.append((os.path.relpath(filepath, search_dir), i, '(link)'))
                        m2 = pattern2.findall(line)
                        for link in m2:
                            matches.append((os.path.relpath(filepath, search_dir), i, link))
            except Exception:
                pass

with open(r"c:\Users\liaml\Documents\GitHub\Research\math_blog\broken_links_list.md", "w", encoding='utf-8') as f:
    f.write("# Broken Links List\n\n")
    for file, line, match in matches:
        f.write(f"- `{file}` line {line}: {match}\n")

print(f"Found {len(matches)} links.")
