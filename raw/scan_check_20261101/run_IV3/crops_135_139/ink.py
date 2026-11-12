import sys
from PIL import Image
import numpy as np
# usage: ink.py src.png x0 y0 x1 y1 [thr]
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
b = im < thr
# connected components (4-neighbour) via simple flood fill
h, w = b.shape
lab = np.zeros((h, w), int)
comps = []
cur = 0
for i in range(h):
    for j in range(w):
        if b[i, j] and not lab[i, j]:
            cur += 1
            stack = [(i, j)]
            lab[i, j] = cur
            pts = []
            while stack:
                a, c = stack.pop()
                pts.append((a, c))
                for da, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    na, nc = a+da, c+dc
                    if 0 <= na < h and 0 <= nc < w and b[na, nc] and not lab[na, nc]:
                        lab[na, nc] = cur
                        stack.append((na, nc))
            ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
            # mean horizontal run length
            sub = (lab[min(ys):max(ys)+1, min(xs):max(xs)+1] == cur)
            runs = []
            for row in sub:
                r = 0
                for v in row:
                    if v: r += 1
                    elif r: runs.append(r); r = 0
                if r: runs.append(r)
            comps.append((min(xs)+x0, min(ys)+y0, max(xs)+x0, max(ys)+y0, len(pts), sum(runs)/len(runs) if runs else 0))
for c in sorted(comps):
    if c[4] > 20:
        print('bbox x%d-%d y%d-%d  px=%d  meanrun=%.1f' % (c[0], c[2], c[1], c[3], c[4], c[5]))
