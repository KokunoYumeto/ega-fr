"""Write test_after.tex / test_before.tex: the IV-4 preamble plus pages 265-269 (fixed / unfixed)."""
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
NAT = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native"
HERE = E / r"run_IV4\crops_265_269"
pre = (NAT / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre[:pre.index("\\begin{document}")]

after = "".join((HERE / f"after_{p}.tex").read_text(encoding="utf-8") for p in range(265, 270))
before = "".join(
    (E / "run_IV4" / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n", 1)[1]
    for p in range(265, 270))
for name, body in (("test_after.tex", after), ("test_before.tex", before)):
    doc = pre + "\\begin{document}\n\\begin{proof}\n" + body + "\n\\end{document}\n"
    (HERE / name).write_text(doc, encoding="utf-8", newline="\n")
    print(name, len(doc))
