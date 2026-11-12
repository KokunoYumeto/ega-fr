"""Read-only check of findings_221_221.json: each 'old' occurs once in its page_NNN.tex, and an in-memory
replay on the release file (same page location rule as apply_fixes.py) applies every edit. Writes nothing."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV1\native\ega4\ega0-23-fr.tex")
findings = json.load(open(RUN / "findings_221_221.json", encoding="utf-8"))
ok = True
for i, x in enumerate(findings):
    fx = x.get("fix")
    if not fx:
        continue
    page_tex = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = page_tex.count(fx["old"])
    print(i, x["page"], "count in page file:", c)
    ok &= c == 1

marker = re.compile(r"\\oldpage\[" + re.escape("0\\textsubscript{IV-1}") + r"\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for k, (n, s) in enumerate(cuts):
        if n == page:
            j = k + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = REL.read_text(encoding="utf-8")
orig = t
for i, x in enumerate(findings):
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(t, x["page"])
    if s is None:
        print(i, "page not found"); ok = False; continue
    seg = t[s:e]
    c = seg.count(fx["old"])
    print(i, x["page"], "count in release segment:", c)
    if c != 1:
        ok = False; continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
k = t.find("cor.~4 du th.~1)~;\nil suffira")
print("--- replayed text around the p. 220/221 boundary ---")
print(t[k - 60:k + 520])
print("markers {221} after replay:", len(re.findall(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{221\}", t)))
print("ALL OK" if ok else "PROBLEM")
