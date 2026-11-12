"""Report horizontal dark runs (length >= MINLEN px) in rows Y0..Y1 of a strip.

Usage: python hruns.py PAGE STRIP X0 X1 Y0 Y1 [MINLEN] [THRESH]
Prints, for each run found, its row, start x, end x and length (original pixels).
Runs on consecutive rows with the same extent are merged into one line.
"""
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, x1, y0, y1 = (int(v) for v in sys.argv[3:7])
minlen = int(sys.argv[7]) if len(sys.argv) > 7 else 20
thr = int(sys.argv[8]) if len(sys.argv) > 8 else 128
im = Image.open(RUN + r"\page_%03d_s%d.png" % (page, strip)).convert('L')
px = im.load()
found = {}
for y in range(y0, y1):
    x = x0
    while x < x1:
        if px[x, y] < thr:
            s = x
            while x < x1 and px[x, y] < thr:
                x += 1
            if x - s >= minlen:
                found.setdefault((s // 3, x // 3), []).append((y, s, x))
        else:
            x += 1
for key, rows in sorted(found.items(), key=lambda kv: kv[1][0][1]):
    ys = [r[0] for r in rows]
    s = min(r[1] for r in rows)
    e = max(r[2] for r in rows)
    print('x %d-%d len %d rows %d-%d (%d rows)' % (s, e, e - s, min(ys), max(ys), len(ys)))
