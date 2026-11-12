"""Build findings_218_222.json and verify every fix.

Checks: each "old" occurs exactly once in page_NNN.tex (LF-normalised) and in the
release segment; applying the fixes of a page in list order succeeds step by step.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_218_222.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega2\ega2-errata-addenda-fr.tex")

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


DISPLAY = "display in the TeX, inline in the print (cf. GLOBAL_ISSUES item 21)"
NOI = ("the print gives this reference without the chapter numeral (the addendum belongs to chap. I); "
       "the TeX adds 'I, '")
HEADDOT = "errata heading: the print has no period after the reference"

# ---------------------------------------------------------------- page 218
add(218, "l. 1, end of Proposition (1.8.1)",
    "Γ(S, 𝒪_S)→Γ(X, 𝒪_X) sur l'ensemble des morphismes ... (inline, at the left margin)",
    r"\[ \Gamma(S,\sh{O}_S)\to\Gamma(X,\sh{O}_X) \] sur l'ensemble", "other", None, "high",
    r"""\[
  \Gamma(S,\sh{O}_S)\to\Gamma(X,\sh{O}_X)
\]
sur l'ensemble""",
    r"""$\Gamma(S,\sh{O}_S)\to\Gamma(X,\sh{O}_X)$
sur l'ensemble""", DISPLAY)
add(218, "l. 2, end of Proposition (1.8.1)",
    "θ^♯_x soit un homomorphisme local : 𝒪_{ψ(x)}→𝒪_x.",
    r"$\theta_x^\sharp:\sh{O}_{\psi(x)}\to\sh{O}_x$ soit un homomorphisme local.", "word", None, "high",
    "$\\theta_x^\\sharp:\\sh{O}_{\\psi(x)}\\to\\sh{O}_x$ soit un\nhomomorphisme local.",
    "$\\theta_x^\\sharp$ soit un\nhomomorphisme local : $\\sh{O}_{\\psi(x)}\\to\\sh{O}_x$.",
    "the print names the map after 'local :'; the TeX moves it next to θ^♯_x and drops the colon")
add(218, "l. 6", "est un idéal premier (italic)", "est un idéal premier", "italics", None, "high",
    "est un idéal premier", r"est un \emph{idéal premier}", "")
add(218, "l. 6", "𝒪_x/𝔪_x = k(x) (bold italic k)", r"\kres(x)", "convention", 1, "high",
    r"=\kres(x)$ est un corps", r"=\boldsymbol{k}(x)$ est un corps", "")
add(218, "l. 8", "(0, 5.5.2) with bold 0", "(0, 5.5.2)", "convention", 2, "high",
    "(0, 5.5.2)", r"(\textbf{0}, 5.5.2)", "")
add(218, "l. 8", "par définition (0, 5.5.2) ^aφ^{-1}(D(f))=X_f, ce qui prouve (inline)",
    r"\[ {}^a\vphi^{-1}(D(f))=X_f, \]", "other", None, "high",
    r"""\[
  {}^a\vphi^{-1}(D(f))=X_f,
\]""",
    r"${}^a\vphi^{-1}(D(f))=X_f$,", DISPLAY)
add(218, "l. 9", "une application continue X→S (continue italic)", "une application continue $X\\to S$",
    "italics", None, "high",
    r"application continue $X\to S$", r"application \emph{continue} $X\to S$", "")
add(218, "l. 11", "Γ(D(f), 𝒪_S)=A_f (1.3.6)", "(I, 1.3.6)", "extra", None, "high",
    "(I, 1.3.6)", "(1.3.6)", NOI)
add(218, "ll. 11-12",
    "l'élément (φ(s)|X_f)(φ(f)|X_f)^{-1} de Γ(X_f, 𝒪_X)=Γ(D(f), ^aφ_*(𝒪_X)), (inline)",
    r"l'élément \[ (\vphi(s)|X_f)(\vphi(f)|X_f)^{-1} \in\Gamma(X_f,\sh{O}_X) =\Gamma(D(f),...), \]",
    "word", None, "high",
    r"""l'élément
\[
  (\vphi(s)|X_f)(\vphi(f)|X_f)^{-1}
  \in\Gamma(X_f,\sh{O}_X)
  =\Gamma(D(f),{}^a\vphi_*(\sh{O}_X)),
\]""",
    r"""l'élément $(\vphi(s)|X_f)(\vphi(f)|X_f)^{-1}$ de
$\Gamma(X_f,\sh{O}_X)=\Gamma(D(f),{}^a\vphi_*(\sh{O}_X))$,""",
    "the print has the word 'de' where the TeX has \\in; the print sets the formula inline (the TeX displays it)")
