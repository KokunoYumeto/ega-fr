"""Compare the current source segment for pp. 120-124 with the prepared page_NNN.tex files."""
import pathlib
import difflib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions"
                   r"\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")

src = SRC.read_bytes().decode("utf-8")
print("CR in source:", "\r" in src)
start = src.index(r"\oldpage[IV-4]{120}")
end = src.index(r"\oldpage[IV-4]{125}")
seg = src[start:end]

pages = []
for n in range(120, 125):
    t = (RUN / f"page_{n:03d}.tex").read_bytes().decode("utf-8")
    first, rest = t.split("\n", 1)
    assert first.startswith("% from"), first
    pages.append(rest)
joined = "".join(pages)
print("segment length", len(seg), "pages length", len(joined))
if seg == joined:
    print("IDENTICAL")
else:
    for line in difflib.unified_diff(joined.splitlines(), seg.splitlines(), "pages", "source", lineterm="", n=0):
        print(line[:300])
