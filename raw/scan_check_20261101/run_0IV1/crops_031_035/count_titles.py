"""Count \\subsection titles in the chapter-0 IV source files and how many end with a full stop."""
import glob
import re

ROOT = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4"
pat = re.compile(r"\\subsection(\[[^\]]*\])?\{")
tot = stop = 0
for f in sorted(glob.glob(ROOT + r"\ega0-*.tex")):
    s = open(f, encoding="utf-8").read()
    for m in pat.finditer(s):
        i, depth = m.end(), 1
        while depth and i < len(s):
            if s[i] == "{":
                depth += 1
            elif s[i] == "}":
                depth -= 1
            i += 1
        title = s[m.end():i - 1]
        tot += 1
        if title.rstrip().endswith("."):
            stop += 1
print("subsections", tot, "ending with full stop", stop)
