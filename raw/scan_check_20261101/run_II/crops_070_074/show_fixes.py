import json, sys
# Print page, kind, convention and old -> new of every finding, for review.
p = r'user\Documents\ega_scan_check_20261101\run_II\findings_070_074.json'
d = json.load(open(p, encoding='utf-8'))
out = sys.stdout.buffer
for i, x in enumerate(d):
    fx = x['fix']
    out.write(('%2d p%d %-17s %-4s %r -> %r%s\n' % (
        i, x['page'], x['kind'], x['convention'], fx['old'], fx['new'],
        ('  CORR=%r' % x['corrected']) if 'corrected' in x else '')).encode('utf-8'))
