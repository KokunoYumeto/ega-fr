# Builds findings_085_089.json from the entries below and checks that every fix's "old" occurs exactly once
# in its page_NNN.tex (CRLF normalized to LF). In the strings, the character U+23CE stands for a line break.
import json
import pathlib
import sys

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_085_089.json"
NL = "⏎"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


def F(page, where, scan, tex, kind, fix, note=None, conv=None, conf="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = []
A = findings.append

# ---------------------------------------------------------------- page 84 (other half of the p. 85 top entry)
A(F(84, "end of p. 84: '... K'^p contient k et K'' / p. 85 'est une extension radicielle de K'^p'",
    "the sentence of Remarque (4.9.3) runs on to p. 85 without a paragraph break",
    "blank line before \\oldpage[IV-2]{85}",
    "other", fx(r"contient $k$ et $K'$⏎⏎", r"contient $k$ et $K'$⏎"),
    "Outside pp. 85-89 (page_084.tex): the other half of the p. 85 top entry (GLOBAL_ISSUES 20). Skip it if the "
    "pp. 80-84 batch already removes this blank line."))

# ---------------------------------------------------------------- page 85
A(F(85, "top of the page: 'est une extension radicielle de K'^p' continues the sentence '... contient k et K'' of p. 84 (Remarque (4.9.3))",
    "no paragraph break: the line continues the sentence of p. 84",
    "blank lines before and after \\oldpage[IV-2]{85} make a paragraph break",
    "other", fx(r"\oldpage[IV-2]{85}⏎⏎est une extension", r"\oldpage[IV-2]{85}⏎est une extension"),
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the edit that removes "
    "the blank line BEFORE the marker; it lies in page_084.tex (outside pp. 85-89): \"$K'^p$ contient $k$ et $K'$\\n\\n\" -> "
    "\"$K'^p$ contient $k$ et $K'$\\n\"."))
A(F(85, "Proposition (4.9.4), line 1: 'Avec les notations de (4.9.1)'",
    "(4.9.1) upright inside the italic statement", "(4.9.1) italic (statement environment)",
    "convention", fx(r"notations de (4.9.1)", r"notations de \textup{(4.9.1)}"), conv=6))
A(F(85, "proof of (4.9.4): 'en vertu du critère (4.6.1, e))'",
    "'e)' italic (e and its parenthesis), the outer ')' upright", "plain 'e))'",
    "italics", fx(r"(4.6.1, e))", r"(4.6.1, \emph{e)})"), "Enlarged crop."))
A(F(85, "end of the proof of (4.9.4): 'a pour espace sous-jacent T.'",
    "T without the bar (enlarged crop; the T-bar elsewhere on the page is clear)", "$\\overline T$",
    "misprint_in_print", fx(r"sous-jacent $\overline T$.", r"sous-jacent $T$."),
    "The TeX silently corrects the print: the reduced subscheme Z-bar has underlying space T-bar (T alone is not defined here).",
    conf="high", corrected=r"$\overline T$"))
A(F(85, "Corollaire (4.9.5), label a)", "label 'a)' upright", "\\item[a)] (italic in the statement environment)",
    "convention", fx(r"\item[a)] $k$ est", r"\item[\textup{a)}] $k$ est"), conv=6))
A(F(85, "Corollaire (4.9.5), label b)", "label 'b)' upright", "\\item[b)] (italic in the statement environment)",
    "convention", fx(r"\item[b)] $K$ est", r"\item[\textup{b)}] $K$ est"), conv=6))
A(F(85, "Corollaire (4.9.5), last line: '(et finie sur k dans l'hypothèse b))'",
    "'b))' upright (the opening parenthesis and the words are italic)", "'b))' italic with the statement",
    "convention", fx(r"dans l'hypothèse b))", r"dans l'hypothèse \textup{b))}"), "Enlarged crop.", conv=6))
A(F(85, "proof of (4.9.5): 'Dans l'hypothèse a), K est séparable'",
    "'a)' italic", "plain 'a)'", "italics", fx(r"Dans l'hypothèse a),", r"Dans l'hypothèse \emph{a)},"), "Enlarged crop."))
A(F(85, "proof of (4.9.5): 'Dans l'hypothèse b) on sait que'",
    "'b)' italic", "plain 'b)'", "italics", fx(r"Dans l'hypothèse⏎b) on sait", r"Dans l'hypothèse⏎\emph{b)} on sait"),
    "Enlarged crop."))
A(F(85, "proof of (4.9.5): 'une extension algébrique séparable de k'",
    "'algébrique séparable' italic", "upright", "italics",
    fx(r"extension algébrique⏎séparable de $k$", r"extension \emph{algébrique⏎séparable} de $k$"), "Enlarged crop."))
A(F(85, "proof of (4.9.5), last words: 'comme dans le cas a).'",
    "'a)' italic", "plain 'a)'", "italics", fx(r"dans le cas a).", r"dans le cas \emph{a)}."), "Enlarged crop."))
A(F(85, "Proposition (4.9.6), label a)", "label 'a)' upright", "\\item[a)] (italic in the statement environment)",
    "convention", fx(r"\item[a)] $K'$", r"\item[\textup{a)}] $K'$"), conv=6))
A(F(85, "Proposition (4.9.6), label a')", "label \"a')\" upright", "\\item[a')] (italic in the statement environment)",
    "convention", fx(r"\item[a')]", r"\item[\textup{a')}]"), conv=6))
A(F(85, "Proposition (4.9.6), label b)", "label 'b)' upright", "\\item[b)] (italic in the statement environment)",
    "convention", fx(r"\item[b)] $K'$", r"\item[\textup{b)}] $K'$"), conv=6))
A(F(85, "Proposition (4.9.6), label b')", "label \"b')\" upright", "\\item[b')] (italic in the statement environment)",
    "convention", fx(r"\item[b')]", r"\item[\textup{b')}]"), conv=6))
A(F(85, "proof of (4.9.6), line 1: \"Il est clair que a') entraîne a), et a) entraîne b')\"",
    "the four labels a'), a), a), b') italic", "plain", "italics",
    fx(r"que a') entraîne a), et a) entraîne b')", r"que \emph{a')} entraîne \emph{a)}, et \emph{a)} entraîne \emph{b')}")))
A(F(85, "proof of (4.9.6), line 2: \"b') entraîne b) et b) entraîne a')\"",
    "the four labels b'), b), b), a') italic", "plain", "italics",
    fx(r"symétriques, b')⏎entraîne b) et b) entraîne a')",
       r"symétriques, \emph{b')}⏎entraîne \emph{b)} et \emph{b)} entraîne \emph{a')}")))
A(F(85, "Corollaire (4.9.7), line 1: 'Sous les hypothèses de (4.9.6)'",
    "(4.9.6) upright inside the italic statement", "(4.9.6) italic (statement environment)",
    "convention", fx(r"hypothèses de (4.9.6)", r"hypothèses de \textup{(4.9.6)}"), "Enlarged crop.", conv=6))
A(F(85, "end of the page: '... désignons par W_i les composantes' / p. 86 'connexes de X_(k-bar)'",
    "the sentence runs on to p. 86 without a paragraph break",
    "blank line before \\oldpage[IV-2]{86} (end of this page's segment)",
    "other", fx(r"les composantes⏎⏎", r"les composantes⏎"),
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 86 edit that "
    "removes the blank line after \\oldpage[IV-2]{86}."))

# ---------------------------------------------------------------- page 86
A(F(86, "top of the page: 'connexes de X_(k-bar) (1<=i<=m); si' continues '... les composantes' of p. 85",
    "no paragraph break", "blank line after \\oldpage[IV-2]{86}",
    "other", fx(r"\oldpage[IV-2]{86}⏎⏎connexes de", r"\oldpage[IV-2]{86}⏎connexes de"),
    "Apply together with the p. 85 edit that removes the blank line before the marker."))
A(F(86, "proof of (4.9.7): 'donc U est une réunion d'un certain nombre de ces composantes'",
    "U without the bar (enlarged crop)", "$\\overline U$",
    "misprint_in_print", fx(r"donc⏎$\overline U$ est une réunion", r"donc⏎$U$ est une réunion"),
    "The TeX silently corrects the print: the open and closed part of X_(K) is U-bar (4.9.6); U is not defined.",
    corrected=r"$\overline U$"))
A(F(86, "end of the proof of (4.9.7): 'résulte par suite de (4.9.5, b))'",
    "'b)' italic (b and its parenthesis), the outer ')' upright", "plain 'b))'",
    "italics", fx(r"(4.9.5, b))", r"(4.9.5, \emph{b)})"), "Enlarged crop."))
A(F(86, "introduction of § 5: 'dans le chapitre 0, §§ 16 et 17'",
    "bold 0", "plain 0", "convention", fx(r"chapitre 0,", r"chapitre \textbf{0},"), conv=2))
A(F(86, "heading 5.1", "'5.1. Dimension des préschémas.' with a full stop", "\\subsection{Dimension des préschémas}",
    "punctuation", fx(r"\subsection{Dimension des préschémas}", r"\subsection{Dimension des préschémas.}"),
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same form as the earlier page fixes."))
A(F(86, "(5.1.1), line 1: 'Rappelons (0, 16.1)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,16.1)$", r"$(\mathbf{0},16.1)$"), conv=2))
A(F(86, "(5.1.1): 'dimension d'un anneau (0, 16.1.1)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,16.1.1)$", r"$(\mathbf{0},16.1.1)$"), conv=2))
A(F(86, "(5.1.1): 'espaces topologiques (0, 14.1.2)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,14.1.2)$", r"$(\mathbf{0},14.1.2)$"), conv=2))
A(F(86, "display (5.1.1.1)", "dim(Spec(A)) = dim(A) with no comma", "comma after \\dim(A)",
    "punctuation", fx(r"=\dim(A),", r"=\dim(A)"), "Enlarged crop; GLOBAL_ISSUES 73 (commas after displays)."))
