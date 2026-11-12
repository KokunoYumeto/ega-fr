import json
import sys

base = "user/Documents/ega_scan_check_20261101"
src_path = base + "/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex"
findings = json.load(open(sys.argv[1], encoding="utf-8"))
src = open(src_path, encoding="utf-8", newline="").read()
assert "\r\n" not in src, "source has CRLF"

pages = {}
for p in sorted({f["page"] for f in findings}):
    pages[p] = open(f"{base}/run_IVback/page_{p}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")

bad = 0
# 1. each old exactly once in its page file and in the source
for i, f in enumerate(findings):
    if not f["fix"]:
        continue
    old = f["fix"]["old"]
    cp = pages[f["page"]].count(old)
    cs = src.count(old)
    if cp != 1 or cs != 1:
        bad += 1
        print(f"#{i} p{f['page']} page-count={cp} source-count={cs}: {old[:80]!r}")

# 2. sequential application in list order, page texts and source
cur_pages = dict(pages)
cur_src = src
for i, f in enumerate(findings):
    if not f["fix"]:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    t = cur_pages[f["page"]]
    if t.count(old) != 1 or cur_src.count(old) != 1:
        bad += 1
        print(f"SEQ #{i} p{f['page']} page={t.count(old)} src={cur_src.count(old)}: {old[:80]!r}")
        continue
    cur_pages[f["page"]] = t.replace(old, new)
    cur_src = cur_src.replace(old, new)

# 3. reverse order application (detect order dependence)
rev_src = src
dep = []
for i, f in reversed(list(enumerate(findings))):
    if not f["fix"]:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    if rev_src.count(old) != 1:
        dep.append(i)
        continue
    rev_src = rev_src.replace(old, new)
print("order-dependent entries (fail when applied in reverse):", dep)

# 4. brace balance per fix
for i, f in enumerate(findings):
    if not f["fix"]:
        continue
    o, n = f["fix"]["old"], f["fix"]["new"]
    def bal(s):
        return s.count("{") - s.count("}")
    if bal(o) != bal(n):
        print(f"brace balance changes in #{i} p{f['page']}: {bal(o)} -> {bal(n)} (expected only for split \\emph pairs)")

open(base + "/run_IVback/crops_355_359/errata_applied_test.tex", "w", encoding="utf-8", newline="").write(cur_src)
print("problems:", bad, "findings:", len(findings))
from collections import Counter
c = Counter((f["page"], "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")) for f in findings)
for p in sorted(pages):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