add(218, "l. 15", "(0, 3.7.1) with bold 0", "(0, 3.7.1)", "convention", 2, "high",
    "(0, 3.7.1)", r"(\textbf{0}, 3.7.1)", "")
add(218, "l. 16", "que l'on a φ̃^♯_x(s_y/f_y)=(φ(s)_x)(φ(f)_x)^{-1}; comme (inline)",
    r"\[ \widetilde{\vphi}_x^\sharp(s_y/f_y) =(\vphi(s)_x)(\vphi(f)_x)^{-1}; \]", "other", None, "high",
    r"""\[
  \widetilde{\vphi}_x^\sharp(s_y/f_y)
  =(\vphi(s)_x)(\vphi(f)_x)^{-1};
\]""",
    r"$\widetilde{\vphi}_x^\sharp(s_y/f_y)=(\vphi(s)_x)(\vphi(f)_x)^{-1}$;", DISPLAY)
add(218, "l. 17", "est un homomorphisme local 𝒪_y→𝒪_x (local italic)", "homomorphisme local",
    "italics", None, "high",
    "est un homomorphisme local\n$\\sh{O}_y", "est un homomorphisme \\emph{local}\n$\\sh{O}_y", "")
add(218, "l. 18", "application σ : Hom(Γ(S, 𝒪_S), Γ(X, 𝒪_X))→𝔏, où (inline)",
    r"\[ \sigma:\Hom(\Gamma(S,\sh{O}_S),\Gamma(X,\sh{O}_X))\to\mathfrak L, \]", "other", None, "high",
    r"""\[
  \sigma:\Hom(\Gamma(S,\sh{O}_S),\Gamma(X,\sh{O}_X))\to\mathfrak L,
\]""",
    r"$\sigma:\Hom(\Gamma(S,\sh{O}_S),\Gamma(X,\sh{O}_X))\to\mathfrak L$,", DISPLAY)
add(218, "l. 20", "pour tout x∈X. Il reste à prouver (same paragraph; 'Il reste' not indented)",
    "blank line before 'Il reste à prouver'", "other", None, "medium",
    "pour tout $x\\in X$.\n\nIl reste", "pour tout $x\\in X$.\nIl reste",
    "paragraph break the print does not have (checked on a crop: 'Il reste' starts at the left margin)")
add(218, "l. 24", "un monomorphisme θ^x : k(ψ(x))→k(x) tel que (inline)",
    r"\[ \theta^x:\kres(\psi(x))\to\kres(x) \]", "other", None, "high",
    r"""\[
  \theta^x:\kres(\psi(x))\to\kres(x)
\]""",
    r"$\theta^x:\kres(\psi(x))\to\kres(x)$",
    DISPLAY + "; apply before the next two convention-1 fixes (their 'old' survives this edit, not vice versa)")
add(218, "l. 24", "k(ψ(x)) bold italic k", r"\kres(\psi(x))", "convention", 1, "high",
    r"\theta^x:\kres(\psi(x))", r"\theta^x:\boldsymbol{k}(\psi(x))", "apply after the display fix of θ^x")
add(218, "l. 24", "→k(x) bold italic k", r"\kres(x)", "convention", 1, "high",
    r"\to\kres(x)", r"\to\boldsymbol{k}(x)", "apply after the display fix of θ^x")
add(218, "diagram, bottom row", "label θ^♯_x below the arrow A_{ψ(x)}→𝒪_x", r"\ar[r]^{\theta_x^\sharp} (label above)",
    "other", None, "high",
    r"\ar[r]^{\theta_x^\sharp}", r"\ar[r]_{\theta_x^\sharp}", "checked on a crop; the top label φ is above, as in the TeX")
add(218, "l. 30", "φ̃^♯_x=θ^♯_x (0, 1.2.4) et par suite φ̃=θ (no comma)", "(0, 1.2.4), et par suite",
    "punctuation", None, "high",
    "1.2.4), et par suite", "1.2.4) et par suite", "")
add(218, "l. 30", "(0, 1.2.4) with bold 0", "(0, 1.2.4)", "convention", 2, "high",
    "(0, 1.2.4)", r"(\textbf{0}, 1.2.4)", "")
add(218, "l. 31, (1.8.2)", "des espaces annelés en anneaux locaux, (italic)", "annelés en anneaux locaux,",
    "italics", None, "high",
    "annelés en\nanneaux locaux, nous aurons", "annelés \\emph{en\nanneaux locaux}, nous aurons", "")
