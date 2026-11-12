"""Count \\item[\\emph{...}] labels in ega4-2-fr.tex by the innermost enclosing statement/proof environment."""
import collections
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = pathlib.Path(json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["IV-2"]["files"][0])
t = src.read_text(encoding="utf-8")
envs = ("definition", "proposition", "theorem", "corollary", "lemma", "remark", "remarks", "scholium", "proof", "env",
        "example", "examples")
tok = re.compile(r"\\(begin|end)\{(" + "|".join(envs) + r")\}|\\item\[\\emph\{")
stack = []
count = collections.Counter()
for m in tok.finditer(t):
    if m.group(1) == "begin":
        stack.append(m.group(2))
    elif m.group(1) == "end":
        if stack and stack[-1] == m.group(2):
            stack.pop()
    else:
        count[stack[-1] if stack else "(none)"] += 1
print(dict(count))
