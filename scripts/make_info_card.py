def generate_info_card(output_path="info-card.svg"):
    title = "adhiviraj@github ~ neofetch"
    rows = [
        ("OS", "Ubuntu 24.04 LTS x86_64"),
        ("Role", "ECE Undergrad & AI/ML Learner"),
        ("Stack", "Python, C++, React, FastAPI, PyTorch"),
        ("Focus", "Wafer Defect Detection & Computer Vision"),
        ("Goal", "SDE Internship & Open Source"),
    ]

    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 370" width="490" height="370">\n'
    svg += '<style>\n'
    svg += '  .bg { fill: #0d1117; rx: 6px; }\n'
    svg += '  .title { font-family: monospace; font-size: 14px; fill: #58a6ff; font-weight: bold; }\n'
    svg += '  .key { font-family: monospace; font-size: 12px; fill: #79c0ff; font-weight: bold; }\n'
    svg += '  .val { font-family: monospace; font-size: 12px; fill: #c9d1d9; }\n'
    svg += '  .line { opacity: 0; animation: fadeIn 0.4s ease-in forwards; }\n'
    svg += '  @keyframes fadeIn { to { opacity: 1; } }\n'
    svg += '</style>\n'
    svg += '<rect class="bg" width="100%" height="100%" />\n'
    svg += f'<text x="25" y="40" class="title">{title}</text>\n'
    svg += '<line x1="25" y1="52" x2="465" y2="52" stroke="#30363d" stroke-width="1" />\n'
    
    y = 90
    for i, (key, val) in enumerate(rows):
        delay = 0.2 + (i * 0.15)
        svg += f'<g class="line" style="animation-delay: {delay:.2f}s;">\n'
        svg += f'  <text x="25" y="{y}" class="key">{key}:</text>\n'
        svg += f'  <text x="110" y="{y}" class="val">{val}</text>\n'
        svg += f'</g>\n'
        y += 45

    svg += '</svg>'

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✅ Info Card generated successfully at {output_path}")

if __name__ == "__main__":
    generate_info_card()