"""List connected dark blobs in a region of a strip (bounding boxes, original pixels).

usage: python blobs.py PAGE STRIP x0 y0 x1 y1 [THRESH] [MINAREA]
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
minarea = int(sys.argv[8]) if len(sys.argv) > 8 else 3
im = Image.open(RUN + "page_%s_s%s.png" % (page, strip)).convert("L")
W, H = x1 - x0, y1 - y0
px = im.load()
dark = [[px[x0 + i, y0 + j] < th for i in range(W)] for j in range(H)]
seen = [[False] * W for _ in range(H)]
blobs = []
for j in range(H):
    for i in range(W):
        if dark[j][i] and not seen[j][i]:
            stack = [(i, j)]
            seen[j][i] = True
            xs, ys, n = [], [], 0
            while stack:
                a, b = stack.pop()
                xs.append(a); ys.append(b); n += 1
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < W and 0 <= d < H and dark[d][c] and not seen[d][c]:
                            seen[d][c] = True
                            stack.append((c, d))
            if n >= minarea:
                blobs.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, n))
blobs.sort()
for b in blobs:
    print("x %4d-%4d  y %4d-%4d  w %3d h %3d  area %5d" % (b[0], b[2], b[1], b[3], b[2] - b[0] + 1, b[3] - b[1] + 1, b[4]))
