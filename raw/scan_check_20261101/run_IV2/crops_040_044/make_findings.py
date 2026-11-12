import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV2"
OUT = os.path.join(RUN, "findings_040_044.json")
NL = "\n"


def s(x):
    return None if x is None else x.replace("<NL>", NL)


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, fix_null=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if fix_null else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------- page 40 ----------------
L.append(F(40, "heading of 3.2", "3.2. Décompositions irredondantes. (final full stop)",
           r"\subsection{Décompositions irredondantes} (no full stop)", "punctuation", None, "high",
           r"\subsection{Décompositions irredondantes}", r"\subsection{Décompositions irredondantes.}",
           "subsection title lacks the printed full stop"))
L.append(F(40, "Définition (3.2.2): 'On dit que F est réduit s'il vérifie'",
           "'réduit' italic like the rest of the definition",
           r"\emph{réduit} inside the italic definition environment (comes out upright)", "convention", 6, "high",
           r"est \emph{réduit}<NL>s'il", r"est réduit<NL>s'il",
           "printed italic word left upright by \\emph"))
L.append(F(40, "paragraph after (3.2.2): 'si F_x est un O_x-module réduit; cela signifie'",
           "O_x-module réduit, with 'module réduit' in italics",
           r"$\mathcal O_x$-module réduit (roman)", "italics", None, "high",
           r"$\mathcal O_x$-module réduit~;", r"$\mathcal O_x$-\emph{module réduit}~;",
           "the defined phrase is italic in the print"))
L.append(F(40, "paragraph after (3.2.2): 'sur le schéma local Spec(O_x), F~_x est réduit'",
           "tilde over the script F only, subscript x outside the tilde",
           r"\widetilde{\mathcal F_x}", "convention", 8, "high",
           r"\widetilde{\mathcal F_x}", r"\widetilde{\mathcal F}_x", ""))
# ---------------- page 41 ----------------
L.append(F(41, "first paragraph: 'dire que X est réduit au point x'",
           "only 'réduit' italic; 'au point x' roman (start of the next line)",
           r"\emph{réduit au point $x$}", "italics", None, "high",
           r"\emph{réduit au point $x$}", r"\emph{réduit} au point $x$", ""))
L.append(F(41, "proof of (3.2.3): 'l'espace sous-jacent (I, 5.2.1)'", "(I, 5.2.1) with bold I",
           "(I, 5.2.1)", "convention", 2, "high", "(I, 5.2.1)", r"(\textbf{I}, 5.2.1)", ""))
L.append(F(41, "proof of (3.2.3): 'donc au corps k(x) = O_{X',x}'", "bold italic k in k(x)",
           r"$k(x)=\mathcal O_{X',x}$", "convention", 1, "high",
           r"$k(x)=\mathcal O_{X',x}$", r"$\boldsymbol{k}(x)=\mathcal O_{X',x}$", ""))
L.append(F(41, "proof of (3.2.3): '(I, 7.4.6 et 7.4.2)'", "(I, 7.4.6 et 7.4.2) with bold I",
           "(I, 7.4.6 et 7.4.2)", "convention", 2, "high",
           "(I, 7.4.6 et 7.4.2)", r"(\textbf{I}, 7.4.6 et 7.4.2)", ""))
L.append(F(41, "Définition (3.2.4): 'On dit que F est irredondant si'",
           "'irredondant' italic like the rest of the definition",
           r"\emph{irredondant} inside the italic definition (comes out upright)", "convention", 6, "high",
           r"\emph{irredondant} si", "irredondant si", ""))
L.append(F(41, "Définition (3.2.4): 'on dit que F est intègre si de plus'",
           "'intègre' italic like the rest of the definition",
           r"\emph{intègre} inside the italic definition (comes out upright)", "convention", 6, "high",
           r"\emph{intègre} si de plus", "intègre si de plus", ""))
L.append(F(41, "Définition (3.2.4): '(autrement dit si long(F_x) = 1)'",
           "the parenthesis '(autrement dit si long(F_x)=1)' is roman inside the italic definition",
           "plain text inside the italic definition (comes out italic)", "convention", 6, "high",
           r"(autrement dit si<NL>$\operatorname{long}(\mathcal F_x)=1$)",
           r"\textup{(autrement dit si<NL>$\operatorname{long}(\mathcal F_x)=1$)}", ""))
