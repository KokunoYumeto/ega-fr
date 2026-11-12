"""Check findings_110_114.json against page_NNN.tex and the current release source, and simulate the edits
the way apply_fixes.py applies them (page segment = from \\oldpage[IV-4]{N} to the next marker). Writes nothing
except the simulated result into this crops folder."""
import difflib
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-18-fr.tex")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def segment(t, page):
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


src = SRC.read_text(encoding="utf-8")
findings = json.load(open(RUN / "findings_110_114.json", encoding="utf-8"))
ok = True
pages = {}
for n in range(110, 115):
    raw = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    first, rest = raw.split("\n", 1)
    assert first.startswith("% from ega4-18-fr.tex"), first
    s, e = segment(src, n)
    seg = src[s:e]
    pages[n] = rest
    same = rest == seg
    print(f"p{n}: page file == current source segment: {same}")
    if not same:
        for line in difflib.unified_diff(rest.splitlines(), seg.splitlines(), "page", "source", lineterm="", n=1):
            print("   ", line)

for i, x in enumerate(findings):
    fx = x.get("fix")
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in x:
            print("MISSING KEY", key, i)
            ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("MISPRINT WITHOUT corrected", i)
        ok = False
    if x["kind"] == "convention" and not x["convention"]:
        print("CONVENTION WITHOUT NUMBER", i)
        ok = False
    if not fx:
        continue
    n = x["page"]
    c_page = pages[n].count(fx["old"])
    s, e = segment(src, n)
    c_src = src[s:e].count(fx["old"])
    c_file = src.count(fx["old"])
    flag = "" if c_page == 1 and c_src == 1 else "   <-- NOT UNIQUE"
    if flag:
        ok = False
    print(f"#{i:02d} p{n} page={c_page} seg={c_src} file={c_file} {x['kind']}/{x['convention']}: {fx['old'][:60]!r}{flag}")

# simulate sequential application, as apply_fixes.py does
t = src
applied = 0
for i, x in enumerate(findings):
    fx = x.get("fix")
    if not fx or not fx.get("old") or fx["old"] == fx["new"]:
        continue
    s, e = segment(t, int(x["page"]))
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        print(f"SIM: #{i} occurs {seg.count(fx['old'])} times at application time")
        ok = False
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    applied += 1
print("simulated:", applied, "edits applied")
out = pathlib.Path(__file__).with_name("simulated_ega4-18_p110-114.txt")
s0, _ = segment(t, 110)
_, e1 = segment(t, 115)
start = t.rfind("\n\n", 0, s0 - 200)
out.write_text(t[start:e1 + 200], encoding="utf-8", newline="\n")
print("ALL OK" if ok else "PROBLEMS FOUND")
