"""Stack several crops (same scale) vertically into one image for side-by-side comparison.

Usage: python montage.py OUTNAME SCALE page:strip:x0:y0:x1:y1 [...]
"""
import sys
from PIL import Image, ImageDraw

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\crops_145_149"

name = sys.argv[1]
scale = float(sys.argv[2])
crops = []
for spec in sys.argv[3:]:
    page, strip, x0, y0, x1, y1 = spec.split(":")
    im = Image.open(rf"{RUN}\page_{page}_s{strip}.png").convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    crops.append((spec, c))
W = max(c.width for _, c in crops) + 10
H = sum(c.height + 22 for _, c in crops)
canvas = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(canvas)
y = 0
for i, (spec, c) in enumerate(crops):
    d.text((2, y + 2), f"{i}: {spec}", fill=0)
    canvas.paste(c, (5, y + 20))
    y += c.height + 22
canvas.save(rf"{OUT}\{name}.png")
print(canvas.size)
