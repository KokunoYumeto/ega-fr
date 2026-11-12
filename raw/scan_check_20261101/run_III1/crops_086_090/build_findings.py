"""Build findings_086_090.json for EGA III part 1, pp. 86-90, and validate the fixes.

Strings are raw; the character U+00B6 (pilcrow) stands for a line break (LF) in
"old"/"new", so that TeX like \\neq is never mangled.
"""
import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_086_090.json")
NL = "¶"

findings = []


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None
    if old is not None:
        fix = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": fix,
    }
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    findings.append(d)


DOTS = "Baseline dots in the print (as GLOBAL_ISSUES item 22 for EGA II); checked on an enlarged crop."
BOLD0 = "Bold 0 in the reference to chapter 0."
BOLDI = "Bold I in the reference to chapter I."
BOLDII = "Bold II in the reference to chapter II."
UPREF = "The reference is upright (roman old-style figures) inside the italic statement; checked on an enlarged crop."
PAIR = "One edit for this finding and the next (convention 6): bold numeral and the upright reference together."
PAIRED = "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."
INLINE = "Layout: the print sets this formula inline in the running text; the TeX displays it."
STAR = "Asterisk subscript in the print (A_*, Γ_* as in (0_I, 5.4.6)); checked on an enlarged crop. ega3-1-fr.tex writes \\Gamma_* elsewhere (e.g. \\Gamma_*(\\mathcal O_X))."

# ---------------------------------------------------------------- page 86
F(86, "Notations (1.2.1), item U_i: 'l'ensemble ouvert (0_I, 5.5.2) des x∈X'",
  "(\U0001D7CE_I, 5.5.2): bold 0", r"0\textsubscript{I}, 5.5.2", "convention", 2, "high",
  r"{0\textsubscript{I}, 5.5.2}", r"{\textbf{0}\textsubscript{I}, 5.5.2}", BOLD0)
F(86, "(1.2.2): 'On sait alors (I, 9.3.3) que l'on a'",
  "(\U0001D408, 9.3.3): bold I", r"I, 9.3.3", "convention", 2, "high",
  r"{I, 9.3.3}", r"{\textbf{I}, 9.3.3}", BOLDI)
F(86, "(1.2.2), display after 'Nous poserons': '= X_{f_{i_0}f_{i_1}...f_{i_p}}'",
  "f_{i_1}...f_{i_p}: dots on the baseline", r"X_{f_{i_0}f_{i_1}\cdots f_{i_p}}", "symbol", None, "high",
  r"=X_{f_{i_0}f_{i_1}\cdots f_{i_p}}", r"=X_{f_{i_0}f_{i_1}\ldots f_{i_p}}", DOTS)
F(86, "(1.2.2): '(0_I, 5.5.3); on a donc aussi'",
  "(\U0001D7CE_I, 5.5.3): bold 0", r"0\textsubscript{I}, 5.5.3", "convention", 2, "high",
  r"{0\textsubscript{I}, 5.5.3}", r"{\textbf{0}\textsubscript{I}, 5.5.3}", BOLD0)
F(86, "(1.2.2.1): 'Γ(U_{i_0i_1...i_p}, ℱ) = M_{f_{i_0}f_{i_1}...f_{i_p}}'",
  "f_{i_1}...f_{i_p}: dots on the baseline", r"M_{f_{i_0}f_{i_1}\cdots f_{i_p}}", "symbol", None, "high",
  r"=M_{f_{i_0}f_{i_1}\cdots", r"=M_{f_{i_0}f_{i_1}\ldots", DOTS)
F(86, "(1.2.2.1): end of the display",
  "no full stop after the display", r"f_{i_p}}." + "\n" + r"\end{equation}", "punctuation", None, "high",
  r"f_{i_p}}." + NL + r"\end{equation}", r"f_{i_p}}" + NL + r"\end{equation}",
  "Enlarged crop: the display ends with the subscript; the text continues 'Or (0_I, 1.6.1)'. Independent of the preceding fix.")
F(86, "(1.2.2): 'Or (0_I, 1.6.1) M_{...} s'identifie'",
  "(\U0001D7CE_I, 1.6.1): bold 0", r"0\textsubscript{I}, 1.6.1", "convention", 2, "high",
  r"{0\textsubscript{I}, 1.6.1}", r"{\textbf{0}\textsubscript{I}, 1.6.1}", BOLD0)
