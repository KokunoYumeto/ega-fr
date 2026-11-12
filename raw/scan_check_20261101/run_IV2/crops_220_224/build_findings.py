"""Build findings_220_224.json (EGA IV-2 pp. 220-224) and verify every fix.

Checks: (1) each fix's "old" occurs exactly once in its page_NNN.tex (CRLF normalised);
(2) applying all fixes in list order to an in-memory copy of ega4-2-fr.tex, page segment by page segment
(same rule as apply_fixes.py), each "old" occurs exactly once at its turn. No .tex file is written.
Newlines in the strings below are written as the character U+23CE and converted to LF."""
import json
import pathlib
import re

RUN = pathlib.Path(__file__).resolve().parent.parent
SRC = RUN.parent / "ega-fr" / "source" / "ega4" / "ega4-2-fr.tex"
OUT = RUN / "findings_220_224.json"
NL = "\u23ce"


def L(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="", corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=L(old), new=L(new)))
    if kind == "misprint_in_print":
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


C_SCAN = "bold italic C (crop: same face as the bold italic R), not a script letter"
C_TEX = "\\mathcal C (script)"
C_NOTE = "Category letter bold italic, as on p. 114 (findings_110_114) and GLOBAL_ISSUES 35."

# ---------------------------------------------------------------- page 220
add(220, "page break 219/220: blank line after \\oldpage[IV-2]{220}",
    "p. 219 ends '... universellement caténaire (5.6.3) (et'; p. 220 begins 'en particulier si X est ...', "
    "same sentence, flush left (no new paragraph)",
    "blank line after \\oldpage[IV-2]{220} (and before it at the end of p. 219): paragraph break inside "
    "the statement of (7.9.5)",
    "marker", r"\oldpage[IV-2]{220}⏎⏎", r"\oldpage[IV-2]{220}⏎",
    note="Companion of the last-but-one p. 219 entry of findings_215_219.json ('(et\\n\\n' -> '(et\\n'); "
         "apply both. Independent of the \\textup entry below (either order).")
add(220, "Proposition (7.9.5), l. 1: 'en particulier si X est localement immersible dans un préschéma "
         "régulier (5.6.4))'",
    "end of the roman parenthesis opened on p. 219 ('(et en particulier si X est ... (5.6.4))'): roman, "
    "with 'localement immersible dans un préschéma régulier' italic (crop)",
    "inside the italic proposition environment: 'en particulier si X est' and '(5.6.4))' come out italic, "
    "the \\emph words upright",
    "convention", r"en particulier si $X$ est \emph{localement immersible dans un préschéma⏎régulier} (5.6.4))",
    r"\textup{en particulier si $X$ est \emph{localement immersible dans un préschéma⏎régulier} (5.6.4))}",
    conv=6, note="Inside \\textup the \\emph words come out italic, as printed. Continues the p. 219 entry "
                 "'\\textup{(5.6.3) (et}' of findings_215_219.json.")
add(220, "Proposition (7.9.5), l. 1-2: ', X est un préschéma excellent'",
    "'est un préschéma excellent' italic like the rest of the statement (crop)",
    "$X$ est un \\emph{préschéma excellent}: the \\emph sets the two words upright in the italic environment",
    "convention", r"\emph{préschéma excellent}", "préschéma excellent", conv=6,
    note="Printed italic words left upright: drop the \\emph (FIX_POLICY 2.6).")
add(220, "Proposition (7.9.5), end: '(7.8.5).'", "reference (7.8.5) upright (crop)",
    "(7.8.5) in the italic environment (italic)", "convention", "(7.8.5).", r"\textup{(7.8.5)}.", conv=6)
add(220, "Remarque (7.9.6), l. 6: 'aux préschémas noethériens réduits'", "'noethériens' italic",
    "no \\emph", "italics", "aux préschémas noethériens réduits", r"aux préschémas \emph{noethériens} réduits",
    note="Remark body judged as roman (document-wide remark environment).")