add(218, "l. 33, (1.8.2)", "θ^♯_x soit un homomorphisme local : 𝒪_{ψ(x)}→𝒪_x. (local italic, colon)",
    r"soit un homomorphisme local $\sh{O}_{\psi(x)}\to\sh{O}_x$.", "italics", None, "high",
    "soit un homomorphisme local\n$\\sh{O}_{\\psi(x)}", "soit un homomorphisme \\emph{local} :\n$\\sh{O}_{\\psi(x)}",
    "'local' italic; the print also has a colon before the map, missing in the TeX")
add(218, "l. 33, (1.8.2)", "𝒪_ψ(x)→𝒪_x. Lorsque nous parlerons désormais (same line, same paragraph)",
    "blank line before 'Lorsque nous parlerons désormais'", "other", None, "high",
    "\\to\\sh{O}_x$.\n\nLorsque", "\\to\\sh{O}_x$.\nLorsque", "paragraph break the print does not have")

# ---------------------------------------------------------------- page 219
add(219, "l. 3", "forment une catégorie; (italic)", "forment une catégorie;", "italics", None, "high",
    "forment une catégorie;", r"forment une \emph{catégorie};", "")
add(219, "l. 6", "l'ensemble des morphismes d'espaces annelés de X dans Y (italic)",
    "des morphismes d'espaces annelés de $X$", "italics", None, "high",
    "l'ensemble des morphismes d'espaces annelés de $X$ dans",
    r"l'ensemble des \emph{morphismes d'espaces annelés} de $X$ dans", "")
add(219, "l. 6", "Hom_an(X, Y) (subscript an italic)", r"\Hom_{\mathrm{an}}(X,Y)", "font", None, "high",
    r"noterons $\Hom_{\mathrm{an}}(X,Y)$", r"noterons $\Hom_{\mathit{an}}(X,Y)$", "checked on a crop")
add(219, "(1.8.2.1)", "ρ : Hom_an(X, Y)→... (subscript an italic)", r"\rho:\Hom_{\mathrm{an}}(X,Y)", "font", None, "high",
    r"\rho:\Hom_{\mathrm{an}}(X,Y)", r"\rho:\Hom_{\mathit{an}}(X,Y)", "")
add(219, "(1.8.2.1)", "...Γ(X, 𝒪_X)) (no comma)", r"\Gamma(X,\sh{O}_X)),", "punctuation", None, "high",
    "\\Gamma(X,\\sh{O}_X)),\n\\tag{1.8.2.1}", "\\Gamma(X,\\sh{O}_X))\n\\tag{1.8.2.1}", "checked on a crop")
add(219, "after (1.8.2.2)", "une application fonctorielle en X et Y (italic)", "application fonctorielle",
    "italics", None, "high",
    "application fonctorielle en $X$ et $Y$", r"application \emph{fonctorielle} en $X$ et $Y$", "")
add(219, "Corollaire (1.8.3)", "l'application (1.8.2.2) soit bijective ((1.8.2.2) upright)",
    "(1.8.2.2) in the italic statement", "convention", 6, "high",
    "l'application (1.8.2.2) soit", r"l'application \textup{(1.8.2.2)} soit", "")
add(219, "proof of (1.8.3)", "X→Hom(X, Y)", r"X\mapsto\Hom(X,Y)", "convention", 3, "high",
    r"$X\mapsto\Hom(X,Y)$", r"$X\to\Hom(X,Y)$", "")
add(219, "proof of (1.8.3)", "X→Hom(X, Spec(A))", r"X\mapsto\Hom(X,\Spec(A))", "convention", 3, "high",
    r"$X\mapsto\Hom(X,\Spec(A))$", r"$X\to\Hom(X,\Spec(A))$", "")
add(219, "proof of (1.8.3)", "en anneaux locaux, dans celle des ensembles", "anneaux locaux dans celle des ensembles",
    "punctuation", None, "high",
    "anneaux locaux dans celle des ensembles", "anneaux locaux, dans celle des ensembles", "checked on a crop")
add(219, "proof of (1.8.3)", "sont isomorphes. (italic)", "sont isomorphes.", "italics", None, "high",
    "sont isomorphes. On sait", r"sont \emph{isomorphes}. On sait", "")
add(219, "proof of (1.8.3)", "(cf. 0, 8) with bold 0", "(cf.~0, 8)", "convention", 2, "high",
    "(cf.~0, 8)", r"(cf.~\textbf{0}, 8)", "")
add(219, "(1.8.4)", "est réduit à un point (italic)", "est réduit à un point", "italics", None, "high",
    "est réduit à un point et le faisceau", r"est \emph{réduit à un point} et le faisceau", "")
add(219, "(1.8.4)", "un π-morphisme ι : A'→𝒪_S ('-morphisme' italic)", r"un $\pi$-morphisme", "italics", None, "high",
    r"un $\pi$-morphisme $\iota", r"un \emph{$\pi$-morphisme} $\iota", "checked on a crop")
