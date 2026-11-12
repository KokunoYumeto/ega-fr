import re
import glob

root = 'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/'
labels = {}
for f in sorted(glob.glob(root + '*.tex')):
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'\\label\{([^}]*)\}', s):
        labels.setdefault(m.group(1), []).append(f.split('/')[-1].split('\\')[-1])
    for m in re.finditer(r'\\EGAReaderTarget\{[^}]*\}\{([^}]*)\}', s):
        labels.setdefault(m.group(1), []).append(f.split('/')[-1].split('\\')[-1] + '(target)')
for k in ['IV.21.1', 'IV.21.6', 'IV.21.7', 'IV.21.11', 'IV.21.12', 'IV.20.1.4.1', 'IV.20.1.5.1', 'IV.20.1.3', 'IV.20.6', 'IV.21.14.1', 'section:I.7', '0.1.5.1', '0.1.4.5']:
    print(k, labels.get(k))
s = open(root + 'ega4-21a-fr.tex', encoding='utf-8').read()
for m in re.finditer(r'.{60}\\hyperref.{80}', s):
    print('HYPERREF:', m.group(0))
