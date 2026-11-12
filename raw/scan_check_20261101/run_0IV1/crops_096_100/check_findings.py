"""Check findings_096_100.json: every fix's old occurs exactly once in its page_NNN.tex, and the fixes apply in order
to an in-memory copy of the release source with apply_fixes.py's page location (nothing is written)."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
R = E / "run_0IV1"
F = json.load(open(R / "findings_096_100.json", encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
bad = 0
for i, x in enumerate(F):
    miss = keys - set(x)
    if miss:
        print("missing keys", i, miss); bad += 1
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected", i); bad += 1
    fx = x.get("fix")
    if not fx:
        continue
    t = (R / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(fx["old"])
    if n != 1:
        print(f"[{i}] page {x['page']}: old occurs {n} times: {fx['old'][:80]!r}"); bad += 1
print("uniqueness problems:", bad)

# simulate on the release source
src_path = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex"
t = src_path.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    return None, None


fails = 0
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        print(f"SIM [{i}] page {x['page']} old occurs {c} times in segment: {fx['old'][:70]!r}"); fails += 1
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("simulation failures:", fails)
# show the result around the moved marker and the page joins
for pat in [r"\oldpage[0\textsubscript{IV-1}]{96}", r"\oldpage[0\textsubscript{IV-1}]{97}", r"\oldpage[0\textsubscript{IV-1}]{99}",
            r"\oldpage[0\textsubscript{IV-1}]{101}"]:
    k = t.find(pat)
    print(repr(t[k - 90:k + 90]))
print("count of p97 markers:", t.count(r"\oldpage[0\textsubscript{IV-1}]{97}"))
(R / "crops_096_100" / "sim_ega0-19_simulated_copy.txt").write_text(t, encoding="utf-8")
