"""For each text line in a strip, list the last few ink components (line end).

Usage: python -I line_ends.py <strip.png> [n_last] [threshold]
Lines are found from the horizontal ink projection. For each line the last
n components (left to right) are printed with bbox, ink area and size, so
that the final digit and period of index entries can be compared across lines.
"""
import sys
from collections import deque
from PIL import Image

src = sys.argv[1]
n_last = int(sys.argv[2]) if len(sys.argv) > 2 else 3
thr = int(sys.argv[3]) if len(sys.argv) > 3 else 128
im = Image.open(src).convert("L")
W, H = im.size
px = im.load()
rows = [sum(1 for x in range(W) if px[x, y] < thr) for y in range(H)]
bands = []
y = 0
while y < H:
    if rows[y] > 3:
        y0 = y
        while y < H and rows[y] > 0:
            y += 1
        if y - y0 > 8:
            bands.append((max(0, y0 - 2), min(H, y + 2)))
    y += 1


def components(x0, y0, x1, y1):
    w, h = x1 - x0, y1 - y0
    dark = [[px[x0 + i, y0 + j] < thr for i in range(w)] for j in range(h)]
    seen = [[False] * w for _ in range(h)]
    out = []
    for j in range(h):
        for i in range(w):
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
                            if 0 <= c < w and 0 <= d < h and dark[d][c] and not seen[d][c]:
                                seen[d][c] = True
                                q.append((c, d))
                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]
                if len(pts) >= 6:
                    out.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(pts)))
    out.sort()
    return out


for y0, y1 in bands:
    # restrict to the text block: ignore far-right specks by requiring
    # components of reasonable size
    comps = components(0, y0, W, y1)
    comps = [c for c in comps if c[4] >= 10]
    tail = comps[-n_last:]
    desc = "  ".join(f"[x{c[0]}-{c[2]} y{c[1]}-{c[3]} ink{c[4]}]" for c in tail)
    print(f"band y {y0}-{y1}: {desc}")
