import pathlib

crops = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_IVback/crops_350_354")
native = pathlib.Path(r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
                      r"diplomatic/packages/IV4/native")
pre = (native / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre[:pre.index("\\begin{document}")]
pre = pre.replace("\\input{preamble-base}", "\\input{" + (native / "preamble-base").as_posix() + "}")
for name, src in (("stub_350_354_after.tex", crops / "simulated_errata_after_fixes.tex"),
                  ("stub_350_354_before.tex", native / "ega4" / "ega4-errata-addenda-list3-fr.tex")):
    sim = src.read_text(encoding="utf-8")
    a = sim.index("\\begin{remark}[4.2.1.4]")
    b = sim.index("\\end{proof}", sim.index("\\oldpage[IV]{355}")) + len("\\end{proof}")
    stub = pre + "\\begin{document}\n" + sim[a:b] + "\n\\end{document}\n"
    (crops / name).write_text(stub, encoding="utf-8", newline="\n")
    print(name, b - a)
