import sys
from PIL import Image

# usage: python compose.py <strip.png> <out.png> <scale> x0,y0,x1,y1 [x0,y0,x1,y1 ...]
# pastes the given boxes side by side, each scaled, with a white gap
src, out, scale = sys.argv[1], sys.argv[2], float(sys.argv[3])
boxes = [tuple(int(v) for v in b.split(',')) for b in sys.argv[4:]]
im = Image.open(src).convert('L')
tiles = []
for b in boxes:
    c = im.crop(b)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    tiles.append(c)
gap = 30
W = sum(t.width for t in tiles) + gap * (len(tiles) + 1)
H = max(t.height for t in tiles) + 2 * gap
canvas = Image.new('L', (W, H), 255)
x = gap
for t in tiles:
    canvas.paste(t, (x, gap))
    x += t.width + gap
canvas.save(out)
print(out, canvas.size)
