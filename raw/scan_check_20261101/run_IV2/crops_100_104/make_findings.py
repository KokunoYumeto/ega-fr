# Builds findings_100_104.json. In the strings below "⏎" stands for a line break (LF).
import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2\findings_100_104.json")
NL = "⏎"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    return d


L = []
# ---------------- page 99/100 break: the p. 100 marker is six printed lines too late ----------------
L.append(F(99, "page break 99/100: the p. 100 marker (edit 1 of 2, insert)",
           "printed p. 99 ends '... sont égaux lorsque Y est universellement'; printed p. 100 begins 'caténaire n'est autre que l'égalité (5.6.1.1)'",
           r"\oldpage[IV-2]{100} stands after '... comme espace sous-jacent.' (before 'Nous démontrerons'), six printed lines too late",
           "marker", None, "high",
           r"universellement caténaire n'est autre que",
           r"universellement⏎\oldpage[IV-2]{100}⏎caténaire n'est autre que",
           "The old text lies in the p. 99 segment (page_099.tex), hence page 99. Apply before the next entry and before the three p. 100 entries that follow it (deg.tr / k(y) / k(x)), whose text moves into the p. 100 segment with this edit."))
L.append(F(100, "page break 99/100: the p. 100 marker (edit 2 of 2, remove the misplaced marker)",
           "see the previous finding; 'Nous démontrerons plus loin' opens a new paragraph on p. 100",
           r"\oldpage[IV-2]{100} between 'sous-jacent.' and 'Nous démontrerons'",
           "marker", None, "high",
           r"\oldpage[IV-2]{100}⏎⏎Nous démontrerons",
           r"Nous démontrerons",
           "Apply together with, and after, the previous edit. The blank line after 'sous-jacent.' remains, so 'Nous démontrerons' still opens a paragraph, as printed."))
L.append(F(100, "p. 100, l. 3 (text now before the p. 100 marker): 'deg.tr_{k(y)} k(x) est la dimension'",
           "deg.tr_{k(y)}k(x): no period after 'tr'",
           r"\operatorname{deg.tr.}_{k(y)}k(x)",
           "punctuation", None, "high",
           r"générale, $\operatorname{deg.tr.}",
           r"générale, $\operatorname{deg.tr}",
           "The old text is in page_099.tex until the p. 100 marker is moved (first entry); apply after that move. Same correction as on pp. 52-54."))
L.append(F(100, "p. 100, l. 3 (text now before the p. 100 marker): subscript k(y) of deg.tr",
           "subscript k(y) with a bold k",
           r"_{k(y)}",
           "convention", 1, "high",
           r"_{k(y)}",
           r"_{\mathbf{k}(y)}",
           "Bold upright k at subscript size. Old text is in page_099.tex until the p. 100 marker is moved; apply after that move: '_{k(y)}' is unique in the p. 100 segment only (the p. 99 display has it twice more)."))
L.append(F(100, "p. 100, l. 3 (text now before the p. 100 marker): 'k(x) est la dimension de'",
           "k(x) with a bold italic k",
           r"k(x)$ est la dimension",
           "convention", 1, "high",
           r"k(x)$ est la dimension",
           r"\boldsymbol{k}(x)$ est la dimension",
           "Old text is in page_099.tex until the p. 100 marker is moved; apply after that move."))
# ---------------- page 100 ----------------
L.append(F(100, "paragraph 'Nous démontrerons plus loin': 'on a toujours δ(x) ⩾ 0'",
           "'on a toujours' italic", "upright",
           "convention", 6, "high",
           r"(5.6.5), on⏎a toujours",
           r"(5.6.5), \emph{on⏎a toujours}"))
L.append(F(100, "Corollaire (5.6.6), l. 1: 'Sous les hypothèses générales de (5.6.5)'",
           "(5.6.5) upright inside the italic statement", "(5.6.5) italic (corollary environment)",
           "convention", 6, "high",
           r"générales de (5.6.5), on a",
           r"générales de \textup{(5.6.5)}, on a"))
L.append(F(100, "Corollaire (5.6.6): 'pour que les deux membres de (5.6.6.1) soient égaux'",
           "(5.6.6.1) upright inside the italic statement", "italic",
           "convention", 6, "high",
           r"de (5.6.6.1) soient égaux",
           r"de \textup{(5.6.6.1)} soient égaux"))
