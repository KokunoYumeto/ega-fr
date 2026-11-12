import pathlib
from PIL import Image, ImageDraw
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
pieces = [  # label, strip, box
    ("1 bold II (II, 4.2.7)", 2, (1945, 776, 1998, 818)),
    ("2 (II, 6.1.1", 4, (996, 101, 1045, 143)),
    ("3 et I, 4.2.4", 4, (1254, 101, 1283, 143)),
    ("4 (II, 5.4.3)", 4, (1799, 274, 1850, 316)),
    ("5 roman VIII", 1, (928, 608, 996, 650)),
]
sc = 6
ims = []
for lab, s, box in pieces:
    im = Image.open(run / f"page_142_s{s}.png").convert("L").crop(box)
    ims.append((lab, im.resize((im.width * sc, im.height * sc), Image.NEAREST)))
W = sum(i.width for _, i in ims) + 50 * (len(ims) - 1)
H = max(i.height for _, i in ims) + 30
c = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(c)
x = 0
for lab, i in ims:
    c.paste(i, (x, 30)); d.text((x + 2, 5), lab.split()[0], fill=0); x += i.width + 50
c.save(out / "I_compare_x6.png")
print(c.size)
