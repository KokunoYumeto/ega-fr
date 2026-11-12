import glob, re, sys
pat = re.compile(r'\\begin\{(proof|env|proposition|lemma|corollary|theorem|definition|remark)\}(\[[^\]]*\])?\s*\Z')
t = open(r'user\Documents\ega_scan_check_20261101\run_0IV1\page_139.tex', encoding='utf-8').read()
print(bool(pat.search(t)))
n = 0
for f in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\page_*.tex')):
    t = open(f, encoding='utf-8').read()
    if pat.search(t):
        n += 1
        print(f, repr(t[-50:]))
print(n)
