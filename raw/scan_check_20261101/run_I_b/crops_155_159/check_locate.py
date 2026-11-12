import json, pathlib, re
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["I"]["files"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}


def seg(page):
    for f, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, t[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(t))]
    return None, None


def before_first(fname):
    for f, t in texts.items():
        if f.endswith(fname):
            m = marker.search(t)
            return t[:m.start()]


for x in json.load(open(E / "run_I_b/findings_155_159.json", encoding="utf-8")):
    if not x["fix"]:
        continue
    f, s = seg(x["page"])
    n = s.count(x["fix"]["old"])
    if n != 1:
        c = before_first("ega1-7-fr.tex").count(x["fix"]["old"])
        print("p%d page-region count %d, ega1-7 before_first_marker count %d: %r"
              % (x["page"], n, c, x["fix"]["old"][:60]))
print("done")
