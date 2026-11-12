import json, os, sys
from collections import Counter, defaultdict

run = r"user/Documents/ega_scan_check_20261101/run_0IV1"
path = os.path.join(run, "findings_016_020.json")
data = json.load(open(path, encoding="utf-8"))
print("findings:", len(data))

texts = {}
for p in range(16, 21):
    b = open(os.path.join(run, "page_%03d.tex" % p), "rb").read()
    print("page", p, "CRLF" if b"\r\n" in b else "LF", len(b))
    texts[p] = b.decode("utf-8").replace("\r\n", "\n")

# segments of the LF source file between markers 16..21 (pages 16..20)
src = open(r"user/Documents/ega_scan_check_20261101/ega-fr/source/ega4/ega0-15-fr.tex",
           encoding="utf-8").read()
print("source CRLF" if "\r\n" in src else "source LF")
seg = {}
for p in range(16, 21):
    a = src.index("\\oldpage[0\\textsubscript{IV-1}]{%d}" % p)
    b2 = src.index("\\oldpage[0\\textsubscript{IV-1}]{%d}" % (p + 1))
    seg[p] = src[a:b2]
# body of each page file after the first comment line, compared with the source segment
for p in range(16, 21):
    body = texts[p].split("\n", 1)[1]
    s = seg[p]
    print("page", p, "body==segment" if body.rstrip() == s.rstrip() else "body!=segment",
          len(body), len(s))

ok = True
allowed = {"word", "formula", "symbol", "font", "italics", "missing", "extra", "number",
           "punctuation", "misprint_in_print", "convention", "marker", "other"}
counts = defaultdict(Counter)
for i, f in enumerate(data):
    p = f["page"]
    k = f["kind"]
    if k not in allowed:
        print("BAD KIND", i, k); ok = False
    if (k == "convention") != (f["convention"] is not None):
        print("CONVENTION MISMATCH", i); ok = False
    if f["confidence"] not in ("high", "medium", "low"):
        print("BAD CONF", i); ok = False
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in f:
            print("MISSING KEY", i, key); ok = False
    cat = "convention" if k == "convention" else ("misprint" if k == "misprint_in_print" else "normal")
    counts[p][cat] += 1
    fx = f["fix"]
    if fx is None:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        print("OLD COUNT", n, "page", p, "finding", i, repr(fx["old"][:80])); ok = False

# sequential application per page
for p in range(16, 21):
    t = texts[p]
    for i, f in enumerate(data):
        if f["page"] != p or f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        n = t.count(old)
        if n != 1:
            print("SEQ CONFLICT page", p, "finding", i, n, repr(old[:60])); ok = False
            continue
        t = t.replace(old, new)
    out = os.path.join(run, "crops_016_020", "applied_%03d.tex" % p)
    open(out, "w", encoding="utf-8", newline="\n").write(t)

for p in sorted(counts):
    c = counts[p]
    print("p%d normal %d / convention %d / misprint %d" % (p, c["normal"], c["convention"], c["misprint"]))
print("ALL OK" if ok else "PROBLEMS")
