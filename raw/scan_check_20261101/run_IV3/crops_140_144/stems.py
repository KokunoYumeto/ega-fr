"""stems.py PAGE STRIP X0 Y0 X1 Y1: print the dark-pixel count and the horizontal run lengths of dark pixels (stem widths) along the middle rows of the box."""
import sys, pathlib
from PIL import Image
run = pathlib.Path(__file__).parent.parent
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png").convert("L").crop((int(x0), int(y0), int(x1), int(y1)))
w, h = im.size
px = im.load()
dark = sum(1 for y in range(h) for x in range(w) if px[x, y] < 128)
print("box", w, "x", h, "dark", dark)
for y in range(h // 3, 2 * h // 3, max(1, h // 12)):
    runs, cur = [], 0
    for x in range(w):
        if px[x, y] < 128:
            cur += 1
        elif cur:
            runs.append(cur); cur = 0
    if cur: runs.append(cur)
    print(y, runs)
