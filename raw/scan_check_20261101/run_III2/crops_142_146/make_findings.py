"""Build findings_142_146.json and check every fix's 'old' against its page file (CRLF -> LF)."""
import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_142_146.json")

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


BOLD0 = "Bold chapter numeral 0 in the print."
UPREF = "The reference is upright (roman figures) inside the italic statement."
INLINE = "The print sets this formula inline in the running text (as GLOBAL_ISSUES item 21)."
FONCT = ("The print reads 'fonctoriel(s)'. 'factoriel(s)' occurs five times in ega3-6-fr.tex, all on pp. 144-145 "
         "(all five reported); the file's other uses read 'fonctoriel'.")
HYPER = ("Hypertor sheaf symbol: the print sets this Tor in the heavy form (script T, bold italic 'or'), as for the bold "
         "Tor of modules; the Tor sheaves of (6.4.3)-(6.4.3.3) are in the lighter roundhand (plain T, light 'or'), which "
         "\\mathscr{T}\\!or reproduces. Proposed page fix \\boldsymbol (bold 'or'); the T shape is a document-wide decision "
         "(GLOBAL_ISSUES item 42).")

# ---------------------------------------------------------------- p. 141 / 142 boundary
add(141, "Boundary p. 141/142: blank line after the display (6.3.1.1), before \\oldpage[III]{142}",
    "p. 142 begins 'et nous dirons que cet A-module ...' flush left: the sentence of (6.3.1) continues after the display",
    "blank line after \\] and before the marker (another follows the marker): new paragraph at 'et nous dirons'",
    "other", None, "high",
    r"""\tag{6.3.1.1}\label{III.6.3.1.1.fr}
\]

""", r"""\tag{6.3.1.1}\label{III.6.3.1.1.fr}
\]
""",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). OUTSIDE pp. 142-146: the edit lies "
    "in p. 141's segment (unique in page_141.tex). Apply together with the p. 142 finding that removes the blank line "
    "after the marker. The pp. 137-141 checker may report the same edit.")

# ---------------------------------------------------------------- p. 142
add(142, "Top of p. 142: blank line after \\oldpage[III]{142}",
    "first line 'et nous dirons ...' flush left, continuing the sentence of (6.3.1)",
    "blank line after the marker", "other", None, "high",
    r"""\oldpage[III]{142}

et nous dirons""", r"""\oldpage[III]{142}
et nous dirons""",
    "Apply together with the p. 141 finding (blank line before the marker); both blank lines must go.")
add(142, "(6.3.1): 'cet A-module est l'hypertor d'indice n'", "'hypertor' italic", "upright (env body is roman)",
    "italics", None, "high", "est l'hypertor d'indice", r"est l'\emph{hypertor} d'indice")
add(142, "(6.3.1): 'complexes de A-modules limités inférieurement, les'", "'limités inférieurement' italic", "upright",
    "italics", None, "high", "$A$-modules limités inférieurement, les", r"$A$-modules \emph{limités inférieurement}, les")
add(142, "(6.3.1): 'forment un bifoncteur homologique en P., Q.'", "'bifoncteur homologique' italic", "upright",
    "italics", None, "high", "forment un bifoncteur homologique en", r"forment un \emph{bifoncteur homologique} en")
add(142, "(6.3.1): 'en P., Q. (0, 11.6.5). En outre :'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 11.6.5). En outre", r"(\textbf{0}, 11.6.5). En outre", BOLD0)
add(142, "Prop. (6.3.2): 'où, dans (6.3.2.1), Tor_q^A(P., Q.) désigne'", "(6.3.2.1) upright",
    "italic (proposition environment)", "convention", 6, "high",
    "où, dans (6.3.2.1),", r"où, dans \textup{(6.3.2.1)},", UPREF)
add(142, "Prop. (6.3.2): 'La suite spectrale (6.3.2.2) est toujours régulière'", "(6.3.2.2) upright",
    "italic (proposition environment)", "convention", 6, "high",
    "spectrale (6.3.2.2) est", r"spectrale \textup{(6.3.2.2)} est", UPREF)
add(142, "Prop. (6.3.2): 'les deux suites spectrales (6.3.2.1) et (6.3.2.2) sont birégulières'",
    "(6.3.2.1) and (6.3.2.2) upright; 'et' italic", "italic (proposition environment)", "convention", 6, "high",
    "spectrales (6.3.2.1) et (6.3.2.2) sont", r"spectrales \textup{(6.3.2.1)} et \textup{(6.3.2.2)} sont",
    "Two references in one edit; the 'et' between them is italic in the print.")
add(142, "Proof of (6.3.2): 'Cela résulte de (0, 11.6.5), car'", "bold 0", "plain 0", "convention", 2, "high",
    "de (0, 11.6.5), car", r"de (\textbf{0}, 11.6.5), car", BOLD0)
