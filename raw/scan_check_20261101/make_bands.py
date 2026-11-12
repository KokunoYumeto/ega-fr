"""Render scan pages at 300 dpi and cut each into horizontal strips with a small overlap, so a checker reads a few
sharp images per page instead of zooming many times.
usage: python make_bands.py SCAN_PDF PDF_OFFSET FIRST LAST OUTDIR [STRIPS]"""
import pathlib
import subprocess
import sys

from PIL import Image

scan, offset, first, last, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), pathlib.Path(sys.argv[5])
strips = int(sys.argv[6]) if len(sys.argv) > 6 else 4
out.mkdir(parents=True, exist_ok=True)
for n in range(first, last + 1):
    full = out / f"page_{n:03d}_300"
    subprocess.run(["pdftoppm", "-png", "-r", "300", "-f", str(n + offset), "-l", str(n + offset), "-singlefile", scan, str(full)], check=True)
    im = Image.open(str(full) + ".png").convert("L")
    w, h = im.size
    # trim the white margins left and right, keep a small border
    box = Image.eval(im, lambda v: 255 - v).getbbox() or (0, 0, w, h)
    left, right = max(0, box[0] - 20), min(w, box[2] + 20)
    top, bottom = max(0, box[1] - 20), min(h, box[3] + 20)
    step = (bottom - top) / strips
    for i in range(strips):
        y0 = int(top + i * step) - (40 if i else 0)
        y1 = int(top + (i + 1) * step) + (40 if i < strips - 1 else 0)
        im.crop((left, max(top, y0), right, min(bottom, y1))).save(out / f"page_{n:03d}_s{i + 1}.png", optimize=True)
    pathlib.Path(str(full) + ".png").unlink()
print("strips made for pages", first, "to", last)