add(219, "(1.8.4)", "un morphisme d'espaces annelés i=(π, ι) (italic)", "un morphisme d'espaces annelés",
    "italics", None, "high",
    "canoniquement un morphisme d'espaces annelés", r"canoniquement un \emph{morphisme d'espaces annelés}", "")
add(219, "(1.8.4), last line", "i_*(M̃)=M' (1.3.7).", "(I, 1.3.7)", "extra", None, "high",
    "(I, 1.3.7)", "(1.3.7)", NOI + " (checked on a crop)")
add(219, "Lemme (1.8.5)", "Avec les notations de (1.8.4), ((1.8.4) upright)", "(1.8.4) in the italic statement",
    "convention", 6, "high",
    "notations de (1.8.4), pour tout", r"notations de \textup{(1.8.4)}, pour tout", "")
add(219, "Lemme (1.8.5)", "canonique fonctoriel (0, 4.4.3.3) (reference upright)", "(0, 4.4.3.3) in the italic statement",
    "convention", 6, "high",
    "fonctoriel (0, 4.4.3.3)", r"fonctoriel \textup{(0, 4.4.3.3)}",
    "apply before the next item (bold 0 of the same reference): its 'old' survives this edit, not vice versa")
add(219, "Lemme (1.8.5)", "(0, 4.4.3.3) with bold upright 0", "(0, 4.4.3.3)", "convention", 2, "high",
    "(0, 4.4.3.3)", r"(\textbf{0}, 4.4.3.3)", "apply after the \\textup fix above")
add(219, "proof of (1.8.5)", "le foncteur M→i_*(M̃)", r"M\mapsto i_*(\widetilde M)", "convention", 3, "high",
    r"$M\mapsto i_*(\widetilde M)$", r"$M\to i_*(\widetilde M)$", "")

# ---------------------------------------------------------------- page 220
add(220, "l. 1, Corollaire (1.8.6)", "on a (avec les notations de (1.8.4)) un (reference and final parenthesis upright)",
    "(avec les notations de (1.8.4)) in the italic statement", "convention", 6, "medium",
    "(avec les notations de (1.8.4))", r"(avec les notations de \textup{(1.8.4))}",
    "checked on a crop: the opening parenthesis and the words are italic; (1.8.4) and the closing parenthesis upright")
add(220, "(1.8.6.1)", "u^*(M̃) ⥲ u^*(i^*(M')) (arrow with tilde)", r"\isoto (= \simeq)", "convention", 4, "high",
    r"u^*(\widetilde M)\isoto", r"u^*(\widetilde M)\xrightarrow{\sim}", "")
add(220, "(1.8.6.1)", "u^*(i^*(M')) (no final period)", "u^*(i^*(M')).", "punctuation", None, "high",
    "(M')).\n\\tag{1.8.6.1}", "(M'))\n\\tag{1.8.6.1}", "checked on a crop")
add(220, "Corollaire (1.8.7)", "Sous les hypothèses de (1.8.6), ((1.8.6) upright)", "(1.8.6) in the italic statement",
    "convention", 6, "high",
    "hypothèses de (1.8.6), on a", r"hypothèses de \textup{(1.8.6)}, on a", "")
add(220, "(1.8.7.1)", "Hom_𝒪S(M̃, u_*(ℱ)) ⥲ Hom_A(M, Γ(X, ℱ)).", r"\isoto", "convention", 4, "high",
    r"\isoto\Hom_A(M", r"\xrightarrow{\sim}\Hom_A(M", "")
add(220, "proof of (1.8.7)", "(0, 4.4.3) with bold 0", "(0, 4.4.3)", "convention", 2, "high",
    "(0, 4.4.3)", r"(\textbf{0}, 4.4.3)", "")
add(220, "proof of (1.8.7), display", "Hom_𝒪S(M̃, u_*(ℱ)) ⥲ Hom_A'(M', i_*(u_*(ℱ)))", r"\isoto", "convention", 4, "high",
    r"\isoto\Hom_{A'}(M'", r"\xrightarrow{\sim}\Hom_{A'}(M'", "")
add(220, "proof of (1.8.7), display", "...i_*(u_*(ℱ))) (no comma)", r"i_*(u_*(\sh{F}))),", "punctuation", None, "high",
    "i_*(u_*(\\sh{F}))),\n\\]", "i_*(u_*(\\sh{F})))\n\\]", "checked on a crop")
