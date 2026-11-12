import json, collections

BASE = r"user\Documents\ega_scan_check_20261101\run_IV4"
F = json.load(open(BASE + r"\findings_015_019.json", encoding="utf-8"))
pages = {}
for p in range(15, 20):
    pages[p] = open(BASE + rf"\page_{p:03d}.tex", encoding="utf-8").read().replace("\r\n", "\n")

ok = True
counts = collections.defaultdict(lambda: [0, 0, 0])
for i, f in enumerate(F):
    p = f["page"]
    k = f["kind"]
    if k == "convention":
        counts[p][1] += 1
    elif k == "misprint_in_print":
        counts[p][2] += 1
    else:
        counts[p][0] += 1
    fx = f["fix"]
    if fx is None:
        continue
    n = pages[p].count(fx["old"])
    if n != 1:
        ok = False
        print("BAD", i, p, n, repr(fx["old"][:80]))
# simulate applying all fixes per page in order and check each old still matches once
for p in range(15, 20):
    t = pages[p]
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQ-BAD", p, n, repr(f["fix"]["old"][:80]))
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
print("all unique" if ok else "PROBLEMS")
for p in sorted(counts):
    print(p, "normal/convention/misprint =", "/".join(map(str, counts[p])))
