import sys
from PIL import Image
import numpy as np
from collections import deque

# usage: cc.py page strip x0 y0 x1 y1 [thresh]
# lists connected components (dark pixels) inside the window: bbox (original coords), pixel count,
# mean horizontal run length (a stroke-width proxy)
run = r'user\Documents\ega_scan_check_20261101\run_IV4'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = np.array(Image.open(rf'{run}\page_{page:03d}_s{strip}.png').convert('L'))
w = im[y0:y1, x0:x1] < th
H, W = w.shape
seen = np.zeros_like(w, dtype=bool)
comps = []
for i in range(H):
    for j in range(W):
        if w[i, j] and not seen[i, j]:
            q = deque([(i, j)]); seen[i, j] = True; pts = []
            while q:
                a, b = q.popleft(); pts.append((a, b))
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        na, nb = a + da, b + db
                        if 0 <= na < H and 0 <= nb < W and w[na, nb] and not seen[na, nb]:
                            seen[na, nb] = True; q.append((na, nb))
            if len(pts) >= 15:
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                comps.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(pts), pts))
comps.sort()
for c in comps:
    bx0, by0, bx1, by1, n, pts = c
    # horizontal run lengths
    sub = np.zeros((by1 - by0 + 1, bx1 - bx0 + 1), dtype=bool)
    for a, b in pts:
        sub[a + y0 - by0, b + x0 - bx0] = True
    runs = []
    for row in sub:
        r = 0
        for v in row:
            if v: r += 1
            elif r: runs.append(r); r = 0
        if r: runs.append(r)
    vruns = []
    for col in sub.T:
        r = 0
        for v in col:
            if v: r += 1
            elif r: vruns.append(r); r = 0
        if r: vruns.append(r)
    print(f'bbox=({bx0},{by0})-({bx1},{by1}) size={bx1-bx0+1}x{by1-by0+1} pixels={n} '
          f'median_hrun={np.median(runs):.1f} median_vrun={np.median(vruns):.1f}')
