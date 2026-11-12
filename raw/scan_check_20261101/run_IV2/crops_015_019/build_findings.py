# Build findings_015_019.json for EGA IV-2 pp. 15-19, check each "old" against its page_NNN.tex,
# and simulate apply_fixes.py on an in-memory copy of ega4-2-fr.tex (no .tex file is written).
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
OUT = RUN / "findings_015_019.json"
N = "\n"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=old, new=new))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def label(page, where, lab, ctx=""):
    add(page, where, f"label {lab} printed upright", f"\\item[{lab}] inside the italic statement (label typeset italic)",
        "convention", 6, "high", "\\item[" + lab + "]" + ctx, "\\item[\\textup{" + lab + "}]" + ctx)


def ref0(page, where, num, ctx_before="", ctx_after="", note=None):
    old = ctx_before + r"$(0_{\mathrm I}," + num + r")$" + ctx_after
    new = ctx_before + r"$(\mathbf{0}_{\mathrm I}," + num + r")$" + ctx_after
    add(page, where, f"(0_I, {num}) with a bold 0", f"$(0_{{\\mathrm I}},{num})$, plain 0", "convention", 2, "high",
        old, new, note)


def refR(page, where, chap, num, pre="(", note=None):
    old = pre + chap + ", " + num + ")"
    new = pre + "\\textbf{" + chap + "}, " + num + ")"
    add(page, where, f"({chap}, {num}) with a bold {chap}", f"({chap}, {num}), plain {chap}", "convention", 2, "high",
        old, new, note)


# ---------------------------------------------------------------- page 15
label(15, "Proposition (2.3.4) (iii), top of the page", "(iii)", " Pour")
add(15, "Proof of (2.3.4): F_x ⊗_{O_y} k(y) ≠ 0", "bold italic k in k(y)", "plain k(y)", "convention", 1, "high",
    r"\otimes_{\mathcal O_y}k(y)", r"\otimes_{\mathcal O_y}\boldsymbol{k}(y)")
ref0(15, "Proof of (2.3.4): 'fidèlement plat (0_I, 6.4.1)'", "6.4.1")
ref0(15, "Proof of (2.3.4): 'q=ρ^{-1}(p) (0_I, 6.5.1)'", "6.5.1")
add(15, "Corollaire (2.3.5), first sentence: 'conditions équivalentes (i), (ii), (iii) de'",
    "(i), (ii), (iii) upright (the following 'de' italic)", "plain text inside the italic corollary (typeset italic)",
    "convention", 6, "high",
    "conditions équivalentes (i), (ii)," + N + "(iii) de",
    "conditions équivalentes \\textup{(i), (ii)," + N + "(iii)} de")
add(15, "Corollaire (2.3.5), first sentence: '(2.3.4) (en particulier un morphisme quasi-plat ou un morphisme ouvert (1.10.4))'",
    "'(2.3.4) (en particulier un morphisme' roman, 'quasi-plat' italic, 'ou un morphisme' roman, 'ouvert' italic, '(1.10.4))' roman",
    "the whole parenthesis italic (no change of face), reference italic", "convention", 6, "high",
    "(2.3.4) (en particulier un morphisme quasi-plat ou un morphisme" + N + "ouvert (1.10.4))",
    "\\textup{(2.3.4) (en particulier un morphisme \\emph{quasi-plat} ou un morphisme" + N + "\\emph{ouvert} (1.10.4))}")
label(15, "Corollaire (2.3.5) (i)", "(i)", " Soient $Z$")
label(15, "Corollaire (2.3.5) (ii)", "(ii)", " Pour toute")
label(15, "Corollaire (2.3.5) (iii)", "(iii)", " Supposons")
ref0(15, "Proof of (2.3.5) (iii): 'résulte alors de (0_I, 2.1.8)'", "2.1.8")
add(15, "Proposition (2.3.6), first sentence: 'est localement fini'",
    "'est localement fini' italic like the rest of the statement (no change of face)",
    r"\emph{localement fini} inside the italic proposition (typeset upright)", "convention", 6, "high",
    r"\emph{localement fini}", "localement fini")
