# Builds findings_158_163.json for run_III1 (pages 158, 159, 161, 162, 163) and checks every fix.
# Placeholder "¶" in old/new strings stands for a line break (LF).
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_158_163.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def c2(page, where, numeral, old, new, note=""):
    add(page, where, "bold " + numeral + " (chapter numeral)", "plain " + numeral, "convention", 2, "high",
        old, new, note)


DISP = "Layout: the print sets this formula inline in the running text (as the inline/display findings on pp. 90-99; GLOBAL_ISSUES 21/36)."

# ---------------------------------------------------------------- page 158
add(158, "Théorème (5.4.5), first line of the page: 'Soit ℒ un 𝒪_X-Module inversible'",
    "𝒪_X with a roman capital X subscript: the same glyph as in 'un 𝒪_X-Module ample ℳ' two lines below, unlike the Fraktur 𝔛 of 'ℱ=𝒪_𝔛' in the proof (4x crops)",
    "$\\mathcal O_{\\mathfrak X}$ (silently corrected)", "misprint_in_print", None, "high",
    r"Soit $\mathcal L$ un $\mathcal O_{\mathfrak X}$-Module inversible",
    r"Soit $\mathcal L$ un $\mathcal O_X$-Module inversible",
    "ℒ is an invertible Module on the formal scheme 𝔛 of the statement (p. 157: f : 𝔛 → 𝔖); X is only introduced later in the sentence ('si X est un S-schéma propre'). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$\mathcal O_{\mathfrak X}$")
add(158, "end of Théorème (5.4.5): '(ce qui entraîne que X est projectif sur S).'",
    "the parenthesis is roman inside the italic statement; only 'projectif' is italic (crop)",
    "italic throughout (theorem environment)", "convention", 6, "high",
    r"(ce qui entraîne que¶$X$ est projectif sur $S$)",
    r"\textup{(ce qui entraîne que¶$X$ est \emph{projectif} sur $S$)}",
    "\\emph inside \\textup keeps 'projectif' italic, as printed.")
add(158, "proof of (5.4.5), l. 2: 'Γ(𝔛, ℒ^{⊗n})→Γ(X_0, ℒ_0^{⊗n}) soit surjectif. On peut supposer'",
    "'surjectif' italic", "upright", "italics", None, "high",
    r"soit surjectif. On peut supposer", r"soit \emph{surjectif}. On peut supposer")
add(158, "proof of (5.4.5), l. 3: 'pour que ℒ_0^{⊗n} soit très ample pour S_0'",
    "'très ample' italic", "upright", "italics", None, "high",
    r"soit très¶ample pour", r"soit \emph{très¶ample} pour")
c2(158, "'très ample pour S_0 (II, 4.5.10). Comme'", "II",
   r"(II, 4.5.10). Comme", r"(\textbf{II}, 4.5.10). Comme")
add(158, "'considérons l'homomorphisme u_k : E/𝔍^{k+1}E→Γ(X_k, ℒ_k^{⊗n}) déduit de l'injection canonique'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶u_k:E/\mathfrak J^{k+1}E\longrightarrow¶\Gamma(X_k,\mathcal L_k^{\otimes n})¶\]",
    r"$u_k:E/\mathfrak J^{k+1}E\longrightarrow¶\Gamma(X_k,\mathcal L_k^{\otimes n})$", DISP)
add(158, "'u_k définit un homomorphisme ũ_k : (E/𝔍^{k+1}E)~→(f_k)_*(ℒ_k^{⊗n}), et par suite'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\widetilde u_k:(E/\mathfrak J^{k+1}E)^\sim¶\longrightarrow(f_k)_*(\mathcal L_k^{\otimes n}),¶\]",
    r"$\widetilde u_k:(E/\mathfrak J^{k+1}E)^\sim¶\longrightarrow(f_k)_*(\mathcal L_k^{\otimes n})$,", DISP)
add(158, "'aussi un homomorphisme ũ_k^♯ : f_k^*((E/𝔍^{k+1}E)~)→ℒ_k^{⊗n}. D'ailleurs'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\widetilde u_k^\sharp:¶f_k^*((E/\mathfrak J^{k+1}E)^\sim)\longrightarrow¶\mathcal L_k^{\otimes n}.¶\]",
    r"$\widetilde u_k^\sharp:¶f_k^*((E/\mathfrak J^{k+1}E)^\sim)\longrightarrow¶\mathcal L_k^{\otimes n}$.", DISP)
c2(158, "'𝒢_0=𝒢_k/𝔍𝒢_k (I, 9.1.5)'", "I", r"(I, 9.1.5)", r"(\textbf{I}, 9.1.5)")
add(158, "'l'homomorphisme canonique σ : f_0^*((f_0)_*(ℒ_0^{⊗n}))→ℒ_0^{⊗n}, et l'hypothèse'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\sigma:f_0^*((f_0)_*(\mathcal L_0^{\otimes n}))\longrightarrow¶\mathcal L_0^{\otimes n},¶\]",
    r"$\sigma:f_0^*((f_0)_*(\mathcal L_0^{\otimes n}))\longrightarrow¶\mathcal L_0^{\otimes n}$,", DISP)
