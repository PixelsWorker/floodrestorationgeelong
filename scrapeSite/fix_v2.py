import os, re

v2_dir = "v2"
html_file = os.path.join(v2_dir, "index.html")

if not os.path.exists(html_file):
    print(f"Error: {html_file} not found. Running from: {os.getcwd()}")
    exit(1)

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Rename all files with ?... in their name and fix references
for fname in os.listdir(v2_dir):
    if "?" in fname:
        safe_name = fname.split("?")[0]
        # avoid collision
        src = os.path.join(v2_dir, fname)
        dst = os.path.join(v2_dir, safe_name)
        if not os.path.exists(dst):
            print(f"Renaming {fname} to {safe_name}")
            os.rename(src, dst)
        else:
            print(f"Skipping rename for {fname} (destination already exists)")
        
        # fix reference in html (both encoded and raw forms)
        html = html.replace(fname, safe_name)
        html = html.replace(fname.replace("?", "%3F").replace("&", "%26"), safe_name)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Done — v2 fixed")
