import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-17-fr.tex").read_text(encoding="utf-8")
print("CR in src:", "\r" in src)
m = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(src)]
segs = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(src)
    segs[n] = src[s:e]
for p in range(80, 85):
    t = (E / ("run_IV4/page_%03d.tex" % p)).read_text(encoding="utf-8").replace("\r\n", "\n")
    body = t.split("\n", 1)[1]
    seg = segs[p]
    print(p, "equal" if body == seg else "DIFF", len(body), len(seg))
    if body != seg:
        for line in difflib.unified_diff(seg.splitlines(), body.splitlines(), lineterm="", n=0):
            print("   ", line[:200])
