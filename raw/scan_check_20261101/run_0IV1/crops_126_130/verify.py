import json, re
BS = "\\"
RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
REL = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-20-fr.tex"
F = json.load(open(RUN + r"\findings_126_130.json", encoding="utf-8"))

# 1. each old exactly once in its page_NNN.tex
print("== occurrences in page_NNN.tex ==")
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    pt = open(RUN + rf"\page_{x['page']}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    c = pt.count(fx["old"])
    if c != 1:
        print(f"  #{i} p.{x['page']} old occurs {c} times: {fx['old'][:70]!r}")
    if "\r" in fx["old"] or "\r" in fx["new"]:
        print("  CR in fix", i)
print("  done")

marker = re.compile(re.escape(BS + "oldpage[0" + BS + "textsubscript{IV-1}]{") + r"(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    return None, None


def simulate(skip_misprints):
    t = open(REL, encoding="utf-8").read()
    ok = True
    for i, x in enumerate(F):
        fx = x.get("fix")
        if not fx:
            continue
        if skip_misprints and x["kind"] == "misprint_in_print":
            continue
        s, e = locate(t, int(x["page"]))
        if s is None:
            print(f"  #{i} p.{x['page']}: page not found"); ok = False; continue
        seg = t[s:e]
        c = seg.count(fx["old"])
        if c != 1:
            print(f"  #{i} p.{x['page']}: old occurs {c} times in segment: {fx['old'][:70]!r}"); ok = False; continue
        t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    return ok, t


print("== sequential simulation, diplomatic (all fixes) ==")
ok, t = simulate(False)
print("  all applied" if ok else "  FAILURES above")
print("== sequential simulation, corrected edition (misprint fixes skipped) ==")
ok2, t2 = simulate(True)
print("  all applied" if ok2 else "  FAILURES above")

out = RUN + r"\crops_126_130\simulated_diplomatic_126_130.txt"
s, _ = locate(t, 126)
_, e = locate(t, 130)
open(out, "w", encoding="utf-8").write(t[s:e])
print("wrote", out)
