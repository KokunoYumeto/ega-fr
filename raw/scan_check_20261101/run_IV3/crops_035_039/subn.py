import sys
from PIL import Image
import numpy as np
from scipy import ndimage
# usage: subn.py page strip x0 y0 x1 y1  -> components of subscript-n size
page, strip, x0, y0, x1, y1 = [int(v) for v in sys.argv[1:7]]
base = r"user/Documents/ega_scan_check_20261101/run_IV3"
im = np.array(Image.open(f"{base}/page_{page:03d}_s{strip}.png").convert("L"))
reg = im[y0:y1, x0:x1] < 128
lab, n = ndimage.label(reg, structure=np.ones((3,3)))
for i in range(1, n+1):
    comp = (lab == i)
    ys, xs = np.where(comp)
    w = xs.max()-xs.min()+1; h = ys.max()-ys.min()+1
    if not (10 <= w <= 19 and 10 <= h <= 17): continue
    area = len(ys)
    runs = []
    for r in range(comp.shape[0]):
        row = comp[r]
        if not row.any(): continue
        d = np.diff(np.concatenate([[0], row.astype(int), [0]]))
        runs += list(np.where(d == -1)[0] - np.where(d == 1)[0])
    vr = []
    for c in range(comp.shape[1]):
        col = comp[:, c]
        if not col.any(): continue
        d = np.diff(np.concatenate([[0], col.astype(int), [0]]))
        vr += list(np.where(d == -1)[0] - np.where(d == 1)[0])
    dt = ndimage.distance_transform_edt(comp)
    print("x %4d-%4d y %4d-%4d w %2d h %2d area %4d hrun %.2f vrun %.2f dtmax %.2f" % (xs.min()+x0, xs.max()+x0, ys.min()+y0, ys.max()+y0, w, h, area, np.mean(runs), np.mean(vr), dt.max()))