add(220, "Remarque (7.9.6), 2nd paragraph: 'des raisonnements de Hironaka (loc. cit.)'",
    "'(loc. cit.)' with a full stop after 'loc'; parentheses italic too (3x crop)",
    "(\\emph{loc, cit.}): comma after 'loc'", "punctuation", r"(\emph{loc, cit.})", r"\emph{(loc. cit.)}",
    note="Comma -> full stop; the parentheses go inside the \\emph (italic in the print), as on pp. 171 and 178.")
for where, old, new in [
        ("(7.9.7), l. 1: 'une sous-catégorie pleine C'", r"pleine $\mathcal C$", r"pleine $\boldsymbol{C}$"),
        ("(7.9.7) 1°: 'Pour tout X∈C, tout préschéma'", r"$1^\circ$ Pour tout $X\in\mathcal C$",
         r"$1^\circ$ Pour tout $X\in\boldsymbol{C}$"),
        ("(7.9.7) 1°: 'appartient à C.'", r"appartient à $\mathcal C$", r"appartient à $\boldsymbol{C}$"),
        ("(7.9.7) 1°: 'tel que Spec(A)∈C et toute partie multiplicative'", r"\in\mathcal C$ et toute partie",
         r"\in\boldsymbol{C}$ et toute partie"),
        ("(7.9.7) 1°: 'on a Spec(S^{-1}A)∈C.'", r"(S^{-1}A)\in\mathcal C$", r"(S^{-1}A)\in\boldsymbol{C}$"),
        ("(7.9.7) 2°: 'Pour tout X∈C, l'ensemble'", r"$2^\circ$ Pour tout $X\in\mathcal C$",
         r"$2^\circ$ Pour tout $X\in\boldsymbol{C}$"),
        ("(7.9.7) 3°: 'tel que Spec(A)∈C et tout élément régulier'", r"\in\mathcal C$ et tout élément",
         r"\in\boldsymbol{C}$ et tout élément"),
        ("(7.9.7), last line: 'un k-préschéma Z∈C'", r"$Z\in\mathcal C$", r"$Z\in\boldsymbol{C}$")]:
    add(220, where, C_SCAN, C_TEX, "font", old, new, note=C_NOTE)
add(220, "(7.9.7) 2°: 'l'ensemble U_R(X)'",
    "subscript R bold upright sans-serif (crop), not the bold italic R of R(O_{X,x}) on the same line",
    "U_{\\boldsymbol R} (bold italic)", "font", r"$U_{\boldsymbol R}(X)$", r"$U_{\mathbf{R}}(X)$", conf="medium",
    note="Same decision as the U_R findings on pp. 195-197 (findings_195_199.json).")
add(220, "printed p. 221, l. 1 (still in the p. 220 segment): '« Pour toute extension finie k' de k'",
    "'finie' italic", "no \\emph", "italics", "extension finie $k'$", r"extension \emph{finie} $k'$",
    note="Apply before the next entry: the marker insertion moves this line into the p. 221 segment.")
add(220, "page break 220/221: the p. 221 marker (edit 1 of 2, insert)",
    "printed p. 220 ends '... un k-préschéma Z∈C, la propriété suivante :'; printed p. 221 begins with the "
    "indented quotation '« Pour toute extension finie k' de k, ... vérifient la propriété R. »'",
    "\\oldpage[IV-2]{221} stands after the « ... » paragraph, before 'Nous supposerons encore' "
    "(two printed lines too late)",
    "marker", "la propriété suivante :⏎⏎« Pour toute", r"la propriété suivante :⏎⏎\oldpage[IV-2]{221}⏎⏎« Pour toute",
    note="Apply after every other p. 220 entry and together with the first p. 221 entry, which removes the old "
         "marker (either order). Afterwards '« Pour toute ... propriété R. »' belongs to p. 221.")

# ---------------------------------------------------------------- page 221
add(221, "page break 220/221: the p. 221 marker (edit 2 of 2, remove the misplaced marker)",
    "see the last p. 220 entry", "\\oldpage[IV-2]{221} before 'Nous supposerons encore'", "marker",
    r"\oldpage[IV-2]{221}⏎⏎Nous supposerons", "Nous supposerons",
    note="Apply together with the last p. 220 entry. The blank line after '... propriété R. »' stays, so "
         "'Nous supposerons' still opens a paragraph, as printed.")
