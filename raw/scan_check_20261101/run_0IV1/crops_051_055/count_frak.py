import re, sys
# usage: count_frak.py file letter  -> occurrences of \mathfrak{letter} per printed page
path, letter = sys.argv[1], sys.argv[2]
pat = re.compile(r'\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}')
tok = '\\mathfrak{' + letter + '}'
pg = '(before first marker)'
cnt = {}
for line in open(path, encoding='utf-8').read().split('\n'):
    m = pat.search(line)
    if m:
        # count occurrences before the marker on the same line under the old page
        pre, post = line[:m.start()], line[m.end():]
        n = pre.count(tok)
        if n:
            cnt[pg] = cnt.get(pg, 0) + n
        pg = m.group(1)
        line = post
    n = line.count(tok)
    if n:
        cnt[pg] = cnt.get(pg, 0) + n
print(path, letter, cnt, 'total', sum(cnt.values()))
