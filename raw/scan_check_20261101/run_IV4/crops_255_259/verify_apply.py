import json

run = r"user\Documents\ega_scan_check_20261101\run_IV4"
F = json.load(open(run + r"\findings_255_259.json", encoding="utf-8"))


def read(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


pages = {n: read(run + rf"\page_{n}.tex") for n in range(255, 260)}
keys = ["page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"]
for d in F:
    for k in keys:
        assert k in d, (k, d)
    if d["kind"] == "misprint_in_print":
        assert "corrected" in d
    if d["kind"] == "convention":
        assert d["convention"] in range(1, 11)
    else:
        assert d["convention"] is None
cur = dict(pages)
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    c = cur[d["page"]].count(fx["old"])
    assert c == 1, (d["page"], fx["old"], c)
    cur[d["page"]] = cur[d["page"]].replace(fx["old"], fx["new"], 1)
print("sequential application OK for", sum(1 for d in F if d["fix"]), "fixes")
for n in (255, 259):
    print("-----", n)
    print(cur[n][:200] if n == 0 else "")
# show the edited Definition 21.1.2 and the p. 259 sentence
t = cur[255]
i = t.find(r"\begin{definition}[21.1.2]")
print(t[i:i + 900])
t = cur[259]
i = t.find("En vertu de")
print(t[i:i + 330])