add(158, "'entraîne que ũ_0^♯ est surjectif (II, 4.4.3)'",
    "'surjectif' italic", "upright", "italics", None, "high",
    r"que¶$\widetilde u_0^\sharp$ est surjectif", r"que¶$\widetilde u_0^\sharp$ est \emph{surjectif}")
c2(158, "'ũ_0^♯ est surjectif (II, 4.4.3); on déduit'", "II",
   r"(II, 4.4.3)~; on déduit", r"(\textbf{II}, 4.4.3)~; on déduit")
add(158, "'chacun des ũ_k^♯ est aussi surjectif.'",
    "'surjectif' italic", "upright", "italics", None, "high",
    r"est aussi surjectif.", r"est aussi \emph{surjectif}.")
c2(158, "'définit donc (II, 4.2.2) un S_k-morphisme'", "II",
   r"(II, 4.2.2) un", r"(\textbf{II}, 4.2.2) un")
add(158, "'un S_k-morphisme g_k : X_k→P_k=P(E/𝔍^{k+1}E), et comme'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶g_k:X_k\longrightarrow P_k=\mathbf P(E/\mathfrak J^{k+1}E),¶\]",
    r"$g_k:X_k\longrightarrow P_k=\mathbf P(E/\mathfrak J^{k+1}E)$,",
    DISP + " Apply before the next finding (bold k), whose 'old' lies inside this one. The bold P is printed bold upright here (matches \\mathbf P).")
add(158, "same formula: 'P_k=P(E/𝔍^{k+1}E)'",
    "the subscript k of P_k is a bold italic k (wrong fount): stroke width 4.0 px against 2.0-2.8 px and ink area 134 px against 82-112 px for the other subscript k's of the same size on this line and the next (g_k, X_k, P_k, S_k); P itself is regular roman",
    "P_k (plain k; silently corrected)", "misprint_in_print", None, "medium",
    r"P_k=\mathbf P(E/", r"P_{\boldsymbol{k}}=\mathbf P(E/",
    "Wrong-fount letter, recorded like the bold italic n of EGA II (GLOBAL_ISSUES 29). Apply after the g_k display edit (preceding finding).",
    corrected="P_k")
c2(158, "'pour h⩽k en vertu de (II, 4.1.3)'", "II", r"(II, 4.1.3)", r"(\textbf{II}, 4.1.3)")
add(158, "'(g_k) est un (S_k)-système inductif adique (I, 10.12.2)'",
    "'système inductif adique' italic, '(S_k)-' upright", "upright", "italics", None, "high",
    r"$(S_k)$-système inductif adique", r"$(S_k)$-\emph{système inductif adique}")
c2(158, "'système inductif adique (I, 10.12.2)'", "I", r"(I, 10.12.2)", r"(\textbf{I}, 10.12.2)")
c2(158, "'et de (II, 4.2.10). Les g_k'", "II", r"(II, 4.2.10)", r"(\textbf{II}, 4.2.10)")
add(158, "'entraîne que g_0 est une immersion fermée (II, 4.4.3)'",
    "'immersion fermée' italic", "upright", "italics", None, "high",
    r"$g_0$ est une immersion fermée", r"$g_0$ est une \emph{immersion fermée}")
c2(158, "'immersion fermée (II, 4.4.3); on en conclut'", "II",
   r"(II, 4.4.3)~; on en conclut", r"(\textbf{II}, 4.4.3)~; on en conclut")
c2(158, "'le complété de ℳ^{⊗n} (I, 10.8.10)'", "I", r"(I, 10.8.10)", r"(\textbf{I}, 10.8.10)")
add(158, "'un homomorphisme bien déterminé v : f^*(Ẽ)→ℳ^{⊗n} (5.1.7)'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶v:f^*(\widetilde E)\longrightarrow\mathcal M^{\otimes n}¶\]",
    r"$v:f^*(\widetilde E)\longrightarrow\mathcal M^{\otimes n}$", DISP)
add(158, "'(5.1.7); d'ailleurs, comme ũ_0^♯ est surjectif, il en est de même de v̂'",
    "ũ_0^♯: subscript 0 (crop)", "$\\widetilde u_k^\\sharp$", "formula", None, "high",
    r"comme $\widetilde u_k^\sharp$ est surjectif", r"comme $\widetilde u_0^\sharp$ est surjectif",
    "The printed 0 is right: (I, 10.11.5) says a homomorphism θ of coherent Modules is surjective iff θ_0 is, and ũ_0^♯ is the reduction of v̂.")
c2(158, "'il en est de même de v̂ (I, 10.11.5)'", "I", r"(I, 10.11.5)", r"(\textbf{I}, 10.11.5)")
c2(158, "'défini par v (II, 4.2.2) a pour prolongement'", "II",
   r"(II, 4.2.2) a pour", r"(\textbf{II}, 4.2.2) a pour")
