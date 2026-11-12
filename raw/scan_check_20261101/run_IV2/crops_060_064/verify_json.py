"""Re-read findings_060_064.json and check every fix against the page files."""
import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
d = json.loads((RUN / "findings_060_064.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
bad = 0
for i, x in enumerate(d):
    missing = keys - set(x)
    if missing:
        bad += 1
        print("missing keys", i, missing)
    if x["kind"] == "misprint_in_print":
        if "corrected" not in x:
            bad += 1
            print("misprint without corrected", i)
    elif "corrected" in x:
        bad += 1
        print("corrected on a non-misprint", i)
    if x["fix"] is None:
        if x["kind"] != "misprint_in_print":
            bad += 1
            print("null fix on a non-misprint", i)
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = t.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("count", c, i, repr(x["fix"]["old"]))
    if "\r" in x["fix"]["old"] or "\r" in x["fix"]["new"]:
        bad += 1
        print("CR in fix", i)
print(len(d), "entries,", bad, "problems")
