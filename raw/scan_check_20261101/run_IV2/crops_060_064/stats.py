"""Small counts in the IV-2 source used for the final note (read-only)."""
import re
from pathlib import Path

src = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex").read_text(encoding="utf-8")
pre = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\EGA_IV2_FR.tex").read_text(encoding="utf-8")
titles = re.findall(r"\\subsection\*?\{(.*?)\}\s*\n\\label", src, re.S)
print("subsection titles:", len(titles), "ending with a full stop:", sum(1 for t in titles if t.rstrip().endswith(".")))
print("\\setmin in ega4-2-fr.tex:", src.count("\\setmin"), "| defined in EGA_IV2_FR.tex:", "setmin" in pre)
print("\\leadsto:", src.count("\\leadsto"), "| \\mapsto:", src.count("\\mapsto"))
print("'Pour (i),' lines:", [i + 1 for i, l in enumerate(src.split("\n")) if l.startswith("Pour (i),") or l.startswith("Pour (ii),")])
