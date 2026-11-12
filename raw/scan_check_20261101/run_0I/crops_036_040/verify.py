import json, pathlib, re
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_0I"
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega1\ega0-1-fr.tex"
L = json.load(open(RUN / "findings_036_040.json", encoding="utf-8"))
marker = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None


t0 = REL.read_text(encoding="utf-8")
assert "\r" not in t0
ok = True
# 1) each old occurs exactly once in its page_NNN.tex (CRLF -> LF) and in its release segment (pristine)
for i, x in enumerate(L):
    fix = x.get("fix")
    if not fix:
        continue
    p = x["page"]
    pt = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    s, e = locate(t0, p)
    c1, c2 = pt.count(fix["old"]), t0[s:e].count(fix["old"])
    if c1 != 1 or c2 != 1:
        ok = False
    print(i, p, x["kind"], "page file:", c1, "segment:", c2, "" if (c1 == 1 and c2 == 1) else "  <-- PROBLEM")
# 2) simulate apply_fixes.py in order on a copy
t = t0
for i, x in enumerate(L):
    fix = x.get("fix")
    if not fix or not fix.get("old") or fix.get("old") == fix.get("new"):
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(fix["old"]) != 1:
        print("SIM FAIL", i, x["page"], seg.count(fix["old"]))
        ok = False
        continue
    t = t[:s] + seg.replace(fix["old"], fix["new"]) + t[e:]
ms = [int(m.group(1)) for m in marker.finditer(t)]
print("markers after simulation (first 45):", ms[:45])
print("strictly increasing and unique:", all(a < b for a, b in zip(ms, ms[1:])))
s41 = t.index(r"\oldpage[0\textsubscript{I}]{41}")
print(repr(t[s41 - 120:s41 + 90]))
s40, e40 = locate(t, 40)
print("p.40 segment now ends with:", repr(t[e40 - 80:e40]))
print("p.40 segment contains 4.3 heading:", r"\subsection{Image réciproque" in t[s40:e40])
print("ALL OK" if ok else "SOME PROBLEMS")