L.append(F(100, "Corollaire (5.6.6), last sentence: 'les deux membres de (5.6.6.1) sont égaux'",
           "(5.6.6.1) upright inside the italic statement", "italic",
           "convention", 6, "high",
           r"de (5.6.6.1) sont égaux lorsque",
           r"de \textup{(5.6.6.1)} sont égaux lorsque"))
L.append(F(100, "proof of (5.6.6), last paragraph: 'f(U) est une partie constructible de Y'",
           "'constructible' italic", "upright",
           "convention", 6, "high",
           r"partie constructible de $Y$",
           r"partie \emph{constructible} de $Y$"))
L.append(F(100, "proof of (5.6.6): '(0_III, 9.2.2)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"$(0_{\mathrm{III}},9.2.2)$",
           r"$(\mathbf{0}_{\mathrm{III}},9.2.2)$"))
L.append(F(100, "'On notera que la condition (5.6.6.2) est trivialement vérifiée lorsque f est surjectif.'",
           "'surjectif' italic", "upright",
           "convention", 6, "high",
           r"$f$⏎est surjectif.",
           r"$f$⏎est \emph{surjectif}."))
L.append(F(100, "proof of (5.6.7), l. 1: 'En vertu de (0, 14.1.7)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"(0, 14.1.7)",
           r"(\textbf{0}, 14.1.7)"))
L.append(F(100, "proof of (5.6.7): 'Z_i est intègre (0_I, 2.1.5)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"$(0_{\mathrm I},2.1.5)$",
           r"$(\mathbf{0}_{\mathrm I},2.1.5)$"))
L.append(F(100, "proof of (5.6.7): 'l'injection canonique (I, 5.2.2)'",
           "bold I", "plain I",
           "convention", 2, "high",
           r"(I, 5.2.2)",
           r"(\textbf{I}, 5.2.2)"))
L.append(F(100, "page break 100/101: the p. 101 marker (edit 1 of 2, insert)",
           "printed p. 100 ends '... et g_i est dominant'; printed p. 101 begins 'et de type fini (1.5.4). On a dim(Z_i) ⩽ dim(Y)' in the same paragraph",
           r"'et de type fini (1.5.4).' ends the p. 100 segment; then a blank line, \oldpage[IV-2]{101}, a blank line and 'On a' (a paragraph break the print does not have)",
           "marker", None, "high",
           r"est dominant et de type fini (1.5.4).⏎⏎",
           r"est dominant⏎\oldpage[IV-2]{101}⏎et de type fini (1.5.4).⏎",
           "Also removes the blank line after '(1.5.4).'. Apply together with the next entry (p. 101), which removes the old marker and the blank line after it."))
# ---------------- page 101 ----------------
L.append(F(101, "page break 100/101: the p. 101 marker (edit 2 of 2, remove the misplaced marker)",
           "'On a dim(Z_i) ⩽ dim(Y)' continues the paragraph of '(1.5.4).' on the first line of p. 101",
           r"\oldpage[IV-2]{101} with blank lines before 'On a $\dim(Z_i)'",
           "marker", None, "high",
           r"\oldpage[IV-2]{101}⏎⏎On a",
           r"On a",
           "Apply together with, and after, the previous entry. Result: 'est dominant\\n\\oldpage[IV-2]{101}\\net de type fini (1.5.4).\\nOn a ...' (one paragraph, as printed)."))
L.append(F(101, "l. 1: 'si z_i est le point générique de Z_i'",
           "z_i (italic z, the same glyph as z_i on p. 79; not the Greek ζ, compare ζ on IV-3 p. 108)",
           r"$\zeta_i$",
           "symbol", None, "high",
           r"si $\zeta_i$ est le",
           r"si $z_i$ est le"))
L.append(F(101, "l. 2: 'dim(g_i^{-1}(z_i)) ⩽ n'",
           "z_i (italic z)", r"\zeta_i",
           "symbol", None, "high",
           r"(g_i^{-1}(\zeta_i))",
           r"(g_i^{-1}(z_i))"))
L.append(F(101, "Corollaire (5.6.8), l. 1-2: 'X un préschéma irréductible'",
           "'irréductible' set roman inside the italic statement", "italic (corollary environment)",
           "convention", 6, "high",
           r"préschéma⏎irréductible,",
           r"préschéma⏎\textup{irréductible},"))