c2(158, "'ℳ^{⊗n} est très ample (II, 4.4.6)'", "II", r"(II, 4.4.6)", r"(\textbf{II}, 4.4.6)")
c2(158, "'et ℳ est ample (II, 4.5.10).'", "II", r"ample (II, 4.5.10).", r"ample (\textbf{II}, 4.5.10).")
c2(158, "Remarque (5.4.6): 'résulte facilement de (I, 10.10.2)'", "I", r"(I, 10.10.2)", r"(\textbf{I}, 10.10.2)")
c2(158, "Remarque (5.4.6): 'défini par 𝒩 (I, 10.14.2)'", "I", r"(I, 10.14.2)", r"(\textbf{I}, 10.14.2)")

# ---------------------------------------------------------------- page 159
add(159, "heading 5.5: '5.5. Une décomposition de certains schémas.'",
    "the bold heading ends with a full stop", "\\subsection{Une décomposition de certains schémas} (no full stop)",
    "punctuation", None, "high",
    r"\subsection{Une décomposition de certains schémas}", r"\subsection{Une décomposition de certains schémas.}",
    "GLOBAL_ISSUES 43 (no \\subsection title of ega3-1 has the printed full stop): drop this page fix if the one-pass change is made.")
add(159, "proof of (5.5.1): 'un sous-schéma fermé Z de T propre sur Y'",
    "'propre' italic (crop)", "upright", "italics", None, "high",
    r"de $T$ propre sur $Y$", r"de $T$ \emph{propre} sur $Y$")
add(159, "proof of (5.5.1): 'î=Ẑ→T̂ soit un isomorphisme'",
    "î=Ẑ→T̂: an equals sign after î (4x crop)", "$\\widehat i:\\widehat Z\\to\\widehat T$ (silently corrected)",
    "misprint_in_print", None, "high",
    r"$\widehat i:\widehat Z\to\widehat T$", r"$\widehat i=\widehat Z\to\widehat T$",
    "The extension î : Ẑ → T̂ of the injection i : Z → T is meant (colon). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$\widehat i:\widehat Z\to\widehat T$")
add(159, "after '(A suivre.)': printed p. 160",
    "printed p. 160 (journal p. 504; PDF p. 157 of PMIHES_1961__11__5_0.pdf) is blank: no text, running head or folio (150-dpi render: 3 isolated dark pixels). Nothing is missing from the TeX.",
    "the blank page is made by \\clearpage \\thispagestyle{empty} \\null \\clearpage after '(A suivre.)' (comment '% La page imprimée 504 est blanche.'), but there is no \\oldpage[III]{160}",
    "marker", None, "high",
    r"\clearpage¶\thispagestyle{empty}", r"\clearpage¶\oldpage[III]{160}¶\thispagestyle{empty}",
    "Marker on the empty page, as for the blank 0_III p. 80 (findings_076_079) and EGA II pp. 212, 216 (GLOBAL_ISSUES 32).")

# ---------------------------------------------------------------- page 161 (scan: page_162_s1..s4.png = PDF p. 159)
S161 = "Scan in page_162_s*.png (the page images of pp. 161 and 162 are swapped). "
add(161, "heading 'BIBLIOGRAPHIE (suite)'",
    "'(suite)' italic, italic parentheses (crop)", "upright", "italics", None, "high",
    r"\section*{BIBLIOGRAPHIE (suite)}", r"\section*{BIBLIOGRAPHIE \textit{(suite)}}",
    S161 + "As the contents entry 'Bibliographie (suite)' of EGA II p. 215.")
add(161, "[27] 'P. Gabriel'", "surname in caps and small caps", "plain 'Gabriel'", "font", None, "high",
    r"P. Gabriel,", r"P. \textsc{Gabriel},", S161 + "Same style as the EGA II bibliography (p. 205 findings).")
add(161, "[28] 'J. E. Roos'", "surname in caps and small caps", "plain 'Roos'", "font", None, "high",
    r"J. E. Roos,", r"J. E. \textsc{Roos},", S161)
add(161, "[28] title 'Sur les foncteurs dérivés de lim←. Applications'",
    "article title roman (crop)", "\\emph{...} (italic)", "italics", None, "high",
    r"\emph{Sur les foncteurs dérivés de $\varprojlim$.¶Applications}",
    r"Sur les foncteurs dérivés de $\varprojlim$.¶Applications",
    S161 + "Article titles are roman in the print, journal names italic (as EGA I p. 214).")
add(161, "[28] journal 'C. R. Acad. Sci. Paris'", "italic (crop)", "upright", "italics", None, "high",
    r"C. R. Acad. Sci. Paris", r"\emph{C. R. Acad. Sci. Paris}", S161)
add(161, "[28] 'p. 3702-3704'", "hyphen between the page numbers (crop)", "en dash (--)", "punctuation", None, "high",
    r"p. 3702--3704", r"p. 3702-3704", S161 + "As EGA II p. 205.")
add(161, "[29] 'H. Cartan'", "surname in caps and small caps", "plain 'Cartan'", "font", None, "high",
    r"H. Cartan,", r"H. \textsc{Cartan},", S161)