add(15, "Proposition (2.3.6), first sentence: '(ce qui est le cas si l'espace sous-jacent à Y est localement noethérien (cf. I, 6.1.9))'",
    "parenthesis roman, only 'localement noethérien' italic",
    r"parenthesis italic, \emph{localement noethérien} upright (inverted)", "convention", 6, "high",
    "(ce qui est le cas si l'espace sous-jacent à $Y$ est" + N + r"\emph{localement noethérien} (cf. I, 6.1.9))",
    "\\textup{(ce qui est le cas si l'espace sous-jacent à $Y$ est" + N + r"\emph{localement noethérien} (cf. I, 6.1.9))}",
    "Apply before the convention-2 fix of '(cf. I, 6.1.9)' (its 'old' lies inside this one).")
refR(15, "Proposition (2.3.6), first sentence", "I", "6.1.9", pre="(cf. ",
     note="Apply after the convention-6 fix just above.")
label(15, "Proposition (2.3.6) (i)", "(i)", " Toute")
add(15, "Proposition (2.3.6) (i): 'stable par générisation'",
    "italic like the rest of the statement (no change of face)",
    r"\emph{stable par générisation} (typeset upright)", "convention", 6, "high",
    r"\emph{stable par générisation}", "stable par générisation")
ref0(15, "Proposition (2.3.6) (i): 'stable par générisation (0_I, 2.1.2)'", "2.1.2")
label(15, "Proposition (2.3.6) (ii)", "(ii)", " Soit")
add(15, "Proposition (2.3.6) (ii): 'un morphisme fermé vérifiant'",
    "'fermé' set roman (emphasis inside the italic statement)", "'fermé' plain (typeset italic)",
    "convention", 6, "high",
    "un morphisme fermé vérifiant", "un morphisme \\emph{fermé} vérifiant",
    r"\emph inside the italic statement typesets 'fermé' upright, as printed.")
add(15, "Proposition (2.3.6) (ii): 'conditions équivalentes (i), (ii), (iii) de'",
    "(i), (ii), (iii) upright", "typeset italic", "convention", 6, "high",
    "les" + N + "  conditions équivalentes (i), (ii), (iii) de",
    "les" + N + "  conditions équivalentes \\textup{(i), (ii), (iii)} de")
add(15, "Proposition (2.3.6) (ii): '(2.3.4) (ce qui sera le cas si f est quasi-plat ou ouvert)'",
    "'(2.3.4) (ce qui sera le cas si f est' roman, 'quasi-plat' italic, 'ou' roman, 'ouvert' italic, ')' roman",
    "all italic", "convention", 6, "high",
    "(2.3.4) (ce qui sera le cas si" + N + "  $f$ est quasi-plat ou ouvert)",
    "\\textup{(2.3.4) (ce qui sera le cas si" + N + "  $f$ est \\emph{quasi-plat} ou \\emph{ouvert})}")
label(15, "Proposition (2.3.6) (iii)", "(iii)", " Soit")
add(15, "Proposition (2.3.6) (iii): 'équivalentes (i), (ii), (iii) de (2.3.4) et tel'",
    "(i), (ii), (iii) and (2.3.4) upright, 'de' italic", "typeset italic", "convention", 6, "high",
    "équivalentes (i), (ii), (iii) de (2.3.4) et tel",
    "équivalentes \\textup{(i), (ii), (iii)} de \\textup{(2.3.4)} et tel")
add(15, "Proposition (2.3.6) (iii): '(ce qui sera le cas si f est quasi-fini ou radiciel)'",
    "'(ce qui sera le cas si f est' roman, 'quasi-fini' italic, 'ou' roman, 'radiciel' italic, ')' roman",
    "all italic", "convention", 6, "high",
    "(ce qui sera le cas si $f$ est" + N + "  quasi-fini ou radiciel)",
    "\\textup{(ce qui sera le cas si $f$ est" + N + "  \\emph{quasi-fini} ou \\emph{radiciel})}")

# ---------------------------------------------------------------- page 16 (page_016.tex)
ref0(16, "Proof of (2.3.6) (i), printed on p. 15 (in the TeX after the p. 16 marker): 'réunion des U∩Y_i (0_I, 2.1.6)'",
     "2.1.6", note="Text printed on p. 15; apply before the marker move at the end of this file.")
label(16, "Proposition (2.3.7) (i)", "(i)", " Si $f$")
label(16, "Proposition (2.3.7) (ii)", "(ii)", " Si toute")
add(16, "Proof of (2.3.7) (i): 'il existe x∈X tel que f(x)=y; donc (I, 3.4.7)'",
    "semicolon after f(x)=y", "comma", "punctuation", None, "high",
    "$f(x)=y$, donc", "$f(x)=y$~; donc")
