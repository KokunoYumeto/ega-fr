base = r"user\Documents\ega_scan_check_20261101"
pre = open(base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\EGA_IV4_FR.tex", encoding="utf-8").read()
head = pre.split(r"\begin{document}")[0]
pb = base.replace("\\", "/") + "/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/preamble-base"
head = head.replace(r"\input{preamble-base}", r"\input{" + pb + "}")
start = r"\begin{document}" + "\n" + r"\setcounter{section}{17}" + "\n"
end = "\n" + r"\end{document}" + "\n"
body = "".join(open(base + r"\run_IV4\crops_160_164\applied_%d.tex" % n, encoding="utf-8").read() for n in range(160, 165))
open(base + r"\run_IV4\crops_160_164\test_applied.tex", "w", encoding="utf-8", newline="\n").write(head + start + body + end)
orig = "".join(open(base + r"\run_IV4\page_%03d.tex" % n, encoding="utf-8").read().replace("\r\n", "\n").split("\n", 1)[1] for n in range(160, 165))
open(base + r"\run_IV4\crops_160_164\test_orig.tex", "w", encoding="utf-8", newline="\n").write(head + start + orig + end)
print("ok")
