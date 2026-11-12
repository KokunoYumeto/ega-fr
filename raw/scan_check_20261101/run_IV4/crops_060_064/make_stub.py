# Write stub documents (original and fixed pp. 60-64) with the IV-4 preamble, for a compile check.
from pathlib import Path

PRE = Path(r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native")
HERE = Path(__file__).resolve().parent

main = (PRE / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
head = main.split(r"\begin{document}")[0]
head = head.replace(r"\input{preamble-base}", r"\input{" + (PRE / "preamble-base.tex").as_posix() + "}")
assert r"\begin{document}" not in head

for tag in ("orig", "fixed"):
    body = []
    for n in (60, 61, 62, 63, 64):
        if tag == "orig":
            t = (HERE.parent / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        else:
            t = (HERE / f"fixed_{n:03d}.tex").read_text(encoding="utf-8")
        body.append(t.split("\n", 1)[1])
    doc = (head + r"\begin{document}" + "\n" + r"\setcounter{section}{16}" + "\n" + r"\section{Stub}" + "\n"
           + "".join(body) + "\n" + r"\end{document}" + "\n")
    (HERE / f"stub_{tag}.tex").write_text(doc, encoding="utf-8")
    print(tag, len(doc))
