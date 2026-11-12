"""Compare the page_NNN.tex copies with the current segments of the diplomatic and current release files."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
run = pathlib.Path(sys.argv[1])
files = sys.argv[2:]
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")
for f in files:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    print(f)
    for n in range(137, 142):
        idx = [i for i, (p, s) in enumerate(cuts) if p == n]
        if not idx:
            print("  page", n, "marker missing")
            continue
        i = idx[0]
        s = cuts[i][1]
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        seg = t[s:e]
        page = (run / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        body = page.split("\n", 1)[1]  # drop the '% from ...' line
        print("  page", n, "segment len", len(seg), "page file len", len(body), "identical" if seg == body else "DIFFERENT")
        if seg != body:
            for k, (a, b) in enumerate(zip(seg, body)):
                if a != b:
                    print("    first difference at", k, repr(seg[max(0, k - 60):k + 60]), "||", repr(body[max(0, k - 60):k + 60]))
                    break
