"""Apply findings_076_080.json to copies of pages 75-81 (in memory) and write the
result to sim_075_081.tex in this folder, to check that the edits compose."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
F = json.load(open(RUN + r"\findings_076_080.json", encoding="utf-8"))

texts = {}
for p in range(75, 82):
    with open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        t = fh.read().replace("\r\n", "\n")
    first, rest = t.split("\n", 1)
    assert first.startswith("% from"), first
    texts[p] = rest

ok = True
# step A: ordinary fixes, per page segment, in list order
for d in F:
    if d["fix"] is None or d["kind"] == "marker":
        continue
    p, o, n = d["page"], d["fix"]["old"], d["fix"]["new"]
    c = texts[p].count(o)
    if c != 1:
        ok = False
        print("STEP A conflict", p, c, repr(o))
        continue
    texts[p] = texts[p].replace(o, n)

# step B/C: marker moves on the joined text, in list order
joined = "".join(texts[p] for p in range(75, 82))
for d in F:
    if d["kind"] != "marker":
        continue
    o, n = d["fix"]["old"], d["fix"]["new"]
    c = joined.count(o)
    if c != 1:
        ok = False
        print("STEP C conflict", d["page"], c, repr(o))
        continue
    joined = joined.replace(o, n)

print("compose ok:", ok)
with open(RUN + r"\crops_076_080\sim_075_081.tex", "w", encoding="utf-8", newline="\n") as fh:
    fh.write(joined)
