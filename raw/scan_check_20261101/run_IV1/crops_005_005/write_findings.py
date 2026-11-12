"""Write findings_005_005.json for printed p. 5 of EGA IV-1 and check the fixes.

Usage: python -I write_findings.py
"""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV1")
R20 = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20")
SOURCES = [
    R20 / "diplomatic" / "packages" / "IV1" / "native" / "ega4" / "ega0-14-fr.tex",
    R20 / "current" / "packages" / "IV1" / "native" / "ega4" / "ega0-14-fr.tex",
]
OUT = RUN / "findings_005_005.json"

F = []


def add(where, scan, tex, kind, convention, confidence, old, new, note):
    F.append({
        "page": 5,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": {"old": old, "new": new},
        "note": note,
    })


add("page marker (first line of the page)",
    "Printed p. 5 is the opening page of CHAPITRE 0 (suite), chapter 0 of EGA IV-1 "
    "(p. 6 carries the running head 'Chap. 0'). The scan's folio reads 101; this scan series runs "
    "96 ahead of the edition's numbering (p. 222 shows 318), so the number 5 is right.",
    "\\oldpage[IV-1]{5}; every later chapter-0 page of the fascicle is \\oldpage[0\\textsubscript{IV-1}]{N}",
    "marker", None, "high",
    r"\oldpage[IV-1]{5}",
    r"\oldpage[0\textsubscript{IV-1}]{5}",
    "Use the chapter-0 label, as the edition does for the opening pages of the other chapter-0 parts: "
    "\\oldpage[0\\textsubscript{I}]{11} (ega0-1-fr.tex) and \\oldpage[0\\textsubscript{III}]{5} "
    "(ega3-1-fr.tex, also a 'CHAPITRE 0 (suite)' page). The label [IV-1] belongs to chapter IV proper, "
    "which starts at \\oldpage[IV-1]{222} (ega4-1-fr.tex). After the change, page_inventory_r20 counts "
    "p. 5 under 0_IV-1 (pp. 5-221) and IV-1 keeps pp. 222-259. Because the two labels differed, "
    "page_005.tex ran to the end of ega0-14-fr.tex (printed pp. 6-12); only the text before the p. 6 "
    "marker was compared here. Printed p. 5 ends with '... conceptions générales (2).' and footnotes (1) "
    "and (2), and printed p. 6 opens with the section 14 heading, so the p. 6 marker placed before "
    "\\setcounter{section}{13} is right.")

add("chapter heading",
    "CHAPITRE O (suite) (1): 'suite' is italic and so are its parentheses (slanted; the parentheses of "
    "the footnote mark (1) are upright)",
    "CHAPITRE 0 (suite), upright",
    "italics", None, "high",
    "CHAPITRE 0 (suite)",
    r"CHAPITRE 0 \textit{(suite)}",
    "Enlarged crop. On 0_III p. 5 the print has upright parentheses around an italic 'suite' "
    "(fixed there as (\\textit{suite}), which is right for that page); here the parentheses are italic. "
    "The 'O' is the print's figure 0.")

add("footnote (1), l. 1",
    "le symbole O_N with a bold 0",
    "$0_N$, plain 0",
    "convention", 2, "high",
    "symbole $0",
    r"symbole $\mathbf{0}",
    "Bold chapter-0 sign, as $\\mathbf{0}_{\\mathrm I}$ elsewhere in this file. The upright subscript N "
    "is the next finding (adjacent, not overlapping).")

add("footnote (1), l. 1",
    "subscript N of the bold O_N is an upright (small-capital) N",
    "$0_N$ with an italic N",
    "font", None, "high",
    "_N$ (resp.",
    r"_{\mathrm N}$ (resp.",
    "Enlarged crop. The EGA III errata footnote writes the same subscript upright: "
    "$\\mathbf{Err}_{\\mathrm N}$. Independent of the bold-0 fix just before (adjacent, not overlapping).")

add("footnote (1), l. 1",
    "(resp. Err_N): 'Err' bold upright, subscript N upright (small capital)",
    "$\\operatorname{Err}_N$: light Err, italic N",
    "font", None, "high",
    r"$\operatorname{Err}_N$",
    r"$\mathbf{Err}_{\mathrm N}$",
    "Enlarged crop. The EGA III errata footnote writes this symbol $\\mathbf{Err}_{\\mathrm N}$.")

add("footnote (1), l. 1",
    "la partie du chapitre o (resp. ...): the 0 is bold",
    "chapitre 0, plain 0",
    "convention", 2, "high",
    "chapitre 0 (resp.",
    r"chapitre \textbf{0} (resp.",
    "Enlarged crop: bold chapter number 0 (old-style figure shape).")

add("footnote (1), l. 2",
    "jointe au chapitre N. with an upright roman N",
    "$N$ (math italic)",
    "font", None, "high",
    "jointe au chapitre\n$N$.}",
    "jointe au chapitre\nN.}",
    "Enlarged crop. The EGA III errata footnote also has 'chapitre N' in text.")


def count(text, s):
    return text.count(s)


raw = (RUN / "page_005.tex").read_bytes().decode("utf-8")
print("page_005.tex CRLF:", raw.count("\r\n"), "lone CR:", raw.replace("\r\n", "").count("\r"))
page = raw.replace("\r\n", "\n")
ok = True
for f in F:
    n = count(page, f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE in page_005.tex:", n, repr(f["fix"]["old"]))
for src in SOURCES:
    text = src.read_bytes().decode("utf-8")
    print(src.parent.parent.parent.parent.parent.name, "CR:", "\r" in text)
    for f in F:
        n = count(text, f["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE in", src, n, repr(f["fix"]["old"]))
    # apply in order and check each later old still occurs exactly once
    t = text
    for f in F:
        if count(t, f["fix"]["old"]) != 1:
            ok = False
            print("ORDER PROBLEM", src, repr(f["fix"]["old"]))
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
    # and in reverse order
    t = text
    for f in reversed(F):
        if count(t, f["fix"]["old"]) != 1:
            ok = False
            print("REVERSE ORDER PROBLEM", src, repr(f["fix"]["old"]))
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT, len(F), "findings; all checks ok:", ok)
