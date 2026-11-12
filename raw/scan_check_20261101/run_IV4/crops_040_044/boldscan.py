import sys
import numpy as np
from PIL import Image

# Flag words whose estimated stroke width is well above the line median.
# usage: python boldscan.py PAGE [PAGE ...]
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"


def segments(mask_1d, min_gap, min_len=1):
    segs = []
    start = None
    gap = 0
    for i, v in enumerate(mask_1d):
        if v:
            if start is None:
                start = i
            gap = 0
            end = i
        else:
            if start is not None:
                gap += 1
                if gap >= min_gap:
                    if end - start + 1 >= min_len:
                        segs.append((start, end))
                    start = None
                    gap = 0
    if start is not None and end - start + 1 >= min_len:
        segs.append((start, end))
    return segs


def stroke(b):
    area = b.sum()
    if area < 30:
        return None
    p = np.pad(b, 1)
    inner = p[1:-1, 1:-1] & p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]
    edge = area - inner.sum()
    if edge == 0:
        return None
    return 2.0 * area / edge


for page in sys.argv[1:]:
    for s in range(1, 5):
        im = np.array(Image.open(f"{RUN}/page_{int(page):03d}_s{s}.png").convert('L'))
        b = im < 140
        rows = b.sum(axis=1) > 2
        lines = segments(rows, 3, 12)
        for (y0, y1) in lines:
            lb = b[y0:y1 + 1]
            cols = lb.sum(axis=0) > 0
            words = segments(cols, 14, 4)
            info = []
            for (x0, x1) in words:
                wb = lb[:, x0:x1 + 1]
                sw = stroke(wb)
                if sw is not None:
                    info.append((x0, x1, sw, wb.sum()))
            if len(info) < 3:
                continue
            med = np.median([w[2] for w in info])
            for (x0, x1, sw, area) in info:
                if sw > 1.28 * med and area > 150:
                    print(f"p{page} s{s} y{y0}-{y1} x{x0}-{x1} sw={sw:.2f} med={med:.2f} ratio={sw/med:.2f}")
