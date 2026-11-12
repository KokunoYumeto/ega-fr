import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize

# usage: stroke.py src.png x0 y0 x1 y1
# prints connected dark components with bbox, area, skeleton length,
# mean stroke width (area / skeleton length) and max inscribed radius
src = sys.argv[1]
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
im = np.asarray(Image.open(src).convert('L').crop((x0, y0, x1, y1)), dtype=np.uint8)
dark = im < 128
lab, n = ndimage.label(dark)
for i in range(1, n + 1):
    comp = lab == i
    area = int(comp.sum())
    if area < 15:
        continue
    ys, xs = np.nonzero(comp)
    sk = skeletonize(comp)
    sl = int(sk.sum())
    dt = ndimage.distance_transform_edt(comp)
    print(f"comp bbox x={x0+xs.min()}-{x0+xs.max()} y={y0+ys.min()}-{y0+ys.max()} "
          f"h={ys.max()-ys.min()+1} area={area} skel={sl} "
          f"width={area/max(sl,1):.2f} maxr={dt.max():.2f}")
