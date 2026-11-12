# Builds findings_070_074.json and checks every fix's "old" against the page files and the source.
# Newlines in old/new are written as the pilcrow sign and converted to "\n".
import json, sys, os

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex"
OUT = os.path.join(RUN, "findings_070_074.json")

NL = "\u00b6"

F = []

def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------------------------------------------------------- page 70
P = 70
add(P, "first line: 'en ce point toutes les propriétés définies dans (6.8.1)'",
    "'toutes' italic", "plain 'toutes'", "italics",
    r"en ce point toutes les propriétés", r"en ce point \emph{toutes} les propriétés")
add(P, "Proposition (17.5.7): '(resp. intégralement clos, resp. géométriquement unibranche)'",
    "'(resp.', ', resp.' and ')' roman, 'intégralement clos' and 'géométriquement unibranche' italic ('réduit' italic) (crops p70_s1_reduit.png, p70_s1_resp.png)",
    "all italic (statement environment)", "convention",
    r"(resp. intégralement clos, resp. géométriquement unibranche)",
    r"\textup{(resp.}\ intégralement clos, \textup{resp.}\ géométriquement unibranche\textup{)}",
    conv=6)
add(P, "after (17.5.7): 'complété par Err_IV, 30.'",
    "bold upright 'Err' with a light roman subscript IV (crop p70_s1_err.png)",
    "Err$_{\\mathrm{IV}}$: normal-weight Err", "font",
    r"complété par Err$_{\mathrm{IV}}$, 30.", r"complété par \textbf{Err}$_{\mathrm{IV}}$, 30.",
    note="Same form as the p. 63 and p. 65 page fixes (\\textbf{Err}$_{\\mathrm{III}}$).")
add(P, "Proposition (17.5.8), label (i)", "label (i) upright", "\\item[(i)] (italic in the italic statement)",
    "convention", r"\item[(i)] On a $\dim", r"\item[\textup{(i)}] On a $\dim", conv=6)
add(P, "Proposition (17.5.8) (i): 'dim(O_{X,x} ⊗_{O_{Y,y}} k(y))'",
    "bold italic k (on the line, not in a subscript; crop p70_s2_dim.png)", "plain k", "convention",
    r"\otimes_{\sh{O}_{Y,y}}k(y))$.", r"\otimes_{\sh{O}_{Y,y}}\boldsymbol{k}(y))$.", conv=1)
add(P, "Proposition (17.5.8), label (ii)", "label (ii) upright", "\\item[(ii)] (italic in the italic statement)",
    "convention", r"\item[(ii)] On a $\operatorname{coprof}", r"\item[\textup{(ii)}] On a $\operatorname{coprof}", conv=6)
add(P, "Proposition (17.5.8), label (iii)", "label (iii) upright", "\\item[(iii)] (italic in the italic statement)",
    "convention", r"\item[(iii)] Pour que l'anneau", r"\item[\textup{(iii)}] Pour que l'anneau", conv=6)
add(P, "Proposition (17.5.8) (iii): '(S_n) (5.7.2) (resp. (R_n) (5.8.2))'",
    "'(5.7.2)', '(resp.' and '(5.8.2))' upright in the italic statement",
    "italic (statement environment)", "convention",
    r"(5.7.2) (resp. $(R_n)$ (5.8.2))", r"\textup{(5.7.2) (resp.}\ $(R_n)$ \textup{(5.8.2))}",
    conv=6, note="The capital S and R of (S_n), (R_n) are upright like every capital in the print's formulas (GLOBAL_ISSUES 17); not reported.")
add(P, "heading 17.6: 'Caractérisations des morphismes étales.'", "full stop after the title", "no full stop",
    "punctuation", r"\subsection{Caractérisations des morphismes étales}",
    r"\subsection{Caractérisations des morphismes étales.}", note="GLOBAL_ISSUES 43/58.")
add(P, "Théorème (17.6.1), labels a) and a')", "labels a), a') upright",
    "\\item[a)], \\item[a')] (italic in the italic statement)", "convention",
    r"\item[a)] $f$ est étale au point $x$." + NL + r"  \item[a')] $f$ est lisse au point",
    r"\item[\textup{a)}] $f$ est étale au point $x$." + NL + r"  \item[\textup{a$'$)}] $f$ est lisse au point",
    conv=6, note="GLOBAL_ISSUES 88. One edit for both labels (the line of a) recurs in (17.15.3) and (17.15.8)); prime written as in the earlier page fixes (\\textup{b$'$)}).")
add(P, "Théorème (17.6.1), label b)", "label b) upright", "\\item[b)] (italic in the italic statement)",
    "convention", r"\item[b)] $f$ est lisse au point $x$ et", r"\item[\textup{b)}] $f$ est lisse au point $x$ et", conv=6)
add(P, "Théorème (17.6.1) b): 'quasi-fini au point x (Err_III, 20).'",
    "bold upright 'Err' with a light roman subscript III; parentheses and 20 upright (crop p70_s3_err.png)",
    "(Err$_{\\mathrm{III}}$, 20): normal-weight Err, the whole reference italic in the italic statement", "font",
    r"quasi-fini au point $x$ (Err$_{\mathrm{III}}$, 20)",
    r"quasi-fini au point $x$ \textup{(\textbf{Err}$_{\mathrm{III}}$, 20)}",
    note="Same form as the p. 65 page fix of (17.4.3); the \\textup covers the upright reference (convention 6).")
add(P, "Théorème (17.6.1), label c)", "label c) upright", "\\item[c)] (italic in the italic statement)",
    "convention", r"\item[c)] $f$ est plat au point", r"\item[\textup{c)}] $f$ est plat au point", conv=6)
add(P, "Théorème (17.6.1), label c')", "label c') upright", "\\item[c')] (italic in the italic statement)",
    "convention", r"\item[c')] $f$ est plat au point", r"\item[\textup{c$'$)}] $f$ est plat au point", conv=6)
