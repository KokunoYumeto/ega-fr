"""Report fixes whose old string occurs more than once in the whole current ega4-21b-fr.tex."""
import json
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parent
R = D.parent
SRC = (R.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV4" / "native"
       / "ega4" / "ega4-21b-fr.tex")
t = SRC.read_text(encoding="utf-8")
for i, x in enumerate(json.loads((R / "findings_275_279.json").read_text(encoding="utf-8"))):
    f = x.get("fix")
    if f:
        c = t.count(f["old"])
        if c != 1:
            sys.stdout.buffer.write(f"{i} p{x['page']} file-wide count {c}: {f['old'][:90]!r}\n".encode("utf-8"))
print("done")
