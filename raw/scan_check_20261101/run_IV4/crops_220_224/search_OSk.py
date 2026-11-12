import re, glob, sys
root = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4"
pat = re.compile(r"otimes_\{\\sh\s*\{?O\}?_\{?([SXY])[^}$]{0,12}\}?\}?\s*(?:\\boldsymbol\{k\}|\\mathbf\{?k\}?|k)\s*\(")
for f in sorted(glob.glob(root + r"\*.tex")):
    t = open(f, encoding="utf-8").read()
    for m in pat.finditer(t):
        line = t.count("\n", 0, m.start()) + 1
        s = max(0, m.start() - 50)
        sys.stdout.buffer.write((f"{f.split(chr(92))[-1]}:{line} [{m.group(1)}] ... " + t[s:m.end() + 15].replace("\n", " ") + "\n").encode("utf-8"))