add(P, "Théorème (17.6.1) c'): 'extension finie séparable de k(y).'", "bold italic k", "plain k", "convention",
    r"extension finie séparable de $k(y)$.", r"extension finie séparable de $\boldsymbol{k}(y)$.", conv=1)
add(P, "Théorème (17.6.1), label d)", "label d) upright", "\\item[d)] (italic in the italic statement)",
    "convention", r"\item[d)] L'anneau", r"\item[\textup{d)}] L'anneau", conv=6)
add(P, "proof of (17.6.1): 'L'équivalence de a) et a') résulte aussitôt'", "labels a), a') italic", "plain labels",
    "italics", r"L'équivalence de a) et a') résulte", r"L'équivalence de \emph{a)} et \emph{a')} résulte",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'celle de a) et d) résulte'", "labels a), d) italic", "plain labels",
    "italics", r"celle de a) et d) résulte", r"celle de \emph{a)} et \emph{d)} résulte", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'de l'équivalence de a) et e) dans (17.4.1)'", "labels a), e) italic", "plain labels",
    "italics", r"l'équivalence de a) et e) dans", r"l'équivalence de \emph{a)} et \emph{e)} dans", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'de l'équivalence de a) et d) dans (17.5.1)'", "labels a), d) italic", "plain labels",
    "italics", r"l'équivalence de a) et d) dans (17.5.1)", r"l'équivalence de \emph{a)} et \emph{d)} dans (17.5.1)",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'L'équivalence de c) et c') résulte de l'équivalence de a) et d') dans (17.4.1).'",
    "labels c), c'), a), d') italic", "plain labels",
    "italics", r"L'équivalence de c) et c') résulte de l'équivalence de a) et d') dans",
    r"L'équivalence de \emph{c)} et \emph{c')} résulte de l'équivalence de \emph{a)} et \emph{d')} dans",
    note="GLOBAL_ISSUES 88. One edit for the four labels (the first clause recurs at (17.11.3)).")
add(P, "proof of (17.6.1): 'Le fait que a') implique c') découle'", "labels a'), c') italic", "plain labels",
    "italics", r"que a') implique c') découle", r"que \emph{a')} implique \emph{c')} découle", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'si c') est vérifiée'", "label c') italic", "plain label",
    "italics", r"si c') est vérifiée", r"si \emph{c')} est vérifiée", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'Le fait que a') implique b) résulte de (17.4.1, d')) et de (17.5.1, b)).'",
    "labels a'), b), d'), b) italic", "plain labels", "italics",
    r"que a') implique b) résulte de (17.4.1, d')) et de (17.5.1, b)).",
    r"que \emph{a')} implique \emph{b)} résulte de (17.4.1, \emph{d')}) et de (17.5.1, \emph{b)}).",
    note="GLOBAL_ISSUES 88. One edit for the four labels.")
add(P, "proof of (17.6.1): 'Il reste donc à voir que b) entraîne c), et'", "labels b), c) italic", "plain labels",
    "italics", r"voir que b) entraîne c), et", r"voir que \emph{b)} entraîne \emph{c)}, et", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'f^{-1}(y) est un k(y)-préschéma non ramifié sur k(y)'",
    "bold italic k (both)", "plain k", "convention",
    r"est un $k(y)$-préschéma non ramifié sur $k(y)$",
    r"est un $\boldsymbol{k}(y)$-préschéma non ramifié sur $\boldsymbol{k}(y)$",
    conv=1, note="Two occurrences in one edit.")
add(P, "proof of (17.6.1): 'à prouver que b) entraîne c) lorsque'", "labels b), c) italic", "plain labels",
    "italics", r"prouver que b) entraîne c) lorsque", r"prouver que \emph{b)} entraîne \emph{c)} lorsque",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1): 'une k-algèbre finie et locale'", "'finie' and 'locale' italic (crop p70_s4_finie.png)",
    "plain", "italics", r"$k$-algèbre finie et locale", r"$k$-algèbre \emph{finie} et \emph{locale}")
add(P, "proof of (17.6.1): '(0_I, 7.4.1)'", "bold 0 with subscript I (crop p70_s4_finie.png)", "plain 0",
    "convention", r"($0_{\mathrm I}$, 7.4.1)", r"($\mathbf{0}_{\mathrm I}$, 7.4.1)", conv=2,
    note="GLOBAL_ISSUES 35 form ($\\mathbf{0}_{\\mathrm I}$).")
add(P, "proof of (17.6.1): 'En vertu de l'hypothèse b),'", "label b) italic", "plain label",
    "italics", r"l'hypothèse b), $A$ est", r"l'hypothèse \emph{b)}, $A$ est", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.1), last line: 'donc (0, 19.6.5), A est un anneau local régulier'",
    "bold 0, no subscript (the speck above the comma is not a semicolon; crop p70_s4_zero_semicolon.png)",
    "plain 0", "convention", r"(0, 19.6.5)", r"(\textbf{0}, 19.6.5)", conv=2)
add(P, "page break 70/71 inside 'A est un anneau local régulier, donc | un corps puisqu'il est artinien'",
    "the sentence runs on to p. 71 ('un corps puisqu'il est artinien')",
    "blank line before \\oldpage[IV-4]{71}: a paragraph break inside the sentence", "marker",
    "anneau local régulier, donc" + NL + NL, "anneau local régulier, donc" + NL,
    note="GLOBAL_ISSUES 20/99. The blank line is the end of this page's segment, just before the p. 71 marker; no blank line follows the marker.")

# ---------------------------------------------------------------- page 71
P = 71
add(P, "l. 1: 'il résulte alors de (0, 19.6.5.1) que A'", "bold 0, no subscript", "plain 0", "convention",
    r"(0, 19.6.5.1)", r"(\textbf{0}, 19.6.5.1)", conv=2)
