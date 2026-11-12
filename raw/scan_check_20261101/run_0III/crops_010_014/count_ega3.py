import re
from pathlib import Path

t = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega3\ega3-1-fr.tex").read_text(encoding="utf-8")
n = envs = 0
for m in re.finditer(r"\\begin\{(definition|proposition|theorem|corollary|lemma)\}(.*?)\\end\{\1\}", t, re.S):
    envs += 1
    n += m.group(2).count("\\emph{")
print("italic statement envs:", envs, " \\emph inside them:", n)
print("$C$:", t.count("$C$"), " standalone C letters:", len(re.findall(r"(?<![A-Za-z\\])C(?![A-Za-z])", t)))
print("mapsto:", t.count("\\mapsto"), " mathrm{Ens}:", t.count("\\mathrm{Ens}"), " setminus:", t.count("\\setminus"))
