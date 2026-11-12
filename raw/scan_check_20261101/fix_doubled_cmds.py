"""Remove doubled one-argument font commands left by the automatic port (\\boldsymbol \\boldsymbol k -> \\boldsymbol k),
in the given trees.  usage: python -I fix_doubled_cmds.py DIR [DIR ...] [--dry]"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
dry = "--dry" in sys.argv
PAT = re.compile(r"\\(boldsymbol|mathbf|mathscr|mathcal|mathfrak|mathrm|mathit|widetilde|widehat|overline|textbf|emph)"
                 r"\s*\\\1(?![A-Za-z])")
n = 0
for d in [a for a in sys.argv[1:] if not a.startswith("--")]:
    for f in pathlib.Path(d).rglob("*.tex"):
        t = f.read_text(encoding="utf-8")
        k = len(PAT.findall(t))
        if k:
            n += k
            print(f, k)
            if not dry:
                f.write_text(PAT.sub(lambda m: "\\" + m.group(1), t), encoding="utf-8", newline="")
print("fixed", n, "(dry run)" if dry else "")
