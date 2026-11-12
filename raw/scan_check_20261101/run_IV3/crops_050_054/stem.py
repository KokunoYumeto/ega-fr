import sys
from PIL import Image
# usage: stem.py page strip x0 y0 x1 y1 : print dark-run lengths per row (threshold 128)
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png").convert("L")
for y in range(y0, y1):
    row = [im.getpixel((x, y)) < 128 for x in range(x0, x1)]
    runs = []; cur = 0; start=None
    for i, d in enumerate(row):
        if d:
            if cur == 0: start = i
            cur += 1
        elif cur:
            runs.append((start + x0, cur)); cur = 0
    if cur: runs.append((start + x0, cur))
    print(y, runs)
