"""Check that every fix 'old' of findings_090_094.json occurs exactly once in its page_NNN.tex (LF-normalised),
and print counts per page (normal / convention / misprint)."""
import collections
import json
import pathlib

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
items = json.load(open(run / "findings_090_094.json", encoding="utf-8"))
bad = 0
counts = collections.defaultdict(lambda: [0, 0, 0])
for i, x in enumerate(items):
    p = int(x["page"])
    k = x["kind"]
    counts[p][2 if k == "misprint_in_print" else 1 if k == "convention" else 0] += 1
    if k == "misprint_in_print" and "corrected" not in x:
        print("missing corrected", i)
    if k != "misprint_in_print" and "corrected" in x:
        print("corrected on a non-misprint", i)
    if k == "convention" and not x.get("convention"):
        print("convention number missing", i)
    f = x.get("fix")
    if not f:
        continue
    tex = (run / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = tex.count(f["old"])
    if n != 1:
        bad += 1
        print(f"#{i} p{p}: old occurs {n} times: {f['old']!r}")
    if "\\\\" in f["old"] or "\\\\" in f["new"]:
        print(f"#{i}: double backslash in decoded string: {f['old']!r} -> {f['new']!r}")
    if "\t" in f["old"] or "\t" in f["new"] or "\b" in f["old"] or "\b" in f["new"] or "\f" in f["new"]:
        print(f"#{i}: control character (JSON escape slip)")
print("items:", len(items), "with fix:", sum(1 for x in items if x.get("fix")), "bad:", bad)
for p in sorted(counts):
    print(p, "normal/convention/misprint =", "/".join(map(str, counts[p])))
