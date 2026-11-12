import sys
sys.dont_write_bytecode = True
from PIL import Image

# usage: ink.py page strip x0 y0 x1 y1 [thr]
# prints the count of dark pixels and the bounding box of dark pixels in the region
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
n = 0
xs, ys = [], []
for y in range(h):
    for x in range(w):
        if px[x, y] < thr:
            n += 1
            xs.append(x)
            ys.append(y)
if n:
    bw, bh = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
    print(f"dark={n} bbox=({min(xs)+x0},{min(ys)+y0})-({max(xs)+x0},{max(ys)+y0}) size={bw}x{bh} density={n/(bw*bh):.3f}")
else:
    print("no dark pixels")
