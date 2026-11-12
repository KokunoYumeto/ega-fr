import re, sys
path = sys.argv[1]
t = open(path, encoding='utf-8').read().replace('\r\n', '\n')
envs = 'lemma|proposition|corollary|theorem|definition'
pat = re.compile(r'\\begin\{(' + envs + r')\}(\[[^\]]*\])?(.*?)\\end\{\1\}', re.S)
starts = ('En effet', 'On a en effet', 'Il suffit', "D'apr", 'Or,', 'Comme ')
for m in pat.finditer(t):
    body = m.group(3)
    paras = re.split(r'\n\s*\n', body)
    for para in paras[1:]:
        s = para.strip()
        if s.startswith(starts):
            line = t[:m.start()].count('\n') + 1
            print(m.group(1), m.group(2), 'line', line, '|', s[:70].replace('\n', ' '))