add(221, "l. 5: 'lorsque l'on prend pour C la catégorie des préschémas excellents'", C_SCAN, C_TEX, "font",
    r"$\mathcal C$ la catégorie des préschémas", r"$\boldsymbol{C}$ la catégorie des préschémas", note=C_NOTE)
add(221, "l. 7: 'pour la condition 1°, cela résulte de (7.8.3, (ii))'", "(7.8.3, (ii)) (crop)", "(7.8.3, (iii))",
    "number", "(7.8.3, (iii))", "(7.8.3, (ii))",
    note="Transcription error, not a misprint: (7.8.3, (ii)) (rings of fractions and finite-type algebras of an "
         "excellent ring are excellent) is condition 1° of (7.9.7); (iii) is about complete local rings and "
         "Dedekind rings.")
add(221, "Proposition (7.9.8), l. 2: 'tel que Spec(B)∈C'", C_SCAN, C_TEX, "font",
    r"(B)\in\mathcal C$", r"(B)\in\boldsymbol{C}$", note=C_NOTE)
add(221, "Proposition (7.9.8), last line: 'la propriété P(f^{-1}(y), k(y)) est vraie'", "bold italic k (crop)",
    "plain k", "convention", r",k(y))$ est vraie", r",\boldsymbol{k}(y))$ est vraie", conv=1)
add(221, "proof of (7.9.8), l. 4: 'appartient aussi à C'", C_SCAN, C_TEX, "font",
    r"aussi à $\mathcal C$", r"aussi à $\boldsymbol{C}$", note=C_NOTE)
add(221, "proof of (7.9.8), 2nd paragraph: 'un préschéma régulier Y''", "'régulier' italic", "no \\emph",
    "italics", "préschéma régulier $Y'$", r"préschéma \emph{régulier} $Y'$")
add(221, "page break 221/222: blank line before \\oldpage[IV-2]{222}",
    "the sentence runs on: p. 221 ends '... montre qu'il suffit de prouver', p. 222 begins 'que l'on a "
    "U_R(X') = X'' flush left",
    "blank lines around \\oldpage[IV-2]{222} make a paragraph break", "marker",
    "qu'il suffit de prouver⏎⏎", "qu'il suffit de prouver⏎",
    note="Apply together with the first p. 222 entry (blank line after the marker).")

# ---------------------------------------------------------------- page 222
add(222, "page break 221/222: blank line after \\oldpage[IV-2]{222}",
    "'que l'on a U_R(X') = X'' continues the sentence of p. 221", "blank line after \\oldpage[IV-2]{222}",
    "marker", r"\oldpage[IV-2]{222}⏎⏎", r"\oldpage[IV-2]{222}⏎",
    note="Apply together with the last p. 221 entry.")
add(222, "l. 1: 'que l'on a U_R(X') = X''", "subscript R bold upright sans-serif (crop)",
    "U_{\\boldsymbol R} (bold italic)", "font", r"$U_{\boldsymbol R}(X')=X'$", r"$U_{\mathbf{R}}(X')=X'$",
    conf="medium", note="Same decision as the U_R findings on pp. 195-197.")
add(222, "l. 1: 'que g'^{-1}(a) ⊂ U_R(X')'", "subscript R bold upright sans-serif (crop)",
    "U_{\\boldsymbol R} (bold italic)", "font", r"\subset U_{\boldsymbol R}(X')", r"\subset U_{\mathbf{R}}(X')",
    conf="medium", note="Same decision as the U_R findings on pp. 195-197.")
add(222, "l. 3: 'On a donc f'^{-1}(z') = f^{-1}(b)⊗_k k(z'), et comme k(z') est une extension'",
    "the formula is in the running text, on one line with 'On a donc' and 'et comme' (crop); k(z') bold italic",
    "displayed with \\[ \\] (comma inside the display); plain k", "formula",
    r"On a donc⏎\[⏎f'^{-1}(z')=f^{-1}(b)\otimes_k k(z'),⏎\]⏎et",
    r"On a donc $f'^{-1}(z')=f^{-1}(b)\otimes_k \boldsymbol{k}(z')$,⏎et",
    note="Formula displayed where the print has it inline; no connecting word lost. The edit also carries the "
         "convention-1 bold k of this formula (next entry, fix null). The subscript k of ⊗_k looks heavy in the "
         "scan but is read as the light italic k of the field k: unchanged.")
