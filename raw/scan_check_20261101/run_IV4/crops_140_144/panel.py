"""Side-by-side panel of several regions (original strip pixel coordinates), same scale.
usage: python panel.py OUTNAME SCALE PAGE:STRIP:x0:y0:x1:y1 [...]"""
import sys
import pathlib
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
OUT = RUN / "crops_140_144"
name, scale = sys.argv[1], float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1 = (int(v) for v in spec.split(":"))
    im = Image.open(RUN / f"page_{p:03d}_s{s}.png").convert("L")
    c = im.crop((x0, y0, x1, y1))
    tiles.append(c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS))
gap = 20
w = sum(t.width for t in tiles) + gap * (len(tiles) - 1)
h = max(t.height for t in tiles)
panel = Image.new("L", (w, h), 255)
x = 0
for t in tiles:
    panel.paste(t, (x, 0))
    x += t.width + gap
panel.save(OUT / name)
print(OUT / name, panel.size)
