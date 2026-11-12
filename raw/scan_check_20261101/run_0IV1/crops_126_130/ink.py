import sys, os
from PIL import Image
run = r"user\Documents\ega_scan_check_20261101\run_0IV1"
# usage: ink.py label page strip x0 y0 x1 y1 ... -> tight bbox of dark pixels and dark count (threshold 128)
a = sys.argv[1:]
for i in range(0, len(a), 7):
    label, p, s, x0, y0, x1, y1 = a[i:i+7]
    im = Image.open(os.path.join(run, f"page_{int(p):03d}_s{s}.png")).convert("L")
    px = im.load(); x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
    pts = [(x, y) for y in range(y0, y1) for x in range(x0, x1) if px[x, y] < 128]
    if not pts: print(label, "none"); continue
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    w = max(xs)-min(xs)+1; h = max(ys)-min(ys)+1
    print(f"{label:10s} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)}) w={w} h={h} dark={len(pts)} density={len(pts)/(w*h):.3f}")
