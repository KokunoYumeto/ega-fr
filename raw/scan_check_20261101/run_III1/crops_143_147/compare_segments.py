"""Compare the page_NNN.tex copies (143-147) with the matching segments of the diplomatic release file and the source."""
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
DIP = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex"
SRC = E / r"ega-fr\source\ega3\ega3-1-fr.tex"
MARK = re.compile(r"\\oldpage\[III\]\{(\d+)\}")


def segs(t):
    cuts = [(int(x.group(1)), x.start()) for x in MARK.finditer(t)]
    out = {}
    for i, (n, st) in enumerate(cuts):
        out.setdefault(n, []).append(t[st: cuts[i + 1][1] if i + 1 < len(cuts) else len(t)])
    return out


d = DIP.read_text(encoding="utf-8")
s = SRC.read_text(encoding="utf-8")
D, S = segs(d), segs(s)
print("markers 140-148 in diplomatic:", [n for n in range(140, 149) if n in D])
print("markers 140-148 in source:   ", [n for n in range(140, 149) if n in S])
print("diplomatic == source:", d == s, len(d), len(s))
for n in range(143, 148):
    p = (E / "run_III1" / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = p.split("\n", 1)[1]
    print(n, "count in dip:", len(D.get(n, [])), "page==dip:", body == D[n][0], "page==src:", body == S[n][0])
