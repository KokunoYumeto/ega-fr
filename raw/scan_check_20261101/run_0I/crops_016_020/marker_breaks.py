"""Count \\oldpage markers preceded by a blank line whose following text starts in lower case (candidate
spurious paragraph breaks at mid-sentence page boundaries) in the ega-fr diplomatic sources."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = (pathlib.Path(__file__).resolve().parents[2] / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic"
        / "packages" / "BASE" / "native")
pat = re.compile(r"\n[ \t]*\n(\\oldpage\[[^\]]*\]\{\d+\})[ \t]*\n((?:[ \t]*\n)?)([^\n]{0,40})")
tot = 0
for f in sorted(ROOT.glob("ega*/*.tex")):
    t = f.read_text(encoding="utf-8").replace("\r\n", "\n")
    hits = [(m.group(1), bool(m.group(2)), m.group(3)) for m in pat.finditer(t)
            if re.match(r"[a-zà-ÿ$(]", m.group(3))]
    if hits:
        tot += len(hits)
        print(f.relative_to(ROOT), len(hits), [h[0].split("]", 1)[1] + ("+blank" if h[1] else "") for h in hits][:15])
print("total", tot)