add(P, "Corollaire (17.6.2), label a)", "label a) upright", "\\item[a)] (italic in the italic statement)",
    "convention", r"\item[a)] $f$ est étale.", r"\item[\textup{a)}] $f$ est étale.", conv=6, note="GLOBAL_ISSUES 88.")
add(P, "Corollaire (17.6.2), label a')", "label a') upright", "\\item[a')]", "convention",
    r"\item[a')] $f$ est lisse et", r"\item[\textup{a$'$)}] $f$ est lisse et", conv=6)
add(P, "Corollaire (17.6.2), label b)", "label b) upright", "\\item[b)]", "convention",
    r"\item[b)] $f$ est lisse et", r"\item[\textup{b)}] $f$ est lisse et", conv=6)
add(P, "Corollaire (17.6.2) b): 'localement quasi-fini (Err_III, 20).'",
    "bold upright 'Err' with a light roman subscript III; parentheses and 20 upright",
    "(Err$_{\\mathrm{III}}$, 20): normal-weight Err, the whole reference italic", "font",
    r"localement quasi-fini (Err$_{\mathrm{III}}$, 20)",
    r"localement quasi-fini \textup{(\textbf{Err}$_{\mathrm{III}}$, 20)}",
    note="Same form as the p. 65 page fix of (17.4.3).")
add(P, "Corollaire (17.6.2), label c)", "label c) upright", "\\item[c)]", "convention",
    r"\item[c)] $f$ est plat et", r"\item[\textup{c)}] $f$ est plat et", conv=6)
add(P, "Corollaire (17.6.2), label c')", "label c') upright", "\\item[c')]", "convention",
    r"\item[c')] $f$ est plat, et toute", r"\item[\textup{c$'$)}] $f$ est plat, et toute", conv=6)
add(P, "Corollaire (17.6.2) c'): 'est un k(y)-schéma somme'", "bold italic k", "plain k", "convention",
    r"est un $k(y)$-schéma somme", r"est un $\boldsymbol{k}(y)$-schéma somme", conv=1)
add(P, "Corollaire (17.6.2) c'): 'extensions finies et séparables de k(y).'", "bold italic k", "plain k",
    "convention", r"finies et séparables de $k(y)$.", r"finies et séparables de $\boldsymbol{k}(y)$.", conv=1)
add(P, "Corollaire (17.6.2), label c'')", "label c'') upright", "\\item[c'')]", "convention",
    r"\item[c'')] $f$ est plat, et pour", r"\item[\textup{c$''$)}] $f$ est plat, et pour", conv=6)
add(P, "Corollaire (17.6.2) c''): 'toute extension algébriquement close k' de k(y)'", "bold italic k (k' light)",
    "plain k", "convention", r"close $k'$ de $k(y)$, la", r"close $k'$ de $\boldsymbol{k}(y)$, la", conv=1)
add(P, "Corollaire (17.6.2) c''): 'f^{-1}(y) ⊗_{k(y)} k' est somme'",
    "bold upright k in the subscript (crop p71_s2_otimes.png)", "plain k", "convention",
    r"f^{-1}(y)\otimes_{k(y)}k'$ est somme", r"f^{-1}(y)\otimes_{\mathbf{k}(y)}k'$ est somme", conv=1,
    note="Bold upright in subscripts (GLOBAL_ISSUES 48).")
add(P, "proof of (17.6.2): 'l'équivalence de c') et c'').'", "labels c'), c'') italic", "plain labels",
    "italics", r"l'équivalence de c') et c'').", r"l'équivalence de \emph{c')} et \emph{c'')}.", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.2): 'Il est clair que c') entraîne c'') par changement de base'", "labels c'), c'') italic",
    "plain labels", "italics", r"que c') entraîne c'') par", r"que \emph{c')} entraîne \emph{c'')} par",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.2): 'f^{-1}(y) ⊗_{k(y)} k' → f^{-1}(y) est ouvert'", "bold upright k in the subscript",
    "plain k", "convention", r"\otimes_{k(y)}k'\to f^{-1}(y)$", r"\otimes_{\mathbf{k}(y)}k'\to f^{-1}(y)$", conv=1,
    note="GLOBAL_ISSUES 48.")
add(P, "proof of (17.6.2): 'l'hypothèse c'') entraîne'", "label c'') italic", "plain label", "italics",
    r"l'hypothèse c'') entraîne", r"l'hypothèse \emph{c'')} entraîne", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.2): 'est une k(y)-algèbre finie, donc un anneau local artinien'", "bold italic k",
    "plain k", "convention", r"est une $k(y)$-algèbre finie, donc", r"est une $\boldsymbol{k}(y)$-algèbre finie, donc", conv=1)
add(P, "proof of (17.6.2): 'il résulte de c'') que'", "label c'') italic", "plain label", "italics",
    r"il résulte de c'') que", r"il résulte de \emph{c'')} que", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.2): 'Spec(A ⊗_{k(y)} k')'", "bold upright k in the subscript", "plain k", "convention",
    r"\Spec(A\otimes_{k(y)}k')", r"\Spec(A\otimes_{\mathbf{k}(y)}k')", conv=1, note="GLOBAL_ISSUES 48.")
add(P, "proof of (17.6.2): 'extension finie séparable de k(y) (4.6.1).'", "bold italic k", "plain k", "convention",
    r"séparable de $k(y)$ (4.6.1)", r"séparable de $\boldsymbol{k}(y)$ (4.6.1)", conv=1)
add(P, "Proposition (17.6.3): 'Soient Y un préschéma localement noethérien,'",
    "'localement noethérien' roman inside the italic statement (as in (17.5.3))", "italic", "convention",
    r"\label{IV.17.6.3}" + NL + r"Soient $Y$ un préschéma localement noethérien,",
    r"\label{IV.17.6.3}" + NL + r"Soient $Y$ un préschéma \textup{localement noethérien},", conv=6,
    note="The authors' emphasis of the hypothesis (same as the page fix of (17.5.3)).")
