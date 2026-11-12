"""Apply findings_270_274.json in list order to in-memory copies of ega4-21a/21b (apply_fixes.py's locate logic,
with the before-first-marker items applied in that region first), then print the resulting pages 270-274."""
import json
import pathlib
import re

here = pathlib.Path(__file__).resolve().parent
run = here.parent
SRC = run.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4"
files = {n: (SRC / n).read_text(encoding="utf-8") for n in ("ega4-21a-fr.tex", "ega4-21b-fr.tex")}
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
F = json.load(open(run / "findings_270_274.json", encoding="utf-8"))


def locate(page):
    for name, t in files.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                j = i + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return name, s, cuts[j][1] if j < len(cuts) else len(t)
    for name, t in files.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
            if a < page < b:
                return name, sa, sb
    return None, None, None


manual = []
# pass 1: what apply_fixes.py would do
for x in F:
    f = x.get("fix")
    if not f:
        continue
    name, s, e = locate(int(x["page"]))
    if name is None:
        manual.append(x); continue
    t = files[name]
    seg = t[s:e]
    if seg.count(f["old"]) != 1:
        manual.append(x); continue
    files[name] = t[:s] + seg.replace(f["old"], f["new"]) + t[e:]
print("manual after pass 1:", len(manual))
# pass 2: manual items in the region before ega4-21b's first marker, in list order
for x in manual:
    f = x["fix"]
    t = files["ega4-21b-fr.tex"]
    cut = marker.search(t).start()
    seg = t[:cut]
    c = seg.count(f["old"])
    print("  manual", x["page"], c, repr(f["old"][:50]))
    if c == 1:
        files["ega4-21b-fr.tex"] = seg.replace(f["old"], f["new"]) + t[cut:]
out = here / "simulated_pages_270_274.tex"
a = files["ega4-21a-fr.tex"]
b = files["ega4-21b-fr.tex"]
i = a.index("\\oldpage[IV-4]{270}")
j = b.index("\\oldpage[IV-4]{275}")
out.write_text(a[i:] + "\n%%%%% ega4-21b\n" + b[:j], encoding="utf-8")
print("markers in 21b:", [m.group(1) for m in marker.finditer(b)][:6])
print(out)
