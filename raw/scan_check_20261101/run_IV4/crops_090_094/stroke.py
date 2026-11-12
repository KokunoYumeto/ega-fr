import sys
from PIL import Image
import numpy as np
from scipy import ndimage
from skimage.morphology import skeletonize

# usage: stroke.py page strip x0 y0 x1 y1 [thresh]
# per connected component: bbox, pixel count, mean stroke width (2 * distance transform on the skeleton)
run = r'user\Documents\ega_scan_check_20261101\run_IV4'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = np.array(Image.open(rf'{run}\page_{page:03d}_s{strip}.png').convert('L'))
w = im[y0:y1, x0:x1] < th
lab, n = ndimage.label(w, structure=np.ones((3, 3)))
dt = ndimage.distance_transform_edt(w)
out = []
for k in range(1, n + 1):
    m = lab == k
    cnt = int(m.sum())
    if cnt < 15:
        continue
    ys, xs = np.nonzero(m)
    sk = skeletonize(m)
    sw = 2 * dt[sk].mean() if sk.any() else 0
    out.append((xs.min() + x0, ys.min() + y0, xs.max() + x0, ys.max() + y0, cnt, sw))
out.sort()
for bx0, by0, bx1, by1, cnt, sw in out:
    print(f'bbox=({bx0},{by0})-({bx1},{by1}) size={bx1-bx0+1}x{by1-by0+1} px={cnt} stroke={sw:.2f}')