add(P, "Proposition (17.6.3): 'les conditions équivalentes a) à d) de (17.6.1) sont'",
    "labels a), d) and (17.6.1) upright, 'à', 'de' italic", "all italic", "convention",
    r"équivalentes a) à d) de (17.6.1) sont", r"équivalentes \textup{a)} à \textup{d)} de \textup{(17.6.1)} sont",
    conv=6, note="Same form as the page fix of (17.5.3).")
add(P, "Proposition (17.6.3), label e)", "label e) upright", "\\item[e)]", "convention",
    r"\item[e)] $\widehat B$ est une", r"\item[\textup{e)}] $\widehat B$ est une", conv=6)
add(P, "Proposition (17.6.3), label e')", "label e') upright", "\\item[e')]", "convention",
    r"\item[e')] $\widehat B$ est un", r"\item[\textup{e$'$)}] $\widehat B$ est un", conv=6)
add(P, "Proposition (17.6.3) e'): '(ce qui entraîne que B^ est une A^-algèbre finie).'",
    "the parenthesis roman, 'finie' italic", "all italic", "convention",
    r"(ce qui entraîne que $\widehat B$ est une $\widehat A$-algèbre finie)",
    r"\textup{(ce qui entraîne que $\widehat B$ est une $\widehat A$-algèbre} finie\textup{)}", conv=6)
add(P, "Proposition (17.6.3): 'Si de plus k(x)=k(y), ou si k est séparablement clos'",
    "bold italic k in k(x), k(y); the residue field k of A light italic", "plain k", "convention",
    r"Si de plus $k(x)=k(y)$, ou si", r"Si de plus $\boldsymbol{k}(x)=\boldsymbol{k}(y)$, ou si", conv=1,
    note="Two occurrences in one formula. 'Si de plus' starts flush left in the print, as the TeX gives after \\end{enumerate}.")
add(P, "Proposition (17.6.3), label e'')", "label e'') upright", "\\item[e'')]", "convention",
    r"\item[e'')] L'homomorphisme", r"\item[\textup{e$''$)}] L'homomorphisme", conv=6)
add(P, "proof of (17.6.3): 'L'équivalence de e) et de chacune'", "label e) italic", "plain label", "italics",
    r"L'équivalence de e) et de chacune", r"L'équivalence de \emph{e)} et de chacune", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.3): 'de (17.4.4, f')) et (17.5.3, d')).'", "labels f'), d') italic", "plain labels",
    "italics", r"(17.4.4, f')) et (17.5.3, d')).", r"(17.4.4, \emph{f')}) et (17.5.3, \emph{d')}).",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.3): 'Le fait que e) entraîne e') résulte de (17.4.4, f))'", "labels e), e'), f) italic",
    "plain labels", "italics", r"Le fait que e) entraîne e') résulte de (17.4.4, f))",
    r"Le fait que \emph{e)} entraîne \emph{e')} résulte de (17.4.4, \emph{f)})", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.3): 'et de (0, 19.7.1), compte tenu'", "bold 0, no subscript", "plain 0", "convention",
    r"(0, 19.7.1), compte", r"(\textbf{0}, 19.7.1), compte", conv=2)
add(P, "proof of (17.6.3): 'est alors une A^-algèbre finie (17.4.4)'", "'finie' italic", "plain", "italics",
    r"algèbre finie (17.4.4)", r"algèbre \emph{finie} (17.4.4)")
add(P, "proof of (17.6.3): '(0_III, 10.1.3)'", "bold 0 with subscript III", "plain 0", "convention",
    r"($0_{\mathrm{III}}$, 10.1.3)", r"($\mathbf{0}_{\mathrm{III}}$, 10.1.3)", conv=2)
add(P, "proof of (17.6.3): 'le fait que e') entraîne e) résulte'", "labels e'), e) italic", "plain labels",
    "italics", r"le fait que e') entraîne e) résulte", r"le fait que \emph{e')} entraîne \emph{e)} résulte",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.3): 'résulte de (17.4.4) et de (0, 19.7.1). Enfin'", "bold 0, no subscript", "plain 0",
    "convention", r"(17.4.4) et de (0, 19.7.1)", r"(17.4.4) et de (\textbf{0}, 19.7.1)", conv=2)
add(P, "proof of (17.6.3): 'Enfin, e') entraîne'", "label e') italic", "plain label", "italics",
    r"Enfin, e') entraîne", r"Enfin, \emph{e')} entraîne", note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.6.3): 'et si k(x)=k(y) ou si k est séparablement clos'", "bold italic k (both)", "plain k",
    "convention", r"et si $k(x)=k(y)$ ou si", r"et si $\boldsymbol{k}(x)=\boldsymbol{k}(y)$ ou si", conv=1,
    note="Two occurrences in one formula.")
add(P, "Proposition (17.6.4): 'Sous les hypothèses de (17.6.3), si'", "(17.6.3) upright", "italic", "convention",
    r"hypothèses de (17.6.3), si", r"hypothèses de \textup{(17.6.3)}, si", conv=6)
add(P, "Proposition (17.6.4): 'au point x, on a dim(O_{X,x})=dim(O_{Y,y})'",
    "the 'a' of 'on a' is BOLD italic (wrong fount): side-by-side crop p71_a_compare.png against the light 'a' of 'au' on the same line (crop p71_s4_ona.png)",
    "normal italic (silent correction)", "misprint_in_print",
    r"$x$, on a $\dim", r"$x$, on \textbf{a} $\dim",
    note="Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). The fix restores the printed reading; independent of the convention-6 edit before it.",
    corrected=r"$x$, on a $\dim")
add(P, "last line: 'puisque x est isolé dans sa fibre f^{-1}(y)'",
    "the x is BOLD italic (wrong fount): side-by-side crops p71_x_compare.png, p71_x_compare2.png against the light italic x of 'au point x' (p. 70) and 'x∈X_y' (p. 71)",
    "$x$ (silent correction)", "misprint_in_print",
    r"puisque $x$ est isolé", r"puisque $\boldsymbol{x}$ est isolé",
    note="Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). The fix restores the printed reading.",
    corrected=r"puisque $x$ est isolé")