add(142, "Proof of (6.3.3): 'en vertu de (6.3.2) (0, 11.1.5).'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 11.1.5)", r"(\textbf{0}, 11.1.5)", BOLD0)
add(142, "Prop. (6.3.4): 'Soit L.. (resp. M..) un bicomplexe'", "'(resp. M..)' upright (crop)",
    "italic (proposition environment)", "convention", 6, "high",
    r"(resp. $M_{\bullet\bullet}$) un", r"\textup{(resp. $M_{\bullet\bullet}$)} un", "")
add(142, "Prop. (6.3.4): 'L_{i,.} (resp. M_{i,.}) soit une résolution'", "'(resp. M_{i,.})' upright (crop)",
    "italic (proposition environment)", "convention", 6, "high",
    r"(resp. $M_{i,\bullet}$)", r"\textup{(resp. $M_{i,\bullet}$)}", "")
add(142, "Prop. (6.3.4): 'de P_i (resp. Q_i).'", "'(resp. Q_i)' upright (crop)",
    "italic (proposition environment)", "convention", 6, "high",
    r"(resp. $Q_i$)", r"\textup{(resp. $Q_i$)}", "")
add(142, "Prop. (6.3.4): 'On a alors des isomorphismes canoniques.' before (6.3.4.1)",
    "full stop after 'canoniques' (crop)", "no full stop", "punctuation", None, "high",
    "isomorphismes canoniques\n\\[", "isomorphismes canoniques.\n\\[", "")
add(142, "Proof of (6.3.4): 'Cela résulte de (0, 11.6.5, (ii) et (iii))'", "bold 0", "plain 0", "convention", 2,
    "high", "(0, 11.6.5, (ii)", r"(\textbf{0}, 11.6.5, (ii)", BOLD0)
add(142, "(6.3.6.1), end of the display", "no full stop after the closing parenthesis (crop)",
    "full stop after \\right)", "punctuation", None, "high",
    r"Q_\bullet^\mu\right).", r"Q_\bullet^\mu\right)", "")
add(142, "Proof of (6.3.6): 'Posons P. = lim P^λ.'", "lim with only the arrow under it, no λ (crop)",
    "\\varinjlim_\\lambda", "formula", None, "high",
    r"$P_\bullet=\varinjlim_\lambda P_\bullet^\lambda$", r"$P_\bullet=\varinjlim P_\bullet^\lambda$",
    "The display (6.3.6.1) has the indices; this inline lim has none.")
add(142, "Proof of (6.3.6): 'Q. = lim Q^μ.;'", "lim with only the arrow under it, no μ (crop)",
    "\\varinjlim_\\mu", "formula", None, "high",
    r"$Q_\bullet=\varinjlim_\mu Q_\bullet^\mu$", r"$Q_\bullet=\varinjlim Q_\bullet^\mu$", "")
add(142, "Boundary p. 142/143: 'les applications Tor(P^λ, Q^μ) → Tor(P., Q.) déduites | des applications canoniques'",
    "p. 143 begins 'des applications canoniques ...' flush left, mid-sentence",
    "blank line before \\oldpage[III]{143}", "other", None, "high",
    "déduites\n\n", "déduites\n",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 143 finding that removes the blank "
    "line after the marker.")

# ---------------------------------------------------------------- p. 143
add(143, "Top of p. 143: blank line after \\oldpage[III]{143}",
    "first line 'des applications canoniques ...' flush left, continuing the sentence from p. 142",
    "blank line after the marker", "other", None, "high",
    r"""\oldpage[III]{143}

des applications""", r"""\oldpage[III]{143}
des applications""",
    "Apply together with the p. 142 finding (blank line before the marker).")
add(143, "Proof of (6.3.6): 'plus généralement un homomorphisme canonique lim ''E(P^λ, Q^μ) → ''E(P., Q.) dont (6.3.6.1)'",
    "formula inline in the running text; lim with only the arrow under it, no λ, μ (crop)",
    "displayed with \\[ \\]; \\varinjlim_{\\lambda,\\mu}", "formula", None, "high",
    r"""\[
  \varinjlim_{\lambda,\mu}''E(P_\bullet^\lambda,Q_\bullet^\mu)
  \longrightarrow ''E(P_\bullet,Q_\bullet)
\]
dont""", r"""$\varinjlim''E(P_\bullet^\lambda,Q_\bullet^\mu)\to''E(P_\bullet,Q_\bullet)$
dont""",
    "Two differences in one edit: inline in the print (GLOBAL_ISSUES item 21) and no index under lim.")
add(143, "Proof of (6.3.6): 'de même de la suite spectrale lim ''E(P^λ, Q^μ), comme il résulte'",
    "lim with only the arrow under it, no λ, μ (crop)", "\\varinjlim_{\\lambda,\\mu}", "formula", None, "high",
    r"$\varinjlim_{\lambda,\mu}''E(P_\bullet^\lambda,Q_\bullet^\mu)$",
    r"$\varinjlim''E(P_\bullet^\lambda,Q_\bullet^\mu)$", "")
