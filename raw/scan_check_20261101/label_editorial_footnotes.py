"""Two editorial footnotes of the corrected French edition (not in the print) carry no label, unlike the other three
("Correction éditoriale :", "Précision éditoriale :", "Note de correction."): label them, so that no added note can be
taken for the print's. Logged to FIXLOG_CURRENT.jsonl.
usage: python -I label_editorial_footnotes.py [--apply]"""
import json
import pathlib
import sys

E = pathlib.Path(__file__).parent
C = E / "ega-fr" / "editions" / "2026-10-24-r20" / "current" / "packages"
BS = chr(92)
ITEMS = [
    (C / "IV1" / "native" / "ega4" / "ega0-15-fr.tex", "0" + BS + "textsubscript{IV-1}", 17,
     BS + "footnote{La régularité de $f_n$", BS + "footnote{Précision éditoriale : la régularité de $f_n$"),
    (C / "IV2" / "native" / "ega4" / "ega4-2-fr.tex", "IV-2", 177,
     BS + "footnote{Le texte imprimé omet le carré", BS + "footnote{Correction éditoriale : le texte imprimé omet le carré"),
]
apply = "--apply" in sys.argv
for f, part, page, old, new in ITEMS:
    t = f.read_text(encoding="utf-8")
    n = t.count(old)
    print(f.name, n)
    if apply and n == 1:
        f.write_text(t.replace(old, new), encoding="utf-8", newline="")
        with open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"file": str(f), "part": part, "page": page, "old": old, "new": new,
                                 "source": "editorial_footnote_label",
                                 "why": "An added note of the corrected edition is labelled as such."},
                                ensure_ascii=False) + "\n")
