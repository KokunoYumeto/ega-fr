"""Count \\item[\\emph{...}] labels in ega4-2-fr.tex by enclosing environment (read-only)."""
import re
import sys
from collections import Counter

t = open(sys.argv[1], encoding="utf-8").read()
env_re = re.compile(r"\\(begin|end)\{(remark|remarks|example|examples|proof|lemma|proposition|corollary|theorem|definition|scholium)\}")
item_re = re.compile(r"\\item\[\\emph\{")
events = [(m.start(), "env", m.group(1), m.group(2)) for m in env_re.finditer(t)]
events += [(m.start(), "item", None, None) for m in item_re.finditer(t)]
events.sort()
stack = []
c = Counter()
first = {}
for p, kind, a, b in events:
    if kind == "env":
        if a == "begin":
            stack.append(b)
        elif b in stack:
            while stack and stack[-1] != b:
                stack.pop()
            if stack:
                stack.pop()
    else:
        k = stack[-1] if stack else "none"
        c[k] += 1
        first.setdefault(k, t[:p].count("\n") + 1)
print(dict(c))
print("first line per env:", first)
