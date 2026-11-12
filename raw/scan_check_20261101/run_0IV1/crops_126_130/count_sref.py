import re, glob
BS = "\\"
pat = re.compile(re.escape(BS + "sref{") + r"[^}]*\},\s*\(([ivx]+|[a-z])\)")
pat2 = re.compile(r"\(" + re.escape(BS + "ref{") + r"[^}]*\},")
pat3 = re.compile(re.escape(BS + "mathrm{I}_"))
base = r"user\Documents\ega_scan_check_20261101"
for f in sorted(glob.glob(base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\*.tex")):
    t = open(f, encoding="utf-8").read()
    a = pat.findall(t); b = pat2.findall(t); c = pat3.findall(t)
    if a or b or c:
        print(f.split(BS)[-1], "sref+item:", len(a), "(ref, ..):", len(b), "mathrm{I}_:", len(c))
