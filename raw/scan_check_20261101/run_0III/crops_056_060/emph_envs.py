import re
import sys

path = sys.argv[1]
t = open(path, encoding="utf-8").read()
envs = ["proposition", "theorem", "corollary", "lemma", "definition", "namedtheorem", "namedlemma"]
pat = re.compile(r"\\begin\{(" + "|".join(envs) + r")\}(\[[^\]]*\])?(\{[^}]*\})?\s*(\\label\{[^}]*\}\s*)*\\emph\{")
ms = list(pat.finditer(t))
print(len(ms))
for m in ms[:60]:
    line = t.count("\n", 0, m.start()) + 1
    print(line, t[m.start():m.end() + 40].replace("\n", " | "))
