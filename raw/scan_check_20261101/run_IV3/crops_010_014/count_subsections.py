import re
import pathlib

src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega4")
for n in range(8, 16):
    f = src / f"ega4-{n}-fr.tex"
    t = f.read_text(encoding="utf-8")
    subs = re.findall(r"\\subsection\{(.*)\}", t)
    print(f.name, len(subs), sum(1 for s in subs if s.rstrip().endswith(".")))
t = (src / "ega4-8-fr.tex").read_text(encoding="utf-8")
print("mathbf C lines:", [i + 1 for i, line in enumerate(t.split("\n")) if "\\mathbf C" in line])
