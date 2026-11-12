import re, sys
path = sys.argv[1]
s = open(path, encoding='utf-8').read()
pat = re.compile(r'\\begin\{(proposition|corollary|lemma|theorem|definition)\}\[([^\]]*)\]\n\\label\{[^}]*\}\n(\\emph\{)?')
n_emph = 0
n = 0
ems = []
for m in pat.finditer(s):
    n += 1
    if m.group(3):
        n_emph += 1
        ems.append(m.group(2))
print(n, n_emph)
print(ems)
