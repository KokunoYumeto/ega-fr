import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
d = json.load(open(RUN + r"\findings_086_090.json", encoding="utf-8"))
texts = {}
for x in d:
    p = x["page"]
    if p not in texts:
        texts[p] = open(RUN + r"\page_%03d.tex" % p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
cur = dict(texts)
bad = 0
for i, x in enumerate(d):
    f = x["fix"]
    if f is None:
        continue
    p = x["page"]
    n_orig = texts[p].count(f["old"])
    n_cur = cur[p].count(f["old"])
    status = "ok" if n_orig == 1 else ("sequential(ok)" if n_cur == 1 else "BAD")
    if status != "ok":
        print(i, p, x["kind"], status, "orig", n_orig, "at-apply", n_cur, repr(f["old"][:70]))
    if n_cur != 1:
        bad += 1
    else:
        cur[p] = cur[p].replace(f["old"], f["new"], 1)
    if "\r" in f["old"] or "\r" in f["new"]:
        print(i, "CR in fix")
        bad += 1
print("fixes:", sum(1 for x in d if x["fix"]), "null fixes:", sum(1 for x in d if not x["fix"]), "bad:", bad)
