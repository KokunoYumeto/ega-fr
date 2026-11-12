"""Horizontal bars (dashes, minus signs, the bars of + and =) in a region of a strip.
python hbars.py PAGE STRIP X0 Y0 X1 Y1 [MINLEN] [THRESH]
Prints each bar as (x_start, length, first_row, last_row): runs of dark pixels at least MINLEN long that sit
on consecutive rows at the same x position (+-3 px)."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
minlen = int(sys.argv[7]) if len(sys.argv) > 7 else 14
th = int(sys.argv[8]) if len(sys.argv) > 8 else 128
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
px = im.load()
bars = []  # [xs, len, ystart, yend]
for y in range(y0, y1):
    x = x0
    while x < x1:
        if px[x, y] < th:
            s = x
            while x < x1 and px[x, y] < th:
                x += 1
            L = x - s
            if L >= minlen:
                for b in bars:
                    if abs(b[0] - s) <= 3 and abs(b[1] - L) <= 6 and b[3] == y - 1:
                        b[3] = y
                        break
                else:
                    bars.append([s, L, y, y])
        x += 1
for b in sorted(bars, key=lambda b: (b[2], b[0])):
    if b[3] - b[2] <= 6:  # thin bars only
        print(tuple(b))
