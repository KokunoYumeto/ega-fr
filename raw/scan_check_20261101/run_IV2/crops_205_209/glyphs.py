"""glyphs.py PAGE STRIP Y0 Y1 [X0 X1] -- ORIGINAL pixel coords; lists connected components (height >= 25 px)
in the band with bbox, ink count and mean horizontal stroke run (dark < 140)."""
import sys, pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
here = pathlib.Path(__file__).resolve().parent
page, strip, y0, y1 = (int(v) for v in sys.argv[1:5])
im = np.array(Image.open(here.parent / f"page_{page:03d}_s{strip}.png").convert("L"))
x0, x1 = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (0, im.shape[1])
band = im[y0:y1, x0:x1] < 140
lab, n = ndimage.label(band, structure=np.ones((3, 3)))
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, 1):
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    if h < int(sys.argv[7]) if len(sys.argv) > 7 else h < 25:
        continue
    m = lab[sl] == i
    ink = int(m.sum())
    runs = []
    for r in m:
        d = np.diff(np.concatenate(([0], r.astype(int), [0])))
        s = np.where(d == 1)[0]; e = np.where(d == -1)[0]
        runs += list(e - s)
    rows.append((sl[1].start + x0, sl[0].start + y0, w, h, ink, np.mean(runs) if runs else 0))
for r in sorted(rows):
    print("x=%4d y=%4d w=%3d h=%3d ink=%5d run=%.2f" % r)
