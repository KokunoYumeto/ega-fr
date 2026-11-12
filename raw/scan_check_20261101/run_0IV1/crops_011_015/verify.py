"""Verify findings_011_015.json: (1) every fix 'old' occurs exactly once in its page_NNN.tex (CRLF normalised);
(2) applying the fixes page by page in list order, each 'old' still occurs exactly once at its turn;
(3) dry simulation of apply_fixes.py's locate/apply on in-memory copies of the release files (nothing is written)."""
import collections
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
E = RUN.parent
F = json.load(open(RUN / "findings_011_015.json", encoding="utf-8"))
pages = {}
for n in range(11, 16):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")

print("(1) occurrences in page_NNN.tex")
cnt = collections.Counter()
for i, x in enumerate(F):
    cnt[(x["page"], x["kind"] == "convention", x["kind"] == "misprint_in_print")] += 1
    fx = x.get("fix")
    if not fx:
        print(f"  #{i} p{x['page']} {x['kind']}: no fix")
        continue
    c = pages[x["page"]].count(fx["old"])
    flag = "" if c == 1 else "   <-- CHECK"
    print(f"  #{i} p{x['page']} {x['kind']}: {c}{flag}")

print("(2) sequential application per page")
work = dict(pages)
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    t = work[x["page"]]
    c = t.count(fx["old"])
    if c == 1:
        work[x["page"]] = t.replace(fx["old"], fx["new"])
    elif pages[x["page"]].count(fx["old"]) == 1:
        print(f"  #{i}: old occurs {c} times after earlier edits   <-- OVERLAP")

print("(3) simulated apply_fixes.py on in-memory copies")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["0_IV-1"]["files"]
mem = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}
part = "0\\textsubscript{IV-1}"
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")


def locate(page):
    for f in inv:
        t = mem[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for k, (n, s) in enumerate(cuts):
            if n == page:
                j = k + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return f, s, cuts[j][1] if j < len(cuts) else len(t)
    return None, None, None


for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx or not fx.get("old") or fx["old"] == fx.get("new"):
        continue
    f, s, e = locate(int(x["page"]))
    if f is None:
        print(f"  #{i} p{x['page']}: MANUAL (page not found)")
        continue
    seg = mem[f][s:e]
    c = seg.count(fx["old"])
    if c != 1:
        print(f"  #{i} p{x['page']} {x['kind']}: MANUAL (old occurs {c} times in {pathlib.Path(f).name} segment)")
        continue
    mem[f] = mem[f][:s] + seg.replace(fx["old"], fx["new"]) + mem[f][e:]
print("  (all others applied)")
print("counts per page (page, convention?, misprint?):", sorted(cnt.items()))
