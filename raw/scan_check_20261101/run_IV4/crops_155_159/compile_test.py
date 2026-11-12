"""Apply findings_155_159.json to a copy of the p. 155-159 segment and write a compile test (no source edits)."""
import json
import pathlib
import re
import shutil

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
OUT = RUN / "crops_155_159"
PKG = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native")
src = (PKG / "ega4" / "ega4-18-fr.tex").read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", src)]
segs = {}
for i, (n, s) in enumerate(cuts):
    if 155 <= n <= 159:
        segs[n] = src[s:cuts[i + 1][1]]
for x in json.load(open(RUN / "findings_155_159.json", encoding="utf-8")):
    fx = x["fix"]
    if fx:
        assert segs[x["page"]].count(fx["old"]) == 1, (x["page"], fx["old"])
        segs[x["page"]] = segs[x["page"]].replace(fx["old"], fx["new"])
body = "".join(segs[n] for n in range(155, 160))
pre_t = (PKG / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre_t[:pre_t.index("\\begin{document}")]
shutil.copy(PKG / "preamble-base.tex", OUT / "preamble-base.tex")
(OUT / "seg_fixed.tex").write_text(body, encoding="utf-8", newline="\n")
test = pre + "\\begin{document}\n\\setcounter{section}{18}\n\\begin{remark}[18.9.7.6]\n" + body + "\n\\end{document}\n"
(OUT / "compile_test.tex").write_text(test, encoding="utf-8", newline="\n")
print("written", len(body))