F(86, "(1.2.2): 'Or (0_I, 1.6.1) M_{f_{i_0}f_{i_1}...f_{i_p}} s'identifie à la limite inductive'",
  "f_{i_1}...f_{i_p}: dots on the baseline", r"$M_{f_{i_0}f_{i_1}\cdots f_{i_p}}$", "symbol", None, "high",
  r"$M_{f_{i_0}f_{i_1}\cdots f_{i_p}}$ s'identifie", r"$M_{f_{i_0}f_{i_1}\ldots f_{i_p}}$ s'identifie", DOTS)
F(86, "(1.2.2): 'étant la multiplication par (f_{i_0}f_{i_1}...f_{i_p})^{n−m}'",
  "f_{i_1}...f_{i_p}: dots on the baseline", r"(f_{i_0}f_{i_1}\cdots f_{i_p})^{n-m}", "symbol", None, "high",
  r"(f_{i_0}f_{i_1}\cdots f_{i_p})^{n-m}", r"(f_{i_0}f_{i_1}\ldots f_{i_p})^{n-m}", DOTS)

# ---------------------------------------------------------------- page 87
F(87, "Corollaire (1.2.4), line 7 of the page: 'qu'il existe des g_i∈Γ(U, ℱ) tels que Σ g_i(f_i|U)=1|U'",
  "g_i∈Γ(U, ℱ) (script F)", r"$g_i\in\Gamma(U,\mathcal F)$", "misprint_in_print", None, "high",
  None, None,
  "The TeX keeps the printed reading. Authors' errata (EGA III, ega3-7-fr.tex, item (III, 1.2.4)): 'Ligne 7 de la p. 87, remplacer Γ(U, ℱ) par Γ(U, \U0001D4AA_X)'. The g_i must be sections of the structure sheaf for Σ g_i(f_i|U)=1|U to make sense.",
  corrected=r"$g_i\in\Gamma(U,\mathcal O_X)$")
F(87, "Corollaire (1.2.4), line 7: 'pour tout (\U0001D4AA_X|U)-Module quasi-cohérent \U0001D4A2,'",
  "\U0001D4A2 (script G)", r"$(\mathcal O_X\vert U)$-Module quasi-cohérent $\mathcal G$", "misprint_in_print", None, "high",
  None, None,
  "The TeX keeps the printed reading. Authors' errata (EGA III, ega3-7-fr.tex, item (III, 1.2.4)): line 7 of p. 87, 'remplacer \U0001D4A2 par ℱ'.",
  corrected=r"$(\mathcal O_X\vert U)$-Module quasi-cohérent $\mathcal F$")
F(87, "Corollaire (1.2.4), line 8: 'on a H^p(\U0001D518, \U0001D4A2)=0 pour p>0'",
  "H^p(\U0001D518, \U0001D4A2)", r"$H^p(\mathfrak U,\mathcal G)=0$", "misprint_in_print", None, "high",
  None, None,
  "The TeX keeps the printed reading. Authors' errata (EGA III, ega3-7-fr.tex, item (III, 1.2.4)): 'Ligne 8 de la p. 87, remplacer H^p(\U0001D518, \U0001D4A2) par H^p(\U0001D518, ℱ)'.",
  corrected=r"$H^p(\mathfrak U,\mathcal F)=0$")
F(87, "Corollaire (1.2.4): 'l'homomorphisme canonique (1.2.3.2) M→H^0(\U0001D518, ℱ)'",
  "(1.2.3.2) upright inside the italic statement",
  r"(\hyperref[III.1.2.3.2-fr]{1.2.3.2}) inside the italic corollary environment: italic", "convention", 6, "high",
  r"canonique (\hyperref[III.1.2.3.2-fr]{1.2.3.2})", r"canonique \textup{(\hyperref[III.1.2.3.2-fr]{1.2.3.2})}", UPREF)
F(87, "After the proof of (1.2.4): 'on a ainsi démontré à nouveau (I, 1.3.7)'",
  "(\U0001D408, 1.3.7): bold I", r"(I, 1.3.7)", "convention", 2, "high",
  r"(I, 1.3.7)", r"(\textbf{I}, 1.3.7)", BOLDI)
