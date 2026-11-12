"""ascii.py spec [spec ...]; spec = page:strip:x0:y0:x1:y1. Prints the crop as # (dark < 110), + (< 170), . (else)."""
import sys
from PIL import Image
for spec in sys.argv[1:]:
    page, strip, x0, y0, x1, y1 = spec.split(':')
    im = Image.open(r'user\Documents\ega_scan_check_20261101\run_IV2\page_%s_s%s.png' % (page, strip)).convert('L')
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    w, h = c.size
    px = c.load()
    print(spec)
    for y in range(h):
        print(''.join('#' if px[x, y] < 110 else '+' if px[x, y] < 170 else '.' for x in range(w)))
    print()
