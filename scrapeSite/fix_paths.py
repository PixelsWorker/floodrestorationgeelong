import os
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Define paths
file_path = "v2/index.html"
source_domain = "floodrestorationgeelong.au"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found. Running from: {os.getcwd()}")
    exit(1)

print(f"Opening {file_path} for robust localization...")
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

def get_local_filename(url):
    if not url or source_domain not in url:
        return url
    
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    
    # If it's a page link (no extension), point it to index.html for local prototyping
    if not filename or "." not in filename:
        return "index.html"
    
    # Files downloaded into v2 often keep their query string in the filename
    if parsed.query:
        filename = f"{filename}?{parsed.query}"
    
    return filename

def process_srcset(srcset_val):
    if not srcset_val:
        return srcset_val
    # srcset is a comma-separated list of "url size, url size"
    parts = []
    for part in srcset_val.split(','):
        subparts = part.strip().split()
        if subparts:
            # First part is the URL
            subparts[0] = get_local_filename(subparts[0])
            parts.append(" ".join(subparts))
    return ", ".join(parts)

# 1. Fix standard attributes
print("Fixing src, href, and data attributes...")
attrs_to_fix = [
    'src', 'href', 'data-rocket-src', 'data-lazy-src', 'data-src', 
    'data-css-url', 'data-gtm-src', 'data-as', 'data-rocket-preload',
    'data-lazy-srcset', 'data-lazy-sizes', 'srcset', 'imagesrcset'
]

for tag in soup.find_all(True):
    for attr in attrs_to_fix:
        if tag.has_attr(attr):
            if 'srcset' in attr:
                tag[attr] = process_srcset(tag[attr])
            else:
                tag[attr] = get_local_filename(tag[attr])

# 2. Fix Meta tags (og:image, etc.)
print("Fixing meta tag content...")
for meta in soup.find_all("meta", content=True):
    if source_domain in meta['content']:
        meta['content'] = get_local_filename(meta['content'])

# 3. Handle inline styles with url()
print("Fixing inline style backgrounds...")
for tag in soup.find_all(style=True):
    style = tag['style']
    def replace_url(match):
        url = match.group(1).strip("'\"")
        return f'url("{get_local_filename(url)}")'
    tag['style'] = re.sub(r'url\(([^)]+)\)', replace_url, style)

# 4. Final Cleanup: Ensure any remaining absolute links to the domain point to index.html
print("Cleaning up remaining domain links...")
for a in soup.find_all("a", href=True):
    if source_domain in a['href']:
        parsed = urlparse(a['href'])
        filename = os.path.basename(parsed.path)
        if not filename or "." not in filename:
            a['href'] = "index.html"
        else:
            a['href'] = filename

# Convert soup back to string for global replacement fallback
html_out = soup.prettify()

# 5. Global Replacement Fallback (for JSON, JS strings, or attributes missed by BS4)
print("Applying global domain replacement fallout...")
def global_path_fix(match):
    full_url = match.group(0)
    return get_local_filename(full_url)

# Regex for URLs on our domain - using double quotes for pattern and correctly handling quotes
domain_regex = rf"https?://{source_domain}[^\"'\s>]*"
html_out = re.sub(domain_regex, global_path_fix, html_out)

# Save results
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_out)

print("Done! All assets in v2/index.html are now strictly local.")
