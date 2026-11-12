"""Count \\subsection titles (with/without final full stop) and 'no~N' numero spellings in the EGA IV-1 files."""
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
pat = re.compile(r"\\subsection\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}")
for f in sorted(root.glob("ega*-fr.tex")):
    t = f.read_text(encoding="utf-8")
    titles = pat.findall(t)
    dot = sum(1 for x in titles if x.rstrip().endswith("."))
    nos = len(re.findall(r"\bno~\d", t))
    sup = t.count("n\\textsuperscript{o}")
    cd = t.count("\\cdots")
    print(f.name, "subsections", len(titles), "with final stop", dot, "| no~N", nos, "| n^o", sup, "| \\cdots", cd)
