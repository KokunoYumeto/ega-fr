import re, sys
pat = re.compile(r"\\sref\{[^}]*\}\[[^\]]*\([a-d]\)\]")
for f in sys.argv[1:]:
    t = open(f, encoding="utf-8").read()
    hits = pat.findall(t)
    print(f.split("/")[-1], len(hits), hits[:6])
