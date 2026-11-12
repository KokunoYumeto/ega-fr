"""bars.py STRIP x0 y0 x1 y1: list horizontal dark runs (thin bars: = signs, dashes, minus) in a region, in original pixels."""
import sys
from PIL import Image

src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
im = Image.open(src).convert("L")
px = im.load()
runs = []
for y in range(y0, y1):
    x = x0
    while x < x1:
        if px[x, y] < 110:
            s = x
            while x < x1 and px[x, y] < 110:
                x += 1
            if x - s >= 20:
                runs.append((y, s, x - s))
        x += 1
# merge rows belonging to the same bar (same start within 3 px, consecutive y)
bars = []
for y, s, L in runs:
    for b in bars:
        if abs(b["s"] - s) <= 4 and y - b["y1"] <= 1:
            b["y1"] = y
            b["L"] = max(b["L"], L)
            break
    else:
        bars.append({"y0": y, "y1": y, "s": s, "L": L})
for b in bars:
    print(f"y {b['y0']}-{b['y1']}  x {b['s']}  len {b['L']}  thick {b['y1'] - b['y0'] + 1}")
