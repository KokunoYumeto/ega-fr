# 1) every fix's "old" occurs exactly once in its page_NNN.tex (CRLF -> LF);
# 2) simulate apply_fixes.py on an in-memory copy of the CURRENT release file: per fix, locate the page segment
#    (marker to next different marker) and require exactly one occurrence there at application time.
import json, re, pathlib, sys
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
run = E / "run_IV4"
src = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
F = json.load(open(run / "findings_220_224.json", encoding="utf-8"))
ok = True
for i, x in enumerate(F):
    if not x.get("fix"):
        continue
    t = (run / f"page_{x['page']:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    c = t.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print(f"[page file] #{i} p{x['page']} occurs {c} times: {x['fix']['old'][:70]!r}")
text = src.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


for i, x in enumerate(F):
    if not x.get("fix"):
        continue
    s, e = locate(text, x["page"])
    seg = text[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print(f"[simulation] #{i} p{x['page']} occurs {c} times: {x['fix']['old'][:70]!r}")
        continue
    text = text[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + text[e:]
# misprint fixes must change only the misprinted characters
for i, x in enumerate(F):
    if x["kind"] == "misprint_in_print":
        print("misprint", i, x["fix"], "| corrected:", x.get("corrected"))
print("ALL OK" if ok else "PROBLEMS")
(run / "crops_220_224" / "simulated_after.tex").write_text(text, encoding="utf-8", newline="\n")
