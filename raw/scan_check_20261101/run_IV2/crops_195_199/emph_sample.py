import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
src = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex'
t = open(src, encoding='utf-8').read()
pat = re.compile(r'\\begin\{(proposition|theorem|corollary|lemma)\}(.*?)\\end\{\1\}', re.S)
blocks = pat.findall(t)
ne = sum(1 for b in blocks if '\\emph{' in b[1])
nt = sum(1 for b in blocks if '\\textup{' in b[1])
print(len(blocks), 'statements; with emph:', ne, 'with textup:', nt)
c = 0
for b in blocks:
    for m in re.finditer(r'\\emph\{([^{}]{1,40})\}', b[1]):
        if c < 15:
            print('emph:', m.group(1))
        c += 1
print('emph total', c)
c = 0
for b in blocks:
    for m in re.finditer(r'\\textup\{([^{}]{1,40})\}', b[1]):
        if c < 15:
            print('textup:', m.group(1))
        c += 1
print('textup total', c)
