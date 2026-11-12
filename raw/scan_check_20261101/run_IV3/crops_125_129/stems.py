import sys
from PIL import Image

# usage: stems.py <page> <strip> <x0> <x1> <y> [thr]
# prints runs of dark pixels along row y (original pixels) between x0 and x1,
# averaged over rows y-3..y+3
page, strip = sys.argv[1], sys.argv[2]
x0, x1, y = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
for yy in range(y - 3, y + 4, 3):
    runs = []
    start = None
    for x in range(x0, x1):
        d = im.getpixel((x, yy)) < thr
        if d and start is None:
            start = x
        elif not d and start is not None:
            runs.append((start, x - start))
            start = None
    if start is not None:
        runs.append((start, x1 - start))
    print(yy, runs)
