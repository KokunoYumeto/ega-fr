import pathlib
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
# subscript X glyphs: 4.6.4 text O_{X_y}, 4.6.4.1 display O_{X_y}, 4.6.5 O_{X_y}
boxes = [
    (2, 1530 + 41, 25 + 34, 1530 + 65, 25 + 58),
    (2, 1235 + 46, 140 + 23, 1235 + 66, 140 + 41),
    (2, 600 + 24, 520 + 40, 600 + 49, 520 + 64),
]
sc = 14
ims = []
for s, x0, y0, x1, y1 in boxes:
    a = Image.open(run / f"page_142_s{s}.png").convert("L").crop((x0, y0, x1, y1))
    m = np.array(a) < 140
    dt = ndimage.distance_transform_edt(m)
    lab, n = ndimage.label(m)
    big = max(range(1, n + 1), key=lambda i: (lab == i).sum())
    g = lab == big
    print("box", (x0, y0, x1, y1), "ink", int(g.sum()), "max inscribed radius", round(float(dt[g].max()), 2),
          "mean radius on ridge", round(float(np.mean(dt[g & (dt >= ndimage.maximum_filter(dt, size=3))])), 2))
    ims.append(a.resize((a.width * sc, a.height * sc), Image.NEAREST))
W = sum(i.width for i in ims) + 60 * (len(ims) - 1)
H = max(i.height for i in ims)
c = Image.new("L", (W, H), 255)
x = 0
for i in ims:
    c.paste(i, (x, 0)); x += i.width + 60
c.save(out / "X_subscripts_x14.png")
