import re, sys, collections
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
pat = re.compile(r'\\begin\{(proposition|theorem|corollary|lemma|definition|remark)\}(\[[^\]]*\])?\s*(\\label\{[^}]*\}\s*)?(.{0,12})', re.S)
c = collections.Counter()
for m in pat.finditer(t):
    c[(m.group(1), m.group(4).startswith('\\emph'))] += 1
print(c)