F(87, "Remarque (1.2.5): 'sont exacts en ℱ (I, 1.3.11)'",
  "(\U0001D408, 1.3.11): bold I", r"(I, 1.3.11)", "convention", 2, "high",
  r"(I, 1.3.11)", r"(\textbf{I}, 1.3.11)", BOLDI)
F(87, "Remarque (1.2.5), first cohomology sequence, start: '... → H^p(\U0001D518, ℱ′)'",
  ". . . → (dots on the baseline)", r"\cdots\longrightarrow H^p(\mathfrak U,\mathcal F')", "symbol", None, "high",
  r"\cdots\longrightarrow H^p(\mathfrak U,\mathcal F')", r"\ldots\longrightarrow H^p(\mathfrak U,\mathcal F')", DOTS)
F(87, "Remarque (1.2.5), first cohomology sequence, end: '→ H^{p+1}(\U0001D518, ℱ′) → ...'",
  "→ . . . (baseline dots, no full stop after the display)", r"\longrightarrow\cdots.", "punctuation", None, "high",
  r"\mathcal F')" + NL + r"\longrightarrow\cdots.", r"\mathcal F')" + NL + r"\longrightarrow\ldots",
  "Enlarged crop: the display ends with baseline dots and no full stop; the fix also turns \\cdots into \\ldots.")
F(87, "Remarque (1.2.5), second cohomology sequence, start: '... → H^p((f), M′)'",
  ". . . → (dots on the baseline)", r"\cdots\longrightarrow H^p((\mathbf f),M')", "symbol", None, "high",
  r"\cdots\longrightarrow H^p((\mathbf f),M')", r"\ldots\longrightarrow H^p((\mathbf f),M')", DOTS)
F(87, "Remarque (1.2.5), second cohomology sequence, end: '→ H^{p+1}((f), M′) → ...'",
  "→ . . . (baseline dots, no full stop after the display)", r"\longrightarrow\cdots.", "punctuation", None, "high",
  r"M')" + NL + r"\longrightarrow\cdots.", r"M')" + NL + r"\longrightarrow\ldots",
  "Enlarged crop: the display ends with baseline dots and no full stop; the fix also turns \\cdots into \\ldots.")

# ---------------------------------------------------------------- page 88
F(88, "(1.2.5.1), bottom row: 'H^{p+1}((f), M″) → H^{p+2}((f), M′)'",
  "the label ∂ is below the arrow", r"\ar[r]^{\partial} (label above)", "formula", None, "high",
  r"H^{p+1}((\mathbf f),M'')\ar[r]^{\partial}", r"H^{p+1}((\mathbf f),M'')\ar[r]_{\partial}",
  "Enlarged crop: in the top row ∂ is above the arrow, in the bottom row below it.")
F(88, "Proof of (1.3.1): 'arbitrairement fins (I, 1.1.10)'",
  "(\U0001D408, 1.1.10): bold I", r"(I, 1.1.10)", "convention", 2, "high",
  r"(I, 1.1.10)", r"(\textbf{I}, 1.1.10)", BOLDI)
F(88, "Proof of (1.3.1): 'préschéma X_f pour f∈A (I, 1.3.6)'",
  "(\U0001D408, 1.3.6): bold I", r"(I, 1.3.6)", "convention", 2, "high",
  r"(I, 1.3.6)", r"(\textbf{I}, 1.3.6)", BOLDI)
F(88, "Corollaire (1.3.2): 'un morphisme affine (II, 1.6.1).'",
  "(\U0001D408\U0001D408, 1.6.1): bold II", r"(II, 1.6.1)", "convention", 2, "high",
  r"(II, 1.6.1)", r"\textup{(\textbf{II}, 1.6.1)}", PAIR)
F(88, "Corollaire (1.3.2): same reference '(II, 1.6.1)'",
  "the reference is upright inside the italic statement (crop)", r"(II, 1.6.1) inside the italic corollary environment: italic",
  "convention", 6, "high", None, None, PAIRED)
