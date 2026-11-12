"""Median horizontal dark-run length (stroke width) per region of a strip.

usage: python stroke.py PAGE STRIP y0 y1 name:x0-x1 [name:x0-x1 ...]
"""
import sys
import pathlib
import statistics
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip = int(sys.argv[1]), int(sys.argv[2])
y0, y1 = int(sys.argv[3]), int(sys.argv[4])
img = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
px = img.load()
THR = 128
for spec in sys.argv[5:]:
    name, rng = spec.split(":")
    x0, x1 = (int(v) for v in rng.split("-"))
    runs = []
    dark = 0
    for y in range(y0, y1):
        run = 0
        for x in range(x0, x1):
            if px[x, y] < THR:
                run += 1
                dark += 1
            else:
                if 0 < run <= 20:
                    runs.append(run)
                run = 0
        if 0 < run <= 20:
            runs.append(run)
    if runs:
        print(f"{name:12s} runs={len(runs):5d} median={statistics.median(runs):.1f} "
              f"mean={statistics.mean(runs):.2f} dark={dark}")
    else:
        print(name, "no runs")
