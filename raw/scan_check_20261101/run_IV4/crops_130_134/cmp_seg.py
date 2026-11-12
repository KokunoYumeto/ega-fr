import pathlib, re, sys
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4")
R = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
t = (D / "ega4-18-fr.tex").read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", t)]
for i, (n, s) in enumerate(cuts):
    if 130 <= n <= 134:
        e = cuts[i + 1][1]
        seg = t[s:e]
        p = (R / f"page_{n:03d}.tex").read_text(encoding="utf-8")
        body = p.split("\n", 1)[1]
        print(n, "identical" if seg == body else "DIFFERENT", len(seg), len(body))
print("CRLF in source:", "\r\n" in t)
