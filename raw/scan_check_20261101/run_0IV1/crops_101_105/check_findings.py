"""Check findings_101_105.json: every fix 'old' occurs exactly once in its page_NNN.tex (CRLF normalised to LF),
and the fixes apply in list order to the release file's page segments (in memory only; no file is written)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV1\native\ega4\ega0-19-fr.tex")
F = json.load(open(RUN / "findings_101_105.json", encoding="utf-8"))

pages = {}
for p in range(101, 107):
    t = (RUN / ("page_%03d.tex" % p)).read_bytes().decode("utf-8").replace("\r\n", "\n")
    pages[p] = t

ok = True
print("--- uniqueness in page_NNN.tex ---")
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    n = pages[x["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("FAIL", i, x["page"], n, repr(fx["old"][:80]))
print("all unique" if ok else "SOME NOT UNIQUE")

# sequential simulation on the release file (as apply_fixes.py does)
part = r"0\textsubscript{IV-1}"
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
t = REL.read_text(encoding="utf-8")


def seg(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    return None, None


# compare page copies with the release segments first
for p in range(101, 107):
    s, e = seg(t, p)
    rel = t[s:e]
    cp = pages[p].split("\n", 1)[1]  # drop the '% from' line
    if p == 105 or True:
        same = rel == cp or rel.rstrip("\n") == cp.rstrip("\n")
    print("page", p, "copy == release segment:", same)

print("--- sequential application ---")
applied = 0
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    s, e = seg(t, x["page"])
    sg = t[s:e]
    c = sg.count(fx["old"])
    if c != 1:
        ok = False
        print("SEQ FAIL", i, x["page"], c, repr(fx["old"][:80]))
        continue
    t = t[:s] + sg.replace(fx["old"], fx["new"]) + t[e:]
    applied += 1
print("applied", applied, "of", sum(1 for x in F if x.get("fix")))
s, e = seg(t, 105)
print("--- resulting end of page 105 / start of 106 ---")
print(t[e - 700:e + 120])
s, e = seg(t, 102)
print("--- resulting page 102 theorem 19.6.4 ---")
i0 = t.find(r"\begin{theorem}[19.6.4]")
print(t[i0:i0 + 1100])
print("OK" if ok else "PROBLEMS")
