import sys
from PIL import Image
import numpy as np
from scipy import ndimage
# usage: cc.py page strip x0 y0 x1 y1 [minarea]
page, strip, x0, y0, x1, y1 = [int(v) for v in sys.argv[1:7]]
minarea = int(sys.argv[7]) if len(sys.argv) > 7 else 30
base = r"user/Documents/ega_scan_check_20261101/run_IV3"
im = np.array(Image.open(f"{base}/page_{page:03d}_s{strip}.png").convert("L"))
reg = im[y0:y1, x0:x1] < 128
lab, n = ndimage.label(reg, structure=np.ones((3,3)))
out = []
for i in range(1, n+1):
    ys, xs = np.where(lab == i)
    area = len(ys)
    if area < minarea: continue
    comp = (lab == i)
    # mean horizontal run length
    runs = []
    for r in range(comp.shape[0]):
        row = comp[r]
        if not row.any(): continue
        d = np.diff(np.concatenate([[0], row.astype(int), [0]]))
        st = np.where(d == 1)[0]; en = np.where(d == -1)[0]
        runs += list(en - st)
    out.append((xs.min()+x0, ys.min()+y0, xs.max()+x0, ys.max()+y0, area, round(float(np.mean(runs)),2)))
out.sort()
for o in out:
    print("x %4d-%4d y %4d-%4d  w %3d h %3d  area %4d  run %.2f" % (o[0], o[2], o[1], o[3], o[2]-o[0]+1, o[3]-o[1]+1, o[4], o[5]))