refR(16, "Proof of (2.3.7) (i): 'donc (I, 3.4.7)'", "I", "3.4.7")
refR(16, "Proof of (2.3.7) (ii): 'En vertu de (I, 5.1.7)'", "I", "5.1.7")
refR(16, "Proof of (2.3.7) (ii): 'en vertu de (I, 3.6.5)'", "I", "3.6.5")
refR(16, "Proof of (2.3.7) (ii): 'et de (I, 2.4.4)'", "I", "2.4.4")
add(16, "Corollaire (2.3.8), 1°: 'essentiellement de type fini (1.3.8)'",
    "(1.3.8) upright", "typeset italic", "convention", 6, "high",
    "(1.3.8).", "\\textup{(1.3.8)}.")

# ---------------------------------------------------------------- page 17 (page_017.tex)
add(17, "Proof of (2.3.8), printed on p. 16 (in the TeX after the p. 17 marker): 'donc B' est un anneau noethérien'",
    "'noethérien' italic", "plain", "italics", None, "high",
    "un anneau noethérien.", "un anneau \\emph{noethérien}.",
    "Text printed on p. 16; apply before the marker move at the end of this file.")
ref0(17, "Proof of (2.3.8), printed on p. 16: 'sous-anneau de Â (0_I, 7.3.5), A est intègre'", "7.3.5",
     ctx_after=", $A$ est intègre", note="Text printed on p. 16; apply before the marker move.")
ref0(17, "Proof of (2.3.8), printed on p. 16: 'l'idéal 0 de A (0_I, 1.5.8)'", "1.5.8",
     note="Text printed on p. 16; apply before the marker move.")
refR(17, "Proof of (2.3.8): 'au-dessus de x et y' (I, 3.4.9)'", "I", "3.4.9")
add(17, "Proof of (2.3.8): 'un diagramme commutatif d'homomorphismes locaux d'anneaux locaux noethériens'",
    "the first 'locaux' italic", "plain", "italics", None, "high",
    "d'homomorphismes locaux", "d'homomorphismes \\emph{locaux}")
add(17, "Proof of (2.3.8): 'tel que u et v soient injectifs'", "'injectifs' italic", "plain", "italics", None, "high",
    "soient injectifs", "soient \\emph{injectifs}")
refR(17, "Proof of (2.3.8): 'injectifs (I, 1.2.7)'", "I", "1.2.7")
ref0(17, "Proof of (2.3.8): 'est donc nulle (0_I, 7.3.5)'", "7.3.5", ctx_before="nulle ")
add(17, "Proof of (2.3.8): 'comme Â est complet'", "'complet' italic", "plain", "italics", None, "high",
    "est complet et", "est \\emph{complet} et")
add(17, "Proof of (2.3.8): 'la topologie de Â est induite par la topologie r-préadique'", "'induite' italic", "plain",
    "italics", None, "high", "est induite", "est \\emph{induite}")
ref0(17, "Proof of (2.3.8): 'la topologie de A (0_I, 7.3.5). D'ailleurs'", "7.3.5", ctx_after=". D'ailleurs")
add(17, "Proof of (2.3.8): 'une topologie plus fine que'", "'plus fine' italic", "plain", "italics", None, "high",
    "topologie plus fine", "topologie \\emph{plus fine}")
add(17, "Proof of (2.3.8): 'ces deux topologies sont identiques. C.Q.F.D.'", "'identiques' italic", "plain",
    "italics", None, "high", "identiques. C.Q.F.D.", "\\emph{identiques}. C.Q.F.D.")
add(17, "Théorème (2.3.10): 'un morphisme quasi-plat (2.3.3). Alors'", "(2.3.3) upright", "typeset italic",
    "convention", 6, "high", "quasi-plat (2.3.3). Alors", "quasi-plat \\textup{(2.3.3)}. Alors")
add(17, "Théorème (2.3.10): 'proconstructible (1.9.4) Z de Y'", "(1.9.4) upright", "typeset italic",
    "convention", 6, "high", "(1.9.4) $Z$ de $Y$", "\\textup{(1.9.4)} $Z$ de $Y$")
add(17, "Théorème (2.3.10): 'pour toute partie proconstructible (1.9.4)'",
    "'proconstructible' without hyphen (mid-line, not a line-end hyphenation); the edition's term is 'pro-constructible' (hyphenated all five times on p. 18)",
    "pro-constructible (silently corrected)", "misprint_in_print", None, "high",
    "partie" + N + "pro-constructible", "partie" + N + "proconstructible",
    "The TeX silently corrects the printed reading; the diplomatic text restores 'proconstructible'. If the coordinator "
    "treats the unhyphenated form as a spelling variant rather than a misprint, the same edit applies as kind 'word'.",
    corrected="pro-constructible")
