"""Prepare a batch for the EGA scan check: for every original page N of PART in [FIRST, LAST] found in the given TeX
files (split at \\oldpage[PART]{N}), write page_NNN.tex and four 300-dpi strips page_NNN_s1..s4.png.

Text in a file before its first marker continues the page before that marker (a section file can start mid-page);
it is appended to that page, in file order. With --tex-only the strips are not rendered again.
usage: python prep_batch.py PART SCAN_PDF PDF_OFFSET FIRST LAST OUTDIR TEXFILE [TEXFILE ...] [--tex-only]"""
import pathlib
import re
import subprocess
import sys

from PIL import Image

argv = [a for a in sys.argv[1:] if a != "--tex-only"]
tex_only = "--tex-only" in sys.argv
part, scan, offset, first, last, out = argv[0], argv[1], int(argv[2]), int(argv[3]), int(argv[4]), pathlib.Path(argv[5])
texfiles = [pathlib.Path(p) for p in argv[6:]]
out.mkdir(parents=True, exist_ok=True)
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
anymarker = re.compile(r"\\oldpage\[[^\]]*\]\{\d+\}")
pages, names, leads = {}, {}, []
for f in texfiles:
    t = f.read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    if not cuts:
        continue
    first_any = anymarker.search(t)
    lead = t[:first_any.start()] if first_any else ""
    if first_any and first_any.start() == cuts[0][1] and lead.strip():
        leads.append((cuts[0][0] - 1, f.name, lead))
    for i, (n, start) in enumerate(cuts):
        end = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        pages[n] = t[start:end]
        names[n] = f.name
for n, name, lead in leads:  # the opening text of a file belongs to the page before its first marker
    if n in pages:
        pages[n] += f"\n% (continued in {name}, before its first page marker)\n" + lead
done = []
for n in range(first, last + 1):
    if n not in pages:
        continue
    (out / f"page_{n:03d}.tex").write_text(f"% from {names[n]}\n" + pages[n], encoding="utf-8")
    done.append(n)
    if tex_only:
        continue
    full = out / f"page_{n:03d}_300"
    subprocess.run(["pdftoppm", "-png", "-r", "300", "-f", str(n + offset), "-l", str(n + offset), "-singlefile", scan, str(full)], check=True)
    im = Image.open(str(full) + ".png").convert("L")
    w, h = im.size
    box = Image.eval(im, lambda v: 255 - v).getbbox() or (0, 0, w, h)
    left, right, top, bottom = max(0, box[0] - 20), min(w, box[2] + 20), max(0, box[1] - 20), min(h, box[3] + 20)
    step = (bottom - top) / 4
    for i in range(4):
        y0 = int(top + i * step) - (40 if i else 0)
        y1 = int(top + (i + 1) * step) + (40 if i < 3 else 0)
        im.crop((left, max(top, y0), right, min(bottom, y1))).save(out / f"page_{n:03d}_s{i + 1}.png", optimize=True)
    pathlib.Path(str(full) + ".png").unlink()
missing = [n for n in range(first, last + 1) if n not in pages]
print("prepared", len(done), "pages:", done[0] if done else None, "-", done[-1] if done else None,
      "| continuations attached:", [n for n, _, _ in leads if n in pages], "| no marker:", missing)
