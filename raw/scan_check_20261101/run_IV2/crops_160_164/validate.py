"""Validate findings_160_164.json: uniqueness of every 'old' in its page_NNN.tex and a dry run of the
sequential application on an in-memory copy of the current source (same locate() logic as apply_fixes.py)."""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
F = RUN / "findings_160_164.json"
d = json.load(open(F, encoding="utf-8"))
print("entries:", len(d))
keys_ok = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
bad = 0
for i, x in enumerate(d):
    missing = keys_ok - set(x)
    if missing:
        print(i, "missing keys", missing); bad += 1
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected"); bad += 1
    if x["kind"] == "convention" and not x.get("convention"):
        print(i, "convention without number"); bad += 1
    if x["kind"] != "convention" and x.get("convention"):
        print(i, "number on a non-convention"); bad += 1
    fx = x.get("fix")
    if not fx:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    n = t.count(fx["old"])
    if n != 1:
        print(i, "page", x["page"], "old occurs", n, "times:", repr(fx["old"])); bad += 1
    if "\\u" in fx["old"] or "\\u" in fx["new"]:
        print(i, "contains backslash-u", repr(fx["new"]))
print("uniqueness problems:", bad)

# dry run on the source
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
fails = 0
for i, x in enumerate(d):
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(t, int(x["page"]))
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        print("DRY RUN FAIL", i, x["page"], c, repr(fx["old"])[:80]); fails += 1
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("dry-run failures:", fails)
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
print("markers 158-166 after the dry run:", [n for n, s in cuts if 158 <= n <= 166])
for p in (160, 161, 162, 163):
    k = t.find("\\oldpage[IV-2]{%d}" % p)
    print("---- around new marker", p)
    print(t[k - 160:k + 140])
# per-page counts
cnt = collections.defaultdict(lambda: [0, 0, 0])
for x in d:
    k = 2 if x["kind"] == "misprint_in_print" else (1 if x["kind"] == "convention" else 0)
    cnt[x["page"]][k] += 1
print("counts normal/convention/misprint:", {p: tuple(v) for p, v in sorted(cnt.items())})
print("kinds:", collections.Counter(x["kind"] for x in d))
