import json, re, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
pat = re.compile(r"\\boldsymbol\{[^}]*\}|\\pmb\{[^}]*\}|\\bm\{[^}]*\}|\\textbf\{\\textit\{[^}]*\}\}|\\leadsto|\\bbGamma|\\mathbf\{k\}|\\mathbf\{Ab\}|\\mathit\{Ab\}")
for line in open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8"):
    x = json.loads(line)
    for m in pat.findall(x.get("new", "")):
        c[m] += 1
for k, v in c.most_common(60):
    print(v, k)
