import re, sys
base = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/'
for fn in sys.argv[1:]:
    s = open(base + fn, encoding='utf-8').read()
    for m in re.finditer(r'\\oldpage\[[^\]]*\]\{(\d+)\}', s):
        before = s[max(0, m.start() - 40):m.start()].replace('\n', '\\n')
        after = s[m.end():m.end() + 40].replace('\n', '\\n')
        # markers not preceded by a newline or not followed by a newline
        if not s[m.start() - 1] == '\n' or not s[m.end()] == '\n':
            print(fn, m.group(1), '|', before, '[[M]]', after)