L.append(F(101, "Corollaire (5.6.8), l. 3: '(resp. dim(f^{-1}(y)) = n)'",
           "'(resp.' and the closing parenthesis upright", "italic",
           "convention", 6, "high",
           r"(resp.⏎$\dim(f^{-1}(y))=n$)",
           r"\textup{(resp.}⏎$\dim(f^{-1}(y))=n$\textup{)}"))
L.append(F(101, "Corollaire (5.6.8): '(resp.' between (5.6.8.1) and (5.6.8.2)",
           "'(resp.' upright", "italic",
           "convention", 6, "high",
           r"\end{equation}⏎(resp.⏎\begin{equation}",
           r"\end{equation}⏎\textup{(resp.}⏎\begin{equation}"))
L.append(F(101, "proof of (5.6.8): 'l'hypothèse entraîne que f est surjectif'",
           "'surjectif' italic", "upright",
           "convention", 6, "high",
           r"que $f$ est surjectif, donc",
           r"que $f$ est \emph{surjectif}, donc"))
L.append(F(101, "proof of (5.6.10): 'on a deg.tr_A B = 0'",
           "deg.tr_A B = 0: no period after 'tr'",
           r"\operatorname{deg.tr.}_A B=0",
           "punctuation", None, "high",
           r"\operatorname{deg.tr.}_A B=0",
           r"\operatorname{deg.tr}_A B=0"))
L.append(F(101, "Exemple (5.6.11), l. 1: 'intègre et intégralement clos'",
           "'intégralement clos' italic", "upright (example body is upright)",
           "convention", 6, "high",
           r"intègre et intégralement clos;",
           r"intègre et \emph{intégralement clos};"))
L.append(F(101, "Exemple (5.6.11), l. 2: 'on a vu (0, 16.1.6)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"(0, 16.1.6)",
           r"(\textbf{0}, 16.1.6)"))
L.append(F(101, "Exemple (5.6.11), l. 4: 'd'anneau local noethérien intègre caténaire A'",
           "'caténaire' italic", "upright",
           "convention", 6, "high",
           r"intègre caténaire $A$",
           r"intègre \emph{caténaire} $A$"))
L.append(F(101, "page break 101/102: blank line before the p. 102 marker",
           "the sentence runs on: p. 101 ends 'm' = (ST−1) de hauteur 1;', p. 102 begins 'les corps résiduels correspondants'",
           "blank lines around \\oldpage[IV-2]{102} make a paragraph break",
           "extra", None, "high",
           r"de hauteur 1;⏎⏎",
           r"de hauteur 1;⏎",
           "Apply together with the first p. 102 entry (blank line after the marker)."))
# ---------------- page 102 ----------------
L.append(F(102, "page break 101/102: blank line after the p. 102 marker",
           "'les corps résiduels correspondants' continues the sentence of p. 101",
           "blank line after \\oldpage[IV-2]{102}",
           "extra", None, "high",
           r"\oldpage[IV-2]{102}⏎⏎les corps",
           r"\oldpage[IV-2]{102}⏎les corps",
           "Apply together with the last p. 101 entry."))
L.append(F(102, "l. 1: 'sont k(m) = k'",
           "bold italic k in k(m) (the second k plain)", r"$k(\mathfrak m)=k$",
           "convention", 1, "high",
           r"sont $k(\mathfrak m)=k$",
           r"sont $\boldsymbol{k}(\mathfrak m)=k$"))
L.append(F(102, "l. 1: 'k(m') = k(S)'",
           "bold italic k in k(m') (k(S) plain)", r"$k(\mathfrak m')=k(S)$",
           "convention", 1, "high",
           r"$k(\mathfrak m')=k(S)$",
           r"$\boldsymbol{k}(\mathfrak m')=k(S)$"))
L.append(F(102, "l. 3: 'E/m = k(m)'",
           "bold italic k", "plain k",
           "convention", 1, "high",
           r"$E/\mathfrak m=k(\mathfrak m)$",
           r"$E/\mathfrak m=\boldsymbol{k}(\mathfrak m)$"))
L.append(F(102, "l. 3: 'E/m' = k(m')'",
           "bold italic k", "plain k",
           "convention", 1, "high",
           r"$E/\mathfrak m'=k(\mathfrak m')$",
           r"$E/\mathfrak m'=\boldsymbol{k}(\mathfrak m')$"))
