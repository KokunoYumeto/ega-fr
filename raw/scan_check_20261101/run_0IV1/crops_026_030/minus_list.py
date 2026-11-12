"""List minus signs inside math in page_NNN.tex files: python minus_list.py 21 22 ...  (read-only)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(__file__).resolve().parent.parent
math = re.compile(r"\$[^$]+\$|\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}", re.S)
for n in sys.argv[1:]:
    t = (RUN / f"page_{int(n):03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    t = re.sub(r"\\(label|tag|ref)\{[^}]*\}", "", t)
    k = 0
    for m in math.finditer(t):
        s = m.group(0)
        for mm in re.finditer(r"-", s):
            k += 1
            print(n, repr(s[max(0, mm.start() - 18):mm.end() + 10]))
    print(n, "total", k)