A(F(86, "display (5.1.1.2)", "dim(V(J)) = dim(A/J) with no comma", "comma after \\dim(A/\\mathfrak J)",
    "punctuation", fx(r"=\dim(A/\mathfrak J),", r"=\dim(A/\mathfrak J)"), "Enlarged crop."))
A(F(86, "display (5.1.1.3)", "codim(V(J), Spec(A)) = ht(J) with no full stop", "full stop after \\operatorname{ht}(\\mathfrak J)",
    "punctuation", fx(r"=\operatorname{ht}(\mathfrak J).", r"=\operatorname{ht}(\mathfrak J)"), "Enlarged crop."))
A(F(86, "(5.1.1.4)", "number (5.1.1.4) bold, like the display tags", "\\textup{(5.1.1.4)} (medium weight)",
    "font", fx(r"\textup{(5.1.1.4)}", r"\textbf{(5.1.1.4)}"),
    "Hand-made number, not an environment heading (the print also indents these three paragraphs; layout only)."))
A(F(86, "(5.1.1.5)", "number (5.1.1.5) bold", "\\textup{(5.1.1.5)}",
    "font", fx(r"\textup{(5.1.1.5)}", r"\textbf{(5.1.1.5)}"), "As (5.1.1.4)."))
A(F(86, "(5.1.1.6)", "number (5.1.1.6) bold", "\\textup{(5.1.1.6)}",
    "font", fx(r"\textup{(5.1.1.6)}", r"\textbf{(5.1.1.6)}"), "As (5.1.1.4)."))
