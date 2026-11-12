import os, re, difflib

run = r"user/Documents/ega_scan_check_20261101/run_0IV1"
for p in range(16, 21):
    orig = open(os.path.join(run, "page_%03d.tex" % p), encoding="utf-8").read().replace("\r\n", "\n")
    new = open(os.path.join(run, "crops_016_020", "applied_%03d.tex" % p), encoding="utf-8").read()
    for name, t in (("orig", orig), ("new", new)):
        s = re.sub(r"\\[{}$]", "", t)
        s = re.sub(r"%.*", "", s)
        opens, closes = s.count("{"), s.count("}")
        dollars = s.count("$")
        disp_o, disp_c = t.count("\\["), t.count("\\]")
        print(p, name, "braces", opens - closes, "dollars-even", dollars % 2 == 0, "displays", disp_o, disp_c)
    print("".join(difflib.unified_diff(orig.splitlines(True), new.splitlines(True), n=0))[:6000])
