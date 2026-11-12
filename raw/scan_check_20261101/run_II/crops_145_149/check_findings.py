# Verifies findings_145_149.json: each fix's old occurs exactly once in its page file (LF-normalized),
# and all fixes of a page apply in listed order and in reverse order. Also reports counts per page.
import json, collections

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
F = json.load(open(RUN + r"\findings_145_149.json", encoding="utf-8"))

def text(page):
    with open(RUN + r"\page_%03d.tex" % page, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")

ok = True
by_page = collections.defaultdict(list)
for i, f in enumerate(F):
    by_page[f["page"]].append(f)
    if f["fix"] is None:
        continue
    t = text(f["page"])
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/ABSENT", f["page"], n, repr(f["fix"]["old"]))

for page, fs in sorted(by_page.items()):
    for order in ("fwd", "rev"):
        t = text(page)
        seq = [f for f in fs if f["fix"]]
        if order == "rev":
            seq = seq[::-1]
        for f in seq:
            o, nw = f["fix"]["old"], f["fix"]["new"]
            c = t.count(o)
            if c != 1:
                ok = False
                print("SEQUENTIAL FAIL", page, order, c, repr(o))
                continue
            t = t.replace(o, nw)
    cnt = collections.Counter()
    for f in fs:
        if f["kind"] == "convention":
            cnt["convention"] += 1
        elif f["kind"] == "misprint_in_print":
            cnt["misprint"] += 1
        else:
            cnt["normal"] += 1
    print(page, "normal/convention/misprint = %d/%d/%d" % (cnt["normal"], cnt["convention"], cnt["misprint"]))

# brace balance of each new vs old (except deliberate \emph split)
for f in F:
    if f["fix"]:
        o, nw = f["fix"]["old"], f["fix"]["new"]
        d = (nw.count("{") - nw.count("}")) - (o.count("{") - o.count("}"))
        if d:
            print("BRACE DELTA", f["page"], d, repr(o), "->", repr(nw))
print("ALL OK" if ok else "PROBLEMS FOUND")
