import pathlib
import re

b = pathlib.Path(__file__).resolve().parent.joinpath("make_findings.py").read_bytes()
bad = [(i, c) for i, c in enumerate(b) if c < 32 and c not in (10, 13)]
print("control chars:", bad[:10])
t = b.decode("utf-8")
bs = chr(92)
print("backslash-u occurrences:", [t[m.start() - 10:m.start() + 10] for m in re.finditer(re.escape(bs + "u"), t)])
print("NL line:", re.findall(r"NL = .*", t))
for w in ["textbf", "frac", "bigl", "times", "to ", "boldsymbol", "begin", "end{", "textup", "emph", "leadsto", "setmin"]:
    print(w, t.count(bs + w))
