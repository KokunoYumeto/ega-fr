"""Write findings_050_055.json and check every fix: "old" once in its page_NNN.tex (LF), and a dry simulation of
apply_fixes.py (sequential, page segments between markers) on an in-memory copy of the release file.
usage: python make_findings.py"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "findings_050_055.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\BASE\native\ega3\ega3-1-fr.tex")

F = []


def add(page, where, scan, tex, kind, fix, note, conf="high", conv=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


CHECK = ("The print has no check accent on the Cech complex/cohomology of a covering: C·(U, F), H^p(U, F) "
         "(checked at 4x on pp. 50-52).")
PARTIAL = ("The print writes ∂-foncteur (the same glyph as the operator ∂ in (12.1.2)); ega3-1-fr.tex itself writes "
           "$\\partial$-foncteurs in §11.2 ('Nous ne revenons pas sur la définition des ∂-foncteurs (T, 2.1)'). "
           "These are all 6 \\delta-foncteur in the file (pp. 50, 51, 55).")
K_NOTE = ("The third module of (12.1.5) is printed script K (𝒦) throughout (12.1.5), pp. 53-54; script H (ℋ) "
          "is a different glyph, see (12.1.6.1) on p. 55. Apply with the other \\mathcal H -> \\mathcal K fixes of (12.1.5).")

# ---------------- p. 50 ----------------
add(50, "end of (12.1.1), line 1: 'à la restriction à la catégorie C(X)'", "catégorie 𝑪(X): bold italic C",
    "catégorie $C(X)$", "font", fx(r"catégorie $C(X)$ du", r"catégorie $\boldsymbol{C}(X)$ du"),
    "Category letter in bold italic, as for the categories C fixed on pp. 8-10 (\\boldsymbol{C}).")
add(50, "(12.1.2), line 2: 'un endomorphisme de ∂-foncteur de H·(X, F)'", "endomorphisme de ∂-foncteur",
    r"endomorphisme de $\delta$-foncteur", "symbol",
    fx(r"endomorphisme de $\delta$-foncteur", r"endomorphisme de $\partial$-foncteur"), PARTIAL)
add(50, "(12.1.2), line 3: 'une structure de A-module, et l'opérateur ∂'", "A-*module* (module italic)",
    r"structure de $A$-module, et", "italics", fx(r"structure de $A$-module, et", r"structure de $A$-\emph{module}, et"),
    "Only 'module' is italic; A and the hyphen upright.")
add(50, "(12.1.2), after (12.1.2.1): 'une A-algèbre graduée anticommutative'",
    "A-*algèbre graduée anticommutative* (italic)", "$A$-algèbre graduée anticommutative (upright)", "italics",
    fx("$A$-algèbre graduée\nanticommutative", "$A$-\\emph{algèbre graduée\nanticommutative}"), "")
add(50, "(12.1.2), after (12.1.2.1): 'un S-module gradué.'", "S-*module gradué* (italic)", "$S$-module gradué",
    "italics", fx("$S$-module\ngradué.", "$S$-\\emph{module\ngradué}."), "")
add(50, "(12.1.2), 2nd paragraph: 'nous désignerons toujours par C·(U, F)'", "C·(U, F), no check accent",
    r"$\check C^\bullet(\mathfrak U,\mathcal F)$", "symbol",
    fx(r"toujours par $\check C^\bullet(\mathfrak U,\mathcal F)$", r"toujours par $C^\bullet(\mathfrak U,\mathcal F)$"),
    CHECK)
add(50, "(12.1.2), 2nd paragraph: 'le système de coefficients Γ(U_σ, F)'", "Γ(U_σ, F): subscript sigma",
    r"$\Gamma(U_\alpha,\mathcal F)$", "symbol", fx(r"\Gamma(U_\alpha,\mathcal F)", r"\Gamma(U_\sigma,\mathcal F)"),
    "Checked at 4x: the subscript is σ (simplex of the nerve), not the α of 𝔘 = (U_α) on p. 51.")
add(50, "(12.1.2), 2nd paragraph: 'Il est clair que C·(U, F) est un'", "C·(U, F), no check accent",
    r"$\check C^\bullet(\mathfrak U,\mathcal F)$ est un", "symbol",
    fx(r"$\check C^\bullet(\mathfrak U,\mathcal F)$ est un", r"$C^\bullet(\mathfrak U,\mathcal F)$ est un"), CHECK)
add(50, "(12.1.2), 2nd paragraph: 'est un A-module gradué, donc'", "A-*module gradué* (italic)",
    "$A$-module gradué (upright)", "italics", fx(r"$A$-module gradué, donc", r"$A$-\emph{module gradué}, donc"), "")
add(50, "(12.1.2), 2nd paragraph: 'les groupes de cohomologie H^p(U, F)'", "H^p(U, F), no check accent",
    r"$\check H^p(\mathfrak U,\mathcal F)$", "symbol",
    fx(r"cohomologie $\check H^p(\mathfrak U,\mathcal F)$", r"cohomologie $H^p(\mathfrak U,\mathcal F)$"), CHECK)
add(50, "(12.1.2), 2nd paragraph: 'd'une structure de A-module; en outre'", "A-*module* (italic)",
    "$A$-module (upright)", "italics",
    fx(r"structure de $A$-module; en outre", r"structure de $A$-\emph{module}; en outre"), "")
add(50, "(12.1.2), end: 'les applications canoniques H^p(U, F) → H^p(X, F) (G, II, 5.4)'",
    "inline formula in the text line, H^p(U, F) without check accent", "displayed \\[ \\check H^p(...)\\longrightarrow"
    " H^p(X,\\mathcal F) \\]", "other",
    fx("canoniques\n\\[\n\\check H^p(\\mathfrak U,\\mathcal F)\\longrightarrow H^p(X,\\mathcal F)\n\\]\n(G, II, 5.4)",
       "canoniques\n$H^p(\\mathfrak U,\\mathcal F)\\to H^p(X,\\mathcal F)$\n(G, II, 5.4)"),
    "Display -> inline (as printed); the same edit drops the check accent (see the other check-accent findings).")
add(50, "(12.1.2), end: 'sont A-linéaires.'", "A-*linéaires* (italic)", "$A$-linéaires (upright)", "italics",
    fx(r"sont $A$-linéaires.", r"sont $A$-\emph{linéaires}."), "")
add(50, "(12.1.3), 2nd paragraph: 'pour tout f-morphisme u : F → F''", "*f-morphisme* (italic, as 'di-homomorphisme')",
    "$f$-morphisme (morphisme upright)", "italics", fx(r"$f$-morphisme $u:", r"\emph{$f$-morphisme} $u:"), "")
add(50, "(12.1.3): reference (0_I, 4.4.1)", "bold 0 with subscript I", r"0\textsubscript{I}, 4.4.1", "convention",
    fx(r"{0\textsubscript{I}, 4.4.1}", r"{\textbf{0}\textsubscript{I}, 4.4.1}"), "", conv=2)
add(50, "(12.1.3), after (12.1.3.1): 'sur X, F ⇝ H·(X', ψ*(F)) est un ∂-foncteur'", "F ⇝ H·(...): squiggly arrow",
    r"$\mathcal F\to H^\bullet(X',\psi^*(\mathcal F))$", "symbol",
    fx(r"$\mathcal F\to H^\bullet(X',\psi^*(\mathcal F))$ est un",
       r"$\mathcal F\leadsto H^\bullet(X',\psi^*(\mathcal F))$ est un"),
    "Functor notation with the squiggly arrow, as in (12.1.7) 'F' ⇝ Γ(...)' where the TeX has \\leadsto.")
add(50, "(12.1.3), after (12.1.3.1): 'est un ∂-foncteur dans cette catégorie'", "∂-foncteur",
    r"$\delta$-foncteur", "symbol", fx(r"$\delta$-foncteur dans cette", r"$\partial$-foncteur dans cette"), PARTIAL)
add(50, "(12.1.3), before (12.1.3.2): 'un homomorphisme canonique de ∂-foncteurs'", "∂-foncteurs",
    r"$\delta$-foncteurs", "symbol", fx(r"canonique de $\delta$-foncteurs", r"canonique de $\partial$-foncteurs"), PARTIAL)
add(50, "(12.1.3), after (12.1.3.1): paragraph 'En effet, comme ψ* est exact'",
    "new indented paragraph after the display", "no blank line after \\]: the text continues the paragraph", "other",
    fx("\\]\nEn effet, comme", "\\]\n\nEn effet, comme"), "Paragraph break as printed (indented line).")

# ---------------- p. 51 text (inside page_050.tex: no \oldpage{51} yet; filed under page 50) ----------------
P51 = "p. 51 (text in page_050.tex, filed under page 50): "
add(50, P51 + "(12.1.3): 'est un homomorphisme de A-modules. Notons'", "A-*modules* (italic)", "$A$-modules (upright)",
    "italics", fx(r"$A$-modules. Notons", r"$A$-\emph{modules}. Notons"), "")
add(50, P51 + "(12.1.3): 'que l'on a f*(F) = ψ*(F) ⊗_{ψ*(O_X)} O_X', et que'", "inline formula in the text line",
    "displayed \\[ ... \\]", "other",
    fx("que l'on a\n\\[\nf^*(\\mathcal F)=\\psi^*(\\mathcal F)\n\\otimes_{\\psi^*(\\mathcal O_X)}\\mathcal O_{X'},\n\\]\n"
       "et que",
       "que l'on a\n$f^*(\\mathcal F)=\\psi^*(\\mathcal F)\n\\otimes_{\\psi^*(\\mathcal O_X)}\\mathcal O_{X'}$,\net que"),
    "Display -> inline, as printed.")
add(50, P51 + "(12.1.3): 'un di-homomorphisme canonique fonctoriel en F'", "*fonctoriel* (italic)",
    "fonctoriel (upright)", "italics", fx(r"canonique fonctoriel en", r"canonique \emph{fonctoriel} en"), "")
add(50, P51 + "(12.1.3), after (12.1.3.5): paragraph 'Enfin, par fonctorialité, on déduit'",
    "new indented paragraph after the display", "no blank line after \\]", "other",
    fx("\\]\nEnfin, par fonctorialité, on déduit", "\\]\n\nEnfin, par fonctorialité, on déduit"),
    "Paragraph break as printed (indented line).")
add(50, P51 + "(12.1.3), last paragraph: 'f'' = f∘f' le morphisme composé'", "f''=f∘f' (composition circle)",
    "$f''=ff'$", "symbol", fx(r"$f''=ff'$", r"$f''=f\circ f'$"), "Checked at 3x: small circle between f and f'.")
add(50, P51 + "(12.1.3): reference (0_I, 4.3.3)", "bold 0 with subscript I", r"0\textsubscript{I}, 4.3.3",
    "convention", fx(r"{0\textsubscript{I}, 4.3.3}", r"{\textbf{0}\textsubscript{I}, 4.3.3}"), "", conv=2)
add(50, P51 + "(12.1.4): 'ψ*(L·) est une résolution de ψ*(F)'", "*résolution* (italic)", "résolution (upright)",
    "italics", fx("est une résolution\nde", "est une \\emph{résolution}\nde"), "")
add(50, P51 + "(12.1.4): '(M, V, 1.1.a))'", "1.1.*a)*): italic a and its closing parenthesis, outer ')' upright",
    "(M, V, 1.1.a)) all upright", "italics", fx(r"(M, V, 1.1.a))", r"(M, V, 1.1.\emph{a)})"),
    "Checked at 8x: the first ')' is slanted like the a, the second upright.")
add(50, P51 + "(12.1.4): 'donne un morphisme de ∂-foncteurs'", "∂-foncteurs", r"$\delta$-foncteurs", "symbol",
    fx(r"morphisme de $\delta$-foncteurs", r"morphisme de $\partial$-foncteurs"), PARTIAL)
add(50, P51 + "(12.1.4), last lines: 'un homomorphisme de complexes C·(U, F) → C·(U', f*(F))'",
    "C·(U, F) → C·(U', f*(F)), no check accents", r"\check C^\bullet ... \check C^\bullet", "symbol",
    fx("$\\check C^\\bullet(\\mathfrak U,\\mathcal F)\\to\n\\check C^\\bullet(\\mathfrak U',f^*(\\mathcal F))$",
       "$C^\\bullet(\\mathfrak U,\\mathcal F)\\to\nC^\\bullet(\\mathfrak U',f^*(\\mathcal F))$"), CHECK)
add(50, P51 + "(12.1.4.1)", "θ_p : H^p(U, F) → H^p(U', f*(F)). no check accents", r"\check H^p ... \check H^p",
    "symbol",
    fx("\\theta_p:\\check H^p(\\mathfrak U,\\mathcal F)\n\\longrightarrow\\check H^p(\\mathfrak U',f^*(\\mathcal F)).",
       "\\theta_p:H^p(\\mathfrak U,\\mathcal F)\n\\longrightarrow H^p(\\mathfrak U',f^*(\\mathcal F))."), CHECK)
add(50, "page break 50/51: printed p. 51 begins 'soit commutatif; par la propriété d'unicité' (after diagram "
         "(12.1.3.3), which ends p. 50); p. 51 ends with (12.1.4.1), p. 52 begins 'En outre, on a des diagrammes'",
    "p. 51 starts at 'soit commutatif;'", "no \\oldpage[0\\textsubscript{III}]{51} in the source", "marker",
    fx("\\]\nsoit commutatif;", "\\]\n\\oldpage[0\\textsubscript{III}]{51}\nsoit commutatif;"),
    "Apply AFTER all other page-50 fixes (it is last among them): the p. 51 text fixes above are filed under page 50 "
    "because that text is still inside the page-50 segment.")

# ---------------- p. 52 ----------------
add(52, "(12.1.4.2), top row", "H^p(U, F) →θ_p H^p(U', f*(F)), no check accents", r"\check H^p ... \check H^p",
    "symbol",
    fx("\\check H^p(\\mathfrak U,\\mathcal F)\\ar[r]^{\\theta_p}\\ar[d]\n&\\check H^p(\\mathfrak U',f^*(\\mathcal F))",
       "H^p(\\mathfrak U,\\mathcal F)\\ar[r]^{\\theta_p}\\ar[d]\n&H^p(\\mathfrak U',f^*(\\mathcal F))"), CHECK)
add(52, "after (12.1.4.2): 'tel que Γ(X, 𝒞·(U, F)) = C·(U, F) (G, II, 5.2)'", "= C·(U, F), no check accent",
    r"\check C^\bullet(\mathfrak U,\mathcal F)", "symbol",
    fx(r"\check C^\bullet(\mathfrak U,\mathcal F)$ (G, II, 5.2)", r"C^\bullet(\mathfrak U,\mathcal F)$ (G, II, 5.2)"),
    CHECK)
add(52, "diagram after 'qui, en passant à la cohomologie', top row", "H^p(U, F) → H^p(U', ψ*(F)), no check accents",
    r"\check H^p ... \check H^p", "symbol",
    fx("\\check H^p(\\mathfrak U,\\mathcal F)\\ar[r]\\ar[d]\n&\\check H^p(\\mathfrak U',\\psi^*(\\mathcal F))",
       "H^p(\\mathfrak U,\\mathcal F)\\ar[r]\\ar[d]\n&H^p(\\mathfrak U',\\psi^*(\\mathcal F))"), CHECK)
add(52, "last diagram of the page, top row", "H^p(U', ψ*(F)) → H^p(U', f*(F)), no check accents",
    r"\check H^p ... \check H^p", "symbol",
    fx("\\check H^p(\\mathfrak U',\\psi^*(\\mathcal F))\\ar[r]\\ar[d]\n&\\check H^p(\\mathfrak U',f^*(\\mathcal F))",
       "H^p(\\mathfrak U',\\psi^*(\\mathcal F))\\ar[r]\\ar[d]\n&H^p(\\mathfrak U',f^*(\\mathcal F))"), CHECK)
add(52, "unnumbered diagram 'avec les notations ci-dessus, un diagramme commutatif' (Γ(X, 𝒞·(U, F)) → Γ(X', 𝒞·(U', "
         "ψ*(F))) over Γ(X, L·) → Γ(X', ψ*(L·)) → Γ(X', L'·))",
    "the right vertical arrow from Γ(X', 𝒞·(U', ψ*(F))) ends at the middle entry Γ(X', ψ*(L·))",
    "same layout (\\ar[d] from column 2 to Γ(X',\\psi^*(\\mathcal L^\\bullet)))", "misprint_in_print", None,
    "TeX keeps the printed layout. Passing to cohomology must give H^p(U', ψ*(F)) → H^p(X', ψ*(F)), computed by "
    "Γ(X', L'·) (injective resolution of ψ*(F)); there is no map 𝒞·(U', ψ*(F)) → ψ*(L·) in general. Corrected: the "
    "arrow ends at Γ(X', L'·).", conf="medium",
    corrected="\\xymatrix{\n\\Gamma(X,\\mathcal C^\\bullet(\\mathfrak U,\\mathcal F))\\ar[rr]\\ar[d]\n&&\\Gamma(X',"
              "\\mathcal C^\\bullet(\\mathfrak U',\\psi^*(\\mathcal F)))\\ar[d]\\\\\n\\Gamma(X,\\mathcal L^\\bullet)\\ar[r]"
              "\n&\\Gamma(X',\\psi^*(\\mathcal L^\\bullet))\\ar[r]\n&\\Gamma(X',\\mathcal L'^\\bullet)\n}")

# ---------------- p. 53 ----------------
add(53, "(12.1.4), last paragraph: 'l'homomorphisme (12.1.4.3) est un di-homomorphisme'", "(12.1.4.3)", "(12.1.4.3)",
    "misprint_in_print", None,
    "TeX keeps the printed reading. There is no (12.1.4.3); the homomorphism meant is θ_p of (12.1.4.1), whose "
    "transitivity is stated in the next sentence.", corrected=r"(\hyperref[0.12.1.4.1-fr]{12.1.4.1})")
add(53, "(12.1.5), line 1: 'Soient F, G, 𝒦 trois O_X-Modules'", "𝒦 (script K)", r"$\mathcal H$", "symbol",
    fx(r"$\mathcal G$, $\mathcal H$ trois", r"$\mathcal G$, $\mathcal K$ trois"), K_NOTE)
add(53, "(12.1.5), line 2: 'u : F ⊗_{O_X} G → 𝒦'", "→ 𝒦", r"\to\mathcal H", "symbol",
    fx(r"\to\mathcal H$, qui donne", r"\to\mathcal K$, qui donne"), K_NOTE)
add(53, "(12.1.5.1)", "H^{p+q}(X, 𝒦)", r"H^{p+q}(X,\mathcal H)", "symbol",
    fx(r"\longrightarrow H^{p+q}(X,\mathcal H)", r"\longrightarrow H^{p+q}(X,\mathcal K)"), K_NOTE)
add(53, "(12.1.5.2), top right", "H^{p+q}(X, 𝒦)", r"H^{p+q}(X,\mathcal H)", "symbol",
    fx(r"&H^{p+q}(X,\mathcal H)\ar[d]", r"&H^{p+q}(X,\mathcal K)\ar[d]"), K_NOTE)
add(53, "(12.1.5.2), bottom right", "H^{p+q}(X', f*(𝒦))", r"H^{p+q}(X',f^*(\mathcal H))", "symbol",
    fx(r"&H^{p+q}(X',f^*(\mathcal H))", r"&H^{p+q}(X',f^*(\mathcal K))"), K_NOTE)
add(53, "after (12.1.5.2): 'L·, M·, N· de F, G, 𝒦 respectivement'", "F, G, 𝒦", r"$\mathcal H$", "symbol",
    fx("$\\mathcal G$, $\\mathcal H$\nrespectivement", "$\\mathcal G$, $\\mathcal K$\nrespectivement"), K_NOTE)
add(53, "after (12.1.5.2): 'des homomorphismes H^p(Γ(X, L·)) ⊗_A H^q(Γ(X, M·)) → H^{p+q}(Γ(X, N·)) (G, II, 6.6)'",
    "inline formula in the text line", "displayed \\[ ... \\]", "other",
    fx("homomorphismes\n\\[\nH^p(\\Gamma(X,\\mathcal L^\\bullet))\\otimes_A\nH^q(\\Gamma(X,\\mathcal M^\\bullet))\n"
       "\\longrightarrow H^{p+q}(\\Gamma(X,\\mathcal N^\\bullet))\n\\]\n(G, II, 6.6)",
       "homomorphismes\n$H^p(\\Gamma(X,\\mathcal L^\\bullet))\\otimes_A\nH^q(\\Gamma(X,\\mathcal M^\\bullet))\n"
       "\\to H^{p+q}(\\Gamma(X,\\mathcal N^\\bullet))$\n(G, II, 6.6)"),
    "Display -> inline, as printed.")

# ---------------- p. 54 ----------------
add(54, "(12.1.5.4), top left", "H^p(X, F) ⊗_A H^p(X, G): second factor with superscript p",
    r"H^p(X,\mathcal F)\otimes_A H^q(X,\mathcal G)", "misprint_in_print",
    fx(r"\otimes_A H^q(X,\mathcal G)", r"\otimes_A H^p(X,\mathcal G)"),
    "TeX silently corrects; fix restores the printed H^p (checked at 3x). The cup product of (12.1.5.1) needs H^q.",
    corrected=r"H^p(X,\mathcal F)\otimes_A H^q(X,\mathcal G)")
add(54, "(12.1.5.4), top right", "H^{p+q}(X, 𝒦)", r"H^{p+q}(X,\mathcal H)", "symbol",
    fx(r"&H^{p+q}(X,\mathcal H)\ar[d]", r"&H^{p+q}(X,\mathcal K)\ar[d]"), K_NOTE)
add(54, "(12.1.5.4), bottom right", "H^{p+q}(Γ(X', ψ*(N·))). with a final period (end of sentence)",
    "no period", "punctuation", fx("\\mathcal N^\\bullet)))\n}", "\\mathcal N^\\bullet))).\n}"), "")
add(54, "after (12.1.5.4): paragraph 'Mais comme ψ*(L·)'", "new indented paragraph after the display",
    "no blank line after \\]", "other", fx("\\]\nMais comme", "\\]\n\nMais comme"), "Paragraph break as printed.")
add(54, "after (12.1.5.4): 'des résolutions de ψ*(F), ψ*(G), ψ*(𝒦) respectivement'", "ψ*(𝒦)",
    r"$\psi^*(\mathcal H)$", "symbol",
    fx("$\\psi^*(\\mathcal H)$\nrespectivement", "$\\psi^*(\\mathcal K)$\nrespectivement"), K_NOTE)
add(54, "(12.1.5.5), bottom right", "H^{p+q}(X', ψ*(𝒦))", r"H^{p+q}(X',\psi^*(\mathcal H))", "symbol",
    fx("&H^{p+q}(X',\\psi^*(\\mathcal H))\n}", "&H^{p+q}(X',\\psi^*(\\mathcal K))\n}"), K_NOTE)
add(54, "after (12.1.5.5): paragraph 'Enfin, par fonctorialité, on a un diagramme commutatif'",
    "new indented paragraph after the display", "no blank line after \\]", "other",
    fx("\\]\nEnfin, par fonctorialité", "\\]\n\nEnfin, par fonctorialité"), "Paragraph break as printed.")
add(54, "(12.1.5.6), top right", "H^{p+q}(X', ψ*(𝒦))", r"H^{p+q}(X',\psi^*(\mathcal H))", "symbol",
    fx("\\ar[r]\\ar[d]\n&H^{p+q}(X',\\psi^*(\\mathcal H", "\\ar[r]\\ar[d]\n&H^{p+q}(X',\\psi^*(\\mathcal K"), K_NOTE)
add(54, "(12.1.5.6), top right", "H^{p+q}(X', ψ*(𝒦)). : stray period after the top-right entry",
    "no period", "misprint_in_print",
    fx("))\\ar[d]\\\\\nH^p(X',f^*(\\mathcal F))", ")).\\ar[d]\\\\\nH^p(X',f^*(\\mathcal F))"),
    "TeX silently drops it; fix restores the printed period (checked at 3x). The sentence goes on after (12.1.5.6) "
    "('et par combinaison...'); the period probably belonged at the end of (12.1.5.5).",
    corrected=r"&H^{p+q}(X',\psi^*(\mathcal K))\ar[d]\\")
add(54, "(12.1.5.6), bottom right", "H^{p+q}(X', f*(𝒦))", r"H^{p+q}(X',f^*(\mathcal H))", "symbol",
    fx(r"&H^{p+q}(X',f^*(\mathcal H))", r"&H^{p+q}(X',f^*(\mathcal K))"), K_NOTE)

# ---------------- p. 55 ----------------
DOTS = "Baseline dots '. . .' in the print (below the arrow axis), not centred \\cdots (cf. GLOBAL_ISSUES item 22)."
add(55, "(12.1.6.2), top row, left end", ". . . → H^p(X, F)", r"\cdots", "symbol",
    fx(r"\cdots\ar[r]&H^p(X,\mathcal F)", r"\ldots\ar[r]&H^p(X,\mathcal F)"), DOTS)
add(55, "(12.1.6.2), top row, right end", "H^{p+1}(X, F) → . . .", r"\cdots", "symbol",
    fx(r"\ar[d]_{u_{p+1}}&\cdots", r"\ar[d]_{u_{p+1}}&\ldots"), DOTS)
add(55, "(12.1.6.2), bottom row, left end", ". . . → H^p(X', F')", r"\cdots", "symbol",
    fx(r"\cdots\ar[r]&H^p(X',\mathcal F')", r"\ldots\ar[r]&H^p(X',\mathcal F')"), DOTS)
add(55, "(12.1.6.2), bottom row, right end", "H^{p+1}(X', F') → . . .", r"\cdots", "symbol",
    fx("\\ar[r]&\\cdots\n}", "\\ar[r]&\\ldots\n}"), DOTS)
add(55, "after (12.1.6.2): paragraph 'En effet, (12.1.6.1) se factorise en'",
    "new indented paragraph after the display", "no blank line after \\]", "other",
    fx("\\]\nEn effet, (", "\\]\n\nEn effet, ("), "Paragraph break as printed.")
add(55, "(12.1.6): reference (0_I, 3.7.2)", "bold 0 with subscript I", r"0\textsubscript{I}, 3.7.2", "convention",
    fx(r"{0\textsubscript{I}, 3.7.2}", r"{\textbf{0}\textsubscript{I}, 3.7.2}"), "", conv=2)
add(55, "(12.1.6), end: 'est un homomorphisme de ∂-foncteurs'", "∂-foncteurs", r"$\delta$-foncteurs", "symbol",
    fx(r"$\delta$-foncteurs et que", r"$\partial$-foncteurs et que"), PARTIAL)
add(55, "(12.1.6), end: 'forment un ∂-foncteur en F''", "∂-foncteur", r"$\delta$-foncteur", "symbol",
    fx(r"$\delta$-foncteur en $\mathcal F'$", r"$\partial$-foncteur en $\mathcal F'$"), PARTIAL)
add(55, "(12.1.7), after (12.1.7.1): 'du foncteur composé F' ⇝ Γ(X', ψ_*(F')) (T, 2.4)'", "Γ(X', ψ_*(F')): X primed",
    r"\Gamma(X,\psi_*(\mathcal F'))", "misprint_in_print",
    fx(r"\leadsto\Gamma(X,\psi_*(\mathcal F'))", r"\leadsto\Gamma(X',\psi_*(\mathcal F'))"),
    "TeX silently corrects; fix restores the printed X' (checked at 3x). ψ_*(F') is a sheaf on X; p. 56 writes the "
    "same composed functor as Γ(X, ψ_*(F')).", corrected=r"\mathcal F'\leadsto\Gamma(X,\psi_*(\mathcal F'))")
add(55, "page break 54/55: printed p. 55 begins with the heading 'Remarque (12.1.6). —'; the marker stands after "
         "\\begin{remark}[12.1.6] and \\label, so the heading falls on p. 54",
    "p. 55 starts at 'Remarque (12.1.6). — Avec les notations'", "\\oldpage{55} after \\begin{remark}...\\label",
    "marker", fx("\\oldpage[0\\textsubscript{III}]{55}\nAvec les notations", "Avec les notations"),
    "Part 1 of 2 of the marker move: remove the marker here, then insert it before \\begin{remark}[12.1.6] (next "
    "finding, page 54). Apply in this order, after all other page 54/55 fixes.")
add(54, "page break 54/55 (end of page_054.tex): insert the p. 55 marker before \\begin{remark}[12.1.6]",
    "p. 55 starts with 'Remarque (12.1.6). —'", "\\begin{remark}[12.1.6] before the marker", "marker",
    fx("\\end{env}\n\n\\begin{remark}[12.1.6]", "\\end{env}\n\n\\oldpage[0\\textsubscript{III}]{55}\n"
       "\\begin{remark}[12.1.6]"),
    "Part 2 of 2 of the marker move; apply right after the page-55 marker removal (previous finding).")

# ---------------- checks ----------------
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in (50, 52, 53, 54, 55)}
bad = 0
for i, x in enumerate(F):
    if x["fix"]:
        c = pages[x["page"]].count(x["fix"]["old"])
        if c != 1:
            bad += 1
            print("NOT UNIQUE in page file", i, x["page"], c, repr(x["fix"]["old"][:60]))
part = r"0\textsubscript{III}"
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
t = REL.read_text(encoding="utf-8")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for k, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[k + 1][1] if k + 1 < len(cuts) else len(text)
    return None, None


for i, x in enumerate(F):
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("SIMULATION FAIL", i, x["page"], c, repr(x["fix"]["old"][:60]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
print("findings:", len(F), "| problems:", bad)
print("markers after simulation:", [m.group(1) for m in marker.finditer(t) if 48 <= int(m.group(1)) <= 57])
if not bad:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
    sim = RUN / "crops_050_055" / "simulated_050_056.txt"
    a, b = t.index(r"\oldpage[0\textsubscript{III}]{50}"), t.index(r"\oldpage[0\textsubscript{III}]{56}")
    sim.write_text(t[a:b], encoding="utf-8")
