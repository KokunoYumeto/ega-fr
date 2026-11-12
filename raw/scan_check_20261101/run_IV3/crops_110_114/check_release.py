# Read-only: count each fix's "old" in the current release segment of its page (same logic as apply_fixes.locate).
import json, pathlib, re
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["IV-3"]["files"]
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}


def seg(page):
    for f, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
                return f, t[s:e]
    return None, None


F = json.load(open(E / "run_IV3" / "findings_110_114.json", encoding="utf-8"))
ok = 0
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    f, s = seg(int(x["page"]))
    n = s.count(fx["old"].replace("\r\n", "\n")) if s is not None else -1
    if n != 1:
        print("COUNT", n, x["page"], repr(fx["old"][:70]))
    else:
        ok += 1
print("ok", ok, "of", sum(1 for x in F if x["fix"]))
for p in range(110, 115):
    f, s = seg(p)
    pt = (E / "run_IV3" / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pt.split("\n", 1)[1]  # drop the '% from' line
    print(p, pathlib.Path(f).name, "segment == page file:", s.rstrip("\n") == body.rstrip("\n"))
