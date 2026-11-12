import sys
from PIL import Image

# usage: stems.py <page> <strip> <x0> <y0> <x1> <y1>
# prints dark-run widths along several horizontal scanlines in the box (original pixels)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
for y in range(y0, y1, max(1, (y1 - y0) // 8)):
    runs = []
    x = x0
    while x < x1:
        if im.getpixel((x, y)) < thr:
            s = x
            while x < x1 and im.getpixel((x, y)) < thr:
                x += 1
            runs.append((s, x - s))
        else:
            x += 1
    print(y, runs)