add(220, "proof of (1.8.7), last line", "le A-homomorphisme Γ(h) : M→Γ(S, u_*(ℱ))=Γ(X, ℱ). (inline)",
    r"\[ \Gamma(h):M\to\Gamma(S,u_*(\sh{F}))=\Gamma(X,\sh{F}). \]", "other", None, "high",
    r"""\[
  \Gamma(h):M\to\Gamma(S,u_*(\sh{F}))=\Gamma(X,\sh{F}).
\]""",
    r"$\Gamma(h):M\to\Gamma(S,u_*(\sh{F}))=\Gamma(X,\sh{F})$.", DISPLAY)
add(220, "(1.8.8)", "(0, 4.1.1) with bold 0", "(0, 4.1.1)", "convention", 2, "high",
    "(0, 4.1.1)", r"(\textbf{0}, 4.1.1)", "")
add(220, "(1.8.8)", "une bijection canonique Hom(X, S) ⥲ Hom(X, S') (où bien entendu (inline)",
    r"\[ \Hom(X,S)\isoto\Hom(X,S') \]", "other", None, "high",
    r"""\[
  \Hom(X,S)\isoto\Hom(X,S')
\]""",
    r"$\Hom(X,S)\isoto\Hom(X,S')$",
    DISPLAY + "; apply before the next item (convention 4 in the same formula)")
add(220, "(1.8.8)", "Hom(X, S) ⥲ Hom(X, S') (arrow with tilde)", r"\isoto", "convention", 4, "high",
    r"\Hom(X,S)\isoto", r"\Hom(X,S)\xrightarrow{\sim}", "apply after the display fix above")
add(220, "(1.8.8)", "défini par l'anneau Γ(Y, O_Y) (roman capital O, not script 𝒪)", r"\Gamma(Y,\sh{O}_Y)",
    "misprint_in_print", None, "high",
    r"l'anneau $\Gamma(Y,\sh{O}_Y)$", r"l'anneau $\Gamma(Y,O_Y)$",
    "the print has a plain roman O (checked on a crop); the TeX silently corrects it to the structure sheaf; "
    "the fix restores the printed reading", corrected=r"\Gamma(Y,\sh{O}_Y)")
add(220, "(1.8.8.1)", "ρ : Hom_an(X, Y)→Hom(X, Y') (subscript an italic)", r"\Hom_{\mathrm{an}}", "font", None, "high",
    r"\rho:\Hom_{\mathrm{an}}(X,Y)", r"\rho:\Hom_{\mathit{an}}(X,Y)", "")
add(220, "(1.8.8.1)", "...→Hom(X, Y') (no final period)", r"\Hom(X,Y').", "punctuation", None, "high",
    "\\Hom(X,Y').\n\\tag{1.8.8.1}", "\\Hom(X,Y')\n\\tag{1.8.8.1}", "checked on a crop")
add(220, "after (1.8.8.2)", "est bijective pour tout espace annelé (bijective, tout italic)",
    "est bijective pour tout espace", "italics", None, "high",
    "est bijective pour tout espace", r"est \emph{bijective} pour \emph{tout} espace", "two words")
add(220, "(1.8.8), end", "un espace annelé quelconque Z (italic)", "annelé quelconque $Z$", "italics", None, "high",
    "annelé quelconque $Z$", r"annelé \emph{quelconque} $Z$", "")
add(220, "(1.8.9)", "une catégorie, un morphisme (X, ℱ)→(Y, 𝒢) (italic)", "un morphisme $(X,\\sh{F})$",
    "italics", None, "high",
    r"catégorie, un morphisme $(X,\sh{F})", r"catégorie, un \emph{morphisme} $(X,\sh{F})", "")

# ---------------------------------------------------------------- page 221
add(221, "l. 3, (1.8.9)", "l'application (u, h)→(ρ'(u), Γ(h))", r"(u,h)\mapsto(\rho'(u),\Gamma(h))",
    "convention", 3, "high",
    r"$(u,h)\mapsto(\rho'(u),\Gamma(h))$", r"$(u,h)\to(\rho'(u),\Gamma(h))$", "")
add(221, "(1.8.9.1)", "...(Γ(X, 𝒪_X), Γ(X, ℱ))) (no comma)", r"\bigr),", "punctuation", None, "high",
    "  \\bigr),\n\\end{split}", "  \\bigr)\n\\end{split}", "checked on a crop")
add(221, "after (1.8.9.1)", "fonctorielle en (X, ℱ) et (Y, 𝒢) (italic)", "fonctorielle en", "italics", None, "high",
    r"fonctorielle en $(X,\sh{F})$", r"\emph{fonctorielle} en $(X,\sh{F})$", "")
add(221, "after (1.8.9.1)", "(0, 1.0.2) with bold 0", "(0, 1.0.2)", "convention", 2, "high",
    "(0, 1.0.2)", r"(\textbf{0}, 1.0.2)", "")