add(17, "Théorème (2.3.10): the equation 'on a f^{-1}(Z̄) = \\overline{f^{-1}(Z)}'",
    "f^{-1}(\\overline Z)=\\overline{f^{-1}(Z)} (barred Z on the left, long bar on the right)",
    "the two sides interchanged: \\overline{f^{-1}(Z)}=f^{-1}(\\overline Z)", "formula", None, "high",
    r"$\overline{f^{-1}(Z)}=f^{-1}(\overline Z)$", r"$f^{-1}(\overline Z)=\overline{f^{-1}(Z)}$",
    "Same order as the print's restatement on p. 18 ('qui a pour espace sous-jacent f^{-1}(Z̄)=\\overline{f^{-1}(Z)} en vertu de (2.3.10)').")
refR(17, "Proof of (2.3.10): 'l'image fermée de Y' par g (I, 9.5.3)'", "I", "9.5.3")
add(17, "Proof of (2.3.10): 'Comme f est quasi-plat, g quasi-compact et dominant' after the diagram",
    "new indented paragraph after the display", "no blank line after \\]: the text continues the paragraph",
    "other", None, "high",
    "\\]" + N + "Comme $f$ est quasi-plat", "\\]" + N + N + "Comme $f$ est quasi-plat")
refR(17, "Proof of (2.3.11): 'comme espace sous-jacent (I, 5.2.1)'", "I", "5.2.1")

# ---------------------------------------------------------------- page 18
add(18, "Corollaire (2.3.12): 'quasi-fidèlement plat (2.3.3) et quasi-compact'", "(2.3.3) upright", "typeset italic",
    "convention", 6, "high", "plat (2.3.3) et quasi-compact.", "plat \\textup{(2.3.3)} et quasi-compact.")
add(18, "Corollaire (2.3.12): '(autrement dit, pour que Z⊂Y soit ouvert (resp. fermé) dans Y, ... dans X)'",
    "parenthesis roman; only 'ouvert' and 'fermé' (twice each) italic", "the whole parenthesis italic",
    "convention", 6, "high",
    "(autrement dit, pour que $Z\\subset Y$ soit" + N + "ouvert (resp. fermé) dans $Y$, il faut et il suffit que $f^{-1}(Z)$ soit"
    + N + "ouvert (resp. fermé) dans $X$)",
    "\\textup{(autrement dit, pour que $Z\\subset Y$ soit" + N
    + "\\emph{ouvert} (resp. \\emph{fermé}) dans $Y$, il faut et il suffit que $f^{-1}(Z)$ soit" + N
    + "\\emph{ouvert} (resp. \\emph{fermé}) dans $X$)}")
add(18, "Corollaire (2.3.13): 'soit fermée'", "'fermée' italic like the rest of the statement (no change of face)",
    r"\emph{fermée} inside the italic corollary (typeset upright)", "convention", 6, "high",
    r"\emph{fermée}", "fermée")
add(18, "Corollaire (2.3.13): 'X×_S X (I, 5.3.10) soit'", "reference upright", "typeset italic", "convention", 6,
    "high", "X\\times_S X$ (I, 5.3.10)", "X\\times_S X$ \\textup{(I, 5.3.10)}",
    "Apply before the convention-2 fix of '(I, 5.3.10)' (its 'old' lies inside this one).")
refR(18, "Corollaire (2.3.13): '(I, 5.3.10)'", "I", "5.3.10", note="Apply after the convention-6 fix just above.")
refR(18, "Proof of (2.3.13): 'diagramme commutatif (I, 5.3.5)'", "I", "5.3.5")
refR(18, "Proof of (2.3.13): 'l'image j(X×_Y X) (I, 3.4.8)'", "I", "3.4.8")
add(18, "Remarque (2.3.15): 'que f est fidèlement plat.'", "'fidèlement plat' italic (remark body roman)",
    "plain", "italics", None, "high",
    "est fidèlement" + N + "plat. Par exemple", "est \\emph{fidèlement" + N + "plat}. Par exemple")

# ---------------------------------------------------------------- page 19
refR(19, "Remarque (2.3.15), top of the page: '(II, 7.4.2)'", "II", "7.4.2")
add(19, "Remarque (2.3.15): 'pour X le préschéma somme des schémas'", "'somme' italic", "plain", "italics", None,
    "high", "préschéma somme des", "préschéma \\emph{somme} des")
