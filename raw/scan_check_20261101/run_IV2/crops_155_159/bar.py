"""Longest horizontal run of dark pixels inside a box (to compare dash, minus and = bar lengths).
usage: python bar.py PAGE STRIP x0 y0 x1 y1 [threshold]   (original strip pixels)"""
import sys
from PIL import Image

d = r"user\Documents\ega_scan_check_20261101\run_IV2"
p, s, x0, y0, x1, y1 = sys.argv[1:7]
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(rf"{d}\page_{int(p):03d}_s{s}.png").convert("L")
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
best = []
for y in range(y0, y1):
    run = 0
    start = None
    for x in range(x0, x1):
        if im.getpixel((x, y)) < th:
            run += 1
            if run == 1:
                start = x
            if run > 0:
                best.append((run, y, start))
        else:
            run = 0
best.sort(reverse=True)
seen = set()
out = []
for r, y, st in best:
    if (y, st) in seen:
        continue
    seen.add((y, st))
    out.append((r, y, st))
    if len(out) >= 6:
        break
print(out)