A(F(86, "(5.1.1), last paragraph: 'On rappelle qu'un anneau noethérien A est dit biéquidimensionnel'",
    "new indented paragraph after (5.1.1.6)", "runs on in the paragraph of (5.1.1.6) (single line break)",
    "other", fx(r"ont même hauteur.⏎On rappelle", r"ont même hauteur.⏎⏎On rappelle"), "Missing paragraph break."))
A(F(86, "display (5.1.2.1)", "codim(Y, X) = dim(O_X,y) with no full stop", "full stop after \\dim(\\mathcal O_{X,y})",
    "punctuation", fx(r"=\dim(\mathcal O_{X,y}).", r"=\dim(\mathcal O_{X,y})"), "Enlarged crop."))
A(F(86, "proof of (5.1.2): 'En effet (I, 2.4.2)'", "bold I", "plain I", "convention",
    fx(r"(I, 2.4.2)", r"(\textbf{I}, 2.4.2)"), conv=2))
A(F(86, "proof of (5.1.2), last line: '(I, 1.1.14)'", "bold I", "plain I", "convention",
    fx(r"(I, 1.1.14)", r"(\textbf{I}, 1.1.14)"), conv=2))

# ---------------------------------------------------------------- page 87
A(F(87, "proof of (5.1.3): 'et de (0, 14.2.6)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,14.2.6)$", r"$(\mathbf{0},14.2.6)$"), conv=2))
A(F(87, "proof of (5.1.4): '(en vertu de (I, 2.4.2))'", "bold I", "plain I", "convention",
    fx(r"(I, 2.4.2)", r"(\textbf{I}, 2.4.2)"), conv=2))
