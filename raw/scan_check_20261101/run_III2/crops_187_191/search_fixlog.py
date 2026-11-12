import json
import re
import sys

# usage: search_fixlog.py FIXLOG PATTERN_NEW [PATTERN_OLD_EXCLUDE] [LIMIT]
# In the patterns, write the letter sequence BS for one literal backslash character.
BS = chr(92)


def conv(p):
    return p.replace('BS', re.escape(BS))


path = sys.argv[1]
pat_new = re.compile(conv(sys.argv[2]))
pat_old = re.compile(conv(sys.argv[3])) if len(sys.argv) > 3 and sys.argv[3] else None
limit = int(sys.argv[4]) if len(sys.argv) > 4 else 15
n = 0
for line in open(path, encoding='utf-8'):
    d = json.loads(line)
    if pat_new.search(d['new']) and not (pat_old and pat_old.search(d['old'])):
        n += 1
        if n <= limit:
            sys.stdout.buffer.write((str(d['page']) + ' ' + d['file'][-14:] + ' ' + repr(d['old'][:110]) + ' => ' + repr(d['new'][:130]) + '\n').encode('utf-8'))
print(n)
