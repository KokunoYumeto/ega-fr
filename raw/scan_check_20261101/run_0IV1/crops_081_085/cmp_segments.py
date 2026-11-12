import re
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
SRC = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex"
src = SRC.read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[" + re.escape(r"0\textsubscript{IV-1}") + r"\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(src)]
for i, (n, s) in enumerate(cuts):
    if 79 <= n <= 87:
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(src)
        seg = src[s:e]
        pf = E / "run_0IV1" / ("page_%03d.tex" % n)
        pt = pf.read_text(encoding="utf-8").replace("\r\n", "\n")
        body = pt.split("\n", 1)[1]
        same = seg.rstrip() == body.rstrip()
        print(n, "same" if same else "DIFFERENT", len(seg), len(body))
        if not same:
            import difflib
            for l in difflib.unified_diff(body.rstrip().split("\n"), seg.rstrip().split("\n"), "page_file", "release", lineterm="", n=1):
                print("   ", l)
