"""Put several small strip regions side by side (same scale) for a visual weight comparison.

usage: python compare.py OUTNAME SCALE PAGE:STRIP:X0:Y0:X1:Y1 [...]
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
out, scale = sys.argv[1], float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1 = (int(v) for v in spec.split(":"))
    im = Image.open(RUN / f"page_{p:03d}_s{s}.png").convert("L").crop((x0, y0, x1, y1))
    tiles.append(im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS))
W = sum(t.width for t in tiles) + 20 * (len(tiles) + 1)
H = max(t.height for t in tiles) + 40
canvas = Image.new("L", (W, H), 255)
x = 20
d = ImageDraw.Draw(canvas)
for i, t in enumerate(tiles):
    canvas.paste(t, (x, 30))
    d.text((x, 5), str(i + 1), fill=0)
    x += t.width + 20
canvas.save(RUN / "crops_145_149" / out)
print(RUN / "crops_145_149" / out, canvas.size)
