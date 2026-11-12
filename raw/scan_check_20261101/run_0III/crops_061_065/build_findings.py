"""Build findings_061_065.json; newline in old/new/corrected strings is written as the pilcrow sign."""
import json, pathlib, sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "findings_061_065.json"
NL = "\u00b6"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    fix = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n") if corrected is not None else None
    d["note"] = note
    F.append(d)


WRAP = ("The proposition environment is \\itshape, so the \\emph wrapper sets the statement upright; "
        "the print sets it italic. Drop the wrapper (FIX_POLICY 2.6).")

# ---------------------------------------------------------------- page 61
add(61, "Proposition (12.3.4), first sentence",
    "italic statement; 'plat' printed roman",
    "\\emph{Soit ... Modules.} inside the italic proposition environment (comes out upright; 'plat' unmarked)",
    "convention", 6, "high",
    r"\emph{Soit $f:X\to Y$ un morphisme plat d'espaces annelés, et soient¶$\mathcal F$, $\mathcal G$ deux $\mathcal O_Y$-Modules.}",
    r"Soit $f:X\to Y$ un morphisme \textup{plat} d'espaces annelés, et soient¶$\mathcal F$, $\mathcal G$ deux $\mathcal O_Y$-Modules.",
    WRAP + " 'plat' is roman in the print (crop), hence \\textup{plat}.")
add(61, "Proposition (12.3.4) (i), opening of the italic text",
    "(i) Il existe un homomorphisme ... (italic)",
    "\\emph{Il existe ... 4.4.6}).} inside the italic environment (comes out upright)",
    "convention", 6, "high",
    r"\item[{\rm(i)}] \emph{Il existe un homomorphisme",
    r"\item[{\rm(i)}] Il existe un homomorphisme",
    WRAP + " Opening brace of the (i) wrapper; apply together with the next two fixes (closing braces).")
add(61, "Proposition (12.3.4), end of (i) / start of (ii)",
    "(i) and (ii) statements italic",
    "closing brace of the (i) wrapper and \\emph{ opening the (ii) wrapper",
    "convention", 6, "high",
    r"4.4.6}).}¶¶\item[{\rm(ii)}] \emph{Il existe",
    r"4.4.6}).¶¶\item[{\rm(ii)}] Il existe",
    WRAP + " Apply together with the (i) opening fix and the (ii) closing fix.")
add(61, "Proposition (12.3.4) (ii), end: 'déduits de (12.3.4.1) et de (12.1.3.1).'",
    "italic statement",
    "closing brace of the (ii) \\emph wrapper",
    "convention", 6, "high",
    r"{12.1.3.1}).}",
    r"{12.1.3.1}).",
    WRAP + " Apply together with the two preceding fixes.")
add(61, "Proposition (12.3.4) (i): 'à l'homomorphisme canonique (0_I, 4.4.6)'",
    "bold 0 in (0_I, 4.4.6)", "plain 0\\textsubscript{I}", "convention", 2, "high",
    r"canonique¶(\hyperref[0.4.4.6-fr]{0\textsubscript{I}",
    r"canonique¶(\hyperref[0.4.4.6-fr]{\textbf{0}\textsubscript{I}",
    "Bold 0 in the print.")
add(61, "(12.3.4.1)",
    "f^*(Ext^._{O_Y}(F, G)) with an isomorphism arrow (tilde over the arrow) to Ext^._{O_X}(f^*(F), f^*(G))",
    "\\xrightarrow{\\sim} (keeps the printed reading)",
    "misprint_in_print", None, "high", None, None,
    "Crop: the print has the tilde arrow. It overclaims: (i) speaks of a homomorphism, Proposition (12.3.5) proves bijectivity "
    "only under coherence hypotheses, and in degree 0 the map can fail to be bijective for flat f (Spec Q -> Spec Z, "
    "F = direct sum of countably many O_Y, G = O_Y: at the generic point the map is the inclusion of the sequences of "
    "rationals with bounded denominators into the product of Q). The diplomatic TeX keeps the printed tilde arrow; "
    "the corrected edition should have a plain arrow.",
    corrected=r"\longrightarrow")
add(61, "proof (i): 'catégorie des O_Y-Modules (0_I, 6.7.2)'",
    "bold 0", "plain 0\\textsubscript{I}", "convention", 2, "high",
    r"{0\textsubscript{I}, 6.7.2}", r"{\textbf{0}\textsubscript{I}, 6.7.2}", "Bold 0 in the print.")
add(61, "proof (i): 'les foncteurs G ~> f^*(Hom(F, G)) et G ~> Hom(f^*(F), f^*(G)) sont exacts à gauche'",
    "both formulas in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"les foncteurs¶\[¶\mathcal G\leadsto¶f^*(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal G))¶\quad\hbox{et}\quad¶\mathcal G\leadsto¶\mathcal{H}om_{\mathcal O_X}(f^*(\mathcal F),f^*(\mathcal G))¶\]¶sont exacts",
    r"les foncteurs¶$\mathcal G\leadsto f^*(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal G))$ et¶$\mathcal G\leadsto\mathcal{H}om_{\mathcal O_X}(f^*(\mathcal F),f^*(\mathcal G))$¶sont exacts",
    "Layout only (display vs inline); the formulas match.")
add(61, "proof (i): 'on déduit canoniquement de (0_I, 4.4.6) un homomorphisme'",
    "bold 0", "plain 0\\textsubscript{I}", "convention", 2, "high",
    r"{0\textsubscript{I}, 4.4.6}) un", r"{\textbf{0}\textsubscript{I}, 4.4.6}) un", "Bold 0 in the print.")
add(61, "proof (i): '... leurs foncteurs dérivés. Pour calculer ces derniers'",
    "same paragraph ('Pour' at the left margin, not indented)", "blank line: new paragraph", "other", None, "high",
    r"foncteurs dérivés.¶¶Pour calculer", r"foncteurs dérivés.¶Pour calculer",
    "The print has no paragraph break here.")
