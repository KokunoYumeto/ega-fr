"""Extract the current source segments for pages 169-175 of IV-4 and compare with the prepared page_NNN.tex files.
usage: python -I segments.py"""
import pathlib
import re
import difflib

SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
OUT = RUN / "crops_170_174"
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
files = ["ega4-16-fr.tex", "ega4-17-fr.tex", "ega4-18-fr.tex", "ega4-20-fr.tex", "ega4-21a-fr.tex", "ega4-21b-fr.tex", "ega4-21c-fr.tex"]
for fn in files:
    t = (SRC / fn).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if 168 <= n <= 176:
            e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
            seg = t[s:e]
            line = t[:s].count("\n") + 1
            (OUT / f"cur_{n}_tex.txt").write_text(f"% {fn} line {line}\n" + seg, encoding="utf-8", newline="")
            print(fn, n, "line", line, "len", len(seg), "CRLF" if "\r\n" in seg else "LF")
            p = RUN / f"page_{n}.tex"
            if p.exists():
                old = p.read_text(encoding="utf-8").replace("\r\n", "\n")
                old_body = old.split("\n", 1)[1]
                if old_body.strip() == seg.strip():
                    print("   identical to page file")
                else:
                    d = list(difflib.unified_diff(old_body.splitlines(), seg.splitlines(), "page", "current", lineterm="", n=0))
                    print("   DIFFERS:", len(d), "diff lines")
                    for x in d[:60]:
                        print("   ", x)