L.append(F(41, "Définition (3.2.4): 'est primaire dans F si F/G est irredondant'",
           "'primaire dans F' italic like the rest of the definition",
           r"\emph{primaire dans $\mathcal F$} inside the italic definition (comes out upright)", "convention", 6,
           "high", r"\emph{primaire dans $\mathcal F$} si", r"primaire dans $\mathcal F$ si", ""))
L.append(F(41, "paragraph after (3.2.4): 'si F_x est un O_x-module intègre : cela signifie'",
           "O_x-module intègre, with 'module intègre' in italics",
           r"$\mathcal O_x$-module \emph{intègre} ('module' roman)", "italics", None, "high",
           r"$\mathcal O_x$-module \emph{intègre}~:", r"$\mathcal O_x$-\emph{module intègre}~:", ""))
L.append(F(41, "end of page: 'tel que F|U' / p. 42 'soit un O_U-Module'",
           "one sentence running over the page break",
           r"blank line before \oldpage[IV-2]{42} (paragraph break mid-sentence)", "extra", None, "high",
           r"tel que $\mathcal F|U$<NL><NL>", r"tel que $\mathcal F|U$<NL>",
           "removes the paragraph break the print does not have"))
# ---------------- page 42 ----------------
L.append(F(42, "first lines: 'il suffit en effet de prendre U tel que F|U soit un O_X-Module réduit (3.2.2)'",
           "O_X-Module réduit", r"$\mathcal O_U$-Module réduit", "misprint_in_print", None, "high",
           r"\mathcal O_U$-Module réduit", r"\mathcal O_X$-Module réduit",
           "misprint in the print (F|U is an O_U-Module, as in the same sentence and on p. 40); "
           "the TeX silently corrects it: restore the printed O_X",
           corrected=r"\mathcal O_U"))
L.append(F(42, "first paragraph: 'Y de X est primaire dans X si l'Idéal'",
           "only 'primaire' italic; 'dans X' roman",
           r"\emph{primaire dans $X$}", "italics", None, "high",
           r"\emph{primaire dans<NL>$X$}", r"\emph{primaire} dans<NL>$X$", ""))
L.append(F(42, "first paragraph: '((I, 2.1.8) et (3.2.1))'", "(I, 2.1.8) with bold I",
           "(I, 2.1.8)", "convention", 2, "high", "((I, 2.1.8)", r"((\textbf{I}, 2.1.8)", ""))
L.append(F(42, "Définition (3.2.5): 'On appelle décomposition irredondante de F'",
           "the phrase italic like the rest of the definition",
           r"\emph{décomposition irredondante de $\mathcal F$} inside the italic definition (comes out upright)",
           "convention", 6, "high",
           r"\emph{décomposition irredondante de<NL>$\mathcal F$}",
           r"décomposition irredondante de<NL>$\mathcal F$", ""))
L.append(F(42, "Définition (3.2.5): 'telle décomposition est réduite si les ensembles'",
           "'réduite' italic like the rest of the definition",
           r"\emph{réduite} inside the italic definition (comes out upright)", "convention", 6, "high",
           r"\emph{réduite} si les", "réduite si les", ""))
L.append(F(42, "paragraph before (3.2.6): 'alpha ~> x_alpha est une bijection'",
           "wavy arrow alpha ~> x_alpha", r"\alpha\mapsto x_\alpha", "symbol", None, "high",
           r"$\alpha\mapsto x_\alpha$", r"$\alpha\leadsto x_\alpha$", "wavy arrow in the print"))
L.append(F(42, "Proposition (3.2.6): 'le morphisme canonique Spec(k(x)) -> X'", "bold italic k in k(x)",
           r"\operatorname{Spec}(k(x))", "convention", 1, "high",
           r"\operatorname{Spec}(k(x))", r"\operatorname{Spec}(\boldsymbol{k}(x))", ""))
L.append(F(42, "proof of (3.2.6): 'Ass(N) = Ass(M)—{x}'", "long dash Ass(M)—{x}",
           r"\operatorname{Ass}(M)-\{x\}", "convention", 7, "high",
           r"\operatorname{Ass}(M)-\{x\}", r"\operatorname{Ass}(M)\setmin\{x\}",
           "\\setmin is not defined in EGA_IV2_FR.tex (global convention-7 pass)"))
L.append(F(42, "proof of (3.2.6): 'qui est un O_X-Module cohérent (I, 6.1.1)'", "(I, 6.1.1) with bold I",
           "(I, 6.1.1)", "convention", 2, "high", "(I, 6.1.1)", r"(\textbf{I}, 6.1.1)", ""))
