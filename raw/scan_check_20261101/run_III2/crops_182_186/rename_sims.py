"""Rename this checker's simulated-result files sim_NNN.tex to sim_NNN.txt (they are scratch output, not sources)."""
import os
import pathlib

here = pathlib.Path(__file__).resolve().parent
for p in sorted(here.glob("sim_*.tex")):
    os.replace(p, p.with_suffix(".txt"))
    print(p.name, "->", p.with_suffix(".txt").name)
b = here / "build_findings.py"
s = b.read_text(encoding="utf-8")
s = s.replace('f"sim_{p}.tex"', 'f"sim_{p}.txt"')
b.write_text(s, encoding="utf-8")