add(161, "[29] 'Séminaire de l'École Normale Supérieure'", "roman (crop)", "\\emph{...} (italic)", "italics", None, "high",
    r"\emph{Séminaire de l'École Normale Supérieure}", r"Séminaire de l'École Normale Supérieure",
    S161 + "Roman as in the EGA I bibliography [1] (p. 214 finding).")
add(161, "[29] '(1960-1961)'", "hyphen (crop)", "en dash (--)", "punctuation", None, "high",
    r"(1960--1961)", r"(1960-1961)", S161)

# ---------------------------------------------------------------- page 162 (scan: page_161_s1..s4.png = PDF p. 158)
S162 = "Scan in page_161_s*.png (the page images of pp. 161 and 162 are swapped). "
add(162, "entry 'Ens : 0, 8.1.1.'", "Ens bold italic (crop)", "$\\mathbf{Ens}$ (bold upright)", "font", None, "high",
    r"$\mathbf{Ens}$", r"$\boldsymbol{\mathit{Ens}}$", S162 + "Form of the fix as in 0_III p. 5 (GLOBAL_ISSUES 33).")
c2(162, "entry 'Ens : 0, 8.1.1.'", "0", r": 0, 8.1.1.¶¶$h_X(Y)$", r": \textbf{0}, 8.1.1.¶¶$h_X(Y)$")
add(162, "entry 'h_X(Y), h_X(u) (X, Y objets d'une catégorie C, u morphisme de C)'",
    "both C bold italic (crop)", "$C$ (plain italic)", "font", None, "high",
    r"catégorie $C$, $u$ morphisme de¶$C$)", r"catégorie $\boldsymbol{C}$, $u$ morphisme de¶$\boldsymbol{C}$)",
    S162 + "Category letter C bold italic (GLOBAL_ISSUES 33; \\boldsymbol as in 0_III p. 5).")
c2(162, "entry 'h_X(Y), h_X(u) ... : 0, 8.1.1.'", "0", r": 0, 8.1.1.¶¶$h_w(u)$", r": \textbf{0}, 8.1.1.¶¶$h_w(u)$")
add(162, "entry 'h_w(u) (u, w morphismes de C)'", "C bold italic (crop)", "$C$ (plain italic)", "font", None, "high",
    r"morphismes de $C$)", r"morphismes de $\boldsymbol{C}$)", S162)
c2(162, "entry 'h_w(u) ... : 0, 8.1.2.'", "0", r": 0, 8.1.2.", r": \textbf{0}, 8.1.2.")
c2(162, "entry 'Z_k(E_r^{pq}), B_k(E_r^{pq}) (k⩾r) : 0, 11.1.1.'", "0",
   r"($k\geq r$) : 0, 11.1.1.", r"($k\geq r$) : \textbf{0}, 11.1.1.")
c2(162, "entry 'Z_∞(E_2^{pq}), B_∞(E_2^{pq}) : 0, 11.1.1.'", "0",
   r"B_\infty(E_2^{pq})$ : 0, 11.1.1.", r"B_\infty(E_2^{pq})$ : \textbf{0}, 11.1.1.")
c2(162, "entry 'K^•, K_• (complexes) : 0, 11.2.1.'", "0",
   r"(complexes) : 0, 11.2.1.", r"(complexes) : \textbf{0}, 11.2.1.")
c2(162, "entry 'K^{••}, K_{••} (bicomplexes) : 0, 11.2.1.'", "0",
   r"(bicomplexes) : 0, 11.2.1.", r"(bicomplexes) : \textbf{0}, 11.2.1.")
c2(162, "entry 'B^i(K^•), ..., H^•(K^•) : 0, 11.2.1.'", "0",
   r"$H^\bullet(K^\bullet)$ : 0, 11.2.1.", r"$H^\bullet(K^\bullet)$ : \textbf{0}, 11.2.1.")
c2(162, "entry 'B_i(K_•), ..., H_•(K_•) : 0, 11.2.1.'", "0",
   r"$H_\bullet(K_\bullet)$ : 0, 11.2.1.", r"$H_\bullet(K_\bullet)$ : \textbf{0}, 11.2.1.")
c2(162, "entry 'T(K^•), T(K_•) (T foncteur) : 0, 11.2.1.'", "0",
   r"($T$ foncteur) : 0, 11.2.1.", r"($T$ foncteur) : \textbf{0}, 11.2.1.")
c2(162, "entry 'E(K^•) (K^• complexe filtré) : 0, 11.2.2.'", "0",
   r"complexe filtré) : 0, 11.2.2.", r"complexe filtré) : \textbf{0}, 11.2.2.")
c2(162, "entry 'K^{i,•}, K^{•,j}, ... H_I^p(K^{•,j}) : 0, 11.3.1.'", "0",
   r"(K^{\bullet,j})$ : 0, 11.3.1.", r"(K^{\bullet,j})$ : \textbf{0}, 11.3.1.")
