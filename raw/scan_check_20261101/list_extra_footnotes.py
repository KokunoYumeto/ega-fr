"""Footnotes of the corrected French edition that the diplomatic edition (the print) does not have.
usage: python -I list_extra_footnotes.py"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(__file__).parent / "ega-fr" / "editions" / "2026-10-24-r20"
BS = chr(92)


def footnotes(t):
    out, i = [], 0
    while True:
        i = t.find(BS + "footnote{", i)
        if i < 0:
            return out
        d, k = 0, i + len(BS + "footnote")
        for k in range(k, len(t)):
            if t[k] == "{":
                d += 1
            elif t[k] == "}":
                d -= 1
                if d == 0:
                    break
        out.append((i, t[i:k + 1]))
        i = k + 1


for f in sorted((B / "current" / "packages").rglob("*-fr.tex")):
    rel = f.relative_to(B / "current" / "packages")
    g = B / "diplomatic" / "packages" / rel
    if not g.exists():
        continue
    cur = footnotes(f.read_text(encoding="utf-8"))
    dip = {x for _, x in footnotes(g.read_text(encoding="utf-8"))}
    for pos, x in cur:
        if x not in dip:
            t = f.read_text(encoding="utf-8")
            marks = [m for m in range(0, pos) if t.startswith(BS + "oldpage[", m)]
            page = t[marks[-1]:t.find("}", marks[-1]) + 1] if marks else "?"
            print(rel, page, "|", x[:400].replace("\n", " "))
            print()
