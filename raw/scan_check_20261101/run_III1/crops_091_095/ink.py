import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
for box in sys.argv[2:]:
    x0, y0, x1, y1 = map(int, box.split(','))
    c = im.crop((x0, y0, x1, y1))
    px = list(c.getdata())
    dark = sum(1 for p in px if p < 128)
    vdark = sum(1 for p in px if p < 64)
    # bounding box of dark pixels
    w, h = c.size
    xs = [i % w for i, p in enumerate(px) if p < 128]
    ys = [i // w for i, p in enumerate(px) if p < 128]
    bb = (min(xs), min(ys), max(xs), max(ys)) if xs else None
    print(box, 'dark<128:', dark, 'dark<64:', vdark, 'bbox:', bb)
