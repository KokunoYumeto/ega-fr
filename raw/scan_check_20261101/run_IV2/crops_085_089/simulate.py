# Simulates apply_fixes.py on the concatenated page files 84-90 (LF) with findings_085_089.json, in file order,
# and prints the regions around each applied edit, so order effects (marker move, paragraph joins) can be checked.
import json
import pathlib
import re

RUN = pathlib.Path(__file__).resolve().parent.parent
parts = []
for n in range(84, 91):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    parts.append(t.split("\n", 1)[1])  # drop the '% from ...' line
text = "".join(parts)
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


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


ok = bad = 0
for x in json.load(open(RUN / "findings_085_089.json", encoding="utf-8")):
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(text, x["page"])
    seg = text[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        bad += 1
        print("FAIL", x["page"], c, repr(fx["old"]))
        continue
    text = text[:s] + seg.replace(fx["old"], fx["new"]) + text[e:]
    ok += 1
print("applied", ok, "failed", bad)
for pat in ["et $K'$\n\\oldpage", "les composantes\n\\oldpage", "l'ensemble $Z$\n\\oldpage", "\\end{proof}\n\n\\oldpage[IV-2]{90}",
            "\\item[\\textup{a')}]", "((5.1.2) et", "\\textbf{(5.1.1.4)}", "On rappelle"]:
    i = text.find(pat)
    print("----", repr(pat), i)
    if i >= 0:
        print(text[max(0, i - 80):i + 160])
print("markers:", [m.group(0) for m in marker.finditer(text)])
(RUN / "crops_085_089" / "simulated_084_090.tex").write_text(text, encoding="utf-8")
