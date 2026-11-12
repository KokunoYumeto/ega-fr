"""Measure stroke weight of subscript-y glyphs (pages 247 and 248 of run_IV3)."""
import numpy as np
from PIL import Image
from scipy import ndimage

RUN = r"user/Documents/ega_scan_check_20261101/run_IV3/"
OUT = r"user/Documents/ega_scan_check_20261101/run_IV3/crops_245_249/"

WINDOWS = {
    "247_1511_fibres_Xy(heavy?)": ("page_247_s2.png", (1530, 315, 1600, 375)),
    "247_1511_telsque_Xy(light?)": ("page_247_s2.png", (1310, 375, 1380, 430)),
    "247_Spec_Oy": ("page_247_s1.png", (1700, 690, 1760, 745)),
    "247_contenant_Zy": ("page_247_s1.png", (670, 280, 725, 330)),
    "247_cqfd_Zy": ("page_247_s1.png", (1130, 395, 1185, 450)),
    "247_1510_Xy_first": ("page_247_s1.png", (310, 575, 370, 630)),
    "247_1510_Xy_second": ("page_247_s1.png", (1690, 575, 1745, 630)),
}


def measure(name, f, box):
    im = Image.open(RUN + f).convert("L").crop(box)
    a = np.asarray(im) < 128
    lab, n = ndimage.label(a)
    rows = []
    for i in range(1, n + 1):
        m = lab == i
        area = int(m.sum())
        if area < 30:
            continue
        ys, xs = np.nonzero(m)
        dt = ndimage.distance_transform_edt(m)
        rows.append((area, xs.min() + box[0], ys.min() + box[1], xs.max() - xs.min() + 1,
                     ys.max() - ys.min() + 1, float(dt.max())))
    big = im.resize((im.width * 6, im.height * 6), Image.NEAREST)
    big.save(OUT + "y_" + name.split("(")[0] + ".png")
    print(name)
    for r in sorted(rows, key=lambda r: r[1]):
        print("   area=%4d x=%4d y=%4d w=%3d h=%3d maxDT=%.2f" % r)


for k, (f, box) in WINDOWS.items():
    measure(k, f, box)
