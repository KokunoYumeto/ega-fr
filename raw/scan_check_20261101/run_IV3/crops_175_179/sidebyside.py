import sys
from PIL import Image
# usage: sidebyside.py out scale img:x0:y0:x1:y1 ...
out = sys.argv[1]; scale = int(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p, x0, y0, x1, y1 = spec.split(':')
    im = Image.open(p).convert('L').crop((int(x0), int(y0), int(x1), int(y1)))
    tiles.append(im.resize((im.width*scale, im.height*scale), Image.NEAREST))
W = sum(t.width for t in tiles) + 20*(len(tiles)-1); H = max(t.height for t in tiles)
canvas = Image.new('L', (W, H), 255); x = 0
for t in tiles:
    canvas.paste(t, (x, 0)); x += t.width + 20
canvas.save(out); print(out, canvas.size)
