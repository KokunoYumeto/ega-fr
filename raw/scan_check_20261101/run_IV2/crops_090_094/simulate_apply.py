"""Read-only simulation: apply findings_090_094.json in order to an in-memory copy of the release ega4-2-fr.tex,
locating pages the way apply_fixes.py does. Writes nothing."""
import json
import pathlib
import re

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV2\native\ega4\ega4-2-fr.tex")
t = src.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


ok = fail = 0
for i, x in enumerate(json.load(open(run / "findings_090_094.json", encoding="utf-8"))):
    f = x.get("fix")
    if not f:
        continue
    s, e = locate(t, int(x["page"]))
    seg = t[s:e]
    n = seg.count(f["old"])
    if n != 1:
        fail += 1
        print(f"#{i} p{x['page']} FAILS ({n}x): {f['old'][:70]!r}")
        continue
    t = t[:s] + seg.replace(f["old"], f["new"]) + t[e:]
    ok += 1
print("applied", ok, "failed", fail)
for p in (90, 91, 92, 93, 94, 95):
    s, e = locate(t, p)
    print(f"--- p{p} starts: {t[s:s + 160]!r}")
    print(f"    ends: {t[e - 120:e]!r}")
