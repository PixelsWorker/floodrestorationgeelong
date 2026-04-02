import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://floodrestorationgeelong.au/"

# 1. Create local folders for CSS and JS
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)

print("Fetching homepage...")
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. IMAGES: Force them to use the absolute main link
print("Updating image tags...")
for img in soup.find_all("img"):
    if img.get("src"):
        # Converts "/wp-content/uploads/image.jpg" to "https://floodrestorationgeelong.au/wp-content/uploads/image.jpg"
        img["src"] = urljoin(base_url, img["src"])
    
    # We delete 'srcset' if it exists so the browser doesn't try to use relative thumbnail paths
    if img.get("srcset"):
        del img["srcset"]

# 3. CSS: Download and link locally
print("Downloading CSS...")
for i, link in enumerate(soup.find_all("link", rel="stylesheet")):
    if link.get("href"):
        css_url = urljoin(base_url, link["href"])
        
        # Create a safe filename
        filename = css_url.split("/")[-1].split("?")[0]
        if not filename.endswith(".css"): 
            filename = f"style_{i}.css"
            
        css_path = os.path.join("css", filename)
            
        try:
            css_content = requests.get(css_url).text
            with open(css_path, "w", encoding="utf-8") as f:
                f.write(css_content)
            # Update the HTML to point to your new local CSS file
            link["href"] = css_path 
        except:
            print(f"Skipped a CSS file: {css_url}")

# 4. JS: Download and link locally
print("Downloading JS...")
for i, script in enumerate(soup.find_all("script", src=True)):
    js_url = urljoin(base_url, script["src"])
    
    # Create a safe filename
    filename = js_url.split("/")[-1].split("?")[0]
    if not filename.endswith(".js"): 
        filename = f"script_{i}.js"
        
    js_path = os.path.join("js", filename)

    try:
        js_content = requests.get(js_url).text
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        # Update the HTML to point to your new local JS file
        script["src"] = js_path 
    except:
        print(f"Skipped a JS file: {js_url}")

# 5. Save the final HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Done! You now have the HTML, CSS, and JS locally, with images pointing to the live site.")
