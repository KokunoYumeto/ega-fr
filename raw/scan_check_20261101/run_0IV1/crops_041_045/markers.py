import re, sys
sys.stdout.reconfigure(encoding='utf-8')
path = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega0-17-fr.tex'
t = open(path, encoding='utf-8', newline='').read()
print('CRLF' if '\r\n' in t else 'LF')
for m in re.finditer(r'\\oldpage\[([^\]]*)\]\{(\d+)\}', t):
    print(m.group(1), m.group(2), 'line', t[:m.start()].count('\n') + 1)
