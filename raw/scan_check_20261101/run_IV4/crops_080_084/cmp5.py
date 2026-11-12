from PIL import Image
import numpy as np
def glyph(path, box):
    im = Image.open(path).convert('L')
    a = np.array(im.crop(box))
    mask = a < 140
    ys, xs = np.where(mask)
    return a, mask, (xs.min(), ys.min(), xs.max(), ys.max()), mask.sum()
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
# heavy 5 in (II, 6.1.5): strip 2 of p81, approx x 1110-1150, y 325-375
for name, path, box in [('heavy5', base+'page_081_s2.png', (1112, 328, 1150, 372)),
                        ('normal5_8115', base+'page_081_s2.png', (640, 372, 685, 418)),
                        ]:
    a, m, bb, n = glyph(path, box)
    print(name, bb, n)
