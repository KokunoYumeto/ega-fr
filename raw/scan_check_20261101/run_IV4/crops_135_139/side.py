import sys
from PIL import Image
# side.py out scale page strip x0 y0 x1 y1 [page strip x0 y0 x1 y1 ...]
out = sys.argv[1]; scale = float(sys.argv[2])
args = sys.argv[3:]
ims = []
for i in range(0, len(args), 6):
    p, s, x0, y0, x1, y1 = args[i:i+6]
    im = Image.open(r'user/Documents/ega_scan_check_20261101/run_IV4/page_%s_s%s.png' % (p, s))
    c = im.crop(tuple(map(int, (x0, y0, x1, y1))))
    c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
    ims.append(c)
W = sum(c.width for c in ims) + 20*(len(ims)-1); H = max(c.height for c in ims)
canvas = Image.new('L', (W, H), 255)
x = 0
for c in ims:
    canvas.paste(c.convert('L'), (x, 0)); x += c.width + 20
canvas.save(out); print(canvas.size)
