"""Cut one EGA part into page pairs for the scan check: the TeX of each original page (split at \\oldpage markers)
and the scan page rendered as PNG.
usage: python prep_pages.py TEXFILE PART_LETTER SCAN_PDF PDF_OFFSET FIRST LAST OUTDIR
(pdf page = printed page + PDF_OFFSET; for EGA I, PMIHES_1960__4__5_0.pdf, the offset is -1)"""
import pathlib
import re
import subprocess
import sys

tex, part, scan, offset, first, last, out = sys.argv[1:8]
offset, first, last = int(offset), int(first), int(last)
out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
t = pathlib.Path(tex).read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
pages = {}
for i, (n, start) in enumerate(cuts):
    end = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    pages[n] = t[start:end]
done = []
for n in range(first, last + 1):
    if n not in pages:
        continue
    (out / f"page_{n:03d}.tex").write_text(pages[n], encoding="utf-8")
    pdf_page = n + offset
    subprocess.run(["pdftoppm", "-png", "-r", "170", "-f", str(pdf_page), "-l", str(pdf_page), "-singlefile",
                    scan, str(out / f"page_{n:03d}")], check=True)
    done.append(n)
print("pages in file:", min(pages), "-", max(pages), "| prepared:", done)
