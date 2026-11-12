import re
import pathlib

D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                 r"\packages\IV4\native\ega4")
for name in ["ega4-18-fr.tex"]:
    t = (D / name).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", t)]
    pat = re.compile(r"\$[a-e]'*\)\$")
    res = {}
    for i, (n, s) in enumerate(cuts):
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        c = len(pat.findall(t[s:e]))
        if c:
            res[n] = c
    lead = len(pat.findall(t[:cuts[0][1]]))
    print(name, "before first marker:", lead)
    print(res)
    print("total", sum(res.values()) + lead)