L.append(F(102, "l. 4: 'un isomorphisme de k(m)'",
           "bold italic k", "plain k",
           "convention", 1, "high",
           r"isomorphisme de⏎$k(\mathfrak m)$",
           r"isomorphisme de⏎$\boldsymbol{k}(\mathfrak m)$"))
L.append(F(102, "l. 4: 'sur k(m')'",
           "bold italic k", "plain k",
           "convention", 1, "high",
           r"sur $k(\mathfrak m')$, et",
           r"sur $\boldsymbol{k}(\mathfrak m')$, et"))
L.append(F(102, "l. 2: 'ces corps sont isomorphes'",
           "'isomorphes' italic", "upright",
           "convention", 6, "high",
           r"ces corps sont isomorphes.",
           r"ces corps sont \emph{isomorphes}."))
L.append(F(102, "l. 10: 'E est une C-algèbre finie'",
           "'finie' italic", "upright",
           "convention", 6, "high",
           r"$C$-algèbre finie et est évidemment",
           r"$C$-algèbre \emph{finie} et est évidemment"))
L.append(F(102, "l. 11: 'que C est noethérien : cela résultera'",
           "'noethérien' italic", "upright",
           "convention", 6, "high",
           r"$C$ est noethérien:",
           r"$C$ est \emph{noethérien}:"))
L.append(F(102, "Lemme (5.6.11.1): label (i)",
           "'(i)' upright", "italic (lemma environment)",
           "convention", 6, "high",
           r"\item[(i)] Pour tout idéal",
           r"\item[\textup{(i)}] Pour tout idéal"))
L.append(F(102, "Lemme (5.6.11.1) (i), l. 2: 'des idéaux 𝔏 de S'",
           "Fraktur capital L (the glyph of (𝔏_n) in the proof of (ii))", r"\mathfrak a",
           "symbol", None, "high",
           r"idéaux⏎$\mathfrak a$ de $S$ tels que",
           r"idéaux⏎$\mathfrak L$ de $S$ tels que"))
L.append(F(102, "Lemme (5.6.11.1) (i), l. 2: 'tels que R.𝔏 = 𝔍'",
           "R.𝔏 = 𝔍 (period between R and Fraktur L)", r"R\mathfrak a=\mathfrak J",
           "formula", None, "high",
           r"$R\mathfrak a=\mathfrak J$",
           r"$R.\mathfrak L=\mathfrak J$"))
L.append(F(102, "Lemme (5.6.11.1): label (ii)",
           "'(ii)' upright", "italic (lemma environment)",
           "convention", 6, "high",
           r"\item[(ii)] Si $S/\mathfrak K$",
           r"\item[\textup{(ii)}] Si $S/\mathfrak K$"))
L.append(F(102, "Lemme (5.6.11.1) (ii), end: 'd'idéaux de S contenus dans K est stationnaire'",
           "roman K, where the conductor Fraktur K is meant (the proof of (ii) has 'contenus dans 𝔎')",
           r"contenus dans $K$ est stationnaire",
           "misprint_in_print", None, "high", None, None,
           "The TeX keeps the printed reading.",
           corrected=r"contenus dans $\mathfrak K$ est stationnaire"))
L.append(F(102, "proof of (5.6.11.1) (i): '𝔎𝔍 = 𝔎(R.𝔏) = 𝔎𝔏 ⊂ 𝔏'",
           "𝔎(R.𝔏) = 𝔎𝔏 ⊂ 𝔏 (Fraktur L, period after R)",
           r"\mathfrak K(R\mathfrak a)=\mathfrak K\mathfrak a\subset\mathfrak a",
           "formula", None, "high",
           r"\mathfrak K(R\mathfrak a)⏎=\mathfrak K\mathfrak a\subset\mathfrak a$",
           r"\mathfrak K(R.\mathfrak L)⏎=\mathfrak K\mathfrak L\subset\mathfrak L$"))
L.append(F(102, "proof of (5.6.11.1) (i): '(𝔏 étant un idéal de S)'",
           "Fraktur L", r"\mathfrak a",
           "symbol", None, "high",
           r"($\mathfrak a$ étant un idéal de $S$)",
           r"($\mathfrak L$ étant un idéal de $S$)"))
