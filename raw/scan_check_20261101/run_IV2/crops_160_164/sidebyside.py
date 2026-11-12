"""Put glyph crops (original pixel boxes) side by side at the same zoom.
usage: python sidebyside.py NAME ZOOM PAGE:STRIP:X0:Y0:X1:Y1 [...]"""
import pathlib
import sys

from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
name, zoom = sys.argv[1], int(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1 = (int(v) for v in spec.split(":"))
    im = Image.open(RUN / f"page_{p:03d}_s{s}.png").convert("L")
    c = im.crop((x0, y0, x1, y1))
    tiles.append(c.resize((c.width * zoom, c.height * zoom), Image.NEAREST))
W = sum(t.width for t in tiles) + 20 * (len(tiles) - 1)
H = max(t.height for t in tiles)
out = Image.new("L", (W, H), 255)
x = 0
for t in tiles:
    out.paste(t, (x, 0))
    x += t.width + 20
out.save(RUN / "crops_160_164" / f"{name}.png")
print(out.size)
