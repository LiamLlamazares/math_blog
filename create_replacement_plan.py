import os, re, json
import urllib.parse

search_dir = r'c:\Users\liaml\Documents\GitHub\Research\math_blog\posts'

slug_to_folder = {
    '2022-05-27-The-Bochner-integral': 'Analysis on Banach spaces/Bochner_integral',
    '2023-01-29-PDE-1-Fourier': 'PDEs/1. The Fourier transform, tempered distributions and Sobolev spaces',
    '2023-01-29-PDE-1': 'PDEs/1. The Fourier transform, tempered distributions and Sobolev spaces',
    '2023-05-30-PDE-2-Hilbert': 'PDEs/2. What is a Hilbert space',
    '2023-07-12-PDEs-3-Sobolev_spaces': 'PDEs/3. Sobolev spaces',
    '2023-12-23-PDEs-4-Physical_derivation_of_parabolic_and_elliptic_PDE': 'PDEs/4. Physical derivation',
    '2024-02-27-PDEs-5-Fractional_Sobolev_spaces': 'PDEs/5. Fractional and negative order Sobolev spaces',
    '2024-02-28-PDEs-6-Elliptic_PDE._Well_posedness_and_regularity': 'PDEs/6. Existence elliptic',
    'posts': 'index'
}

def get_target_tex(folder):
    if folder == 'index': return None
    path = os.path.join(search_dir, folder)
    texs = [f for f in os.listdir(path) if f.endswith('.tex') and f != 'preamble.tex']
    # return the file with \begin{document}
    for t in texs:
        with open(os.path.join(path, t), 'r', encoding='utf-8') as f:
            if r'\begin{document}' in f.read():
                return os.path.join(path, t)
    return os.path.join(path, texs[0]) if texs else None

# load all target tex contents
folder_contents = {}
for slug, folder in slug_to_folder.items():
    if folder == 'index': continue
    tex_path = get_target_tex(folder)
    if tex_path:
        with open(tex_path, 'r', encoding='utf-8') as f:
            folder_contents[folder] = f.read()

def find_label_for_fragment(folder, fragment):
    if folder not in folder_contents: return ""
    text = folder_contents[folder]
    
    # decode fragment
    # format: #:~:text=prefix-,start,end,-suffix or just #:~:text=start
    m = re.match(r'~:text=(.*)', fragment)
    if not m: return ""
    parts = m.group(1).split(',')
    search_terms = []
    for p in parts:
        term = urllib.parse.unquote(p)
        term = term.replace('-', ' ') # approximation
        search_terms.append(term.strip())
    
    # search for the first term in the tex document
    first_term = search_terms[0] if search_terms else ""
    if not first_term: return ""
    
    # simplistic finding:
    # try to find first_term
    idx = text.find(first_term)
    if idx == -1: return f"? ({first_term})"
    
    # look backwards for \label{
    label_start = text.rfind(r'\label{', 0, idx)
    if label_start != -1:
        # check if it's not too far (e.g. within 1000 chars)
        if idx - label_start < 1000:
            end_brace = text.find('}', label_start)
            return text[label_start+7:end_brace]
            
    # look forwards for \label{
    label_start2 = text.find(r'\label{', idx)
    if label_start2 != -1 and label_start2 - idx < 500:
        end_brace = text.find('}', label_start2)
        return text[label_start2+7:end_brace]

    return f"ADD_LABEL"

replacements = []

for root, _, files in os.walk(search_dir):
    for file in files:
        if file.endswith('.tex'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # find \href
            for url_match in re.finditer(r'\\href\{(https://nowheredifferentiable\.com/([^}#]*)/?(#[^}]*)?)\}\{([^}]*)\}', content):
                full_url = url_match.group(1)
                slug = url_match.group(2).strip('/')
                fragment = (url_match.group(3) or "").lstrip('#')
                link_text = url_match.group(4)
                
                if 'assets/code' in slug: continue
                
                folder = slug_to_folder.get(slug, '?FOLDER?')
                label = ""
                if fragment:
                    label = find_label_for_fragment(folder, fragment)
                
                replacements.append({
                    'file': filepath,
                    'original': full_url,
                    'folder': folder,
                    'label': label,
                    'text': link_text
                })

with open('c:/Users/liaml/Documents/GitHub/Research/math_blog/replacements.json', 'w') as f:
    json.dump(replacements, f, indent=2)

print(f"Proposed {len(replacements)} replacements.")