add(61, "proof (i): 'on a donc des morphismes H^p(...) -> H^p(...) de cohomologies'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"morphismes¶\[¶\mathcal H^p(f^*(\mathcal{H}om_{\mathcal O_Y}¶(\mathcal F,\mathcal L^\bullet)))¶\longrightarrow¶\mathcal H^p(\mathcal{H}om_{\mathcal O_X}¶(f^*(\mathcal F),f^*(\mathcal L^\bullet)))¶\]¶de cohomologies",
    r"morphismes¶$\mathcal H^p(f^*(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal L^\bullet)))\longrightarrow\mathcal H^p(\mathcal{H}om_{\mathcal O_X}(f^*(\mathcal F),f^*(\mathcal L^\bullet)))$¶de cohomologies",
    "Layout only (display vs inline).")
add(61, "proof (i): 'on a H^p(...) = f^*(H^p(...)) = f^*(Ext^p(F, G)) par définition'",
    "formula in the running text (justified line ending 'par définition.')", "displayed with \\[ ... \\]",
    "other", None, "high",
    r"on a¶\[¶\mathcal H^p(f^*(\mathcal{H}om_{\mathcal O_Y}¶(\mathcal F,\mathcal L^\bullet)))¶=f^*(\mathcal H^p(\mathcal{H}om_{\mathcal O_Y}¶(\mathcal F,\mathcal L^\bullet)))¶=f^*(\mathcal{E}xt_{\mathcal O_Y}^p(\mathcal F,\mathcal G))¶\]¶par définition.",
    r"on a¶$\mathcal H^p(f^*(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal L^\bullet)))=f^*(\mathcal H^p(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal L^\bullet)))=f^*(\mathcal{E}xt_{\mathcal O_Y}^p(\mathcal F,\mathcal G))$¶par définition.",
    "Layout only (display vs inline).")
add(61, "proof (i): 'f^*(L^.) est une résolution de f^*(G)'",
    "'résolution' in italics", "résolution upright", "italics", None, "high",
    r"une résolution de $f^*(\mathcal G)$", r"une \emph{résolution} de $f^*(\mathcal G)$",
    "Checked on a crop.")
