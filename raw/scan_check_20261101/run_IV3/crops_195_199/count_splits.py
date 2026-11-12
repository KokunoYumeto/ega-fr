import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')
d = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4'
split = re.compile(r'([A-Za-zéèàùâêîôûçï]+)-\n(\\oldpage\[[^\]]*\]\{\d+\})\n([A-Za-zéèàùâêîôûçï]+)')
joined = re.compile(r'([A-Za-zéèàùâêîôûçï]+)-?(\\oldpage\[[^\]]*\]\{\d+\})([A-Za-zéèàùâêîôûçï]+)')
for fn in sorted(glob.glob(d + r'\ega4-*.tex')):
    t = open(fn, encoding='utf-8').read()
    a = split.findall(t)
    b = joined.findall(t)
    if a or b:
        print(fn.split('\\')[-1], 'split-with-newlines:', len(a), [x[0] + '-|' + x[2] + ' ' + x[1] for x in a][:6], 'joined:', len(b), b[:3])
