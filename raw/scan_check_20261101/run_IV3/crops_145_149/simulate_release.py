import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")
L = json.load(open(RUN / "findings_145_149.json", encoding="utf-8"))
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, (cuts[i + 1][1] if i + 1 < len(cuts) else len(text))
    return None, None


ok = True
for x in L:
    fx = x["fix"]
    if not fx:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        ok = False
        print("FAIL", x["page"], seg.count(fx["old"]), repr(fx["old"][:70]))
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("sequential application on the release text ok:", ok)
s, _ = locate(t, 145)
_, e = locate(t, 150)
part = t[s:e + 400]
(RUN / "crops_145_149" / "sim_release_145_150.tex").write_text(part, encoding="utf-8")
st = []
for m in re.finditer(r"\\(begin|end)\{(\w+)\}", part):
    k, n = m.groups()
    if k == "begin":
        st.append(n)
    elif st and st[-1] == n:
        st.pop()
    else:
        print("unmatched end", n, "near", part[max(0, m.start() - 50):m.start()].replace("\n", " | "))
print("open environments after the p. 150 opening:", st)
