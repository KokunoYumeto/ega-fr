import sys
import numpy as np
from PIL import Image
from scipy import ndimage
# usage: cc.py page strip x0 y0 x1 y1 -> connected components (abs coords), with ink stats
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
p, s, x0, y0, x1, y1 = map(int, sys.argv[1:7])
im = np.array(Image.open(rf"{base}\page_{p:03d}_s{s}.png").convert("L")).astype(int)
c = im[y0:y1, x0:x1] < 128
lab, n = ndimage.label(c)
objs = ndimage.find_objects(lab)
for i, sl in enumerate(objs):
    m = lab[sl] == i+1
    cnt = m.sum()
    if cnt < 15: continue
    yy, xx = sl
    # stroke width estimate: 2*mean distance transform on skeleton approx -> use dt max per row
    dt = ndimage.distance_transform_edt(m)
    sw = 2*np.percentile(dt[m], 90)
    print(f"x {xx.start+x0}-{xx.stop+x0} y {yy.start+y0}-{yy.stop+y0} ink={cnt} h={yy.stop-yy.start} w={xx.stop-xx.start} sw90={sw:.2f} ink/h={cnt/(yy.stop-yy.start):.1f}")
