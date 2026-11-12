import json, sys
SRC = r"user/Documents/ega_scan_check_20261101/ega-fr/source/ega4/ega0-21-fr.tex"
FND = r"user/Documents/ega_scan_check_20261101/run_0IV1/findings_176_180.json"
s = open(SRC, encoding="utf-8").read()
findings = json.load(open(FND, encoding="utf-8"))
# restrict each edit to its page segment: from \oldpage{N} to \oldpage{N+1}
def seg(text, n):
    a = text.find(r"\oldpage[0\textsubscript{IV-1}]{%d}" % n)
    b = text.find(r"\oldpage[0\textsubscript{IV-1}]{%d}" % (n + 1))
    return a, b
for f in findings:
    fx = f["fix"]
    if not fx:
        continue
    a, b = seg(s, f["page"])
    # the p.178 part-1 edit ends right before the p.179 marker; allow b inclusive
    region = s[a:b]
    c = region.count(fx["old"])
    if c != 1:
        print("PROBLEM p", f["page"], c, repr(fx["old"][:70]))
        continue
    i = a + region.find(fx["old"])
    s = s[:i] + fx["new"] + s[i + len(fx["old"]):]
out = sys.argv[1] if len(sys.argv) > 1 else None
a = s.find("Il suffit de prouver qu'un")
b = s.find(r"\oldpage[0\textsubscript{IV-1}]{181}")
text = s[a:b + 60]
if out:
    open(out, "w", encoding="utf-8", newline="\n").write(text)
print("simulated region length", len(text))
