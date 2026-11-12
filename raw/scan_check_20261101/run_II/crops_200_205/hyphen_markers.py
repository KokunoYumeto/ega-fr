"""List \\oldpage markers that sit inside or next to a hyphenated word, to see the edition's placement habit."""
import glob
import re
import sys

root = sys.argv[1]
pat = re.compile(r"\\oldpage\[[^\]]*\]\{\d+\}")
for f in sorted(glob.glob(root + "/*/*.tex")):
    t = open(f, encoding="utf-8").read()
    for m in pat.finditer(t):
        before = t[max(0, m.start() - 50):m.start()]
        after = t[m.end():m.end() + 50]
        if re.search(r"[a-zé]-\s*$", before) or re.search(r"^\s*(coh|compact|projectif|fini|affine|sépar)", after):
            print(f.split("native")[-1], repr(before), m.group(0), repr(after))
