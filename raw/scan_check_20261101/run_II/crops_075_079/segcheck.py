import re, pathlib
rel = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
t = rel.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = t[s: cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
for n in range(75, 80):
    p = (run / f"page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    body = p.split("\n", 1)[1]
    seg = segs[n]
    status = "identical" if body == seg else ("page file startswith seg" if body.startswith(seg) else "DIFFERENT")
    print(n, status, len(body), len(seg))
for n in range(75, 81):
    s = t.find("\\oldpage[II]{%d}" % n)
    print("----", n, repr(t[s - 120:s + 90]))
