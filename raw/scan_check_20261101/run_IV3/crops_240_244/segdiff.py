"""Compare run_IV3 page_NNN.tex (pages 240-244) with the same segments of the r20 sources (read-only)."""
import difflib
import re

root = "user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
run = "user/Documents/ega_scan_check_20261101/run_IV3/"
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
anymarker = re.compile(r"\\oldpage\[[^\]]*\]\{\d+\}")
for v in ("current", "diplomatic"):
    pages, names, leads = {}, {}, []
    for fn in ("ega4-15-fr.tex", "ega4-15-terminal-fr.tex"):
        t = open(root + v + "/packages/IV3/native/ega4/" + fn, encoding="utf-8", newline="").read()
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        first_any = anymarker.search(t)
        lead = t[:first_any.start()] if first_any else ""
        if first_any and first_any.start() == cuts[0][1] and lead.strip():
            leads.append((cuts[0][0] - 1, fn, lead))
        for i, (n, start) in enumerate(cuts):
            end = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
            pages[n] = t[start:end]
            names[n] = fn
    for n, fn, lead in leads:
        if n in pages:
            pages[n] += f"\n% (continued in {fn}, before its first page marker)\n" + lead
    for n in range(240, 245):
        mine = open(run + f"page_{n:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
        src = f"% from {names[n]}\n" + pages[n]
        if mine == src:
            print(v, n, "identical")
        else:
            print(v, n, "DIFFERENT")
            for line in difflib.unified_diff(mine.splitlines(), src.splitlines(), "page", "source", lineterm="", n=0):
                print("   ", line[:300])
