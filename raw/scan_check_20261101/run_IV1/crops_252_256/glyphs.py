"""List connected ink components (glyphs) in a strip region, left to right.

Usage: python -I glyphs.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
Prints, for each component: bbox (in strip pixels), ink area, height,
and ink/height (an average horizontal stroke-width measure).
"""
import sys
from collections import deque
from PIL import Image

src, x0, y0, x1, y1 = sys.argv[1:6]
x0, y0, x1, y1 = (int(v) for v in (x0, y0, x1, y1))
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert("L")
W, H = x1 - x0, y1 - y0
px = im.load()
dark = [[px[x0 + i, y0 + j] < thr for i in range(W)] for j in range(H)]
seen = [[False] * W for _ in range(H)]
comps = []
for j in range(H):
    for i in range(W):
        if dark[j][i] and not seen[j][i]:
            q = deque([(i, j)])
            seen[j][i] = True
            pts = []
            while q:
                a, b = q.popleft()
                pts.append((a, b))
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < W and 0 <= d < H and dark[d][c] and not seen[d][c]:
                            seen[d][c] = True
                            q.append((c, d))
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            comps.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(pts)))
comps.sort()
for bx0, by0, bx1, by1, area in comps:
    if area < 4:
        continue
    h = by1 - by0 + 1
    w = bx1 - bx0 + 1
    print(f"x {bx0:5d}-{bx1:5d} y {by0:4d}-{by1:4d}  w {w:3d} h {h:3d}  ink {area:5d}  ink/h {area / h:6.2f}")
