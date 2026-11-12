import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
# regions containing one V_y each (strip, box); report the components of the subscript y (bbox below the V's x-height)
regions = {
    "s3 voisinage V_y": (3, (650, 715, 790, 805)),
    "s3 f^-1(V_y)":     (3, (1270, 715, 1410, 805)),
    "s3 ->V_y":         (3, (1400, 715, 1540, 805)),
    "s4 reunion des V_y": (4, (640, 25, 780, 115)),
    "p143 s1 voisinage V_y": (None, None),
}
def comps(arr):
    lab, n = ndimage.label(arr < 140)
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        m = lab[sl] == i
        area = int(m.sum())
        if area < 40:
            continue
        runs = []
        for row in m:
            r = 0
            for v in row:
                if v: r += 1
                elif r: runs.append(r); r = 0
            if r: runs.append(r)
        out.append((sl[1].start, sl[0].start, sl[1].stop, sl[0].stop, area, float(np.median(runs)), float(np.mean(runs))))
    return out
for name, (s, box) in regions.items():
    if s is None:
        continue
    im = np.array(Image.open(run / f"page_142_s{s}.png").convert("L").crop(box))
    print(name)
    for c in sorted(comps(im)):
        x0, y0, x1, y1, area, med, mean = c
        print(f"   bbox x{x0}-{x1} y{y0}-{y1} (w{x1-x0} h{y1-y0}) area {area} run median {med:.1f} mean {mean:.2f}")
