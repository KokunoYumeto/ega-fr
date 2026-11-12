"""Compare the page_NNN.tex copies (CRLF) with the current page segments of the release source (LF).
usage: python -I compare_segments.py RUN_FOLDER SOURCE_TEX FIRST LAST"""
import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
run, source = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
first, last = int(sys.argv[3]), int(sys.argv[4])
src = source.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {n: src[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(src))] for i, (n, s) in enumerate(cuts)}
for n in range(first, last + 1):
    page = (run / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    body = page.split("\n", 1)[1]  # drop the '% from ...' line
    if body == seg.get(n):
        print(n, "identical")
    else:
        print(n, "DIFFERENT")
        for d in difflib.unified_diff(body.split("\n"), (seg.get(n) or "").split("\n"), "page", "source", lineterm="", n=0):
            print("   ", d[:200])
