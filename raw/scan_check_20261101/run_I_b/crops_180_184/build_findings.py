"""Build findings_180_184.json; check every fix against the page text (sequential application per page)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_180_184.json"
NL = "\u23ce"  # placeholder for a line break inside raw strings


def s(x):
    return None if x is None else x.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old=None, new=None, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=s(tex), kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=s(old), new=s(new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C2 = "Bold 0 in the print; plain 0 in the TeX."
C6REF = "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop."
CONT180 = (" In the page-180 continuation (ega1-10-fr.tex, before \\oldpage[I]{181}); apply_fixes.py searches only"
           " ega1-9-fr.tex for p. 180, so this edit lands in the manual list.")

L = []
# ---------------- page 180 ----------------
L.append(F(180, "Corollaire (9.6.4), statement: 'Sous les hypothèses de (9.6.3), pour qu'un 𝓑-Module 𝓕 soit cohérent'",
           "(9.6.3) upright inside the italic statement", r"(\hyperref[I.9.6.3-fr]{9.6.3})",
           "convention", 6, "high", r"(\hyperref[I.9.6.3-fr]{9.6.3})",
           r"\textup{(\hyperref[I.9.6.3-fr]{9.6.3})}", C6REF))
L.append(F(180, "proof of (9.6.4): 'faisceau cohérent d'anneaux (0, 5.3.4)'", "(𝟎, 5.3.4) with bold 0",
           r"(\hyperref[0.5.3.4-fr]{0, 5.3.4})", "convention", 2, "high", "{0, 5.3.4}", r"{\textbf{0}, 5.3.4}", C2))
L.append(F(180, "proof of (9.6.4): 'On en conclut (1.3.13) que 𝓕 est le conoyau d'un 𝓑-homomorphisme 𝓑^m→𝓑^n'",
           "𝓑^m→𝓑^n (exponent m on the source, n on the target)",
           r"$\mathscr{B}^n\to\mathscr{B}^m$ (silently corrected)", "misprint_in_print", None, "high",
           r"$\mathscr{B}^n\to\mathscr{B}^m$", r"$\mathscr{B}^m\to\mathscr{B}^n$",
           "The TeX silently corrects the print. Checked on a crop at 3x. m is the rank of the surjection 𝓑^m→𝓕→0"
           " two lines earlier; n appears only here, as the number of generators of the kernel P of B^m→M (of finite"
           " type because B is noetherian), so 𝓕 is the cokernel of 𝓑^n→𝓑^m: the print swaps the exponents."
           " Not in the EGA II and EGA III errata lists. The corrected edition (r20 current) has 𝓑^n→𝓑^m.",
           r"\mathscr{B}^n\to\mathscr{B}^m"))
L.append(F(180, "Proposition (9.6.5), statement: 'tel que 𝓔 engendre (0, 4.1.4) la 𝒪_X-Algèbre 𝓑'",
           "(𝟎, 4.1.4)", r"(\hyperref[0.4.1.4-fr]{0, 4.1.4}) (printed reading kept)", "misprint_in_print", None,
           "high", None, None,
           "The TeX keeps the printed reading. Authors' errata (EGA III, Errata et addenda, liste 2): '(I, 9.6.5)"
           " Ligne 17 du bas de la p. 180, remplacer (0, 4.1.4) par (0, 4.1.3).' Line 17 from the bottom of p. 180"
           " (headings counted) is this line. (0, 4.1.3) introduces 𝒜-Algèbres; (0, 4.1.4) is about reduced, regular"
           " and normal sheaves of rings. The corrected edition (r20 current) still has 0, 4.1.4.",
           r"(\hyperref[0.4.1.3-fr]{\textbf{0}, 4.1.3})"))
L.append(F(180, "Proposition (9.6.5), statement: 'tel que 𝓔 engendre (0, 4.1.4) la 𝒪_X-Algèbre 𝓑'",
           "(𝟎, 4.1.4) upright inside the italic statement", r"(\hyperref[0.4.1.4-fr]{0, 4.1.4})",
           "convention", 6, "high", r"(\hyperref[0.4.1.4-fr]{0, 4.1.4})",
           r"\textup{(\hyperref[0.4.1.4-fr]{0, 4.1.4})}",
           C6REF + " Listed before the bold-0 finding for the same reference, so both edits apply in this order."))
L.append(F(180, "Proposition (9.6.5), statement: 'engendre (0, 4.1.4)'", "(𝟎, 4.1.4) with bold 0",
           r"(\hyperref[0.4.1.4-fr]{0, 4.1.4})", "convention", 2, "high", "{0, 4.1.4}", r"{\textbf{0}, 4.1.4}",
           C2 + " Apply after the \\textup finding above (its 'new' keeps '{0, 4.1.4}')."))
L.append(F(180, "proof of (9.6.5): 'tel que 𝓔_i|U_i=Ẽ_i'", "Ẽ_i: the tilde covers E only; the subscript i stands outside",
           r"$\mathscr{E}_i|U_i=\widetilde{E_i}$", "convention", 8, "high", r"=\widetilde{E_i}$", r"=\widetilde{E}_i$",
           "Checked on a crop at 3x."))
L.append(F(180, "proof of (9.6.6): 'de ses sous-𝒪_X-Modules quasi-cohérents de type fini'",
           "'Modules' in italics (roman proof text)", r"sous-$\mathscr{O}_X$-Modules quasi-cohérents", "italics", None,
           "high", r"sous-$\mathscr{O}_X$-Modules quasi-cohérents", r"sous-$\mathscr{O}_X$-\emph{Modules} quasi-cohérents",
           "Checked on a crop at 2x: 'Modules' italic, 'quasi-cohérents' roman."))
L.append(F(180, "proof of (9.6.6): 'ces derniers engendrent des sous-𝒪_X-Algèbres quasi-cohérentes de type fini de 𝓑'",
           "'Algèbres' in italics (roman proof text)", r"engendrent des sous-$\mathscr{O}_X$-Algèbres", "italics", None,
           "high", r"engendrent des sous-$\mathscr{O}_X$-Algèbres", r"engendrent des sous-$\mathscr{O}_X$-\emph{Algèbres}",
           "Checked on a crop at 2x."))
L.append(F(180, "(10.1.1): 'Soit A un anneau topologique admissible (0, 7.1.2)'", "(𝟎, 7.1.2) with bold 0",
           r"(\hyperref[0.7.1.2-fr]{0, 7.1.2})", "convention", 2, "high", "{0, 7.1.2}", r"{\textbf{0}, 7.1.2}",
           C2 + CONT180))
# ---------------- page 181 ----------------
L.append(F(181, "(10.1.1), between '(lequel est nul hors de 𝔛).' and 'Pour 𝔍_μ⊂𝔍_λ'",
           "'... (lequel est nul hors de 𝔛). Pour 𝔍_μ⊂𝔍_λ, l'homomorphisme canonique ...' in one paragraph ('Pour' starts flush left, not indented; the previous line is full)",
           "blank line before 'Pour' (new paragraph)", "other", None, "medium",
           r"$\mathfrak{X}$)." + NL + NL + r"Pour $\mathfrak{J}_\mu", r"$\mathfrak{X}$)." + NL + r"Pour $\mathfrak{J}_\mu",
           "Spurious paragraph break: printed paragraphs are indented, 'Pour' is not (checked on a crop)."))
for ref, where in [("3.8.1", "(10.1.1): 'faisceau d'anneaux topologiques pseudo-discrets (0, 3.8.1)'"),
                   ("3.8.2", "(10.1.1): 'système projectif de faisceaux d'anneaux topologiques (0, 3.8.2)'"),
                   ("3.2.6", "(10.1.1), end: 'du système d'anneaux discrets Γ(U, 𝒪_λ) (0, 3.2.6)'"),
                   ("7.2.1", "proof of (10.1.3): 'topologiquement isomorphe à lim← A/𝔍_λ (0, 7.2.1)'")]:
    L.append(F(181, where, f"(𝟎, {ref}) with bold 0", rf"(\hyperref[0.{ref}-fr]{{0, {ref}}})", "convention", 2, "high",
               f"{{0, {ref}}}", rf"{{\textbf{{0}}, {ref}}}", C2))
L.append(F(181, "Proposition (10.1.4), statement: 'au spectre formel affine Spf(A_{f}) (0, 7.6.15)'",
           "(𝟎, 7.6.15) upright inside the italic statement", r"(\hyperref[0.7.6.15-fr]{0, 7.6.15})", "convention", 6,
           "high", r"(\hyperref[0.7.6.15-fr]{0, 7.6.15})", r"\textup{(\hyperref[0.7.6.15-fr]{0, 7.6.15})}",
           C6REF + " Listed before the bold-0 finding for the same reference, so both edits apply in this order."))
L.append(F(181, "Proposition (10.1.4), statement: '(0, 7.6.15)'", "(𝟎, 7.6.15) with bold 0",
           r"(\hyperref[0.7.6.15-fr]{0, 7.6.15})", "convention", 2, "high", "{0, 7.6.15}", r"{\textbf{0}, 7.6.15}",
           C2 + " Apply after the \\textup finding above."))
L.append(F(181, "proof of (10.1.4): 's'identifie canoniquement à A_{f}/𝔍_{f} (0, 7.6.9)'", "(𝟎, 7.6.9) with bold 0",
           r"(\hyperref[0.7.6.9-fr]{0, 7.6.9})", "convention", 2, "high", "{0, 7.6.9}", r"{\textbf{0}, 7.6.9}", C2))
# ---------------- page 182 ----------------
L.append(F(182, "(10.1.5): 's'identifie à la limite inductive lim→ A_{f} pour les f∉𝔧_x.'",
           "'la limite inductive lim→ A_{f} pour les f∉𝔧_x' (no index under lim; the condition is stated in words)",
           r"la limite inductive $\varinjlim_{f\notin\mathfrak{j}_x}A_{\{f\}}$", "missing", None, "high",
           r"$\varinjlim_{f\notin\mathfrak{j}_x}A_{\{f\}}$", r"$\varinjlim A_{\{f\}}$ pour les $f\notin\mathfrak{j}_x$",
           "Checked on a crop at 2x: only the arrow under 'lim'. The TeX moves the condition into an index of lim and drops 'pour les'."))
L.append(F(182, "(10.1.5): 'Par suite (0, 7.6.17 et 7.6.18) :'", "(𝟎, 7.6.17 et 7.6.18) with bold 0",
           r"(\hyperref[0.7.6.17-fr]{0, 7.6.17} et", "convention", 2, "high", "{0, 7.6.17} et",
           r"{\textbf{0}, 7.6.17} et", C2))
L.append(F(182, "Proposition (10.1.6): 'le corps résiduel est isomorphe à k(x)=A_x/𝔧_xA_x'", "bold italic k(x)",
           r"$k(x)=A_x/\mathfrak{j}_xA_x$", "convention", 1, "high", "$k(x)=A_x", r"$\boldsymbol{k}(x)=A_x",
           "Bold italic k in the print; plain k in the TeX."))
L.append(F(182, "after (10.1.6): 'Comme k(x) n'est pas réduit à 0'", "bold italic k(x)", "Comme $k(x)$", "convention", 1,
           "high", "Comme $k(x)$", r"Comme $\boldsymbol{k}(x)$", "Bold italic k in the print; plain k in the TeX."))
L.append(F(182, "(10.2.1): 'φ définit un homomorphisme continu Γ(𝔇(g), 𝒪_𝔜)→Γ(𝔇(φ(g)), 𝒪_𝔛) en vertu de (10.1.4)'",
           "formula set inline in the running text",
           r"displayed formula \[ \Gamma(\mathfrak{D}(g),\mathscr{O}_{\mathfrak{Y}}) \longrightarrow \Gamma(\mathfrak{D}(\varphi(g)),\mathscr{O}_{\mathfrak{X}}) \]",
           "other", None, "low",
           "continu" + NL + r"\[" + NL + r"  \Gamma(\mathfrak{D}(g),\mathscr{O}_{\mathfrak{Y}})" + NL + r"  \longrightarrow" + NL
           + r"  \Gamma(\mathfrak{D}(\varphi(g)),\mathscr{O}_{\mathfrak{X}})" + NL + r"\]" + NL + "en vertu",
           "continu" + NL + r"$\Gamma(\mathfrak{D}(g),\mathscr{O}_{\mathfrak{Y}})\to" + NL
           + r"\Gamma(\mathfrak{D}(\varphi(g)),\mathscr{O}_{\mathfrak{X}})$" + NL + "en vertu",
           "Layout only (display vs inline); the formula itself matches."))
L.append(F(182, "(10.2.1): 'en vertu de (10.1.4), (10.1.3) et (0, 7.6.7) ; comme ces homomorphismes'",
           "(𝟎, 7.6.7) with bold 0", r"(\hyperref[0.7.6.7-fr]{0, 7.6.7})~; comme", "convention", 2, "high",
           "{0, 7.6.7})~; comme", r"{\textbf{0}, 7.6.7})~; comme", C2))
L.append(F(182, "(10.2.1): '𝒪_𝔜→^aφ_*(𝒪_𝔛) (0, 3.2.5), que nous noterons encore φ̃'", "(𝟎, 3.2.5) with bold 0",
           r"(\hyperref[0.3.2.5-fr]{0, 3.2.5})", "convention", 2, "high", "{0, 3.2.5}", r"{\textbf{0}, 3.2.5}", C2))
L.append(F(182, "Proposition (10.2.2), statement: 'il faut et il suffit que pour tout x∈X, θ^♯_x soit un homomorphisme local'",
           "x∈X with a roman capital X (not the Fraktur 𝔛 of the rest of the statement)",
           r"$x\in\mathfrak{X}$ (silently corrected)", "misprint_in_print", None, "high",
           r"suffit que pour tout $x\in\mathfrak{X}$", r"suffit que pour tout $x\in X$",
           "The TeX silently corrects the print. Checked on a crop at 2x: a roman serif X, unlike the Fraktur 𝔛 = Spf(A) two lines"
           " earlier. The points x range over 𝔛 (θ_x^♯ : 𝒪_ψ(x)→𝒪_x). Same slip as the one the authors' errata correct in (I, 10.6.3)"
           " ('Ligne 3 du bas de la p. 189, remplacer X par 𝔛', EGA II errata); the EGA II and EGA III errata lists do not list this line. The corrected edition"
           " (r20 current) has x∈𝔛.",
           r"x\in\mathfrak{X}"))
L.append(F(182, "proof of (10.2.2): 'l'homomorphisme B_{g}→A_{φ(g)} déduit de φ (0, 7.6.7) transforme'",
           "(𝟎, 7.6.7) with bold 0", r"(\hyperref[0.7.6.7-fr]{0, 7.6.7}) transforme", "convention", 2, "high",
           "{0, 7.6.7}) transforme", r"{\textbf{0}, 7.6.7}) transforme", C2))
L.append(F(182, "proof of (10.2.2): '(compte tenu de (10.1.5) et de (0, 7.6.17)) que φ̃^♯_x'", "(𝟎, 7.6.17) with bold 0",
           r"(\hyperref[0.7.6.17-fr]{0, 7.6.17}))", "convention", 2, "high", "{0, 7.6.17}))", r"{\textbf{0}, 7.6.17}))", C2))
L.append(F(182, "proof of (10.2.2): 'Mais en vertu de (0, 7.6.17), les sections de 𝒪_𝔛'", "(𝟎, 7.6.17) with bold 0",
           r"(\hyperref[0.7.6.17-fr]{0, 7.6.17}), les", "convention", 2, "high", "{0, 7.6.17}), les",
           r"{\textbf{0}, 7.6.17}), les", C2))
# ---------------- page 183 ----------------
L.append(F(183, "proof of (10.2.2): 'des anneaux complets de fractions (0, 7.6.6)'", "(𝟎, 7.6.6) with bold 0",
           r"(\hyperref[0.7.6.6-fr]{0, 7.6.6})", "convention", 2, "high", "{0, 7.6.6}", r"{\textbf{0}, 7.6.6}", C2))
L.append(F(183, "proof of (10.2.2): 'donc (0, 3.2.5) on a θ=φ̃'", "(𝟎, 3.2.5) with bold 0",
           r"(\hyperref[0.3.2.5-fr]{0, 3.2.5})", "convention", 2, "high", "{0, 3.2.5}", r"{\textbf{0}, 3.2.5}", C2))
L.append(F(183, "(10.2.3), after the diagram 𝔇(g)→𝔇(h), 𝔛→𝔜: 'Ce morphisme correspond à l'unique homomorphisme continu'",
           "'Ce morphisme' begins an indented paragraph", "no blank line after \\] (the text continues the paragraph, unindented)",
           "other", None, "medium", r"\]" + NL + "Ce morphisme", r"\]" + NL + NL + "Ce morphisme",
           "Missing paragraph break: 'Ce morphisme' is indented in the print like other paragraph openings (checked on a crop),"
           " while the TeX continues the paragraph after the display."))
L.append(F(183, "(10.2.3): 'φ' : B_{h}→A_{g} (0, 7.6.7) rendant commutatif le diagramme'", "(𝟎, 7.6.7) with bold 0",
           r"(\hyperref[0.7.6.7-fr]{0, 7.6.7})", "convention", 2, "high", "{0, 7.6.7}", r"{\textbf{0}, 7.6.7}", C2))
L.append(F(183, "(10.2.3), last diagram: bottom arrow A_{g}←B_{h} labelled φ'",
           "φ' set below the bottom arrow (φ above the top arrow)", r"B_{\{h\}}\ar[l]_{\varphi'}", "other", None, "high",
           r"\ar[l]_{\varphi'}", r"\ar[l]^{\varphi'}",
           "Label placement only. For a leftward arrow xy-pic puts a '_' label above the arrow (checked by compiling the diagram:"
           " both φ and φ' come out above), so the top arrow B\\ar[l]_\\varphi is right and the bottom one needs '^'."))
L.append(F(183, "(10.3.1): 'qui s'identifie à un faisceau d'idéaux de 𝒪_𝔛 (0, 3.2.6)'", "(𝟎, 3.2.6) with bold 0",
           r"(\hyperref[0.3.2.6-fr]{0, 3.2.6})", "convention", 2, "high", "{0, 3.2.6}", r"{\textbf{0}, 3.2.6}", C2))
L.append(F(183, "(10.3.1): 'l'idéal ouvert 𝔍_{f} de l'anneau A_{f} (0, 7.6.9)'", "(𝟎, 7.6.9) with bold 0",
           r"(\hyperref[0.7.6.9-fr]{0, 7.6.9})", "convention", 2, "high", "{0, 7.6.9}", r"{\textbf{0}, 7.6.9}", C2))
L.append(F(183, "formula (10.3.1.1): '𝔍^Δ|𝔇(f)=(𝔍_{f})^Δ'", "no full stop after the displayed formula",
           r"=(\mathfrak{J}_{\{f\}})^\Delta.", "punctuation", None, "high",
           r"=(\mathfrak{J}_{\{f\}})^\Delta.", r"=(\mathfrak{J}_{\{f\}})^\Delta",
           "Checked on a crop at 3x: nothing follows ^Δ."))
# ---------------- page 184 ----------------
L.append(F(184, "(10.3.2): 'a pour noyau Γ(𝔇(f), 𝔍^Δ)=𝔍_{f} (0, 7.6.9) ; ces applications'", "(𝟎, 7.6.9) with bold 0",
           r"(\hyperref[0.7.6.9-fr]{0, 7.6.9})~; ces", "convention", 2, "high", "{0, 7.6.9})~; ces",
           r"{\textbf{0}, 7.6.9})~; ces", C2))
L.append(F(184, "formula (10.3.2.1): '𝒪_𝔛/𝔍^Δ ⥲ (Ã/𝔍̃)|𝔛'", "no full stop after the displayed formula",
           r"(\widetilde{A}/\widetilde{\mathfrak{J}})|\mathfrak{X}.", "punctuation", None, "high",
           r"(\widetilde{A}/\widetilde{\mathfrak{J}})|\mathfrak{X}.", r"(\widetilde{A}/\widetilde{\mathfrak{J}})|\mathfrak{X}",
           "Checked on a crop at 3x: nothing follows |𝔛."))
L.append(F(184, "(10.3.2), end: 'canoniquement isomorphe à 𝔍̃'/𝔍̃=(𝔍'/𝔍)~'", "𝔍̃': the tilde covers 𝔍 only; the prime stands outside",
           r"\widetilde{\mathfrak{J}'}/\widetilde{\mathfrak{J}}", "convention", 8, "high",
           r"\widetilde{\mathfrak{J}'}/", r"\widetilde{\mathfrak{J}}'/", "Checked on a crop at 3x."))
L.append(F(184, "(10.3.2), end: '𝔍̃'/𝔍̃=(𝔍'/𝔍)~.'", "(𝔍'/𝔍)~: parentheses with the tilde written after the closing parenthesis",
           r"=\widetilde{\mathfrak{J}'/\mathfrak{J}}$", "convention", 5, "high",
           r"=\widetilde{\mathfrak{J}'/\mathfrak{J}}$", r"=(\mathfrak{J}'/\mathfrak{J})\supertilde$",
           "Checked on a crop at 3x. The TeX also drops the printed parentheses; \\supertilde as in ega1-1-fr.tex ((\\Gamma(v))\\supertilde)."))
L.append(F(184, "(10.3.3): 'est un faisceau d'idéaux de définition de 𝔛'", "'faisceau d'idéaux de définition' italic, 'de 𝔛' roman",
           r"\emph{faisceau d'idéaux de définition de $\mathfrak{X}$}", "italics", None, "high",
           r"\emph{faisceau d'idéaux de définition de $\mathfrak{X}$}", r"\emph{faisceau d'idéaux de définition} de $\mathfrak{X}$",
           "Checked on a crop: the final 'de' is upright."))
L.append(F(184, "(10.3.3): '(ou un Idéal de définition de 𝔛)'", "'Idéal de définition' italic, 'de 𝔛' roman",
           r"\emph{Idéal de définition de $\mathfrak{X}$}", "italics", None, "high",
           r"\emph{Idéal de définition de $\mathfrak{X}$}", r"\emph{Idéal de définition} de $\mathfrak{X}$",
           "Checked on a crop: the final 'de' is upright."))
L.append(F(184, "proof of (10.3.5): 'dans le faisceau structural (A/𝔎)~ de Spec(A/𝔎)'", "(A/𝔎)~",
           r"$\widetilde{A/\mathfrak{K}}$", "convention", 5, "high", r"$\widetilde{A/\mathfrak{K}}$",
           r"$(A/\mathfrak{K})\supertilde$", "Checked on a crop. The TeX also drops the printed parentheses."))
L.append(F(184, "proof of (10.3.5): 'soit égale à celle de (𝔎_i/𝔎)~ ;'", "(𝔎_i/𝔎)~",
           r"$\widetilde{\mathfrak{K}_i/\mathfrak{K}}$", "convention", 5, "high",
           r"$\widetilde{\mathfrak{K}_i/\mathfrak{K}}$", r"$(\mathfrak{K}_i/\mathfrak{K})\supertilde$",
           "Checked on a crop. The TeX also drops the printed parentheses."))
L.append(F(184, "proof of (10.3.5): 'cette image canonique est un faisceau quasi-cohérent sur Spec(A/𝔎)'",
           "'quasi-cohérent' in italics (roman proof text)", "faisceau quasi-cohérent sur", "italics", None, "high",
           "faisceau quasi-cohérent sur", r"faisceau \emph{quasi-cohérent} sur", "Checked on a crop."))
L.append(F(184, "proof of (10.3.5): 'donc de la forme (𝔍/𝔎)~, où 𝔍 est un idéal de A'", "(𝔍/𝔎)~",
           r"$\widetilde{\mathfrak{J}/\mathfrak{K}}$", "convention", 5, "high",
           r"$\widetilde{\mathfrak{J}/\mathfrak{K}}$, où", r"$(\mathfrak{J}/\mathfrak{K})\supertilde$, où",
           "Checked on a crop. The TeX also drops the printed parentheses."))
L.append(F(184, "proof of (10.3.5): 'et par suite (10.3.2) ((𝔍/𝔎)~)^n=0'", "((𝔍/𝔎)~)^n=0",
           r"$(\widetilde{\mathfrak{J}/\mathfrak{K}})^n=0$", "convention", 5, "high",
           r"$(\widetilde{\mathfrak{J}/\mathfrak{K}})^n=0$", r"$((\mathfrak{J}/\mathfrak{K})\supertilde)^n=0$",
           "Checked on a crop at 1.6x. The TeX also drops the inner printed parentheses."))
L.append(F(184, "proof of (10.3.5): 'tel que (𝔎_i)_{f_i}=𝔥_i (0, 7.6.9) ; soit 𝔎'", "(𝟎, 7.6.9) with bold 0",
           r"(\hyperref[0.7.6.9-fr]{0, 7.6.9})~; soit", "convention", 2, "high", "{0, 7.6.9})~; soit",
           r"{\textbf{0}, 7.6.9})~; soit", C2))
L.append(F(184, "proof of (10.3.5), end: 'est un idéal de définition de A (0, 7.1.4).'", "(𝟎, 7.1.4) with bold 0",
           r"(\hyperref[0.7.1.4-fr]{0, 7.1.4})", "convention", 2, "high", "{0, 7.1.4}", r"{\textbf{0}, 7.1.4}", C2))

# ---- checks: every old must occur exactly once in its page at application time (sequential, per page) ----
pages = {n: (RUN / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(180, 185)}
ok = True
for i, x in enumerate(L):
    f = x["fix"]
    if not f:
        continue
    t = pages[x["page"]]
    c = t.count(f["old"])
    orig = (RUN / f"page_{x['page']}.tex").read_text(encoding="utf-8").count(f["old"])
    if c != 1 or orig < 1:
        ok = False
        print("PROBLEM", i, x["page"], x["where"][:60], "count now", c, "in original", orig)
    pages[x["page"]] = t.replace(f["old"], f["new"], 1)
json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(180, 185):
    print(n, {k: cnt[(n, k)] for k in ("normal", "convention", "misprint")})
print("total", len(L), "all fixes apply in order:", ok)