add(221, "Corollaire (1.8.10)", "l'application canonique (1.8.8.1) soit bijective ((1.8.8.1) upright)",
    "(1.8.8.1) in the italic statement", "convention", 6, "high",
    "canonique (1.8.8.1) soit", r"canonique \textup{(1.8.8.1)} soit", "")
add(221, "Corollaire (1.8.10)", "l'application canonique (1.8.8.1) soit bijective", "(1.8.8.1)",
    "misprint_in_print", None, "high", None, None,
    "the TeX keeps the printed reading. The statement concerns couples (X, ℱ), (Y, 𝒢), so the map meant is "
    "(1.8.9.1); (1.8.8.1) is ρ : Hom_an(X, Y)→Hom(X, Y'), which involves no Modules",
    corrected="(1.8.9.1)")
add(221, "Remarque (1.8.11), l. 1", "Les énoncés (1.7.3), (1.7.4) et (2.2.4)", "(I, 1.7.3), (I, 1.7.4) et (I, 2.2.4)",
    "extra", None, "high",
    "Les énoncés (I, 1.7.3), (I, 1.7.4) et (I, 2.2.4) sont", "Les énoncés (1.7.3), (1.7.4) et (2.2.4) sont",
    NOI + " (three references)")
add(221, "Remarque (1.8.11), l. 2", "la définition (1.6.1); de même (2.2.5) résulte", "(I, 1.6.1) ... (I, 2.2.5)",
    "extra", None, "high",
    "la définition (I, 1.6.1); de même\n(I, 2.2.5) résulte", "la définition (1.6.1); de même\n(2.2.5) résulte",
    NOI + " (two references)")
add(221, "Remarque (1.8.11), l. 3", "aussi (1.6.3) (et par suite (1.6.4))", "(I, 1.6.3) (et par suite (I, 1.6.4))",
    "extra", None, "high",
    "(I, 1.6.3) (et par suite (I, 1.6.4))", "(1.6.3) (et par suite (1.6.4))", NOI + " (two references)")
add(221, "Remarque (1.8.11), ll. 4-5",
    "les foncteurs M→Hom_𝒪S(M̃, u_*(Ñ)) et M→Hom_𝒪S(M̃, (N_[φ])~) (où (inline)",
    r"\[ M\longmapsto \Hom_{\sh{O}_S}(...) \quad\hbox{et}\quad M\longmapsto \Hom_{\sh{O}_S}(...) \]",
    "other", None, "high",
    r"""\[
  M\longmapsto
  \Hom_{\sh{O}_S}(\widetilde M,u_*(\widetilde N))
  \quad\hbox{et}\quad
  M\longmapsto
  \Hom_{\sh{O}_S}(\widetilde M,(N_{[\vphi]})\supertilde)
\]""",
    r"""$M\longmapsto
  \Hom_{\sh{O}_S}(\widetilde M,u_*(\widetilde N))$ et
$M\longmapsto
  \Hom_{\sh{O}_S}(\widetilde M,(N_{[\vphi]})\supertilde)$""",
    DISPLAY + "; apply before the next two convention-3 fixes (their 'old' survives this edit, not vice versa)")
add(221, "Remarque (1.8.11), l. 4", "M→Hom_𝒪S(M̃, u_*(Ñ))", r"M\longmapsto", "convention", 3, "high",
    "\\longmapsto\n  \\Hom_{\\sh{O}_S}(\\widetilde M,u_*", "\\to\n  \\Hom_{\\sh{O}_S}(\\widetilde M,u_*",
    "apply after the display fix above")
add(221, "Remarque (1.8.11), l. 5", "M→Hom_𝒪S(M̃, (N_[φ])~)", r"M\longmapsto", "convention", 3, "high",
    "\\longmapsto\n  \\Hom_{\\sh{O}_S}(\\widetilde M,(N", "\\to\n  \\Hom_{\\sh{O}_S}(\\widetilde M,(N",
    "apply after the display fix above")
add(221, "Remarque (1.8.11), l. 6", "isomorphes par (1.8.7) et (1.3.8)", "(I, 1.3.8)", "extra", None, "high",
    "par (1.8.7) et (I, 1.3.8)", "par (1.8.7) et (1.3.8)", NOI)
add(221, "Remarque (1.8.11), l. 6", "Enfin, (1.6.5) (et par suite (1.6.6))", "(I, 1.6.5) (et par suite (I, 1.6.6))",
    "extra", None, "high",
    "Enfin, (I, 1.6.5) (et par suite (I, 1.6.6))", "Enfin, (1.6.5) (et par suite (1.6.6))", NOI + " (two references)")
