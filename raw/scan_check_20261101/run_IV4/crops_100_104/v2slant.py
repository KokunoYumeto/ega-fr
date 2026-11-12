"""v2slant.py PAGE STRIP x0 y0 x1 y1 [THRESH]
Estimate the slant of a single glyph (e.g. a parenthesis) inside the given box (original pixel coordinates of
run_IV4/page_PAGE_sSTRIP.png): fits x = a*y + b to the per-row centroid of dark pixels; slant = -a
(positive = top leans right, as in italic)."""
import sys
import pathlib
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip = int(sys.argv[1]), sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < th]
    if xs:
        rows.append((y, sum(xs) / len(xs), min(xs), max(xs)))
if len(rows) < 3:
    print("too few dark rows")
    sys.exit()
n = len(rows)
my = sum(r[0] for r in rows) / n
mx = sum(r[1] for r in rows) / n
sxy = sum((r[0] - my) * (r[1] - mx) for r in rows)
syy = sum((r[0] - my) ** 2 for r in rows)
a = sxy / syy
top = rows[: max(1, n // 5)]
bot = rows[-max(1, n // 5):]
print(f"rows {n}, height {rows[-1][0]-rows[0][0]}, centroid-fit slant {-a:.3f}")
print("top rows (y, centroid, min, max):", [(r[0], round(r[1], 1), r[2], r[3]) for r in top[:4]])
print("bottom rows:", [(r[0], round(r[1], 1), r[2], r[3]) for r in bot[-4:]])
