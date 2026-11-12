import re
import sys

p = sys.argv[1]
t = open(p, encoding="utf-8").read()
pat = re.compile(r"\\begin\{(proposition|theorem|corollary|lemma|definition)\}(\[[^\]]*\])?\s*(\\label\{[^}]*\})?\s*")
i = t.find(r"\oldpage[III]")
for part, (a, b) in {"0III": (0, i), "III": (i, len(t))}.items():
    s = t[a:b]
    tot = 0
    em = 0
    for m in pat.finditer(s):
        tot += 1
        if s[m.end():m.end() + 6] == "\\emph{":
            em += 1
    print(part, "statements", tot, "starting with emph", em)