c2(162, "entry 'H_II^p(K^{••}), ..., H^n(K^{••}) : 0, 11.3.1.'", "0",
   r"$H^n(K^{\bullet\bullet})$ : 0, 11.3.1.", r"$H^n(K^{\bullet\bullet})$ : \textbf{0}, 11.3.1.")
c2(162, "entry 'F_I^p(K^{••}), ..., ''E(K^{••}) : 0, 11.3.2.'", "0", r": 0, 11.3.2.", r": \textbf{0}, 11.3.2.")
c2(162, "entry 'K_{i,•}, K_{•,j}, ..., H_n(K_{••}) : 0, 11.3.5.'", "0", r": 0, 11.3.5.", r": \textbf{0}, 11.3.5.")
add(162, "entry 'R^•T(K^•) (T foncteur covariant additif) : 0, 11.4.3.'", "bold upright R (crop)",
    "\\mathrm R", "font", None, "high",
    r"$\mathrm R^\bullet T(K^\bullet)$", r"$\mathbf R^\bullet T(K^\bullet)$",
    S162 + "Hypercohomology R bold, as the hyperhomology L (GLOBAL_ISSUES 39); R^p f_* of the 12.2.1 entry is not bold.")
c2(162, "entry 'R^•T(K^•) ... : 0, 11.4.3.'", "0", r": 0, 11.4.3.", r": \textbf{0}, 11.4.3.")
add(162, "entry 'R^•T(K^•, K'^•) (T bifoncteur covariant additif) : 0, 11.4.6.'", "bold upright R (crop)",
    "\\mathrm R", "font", None, "high",
    r"$\mathrm R^\bullet T(K^\bullet,K'^{\bullet})$", r"$\mathbf R^\bullet T(K^\bullet,K'^{\bullet})$", S162)
c2(162, "entry 'R^•T(K^•, K'^•) ... : 0, 11.4.6.'", "0", r": 0, 11.4.6.", r": \textbf{0}, 11.4.6.")
add(162, "entry 'L_•T(K_•) (T foncteur covariant additif) : 0, 11.6.2.'", "bold upright L (crop)",
    "\\mathrm L", "font", None, "high",
    r"$\mathrm L_\bullet T(K_\bullet)$", r"$\mathbf L_\bullet T(K_\bullet)$", S162 + "GLOBAL_ISSUES 39.")
c2(162, "entry 'L_•T(K_•) ... : 0, 11.6.2.'", "0", r": 0, 11.6.2.", r": \textbf{0}, 11.6.2.")
add(162, "entry 'L_•T(K_•, K'_•) (T bifoncteur covariant additif) : 0, 11.6.6.'", "bold upright L (crop)",
    "\\mathrm L", "font", None, "high",
    r"$\mathrm L_\bullet T(K_\bullet,K'_\bullet)$", r"$\mathbf L_\bullet T(K_\bullet,K'_\bullet)$", S162)
c2(162, "entry 'L_•T(K_•, K'_•) ... : 0, 11.6.6.'", "0", r": 0, 11.6.6.", r": \textbf{0}, 11.6.6.")
add(162, "entry 'L_•T(K_{••}) (T foncteur covariant additif) : 0, 11.7.2.'", "bold upright L (crop)",
    "\\mathrm L", "font", None, "high",
    r"$\mathrm L_\bullet T(K_{\bullet\bullet})$", r"$\mathbf L_\bullet T(K_{\bullet\bullet})$", S162)
c2(162, "entry 'L_•T(K_{••}) ... : 0, 11.7.2.'", "0", r"0, 11.7.2.", r"\textbf{0}, 11.7.2.")
c2(162, "entry '|σ|, Σ(A), C_•(A), L_•(A) ... : 0, 11.8.1.'", "0",
   r"simplexe de $A$) : 0, 11.8.1.", r"simplexe de $A$) : \textbf{0}, 11.8.1.")
c2(162, "entry 'C^•(A, B; 𝒮), L^•(A, B; 𝒮) ... : 0, 11.8.4.'", "0", r": 0, 11.8.4.", r": \textbf{0}, 11.8.4.")
add(162, "entry 'P^•(A, B, 𝒮) (A, B ensembles finis, 𝒮 système de coefficients) : 0, 11.8.6.'",
    "P^•(A, B, 𝒮): a comma before 𝒮 (crop)", "$\\mathrm P^\\bullet(A,B,\\mathscr S)$ (printed reading kept)",
    "misprint_in_print", None, "medium", None, None,
    S162 + "The neighbouring entries (11.8.4, 11.8.8, 11.8.10) and the body (11.8.6), P^•(A, B; Γ), have a semicolon.",
    corrected=r"$\mathrm P^\bullet(A,B;\mathscr S)$")
