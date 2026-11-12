"""Count {\\hyperlink..}/{\\hyperref..} references inside italic statement environments of the errata file."""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
fn = sys.argv[1]
t = open(fn, encoding="utf-8").read()
env = re.compile(r"\\begin\{(proposition|corollary|lemma|theorem|definition)\}(.*?)\\end\{\1\}", re.S)
ref = re.compile(r"\{\\hyper(?:link|ref)(?:\{[^}]*\}|\[[^\]]*\])\{[^}]*\}\}")
for m in env.finditer(t):
    body = m.group(2)
    refs = ref.findall(body)
    line = t[: m.start()].count("\n") + 1
    print(line, m.group(1), len(refs), refs[:4])
