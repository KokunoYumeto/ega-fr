import sys
from PIL import Image

# usage: crop_many.py <outdir> <scale> <strip>:<x0>:<y0>:<x1>:<y1>:<name> ...
outdir, scale = sys.argv[1], float(sys.argv[2])
for spec in sys.argv[3:]:
    strip, x0, y0, x1, y1, name = spec.split(':')
    im = Image.open(strip)
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(f"{outdir}/{name}.png")
    print(name, c.size)
