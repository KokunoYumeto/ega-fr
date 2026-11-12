"""stem.py PAGE STRIP x0 y0 x1 y1 : per-row lengths of the leftmost dark run (stem width) in the box, threshold 140."""
import sys
from PIL import Image
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
im = Image.open(f'user/Documents/ega_scan_check_20261101/run_IVback/page_{page}_s{strip}.png').convert('L')
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
rows = []
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < 140]
    if not xs:
        rows.append(None); continue
    start = xs[0]; n = 0
    x = start
    while x < w and px[x, y] < 140:
        n += 1; x += 1
    rows.append((start, n))
print([r[1] if r else 0 for r in rows])
vals = sorted(r[1] for r in rows if r)
if vals:
    mid = vals[len(vals)//4: 3*len(vals)//4]
    print('median stem', vals[len(vals)//2], 'interquartile', mid[:1], mid[-1:])
