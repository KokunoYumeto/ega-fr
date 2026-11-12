import json
import os

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = os.path.join(RUN, "findings_170_174.json")
N = "\n"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 170 ----------------
L.append(F(170, "subsection heading 11.10",
           "'11.10. Familles schématiquement dominantes de morphismes et familles schématiquement denses de sous-préschémas.' (final full stop)",
           r"\subsection{... de sous-préschémas} (no full stop)",
           "punctuation", None, "high",
           r"denses de sous-préschémas}", r"denses de sous-préschémas.}",
           "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))
L.append(F(170, "Proposition (11.10.1) a): '(autrement dit (11.9.1), l'intersection des noyaux des θ_λ est nulle).'",
           "the parenthesis is roman, only 'nulle' is italic (crop p170_a.png)",
           "the whole parenthesis italic (proposition environment)",
           "convention", 6, "high",
           r"séparante (autrement dit (11.9.1), l'intersection des noyaux des" + N + r"  $\theta_\lambda$ est nulle).",
           r"séparante \textup{(autrement dit (11.9.1), l'intersection des noyaux des" + N + r"  $\theta_\lambda$ est} nulle\textup{)}.",
           None))
L.append(F(170, "Proposition (11.10.1) b), first line: 'Pour tout ouvert U de X, toute section t'",
           "the final t of 'ouvert' is a bold italic sort (wrong font); ink area 243 px against 139-153 px for the t's of 'tout', 'toute', 'section' on the same line (crops p170_ouvert.png, p170_ouvert4.png)",
           "ouvert (ordinary italic t): silent correction",
           "misprint_in_print", None, "high",
           r"ouvert $U$ de $X$, toute", r"ouver\textbf{t} $U$ de $X$, toute",
           "Wrong-font letter, reproduced in the diplomatic text as the other wrong-font sorts (GLOBAL_ISSUES 29); \\textbf in the italic statement gives the bold italic t. The corrected reading is the ordinary 'ouvert'.",
           corrected=r"ouvert $U$ de $X$, toute"))
L.append(F(170, "Proposition (11.10.1) c): '(où j est l'injection canonique)'",
           "the parenthesis is roman inside the italic statement; ', on a Y=U.' italic again (crop p170_c_end.png)",
           "italic (proposition environment)",
           "convention", 6, "high",
           r"(où $j$ est" + N + r"  l'injection canonique)",
           r"\textup{(où $j$ est" + N + r"  l'injection canonique)}",
           None))
L.append(F(170, "proof of (11.10.1), l. 1: 'L'équivalence de a) et b) résulte des définitions.'",
           "'a)' and 'b)' italic, parentheses included",
           "upright",
           "italics", None, "high",
           r"L'équivalence de a) et b) résulte", r"L'équivalence de \emph{a)} et \emph{b)} résulte",
           None))
L.append(F(170, "proof of (11.10.1), l. 1-2: 'Pour voir que b) entraîne c), il suffit'",
           "'b)' and 'c)' italic",
           "upright",
           "italics", None, "high",
           r"Pour voir que b) entraîne" + N + r"c), il suffit",
           r"Pour voir que \emph{b)} entraîne" + N + r"\emph{c)}, il suffit",
           None))
L.append(F(170, "proof of (11.10.1): 'donc, en vertu de b), J=0 et Y=U'",
           "'b)' italic",
           "upright",
           "italics", None, "high",
           r"en vertu de b), $\mathcal J=0$", r"en vertu de \emph{b)}, $\mathcal J=0$",
           None))
L.append(F(170, "proof of (11.10.1): 'Inversement, si c) est vérifiée'",
           "'c)' italic",
           "upright",
           "italics", None, "high",
           r"si c) est vérifiée", r"si \emph{c)} est vérifiée",
           None))
L.append(F(170, "proof of (11.10.1): 'il suffit, pour prouver b), d'appliquer c) au sous-préschéma fermé Y de U défini par'",
           "'b)' and 'c)' italic",
           "upright",
           "italics", None, "high",
           r"pour prouver b), d'appliquer c) au", r"pour prouver \emph{b)}, d'appliquer \emph{c)} au",
           None))
L.append(F(170, "proof of (11.10.1): 'Pour prouver que c) entraîne d), il suffit d'appliquer c) au sous-préschéma fermé Y de U, image'",
           "'c)', 'd)', 'c)' italic",
           "upright",
           "italics", None, "high",
           r"Pour prouver que c)" + N + r"entraîne d), il suffit d'appliquer c) au",
           r"Pour prouver que \emph{c)}" + N + r"entraîne \emph{d)}, il suffit d'appliquer \emph{c)} au",
           None))
L.append(F(170, "proof of (11.10.1): 'Inversement, on déduit b) de d) en considérant'",
           "'b)' and 'd)' italic",
           "upright",
           "italics", None, "high",
           r"on déduit b) de d) en", r"on déduit \emph{b)} de \emph{d)} en",
           None))

# ---------------- page 171 ----------------
L.append(F(171, "Définition (11.10.2), l. 1: 'Lorsque les conditions équivalentes de (11.10.1) sont vérifiées'",
           "(11.10.1) upright inside the italic statement (crop p171_def.png)",
           "italic (definition environment)",
           "convention", 6, "high",
           r"de (11.10.1) sont", r"de \textup{(11.10.1)} sont",
           None))
L.append(F(171, "Définition (11.10.2): 'on dit que la famille (f_λ) est schématiquement dominante.'",
           "the defined term is in the same italic as the statement (no change of face)",
           r"\emph{schématiquement dominante} inside the italic definition environment: upright",
           "convention", 6, "high",
           r"\emph{schématiquement dominante}", r"schématiquement dominante",
           "Drop \\emph inside the italic environment (FIX_POLICY 2.6)."))
L.append(F(171, "Définition (11.10.2), end: 'on dit aussi que la famille (Z_λ) est schématiquement dense.'",
           "the defined term is in the same italic as the statement",
           r"\emph{schématiquement dense} inside the italic definition environment: upright",
           "convention", 6, "high",
           r"\emph{schématiquement dense}", r"schématiquement dense",
           None))
L.append(F(171, "Remarques (11.10.3) (i): 'comme il résulte par exemple de la forme b) dans (11.10.1)'",
           "'b)' italic in the roman remark (crop p171_formeb.png)",
           "plain b) (italic now only because the remark environment is italic)",
           "italics", None, "high",
           r"la forme b) dans", r"la forme \emph{b)} dans",
           "Judged with the remark body roman (document-wide remark item)."))
L.append(F(171, "Remarques (11.10.3) (i): 'de chacune des familles formée des morphismes f_λ^{-1}(W_α)→W_α'",
           "'formée' (singular, no final s; crops p171_formee_zoom.png, p171_formee_zoom2.png)",
           "'formées': silent correction",
           "misprint_in_print", None, "medium",
           r"familles formées des", r"familles formée des",
           "The participle qualifies 'familles', so 'formées' is the expected form; agreement with 'chacune' would make 'formée' defensible, hence medium. If it is not treated as a misprint, apply the same edit as a plain word fix.",
           corrected=r"familles formées des"))
L.append(F(171, "Remarques (11.10.3) (i), end: 'f_λ^{-1}(W_α)→W_α restrictions des f_λ.'",
           "no comma after W_α at the end of the line (crop p171_Walpha_zoom.png)",
           "'W_\\alpha$, restrictions': silent correction",
           "misprint_in_print", None, "medium",
           r"W_\alpha$, restrictions", r"W_\alpha$ restrictions",
           "The apposition takes a comma elsewhere (p. 170, d): 'f_λ^{-1}(U)→U, restriction de f_λ,'); medium because the omission could be the authors' own punctuation.",
           corrected=r"W_\alpha$, restrictions"))
L.append(F(171, "Remarques (11.10.3) (iv): 'signifie que l'image fermée de Z par f (I, 9.5.3)'",
           "\"l'\" upright, only 'image fermée de Z par f' italic (crop p171_limage.png)",
           r"\emph{l'image fermée de $Z$ par $f$}: the elision is inside the italic",
           "italics", None, "high",
           r"\emph{l'image fermée de $Z$ par $f$}", r"l'\emph{image fermée de $Z$ par $f$}",
           "Judged with the remark body roman."))
L.append(F(171, "Remarques (11.10.3) (iv), end: '(I, 9.5.3) est identique à X.'",
           "'est' italic like 'identique à' (crop p171_estid.png)",
           r"'est' outside \emph (roman)",
           "italics", None, "high",
           r"9.5.3) est" + N + r"  \emph{identique à $X$}",
           r"9.5.3) \emph{est" + N + r"  identique à $X$}",
           "Judged with the remark body roman."))
L.append(F(171, "Proposition (11.10.4): 'et si de plus X est réduit, la famille'",
           "'réduit' roman (upright) inside the italic statement (crop p171_s2_prop.png)",
           "italic (proposition environment)",
           "convention", 6, "high",
           r"de plus $X$ est réduit,", r"de plus $X$ est \textup{réduit},",
           None))
L.append(F(171, "proof of (11.10.4), l. 1: 'résulte aussitôt de (11.10.1, b))'",
           "'b)' italic, the outer parenthesis upright",
           "upright",
           "italics", None, "high",
           r"(11.10.1, b))", r"(11.10.1, \emph{b)})",
           None))
L.append(F(171, "proof of (11.10.4): 'on a aussi des factorisations (f_λ^{-1}(U))_red -> Y_red -> U, et l'hypothèse'",
           "the factorisation is set in the running text, followed by a comma (crop p171_factor.png)",
           "a displayed formula \\[ ... \\]",
           "other", None, "high",
           N.join([r"aussi des factorisations", r"\[", r"(f_\lambda^{-1}(U))_{\mathrm{red}}",
                   r"\xrightarrow{(g_\lambda)_{\mathrm{red}}}Y_{\mathrm{red}}",
                   r"\xrightarrow{j_{\mathrm{red}}}U,", r"\]"]),
           N.join([r"aussi des factorisations", r"$(f_\lambda^{-1}(U))_{\mathrm{red}}",
                   r"\xrightarrow{(g_\lambda)_{\mathrm{red}}}Y_{\mathrm{red}}",
                   r"\xrightarrow{j_{\mathrm{red}}}U$,"]),
           "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting words lost."))
L.append(F(171, "'Les résultats du n° 11.9 sur les familles séparantes'",
           "n with a raised letter o (crop p171_no.png)",
           "n$^\\circ$ (degree ring)",
           "symbol", None, "high",
           r"n$^\circ$~11.9", r"n\textsuperscript{o}~11.9",
           "The edition's form is n\\textsuperscript{o} (as IV-3 pp. 79, 121-128)."))
L.append(F(171, "Théorème (11.10.5): item labels (i), (ii)",
           "labels (i) and (ii) upright before the italic items",
           "label=(\\roman*) inside the italic theorem environment: italic labels",
           "convention", 6, "high",
           r"\begin{enumerate}[label=(\roman*)]" + N + r"  \item Si $g$",
           r"\begin{enumerate}[label=\textup{(\roman*)}]" + N + r"  \item Si $g$",
           "One edit of the label option covers (i) and (ii) (GLOBAL_ISSUES 16). The other label=(\\roman*) on this page belongs to Remarques (11.10.3) (remark-font item)."))
L.append(F(171, "Théorème (11.10.5) (ii): 'et en outre que l'une des conditions suivantes soit vérifiée'",
           "\"l'une\" roman (upright) inside the italic statement (crop p171_lune.png)",
           "italic (theorem environment)",
           "convention", 6, "high",
           r"en outre que l'une des", r"en outre que \textup{l'une} des",
           None))
L.append(F(171, "Théorème (11.10.5) (ii), after a), b): 'Alors, si la famille (f_λ) est schématiquement dominante, il en est de même de la famille (f'_λ).'",
           "'Alors' begins an indented new paragraph after the list a), b)",
           "follows the inner \\end{enumerate} without a blank line: set as a continuation, no indent",
           "other", None, "medium",
           r"  \end{enumerate}" + N + r"  Alors, si la famille",
           r"  \end{enumerate}" + N + N + r"  Alors, si la famille",
           "GLOBAL_ISSUES 80. The paragraph lies inside item (ii) of the outer list, where the indent depends on \\listparindent."))

# ---------------- page 172 ----------------
L.append(F(172, "Proposition (11.10.6), l. 1: 'Les notations étant celles de (11.10.5), supposons'",
           "(11.10.5) upright inside the italic statement",
           "italic (proposition environment)",
           "convention", 6, "high",
           r"(11.10.5), supposons que $X$ soit un préschéma",
           r"\textup{(11.10.5)}, supposons que $X$ soit un préschéma",
           None))
L.append(F(172, "proof of (11.10.7), l. 1: 'les morphismes f_λ se factorisent en f_λ : Z_λ -g_λ-> Y -j-> X, où j est'",
           "the factorisation is in the running text and begins with 'f_λ :' (crop p172_factor1.png)",
           "displayed \\[ Z_\\lambda\\xrightarrow{g_\\lambda}Y\\xrightarrow{j}X, \\] without 'f_\\lambda:'",
           "missing", None, "high",
           N.join([r"en", r"\[", r"Z_\lambda\xrightarrow{g_\lambda}Y\xrightarrow{j}X,", r"\]"]),
           r"en $f_\lambda:Z_\lambda\xrightarrow{g_\lambda}Y\xrightarrow{j}X$,",
           "One edit restores the printed 'f_λ :' and sets the formula inline as printed (GLOBAL_ISSUES 21)."))
L.append(F(172, "proof of (11.10.7): 'de sorte que f'_λ se factorise en Z'_λ -g'_λ-> Y'_1 -j'-> X', où j' est l'injection canonique'",
           "the factorisation is in the running text (crop p172_factor2.png)",
           "a displayed formula \\[ ... \\]",
           "other", None, "high",
           N.join([r"\[", r"Z'_\lambda\xrightarrow{g'_\lambda}Y'_1\xrightarrow{j'}X',", r"\]"]),
           r"$Z'_\lambda\xrightarrow{g'_\lambda}Y'_1\xrightarrow{j'}X'$,",
           "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting words lost."))
L.append(F(172, "Définition (11.10.8), l. 1: 'Les notations étant celles de (11.10.5), supposons'",
           "(11.10.5) upright inside the italic statement (crop p172_def.png)",
           "italic (definition environment)",
           "convention", 6, "high",
           r"(11.10.5), supposons que $X$ soit un" + N + r"$S$-préschéma. On dit",
           r"\textup{(11.10.5)}, supposons que $X$ soit un" + N + r"$S$-préschéma. On dit",
           None))
L.append(F(172, "Définition (11.10.8): 'On dit que (f_λ) est universellement schématiquement dominante (relativement à S)'",
           "the defined term is in the same italic as the statement",
           r"\emph{universellement schématiquement dominante} inside the italic definition environment: upright",
           "convention", 6, "high",
           r"\emph{universellement" + N + r"schématiquement dominante}",
           r"universellement" + N + r"schématiquement dominante",
           "Drop \\emph inside the italic environment (FIX_POLICY 2.6)."))
L.append(F(172, "Théorème (11.10.9), l. 1: 'Les notations étant celles de (11.10.5), supposons'",
           "(11.10.5) upright inside the italic statement",
           "italic (theorem environment)",
           "convention", 6, "high",
           r"(11.10.5), supposons que $X$ soit un" + N + r"$S$-préschéma localement",
           r"\textup{(11.10.5)}, supposons que $X$ soit un" + N + r"$S$-préschéma localement",
           None))
L.append(F(172, "Théorème (11.10.9): 'X_s = X ×_S Spec(k(s))'",
           "bold italic k in k(s) (crop p172_ks.png)",
           "plain k(s)",
           "convention", 1, "high",
           r"X_s=X\times_S\operatorname{Spec}(k(s))", r"X_s=X\times_S\operatorname{Spec}(\boldsymbol{k}(s))",
           None))
L.append(F(172, "Théorème (11.10.9): '(Z_λ)_s = Z_λ ×_S Spec(k(s))'",
           "bold italic k in k(s)",
           "plain k(s)",
           "convention", 1, "high",
           r"Z_\lambda\times_S\operatorname{Spec}(k(s))", r"Z_\lambda\times_S\operatorname{Spec}(\boldsymbol{k}(s))",
           None))

# ---------------- page 173 ----------------
L.append(F(173, "subsection heading 12.0",
           "'12.0. Introduction.' (final full stop)",
           r"\subsection{Introduction} (no full stop)",
           "punctuation", None, "high",
           r"\subsection{Introduction}", r"\subsection{Introduction.}",
           "GLOBAL_ISSUES 43/58; same fix as heading 8.1 on p. 5."))
L.append(F(173, "(12.0.1), l. 1: 'Étant donné un morphisme localement de présentation finie f : X→Y'",
           "'localement de présentation finie' italic (crop p173_s1end.png)",
           "roman (env body)",
           "italics", None, "high",
           r"un morphisme localement de présentation finie $f:X\to Y$",
           r"un morphisme \emph{localement de présentation finie} $f:X\to Y$",
           None))
L.append(F(173, "(12.0.1): 'pour certaines propriétés locales P de préschémas'",
           "'locales' italic",
           "roman",
           "italics", None, "high",
           r"certaines propriétés locales", r"certaines propriétés \emph{locales}",
           None))
L.append(F(173, "(12.0.1): 'propriétés locales P de préschémas'",
           "bold italic P",
           r"\mathbf P (bold upright)",
           "convention", 10, "high",
           r"$\mathbf P$ de préschémas", r"$\boldsymbol{P}$ de préschémas",
           None))
L.append(F(173, "(12.0.1): 'tels que la propriété P ait lieu, pour la fibre'",
           "bold italic P",
           r"\mathbf P",
           "convention", 10, "high",
           r"$\mathbf P$ ait lieu,", r"$\boldsymbol{P}$ ait lieu,",
           None))
L.append(F(173, "(12.0.1): 'pour la fibre X_{f(x)}, au point x de cette fibre'",
           "the first 'fibre' italic, the second ('de cette fibre') roman (crop p173_s2a.png)",
           "roman",
           "italics", None, "high",
           r"la fibre $X_{f(x)}$", r"la \emph{fibre} $X_{f(x)}$",
           None))
L.append(F(173, "(12.0.1): 'est localement constructible dans X'",
           "'localement constructible dans' italic",
           "roman",
           "italics", None, "high",
           r"localement constructible dans $X$", r"\emph{localement constructible dans} $X$",
           None))
L.append(F(173, "(12.0.1): 'le morphisme f est plat, alors'",
           "'plat' italic",
           "roman",
           "italics", None, "high",
           r"est plat, alors", r"est \emph{plat}, alors",
           None))
L.append(F(173, "(12.0.1): 'l'ensemble E est même ouvert dans X'",
           "'ouvert dans' italic",
           "roman",
           "italics", None, "high",
           r"même ouvert dans $X$", r"même \emph{ouvert dans} $X$",
           None))
L.append(F(173, "(12.0.1): 'nous avons montré que si f est de présentation finie,'",
           "'de présentation finie' italic (crop p173_s2b.png)",
           "roman",
           "italics", None, "high",
           r"$f$ est de présentation finie,", r"$f$ est \emph{de présentation finie},",
           None))
L.append(F(173, "(12.0.1): 'et si cette fois P désigne'",
           "bold italic P",
           r"\mathbf P",
           "convention", 10, "high",
           r"$\mathbf P$ désigne", r"$\boldsymbol{P}$ désigne",
           None))
L.append(F(173, "(12.0.1): 'certaines propriétés globales de préschémas'",
           "'globales' italic",
           "roman",
           "italics", None, "high",
           r"propriétés globales", r"propriétés \emph{globales}",
           None))
L.append(F(173, "(12.0.1): 'tels que la propriété P ait lieu pour la fibre X_y'",
           "bold italic P",
           r"\mathbf P",
           "convention", 10, "high",
           r"$\mathbf P$ ait lieu pour", r"$\boldsymbol{P}$ ait lieu pour",
           None))
L.append(F(173, "(12.0.1): 'est localement constructible dans Y'",
           "'localement constructible dans' italic",
           "roman",
           "italics", None, "high",
           r"localement constructible dans $Y$", r"\emph{localement constructible dans} $Y$",
           None))
L.append(F(173, "(12.0.1): 'le morphisme f est propre et plat,'",
           "'propre' and 'plat' italic, 'et' roman",
           "roman",
           "italics", None, "high",
           r"est propre et plat,", r"est \emph{propre} et \emph{plat},",
           None))
L.append(F(173, "(12.0.1), end: 'F est même ouvert dans Y.'",
           "'ouvert dans' italic",
           "roman",
           "italics", None, "high",
           r"même ouvert dans $Y$", r"même \emph{ouvert dans} $Y$",
           None))
L.append(F(173, "(12.0.2): 'au cas où Y est affine et X de présentation finie'",
           "'affine' italic",
           "roman",
           "italics", None, "high",
           r"est affine et", r"est \emph{affine} et",
           None))
L.append(F(173, "(12.0.2): labels A), B), C)",
           "the labels are upright (crops p173_Alaide.png, p173_B.png, p173_C.png)",
           "label=\\emph{\\Alph*)} in the roman env: italic labels",
           "italics", None, "high",
           r"\begin{enumerate}[label=\emph{\Alph*)}]", r"\begin{enumerate}[label=\Alph*)]",
           "One edit covers A), B) and C)."))
L.append(F(173, "(12.0.2) A): 'A l'aide de (8.9.1)'",
           "capital A without the grave accent (crop p173_Alaide.png)",
           "À l'aide",
           "word", None, "high",
           r"À l'aide", r"A l'aide",
           "As the page fixes for IV-3 p. 116, EGA II pp. 17, 29, 0_III p. 27."))
L.append(F(173, "(12.0.2) A), end: 'on se ramène au cas où X et Y sont noethériens.'",
           "'noethériens' italic",
           "roman",
           "italics", None, "high",
           r"sont noethériens.", r"sont \emph{noethériens}.",
           None))
L.append(F(173, "(12.0.2) B), end: 'prouvant que E (resp. F) est constructible.'",
           "'constructible' italic",
           "roman",
           "italics", None, "high",
           r"est constructible.", r"est \emph{constructible}.",
           None))
L.append(F(173, "(12.0.2) C): 'alors toute générisation x' de x appartient aussi à E'",
           "'générisation' italic (the later 'pour une générisation x'_1' is roman)",
           "roman",
           "italics", None, "high",
           r"alors toute" + N + r"  générisation $x'$", r"alors toute" + N + r"  \emph{générisation} $x'$",
           None))
L.append(F(173, "(12.0.2) C): 'on voit, puisque Y est noethérien, qu'il existe'",
           "'noethérien' italic",
           "roman",
           "italics", None, "high",
           r"$Y$ est noethérien,", r"$Y$ est \emph{noethérien},",
           None))
L.append(F(173, "(12.0.2) C): 'un spectre d'anneau de valuation discrète Y_1'",
           "'anneau de valuation discrète' italic, \"d'\" roman",
           "roman",
           "italics", None, "high",
           r"spectre d'anneau" + N + r"  de valuation discrète $Y_1$",
           r"spectre d'\emph{anneau" + N + r"  de valuation discrète} $Y_1$",
           None))
L.append(F(173, "(12.0.2) C): 'et que t est M-régulier (ce qui résulte'",
           "'régulier' italic",
           "roman",
           "italics", None, "high",
           r"$M$-régulier", r"$M$-\emph{régulier}",
           None))

# ---------------- page 174 ----------------
L.append(F(174, "subsection heading 12.1",
           "'12.1. Propriétés locales des fibres d'un morphisme plat localement de présentation finie.' (final full stop)",
           r"\subsection{...} (no full stop)",
           "punctuation", None, "high",
           r"localement de" + N + r"présentation finie}", r"localement de" + N + r"présentation finie.}",
           "GLOBAL_ISSUES 43/58."))
L.append(F(174, "Théorème (12.1.1): item labels (i) to (viii)",
           "the eight labels are upright before the italic items",
           "label=(\\roman*) inside the italic theorem environment: italic labels",
           "convention", 6, "high",
           r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
           "One edit covers (i)-(viii) (GLOBAL_ISSUES 16)."))
L.append(F(174, "Théorème (12.1.1) (iv): 'soit équidimensionnel au point x'",
           "'équidimensionnel' roman (upright) inside the italic statement (crop p174_iv_v.png)",
           "italic (theorem environment)",
           "convention", 6, "high",
           r"équidimensionnel", r"\textup{équidimensionnel}",
           None))
L.append(F(174, "Théorème (12.1.1) (iv), end: '(5.7.2)'",
           "reference upright inside the italic statement",
           "italic",
           "convention", 6, "high",
           r"(5.7.2)", r"\textup{(5.7.2)}",
           None))
L.append(F(174, "Théorème (12.1.1) (v): '(0, 16.4.9)'",
           "reference upright (bold 0) inside the italic statement",
           "parentheses and numbers italic",
           "convention", 6, "high",
           r"($\mathbf 0$, 16.4.9)", r"\textup{($\mathbf 0$, 16.4.9)}",
           None))
L.append(F(174, "Théorème (12.1.1) (vi), end: '(5.7.1)'",
           "reference upright inside the italic statement (crop p174_vi_viii.png)",
           "italic",
           "convention", 6, "high",
           r"(5.7.1)", r"\textup{(5.7.1)}",
           None))
L.append(F(174, "Théorème (12.1.1) (vii), end: '(4.6.22)'",
           "reference upright inside the italic statement",
           "italic",
           "convention", 6, "high",
           r"réduit au point $x$ (4.6.22)", r"réduit au point $x$ \textup{(4.6.22)}",
           None))
L.append(F(174, "Théorème (12.1.1) (viii), end: '(4.6.22)'",
           "reference upright inside the italic statement",
           "italic",
           "convention", 6, "high",
           r"intègre au point $x$ (4.6.22)", r"intègre au point $x$ \textup{(4.6.22)}",
           None))
L.append(F(174, "proof of (12.1.1): 'on peut supposer que F_0 est Y_0-plat'",
           "'plat' italic",
           "roman",
           "italics", None, "high",
           r"$Y_0$-plat", r"$Y_0$-\emph{plat}",
           None))
L.append(F(174, "proof of (12.1.1), 2nd paragraph: 'au cas où A et B sont noethériens, f de type fini'",
           "'noethériens' italic",
           "roman",
           "italics", None, "high",
           r"sont noethériens,", r"sont \emph{noethériens},",
           None))
L.append(F(174, "proof of (12.1.1): 'on sait que l'ensemble E est constructible pour toutes les propriétés'",
           "'constructible' italic",
           "roman",
           "italics", None, "high",
           r"est constructible pour", r"est \emph{constructible} pour",
           None))
L.append(F(174, "proof of (12.1.1): 'où l'on doit prouver que E est stable par générisation.'",
           "'stable par générisation' italic",
           "roman",
           "italics", None, "high",
           r"stable par générisation.", r"\emph{stable par générisation}.",
           None))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
print(len(L), "findings written to", OUT)
