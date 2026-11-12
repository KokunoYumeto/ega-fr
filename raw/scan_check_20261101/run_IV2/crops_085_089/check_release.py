# Checks the findings against the current release file: each "old" must occur exactly once in its page segment
# (same locate rule as apply_fixes.py), and reports whether the page files still equal the release segments.
import json
import pathlib
import re

RUN = pathlib.Path(__file__).resolve().parent.parent
SRC = RUN.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV2/native/ega4/ega4-2-fr.tex"
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]


def seg(page):
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return t[s:cuts[j][1] if j < len(cuts) else len(t)]
    return None


for n in range(84, 91):
    p = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n", 1)[1]
    print(n, "page file == release segment:", p == seg(n))
bad = 0
for x in json.load(open(RUN / "findings_085_089.json", encoding="utf-8")):
    if x["fix"]:
        c = seg(x["page"]).count(x["fix"]["old"])
        if c != 1:
            bad += 1
            print("count", c, x["page"], repr(x["fix"]["old"]))
print("entries not unique in the release segments:", bad)