A(F(87, "proof of (5.1.4), second paragraph: 'quasi-compact (0_I, 2.1.3)'", "bold 0", "plain 0", "convention",
    fx(r"$(0_{\mathrm I},2.1.3)$", r"$(\mathbf{0}_{\mathrm I},2.1.3)$"), conv=2))
A(F(87, "(5.1.6), second paragraph: 'Rappelons (0, 16.2.3)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,16.2.3)$", r"$(\mathbf{0},16.2.3)$"), conv=2))
A(F(87, "end of the page: Corollaire (5.1.8) '... de l'ensemble Z' / p. 88 'des x∈X tels que f(x)=0'",
    "the statement runs on to p. 88 without a paragraph break", "blank line before \\oldpage[IV-2]{88}",
    "other", fx(r"l'ensemble $Z$⏎⏎", r"l'ensemble $Z$⏎"),
    "Spurious paragraph break inside the italic statement (GLOBAL_ISSUES 20). Apply together with the p. 88 edit "
    "that removes the blank line after the marker."))

# ---------------------------------------------------------------- page 88
A(F(88, "top of the page: 'des x∈X tels que f(x)=0' continues Corollaire (5.1.8) of p. 87",
    "no paragraph break", "blank line after \\oldpage[IV-2]{88}",
    "other", fx(r"\oldpage[IV-2]{88}⏎⏎des $x\in X$", r"\oldpage[IV-2]{88}⏎des $x\in X$"),
    "Apply together with the p. 87 edit that removes the blank line before the marker."))
A(F(88, "proof of (5.1.8), last line: 'en vertu de (0, 14.2.1)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,14.2.1)$", r"$(\mathbf{0},14.2.1)$"), conv=2))
A(F(88, "display (5.1.9.1), first line: 'dim(O_X,x) — codim(...)'",
    "long dash for the minus sign (bar 39-40 px at 300 dpi; the = bars 33-34 px)", "-",
    "convention", fx(r"O_{X,x})-\operatorname{codim}", r"O_{X,x})\setmin\operatorname{codim}"),
    "Subtraction with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.", conv=7))
A(F(88, "display (5.1.9.1), second line: 'dim(O_X,x) — dim(O_Y,x)'", "long dash (bar 40 px)", "-",
    "convention", fx(r"O_{X,x})-\dim", r"O_{X,x})\setmin\dim"), "As the previous entry.", conv=7))
A(F(88, "display (5.1.9.1), end", "no full stop after dim(O_Y,x)", "full stop",
    "punctuation", fx(r"O_{Y,x}).⏎\tag{5.1.9.1}", r"O_{Y,x})⏎\tag{5.1.9.1}"), "Enlarged crop."))
A(F(88, "proof of (5.1.9): 'qui sont en nombre fini'", "'fini' italic", "upright", "italics",
    fx(r"en nombre fini", r"en nombre \emph{fini}"), "Enlarged crop."))
A(F(88, "proof of (5.1.9): 'dim(A)=dim(A/p_i)+dim(A_p_i) (0, 16.1.4)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,16.1.4)$", r"$(\mathbf{0},16.1.4)$"), conv=2))
A(F(88, "proof of (5.1.9), last line: '((5.1.2) et (0, 14.2.6))'",
    "'((5.1.2) et (0, 14.2.6))': the reference (5.1.2) has its own parentheses", "'(5.1.2 et (0,14.2.6))'",
    "punctuation", fx(r"(5.1.2 et", r"((5.1.2) et"), "Enlarged crop. Does not overlap the next edit."))
A(F(88, "proof of (5.1.9), last line: '(0, 14.2.6)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,14.2.6)$", r"$(\mathbf{0},14.2.6)$"), conv=2))
A(F(88, "Proposition (5.1.10), label (i)", "label '(i)' upright", "\\item[(i)] (italic in the statement environment)",
    "convention", fx(r"\item[(i)]", r"\item[\textup{(i)}]"), "GLOBAL_ISSUES 16.", conv=6))
