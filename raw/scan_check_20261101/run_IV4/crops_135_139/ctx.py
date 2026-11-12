import sys, re
sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex'
src = open(SRC, encoding='utf-8', newline='').read()
for s in sys.argv[1:]:
    print('=====', s, src.count(s))
    i = -1
    while True:
        i = src.find(s, i + 1)
        if i < 0: break
        print('  ...', src[max(0, i-90):i+len(s)+90].replace('\n', '\n'))
