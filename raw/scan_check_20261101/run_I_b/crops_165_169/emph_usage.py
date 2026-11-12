"""Count \\emph / \\textup inside italic statement environments of EGA I (read-only)."""
import collections
import glob
import re
import sys

root = sys.argv[1]
envs = ("proposition", "corollary", "lemma", "theorem", "definition")
pat = re.compile(r"\\begin\{(%s)\}(.*?)\\end\{\1\}" % "|".join(envs), re.S)
keys = ("\\emph{", "\\textup{", "\\textrm{", "\\upshape")
cnt = collections.Counter()
ex = collections.defaultdict(list)
for f in sorted(glob.glob(root + "/ega1-*-fr.tex")):
    t = open(f, encoding="utf-8").read()
    for m in pat.finditer(t):
        body = m.group(2)
        for k in keys:
            i = body.find(k)
            n = body.count(k)
            if n:
                cnt[k] += n
                ex[k].append((f.split("\\")[-1].split("/")[-1], body[i:i + 70].replace("\n", " ")))
print(dict(cnt))
for k, v in ex.items():
    print(k, len(v))
    for a, b in v[:6]:
        print("   ", a, "|", b)
