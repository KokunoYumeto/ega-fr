import json
import pathlib
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
F = json.load(open(RUN / "findings_080_084.json", encoding="utf-8"))


def page_text(n, strip_header=True):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    if strip_header and t.startswith("% from"):
        t = t.split("\n", 1)[1]
    return t


ok = True
# 1. every old occurs exactly once in its page_NNN.tex (raw file, LF-normalised, header kept and stripped)
for i, f in enumerate(F):
    fx = f.get("fix")
    if not fx:
        continue
    for strip in (False, True):
        c = page_text(f["page"], strip).count(fx["old"])
        if c != 1:
            ok = False
            print("NOT UNIQUE", i, f["page"], repr(fx["old"]), c, "strip" if strip else "raw")
    if fx["old"] == fx["new"]:
        ok = False
        print("NO-OP", i)
    bal = lambda s: s.count("{") - s.count("}")
    if bal(fx["old"]) != bal(fx["new"]):
        ok = False
        print("BRACE BALANCE CHANGES", i, repr(fx["old"]), repr(fx["new"]))
    if fx["old"].count("$") % 2 != fx["new"].count("$") % 2:
        ok = False
        print("DOLLAR PARITY CHANGES", i)
# 2. sequential application per page in listed order
texts = {}
for i, f in enumerate(F):
    fx = f.get("fix")
    if not fx:
        continue
    p = f["page"]
    t = texts.setdefault(p, page_text(p))
    c = t.count(fx["old"])
    if c != 1:
        ok = False
        print("SEQUENTIAL FAIL", i, p, repr(fx["old"]), c)
        continue
    texts[p] = t.replace(fx["old"], fx["new"])
# 3. counts
cnt = defaultdict(Counter)
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[f["page"]][k] += 1
for p in sorted(cnt):
    print(p, dict(cnt[p]))
print("ALL OK" if ok else "PROBLEMS")
# show resulting page ends/starts around markers
for p in sorted(texts):
    t = texts[p]
    print("----", p, "start:", repr(t[:60]), "end:", repr(t[-50:]))
