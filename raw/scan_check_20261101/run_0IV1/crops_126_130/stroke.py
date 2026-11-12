import sys, os
from PIL import Image
import statistics
run = r"user\Documents\ega_scan_check_20261101\run_0IV1"
# usage: stroke.py label page strip x0 y0 x1 y1 ...  -> median/mean horizontal and vertical dark-run lengths
args = sys.argv[1:]
i = 0
while i < len(args):
    label, page, strip, x0, y0, x1, y1 = args[i:i+7]; i += 7
    im = Image.open(os.path.join(run, f"page_{int(page):03d}_s{strip}.png")).convert("L")
    x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
    px = im.load()
    hr = []
    for y in range(y0, y1):
        r = 0
        for x in range(x0, x1 + 1):
            d = x < x1 and px[x, y] < 128
            if d: r += 1
            elif r: hr.append(r); r = 0
    vr = []
    for x in range(x0, x1):
        r = 0
        for y in range(y0, y1 + 1):
            d = y < y1 and px[x, y] < 128
            if d: r += 1
            elif r: vr.append(r); r = 0
    dark = sum(1 for y in range(y0, y1) for x in range(x0, x1) if px[x, y] < 128)
    hr2 = [h for h in hr if h >= 2]
    print(f"{label:12s} hruns n={len(hr2):4d} median={statistics.median(hr2) if hr2 else 0:5.1f} mean={statistics.mean(hr2) if hr2 else 0:5.2f}  dark={dark}")
