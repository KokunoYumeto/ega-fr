"""Write a compile stub: the IV-4 preamble plus the simulated (fixed) text of pp. 195-199 (crops_195_199/simulated_195_199.tex)."""
import pathlib

NATIVE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native")
HERE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4\crops_195_199")
t = (NATIVE / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = t[:t.index("\\begin{document}")]
pre = pre.replace("\\input{preamble-base}", "\\input{" + (NATIVE / "preamble-base").as_posix() + "}")
body = (HERE / "simulated_195_199.tex").read_text(encoding="utf-8")
body = body[body.index("\\oldpage[IV-4]{195}"):body.index("\\oldpage[IV-4]{200}")]
stub = pre + "\\begin{document}\n\\setcounter{section}{19}\n\\begin{enumerate}\n\\item[(ii)] on en\n" + body + "\n\\end{enumerate}\n\\end{document}\n"
(HERE / "stub_195_199.tex").write_text(stub, encoding="utf-8")
print("ok", len(stub))
