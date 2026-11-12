"""heavy.py PAGE: list connected components of capital-letter size whose mean horizontal stroke run is high
(possible wrong-fount bold letters). Read-only; prints strip, bbox, ink, run."""
import sys, pathlib
import numpy as np
from PIL import Image
from scipy import ndimage

here = pathlib.Path(__file__).resolve().parent
page = int(sys.argv[1])
thr = float(sys.argv[2]) if len(sys.argv) > 2 else 5.6
for s in range(1, 5):
    im = np.array(Image.open(here.parent / f"page_{page:03d}_s{s}.png").convert("L"))
    band = im < 140
    lab, n = ndimage.label(band, structure=np.ones((3, 3)))
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        if not (20 <= h <= 34 and 14 <= w <= 36):
            continue
        m = lab[sl] == i
        runs = []
        for r in m:
            d = np.diff(np.concatenate(([0], r.astype(int), [0])))
            runs += list(np.where(d == -1)[0] - np.where(d == 1)[0])
        run = float(np.mean(runs))
        if run >= thr:
            print("s%d x=%4d y=%4d w=%2d h=%2d ink=%4d run=%.2f" % (s, sl[1].start, sl[0].start, w, h, int(m.sum()), run))
