"""Read-only simulation of apply_fixes.py for findings_100_104.json: applies the edits in memory, in order,
with the same page-segment rule, and reports failures. Writes nothing."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
files = inv["IV-3"]["files"]
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in files}
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")


def locate(page):
    for f in files:
        t = texts[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                j = i + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return f, s, cuts[j][1] if j < len(cuts) else len(t)
    return None, None, None


before = {f: texts[f] for f in files}
fails = 0
pre = [x for x in json.load(open(E / "run_IV3" / "findings_095_099.json", encoding="utf-8"))
       if x.get("page") == 100 and x.get("kind") == "marker"]
for x in pre + json.load(open(E / "run_IV3" / "findings_100_104.json", encoding="utf-8")):
    fx = x.get("fix")
    if not fx:
        continue
    f, s, e = locate(int(x["page"]))
    seg = texts[f][s:e]
    c = seg.count(fx["old"])
    if c != 1:
        fails += 1
        print("FAIL page", x["page"], "count", c, repr(fx["old"][:70]))
        continue
    texts[f] = texts[f][:s] + seg.replace(fx["old"], fx["new"]) + texts[f][e:]
print("failures:", fails)
for f in files:
    if texts[f] != before[f]:
        t = texts[f]
        print(pathlib.Path(f).name, "changed; markers 100-105 at lines:",
              [(int(m.group(1)), t[:m.start()].count("\n") + 1) for m in marker.finditer(t) if 99 <= int(m.group(1)) <= 105])
        print("begin{env} count", t.count("\\begin{env}"), "end{env} count", t.count("\\end{env}"))
        for probe in ("\\oldpage[IV-3]{100}", "(10.4.10)~: I~:", "\\textbf{(10.4.11)}", "on a\n$f^*"):
            i = t.find(probe)
            print(repr(t[max(0, i - 80):i + 120]))
