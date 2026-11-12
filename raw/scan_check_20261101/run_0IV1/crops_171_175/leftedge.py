import sys
from PIL import Image
import numpy as np
path = sys.argv[1]
im = np.array(Image.open(path).convert('L'))
dark = im < 128
rows = dark.any(axis=1)
# group consecutive dark rows into lines
lines = []
start = None
for y, r in enumerate(rows):
    if r and start is None:
        start = y
    elif not r and start is not None:
        if y - start > 8:
            lines.append((start, y))
        start = None
for a, b in lines:
    xs = np.where(dark[a:b].any(axis=0))[0]
    # ignore specks: require column runs
    print(a, b, 'left', xs.min(), 'right', xs.max())