# ---------------------------------------------------------------- page 72
P = 72
add(P, "heading 17.7: 'Propriétés de descente, de passage à la limite et de constructibilité.'",
    "full stop after the title; the page begins with the heading (marker 72 in place)", "no full stop",
    "punctuation", r"de passage à la limite et de constructibilité}", r"de passage à la limite et de constructibilité.}",
    note="GLOBAL_ISSUES 43/58.")
add(P, "Proposition (17.7.1), label (i)", "label (i) upright", "\\item[(i)]", "convention",
    r"\item[(i)] Si $f'$ est non ramifié", r"\item[\textup{(i)}] Si $f'$ est non ramifié", conv=6)
add(P, "Proposition (17.7.1), label (ii)", "label (ii) upright", "\\item[(ii)]", "convention",
    r"\item[(ii)] Supposons de plus que $g$ soit plat au point", r"\item[\textup{(ii)}] Supposons de plus que $g$ soit plat au point", conv=6)
add(P, "Proposition (17.7.1) (ii): 'si f' est lisse (resp. étale) au point x', f est lisse (resp. étale) au point x.'",
    "'(resp.' and ')' roman twice, 'étale' italic (crop p72_s1_ii.png)", "all italic", "convention",
    r"lisse (resp. étale) au point $x'$, $f$ est lisse (resp. étale) au point $x$.",
    r"lisse \textup{(resp.}\ étale\textup{)} au point $x'$, $f$ est lisse \textup{(resp.}\ étale\textup{)} au point $x$.",
    conv=6, note="Two occurrences in one edit.")
add(P, "proof of (17.7.1): 'f'^{-1}(y') = f^{-1}(y) ⊗_{k(y)} k(y')'",
    "bold upright k in the subscript, bold italic k in k(y') (crop p72_s1_otimes.png)", "plain k (both)",
    "convention", r"f^{-1}(y)\otimes_{k(y)}k(y')$", r"f^{-1}(y)\otimes_{\mathbf{k}(y)}\boldsymbol{k}(y')$", conv=1,
    note="One edit for both k (GLOBAL_ISSUES 48: bold upright in the subscript, bold italic on the line).")
add(P, "proof of (17.7.1) (i): 'en ce point (17.4.1, d))'", "label d) italic, parenthesis included",
    "$d$): italic letter, upright parenthesis", "italics", r"en ce point (17.4.1, $d$))", r"en ce point (17.4.1, \emph{d)})",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.7.1) (i): 'étale en ce point (17.6.1, c))'", "label c) italic, parenthesis included",
    "$c$): italic letter, upright parenthesis", "italics", r"(17.6.1, $c$))", r"(17.6.1, \emph{c)})",
    note="GLOBAL_ISSUES 88.")
add(P, "proof of (17.7.1) (ii): 'f∘g'=g∘f' est un morphisme plat au point X', d'où la conclusion'",
    "capital X' (crop p72_s2_pointX.png)", "$X'$: the TeX keeps the printed reading", "misprint_in_print",
    None, None, conf="high",
    note="The point is x' (the composite X'→Y is flat at x', whence f flat at x by (2.2.11, (iv))). No erratum in Liste 3.",
    corrected=r"plat au point $x'$, d'où")
add(P, "proof of (17.7.1) (ii): 'Supposons de plus que f' soit étale au point x' de sorte que x' est isolé'",
    "no comma after 'au point x'' (crop p72_s2_virgule.png)", "comma: 'au point $x'$, de sorte que'",
    "punctuation", r"au point $x'$, de sorte que", r"au point $x'$ de sorte que")
add(P, "proof of (17.7.1) (ii): 'est un morphisme ouvert (2.4.10)'", "'ouvert' italic", "plain", "italics",
    r"un morphisme ouvert (2.4.10)", r"un morphisme \emph{ouvert} (2.4.10)")
add(P, "Corollaire (17.7.2), label (i)", "label (i) upright (on the heading line in the print; layout not reported)",
    "\\item[(i)]", "convention", r"\item[(i)] Avec", r"\item[\textup{(i)}] Avec", conv=6)
add(P, "Corollaire (17.7.2) (i): '(17.7.1), soit U (resp. U') l'ensemble des points de X (resp. X') où f (resp. f') est non ramifié'",
    "(17.7.1), '(resp.' and the parentheses roman (crop p72_s3_1772.png)", "all italic", "convention",
    r"(17.7.1), soit $U$ (resp. $U'$) l'ensemble des points de $X$ (resp. $X'$) où $f$ (resp. $f'$) est non ramifié",
    r"\textup{(17.7.1)}, soit $U$ \textup{(resp.}\ $U'$\textup{)} l'ensemble des points de $X$ \textup{(resp.}\ $X'$\textup{)} où $f$ \textup{(resp.}\ $f'$\textup{)} est non ramifié",
    conv=6, note="One edit for the reference and the three resp. parentheses.")
add(P, "Corollaire (17.7.2) (i): 'alors on a U' = g^{-1}(U).'",
    "g^{-1}(U), no prime on g (crop p72_s3_U.png)", "$U'=g'^{-1}(U)$: silent correction", "misprint_in_print",
    r"$U'=g'^{-1}(U)$", r"$U'=g^{-1}(U)$",
    note="U is a subset of X and g: Y'→Y; the inverse image is under the projection g': X'→X. The fix restores the printed reading. No erratum in Liste 3.",
    corrected=r"$U'=g'^{-1}(U)$")
add(P, "Corollaire (17.7.2), label (ii)", "label (ii) upright", "\\item[(ii)]", "convention",
    r"\item[(ii)] Supposons de plus que $g$ soit plat, et", r"\item[\textup{(ii)}] Supposons de plus que $g$ soit plat, et", conv=6)
