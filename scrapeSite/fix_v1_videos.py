import os

html_file = "v1/index.html"
if not os.path.exists(html_file):
    print(f"Error: {html_file} not found.")
    exit(1)

with open(html_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

videos = [
    ("3MpcsgzQGE0", 1725),
    ("ub6Bk-nlje8", 1733),
    ("ZOd4APGKdH0", 1741),
    ("p2jKh8yj160", 1749)
]

for video_id, line_num in videos:
    idx = line_num - 1
    if idx < len(lines):
        orig = lines[idx]
        if "elementor-video" in orig:
            print(f"Replacing video {video_id} on line {line_num}")
            # Identify leading whitespace
            leading = orig[:orig.find("<")]
            new_content = f'{leading}<div class="elementor-video">\n'
            new_content += f'{leading}  <iframe \n'
            new_content += f'{leading}    src="https://www.youtube-nocookie.com/embed/{video_id}?rel=0&autoplay=0"\n'
            new_content += f'{leading}    width="100%" height="315"\n'
            new_content += f'{leading}    frameborder="0"\n'
            new_content += f'{leading}    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope"\n'
            new_content += f'{leading}    allowfullscreen>\n'
            new_content += f'{leading}  </iframe>\n'
            new_content += f'{leading}</div> </div>\n'
            lines[idx] = new_content
        else:
            print(f"Warning: 'elementor-video' not found on line {line_num}. Content: {repr(orig)}")
    else:
        print(f"Error: Line {line_num} out of range.")

with open(html_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Done — v1 YouTube embeds fixed")