L.append(F(42, "end of page: 'En outre, si' / p. 43 'N^(x) = Ker(v)'",
           "one sentence running over the page break",
           r"blank line before \oldpage[IV-2]{43} (paragraph break mid-sentence)", "extra", None, "high",
           "En outre, si<NL><NL>", "En outre, si<NL>",
           "removes the paragraph break the print does not have"))
# ---------------- page 43 ----------------
L.append(F(43, "end of the proof of (3.2.6): 'compte tenu de (I, 1.6.7)'", "(I, 1.6.7) with bold I",
           "(I, 1.6.7)", "convention", 2, "high", "(I, 1.6.7)", r"(\textbf{I}, 1.6.7)", ""))
L.append(F(43, "Corollaire (3.2.7): 'Sous les hypothèses de (3.2.6)'",
           "(3.2.6) upright inside the italic statement", "(3.2.6) italic (plain text in the italic environment)",
           "convention", 6, "high", "hypothèses de (3.2.6)", r"hypothèses de \textup{(3.2.6)}", ""))
L.append(F(43, "heading of 3.3", "3.3. Relations avec la platitude. (final full stop)",
           r"\subsection{Relations avec la platitude} (no full stop)", "punctuation", None, "high",
           r"\subsection{Relations avec la platitude}", r"\subsection{Relations avec la platitude.}",
           "subsection title lacks the printed full stop"))