L.append(F(102, "proof of (5.6.11.1) (ii), l. 2: 'La suite des idéaux R.𝔏_n de R'",
           "R.𝔏_n (period)", r"R\mathfrak L_n",
           "symbol", None, "high",
           r"idéaux $R\mathfrak L_n$ de $R$",
           r"idéaux $R.\mathfrak L_n$ de $R$"))
L.append(F(102, "proof of (5.6.11.1) (ii), l. 3: 'tous les idéaux R.𝔏_n sont égaux'",
           "R.𝔏_n (period)", r"R\mathfrak L_n",
           "symbol", None, "high",
           r"idéaux $R\mathfrak L_n$ sont égaux",
           r"idéaux $R.\mathfrak L_n$ sont égaux"))
L.append(F(102, "'Il résulte de (0, 16.1.5) que l'on a dim(C) = dim(E) = 2'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"Il résulte de (0, 16.1.5)",
           r"Il résulte de (\textbf{0}, 16.1.5)"))
L.append(F(102, "'si U = C — 𝔫'",
           "long dash for set difference", "minus",
           "convention", 7, "high",
           r"$U=C-\mathfrak n$",
           r"$U=C\setmin\mathfrak n$"))
L.append(F(102, "'donc aussi dim(A) = 2 (0, 16.1.5)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"$\dim(A)=2$ (0, 16.1.5)",
           r"$\dim(A)=2$ (\textbf{0}, 16.1.5)"))
L.append(F(102, "last paragraph: 'il existe un seul idéal premier 𝔭''",
           "'un seul' italic", "upright",
           "convention", 6, "high",
           r"il existe un⏎seul idéal",
           r"il existe \emph{un⏎seul} idéal"))
L.append(F(102, "page break 102/103: blank line before the p. 103 marker",
           "the sentence runs on: p. 102 ends 'du théorème de Cohen-Seidenberg qu'un', p. 103 begins 'tel idéal est nécessairement'",
           "blank lines around \\oldpage[IV-2]{103} make a paragraph break",
           "extra", None, "high",
           r"Cohen-Seidenberg qu'un⏎⏎",
           r"Cohen-Seidenberg qu'un⏎",
           "Apply together with the first p. 103 entry."))
# ---------------- page 103 ----------------
L.append(F(103, "page break 102/103: blank line after the p. 103 marker",
           "'tel idéal est nécessairement de hauteur 1' continues the sentence of p. 102",
           "blank line after \\oldpage[IV-2]{103}",
           "extra", None, "high",
           r"\oldpage[IV-2]{103}⏎⏎tel idéal",
           r"\oldpage[IV-2]{103}⏎tel idéal",
           "Apply together with the last p. 102 entry."))
L.append(F(103, "l. 3: 'donc E_𝔭 = C_𝔭, ce qui prouve nos assertions'",
           "E_𝔭 = C_𝔭 (no prime on 𝔭 in E's subscript; p. 102 has C_𝔭 = E_𝔭' with a prime)",
           r"$E_{\mathfrak p'}=C_{\mathfrak p}$",
           "formula", None, "high",
           r"$E_{\mathfrak p'}=C_{\mathfrak p}$",
           r"$E_{\mathfrak p}=C_{\mathfrak p}$",
           "Not a misprint: E_𝔭 (E localized at C−𝔭) is integral over the integrally closed C_𝔭 inside its field of fractions, so E_𝔭 = C_𝔭; this gives the uniqueness of 𝔭' and E_𝔭' = C_𝔭. The TeX changed the printed formula."))
L.append(F(103, "heading 5.7: 'Profondeur et propriété (S_k).'",
           "the heading ends with a period", "no period",
           "punctuation", None, "high",
           r"\texorpdfstring{Profondeur et propriété $(S_k)$}",
           r"\texorpdfstring{Profondeur et propriété $(S_k)$.}"))
L.append(F(103, "Définition (5.7.1), l. 2: 'On appelle profondeur'",
           "'profondeur' italic like the rest of the statement", r"\emph{profondeur} (upright in the italic environment)",
           "convention", 6, "high",
           r"\emph{profondeur}",
           r"profondeur"))
L.append(F(103, "Définition (5.7.1), l. 2: '(resp. coprofondeur)'",
           "'(resp.' and ')' upright, 'coprofondeur' italic", r"(resp. \emph{coprofondeur}) in the italic environment",
           "convention", 6, "high",
           r"(resp.⏎\emph{coprofondeur})",
           r"\textup{(resp.}⏎coprofondeur\textup{)}"))
