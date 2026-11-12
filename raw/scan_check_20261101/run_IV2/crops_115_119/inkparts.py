"""inkparts.py page:strip:x0:y0:x1:y1:c1:c2:c3:c4 ...
Sum of darkness (255 - value, pixels darker than 170 only) in columns [c1,c2) (the letter) and [c3,c4)
(a reference glyph, e.g. the parenthesis), relative to the box's x0."""
import sys
from PIL import Image
for spec in sys.argv[1:]:
    page, strip, x0, y0, x1, y1, c1, c2, c3, c4 = spec.split(':')
    im = Image.open(r'user\Documents\ega_scan_check_20261101\run_IV2\page_%s_s%s.png' % (page, strip)).convert('L')
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    w, h = c.size
    px = c.load()
    def ink(a, b):
        return sum(255 - px[x, y] for x in range(int(a), int(b)) for y in range(h) if px[x, y] < 170)
    a, b = ink(c1, c2), ink(c3, c4)
    print(spec, 'letter %d, reference %d, ratio %.2f' % (a, b, a / b if b else 0))
