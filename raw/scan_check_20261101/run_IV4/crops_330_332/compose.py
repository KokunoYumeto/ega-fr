"""Compose several boxes (page, strip, x0, y0, x1, y1) side by side at one scale.

Usage: python compose.py NAME SCALE page:strip:x0:y0:x1:y1 [...]
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
name, scale = sys.argv[1], float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    page, strip, x0, y0, x1, y1 = spec.split(":")
    im = Image.open(rf"{RUN}\page_{page}_s{strip}.png").convert("L")
    b = tuple(int(v) for v in (x0, y0, x1, y1))
    c = im.crop(b)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    tiles.append(c)
W = sum(t.width for t in tiles) + 24 * (len(tiles) - 1)
H = max(t.height for t in tiles)
out = Image.new("L", (W, H), 170)
x = 0
for t in tiles:
    out.paste(t, (x, 0))
    x += t.width + 24
out.save(rf"{RUN}\crops_330_332\{name}.png")
print(out.size)
