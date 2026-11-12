"""Check whether each page_NNN.tex body (without its first comment line) still occurs verbatim in the current source."""
import pathlib
import sys

run = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
for n in map(int, sys.argv[2:]):
    body = (run / f"page_{n:03d}.tex").read_text(encoding="utf-8").split("\n", 1)[1]
    print(n, "verbatim in source" if body in src else "DIFFERS from current source", len(body))
