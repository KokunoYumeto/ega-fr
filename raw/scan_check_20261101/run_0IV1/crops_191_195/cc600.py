import sys
import numpy as np
from PIL import Image
from scipy import ndimage

# usage: cc600.py page X0 Y0 X1 Y1   (coordinates in the 600-dpi page image p<page>_600.png)
page = int(sys.argv[1])
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
D = r'user/Documents/ega_scan_check_20261101/run_0IV1/crops_191_195/'
im = np.asarray(Image.open(D + 'p%d_600.png' % page).convert('L'))
sub = im[y0:y1, x0:x1] < 128
lab, n = ndimage.label(sub, structure=np.ones((3, 3)))
rows = []
for k, sl in enumerate(ndimage.find_objects(lab), 1):
    comp = lab[sl] == k
    cnt = int(comp.sum())
    if cnt < 6:
        continue
    # stroke thickness estimate: max of distance transform * 2
    dt = ndimage.distance_transform_edt(comp)
    rows.append((sl[1].start + x0, sl[1].stop + x0, sl[0].start + y0, sl[0].stop + y0, cnt, float(dt.max()) * 2))
rows.sort()
for r in rows:
    print('x %4d-%4d y %4d-%4d w %3d h %3d px %5d maxthick %.1f' % (r[0], r[1], r[2], r[3], r[1] - r[0], r[3] - r[2], r[4], r[5]))
