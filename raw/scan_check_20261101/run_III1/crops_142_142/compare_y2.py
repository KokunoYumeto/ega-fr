import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
# second-level y: 4.6.4 text O_{X_y}, 4.6.4.1 display O_{X_y}, 4.6.5 O_{X_y}; first-level y of X_y in 4.6.5 H^1(X_y
boxes = [
    (2, 1530 + 60, 25 + 48, 1530 + 81, 25 + 74),
    (2, 1235 + 61, 140 + 27, 1235 + 80, 140 + 52),
    (2, 600 + 44, 520 + 54, 600 + 65, 520 + 80),
]
sc = 12
ims = []
for s, x0, y0, x1, y1 in boxes:
    a = Image.open(run / f"page_142_s{s}.png").convert("L").crop((x0, y0, x1, y1))
    m = np.array(a) < 140
    dt = ndimage.distance_transform_edt(m)
    ridge = m & (dt >= ndimage.maximum_filter(dt, size=3))
    print("box", (x0, y0, x1, y1), "ink", int(m.sum()), "max radius", round(float(dt.max()), 2), "mean ridge radius", round(float(dt[ridge].mean()), 2))
    ims.append(a.resize((a.width * sc, a.height * sc), Image.NEAREST))
W = sum(i.width for i in ims) + 60 * (len(ims) - 1)
H = max(i.height for i in ims)
c = Image.new("L", (W, H), 255)
x = 0
for i in ims:
    c.paste(i, (x, 0)); x += i.width + 60
c.save(out / "y_second_level_x12.png")
# same ridge-radius measure for the four V_y subscripts
for s, x0, y0, x1, y1 in [(3, 680, 752, 710, 786), (3, 1353, 752, 1383, 786), (3, 1467, 752, 1497, 786), (4, 721, 69, 751, 103)]:
    a = np.array(Image.open(run / f"page_142_s{s}.png").convert("L").crop((x0, y0, x1, y1))) < 140
    lab, n = ndimage.label(a)
    sizes = ndimage.sum(a, lab, range(1, n + 1))
    keep = np.isin(lab, [i + 1 for i, v in enumerate(sizes) if v >= 40])
    dt = ndimage.distance_transform_edt(keep)
    ridge = keep & (dt >= ndimage.maximum_filter(dt, size=3))
    print("V_y", (s, x0, y0), "ink", int(keep.sum()), "max radius", round(float(dt.max()), 2), "mean ridge radius", round(float(dt[ridge].mean()), 2))