add(P, "Corollaire (17.7.2) (ii): 'soit V (resp. V') l'ensemble des points de X où f (resp. f') est lisse'",
    "'(resp.' and the parentheses roman (crop p72_s3_1772.png)", "all italic", "convention",
    r"soit $V$ (resp. $V'$) l'ensemble des points de $X$ où $f$ (resp. $f'$) est lisse",
    r"soit $V$ \textup{(resp.}\ $V'$\textup{)} l'ensemble des points de $X$ où $f$ \textup{(resp.}\ $f'$\textup{)} est lisse",
    conv=6, note="Two occurrences in one edit.")
add(P, "Corollaire (17.7.2) (ii): 'alors V' = g^{-1}(V).'",
    "g^{-1}(V), no prime on g (crop p72_s3_V.png)", "$V'=g'^{-1}(V)$: silent correction", "misprint_in_print",
    r"alors $V'=g'^{-1}(V)$", r"alors $V'=g^{-1}(V)$",
    note="Same slip as in (i): V is a subset of X, the inverse image is under g'. The print (and the TeX) also say 'des points de X' without '(resp. X')' here (an ellipsis, cf. (i)); not listed separately. The fix restores the printed reading.",
    corrected=r"alors $V'=g'^{-1}(V)$")
add(P, "Corollaire (17.7.3), label (i)", "label (i) upright", "\\item[(i)]", "convention",
    r"\item[(i)] Supposons $g$ surjectif", r"\item[\textup{(i)}] Supposons $g$ surjectif", conv=6)
add(P, "Corollaire (17.7.3), label (ii)", "label (ii) upright", "\\item[(ii)]", "convention",
    r"\item[(ii)] Soient $f:X\to Y$ un $S$-morphisme", r"\item[\textup{(ii)}] Soient $f:X\to Y$ un $S$-morphisme", conv=6)
add(P, "Corollaire (17.7.3) (ii): 'localement de présentation finie, ou que g soit quasi-compact'",
    "'ou' roman (crop p72_s3_ou.png)", "italic", "convention",
    r"finie, ou que $g$ soit quasi-compact", r"finie, \textup{ou} que $g$ soit quasi-compact", conv=6,
    note="The authors' emphasis of the alternative.")
add(P, "Corollaire (17.7.3) (ii): 'pour que f soit lisse (resp. non ramifié, resp. étale), il faut et il suffit que f' le soit.'",
    "'(resp.', ', resp.' and ')' roman, 'non ramifié', 'étale' italic", "all italic", "convention",
    r"lisse (resp. non ramifié, resp. étale), il faut et il suffit que $f'$ le soit.",
    r"lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)}, il faut et il suffit que $f'$ le soit.", conv=6)
add(P, "proof of (17.7.3): 'Si g est quasi-compact et f' lisse (...), f' est localement de présentation finie par (2.7.1, (iv))'",
    "the second f' (crops p72_s4_fprime.png, p72_s4_fprime_z.png)", "$f'$: the TeX keeps the printed reading",
    "misprint_in_print", None, None, conf="medium",
    note="f' is locally of finite presentation by the definition of smooth (resp. unramified, étale) morphisms; (2.7.1, (iv)) is the descent statement that gives it for f, which is 'le premier cas' (f locally of finite presentation). No erratum in Liste 3.",
    corrected=r"étale), $f$ est localement de présentation finie par (2.7.1, (iv))")
add(P, "page break 72/73 inside 'et g': X'→X les | projections canoniques'",
    "the sentence runs on to p. 73 ('projections canoniques. Soit V')",
    "blank line before \\oldpage[IV-4]{73}: a paragraph break inside the sentence", "marker",
    r"$g':X'\to X$ les" + NL + NL, r"$g':X'\to X$ les" + NL,
    note="GLOBAL_ISSUES 20/99. The blank line is the end of this page's segment; the blank line after the marker is removed by the first p. 73 finding (apply both).")

# ---------------------------------------------------------------- page 73
P = 73
add(P, "top of page_073.tex: blank line after \\oldpage[IV-4]{73}",
    "p. 73 begins mid-sentence ('projections canoniques.')",
    "blank line after the marker: a paragraph break inside the sentence", "marker",
    r"\oldpage[IV-4]{73}" + NL + NL + "projections", r"\oldpage[IV-4]{73}" + NL + "projections",
    note="GLOBAL_ISSUES 20/99. Apply together with the p. 72 finding that removes the blank line before the marker.")
add(P, "Proposition (17.7.4): 'Soit V (resp. V') l'ensemble des x∈X (resp. x'∈X')'",
    "'(resp.' and the parentheses roman (crop p73_s1_top.png)", "all italic", "convention",
    r"(resp. $V'$) l'ensemble des $x\in X$ (resp. $x'\in X'$)",
    r"\textup{(resp.}\ $V'$\textup{)} l'ensemble des $x\in X$ \textup{(resp.}\ $x'\in X'$\textup{)}",
    conv=6, note="Two occurrences in one edit.")
add(P, "Proposition (17.7.4): '(resp. où f' possède la même propriété)'",
    "'(resp.' and ')' roman, 'où f' possède la même propriété' italic", "all italic", "convention",
    r"(resp. où $f'$ possède la même propriété)", r"\textup{(resp.}\ où $f'$ possède la même propriété\textup{)}", conv=6)
add(P, "Proposition (17.7.4), labels (i), (ii), (iii)", "labels upright", "\\item[(i)], \\item[(ii)], \\item[(iii)] (italic in the italic statement)",
    "convention",
    r"\item[(i)] localement de type fini;" + NL + r"  \item[(ii)] localement de présentation finie;" + NL + r"  \item[(iii)] plat;",
    r"\item[\textup{(i)}] localement de type fini;" + NL + r"  \item[\textup{(ii)}] localement de présentation finie;" + NL + r"  \item[\textup{(iii)}] plat;",
    conv=6, note="One edit for three labels (the lines of (i) and (ii) recur in (17.7.5)).")
