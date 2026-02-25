import os, re, json, string
import urllib.parse
from uuid import uuid4

with open('c:/Users/liaml/Documents/GitHub/Research/math_blog/replacements.json', 'r') as f:
    replacements = json.load(f)

search_dir = r'c:\Users\liaml\Documents\GitHub\Research\math_blog\posts'

slug_to_folder = {
    '2022-05-27-The-Bochner-integral': 'Analysis on Banach spaces/Bochner_integral',
    '2023-01-29-PDE-1-Fourier': 'PDEs/1. The Fourier transform, tempered distributions and Sobolev spaces',
    '2023-01-29-PDE-1': 'PDEs/1. The Fourier transform, tempered distributions and Sobolev spaces',
    '2023-05-30-PDE-2-Hilbert': 'PDEs/2. What is a Hilbert space',
    '2023-07-12-PDEs-3-Sobolev_spaces': 'PDEs/3. Sobolev spaces',
    '2023-12-23-PDEs-4-Physical_derivation_of_parabolic_and_elliptic_PDE': 'PDEs/4. Physical derivation',
    '2024-02-27-PDEs-5-Fractional_Sobolev_spaces': 'PDEs/5. Fractional and negative order Sobolev spaces',
    '2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity': 'PDEs/6. Existence elliptic'
}

def get_target_tex(folder):
    if folder == 'index': return None
    path = os.path.join(search_dir, folder)
    if not os.path.exists(path): return None
    texs = [f for f in os.listdir(path) if f.endswith('.tex') and f != 'preamble.tex']
    for t in texs:
        with open(os.path.join(path, t), 'r', encoding='utf-8') as f:
            if r'\begin{document}' in f.read():
                return os.path.join(path, t)
    return os.path.join(path, texs[0]) if texs else None

# Load target files into memory
target_files = {} # path -> content
for folder in set(slug_to_folder.values()):
    tp = get_target_tex(folder)
    if tp:
        with open(tp, 'r', encoding='utf-8') as f:
            target_files[tp] = f.read()

def find_or_create_label(target_path, fragment):
    if not target_path or target_path not in target_files: return ""
    text = target_files[target_path]
    
    m = re.match(r'~:text=(.*)', fragment)
    if not m: return ""
    parts = m.group(1).split(',')
    
    first_term = urllib.parse.unquote(parts[0]).replace('-', ' ').strip()
    if not first_term: return ""
    
    # Try finding first term exactly
    idx = text.find(first_term)
    if idx == -1:
        # try case insensitive or partial
        first_term_short = first_term[:10]
        idx = text.find(first_term_short)
        if idx == -1: return ""
    
    # Check backwards for label
    label_start = text.rfind(r'\label{', max(0, idx-500), idx)
    if label_start != -1:
        end_brace = text.find('}', label_start)
        return text[label_start+7:end_brace]
        
    # Check forwards for label
    label_start2 = text.find(r'\label{', idx, idx+500)
    if label_start2 != -1:
        end_brace = text.find('}', label_start2)
        return text[label_start2+7:end_brace]

    # No label found -> create one!
    new_label = "auto-" + ''.join(c for c in first_term[:15].lower() if c in string.ascii_lowercase + string.digits) + "-" + str(uuid4())[:4]
    
    # Insert right before the found term
    new_text = text[:idx] + f"\\label{{{new_label}}}" + text[idx:]
    target_files[target_path] = new_text # Update in memory
    
    print(f"Injected \\label{{{new_label}}} into {os.path.basename(target_path)}")
    return new_label

# Maps (file, original_href) -> postref_string
url_to_postref = {}

for rep in replacements:
    original = rep['original']
    folder = rep['folder']
    link_text = rep['text']
    
    # Extract fragment
    m = re.match(r'https://nowheredifferentiable\.com/[^#]+#(.*)', original)
    fragment = m.group(1) if m else ""
    
    target_path = get_target_tex(folder) if folder != '?FOLDER?' else None
    
    label = ""
    if fragment:
        label = find_or_create_label(target_path, fragment)
    
    postref_str = f"\\postref{{{folder}}}{{{label}}}{{{link_text}}}"
    url_to_postref[(rep['file'], original)] = postref_str

# Apply replacements to source files
source_files = {} # path -> content

for (filepath, original_url), postref in url_to_postref.items():
    if filepath not in source_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            source_files[filepath] = f.read()
            
    # The original was inside an \href{original}{link_text}
    old_href = f"\\href{{{original_url}}}{{{next(r['text'] for r in replacements if r['file']==filepath and r['original']==original_url)}}}"
    
    # We should search for the exact match or roughly match
    # Because LaTeX might have newlines or spacing, we can just replace the url string and macro if it matches
    # but the simplest way is to regex the exact href block out.
    pattern = re.escape(r'\href{') + re.escape(original_url) + re.escape(r'}{') + r'([^}]*)' + re.escape(r'}')
    
    def replacer(match):
        return postref # ignoring captured linktext, we already embedded it in postref
        
    source_files[filepath] = re.sub(pattern, replacer, source_files[filepath])

# Write back source files
for filepath, content in source_files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Write back target files (that got labels injected)
for filepath, content in target_files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully processed {len(replacements)} replacements.")
