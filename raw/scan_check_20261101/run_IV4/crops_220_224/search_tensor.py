import re, glob, sys
root = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages"
pat = re.compile(r"otimes_\{?\\(?:sh|mathcal|mathscr)\s*\{?O\}?_\{?X[^}$]{0,12}\}?\s*\\?(?:boldsymbol\{k\}|mathbf\{k\}|mathbf k|k|kappa)\s*\(")
for f in sorted(glob.glob(root + r"\IV*\native\**\*.tex", recursive=True)):
    t = open(f, encoding="utf-8").read()
    for m in pat.finditer(t):
        s = max(0, m.start() - 90)
        sys.stdout.buffer.write((f.split("packages")[1] + " ... " + t[s:m.end() + 25].replace("\n", " ") + "\n").encode("utf-8"))
