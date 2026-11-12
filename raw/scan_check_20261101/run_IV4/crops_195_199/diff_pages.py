import re, pathlib
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
for p in range(195, 200):
    i = [k for k, (n, s) in enumerate(cuts) if n == p][0]
    s, e = cuts[i][1], cuts[i + 1][1]
    seg = t[s:e]
    pg = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pg.split("\n", 1)[1]  # drop the '% from' line
    print(p, "identical" if body == seg else "DIFFERENT", len(body), len(seg))
    if body != seg:
        import difflib
        for l in difflib.unified_diff(seg.splitlines(), body.splitlines(), "source", "page", lineterm="", n=0):
            print("   ", l[:300])
