import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap(json_path="data/contributions.json", output_path="contrib-heatmap.svg"):
    with open(json_path, "r") as f:
        data = json.load(f)
    days = data["days"]
    box_size, gap = 11, 3
    svg_width, svg_height = 53 * (box_size + gap) + 40, 7 * (box_size + gap) + 50

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">\n<style>.bg {{ fill: #0d1117; rx: 6px; }} .box {{ animation: slideIn 0.3s ease-out forwards; opacity: 0; }} @keyframes slideIn {{ to {{ opacity: 1; }} }} text {{ font-family: monospace; font-size: 11px; fill: #8b949e; }}</style>\n<rect class="bg" width="{svg_width}" height="{svg_height}" />\n<g transform="translate(20, 20)">\n'
    for idx, day in enumerate(days):
        col, row = idx // 7, idx % 7
        svg += f'  <rect class="box" x="{col * (box_size + gap)}" y="{row * (box_size + gap)}" width="{box_size}" height="{box_size}" rx="2" fill="{PALETTE[min(day["level"], 5)]}" style="animation-delay: {(col + row) * 0.015:.3f}s;" />\n'
    svg += f'</g>\n<text x="20" y="{svg_height - 12}">Live Contribution Graph • {len(days)} days tracked</text>\n</svg>'

    with open(output_path, "w") as f:
        f.write(svg)

if __name__ == "__main__":
    render_heatmap()