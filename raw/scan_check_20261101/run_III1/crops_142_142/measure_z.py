import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
targets = {  # name: (strip, cx, cy) approximate centre of the subscript z
    "et soit f_z": (3, 1145, 305),
    "(i) Si f_z": (3, 712, 360),
    "(ii) si f_z": (3, 1747, 535),
}
ims = []
for name, (s, cx, cy) in targets.items():
    a = np.array(Image.open(run / f"page_142_s{s}.png").convert("L"))
    win = a[cy - 30:cy + 30, cx - 30:cx + 30]
    m = win < 140
    lab, n = ndimage.label(m)
    best = None
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        area = int((lab[sl] == i).sum())
        if 8 <= h <= 22 and 8 <= w <= 22 and area >= 40:
            c = ((sl[0].start + sl[0].stop) / 2 - 30, (sl[1].start + sl[1].stop) / 2 - 30)
            d = abs(c[0]) + abs(c[1])
            if best is None or d < best[0]:
                best = (d, i, sl, area, w, h)
    d, i, sl, area, w, h = best
    g = lab == i
    dt = ndimage.distance_transform_edt(g)
    ridge = g & (dt >= ndimage.maximum_filter(dt, size=3))
    print(f"{name}: w{w} h{h} area {area} max radius {dt.max():.2f} mean ridge radius {dt[ridge].mean():.2f}")
    crop = Image.fromarray(win[max(0, sl[0].start - 4):sl[0].stop + 4, max(0, sl[1].start - 4):sl[1].stop + 4])
    ims.append(crop.resize((crop.width * 12, crop.height * 12), Image.NEAREST))
W = sum(i.width for i in ims) + 60 * (len(ims) - 1)
H = max(i.height for i in ims)
c = Image.new("L", (W, H), 255)
x = 0
for i in ims:
    c.paste(i, (x, 0)); x += i.width + 60
c.save(out / "z_subscripts_x12.png")