add(221, "Remarque (1.8.11), l. 7", "les A_f-modules N'⊗_A'A_f et (N'⊗_A'A)_f (notations (inline)",
    r"\[ N'\otimes_{A'}A_f \quad\hbox{et}\quad (N'\otimes_{A'}A)_f \]", "other", None, "high",
    r"""\[
  N'\otimes_{A'}A_f
  \quad\hbox{et}\quad
  (N'\otimes_{A'}A)_f
\]""",
    r"$N'\otimes_{A'}A_f$ et $(N'\otimes_{A'}A)_f$", DISPLAY)
add(221, "Remarque (1.8.11), l. 7", "(notations de (1.6.5))", "(notations de (I, 1.6.5))", "extra", None, "high",
    "(notations de (I, 1.6.5))", "(notations de (1.6.5))", NOI)
add(221, "Insérer après (I, 3.2.8)", "Insérer après (I, 3.2.8) : ('Insérer après' and ':' roman; I and 3.2.8 bold)",
    r"\paragraph{Insérer après (I, 3.2.8) :} (all bold)", "font", None, "medium",
    r"\paragraph{Insérer après (I, 3.2.8) :}", r"Insérer après (\textbf{I}, \textbf{3.2.8}) :",
    "checked on a crop; the print sets this line as an ordinary indented line")
add(221, "(3.2.9)", "préciser (3.2.2) de la façon", "(I, 3.2.2)", "extra", None, "high",
    "préciser (I, 3.2.2) de la façon", "préciser (3.2.2) de la façon", NOI)
add(221, "(3.2.9)", "la catégorie des S-préschémas, ('préschémas' italic)", "$S$-préschémas,", "italics", None, "high",
    "$S$-préschémas,\nmais aussi", "$S$-\\emph{préschémas},\nmais aussi", "checked on a crop")
add(221, "(3.2.9)", "des espaces annelés en anneaux locaux, au-dessus de S (both italic)",
    "des espaces annelés en anneaux locaux, au-dessus de $S$", "italics", None, "high",
    "des espaces annelés en anneaux locaux,\nau-dessus de $S$",
    "des \\emph{espaces annelés en anneaux locaux},\n\\emph{au-dessus de} $S$", "checked on a crop")
add(221, "(3.2.9)", "calquée sur celle de (2.5.2))", "(I, 2.5.2)", "extra", None, "high",
    "celle de (I, 2.5.2))", "celle de (2.5.2))", NOI)
add(221, "(3.2.9)", "La démonstration de (3.2.6)", "(I, 3.2.6)", "extra", None, "high",
    "démonstration de (I, 3.2.6)", "démonstration de (3.2.6)", NOI)
add(221, "errata (I, 4.4.5)", "(I, 4.4.5) Ligne 14", r"\paragraph{(I, 4.4.5).}", "punctuation", None, "high",
    r"\paragraph{(I, 4.4.5).}", r"\paragraph{(I, 4.4.5)}", HEADDOT)
add(221, "errata (I, 4.4.5)", "remplacer A-algèbre par B-algèbre. (no guillemets)",
    "remplacer «~$A$-algèbre~» par «~$B$-algèbre~».", "extra", None, "high",
    "remplacer «~$A$-algèbre~» par «~$B$-algèbre~».", "remplacer $A$-algèbre par $B$-algèbre.",
    "checked on a crop")
add(221, "errata (I, 5.3.5)", "(I, 5.3.5) Ligne 2", r"\paragraph{(I, 5.3.5).}", "punctuation", None, "high",
    r"\paragraph{(I, 5.3.5).}", r"\paragraph{(I, 5.3.5)}", HEADDOT)
add(221, "errata (I, 6.3.2.1)", "(I, 6.3.2.1) Ligne 6", r"\paragraph{(I, 6.3.2.1).}", "punctuation", None, "high",
    r"\paragraph{(I, 6.3.2.1).}", r"\paragraph{(I, 6.3.2.1)}", HEADDOT)
add(221, "errata (I, 6.3.2.1)", "lire : D(g_i)⊂W. (inline)", r"lire : \[ D(g_i)\subset W. \]", "other", None, "high",
    r"""lire :
\[
  D(g_i)\subset W.
\]""",
    r"lire : $D(g_i)\subset W$.", DISPLAY)
add(221, "errata (I, 7.3.8)", "(I, 7.3.8) Remplacer", r"\paragraph{(I, 7.3.8).}", "punctuation", None, "high",
    r"\paragraph{(I, 7.3.8).}", r"\paragraph{(I, 7.3.8)}", HEADDOT)
add(221, "errata (I, 7.3.8), text", "deux préschémas intègres, (italic)", "préschémas intègres,", "italics", None, "high",
    "deux préschémas intègres, ce qui", r"deux préschémas \emph{intègres}, ce qui", "")
