from PIL import Image

RAMP = " .`:-=+*cs#%@"

def generate_ascii_svg(image_path="source-prepped.png", output_path="avi-ascii.svg", width=100):
    img = Image.open(image_path).convert("L")
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, height))
    pixels = img.load()
    lines = []
    for y in range(height):
        line = ""
        for x in range(width):
            val = pixels[x, y]
            char = RAMP[int((val / 255) * (len(RAMP) - 1))]
            line += "&amp;" if char == "&" else ("&lt;" if char == "<" else ("&gt;" if char == ">" else char))
        lines.append(line)

    line_height = 14
    svg_width = width * 7.2
    svg_height = height * line_height + 20
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">\n<style>text {{ font-family: monospace; font-size: 12px; fill: #8b949e; white-space: pre; }}</style>\n<rect width="100%" height="100%" fill="#0d1117" rx="6"/>\n'
    for i, line in enumerate(lines):
        y_pos = 20 + i * line_height
        svg += f'  <g clip-path="url(#clip-{i})"><text x="10" y="{y_pos}">{line}</text></g>\n'
        svg += f'  <clipPath id="clip-{i}"><rect x="0" y="{y_pos-12}" width="0" height="{line_height}"><animate attributeName="width" from="0" to="{svg_width}" dur="0.2s" begin="{i*0.05:.2f}s" fill="freeze" /></rect></clipPath>\n'
    svg += '</svg>'

    with open(output_path, "w") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_ascii_svg()