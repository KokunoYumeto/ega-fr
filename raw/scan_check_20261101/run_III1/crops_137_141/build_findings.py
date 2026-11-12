"""Build findings_137_141.json, check every fix's old against its page_NNN.tex, and simulate apply_fixes.py
(segment from \\oldpage[III]{N} to the next marker, old must occur once at apply time, list order) on a copy."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex")
OUT = RUN / "findings_137_141.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def c2(page, where, old, new, numeral):
    add(page, where, f"({numeral}, ...): bold {numeral}", old, "convention", 2, "high", old, new,
        f"Bold {numeral} in the reference.")


COVERED = "Covered by the edit of the preceding finding (one edit for both)."

# ---------------------------------------------------------------- page 137
add(137, "Corollaire (4.4.6): 'Alors il existe g∈B—q'", "g∈B—q: long dash", r"g\in B-\mathfrak q",
    "convention", 7, "high", r"B-\mathfrak q", r"B\setmin\mathfrak q", "Long dash for set difference.")
c2(137, "Proof of (4.4.6): 'isolé dans sa fibre (I, 1.1.7)'", "(I, 1.1.7)", r"(\textbf{I}, 1.1.7)", "I")
add(137, "Corollaire (4.4.8): 'Sous les conditions de (4.4.7), supposons'",
    "the reference (4.4.7) is upright inside the italic statement (crop)",
    "(4.4.7) inside the italic corollary environment: italic", "convention", 6, "high",
    r"(\hyperref[III.4.4.7-fr]{4.4.7}), supposons", r"\textup{(\hyperref[III.4.4.7-fr]{4.4.7})}, supposons",
    "Upright reference in an italic statement.")
add(137, "Proof of (4.4.8): 'En effet, la Remarque (4.4.4) montre'", "Remarque in italic (crop)",
    "Remarque in roman", "italics", None, "high", "la Remarque (", r"la \emph{Remarque} (",
    "The word Remarque is italic in the print.")
add(137, "Proof of (4.4.9): 'un schéma algébrique sur k(y)'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "sur $k(y)$", r"sur $\boldsymbol{k}(y)$", "Bold italic k of the residue field.")
c2(137, "Proof of (4.4.9): 'discret (I, 6.4.4)'", "(I, 6.4.4)", r"(\textbf{I}, 6.4.4)", "I")
c2(137, "Proof of (4.4.9): 'même corps des fractions (I, 7.1.5)'", "(I, 7.1.5)", r"(\textbf{I}, 7.1.5)", "I")
add(137, "Proof of (4.4.9): 'l'homomorphisme θ♯_y : 𝒪_y→𝒪_x'", "sharp sign ♯", r"\theta_y^\#", "convention", 9,
    "high", r"\theta_y^\#", r"\theta_y^\sharp", "Sharp sign, typeset # by \\#.")
c2(137, "Proof of (4.4.9): 'on en conclut (I, 6.5.4)'", "(I, 6.5.4)", r"(\textbf{I}, 6.5.4)", "I")
c2(137, "Proof of (4.4.9): 'immersion ouverte (I, 8.2.8)'", "(I, 8.2.8)", r"(\textbf{I}, 8.2.8)", "I")
c2(137, "Proof of (4.4.10): 'quasi-projectif (II, 5.3.4, (i))'", "(II, 5.3.4, (i))", r"(\textbf{II}, 5.3.4, (i))", "II")

# ---------------------------------------------------------------- page 138
add(138, "Proof of (4.4.11): 'l'image par f de X—X''", "X—X': long dash", "$X-X'$", "convention", 7, "high",
    "X-X'", r"X\setmin X'", "Long dash for set difference.")
c2(138, "Proof of (4.4.11): 'il résulte de (II, 6.2.2)'", "(II, 6.2.2)", r"(\textbf{II}, 6.2.2)", "II")
c2(138, "Proof of (4.4.11): 'est propre (II, 5.4.1)'", "(II, 5.4.1)", r"(\textbf{II}, 5.4.1)", "II")
c2(138, "Remarques (4.4.12) (i): 'annoncé dans (II, 6.2.7)'", "(II, 6.2.7)", r"(\textbf{II}, 6.2.7)", "II")
add(138, "Remarques (4.4.12) (i): 'lorsqu'on suppose seulement f séparé et de type fini'",
    "'séparé et de type fini' italic (crop)", "roman (env body)", "italics", None, "high",
    "$f$ séparé et de type fini.", r"$f$ \emph{séparé et de type fini}.",
    "The remark is roman; these words are italic in the print.")
c2(138, "Remarques (4.4.12) (i): 'encore de type fini (I, 6.3.5)'", "(I, 6.3.5)", r"(\textbf{I}, 6.3.5)", "I")
add(138, "Proposition (4.5.1): 'sur Y=Spec(A) (II, 5.4.10). Alors'", "(𝐈𝐈, 5.4.10): bold II",
    "(II, 5.4.10)", "convention", 2, "high", r"\operatorname{Spec}(A)$ (II, 5.4.10)",
    r"\operatorname{Spec}(A)$ \textup{(\textbf{II}, 5.4.10)}",
    "One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
add(138, "Proposition (4.5.1): same reference '(II, 5.4.10)'",
    "the reference is upright inside the italic statement (crop)",
    "(II, 5.4.10) inside the italic proposition environment: italic", "convention", 6, "high", None, None, COVERED)
add(138, "Proposition (4.5.1): '(avec les notations de (4.1.7)) à Ext^n'",
    "the reference (4.1.7) is upright inside the italic statement (crop)",
    "(4.1.7) inside the italic proposition environment: italic", "convention", 6, "high",
    r"(\hyperref[III.4.1.7-fr]{4.1.7})) à", r"\textup{(\hyperref[III.4.1.7-fr]{4.1.7})}) à",
    "Upright reference in an italic statement.")
add(138, "Proof of (4.5.1): 'les termes E_2 sont donnés par E_2^{pq}=H^p(X, Ext^q(F, G)). On sait que'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\n\\mathrm E_2^{pq}=\\mathrm H^p\\bigl(X,\n\\mathcal{E}\\!xt^q_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\\bigr).\n\\]",
    "$\\mathrm E_2^{pq}=\\mathrm H^p\\bigl(X,\n\\mathcal{E}\\!xt^q_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\\bigr)$.",
    "Layout: the print sets this formula inline in the running text; the TeX displays it.")
c2(138, "Proof of (4.5.1): 'Module cohérent (0, 12.3.3)'", "(0, 12.3.3)", r"(\textbf{0}, 12.3.3)", "0")
c2(138, "Proof of (4.5.1): 'propre sur Y (II, 5.4.10). On conclut'", "$Y$ (II, 5.4.10)", r"$Y$ (\textbf{II}, 5.4.10)", "II")
c2(138, "Proof of (4.5.1): 'et par suite (0, 11.1.8)'", "(0, 11.1.8)", r"(\textbf{0}, 11.1.8)", "0")
add(138, "Proof of (4.5.1): 'et i est plat (I, 10.8.8 et 10.8.9)'", "'plat' italic (crop)", "plat in roman",
    "italics", None, "high", "est plat", r"est \emph{plat}", "The word plat is italic in the print.")
c2(138, "Proof of (4.5.1): '(I, 10.8.8 et 10.8.9)'", "(I, 10.8.8 et", r"(\textbf{I}, 10.8.8 et", "I")
c2(138, "Proof of (4.5.1): 'On sait alors (0, 12.3.4)'", "(0, 12.3.4)", r"(\textbf{0}, 12.3.4)", "0")
add(138, "Proof of (4.5.1): 'un i-morphisme canonique u_q : Ext^q(F, G)→Ext^q(F̂, Ĝ), et que le'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nu_q:\\mathcal{E}\\!xt^q_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\n\\longrightarrow\n"
    "\\mathcal{E}\\!xt^q_{\\mathcal O_{\\widehat X}}\n(\\widehat{\\mathcal F},\\widehat{\\mathcal G}),\n\\]",
    "$u_q:\\mathcal{E}\\!xt^q_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\n\\longrightarrow\n"
    "\\mathcal{E}\\!xt^q_{\\mathcal O_{\\widehat X}}\n(\\widehat{\\mathcal F},\\widehat{\\mathcal G})$,",
    "Layout: the print sets this formula inline in the running text; the TeX displays it. The comma follows the formula.")
add(138, "Proof of (4.5.1): 'le 𝒪_X̂-homomorphisme correspondant u♯ : i*(Ext^q(F, G))→Ext^q(F̂, Ĝ) est un isomorphisme'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nu_q^\\#:i^*\\bigl(\\mathcal{E}\\!xt^q_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\\bigr)\n\\longrightarrow\n"
    "\\mathcal{E}\\!xt^q_{\\mathcal O_{\\widehat X}}\n(\\widehat{\\mathcal F},\\widehat{\\mathcal G})\n\\]",
    "$u_q^\\#:i^*\\bigl(\\mathcal{E}\\!xt^q_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\\bigr)\n\\longrightarrow\n"
    "\\mathcal{E}\\!xt^q_{\\mathcal O_{\\widehat X}}\n(\\widehat{\\mathcal F},\\widehat{\\mathcal G})$",
    "Layout: the print sets this formula inline. Apply this edit before the next finding (misprint u♯), whose old "
    "lies inside this span; this edit keeps u_q^\\# unchanged.")
add(138, "Proof of (4.5.1): 'correspondant u♯ : i*(Ext^q_{𝒪_X}(F, G))→...'",
    "u♯ without the subscript q (crop; the line above has u_q)", r"u_q^\#", "misprint_in_print", None, "high",
    r"u_q^\#:i^*", r"u^\sharp:i^*",
    "The print drops the index q: the homomorphism corresponding to the i-morphism u_q is u_q♯. The TeX silently "
    "corrects; the fix restores the printed reading and also writes the sharp sign as \\sharp (convention 9, next "
    "finding). Apply after the preceding layout edit.",
    corrected=r"u_q^\sharp:i^*")
add(138, "Proof of (4.5.1): same symbol u♯", "sharp sign ♯", r"u_q^\#", "convention", 9, "high", None, None,
    "Covered by the edit of the preceding finding (misprint), which writes \\sharp.")
add(138, "Proof of (4.5.1): 'est un isomorphisme (0, 12.3.5)'", "'isomorphisme' italic (crop)",
    "isomorphisme in roman", "italics", None, "high", "un isomorphisme", r"un \emph{isomorphisme}",
    "The word isomorphisme is italic in the print.")
c2(138, "Proof of (4.5.1): 'est un isomorphisme (0, 12.3.5)'", "(0, 12.3.5)", r"(\textbf{0}, 12.3.5)", "0")
c2(138, "Proof of (4.5.1): 'autrement dit (I, 10.8.8),'", "(I, 10.8.8),", r"(\textbf{I}, 10.8.8),", "I")
add(138, "Proof of (4.5.1): 'au complété (Ext^q_{𝒪_X}(F, G))^'", "a raised circumflex after the parenthesis (crop)",
    r"^\wedge (a wedge)", "symbol", None, "high", r"(\mathcal F,\mathcal G))^\wedge",
    r"(\mathcal F,\mathcal G))^{\widehat{\,}}",
    "Circumflex accent, not ∧; same form as the EGA II p. 194 fixes (GLOBAL_ISSUES item 31).")
add(138, "Proof of (4.5.1): 'pour tout p≥0, H^p(X̂, Ext^q(F̂, Ĝ)) s'identifie canoniquement'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\n\\mathrm H^p\\bigl(\\widehat X,\n\\mathcal{E}\\!xt^q_{\\mathcal O_{\\widehat X}}\n"
    "(\\widehat{\\mathcal F},\\widehat{\\mathcal G})\\bigr)\n\\]",
    "$\\mathrm H^p\\bigl(\\widehat X,\n\\mathcal{E}\\!xt^q_{\\mathcal O_{\\widehat X}}\n"
    "(\\widehat{\\mathcal F},\\widehat{\\mathcal G})\\bigr)$",
    "Layout: the print sets this formula inline in the running text; the TeX displays it.")

# ---------------------------------------------------------------- page 139 (print p. 139)
add(139, "Proof of (4.5.1): 'à un isomorphisme canonique près, E_2^{pq}(F̂, Ĝ)=E_2^{pq}(F, G)⊗_A Â (0_I, 7.3.3).'",
    "the formula is set inline in the running text; bold 0 in (𝟎_I, 7.3.3)",
    r"displayed with \[ ... \], reference inside the display", "other", None, "high",
    "\\[\n\\mathrm E_2^{pq}(\\widehat{\\mathcal F},\\widehat{\\mathcal G})\n"
    "=\\mathrm E_2^{pq}(\\mathcal F,\\mathcal G)\\otimes_A\\widehat A\n\\qquad (0\\textsubscript{I}, 7.3.3).\n\\]",
    "$\\mathrm E_2^{pq}(\\widehat{\\mathcal F},\\widehat{\\mathcal G})\n"
    "=\\mathrm E_2^{pq}(\\mathcal F,\\mathcal G)\\otimes_A\\widehat A$\n(\\textbf{0}\\textsubscript{I}, 7.3.3).",
    "Layout: the print sets this formula and its reference inline. One edit for this finding and the next "
    "(convention 2).")
add(139, "Proof of (4.5.1): same reference (0_I, 7.3.3)", "(𝟎_I, 7.3.3): bold 0", r"(0\textsubscript{I}, 7.3.3)",
    "convention", 2, "high", None, None, COVERED)
c2(139, "Proof of (4.5.1): 'par fonctorialité (0, 12.3.4)'", "(0, 12.3.4)", r"(\textbf{0}, 12.3.4)", "0")
add(139, "Proof of (4.5.1): 'Comme Â est un A-module plat' after the ψ^n display",
    "'Comme' is indented: a new paragraph", "no blank line after the display: the paragraph continues",
    "other", None, "high", "\\]\nComme $\\widehat A$", "\\]\n\nComme $\\widehat A$",
    "Paragraph break missing after the display.")
add(139, "Proof of (4.5.1): 'Comme Â est un A-module plat (0_I, 7.3.3)'", "'plat' italic (crop)", "plat in roman",
    "italics", None, "high", "$A$-module plat", r"$A$-module \emph{plat}", "The word plat is italic in the print.")
c2(139, "Proof of (4.5.1): 'A-module plat (0_I, 7.3.3), les'", r"(0\textsubscript{I}, 7.3.3), les",
   r"(\textbf{0}\textsubscript{I}, 7.3.3), les", "0")
add(139, "Proof of (4.5.1): 'et les ψ_r^{pq} et ψ_n un morphisme de suites spectrales'",
    "ψ_n with a subscript n (3x crop)", r"$\psi^n$", "misprint_in_print", None, "high",
    "et $\\psi^n$ un morphisme", "et $\\psi_n$ un morphisme",
    "The maps are ψ^n everywhere else (definition, and 'il en est de même des ψ^n' two lines later). The TeX "
    "silently corrects; the fix restores the printed reading.",
    corrected="et $\\psi^n$ un morphisme")
add(139, "Proof of (4.5.1): 'Comme les ψ_2^{pq} sont des isomorphismes'", "'isomorphismes' italic",
    "isomorphismes in roman", "italics", None, "high", "sont des isomorphismes", r"sont des \emph{isomorphismes}",
    "The word isomorphismes is italic in the print.")
c2(139, "Proof of (4.5.1): 'il en est de même des ψ^n (0, 11.1.5)'", "(0, 11.1.5)", r"(\textbf{0}, 11.1.5)", "0")
add(139, "Corollaire (4.5.2): 'Sous les hypothèses de (4.5.1), supposons'",
    "the reference (4.5.1) is upright inside the italic statement",
    "(4.5.1) inside the italic corollary environment: italic", "convention", 6, "high",
    r"(\hyperref[III.4.5.1-fr]{4.5.1}), supposons", r"\textup{(\hyperref[III.4.5.1-fr]{4.5.1})}, supposons",
    "Upright reference in an italic statement.")
c2(139, "Proof of (4.5.2): 'J-préadique (0_I, 7.3.6)'", r"(0\textsubscript{I}, 7.3.6)",
   r"(\textbf{0}\textsubscript{I}, 7.3.6)", "0")
add(139, "Corollaire (4.5.3): 'Sous les hypothèses de (4.5.1), pour tout homomorphisme'",
    "the reference (4.5.1) is upright inside the italic statement",
    "(4.5.1) inside the italic corollary environment: italic", "convention", 6, "high",
    r"(\hyperref[III.4.5.1-fr]{4.5.1}), pour tout", r"\textup{(\hyperref[III.4.5.1-fr]{4.5.1})}, pour tout",
    "Upright reference in an italic statement.")
add(139, "Corollaire (4.5.3): 'désignons par û l'homomorphisme complété F̂→Ĝ (I, 10.8.4)'",
    "û l'homomorphisme complété F̂→Ĝ (crop)", "û: F̂→Ĝ l'homomorphisme complété", "formula", None, "high",
    "$\\widehat u:\\widehat{\\mathcal F}\\to\\widehat{\\mathcal G}$ l'homomorphisme\ncomplété",
    "$\\widehat u$ l'homomorphisme\ncomplété $\\widehat{\\mathcal F}\\to\\widehat{\\mathcal G}$",
    "The print names û first and writes F̂→Ĝ after 'complété'.")
add(139, "Corollaire (4.5.3): '(I, 10.8.4). Alors'", "(I, 10.8.4): bold I (damaged sort), upright",
    "(I, 10.8.4)", "convention", 2, "medium", "(I, 10.8.4)", r"\textup{(\textbf{I}, 10.8.4)}",
    "The I is a damaged bold sort (4x crop: heavier and taller than the figures). One edit for this finding and "
    "the next (convention 6).")
add(139, "Corollaire (4.5.3): same reference '(I, 10.8.4)'", "the reference is upright inside the italic statement",
    "(I, 10.8.4) inside the italic corollary environment: italic", "convention", 6, "high", None, None, COVERED)
add(139, "Corollaire (4.5.3), (4.5.3.1): '(Hom_{𝒪_X}(F, G))^ ⥲ ...'", "a raised circumflex after the parenthesis",
    r"\right)^\wedge (a wedge)", "symbol", None, "high", r"\right)^\wedge", r"\right)^{\widehat{\,}}",
    "Circumflex accent, not ∧; same form as the EGA II p. 194 fixes (GLOBAL_ISSUES item 31).")
add(139, "Corollaire (4.5.3), (4.5.3.1): end of the display '... Hom(F̂, Ĝ)'", "no comma after the formula (crop)",
    "comma before \\tag{4.5.3.1}", "punctuation", None, "high",
    "(\\widehat{\\mathcal F},\\widehat{\\mathcal G}),\n\\tag{4.5.3.1}",
    "(\\widehat{\\mathcal F},\\widehat{\\mathcal G})\n\\tag{4.5.3.1}",
    "The display ends without punctuation; the statement continues 'où le premier membre'. (The faint hat over the "
    "subscript X of the right-hand Hom is broken in the print, only its apex shows; no change.)")
add(139, "Corollaire (4.5.3): 'à partir de l'homomorphisme u→û'", "plain arrow →", r"u\mapsto\widehat u",
    "convention", 3, "high", "$u\\mapsto\\widehat u$", "$u\\to\\widehat u$", "Plain arrow in the print.")

# ---- page 139 segment, text printed on p. 140 (before the misplaced \oldpage[III]{140})
P140 = "printed p. 140, text in the p. 139 segment: "
add(139, P140 + "Proposition (4.6.1): 'entier n, on ait H^n(f^{-1}(y), F⊗k(y))=0. Alors'",
    "the formula is set inline in the running text; bold italic k", r"displayed with \[ ... \]; plain k",
    "other", None, "high",
    "\\[\nH^n\\bigl(f^{-1}(y),\\mathcal F\\otimes_{\\mathcal O_Y}k(y)\\bigr)=0.\n\\]",
    "$H^n\\bigl(f^{-1}(y),\\mathcal F\\otimes_{\\mathcal O_Y}\\boldsymbol{k}(y)\\bigr)=0$.",
    "Layout: inline in the print. One edit for this finding and the next (convention 1). Apply before the marker "
    "move of \\oldpage[III]{140}.")
add(139, P140 + "Proposition (4.6.1): same formula, k(y)", "bold italic k", "k(y)", "convention", 1, "high",
    None, None, COVERED)
add(139, P140 + "Proposition (4.6.1): '(4.2.1.1) est surjectif.'",
    "'(4.2.1.1) est surjectif.' without 'de'; the reference is upright (crop)", "de (4.2.1.1) est surjectif.",
    "extra", None, "high", "de (\\hyperref[III.4.2.1.1-fr]{4.2.1.1}) est surjectif.",
    "\\textup{(\\hyperref[III.4.2.1.1-fr]{4.2.1.1})} est surjectif.",
    "The TeX adds 'de'. One edit for this finding and the next (convention 6).")
add(139, P140 + "Proposition (4.6.1): same reference (4.2.1.1)", "upright inside the italic statement",
    "(4.2.1.1) inside the italic proposition environment: italic", "convention", 6, "high", None, None, COVERED)
c2(139, P140 + "proof of (4.6.1): '(R^n f_*(F))_y=0 (0_I, 5.2.2)'", r"(0\textsubscript{I}, 5.2.2)",
   r"(\textbf{0}\textsubscript{I}, 5.2.2)", "0")
add(139, P140 + "proof of (4.6.1): 'il suffira de prouver que H^n(f^{-1}(y), F⊗(𝒪_y/m^{p+1}))=0 pour tout p'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nH^n\\bigl(f^{-1}(y),\\mathcal F\\otimes_{\\mathcal O_Y}\n(\\mathcal O_y/\\mathfrak m_y^{p+1})\\bigr)=0\n\\]",
    "$H^n\\bigl(f^{-1}(y),\\mathcal F\\otimes_{\\mathcal O_Y}\n(\\mathcal O_y/\\mathfrak m_y^{p+1})\\bigr)=0$",
    "Layout: the print sets this formula inline in the running text; the TeX displays it.")
add(139, P140 + "proof of (4.6.1): 'Posons X_p=X×_Y Spec(𝒪_y/m^{p+1}), de sorte que'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nX_p=X\\times_Y\\operatorname{Spec}\n(\\mathcal O_y/\\mathfrak m_y^{p+1}),\n\\]",
    "$X_p=X\\times_Y\\operatorname{Spec}\n(\\mathcal O_y/\\mathfrak m_y^{p+1})$,",
    "Layout: the print sets this formula inline; the comma follows the formula.")
c2(139, P140 + "proof of (4.6.1): 'même espace sous-jacent (I, 3.6.1)'", "(I, 3.6.1)", r"(\textbf{I}, 3.6.1)", "I")
add(139, P140 + "proof of (4.6.1): 'l'hypothèse de récurrence H^n(X_{p-1}, F⊗(𝒪_y/m^p))=0 entraîne donc'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nH^n\\bigl(X_{p-1},\\mathcal F\\otimes_{\\mathcal O_Y}\n(\\mathcal O_y/\\mathfrak m_y^p)\\bigr)=0\n\\]",
    "$H^n\\bigl(X_{p-1},\\mathcal F\\otimes_{\\mathcal O_Y}\n(\\mathcal O_y/\\mathfrak m_y^p)\\bigr)=0$",
    "Layout: the print sets this formula inline in the running text; the TeX displays it.")
add(139, P140 + "proof of (4.6.1): 'entraîne donc H^n(X_p, F⊗(𝒪_y/m^p))=0; d'autre part'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nH^n\\bigl(X_p,\\mathcal F\\otimes_{\\mathcal O_Y}\n(\\mathcal O_y/\\mathfrak m_y^p)\\bigr)=0~;\n\\]",
    "$H^n\\bigl(X_p,\\mathcal F\\otimes_{\\mathcal O_Y}\n(\\mathcal O_y/\\mathfrak m_y^p)\\bigr)=0$~;",
    "Layout: the print sets this formula inline; the semicolon follows the formula.")
add(139, P140 + "proof of (4.6.1), (4.6.1.1): 'H^n(X_p, m^pF/m^{p+1}F)=0' then 'car alors'",
    "no full stop after the formula (crop)", "full stop before \\tag{4.6.1.1}", "punctuation", None, "high",
    "\\mathfrak m_y^p\\mathcal F/\\mathfrak m_y^{p+1}\\mathcal F\\bigr)=0.\n\\tag{4.6.1.1}",
    "\\mathfrak m_y^p\\mathcal F/\\mathfrak m_y^{p+1}\\mathcal F\\bigr)=0\n\\tag{4.6.1.1}",
    "The sentence continues 'car alors ...'.")

# ---------------------------------------------------------------- page 140
add(140, "Proof of (4.6.1): 'la fibre Z=f^{-1}(y)=X×_Y Spec(k(y))'", "bold italic k", "Spec(k(y))", "convention", 1,
    "high", "\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))", "Bold italic k of the residue field.")
add(140, "Proof of (4.6.1): 'de sorte que H^n(Z, m^pF/m^{p+1}F)=H^n(X_p, m^pF/m^{p+1}F). Cela étant'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nH^n\\bigl(Z,\\mathfrak m_y^p\\mathcal F/\n\\mathfrak m_y^{p+1}\\mathcal F\\bigr)\n"
    "=H^n\\bigl(X_p,\\mathfrak m_y^p\\mathcal F/\n\\mathfrak m_y^{p+1}\\mathcal F\\bigr).\n\\]",
    "$H^n\\bigl(Z,\\mathfrak m_y^p\\mathcal F/\n\\mathfrak m_y^{p+1}\\mathcal F\\bigr)\n"
    "=H^n\\bigl(X_p,\\mathfrak m_y^p\\mathcal F/\n\\mathfrak m_y^{p+1}\\mathcal F\\bigr)$.",
    "Layout: the print sets this formula inline in the running text; the TeX displays it.")
add(140, "(4.6.1.2): '(F/m_yF)⊗_{k(y)}(m^p/m^{p+1})'", "bold k in the subscript (8x crop: bold upright form)",
    "\\otimes_{k(y)}", "convention", 1, "high",
    "(\\mathcal F/\\mathfrak m_y\\mathcal F)\n\\otimes_{k(y)}", "(\\mathcal F/\\mathfrak m_y\\mathcal F)\n\\otimes_{\\mathbf{k}(y)}",
    "In subscripts the print's k is bold upright (sans-serif-like), not bold italic: \\mathbf{k}.")
add(140, "Proof of (4.6.1): '(4.6.1.2) est bijectif; cela établi'", "'bijectif' italic (crop)", "bijectif in roman",
    "italics", None, "high", "est bijectif~; cela", "est \\emph{bijectif}~; cela", "The word bijectif is italic in the print.")
add(140, "Proof of (4.6.1): 'est un k(y)-module libre'", "bold italic k", "$k(y)$-module", "convention", 1, "high",
    "un $k(y)$-module libre", "un $\\boldsymbol{k}(y)$-module libre", "Bold italic k of the residue field.")
add(140, "Proof of (4.6.1): display 'H^n(Z, F/m_yF)⊗_{k(y)}(m^p/m^{p+1})=0'", "bold k in the subscript (bold upright form)",
    "\\otimes_{k(y)}", "convention", 1, "high",
    "\\bigr)\n\\otimes_{k(y)}(\\mathfrak m_y^p", "\\bigr)\n\\otimes_{\\mathbf{k}(y)}(\\mathfrak m_y^p",
    "In subscripts the print's k is bold upright, not bold italic: \\mathbf{k}.")
c2(140, "Proof of (4.6.1): '(0, 12.2.3), puisque'", "(0, 12.2.3)", r"(\textbf{0}, 12.2.3)", "0")
add(140, "Proof of (4.6.1): 'F_x est un 𝒪_y-module plat par hypothèse'", "'plat' italic (crop)", "plat in roman",
    "italics", None, "high", "$\\mathcal O_y$-module plat par", "$\\mathcal O_y$-module \\emph{plat} par",
    "The word plat is italic in the print.")
add(140, "Proof of (4.6.1): 'il suffit d'appliquer (0, 10.2.1, c))'", "c) italic, bold 0 (3x crop)", "(0, 10.2.1, c))",
    "italics", None, "high", "(0, 10.2.1, c))", "(\\textbf{0}, 10.2.1, \\emph{c)})",
    "The letter label c) is italic in the print. One edit for this finding and the next (convention 2).")
add(140, "Proof of (4.6.1): same reference (0, 10.2.1, c))", "bold 0", "(0, 10.2.1, c))", "convention", 2, "high",
    None, None, COVERED)
add(140, "Proof of (4.6.1): 'sur le corps k(y)=𝒪_y/m_y'", "bold italic k", "$k(y)=...", "convention", 1, "high",
    "$k(y)=\\mathcal O_y/\\mathfrak m_y$", "$\\boldsymbol{k}(y)=\\mathcal O_y/\\mathfrak m_y$",
    "Bold italic k of the residue field.")
add(140, "Proof of (4.6.1), (4.6.1.3): 'H^n(X_{k+1}, m^kF/m^{k+p+1}F)=0' (continued on p. 141 'd'où on déduit')",
    "no full stop after the formula (crop)", "full stop before \\tag{4.6.1.3}", "punctuation", None, "high",
    "\\mathfrak m_y^{k+p+1}\\mathcal F\\bigr)=0.\n\\tag{4.6.1.3}", "\\mathfrak m_y^{k+p+1}\\mathcal F\\bigr)=0\n\\tag{4.6.1.3}",
    "The sentence continues on p. 141.")
add(140, "End of p. 140: (4.6.1.3) display, then the page break to 'd'où on déduit' (p. 141)",
    "the sentence runs on: p. 141 begins flush left 'd'où on déduit' (no paragraph indent)",
    "blank line after the display (before \\oldpage[III]{141})", "other", None, "high",
    "\\tag{4.6.1.3}\n\\]\n\n", "\\tag{4.6.1.3}\n\\]\n",
    "Blank lines around \\oldpage at a mid-sentence page break (GLOBAL_ISSUES item 20). Apply together with the "
    "first finding of p. 141 (blank line after the marker).")

# ---------------------------------------------------------------- page 141
add(141, "Top of p. 141: 'd'où on déduit, par (4.2.1), que l'on a aussi'",
    "flush left: continues the sentence of p. 140", "blank line after \\oldpage[III]{141}: a new paragraph",
    "other", None, "high", "\\oldpage[III]{141}\n\nd'où on déduit", "\\oldpage[III]{141}\nd'où on déduit",
    "Blank lines around \\oldpage at a mid-sentence page break (GLOBAL_ISSUES item 20). Apply together with the "
    "last non-marker finding of p. 140 (blank line before the marker).")
add(141, "Proof of (4.6.1): 'Cela étant, on tire de la suite exacte' after (4.6.1.4)",
    "'Cela étant' is indented: a new paragraph", "no blank line after the display", "other", None, "high",
    "\\tag{4.6.1.4}\n\\]\nCela étant, on tire", "\\tag{4.6.1.4}\n\\]\n\nCela étant, on tire",
    "Paragraph break missing after the display.")
add(141, "Corollaire (4.6.2): 'Posons X_y=f^{-1}(y)=X⊗_Y k(y), F_y=F⊗k(y), G_y=G⊗k(y), et supposons'",
    "the formulas are set inline in the running text; bold italic k (three times)",
    r"displayed with \[ ... \] and \qquad; plain k", "other", None, "high",
    "\\[\nX_y=f^{-1}(y)=X\\otimes_Yk(y),\\qquad\n\\mathcal F_y=\\mathcal F\\otimes_{\\mathcal O_Y}k(y),\\qquad\n"
    "\\mathcal G_y=\\mathcal G\\otimes_{\\mathcal O_Y}k(y),\n\\]",
    "$X_y=f^{-1}(y)=X\\otimes_Y\\boldsymbol{k}(y)$,\n$\\mathcal F_y=\\mathcal F\\otimes_{\\mathcal O_Y}\\boldsymbol{k}(y)$,\n"
    "$\\mathcal G_y=\\mathcal G\\otimes_{\\mathcal O_Y}\\boldsymbol{k}(y)$,",
    "Layout: inline in the print. One edit for this finding and the three next ones (convention 1).")
for w in ("X⊗_Y k(y)", "F⊗_{𝒪_Y} k(y)", "G⊗_{𝒪_Y} k(y)"):
    add(141, "Corollaire (4.6.2): '" + w + "'", "bold italic k", "k(y)", "convention", 1, "high", None, None,
        "Covered by the layout edit of this display (one edit).")
add(141, "Corollaire (4.6.2): 'Alors, pour tout homomorphisme' after (4.6.2.1)",
    "'Alors' is indented: a new paragraph", "no blank line after the display", "other", None, "high",
    "\\tag{4.6.2.1}\n\\]\nAlors, pour tout", "\\tag{4.6.2.1}\n\\]\n\nAlors, pour tout",
    "Paragraph break missing after the display.")
add(141, "Corollaire (4.6.2): 'il existe un voisinage ouvert U de Y et un homomorphisme'",
    "capital roman Y (crop)", "$y$", "misprint_in_print", None, "high",
    "$U$ de $y$ et un", "$U$ de $Y$ et un",
    "U is a neighbourhood of the point y (as in (4.6.4), (4.6.5)). The TeX silently corrects; the fix restores the "
    "printed reading.",
    corrected="$U$ de $y$ et un")
add(141, "Corollaire (4.6.2): 'et un homomorphisme u : F|f^{-1}(U)→G|f^{-1}(U) tels que'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nu:\\mathcal F|f^{-1}(U)\\longrightarrow\\mathcal G|f^{-1}(U)\n\\]",
    "$u:\\mathcal F|f^{-1}(U)\\longrightarrow\\mathcal G|f^{-1}(U)$",
    "Layout: inline in the print. Apply this edit before the next finding (misprint F), whose old lies inside "
    "this span; this edit keeps \\mathcal F unchanged.")
add(141, "Corollaire (4.6.2): 'u : F|f^{-1}(U)→G|f^{-1}(U)'", "roman capital F, not script ℱ (crop; G is script)",
    "\\mathcal F", "misprint_in_print", None, "high", "u:\\mathcal F|f^{-1}(U)", "u:F|f^{-1}(U)",
    "Wrong-font F in the print (the sheaf ℱ is meant). The TeX silently corrects; the fix restores the printed "
    "reading. Apply after the preceding layout edit.",
    corrected="u:\\mathcal F|f^{-1}(U)")
add(141, "Proof of (4.6.2): 'le 𝒪_{X_y}-Module H⊗_{𝒪_Y} k(y)'", "bold italic k", "k(y)", "convention", 1, "high",
    "\\mathcal H\\otimes_{\\mathcal O_Y}k(y)", "\\mathcal H\\otimes_{\\mathcal O_Y}\\boldsymbol{k}(y)",
    "Bold italic k of the residue field.")
c2(141, "Proof of (4.6.2): '(0_I, 6.2.2). On peut supposer'", r"(0\textsubscript{I}, 6.2.2)",
   r"(\textbf{0}\textsubscript{I}, 6.2.2)", "0")
add(141, "Proof of (4.6.2): 'et alors (1.4.11) R^0f_*(H)=(Hom(F, G))~, donc'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\nR^0f_*(\\mathcal H)=\n\\bigl(\\operatorname{Hom}_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\\bigr)^\\sim,\n\\]",
    "$R^0f_*(\\mathcal H)=\n\\bigl(\\operatorname{Hom}_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\\bigr)^\\sim$,",
    "Layout: inline in the print; the comma follows the formula.")
add(141, "Proof of (4.6.2): 'donc (R^0f_*(H))_y=Hom(F, G)⊗_A 𝒪_y; l'homomorphisme canonique'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    "\\[\n\\bigl(R^0f_*(\\mathcal H)\\bigr)_y\n=\\operatorname{Hom}_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\n"
    "\\otimes_A\\mathcal O_y~;\n\\]",
    "$\\bigl(R^0f_*(\\mathcal H)\\bigr)_y\n=\\operatorname{Hom}_{\\mathcal O_X}(\\mathcal F,\\mathcal G)\n"
    "\\otimes_A\\mathcal O_y$~;",
    "Layout: inline in the print; the semicolon follows the formula.")
add(141, "Corollaire (4.6.3): 'Sous les hypothèses de (4.6.2), si u_0'",
    "the reference (4.6.2) is upright inside the italic statement",
    "(4.6.2) inside the italic corollary environment: italic", "convention", 6, "high",
    "(\\hyperref[III.4.6.2-fr]{4.6.2}), si", "\\textup{(\\hyperref[III.4.6.2-fr]{4.6.2})}, si",
    "Upright reference in an italic statement.")
add(141, "Corollaire (4.6.3): 'si u_0 est injectif (resp. surjectif, bijectif)'",
    "'(resp.' upright, 'surjectif, bijectif' italic (crop)", "(resp. inside the italic environment: italic",
    "convention", 6, "high", "injectif (resp. surjectif, bijectif)", "injectif \\textup{(resp.} surjectif, bijectif)",
    "Roman word in an italic statement.")
c2(141, "Proof of (4.6.3): 'Modules cohérents (0_I, 5.3.4)'", r"(0\textsubscript{I}, 5.3.4)",
   r"(\textbf{0}\textsubscript{I}, 5.3.4)", "0")
c2(141, "Proof of (4.6.3): 'à V soit 0 (0_I, 5.2.2)'", r"(0\textsubscript{I}, 5.2.2)",
   r"(\textbf{0}\textsubscript{I}, 5.2.2)", "0")
add(141, "Proof of (4.6.3): 'Par hypothèse, u_x⊗1 : F_x⊗k(y)→G_x⊗k(y) est injectif'",
    "the formula is set inline in the running text; bold italic k (twice)", r"displayed with \[ ... \]; plain k",
    "other", None, "high",
    "\\[\nu_x\\otimes1:\n\\mathcal F_x\\otimes_{\\mathcal O_y}k(y)\n\\longrightarrow\n\\mathcal G_x\\otimes_{\\mathcal O_y}k(y)\n\\]",
    "$u_x\\otimes1:\n\\mathcal F_x\\otimes_{\\mathcal O_y}\\boldsymbol{k}(y)\n\\longrightarrow\n"
    "\\mathcal G_x\\otimes_{\\mathcal O_y}\\boldsymbol{k}(y)$",
    "Layout: inline in the print. One edit for this finding and the two next ones (convention 1).")
for w in ("F_x⊗_{𝒪_y} k(y)", "G_x⊗_{𝒪_y} k(y)"):
    add(141, "Proof of (4.6.3): '" + w + "'", "bold italic k", "k(y)", "convention", 1, "high", None, None,
        "Covered by the layout edit of this display (one edit).")

# ---------------------------------------------------------------- page markers (apply last, in this order)
add(139, "Top of p. 139: \\oldpage[III]{139} before 'Si on désigne'",
    "printed p. 139 begins 'de H^p(X, Ext^q(F, G)) pour la topologie J-préadique. Si on désigne ...' (one paragraph)",
    "marker after 'préadique.' and a paragraph break", "marker", None, "high",
    "\\oldpage[III]{139}\n\nSi on désigne", "Si on désigne",
    "Step 1 of the move of \\oldpage[III]{139}: remove it here, then apply the next finding (p. 138), which "
    "re-inserts it before 'de' and joins the paragraph. Apply both after all other fixes of pp. 138-139.")
add(138, "End of p. 138: 's'identifie canoniquement au séparé complété | de H^p(X, ...)'",
    "printed p. 138 ends with 'séparé complété'; p. 139 begins with 'de'", "marker after 'préadique.'", "marker",
    None, "high",
    "séparé complété de\n$\\mathrm H^p\\bigl(X,\\mathcal{E}\\!xt^q_{\\mathcal O_X}\n(\\mathcal F,\\mathcal G)\\bigr)$ "
    "pour la topologie $\\mathfrak J$-préadique.\n\n",
    "séparé complété\n\\oldpage[III]{139}\nde\n$\\mathrm H^p\\bigl(X,\\mathcal{E}\\!xt^q_{\\mathcal O_X}\n"
    "(\\mathcal F,\\mathcal G)\\bigr)$ pour la topologie $\\mathfrak J$-préadique.\n",
    "Step 2 of the move of \\oldpage[III]{139} (after the removal in the preceding finding): the marker goes "
    "before 'de', and the blank line after 'préadique.' goes, since 'Si on désigne' continues the paragraph.")
add(140, "Top of p. 140 segment: \\oldpage[III]{140} before 'Notons maintenant'",
    "printed p. 140 begins 'entier n, on ait H^n(f^{-1}(y), ...)' inside Proposition (4.6.1)",
    "marker about 60 lines too late", "marker", None, "high",
    "\\oldpage[III]{140}\n\nNotons maintenant", "Notons maintenant",
    "Step 1 of the move of \\oldpage[III]{140}: remove it here (the paragraph break before 'Notons maintenant' "
    "stays; it is printed), then apply the next finding (p. 139).")
add(139, "Proposition (4.6.1): 'Supposons que pour un | entier n, on ait'",
    "printed p. 139 ends with 'Supposons que pour un'", "no marker here", "marker", None, "high",
    "Supposons que pour un entier $n$, on ait", "Supposons que pour un\n\\oldpage[III]{140}\nentier $n$, on ait",
    "Step 2 of the move of \\oldpage[III]{140} (after the removal in the preceding finding).")
add(141, "Proof of (4.6.3): 'est injectif (resp. surjectif), | F_x et G_x sont des'",
    "printed p. 141 ends with 'est injectif (resp. surjectif),'", "no \\oldpage[III]{142} anywhere in ega3-1-fr.tex",
    "marker", None, "high",
    "surjectif), $\\mathcal F_x$ et $\\mathcal G_x$ sont des",
    "surjectif),\n\\oldpage[III]{142}\n$\\mathcal F_x$ et $\\mathcal G_x$ sont des",
    "The marker for p. 142 is missing: the rest of this segment (to \\oldpage[III]{143}) is printed p. 142 and was "
    "not in any check batch.")

# ---------------------------------------------------------------- checks
ok = True
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(137, 142)}
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    c = pages[x["page"]].count(fx["old"])
    if c != 1:
        ok = False
        print("PAGE-FILE COUNT", c, "for finding", i, x["page"], repr(fx["old"])[:80])
    if "\\u" in fx["old"] or "\\u" in fx["new"] or "\t" in fx["old"] or "\t" in fx["new"]:
        print("suspicious escape in finding", i)

# simulate apply_fixes.py on a copy of the diplomatic file (only ega3-1-fr.tex, as with --only)
text = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for j, (n, s) in enumerate(cuts):
        if n == page:
            return s, (cuts[j + 1][1] if j + 1 < len(cuts) else len(t))
    return None, None


applied = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx or not fx.get("old") or fx["old"] == fx["new"]:
        continue
    s, e = locate(text, x["page"])
    if s is None:
        ok = False
        print("SIM page not found", i, x["page"])
        continue
    seg = text[s:e]
    if seg.count(fx["old"]) != 1:
        ok = False
        print("SIM count", seg.count(fx["old"]), "finding", i, x["page"], repr(fx["old"])[:80])
        continue
    text = text[:s] + seg.replace(fx["old"], fx["new"]) + text[e:]
    applied += 1
print("simulated edits applied:", applied, "of", sum(1 for x in F if x["fix"]))
sim = RUN / "crops_137_141" / "sim_after_fixes.txt"
sim.write_text(text, encoding="utf-8", newline="")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
for n, s in cuts:
    if 137 <= n <= 143:
        print("marker", n, "context:", repr(text[max(0, s - 70):s + 45]))

counts = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("counts", counts, "total", len(F))
print("ALL CHECKS OK" if ok else "CHECKS FAILED")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