add(221, "errata (I, 7.3.8), text", "quasi-cohérent (7.3.3).", "(I, 7.3.3)", "extra", None, "high",
    "quasi-cohérent (I, 7.3.3)", "quasi-cohérent (7.3.3)", NOI)
add(221, "errata (I, 7.3.8), text", "un morphisme dominant; (italic)", "morphisme dominant;", "italics", None, "high",
    "morphisme dominant;", r"morphisme \emph{dominant};", "")

# ---------------------------------------------------------------- page 222
add(222, "l. 4", "l'homomorphisme canonique L⊗_B A→K (1.6.5). (inline)", r"\[ L\otimes_B A\to K \]",
    "other", None, "high",
    r"""\[
  L\otimes_B A\to K
\]""",
    r"$L\otimes_B A\to K$", DISPLAY)
add(222, "l. 5", "(1.6.5). Dans le cas général", "(I, 1.6.5)", "extra", None, "high",
    "(I, 1.6.5). Dans", "(1.6.5). Dans", NOI)
add(222, "after the display", "(0, 4.3.1) et τ_x est donc (no comma)", "(0, 4.3.1), et", "punctuation", None, "high",
    "4.3.1), et $\\tau_x$", "4.3.1) et $\\tau_x$", "checked on a crop")
add(222, "after the display", "(0, 4.3.1) with bold 0", "(0, 4.3.1)", "convention", 2, "high",
    "(0, 4.3.1)", r"(\textbf{0}, 4.3.1)", "")
add(222, "after the display", "est donc un isomorphisme. (italic)", "un isomorphisme.", "italics", None, "high",
    "est donc un isomorphisme.", r"est donc un \emph{isomorphisme}.", "")
add(222, "errata (I, 9.5.2)", "(I, 9.5.2) Dans les 3 dernières", r"\paragraph{(I, 9.5.2).}", "punctuation", None, "high",
    r"\paragraph{(I, 9.5.2).}", r"\paragraph{(I, 9.5.2)}", HEADDOT)
add(222, "errata (I, 10.5.4)", "(I, 10.5.4) Ligne 11", r"\paragraph{(I, 10.5.4).}", "punctuation", None, "high",
    r"\paragraph{(I, 10.5.4).}", r"\paragraph{(I, 10.5.4)}", HEADDOT)
add(222, "errata (I, 10.6.3)", "(I, 10.6.3) Ligne 3", r"\paragraph{(I, 10.6.3).}", "punctuation", None, "high",
    r"\paragraph{(I, 10.6.3).}", r"\paragraph{(I, 10.6.3)}", HEADDOT)
add(222, "errata (I, 10.14.2)", "(I, 10.14.2) Ligne 5", r"\paragraph{(I, 10.14.2).}", "punctuation", None, "high",
    r"\paragraph{(I, 10.14.2).}", r"\paragraph{(I, 10.14.2)}", HEADDOT)
add(222, "errata (I, 10.14.2)",
    "remplacer « 𝒪_𝔛-Module cohérent » par « Idéal cohérent de 𝒪_𝔛 » (words italic in this first pair only)",
    "«~$\\sh{O}_{\\mathfrak X}$-Module cohérent~» par «~Idéal cohérent de $\\sh{O}_{\\mathfrak X}$~» (upright)",
    "italics", None, "high",
    "remplacer «~$\\sh{O}_{\\mathfrak X}$-Module cohérent~» par\n«~Idéal cohérent de $\\sh{O}_{\\mathfrak X}$~»",
    "remplacer «~$\\sh{O}_{\\mathfrak X}$-\\emph{Module cohérent}~» par\n«~\\emph{Idéal cohérent de} $\\sh{O}_{\\mathfrak X}$~»",
    "checked on a crop; the second pair (ligne 7) is roman, as in the TeX")

# ---------------------------------------------------------------- checks
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = rel[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]

ok = True
pages = sorted({x["page"] for x in F})
for p in pages:
    orig = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    seg = segs[p]
    if orig.split("\n", 1)[1] != seg:
        print(f"WARNING page {p}: page file and release segment differ")
    cur = seg
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        c0, c1 = orig.count(old), seg.count(old)
        if c0 != 1 or c1 != 1:
            ok = False
            print(f"page {p}: old occurs {c0}x in page file, {c1}x in release segment: {old!r}")
        cs = cur.count(old)
        if cs != 1:
            ok = False
            print(f"page {p}: sequential application fails ({cs}x): {old!r}")
        else:
            cur = cur.replace(old, new)

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("all checks passed" if ok else "CHECK FAILURES")
print({p: tuple(v) for p, v in counts.items()}, len(F))