c2(162, "entry 'P^•(A, B, 𝒮) ... : 0, 11.8.6.'", "0", r": 0, 11.8.6.", r": \textbf{0}, 11.8.6.")
c2(162, "entry 'C^•(A, B; 𝒮^•), L^•(A, B; 𝒮^•) ... : 0, 11.8.8.'", "0", r": 0, 11.8.8.", r": \textbf{0}, 11.8.8.")
c2(162, "entry 'P^•(A, B; 𝒮^•) ... : 0, 11.8.10.'", "0", r": 0, 11.8.10.", r": \textbf{0}, 11.8.10.")
c2(162, "entry 'χ(M^•) ... : 0, 11.10.1.'", "0", r"0, 11.10.1.", r"\textbf{0}, 11.10.1.")
add(162, "entry 'C^•(𝔘, ℱ) (ℱ faisceau de groupes abéliens sur X, 𝔘 recouvrement ouvert de X) : 0, 12.1.2.'",
    "plain C^•, no check accent (crop)", "$\\check C^\\bullet$", "extra", None, "high",
    r"$\check C^\bullet(\mathfrak U,\mathcal F)$", r"$C^\bullet(\mathfrak U,\mathcal F)$",
    S162 + "The \\check left on III p. 162 in GLOBAL_ISSUES 37.")
c2(162, "entry 'C^•(𝔘, ℱ) ... : 0, 12.1.2.'", "0", r": 0, 12.1.2.", r": \textbf{0}, 12.1.2.")
c2(162, "entry 'R^p f_*(ℱ) ... : 0, 12.2.1.'", "0", r": 0, 12.2.1.", r": \textbf{0}, 12.2.1.")
add(162, "entry 12.4.1: 'ℋ^p(f, 𝒦^•)'", "second (roundhand) script H (crop)", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H^p(f,\mathcal K^\bullet)$", r"$\mathscr H^p(f,\mathcal K^\bullet)$",
    S162 + "Same letter as the hypercohomology H of the body (0_III pp. 62-64); fix form as proposed there, pending the GLOBAL_ISSUES 42 decision.")
add(162, "entry 12.4.1: 'ℋ_f^p(𝒦^•)'", "second (roundhand) script H (crop)", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H_f^p(\mathcal K^\bullet)$", r"$\mathscr H_f^p(\mathcal K^\bullet)$",
    S162 + "As the preceding finding (GLOBAL_ISSUES 42).")
add(162, "entry 12.4.1: ''ℰ(f, 𝒦^•), ''ℰ(f, 𝒦^•)'", "script E in both spectral sequences (crop)", "plain E (twice)",
    "font", None, "high",
    r"${}'E(f,\mathcal K^\bullet)$,¶${}''E(f,\mathcal K^\bullet)$",
    r"${}'\mathcal E(f,\mathcal K^\bullet)$,¶${}''\mathcal E(f,\mathcal K^\bullet)$",
    S162 + "As in the body (0_III p. 62 findings: 'E, ''E of (12.4.1) printed with the script E). The 'E, ''E of the 11.3.2 entry are roman, as in the TeX.")
c2(162, "entry 'ℋ^p(f, 𝒦^•), ... : 0, 12.4.1.'", "0", r": 0, 12.4.1.", r": \textbf{0}, 12.4.1.")
c2(162, "entry 'H^•(X, 𝒦^•), H^•(V, 𝒦^•) ... : 0, 12.4.2.'", "0", r"0, 12.4.2.", r"\textbf{0}, 12.4.2.")
add(162, "entry 'gr^•(A) (A système projectif vérifiant (ML)) : 0, 13.4.2.'", "'gr' bold (crop)",
    "\\operatorname{gr} (regular weight)", "font", None, "high",
    r"$\operatorname{gr}^\bullet", r"$\mathbf{gr}^\bullet", S162)
add(162, "same entry: 'gr^•(A) (A système projectif ...)'", "both A bold upright (crop)", "$A$ (plain italic)",
    "font", None, "high",
    r"(A)$ ($A$ système", r"(\mathbf A)$ ($\mathbf A$ système",
    S162 + "The body (13.4.2) writes the projective system as $\\mathbf A$.")
c2(162, "entry 'gr^•(A) ... : 0, 13.4.2.'", "0", r"0, 13.4.2.", r"\textbf{0}, 13.4.2.")
c2(162, "entry 'E(A) (A objet filtré) : 0, 13.6.4.'", "0", r": 0, 13.6.4.", r": \textbf{0}, 13.6.4.")
c2(162, "entry 'K_•(f), i_f ... : III, 1.1.1.'", "III", r"III, 1.1.1.", r"\textbf{III}, 1.1.1.")
c2(162, "entry 'K^•(f, M), K_•(f, M) ... : III, 1.1.2.'", "III", r"III, 1.1.2.", r"\textbf{III}, 1.1.2.")
c2(162, "entry 'H^•(f, M), H_•(f, M) ... : III, 1.1.3.'", "III", r"III, 1.1.3.", r"\textbf{III}, 1.1.3.")
c2(162, "entry 'C^•((f), M), H^•((f), M) ... : III, 1.1.6.'", "III", r"III, 1.1.6.", r"\textbf{III}, 1.1.6.")
add(162, "entry 2.1.1: 'H^•(U, ℱ(*))'", "ℱ(*) with (*) on the line (crop)", "$\\mathcal F^{(*)}$ (superscript)",
    "formula", None, "high",
    r"$H^\bullet(U,\mathcal F^{(*)})$", r"$H^\bullet(U,\mathcal F(*))$",
    S162 + "As in the body (2.1.1.2): H^•(U, ℱ(*)).")
