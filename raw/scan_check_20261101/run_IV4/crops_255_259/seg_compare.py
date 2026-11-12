import re
base = r"user\Documents\ega_scan_check_20261101"
src_dir = base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4"
run = base + r"\run_IV4"

def read(p):
    with open(p, encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')

s20 = read(src_dir + r"\ega4-20-fr.tex")
s21 = read(src_dir + r"\ega4-21a-fr.tex")

def seg(src, start_marker, end_marker):
    i = src.index(start_marker)
    j = src.index(end_marker) if end_marker else len(src)
    return src[i:j]

for n in range(255, 260):
    page = read(run + rf"\page_{n}.tex")
    body = page.split('\n', 1)[1]  # drop '% from' line
    if n == 255:
        a = seg(s20, r"\oldpage[IV-4]{255}", None)
        b = s21[:s21.index(r"\oldpage[IV-4]{256}")]
        # page file has the continuation after a comment line
        parts = body.split('% (continued in ega4-21a-fr.tex, before its first page marker)\n')
        print(n, 'part A same:', parts[0].rstrip('\n') == a.rstrip('\n'), ' part B same:', parts[1].rstrip('\n') == b.rstrip('\n'))
    else:
        a = seg(s21, rf"\oldpage[IV-4]{{{n}}}", rf"\oldpage[IV-4]{{{n+1}}}")
        print(n, 'same:', body.rstrip('\n') == a.rstrip('\n'), len(body), len(a))