add(P, "Proposition (17.7.4), label (iv)", "label upright", "\\item[(iv)]", "convention",
    r"\item[(iv)] non ramifié;", r"\item[\textup{(iv)}] non ramifié;", conv=6)
add(P, "Proposition (17.7.4), label (v)", "label upright", "\\item[(v)]", "convention",
    r"\item[(v)] lisse;", r"\item[\textup{(v)}] lisse;", conv=6)
add(P, "Proposition (17.7.4), label (vi)", "label upright", "\\item[(vi)]", "convention",
    r"\item[(vi)] étale.", r"\item[\textup{(vi)}] étale.", conv=6)
add(P, "Proposition (17.7.4): 'Alors on a V'=g'^{-1}(V)' after the list",
    "'Alors' opens an indented paragraph (at the paragraph indent, like the list items)",
    "text follows \\end{enumerate} without a blank line (set without indent)", "other",
    r"\end{enumerate}" + NL + "Alors on a $V'", r"\end{enumerate}" + NL + NL + "Alors on a $V'",
    note="Paragraph after the list, indented as printed (same form as the IV-2/IV-3 \\end{enumerate} fixes; GLOBAL_ISSUES 80).")
add(P, "Proposition (17.7.4): '(autrement dit, pour que f' ait la propriété considérée en un point x', il faut et il suffit que f ait cette propriété au point x)'",
    "the whole parenthesis roman (crop p73_s2_alors.png)", "italic (statement environment)", "convention",
    r"(autrement dit, pour que $f'$ ait la propriété considérée en un point $x'$, il faut et il suffit que $f$ ait cette propriété au point $x$)",
    r"\textup{(autrement dit, pour que $f'$ ait la propriété considérée en un point $x'$, il faut et il suffit que $f$ ait cette propriété au point $x$)}",
    conv=6)
add(P, "proof of (17.7.4): 'le composé V' --g''--> W --f|W--> Y (où g'' est la restriction de g')'",
    "the composite is set in the running text", "set as a display \\[ ... \\]", "other",
    "le composé" + NL + r"\[" + NL + r"V'\xrightarrow{g''}W\xrightarrow{f|W}Y" + NL + r"\]" + NL + "(où",
    r"le composé $V'\xrightarrow{g''}W\xrightarrow{f|W}Y$ (où",
    note="Formula displayed in the TeX where the print sets it in the line (the second composite of the sentence is already inline).")
add(P, "proof of (17.7.4): '(donc fidèlement plat)'", "'fidèlement plat' italic", "plain", "italics",
    r"(donc fidèlement plat)", r"(donc \emph{fidèlement plat})")
add(P, "Lemme (17.7.5), labels (i), (ii), (iii)", "labels upright",
    "\\item[(i)], \\item[(ii)], \\item[(iii)] (italic in the italic statement)", "convention",
    r"\item[(i)] localement de type fini;" + NL + r"  \item[(ii)] localement de présentation finie;" + NL + r"  \item[(iii)] de type fini.",
    r"\item[\textup{(i)}] localement de type fini;" + NL + r"  \item[\textup{(ii)}] localement de présentation finie;" + NL + r"  \item[\textup{(iii)}] de type fini.",
    conv=6, note="One edit for three labels (the lines of (i) and (ii) recur in (17.7.4)).")
add(P, "Lemme (17.7.5): 'Alors g a la même propriété.' after the list",
    "'Alors g a la même propriété.' is an indented paragraph of its own",
    "text follows \\end{enumerate} without a blank line (set without indent)", "other",
    r"\end{enumerate}" + NL + r"Alors $g$ a", r"\end{enumerate}" + NL + NL + r"Alors $g$ a",
    note="Paragraph after the list, indented as printed (GLOBAL_ISSUES 80).")
add(P, "Lemme (17.7.5): 'Si en outre f est quasi-compact ou g quasi-séparé, ...'",
    "'Si en outre' opens a new indented paragraph", "same paragraph as 'Alors g a la même propriété.'", "other",
    r"la même propriété. Si en outre", r"la même propriété." + NL + NL + "Si en outre",
    note="Missing paragraph break of the print. Independent of the previous edit.")
add(P, "Lemme (17.7.5), label (iv)", "label upright", "\\item[(iv)]", "convention",
    r"\item[(iv)] être de présentation finie.", r"\item[\textup{(iv)}] être de présentation finie.", conv=6)
add(P, "proof of (17.7.5): 'un voisinage ouvert affine W de z=g(y) dans Z contenant g(V) tels que'",
    "no comma after g(V) (crop p73_s3_gV.png)", "comma: 'contenant $g(V)$, tels que'", "punctuation",
    r"contenant $g(V)$, tels que", r"contenant $g(V)$ tels que")
add(P, "proof of (17.7.5): 'le morphisme f_1 : U→V' restriction de f soit plat'",
    "no comma after V' (crop p73_s4_f1g1.png)", "comma: '$f_1:U\\to V'$, restriction'", "punctuation",
    r"$f_1:U\to V'$, restriction", r"$f_1:U\to V'$ restriction")
add(P, "proof of (17.7.5): 'le morphisme g_1 : V'→W restriction de g tel que g_1∘f_1'",
    "no comma after 'restriction de g' (crop p73_s4_f1g1.png)", "comma: 'restriction de $g$, tel que'", "punctuation",
    r"restriction de $g$, tel que", r"restriction de $g$ tel que")
add(P, "page break 73/74 inside 'le morphisme f_2 : f_1^{-1}(V)→V, | restriction de f_1'",
    "the sentence runs on to p. 74 ('restriction de f_1, est encore')",
    "blank line before \\oldpage[IV-4]{74}: a paragraph break inside the sentence", "marker",
    r"f_2:f_1^{-1}(V)\to V$," + NL + NL, r"f_2:f_1^{-1}(V)\to V$," + NL,
    note="GLOBAL_ISSUES 20/99. The blank line is the end of this page's segment; the blank line after the marker is removed by the first p. 74 finding (apply both).")

