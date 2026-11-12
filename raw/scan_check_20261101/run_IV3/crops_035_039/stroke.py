import sys
from PIL import Image
import numpy as np
from scipy import ndimage
from skimage.morphology import skeletonize
base = r"user/Documents/ega_scan_check_20261101/run_IV3"
# args: "page,strip,x0,y0,x1,y1,label" ...
for spec in sys.argv[1:]:
    p, st, x0, y0, x1, y1, lab = spec.split(",")
    im = np.array(Image.open(f"{base}/page_{int(p):03d}_s{st}.png").convert("L"))
    reg = im[int(y0):int(y1)+1, int(x0):int(x1)+1]
    b = reg < 128
    lb, n = ndimage.label(b, structure=np.ones((3,3)))
    if n == 0: print(lab, "none"); continue
    sizes = ndimage.sum(b, lb, range(1, n+1))
    k = int(np.argmax(sizes)) + 1
    comp = lb == k
    dt = ndimage.distance_transform_edt(np.pad(comp, 1))[1:-1, 1:-1]
    sk = skeletonize(comp)
    w = 2*dt[sk]
    ink = (255 - reg.astype(float))[comp].sum() / 255.0
    print("%-12s area %4d  ink %6.1f  skel %3d  stroke mean %.2f median %.2f  area/skel %.2f" % (lab, comp.sum(), ink, sk.sum(), w.mean(), np.median(w), comp.sum()/max(1, sk.sum())))