A(F(88, "Proposition (5.1.10) (i): '(ou, ce qui revient au même, tel que x soit isolé dans {x}-bar)'",
    "the parenthesis is roman, with 'isolé dans' italic", "all italic (statement environment)",
    "convention", fx(r"(ou, ce qui revient au même, tel que $x$ soit isolé dans⏎$\overline{\{x\}}$)",
                     r"\textup{(ou, ce qui revient au même, tel que $x$ soit \emph{isolé dans}⏎$\overline{\{x\}}$)}"),
    "Enlarged crop. \\emph inside \\textup gives the printed italic 'isolé dans'.", conv=6))
A(F(88, "Proposition (5.1.10), label (ii)", "label '(ii)' upright", "\\item[(ii)] (italic in the statement environment)",
    "convention", fx(r"\item[(ii)]", r"\item[\textup{(ii)}]"), "GLOBAL_ISSUES 16.", conv=6))
A(F(88, "Lemme (5.1.10.1): '(ou dans Z, ce qui revient au même)'",
    "the parenthesis is roman, with 'dans' italic", "all italic (statement environment)",
    "convention", fx(r"(ou dans $Z$, ce qui revient au même)", r"\textup{(ou \emph{dans} $Z$, ce qui revient au même)}"),
    "Enlarged crop.", conv=6))
A(F(88, "Lemme (5.1.10.1): 'et un point x∈Z', fermé dans Z''",
    "'dans' upright (emphasis inside the italic statement); 'fermé' italic", "'dans' italic",
    "convention", fx(r"fermé dans $Z'$. Alors", r"fermé \textup{dans} $Z'$. Alors"), "Enlarged crop.", conv=6))
A(F(88, "proof of (5.1.10.1): 'tel que Z'∩U soit fermé dans U'", "'dans' italic", "upright", "italics",
    fx(r"soit fermé dans $U$", r"soit fermé \emph{dans} $U$"), "The following 'aussi fermé dans U' is upright, as in the TeX."))
A(F(88, "proof of (5.1.10.1), second paragraph: 'à un préschéma (I, 5.2.1)'", "bold I", "plain I", "convention",
    fx(r"(I, 5.2.1)", r"(\textbf{I}, 5.2.1)"), conv=2))
A(F(88, "proof of (5.1.10.1), second paragraph: 'un ouvert affine dans Z'", "'dans' italic", "upright", "italics",
    fx(r"ouvert affine dans $Z$", r"ouvert affine \emph{dans} $Z$")))
A(F(88, "proof of (5.1.10.1), last line: 'un point fermé (0_I, 2.1.3)'", "bold 0", "plain 0", "convention",
    fx(r"$(0_{\mathrm I},2.1.3)$", r"$(\mathbf{0}_{\mathrm I},2.1.3)$"), conv=2))

# ---------------------------------------------------------------- page 89
A(F(89, "proof of (5.1.10) (ii): 'est isolé dans Spec(O_Z,z)'", "'isolé' italic", "upright", "italics",
    fx(r"est isolé dans", r"est \emph{isolé} dans")))
A(F(89, "proof of (5.1.10) (ii): 'tel que A_f soit un corps'", "'corps' italic", "upright", "italics",
    fx(r"soit un corps;", r"soit un \emph{corps};")))
A(F(89, "proof of (5.1.10) (ii): 'on sait (0, 16.3.3)'", "bold 0", "plain 0", "convention",
    fx(r"$(0,16.3.3)$", r"$(\mathbf{0},16.3.3)$"), conv=2))
A(F(89, "proof of (5.1.11): '(0_III, 9.1.1 et 9.1.5)'", "bold 0", "plain 0", "convention",
    fx(r"$(0_{\mathrm{III}},9.1.1", r"$(\mathbf{0}_{\mathrm{III}},9.1.1"), conv=2))
A(F(89, "(5.1.12): 'qui est fermé dans X (0_I, 5.2.2)'", "bold 0", "plain 0", "convention",
    fx(r"$(0_{\mathrm I},5.2.2)$", r"$(\mathbf{0}_{\mathrm I},5.2.2)$"), conv=2))
A(F(89, "(5.1.12): 'par définition (0, 16.1.7)'", "bold 0", "plain 0", "convention",
    fx(r"définition $(0,16.1.7)$", r"définition $(\mathbf{0},16.1.7)$"), conv=2))
