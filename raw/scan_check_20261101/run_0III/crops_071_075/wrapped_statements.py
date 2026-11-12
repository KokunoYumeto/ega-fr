import re
import sys

t = open(sys.argv[1], encoding='utf-8').read()
envs = ['proposition', 'corollary', 'lemma', 'theorem', 'definition']
pat = re.compile(r'\\begin\{(' + '|'.join(envs) + r')\}(\[[^\]]*\])?\n(\\label\{[^}]*\}\n)?')
out = []
for m in pat.finditer(t):
    if t[m.end():m.end() + 6] == '\\emph{':
        out.append('%s %s' % (m.group(1), (m.group(2) or '').strip('[]')))
print(len(out))
print(', '.join(out))
