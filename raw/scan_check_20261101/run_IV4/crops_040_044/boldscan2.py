import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize

# Per word: skeleton stroke width and ink per column; flag words heavier than the page median.
# usage: python boldscan2.py PAGE [PAGE ...]
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"


def segments(m, min_gap, min_len=1):
    segs = []; start = None; gap = 0; end = 0
    for i, v in enumerate(m):
        if v:
            if start is None:
                start = i
            gap = 0; end = i
        else:
            if start is not None:
                gap += 1
                if gap >= min_gap:
                    if end - start + 1 >= min_len:
                        segs.append((start, end))
                    start = None; gap = 0
    if start is not None and end - start + 1 >= min_len:
        segs.append((start, end))
    return segs


for page in sys.argv[1:]:
    recs = []
    for s in range(1, 5):
        im = np.array(Image.open(f"{RUN}/page_{int(page):03d}_s{s}.png").convert('L')).astype(float)
        b = im < 140
        rows = b.sum(axis=1) > 2
        for (y0, y1) in segments(rows, 3, 12):
            if y1 - y0 > 60:  # skip displays/diagram blocks with stacked material
                continue
            lb = b[y0:y1 + 1]
            li = (255 - im[y0:y1 + 1]) / 255.0
            cols = lb.sum(axis=0) > 0
            for (x0, x1) in segments(cols, 9, 6):
                wb = lb[:, x0:x1 + 1]
                if wb.sum() < 120:
                    continue
                dt = ndimage.distance_transform_edt(wb)
                sk = skeletonize(wb)
                if sk.sum() == 0:
                    continue
                sw = 2 * dt[sk].mean()
                inkw = li[:, x0:x1 + 1].sum() / (x1 - x0 + 1)
                recs.append((s, y0, y1, x0, x1, sw, inkw))
    sws = np.array([r[5] for r in recs]); inks = np.array([r[6] for r in recs])
    msw, mink = np.median(sws), np.median(inks)
    print(f"page {page}: words={len(recs)} median sw={msw:.2f} ink/w={mink:.2f}")
    for (s, y0, y1, x0, x1, sw, inkw) in recs:
        if sw > 1.18 * msw and inkw > 1.15 * mink:
            print(f"  s{s} y{y0}-{y1} x{x0}-{x1} sw={sw:.2f} ({sw/msw:.2f}) ink/w={inkw:.1f} ({inkw/mink:.2f})")
