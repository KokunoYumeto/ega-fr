import sys
from PIL import Image
import numpy as np
# usage: bbox.py src.png x0 y0 x1 y1 [threshold]
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
ink = im < thr
# connected components (4-neighbour) by simple flood fill
h, w = ink.shape
lab = np.zeros((h, w), int)
n = 0
comps = []
for yy in range(h):
    for xx in range(w):
        if ink[yy, xx] and lab[yy, xx] == 0:
            n += 1
            stack = [(yy, xx)]
            lab[yy, xx] = n
            pts = []
            while stack:
                a, b = stack.pop()
                pts.append((a, b))
                for da, db in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    c, d = a+da, b+db
                    if 0 <= c < h and 0 <= d < w and ink[c, d] and lab[c, d] == 0:
                        lab[c, d] = n
                        stack.append((c, d))
            ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
            comps.append((min(xs)+x0, min(ys)+y0, max(xs)+x0, max(ys)+y0, len(pts)))
comps.sort()
for c in comps:
    if c[4] >= 8:
        print('x %d-%d  y %d-%d  px %d' % (c[0], c[2], c[1], c[3], c[4]))
