import re
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex").read_text(encoding="utf-8")
m = list(re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", src))
for p in range(154, 161):
    idx = [i for i, x in enumerate(m) if int(x.group(1)) == p]
    s = m[idx[0]].start()
    e = m[idx[-1] + 1].start() if idx[-1] + 1 < len(m) else len(src)
    seg = src[s:e]
    f = (E / rf"run_IV2\page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = f.split("\n", 1)[1]
    print(p, "markers", len(idx), "same" if body == seg else "DIFF", len(seg), len(body))
    if body != seg:
        import difflib
        for l in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm="", n=0):
            print("   ", l)