add(143, "Proof of (6.3.6): 'définitions (0, 11.1.7)'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 11.1.7)", r"(\textbf{0}, 11.1.7)", BOLD0)
add(143, "Proof of (6.3.6): 'la démonstration de (0, 11.3.3)'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 11.3.3)", r"(\textbf{0}, 11.3.3)", BOLD0)
add(143, "Proof of (6.3.6): 'il suffit donc (0, 11.1.5)'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 11.1.5)", r"(\textbf{0}, 11.1.5)", BOLD0)
add(143, "(6.3.6.2)", "lim with only the arrow under it, no λ, μ (crop)", "\\varinjlim_{\\lambda,\\mu}",
    "formula", None, "high",
    r"""\varinjlim_{\lambda,\mu}''E(P_\bullet^\lambda,Q_\bullet^\mu)
  \longrightarrow ''E(P_\bullet,Q_\bullet)
  \tag{6.3.6.2}""", r"""\varinjlim''E(P_\bullet^\lambda,Q_\bullet^\mu)
  \longrightarrow ''E(P_\bullet,Q_\bullet)
  \tag{6.3.6.2}""", "")
add(143, "Proof of (6.3.6): display 'lim_{λ,μ} (Tor(F^λ, G^μ)) → Tor(lim F^λ, lim G^μ)'",
    "parentheses around Tor_.^A(F^λ, G^μ) after lim (crop)", "no parentheses", "formula", None, "high",
    r"\varinjlim_{\lambda,\mu}\operatorname{Tor}_\bullet^A(F^\lambda,G^\mu)",
    r"\varinjlim_{\lambda,\mu}(\operatorname{Tor}_\bullet^A(F^\lambda,G^\mu))", "")
add(143, "Proof of (6.3.6): 'considérons pour chaque F^λ la résolution libre canonique'",
    "'résolution libre canonique' italic", "upright", "italics", None, "high",
    "la résolution\nlibre canonique", "la \\emph{résolution\nlibre canonique}",
    "The second 'résolution libre canonique' (of G^μ) is roman in the print, as in the TeX.")
add(143, "Proof of (6.3.6): display 'L^λ. : ... → L^λ_{i+1} → L^λ_i → ... → L^λ_1 → L^λ_0 → 0'",
    "baseline dots '...' (twice, crop)", "\\cdots (twice)", "symbol", None, "high",
    r"""\cdots\longrightarrow L_{i+1}^\lambda
  \longrightarrow L_i^\lambda\longrightarrow\cdots""", r"""\ldots\longrightarrow L_{i+1}^\lambda
  \longrightarrow L_i^\lambda\longrightarrow\ldots""",
    "Baseline dots in the print; the TeX has centred \\cdots.")
add(143, "Proof of (6.3.6): 'les L_i forment une résolution L. de F'", "'résolution' italic", "upright",
    "italics", None, "high", r"forment une résolution $L_\bullet$", r"forment une \emph{résolution} $L_\bullet$")
add(143, "Proof of (6.3.6): 'limites inductives de A-modules libres, sont plats'", "'plats' italic", "upright",
    "italics", None, "high", "sont plats", r"sont \emph{plats}")
add(143, "Proof of (6.3.6): 'sont plats (0_I, 6.1.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 6.1.2)", r"(\textbf{0}\textsubscript{I}, 6.1.2)", BOLD0)
add(143, "Proof of (6.3.6): 'et M. = lim M^μ. est une résolution plate'", "lim with only the arrow under it, no μ (crop)",
    "\\varinjlim_\\mu", "formula", None, "high",
    r"$M_\bullet=\varinjlim_\mu M_\bullet^\mu$", r"$M_\bullet=\varinjlim M_\bullet^\mu$", "")
add(143, "Proof of (6.3.6): 'résolution plate de G = lim G^μ.'", "lim with only the arrow under it, no μ (crop)",
    "\\varinjlim_\\mu", "formula", None, "high",
    r"$G=\varinjlim_\mu G^\mu$", r"$G=\varinjlim G^\mu$", "")
add(143, "Proof of (6.3.6): 'On a alors Tor_.^A(lim F^λ, lim G^μ) = H.(L. ⊗_A M.)'",
    "both lims with only the arrow under them, no λ, μ (crop)", "\\varinjlim_\\lambda, \\varinjlim_\\mu",
    "formula", None, "high",
    "\\operatorname{Tor}_\\bullet^A(\\varinjlim_\\lambda F^\\lambda,\n\\varinjlim_\\mu G^\\mu)",
    "\\operatorname{Tor}_\\bullet^A(\\varinjlim F^\\lambda,\n\\varinjlim G^\\mu)", "")
