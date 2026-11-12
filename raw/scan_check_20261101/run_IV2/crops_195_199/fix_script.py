p = r'user\Documents\ega_scan_check_20261101\run_IV2\crops_195_199\make_findings.py'
lines = open(p, encoding='utf-8', newline='').read().split('\n')
out = []
i = 0
while i < len(lines):
    ln = lines[i]
    if ln.rstrip('\r').endswith(".read().replace('") and 'page_%03d.tex' % () if False else ln.rstrip('\r').endswith(".read().replace('"):
        # broken 3-line construct: join and replace with the CRLF->LF normalisation
        indent = ln[:len(ln) - len(ln.lstrip())]
        out.append(indent + "t = open(os.path.join(RUN, 'page_%03d.tex' % pg), encoding='utf-8', newline='').read().replace(CRLF, LF)")
        i += 3
        continue
    out.append(ln)
    i += 1
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(out))
print('ok')
