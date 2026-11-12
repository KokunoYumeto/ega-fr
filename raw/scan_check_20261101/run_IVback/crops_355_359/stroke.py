import sys
from PIL import Image
# usage: stroke.py page strip x0 y0 x1 y1  -> per row max horizontal dark run (original px), and ink count
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = "user/Documents/ega_scan_check_20261101/run_IVback"
im = Image.open(f"{base}/page_{page}_s{strip}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
ink = 0
runs = []
for y in range(h):
    best = cur = 0
    for x in range(w):
        if px[x, y] < 128:
            cur += 1
            ink += 1
            best = max(best, cur)
        else:
            cur = 0
    runs.append(best)
print("size", w, h, "ink", ink, "max run", max(runs), "median run of nonzero rows",
      sorted(r for r in runs if r)[len([r for r in runs if r]) // 2] if any(runs) else 0)
