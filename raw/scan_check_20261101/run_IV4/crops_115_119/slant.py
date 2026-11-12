import sys
from PIL import Image

# usage: slant.py src.png x0 y0 x1 y1 [thr]
# For a region holding one parenthesis: prints the mean x of the dark pixels in
# the top 15% and bottom 15% of its dark rows, and the shift per unit height
# (about 0 for an upright parenthesis, about 0.2 for an italic one).
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
rows = {}
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < thr]
    if xs:
        rows[y] = xs
if not rows:
    print('no ink'); sys.exit()
ys = sorted(rows)
top, bot = ys[0], ys[-1]
H = bot - top + 1
band = max(2, int(H * 0.15))
tx = [x for y in ys if y < top + band for x in rows[y]]
bx = [x for y in ys if y > bot - band for x in rows[y]]
mt = sum(tx) / len(tx)
mb = sum(bx) / len(bx)
print('height=%d top_mean_x=%.1f bottom_mean_x=%.1f shift/height=%.3f' % (H, mt, mb, (mt - mb) / H))