L.append(F(103, "Définition (5.7.1), l. 3: '(resp. coprof(ℱ_x))'",
           "'(resp.' and the closing parenthesis upright", "italic",
           "convention", 6, "high",
           r"(resp.⏎$\operatorname{coprof}(\mathscr F_x)$)",
           r"\textup{(resp.}⏎$\operatorname{coprof}(\mathscr F_x)$\textup{)}"))
L.append(F(103, "Définition (5.7.1), l. 3: '(0, 16.4.5 et 16.4.9)'",
           "bold 0; the reference upright inside the italic statement", "plain 0, italic",
           "convention", 2, "high",
           r"(0, 16.4.5 et 16.4.9)",
           r"\textup{(\textbf{0}, 16.4.5 et 16.4.9)}",
           "Includes the upright setting (convention 6) of the same reference."))
L.append(F(103, "Définition (5.7.1), l. 3: 'On appelle coprofondeur de ℱ le nombre'",
           "italic like the rest of the statement", r"\emph{coprofondeur de $\mathscr F$} (upright)",
           "convention", 6, "high",
           r"\emph{coprofondeur de $\mathscr F$} le nombre",
           r"coprofondeur de $\mathscr F$ le nombre"))
L.append(F(103, "equation number of the display in (5.7.1)",
           "(7.5.1.1): digits 5 and 7 interchanged", r"\tag{5.7.1.1}",
           "misprint_in_print", None, "high",
           r"\tag{5.7.1.1}",
           r"\tag{7.5.1.1}",
           "The TeX silently corrected the printed number; the fix restores the printed (7.5.1.1). The label IV.2.s5.7.1.1-fr is unchanged.",
           corrected=r"\tag{5.7.1.1}"))
L.append(F(103, "Définition (5.7.1), second paragraph: 'c'est-à-dire (0, 16.5.1) si'",
           "bold 0; the reference upright inside the italic statement", "plain 0, italic",
           "convention", 2, "high",
           r"c'est-à-dire (0, 16.5.1) si",
           r"c'est-à-dire \textup{(\textbf{0}, 16.5.1)} si",
           "Includes the upright setting (convention 6) of the same reference."))
L.append(F(103, "Définition (5.7.1), second paragraph, end: 'est encore appelé point de Cohen-Macaulay de X'",
           "italic like the rest of the statement", r"\emph{point de Cohen-Macaulay} (upright)",
           "convention", 6, "high",
           r"\emph{point de Cohen-Macaulay}",
           r"point de Cohen-Macaulay"))
L.append(F(103, "after Définition (5.7.1): paragraph 'On appelle coprofondeur de X et on note coprof(X) ...' (edit 1 of 2)",
           "this paragraph is printed roman (only 'coprofondeur', 'préschéma de Cohen-Macaulay' and 'dimension' italic): the definition ends at '... point de Cohen-Macaulay de X.'",
           r"the paragraph stands inside \begin{definition}[5.7.1] (italic), with \emph{coprofondeur de $X$}",
           "italics", None, "high",
           r"$X$.⏎⏎On appelle \emph{coprofondeur de $X$} et",
           r"$X$.⏎\end{definition}⏎⏎On appelle \emph{coprofondeur} de $X$ et",
           "Ends the definition environment before the paragraph and limits the emphasis to 'coprofondeur'. Apply together with the edit that removes \\end{definition} after '(0, 16.5.13).' and with the 'dimension' entry."))
L.append(F(103, "paragraph 'On appelle coprofondeur de X': 'de dimension 0'",
           "'dimension' italic", "no emphasis (italic only because the paragraph is inside the definition)",
           "convention", 6, "high",
           r"de⏎dimension 0",
           r"de⏎\emph{dimension} 0",
           "Must be applied together with the two edits that end Définition (5.7.1) before this paragraph; otherwise \\emph would set the word upright."))