add(222, "l. 3, same formula: 'k(z')' after ⊗_k", "bold italic k (crop)", "plain k", "convention", None, None,
    conv=1, note="Carried by the previous edit.")
add(222, "l. 3: 'et comme k(z') est une extension'", "bold italic k", "plain k", "convention",
    r"comme $k(z')$", r"comme $\boldsymbol{k}(z')$", conv=1)
add(222, "l. 3: 'est une extension de type fini de k'", "'de type fini' italic (the later 'donc de type fini' "
    "is roman)", "no \\emph", "italics", "extension de type fini de $k$", r"extension \emph{de type fini} de $k$")
add(222, "l. 5: 'qu'il en est de même de P(f'^{-1}(z'), k(z'))'", "bold italic k", "plain k", "convention",
    r",k(z'))$", r",\boldsymbol{k}(z'))$", conv=1)
add(222, "l. 6: 'Mais comme O_{z'} est un anneau régulier'", "𝒪_{z'}: subscript z' only (crop)",
    "\\mathcal O_{Y',z'}", "formula", r"\mathcal O_{Y',z'}", r"\mathcal O_{z'}",
    note="Abbreviated notation of the print, not a misprint.")
add(222, "l. 6: 'et que Spec(O_{x'})∈C'", "𝒪_{x'}: subscript x' only (crop)", "\\mathcal O_{X',x'}",
    "formula", r"\operatorname{Spec}(\mathcal O_{X',x'})", r"\operatorname{Spec}(\mathcal O_{x'})",
    note="The following 'R(O_{X',x'})' has X', x' in the print as in the TeX (unchanged).")
add(222, "l. 6: 'Spec(O_{x'})∈C en vertu de la condition 1°'", C_SCAN, C_TEX, "font",
    r"\in\mathcal C$ en vertu", r"\in\boldsymbol{C}$ en vertu", note=C_NOTE)
add(222, "Corollaire (7.9.9): '(ce qui sera par exemple le cas si ... résultats de Hironaka [35])'",
    "the parenthesis is roman inside the italic statement (strip s2)",
    "inside the italic corollary environment (italic)", "convention",
    "(ce qui sera par⏎exemple le cas si les fibres formelles de $A$ sont géométriquement régulières⏎"
    "et le corps résiduel de $A$ de caractéristique $0$, en raison des résultats de⏎Hironaka [35])",
    r"\textup{(ce qui sera par⏎exemple le cas si les fibres formelles de $A$ sont géométriquement régulières⏎"
    r"et le corps résiduel de $A$ de caractéristique $0$, en raison des résultats de⏎Hironaka [35])}",
    conv=6)
add(222, "Corollaire (7.9.9), end: 'ponctuellement intègre (4.6.9). Alors'", "reference (4.6.9) upright",
    "(4.6.9) in the italic environment (italic)", "convention", "(4.6.9). Alors", r"\textup{(4.6.9)}. Alors",
    conv=6)
add(222, "proof of (7.9.9), l. 1: 'en prenant pour C la catégorie de tous les préschémas'", C_SCAN, C_TEX,
    "font", r"pour $\mathcal C$ la catégorie de", r"pour $\boldsymbol{C}$ la catégorie de", note=C_NOTE)
add(222, "proof of (7.9.9): 'on voit déjà que B est réduit (3.3.5)'", "'réduit' italic", "no \\emph",
    "italics", "est réduit (3.3.5)", r"est \emph{réduit} (3.3.5)")
add(222, "proof of (7.9.9): 'Il reste à prouver que X = Spec(B) est irréductible.'", "'irréductible' italic",
    "no \\emph", "italics", "irréductible. Or, la", r"\emph{irréductible}. Or, la",
    note="The later 'que X' est irréductible, ou' is roman in the print, as in the TeX.")
