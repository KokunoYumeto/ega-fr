import re
import sys

base = sys.argv[1]
for fn in sys.argv[2:]:
    s = open(base + '/' + fn, encoding='utf-8').read()
    pat = re.compile(r'\\begin\{(proposition|corollary|theorem|lemma|definition)\}\[([^\]]*)\](.*?)\\end\{\1\}', re.S)
    for m in pat.finditer(s):
        body = m.group(3)
        body = re.sub(r'\\oldpage\[[^\]]*\]\{\d+\}\s*', '', body)
        paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
        # also text directly after \end{enumerate}
        tails = re.findall(r'\\end\{enumerate\}\s*\n([^\n\\][^\n]{0,60})', body)
        flag = []
        for p in paras[1:]:
            if re.match(r'(En effet|Montrons|Il suffit|Comme |D.apr.s|Cela |Ceci |La condition|On a |Notons|Supposons d.abord|Par hypoth)', p):
                flag.append(p[:70].replace('\n', ' '))
        for t in tails:
            if re.match(r'(En effet|Montrons|Il suffit|Comme |D.apr.s|Cela |Ceci |La condition|On a |Notons)', t):
                flag.append('after enumerate: ' + t[:70])
        if flag:
            line = s.count('\n', 0, m.start()) + 1
            print(fn, m.group(2), 'line', line, flag)
