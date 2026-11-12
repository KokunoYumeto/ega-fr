import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
regions = {
    "4.6.4 text O_{X_y}":   (2, (1530, 25, 1640, 100)),
    "4.6.4.1 O_{X_y}":      (2, (1235, 140, 1330, 205)),
    "4.6.5 O_{X_y}":        (2, (600, 520, 700, 600)),
}
def comps(arr):
    lab, n = ndimage.label(arr < 140)
    res = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        m = lab[sl] == i
        area = int(m.sum())
        if area < 15:
            continue
        runs = []
        for row in m:
            r = 0
            for v in row:
                if v: r += 1
                elif r: runs.append(r); r = 0
            if r: runs.append(r)
        res.append((sl[1].start, sl[0].start, sl[1].stop, sl[0].stop, area, float(np.mean(runs))))
    return res
for name, (s, box) in regions.items():
    im = Image.open(run / f"page_142_s{s}.png").convert("L").crop(box)
    im.resize((im.width * 6, im.height * 6), Image.NEAREST).save(out / ("oxy_" + name.split()[0].replace('.', '') + ".png"))
    print(name)
    for c in sorted(comps(np.array(im))):
        x0, y0, x1, y1, area, mean = c
        print(f"   bbox x{x0}-{x1} y{y0}-{y1} (w{x1-x0} h{y1-y0}) area {area} run mean {mean:.2f}")