add(222, "proof of (7.9.9): 'que X' est connexe. Mais'", "'connexe' italic", "no \\emph", "italics",
    "que $X'$ est connexe. Mais", r"que $X'$ est \emph{connexe}. Mais")
add(222, "proof of (7.9.9): 'la fibre g'^{-1}(a) est connexe. En effet'", "'connexe' italic", "no \\emph",
    "italics", "$g'^{-1}(a)$ est connexe. En effet", r"$g'^{-1}(a)$ est \emph{connexe}. En effet")
add(222, "proof of (7.9.9): '... ce qui est absurde. Or, on a g'^{-1}(a) = ...'",
    "'Or, on a' starts flush left: same paragraph (crop; new paragraphs are indented)",
    "blank line before 'Or, on a': paragraph break", "other", "absurde.⏎⏎Or, on a", "absurde.⏎Or, on a",
    note="Removes the paragraph break the print does not have.")
add(222, "proof of (7.9.9): 'Or, on a g'^{-1}(a) = g^{-1}(b)⊗_k k(a)'", "subscript of ⊗ is k alone (crop)",
    "\\otimes_{k(b)}", "formula", r"\otimes_{k(b)}", "\\otimes_k ",
    note="k = k(b), b being the closed point of Y: the print is right; the TeX rewrote the subscript. The "
         "new string ends with a space. Independent of the next entry (either order).")
add(222, "same formula: 'k(a)'", "bold italic k (crop)", "plain k", "convention",
    "k(a)$; mais", r"\boldsymbol{k}(a)$; mais", conv=1)
add(222, "end of the proof of (7.9.9): 'que g^{-1}(b) est géométriquement connexe, ce qui achève'",
    "'géométriquement connexe' italic", "no \\emph", "italics", "est géométriquement connexe, ce qui",
    r"est \emph{géométriquement connexe}, ce qui")
add(222, "Remarques (7.9.10) (i), end: 'que B est géométriquement unibranche.'",
    "'géométriquement unibranche' italic", "no \\emph", "italics",
    "que $B$ est⏎géométriquement unibranche.", r"que $B$ est⏎\emph{géométriquement unibranche}.",
    note="Remark body judged as roman (document-wide remark environment).")

# ---------------------------------------------------------------- page 223
add(223, "Remarques (7.9.10) (ii), l. 3: 'la propriété d'être régulier'", "'régulier' italic", "no \\emph",
    "italics", "d'être régulier,", r"d'être \emph{régulier},",
    note="Remark body judged as roman (document-wide remark environment).")
add(223, "display: 'Spec(O_x ⊗_{O_{f(x)}} k(f(x)))'", "bold italic k", "plain k", "convention",
    r"}}k(f(x)))", r"}}\boldsymbol{k}(f(x)))", conv=1)
add(223, "display: '→ Spec(k(f(x)))'", "bold italic k", "plain k", "convention",
    r"\operatorname{Spec}(k(f(x)))", r"\operatorname{Spec}(\boldsymbol{k}(f(x)))", conv=1)
add(223, "after the display: 'soit géométriquement régulière,'", "'géométriquement régulière' italic",
    "no \\emph", "italics", "soit géométriquement régulière,", r"soit \emph{géométriquement régulière},")
add(223, "after the display: 'est stable par générisation.'", "'stable par générisation' italic", "no \\emph",
    "italics", "stable par générisation", r"\emph{stable par générisation}")
add(223, "'Nous ignorons si cet ensemble est ouvert (ou'", "'ouvert' italic", "no \\emph", "italics",
    "est ouvert (ou,", r"est \emph{ouvert} (ou,")
add(223, "'(ou, ce qui revient au même (0_III, 9.2.5)'", "bold 0 with roman subscript III", "plain 0",
    "convention", r"(0$_{\mathrm{III}}$,", r"(\textbf{0}$_{\mathrm{III}}$,", conv=2)
add(223, "'s'il est constructible)'", "'constructible' italic", "no \\emph", "italics",
    "s'il est constructible)", r"s'il est \emph{constructible})")

# ---------------------------------------------------------------- page 224 (bibliography)
LBL = ("label in the weight of the text (crop: regular, not bold)", "\\textbf{[..]}")
for n in (33, 34, 35, 36, 37, 38):
    pass  # labels added in entry order below


