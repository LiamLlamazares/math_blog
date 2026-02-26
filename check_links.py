import os
import re
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin
from pathlib import Path
import time
import sys
from colorama import Fore, Style, init

init()

SITE_DIR = Path("_site")
SOURCE_DIR = Path("posts")

if not SITE_DIR.exists():
    print(Fore.RED + "Error: '_site' directory not found. Please run 'quarto render' first." + Style.RESET_ALL)
    exit(1)

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr, value in attrs:
                if attr == "href":
                    line, _ = self.getpos()
                    self.links.append((value, line))

def is_soft_404(html_content):
    """
    Checks if the HTML content corresponds to a 'soft 404' page 
    """
    html_lower = html_content.lower()
    not_found_phrases = [
        b"<title>page not found",
        b"<title>404",
        b"this page does not exist",
        b"404 not found",
        b"we couldn't find the page",
        b"page not found"
    ]
    for phrase in not_found_phrases:
        if phrase in html_lower[:10000]: 
            return True
    return False

def check_external_link(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status >= 400:
                return (False, f"HTTP {response.status}")
            
            content = response.read(10000)
            if is_soft_404(content):
                return (False, "Soft 404 (Page Not Found string detected)")
            
            return (True, "OK")
    except urllib.error.HTTPError as e:
        return (False, f"HTTP {e.code}")
    except urllib.error.URLError as e:
        return (False, f"Connection Error: {e.reason}")
    except Exception as e:
        return (False, f"Error: {e}")

def check_anchor_exists(filepath, anchor):
    """
    Parses a local HTML file and checks if an id="anchor" exists.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Simple regex to find id="anchor" or id='anchor'
            pattern = re.compile(rf'id=[\'"]{re.escape(anchor)}[\'"]')
            if pattern.search(content):
                return True
            return False
    except Exception:
        return False

def get_source_line(filepath, html_line_num):
    """
    Attempts to pull the corresponding line of text from the compiled HTML file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if 0 < html_line_num <= len(lines):
                return lines[html_line_num - 1].strip()
    except Exception:
        pass
    return "Could not retrieve source HTML context."

def check_links():
    print(f"Scanning '{SITE_DIR}' for broken HTML & \postref links...\n")
    
    html_files = list(SITE_DIR.rglob("*.html"))
    broken_links = []
    checked_external = {} 
    total_links = 0
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                content = f.read()
            except UnicodeDecodeError:
                continue
            
        parser = LinkExtractor()
        parser.feed(content)
        
        for href, line_num in parser.links:
            total_links += 1
            
            if href.startswith(('mailto:', 'tel:', 'javascript:', '#', 'data:')):
                # Check internal current-page anchors
                if href.startswith('#') and len(href) > 1:
                     anchor = href[1:]
                     if not check_anchor_exists(file_path, anchor):
                          broken_links.append({
                            'file': str(file_path.relative_to(SITE_DIR)),
                            'line': line_num,
                            'url': href,
                            'reason': f"Anchor '{href}' not found in file",
                            'context': get_source_line(file_path, line_num)
                        })
                continue
                
            # If external link
            if href.startswith(('http://', 'https://')):
                if href in checked_external:
                    success, reason = checked_external[href]
                else:
                    success, reason = check_external_link(href)
                    checked_external[href] = (success, reason)
                    time.sleep(0.05) 
                
                if not success:
                    broken_links.append({
                        'file': str(file_path.relative_to(SITE_DIR)),
                        'line': line_num,
                        'url': href,
                        'reason': reason,
                        'context': get_source_line(file_path, line_num)
                    })
                    print(Fore.RED + f"[BROKEN EXTERNAL] {href} -> {reason} (in {file_path.name}:{line_num})" + Style.RESET_ALL)
            else:
                # Internal link
                parts = href.split('#')
                clean_href = parts[0].split('?')[0]
                anchor = parts[1] if len(parts) > 1 else None

                if not clean_href:
                    continue
                
                if clean_href.startswith('/'):
                    target_path = SITE_DIR / clean_href.lstrip('/')
                else:
                    target_path = (file_path.parent / clean_href).resolve()
                
                if target_path.is_dir():
                    target_path = target_path / 'index.html'
                
                if not target_path.exists():
                    broken_links.append({
                        'file': str(file_path.relative_to(SITE_DIR)),
                        'line': line_num,
                        'url': href,
                        'reason': f"Local file '{target_path.name}' does not exist",
                        'context': get_source_line(file_path, line_num)
                    })
                    print(Fore.YELLOW + f"[BROKEN INTERNAL] {href} -> Missing file (in {file_path.name}:{line_num})" + Style.RESET_ALL)
                elif anchor:
                    # File exists, check the anchor inside the file
                    if not check_anchor_exists(target_path, anchor):
                        broken_links.append({
                            'file': str(file_path.relative_to(SITE_DIR)),
                            'line': line_num,
                            'url': href,
                            'reason': f"Anchor '#{anchor}' missing in target file '{target_path.name}'",
                            'context': get_source_line(file_path, line_num)
                        })
                        print(Fore.YELLOW + f"[BROKEN POSTREF/ANCHOR] {href} -> Missing anchor (in {file_path.name}:{line_num})" + Style.RESET_ALL)

    print("\n" + "="*70)
    print(Fore.CYAN + f"Scan complete! Checked {len(html_files)} HTML files and {total_links} links." + Style.RESET_ALL)
    
    if broken_links:
        print(Fore.RED + f"Found {len(broken_links)} broken links." + Style.RESET_ALL)
        with open("broken_links_report.md", "w", encoding='utf-8') as f:
            f.write(f"# Broken Links Report\n\nTotal Checked: {total_links} links across {len(html_files)} files.\n\n")
            for link in broken_links:
                f.write(f"### `{link['file']}` (Line {link['line']})\n")
                f.write(f"- **URL:** `{link['url']}`\n")
                f.write(f"- **Issue:** {link['reason']}\n")
                f.write(f"- **HTML Snippet:**\n```html\n{link['context']}\n```\n\n")
        print("\nSaved detailed report to 'broken_links_report.md'. Open this file to see exactly where the broken links are!")
        sys.exit(1)
    else:
        print(Fore.GREEN + "All links are alive and valid! 🎉" + Style.RESET_ALL)
        sys.exit(0)
        
if __name__ == "__main__":
    check_links()
