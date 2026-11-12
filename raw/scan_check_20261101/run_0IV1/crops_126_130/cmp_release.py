import re, difflib
BS = "\\"
rel = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-20-fr.tex"
t = open(rel, encoding="utf-8", newline="").read()
print("release has CR:", "\r" in t)
marker = re.compile(re.escape(BS + "oldpage[0" + BS + "textsubscript{IV-1}]{") + r"(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
def seg(page):
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return t[s:cuts[j][1] if j < len(cuts) else len(t)]
for p in range(126, 131):
    pt = open(rf"user\Documents\ega_scan_check_20261101\run_0IV1\page_{p}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    body = pt.split("\n", 1)[1]  # drop '% from ...' line
    s = seg(p)
    same = body.rstrip("\n") == s.rstrip("\n")
    print(p, "identical" if same else "DIFFERENT")
    if not same:
        for l in difflib.unified_diff(body.splitlines(), s.splitlines(), "page", "release", lineterm="", n=1):
            print("   ", l)
