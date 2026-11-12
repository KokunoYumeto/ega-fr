"""Print a thresholded ASCII map of a strip region (original pixels).

Usage: python ascii.py PAGE STRIP X0 Y0 X1 Y1 [THRESH]
"""
import sys
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(run / f"page_{page:03d}_s{strip}.png").convert("L")
for y in range(y0, y1):
    row = "".join("#" if im.getpixel((x, y)) < th else "." for x in range(x0, x1))
    runs = []
    cnt = 0
    for ch in row:
        if ch == "#":
            cnt += 1
        elif cnt:
            runs.append(cnt)
            cnt = 0
    if cnt:
        runs.append(cnt)
    print(f"{y:4d} {row} {runs}")
