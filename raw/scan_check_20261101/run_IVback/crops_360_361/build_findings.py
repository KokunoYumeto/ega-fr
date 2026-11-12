"""Build findings_360_361.json and check every fix's old string.

Checks: old occurs exactly once in its page_NNN.tex (CRLF -> LF), exactly once in that page's segment of the
current diplomatic source (\\oldpage[IV]{N} to the next marker), and exactly once in the whole source file.
"""
import json
import pathlib
import re
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IVback")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-errata-addenda-list3-fr.tex")
OUT = RUN / "findings_360_361.json"

F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- boundary 359/360 (lies in p. 359's segment)
add(359,
    "page break 359/360 inside '... pour tout ouvert quasi-compact T_α⊃T de X, | f(T_α)=Y et f|T_α est quasi-compact'",
    "p. 359 ends with 'pour tout ouvert quasi-compact T_α⊃T de X,' (page_359_s4.png); p. 360 begins "
    "'f(T_α)=Y et f|T_α est quasi-compact' at the left margin, no indent (page_360_s1.png): a mid-sentence break",
    "blank line before \\oldpage[IV]{360} (none after it): a paragraph break inside the sentence",
    "marker",
    {"old": "$T_\\alpha\\supset T$ de $X$,\n\n", "new": "$T_\\alpha\\supset T$ de $X$,\n"},
    "BOUNDARY FIX (page break 359/360), outside pp. 360-361: the blank line is the last line of p. 359's segment, "
    "just before \\oldpage[IV]{360}, so the entry is listed under page 359 ('old' occurs once in page_359.tex, in "
    "p. 359's segment and in ega4-errata-addenda-list3-fr.tex). The marker is at the right place and has no blank "
    "line after it (\\oldpage ends with \\ignorespaces, which does not skip a \\par). The p. 359 checker may report "
    "the same edit: apply once.")

# ---------------------------------------------------------------- page 360
add(360,
    "proof of (21.4.9) II), l. 2: 'tel que (f|T_α)^*(D_α)=D'|T_α; en vertu de'",
    "set in the line (crop crops_360_361/p360_s1_l2.png)",
    "displayed",
    "formula",
    {"old": "tel que\n\\[\n (f|T_\\alpha)^*(D_\\alpha)=D'|T_\\alpha;\n\\]\nen vertu de",
     "new": "tel que $(f|T_\\alpha)^*(D_\\alpha)=D'|T_\\alpha$;\nen vertu de"})

add(360,
    "proof of (21.4.9) II), l. 5: 'on a (f|T)^*(D_α)=(f|T)^*(D_β), d'où (par (21.4.8)), D_α=D_β'",
    "set in the line (crop crops_360_361/p360_s1_l5.png)",
    "displayed",
    "formula",
    {"old": "distincts, on a\n\\[\n (f|T)^*(D_\\alpha)=(f|T)^*(D_\\beta),\n\\]\nd'où",
     "new": "distincts, on a $(f|T)^*(D_\\alpha)=(f|T)^*(D_\\beta)$,\nd'où"})

add(360,
    "end of the proof of (21.4.9): 'et par suite f^*(D)=D'. C.Q.F.D.'",
    "'C.Q.F.D.' after the last formula",
    "missing",
    "missing",
    {"old": "$f^*(D)=D'$.\n\\end{proof}", "new": "$f^*(D)=D'$. C.Q.F.D.\n\\end{proof}"},
    "Written as elsewhere in the edition ('... $. C.Q.F.D.' before \\end{proof}).")

add(360,
    "Corollaire (21.4.10), l. 1: 'les hypothèses générales de (21.4.9), et en outre'",
    "the reference upright (upright parentheses and figures) inside the italic statement "
    "(crop crops_360_361/p360_s1_ref2149.png)",
    "{\\hyperlink{ega4.c04.prop.21-4-9}{(21.4.9)}} inside the corollary environment: italic",
    "convention",
    {"old": "générales de\n{\\hyperlink{ega4.c04.prop.21-4-9}{(21.4.9)}}, et en outre",
     "new": "générales de\n\\textup{\\hyperlink{ega4.c04.prop.21-4-9}{(21.4.9)}}, et en outre"},
    "The errata file writes references as {\\hyperlink...}, which take the statement's italic (\\sref would add "
    "\\normalfont); references inside italic statements are upright in the print.",
    convention=6)

add(360,
    "proof of (21.4.10), l. 7: 'l'application n⇝div(t^n) est un isomorphisme de Z'",
    "wavy arrow (crop crops_360_361/p360_s3_arrow.png)",
    "\\mapsto",
    "symbol",
    {"old": "$n\\mapsto\\operatorname{div}(t^n)$", "new": "$n\\leadsto\\operatorname{div}(t^n)$"})

add(360,
    "Corollaire (21.4.11), l. 1: 'les hypothèses générales de (21.4.9), et supposons en outre'",
    "the reference upright inside the italic statement (crop crops_360_361/p360_s3_ref2149b.png)",
    "{\\hyperlink{ega4.c04.prop.21-4-9}{(21.4.9)}} inside the corollary environment: italic",
    "convention",
    {"old": "{\\hyperlink{ega4.c04.prop.21-4-9}{(21.4.9)}}, et supposons en outre",
     "new": "\\textup{\\hyperlink{ega4.c04.prop.21-4-9}{(21.4.9)}}, et supposons en outre"},
    "Same as the (21.4.9) of Corollaire (21.4.10).",
    convention=6)

add(360,
    "proof of (21.4.11), l. 6: 'une uniformisante de O_X,x (0, 17.3.3); l'image réciproque'",
    "bold 0, no subscript (crop crops_360_361/p360_s4_0_1733.png)",
    "($0$, 17.3.3), light 0",
    "convention",
    {"old": "($0$, 17.3.3)", "new": "($\\mathbf{0}$, 17.3.3)"},
    convention=2)

add(360,
    "page break 360/361 inside '... est donc bien de la forme | div(t_y^n), ce qui n'est autre ...'",
    "p. 360 ends with 'est donc bien de la forme' (page_360_s4.png); p. 361 begins 'div(t^n_y), ce qui n'est autre' "
    "at the left margin, no indent (page_361_s1.png): a mid-sentence break",
    "blank line before \\oldpage[IV]{361} (none after it): a paragraph break inside the sentence",
    "marker",
    {"old": "est donc bien\nde la forme\n\n", "new": "est donc bien\nde la forme\n"},
    "The marker is at the right place; the blank line before it (end of p. 360's segment) must go. Inside this "
    "batch (pp. 360-361), not a boundary with another checker's pages.")

# ---------------------------------------------------------------- page 361
add(361,
    "Remarque (21.4.12), l. 1-2: 'que les X_y sont réduits, il faut ajouter'",
    "'réduits' italic in the roman remark (crop crops_360_361/p361_s1_reduits.png)",
    "no emphasis",
    "italics",
    {"old": "sont réduits, il faut", "new": "sont \\emph{réduits}, il faut"},
    "Judged as if the remark body were roman (the italic remark environment is a document-wide item).")

add(361,
    "Remarque (21.4.12), l. 3: 'de D' dans chacun des ensembles'",
    "'chacun' italic (crop crops_360_361/p361_s1_chacun.png)",
    "no emphasis",
    "italics",
    {"old": "dans chacun des ensembles", "new": "dans \\emph{chacun} des ensembles"},
    "Judged as if the remark body were roman.")

add(361,
    "Remarque (21.4.12), l. 3: 'Div(Spec(O_X,x)) où x parcourt l'ensemble'",
    "no comma after Div(Spec(O_X,x)) (crop crops_360_361/p361_s1_chacun.png)",
    "comma before 'où'",
    "punctuation",
    {"old": "(\\sh{O}_{X,x}))$, où $x$", "new": "(\\sh{O}_{X,x}))$ où $x$"},
    "The comma after 'de X_y,' (next line) stays.")

add(361,
    "Remarque (21.4.12), l. 4: 'sont toutes de la forme div(t'^n_x) où t'_x est une uniformisante'",
    "t carrying the prime and the exponent n above and the subscript x below, no inner parentheses "
    "(crop crops_360_361/p361_s1_divt.png)",
    "\\operatorname{div}((t'_x)^n)",
    "formula",
    {"old": "\\operatorname{div}((t'_x)^n)", "new": "\\operatorname{div}(t'^n_x)"},
    "t'^n_x typesets as t with the superscript ′n and the subscript x, as printed.")

add(361,
    "Remarque (21.4.12), last line: 'l'entier n étant le même pour tous ces points'",
    "'le même' italic (crop crops_360_361/p361_s1_lememe.png)",
    "no emphasis",
    "italics",
    {"old": "étant le même pour", "new": "étant \\emph{le même} pour"},
    "Judged as if the remark body were roman.")

add(361,
    "Corollaire (21.4.13), l. 1: 'Supposons vérifiées les conditions de (21.4.11). Pour tout'",
    "the reference upright inside the italic statement (crop crops_360_361/p361_s1_ref21411.png)",
    "{\\hyperlink{ega4.c04.cor.21-4-11}{(21.4.11)}} inside the corollary environment: italic",
    "convention",
    {"old": "{\\hyperlink{ega4.c04.cor.21-4-11}{(21.4.11)}}. Pour tout",
     "new": "\\textup{\\hyperlink{ega4.c04.cor.21-4-11}{(21.4.11)}}. Pour tout"},
    "Same as the (21.4.9) references of p. 360.",
    convention=6)

add(361,
    "Corollaire (21.4.13), l. 2: 'l'image réciproque L_η=L⊗_{O_X}O_{X_η} soit isomorphe à O_{X_η}'",
    "set in the line (crop crops_360_361/p361_s1_Leta.png)",
    "displayed",
    "formula",
    {"old": "l'image réciproque\n\\[\n \\sh{L}_\\eta=\\sh{L}\\otimes_{\\sh{O}_X}\\sh{O}_{X_\\eta}\n\\]\nsoit isomorphe",
     "new": "l'image réciproque\n$\\sh{L}_\\eta=\\sh{L}\\otimes_{\\sh{O}_X}\\sh{O}_{X_\\eta}$\nsoit isomorphe"})

add(361,
    "proof of (21.4.13): 'Soit s_η la section de L_η au-dessus de X qui correspond par isomorphie'",
    "'au-dessus de X', no subscript η: a normal word space follows the X (crop crops_360_361/p361_s2_section_de_L.png)",
    "'au-dessus de $X_\\eta$': the TeX silently corrects the print",
    "misprint_in_print",
    {"old": "au-dessus de $X_\\eta$ qui correspond", "new": "au-dessus de $X$ qui correspond"},
    "L_η=L⊗O_{X_η} lives on the fibre X_η, and s_η corresponds to the unit section of O_{X_η}: the section is over "
    "X_η. The fix restores the printed X; the corrected edition keeps X_η.",
    corrected="au-dessus de $X_\\eta$ qui correspond")

add(361,
    "proof of (21.4.13), end: 'que s induit sur X une section méromorphe régulière de L_η égale à s_η'",
    "'induit sur X' (last word of the line, at the right margin, no subscript; "
    "crop crops_360_361/p361_s3_induit_sur_X.png)",
    "'induit sur $X_\\eta$': the TeX silently corrects the print",
    "misprint_in_print",
    {"old": "que $s$ induit sur $X_\\eta$", "new": "que $s$ induit sur $X$"},
    "s is already a section over X; what it induces on the fibre X_η is a section of L_η, compared with s_η. "
    "Same slip as 'au-dessus de X' above. The fix restores the printed X; the corrected edition keeps X_η.",
    corrected="que $s$ induit sur $X_\\eta$")

add(361,
    "printer's colophon at the foot of p. 361: rule",
    "a full-width rule above '1967. — Imprimerie des Presses Universitaires de France. — Vendôme (France)' "
    "(crop crops_360_361/p361_s4_colophon.png)",
    "no rule (\\bigskip only)",
    "missing",
    {"old": "\\bigskip\n\\begin{center}", "new": "\\bigskip\n\\noindent\\rule{\\textwidth}{0.4pt}\n\\begin{center}"},
    "Part of the printer's colophon, which the TeX reproduces; not the short centred end-of-article rule of "
    "GLOBAL_ISSUES 61 (the print has none after 'répond donc à la question.'). The block stands at the foot of the "
    "page in the print (layout, not reported). The '46' at the bottom right is the printer's signature mark "
    "(sheet 46; p. 353 has '45', not transcribed): not reported. Independent of the next two entries (no overlap).")

add(361,
    "printer's colophon: typeface",
    "the colophon is set in a bold face, heavier than the text and of another design (crop "
    "crops_360_361/p361_s4_colophon.png)",
    "\\small, normal weight",
    "font",
    {"old": "\\small\n1967.", "new": "\\small\\bfseries\n1967."},
    "The printer's own type; bold is the nearest reproduction. With the next entry it gives bold small capitals, "
    "as printed.",
    confidence="medium")

add(361,
    "printer's colophon, l. 2: 'IMPRIMÉ EN FRANCE'",
    "small capitals, much smaller than the capitals of 'ÉDIT.' and 'IMP.' on the same line "
    "(crop crops_360_361/p361_s4_colophon_l2.png)",
    "full capitals",
    "font",
    {"old": "IMPRIMÉ EN FRANCE\\qquad", "new": "\\textsc{imprimé en france}\\qquad"})

# ---------------------------------------------------------------- checks
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]


def segment(page):
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]
    return ""


ok = True
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    old = fx["old"]
    pg = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    a, b, c = pg.count(old), segment(x["page"]).count(old), src.count(old)
    flag = "" if (a, b, c) == (1, 1, 1) else "  <-- CHECK"
    if flag:
        ok = False
    print(f"p.{x['page']} page_tex={a} segment={b} file={c}{flag} :: {old[:60]!r}")

# a fix applied on top of the others must still find its old text: apply all in order on the source
t = src
for x in F:
    fx = x["fix"]
    if fx:
        if t.count(fx["old"]) != 1:
            ok = False
            print("SEQUENTIAL CHECK FAILED:", fx["old"][:60])
        t = t.replace(fx["old"], fx["new"], 1)

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written;", "all unique" if ok else "PROBLEMS")
sys.exit(0 if ok else 1)
