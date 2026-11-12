# Builds findings_135_139.json for the EGA IV-3 scan check, pp. 135-139.
# In the strings below, the pilcrow character stands for a line feed.
import json, sys, os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_135_139.json')
NL = '¶'

def s(x):
    return None if x is None else x.replace(NL, '\n')

F = []

def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": s(old), "new": s(new)}}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

AFTER = "Apply after the display fix above (its 'old' is unchanged by that edit)."

# ---------------------------------------------------------------- page 135
add(135, "Proposition (11.3.7) a): 'On a (Ker u)_x = 0'",
    "'Ker' with capital K, roman",
    "$(\\ker u)_x=0$: \\ker typesets lower-case 'ker'",
    "formula", None, "high",
    r"(\ker u)_x", r"(\operatorname{Ker}u)_x",
    "The IV-3 preamble does not redefine \\ker (see the document-wide note on \\ker in ega4-11).")
add(135, "Proposition (11.3.7) b): 'L'homomorphisme (u⊗1)_x : (F'⊗_{O_Y} k(y))_x → (F⊗_{O_Y} k(y))_x est injectif'",
    "the formula is in the running text of item b)",
    "set as a display \\[ ... \\]",
    "other", None, "high",
    r"\[¶(u\otimes1)_x:(\mathcal F'\otimes_{\mathcal O_Y}k(y))_x¶\longrightarrow(\mathcal F\otimes_{\mathcal O_Y}k(y))_x¶\]",
    r"$(u\otimes1)_x:(\mathcal F'\otimes_{\mathcal O_Y}k(y))_x¶\longrightarrow(\mathcal F\otimes_{\mathcal O_Y}k(y))_x$",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost. Apply before the two convention-1 entries that follow.")
add(135, "Proposition (11.3.7) b): '(F'⊗_{O_Y} k(y))_x'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"\mathcal F'\otimes_{\mathcal O_Y}k(y)", r"\mathcal F'\otimes_{\mathcal O_Y}\boldsymbol{k}(y)", AFTER)
add(135, "Proposition (11.3.7) b): '(F⊗_{O_Y} k(y))_x'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"(\mathcal F\otimes_{\mathcal O_Y}k(y))_x", r"(\mathcal F\otimes_{\mathcal O_Y}\boldsymbol{k}(y))_x", AFTER)
add(135, "Proposition (11.3.7), after the list: 'Si de plus F est f-plat, ...'",
    "'Si de plus' begins an indented new paragraph",
    "follows \\end{enumerate} without a blank line, so it is set without indent",
    "other", None, "high",
    r"\end{enumerate}¶Si de plus", r"\end{enumerate}¶¶Si de plus",
    "GLOBAL_ISSUES 80.")
add(135, "proof of (11.3.7), l. 1: 'La condition a) entraîne b)'",
    "'a)' and 'b)' italic in the roman proof", "upright", "italics", None, "high",
    r"La condition a) entraîne b) en vertu", r"La condition \emph{a)} entraîne \emph{b)} en vertu", None)
add(135, "proof of (11.3.7): 'supposer que l'on a X = X_0×_{Y_0}Y, f = f_0×1, F = F_0⊗_{O_{Y_0}}O_Y, F' = F'_0⊗_{O_{Y_0}}O_Y, u = u_0⊗1_Y, où'",
    "all five formulas in the running text (two lines of the paragraph)",
    "set as two displays joined by \\quad/\\qquad",
    "other", None, "high",
    r"\[¶X=X_0\times_{Y_0}Y,\quad f=f_0\times1,\quad¶\mathcal F=\mathcal F_0\otimes_{\mathcal O_{Y_0}}\mathcal O_Y,¶\]¶\[¶\mathcal F'=\mathcal F'_0\otimes_{\mathcal O_{Y_0}}\mathcal O_Y,¶\qquad u=u_0\otimes1_Y,¶\]",
    r"$X=X_0\times_{Y_0}Y$, $f=f_0\times1$,¶$\mathcal F=\mathcal F_0\otimes_{\mathcal O_{Y_0}}\mathcal O_Y$,¶$\mathcal F'=\mathcal F'_0\otimes_{\mathcal O_{Y_0}}\mathcal O_Y$, $u=u_0\otimes1_Y$,",
    "Formulas displayed where the print has them inline (GLOBAL_ISSUES 21); no connecting word lost.")
add(135, "proof of (11.3.7): 'et comme (u⊗1)_x = ((u_0⊗1)_{x_0})⊗1_{k(y)}, l'hypothèse'",
    "the formula is in the running text",
    "set as a display",
    "other", None, "high",
    r"\[¶(u\otimes1)_x=((u_0\otimes1)_{x_0})\otimes1_{k(y)},¶\]",
    r"$(u\otimes1)_x=((u_0\otimes1)_{x_0})\otimes1_{k(y)}$,",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21). Apply before the next entry.")
add(135, "proof of (11.3.7): subscript of 1_{k(y)}",
    "bold UPRIGHT k in the subscript (enlarged crop)", "plain k", "convention", 1, "high",
    r"\otimes1_{k(y)}", r"\otimes1_{\mathbf{k}(y)}",
    "Subscript k is bold upright (GLOBAL_ISSUES 48), hence \\mathbf{k}. " + AFTER)
add(135, "proof of (11.3.7): 'appliqué aux anneaux locaux noethériens'",
    "'noethériens' italic", "upright", "italics", None, "high",
    r"locaux noethériens", r"locaux \emph{noethériens}", None)
add(135, "proof of (11.3.7): 'anneaux locaux noethériens O_{y_0} et O_{x_0}'",
    "O with the subscript y_0 alone (enlarged crop)", "\\mathcal O_{Y_0,y_0}", "formula", None, "high",
    r"\mathcal O_{Y_0,y_0}$ et", r"\mathcal O_{y_0}$ et", None)
add(135, "proof of (11.3.7): 'O_{y_0} et O_{x_0} et aux'",
    "O with the subscript x_0 alone", "\\mathcal O_{X_0,x_0}", "formula", None, "high",
    r"\mathcal O_{X_0,x_0}$ et aux", r"\mathcal O_{x_0}$ et aux", None)
add(135, "proof of (11.3.7): 'aux O_{x_0}-modules'",
    "O_{x_0}-modules", "\\mathcal O_{X_0,x_0}-modules", "formula", None, "high",
    r"\mathcal O_{X_0,x_0}$-modules", r"\mathcal O_{x_0}$-modules", None)
add(135, "proof of (11.3.7): '(dont le second est plat sur O_{y_0})'",
    "'plat' italic", "upright", "italics", None, "high",
    r"second est plat", r"second est \emph{plat}", None)
add(135, "proof of (11.3.7): 'plat sur O_{y_0})'",
    "O_{y_0}", "\\mathcal O_{Y_0,y_0}", "formula", None, "high",
    r"sur $\mathcal O_{Y_0,y_0}$", r"sur $\mathcal O_{y_0}$", None)
add(135, "proof of (11.3.7): '(dont le second est plat sur O_{y_0}) que l'on a'",
    "no comma after the closing parenthesis (enlarged crop)", "'),' before 'que l'on a'",
    "punctuation", None, "high",
    r"),¶que l'on a", r")¶que l'on a", None)
add(135, "proof of (11.3.7): 'que l'on a (Ker u_0)_{x_0} = 0'",
    "'Ker' capital", "\\ker (lower-case 'ker')", "formula", None, "high",
    r"(\ker u_0)_{x_0}", r"(\operatorname{Ker}u_0)_{x_0}", None)
add(135, "proof of (11.3.7): 'on a d'ailleurs Coker u = (Coker u_0)⊗_{O_{Y_0}}O_Y; appliquant'",
    "the formula is in the running text", "set as a display", "other", None, "high",
    r"\[¶\operatorname{Coker}u=(\operatorname{Coker}u_0)¶ \otimes_{\mathcal O_{Y_0}}\mathcal O_Y~;¶\]",
    r"$\operatorname{Coker}u=(\operatorname{Coker}u_0)¶ \otimes_{\mathcal O_{Y_0}}\mathcal O_Y$~;",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21).")
add(135, "proof of (11.3.7): display '0 → (F'_0)_{x_0} → (F_0)_{x_0} → (Coker u_0)_{x_0} → 0'",
    "no punctuation after the final 0 (enlarged crop)", "comma after the final 0", "punctuation", None, "high",
    r"\longrightarrow0,¶\]", r"\longrightarrow0¶\]", None)
add(135, "Théorème (11.3.8): 'posons F_i = F/Σ_{j=1}^{i} g_jF pour 0≤i≤n (avec F_0 = F). Soient x'",
    "in the running text (the Σ with stacked limits inside the line); the parentheses of '(avec F_0 = F)' upright, 'pour' and 'avec' italic",
    "set as a display with \\text{pour}, \\text{avec}",
    "other", None, "high",
    r"\[¶\mathcal F_i=\mathcal F\big/\sum_{j=1}^{i}g_j\mathcal F¶\quad\text{pour }0\leq i\leq n¶\quad(\text{avec }\mathcal F_0=\mathcal F).¶\]",
    r"$\mathcal F_i=\mathcal F\big/\sum_{j=1}^{i}g_j\mathcal F$¶pour $0\leq i\leq n$¶\textup{(}avec $\mathcal F_0=\mathcal F$\textup{)}.",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); the position of the Σ limits is ignored. \\textup keeps the upright parentheses the display had (GLOBAL_ISSUES 26).")
add(135, "Théorème (11.3.8): 'X_y = f^{-1}(y) = X×_Y Spec(k(y))'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))", None)
add(135, "Théorème (11.3.8): 'F_y = F⊗_{O_Y} k(y)'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"_y=\mathcal F\otimes_{\mathcal O_Y}k(y)", r"_y=\mathcal F\otimes_{\mathcal O_Y}\boldsymbol{k}(y)", None)

# ---------------------------------------------------------------- page 136
add(136, "Théorème (11.3.8), after the list: 'En outre l'ensemble des x∈X vérifiant ces conditions ...'",
    "'En outre' begins an indented new paragraph",
    "follows \\end{enumerate} without a blank line: no indent",
    "other", None, "high",
    r"\end{enumerate}¶En outre", r"\end{enumerate}¶¶En outre", "GLOBAL_ISSUES 80.")
add(136, "proof of (11.3.8), l. 1: 'Le fait que a) entraîne d) résulte'",
    "'a)', 'd)' italic", "upright", "italics", None, "high",
    r"Le fait que a) entraîne d) résulte", r"Le fait que \emph{a)} entraîne \emph{d)} résulte", None)
add(136, "proof of (11.3.8): 'et c) est un cas particulier de d);'",
    "'c)', 'd)' italic", "upright", "italics", None, "high",
    r"et c) est¶un cas particulier de d)~;", r"et \emph{c)} est¶un cas particulier de \emph{d)}~;", None)
add(136, "proof of (11.3.8): 'par ailleurs a) implique b) trivialement'",
    "'a)', 'b)' italic", "upright", "italics", None, "high",
    r"par ailleurs a) implique b) trivialement", r"par ailleurs \emph{a)} implique \emph{b)} trivialement", None)
add(136, "proof of (11.3.8): 'Montrons que b) ou c) entraîne a).'",
    "'b)', 'c)', 'a)' italic", "upright", "italics", None, "high",
    r"que b) ou c) entraîne a). Les", r"que \emph{b)} ou \emph{c)} entraîne \emph{a)}. Les", None)
add(136, "proof of (11.3.8): 'le fait que c) implique a) résulte alors'",
    "'c)', 'a)' italic", "upright", "italics", None, "high",
    r"fait que c) implique a) résulte", r"fait que \emph{c)} implique \emph{a)} résulte", None)
add(136, "proof of (11.3.8): 'l'ensemble des x∈X vérifiant c) est ouvert dans Z'",
    "'c)' italic", "upright", "italics", None, "high",
    r"vérifiant c) est ouvert", r"vérifiant \emph{c)} est ouvert", None)
add(136, "proof of (11.3.8): 'Pour montrer que b) entraîne a), on est aussitôt ramené'",
    "'b)', 'a)' italic", "upright", "italics", None, "high",
    r"Pour montrer que b) entraîne a), on", r"Pour montrer que \emph{b)} entraîne \emph{a)}, on", None)
add(136, "proof of (11.3.8): 'sous-anneaux A_λ qui sont des A_0-algèbres de type fini (donc noethériennes)'",
    "'(donc noethériennes)' (feminine plural; enlarged crop)", "'(donc noethériens)'",
    "word", None, "high",
    r"(donc¶noethériens)", r"(donc¶noethériennes)",
    "The print's adjective agrees with 'A_0-algèbres'; not a misprint.")
add(136, "proof of (11.3.8): 'posant ... et F_λ = M̃_λ'",
    "tilde over M only, subscript λ outside (enlarged crop)", "\\widetilde{M_\\lambda}",
    "convention", 8, "high",
    r"\widetilde{M_\lambda}", r"\widetilde{M}_\lambda", None)
add(136, "proof of (11.3.8): 'Le fait que b) entraîne a) résultera donc de la proposition suivante'",
    "'b)', 'a)' italic", "upright", "italics", None, "high",
    r"Le fait que b) entraîne a) résultera", r"Le fait que \emph{b)} entraîne \emph{a)} résultera", None)
add(136, "Proposition (11.3.9): 'étant celles de (8.5.1)'",
    "the reference is upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"celles de (8.5.1)", r"celles de \textup{(8.5.1)}", None)
add(136, "Proposition (11.3.9): 'et (8.8.1), supposons'",
    "the reference is upright inside the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"(8.8.1),¶supposons", r"\textup{(8.8.1)},¶supposons", None)
add(136, "end of page_136.tex / top of p. 137: 'Pour prouver que | la condition est nécessaire'",
    "p. 137 begins 'la condition est nécessaire' flush left: the sentence continues; no paragraph break",
    "blank line after 'Pour prouver que', before \\oldpage[IV-3]{137}",
    "marker", None, "high",
    r"Pour prouver que¶¶", r"Pour prouver que¶",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place. Apply together with the p. 137 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- page 137
add(137, "top of p. 137, after \\oldpage[IV-3]{137}",
    "'la condition est nécessaire' continues the sentence of p. 136", "blank line after the marker",
    "marker", None, "high",
    r"\oldpage[IV-3]{137}¶¶la condition", r"\oldpage[IV-3]{137}¶la condition",
    "Mid-sentence page break (GLOBAL_ISSUES 20); apply together with the p. 136 entry removing the blank line before the marker.")
add(137, "proof of (11.3.9): 'supposer que H est f-plat. Notons maintenant le'",
    "'f-plat' italic (enlarged crop)", "upright 'plat'", "italics", None, "high",
    r"est $f$-plat. Notons", r"est \emph{$f$-plat}. Notons", None)
add(137, "Lemme (11.3.9.1): 'Alors Ker(p) est un O_X-Module'",
    "'Ker'", "\\ker (lower-case 'ker')", "formula", None, "high",
    r"Alors $\ker(p)$", r"Alors $\operatorname{Ker}(p)$", None)
add(137, "proof of (11.3.9.1): 'si K_0 = Ker(p_0)'",
    "'Ker'", "\\ker", "formula", None, "high",
    r"\mathcal K_0=\ker(p_0)", r"\mathcal K_0=\operatorname{Ker}(p_0)", None)
add(137, "proof of (11.3.9.1): 'K = Ker(p) se déduit'",
    "'Ker'", "\\ker", "formula", None, "high",
    r"\mathcal K=\ker(p)$", r"\mathcal K=\operatorname{Ker}(p)$", None)
add(137, "'Ce lemme étant démontré, posons K = Ker(G→H)'",
    "'Ker'", "\\ker", "formula", None, "high",
    r"posons $\mathcal K=\ker(\mathcal G\to\mathcal H)$", r"posons $\mathcal K=\operatorname{Ker}(\mathcal G\to\mathcal H)$", None)
add(137, "'posons K_λ = Ker(G_λ→H_λ)'",
    "'Ker'", "\\ker", "formula", None, "high",
    r"\ker(\mathcal G_\lambda\to\mathcal H_\lambda)", r"\operatorname{Ker}(\mathcal G_\lambda\to\mathcal H_\lambda)", None)
add(137, "'l'on a K_μ = Ker(G_μ→H_μ)'",
    "'Ker'", "\\ker", "formula", None, "high",
    r"\ker(\mathcal G_\mu\to\mathcal H_\mu)", r"\operatorname{Ker}(\mathcal G_\mu\to\mathcal H_\mu)", None)
add(137, "'K = v_λ*(K_λ) = Ker(G→H) = F'",
    "'Ker'", "\\ker", "formula", None, "high",
    r"=\ker(\mathcal G\to\mathcal H)=\mathcal F", r"=\operatorname{Ker}(\mathcal G\to\mathcal H)=\mathcal F", None)
add(137, "proof of (11.3.9): 'et par suite u_μ : F_μ → G_μ un homomorphisme injectif'",
    "'u_μ' (enlarged crop)", "'u_\\mu' (the TeX keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "Wrong letter: (11.3.9) and its proof call the homomorphism h (h_α, (h_λ)_{x_λ}, 0 → F →^h G → H → 0); u is the letter of (11.3.7). Not in the authors' errata (EGA IV, liste 3). Diplomatic TeX already right; the corrected edition replaces 'suite $u_\\mu:\\mathcal F_\\mu\\to\\mathcal G_\\mu$' by the corrected reading.",
    corrected=r"$h_\mu:\mathcal F_\mu\to\mathcal G_\mu$", nofix=True)
add(137, "proof of (11.3.8): 'Puisque l'ensemble des x∈X vérifiant b) est ouvert'",
    "'b)' italic", "upright", "italics", None, "high",
    r"vérifiant b) est ouvert", r"vérifiant \emph{b)} est ouvert", None)
add(137, "proof of (11.3.8): 'il est clair que b) entraîne b')'",
    "first 'b)' italic", "upright", "italics", None, "high",
    r"clair¶que b) entraîne", r"clair¶que \emph{b)} entraîne", None)
add(137, "proof of (11.3.8): 'entraîne b'). Montrons'",
    "italic \"b')\" with its closing parenthesis", "'b$'$' without the parenthesis, upright",
    "punctuation", None, "high",
    r"b$'$. Montrons", r"\emph{b$'$)}. Montrons",
    "Restores the missing ')' and the italics in one edit.")
add(137, "proof of (11.3.8): 'Montrons enfin que b') entraîne c).'",
    "italic \"b')\" (with ')') and italic 'c)'", "'b$'$' without the parenthesis; 'b'' and 'c)' upright",
    "punctuation", None, "high",
    r"que b$'$ entraîne c).", r"que \emph{b$'$)} entraîne \emph{c)}.",
    "Restores the missing ')' and the italics of b') and c) in one edit.")
add(137, "proof of (11.3.8): 'F_n est f-plat dans un voisinage de x (11.3.1), et on peut donc'",
    "comma after '(11.3.1)' (enlarged crop)", "no comma", "punctuation", None, "high",
    r"(11.3.1) et on peut", r"(11.3.1), et on peut", None)
add(137, "proof of (11.3.8): 'Comme par définition gr•_J(F) est isomorphe'",
    "Fraktur J subscript and raised bullet: gr•_𝔍(F) (enlarged crop)", "\\operatorname{gr}_{\\mathcal J}^*: script J and asterisk",
    "formula", None, "high",
    r"\operatorname{gr}_{\mathcal J}^*(\mathcal F)", r"\operatorname{gr}_{\mathfrak J}^\bullet(\mathcal F)",
    "Two differences in one token: Fraktur J (ega4-11 writes \\mathfrak J for it elsewhere, e.g. 11.2.9) and the raised bullet of the graded object (GLOBAL_ISSUES 60; see the document-wide note). The script J of '(J_y)_x est l'idéal' two lines below is right.")
add(137, "proof of (11.3.8): 'il est f-plat, et on en conclut'",
    "'f-plat' italic", "upright 'plat'", "italics", None, "high",
    r"il est $f$-plat, et", r"il est \emph{$f$-plat}, et", None)
add(137, "proof of (11.3.8): 'F lui-même est f-plat au voisinage de x'",
    "'f-plat' italic", "upright 'plat'", "italics", None, "high",
    r"lui-même est $f$-plat au", r"lui-même est \emph{$f$-plat} au", None)
add(137, "diagram, top left: '((gr⁰_{J_x}(F_x))[T_1, ..., T_n])⊗_{O_y} k(y)'",
    "an extra pair of parentheses around gr⁰_{J_x}(F_x); Fraktur J_x (enlarged crop)",
    "(\\operatorname{gr}_{\\mathcal J_x}^0(\\mathcal F_x)[T_1,\\ldots,T_n]): one pair of parentheses fewer, script J",
    "formula", None, "high",
    r"(\operatorname{gr}_{\mathcal J_x}^0(\mathcal F_x)[T_1,\ldots,T_n])",
    r"((\operatorname{gr}_{\mathfrak J_x}^0(\mathcal F_x))[T_1,\ldots,T_n])",
    "Missing parentheses and Fraktur J in one edit.")
add(137, "diagram, top left: '⊗_{O_y} k(y)'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"k(y) \ar[r] \ar[d]", r"\boldsymbol{k}(y) \ar[r] \ar[d]", None)
add(137, "diagram, top right: 'gr•_{J_x}(F_x)⊗_{O_y} k(y)'",
    "Fraktur J_x and raised bullet", "\\operatorname{gr}_{\\mathcal J_x}^*", "formula", None, "high",
    r"\operatorname{gr}_{\mathcal J_x}^*(\mathcal F_x)", r"\operatorname{gr}_{\mathfrak J_x}^\bullet(\mathcal F_x)",
    "Fraktur J and bullet in one edit.")
add(137, "diagram, top right: '⊗_{O_y} k(y)'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"k(y) \ar[d] \\", r"\boldsymbol{k}(y) \ar[d] \\", None)
add(137, "diagram, bottom left: '(gr⁰_{(J_y)_x}((F_y)_x))[T_1, ..., T_n]'",
    "Fraktur J (enlarged crop)", "\\mathcal J", "font", None, "high",
    r"(\operatorname{gr}_{(\mathcal J_y)_x}^0", r"(\operatorname{gr}_{(\mathfrak J_y)_x}^0", None)
add(137, "diagram, bottom right: 'gr•_{(J_y)_x}((F_y)_x)'",
    "Fraktur J and raised bullet", "\\operatorname{gr}_{(\\mathcal J_y)_x}^*", "formula", None, "high",
    r"\operatorname{gr}_{(\mathcal J_y)_x}^*((\mathcal F_y)_x)", r"\operatorname{gr}_{(\mathfrak J_y)_x}^\bullet((\mathcal F_y)_x)",
    "Fraktur J and bullet in one edit.")
add(137, "end of page_137.tex / top of p. 138: 'dans le diagramme [diagram] | les flèches verticales sont des isomorphismes'",
    "p. 138 begins 'les flèches verticales' flush left: the sentence continues after the diagram; no paragraph break",
    "blank line after the diagram's \\], before \\oldpage[IV-3]{138}",
    "marker", None, "high",
    r"}¶\]¶¶", r"}¶\]¶",
    "Mid-sentence page break (GLOBAL_ISSUES 20/47); the marker itself is in the right place. Apply together with the p. 138 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- page 138
add(138, "top of p. 138, after \\oldpage[IV-3]{138}",
    "'les flèches verticales' continues the sentence of p. 137", "blank line after the marker",
    "marker", None, "high",
    r"\oldpage[IV-3]{138}¶¶les flèches", r"\oldpage[IV-3]{138}¶les flèches",
    "Mid-sentence page break (GLOBAL_ISSUES 20); apply together with the p. 137 entry removing the blank line before the marker.")
add(138, "end of the proof of (11.3.8), l. 2: 'la suite ((g_i⊗1)_x) est (F_y)_x-quasi-régulière'",
    "roman upright F, not the script F (enlarged crop)", "$(\\mathcal F_y)_x$: silently corrected",
    "misprint_in_print", None, "high",
    r"$(\mathcal F_y)_x$-quasi", r"$(F_y)_x$-quasi",
    "Wrong-fount letter (the sheaf F_y is script everywhere else; the authors' errata, liste 3, corrects the same slip on p. 134, l. 16). The fix restores the printed roman F (upright capital, written $F$ like the edition's other upright capitals).",
    corrected=r"$(\mathcal F_y)_x$-quasi-régulière")
add(138, "end of the proof of (11.3.8), l. 3: 'et par suite aussi (F_y)_x-régulière'",
    "roman upright F (enlarged crop)", "$(\\mathcal F_y)_x$: silently corrected",
    "misprint_in_print", None, "high",
    r"$(\mathcal F_y)_x$-régulière, puisque", r"$(F_y)_x$-régulière, puisque",
    "Same wrong-fount F as the previous entry.",
    corrected=r"$(\mathcal F_y)_x$-régulière")
add(138, "end of the proof of (11.3.8): 'localement de type fini sur k(y). C.Q.F.D.'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"$k(y)$. C.Q.F.D.", r"$\boldsymbol{k}(y)$. C.Q.F.D.", None)
add(138, "Théorème (11.3.10): 'On suppose vérifiée l'une des deux hypothèses suivantes'",
    "'l'une' roman (emphasis) inside the italic statement (enlarged crop)", "italic like its context",
    "italics", None, "high",
    r"vérifiée l'une des", r"vérifiée \emph{l'une} des",
    "\\emph gives the printed upright inside the italic theorem (same treatment as (8.4.2), p. 18).")
add(138, "Théorème (11.3.10): item labels 1°, 2°",
    "labels '1°', '2°' upright", "label=\\arabic{enumi}\\textsuperscript{o} inside the italic theorem: italic labels",
    "convention", 6, "high",
    r"\begin{enumerate}[label=\arabic{enumi}\textsuperscript{o}]¶\item $S$",
    r"\begin{enumerate}[label=\textup{\arabic{enumi}\textsuperscript{o}}]¶\item $S$",
    "One edit covers both labels (GLOBAL_ISSUES 16; cf. \\textup{1\\textsuperscript{o}}, p. 40).")
add(138, "Théorème (11.3.10): 'Alors, avec les notations de (9.4.1), si F_x ≠ 0'",
    "the reference is upright inside the italic statement (enlarged crop)", "italic",
    "convention", 6, "high",
    r"notations de (9.4.1)", r"notations de \textup{(9.4.1)}", None)
add(138, "Théorème (11.3.10): 'En outre, dans l'hypothèse 2°'",
    "'2°' upright", "italic (theorem environment)", "convention", 6, "high",
    r"l'hypothèse 2\textsuperscript{o}, l'ensemble", r"l'hypothèse \textup{2\textsuperscript{o}}, l'ensemble", None)
add(138, "Théorème (11.3.10): 'vérifiant la condition b) est ouvert dans X'",
    "'b)' upright", "italic", "convention", 6, "high",
    r"la condition b) est ouvert", r"la condition \textup{b)} est ouvert", None)
add(138, "proof of (11.3.10): 'il est clair que b) implique a) sans supposer'",
    "'b)', 'a)' italic", "upright", "italics", None, "high",
    r"clair que b) implique a) sans", r"clair que \emph{b)} implique \emph{a)} sans", None)
add(138, "proof of (11.3.10): 'Pour prouver que a) entraîne b), on peut'",
    "'a)', 'b)' italic", "upright", "italics", None, "high",
    r"que¶a) entraîne b), on peut", r"que¶\emph{a)} entraîne \emph{b)}, on peut", None)
add(138, "proof of (11.3.10): 'de plus S est noethérien, c'est-à-dire'",
    "'noethérien' italic", "upright", "italics", None, "high",
    r"est noethérien, c'est", r"est \emph{noethérien}, c'est", None)
add(138, "Lemme (11.3.10.2) (ii): 'pour la topologie JB-préadique (0_III, 10.2.1)'",
    "'préadique' (singular; enlarged crop)", "'préadiques'", "word", None, "high",
    r"-préadiques $(\mathbf 0", r"-préadique $(\mathbf 0", None)
add(138, "Lemme (11.3.10.2): 'Alors :'",
    "'Alors :' begins an indented new paragraph", "follows \\end{enumerate} without a blank line: no indent",
    "other", None, "high",
    r"\end{enumerate}¶Alors~:", r"\end{enumerate}¶¶Alors~:", "GLOBAL_ISSUES 80.")
add(138, "Lemme (11.3.10.2): item labels 1°, 2°",
    "labels '1°' (p. 138) and '2°' (p. 139) upright", "label=\\arabic{enumi}\\textsuperscript{o} inside the italic lemma: italic labels",
    "convention", 6, "high",
    r"\begin{enumerate}[label=\arabic{enumi}\textsuperscript{o}]¶\item Si",
    r"\begin{enumerate}[label=\textup{\arabic{enumi}\textsuperscript{o}}]¶\item Si",
    "One edit covers 1° here and 2° on p. 139.")
add(138, "Lemme (11.3.10.2) 1°: 'Si l'une des conditions (i), (ii) est vérifiée'",
    "'(i), (ii)' upright", "italic", "convention", 6, "high",
    r"conditions (i), (ii) est", r"conditions \textup{(i), (ii)} est", None)
add(138, "Lemme (11.3.10.2) 1°: 'la conjonction de a) et b) implique c), et c) implique a).'",
    "'a)', 'b)', 'c)', 'c)', 'a)' upright; 'et', 'implique' italic", "all italic",
    "convention", 6, "high",
    r"conjonction de a) et¶b) implique c), et c) implique a).",
    r"conjonction de \textup{a)} et¶\textup{b)} implique \textup{c)}, et \textup{c)} implique \textup{a)}.",
    "Five upright condition letters.")

# ---------------------------------------------------------------- page 139
add(139, "Lemme (11.3.10.2) 2°: 'Si la condition (i) ou la conjonction de (ii) et (iii) est vérifiée'",
    "'(i)', '(ii)', '(iii)' upright", "italic", "convention", 6, "high",
    r"condition (i) ou la conjonction de (ii) et (iii) est",
    r"condition \textup{(i)} ou la conjonction de \textup{(ii)} et \textup{(iii)} est", None)
add(139, "Lemme (11.3.10.2) 2°: 'la conjonction de c) et d) implique la conjonction de a) et b).'",
    "'c)', 'd)', 'a)', 'b)' upright", "italic", "convention", 6, "high",
    r"conjonction de c) et d) implique la conjonction de a) et b).",
    r"conjonction de \textup{c)} et \textup{d)} implique la conjonction de \textup{a)} et \textup{b)}.", None)
add(139, "proof of (11.3.10.2) 1°: 'Supposons donc c) vérifiée, et prouvons a).'",
    "'c)', 'a)' italic", "upright", "italics", None, "high",
    r"Supposons donc c) vérifiée, et prouvons a).", r"Supposons donc \emph{c)} vérifiée, et prouvons \emph{a)}.", None)
for old, new, w in [
    (r"gradués $\operatorname{gr}_{\mathfrak J}^*(A)$", r"gradués $\operatorname{gr}_{\mathfrak J}^\bullet(A)$", "'les anneaux gradués gr•_J(A)'"),
    (r"$\operatorname{gr}_{\mathfrak J}^*(B)$ et le module", r"$\operatorname{gr}_{\mathfrak J}^\bullet(B)$ et le module", "'gr•_J(B) et le module gradué'"),
    (r"$\operatorname{gr}_{\mathfrak J}^*(M)$ (à la fois", r"$\operatorname{gr}_{\mathfrak J}^\bullet(M)$ (à la fois", "'gr•_J(M) (à la fois sur'"),
    (r"$\operatorname{gr}_{\mathfrak J}^*(A)$ et¶", r"$\operatorname{gr}_{\mathfrak J}^\bullet(A)$ et¶", "'sur gr•_J(A) et'"),
    (r"$\operatorname{gr}_{\mathfrak J}^*(B)$) relatifs", r"$\operatorname{gr}_{\mathfrak J}^\bullet(B)$) relatifs", "'gr•_J(B)) relatifs'"),
]:
    add(139, "proof of (11.3.10.2) 1°: " + w,
        "raised bullet", "^* (asterisk)", "symbol", None, "high", old, new,
        "Graded object: the print has a raised bullet (GLOBAL_ISSUES 60; document-wide note).")
add(139, "proof of (11.3.10.2) 1°: 'relatifs aux filtrations J-préadiques'",
    "'préadiques' (plural; enlarged crop)", "'préadique'", "word", None, "high",
    r"$\mathfrak J$-préadique, ainsi", r"$\mathfrak J$-préadiques, ainsi", None)
add(139, "proof of (11.3.10.2), display u: 'u : gr⁰(B)⊗_{gr⁰(A)} gr•(A) → gr•(B)'",
    "two raised bullets", "two ^*", "symbol", None, "high",
    r"\operatorname{gr}^*(A)\longrightarrow\operatorname{gr}^*(B)", r"\operatorname{gr}^\bullet(A)\longrightarrow\operatorname{gr}^\bullet(B)", None)
add(139, "proof of (11.3.10.2), display u: end of the line",
    "no punctuation after gr•(B)", "comma", "punctuation", None, "high",
    r",\\¶v&:", r"\\¶v&:", None)
add(139, "proof of (11.3.10.2), display v: 'v : gr⁰(M)⊗_{gr⁰(A)} gr•(A) → gr•(M)'",
    "two raised bullets", "two ^*", "symbol", None, "high",
    r"\operatorname{gr}^*(A)\longrightarrow\operatorname{gr}^*(M)", r"\operatorname{gr}^\bullet(A)\longrightarrow\operatorname{gr}^\bullet(M)", None)
add(139, "proof of (11.3.10.2), display v: end of the line",
    "no punctuation after gr•(M)", "comma", "punctuation", None, "high",
    r",\\¶w", r"\\¶w", "Listed before the misprint entry of the w line; the two edits do not change the same characters.")
add(139, "proof of (11.3.10.2), display w: 'w : gr⁰(M)⊗_{gr⁰(B)} gr•(B) → gr•(M)', first M",
    "the M of gr⁰(M) is a bold M (wrong fount): 666 dark px, mean stroke run 6.7 px against 470-479 px and 4.6-4.7 px for the M of gr•(M) on the same line and of gr⁰(M) in line v (enlarged crop)",
    "plain M: silently corrected",
    "misprint_in_print", None, "high",
    r"w&:\operatorname{gr}^0(M)", r"w&:\operatorname{gr}^0(\mathbf M)",
    "Wrong-fount letter, reproduced in the diplomatic text as for the bold n of p. 36 (GLOBAL_ISSUES 29). The fix changes only the M.",
    corrected=r"w&:\operatorname{gr}^0(M)")
add(139, "proof of (11.3.10.2), display w: 'gr•(B) → gr•(M)'",
    "two raised bullets", "two ^*", "symbol", None, "high",
    r"\operatorname{gr}^*(B)\longrightarrow\operatorname{gr}^*(M)", r"\operatorname{gr}^\bullet(B)\longrightarrow\operatorname{gr}^\bullet(M)", None)
add(139, "proof of (11.3.10.2), display w: end of the line",
    "no full stop after gr•(M)", "full stop", "punctuation", None, "high",
    r".¶\end{align*}", r"¶\end{align*}", None)
add(139, "diagram (11.3.10.3), top left: 'gr⁰(M)⊗_{gr⁰(A)} gr•(A)'",
    "raised bullet", "^*", "symbol", None, "high",
    r"\operatorname{gr}^*(A)¶ \ar[rr]^v", r"\operatorname{gr}^\bullet(A)¶ \ar[rr]^v", None)
add(139, "diagram (11.3.10.3), top right: 'gr•(M)'",
    "raised bullet", "^*", "symbol", None, "high",
    r"&& \operatorname{gr}^*(M) \\", r"&& \operatorname{gr}^\bullet(M) \\", None)
add(139, "diagram (11.3.10.3), bottom: 'gr⁰(M)⊗_{gr⁰(B)} gr•(B)'",
    "raised bullet", "^*", "symbol", None, "high",
    r"\operatorname{gr}^*(B) \ar[ur]_w", r"\operatorname{gr}^\bullet(B) \ar[ur]_w", None)
add(139, "after diagram (11.3.10.3): 'L'hypothèse c) entraîne que v est bijective'",
    "'L'hypothèse' begins an indented new paragraph", "follows \\end{equation} without a blank line: no indent",
    "other", None, "high",
    r"\end{equation}¶L'hypothèse", r"\end{equation}¶¶L'hypothèse",
    "Paragraph break after a display (GLOBAL_ISSUES 47).")
add(139, "proof of (11.3.10.2) 1°: 'L'hypothèse c) entraîne que v est bijective'",
    "'c)' italic", "upright", "italics", None, "high",
    r"c) entraîne que $v$", r"\emph{c)} entraîne que $v$", None)
add(139, "proof of (11.3.10.2) 1°: 'en vertu de l'hypothèse c), M/JM est'",
    "'c)' italic", "upright", "italics", None, "high",
    r"l'hypothèse c), $M/", r"l'hypothèse \emph{c)}, $M/", None)
add(139, "proof of (11.3.10.2) 2°: 'de la conjonction de c) et d) que M est'",
    "'c)', 'd)' italic", "upright", "italics", None, "high",
    r"conjonction de c) et d) que", r"conjonction de \emph{c)} et \emph{d)} que", None)
add(139, "proof of (11.3.10.2) 2°: 'On a vu dans 1° que l'hypothèse c) entraîne que les trois applications'",
    "'c)' italic", "upright", "italics", None, "high",
    r"l'hypothèse c) entraîne que les trois", r"l'hypothèse \emph{c)} entraîne que les trois", None)
add(139, "proof of (11.3.10.2) 2°: '(Bourbaki, Alg. comm., chap. III, § 5, n° 4, prop. 2)'",
    "n with a raised small o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
    r"n$^\circ$~4, prop.~2)~; on", r"n\textsuperscript{o}~4, prop.~2)~; on",
    "The edition writes n\\textsuperscript{o} elsewhere (GLOBAL_ISSUES 46c, 74).")
add(139, "(11.3.10.4): '(Bourbaki, Alg. comm., chap. III, § 5, n° 4, prop. 2)'",
    "n with a raised small o", "n$^\\circ$", "symbol", None, "medium",
    r"n$^\circ$~4,¶prop.~2). Ceci", r"n\textsuperscript{o}~4,¶prop.~2). Ceci", None)
add(139, "(11.3.10.4), last sentence: 'Ceci achève donc aussi la démonstration de (11.3.7).'",
    "'(11.3.7)' (enlarged crop)", "'(11.3.7)' (the TeX keeps the printed reading)",
    "misprint_in_print", None, "high", None, None,
    "Authors' errata, EGA IV liste 3, (IV, 11.3.10): 'Ligne 9 du bas de la p. 139, remplacer (11.3.7) par (11.3.10)' (this is line 9 from the foot). Diplomatic TeX already right; the corrected edition writes 'démonstration de (11.3.10)'.",
    corrected="(11.3.10)", nofix=True)
add(139, "end of page_139.tex / top of p. 140: 'Remarque (11.3.12): ... M un B-module de présentation finie, J un | idéal de A'",
    "p. 140 continues the sentence ('idéal de A, p un idéal premier ...'); no paragraph break",
    "blank line after '$\\mathfrak J$ un', before \\oldpage[IV-3]{140}",
    "marker", None, "high",
    None, None,
    "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 140 marker itself is in the right place. Already reported by the pp. 140-144 checker (edit '$\\mathfrak J$ un\\n\\n' -> '$\\mathfrak J$ un\\n', filed under page 139, with the blank line after the p. 140 marker) and applied (FIXLOG_CURRENT.jsonl): no second edit here.",
    nofix=True)

# ---------------------------------------------------------------- checks
pages = {}
for p in (135, 136, 137, 138, 139):
    with open(os.path.join(RUN, 'page_%d.tex' % p), encoding='utf-8', newline='') as fh:
        pages[p] = fh.read().replace('\r\n', '\n')  # page files are CRLF; release files LF
ok = True
for i, d in enumerate(F):
    if d['fix'] is None:
        continue
    n = pages[d['page']].count(d['fix']['old'])
    if n != 1:
        ok = False
        print('COUNT %d  #%d p.%d  %r' % (n, i, d['page'], d['fix']['old']))
# sequential application in list order
work = dict(pages)
for i, d in enumerate(F):
    if d['fix'] is None:
        continue
    t = work[d['page']]
    if t.count(d['fix']['old']) != 1:
        ok = False
        print('SEQ FAIL #%d p.%d %r' % (i, d['page'], d['fix']['old']))
        continue
    work[d['page']] = t.replace(d['fix']['old'], d['fix']['new'], 1)
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
from collections import Counter
c = Counter()
for d in F:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    c[(d['page'], k)] += 1
for p in (135, 136, 137, 138, 139):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('total', len(F), 'checks ok' if ok else 'CHECKS FAILED')
for p in (137, 139):
    sys.stdout.reconfigure(encoding='utf-8')
