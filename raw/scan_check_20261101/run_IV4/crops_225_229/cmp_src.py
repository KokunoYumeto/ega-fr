import difflib
src = "user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
run = "user/Documents/ega_scan_check_20261101/run_IV4/"


def rd(p):
    return open(p, encoding='utf-8', newline='').read().replace('\r\n', '\n')


s18 = rd(src + "ega4-18-fr.tex")
s20 = rd(src + "ega4-20-fr.tex")
i = s18.index("\\oldpage[IV-4]{225}")
seg = s18[i:]
j = s20.index("\\oldpage[IV-4]{226}")
pre20 = s20[:j]
t = rd(run + "page_225.tex")
body = t.split('\n', 1)[1]
k = body.index("% (continued in ega4-20-fr.tex")
part1 = body[:k]
part2 = body[k:].split('\n', 1)[1]
print("225 part1 == src:", part1 == seg or part1.rstrip('\n') == seg.rstrip('\n'))
if part1.rstrip('\n') != seg.rstrip('\n'):
    for l in difflib.unified_diff(seg.splitlines(), part1.splitlines(), lineterm=''):
        print(l)
print("225 part2 == src pre-marker of ega4-20:", part2 == pre20)
if part2 != pre20:
    for l in difflib.unified_diff(pre20.splitlines(), part2.splitlines(), lineterm=''):
        print(l)
marks = [s20.index("\\oldpage[IV-4]{%d}" % n) for n in [226, 227, 228, 229, 230]]
for n, (a, b) in zip([226, 227, 228, 229], zip(marks, marks[1:])):
    seg = s20[a:b]
    t = rd(run + "page_%d.tex" % n).split('\n', 1)[1]
    print(n, t == seg)
    if t != seg:
        for l in difflib.unified_diff(seg.splitlines(), t.splitlines(), lineterm=''):
            print(l)