# ---------------------------------------------------------------- page 74
P = 74
add(P, "top of page_074.tex: blank line after \\oldpage[IV-4]{74}",
    "p. 74 begins mid-sentence ('restriction de f_1, est encore')",
    "blank line after the marker: a paragraph break inside the sentence", "marker",
    r"\oldpage[IV-4]{74}" + NL + NL + "restriction", r"\oldpage[IV-4]{74}" + NL + "restriction",
    note="GLOBAL_ISSUES 20/99. Apply together with the p. 73 finding that removes the blank line before the marker.")
add(P, "Proposition (17.7.7): 'Supposons que g soit plat au point x.'",
    "'plat' roman inside the italic statement (crop p74_s3_1777.png)", "italic", "convention",
    r"soit plat au point $x$. Alors", r"soit \textup{plat} au point $x$. Alors", conv=6,
    note="The authors' emphasis of the hypothesis.")
add(P, "Proposition (17.7.7): 'si h est lisse (resp. non ramifié, resp. étale) au point x, f est lisse (resp. non ramifié, resp. étale) au point y.'",
    "'(resp.', ', resp.' and ')' roman twice, 'non ramifié', 'étale' italic (crop p74_s3_1777.png)", "all italic",
    "convention",
    r"lisse (resp. non ramifié, resp. étale) au point $x$, $f$ est lisse (resp. non ramifié, resp. étale) au point $y$.",
    r"lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)} au point $x$, $f$ est lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)} au point $y$.",
    conv=6, note="Two occurrences in one edit.")
add(P, "proof of (17.7.7): 'h^{-1}(s) est étale sur k(s) au point x (resp.'", "bold italic k", "plain k", "convention",
    r"étale sur $k(s)$ au point $x$ (resp.", r"étale sur $\boldsymbol{k}(s)$ au point $x$ (resp.", conv=1)
add(P, "proof of (17.7.7): 'f^{-1}(s) est étale sur k(s) au point y)'", "bold italic k", "plain k", "convention",
    r"étale sur $k(s)$ au point $y$)", r"étale sur $\boldsymbol{k}(s)$ au point $y$)", conv=1)
add(P, "proof of (17.7.7): 'f^{-1}(s) est lisse (resp. étale) sur k(s) au point x.'", "bold italic k", "plain k",
    "convention", r"étale) sur $k(s)$ au point $x$.", r"étale) sur $\boldsymbol{k}(s)$ au point $x$.", conv=1,
    note="Same phrase as the misprint entry below (the misprint has no diplomatic edit).")
add(P, "proof of (17.7.7): 'de dire que f est lisse (resp. étale) au point y, ou que f^{-1}(s) est lisse (resp. étale) sur k(s) au point x.'",
    "'au point x' (crop p74_s3_pointx.png)", "'au point $x$': the TeX keeps the printed reading", "misprint_in_print",
    None, None, conf="medium",
    note="f^{-1}(s) is the fibre of f: Y→S, and by (17.5.1) (f flat at y) f is smooth (resp. étale) at y iff f^{-1}(s) is so over k(s) at y. No erratum in Liste 3. In the corrected edition change the x after the convention-1 edit above ('...sur $\\boldsymbol{k}(s)$ au point $x$.').",
    corrected=r"sur $\boldsymbol{k}(s)$ au point $y$.")
add(P, "proof of (17.7.7): 'est le spectre d'un corps.'", "'spectre d'un corps' italic", "plain", "italics",
    r"cas où $S=\Spec(k)$ est le spectre d'un corps.", r"cas où $S=\Spec(k)$ est le \emph{spectre d'un corps}.")
add(P, "proof of (17.7.7) (i): 'et que h est lisse, et on est ramené'", "'lisse' italic", "plain", "italics",
    r"que $h$ est lisse, et on", r"que $h$ est \emph{lisse}, et on")
add(P, "proof of (17.7.7) (i): 'prouver que f est alors lisse.'", "'lisse' italic", "plain", "italics",
    r"$f$ est alors lisse.", r"$f$ est alors \emph{lisse}.")
add(P, "page break 74/75 inside 'Si k' est une extension algébriquement | close de k'",
    "the sentence runs on to p. 75 ('close de k, X⊗_k k'...'; crop p75_s1_top.png)",
    "blank line before \\oldpage[IV-4]{75}: a paragraph break inside the sentence", "marker",
    "extension algébriquement" + NL + NL, "extension algébriquement" + NL,
    note="GLOBAL_ISSUES 20/99. The blank line is the end of this page's segment. The blank line AFTER \\oldpage[IV-4]{75} (before 'close de $k$') lies in page_075.tex and must go too (p. 75 batch).")

# ---------------------------------------------------------------- checks
src = open(SRC, encoding="utf-8", newline="").read()
assert "\r" not in src
pages = {}
for p in range(70, 75):
    t = open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="").read().replace("\r\n", "\n")
    pages[p] = t

bad = 0
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    o = fx["old"]
    cp = pages[d["page"]].count(o)
    cs = src.count(o)
    if cp != 1 or cs != 1:
        bad += 1
        print("NOT UNIQUE", i, d["page"], repr(o)[:90], "page:", cp, "src:", cs)
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO CHANGE", i, repr(o)[:80])

# overlaps between fixes on the same page (by position in the source)
spans = []
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    pos = src.find(fx["old"])
    spans.append((pos, pos + len(fx["old"]), i))
spans.sort()
for a, b in zip(spans, spans[1:]):
    if b[0] < a[1]:
        bad += 1
        print("OVERLAP", a, b, repr(F[a[2]]["fix"]["old"])[:60], repr(F[b[2]]["fix"]["old"])[:60])

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(70, 75):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "problems", bad)

if bad == 0 or "--force" in sys.argv:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