add(162, "entry 2.1.1: 'H^•(𝔘, ℱ(*))'", "ℱ(*) with (*) on the line (crop)", "$\\mathcal F^{(*)}$ (superscript)",
    "formula", None, "high",
    r"$H^\bullet(\mathfrak U,\mathcal F^{(*)})$", r"$H^\bullet(\mathfrak U,\mathcal F(*))$",
    S162 + "As in the body (2.1.1.3).")
c2(162, "entry 'H^•(U, ℱ(*)), H^•(𝔘, ℱ(*)) ... : III, 2.1.1.'", "III", r"III, 2.1.1.", r"\textbf{III}, 2.1.1.")

# ---------------------------------------------------------------- page 163
c2(163, "'Aboutissement d'une suite spectrale : 0, 11.1.1.'", "0", r": 0, 11.1.1.", r": \textbf{0}, 11.1.1.")
add(163, "'Algébrisable (𝒪_X̂-Module) : III, 5.2.1.'", "𝒪 with subscript X̂ (hat over the X; 3x crop)",
    "$\\mathcal O_X$ (no hat)", "formula", None, "high",
    r"Algébrisable ($\mathcal O_X$-Module)", r"Algébrisable ($\mathcal O_{\widehat X}$-Module)",
    "The printed reading is right: (5.2.1) defines algebrisable 𝒪_X̂-Modules on the completion X̂.")
c2(163, "'Algébrisable (𝒪_X̂-Module) : III, 5.2.1.'", "III", r"III, 5.2.1.", r"\textbf{III}, 5.2.1.")
c2(163, "'Algébrisable (schéma formel) : III, 5.4.2.'", "III", r"III, 5.4.2.", r"\textbf{III}, 5.4.2.")
c2(163, "'Analytiquement intègre (anneau) : III, 4.3.6.'", "III", r"III, 4.3.6.", r"\textbf{III}, 4.3.6.")
c2(163, "'Application quasi-compacte : 0, 9.1.1.'", "0", r": 0, 9.1.1.", r": \textbf{0}, 9.1.1.")
c2(163, "'Augmentation d'une résolution : 0, 11.4.1.'", "0", r": 0, 11.4.1.", r": \textbf{0}, 11.4.1.")
c2(163, "'Caractéristique d'Euler-Poincaré d'un complexe : 0, 11.10.1.'", "0", r": 0, 11.10.1.", r": \textbf{0}, 11.10.1.")
c2(163, "'Caractéristique d'Euler-Poincaré d'un 𝒪_X-Module cohérent (...) : III, 2.5.1.'", "III",
   r"artinien) : III, 2.5.1.", r"artinien) : \textbf{III}, 2.5.1.")
c2(163, "'Cochaîne bi-alternée : 0, 11.8.4.'", "0", r": 0, 11.8.4.", r": \textbf{0}, 11.8.4.")
c2(163, "'Complexe défini par un bicomplexe : 0, 11.3.1.'", "0", r": 0, 11.3.1.", r": \textbf{0}, 11.3.1.")
c2(163, "'Complexe de l'algèbre extérieure : III, 1.1.1.'", "III", r"III, 1.1.1.", r"\textbf{III}, 1.1.1.")
c2(163, "'Condition (ML) : 0, 13.1.2.'", "0", r": 0, 13.1.2.", r": \textbf{0}, 13.1.2.")
c2(163, "'Constructible (partie, ensemble) : 0, 9.1.2.'", "0", r": 0, 9.1.2.", r": \textbf{0}, 9.1.2.")
c2(163, "'Constructible (fonction) : 0, 9.3.1.'", "0", r": 0, 9.3.1.", r": \textbf{0}, 9.3.1.")
c2(163, "'Cup-produit : 0, 12.1.2.'", "0", r": 0, 12.1.2.", r": \textbf{0}, 12.1.2.")
c2(163, "'Dihomomorphisme pour les structures algébriques sur les catégories : 0, 8.2.1.'", "0",
   r"catégories : 0, 8.2.1.¶¶Exact", r"catégories : \textbf{0}, 8.2.1.¶¶Exact")
c2(163, "'Exact (sous-ensemble) dans une catégorie abélienne : III, 3.1.1.'", "III", r"III, 3.1.1.", r"\textbf{III}, 3.1.1.")
c2(163, "'Essentiellement constant (système projectif) : 0, 13.4.2.'", "0", r": 0, 13.4.2.", r": \textbf{0}, 13.4.2.")
c2(163, "'Factorisation de Stein : III, 4.3.3.'", "III", r"III, 4.3.3.", r"\textbf{III}, 4.3.3.")
c2(163, "'Filtration co-discrète, ..., séparée : 0, 11.1.3.'", "0", r"0, 11.1.3.", r"\textbf{0}, 11.1.3.")
c2(163, "'Final (objet) d'une catégorie : 0, 8.1.10.'", "0", r": 0, 8.1.10.", r": \textbf{0}, 8.1.10.")
c2(163, "'Fini (morphisme) de préschémas formels : III, 4.8.2.'", "III",
   r"formels : III, 4.8.2.", r"formels : \textbf{III}, 4.8.2.")
