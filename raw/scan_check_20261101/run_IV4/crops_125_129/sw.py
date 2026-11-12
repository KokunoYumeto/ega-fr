import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize
# usage: sw.py label page strip x0 y0 x1 y1 ... : stroke width along skeleton of the largest component in the box
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
a = sys.argv[1:]
for i in range(0, len(a), 7):
    lab = a[i]; p, s, x0, y0, x1, y1 = map(int, a[i+1:i+7])
    im = np.array(Image.open(rf"{base}\page_{p:03d}_s{s}.png").convert("L")).astype(float)
    c = im[y0:y1, x0:x1]
    m = c < 128
    L, n = ndimage.label(m)
    sizes = ndimage.sum(m, L, range(1, n+1))
    k = int(np.argmax(sizes)) + 1
    g = L == k
    dt = ndimage.distance_transform_edt(g)
    sk = skeletonize(g)
    w = 2*dt[sk]
    darkness = (255 - c[g]).sum() / 255.0
    print(f"{lab}: ink={g.sum()} dark-sum={darkness:.0f} skel-len={sk.sum()} sw_median={np.median(w):.2f} sw_mean={w.mean():.2f} ink/skel={g.sum()/sk.sum():.2f}")
