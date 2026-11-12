import difflib
import pathlib
import re

R = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                 r"\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
C = pathlib.Path(str(R).replace("\\diplomatic\\", "\\current\\"))
m = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def seg(p):
    t = p.read_text(encoding="utf-8")
    c = [(int(x.group(1)), x.start()) for x in m.finditer(t)]
    return {n: t[s:(c[i + 1][1] if i + 1 < len(c) else len(t))] for i, (n, s) in enumerate(c)}


a, b = seg(R), seg(C)
for p in range(50, 55):
    for line in difflib.unified_diff(a[p].splitlines(), b[p].splitlines(), lineterm="", n=0):
        print(p, line)
