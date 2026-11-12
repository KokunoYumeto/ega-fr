import pathlib
p = pathlib.Path(__file__).with_name("build_findings.py")
s = p.read_text(encoding="utf-8")
a = r"\boldsymbol{\mathit{Ab}}"
b = r"\boldsymbol{Ab}"
print("before", s.count(a), s.count(b))
s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
print("after", s.count(a), s.count(b))