c2(163, "'Fini (préschéma formel) au-dessus de 𝔜, 𝔜-fini (préschéma formel) : III, 4.8.2.'", "III",
   r"formel) : III, 4.8.2.", r"formel) : \textbf{III}, 4.8.2.")
add(163, "'Foncteur covariant canonique C→Hom(C^0, Ens) : 0, 8.1.2.'",
    "C, Hom, C^0 and Ens bold italic (crop)", "$C\\to\\operatorname{Hom}(C^o,\\mathbf{Ens})$", "font", None, "high",
    r"$C\to\operatorname{Hom}(C^o,\mathbf{Ens})$",
    r"$\boldsymbol{C}\to\boldsymbol{\mathit{Hom}}(\boldsymbol{C}^0,\boldsymbol{\mathit{Ens}})$",
    "Form as in 0_III p. 5 (GLOBAL_ISSUES 33). The edit also writes the exponent as the figure 0 (next finding).")
add(163, "same entry: exponent of C^0", "superscript figure 0 (a narrow oval, not the round letter o of 'Hom')",
    "C^o (letter o; the body writes C^0 everywhere, e.g. (8.1.1))", "symbol", None, "medium", None, None,
    "Included in the edit of the preceding finding.")
c2(163, "'Foncteur covariant canonique ... : 0, 8.1.2.'", "0", r"0, 8.1.2.", r"\textbf{0}, 8.1.2.")
c2(163, "'Genre arithmétique : III, 2.5.1.'", "III", r"arithmétique : III, 2.5.1.", r"arithmétique : \textbf{III}, 2.5.1.")
c2(163, "'Géométriquement connexe (fibre) : III, 4.3.4.'", "III", r"III, 4.3.4.", r"\textbf{III}, 4.3.4.")
c2(163, "'Homomorphisme de structures algébriques sur les catégories : 0, 8.2.1.'", "0",
   r"catégories : 0, 8.2.1.¶¶Hypercohomologie", r"catégories : \textbf{0}, 8.2.1.¶¶Hypercohomologie")
c2(163, "'Hypercohomologie d'un foncteur par rapport à un complexe K^• : 0, 11.4.3.'", "0",
   r"0, 11.4.3.", r"\textbf{0}, 11.4.3.")
c2(163, "'Hypercohomologie d'un bifoncteur ... K^•, K'^• : 0, 11.4.6.'", "0", r": 0, 11.4.6.", r": \textbf{0}, 11.4.6.")
c2(163, "'Hyperhomologie d'un foncteur par rapport à un complexe K_• : 0, 11.6.2.'", "0",
   r"0, 11.6.2.", r"\textbf{0}, 11.6.2.")
c2(163, "'Hyperhomologie d'un bifoncteur ... K_•, K'_• : 0, 11.6.6.'", "0", r": 0, 11.6.6.", r": \textbf{0}, 11.6.6.")
c2(163, "'Hyperhomologie d'un foncteur par rapport à un bicomplexe : 0, 11.7.2.'", "0",
   r": 0, 11.7.2.", r": \textbf{0}, 11.7.2.")
c2(163, "'Localement constructible (ensemble) : 0, 9.1.11.'", "0", r": 0, 9.1.11.", r": \textbf{0}, 9.1.11.")
c2(163, "'Loi de composition externe (interne) sur les objets d'une catégorie : 0, 8.2.1.'", "0",
   r"catégorie :¶0, 8.2.1.", r"catégorie :¶\textbf{0}, 8.2.1.")

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for p in sorted({d["page"] for d in F}):
    texts[p] = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
for d in F:
    if d["fix"] is None:
        continue
    n = texts[d["page"]].count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
# sequential application in list order: every old must still occur exactly once when its turn comes
work = dict(texts)
for d in F:
    if d["fix"] is None:
        continue
    t = work[d["page"]]
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("SEQUENTIAL FAIL", d["page"], n, repr(d["fix"]["old"]))
        continue
    work[d["page"]] = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
# reverse order too (shows order dependencies)
work = dict(texts)
for d in reversed(F):
    if d["fix"] is None:
        continue
    t = work[d["page"]]
    if t.count(d["fix"]["old"]) != 1:
        print("ORDER-DEPENDENT (fails when applied in reverse order):", d["page"], repr(d["fix"]["old"][:60]))
        continue
    work[d["page"]] = t.replace(d["fix"]["old"], d["fix"]["new"], 1)

counts = {}
for d in F:
    c = counts.setdefault(d["page"], {"normal": 0, "convention": 0, "misprint": 0})
    if d["kind"] == "convention":
        c["convention"] += 1
    elif d["kind"] == "misprint_in_print":
        c["misprint"] += 1
    else:
        c["normal"] += 1
print("all unique and sequentially applicable:", ok)
print(counts, "total", len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
