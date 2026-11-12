"""0_IV p. 89 (proof of 19.4.7): the print has the Fraktur K of the open ideal (B_0/KB_0) throughout; the French TeX
kept \\mathfrak R in "(B_0/\\mathfrak RB_0)" three times (transcription error, found by the English slips agent and
checked on the scan). Fix both French editions and both Spanish IV-1 editions; log FIXLOG.jsonl / FIXLOG_CURRENT.jsonl.
usage: python -I fix_0IV_p89.py [--apply]"""
import json
import pathlib
import sys

E = pathlib.Path(__file__).parent
BS = chr(92)
OLD, NEW = BS + "mathfrak RB_0", BS + "mathfrak KB_0"
B = E / "ega-fr" / "editions" / "2026-10-24-r20"
TARGETS = [
    (B / "diplomatic" / "packages" / "IV1" / "native" / "ega4" / "ega0-19-fr.tex", "FIXLOG.jsonl"),
    (B / "current" / "packages" / "IV1" / "native" / "ega4" / "ega0-19-fr.tex", "FIXLOG_CURRENT.jsonl"),
    (E / "ega-fga-es" / "editions" / "IV1_CURRENT" / "ega4" / "ega0-19-es.tex", "PORT_ES_CURRENT_LOG.jsonl"),
    (E / "ega-fga-es" / "editions" / "IV1_DIPLOMATIC" / "ega4" / "ega0-19-es.tex", "PORT_ES_DIPLOMATIC_LOG.jsonl"),
]
MARK = BS + "oldpage[0" + BS + "textsubscript{IV-1}]{"
apply = "--apply" in sys.argv
for f, log in TARGETS:
    t = f.read_text(encoding="utf-8")
    a = t.find(MARK + "89}")
    b = t.find(MARK + "90}")
    if a < 0 or b < a:
        print(f.name, "page 89 not found")
        continue
    seg = t[a:b]
    n = seg.count(OLD)
    print(f, "occurrences on p. 89:", n)
    if apply and n:
        f.write_text(t[:a] + seg.replace(OLD, NEW) + t[b:], encoding="utf-8", newline="")
        with open(E / log, "a", encoding="utf-8") as fh:
            for _ in range(n):
                fh.write(json.dumps({"file": str(f), "part": "0" + BS + "textsubscript{IV-1}", "page": 89, "old": OLD,
                                     "new": NEW, "source": "slips_0IV_19_20 (checked on the scan)"},
                                    ensure_ascii=False) + "\n")
