from PIL import Image

# Refined brightness ramp: dark (dense) -> bright (spaces/light)
RAMP = "@%#*+=-:. "

def generate_ascii_svg(image_path="source-prepped.png", output_path="avi-ascii.svg", width=72):
    try:
        img = Image.open(image_path).convert("L")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.52)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    pixels = img.load()
    lines = []
    for y in range(height):
        line = ""
        for x in range(width):
            val = pixels[x, y]
            # Map dark pixels to dense characters, bright to sparse
            char = RAMP[int((val / 255) * (len(RAMP) - 1))]
            line += "&amp;" if char == "&" else ("&lt;" if char == "<" else ("&gt;" if char == ">" else char))
        lines.append(line)

    line_height = 14
    char_width = 7.5
    svg_width = int(width * char_width) + 20
    svg_height = height * line_height + 20
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="370" height="370">\n'
    svg += '<style>\n'
    svg += '  text { font-family: "Courier New", Courier, monospace; font-size: 11px; fill: #58a6ff; white-space: pre; font-weight: bold; }\n'
    svg += '</style>\n'
    svg += f'<rect width="100%" height="100%" fill="#0d1117" rx="6"/>\n'

    for i, line in enumerate(lines):
        y_pos = 20 + i * line_height
        svg += f'  <g clip-path="url(#clip-{i})"><text x="10" y="{y_pos}">{line}</text></g>\n'
        svg += f'  <clipPath id="clip-{i}"><rect x="0" y="{y_pos-12}" width="0" height="{line_height}"><animate attributeName="width" from="0" to="{svg_width}" dur="0.15s" begin="{i*0.04:.2f}s" fill="freeze" /></rect></clipPath>\n'
    svg += '</svg>'

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✅ ASCII SVG generated successfully at {output_path}")

if __name__ == "__main__":
    generate_ascii_svg()