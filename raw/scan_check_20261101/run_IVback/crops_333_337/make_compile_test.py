import json
import os
import re

base = r"user/Documents/ega_scan_check_20261101/run_IVback/"
pkg = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/"
src = pkg + "ega4/"
out = base + "crops_333_337/compile_test/"
os.makedirs(out + "ega4", exist_ok=True)

srcfile = {333: "ega4-backmatter-bibliography-fr.tex",
           334: "ega4-backmatter-notation-fr.tex",
           335: "ega4-backmatter-notation-fr.tex",
           336: "ega4-backmatter-terminology-fr.tex",
           337: "ega4-backmatter-terminology-fr.tex"}
texts = {f: open(src + f, encoding="utf-8").read() for f in set(srcfile.values())}
F = json.load(open(base + "findings_333_337.json", encoding="utf-8"))
for x in F:
    if x["fix"]:
        f = srcfile[x["page"]]
        assert texts[f].count(x["fix"]["old"]) == 1
        texts[f] = texts[f].replace(x["fix"]["old"], x["fix"]["new"], 1)
for f, t in texts.items():
    open(out + "ega4/" + f, "w", encoding="utf-8", newline="\n").write(t)

pre = open(src + "EGA_IV4_FR.tex", encoding="utf-8").read()
pre = pre.split("\\begin{document}")[0]
open(out + "preamble-base.tex", "w", encoding="utf-8", newline="\n").write(
    open(pkg + "preamble-base.tex", encoding="utf-8").read())
body = ("\\begin{document}\n"
        "Test \\cite{IV-41}.\n"
        "\\input{ega4/ega4-backmatter-bibliography-fr.tex}\n"
        "\\input{ega4/ega4-backmatter-notation-fr.tex}\n"
        "\\input{ega4/ega4-backmatter-terminology-fr.tex}\n"
        "\\end{document}\n")
open(out + "test_backmatter.tex", "w", encoding="utf-8", newline="\n").write(pre + body)
print("written")
