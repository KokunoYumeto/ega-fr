import re, sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
envs = ['proposition', 'corollary', 'lemma', 'theorem', 'definition']
for e in envs:
    pat = re.compile(r'\\begin\{' + e + r'\}(\[[^\]]*\])?\n(\\label\{[^}]*\}\n)?')
    starts = [m.end() for m in pat.finditer(t)]
    em = sum(1 for s in starts if t[s:s + 6] == '\\emph{')
    print(e, len(starts), 'start with \\emph{:', em)