A(F(89, "(5.1.12): 'par définition (0, 16.1.7) dim(F_x)=dim(Supp(F_x))'", "no comma after (0, 16.1.7)",
    "comma after the reference", "punctuation",
    fx(r",⏎$\dim(\mathcal F_x)=\dim(\operatorname{Supp}", r"⏎$\dim(\mathcal F_x)=\dim(\operatorname{Supp}"),
    "Enlarged crop. Does not overlap the previous edit."))
A(F(89, "(5.1.12), third paragraph: 'c'est-à-dire (0, 16.1.7)'", "bold 0", "plain 0", "convention",
    fx(r"c'est-à-dire $(0,16.1.7)$", r"c'est-à-dire $(\mathbf{0},16.1.7)$"), conv=2))
A(F(89, "(5.1.12), third paragraph, last word: 'l'anneau O_S,x est équidimensionnel.'", "'équidimensionnel' italic",
    "upright", "italics",
    fx(r"$\mathcal O_{S,x}$ est équidimensionnel.", r"$\mathcal O_{S,x}$ est \emph{équidimensionnel}."), "Enlarged crop."))
A(F(89, "(5.1.12), last paragraph: 'en vertu de (0, 16.1.7) et (5.1.4)'", "bold 0", "plain 0", "convention",
    fx(r"en vertu de $(0,16.1.7)$", r"en vertu de $(\mathbf{0},16.1.7)$"), conv=2))
A(F(89, "display (5.1.13.1)", "no full stop after dim(F_x)", "full stop", "punctuation",
    fx(r"\leq\dim(\mathcal F_x).", r"\leq\dim(\mathcal F_x)"), "Enlarged crop."))
A(F(89, "heading 5.2 (printed at the top of p. 90; in the TeX it stands before \\oldpage[IV-2]{90}, in this page's segment)",
    "'5.2. Dimension d'un préschéma algébrique.' with a full stop", "\\subsection{Dimension d'un préschéma algébrique}",
    "punctuation", fx(r"préschéma algébrique}", r"préschéma algébrique.}"),
    "GLOBAL_ISSUES 43/58. Apply BEFORE the next entry: the marker insertion moves the heading into the p. 90 segment."))
A(F(89, "page break 89/90: marker position (edit 1 of 2, insert)",
    "printed p. 89 ends with the proof of (5.1.13) ('Cela résulte aussitôt de (5.1.12.1) et des définitions.'); "
    "printed p. 90 begins with the heading '5.2. Dimension d'un préschéma algébrique.'",
    "\\oldpage[IV-2]{90} stands after \\subsection{Dimension d'un préschéma algébrique}, so the heading falls on p. 89",
    "marker", fx(r"\subsection{Dimension d'un", r"\oldpage[IV-2]{90}⏎\subsection{Dimension d'un"),
    "Apply after every other p. 89 entry and together with the p. 90 entry below, which removes the old marker. "
    "Result: '\\end{proof}\\n\\n\\oldpage[IV-2]{90}\\n\\subsection{Dimension d'un préschéma algébrique.}\\n\\n"
    "\\begin{proposition}[5.2.1]'."))

# ---------------------------------------------------------------- page 90 (other half of the p. 89 marker move)
A(F(90, "page break 89/90: marker position (edit 2 of 2, remove the old marker)", "see the previous entry",
    "\\oldpage[IV-2]{90} directly before \\begin{proposition}[5.2.1]",
    "marker", fx(r"\oldpage[IV-2]{90}⏎⏎\begin{proposition}[5.2.1]", r"\begin{proposition}[5.2.1]"),
    "Outside pp. 85-89 (page_090.tex): apply together with, and after, the p. 89 insertion. Skip both if the "
    "pp. 90-94 batch moves this marker another way."))

# ---------------------------------------------------------------- check and write
bad = 0
for d in findings:
    if not d["fix"]:
        continue
    t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = t.count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", d["page"], c, repr(d["fix"]["old"]))
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter((d["page"], "misprint" if d["kind"] == "misprint_in_print" else "convention" if d["kind"] == "convention" else "normal") for d in findings)
for p in sorted({d["page"] for d in findings}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("findings:", len(findings), "bad:", bad)
sys.exit(1 if bad else 0)