add(143, "Proof of (6.3.6): 'mais H.(L. ⊗_A M.) = lim_{λ,μ} H.(L^λ. ⊗_A M^μ.) puisque'",
    "formula inline in the running text (lim with λ, μ under the arrow)", "displayed with \\[ \\]",
    "other", None, "high",
    r"""\[
  H_\bullet(L_\bullet\otimes_A M_\bullet)
  =\varinjlim_{\lambda,\mu}
   H_\bullet(L_\bullet^\lambda\otimes_A M_\bullet^\mu)
\]""", r"""$H_\bullet(L_\bullet\otimes_A M_\bullet)
=\varinjlim_{\lambda,\mu}
H_\bullet(L_\bullet^\lambda\otimes_A M_\bullet^\mu)$""", INLINE)
add(143, "(6.3.6.3)", "lim with only the arrow under it, no λ, μ (crop)", "\\varinjlim_{\\lambda,\\mu}",
    "formula", None, "high",
    r"\varinjlim_{\lambda,\mu}'E(P_\bullet^\lambda,Q_\bullet^\mu)",
    r"\varinjlim'E(P_\bullet^\lambda,Q_\bullet^\mu)", "")
add(143, "End of the proof of (6.3.6): 'est bijectif.' after (6.3.6.3)", "'bijectif' italic", "upright",
    "italics", None, "high", "est bijectif.\n\\end{proof}", "est \\emph{bijectif}.\n\\end{proof}")
add(143, "Proof of (6.3.7): 'est birégulière et dégénérée'", "'dégénérée' italic", "upright",
    "italics", None, "high", "birégulière et dégénérée", r"birégulière et \emph{dégénérée}")
add(143, "Proof of (6.3.7): 'résulte de (0, 11.1.6)'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 11.1.6)", r"(\textbf{0}, 11.1.6)", BOLD0)
add(143, "End of the p. 143 segment: \\begin{env}[6.3.8]",
    "p. 143 ends with the proof of (6.3.7) ('... ∂-foncteurs en Q.'); '(6.3.8) Soit ρ : A → A'' opens p. 144",
    "\\begin{env}[6.3.8] stands before \\oldpage[III]{144}, so the heading (6.3.8) falls on p. 143",
    "marker", None, "high",
    "\\end{proof}\n\\begin{env}[6.3.8]\n", "\\end{proof}\n",
    "Two-part move: this edit removes the opening of (6.3.8) from the end of p. 143; the p. 144 marker finding "
    "re-inserts it after \\oldpage[III]{144}. Apply both or neither.")

# ---------------------------------------------------------------- p. 144
add(144, "Start of p. 144: (6.3.8)", "p. 144 begins with '(6.3.8) Soit ρ : A → A' ...'",
    "page_144.tex begins with the marker and 'Soit'; \\begin{env}[6.3.8] stands in page_143.tex",
    "marker", None, "high",
    "\\oldpage[III]{144}\nSoit $\\rho", "\\oldpage[III]{144}\n\\begin{env}[6.3.8]\nSoit $\\rho",
    "Second half of the move begun by the p. 143 marker finding. Apply both or neither.")
add(144, "(6.3.8): 'définir un A-homomorphisme fonctoriel de degré 0'", "'fonctoriel' (crop)", "'factoriel'",
    "word", None, "high", "$A$-homomorphisme factoriel", "$A$-homomorphisme fonctoriel", FONCT)
add(144, "(6.3.8): 'une résolution de Cartan-Eilenberg projective L.. de P.'", "'projective' italic", "upright",
    "italics", None, "high",
    "Cartan-Eilenberg projective\n$L_{\\bullet\\bullet}$", "Cartan-Eilenberg \\emph{projective}\n$L_{\\bullet\\bullet}$")
add(144, "(6.3.8): 'une résolution de Cartan-Eilenberg projective L'.. de P. ⊗_A A''", "'projective' italic",
    "upright", "italics", None, "high",
    r"Cartan-Eilenberg projective $L'_{\bullet\bullet}$", r"Cartan-Eilenberg \emph{projective} $L'_{\bullet\bullet}$")
