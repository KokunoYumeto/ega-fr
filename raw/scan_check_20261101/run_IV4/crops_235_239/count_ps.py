import re, sys
f = sys.argv[1]
t = open(f, encoding="utf-8").read()
lines = t.split("\n")
pages = []
cur = None
for i, l in enumerate(lines, 1):
    m = re.search(r"\\oldpage\[IV-4\]\{(\d+)\}", l)
    if m:
        cur = int(m.group(1))
    pages.append(cur)
def where(pattern):
    out = {}
    for i, l in enumerate(lines):
        n = len(re.findall(pattern, l))
        if n:
            out[pages[i]] = out.get(pages[i], 0) + n
    return out
print("sheaf Ps.hom (mathscr P + operatorname hom):", where(r"\\mathscr\{P\}\\!s\.\\!\\operatorname\{hom\}"))
print("Ps.hom total:", where(r"\\operatorname\{Ps\.hom\}"))
print("mapsto:", where(r"\\mapsto"))
print("leadsto:", where(r"\\leadsto"))
print("vphi:", where(r"\\vphi(?![A-Za-z])"))
print("sref[0]:", where(r"\\sref\[0\]"))
print("varinjlim:", where(r"\\varinjlim"))