F(88, "Proof of (1.3.2): 'associé au préfaisceau U⇝H^q(f^{-1}(U), ℱ)'",
  "U ⇝ H^q(...) (wavy arrow)", r"U\mapsto H^q(f^{-1}(U),\mathcal F)", "symbol", None, "high",
  r"U\mapsto H^q", r"U\leadsto H^q", "Wavy maps-to arrow in the print (\\leadsto); enlarged crop.")
F(88, "Proof of (1.3.2): 'f^{-1}(U) est affine (II, 1.3.2)'",
  "(\U0001D408\U0001D408, 1.3.2): bold II", r"(II, 1.3.2)", "convention", 2, "high",
  r"(II, 1.3.2)", r"(\textbf{II}, 1.3.2)", BOLDII)
F(88, "Corollaire (1.3.3): '(0, 12.1.3.1) est bijectif pour tout p'",
  "(\U0001D7CE, 12.1.3.1): bold 0", r"(0, 12.1.3.1)", "convention", 2, "high",
  r"(0, 12.1.3.1)", r"\textup{(\textbf{0}, 12.1.3.1)}", PAIR)
F(88, "Corollaire (1.3.3): same reference '(0, 12.1.3.1)'",
  "the reference is upright inside the italic statement (crop)", r"(0, 12.1.3.1) inside the italic corollary environment: italic",
  "convention", 6, "high", None, None, PAIRED)
F(88, "Proof of (1.3.3): 'il suffit (en vertu de (0, 12.1.7))'",
  "(\U0001D7CE, 12.1.7): bold 0", r"(0, 12.1.7)", "convention", 2, "high",
  r"(0, 12.1.7)", r"(\textbf{0}, 12.1.7)", BOLD0)
F(88, "Proof of (1.3.3): 'd'où notre assertion (0, 11.1.6)'",
  "(\U0001D7CE, 11.1.6): bold 0", r"(0, 11.1.6)", "convention", 2, "high",
  r"(0, 11.1.6)", r"(\textbf{0}, 11.1.6)", BOLD0)

# ---------------------------------------------------------------- page 89
F(89, "Corollaire (1.3.4), end: '(0, 12.2.5.1) est bijectif pour tout p'",
  "(\U0001D7CE, 12.2.5.1): bold 0", r"(0, 12.2.5.1)", "convention", 2, "high",
  r"(0, 12.2.5.1)", r"\textup{(\textbf{0}, 12.2.5.1)}", PAIR)
F(89, "Corollaire (1.3.4): same reference '(0, 12.2.5.1)'",
  "the reference is upright inside the italic statement (crop)", r"(0, 12.2.5.1) inside the italic corollary environment: italic",
  "convention", 6, "high", None, None, PAIRED)
F(89, "Proof of (1.3.4): 'est bijectif (0, 12.2.5).'",
  "(\U0001D7CE, 12.2.5): bold 0", r"(0, 12.2.5)", "convention", 2, "high",
  r"(0, 12.2.5)", r"(\textbf{0}, 12.2.5)", BOLD0)
F(89, "Proof of (1.4.1): 'du recouvrement \U0001D518 est affine (I, 5.5.6)'",
  "(\U0001D408, 5.5.6): bold I", r"(I, 5.5.6)", "convention", 2, "high",
  r"(I, 5.5.6)", r"(\textbf{I}, 5.5.6)", BOLDI)
F(89, "Corollaire (1.4.3), first words: 'Soient. X un schéma dont l'espace sous-jacent'",
  "'Soient.' with a full stop before X", r"Soient $X$ un schéma dont", "misprint_in_print", None, "high",
  r"Soient $X$ un schéma dont", r"Soient. $X$ un schéma dont",
  "The TeX silently corrects the print; the fix restores the printed reading. 4x crop: a full stop of the same size and shape as the one after (1.4.3), not a speck.",
  corrected=r"Soient $X$ un schéma dont")
F(89, "Corollaire (1.4.3): 'les X_{f_i} (notations de (1.2.1)) soient affines'",
  "(1.2.1) upright inside the italic statement",
  r"(\hyperref[III.1.2.1-fr]{1.2.1}) inside the italic corollary environment: italic", "convention", 6, "high",
  r"(\hyperref[III.1.2.1-fr]{1.2.1})) soient", r"\textup{(\hyperref[III.1.2.1-fr]{1.2.1})}) soient",
  UPREF + " The outer closing parenthesis looks upright too; left to the parenthesis convention.")