L.append(F(43, "Proposition (3.3.1): 'on pose F_y = F (x)_{O_Y} k(y)'", "bold italic k in k(y)",
           r"\otimes_{\mathcal O_Y}k(y)", "convention", 1, "high",
           r"\otimes_{\mathcal O_Y}k(y)", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)", ""))
L.append(F(43, "formula (3.3.1.1), left side", "Ass(E (x)_{O_Y} F): tensor product subscript O_Y",
           r"\operatorname{Ass}(\mathcal E\otimes_Y\mathcal F)", "formula", None, "high",
           r"\operatorname{Ass}(\mathcal E\otimes_Y\mathcal F)<NL>\supset",
           r"\operatorname{Ass}(\mathcal E\otimes_{\mathcal O_Y}\mathcal F)<NL>\supset", ""))
L.append(F(43, "formula (3.3.1.1), end", "no comma after Ass(F_y)",
           r"\operatorname{Ass}(\mathcal F_y), (comma)", "punctuation", None, "high",
           r"\operatorname{Ass}(\mathcal F_y),<NL>\]", r"\operatorname{Ass}(\mathcal F_y)<NL>\]", ""))
L.append(F(43, "after (3.3.1.1): 'et les deux membres sont égaux si Y est localement noethérien.'",
           "italic: the end of the statement of (3.3.1)",
           "roman (set after \\end{env}, outside the proposition environment)", "italics", None, "high",
           r"et les deux membres sont égaux si $Y$ est localement noethérien.",
           r"\emph{et les deux membres sont égaux si $Y$ est localement noethérien.}",
           "the print continues the italic statement after the display (flush left)"))
L.append(F(43, "paragraph after (3.3.1): 'un sous-espace de X (I, 3.6.1).)'", "(I, 3.6.1) with bold I",
           "(I, 3.6.1)", "convention", 2, "high", "(I, 3.6.1)", r"(\textbf{I}, 3.6.1)", ""))
L.append(F(43, "Corollaire (3.3.3): 'Sous les hypothèses de (3.3.1)'",
           "(3.3.1) upright inside the italic statement", "(3.3.1) italic (plain text in the italic environment)",
           "convention", 6, "high", "hypothèses de (3.3.1)", r"hypothèses de \textup{(3.3.1)}", ""))
# ---------------- page 44 ----------------
L.append(F(44, "first paragraph: 'cohérent (0_I, 5.3.11 et 5.3.5)'", "bold 0 in (0_I, 5.3.11 et 5.3.5)",
           r"$(0_{\mathrm I},5.3.11\text{ et }5.3.5)$", "convention", 2, "high",
           r"$(0_{\mathrm I},5.3.11", r"$(\mathbf{0}_{\mathrm I},5.3.11", ""))
L.append(F(44, "first paragraph: 'entraîne F_y != 0 (I, 9.1.13)'", "(I, 9.1.13) with bold I",
           "(I, 9.1.13)", "convention", 2, "high", "(I, 9.1.13)", r"(\textbf{I}, 9.1.13)", ""))
L.append(F(44, "second paragraph: 'aucun d'eux ne peut être adhérent à l'autre dans X. Si y = f(z)'",
           "'dans' italic (as in 'dans f^-1(y)' just before)", "dans (roman)", "italics", None, "high",
           r"l'autre dans $X$. Si", r"l'autre \emph{dans} $X$. Si", ""))
L.append(F(44, "Proposition (3.3.4): 'E un O_X-Module cohérent, F un O_X-Module cohérent'",
           "E un O_X-Module cohérent", r"$\mathcal E$ un $\mathcal O_Y$-Module cohérent",
           "misprint_in_print", None, "high",
           r"\mathcal E$ un $\mathcal O_Y$-Module", r"\mathcal E$ un $\mathcal O_X$-Module",
           "misprint in the print (E is an O_Y-Module: E (x)_Y F, Ass(E) in Y, as in (3.3.1)); "
           "the TeX silently corrects it: restore the printed O_X",
           corrected=r"\mathcal O_Y"))
L.append(F(44, "Proposition (3.3.4) a): 'E (x)_Y F est réduit (3.2.2).'",
           "(3.2.2) upright inside the italic statement", "(3.2.2) italic (plain text in the italic environment)",
           "convention", 6, "high", "est réduit (3.2.2).", r"est réduit \textup{(3.2.2)}.", ""))
L.append(F(44, "proof of (3.3.4): 'on a 1 = long((E (x)_Y F)_x) = long(E_y).long((F_y)_x), donc'",
           "formula in the running text, with a baseline dot between long(E_y) and long((F_y)_x)",
           r"displayed with \[ ... \], centred dot \cdot", "formula", None, "high",
           r"on a<NL>\[<NL>1=\operatorname{long}((\mathcal E\otimes_Y\mathcal F)_x)<NL>"
           r"=\operatorname{long}(\mathcal E_y)\cdot\operatorname{long}((\mathcal F_y)_x),<NL>\]<NL>donc",
           r"on a<NL>$1=\operatorname{long}((\mathcal E\otimes_Y\mathcal F)_x)<NL>"
           r"=\operatorname{long}(\mathcal E_y).\operatorname{long}((\mathcal F_y)_x)$,<NL>donc",
           "one edit: display -> inline, and \\cdot -> baseline dot"))
L.append(F(44, "Corollaire (3.3.5): 'f^-1(y) est un k(y)-préschéma réduit'", "bold italic k in k(y)",
           r"$k(y)$-préschéma", "convention", 1, "high",
           r"un $k(y)$-préschéma", r"un $\boldsymbol{k}(y)$-préschéma", ""))
L.append(F(44, "proof of (3.3.5): 'est ouvert (0_I, 5.2.2)'", "bold 0 in (0_I, 5.2.2)",
           r"$(0_{\mathrm I},5.2.2)$", "convention", 2, "high",
           r"$(0_{\mathrm I},5.2.2)$", r"$(\mathbf{0}_{\mathrm I},5.2.2)$", ""))
L.append(F(44, "proof of (3.3.5): 'd'appliquer (3.3.4) à E = O_Y et F = O_Y.'",
           "F = O_Y", r"$\mathcal F=\mathcal O_X$", "misprint_in_print", None, "high",
           r"\mathcal F=\mathcal O_X$.", r"\mathcal F=\mathcal O_Y$.",
           "misprint in the print (F must be the O_X-Module O_X); the TeX silently corrects it: "
           "restore the printed O_Y",
           corrected=r"\mathcal O_X"))
L.append(F(44, "end of page: 'tel que x in X, y in Y et' / p. 45 'f(x) = g(y) = s'",
           "one sentence running over the page break",
           r"blank line before \oldpage[IV-2]{45} (paragraph break mid-sentence)", "extra", None, "high",
           r"$y\in Y$ et<NL><NL>", r"$y\in Y$ et<NL>",
           "removes the paragraph break the print does not have"))

# ---- verification: each old occurs exactly once in its LF-normalised page file ----
bad = 0
for x in L:
    if x["fix"] is None:
        continue
    p = os.path.join(RUN, "page_%03d.tex" % x["page"])
    t = open(p, encoding="utf-8").read().replace("\r\n", "\n")
    c = t.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], c, repr(x["fix"]["old"]))
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
print("written", len(L), "findings; non-unique:", bad)
from collections import Counter
c = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for pg in range(40, 45):
    print(pg, c[(pg, "normal")], c[(pg, "convention")], c[(pg, "misprint")])
