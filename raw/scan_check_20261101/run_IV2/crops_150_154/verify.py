import json
from collections import Counter

RUN = "user/Documents/ega_scan_check_20261101/run_IV2"
d = json.load(open(RUN + "/findings_150_154.json", encoding="utf-8"))
texts = {}
for p in range(150, 155):
    with open(f"{RUN}/page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")
bad = 0
for i, x in enumerate(d):
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in x:
            print("missing key", key, i)
            bad += 1
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected", i)
        bad += 1
    if x["kind"] == "convention" and not x["convention"]:
        print("convention without number", i)
        bad += 1
    if x["fix"] is not None:
        n = texts[x["page"]].count(x["fix"]["old"])
        if n != 1:
            print("old count", n, i, x["page"], repr(x["fix"]["old"]))
            bad += 1
c = Counter()
for x in d:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in range(150, 155):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("entries", len(d), "problems", bad)
