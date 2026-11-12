import sys
from PIL import Image

# usage: ink.py src.png x0 y0 x1 y1 [thr]
# prints the dark-pixel count, the bounding box of dark pixels and the mean
# horizontal run length of dark pixels (a proxy for stem thickness).
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = 0
runs = []
minx, miny, maxx, maxy = w, h, -1, -1
for y in range(h):
    run = 0
    for x in range(w):
        if px[x, y] < thr:
            dark += 1
            run += 1
            minx = min(minx, x); maxx = max(maxx, x)
            miny = min(miny, y); maxy = max(maxy, y)
        else:
            if run:
                runs.append(run)
            run = 0
    if run:
        runs.append(run)
mean_run = sum(runs) / len(runs) if runs else 0
print('dark=%d bbox=(%d,%d,%d,%d) size=%dx%d mean_run=%.2f' % (
    dark, minx, miny, maxx, maxy, maxx - minx + 1, maxy - miny + 1, mean_run))
