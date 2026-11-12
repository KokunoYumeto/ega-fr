import json
import pathlib
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
F = json.load(open(RUN / "findings_170_174.json", encoding="utf-8"))
keys = ["page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"]
kinds = set("word formula symbol font italics missing extra number punctuation misprint_in_print convention marker "
            "other".split())
bad = 0
cnt = defaultdict(Counter)
for i, d in enumerate(F):
    for k in keys:
        if k not in d:
            print(i, "missing key", k)
            bad += 1
    if d["kind"] not in kinds:
        print(i, "bad kind", d["kind"])
        bad += 1
    if d["kind"] == "misprint_in_print" and "corrected" not in d:
        print(i, "misprint without corrected")
        bad += 1
    if d["kind"] != "misprint_in_print" and "corrected" in d:
        print(i, "corrected on a non-misprint")
        bad += 1
    if d["kind"] == "convention" and not d["convention"]:
        print(i, "convention without number")
        bad += 1
    if d["fix"]:
        t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        n = t.count(d["fix"]["old"])
        if n != 1:
            print(i, "old occurs", n, "times on page", d["page"])
            bad += 1
        if "\r" in d["fix"]["old"] or "\r" in d["fix"]["new"]:
            print(i, "CR in fix")
            bad += 1
    cat = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[d["page"]][cat] += 1
print("problems:", bad, "findings:", len(F))
for p in sorted(cnt):
    c = cnt[p]
    print(p, f"{c['normal']}/{c['convention']}/{c['misprint']}")
print("kinds:", Counter(d["kind"] for d in F))
print("conventions:", Counter(d["convention"] for d in F if d["convention"]))
