"""Count statement environments in ega4-2-fr.tex that close right before a numbered display (env)."""
import re
import sys
from collections import Counter

path = sys.argv[1]
t = open(path, encoding="utf-8").read()
pat = re.compile(r"\\end\{(proposition|corollary|lemma|theorem|definition)\}\s*\\begin\{env\}\[([^\]]*)\]")
hits = pat.findall(t)
print(len(hits), Counter(h[0] for h in hits))
print(", ".join(h[1] for h in hits))
