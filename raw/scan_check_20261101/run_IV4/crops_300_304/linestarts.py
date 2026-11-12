"""Print the left and right ink edges of each text line of a strip (original pixels).

usage: python linestarts.py PAGE STRIP [THRESH]
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
page, strip = sys.argv[1], sys.argv[2]
th = int(sys.argv[3]) if len(sys.argv) > 3 else 128
im = Image.open(RUN + "page_%s_s%s.png" % (page, strip)).convert("L")
W, H = im.size
px = im.load()
# ignore the outer 150 px at both sides (scan margins)
X0, X1 = 150, W - 60
rows = []
for y in range(H):
    cnt = 0
    for x in range(X0, X1, 2):
        if px[x, y] < th:
            cnt += 1
    rows.append(cnt)
lines = []
y = 0
while y < H:
    if rows[y] > 2:
        y0 = y
        while y < H and rows[y] > 0:
            y += 1
        lines.append((y0, y - 1))
    y += 1
for (a, b) in lines:
    if b - a < 6:
        continue
    left, right = None, None
    for x in range(X0, X1):
        if any(px[x, yy] < th for yy in range(a, b + 1)):
            left = x
            break
    for x in range(X1 - 1, X0, -1):
        if any(px[x, yy] < th for yy in range(a, b + 1)):
            right = x
            break
    print("y %4d-%4d  left %4s  right %4s" % (a, b, left, right))
