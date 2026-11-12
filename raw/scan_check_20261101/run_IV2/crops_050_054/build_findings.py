"""Build findings_050_054.json and check every fix: 'old' occurs exactly once in its page_NNN.tex (CRLF -> LF),
fix ranges on a page do not overlap, and all fixes of a page apply in sequence."""
import json
import pathlib
import sys

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_050_054.json"


def F(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


S7 = "Long dash (bar about 40-41 px at 300 dpi; the = bars on the same line 34-35 px); \\setmin pending the convention-7 decision (GLOBAL_ISSUES 23)."
DT = "GLOBAL_ISSUES candidate: \\operatorname{deg.tr.} (47 in ega4-2-fr.tex) prints a point after 'tr' that the print does not have."
L = []

# ---------------- page 50 ----------------
L += [
    F(50, "top of page, 'un O_X-Module cohérent' (statement of (3.4.5) continued)",
      "the statement runs on over the page break ('Soient F' | 'un O_X-Module cohérent'); p. 50 begins flush left, no new paragraph",
      "blank line after \\oldpage[IV-2]{50} (and before it at the end of p. 49): paragraph break inside the statement",
      "other", "\\oldpage[IV-2]{50}\n\nun $\\mathcal O_X$", "\\oldpage[IV-2]{50}\nun $\\mathcal O_X$",
      note="Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). The blank line before the marker ('Soient $\\mathcal F$\\n\\n\\oldpage[IV-2]{50}') lies in the p. 49 segment: remove it together with this fix."),
    F(50, "Proposition (3.4.5), end of the statement", "(3.2.4) upright", "(3.2.4) as text in the italic proposition (typeset italic)",
      "convention", "(3.2.4). Alors", "\\textup{(3.2.4)}. Alors", conv=6),
    F(50, "proof of (3.4.5), l. 1", "'dans une seule composante': 'une seule' both italic (enlarged crop)", "une \\emph{seule}",
      "italics", "une\n\\emph{seule}", "\\emph{une\nseule}"),
    F(50, "Proposition (3.4.6), l. 1", "(3.4.1) upright", "(3.4.1) as text in the italic proposition (typeset italic)",
      "convention", "(3.4.1), soit", "\\textup{(3.4.1)}, soit", conv=6),
    F(50, "Proposition (3.4.6), l. 2", "(3.2.2) upright", "(3.2.2) as text in the italic proposition (typeset italic)",
      "convention", "point $x$ (3.2.2)", "point $x$ \\textup{(3.2.2)}", conv=6),
    F(50, "Proposition (3.4.6), last sentence", "O_{S, z_j}: the subscript is S without index, then z_j (enlarged crop)",
      "\\mathcal O_{S_i,z_j}", "formula", "$\\mathcal O_{S_i,z_j}$", "$\\mathcal O_{S,z_j}$",
      note="Not a misprint: S is the reduced closed subprescheme with underlying space Supp(F) of (3.4.1), and z_j lies in only one S_i, so O_{S,z_j} = O_{S_i,z_j}."),
    F(50, "Lemme (3.4.6.1), 'n'appartient à aucun des p_i et que M/tM'", "no comma after p_i (line end, enlarged crop)",
      "aucun des $\\mathfrak p_i$, et que", "punctuation", "$\\mathfrak p_i$,\net que", "$\\mathfrak p_i$\net que"),
    F(50, "Lemme (3.4.6.1)", "(3.2.2) upright", "(3.2.2) as text in the italic lemma (typeset italic)",
      "convention", "réduit (3.2.2)", "réduit \\textup{(3.2.2)}", conv=6),
    F(50, "proof of (3.4.6.1), after the display 0->N/tN->M/tM->P/tP->0",
      "'Comme N est de type fini' begins an indented new paragraph", "no blank line after \\]: same paragraph",
      "other", "\\]\nComme $N$ est de type fini", "\\]\n\nComme $N$ est de type fini",
      note="Missing paragraph break after a display (as GLOBAL_ISSUES 47)."),
    F(50, "proof of (3.4.6.1), 'ou encore que l'homomorphisme u_p : (M/tM)_p -> (P/tP)_p est bijectif'",
      "formula in the running text (the line begins 'u_p : (M/tM)_p -> (P/tP)_p est bijectif pour tout')",
      "displayed with \\[ \\]", "formula",
      "l'homomorphisme\n\\[\nu_{\\mathfrak p}:(M/tM)_{\\mathfrak p}\\longrightarrow(P/tP)_{\\mathfrak p}\n\\]\nest bijectif",
      "l'homomorphisme\n$u_{\\mathfrak p}:(M/tM)_{\\mathfrak p}\\longrightarrow(P/tP)_{\\mathfrak p}$\nest bijectif",
      note="Display where the print sets the formula inline (GLOBAL_ISSUES 21)."),
    F(50, "proof of (3.4.6.1), 'Supp(M) n V(t) (0_I, 1.7.5)'", "bold 0 in (0_I, 1.7.5)", "$(0_{\\mathrm I},1.7.5)$, plain 0",
      "convention", "$(0_{\\mathrm I},1.7.5)$", "$(\\mathbf{0}_{\\mathrm I},1.7.5)$", conv=2),
    F(50, "end of page, 'formant une partie d'un système de' | p. 51 'paramètres pour M'",
      "the statement of (3.4.7) runs on over the page break; p. 51 begins 'paramètres pour M' flush left",
      "blank line before \\oldpage[IV-2]{51} (and after it): paragraph break inside the statement",
      "other", "partie d'un système de\n\n", "partie d'un système de\n",
      note="Apply together with the p. 51 entry that removes the blank line after \\oldpage[IV-2]{51} (GLOBAL_ISSUES 20)."),
]

# ---------------- page 51 ----------------
L += [
    F(51, "top of page, 'paramètres pour M'", "continuation of the statement of (3.4.7), flush left, no new paragraph",
      "blank line after \\oldpage[IV-2]{51}", "other", "\\oldpage[IV-2]{51}\n\nparamètres", "\\oldpage[IV-2]{51}\nparamètres",
      note="Apply together with the p. 50 entry 'partie d'un système de' (blank line before the marker)."),
    F(51, "Corollaire (3.4.7), l. 1", "(0, 16.3.6) with a bold 0", "$(0,16.3.6)$, plain 0",
      "convention", "$(0,16.3.6)$", "$(\\mathbf{0},16.3.6)$", conv=2),
    F(51, "Corollaire (3.4.7), 'Si le A-module N = M/(sum x_iM) est intègre'",
      "formula in the running text, ordinary-size slash and parentheses", "displayed with \\[ \\], \\Big/ \\Big( \\Big)",
      "formula", "Si le $A$-module\n\\[\nN=M\\Big/\\Big(\\sum_{i=1}^k x_iM\\Big)\n\\]\nest intègre",
      "Si le $A$-module\n$N=M/(\\sum_{i=1}^k x_iM)$\nest intègre",
      note="Display where the print sets the formula inline (GLOBAL_ISSUES 21); the print sets the sum's limits above and below even in the line."),
    F(51, "Corollaire (3.4.7), 'est intègre (3.2.4)'", "(3.2.4) upright", "(3.2.4) as text in the italic corollary (typeset italic)",
      "convention", "(3.2.4), alors", "\\textup{(3.2.4)}, alors", conv=6),
    F(51, "proof of (3.4.7), 'dim(N) = dim(M) - 1'", "long dash for the subtraction (measured)", "minus sign",
      "convention", "\\dim(M)-1$", "\\dim(M)\\setmin 1$", conv=7, note=S7),
    F(51, "proof of (3.4.7), (0, 16.3.7)", "bold 0", "$(0,16.3.7)$, plain 0",
      "convention", "$(0,16.3.7)$", "$(\\mathbf{0},16.3.7)$", conv=2),
    F(51, "proof of (3.4.7), 'dim(M/pM) = n+1 (0, 16.3.4)'", "bold 0", "$(0,16.3.4)$, plain 0",
      "convention", "$(0,16.3.4)$, et pour", "$(\\mathbf{0},16.3.4)$, et pour", conv=2),
    F(51, "proof of (3.4.7), 'dim(M/p^jM) = n+1 (0, 16.3.5)'", "bold 0", "$(0,16.3.5)$, plain 0",
      "convention", "$(0,16.3.5)$~; en outre", "$(\\mathbf{0},16.3.5)$~; en outre", conv=2),
    F(51, "proof of (3.4.7), 'pour M/p^jM (0, 16.3.5), donc'", "bold 0", "$(0,16.3.5)$, plain 0",
      "convention", "$(0,16.3.5)$, donc", "$(\\mathbf{0},16.3.5)$, donc", conv=2),
    F(51, "proof of (3.4.7), 'montrons que v est bijectif'", "'bijectif' italic (enlarged crop)", "bijectif upright",
      "italics", "est\nbijectif.", "est\n\\emph{bijectif}."),
    F(51, "proof of (3.4.7), 'le support de N' (égal à l'intersection de Supp(M) et de V(x))'",
      "Supp(M) without prime (enlarged crop; the Supp(M') later in the line has its prime)", "\\operatorname{Supp}(M')",
      "formula", "l'intersection de $\\operatorname{Supp}(M')$", "l'intersection de $\\operatorname{Supp}(M)$",
      note="The printed reading is correct as it stands (N' is isomorphic to N, so Supp(N') = Supp(M) n V(x)); M' may have been meant, but this is no misprint."),
    F(51, "proof of (3.4.7), 'l'homothétie z -> xz'", "plain arrow", "\\mapsto",
      "convention", "$z\\mapsto xz$", "$z\\to xz$", conv=3),
    F(51, "proof of (3.4.7), (0_I, 7.3.5)", "bold 0", "$(0_{\\mathrm I},7.3.5)$, plain 0",
      "convention", "$(0_{\\mathrm I},7.3.5)$", "$(\\mathbf{0}_{\\mathrm I},7.3.5)$", conv=2),
    F(51, "Remarque (3.4.8), last sentence, (0, 16.3.4)", "bold 0", "$(0,16.3.4)$, plain 0",
      "convention", "$(0,16.3.4)$, $A/xA$", "$(\\mathbf{0},16.3.4)$, $A/xA$", conv=2),
    F(51, "Proposition (3.4.9), 'Si p_i (1 <= i <= m) sont'",
      "wrong fount: 'i <= m' (italic i, the second <= sign and italic m) printed bold; '1 <=' and the later (1 <= i <= m) normal weight (enlarged crops)",
      "$(1\\leqslant i\\leqslant m)$ in normal weight (silently corrected)", "misprint_in_print",
      "$(1\\leqslant i\\leqslant m)$ sont", "$(1\\leqslant\\boldsymbol{i\\leqslant m})$ sont",
      corrected="$(1\\leqslant i\\leqslant m)$ sont",
      note="Wrong-fount letters are reproduced in the diplomatic text (GLOBAL_ISSUES 29); the TeX silently corrects."),
    F(51, "proof of (3.4.9), 'car alors les saturés des f^nM pour les p_i'",
      "'des f^nM' (enlarged crop)", "'de $f^nM$' (silently corrected)", "misprint_in_print",
      "les saturés de $f^nM$", "les saturés des $f^nM$", corrected="les saturés de $f^nM$",
      note="'des' does not fit the single module f^nM (the sentence goes on '... de f^nM dans M'); correct reading 'de'."),
]

# ---------------- page 52 ----------------
L += [
    F(52, "heading 4.1", "'4.1. Dimension des préschémas algébriques.' (final full stop)",
      "\\subsection{Dimension des préschémas algébriques} (no full stop)", "punctuation",
      "\\subsection{Dimension des préschémas algébriques}", "\\subsection{Dimension des préschémas algébriques.}",
      note="GLOBAL_ISSUES 43/58 (subsection titles without the printed full stop)."),
    F(52, "4.1, l. 5, 'on notera deg.tr_K L'", "'deg.tr' with no point after tr (enlarged crop)", "\\operatorname{deg.tr.} prints 'deg.tr.'",
      "punctuation", "$\\operatorname{deg.tr.}_K L$", "$\\operatorname{deg.tr}_K L$", note=DT),
    F(52, "Définition (4.1.1), 'On appelle dimension de X'", "'dimension' in the italic of the statement, no change of face (enlarged crop)",
      "\\emph{dimension} inside the italic definition (typeset upright)", "italics",
      "appelle \\emph{dimension} de", "appelle dimension de"),
    F(52, "(4.1.1.1)", "'deg.tr_k k(x)': no point after tr", "\\operatorname{deg.tr.}", "punctuation",
      "\\sup_x\\operatorname{deg.tr.}", "\\sup_x\\operatorname{deg.tr}", note=DT),
    F(52, "(4.1.1.1)", "bold italic k in k(x)", "plain k(x)", "convention", "_k k(x)\n\\end{equation}",
      "_k \\boldsymbol{k}(x)\n\\end{equation}", conv=1),
    F(52, "after (4.1.1), '(définie dans (0, 14.1.2))'", "bold 0", "$(0,14.1.2)$, plain 0",
      "convention", "$(0,14.1.2)$", "$(\\mathbf{0},14.1.2)$", conv=2),
    F(52, "'On notera que chaque k(x)'", "bold italic k", "plain k(x)", "convention",
      "chaque $k(x)$", "chaque $\\boldsymbol{k}(x)$", conv=1),
    F(52, "'de type fini de k (I, 6.3.3)'", "bold I", "plain I", "convention", "(I, 6.3.3)", "(\\textbf{I}, 6.3.3)", conv=2),
    F(52, "'il est noethérien (I, 6.3.7)'", "bold I", "plain I", "convention", "(I, 6.3.7)", "(\\textbf{I}, 6.3.7)", conv=2),
    F(52, "display dim(empty set) = -infinity", "long dash before the infinity sign (bar 41 px, = bars 35 px)", "minus sign",
      "convention", "=-\\infty.", "=\\setmin\\infty.", conv=7,
      note="Unary minus with the long dash (GLOBAL_ISSUES 23/49); \\setmin pending the convention-7 decision."),
    F(52, "'composantes irréductibles de X (I, 5.2.1)'", "bold I", "plain I", "convention", "(I, 5.2.1)", "(\\textbf{I}, 5.2.1)", conv=2),
    F(52, "after (4.1.1.2)", "'Cela ramène donc le calcul' begins an indented new paragraph", "no blank line after \\end{equation}",
      "other", "\\end{equation}\nCela ramène", "\\end{equation}\n\nCela ramène",
      note="Missing paragraph break after a display (as GLOBAL_ISSUES 47); after (4.1.1.1) and (4.1.1.3) the print continues flush left, as the TeX does."),
]

# ---------------- page 53 ----------------
L += [
    F(53, "Théorème (4.1.2), label (i)", "label (i) upright", "\\item[(i)] inside the italic theorem (typeset italic)",
      "convention", "\\item[(i)]", "\\item[\\textup{(i)}]", conv=6, note="GLOBAL_ISSUES 16."),
    F(53, "Théorème (4.1.2), label (ii)", "label (ii) upright", "\\item[(ii)] (typeset italic)",
      "convention", "\\item[(ii)]", "\\item[\\textup{(ii)}]", conv=6, note="GLOBAL_ISSUES 16."),
    F(53, "Théorème (4.1.2), label (iii)", "label (iii) upright", "\\item[(iii)] (typeset italic)",
      "convention", "\\item[(iii)]", "\\item[\\textup{(iii)}]", conv=6, note="GLOBAL_ISSUES 16."),
    F(53, "Théorème (4.1.2) (iii), '(resp. dim(X) <= n, dim(X) = n)'", "the parenthesis and 'resp.' upright (enlarged crop)",
      "italic inside the theorem", "convention", "(resp. $\\dim(X)\\leqslant n$, $\\dim(X)=n$)",
      "\\textup{(resp. $\\dim(X)\\leqslant n$, $\\dim(X)=n$)}", conv=6),
    F(53, "Théorème (4.1.2) (iii), 'g : U -> V(k^n) (= Spec(k[T_1, ..., T_n]), que nous noterons aussi V_k^n) qui soit surjectif'",
      "in the running text; '(=' opens a parenthesis that closes after V_k^n, no comma before 'qui'",
      "displayed 'g:U->V(k^n) = Spec(...)', without the parenthesis, and 'V_k^n, qui soit'",
      "formula",
      "et un $k$-morphisme\n\\[\ng:U\\longrightarrow\\mathbf V(k^n)\n=\\operatorname{Spec}(k[T_1,\\ldots,T_n]),\n\\]\nque nous noterons aussi $\\mathbf V_k^n$, qui soit surjectif",
      "et un $k$-morphisme\n$g:U\\longrightarrow\\mathbf V(k^n)$\n$(=\\operatorname{Spec}(k[T_1,\\ldots,T_n])$,\nque nous noterons aussi $\\mathbf V_k^n)$ qui soit surjectif",
      note="Display where the print sets the formula inline (GLOBAL_ISSUES 21); the display also lost the parenthesis '(= ... V_k^n)' and added a comma."),
    F(53, "Théorème (4.1.2) (iii), 'surjectif (resp. fini, resp. fini et surjectif)'",
      "'(resp.', 'resp.' and the closing parenthesis upright; 'fini', 'fini et surjectif' italic (enlarged crop)",
      "all italic", "convention", "(resp. fini,\nresp. fini et surjectif).",
      "\\textup{(resp.} fini,\n\\textup{resp.} fini et surjectif\\textup{)}.", conv=6),
    F(53, "proof (i), 'donc k(x) est une extension'", "bold italic k", "plain k", "convention",
      "donc $k(x)$", "donc $\\boldsymbol{k}(x)$", conv=1),
    F(53, "proof (i), 'extension de k(y)'", "bold italic k", "plain k", "convention",
      "extension de $k(y)$", "extension de $\\boldsymbol{k}(y)$", conv=1),
    F(53, "proof (i), 'd'où l'inégalité deg.tr_k k(y) <= deg.tr_k k(x) <= dim(X), ce qui démontre (i)'",
      "in the running text; 'deg.tr' without a point after tr; bold italic k(y), k(x)",
      "displayed with \\[ \\]; \\operatorname{deg.tr.}; plain k", "formula",
      "d'où l'inégalité\n\\[\n\\operatorname{deg.tr.}_k k(y)\n\\leqslant\\operatorname{deg.tr.}_k k(x)\n\\leqslant\\dim(X),\n\\]\nce qui",
      "d'où l'inégalité\n$\\operatorname{deg.tr}_k \\boldsymbol{k}(y)\n\\leqslant\\operatorname{deg.tr}_k \\boldsymbol{k}(x)\n\\leqslant\\dim(X)$,\nce qui",
      note="One edit for three differences: inline formula (GLOBAL_ISSUES 21), the two points after tr (" + DT + "), and the two bold k (convention 1, the next two entries, fix null)."),
    F(53, "proof (i), inequality, k(y)", "bold italic k", "plain k", "convention", None, None, conv=1,
      note="Set by the fix of the preceding entry (display made inline)."),
    F(53, "proof (i), inequality, k(x)", "bold italic k", "plain k", "convention", None, None, conv=1,
      note="Set by the fix of the entry before the preceding one (display made inline)."),
    F(53, "proof (ii), 'k(x) est une extension finie'", "bold italic k", "plain k", "convention",
      "$k(x)$ est une extension finie", "$\\boldsymbol{k}(x)$ est une extension finie", conv=1),
    F(53, "proof (ii), 'k(f(x))'", "bold italic k", "plain k", "convention",
      "$k(f(x))$", "$\\boldsymbol{k}(f(x))$", conv=1),
    F(53, "proof (ii), (II, 6.2.2)", "bold II", "plain II", "convention", "(II, 6.2.2)", "(\\textbf{II}, 6.2.2)", conv=2),
    F(53, "proof (ii), last sentence", "'... on voit qu'on est ramené à démontrer le' and the heading 'Corollaire (4.1.2.1). —' follows; no 'corollaire suivant.'",
      "'à démontrer le corollaire suivant.'", "extra", "démontrer le corollaire\nsuivant.", "démontrer le",
      note="The printed sentence ends with 'le' and runs into the corollary heading."),
    F(53, "proof of (4.1.2.1), '(Bourbaki, ..., th. 1) il existe'", "no comma after the parenthesis (enlarged crop)",
      "th.~1), il existe", "punctuation", "th.~1), il existe", "th.~1) il existe"),
    F(53, "proof of (4.1.2.1), 'deg.tr_k k(y) = n'", "no point after tr", "\\operatorname{deg.tr.}", "punctuation",
      "donc\n$\\operatorname{deg.tr.}", "donc\n$\\operatorname{deg.tr}", note=DT),
    F(53, "proof of (4.1.2.1), 'deg.tr_k k(y) = n'", "bold italic k", "plain k", "convention",
      "_k k(y)=n", "_k \\boldsymbol{k}(y)=n", conv=1),
    F(53, "proof of (4.1.2.1), 'deg.tr_k k(z) = n - p'", "no point after tr", "\\operatorname{deg.tr.}", "punctuation",
      "et\n$\\operatorname{deg.tr.}", "et\n$\\operatorname{deg.tr}", note=DT),
    F(53, "proof of (4.1.2.1), 'deg.tr_k k(z) = n - p'", "bold italic k", "plain k", "convention",
      "_k k(z)", "_k \\boldsymbol{k}(z)", conv=1),
    F(53, "proof of (4.1.2.1), 'n - p'", "long dash for the subtraction (bar 41 px; = bars 34-35 px)", "minus sign",
      "convention", "=n-p$,", "=n\\setmin p$,", conv=7, note=S7),
    F(53, "proof of (4.1.2.1), 'puisque k(y)'", "bold italic k", "plain k", "convention",
      "puisque $k(y)$", "puisque $\\boldsymbol{k}(y)$", conv=1),
    F(53, "proof of (4.1.2.1), '(resp. k(z))'", "bold italic k", "plain k", "convention",
      "(resp. $k(z)$)", "(resp. $\\boldsymbol{k}(z)$)", conv=1),
    F(53, "proof of (4.1.2.1), 'k(g(y))'", "bold italic k", "plain k", "convention",
      "$k(g(y))$", "$\\boldsymbol{k}(g(y))$", conv=1),
    F(53, "proof of (4.1.2.1), 'k(g(z))'", "bold italic k", "plain k", "convention",
      "$k(g(z))$", "$\\boldsymbol{k}(g(z))$", conv=1),
    F(53, "proof of (4.1.2.1), 'est donc rare dans'", "'rare' italic (enlarged crop)", "rare upright",
      "italics", "est donc rare dans", "est donc \\emph{rare} dans"),
    F(53, "proof (iii), (0_I, 2.1.6)", "bold 0", "$(0_{\\mathrm I},2.1.6)$, plain 0", "convention",
      "$(0_{\\mathrm I},2.1.6)$", "$(\\mathbf{0}_{\\mathrm I},2.1.6)$", conv=2),
    F(53, "end of page, 'Le même' | p. 54 'raisonnement que dans'",
      "the sentence runs on over the page break; p. 54 begins 'raisonnement' flush left",
      "blank line before \\oldpage[IV-2]{54} (and after it)", "other", "Le même\n\n", "Le même\n",
      note="Apply together with the p. 54 entry that removes the blank line after \\oldpage[IV-2]{54} (GLOBAL_ISSUES 20)."),
]

# ---------------- page 54 ----------------
L += [
    F(54, "top of page, 'raisonnement que dans (4.1.2.1)'", "continuation of the sentence 'Le même', flush left",
      "blank line after \\oldpage[IV-2]{54}", "other", "\\oldpage[IV-2]{54}\n\nraisonnement", "\\oldpage[IV-2]{54}\nraisonnement",
      note="Apply together with the p. 53 entry 'Le même' (blank line before the marker)."),
    F(54, "l. 2, (II, 6.1.10)", "bold II", "plain II", "convention", "(II, 6.1.10)", "(\\textbf{II}, 6.1.10)", conv=2),
    F(54, "'Lorsque n' >= n on aura'", "no comma after n' >= n (line end, enlarged crop)", "Lorsque $n'\\geqslant n$, on aura",
      "punctuation", "Lorsque $n'\\geqslant n$, on aura", "Lorsque $n'\\geqslant n$ on aura"),
    F(54, "proof of (4.1.4), '(I, 3.5.2 et II, 6.1.5)'", "bold I", "plain I", "convention",
      "V_K^n$ (I,", "V_K^n$ (\\textbf{I},", conv=2),
    F(54, "proof of (4.1.4), '(I, 3.5.2 et II, 6.1.5)'", "bold II", "plain II", "convention",
      "et II, 6.1.5), d'où le\ncorollaire", "et \\textbf{II}, 6.1.5), d'où le\ncorollaire", conv=2),
    F(54, "proof of (4.1.5), 'deg.tr_k k(x) = m = dim U'", "no point after tr", "\\operatorname{deg.tr.}", "punctuation",
      "tel que\n$\\operatorname{deg.tr.}", "tel que\n$\\operatorname{deg.tr}", note=DT),
    F(54, "proof of (4.1.5), 'deg.tr_k k(x)'", "bold italic k", "plain k", "convention",
      "_k k(x)=m", "_k \\boldsymbol{k}(x)=m", conv=1),
    F(54, "proof of (4.1.5), 'deg.tr_k k(y) = n = dim V'", "no point after tr", "\\operatorname{deg.tr.}", "punctuation",
      "et\n$\\operatorname{deg.tr.}", "et\n$\\operatorname{deg.tr}", note=DT),
    F(54, "proof of (4.1.5), 'deg.tr_k k(y)'", "bold italic k", "plain k", "convention",
      "_k k(y)=n", "_k \\boldsymbol{k}(y)=n", conv=1),
    F(54, "proof of (4.1.5), '(I, 3.5.2 et II, 6.1.5)'", "bold I", "plain I", "convention",
      "surjectif\n(I, 3.5.2", "surjectif\n(\\textbf{I}, 3.5.2", conv=2),
    F(54, "proof of (4.1.5), '(I, 3.5.2 et II, 6.1.5)'", "bold II", "plain II", "convention",
      "et II, 6.1.5), d'où le corollaire", "et \\textbf{II}, 6.1.5), d'où le corollaire", conv=2),
    F(54, "heading 4.2", "'4.2. Cycles premiers associés sur les préschémas algébriques.' (final full stop)",
      "\\subsection{Cycles premiers associés sur les préschémas algébriques} (no full stop)", "punctuation",
      "\\subsection{Cycles premiers associés sur les préschémas algébriques}",
      "\\subsection{Cycles premiers associés sur les préschémas algébriques.}",
      note="GLOBAL_ISSUES 43/58."),
    F(54, "(4.2.1.1)", "'deg.tr' four times without a point after tr", "\\operatorname{deg.tr.} four times", "punctuation",
      "\\operatorname{deg.tr.}_K E=\\operatorname{deg.tr.}_k L,\n\\qquad\n\\operatorname{deg.tr.}_L E=\\operatorname{deg.tr.}_k K",
      "\\operatorname{deg.tr}_K E=\\operatorname{deg.tr}_k L,\n\\qquad\n\\operatorname{deg.tr}_L E=\\operatorname{deg.tr}_k K",
      note=DT),
    F(54, "(4.2.1.1), end", "no comma after the second equation 'deg.tr_L E = deg.tr_k K' (enlarged crop)", "'..._k K,'",
      "punctuation", ",\n\\end{equation}\nd'où", "\n\\end{equation}\nd'où"),
    F(54, "(4.2.1.2)", "'deg.tr' three times without a point after tr", "\\operatorname{deg.tr.} three times", "punctuation",
      "\\operatorname{deg.tr.}_k E\n=\\operatorname{deg.tr.}_k K+\\operatorname{deg.tr.}_k L.",
      "\\operatorname{deg.tr}_k E\n=\\operatorname{deg.tr}_k K+\\operatorname{deg.tr}_k L.", note=DT),
    F(54, "end of page, proof of (4.2.1): 'qui en est un anneau de fractions, et le' | p. 55 'corps des fractions de K'(x)_k L est L(t); on a le diagramme commutatif d'homomorphismes canoniques'",
      "printed p. 54 ends with 'et le'; p. 55 begins 'corps des fractions de K'(x)_k L ...' (scan of p. 55 checked)",
      "\\oldpage[IV-2]{55} stands after 'd'homomorphismes canoniques' (first line of page_055.tex), so p. 54 carries two lines of p. 55",
      "marker", "et le corps des fractions", "et le\n\\oldpage[IV-2]{55}\ncorps des fractions",
      note="Apply together with the deletion of the old \\oldpage[IV-2]{55} after 'd'homomorphismes canoniques' (and its surrounding blank lines), which lies in the p. 55 segment."),
]


def norm(t):
    return t.replace("\r\n", "\n")


ok = True
by_page = {}
for i, f in enumerate(L):
    by_page.setdefault(f["page"], []).append((i, f))
for p, items in by_page.items():
    text = norm((RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8"))
    spans = []
    for i, f in items:
        if f["fix"] is None:
            continue
        old = f["fix"]["old"]
        n = text.count(old)
        if n != 1:
            ok = False
            print(f"p{p} entry {i}: old occurs {n} times: {old!r}")
            continue
        s = text.index(old)
        spans.append((s, s + len(old), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print(f"p{p}: overlap between entries {a[2]} and {b[2]}")
    t = text
    for i, f in items:
        if f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        if t.count(old) != 1:
            ok = False
            print(f"p{p} entry {i}: sequential application fails ({t.count(old)})")
            continue
        t = t.replace(old, new)
    (RUN / "crops_050_054" / f"applied_{p:03d}.tex").write_text(t, encoding="utf-8", newline="\n")

counts = {}
for f in L:
    c = counts.setdefault(f["page"], [0, 0, 0])
    if f["kind"] == "misprint_in_print":
        c[2] += 1
    elif f["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", {p: tuple(c) for p, c in sorted(counts.items())})
print("all checks passed" if ok else "CHECK FAILURES")
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote", OUT, len(L), "findings")
sys.exit(0 if ok else 1)