add(144, "(6.3.8): 'respectivement égales à B^I_i(L..) et H^I_i(L..)); on en déduit'",
    "two closing parentheses after H^I_i(L..) (crop); no parenthesis is open", "one closing parenthesis",
    "misprint_in_print", None, "high",
    r"\mathrm H_i^{\mathrm I}(L_{\bullet\bullet})$; on en", r"\mathrm H_i^{\mathrm I}(L_{\bullet\bullet}))$; on en",
    "Misprint: an unmatched ')'. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"\mathrm H_i^{\mathrm I}(L_{\bullet\bullet})")
add(144, "(6.3.8): 'on en déduit successivement Z^I_i(L..) = H^I_i(L..) ⊕ B^I_i(L..), puis L_{i,.} = Z^I_i(L..) ⊕ B^I_{i-1}(L..).'",
    "both formulas inline in the running text, joined by 'puis'",
    "one display with \\qquad between the formulas; 'puis' missing", "missing", None, "high",
    r"""successivement
\[
  \mathrm Z_i^{\mathrm I}(L_{\bullet\bullet})
  =\mathrm H_i^{\mathrm I}(L_{\bullet\bullet})
   \oplus\mathrm B_i^{\mathrm I}(L_{\bullet\bullet}),
  \qquad
  L_{i,\bullet}=\mathrm Z_i^{\mathrm I}(L_{\bullet\bullet})
   \oplus\mathrm B_{i-1}^{\mathrm I}(L_{\bullet\bullet}).
\]
Cela étant""", r"""successivement
$\mathrm Z_i^{\mathrm I}(L_{\bullet\bullet})
=\mathrm H_i^{\mathrm I}(L_{\bullet\bullet})
\oplus\mathrm B_i^{\mathrm I}(L_{\bullet\bullet})$, puis
$L_{i,\bullet}=\mathrm Z_i^{\mathrm I}(L_{\bullet\bullet})
\oplus\mathrm B_{i-1}^{\mathrm I}(L_{\bullet\bullet})$. Cela étant""",
    "Restores the missing word 'puis' and the inline setting (GLOBAL_ISSUES item 21).")
add(144, "(6.3.8): 'X^B_{i,.} ⊗_A A' n'est plus en général une résolution de P_i ⊗_A A''",
    "'de P_i ⊗_A A'' (crop)", "'de B_i(P.) ⊗_A A''", "misprint_in_print", None, "high",
    r"une résolution de $\mathrm B_i(P_\bullet)\otimes_A A'$", r"une résolution de $P_i\otimes_A A'$",
    "Misprint: X^B_{i,.} is the chosen projective resolution of B_i(P.), so the sentence must read B_i(P.) ⊗_A A'. "
    "The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"\mathrm B_i(P_\bullet)\otimes_A A'")
add(144, "(6.3.8): 'un complexe formé de A'-modules projectifs'", "'projectifs' italic", "upright",
    "italics", None, "high", "$A'$-modules projectifs", r"$A'$-modules \emph{projectifs}")
add(144, "(6.3.8): 'un A'-homomorphisme X^B_{i,.} ⊗_A A' → B^I_i(L'..) compatible avec les augmentations'",
    "formula inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"""\[
  X_{i,\bullet}^{\mathrm B}\otimes_A A'
  \longrightarrow \mathrm B_i^{\mathrm I}(L'_{\bullet\bullet})
\]""", r"""$X_{i,\bullet}^{\mathrm B}\otimes_A A'
\to\mathrm B_i^{\mathrm I}(L'_{\bullet\bullet})$""", INLINE)
add(144, "(6.3.8): 'un A'-homomorphisme X^H_{i,.} ⊗_A A' → H^I_i(L'..) déterminé à homotopie près'",
    "formula inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"""\[
  X_{i,\bullet}^{\mathrm H}\otimes_A A'
  \longrightarrow \mathrm H_i^{\mathrm I}(L'_{\bullet\bullet})
\]""", r"""$X_{i,\bullet}^{\mathrm H}\otimes_A A'
\to\mathrm H_i^{\mathrm I}(L'_{\bullet\bullet})$""", INLINE)
add(144, "(6.3.8): 'un A'-homomorphisme (L.. ⊗_A A') ⊗_{A'} (M.. ⊗_A A') → L'.. ⊗_{A'} M'.., puis par composition'",
    "formula inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"""\[
  (L_{\bullet\bullet}\otimes_A A')\otimes_{A'}
  (M_{\bullet\bullet}\otimes_A A')
  \longrightarrow
  L'_{\bullet\bullet}\otimes_{A'}M'_{\bullet\bullet},
\]""", r"""$(L_{\bullet\bullet}\otimes_A A')\otimes_{A'}
(M_{\bullet\bullet}\otimes_A A')
\to
L'_{\bullet\bullet}\otimes_{A'}M'_{\bullet\bullet}$,""", INLINE)
add(144, "(6.3.8): 'un A-homomorphisme de bicomplexes L.. ⊗_A M.. → L'.. ⊗_{A'} M'.., et en passant'",
    "formula inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"""\[
  L_{\bullet\bullet}\otimes_A M_{\bullet\bullet}
  \longrightarrow
  L'_{\bullet\bullet}\otimes_{A'}M'_{\bullet\bullet},
\]""", r"""$L_{\bullet\bullet}\otimes_A M_{\bullet\bullet}
\to
L'_{\bullet\bullet}\otimes_{A'}M'_{\bullet\bullet}$,""", INLINE)
add(144, "(6.3.8): 'il est clair que ρ''_{P.,Q.} = ρ'_{P'.,Q'.} ∘ ρ_{P.,Q.}, où' followed by the display 'P'. = P. ⊗_A A', Q'. = Q. ⊗_A A'.'",
    "the composition formula inline, then 'où', then only P'., Q'. displayed",
    "all in one display; 'où' missing", "missing", None, "high",
    r"""il est clair que
\[
  \rho''_{P_\bullet,Q_\bullet}
  =\rho'_{P'_\bullet,Q'_\bullet}\circ\rho_{P_\bullet,Q_\bullet},
  \qquad
""", r"""il est clair que
$\rho''_{P_\bullet,Q_\bullet}
=\rho'_{P'_\bullet,Q'_\bullet}\circ\rho_{P_\bullet,Q_\bullet}$, où
\[
""",
    "Restores the missing word 'où' and the printed layout; the rest of the display (P'., Q'.) is unchanged.")
add(144, "(6.3.8): 'Notons encore que le morphisme de bicomplexes ...'", "'Notons' begins an indented new paragraph",
    "continues the paragraph after \\]", "other", None, "high",
    "\\]\nNotons encore", "\\]\n\nNotons encore", "Paragraph break after the display in the print.")
add(144, "(6.3.8): 'définit des morphismes fonctoriels (en P. et Q.)'", "'fonctoriels' (crop)", "'factoriels'",
    "word", None, "high", "des morphismes factoriels", "des morphismes fonctoriels", FONCT)
add(144, "(6.3.8): the two morphisms of spectral sequences ''E^r_{pq}(P., Q.) → ... et ''E^r_{pq}(P., Q.) → ...,'",
    "one displayed line containing both morphisms with 'et' between them",
    "two separate displays with 'et' as a text line between them", "other", None, "medium",
    r"""\[
  'E_{pq}^r(P_\bullet,Q_\bullet)
  \longrightarrow
  'E_{pq}^r(P_\bullet\otimes_A A',Q_\bullet\otimes_A A')
\]
et
\[
  ''E_{pq}^r(P_\bullet,Q_\bullet)""", r"""\[
  'E_{pq}^r(P_\bullet,Q_\bullet)
  \longrightarrow
  'E_{pq}^r(P_\bullet\otimes_A A',Q_\bullet\otimes_A A')
  \quad\text{et}\quad
  ''E_{pq}^r(P_\bullet,Q_\bullet)""",
    "Layout only: words and formulas agree.")
add(144, "Prop. (6.3.9): 'tel que A' soit un A-module plat.'", "'plat' upright (roman) inside the italic statement (crop)",
    "italic (proposition environment)", "convention", 6, "high",
    "$A$-module plat. On a alors", r"$A$-module \textup{plat}. On a alors", "")
add(144, "Prop. (6.3.9): 'On a alors des isomorphismes canoniques fonctoriels'", "'fonctoriels' (crop)", "'factoriels'",
    "word", None, "high", "isomorphismes canoniques factoriels", "isomorphismes canoniques fonctoriels", FONCT)
add(144, "(6.3.9.1), end of the display", "no full stop after Tor(P., Q.) ⊗_A A' (crop)", "full stop",
    "punctuation", None, "high",
    "\\otimes_A A'.\n  \\tag{6.3.9.1}", "\\otimes_A A'\n  \\tag{6.3.9.1}", "")
add(144, "(6.3.9.2), end of the first line ''E(P. ⊗_A A', Q. ⊗_A A') ⥲ 'E(P., Q.) ⊗_A A''",
    "no comma at the end of the first line (crop)", "comma before \\\\", "punctuation", None, "high",
    r"'E(P_\bullet,Q_\bullet)\otimes_A A',\\", r"'E(P_\bullet,Q_\bullet)\otimes_A A'\\", "")

# ---------------------------------------------------------------- p. 145
add(145, "Proof of (6.3.9): 'sont alors des résolutions projectives de Cartan-Eilenberg'", "'résolutions' italic",
    "upright", "italics", None, "high",
    "alors des résolutions projectives", r"alors des \emph{résolutions} projectives")
add(145, "(6.3.10): 'on a donc des homomorphismes canoniques fonctoriels de degré 0'", "'fonctoriels'", "'factoriels'",
    "word", None, "high", "canoniques factoriels de degré 0", "canoniques fonctoriels de degré 0", FONCT)
add(145, "(6.3.10.1), end of the display", "no comma after Tor^{A'}(P'., Q'.) (crop)", "comma",
    "punctuation", None, "high",
    "(P'_\\bullet,Q'_\\bullet),\n  \\tag{6.3.10.1}", "(P'_\\bullet,Q'_\\bullet)\n  \\tag{6.3.10.1}", "")
add(145, "Prop. (6.3.11): 'on a un isomorphisme canonique fonctoriel'", "'fonctoriel'", "'factoriel'",
    "word", None, "high", "isomorphisme canonique factoriel", "isomorphisme canonique fonctoriel", FONCT)
add(145, "Proof of (6.3.11): 'à un isomorphisme canonique près, P'_{.[ρ]} ⊗_A M.. = P'. ⊗_{A'} (M.. ⊗_A A'); la conclusion'",
    "formula inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"""\[
  P'_{\bullet[\rho]}\otimes_A M_{\bullet\bullet}
  =P'_\bullet\otimes_{A'}(M_{\bullet\bullet}\otimes_A A');
\]""", r"""$P'_{\bullet[\rho]}\otimes_A M_{\bullet\bullet}
=P'_\bullet\otimes_{A'}(M_{\bullet\bullet}\otimes_A A')$;""", INLINE)
add(145, "(6.3.12.1)", "lim with only the arrow under it, no λ (crop)", "\\varinjlim_\\lambda",
    "formula", None, "high",
    "\\varinjlim_\\lambda\n  \\mathbf{Tor}_\\bullet^{A^\\lambda}", "\\varinjlim\n  \\mathbf{Tor}_\\bullet^{A^\\lambda}", "")
add(145, "(6.3.12.1), end of the display", "no comma after Tor^A(P., Q.) (crop)", "comma",
    "punctuation", None, "high",
    "\\mathbf{Tor}_\\bullet^A(P_\\bullet,Q_\\bullet),\n  \\tag{6.3.12.1}",
    "\\mathbf{Tor}_\\bullet^A(P_\\bullet,Q_\\bullet)\n  \\tag{6.3.12.1}", "")
add(145, "Prop. (6.3.13): 'Alors on a un isomorphisme canonique Tor^A(P., Q.) ⥲ Tor^{A'}(P., Q.).'",
    "formula inline: the line starts at the left margin as part of the statement", "displayed with \\[ \\]",
    "other", None, "high",
    r"""\[
  \mathbf{Tor}_\bullet^A(P_\bullet,Q_\bullet)
  \xrightarrow{\sim}
  \mathbf{Tor}_\bullet^{A'}(P_\bullet,Q_\bullet).
\]""", r"""$\mathbf{Tor}_\bullet^A(P_\bullet,Q_\bullet)
\xrightarrow{\sim}
\mathbf{Tor}_\bullet^{A'}(P_\bullet,Q_\bullet)$.""", INLINE)
add(145, "Proof of (6.3.13): 'tout s ∈ S définit une homothétie bijective dans Tor_.^A(P., Q.)'",
    "this Tor is set in roman, not bold (crop; the display below has bold Tor)", "\\mathbf{Tor}",
    "misprint_in_print", None, "high",
    r"bijective dans $\mathbf{Tor}_\bullet^A(P_\bullet,Q_\bullet)$",
    r"bijective dans $\operatorname{Tor}_\bullet^A(P_\bullet,Q_\bullet)$",
    "Misprint (wrong font): the homothety is on the hypertor (bold Tor, 'la fonctorialité de l'hypertor'). The TeX "
    "silently corrects; the fix restores the printed reading.",
    corrected=r"\mathbf{Tor}_\bullet^A(P_\bullet,Q_\bullet)")
add(145, "Boundary p. 145/146: display 'Tor(P., Q.) → Tor(P., Q.) ⊗_A A'' | 'est aussi un homomorphisme bijectif'",
    "p. 146 begins 'est aussi un homomorphisme bijectif.' flush left, mid-sentence",
    "blank line after \\] before \\oldpage[III]{146}", "other", None, "high",
    "\\otimes_A A'\n\\]\n\n", "\\otimes_A A'\n\\]\n",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 146 finding that removes the blank "
    "line after the marker.")

# ---------------------------------------------------------------- p. 146
add(146, "Top of p. 146: blank line after \\oldpage[III]{146}",
    "first line 'est aussi un homomorphisme bijectif.' flush left, continuing the sentence from p. 145",
    "blank line after the marker", "other", None, "high",
    r"""\oldpage[III]{146}

est aussi""", r"""\oldpage[III]{146}
est aussi""",
    "Apply together with the p. 145 finding (blank line before the marker).")
add(146, "Heading 6.4: '... cas des schémas affines.'", "final full stop", "no full stop", "punctuation", None, "high",
    "cas des schémas affines}", "cas des schémas affines.}",
    "Same pattern as GLOBAL_ISSUES item 43 (ega3-1): in ega3-6 the titles of 6.1-6.6 lack the stop and 6.7-6.10 "
    "have it; in ega3-7 no title has it (the other titles not checked against the print here).")
add(146, "(6.4.1): 'est de la forme P̃. (resp. Q̃.)'", "tilde over P only", "\\widetilde{P_\\bullet}",
    "convention", 8, "high", r"\widetilde{P_\bullet}", r"\widetilde{P}_\bullet", "")
add(146, "(6.4.1): '(resp. Q̃.)'", "tilde over Q only", "\\widetilde{Q_\\bullet}",
    "convention", 8, "high", r"\widetilde{Q_\bullet}", r"\widetilde{Q}_\bullet", "")
add(146, "(6.4.1): '(I, 1.3.7 et 1.3.8)'", "bold I", "plain I", "convention", 2, "high",
    "(I, 1.3.7 et 1.3.8)", r"(\textbf{I}, 1.3.7 et 1.3.8)", "Bold chapter numeral I in the print.")
add(146, "(6.4.1.1), left side 𝒯or_n^{𝒪_S}(𝒫., 𝒬.)", "heavy hypertor form (bold italic 'or', crop)",
    "\\mathscr{T}\\!or (light)", "font", None, "high",
    r"\mathscr{T}\!or_n^{\mathscr O_S}(\mathscr P_\bullet", r"\boldsymbol{\mathscr{T}\!or}_n^{\mathscr O_S}(\mathscr P_\bullet",
    HYPER)
add(146, "(6.4.1): 'que l'on appelle l'hypertor local d'indice n'", "only 'hypertor local' italic; 'd'indice' roman",
    "\\emph covers 'hypertor local d'indice $n$'", "italics", None, "high",
    r"l'\emph{hypertor local d'indice $n$}", r"l'\emph{hypertor local} d'indice $n$", "")
add(146, "(6.4.1): 'que l'on note aussi 𝒯or_n^S(𝒫., 𝒬.)'", "heavy hypertor form (crop)", "\\mathscr{T}\\!or (light)",
    "font", None, "high",
    r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet", r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet", HYPER)
add(146, "Lemme (6.4.2): 'Avec les notations de (6.4.1), supposons'", "(6.4.1) upright",
    "italic (namedtheorem environment)", "convention", 6, "high",
    "Avec les notations de (6.4.1), supposons", r"Avec les notations de \textup{(6.4.1)}, supposons", UPREF)
add(146, "Lemme (6.4.2): '(I, 1.6.2 et 3.2.4)'", "bold I; the reference upright except 'et', which is italic (crop)",
    "plain I; all italic", "convention", 2, "high",
    "(I, 1.6.2 et 3.2.4)", r"\textup{(\textbf{I}, 1.6.2} et \textup{3.2.4)}",
    "One edit for this finding and the next (convention 6): bold numeral and the upright parts of the reference.")
add(146, "Lemme (6.4.2): same reference '(I, 1.6.2 et 3.2.4)'", "upright inside the italic statement, 'et' italic",
    "italic (namedtheorem environment)", "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.", nofix=True)
add(146, "Lemme (6.4.2): 'On a alors 𝒯or_.^{S'}(𝒫., 𝒬.) = 𝒯or_.^S(𝒫., 𝒬.).'",
    "formula inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"""On a alors
\[
  \mathscr{T}\!or_\bullet^{S'}(\mathscr P_\bullet,\mathscr Q_\bullet)
  =\mathscr{T}\!or_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet).
\]""", r"""On a alors
$\boldsymbol{\mathscr{T}\!or}_\bullet^{S'}(\mathscr P_\bullet,\mathscr Q_\bullet)
=\boldsymbol{\mathscr{T}\!or}_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$.""",
    INLINE + " The same edit sets the two hypertor symbols in the heavy form (next finding); without that: "
    "the same new text with \\mathscr{T}\\!or for \\boldsymbol{\\mathscr{T}\\!or}.")
add(146, "Lemme (6.4.2): the two symbols 𝒯or_.^{S'}, 𝒯or_.^S", "heavy hypertor form (crop)", "\\mathscr{T}\\!or (light)",
    "font", None, "high", None, None, "Covered by the edit of the preceding finding. " + HYPER, nofix=True)
add(146, "(6.4.3): 'compte tenu de la prop. (6.3.2), que 𝒯or_.^S(𝒫., 𝒬.) est l'aboutissement'",
    "heavy hypertor form (crop)", "\\mathscr{T}\\!or (light)", "font", None, "high",
    r"$\mathscr{T}\!or_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ est",
    r"$\boldsymbol{\mathscr{T}\!or}_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ est", HYPER)
add(146, "Boundary p. 146/147: '(6.4.4) ... et supposons donnés deux | S-morphismes u : X^(1) → X'",
    "p. 147 begins 'S-morphismes u : ...' flush left, mid-sentence (top strip of p. 147)",
    "blank line before \\oldpage[III]{147}", "other", None, "high",
    "supposons donnés deux\n\n", "supposons donnés deux\n",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). page_147.tex has no blank line after its marker, so this edit "
    "alone repairs the break.")


# ---------------------------------------------------------------- checks
def page_text(p):
    with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


bad = 0
for f in F:
    if f["fix"] is None:
        continue
    t = page_text(f["page"])
    n = t.count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE (%d): p.%d %s" % (n, f["page"], f["where"]))
# apply all fixes of a page in sequence to check that they do not interfere
for p in sorted({f["page"] for f in F}):
    t = page_text(p)
    for f in F:
        if f["page"] == p and f["fix"] is not None:
            if t.count(f["fix"]["old"]) != 1:
                bad += 1
                print("SEQUENTIAL CONFLICT: p.%d %s" % (p, f["where"]))
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in sorted({f["page"] for f in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("findings", len(F), "problems", bad)
sys.exit(1 if bad else 0)