def label(n, note=""):
    add(224, f"[{n}] label", LBL[0], LBL[1].replace("..", str(n)), "font", "\\textbf{[%d]}" % n, "[%d]" % n,
        note=note)


def roman_title(n, old, what):
    add(224, f"[{n}] title '{what}'", "title roman (crop)", "\\emph{...} (italic)", "italics", old,
        old[len("\\emph{"):-1], note="Titles roman, journal or series names italic, as in the other "
                                      "bibliographies (IV-1 p. 251, II p. 205, I p. 214).")


def hyphen(n, old, new):
    add(224, f"[{n}] '{new.replace('~', ' ')}'", "hyphen between the numbers (crop)", "en dash (--)",
        "punctuation", old, new, note="As IV-1 p. 251 and III p. 161.")


label(33, note="Applies to all six labels: the print sets [33]-[38] in the roman of the text.")
roman_title(33, r"\emph{Note on a chain condition for prime⏎ideals}", "Note on a chain condition for prime ideals")
hyphen(33, "p.~85--90", "p.~85-90")
label(34)
roman_title(34, r"\emph{Les morphismes⏎projectifs}", "Les morphismes projectifs")
label(35)
roman_title(35, r"\emph{Resolution of singularities of an⏎algebraic variety over a field of characteristic zero}",
            "Resolution of singularities of an algebraic variety over a field of characteristic zero")
hyphen(35, "p.~109--326", "p.~109-326")
label(36)
add(224, "[36] author: 'S. ABHYANKHAR'", "'ABHYANKHAR' (caps and small caps)", "S.~\\textsc{Abhyankhar}",
    "misprint_in_print", None, None, corrected=r"S.~\textsc{Abhyankar}",
    note="The TeX keeps the printed reading. The author's name is Abhyankar.")
roman_title(36, r"\emph{Local uniformization of algebraic⏎surfaces over ground fields of characteristic $p\ne0$}",
            "Local uniformization of algebraic surfaces over ground fields of characteristic p ≠ 0")
add(224, "[36] title: 'Local uniformization of algebraic surfaces'", "'of algebraic surfaces'",
    "'of algebraic' (keeps the print)", "misprint_in_print", None, None,
    corrected="Local uniformization on algebraic surfaces",
    note="The TeX keeps the printed reading. The paper's title is 'Local uniformization on algebraic surfaces "
         "over ground fields of characteristic p ≠ 0' (IAS repository record; Numdam bibliographies).")
add(224, "[36] journal: 'Amer. J. of Math., t. 63 (1956), p. 491-526'", "'Amer. J. of Math.' (italic)",
    "\\emph{Amer. J. of Math.} (keeps the print)", "misprint_in_print", None, None,
    corrected=r"\emph{Ann. of Math.}",
    note="The TeX keeps the printed reading. The paper appeared in Annals of Mathematics (2) 63 (1956), "
         "491-526; volume, year and pages are right.")
hyphen(36, "p.~491--526", "p.~491-526")
label(37)
roman_title(37, r"\emph{Séminaire de l'École Normale⏎Supérieure}", "Séminaire de l'École Normale Supérieure")
hyphen(37, "(1960--61)", "(1960-61)")
label(38)

# ---------------------------------------------------------------- checks
pages = {p: (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(220, 225)}
bad = 0
for i, x in enumerate(F):
    if x["fix"]:
        c = pages[x["page"]].count(x["fix"]["old"])
        if c != 1:
            bad += 1
            print("PAGE-FILE COUNT", c, i, x["page"], repr(x["fix"]["old"]))

src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("SEGMENT COUNT", c, i, x["page"], repr(x["fix"]["old"]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(220, 225):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("entries", len(F), "bad", bad, "->", OUT)
# show the simulated result around the edited page breaks (in memory only)
for key in ("(et", "la propriété suivante :", "de prouver", "absurde.", "On a donc $f'"):
    k = t.find(key, t.find(r"\oldpage[IV-2]{219}"))
    print("----", key, "\n", t[k - 20:k + 160])
