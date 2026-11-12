import pathlib
p = pathlib.Path('build_findings.py')
t = p.read_text(encoding='utf-8')
bs = chr(92)
old = bs + bs + 'boldsymbol{' + bs + 'mathsf{Y}}'
new = bs + bs + 'boldsymbol{' + bs + bs + 'mathsf{Y}}'
n = t.count(old)
t = t.replace(old, new)
t = t.replace('(findings_260_264); ' + new + ' as there.',
              '(findings_260_264); written ' + new + ' (heavy sans-serif; coordinator decision, 4 Nov).')
p.write_text(t, encoding='utf-8')
print(n)
