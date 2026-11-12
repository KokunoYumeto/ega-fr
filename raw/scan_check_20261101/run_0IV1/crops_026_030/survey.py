"""Read-only survey of the IV-1 release files: markers placed right after \\begin{..}\\label, and counts of
'no~' (for the printed n degree sign) and \\cdots per file."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                 r"\diplomatic\packages\IV1\native\ega4")
pat = re.compile(r"\\begin\{(\w+)\}(\[[^\]]*\])?\s*\n\s*\\label\{[^}]*\}\s*\n\s*\\oldpage\[[^\]]*\]\{(\d+)\}")
for f in sorted(D.glob("ega0-*-fr.tex")):
    t = f.read_text(encoding="utf-8")
    hits = [(m.group(1), m.group(2), m.group(3)) for m in pat.finditer(t)]
    nos = len(re.findall(r"(?<![A-Za-z\\])no~\d", t))
    cd = t.count("\\cdots")
    print(f.name, "marker-after-label:", hits, "| no~N:", nos, "| \\cdots:", cd)