F(89, "Corollaire (1.4.3): 'Alors (avec les notations de (1.2.1)), pour tout'",
  "(1.2.1) upright inside the italic statement",
  r"(\hyperref[III.1.2.1-fr]{1.2.1}) inside the italic corollary environment: italic", "convention", 6, "high",
  r"de (\hyperref[III.1.2.1-fr]{1.2.1})), pour", r"de \textup{(\hyperref[III.1.2.1-fr]{1.2.1})}), pour",
  UPREF + " The outer closing parenthesis looks upright too; left to the parenthesis convention.")
F(89, "(1.4.4.1), bottom row: 'H^{q+1}((f), M″) → H^{q+2}((f), M′)'",
  "the label ∂ is below the arrow", r"\ar[r]^{\partial} (label above)", "formula", None, "high",
  r"H^{q+1}((\mathbf f),M'')\ar[r]^{\partial}", r"H^{q+1}((\mathbf f),M'')\ar[r]_{\partial}",
  "In the top row ∂ is above the arrow, in the bottom row below it.")

# ---------------------------------------------------------------- page 90
F(90, "Proposition (1.4.5): 'considérons l'anneau gradué A_* = Γ_*(ℒ)'",
  "A_* and Γ_* with an asterisk subscript", r"$A_\bullet=\Gamma_\bullet(\mathcal L)$", "symbol", None, "high",
  r"$A_\bullet=\Gamma_\bullet(\mathcal L)$", r"$A_*=\Gamma_*(\mathcal L)$", STAR)
F(90, "Proposition (1.4.5): 'Γ_*(ℒ) (0_I, 5.4.6); alors'",
  "(\U0001D7CE_I, 5.4.6): bold 0", r"(0\textsubscript{I}, 5.4.6)", "convention", 2, "high",
  r"(0\textsubscript{I}, 5.4.6)", r"\textup{(\textbf{0}\textsubscript{I}, 5.4.6)}", PAIR)
F(90, "Proposition (1.4.5): same reference '(0_I, 5.4.6)'",
  "the reference is upright inside the italic statement (crop)",
  r"(0\textsubscript{I}, 5.4.6) inside the italic proposition environment: italic", "convention", 6, "high",
  None, None, PAIRED)
F(90, "Proposition (1.4.5): 'alors H^•(ℱ, ℒ) = ⊕_{n∈Z} H^•(X, ℱ⊗ℒ^{⊗n}) est un A_*-module gradué'",
  "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
  r"alors" + NL + r"\[" + NL + r"H^\bullet(\mathcal F,\mathcal L)" + NL
  + r"=\bigoplus_{n\in\mathbb Z}H^\bullet(X,\mathcal F\otimes\mathcal L^{\otimes n})" + NL + r"\]",
  r"alors" + NL + r"$H^\bullet(\mathcal F,\mathcal L)" + NL
  + r"=\bigoplus_{n\in\mathbb Z}H^\bullet(X,\mathcal F\otimes\mathcal L^{\otimes n})$",
  INLINE + " Index position under ⊕ left as is.")
F(90, "Proposition (1.4.5): 'est un A_*-module gradué'",
  "A_* (asterisk subscript)", r"$A_\bullet$", "symbol", None, "high",
  r"est un $A_\bullet$-module", r"est un $A_*$-module", STAR)
F(90, "Proposition (1.4.5), last line: 'de (A_*)_{(f)}-modules.'",
  "(A_*)_{(f)} (asterisk subscript)", r"$(A_\bullet)_{(f)}$", "symbol", None, "high",
  r"de $(A_\bullet)_{(f)}$-modules.", r"de $(A_*)_{(f)}$-modules.", STAR)
F(90, "Proof of (1.4.5): 'les U_i∩X_f sont des ouverts affines (I, 1.3.6)'",
  "(\U0001D408, 1.3.6): bold I", r"(I, 1.3.6)", "convention", 2, "high",
  r"(I, 1.3.6)", r"(\textbf{I}, 1.3.6)", BOLDI)
