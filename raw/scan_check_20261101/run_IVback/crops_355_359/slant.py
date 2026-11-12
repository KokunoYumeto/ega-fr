import sys
from PIL import Image
# usage: slant.py page strip x0 y0 x1 y1 -> for a single glyph in the box: x-centre of ink in top 15% and bottom 15% rows
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = "user/Documents/ega_scan_check_20261101/run_IVback"
im = Image.open(f"{base}/page_{page}_s{strip}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
rows = []
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < 128]
    if xs:
        rows.append((y, xs))
if not rows:
    print("no ink"); sys.exit()
top, bot = rows[0][0], rows[-1][0]
H = bot - top + 1
k = max(2, int(H * 0.15))
def cen(sel):
    xs = [x for (y, r) in sel for x in r]
    return sum(xs) / len(xs)
t = cen([r for r in rows if r[0] < top + k])
b = cen([r for r in rows if r[0] > bot - k])
mid = cen([r for r in rows if abs(r[0] - (top + bot) / 2) < k / 2 + 1])
print(f"height {H}  top-x {t:.1f}  mid-x {mid:.1f}  bottom-x {b:.1f}  top-bottom {t-b:+.1f}  bulge(mid-avg) {mid-(t+b)/2:+.1f}")
