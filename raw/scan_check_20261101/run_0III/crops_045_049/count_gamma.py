import re
import sys

t = open(sys.argv[1], encoding="utf-8").read()
a = t.find(r"\label{0.11.8.2-fr}")
b = t.find(r"\label{subsection:0.11.9-fr}")
s = t[a:b]
sys_letter = re.findall(r"\\Gamma(?!_\{\\sigma)(?!\^k_)(?!\^\{k\+1\}_)", s)
comp = re.findall(r"\\Gamma(?:\^k|\^\{k\+1\})?_\{\\sigma", s)
print("11.8.2..11.8.10 chars", len(s), "Gamma as system letter:", len(sys_letter), "Gamma components:", len(comp))
print("transposes {}':", len(re.findall(r"\{\}'[a-z]", s)))
for m in re.finditer(r"\\Gamma(?!_\{\\sigma)(?!\^k_)(?!\^\{k\+1\}_)", s):
    pass
