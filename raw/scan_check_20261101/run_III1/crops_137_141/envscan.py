import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
src = sys.argv[1]
s = open(src, encoding="utf-8").read()
pat = re.compile(
    r"\\begin\{env\}\[([^\]]*)\]\n(?:\\label\{[^}]*\}\n)?((?:\\emph|\\textit)\{[^}]*\}[^\n]*)"
)
m = pat.findall(s)
print("env blocks whose first line is a hand-made italic heading:", len(m))
for a, b in m:
    print(" ", a, "|", b[:100])
print(
    "remark:", s.count(r"\begin{remark}"),
    "remarks:", s.count(r"\begin{remarks}"),
    "env:", s.count(r"\begin{env}"),
)
