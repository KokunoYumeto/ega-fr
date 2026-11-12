import re
import glob

root = 'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/'
for f in sorted(glob.glob(root + 'ega4-2*.tex')):
    s = open(f, encoding='utf-8').read()
    name = f.replace('\\', '/').split('/')[-1]
    print(name,
          'sref', len(re.findall(r'\\sref', s)),
          'sref[0]{', len(re.findall(r'\\sref\[0\]\{', s)),
          'sref[0\\textsubscript{I}]', len(re.findall(r'\\sref\[0\\textsubscript\{I\}\]', s)),
          '(\\sref', len(re.findall(r'\(\\sref', s)),
          'nos \\sref', len(re.findall(r'textsuperscript\{os?\} \\sref', s)),
          'isoto', len(re.findall(r'\\isoto', s)))
s = open(root + 'ega4-20-fr.tex', encoding='utf-8').read()
for i, line in enumerate(s.split('\n'), 1):
    if re.search(r'\\sref\[0\]\{', line) or re.search(r'textsuperscript\{os?\} \\sref', line):
        for m in re.finditer(r'(\\sref\[0\]\{[^}]*\}|n\\textsuperscript\{os?\} \\sref\{[^}]*\})', line):
            print(i, m.group(0))
