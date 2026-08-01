import os

def generate_info_card(output_path="info-card.svg"):
    title = "adhiviraj@github ~ neofetch"
    rows = [
        ("OS", "Ubuntu 24.04 LTS x86_64"),
        ("Role", "ECE Undergrad & AI/ML Learner"),
        ("Stack", "Python, C++, React, FastAPI, PyTorch"),
        ("Focus", "Wafer Defect Detection & Algorithmic Optimization"),
        ("Goal", "SDE Internship & Open Source Contributions"),
    ]

    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 370" width="490" height="370">\n<style>.bg { fill: #0d1117; rx: 6px; } .title { font-family: monospace; font-size: 14px; fill: #58a6ff; font-weight: bold; } .key { font-family: monospace; font-size: 12px; fill: #79c0ff; font-weight: bold; } .val { font-family: monospace; font-size: 12px; fill: #c9d1d9; } .line { opacity: 0; animation: fadeIn 0.3s forwards; } @keyframes fadeIn { to { opacity: 1; } }</style>\n<rect class="bg" width="100%" height="100%" />\n'
    svg += f'<text x="20" y="35" class="title">{title}</text>\n<line x1="20" y1="45" x2="470" y2="45" stroke="#30363d" stroke-width="1" />\n'
    y = 75
    for i, (key, val) in enumerate(rows):
        svg += f'<g class="line" style="animation-delay: {0.2 + (i * 0.15):.2f}s;"><text x="20" y="{y}" class="key">{key}:</text><text x="100" y="{y}" class="val">{val}</text></g>\n'
        y += 45
    svg += '</svg>'

    with open(output_path, "w") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_info_card()