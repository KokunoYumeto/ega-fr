import os
from PIL import Image
run = r"user/Documents/ega_scan_check_20261101/run_0IV1"
out = os.path.join(run, "crops_016_020")
crops = [
 ("p19_fdot1", 19, 2, 1150, 175, 1680, 240, 3),
 ("p19_fdot2", 19, 2, 320, 320, 960, 380, 3),
 ("p19_eol",   19, 2, 1700, 440, 2060, 640, 2),
 ("p16_neq",   16, 4, 1300, 110, 2150, 170, 2),
 ("p17_neq",   17, 1, 1300, 340, 2100, 520, 2),
]
for name, page, strip, x0, y0, x1, y1, s in crops:
    im = Image.open(os.path.join(run, f"page_{page:03d}_s{strip}.png"))
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((c.width * s, c.height * s), Image.LANCZOS)
    c.save(os.path.join(out, name + ".png"))
    print(name, c.size)
