"""Compare page_NNN.tex (CRLF-normalized) with the current release files' segments for pages 115-119."""
import pathlib
import re

run = pathlib.Path(__file__).resolve().parent.parent
rel = run.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV3" / "native" / "ega4"
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
segs = {}
leads = {}
for name in ["ega4-10-fr.tex", "ega4-11-fr.tex"]:
    t = (rel / name).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    leads[name] = t[:cuts[0][1]]
    for i, (n, s) in enumerate(cuts):
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        segs[n] = (name, t[s:e])
segs[116] = ("ega4-10-fr.tex", segs[116][1] + "\n% (continued in ega4-11-fr.tex, before its first page marker)\n" + leads["ega4-11-fr.tex"])
for n in range(115, 120):
    p = (run / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = p.split("\n", 1)[1]
    name, seg = segs[n]
    print(n, name, "identical" if body == seg else "DIFFERENT", len(body), len(seg))
    if body != seg:
        import difflib
        for line in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm="", n=0):
            print("   ", line)