refR(19, "Remarque (2.3.15): 'où y parcourt Y (I, 3.1)'", "I", "3.1")
refR(19, "Remarque (2.3.15): 'fidèlement plat (I, 2.4.2)'", "I", "2.4.2")
refR(19, "Remarque (2.3.15): 'pas ouvert dans Y (II, 7.4.3)'", "II", "7.4.3")
add(19, "Title of 2.4", "'2.4. Morphismes universellement ouverts et morphismes plats.' with a final full stop",
    "no full stop", "punctuation", None, "high",
    r"\subsection{Morphismes universellement ouverts et morphismes plats}",
    r"\subsection{Morphismes universellement ouverts et morphismes plats.}")
refR(19, "(2.4.1): 'Nous avons déjà défini (II, 5.4.9)'", "II", "5.4.9")
add(19, "Définition (2.4.2): 'est universellement ouvert (resp. universellement bicontinu, resp. un homéomorphisme universel)'",
    "'universellement ouvert', 'universellement bicontinu', 'un homéomorphisme universel' italic like the statement; '(resp.' and ', resp.' roman",
    r"the three terms in \emph (typeset upright), 'resp.' italic", "convention", 6, "high",
    "\\emph{universellement" + N + "ouvert} (resp. \\emph{universellement bicontinu}, resp. un" + N
    + "\\emph{homéomorphisme universel})",
    "universellement" + N + "ouvert \\textup{(resp.} universellement bicontinu, \\textup{resp.} un" + N
    + "homéomorphisme universel)")
add(19, "Définition (2.4.2): 'est ouvert (resp. un homéomorphisme sur son image, resp. un homéomorphisme sur Y')'",
    "'(resp.' and ', resp.' roman", "typeset italic", "convention", 6, "high",
    "est ouvert (resp. un homéomorphisme" + N + "sur son image, resp. un homéomorphisme sur $Y'$)",
    "est ouvert \\textup{(resp.} un homéomorphisme" + N + "sur son image, \\textup{resp.} un homéomorphisme sur $Y'$)")
refR(19, "Paragraph after (2.4.2): 'la définition (III, 4.3.9)'", "III", "4.3.9")
for lab in ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)", "(vii)"]:
    label(19, f"Proposition (2.4.3) {lab}", lab)
RESP = [
    ("(i)", "Une immersion (resp. une immersion ouverte, resp. une immersion" + N
     + "fermée) est universellement bicontinue (resp. universellement ouverte, resp." + N + "universellement fermée)"),
    ("(ii)", "ouverts (resp." + N + "universellement fermés, resp. universellement bicontinus, resp. deux" + N
     + "homéomorphismes universels) l'est aussi"),
    ("(iii)", "$S$-morphisme universellement ouvert (resp." + N
     + "universellement fermé, resp. universellement bicontinu, resp. un" + N
     + "homéomorphisme universel), il en est de même de" + N + "$f_{(S')}"),
    ("(iv)", "universellement ouverts (resp. universellement fermés, resp. universellement" + N
     + "bicontinus, resp. deux homéomorphismes universels), il en est de même de"),
    ("(v)", "est universellement ouvert (resp. universellement" + N
     + "fermé, resp. universellement bicontinu, resp. un homéomorphisme universel), il" + N + "en est de même de $g$"),
    ("(vi)", "un morphisme universellement ouvert (resp." + N
     + "universellement fermé, resp. universellement bicontinu, resp. un" + N
     + "homéomorphisme universel), il faut et il suffit que $f_{\\mathrm{red}}$"),
    ("(vii)", "soit universellement ouvert (resp. universellement fermé, resp." + N
     + "universellement bicontinu, resp. un homéomorphisme universel), il faut et il" + N + "suffit que pour tout"),
]
for lab, old in RESP:
    new = old.replace("(resp.", "\\textup{(RESP}").replace("resp.", "\\textup{resp.}").replace("\\textup{(RESP}", "\\textup{(resp.}")
    k = old.count("resp.")
    add(19, f"Proposition (2.4.3) {lab}: the {k} 'resp.' of the item", "'(resp.' and ', resp.' roman",
        "typeset italic", "convention", 6, "high", old, new)
