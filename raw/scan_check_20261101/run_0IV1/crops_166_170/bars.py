"""List thin horizontal bars (minus signs, dashes, equals/plus strokes) in a strip.

usage: bars.py image [y0 y1]
Prints x0, x1, width, y-centre, height of every connected dark component whose
height is small and width is large relative to height.
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

path = sys.argv[1]
y0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
y1 = int(sys.argv[3]) if len(sys.argv) > 3 else None
im = np.array(Image.open(path).convert('L'))
if y1 is None:
    y1 = im.shape[0]
sub = im[y0:y1]
dark = sub < 128
lab, n = ndimage.label(dark)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs):
    if sl is None:
        continue
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    if h <= 8 and w >= 18 and w >= 4 * h:
        rows.append((sl[0].start + y0, sl[1].start, sl[1].stop, w, h))
rows.sort()
for (y, xa, xb, w, h) in rows:
    print(f"y={y:5d} x={xa:5d}-{xb:5d} w={w:3d} h={h}")
