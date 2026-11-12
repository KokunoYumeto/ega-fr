import json

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current"
       r"\packages\IV3\native\ega4\ega4-9-fr.tex")
F = json.load(open(RUN + r"\findings_075_079.json", encoding="utf-8"))

pages = {}
for p in range(75, 80):
    with open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="") as f:
        pages[p] = f.read().replace("\r\n", "\n")

# sequential application per page
for d in F:
    if not d["fix"]:
        continue
    p = d["page"]
    o, n = d["fix"]["old"], d["fix"]["new"]
    c = pages[p].count(o)
    if c != 1:
        print("SEQ FAIL", p, c, repr(o)[:80])
    pages[p] = pages[p].replace(o, n, 1)
print("sequential application done")

# uniqueness in the whole source file (informational)
src = open(SRC, encoding="utf-8").read()
for d in F:
    if not d["fix"]:
        continue
    c = src.count(d["fix"]["old"])
    if c != 1:
        print("source count", c, "page", d["page"], repr(d["fix"]["old"])[:90])

# show the patched page 78 formula region and the marker regions
for p in (75, 76, 77, 78, 79):
    t = pages[p]
    for key in ("considérons le polynôme de", "\\oldpage", "\\end{enumerate}", "Fin de la"):
        i = t.find(key)
        if i >= 0:
            print("----", p, key)
            print(t[max(0, i - 60): i + 260])
