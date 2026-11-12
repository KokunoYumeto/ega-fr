"""Crop a region of a printed page at the scan's native 600 dpi, addressed in strip coordinates.
usage: hires.py PRINTED_PAGE STRIP_NO X0 Y0 X1 Y1 OUT [SCALE]
X/Y are pixel coordinates inside the 300-dpi strip page_NNN_sK.png made by prep_batch.py."""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
PDF = r"user\Documents\Free or receipted\free\lesson-sources\numdam\PMIHES_1961__11__5_0.pdf"
OFFSET = -3  # pdf page = printed page + offset

n, k, x0, y0, x1, y1 = (int(v) for v in sys.argv[1:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
p300 = HERE / f"_full_{n:03d}_300"
p600 = HERE / f"_full_{n:03d}_600"
if not pathlib.Path(str(p300) + ".png").exists():
    subprocess.run(["pdftoppm", "-png", "-r", "300", "-f", str(n + OFFSET), "-l", str(n + OFFSET), "-singlefile", PDF, str(p300)], check=True)
if not pathlib.Path(str(p600) + ".png").exists():
    subprocess.run(["pdftoppm", "-png", "-r", "600", "-f", str(n + OFFSET), "-l", str(n + OFFSET), "-singlefile", PDF, str(p600)], check=True)
im = Image.open(str(p300) + ".png").convert("L")
w, h = im.size
box = Image.eval(im, lambda v: 255 - v).getbbox() or (0, 0, w, h)
left, right, top, bottom = max(0, box[0] - 20), min(w, box[2] + 20), max(0, box[1] - 20), min(h, box[3] + 20)
step = (bottom - top) / 4
i = k - 1
sy0 = max(top, int(top + i * step) - (40 if i else 0))
big = Image.open(str(p600) + ".png").convert("L")
c = big.crop((2 * (left + x0), 2 * (sy0 + y0), 2 * (left + x1), 2 * (sy0 + y1)))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
