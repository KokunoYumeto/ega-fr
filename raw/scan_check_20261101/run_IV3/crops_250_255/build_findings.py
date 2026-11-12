"""Build findings_250_255.json for EGA IV-3 pp. 250-255 and verify every fix:
'old' must occur exactly once in its page_NNN.tex (LF-normalised; the blank p. 252 has no page file, its edit lies in
page_251.tex) and exactly once in the current release segment found the way apply_fixes.locate() finds it.
Read-only on all .tex files."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4")
OUT = RUN / "findings_250_255.json"
PAGEFILE = {252: 251}  # page without its own page file -> file that holds the edit

F = []


def add(page, where, scan, tex, kind, conf, old, new, note, convention=None):
    F.append({"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
              "confidence": conf, "fix": None if old is None else {"old": old, "new": new}, "note": note})


# ---------------- p. 250, Index des notations ----------------
add(250, "Index des notations, first entry (8.3.9), second notation",
    "𝔒𝔠(X): Fraktur O followed by a full-size Fraktur c on the baseline (the same O as in '𝔒(X)' of the 10.1.1 entry)",
    r"$\mathfrak D_c(X)$ (Fraktur D with a subscript italic c)", "symbol", "high",
    r"$\mathfrak D_c(X)$", r"$\mathfrak{Oc}(X)$",
    "Wrong Fraktur letter and wrong c: GLOBAL_ISSUES item 79 names this place (ega4-15-terminal-fr.tex, p. 250). "
    "Same form as the pp. 15-16 page fixes in ega4-8 (\\mathfrak{Oc}) and as the body text of (8.3.9).")
add(250, "Index des notations, first entry (8.3.9), third notation",
    "𝔉𝔠(X): full-size Fraktur c on the baseline", r"$\mathfrak F_c(X)$ (subscript italic c)", "formula", "high",
    r"$\mathfrak F_c(X)$", r"$\mathfrak{Fc}(X)$",
    "GLOBAL_ISSUES item 79; same form as the ega4-8 page fixes and the body of (8.3.9).")
add(250, "Index des notations, first entry (8.3.9), fourth notation",
    "𝔏𝔉𝔠(X): full-size Fraktur c on the baseline", r"$\mathfrak{LF}_c(X)$ (subscript italic c)", "formula", "high",
    r"$\mathfrak{LF}_c(X)$", r"$\mathfrak{LFc}(X)$",
    "GLOBAL_ISSUES item 79; same form as the ega4-8 page fixes and the body of (8.3.9).")
add(250, "Index des notations, entry 8.13.3, 'Pro'",
    "Pro printed bold italic", r"$\mathbf{Pro}$ (bold upright)", "font", "high",
    r"$\mathbf{Pro}", r"$\boldsymbol{\mathit{Pro}}",
    "As in the body of (8.13.3) after the p. 50 page fixes (\\boldsymbol{\\mathit{Pro}}). Does not overlap the next edit.")
add(250, "Index des notations, entry 8.13.3, the category in Pro(C)",
    "C printed bold italic (category letter)", r"(\mathcal C) (calligraphic C)", "font", "high",
    r"(\mathcal C)$", r"(\boldsymbol{C})$",
    "Category letter C, bold italic in the print (\\boldsymbol{C}); the body of (8.13.3) has \\boldsymbol{C}.")
add(250, "Index des notations, entry 8.13.3, '(C catégorie)'",
    "C printed bold italic", r"($\mathcal C$ catégorie)", "font", "high",
    r"($\mathcal C$ catégorie)", r"($\boldsymbol{C}$ catégorie)",
    "Same letter as in Pro(C).")

# ---------------- p. 252, blank page ----------------
add(252, "printed p. 252 (between the Index terminologique and the Table des matières); the edit is in page_251.tex, "
         "between the \\oldpage[IV-3]{251} and {253} markers",
    "p. 252 is blank (scan pdf page 251: no ink at all, no page number); no text is missing",
    r"blank page set by \clearpage, \thispagestyle{empty}, \null, \clearpage, with the comment '% La page imprimée 252 "
    r"est blanche.', but no \oldpage[IV-3]{252} marker", "marker", "high",
    "blanche.\n\\thispagestyle{empty}", "blanche.\n\\oldpage[IV-3]{252}\n\\thispagestyle{empty}",
    "Markers for every printed page, blank ones included (GLOBAL_ISSUES item 32); same order as the blank pages "
    "III 216 and III 160 (\\clearpage, \\oldpage, \\thispagestyle{empty}, \\null, \\clearpage). The finding carries "
    "page 252: apply_fixes.locate() finds no 252 marker and uses the gap between the 251 and 253 markers, where "
    "'old' occurs once.")

# ---------------- p. 253, Table des matières ----------------
add(253, "Table des matières, top right above the page-number column (before the Chapitre IV line)",
    "column head 'Pages' in small capitals, short rule under it", "absent", "missing", "high",
    "\\setlength{\\parskip}{1.5pt}\n", "\\setlength{\\parskip}{1.5pt}\n\\hfill\\textsc{Pages}\\par\n",
    "GLOBAL_ISSUES item 45; same form as the EGA IV-2 contents (p. 229). Placed inside the group so that it gets "
    "\\small; it does not touch the \\newcommand line. The rule under it is layout.")
add(253, "contents macro \\EGAIVthreeContentsLine (defined on p. 253): entry labels of every contents line, pp. 253-255",
    "labels '§ 8.', '8.1.', ..., '15.7.' and 'Chapitre IV.' in medium weight", r"\textbf{#1}: every label bold",
    "font", "high",
    r"\newcommand{\EGAIVthreeContentsLine}[3]{\textbf{#1}\quad", r"\newcommand{\EGAIVthreeContentsLine}[3]{#1\quad",
    "One edit for all labels of pp. 253-255 (no separate findings on pp. 254-255). Same fix as for the EGA IV-2 "
    "contents macro.")
add(253, "contents line 'Chapitre IV. — Étude locale des schémas et des morphismes de schémas (suite) ... 5', label",
    "'Chapitre' in small capitals, 'IV.' roman, medium weight", r"CHAPITRE IV. (full capitals, bold through the macro)",
    "font", "high",
    r"\EGAIVthreeContentsLine{CHAPITRE IV.}", r"\EGAIVthreeContentsLine{\textsc{Chapitre IV.}}",
    "Same form as the EGA IV-2 contents (p. 229). Independent of the macro edit and of the dash edit (no overlap).")
add(253, "same line, between 'IV.' and 'Étude'",
    "an em dash: 'Chapitre IV. — Étude locale ...'", "no dash", "punctuation", "high",
    r"{\textbf{Étude locale", r"{--- \textbf{Étude locale",
    "As in the EGA IV-1 and IV-2 contents. With the previous edit the line reads "
    "'\\textsc{Chapitre IV.}' + '--- \\textbf{Étude locale ...} \\emph{(suite)}'.")

# ---------------- p. 254 ----------------
add(254, "top right above the page-number column (before the 9.4 entry)",
    "column head 'Pages' in small capitals, short rule under it", "absent", "missing", "high",
    r"\EGAIVthreeContentsLine{9.4.}", "\\hfill\\textsc{Pages}\n\n\\EGAIVthreeContentsLine{9.4.}",
    "Repeated on each contents page; GLOBAL_ISSUES item 45, same form as EGA IV-2 pp. 230-231. The rule under it is layout.")

# ---------------- p. 255 ----------------
add(255, "top right above the page-number column (before the 12.2 entry)",
    "column head 'Pages' in small capitals, short rule under it", "absent", "missing", "high",
    r"\EGAIVthreeContentsLine{12.2.}", "\\hfill\\textsc{Pages}\n\n\\EGAIVthreeContentsLine{12.2.}",
    "GLOBAL_ISSUES item 45, as on p. 254.")
add(255, "back-matter entry 'Bibliographie (suite) ... 249'",
    "'Bibliographie' in small capitals; '(suite)' italic", r"BIBLIOGRAPHIE (full capitals)", "font", "high",
    "BIBLIOGRAPHIE", r"\textsc{Bibliographie}",
    "As in the EGA II, III, IV-1 and IV-2 contents. The \\emph{(suite)} matches the print.")
add(255, "back-matter entry 'Index des notations ... 250'",
    "small capitals", r"INDEX DES NOTATIONS (full capitals)", "font", "high",
    "INDEX DES NOTATIONS", r"\textsc{Index des notations}",
    "As in the EGA II, IV-1 and IV-2 contents.")
add(255, "back-matter entry 'Index terminologique ... 251'",
    "small capitals", r"INDEX TERMINOLOGIQUE (full capitals)", "font", "high",
    "INDEX TERMINOLOGIQUE", r"\textsc{Index terminologique}",
    "As in the EGA II, IV-1 and IV-2 contents.")
add(255, "below 'Manuscrit reçu le 15 novembre 1964.', end of the fascicle",
    "a centred closing rule", "absent", "missing", "high",
    "\\end{center}\n", "\\end{center}\n\n\\begin{center}\\rule{25mm}{0.4pt}\\end{center}\n",
    "GLOBAL_ISSUES item 61: apply only if the closing rules of all parts are reproduced; same form as the EGA III "
    "p. 223 and EGA IV-2 p. 231 findings. The Index terminologique (p. 251) also ends with a centred rule under its "
    "last entry; the Index des notations (p. 250) has none. End-of-fascicle check: p. 255 is the last page of the "
    "scan (pdf page 254) and the TeX has nothing after the last printed line; every contents page number agrees "
    "with the page markers of the section headings (8.1-15.7, bibliography 249, indexes 250, 251).")


def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
rel = (REL / "ega4-15-terminal-fr.tex").read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]


def release_segment(page):
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return rel[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return rel[sa:sb]
    return None


# page files against the current release text
for n in (250, 251, 253, 254, 255):
    body = page_text(n).split("\n", 1)[1]
    seg = release_segment(n)
    print(f"page_{n}.tex vs release segment:", "identical" if body.rstrip() == seg.rstrip() else "DIFFERENT")

ok = True
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    old = fx["old"]
    n_page = page_text(PAGEFILE.get(x["page"], x["page"])).count(old)
    n_rel = release_segment(x["page"]).count(old)
    flag = "ok" if n_page == 1 and n_rel == 1 else "PROBLEM"
    ok &= flag == "ok"
    print(f"{x['page']} {flag} page-file:{n_page} release:{n_rel}  {old[:60]!r}")
# overlapping edits on the same page
for i, a in enumerate(F):
    for b in F[i + 1:]:
        if a["fix"] and b["fix"] and a["page"] == b["page"]:
            t = page_text(PAGEFILE.get(a["page"], a["page"]))
            ia, ib = t.find(a["fix"]["old"]), t.find(b["fix"]["old"])
            if ia < ib + len(b["fix"]["old"]) and ib < ia + len(a["fix"]["old"]):
                ok = False
                print("OVERLAP", a["page"], a["fix"]["old"][:40], "|", b["fix"]["old"][:40])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(F), "findings; all checks", "passed" if ok else "FAILED")
