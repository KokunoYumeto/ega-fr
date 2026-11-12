"""Compare run_IV1 page files 222-227 with the current release source ega4-1-fr.tex (read only)."""
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
S = E / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV1" / "native" / "ega4" / "ega4-1-fr.tex"
t = S.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-1\]\{(\d+)\}", t)]
d = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    d.setdefault(n, t[s:e])
for n in range(222, 228):
    p = (E / "run_IV1" / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    body = p.split("\n", 1)[1]
    print(n, "same" if body == d[n] else "DIFFERENT", len(body), len(d[n]))
print("CRLF in page files:", any(b"\r\n" in (E / "run_IV1" / f"page_{n:03d}.tex").read_bytes() for n in range(222, 228)))
print("source has CRLF:", b"\r\n" in S.read_bytes())
