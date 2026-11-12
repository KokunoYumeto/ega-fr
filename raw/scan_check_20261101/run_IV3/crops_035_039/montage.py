import sys, json
from PIL import Image, ImageDraw
# usage: montage.py out.png scale "page,strip,x0,y0,x1,y1,label" ...
base = r"user/Documents/ega_scan_check_20261101/run_IV3"
out = sys.argv[1]; s = int(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p, st, x0, y0, x1, y1, lab = spec.split(",")
    im = Image.open(f"{base}/page_{int(p):03d}_s{st}.png").convert("L")
    pad = 4
    c = im.crop((int(x0)-pad, int(y0)-pad, int(x1)+1+pad, int(y1)+1+pad))
    c = c.resize((c.width*s, c.height*s), Image.NEAREST)
    t = Image.new("L", (c.width+10, c.height+30), 255)
    t.paste(c, (5, 25))
    ImageDraw.Draw(t).text((5, 5), lab, fill=0)
    tiles.append(t)
W = sum(t.width for t in tiles); H = max(t.height for t in tiles)
m = Image.new("L", (W, H), 255)
x = 0
for t in tiles:
    m.paste(t, (x, 0)); x += t.width
m.save(f"{base}/crops_035_039/{out}")
print(m.size)
