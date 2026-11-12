"""Independent check of findings_020_024.json: every fix's old occurs exactly once in page_NNN.tex
(LF-normalised), both in the original page and at its turn when the edits are applied in list order."""
import json
import pathlib

RUN = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((RUN / "findings_020_024.json").read_text(encoding="utf-8"))
pages = {}
bad = 0
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
for i, x in enumerate(d):
    missing = keys - set(x)
    if missing or (x["kind"] == "misprint_in_print") != ("corrected" in x):
        bad += 1
        print("KEYS", i, missing)
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
        pages[(p, "orig")] = pages[p]
    n0, n1 = pages[(p, "orig")].count(fx["old"]), pages[p].count(fx["old"])
    if n0 != 1 or n1 != 1:
        bad += 1
        print("COUNT", i, p, repr(fx["old"])[:70], n0, n1)
    pages[p] = pages[p].replace(fx["old"], fx["new"], 1)
print("entries", len(d), "with fix", sum(1 for x in d if x["fix"]), "problems", bad)
