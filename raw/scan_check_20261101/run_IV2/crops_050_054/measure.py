"""measure.py IMG X0 Y0 X1 Y1 [THRESH]
Box in the displayed 2000-px-wide frame. Lists horizontal dark runs (length >= 8 px, original pixels)
per row, so bar lengths of dashes, minus, plus and equals signs can be compared."""
import sys
from PIL import Image

img = sys.argv[1]
x0, y0, x1, y1 = map(float, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(img).convert('L')
f = im.size[0] / 2000.0
X0, Y0, X1, Y1 = (int(round(v * f)) for v in (x0, y0, x1, y1))
px = im.load()
for y in range(Y0, Y1):
    runs = []
    x = X0
    while x < X1:
        if px[x, y] < th:
            s = x
            while x < X1 and px[x, y] < th:
                x += 1
            if x - s >= 8:
                runs.append((s, x - s))
        else:
            x += 1
    if runs:
        print(y, ' '.join(f'{s}:{l}' for s, l in runs))
