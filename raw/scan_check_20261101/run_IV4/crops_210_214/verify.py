"""Check findings_210_214.json (read-only): (1) every 'old' once in its original page text; (2) sequential application
on copies of the page texts; (3) simulation of apply_fixes.py on a copy of the CURRENT ega4-18-fr.tex (nothing written
to the release); (4) leftovers in the simulated segments."""
import json
import re

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
F = json.load(open(rf"{RUN}\findings_210_214.json", encoding="utf-8"))

pages = {}
for n in range(210, 215):
    pages[n] = open(rf"{RUN}\page_{n:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
orig = dict(pages)
print("== page files (original and sequential) ==")
bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    if p not in pages:
        print(f"#{i} p.{p}: outside the page files (boundary edit), checked in the source simulation")
        continue
    c0 = orig[p].count(fx["old"])
    c = pages[p].count(fx["old"])
    if c != 1 or c0 != 1:
        bad += 1
        print(f"#{i} p.{p} {x['kind']}: original count {c0}, sequential count {c}  <-- PROBLEM")
    if c == 1:
        pages[p] = pages[p].replace(fx["old"], fx["new"])
print("page-file problems:", bad)

t = open(SRC, encoding="utf-8").read()
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    return None, None


print("== source simulation ==")
bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        bad += 1
        print(f"#{i} p.{x['page']} FAILS: old occurs {c} times: {fx['old'][:70]!r}")
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("source failures:", bad)
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
print("markers 208-216 after simulation:", [n for n, s in cuts if 208 <= n <= 216])
open(rf"{RUN}\crops_210_214\simulated_ega4-18.tex", "w", encoding="utf-8", newline="").write(t)

print("== leftovers in simulated pp. 210-214 ==")
for p in range(210, 215):
    s, e = locate(t, p)
    seg = t[s:e]
    left = {
        "mathfrak R": seg.count(r"\mathfrak R"),
        "^*": seg.count("^*"),
        "$x)$ labels": len(re.findall(r"\$[a-h]'?\)", seg)),
        "item[x)] unwrapped": len(re.findall(r"\\item\[[a-h](\$'\$)?\)\]", seg)),
        "cdots": seg.count(r"\cdots"),
        "($0": seg.count("($0"),
        "begin{env}+display": len(re.findall(r"\\begin\{env\}\[[0-9.]+\]\n\\label\{[^}]*\}\n\\\[", seg)),
    }
    print(p, left)
    # brace balance and $ parity per page
    depth = 0
    k = 0
    while k < len(seg):
        ch = seg[k]
        if ch == "\\":
            k += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        k += 1
    dollars = len(re.findall(r"(?<!\\)\$", seg))
    print("   brace balance", depth, "| $ count", dollars, "(even)" if dollars % 2 == 0 else "(ODD!)")
s, e = locate(t, 209)
print("209 segment tail after simulation:", repr(t[s:e][-80:]))
