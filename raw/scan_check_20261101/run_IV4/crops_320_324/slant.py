"""Measure the slant of a single glyph (e.g. a parenthesis) in a strip.

Usage: python slant.py PAGE STRIP x0 y0 x1 y1
Prints the x-centroid of the ink in the top and bottom fifth of the glyph's
vertical extent, and their difference (positive = top leans right = italic).
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
im = Image.open(rf"{RUN}\page_{page}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < 128]
    if xs:
        rows.append((y, xs))
if not rows:
    print("no ink")
    sys.exit()
ytop, ybot = rows[0][0], rows[-1][0]
span = ybot - ytop + 1
band = max(1, span // 5)


def centroid(sel):
    pts = [x for (y, xs) in sel for x in xs]
    return sum(pts) / len(pts)


top = [r for r in rows if r[0] < ytop + band]
bot = [r for r in rows if r[0] > ybot - band]
ct, cb = centroid(top), centroid(bot)
print(f"height {span}px  top-centroid {ct:.1f}  bottom-centroid {cb:.1f}  lean {ct - cb:+.1f}px  ({(ct - cb) / span * 100:+.1f}% of height)")