add(19, "Proposition (2.4.3) (iv): 'il en est de même de f×_S g: X×_S Y→X'×_S Y'.'",
    "formula in the running text, ending the line 'il en est de même de f×_S g : X×_S Y→X'×_S Y'.'",
    "set as a display \\[ ... \\]", "formula", None, "high",
    "\\[" + N + "f\\times_S g:X\\times_S Y\\longrightarrow X'\\times_S Y'." + N + "\\]",
    "$f\\times_S g:X\\times_S Y\\to X'\\times_S Y'$.")
refR(19, "Proof of (2.4.3): 'résulte de (I, 4.3.2)'", "I", "4.3.2")
refR(19, "Proof of (2.4.3): 'grâce à (I, 3.3.11)'", "I", "3.3.11")
refR(19, "Proof of (2.4.3): 'de (ii) et (iii) (I, 3.5.1)'", "I", "3.5.1")
refR(19, "Proof of (2.4.3): 'est surjectif (I, 3.5.2)'", "I", "3.5.2")

# ---------------------------------------------------------------- marker moves (apply last)
add(16, "Page break 15/16: marker position (edit 1 of 2, insert)",
    "printed p. 15 ends '... on a U⊂W, donc W'; printed p. 16 begins 'est ouvert. Comme pour tout y∈Y'",
    "\\oldpage[IV-2]{16} stands before '(i) Si $y\\in W$' (the paragraph's start, four printed lines too early)",
    "marker", None, "high",
    "$U\\subset W$, donc $W$ est ouvert.", "$U\\subset W$, donc $W$" + N + "\\oldpage[IV-2]{16}" + N + "est ouvert.",
    "Inserts the marker mid-sentence on its own line (no blank lines). Apply after every other page-16 fix and "
    "together with the next edit, which removes the old marker; afterwards '(i) Si y∈W ... donc W' belongs to p. 15.")
add(16, "Page break 15/16: marker position (edit 2 of 2, remove the misplaced marker)", "see the previous finding",
    "\\oldpage[IV-2]{16} directly before '(i) Si $y\\in W$'", "marker", None, "high",
    "\\oldpage[IV-2]{16}" + N + "(i) Si $y\\in W$", "(i) Si $y\\in W$",
    "Apply together with, and after, the previous edit. The blank line after \\end{proposition} remains, so "
    "'(i) Si' still opens a paragraph, as printed.")
add(17, "Page break 16/17: marker position (edit 1 of 2, insert)",
    "printed p. 16 ends '... comme le morphisme Y'→Y est plat et que X'; printed p. 17 begins '(qui est intègre) domine le schéma intègre Y'",
    "\\oldpage[IV-2]{17} stands before 'Posons $B'=...$' (the paragraph's start, eight printed lines too early)",
    "marker", None, "high",
    "et que $X$ (qui est intègre)", "et que $X$" + N + "\\oldpage[IV-2]{17}" + N + "(qui est intègre)",
    "Inserts the marker mid-sentence on its own line. Apply after every other page-17 fix and together with the "
    "next edit; afterwards 'Posons ... et que X' belongs to p. 16.")
add(17, "Page break 16/17: marker position (edit 2 of 2, remove the misplaced marker)", "see the previous finding",
    "\\oldpage[IV-2]{17} directly before 'Posons'", "marker", None, "high",
    "\\oldpage[IV-2]{17}" + N + "Posons", "Posons",
    "Apply together with, and after, the previous edit. The blank line after \\end{corollary} remains, so 'Posons' "
    "still opens a paragraph, as printed.")

# ---------------------------------------------------------------- checks
bad = 0
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(15, 20)}
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    c = pages[x["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], c, repr(fx["old"][:80]))

# simulate apply_fixes.py in memory
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    raise SystemExit("page not found")


applied = 0
for x in F:
    fx = x["fix"]
    if not fx or fx["old"] == fx["new"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        bad += 1
        print("SIM FAIL", x["page"], seg.count(fx["old"]), repr(fx["old"][:80]))
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    applied += 1
print("findings", len(F), "simulated applied", applied, "problems", bad)
# show the simulated page segments around the moved markers
for n in (16, 17):
    s, e = locate(t, n)
    print("---- simulated p.%d starts:" % n, repr(t[s - 60:s + 80]))
s, e = locate(t, 15)
print("---- simulated p.15 ends:", repr(t[e - 120:e]))
s, e = locate(t, 16)
print("---- simulated p.16 ends:", repr(t[e - 120:e]))
import collections
cnt = collections.Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(15, 20):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
if not bad:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