F(90, "Proof of (1.4.5): 'par f définit un homomorphisme C^•(\U0001D518, ℱ⊗ℒ^{⊗m})→C^•(\U0001D518, ℱ⊗ℒ^{⊗(m+n)}), d'où un'",
  "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
  r"définit un homomorphisme" + NL + r"\[" + NL
  + r"C^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes m})" + NL + r"\longrightarrow" + NL
  + r"C^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes(m+n)})," + NL + r"\]",
  r"définit un homomorphisme" + NL
  + r"$C^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes m})" + NL + r"\longrightarrow" + NL
  + r"C^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes(m+n)})$,",
  INLINE + " The comma follows the formula.")
F(90, "Proof of (1.4.5): 'd'où un homomorphisme H^•(\U0001D518, ℱ⊗ℒ^{⊗m})→H^•(\U0001D518, ℱ⊗ℒ^{⊗(m+n)}), ce qui établit'",
  "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
  r"d'où un homomorphisme" + NL + r"\[" + NL
  + r"H^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes m})" + NL + r"\longrightarrow" + NL
  + r"H^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes(m+n)})," + NL + r"\]",
  r"d'où un homomorphisme" + NL
  + r"$H^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes m})" + NL + r"\longrightarrow" + NL
  + r"H^\bullet(\mathfrak U,\mathcal F\otimes\mathcal L^{\otimes(m+n)})$,",
  INLINE + " The comma follows the formula.")
F(90, "Proof of (1.4.5): 'il résulte de (I, 9.3.2) que l'on a'",
  "(\U0001D408, 9.3.2): bold I", r"(I, 9.3.2)", "convention", 2, "high",
  r"(I, 9.3.2)", r"(\textbf{I}, 9.3.2)", BOLDI)
F(90, "Proof of (1.4.5): 'un isomorphisme de complexes de (A_*)_{(f)}-modules'",
  "(A_*)_{(f)} (asterisk subscript)", r"$(A_\bullet)_{(f)}$", "symbol", None, "high",
  r"complexes de" + NL + r"$(A_\bullet)_{(f)}$-modules", r"complexes de" + NL + r"$(A_*)_{(f)}$-modules", STAR)
F(90, "Proof of (1.4.5): 'compte tenu de (I, 1.3.9, (ii))'",
  "(\U0001D408, 1.3.9, (ii)): bold I", r"(I, 1.3.9, (ii))", "convention", 2, "high",
  r"(I, 1.3.9, (ii))", r"(\textbf{I}, 1.3.9, (ii))", BOLDI)
F(90, "Proof of (1.4.5): 'le foncteur M⇝M_{(f)} est exact'",
  "M ⇝ M_{(f)} (wavy arrow)", r"$M\mapsto M_{(f)}$", "symbol", None, "high",
  r"$M\mapsto M_{(f)}$", r"$M\leadsto M_{(f)}$", "Wavy maps-to arrow in the print (\\leadsto); enlarged crop.")
F(90, "Proof of (1.4.5), end: 'dans la catégorie des A_*-modules gradués'",
  "A_* (asterisk subscript)", r"$A_\bullet$", "symbol", None, "high",
  r"des $A_\bullet$-modules", r"des $A_*$-modules", STAR)
F(90, "Corollaire (1.4.6): 'les hypothèses de (1.4.5) et on suppose en outre'",
  "(1.4.5) upright inside the italic statement",
  r"(\hyperref[III.1.4.5-fr]{1.4.5}) inside the italic corollary environment: italic", "convention", 6, "high",
  r"(\hyperref[III.1.4.5-fr]{1.4.5}) et on suppose", r"\textup{(\hyperref[III.1.4.5-fr]{1.4.5})} et on suppose", UPREF)
F(90, "Corollaire (1.4.6): 'un isomorphisme canonique H^•(X_f, ℱ)⥲(H^•(X, ℱ))_f de A_f-modules'",
  "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
  r"\[" + NL + r"H^\bullet(X_f,\mathcal F)" + NL + r"\xrightarrow{\sim}(H^\bullet(X,\mathcal F))_f" + NL + r"\]",
  r"$H^\bullet(X_f,\mathcal F)" + NL + r"\xrightarrow{\sim}(H^\bullet(X,\mathcal F))_f$",
  INLINE)
