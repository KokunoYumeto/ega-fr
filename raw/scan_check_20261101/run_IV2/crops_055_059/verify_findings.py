import json
import collections

base = "user/Documents/ega_scan_check_20261101/run_IV2/"
F = json.load(open(base + "findings_055_059.json", encoding="utf-8"))
texts = {}
for p in sorted({x["page"] for x in F}):
    texts[p] = open(base + f"page_{p:03d}.tex", encoding="utf-8").read().replace("\r\n", "\n")
orig = dict(texts)
bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    n_orig = orig[p].count(fx["old"])
    n_seq = texts[p].count(fx["old"])
    flag = "" if n_seq == 1 else "  <-- SEQUENTIAL COUNT != 1"
    if n_seq != 1:
        bad += 1
    if n_orig != 1 or n_seq != 1:
        print(f"#{i} p{p} {x['kind']}: original count {n_orig}, sequential count {n_seq}{flag}")
    texts[p] = texts[p].replace(fx["old"], fx["new"], 1)
print("bad:", bad)
cnt = collections.defaultdict(lambda: collections.Counter())
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[x["page"]][k] += 1
for p in sorted(cnt):
    print(p, dict(cnt[p]))
