import re
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex").read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(src)]
for page in range(96, 101):
    i = [k for k, (n, s) in enumerate(cuts) if n == page][0]
    seg = src[cuts[i][1]:cuts[i + 1][1]]
    pf = (E / "run_0IV1" / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pf.split("\n", 1)[1]
    print(page, "same" if body.rstrip() == seg.rstrip() else "DIFFERENT", len(body), len(seg))
    if body.rstrip() != seg.rstrip():
        import difflib
        for l in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm="", n=0):
            print("   ", l)
# context around the p. 96 and p. 101 markers
for page in (96, 99, 101):
    i = [k for k, (n, s) in enumerate(cuts) if n == page][0]
    s = cuts[i][1]
    print(page, repr(src[s - 120:s + 140]))