F(90, "Corollaire (1.4.7): label '(i) Supposons l'ouvert X_f affine'",
  "label (i) upright", r"\item[(i)] inside the italic corollary environment: italic", "convention", 6, "high",
  r"\item[(i)] Supposons", r"\item[\textup{(i)}] Supposons",
  "Roman-numeral item labels are upright in the print (as GLOBAL_ISSUES item 16).")
F(90, "Corollaire (1.4.7): label '(ii) Inversement'",
  "label (ii) upright", r"\item[(ii)] inside the italic corollary environment: italic", "convention", 6, "high",
  r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement",
  "Roman-numeral item labels are upright in the print (as GLOBAL_ISSUES item 16).")
F(90, "Proof of (1.4.7) (ii): 'En vertu du critère de Serre (II, 5.2.1)'",
  "(\U0001D408\U0001D408, 5.2.1): bold II", r"(II, 5.2.1)", "convention", 2, "high",
  r"(II, 5.2.1)", r"(\textbf{II}, 5.2.1)", BOLDII)
F(90, "Proof of (1.4.7) (ii): '\U0001D4A6=\U0001D4A5|X_f (I, 9.4.2)'",
  "(\U0001D408, 9.4.2): bold I", r"(I, 9.4.2)", "convention", 2, "high",
  r"(I, 9.4.2)", r"(\textbf{I}, 9.4.2)", BOLDI)
F(90, "Remarque (1.4.8): 'de la relation (II, 4.5.13.2)'",
  "(\U0001D408\U0001D408, 4.5.13.2): bold II", r"(II, 4.5.13.2)", "convention", 2, "high",
  r"(II, 4.5.13.2)", r"(\textbf{II}, 4.5.13.2)", BOLDII)


def main():
    ok = True
    pages = sorted({f["page"] for f in findings})
    for p in pages:
        path = os.path.join(RUN, "page_%03d.tex" % p)
        with open(path, encoding="utf-8", newline="") as fh:
            text = fh.read()
        # the page extracts are CRLF; the release files (and the fixes) use LF
        text = text.replace("\r\n", "\n")
        if "\r" in text:
            print("WARNING: stray CR in", path)
        # 1) each old occurs exactly once in the original page text
        for f in findings:
            if f["page"] != p or not f["fix"]:
                continue
            n = text.count(f["fix"]["old"])
            if n != 1:
                ok = False
                print("NOT UNIQUE (%d) p%d: %r" % (n, p, f["fix"]["old"]))
        # 2) applying all fixes in sequence keeps every later old unique
        t = text
        for f in findings:
            if f["page"] != p or not f["fix"]:
                continue
            n = t.count(f["fix"]["old"])
            if n != 1:
                ok = False
                print("SEQUENTIAL CONFLICT p%d: %r (count %d)" % (p, f["fix"]["old"], n))
                continue
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
    # 3) the same check against each page's segment of the current source file
    src_path = os.path.join(os.path.dirname(RUN), "ega-fr", "source", "ega3", "ega3-1-fr.tex")
    if os.path.exists(src_path):
        with open(src_path, encoding="utf-8", newline="") as fh:
            src = fh.read()
        print("source has CR:", "\r" in src)
        src = src.replace("\r\n", "\n")
        for p in pages:
            a = src.find("\\oldpage[III]{%d}" % p)
            b = src.find("\\oldpage[III]{%d}" % (p + 1))
            seg = src[a:b] if a >= 0 and b > a else ""
            if not seg:
                print("no source segment for page", p)
                continue
            for f in findings:
                if f["page"] != p or not f["fix"]:
                    continue
                n = seg.count(f["fix"]["old"])
                if n != 1:
                    ok = False
                    print("SOURCE SEGMENT COUNT %d p%d: %r" % (n, p, f["fix"]["old"]))
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(findings, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    counts = {}
    for f in findings:
        c = counts.setdefault(f["page"], [0, 0, 0])
        if f["kind"] == "misprint_in_print":
            c[2] += 1
        elif f["kind"] == "convention":
            c[1] += 1
        else:
            c[0] += 1
    print("written", OUT, len(findings), "findings; all fixes unique:", ok)
    for p in sorted(counts):
        print(p, "normal/convention/misprint =", "/".join(map(str, counts[p])))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
