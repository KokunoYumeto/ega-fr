"""Compare page_NNN.tex (pages 242-246) with the current segment of ega4-1-fr.tex."""
import sys, difflib
sys.stdout.reconfigure(encoding="utf-8")
run = r"user\Documents\ega_scan_check_20261101\run_IV1"
src = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega4-1-fr.tex"
s = open(src, encoding="utf-8", newline="").read()
print("CRLF in source:", "\r\n" in s)
s = s.replace("\r\n", "\n")
for p in range(242, 247):
    page = open(run + "\\page_%03d.tex" % p, encoding="utf-8", newline="").read()
    if "\r\n" in page:
        print(p, "page file has CRLF")
    page = page.replace("\r\n", "\n")
    body = page.split("\n", 1)[1]  # drop '% from ...' line
    a = s.index("\\oldpage[IV-1]{%d}" % p)
    b = s.index("\\oldpage[IV-1]{%d}" % (p + 1))
    seg = s[a:b]
    if seg == body:
        print(p, "identical")
    else:
        print(p, "DIFFERS")
        for l in difflib.unified_diff(body.split("\n"), seg.split("\n"), "page", "source", lineterm="", n=1):
            print("   ", l)