L.append(F(103, "paragraph 'On appelle coprofondeur de X', end: '(0, 16.5.13)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"Cohen-Macaulay (0,",
           r"Cohen-Macaulay (\textbf{0},"))
L.append(F(103, "after Définition (5.7.1) (edit 2 of 2): remove the old end of the definition",
           "see the edit 1 of 2", r"\end{definition} after '(0, 16.5.13).'",
           "italics", None, "high",
           r"16.5.13).⏎\end{definition}",
           r"16.5.13).",
           "Apply together with edit 1 of 2."))
L.append(F(103, "display (5.7.2.1): 'prof(ℱ_x) ⩾ inf(k, dim(ℱ_x))'",
           "no period at the end of the display (the next sentence 'On dit que ℱ possède ...' follows)",
           r"\inf(k,\dim(\mathscr F_x)).",
           "misprint_in_print", None, "high",
           r"\inf(k,\dim(\mathscr F_x)).⏎\tag{5.7.2.1}",
           r"\inf(k,\dim(\mathscr F_x))⏎\tag{5.7.2.1}",
           "The TeX silently added the missing period; the fix restores the printed reading.",
           corrected=r"\inf(k,\dim(\mathscr F_x))."))
L.append(F(103, "after (5.7.2.2): paragraphs 'On dit que X vérifie la propriété (S_k) ...' and 'Pour que ℱ vérifie la propriété (S_k) ...' (edit 1 of 2)",
           "both paragraphs are printed roman: Définition (5.7.2) ends with the display (5.7.2.2)",
           r"both paragraphs stand inside \begin{definition}[5.7.2] (italic)",
           "italics", None, "high",
           r"\end{equation}⏎⏎On dit que $X$ vérifie",
           r"\end{equation}⏎\end{definition}⏎⏎On dit que $X$ vérifie",
           "Apply together with the next entry."))
L.append(F(103, "after (5.7.2.2) (edit 2 of 2): remove the old end of the definition",
           "see edit 1 of 2", r"\end{definition} after '$\mathscr F$ vérifie $(S_k)$.'",
           "italics", None, "high",
           r"$\mathscr F$ vérifie $(S_k)$.⏎\end{definition}",
           r"$\mathscr F$ vérifie $(S_k)$.",
           "Apply together with the previous entry."))
L.append(F(103, "Remarques (5.7.3) (i), l. 2: '(0, 16.4.5.1)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"(0, 16.4.5.1)",
           r"(\textbf{0}, 16.4.5.1)"))
L.append(F(103, "Remarques (5.7.3) (i), l. 3: 'prof(ℱ_x) ⩾ k sauf aux points'",
           "'sauf' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"\geq k$ sauf aux",
           r"\geq k$ \emph{sauf} aux"))
L.append(F(103, "Remarques (5.7.3) (i), l. 4: 'c'est-à-dire (0, 16.5.1) que'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"c'est-à-dire⏎(0, 16.5.1) que",
           r"c'est-à-dire⏎(\textbf{0}, 16.5.1) que"))
L.append(F(103, "Remarques (5.7.3) (i), l. 4-5: 'un O_X-Module de Cohen-Macaulay en ces points'",
           "'de Cohen-Macaulay' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"$\mathcal O_X$-Module de⏎Cohen-Macaulay en ces points;",
           r"$\mathcal O_X$-Module \emph{de⏎Cohen-Macaulay} en ces points;"))
L.append(F(103, "page break 103/104: blank line before the p. 104 marker",
           "the sentence runs on: p. 103 ends 'on a prof(ℱ_x) = k,', p. 104 begins 'donc ℱ est encore'",
           "blank lines around \\oldpage[IV-2]{104} make a paragraph break",
           "extra", None, "high",
           r"\operatorname{prof}(\mathscr F_x)=k$,⏎⏎",
           r"\operatorname{prof}(\mathscr F_x)=k$,⏎",
           "Apply together with the first p. 104 entry."))
# ---------------- page 104 ----------------
L.append(F(104, "page break 103/104: blank line after the p. 104 marker",
           "'donc ℱ est encore un O_X-Module de Cohen-Macaulay' continues the sentence of p. 103",
           "blank line after \\oldpage[IV-2]{104}",
           "extra", None, "high",
           r"\oldpage[IV-2]{104}⏎⏎donc",
           r"\oldpage[IV-2]{104}⏎donc",
           "Apply together with the last p. 103 entry."))
L.append(F(104, "Remarques (5.7.3) (i), cont., l. 2: 'la propriété (S_k) pour tout k'",
           "'pour tout' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"$(S_k)$ pour tout⏎$k$ signifie",
           r"$(S_k)$ \emph{pour tout}⏎$k$ signifie"))
L.append(F(104, "Remarques (5.7.3) (i), cont., l. 2: 'ℱ est un O_X-Module de Cohen-Macaulay.'",
           "'Module de Cohen-Macaulay' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"$\mathcal O_X$-Module de⏎Cohen-Macaulay. Il est",
           r"$\mathcal O_X$-\emph{Module de⏎Cohen-Macaulay}. Il est"))
L.append(F(104, "Remarques (5.7.3) (i), cont., l. 3: 'pour k ⩽ 0, tout O_X-Module cohérent'",
           "'tout' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"tout $\mathcal O_X$-Module cohérent a la",
           r"\emph{tout} $\mathcal O_X$-Module cohérent a la"))
L.append(F(104, "Remarques (5.7.3) (ii): '(0, 14.1.2)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"(0, 14.1.2)",
           r"(\textbf{0}, 14.1.2)"))
L.append(F(104, "Remarques (5.7.3) (iii), l. 4: 'la propriété (S_k) en un point x ∈ X'",
           "'en un point' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"$(S_k)$ en un point $x\in X$⏎signifie",
           r"$(S_k)$ \emph{en un point} $x\in X$⏎signifie"))
L.append(F(104, "Remarques (5.7.3) (iii), l. 4: 'le O_Y-Module ℱ̃_x'",
           "tilde over ℱ only, subscript x outside", r"\widetilde{\mathscr F_x}",
           "convention", 8, "high",
           r"\widetilde{\mathscr F_x}",
           r"\widetilde{\mathscr F}_x"))
L.append(F(104, "Remarques (5.7.3) (iii), l. 5-6: 'en général n'entraîne pas (5.7.2.2)'",
           "'n'entraîne pas' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"en général n'entraîne pas",
           r"en général \emph{n'entraîne pas}"))
L.append(F(104, "Remarques (5.7.3) (iii), end: '(0, 16.4.6)'",
           "bold 0", "plain 0",
           "convention", 2, "high",
           r"(0, 16.4.6)",
           r"(\textbf{0}, 16.4.6)"))
L.append(F(104, "Remarques (5.7.3) (iv): 'en tout point x' générisation de x'",
           "'générisation' italic in the roman remark", "no emphasis",
           "convention", 6, "high",
           r"$x'$⏎générisation de $x$.",
           r"$x'$⏎\emph{générisation} de $x$."))
L.append(F(104, "Proposition (5.7.4): label (i)",
           "'(i)' upright", "italic (proposition environment)",
           "convention", 6, "high",
           r"\item[(i)] Pour que",
           r"\item[\textup{(i)}] Pour que"))
L.append(F(104, "Proposition (5.7.4): label (ii)",
           "'(ii)' upright", "italic (proposition environment)",
           "convention", 6, "high",
           r"\item[(ii)] Supposons",
           r"\item[\textup{(ii)}] Supposons"))
L.append(F(104, "Proposition (5.7.4), l. 3: 'l'ensemble des z ∈ X tels que coprof(ℱ_x) > n'",
           "coprof(ℱ_x) > n: subscript x, while the condition is on the points z (the proof uses ℱ_z)",
           r"$\operatorname{coprof}(\mathscr F_x)>n$",
           "misprint_in_print", None, "high", None, None,
           "The TeX keeps the printed reading.",
           corrected=r"$\operatorname{coprof}(\mathscr F_z)>n$"))
L.append(F(104, "proof of (5.7.4): 'Mais si l'on pose a = dim(ℱ_z)'",
           "'Mais si l'on pose' opens a new (indented) paragraph after the display",
           r"'\]' followed directly by 'Mais si l'on pose' (same paragraph)",
           "missing", None, "high",
           r"\]⏎Mais si l'on pose",
           r"\]⏎⏎Mais si l'on pose",
           "Listed before the misprint entry for the same display; the two edits do not overlap."))
L.append(F(104, "proof of (5.7.4), second display: 'dim(ℱ_z) ⩾ n+k+1'",
           "no period at the end of the display (a new paragraph follows)",
           r"\dim(\mathscr F_z)\geq n+k+1.",
           "misprint_in_print", None, "high",
           r"\geq n+k+1.",
           r"\geq n+k+1",
           "The TeX silently added the missing period; the fix restores the printed reading.",
           corrected=r"\geq n+k+1."))

OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(L), "findings written")
