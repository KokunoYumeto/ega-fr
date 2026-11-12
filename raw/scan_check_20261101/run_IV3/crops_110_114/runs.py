import sys
from PIL import Image
# usage: runs.py page strip x0 y0 x1 y1 : print dark-run lengths per row (threshold 128) inside the box, original pixels
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
for y in range(y0, y1):
    runs = []
    n = 0
    for x in range(x0, x1):
        if im.getpixel((x, y)) < 128:
            n += 1
        elif n:
            runs.append(n); n = 0
    if n:
        runs.append(n)
    print(y, runs)
