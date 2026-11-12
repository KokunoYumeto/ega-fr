import pathlib
import re

d = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4")
pat = re.compile(r"\\end\{(enumerate|itemize)\}\n(?!\s*\n)(?![\\%])(\S.{0,40})")
for f in sorted(d.glob("ega4-*.tex")):
    t = f.read_text(encoding="utf-8")
    hits = pat.findall(t)
    print(f.name, len(hits), [h[1][:30] for h in hits[:6]])
