import sys, os
from PIL import Image
run = r"user\Documents\ega_scan_check_20261101\run_0IV1"
# usage: rows.py page strip x0 x1 y0 y1 : print dark runs per row as text art
p, s, x0, x1, y0, y1 = sys.argv[1:7]
im = Image.open(os.path.join(run, f"page_{int(p):03d}_s{s}.png")).convert("L")
px = im.load()
for y in range(int(y0), int(y1)):
    print(f"{y:4d} " + "".join("#" if px[x, y] < 128 else "." for x in range(int(x0), int(x1))))