add(61, "proof (ii): 'de O_X-Modules f^*(Hom(F, L^.)) -> Hom(f^*(F), L'^.). Soit'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"faisceaux de $\mathcal O_X$-Modules¶\[¶f^*(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal L^\bullet))¶\longrightarrow¶\mathcal{H}om_{\mathcal O_X}(f^*(\mathcal F),\mathcal L'^\bullet).¶\]¶Soit",
    r"faisceaux de $\mathcal O_X$-Modules¶$f^*(\mathcal{H}om_{\mathcal O_Y}(\mathcal F,\mathcal L^\bullet))\longrightarrow\mathcal{H}om_{\mathcal O_X}(f^*(\mathcal F),\mathcal L'^\bullet)$.¶Soit",
    "Layout only (display vs inline).")
add(61, "proof (ii): 'du complexe Hom_{O_X}(f^*(F), L'^.)), il y a donc (11.4.2)'",
    "two closing parentheses after L'^. (one unmatched)", "one closing parenthesis",
    "misprint_in_print", None, "high",
    r"\mathcal L'^\bullet)$, il y a", r"\mathcal L'^\bullet))$, il y a",
    "Crop: the print has '))'; no parenthesis is open before 'Hom'. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"\mathcal L'^\bullet)$, il y a")
add(61, "proof (ii): 'un homomorphisme (déterminé à homotopie près) f^*(M^..) -> M'^.. compatible'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"homotopie près)¶\[¶f^*(\mathcal M^{\bullet\bullet})\longrightarrow¶\mathcal M'^{\bullet\bullet}¶\]¶compatible",
    r"homotopie près)¶$f^*(\mathcal M^{\bullet\bullet})\longrightarrow\mathcal M'^{\bullet\bullet}$¶compatible",
    "Layout only (display vs inline).")
add(61, "Proposition (12.3.5)",
    "italic statement", "\\emph{Sous ... bijectifs.} inside the italic proposition environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{Sous les hypothèses de (\hyperref[0.12.3.4-fr]{12.3.4}), supposons en¶outre le faisceau d'anneaux $\mathcal O_Y$ cohérent; alors, pour tout¶$\mathcal O_Y$-Module cohérent $\mathcal F$, les homomorphismes canoniques¶(\hyperref[0.12.3.4.1-fr]{12.3.4.1}) sont bijectifs.}",
    r"Sous les hypothèses de (\hyperref[0.12.3.4-fr]{12.3.4}), supposons en¶outre le faisceau d'anneaux $\mathcal O_Y$ cohérent; alors, pour tout¶$\mathcal O_Y$-Module cohérent $\mathcal F$, les homomorphismes canoniques¶(\hyperref[0.12.3.4.1-fr]{12.3.4.1}) sont bijectifs.",
    WRAP)

# ---------------------------------------------------------------- page 62
add(62, "proof of (12.3.5): 'une suite exacte 0 -> R -> O_Y^n -> F -> 0, et R est alors'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"exacte¶\[¶0\longrightarrow\mathcal R\longrightarrow\mathcal O_Y^n¶\longrightarrow\mathcal F\longrightarrow0,¶\]¶et $\mathcal R$",
    r"exacte $0\longrightarrow\mathcal R\longrightarrow\mathcal O_Y^n\longrightarrow\mathcal F\longrightarrow0$,¶et $\mathcal R$",
    "Layout only (display vs inline).")
add(62, "proof of (12.3.5): 'O_Y-Module cohérent (0_I, 5.3.4)'",
    "bold 0", "plain 0\\textsubscript{I}", "convention", 2, "high",
    r"{0\textsubscript{I}, 5.3.4}", r"{\textbf{0}\textsubscript{I}, 5.3.4}", "Bold 0 in the print.")
add(62, "proof of (12.3.5): 'la proposition résultant de (0_I, 6.7.6.1)'",
    "bold 0", "plain 0\\textsubscript{I}", "convention", 2, "high",
    r"{0\textsubscript{I}, 6.7.6.1}", r"{\textbf{0}\textsubscript{I}, 6.7.6.1}", "Bold 0 in the print.")
add(62, "commutative diagram, end of the bottom row: 'Ext^p_{O_X}(O_X^n, f^*(G))'",
    "no full stop after the last entry (the sentence continues with 'puisque')", "full stop after the last entry",
    "punctuation", None, "high",
    r"f^*(\mathcal G)).¶}", r"f^*(\mathcal G))¶}",
    "Checked on a crop.")
add(62, "'on a Ext^p_{O_Y}(O_Y^n, G) = 0 pour tout p>0 et de même Ext^p_{O_X}(O_X^n, f^*(G)) = 0 pour tout p>0 (T, 4.2.3)'",
    "formulas in the running text (a justified line)", "displayed with \\[ ... \\]", "other", None, "high",
    r"on a¶\[¶\mathcal{E}xt_{\mathcal O_Y}^p(\mathcal O_Y^n,\mathcal G)=0¶\quad\hbox{pour tout }p>0¶\quad\hbox{et de même}\quad¶\mathcal{E}xt_{\mathcal O_X}^p(\mathcal O_X^n,f^*(\mathcal G))=0¶\quad\hbox{pour tout }p>0¶\]¶(T, 4.2.3).",
    r"on a¶$\mathcal{E}xt_{\mathcal O_Y}^p(\mathcal O_Y^n,\mathcal G)=0$ pour tout $p>0$ et de même¶$\mathcal{E}xt_{\mathcal O_X}^p(\mathcal O_X^n,f^*(\mathcal G))=0$ pour tout $p>0$¶(T, 4.2.3).",
    "Layout only (display vs inline).")
add(62, "end of the proof: 'donc f^*(Ext^p(F, G)) -> Ext^p(f^*(F), f^*(G)) est un isomorphisme.'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"donc¶\[¶f^*(\mathcal{E}xt_{\mathcal O_Y}^p(\mathcal F,\mathcal G))¶\longrightarrow¶\mathcal{E}xt_{\mathcal O_X}^p(f^*(\mathcal F),f^*(\mathcal G))¶\]¶est un isomorphisme.",
    r"donc¶$f^*(\mathcal{E}xt_{\mathcal O_Y}^p(\mathcal F,\mathcal G))\longrightarrow\mathcal{E}xt_{\mathcal O_X}^p(f^*(\mathcal F),f^*(\mathcal G))$¶est un isomorphisme.",
    "Layout only (display vs inline). The earlier occurrence ('Pour prouver que les homomorphismes') is displayed in the print too.")
add(62, "heading 12.4",
    "'12.4. Hypercohomologie du foncteur image directe.' (final full stop)", "no full stop", "punctuation", None, "high",
    r"\subsection{Hypercohomologie du foncteur image directe}",
    r"\subsection{Hypercohomologie du foncteur image directe.}",
    "None of the 56 \\subsection titles in ega3-1-fr.tex has the printed final full stop (see final message).")
add(62, "(12.4.1): 'par rapport à un complexe quelconque de O_X-Modules'",
    "'quelconque' in italics", "upright", "italics", None, "high",
    r"un complexe quelconque de", r"un complexe \emph{quelconque} de", "Checked on a crop.")
add(62, "(12.4.1): 'Les O_Y-Modules d'hypercohomologie R^p f_*(K^.)'",
    "bold upright R", "plain R", "font", None, "high",
    r"$R^p f_*(\mathcal K^\bullet)$", r"$\mathbf{R}^p f_*(\mathcal K^\bullet)$",
    "Crop: bold R here; the later R^p f_* in (12.4.1.2) and 'au lieu de R^p f_*(F)' are not bold.")
HNOTE = ("Crop: the hypercohomology H in the text of (12.4.1) ('se noteront aussi H^p(f, K^.) ou H_f^p(K^.)', 'Rappelons que "
         "H^.(f, K^.)', 'O_X-Modules; H^.(f, K^.) est') is a second, lighter roundhand script H, unlike the usual script H of "
         "Hom and of (12.4.1.1)-(12.4.1.2) and 'on écrit H^p(f, F)'. \\mathscr is proposed because ega3-1 uses \\mathcal for "
         "the usual script; this needs one decision (see final message).")
add(62, "(12.4.1): 'se noteront aussi H^p(f, K^.)'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H^p(f,\mathcal K^\bullet)$ ou", r"$\mathscr H^p(f,\mathcal K^\bullet)$ ou", HNOTE)
add(62, "(12.4.1): 'ou H_f^p(K^.)'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H_f^p(\mathcal K^\bullet)$", r"$\mathscr H_f^p(\mathcal K^\bullet)$", HNOTE)
add(62, "(12.4.1): 'Rappelons que H^.(f, K^.) est la cohomologie'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"Rappelons que¶$\mathcal H^\bullet(f,\mathcal K^\bullet)$", r"Rappelons que¶$\mathscr H^\bullet(f,\mathcal K^\bullet)$", HNOTE)
add(62, "(12.4.1): 'O_X-Modules; H^.(f, K^.) est l'aboutissement'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"Modules~; $\mathcal H^\bullet(f,\mathcal K^\bullet)$", r"Modules~; $\mathscr H^\bullet(f,\mathcal K^\bullet)$", HNOTE)
ENOTE = "Crop: the spectral sequences 'E, ''E of (12.4.1) are printed with the script E (as in Ext); the E_2 of 'les termes E_2' is roman."
add(62, "(12.4.1): 'deux suites spectrales 'E(f, K^.) et ''E(f, K^.) dont'",
    "script E (twice)", "plain E", "font", None, "high",
    r"${}'E(f,\mathcal K^\bullet)$ et ${}''E(f,\mathcal K^\bullet)$ dont",
    r"${}'\mathcal E(f,\mathcal K^\bullet)$ et ${}''\mathcal E(f,\mathcal K^\bullet)$ dont", ENOTE)
add(62, "(12.4.1.1)", "script E in 'E_2^{pq}", "plain E", "font", None, "high",
    r"{}'E_2^{pq}", r"{}'\mathcal E_2^{pq}", ENOTE)
add(62, "(12.4.1.2)", "script E in ''E_2^{pq}", "plain E", "font", None, "high",
    r"{}''E_2^{pq}", r"{}''\mathcal E_2^{pq}", ENOTE)
add(62, "(12.4.1.2): '(= R^p f_*(H^q(K^.)))'",
    "no full stop after the formula", "full stop after the closing parenthesis", "punctuation", None, "high",
    r"(\mathcal H^q(\mathcal K^\bullet))).", r"(\mathcal H^q(\mathcal K^\bullet)))",
    "Checked on a crop.")
add(62, "(12.4.1): '... (12.4.1.2) / On a, dans ces formules, adopté'",
    "'On a, dans ces formules' begins a new (indented) paragraph", "no blank line after \\end{equation}: no paragraph break",
    "other", None, "medium",
    r"\end{equation}¶On a, dans ces formules", r"\end{equation}¶¶On a, dans ces formules",
    "Paragraph break of the print (indented line).")
add(62, "(12.4.1): 'la suite 'E(f, K^.) est toujours régulière'",
    "script E", "plain E", "font", None, "high",
    r"${}'E(f,\mathcal K^\bullet)$ est toujours", r"${}'\mathcal E(f,\mathcal K^\bullet)$ est toujours", ENOTE)
add(62, "(12.4.1): 'les deux suites spectrales 'E(f, K^.) et ''E(f, K^.) sont birégulières'",
    "script E (twice)", "plain E", "font", None, "high",
    r"${}'E(f,\mathcal K^\bullet)$ et¶${}''E(f,\mathcal K^\bullet)$ sont",
    r"${}'\mathcal E(f,\mathcal K^\bullet)$ et¶${}''\mathcal E(f,\mathcal K^\bullet)$ sont", ENOTE)

# ---------------------------------------------------------------- page 63
add(63, "(12.4.2): 'comme un cas particulier de H^.(f, K^.), où f'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H^\bullet(f,\mathcal K^\bullet)$, où", r"$\mathscr H^\bullet(f,\mathcal K^\bullet)$, où", HNOTE)
add(63, "Proposition (12.4.3), opening",
    "italic statement", "\\emph{Pour tout entier ... sur $Y$.} inside the italic proposition environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{Pour tout entier", r"Pour tout entier",
    WRAP + " Opening brace; apply together with the closing fix 'sur $Y$.}'.")
add(63, "Proposition (12.4.3), end: 'sur Y.'",
    "italic statement", "closing brace of the \\emph wrapper", "convention", 6, "high",
    r"sur $Y$.}", r"sur $Y$.",
    WRAP + " Apply together with the opening fix '\\emph{Pour tout entier'.")
add(63, "Proposition (12.4.3): 'le O_Y-Module H^p(f, K^.) est canoniquement'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H^p(f,\mathcal K^\bullet)$ est canoniquement", r"$\mathscr H^p(f,\mathcal K^\bullet)$ est canoniquement", HNOTE)
add(63, "Proposition (12.4.3): 'au préfaisceau U ~> H^p(f^{-1}(U), K^.)'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$U\mapsto\mathbf H^p", r"$U\leadsto\mathbf H^p",
    "Crop: wavy arrow (edition point for this file).")
add(63, "proof of (12.4.3): 'est associé au préfaisceau U ~> H^p(Gamma(U, f_*(L^..))) = H^p(Gamma(f^{-1}(U), L^..)). Mais'",
    "wavy arrow; the formula is in the running text", "\\longmapsto; displayed with \\[ ... \\]", "symbol", None, "high",
    r"préfaisceau¶\[¶U\longmapsto H^p(\Gamma(U,f_*(\mathcal L^{\bullet\bullet})))¶=H^p(\Gamma(f^{-1}(U),\mathcal L^{\bullet\bullet})).¶\]¶Mais",
    r"préfaisceau¶$U\leadsto H^p(\Gamma(U,f_*(\mathcal L^{\bullet\bullet})))=H^p(\Gamma(f^{-1}(U),\mathcal L^{\bullet\bullet}))$.¶Mais",
    "Crop: wavy arrow. The fix also sets the formula inline, as printed (display vs inline).")
add(63, "proof of (12.4.3): 'donc H^p(Gamma(f^{-1}(U), L^..)) = H^p(f^{-1}(U), K^.) par définition.'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"donc¶\[¶H^p(\Gamma(f^{-1}(U),\mathcal L^{\bullet\bullet}))¶=\mathbf H^p(f^{-1}(U),\mathcal K^\bullet)¶\]¶par définition.",
    r"donc¶$H^p(\Gamma(f^{-1}(U),\mathcal L^{\bullet\bullet}))=\mathbf H^p(f^{-1}(U),\mathcal K^\bullet)$¶par définition.",
    "Layout only (display vs inline).")
add(63, "Proposition (12.4.4), opening sentence",
    "italic statement", "\\emph{L'hypercohomologie ... suivants~:} inside the italic proposition environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{L'hypercohomologie", r"L'hypercohomologie",
    WRAP + " Opening brace; apply together with the closing fix 'suivants~:}'.")
add(63, "Proposition (12.4.4): 'dans chacun des cas suivants :'",
    "italic statement", "closing brace of the \\emph wrapper", "convention", 6, "high",
    r"suivants~:}", r"suivants~:",
    WRAP + " Apply together with the opening fix '\\emph{L'hypercohomologie'.")
add(63, "Proposition (12.4.4): 'L'hypercohomologie H^.(f, K^.) est un foncteur cohomologique'",
    "second (roundhand) script H", "\\mathcal H", "font", None, "medium",
    r"$\mathcal H^\bullet(f,\mathcal K^\bullet)$ est¶un foncteur", r"$\mathscr H^\bullet(f,\mathcal K^\bullet)$ est¶un foncteur", HNOTE)
add(63, "Proposition (12.4.4) a)",
    "italic (label a) upright)", "\\emph{...} item body inside the italic environment (comes out upright)", "convention", 6, "high",
    r"\emph{$\mathcal K^\bullet$ varie dans la catégorie des complexes limités¶inférieurement.}",
    r"$\mathcal K^\bullet$ varie dans la catégorie des complexes limités¶inférieurement.",
    WRAP + " The labels \\item[\\emph{a)}] come out upright, as printed.")
add(63, "Proposition (12.4.4) b)",
    "italic", "\\emph{...} item body inside the italic environment (comes out upright)", "convention", 6, "high",
    r"\emph{Il existe un entier $m$ tel que tout $\mathcal O_X$-Module admette¶une résolution flasque de longueur $\leq m$.}",
    r"Il existe un entier $m$ tel que tout $\mathcal O_X$-Module admette¶une résolution flasque de longueur $\leq m$.",
    WRAP)
add(63, "Proposition (12.4.4) c)",
    "italic ('X' upright)", "\\emph{...} item body inside the italic environment (comes out upright)", "convention", 6, "high",
    r"\emph{$X$ est un espace noethérien.}", r"$X$ est un espace noethérien.", WRAP)
add(63, "proof of (12.4.4): 'Les cas a) et b) sont des cas particuliers'",
    "a) and b) in italics", "upright", "italics", None, "high",
    r"Les cas a) et b) sont", r"Les cas \emph{a)} et \emph{b)} sont", "Checked on a crop.")
add(63, "proof of (12.4.4): 'le cas c) se déduit'",
    "c) in italics", "upright", "italics", None, "high",
    r"le cas c) se", r"le cas \emph{c)} se", "Checked on a crop.")
CNOTE = ("Crop: the print has a plain roman C (no háček) for the cochain complex in (12.4.5) and in the proof of (12.4.6); "
         "the TeX adds \\check.")
add(63, "(12.4.5): 'le bicomplexe C^.(U, K^.), dont'",
    "C^. without háček", "\\check C^\\bullet", "symbol", None, "high",
    r"bicomplexe $\check C^\bullet(\mathfrak U,\mathcal K^\bullet)$", r"bicomplexe $C^\bullet(\mathfrak U,\mathcal K^\bullet)$", CNOTE)
add(63, "(12.4.5): 'le composant d'indices (i, j) est C^i(U, K^j)'",
    "C^i without háček", "\\check C^i", "symbol", None, "high",
    r"$\check C^i(\mathfrak U,\mathcal K^j)$", r"$C^i(\mathfrak U,\mathcal K^j)$", CNOTE)
add(63, "(12.4.5): 'est l'hypercohomologie du recouvrement U à coefficients dans K^.'",
    "only 'hypercohomologie' in italics", "\\emph covers 'hypercohomologie du recouvrement U à coefficients dans K^.'",
    "italics", None, "high",
    r"l'\emph{hypercohomologie du recouvrement $\mathfrak U$ à coefficients dans¶$\mathcal K^\bullet$}",
    r"l'\emph{hypercohomologie} du recouvrement $\mathfrak U$ à coefficients dans¶$\mathcal K^\bullet$",
    "Checked on a crop.")
add(63, "(12.4.5): 'et nous la noterons H^.(U, K^.) = H^.(C^.(U, K^.)). La suite spectrale'",
    "C^. without háček; the formula is in the running text", "\\check C^\\bullet; displayed with \\[ ... \\]",
    "symbol", None, "high",
    r"noterons¶\[¶\mathbf H^\bullet(\mathfrak U,\mathcal K^\bullet)¶=H^\bullet(\check C^\bullet(\mathfrak U,\mathcal K^\bullet)).¶\]¶La suite",
    r"noterons¶$\mathbf H^\bullet(\mathfrak U,\mathcal K^\bullet)=H^\bullet(C^\bullet(\mathfrak U,\mathcal K^\bullet))$.¶La suite",
    CNOTE + " The fix also sets the formula inline, as printed (display vs inline).")
add(63, "Proposition (12.4.6), statement before (12.4.6.1)",
    "italic statement", "\\emph{Soit ... donné par} inside the italic proposition environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{Soit $\mathcal K^\bullet=(\mathcal K^i)$ un complexe de¶$\mathcal O_X$-Modules. Il existe un foncteur spectral régulier en¶$\mathcal K^\bullet$ ayant pour aboutissement l'hypercohomologie¶$\mathbf H^\bullet(X,\mathcal K^\bullet)$, et dont le terme $E_2$ est donné¶par}",
    r"Soit $\mathcal K^\bullet=(\mathcal K^i)$ un complexe de¶$\mathcal O_X$-Modules. Il existe un foncteur spectral régulier en¶$\mathcal K^\bullet$ ayant pour aboutissement l'hypercohomologie¶$\mathbf H^\bullet(X,\mathcal K^\bullet)$, et dont le terme $E_2$ est donné¶par",
    WRAP)
add(63, "(12.4.6.1): left side E_2^{pq}",
    "bold E (E_2^{pq} set in bold; the statement's 'le terme E_2' is roman)", "plain E", "font", None, "medium",
    r"E_2^{pq}=", r"\mathbf{E}_2^{pq}=",
    "Crop at 7x: E clearly bold, like the bold H after it; the subscript 2 and pq also look heavier. Possibly a wrong-font "
    "slip (then also a MISPRINTS entry with the reading E_2^{pq}); the diplomatic text has the bold E either way.")
add(63, "(12.4.6.1): right side H^p(U, h^q(K^.))",
    "bold H (the covering hypercohomology of (12.4.5)), no háček", "\\check H^p", "symbol", None, "high",
    r"\check H^p(\mathfrak U,h^q", r"\mathbf H^p(\mathfrak U,h^q",
    "Crop: bold H without háček, the notation H^.(U, K^.) of (12.4.5) applied to the complex of presheaves h^q(K^.).")
add(63, "(12.4.6.1): end of the formula",
    "no comma after the formula", "comma after the closing parenthesis", "punctuation", None, "high",
    r"(\mathcal K^\bullet)),¶\end{equation}", r"(\mathcal K^\bullet))¶\end{equation}",
    "Checked on a crop.")
add(63, "Proposition (12.4.6), after (12.4.6.1), opening",
    "italic statement", "\\emph{où ... inférieurement.} inside the italic proposition environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{où $h^q(\mathcal K^\bullet)$", r"où $h^q(\mathcal K^\bullet)$",
    WRAP + " Opening brace; apply together with the closing fix 'est limité inférieurement.}'.")
add(63, "Proposition (12.4.6), end: 'si K^. est limité inférieurement.'",
    "italic statement", "closing brace of the \\emph wrapper", "convention", 6, "high",
    r"est limité inférieurement.}", r"est limité inférieurement.",
    WRAP + " Apply together with the opening fix '\\emph{où $h^q(\\mathcal K^\\bullet)$'.")
add(63, "Proposition (12.4.6): 'le complexe de préfaisceaux V ~> H^q(V, K^.) sur X'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$V\mapsto H^q(V", r"$V\leadsto H^q(V",
    "Crop: wavy arrow. The H^q here is not bold (same weight as the upright V beside it).")
add(63, "proof of (12.4.6): 'le tricomplexe C^.(U, L^..) = (C^i(U, L^{jk}))'",
    "C^. and C^i without háček", "\\check C^\\bullet, \\check C^i", "symbol", None, "high",
    r"$\check C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet})¶=(\check C^i(\mathfrak U,\mathcal L^{jk}))$",
    r"$C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet})¶=(C^i(\mathfrak U,\mathcal L^{jk}))$", CNOTE)
add(63, "proof of (12.4.6): 'car on a H^q(U, L^{jk}) = 0 pour tout q>0'",
    "bold H, no háček", "\\check H^q", "symbol", None, "high",
    r"$\check H^q(\mathfrak U,\mathcal L^{jk})=0$", r"$\mathbf H^q(\mathfrak U,\mathcal L^{jk})=0$",
    "Crop: bold H without háček (notation of (12.4.5)).")

# ---------------------------------------------------------------- page 64
add(64, "proof of (12.4.6): 'un isomorphisme canonique H^n(C^.(U, L^..)) ~-> H^n(Gamma(X, L^..)) (en vertu de'",
    "C^. without háček; the formula is in the running text", "\\check C^\\bullet; displayed with \\[ ... \\]",
    "symbol", None, "high",
    r"canonique¶\[¶H^n(\check C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet}))¶\xrightarrow{\sim}¶H^n(\Gamma(X,\mathcal L^{\bullet\bullet}))¶\]¶(en vertu",
    r"canonique¶$H^n(C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet}))\xrightarrow{\sim}H^n(\Gamma(X,\mathcal L^{\bullet\bullet}))$¶(en vertu",
    CNOTE + " The fix also sets the formula inline, as printed (display vs inline).")
add(64, "proof of (12.4.6): '(12.4.2) un isomorphisme H^n(C^.(U, L^..)) ~-> H^n(X, K^.). Considérons'",
    "C^. without háček; the formula is in the running text", "\\check C^\\bullet; displayed with \\[ ... \\]",
    "symbol", None, "high",
    r"isomorphisme¶\[¶H^n(\check C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet}))¶\xrightarrow{\sim}\mathbf H^n(X,\mathcal K^\bullet).¶\]¶Considérons",
    r"isomorphisme¶$H^n(C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet}))\xrightarrow{\sim}\mathbf H^n(X,\mathcal K^\bullet)$.¶Considérons",
    CNOTE + " The fix also sets the formula inline, as printed (display vs inline).")
add(64, "proof of (12.4.6): 'Considérons d'autre part le tricomplexe C^.(U, L^..) comme un bicomplexe'",
    "C^.(U, L^..) with roman U and roman L (not Fraktur U and script L), no háček",
    "\\check C^\\bullet(\\mathfrak U,\\mathcal L^{\\bullet\\bullet}) (silently corrected)",
    "misprint_in_print", None, "high",
    r"$\check C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet})$ comme un",
    r"$C^\bullet(U,L^{\bullet\bullet})$ comme un",
    "Crop: plain roman U and L, same weight as the C (wrong-font slip; the same tricomplex is C^.(U, L^..) with Fraktur U and "
    "script L on p. 63). The fix restores the printed reading; the TeX's háček is not printed either.",
    corrected=r"$C^\bullet(\mathfrak U,\mathcal L^{\bullet\bullet})$ comme un")
add(64, "proof of (12.4.6): 'par suite, H^q(C^i(U, L^{j,.})) n'est autre'",
    "C^i without háček", "\\check C^i", "symbol", None, "high",
    r"$H^q(\check C^i(\mathfrak U,\mathcal L^{j,\bullet}))$", r"$H^q(C^i(\mathfrak U,\mathcal L^{j,\bullet}))$", CNOTE)
add(64, "proof of (12.4.6): 'le complexe de cochaînes C^i(U, h^q(K^j))'",
    "C^i without háček", "\\check C^i", "symbol", None, "high",
    r"$\check C^i(\mathfrak U,h^q(\mathcal K^j))$", r"$C^i(\mathfrak U,h^q(\mathcal K^j))$", CNOTE)
add(64, "Corollaire (12.4.7)",
    "italic statement", "\\emph{Si, pour tout simplexe ... canonique} inside the italic corollary environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{Si, pour tout simplexe $\sigma$ du nerf de $\mathfrak U$, et pour¶tout entier $i$, on a¶$H^q(U_\sigma,\mathcal K^i)=0$ pour $q>0$, alors on a un isomorphisme¶canonique}",
    r"Si, pour tout simplexe $\sigma$ du nerf de $\mathfrak U$, et pour¶tout entier $i$, on a¶$H^q(U_\sigma,\mathcal K^i)=0$ pour $q>0$, alors on a un isomorphisme¶canonique",
    WRAP.replace("proposition", "corollary"))
add(64, "proof of (12.4.7): 'l'hypothèse entraîne que C^.(U, h^q(K^j)) = 0'",
    "C^. without háček", "\\check C^\\bullet", "symbol", None, "high",
    r"$\check C^\bullet(\mathfrak U,h^q", r"$C^\bullet(\mathfrak U,h^q", CNOTE)
add(64, "proof of (12.4.7): 'C^.(U, h^q(K^j)) = 0 pour q>0'",
    "superscript j: h^q(K^j)", "h^q(\\mathcal K^i)", "formula", None, "medium",
    r"(\mathcal K^i))=0$", r"(\mathcal K^j))=0$",
    "6x crop: the superscript has the descender with a leftward hook of the j in C^i(U, h^q(K^j)) a few lines above, "
    "unlike the i of 'H^q(U_sigma, K^i)' in the statement. Not a mathematical error (any index).")
add(64, "(12.4.8): '(12.4.8.1) / On part d'une résolution injective'",
    "'On part d'une résolution' begins a new (indented) paragraph", "no blank line after \\end{equation}: no paragraph break",
    "other", None, "medium",
    r"\end{equation}¶On part d'une", r"\end{equation}¶¶On part d'une",
    "Paragraph break of the print (indented line).")
add(64, "(12.4.8): 'un morphisme pour la cohomologie : H^.(X, K^.) -> H^.(X', psi^*(K^.)); par composition'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"cohomologie~:¶\[¶\mathbf H^\bullet(X,\mathcal K^\bullet)¶\longrightarrow\mathbf H^\bullet(X',\psi^*(\mathcal K^\bullet))~;¶\]¶par composition",
    r"cohomologie~: $\mathbf H^\bullet(X,\mathcal K^\bullet)\longrightarrow\mathbf H^\bullet(X',\psi^*(\mathcal K^\bullet))$~;¶par composition",
    "Layout only (display vs inline).")
add(64, "(12.4.8.2)",
    "second (roundhand) script H, twice", "\\mathcal H", "font", None, "medium",
    r"\mathcal H^n(g,f_*(\mathcal K^\bullet))¶\longrightarrow\mathcal H^n(h,\mathcal K^\bullet)",
    r"\mathscr H^n(g,f_*(\mathcal K^\bullet))¶\longrightarrow\mathscr H^n(h,\mathcal K^\bullet)", HNOTE)
add(64, "(12.4.8.3)",
    "second (roundhand) script H, twice", "\\mathcal H", "font", None, "medium",
    r"\mathcal H^n(h,\mathcal K^\bullet)¶\longrightarrow g_*(\mathcal H^n(f,\mathcal K^\bullet)).",
    r"\mathscr H^n(h,\mathcal K^\bullet)¶\longrightarrow g_*(\mathscr H^n(f,\mathcal K^\bullet)).", HNOTE)
add(64, "(12.4.8): '(12.4.8.3) / Nous laissons au lecteur le détail des définitions.'",
    "'Nous laissons' begins a new (indented) paragraph", "no blank line after \\end{equation}: no paragraph break",
    "other", None, "medium",
    r"\end{equation}¶Nous laissons", r"\end{equation}¶¶Nous laissons",
    "Paragraph break of the print (indented line).")
add(64, "heading 13.1",
    "'13.1. La condition de Mittag-Leffler.' (final full stop)", "no full stop", "punctuation", None, "high",
    r"\subsection{La condition de Mittag-Leffler}", r"\subsection{La condition de Mittag-Leffler.}",
    "Same as heading 12.4 (p. 62).")
BOLDC = ("Category letter C printed bold italic (as in the rest of chapter 0 of EGA III); the TeX has the script \\mathcal C. "
         "\\boldsymbol{C} as in the p. 10 fixes; GLOBAL_ISSUES 35 (no blind replace).")
add(64, "(13.1.1): 'Soit C une catégorie abélienne'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"Soit $\mathcal C$ une", r"Soit $\boldsymbol{C}$ une", BOLDC)
add(64, "(13.1.1): 'sous-objets d'un objet de C existe'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"objet de $\mathcal C$ existe", r"objet de $\boldsymbol{C}$ existe", BOLDC)
add(64, "(13.1.1): 'tout système projectif d'objets de C admet'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"d'objets de $\mathcal C$ admet", r"d'objets de $\boldsymbol{C}$ admet", BOLDC)
add(64, "(13.1.1): '(axiome AB 3*) de T, 1.5));'",
    "closing parenthesis after 'AB 3*' (the asterisk raised)", "no parenthesis after 3*", "punctuation", None, "high",
    r"AB~3* de T", r"AB~3*) de T",
    "Crop: the print reads '(axiome AB 3*) de T, 1.5));' (Tohoku labels its axioms 'AB 3*)'); the parentheses of the "
    "print do not balance either way.")

# ---------------------------------------------------------------- page 65
add(65, "(13.1.1): 'un système projectif d'objets de C dont l'ensemble d'indices'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"d'objets de $\mathcal C$ dont", r"d'objets de $\boldsymbol{C}$ dont", BOLDC)
add(65, "(13.1.1): 'l'ensemble d'indices I est filtrant à droite'",
    "'filtrant' in italics", "upright", "italics", None, "high",
    r"est filtrant à droite", r"est \emph{filtrant} à droite", "Checked on the strip.")
add(65, "(13.1.1): 'soient A = lim A_alpha et pour tout alpha in I, soit'",
    "no comma after 'et'", "'et, pour tout'", "punctuation", None, "high",
    r"A_\alpha$ et, pour tout", r"A_\alpha$ et pour tout", "Checked on a crop.")
add(65, "(13.1.1): 'le sous-objet A'_alpha = inf_{beta>=alpha} f_{alpha beta}(A_beta) est dit'",
    "formula in the running text (index under inf)", "displayed with \\[ ... \\]", "other", None, "high",
    r"le sous-objet¶\[¶A'_\alpha=\inf_{\beta\geq\alpha}f_{\alpha\beta}(A_\beta)¶\]¶est dit",
    r"le sous-objet $A'_\alpha=\inf_{\beta\geq\alpha}f_{\alpha\beta}(A_\beta)$¶est dit",
    "Layout only (display vs inline).")
add(65, "(13.1.2): 'un système projectif (A_alpha, f_{alpha beta}) dans C, on appelle'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"dans¶$\mathcal C$, on appelle", r"dans¶$\boldsymbol{C}$, on appelle", BOLDC)
add(65, "(13.1.2): label of the condition '(ML) Pour tout indice ...'",
    "(ML) in regular roman (same weight as '(ML)' in the running text)", "\\item[\\textbf{(ML)}] (bold)",
    "font", None, "high",
    r"\item[\textbf{(ML)}]", r"\item[(ML)]", "Checked on a crop.")
add(65, "(13.1.2): '(ML) ... / Il est clair que si les f_{alpha beta}'",
    "'Il est clair' begins a new (indented) paragraph", "no blank line after \\end{itemize}: unindented continuation",
    "other", None, "medium",
    r"\end{itemize}¶Il est clair", r"\end{itemize}¶¶Il est clair",
    "Paragraph break of the print (indented line).")
add(65, "(13.1.2): 'les objets A_alpha sont artiniens dans C'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"\emph{artiniens} dans $\mathcal C$", r"\emph{artiniens} dans $\boldsymbol{C}$", BOLDC)
add(65, "Remarque (13.1.3): 'lorsque C est par exemple la catégorie des ensembles'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"lorsque $\mathcal C$ est par", r"lorsque $\boldsymbol{C}$ est par", BOLDC)
add(65, "heading 13.2",
    "'13.2. La condition de Mittag-Leffler pour les groupes abéliens.' (final full stop)", "no full stop",
    "punctuation", None, "high",
    r"\subsection{La condition de Mittag-Leffler pour les groupes abéliens}",
    r"\subsection{La condition de Mittag-Leffler pour les groupes abéliens.}",
    "Same as heading 12.4 (p. 62).")
add(65, "Proposition (13.2.1): 'Soit'",
    "italic", "\\emph{Soit} inside the italic proposition environment (comes out upright)", "convention", 6, "high",
    r"\emph{Soit}", r"Soit", WRAP)
add(65, "Proposition (13.2.1): 'une suite exacte de systèmes projectifs ... d'indices I).'",
    "italic statement", "\\emph{...} inside the italic proposition environment (comes out upright)", "convention", 6, "high",
    r"\emph{une suite exacte de systèmes projectifs de groupes abéliens (relatifs¶à un même ensemble filtrant d'indices $I$).}",
    r"une suite exacte de systèmes projectifs de groupes abéliens (relatifs¶à un même ensemble filtrant d'indices $I$).",
    WRAP)
add(65, "Proposition (13.2.1) (i): 'Si (B_alpha) vérifie (ML), il en est de même de (C_alpha).'",
    "italic; '(ML)' upright", "\\emph{...} item body inside the italic environment (comes out upright)", "convention", 6, "high",
    r"\emph{Si $(B_\alpha)$ vérifie (ML), il en est de même de $(C_\alpha)$.}",
    r"Si $(B_\alpha)$ vérifie \textup{(ML)}, il en est de même de $(C_\alpha)$.",
    WRAP + " '(ML)' is upright in the print (crop), hence \\textup.")
add(65, "Proposition (13.2.1) (ii): 'Si (A_alpha) et (C_alpha) vérifient (ML), il en est de même de (B_alpha).'",
    "italic; '(ML)' upright", "\\emph{...} item body inside the italic environment (comes out upright)", "convention", 6, "high",
    r"\emph{Si $(A_\alpha)$ et $(C_\alpha)$ vérifient (ML), il en est de même de¶$(B_\alpha)$.}",
    r"Si $(A_\alpha)$ et $(C_\alpha)$ vérifient \textup{(ML)}, il en est de même de¶$(B_\alpha)$.",
    WRAP + " '(ML)' is upright in the print (crop), hence \\textup.")
add(65, "proof of (13.2.1) (i): 'on a h_{alpha beta}(C_beta) = ... = h_{alpha lambda}(C_lambda) pour lambda >= beta.'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"on a¶\[¶h_{\alpha\beta}(C_\beta)¶=v_\alpha(g_{\alpha\beta}(B_\beta))¶=v_\alpha(g_{\alpha\lambda}(B_\lambda))¶=h_{\alpha\lambda}(C_\lambda)¶\]¶pour",
    r"on a¶$h_{\alpha\beta}(C_\beta)=v_\alpha(g_{\alpha\beta}(B_\beta))=v_\alpha(g_{\alpha\lambda}(B_\lambda))=h_{\alpha\lambda}(C_\lambda)$¶pour",
    "Layout only (display vs inline).")
add(65, "proof of (13.2.1) (ii): 'Soit alors v_alpha un élément de g_{alpha gamma}(B_gamma); on a donc y_alpha = ...'",
    "v_alpha (italic v, no descender)", "y_alpha (silently corrected)", "misprint_in_print", None, "high",
    r"$y_\alpha$ un élément", r"$v_\alpha$ un élément",
    "Crop: the letter has no descender and matches the v of v_beta on the same page; the next clause 'on a donc "
    "y_alpha = g_{alpha gamma}(y_gamma)' shows that y_alpha is meant. The fix restores the printed reading.",
    corrected=r"$y_\alpha$ un élément")
add(65, "proof of (13.2.1) (ii): 'd'où v_beta(y_beta — g_{beta lambda}(y_lambda)) = 0'",
    "long dash for the subtraction", "minus sign", "convention", 7, "high",
    r"y_\beta-g_{\beta\lambda}(y_\lambda)", r"y_\beta\setmin g_{\beta\lambda}(y_\lambda)",
    "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin as in the p. 13 fixes, pending the convention-7 decision.")

# ---------------------------------------------------------------- checks and output
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"][:80]).encode("ascii", "backslashreplace").decode())
# overlapping olds on the same page
for i, a in enumerate(F):
    for b in F[i + 1:]:
        if a["fix"] and b["fix"] and a["page"] == b["page"]:
            t = (RUN / f"page_{a['page']:03d}.tex").read_text(encoding="utf-8")
            ia, ib = t.find(a["fix"]["old"]), t.find(b["fix"]["old"])
            if ia < ib + len(b["fix"]["old"]) and ib < ia + len(a["fix"]["old"]):
                print("OVERLAP", a["page"], repr(a["fix"]["old"][:40]), repr(b["fix"]["old"][:40]))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter()
for d in F:
    c[(d["page"], "convention" if d["kind"] == "convention" else "misprint" if d["kind"] == "misprint_in_print" else "normal")] += 1
print("written", len(F), "findings; not unique:", bad)
print(sorted(c.items()))
