"""Stack several display-frame crops (from any page strips) vertically at one scale.

usage: python -I stack.py NAME SCALE PAGE:STRIP:x0,y0,x1,y1 [PAGE:STRIP:x0,y0,x1,y1 ...]
"""
import sys
from PIL import Image

name, scale = sys.argv[1], float(sys.argv[2])
parts = []
for spec in sys.argv[3:]:
    page, strip, box = spec.split(':')
    im = Image.open(rf'user\Documents\ega_scan_check_20261101\run_III2\page_{page}_s{strip}.png')
    r = im.width / 2000.0
    x0, y0, x1, y1 = (float(v) for v in box.split(','))
    c = im.crop((int(x0 * r), int(y0 * r), int(x1 * r), int(y1 * r)))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    parts.append(c)
w = max(p.width for p in parts)
h = sum(p.height for p in parts) + 10 * (len(parts) - 1)
out = Image.new('L', (w, h), 255)
y = 0
for p in parts:
    out.paste(p.convert('L'), (0, y))
    y += p.height + 10
path = rf'user\Documents\ega_scan_check_20261101\run_III2\crops_207_211\{name}.png'
out.save(path)
print(path, out.size)
