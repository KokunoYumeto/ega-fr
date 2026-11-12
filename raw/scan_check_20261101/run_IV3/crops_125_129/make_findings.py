"""Builds findings_125_129.json (EGA IV-3 pp. 125-129) and checks every fix's old string.

Strings use '⏎' for a line break (LF), so that LaTeX backslashes can stay in raw strings."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_125_129.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")

F = []


def nl(s):
    return None if s is None else s.replace("⏎", "\n")


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note=None, corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=nl(old), new=nl(new)))
    if kind == "misprint_in_print":
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


BUL = "Raised bullet in the print (gr•, as on all pages of 11.2.9); the TeX writes ^* (asterisk)."

# ---------------------------------------------------------------- p. 125
add(125, "proof of (11.2.6), I), after 'on a par suite': (M_λ)_𝔭λ = (M_ξ⊗_{C_λ}A_λ)_𝔭λ = ((M_ξ)_𝔭ξ⊗_{C_λ}A_λ)_𝔭λ, donc",
    "formula set inline in the running text: 'on a par suite (M_λ)_𝔭λ=(M_ξ⊗A_λ)_𝔭λ=((M_ξ)_𝔭ξ⊗A_λ)_𝔭λ, donc (M_λ)_𝔭λ est un A_λ-module'",
    "displayed with \\[ ... \\] (comma inside the display)", "formula",
    r"on a par suite⏎\[⏎(M_\lambda)_{\mathfrak p_\lambda}⏎=(M_\xi\otimes_{C_\lambda}A_\lambda)_{\mathfrak p_\lambda}⏎=((M_\xi)_{\mathfrak p_\xi}\otimes_{C_\lambda}A_\lambda)_{\mathfrak p_\lambda},⏎\]⏎donc",
    r"on a par suite⏎$(M_\lambda)_{\mathfrak p_\lambda}⏎=(M_\xi\otimes_{C_\lambda}A_\lambda)_{\mathfrak p_\lambda}⏎=((M_\xi)_{\mathfrak p_\xi}\otimes_{C_\lambda}A_\lambda)_{\mathfrak p_\lambda}$,⏎donc",
    note="Display vs inline; no connecting word lost or added.")
add(125, "end of I): 'Nous pouvons donc par la suite supposer les A_λ noethériens pour λ∈L'",
    "'noethériens' italic (crop p125_s1_II_noeth.png)", "upright", "italics",
    r"noethériens pour $\lambda\in L$", r"\emph{noethériens} pour $\lambda\in L$")
add(125, "proof of (11.2.6): label 'II)'",
    "'II)' in ordinary roman: stems 6 px, as the roman I of 'Il' (6-7 px); the bold I of '(I, 3.6.5)' on the same page is 10 px",
    "\\textbf{II)} (bold)", "font",
    r"\noindent\textbf{II)}", r"\noindent II)",
    note="All proof-part labels I)-V) of ega4-11 are \\textbf (see the final message); GLOBAL_ISSUES 51/76: printed upright, not bold.")
add(125, "heading II): 'Réduction de l'énoncé global (ii) à l'énoncé ponctuel (i).'",
    "only the words are italic: '(ii)', '(i)' and the full stop are upright (crop p125_s1_II_zoom.png)",
    "the whole heading inside \\emph, so (ii) and (i) come out italic", "italics",
    r"\emph{Réduction de l'énoncé global (ii) à l'énoncé⏎ponctuel (i).}",
    r"\emph{Réduction de l'énoncé global} (ii) \emph{à l'énoncé⏎ponctuel} (i).")
add(125, "proof of (11.2.6): label 'III)'",
    "'III)' in ordinary roman (stems 6-7 px, crop p125_s2_III_wide.png)", "\\textbf{III)} (bold)", "font",
    r"\noindent\textbf{III)}", r"\noindent III)")
add(125, "III): 'ce qui s'écrit aussi, puisque les Tor_i^A(A/𝔪_0A, M) sont des B-modules'",
    "Tor with subscript italic i (crop p125_s2_Tori.png)", "\\operatorname{Tor}_1^A", "formula",
    r"puisque les $\operatorname{Tor}_1^A(A/\mathfrak m_0A,M)$",
    r"puisque les $\operatorname{Tor}_i^A(A/\mathfrak m_0A,M)$",
    note="Not a misprint: the plural sentence is about all the Tor_i; the formula after it, (Tor_1^A(A/𝔪_0A, M))_𝔭=0, has subscript 1 in both.")
add(125, "III): 'est un B_0-module de type fini, car on peut le définir'",
    "'module de type fini' all italic: 'B_0-module de type fini' (crop p125_s2_module.png)",
    "only 'de type fini' in \\emph", "italics",
    r"$B_0$-module \emph{de type fini}", r"$B_0$-\emph{module de type fini}")
add(125, "III): 'il existe un h∈B—𝔭 tel que ht_i=0'", "long dash B—𝔭", "minus sign", "convention",
    r"$h\in B-\mathfrak p$", r"$h\in B\setmin\mathfrak p$", conv=7)
add(125, "III): 'Or, on a (11.2.2.1) Tor_1^A(A/𝔪_0A, M)=lim→ Tor_1^{A_λ}(A_λ/𝔪_0A_λ, M_λ); il existe donc'",
    "formula set inline in the running text", "displayed with \\[ ... \\] (with '~;' inside)", "formula",
    r"on a (11.2.2.1)⏎\[⏎\operatorname{Tor}_1^A(A/\mathfrak m_0A,M)=⏎\varinjlim\operatorname{Tor}_1^{A_\lambda}⏎(A_\lambda/\mathfrak m_0A_\lambda,M_\lambda)~;⏎\]⏎il existe donc",
    r"on a (11.2.2.1)⏎$\operatorname{Tor}_1^A(A/\mathfrak m_0A,M)=⏎\varinjlim\operatorname{Tor}_1^{A_\lambda}⏎(A_\lambda/\mathfrak m_0A_\lambda,M_\lambda)$~;⏎il existe donc",
    note="Display vs inline; no connecting word lost or added.")
add(125, "III): 'on a h_λ∈B_λ—𝔭_λ, donc'", "long dash B_λ—𝔭_λ", "minus sign", "convention",
    r"$h_\lambda\in B_\lambda-\mathfrak p_\lambda$", r"$h_\lambda\in B_\lambda\setmin\mathfrak p_\lambda$", conv=7)
add(125, "Corollaire (11.2.7) a), end: '(resp. f-plat)'",
    "'resp.' upright inside the italic statement", "italic (corollary environment)", "convention",
    r"point $x$ (resp. $f$-plat)", r"point $x$ (\textup{resp.} $f$-plat)", conv=6)

# ---------------------------------------------------------------- p. 126
add(126, "(11.2.7) b), l. 1: 'Il existe un schéma affine noethérien S_0=Spec(A_0)'",
    "'noethérien' roman (upright) inside the italic statement (crop p126_s1_noeth.png)",
    "italic (corollary environment)", "convention",
    r"affine noethérien $S_0", r"affine \textup{noethérien} $S_0", conv=6)
add(126, "(11.2.7) b), end: '(resp. f_0-plat)'", "'resp.' upright", "italic", "convention",
    r"(resp.⏎$f_0$-plat)", r"(\textup{resp.}⏎$f_0$-plat)", conv=6)
add(126, "(11.2.7) c): 'Les conditions de b) sont vérifiées'",
    "'b)' upright inside the italic statement (crop p126_s1_c_b.png)", "italic", "convention",
    r"Les conditions de b) sont", r"Les conditions de \textup{b)} sont", conv=6)
add(126, "proof of (11.2.7): 'Il est clair que c) implique b) et b) implique a)'",
    "c), b), b), a) italic, parentheses included (crop p126_s1_cba.png)", "upright", "italics",
    r"Il est clair que c) implique b) et b) implique a)",
    r"Il est clair que \emph{c)} implique \emph{b)} et \emph{b)} implique \emph{a)}")
add(126, "proof of (11.2.7), end: 'vérifie les conditions de c).'",
    "'c)' italic (crop p126_s2_c.png)", "upright", "italics",
    r"conditions de c).", r"conditions de \emph{c)}.")
add(126, "Proposition (11.2.8): 'X_s=g^{-1}(s)=X×_S Spec(k(s))'", "bold italic k", "plain k", "convention",
    r"X\times_S\operatorname{Spec}(k(s))", r"X\times_S\operatorname{Spec}(\boldsymbol{k}(s))", conv=1)
add(126, "Proposition (11.2.8): 'Y_s=h^{-1}(s)=Y×_S Spec(k(s))'", "bold italic k", "plain k", "convention",
    r"Y\times_S\operatorname{Spec}(k(s))", r"Y\times_S\operatorname{Spec}(\boldsymbol{k}(s))", conv=1)
add(126, "Proposition (11.2.8): 'ℱ_s=ℱ⊗_{𝒪_S}k(s)'", "bold italic k", "plain k", "convention",
    r"\mathcal F\otimes_{\mathcal O_S}k(s)", r"\mathcal F\otimes_{\mathcal O_S}\boldsymbol{k}(s)", conv=1)
add(126, "proof of (11.2.8): 'que E ou S—E est un voisinage'", "long dash S—E", "minus sign", "convention",
    r"$E$ ou $S-E$", r"$E$ ou $S\setmin E$", conv=7)
add(126, "proof of (11.2.8): 'Si η∈S—E, cela résulte'", "long dash S—E", "minus sign", "convention",
    r"$\eta\in S-E$", r"$\eta\in S\setmin E$", conv=7)
add(126, "proof of (11.2.8): 'appliqué suivant la méthode de (8.1.2, a))'",
    "'a)' italic, the outer parenthesis upright (crop p126_s3_a.png)", "upright", "italics",
    r"(8.1.2, a))", r"(8.1.2, \emph{a)})")
add(126, "Théorème (11.2.9): 'Pour que gr•_𝔍(M) soit un A-module plat'", "gr with a raised bullet", "gr^*", "symbol",
    r"$\operatorname{gr}_{\mathfrak J}^*(M)$ soit un $A$-module plat",
    r"$\operatorname{gr}_{\mathfrak J}^\bullet(M)$ soit un $A$-module plat", note=BUL)
add(126, "Théorème (11.2.9): 'qu'il existe λ tel que gr•_{𝔍_λ}(M_λ) soit un A_λ-module plat'", "gr•", "gr^*", "symbol",
    r"$\operatorname{gr}_{\mathfrak J_\lambda}^*(M_\lambda)$ soit un",
    r"$\operatorname{gr}_{\mathfrak J_\lambda}^\bullet(M_\lambda)$ soit un")
add(126, "(11.2.9.1), first line: gr•_{𝔍_λ}(M_λ)⊗_{A_λ}A → gr•_𝔍(M)", "gr• twice", "gr^* twice", "symbol",
    r"\operatorname{gr}_{\mathfrak J_\lambda}^*(M_\lambda)⏎  \otimes_{A_\lambda}A&\longrightarrow⏎  \operatorname{gr}_{\mathfrak J}^*",
    r"\operatorname{gr}_{\mathfrak J_\lambda}^\bullet(M_\lambda)⏎  \otimes_{A_\lambda}A&\longrightarrow⏎  \operatorname{gr}_{\mathfrak J}^\bullet")
add(126, "(11.2.9.1), end of the first line: '→ gr•_𝔍(M)'", "no comma after gr•_𝔍(M) (crop p126_s4_eq.png)",
    "comma before \\\\", "punctuation", r"(M),\\", r"(M)\\")
add(126, "(11.2.9.1), second line: gr•_{𝔍_λ}(M_λ)⊗_{A_λ}A_μ → gr•_{𝔍_μ}(M_μ)", "gr• twice", "gr^* twice", "symbol",
    r"\operatorname{gr}_{\mathfrak J_\lambda}^*(M_\lambda)⏎  \otimes_{A_\lambda}A_\mu&\longrightarrow⏎  \operatorname{gr}_{\mathfrak J_\mu}^*",
    r"\operatorname{gr}_{\mathfrak J_\lambda}^\bullet(M_\lambda)⏎  \otimes_{A_\lambda}A_\mu&\longrightarrow⏎  \operatorname{gr}_{\mathfrak J_\mu}^\bullet",
    note="The faint mark above M_μ in this line is a speck, not a prime.")
add(126, "(11.2.9), end: 'sont alors bijectifs et gr•_{𝔍_μ}(M_μ) est un A_λ-module plat'", "gr•", "gr^*", "symbol",
    r"$\operatorname{gr}_{\mathfrak J_\mu}^*(M_\mu)$ est un",
    r"$\operatorname{gr}_{\mathfrak J_\mu}^\bullet(M_\mu)$ est un")
add(126, "Lemme (11.2.9.2) (printed at the top of p. 127; TeX still in the p. 126 segment): 'Si gr•_𝔍(M) est un A-module plat'",
    "gr•", "gr^*", "symbol",
    r"$\operatorname{gr}_{\mathfrak J}^*(M)$ est un $A$-module plat",
    r"$\operatorname{gr}_{\mathfrak J}^\bullet(M)$ est un $A$-module plat",
    note="Apply before the marker insert below (after it this text belongs to the p. 127 segment).")
add(126, "Lemme (11.2.9.2) (printed p. 127), display: (gr•_𝔍(M))⊗_AA' → gr•_{𝔍'}(M')", "gr• twice", "gr^* twice", "symbol",
    r"(\operatorname{gr}_{\mathfrak J}^*(M))\otimes_AA'⏎\longrightarrow \operatorname{gr}_{\mathfrak J'}^*(M')",
    r"(\operatorname{gr}_{\mathfrak J}^\bullet(M))\otimes_AA'⏎\longrightarrow \operatorname{gr}_{\mathfrak J'}^\bullet(M')",
    note="Apply before the marker insert below.")
add(126, "page break 126/127 (edit 1 of 2, insert): before Lemme (11.2.9.2)",
    "printed p. 126 ends 'Cela résulte du lemme suivant :' (page_126_s4.png); printed p. 127 begins 'Lemme (11.2.9.2). — Soient A un anneau, ...' (page_127_s1.png)",
    "\\oldpage[IV-3]{127} stands after the lemma (11.2.9.2), before 'En effet, par récurrence': one statement (six printed lines) too late",
    "marker",
    r"Cela résulte du lemme suivant~:⏎⏎\begin{lemma}[11.2.9.2]",
    r"Cela résulte du lemme suivant~:⏎⏎\oldpage[IV-3]{127}⏎\begin{lemma}[11.2.9.2]",
    note="Marker move: apply together with the p. 127 entry that removes the old marker (edit 2 of 2), after the two lemma entries above.")

# ---------------------------------------------------------------- p. 127
add(127, "page break 126/127 (edit 2 of 2, remove the old marker): before 'En effet, par récurrence sur k'",
    "'En effet' opens an indented paragraph after the lemma, below the top of p. 127",
    "\\oldpage[IV-3]{127} after \\end{lemma}", "marker",
    r"\oldpage[IV-3]{127}⏎⏎En effet", r"En effet",
    note="Apply together with the p. 126 insert (edit 1 of 2); leaves '\\end{lemma}', a blank line, 'En effet' (new paragraph, as printed).")
add(127, "proof of (11.2.9.2): 'entraîne d'abord, par (0_I, 6.1.2) que M/𝔍^{k+1}M est'",
    "no comma after '(0_I, 6.1.2)' (crop p127_s1_que.png)", "comma: '6.1.2), que'", "punctuation",
    r"par ($\mathbf 0_{\mathrm I}$, 6.1.2), que", r"par ($\mathbf 0_{\mathrm I}$, 6.1.2) que")
add(127, "proof of (11.2.9.2): 'à son image canonique 𝔍'^{k+1}M' dans M''",
    "𝔍'^{k+1}M': prime and exponent k+1, no comma (crop p127_s2_Jprime.png)",
    "\\mathfrak J'^{,k+1} typesets a comma between the prime and k+1", "formula",
    r"$\mathfrak J'^{,k+1}M'$", r"$\mathfrak J'^{k+1}M'$",
    note="Same pattern as GLOBAL_ISSUES 49 (^{,..} exponents after a prime).")
add(127, "proof of (11.2.9): label 'I)'", "'I)' in ordinary roman (stem 6-7 px)", "\\textbf{I)} (bold)", "font",
    r"\noindent\textbf{I)}", r"\noindent I)")
add(127, "I): 'On peut donc supposer que A_0 (donc aussi B_0) est noethérien.'",
    "'noethérien' italic (crop p127_s3_noeth.png)", "upright", "italics",
    r"(donc aussi $B_0$) est noethérien.", r"(donc aussi $B_0$) est \emph{noethérien}.")
add(127, "I): 'tel que gr•_{𝔍_ξ}(M_ξ) soit un C_λ-module plat'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_\xi}^*(M_\xi)", r"\operatorname{gr}_{\mathfrak J_\xi}^\bullet(M_\xi)")
add(127, "I): 'il résulte de (11.2.9.2) que gr•_{𝔍_λ}(M_λ) est un A_λ-module plat'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_\lambda}^*(M_\lambda)", r"\operatorname{gr}_{\mathfrak J_\lambda}^\bullet(M_\lambda)")
add(127, "proof of (11.2.9): label 'II)' (Lemmes préliminaires)", "'II)' in ordinary roman (stems 6 px)",
    "\\textbf{II)} (bold)", "font", r"\noindent\textbf{II)}", r"\noindent II)")
add(127, "Lemme (11.2.9.3): 'M⊗_A k(𝔮) soit un'", "bold italic k", "plain k", "convention",
    r"$M\otimes_Ak(\mathfrak q)$ soit un", r"$M\otimes_A\boldsymbol{k}(\mathfrak q)$ soit un", conv=1)
add(127, "Lemme (11.2.9.3), end: '(B⊗_A k(𝔮))-module de type fini'", "bold italic k", "plain k", "convention",
    r"$(B\otimes_Ak(\mathfrak q))$-module", r"$(B\otimes_A\boldsymbol{k}(\mathfrak q))$-module", conv=1)
add(127, "proof of (11.2.9.3): 'supposer que A est aussi un anneau local dont 𝔮 est l'idéal maximal'",
    "'local' italic", "upright", "italics", r"un anneau local dont", r"un anneau \emph{local} dont")
add(127, "proof of (11.2.9.3), display at the foot of the page: ⊕_{-N≤i≤N}(M_i⊗_{B_0}B)⊗_A k(𝔮) → M⊗_A k(𝔮)",
    "no parentheses around the direct sum (crop p127_s4_disp.png)", "\\left( ... \\right) around the direct sum", "formula",
    r"\left(\bigoplus_{-N\leq i\leq N}(M_i\otimes_{B_0}B)\right)", r"\bigoplus_{-N\leq i\leq N}(M_i\otimes_{B_0}B)")
add(127, "same display: '⊗_A k(𝔮) →'", "bold italic k", "plain k", "convention",
    r"\otimes_Ak(\mathfrak q)\longrightarrow", r"\otimes_A\boldsymbol{k}(\mathfrak q)\longrightarrow", conv=1)
add(127, "same display: '→ M⊗_A k(𝔮)'", "bold italic k", "plain k", "convention",
    r" M\otimes_Ak(\mathfrak q)", r" M\otimes_A\boldsymbol{k}(\mathfrak q)", conv=1)
add(127, "end of p. 127 / top of p. 128: display, then 'soit surjectif; cela signifie ...'",
    "'soit surjectif' (first line of p. 128) is flush left: the sentence continues after the display; no paragraph break",
    "blank line after \\] at the end of page_127.tex, before \\oldpage[IV-3]{128}", "marker",
    r"⏎\]⏎⏎", r"⏎\]⏎",
    note="Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place. Apply with the p. 128 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- p. 128
add(128, "top of p. 128, after \\oldpage[IV-3]{128}: 'soit surjectif'",
    "continues the sentence of p. 127 (flush left)", "blank line after \\oldpage[IV-3]{128}", "marker",
    r"\oldpage[IV-3]{128}⏎⏎soit", r"\oldpage[IV-3]{128}⏎soit",
    note="Apply with the p. 127 entry removing the blank line before the marker.")
add(128, "l. 1: 'soit surjectif; cela signifie aussi'", "'surjectif' italic (crop p128_s1_surj.png)", "upright", "italics",
    r"surjectif~; cela", r"\emph{surjectif}~; cela")
add(128, "l. 2: 'l'homomorphisme canonique de k(𝔮)-modules'", "bold italic k", "plain k", "convention",
    r"de $k(\mathfrak q)$-modules", r"de $\boldsymbol{k}(\mathfrak q)$-modules", conv=1)
add(128, "first display: ⊕_{-N≤i≤N}(M_i⊗_{B_0}B_{n-i})⊗_A k(𝔮) → M_n⊗_A k(𝔮)",
    "no parentheses around the direct sum", "\\left( ... \\right) around the direct sum", "formula",
    r"\left(\bigoplus_{-N\leq i\leq N}(M_i\otimes_{B_0}B_{n-i})\right)", r"\bigoplus_{-N\leq i\leq N}(M_i\otimes_{B_0}B_{n-i})")
add(128, "first display: '⊗_A k(𝔮) → M_n'", "bold italic k", "plain k", "convention",
    r"\otimes_Ak(\mathfrak q)\longrightarrow M_n", r"\otimes_A\boldsymbol{k}(\mathfrak q)\longrightarrow M_n", conv=1)
add(128, "first display: 'M_n⊗_A k(𝔮)'", "bold italic k", "plain k", "convention",
    r"\otimes_Ak(\mathfrak q)⏎\]⏎est surjectif. Or", r"\otimes_A\boldsymbol{k}(\mathfrak q)⏎\]⏎est surjectif. Or", conv=1)
add(128, "Corollaire (11.2.9.4): 'Sous les hypothèses de (11.2.9.3), on suppose'",
    "reference upright inside the italic statement (crop p128_s2_cor.png)", "italic", "convention",
    r"Sous les hypothèses de (11.2.9.3), on", r"Sous les hypothèses de \textup{(11.2.9.3)}, on", conv=6)
add(128, "Corollaire (11.2.9.4): 'il faut et il suffit que M⊗_A k(𝔮) soit'", "bold italic k", "plain k", "convention",
    r"il suffit que $M\otimes_Ak(\mathfrak q)$", r"il suffit que $M\otimes_A\boldsymbol{k}(\mathfrak q)$", conv=1)
add(128, "Corollaire (11.2.9.4), end: '(B⊗_A k(𝔮))-module de présentation finie'", "bold italic k", "plain k", "convention",
    r"$(B\otimes_Ak(\mathfrak q))$-module de présentation", r"$(B\otimes_A\boldsymbol{k}(\mathfrak q))$-module de présentation", conv=1)
add(128, "proof of (11.2.9.4): 'il existe un B-module libre gradué de type fini L'",
    "'libre gradué' both italic (crop p128_s2_libre_ker.png)", "only 'gradué' in \\emph", "italics",
    r"$B$-module libre \emph{gradué} de", r"$B$-module \emph{libre gradué} de")
add(128, "proof of (11.2.9.4): 'Soit R=Ker(u)'", "Ker with a capital K", "\\ker (prints lower-case ker)", "formula",
    r"$R=\ker(u)$", r"$R=\operatorname{Ker}(u)$")
add(128, "proof of (11.2.9.4): 'le noyau d'un homomorphisme surjectif ⊕_{1≤j≤r}B_{i+m_j}→M_i; on conclut'",
    "formula set inline in the running text", "displayed with \\[ ... \\] (with '~;' inside)", "formula",
    r"homomorphisme surjectif⏎\[⏎\bigoplus_{1\leq j\leq r}B_{i+m_j}\longrightarrow M_i~;⏎\]⏎on conclut",
    r"homomorphisme surjectif⏎$\bigoplus_{1\leq j\leq r}B_{i+m_j}\longrightarrow M_i$~;⏎on conclut",
    note="Display vs inline; no connecting word lost or added.")
add(128, "proof of (11.2.9.4): '(Bourbaki, Alg. comm., chap. I, § 2, n° 8, lemme 9)'",
    "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol",
    r"n$^\circ$~8", r"n\textsuperscript{o}~8", note="The edition's form is n\\textsuperscript{o} (as on IV-3 p. 79, 0_IV pp. 156-164).")
add(128, "proof of (11.2.9.4), exact sequence: '0 → R⊗_A k(𝔮)'", "bold italic k", "plain k", "convention",
    r"0\longrightarrow R\otimes_Ak(", r"0\longrightarrow R\otimes_A\boldsymbol{k}(", conv=1)
add(128, "exact sequence: '→ L⊗_A k(𝔮)'", "bold italic k", "plain k", "convention",
    r"\longrightarrow L\otimes_Ak(", r"\longrightarrow L\otimes_A\boldsymbol{k}(", conv=1)
add(128, "exact sequence: '→ M⊗_A k(𝔮) → 0'", "bold italic k", "plain k", "convention",
    r"\longrightarrow M\otimes_Ak(", r"\longrightarrow M\otimes_A\boldsymbol{k}(", conv=1)
add(128, "proof of (11.2.9.4): 'que R⊗_A k(𝔮) est un'", "bold italic k", "plain k", "convention",
    r"$R\otimes_Ak(\mathfrak q)$ est un", r"$R\otimes_A\boldsymbol{k}(\mathfrak q)$ est un", conv=1)
add(128, "proof of (11.2.9.4): '(B⊗_A k(𝔮))-module de type fini'", "bold italic k", "plain k", "convention",
    r"$(B\otimes_Ak(\mathfrak q))$-module de type", r"$(B\otimes_A\boldsymbol{k}(\mathfrak q))$-module de type", conv=1)
add(128, "proof of (11.2.9): label 'III)'", "'III)' in ordinary roman (stems 6-7 px)", "\\textbf{III)} (bold)", "font",
    r"\noindent\textbf{III)}", r"\noindent III)")
add(128, "III): 'un système inductif de sous-anneaux noethériens de A'",
    "'noethériens' italic (crop p128_s3_III.png)", "upright", "italics",
    r"noethériens de $A$, dont", r"\emph{noethériens} de $A$, dont")
add(128, "III): 'pour μ≥λ, gr•_{𝔍'_μ}(M'_μ) soit un A'_μ-module plat'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J'_\mu}^*(M'_\mu)", r"\operatorname{gr}_{\mathfrak J'_\mu}^\bullet(M'_\mu)")
add(128, "III): 'B_μ=B'_λ⊗_{A'_λ}A_μ, 𝔍_μ=𝔍'_λB_μ et M_μ=M'_λ⊗_{A'_λ}A_μ'",
    "no comma before 'et' (crop p128_s4_et.png)", "comma: '𝔍_μ=𝔍'_λB_μ$, et'", "punctuation",
    r"$\mathfrak J_\mu=\mathfrak J'_\lambda B_\mu$, et", r"$\mathfrak J_\mu=\mathfrak J'_\lambda B_\mu$ et")
add(128, "III), end: 'que gr•_{𝔍_μ}(M_μ) est un A_μ-module plat'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_\mu}^*(M_\mu)", r"\operatorname{gr}_{\mathfrak J_\mu}^\bullet(M_\mu)")
add(128, "proof of (11.2.9): label 'IV)'", "'IV)' in ordinary roman (stems 6-7 px)", "\\textbf{IV)} (bold)", "font",
    r"\noindent\textbf{IV)}", r"\noindent IV)")
add(128, "heading IV): 'et gr•_{𝔍_0}(B_0)=B_0'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_0}^*(B_0)=B_0", r"\operatorname{gr}_{\mathfrak J_0}^\bullet(B_0)=B_0")
add(128, "end of p. 128 / top of p. 129: 'Posons B'_0=A_0[T_1, ..., T_n], | algèbre de polynômes'",
    "page break inside the sentence; p. 129 begins flush left 'algèbre de polynômes (donc noethérienne)'",
    "blank line before \\oldpage[IV-3]{129}", "marker",
    r"Posons $B'_0=A_0[T_1,\ldots,T_n]$,⏎⏎", r"Posons $B'_0=A_0[T_1,\ldots,T_n]$,⏎",
    note="Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place. Apply with the p. 129 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- p. 129
add(129, "top of p. 129, after \\oldpage[IV-3]{129}: 'algèbre de polynômes'",
    "continues the sentence of p. 128 (flush left)", "blank line after \\oldpage[IV-3]{129}", "marker",
    r"\oldpage[IV-3]{129}⏎⏎algèbre", r"\oldpage[IV-3]{129}⏎algèbre",
    note="Apply with the p. 128 entry removing the blank line before the marker.")
add(129, "IV): 'On pose alors B'_λ=B'_0⊗_{A_0}A_λ=A_λ[T_1, ..., T_n], 𝔍'_λ=𝔍'_0B'_λ, B'=B'_0⊗_{A_0}A=A[T_1, ..., T_n], 𝔍'=𝔍'_0B', de sorte que'",
    "all four formulas set inline in the running text", "two displays \\[ ... \\] joined by \\qquad", "formula",
    r"On pose alors⏎\[⏎B'_\lambda=B'_0\otimes_{A_0}A_\lambda⏎=A_\lambda[T_1,\ldots,T_n],\qquad⏎\mathfrak J'_\lambda=\mathfrak J'_0B'_\lambda,⏎\]⏎\[⏎B'=B'_0\otimes_{A_0}A=A[T_1,\ldots,T_n],\qquad⏎\mathfrak J'=\mathfrak J'_0B',⏎\]⏎de sorte",
    r"On pose alors⏎$B'_\lambda=B'_0\otimes_{A_0}A_\lambda⏎=A_\lambda[T_1,\ldots,T_n]$, $\mathfrak J'_\lambda=\mathfrak J'_0B'_\lambda$,⏎$B'=B'_0\otimes_{A_0}A=A[T_1,\ldots,T_n]$, $\mathfrak J'=\mathfrak J'_0B'$,⏎de sorte",
    note="Display vs inline; no connecting word lost or added.")
add(129, "IV): 'donc gr•_{𝔍'}(M)=gr•_𝔍(M) en tant que A-module'", "gr• twice", "gr^* twice", "symbol",
    r"\operatorname{gr}_{\mathfrak J'}^*(M)=\operatorname{gr}_{\mathfrak J}^*(M)",
    r"\operatorname{gr}_{\mathfrak J'}^\bullet(M)=\operatorname{gr}_{\mathfrak J}^\bullet(M)")
add(129, "IV): 'gr•_{𝔍'_λ}(M_λ)=gr•_{𝔍_λ}(M_λ) en tant que A_λ-module'", "gr• twice", "gr^* twice", "symbol",
    r"\operatorname{gr}_{\mathfrak J'_\lambda}^*(M_\lambda)⏎=\operatorname{gr}_{\mathfrak J_\lambda}^*(M_\lambda)",
    r"\operatorname{gr}_{\mathfrak J'_\lambda}^\bullet(M_\lambda)⏎=\operatorname{gr}_{\mathfrak J_\lambda}^\bullet(M_\lambda)")
add(129, "IV), end: 'par construction gr•_{𝔍'}(B') s'identifie à B''", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J'}^*(B')", r"\operatorname{gr}_{\mathfrak J'}^\bullet(B')")
add(129, "IV), end: 'et gr•_{𝔍'_λ}(B'_λ) à B'_λ'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J'_\lambda}^*(B'_\lambda)", r"\operatorname{gr}_{\mathfrak J'_\lambda}^\bullet(B'_\lambda)")
add(129, "proof of (11.2.9): label 'V)'", "'V)' in ordinary roman (crop p129_s2_V.png)", "\\textbf{V)} (bold)", "font",
    r"\noindent\textbf{V)}", r"\noindent V)")
add(129, "heading V): 'Preuve du fait que gr•_𝔍(M) est un gr•_𝔍(B)-module de présentation finie'", "gr• twice", "gr^* twice", "symbol",
    r"$\operatorname{gr}_{\mathfrak J}^*(M)$ est un⏎$\operatorname{gr}_{\mathfrak J}^*(B)$-module",
    r"$\operatorname{gr}_{\mathfrak J}^\bullet(M)$ est un⏎$\operatorname{gr}_{\mathfrak J}^\bullet(B)$-module")
add(129, "V): 'l'anneau C_0=gr•_{𝔍_0}(B_0) s'identifie donc à B_0'", "gr•", "gr^*", "symbol",
    r"C_0=\operatorname{gr}_{\mathfrak J_0}^*(B_0)", r"C_0=\operatorname{gr}_{\mathfrak J_0}^\bullet(B_0)")
add(129, "V): 'et C=gr•_𝔍(B) s'identifie à B'", "gr•", "gr^*", "symbol",
    r"$C=\operatorname{gr}_{\mathfrak J}^*(B)$", r"$C=\operatorname{gr}_{\mathfrak J}^\bullet(B)$")
add(129, "Lemme (11.2.9.5): item labels 1°, 2°, 3°, 4°",
    "the numerals are upright old-style figures (crop p129_s2_labels.png)",
    "label=\\arabic{enumi}$^\\circ$ inside the italic lemma: italic numerals", "convention",
    r"\begin{enumerate}[label=\arabic{enumi}$^\circ$]", r"\begin{enumerate}[label=\textup{\arabic{enumi}}$^\circ$]", conv=6,
    note="One edit for the four labels.")
add(129, "Lemme (11.2.9.5) 4°: 'gr•_{𝔍_{0i}}(M_0⊗_{A_0}A_{0i}) est un A_{0i}-module plat'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_{0i}}^*", r"\operatorname{gr}_{\mathfrak J_{0i}}^\bullet")
add(129, "proof of (11.2.9.5), l. 3: '𝔍_0 par 𝔍'_0=𝔍_0B_0 et M_0 par M_0⊗_{A_0}A'_0'",
    "𝔍'_0=𝔍_0B_0: no prime on B_0 (crop p129_s3_B0_zoom.png; the B'_0 just before on the line has its prime)",
    "silently corrected: $\\mathfrak J'_0=\\mathfrak J_0B'_0$", "misprint_in_print",
    r"$\mathfrak J'_0=\mathfrak J_0B'_0$", r"$\mathfrak J'_0=\mathfrak J_0B_0$",
    corrected=r"$\mathfrak J'_0=\mathfrak J_0B'_0$",
    note="𝔍'_0 is the ideal of B'_0=B_0⊗_{A_0}A'_0 generated by 𝔍_0, as in 4° of the lemma (𝔍_{0i}=𝔍_0B_{0i}).")
add(129, "proof of (11.2.9.5), l. 5: 'et B_0, J_0, M_0 par les objets correspondants'",
    "a roman J_0 (wrong fount), not the Fraktur 𝔍_0 (crop p129_s3_J0_zoom.png)",
    "silently corrected: $\\mathfrak J_0$", "misprint_in_print",
    r"$\mathfrak J_0$, $M_0$ par les objets", r"$J_0$, $M_0$ par les objets",
    corrected=r"$\mathfrak J_0$",
    note="Capital letters in formulas are upright in the print and $X$ in the TeX throughout, so the roman J is $J_0$.")
add(129, "proof of (11.2.9.5): 'gr•_{𝔍_0}(B_0) est une A_0-algèbre de type fini'", "gr•", "gr^*", "symbol",
    r"$\operatorname{gr}_{\mathfrak J_0}^*(B_0)$ est une", r"$\operatorname{gr}_{\mathfrak J_0}^\bullet(B_0)$ est une")
add(129, "proof of (11.2.9.5): 'et gr•_{𝔍_0}(M_0) un gr•_{𝔍_0}(B_0)-module de type fini'", "gr• twice", "gr^* twice", "symbol",
    r"\operatorname{gr}_{\mathfrak J_0}^*(M_0)$ un⏎$\operatorname{gr}_{\mathfrak J_0}^*(B_0)$-module",
    r"\operatorname{gr}_{\mathfrak J_0}^\bullet(M_0)$ un⏎$\operatorname{gr}_{\mathfrak J_0}^\bullet(B_0)$-module")
add(129, "proof of (11.2.9.5): 'gr•_{𝔍_0}(M_0)⊗_{A_0}A_{01} soit un A_{01}-module plat'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_0}^*(M_0)\otimes_{A_0}A_{01}$ soit un",
    r"\operatorname{gr}_{\mathfrak J_0}^\bullet(M_0)\otimes_{A_0}A_{01}$ soit un")
add(129, "proof of (11.2.9.5): 'gr•_{𝔍_0}(M_0)⊗_{A_0}A_{01} s'identifie à'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_0}^*(M_0)\otimes_{A_0}A_{01}$ s'identifie",
    r"\operatorname{gr}_{\mathfrak J_0}^\bullet(M_0)\otimes_{A_0}A_{01}$ s'identifie")
add(129, "proof of (11.2.9.5): 'à gr•_{𝔍_{01}}(M_0⊗_{A_0}A_{01})'", "gr•", "gr^*", "symbol",
    r"\operatorname{gr}_{\mathfrak J_{01}}^*", r"\operatorname{gr}_{\mathfrak J_{01}}^\bullet")
add(129, "last paragraph: 'Il y a donc une famille finie (f_{ik})_{1≤i≤m, 1≤k≤n} d'éléments de A_0'",
    "'une famille finie' (page_129_s4.png, start of the line)", "'finie' missing", "missing",
    r"Il y a donc une famille⏎$(f_{ik})", r"Il y a donc une famille⏎finie $(f_{ik})")

# ---------------------------------------------------------------- checks
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = rel[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(rel))]
bad = 0
pages = {}
for x in F:
    fx = x["fix"]
    if fx is None:
        continue
    p = x["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c1 = pages[p].count(fx["old"])
    c2 = segs[p].count(fx["old"])
    if c1 != 1 or c2 != 1:
        bad += 1
        print("COUNT", p, c1, c2, repr(fx["old"][:80]))
# sequential application on the release segments (in JSON order) to catch overlaps
work = rel
for x in F:
    fx = x["fix"]
    if fx is None:
        continue
    p = x["page"]
    cs = [(int(m.group(1)), m.start()) for m in marker.finditer(work)]
    s = e = None
    for i, (n, st) in enumerate(cs):
        if n == p:
            j = i + 1
            while j < len(cs) and cs[j][0] == p:
                j += 1
            s, e = st, (cs[j][1] if j < len(cs) else len(work))
            break
    seg = work[s:e]
    if seg.count(fx["old"]) != 1:
        bad += 1
        print("SEQ", p, seg.count(fx["old"]), repr(fx["old"][:80]))
        continue
    work = work[:s] + seg.replace(fx["old"], fx["new"]) + work[e:]
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(125, 130):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("findings", len(F), "problems", bad)
(RUN / "crops_125_129" / "sequential_result_ega4-11.tex").write_text(work, encoding="utf-8", newline="")
