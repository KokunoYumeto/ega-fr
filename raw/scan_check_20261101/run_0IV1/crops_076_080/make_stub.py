"""Write stub_sim_076_081.tex: the IV1 preamble plus the simulated pages 76-81
(sim_075_081.tex), for a compile test in this folder only."""
PRE = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\EGA_IV1_FR.tex"
HERE = r"user\Documents\ega_scan_check_20261101\run_0IV1\crops_076_080"

pre = open(PRE, encoding="utf-8").read()
pre = pre[: pre.index(r"\begin{document}")]
sim = open(HERE + r"\sim_075_081.tex", encoding="utf-8").read()
body = sim[sim.index(r"\oldpage[0\textsubscript{IV-1}]{76}"):]
stub = pre + "\\begin{document}\n\\begin{proof}\n" + body + "\n\\end{document}\n"
open(HERE + r"\stub_sim_076_081.tex", "w", encoding="utf-8", newline="\n").write(stub)
print(len(stub))
