"""Render one pdf page of the IV-3 scan at 600 dpi (native) and list its text lines, or crop a region.
usage: python -I lines.py PDFPAGE list
       python -I lines.py PDFPAGE crop NAME X0 Y0 X1 Y1 [SCALE]
Crops are written next to this script."""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
PDF = r"user\Documents\Free or receipted\free\lesson-sources\numdam\PMIHES_1966__28__5_0.pdf"
page = int(sys.argv[1])
full = HERE / f"pdf{page:03d}_600.png"
if not full.exists():
    subprocess.run(["pdftoppm", "-png", "-r", "600", "-f", str(page), "-l", str(page), "-singlefile", PDF,
                    str(full)[:-4]], check=True)
im = Image.open(full).convert("L")
w, h = im.size
if sys.argv[2] == "list":
    px = im.load()
    rows = []
    for y in range(h):
        dark = [x for x in range(0, w, 2) if px[x, y] < 128]
        rows.append((len(dark), dark[0] if dark else None, dark[-1] if dark else None))
    y = 0
    n = 0
    while y < h:
        if rows[y][0] > 0:
            y0 = y
            xs0, xs1 = [], []
            while y < h and rows[y][0] > 0:
                xs0.append(rows[y][1]); xs1.append(rows[y][2]); y += 1
            if y - y0 > 8:
                n += 1
                print(f"line {n}: y {y0}-{y} x {min(xs0)}-{max(xs1)}")
        y += 1
    print("size", w, h)
else:
    name, x0, y0, x1, y1 = sys.argv[3], *map(int, sys.argv[4:8])
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
    c = im.crop((x0, y0, x1, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(HERE / f"{name}.png")
    print("saved", name, c.size)
