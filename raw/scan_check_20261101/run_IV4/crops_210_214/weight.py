"""Median dark-run width (stroke weight proxy) over the middle rows of the x-height band of a word box.
usage: python weight.py page strip x0 y0 x1 y1 [threshold]"""
import statistics
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(r'user/Documents/ega_scan_check_20261101/run_IV4/page_%03d_s%d.png' % (page, strip)).convert('L')
rows = []
for y in range(y0, y1):
    dark = sum(1 for x in range(x0, x1) if im.getpixel((x, y)) < th)
    rows.append((y, dark))
# x-height band: rows whose dark count exceeds 40% of the maximum
mx = max(d for _, d in rows)
band = [y for y, d in rows if d > 0.4 * mx]
lo, hi = band[0], band[-1]
mid = range(lo + (hi - lo) // 3, hi - (hi - lo) // 3 + 1)
runs = []
for y in mid:
    x = x0
    while x < x1:
        if im.getpixel((x, y)) < th:
            s = x
            while x < x1 and im.getpixel((x, y)) < th:
                x += 1
            runs.append(x - s)
        else:
            x += 1
total_dark = sum(1 for y in range(lo, hi + 1) for x in range(x0, x1) if im.getpixel((x, y)) < th)
print(f"band {lo}-{hi}, rows used {len(mid)}, runs {len(runs)}, median {statistics.median(runs)}, mean {statistics.mean(runs):.2f}, "
      f"dark px in band {total_dark}")
