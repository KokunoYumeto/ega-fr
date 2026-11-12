"""Stack several enlarged strip regions into one labelled contact sheet.

Usage: python sheet.py OUTNAME SCALE "PAGE STRIP X0 Y0 X1 Y1" ...
Coordinates are in the 2000-px-wide display frame of each strip.
"""
import sys
from PIL import Image, ImageDraw

out_name = sys.argv[1]
scale = float(sys.argv[2])
specs = sys.argv[3:]
tiles = []
for spec in specs:
    page, strip, x0, y0, x1, y1 = spec.split()
    page, strip = int(page), int(strip)
    src = f"user/Documents/ega_scan_check_20261101/run_IV2/page_{page:03d}_s{strip}.png"
    im = Image.open(src).convert("L")
    f = im.size[0] / 2000.0
    box = tuple(int(round(float(v) * f)) for v in (x0, y0, x1, y1))
    c = im.crop(box)
    c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
    tiles.append((f"p{page} s{strip} {x0},{y0}", c))
width = max(t[1].size[0] for t in tiles)
height = sum(t[1].size[1] + 22 for t in tiles)
sheet = Image.new("L", (width, height), 255)
draw = ImageDraw.Draw(sheet)
y = 0
for label, c in tiles:
    draw.text((4, y + 4), label, fill=0)
    y += 22
    sheet.paste(c, (0, y))
    y += c.size[1]
out = f"user/Documents/ega_scan_check_20261101/run_IV2/crops_150_154/{out_name}.png"
sheet.save(out)
print(out, sheet.size)
