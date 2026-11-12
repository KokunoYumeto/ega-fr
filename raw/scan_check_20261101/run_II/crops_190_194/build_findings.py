"""Build findings_190_194.json for the EGA II scan check (pp. 190-194), check every fix's "old"
occurs exactly once in its LF-normalised page_NNN.tex, and that the fixes of a page apply in any order."""
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_190_194.json"

F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


SETMIN = "Long dash for the set difference in the print, minus sign in the TeX (\\setmin is not yet the long dash; global change pending)."
PROJ = ("Script 𝒫 followed by italic 'roj' in the print (checked on crops), roman \\operatorname{Proj} in the TeX. "
        "The print keeps roman Proj for the schemes Proj(𝒮'), Proj(𝒮_X^≥), Proj(φ), Proj(α̂). "
        "ega2-indexes-and-contents-fr.tex defines \\egaShProj = \\mathcal{P}\\!\\operatorname{roj} (upright roj, not available in ega2-1); "
        "a single macro decision would cover pp. 192-198 and 202.")
TEXTUP = "Reference printed upright inside the italic statement (checked on a crop); italic in the TeX environment."

# ---------------------------------------------------------------- page 189 (segment end, outside this batch)
add(189, "end of p. 189 segment: blank line before \\oldpage[II]{190} (top of p. 190: 'est dense dans V')",
    "p. 190 begins flush left with 'est dense dans V, donc h_0 est un homéomorphisme', continuing the sentence '... et que h_0(U)' of p. 189",
    "$h_0(U)$\\n\\n\\oldpage[II]{190}: the blank line starts a new paragraph",
    "other", fx("fermé, et que $h_0(U)$\n\n", "fermé, et que $h_0(U)$\n"),
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line lies in p. 189's segment (page_189.tex), outside this batch; nothing after the p. 190 marker needs to change.")

# ---------------------------------------------------------------- page 190
add(190, "proof of (8.11.2): 'h correspond alors (I, 2.2.4) à un homomorphisme'", "(𝐈, 2.2.4), bold I",
    "plain I in the link text", "convention", fx("{I, 2.2.4}", "{\\textbf{I}, 2.2.4}"), convention=2)
add(190, "proof of (8.11.2): 'Γ(U, O_U) a pour hypothèse K pour corps des fractions'",
    "a pour hypothèse K pour corps des fractions (checked on a crop)", "a par hypothèse $K$ pour corps des fractions",
    "misprint_in_print", fx("a par hypothèse $K$", "a pour hypothèse $K$"),
    "The TeX silently corrects the print; the fix restores the printed 'pour'. 'a pour hypothèse K pour corps des fractions' does not parse; the sense is 'a, par hypothèse, K pour corps des fractions' (U is assumed to have K as field of fractions). Not in the EGA III list of errata to EGA II.",
    corrected="a par hypothèse $K$")
add(190, "proof of (8.11.2): 'φ étant l'injection canonique (I, 8.2.7)'", "(𝐈, 8.2.7), bold I",
    "plain I in the link text", "convention", fx("{I, 8.2.7}", "{\\textbf{I}, 8.2.7}"), convention=2)
add(190, "Remarque (8.11.3): 'On verra au chapitre III (III, 4.4.11)'", "(𝐈𝐈𝐈, 4.4.11), bold III",
    "plain III in the link text", "convention", fx("{III, 4.4.11}", "{\\textbf{III}, 4.4.11}"), convention=2)
add(190, "(8.11.4): 'déterminés de façon essentiellement unique.'", "'essentiellement unique' in italics (checked on a crop)",
    "upright", "italics", fx("essentiellement\nunique.", "\\emph{essentiellement\nunique}."))
add(190, "Lemme (8.11.5): 'tels que le diagramme (8.9.1.1) soit commutatif'", "(8.9.1.1) upright", "italic (lemma environment)",
    "convention", fx("(\\hyperref[II.8.9.1.1-fr]{8.9.1.1}) soit commutatif",
                     "\\textup{(\\hyperref[II.8.9.1.1-fr]{8.9.1.1})} soit commutatif"), TEXTUP, convention=6)
add(190, "Lemme (8.11.5): 'le Y-morphisme canonique (8.8.5). Il existe'", "(8.8.5) upright", "italic (lemma environment)",
    "convention", fx("(\\hyperref[II.8.8.5-fr]{8.8.5}). Il existe",
                     "\\textup{(\\hyperref[II.8.8.5-fr]{8.8.5})}. Il existe"), TEXTUP, convention=6)
add(190, "proof of (8.11.5): 'la restriction de q' à V(L)—j(X) est un isomorphisme'", "V(ℒ)—j(X), long dash", "minus sign",
    "convention", fx("$\\mathbf{V}(\\mathcal{L})-j(X)$ est un \\emph{isomorphisme}",
                     "$\\mathbf{V}(\\mathcal{L})\\setmin j(X)$ est un \\emph{isomorphisme}"), SETMIN, convention=7)
add(190, "proof of (8.11.5): 'sur C'—ε'(Y) (ε' étant la section sommet de C')'", "C'—ε'(Y), long dash", "minus sign",
    "convention", fx("$C'-\\varepsilon'(Y)$ ($\\varepsilon'$ étant", "$C'\\setmin\\varepsilon'(Y)$ ($\\varepsilon'$ étant"),
    SETMIN, convention=7)
add(190, "proof of (8.11.5): 'que q' est propre et surjectif'", "'propre' and 'surjectif' italic, 'et' roman (checked on a crop)",
    "\\emph{propre et surjectif} (the 'et' italic too)", "italics",
    fx("\\emph{propre et\nsurjectif}", "\\emph{propre} et\n\\emph{surjectif}"))
add(190, "proof of (8.11.5): 'il existe un y∈Y et un seul tel que z'=ε'(y), et en vertu de la commutativité'",
    "comma after z'=ε'(y) (checked on a crop)", "semicolon '~;'", "punctuation",
    fx("\\varepsilon'(y)$~; et en vertu", "\\varepsilon'(y)$, et en vertu"))
add(190, "proof of (8.11.5): 'en vertu de la commutativité de (8.8.5.2) et le fait que q' applique'",
    "et le fait que", "et le fait que (same as the print)", "misprint_in_print", None,
    "The TeX keeps the printed reading. 'en vertu de ... et le fait que' lacks the contraction required by 'en vertu de'; probably an authorial slip rather than a typesetting error, hence low confidence.",
    confidence="low", corrected="et du fait que")
add(190, "proof of (8.11.5): 'le fait que q' applique V(L)—j(X) dans C'—ε'(Y)', first set", "V(ℒ)—j(X), long dash", "minus sign",
    "convention", fx("$\\mathbf{V}(\\mathcal{L})-j(X)$ dans", "$\\mathbf{V}(\\mathcal{L})\\setmin j(X)$ dans"), SETMIN, convention=7)
add(190, "proof of (8.11.5): 'le fait que q' applique V(L)—j(X) dans C'—ε'(Y)', second set", "C'—ε'(Y), long dash", "minus sign",
    "convention", fx("dans $C'-\\varepsilon'(Y)$,", "dans $C'\\setmin\\varepsilon'(Y)$,"), SETMIN, convention=7)
add(190, "Corollaire (8.11.6): 'Sous les hypothèses de (8.11.5)'", "(8.11.5) upright", "italic (corollary environment)",
    "convention", fx("hypothèses de (\\hyperref[II.8.11.5-fr]{8.11.5})",
                     "hypothèses de \\textup{(\\hyperref[II.8.11.5-fr]{8.11.5})}"), TEXTUP, convention=6)
add(190, "Corollaire (8.11.6): 'supposons outre que q soit propre'", "supposons outre que (checked on a crop)",
    "supposons outre que (same as the print)", "misprint_in_print", None,
    "The TeX keeps the printed reading. 'en' is missing (compare 'On suppose en outre que' in Lemme (8.11.5)). Not in the EGA III list of errata to EGA II.",
    corrected="supposons en outre que")
add(190, "Corollaire (8.11.6): 'la restriction de q à V(L)—j(X) soit un isomorphisme'", "V(ℒ)—j(X), long dash", "minus sign",
    "convention", fx("-j(X)$ soit un", "\\setmin j(X)$ soit un"), SETMIN, convention=7)
add(190, "Corollaire (8.11.6): 'soit un isomorphisme sur C—ε(Y). Alors'", "C—ε(Y), long dash", "minus sign",
    "convention", fx("$C-\\varepsilon(Y)$. Alors", "$C\\setmin\\varepsilon(Y)$. Alors"), SETMIN, convention=7)
add(190, "Corollaire (8.11.6): 'sa restriction à C'—ε'(Y) est un isomorphisme'", "C'—ε'(Y), long dash", "minus sign",
    "convention", fx("restriction à $C'-\\varepsilon'(Y)$", "restriction à $C'\\setmin\\varepsilon'(Y)$"), SETMIN, convention=7)
add(190, "Corollaire (8.11.6), end: 'isomorphisme sur C—ε(Y).'", "C—ε(Y), long dash", "minus sign",
    "convention", fx("sur $C-\\varepsilon(Y)$.\n\\end{corollary}", "sur $C\\setmin\\varepsilon(Y)$.\n\\end{corollary}"),
    SETMIN, convention=7)
add(190, "proof of (8.11.6): 'Comme q' est un isomorphisme de V(L)—j(X)'", "V(ℒ)—j(X), long dash", "minus sign",
    "convention", fx("isomorphisme de $\\mathbf{V}(\\mathcal{L})-j(X)$", "isomorphisme de $\\mathbf{V}(\\mathcal{L})\\setmin j(X)$"),
    SETMIN, convention=7)
add(190, "proof of (8.11.6): 'sur C'—ε'(Y) (8.8.4), la dernière assertion'", "C'—ε'(Y), long dash", "minus sign",
    "convention", fx("$C'-\\varepsilon'(Y)$ (\\hyperref[II.8.8.4-fr]{8.8.4}), la dernière",
                     "$C'\\setmin\\varepsilon'(Y)$ (\\hyperref[II.8.8.4-fr]{8.8.4}), la dernière"), SETMIN, convention=7)
add(190, "end of p. 190 segment: blank line before \\oldpage[II]{191} ('la commutativité des dia-|grammes (8.8.5.2)')",
    "the word 'diagrammes' is hyphenated across the page break; p. 191 begins flush left 'grammes (8.8.5.2) et (8.9.1.1) montre que': one sentence",
    "diagrammes\\n\\n\\oldpage[II]{191}: the blank line starts a new paragraph", "other",
    fx("la commutativité des diagrammes\n\n", "la commutativité des diagrammes\n"),
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). Nothing after the p. 191 marker needs to change.")

# ---------------------------------------------------------------- page 191
add(191, "proof of (8.11.6): 'un isomorphisme de k(z) sur k(z')', first k", "bold italic k", "plain k", "convention",
    fx("$k(z)$ sur", "$\\boldsymbol{k}(z)$ sur"), "Checked on a crop.", convention=1)
add(191, "proof of (8.11.6): 'un isomorphisme de k(z) sur k(z')', second k", "bold italic k", "plain k", "convention",
    fx("sur $k(z')$", "sur $\\boldsymbol{k}(z')$"), "Independent of the first-k fix (either order works).", convention=1)
add(191, "proof of (8.11.6): 'il en est de même de u (I, 5.5.1, (v))'", "(𝐈, 5.5.1, (v)), bold I", "plain I in the link text",
    "convention", fx("{I, 5.5.1, (v)}", "{\\textbf{I}, 5.5.1, (v)}"), convention=2)
add(191, "Proposition (8.11.7): 'X un préschéma intègre'", "'intègre' roman inside the italic statement (checked on a crop)",
    "italic (proposition environment)", "convention", fx("préschéma intègre,", "préschéma \\textup{intègre},"), convention=6)
add(191, "Proposition (8.11.7): 'C un Y-préschéma normal'", "'normal' roman inside the italic statement (checked on a crop)",
    "italic (proposition environment)", "convention", fx("$Y$-préschéma normal,", "$Y$-préschéma \\textup{normal},"), convention=6)
add(191, "Proposition (8.11.7): 'tels que le diagramme (8.9.1.1) soit commutatif'", "(8.9.1.1) upright", "italic (proposition environment)",
    "convention", fx("(\\hyperref[II.8.9.1.1-fr]{8.9.1.1}) soit commutatif",
                     "\\textup{(\\hyperref[II.8.9.1.1-fr]{8.9.1.1})} soit commutatif"), TEXTUP, convention=6)
add(191, "Proposition (8.11.7): 'C'=Spec(S'), et q' : V(L)→C''", "'et' roman inside the italic statement (checked on a crop; italic in the same place in Lemme (8.11.5))",
    "italic (proposition environment)", "convention", fx("(\\mathcal{S}')$, et\n$q'", "(\\mathcal{S}')$, \\textup{et}\n$q'"), convention=6)
add(191, "Proposition (8.11.7): 'le Y-morphisme canonique (8.8.5). Alors'", "(8.8.5) upright", "italic (proposition environment)",
    "convention", fx("(\\hyperref[II.8.8.5-fr]{8.8.5}). Alors", "\\textup{(\\hyperref[II.8.8.5-fr]{8.8.5})}. Alors"), TEXTUP, convention=6)
add(191, "Proposition (8.11.7), end: 'tel que q=u∘q' est un isomorphisme.'", "'isomorphisme' roman, 'est un' italic (checked on a crop)",
    "italic (proposition environment)", "convention",
    fx("est un isomorphisme.\n\\end{proposition}", "est un \\textup{isomorphisme}.\n\\end{proposition}"), convention=6)
add(191, "Remarques (8.11.8) (i): 'si Y est affine, S' = S'~'", "S̃′: tilde over S only, the prime outside it (checked on a 5x crop)",
    "\\widetilde{S'}", "convention", fx("\\widetilde{S'}", "\\widetilde{S}'"), convention=8)
add(191, "Remarques (8.11.8) (i): 'l'anneau S'=Γ(C', S') est intègre et intégralement clos'",
    "S′=Γ(C′, 𝒮′): the second argument is the script 𝒮′ (checked on a crop)", "$S'=\\Gamma(C',\\mathcal{O}_{C'})$",
    "misprint_in_print", fx("S'=\\Gamma(C',\\mathcal{O}_{C'})", "S'=\\Gamma(C',\\mathcal{S}')"),
    "The TeX silently corrects the print; the fix restores the printed reading. 𝒮′ is an 𝒪_Y-Algèbre, not a sheaf on C′; with Y affine the ring is S′=Γ(C′, 𝒪_{C′})=Γ(Y, 𝒮′). Medium confidence only because Γ(C′, 𝒮′) may be a deliberate abuse of notation. Not in the EGA III list of errata to EGA II.",
    confidence="medium", corrected="S'=\\Gamma(C',\\mathcal{O}_{C'})")
add(191, "Remarques (8.11.8) (ii): 'il suffit de remplacer Y par le Y-schéma Y'=Spec(p_*(O_X)) et de considérer'",
    "no comma after Spec(p_*(𝒪_X)) (end of the line, checked on a crop)", "comma: '$Y'=\\operatorname{Spec}(p_*(\\mathcal{O}_X))$, et de'",
    "punctuation", fx("(p_*(\\mathcal{O}_X))$, et de", "(p_*(\\mathcal{O}_X))$ et de"))
add(191, "(8.12.1): 'Soit M un S-Module gradué quasi-cohérent;'", "'-Module gradué quasi-cohérent' in italics (checked on a crop)",
    "upright", "italics", fx("$\\mathcal{S}$-Module gradué quasi-cohérent~;", "\\emph{$\\mathcal{S}$-Module gradué quasi-cohérent}~;"))
add(191, "end of p. 191 segment: blank line before \\oldpage[II]{192} ('nous désignerons par M~ le O_C-Module | quasi-cohérent associé à M')",
    "p. 192 begins flush left with 'quasi-cohérent associé à M (1.4.3)', continuing the sentence",
    "$\\mathcal{O}_C$-Module\\n\\n\\oldpage[II]{192}: the blank line starts a new paragraph", "other",
    fx("le $\\mathcal{O}_C$-Module\n\n", "le $\\mathcal{O}_C$-Module\n"),
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). Nothing after the p. 192 marker needs to change.")

# ---------------------------------------------------------------- page 192
add(192, "(8.12.1): 'et par Proj_0(M) le O_X-Module quasi-cohérent'", "𝒫roj_0(ℳ)", "\\operatorname{Proj}_0(\\mathcal{M})",
    "font", fx("$\\operatorname{Proj}_0(\\mathcal{M})$ le", "$\\mathcal{P}\\mathit{roj}_0(\\mathcal{M})$ le"), PROJ)
add(192, "(8.12.1.1), middle term", "𝒫roj(ℳ)", "\\operatorname{Proj}(\\mathcal{M})", "font",
    fx("\\mathcal{M}_X=\\operatorname{Proj}", "\\mathcal{M}_X=\\mathcal{P}\\mathit{roj}"), "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1.1), right-hand side", "⊕_{n∈Z} 𝒫roj_0(ℳ(n))", "\\operatorname{Proj}_0", "font",
    fx("\\bigoplus_{n\\in\\mathbf{Z}}\\operatorname{Proj}_0", "\\bigoplus_{n\\in\\mathbf{Z}}\\mathcal{P}\\mathit{roj}_0"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1): 'Proj(M) est muni d'une structure'", "𝒫roj(ℳ)", "\\operatorname{Proj}(\\mathcal{M})", "font",
    fx("$\\operatorname{Proj}(\\mathcal{M})$ est muni", "$\\mathcal{P}\\mathit{roj}(\\mathcal{M})$ est muni"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1): 'une structure de S_X-Module gradué (quasi-cohérent), au moyen'",
    "'-Module gradué (quasi-cohérent)' in italics, parentheses included (checked on a crop)", "upright", "italics",
    fx("$\\mathcal{S}_X$-Module gradué (quasi-cohérent)", "\\emph{$\\mathcal{S}_X$-Module gradué (quasi-cohérent)}"))
add(192, "(8.12.1.2), first term", "𝒪_X(m)⊗_{𝒪_X}𝒫roj_0(ℳ(n))", "\\operatorname{Proj}_0", "font",
    fx("\\otimes_{\\mathcal{O}_X}\n  \\operatorname{Proj}", "\\otimes_{\\mathcal{O}_X}\n  \\mathcal{P}\\mathit{roj}"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1.2), middle term", "𝒫roj_0(𝒮(m)⊗_𝒮 ℳ(n))", "\\operatorname{Proj}_0", "font",
    fx("\\to \\operatorname{Proj}_0(\\mathcal{S}(m)", "\\to \\mathcal{P}\\mathit{roj}_0(\\mathcal{S}(m)"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1.2), last term", "𝒫roj_0(ℳ(m+n))", "\\operatorname{Proj}_0", "font",
    fx("\\to \\operatorname{Proj}_0(\\mathcal{M}(m+n))", "\\to \\mathcal{P}\\mathit{roj}_0(\\mathcal{M}(m+n))"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1.3)", "Γ(X_f, 𝒫roj(M̃))=M_f (checked on a crop)", "\\Gamma(X_f,\\operatorname{Proj}(\\widetilde{M}))", "font",
    fx("\\Gamma(X_f,\\operatorname{Proj}", "\\Gamma(X_f,\\mathcal{P}\\mathit{roj}"), "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1): 'on en déduit un O_Ĉ-Module gradué quasi-cohérent Proj_0(M̂)'", "𝒫roj_0(ℳ̂)", "\\operatorname{Proj}_0", "font",
    fx("$\\operatorname{Proj}_0(\\widehat{\\mathcal{M}})$, que", "$\\mathcal{P}\\mathit{roj}_0(\\widehat{\\mathcal{M}})$, que"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1.5)", "ℳ^□=𝒫roj_0(ℳ̂)", "\\operatorname{Proj}_0", "font",
    fx("\\mathcal{M}^{\\square}=\\operatorname{Proj}_0", "\\mathcal{M}^{\\square}=\\mathcal{P}\\mathit{roj}_0"),
    "See the first 𝒫roj finding on this page.")
add(192, "(8.12.1), after display (8.12.1.5): 'Il est clair (3.2.4) que M^□ est un foncteur'", "new paragraph (first line indented)",
    "\\end{equation}\\nIl est clair: no paragraph break", "other",
    fx("\\end{equation}\nIl est clair", "\\end{equation}\n\nIl est clair"), "Missing paragraph break.")
add(192, "(8.12.1): 'un foncteur additif exact en M'", "'exact' in italics (checked on a crop)", "upright", "italics",
    fx("additif exact en", "additif \\emph{exact} en"))
add(192, "Proposition (8.12.2): 'Avec les notations de (8.3.2)'", "(8.3.2) upright", "italic (proposition environment)",
    "convention", fx("Avec les notations de (\\hyperref[II.8.3.2-fr]{8.3.2})",
                     "Avec les notations de \\textup{(\\hyperref[II.8.3.2-fr]{8.3.2})}"), TEXTUP, convention=6)
add(192, "(8.12.2.1), second isomorphism", "j^*(ℳ^□) ⥲ 𝒫roj_0(ℳ) (checked on a crop)", "\\operatorname{Proj}_0(\\mathcal{M})", "font",
    fx("\\xrightarrow{\\sim}\n  \\operatorname{Proj}", "\\xrightarrow{\\sim}\n  \\mathcal{P}\\mathit{roj}"),
    "See the first 𝒫roj finding on this page.")
add(192, "proof of (8.12.2): 'à (M̂/(z−1)M̂)~'", "bold upright z (checked on a crop)", "italic z", "font",
    fx("\\left(\\widehat{\\mathcal{M}}/(z-1)", "\\left(\\widehat{\\mathcal{M}}/(\\mathbf{z}-1)"),
    "The indeterminate z of 𝒮̂=𝒮[z] is bold upright in the print (as reported for pp. 165-169).")
add(192, "proof of (8.12.2): 'sur Spec(Ŝ/(z−1)Ŝ)'", "bold upright z", "italic z", "font",
    fx("\\widehat{\\mathcal{S}}/(z-1)", "\\widehat{\\mathcal{S}}/(\\mathbf{z}-1)"))
add(192, "proof of (8.12.2): 'de l'isomorphisme canonique M̂/(z−1)M̂ ⥲ M'", "bold upright z", "italic z", "font",
    fx("(z-1)\\widehat{\\mathcal{M}}\n\\xrightarrow", "(\\mathbf{z}-1)\\widehat{\\mathcal{M}}\n\\xrightarrow"))
add(192, "proof of (8.12.2): 'de noyau zŜ (8.3.2)'", "bold upright z (checked on a crop)", "italic z", "font",
    fx("$z\\widehat{\\mathcal{S}}$", "$\\mathbf{z}\\widehat{\\mathcal{S}}$"))

# ---------------------------------------------------------------- page 193
add(193, "(8.12.3.1)", "p^*(𝒫roj_0(ℳ)) → ℳ^□|Ê", "\\operatorname{Proj}_0", "font",
    fx("p^*(\\operatorname{Proj}", "p^*(\\mathcal{P}\\mathit{roj}"), PROJ)
add(193, "(8.12.3), after display (8.12.3.1): 'En effet, c'est un cas particulier'", "new paragraph (first line indented)",
    "\\end{equation}\\nEn effet: no paragraph break", "other",
    fx("\\end{equation}\nEn effet, c'est", "\\end{equation}\n\nEn effet, c'est"), "Missing paragraph break.")
add(193, "(8.12.3): 'un cas particulier de l'homomorphisme υ^♯ défini de façon générale dans (3.5.6)'",
    "Greek upsilon υ^♯ (upright, hooked top, round bottom; the italic u of p. 191 and p. 194 has a tail; checked on a 4x crop)",
    "$u^{\\sharp}$", "symbol", fx("$u^{\\sharp}$ défini", "$\\upsilon^{\\sharp}$ défini"),
    "υ^♯ is the module homomorphism of (3.5.6) (υ in (3.5.6.1)-(3.5.6.2), reported as \\nu → \\upsilon for p. 64); u^♯ : g^*(𝒮)→𝒮' of (3.5.6) is the algebra homomorphism, not the case meant here.")
add(193, "(8.12.4.2), left-hand side: 𝒫roj", "𝒫roj_0ℳ", "\\operatorname{Proj}_0", "font",
    fx("\\label{II.8.12.4.2-fr}\n  \\operatorname{Proj}", "\\label{II.8.12.4.2-fr}\n  \\mathcal{P}\\mathit{roj}"),
    "See the first 𝒫roj finding on this page. Independent of the parenthesis finding at the same place (either order works).")
add(193, "(8.12.4.2), left-hand side: argument", "𝒫roj_0ℳ → (…): no parentheses around ℳ (checked on a crop)",
    "\\operatorname{Proj}_0(\\mathcal{M})\\to", "extra", fx("_0(\\mathcal{M})\\to", "_0\\mathcal{M}\\to"),
    "Same unparenthesised form as the TeX already has in (8.12.5.3), p. 194.")
add(193, "(8.12.4.2), right-hand side", "(𝒫roj_0(q^*(ℳ)⊗_{q^*(𝒮)}𝒮'))|G(φ)", "\\operatorname{Proj}_0", "font",
    fx("\\left(\\operatorname{Proj}_0\n  (q^*(\\mathcal{M})", "\\left(\\mathcal{P}\\mathit{roj}_0\n  (q^*(\\mathcal{M})"),
    "See the first 𝒫roj finding on this page.")
add(193, "(8.12.4.3), left-hand side: 𝒫roj", "𝒫roj_0ℳ̂", "\\operatorname{Proj}_0", "font",
    fx("\\label{II.8.12.4.3-fr}\n  \\operatorname{Proj}", "\\label{II.8.12.4.3-fr}\n  \\mathcal{P}\\mathit{roj}"),
    "See the first 𝒫roj finding on this page. Independent of the parenthesis finding at the same place (either order works).")
add(193, "(8.12.4.3), left-hand side: argument", "𝒫roj_0ℳ̂ → (…): no parentheses around ℳ̂ (checked on a crop)",
    "\\operatorname{Proj}_0(\\widehat{\\mathcal{M}})\\to", "extra",
    fx("_0(\\widehat{\\mathcal{M}})\\to", "_0\\widehat{\\mathcal{M}}\\to"))
add(193, "(8.12.4.3), right-hand side", "(𝒫roj_0(q^*(ℳ̂)⊗_{q^*(𝒮̂)}𝒮̂'))|G(φ̂)", "\\operatorname{Proj}_0", "font",
    fx("\\left(\\operatorname{Proj}_0\n  (q^*(\\widehat{\\mathcal{M}})", "\\left(\\mathcal{P}\\mathit{roj}_0\n  (q^*(\\widehat{\\mathcal{M}})"),
    "See the first 𝒫roj finding on this page.")
add(193, "(8.12.4.3), last factor 𝒮̂'", "𝒮̂′: hat over 𝒮 only, the prime outside it (checked on a 5x crop)",
    "\\widehat{\\mathcal{S}'}", "formula", fx("\\widehat{\\mathcal{S}'}", "\\widehat{\\mathcal{S}}'"),
    "The hat analogue of convention 8.")
add(193, "(8.12.5): 'en posant M_X^≥ = ⊕_{n≥0} Proj_0(M(n))'", "𝒫roj_0(ℳ(n))", "\\operatorname{Proj}_0", "font",
    fx("\\bigoplus_{n\\geq0}\\operatorname{Proj}_0", "\\bigoplus_{n\\geq0}\\mathcal{P}\\mathit{roj}_0"),
    "See the first 𝒫roj finding on this page.")

# ---------------------------------------------------------------- page 194
HAT = ("The print sets a circumflex accent ˆ (the hat of Ŝ, M̂) raised after the closing parenthesis (checked on a crop); "
       "^{\\wedge} typesets the wedge ∧. Proposed: the same superscript with \\widehat{\\,}; a \\superhat macro analogous to "
       "\\supertilde would be cleaner. ^{\\wedge} occurs only on this page among the EGA II page files.")
add(194, "first paragraph: 'et S_X par (S_X^≥)^ dans le raisonnement'", "(𝒮_X^≥)ˆ: circumflex after the parenthesis",
    "(\\mathcal{S}_X^{\\geq})^{\\wedge}", "symbol",
    fx("(\\mathcal{S}_X^{\\geq})^{\\wedge}$ dans", "(\\mathcal{S}_X^{\\geq})^{\\widehat{\\,}}$ dans"), HAT, confidence="medium")
add(194, "(8.12.5.2), left-hand side", "(𝒮_X^≥)ˆ", "(\\mathcal{S}_X^{\\geq})^{\\wedge}", "symbol",
    fx("(\\mathcal{S}_X^{\\geq})^{\\wedge}\n", "(\\mathcal{S}_X^{\\geq})^{\\widehat{\\,}}\n"),
    "See the first circumflex finding on this page.", confidence="medium")
add(194, "(8.12.5.2), right-hand side", "(ℳ_X^≥)ˆ.", "(\\mathcal{M}_X^{\\geq})^{\\wedge}", "symbol",
    fx("(\\mathcal{M}_X^{\\geq})^{\\wedge}.", "(\\mathcal{M}_X^{\\geq})^{\\widehat{\\,}}."),
    "See the first circumflex finding on this page.", confidence="medium")
add(194, "(8.12.5), after display (8.12.5.2): 'Si l'on se souvient (8.6.2)'", "new paragraph (first line indented)",
    "\\end{equation}\\nSi l'on: no paragraph break", "other",
    fx("\\end{equation}\nSi l'on se souvient", "\\end{equation}\n\nSi l'on se souvient"), "Missing paragraph break.")
add(194, "(8.12.5.3), left-hand side", "𝒫roj_0ℳ (checked on a crop)", "\\operatorname{Proj}_0\\mathcal{M}", "font",
    fx("\\operatorname{Proj}_0\\mathcal{M}", "\\mathcal{P}\\mathit{roj}_0\\mathcal{M}"), PROJ)
add(194, "(8.12.5.3), right-hand side", "𝒫roj_0(ℳ_X^≥)", "\\operatorname{Proj}_0", "font",
    fx("\\xrightarrow{\\sim}\\operatorname{Proj}_0(\\mathcal{M}_X^{\\geq})", "\\xrightarrow{\\sim}\\mathcal{P}\\mathit{roj}_0(\\mathcal{M}_X^{\\geq})"),
    "See the first 𝒫roj finding on this page.")
add(194, "(8.12.5), after display (8.12.5.4): 'Rappelons maintenant (8.6.2)'", "new paragraph (first line indented)",
    "\\end{equation}\\nRappelons: no paragraph break", "other",
    fx("\\end{equation}\nRappelons maintenant", "\\end{equation}\n\nRappelons maintenant"), "Missing paragraph break.")
add(194, "Proposition (8.12.6): 'du r-morphisme canonique (8.12.5.4)'", "(8.12.5.4) upright", "italic (proposition environment)",
    "convention", fx("(\\hyperref[II.8.12.5.4-fr]{8.12.5.4}) sont des", "\\textup{(\\hyperref[II.8.12.5.4-fr]{8.12.5.4})} sont des"),
    TEXTUP, convention=6)
add(194, "(8.12.6.2), left-hand side", "ℳ~|E: the tilde written after ℳ at superscript height, not over it (checked on a 3x crop)",
    "\\widetilde{\\mathcal{M}}|E", "symbol", fx("\\widetilde{\\mathcal{M}}|E", "\\mathcal{M}^{\\sim}|E"),
    "Same post-positioned tilde as (ℳ_X^≥)~ on the right-hand side, which the TeX writes ^{\\sim}; the global ^{\\sim} → \\supertilde pass (GLOBAL_ISSUES item 25) then covers both.")
add(194, "proof of (8.12.6), display, first term", "(S_f^≥)ˆ_{(f/1)}: circumflex above the subscript", "^{\\wedge}", "symbol",
    fx("(S_f^{\\geq})_{(f/1)}^{\\wedge}", "(S_f^{\\geq})_{(f/1)}^{\\widehat{\\,}}"),
    "See the first circumflex finding on this page.", confidence="medium")
add(194, "proof of (8.12.6), display, second term", "(M⊗_S S_f^≥)ˆ_{(f/1)}", "^{\\wedge}", "symbol",
    fx("(M\\otimes_S S_f^{\\geq})_{(f/1)}^{\\wedge}", "(M\\otimes_S S_f^{\\geq})_{(f/1)}^{\\widehat{\\,}}"),
    "See the first circumflex finding on this page.", confidence="medium")
add(194, "Corollaire (8.12.7): 'Avec les identifications de (8.6.3)'", "(8.6.3) upright", "italic (corollary environment)",
    "convention", fx("identifications de (\\hyperref[II.8.6.3-fr]{8.6.3})", "identifications de \\textup{(\\hyperref[II.8.6.3-fr]{8.6.3})}"),
    TEXTUP, convention=6)
add(194, "Proposition (8.12.8): 'Sous les hypothèses de (8.6.4)'", "(8.6.4) upright", "italic (proposition environment)",
    "convention", fx("hypothèses de (\\hyperref[II.8.6.4-fr]{8.6.4})", "hypothèses de \\textup{(\\hyperref[II.8.6.4-fr]{8.6.4})}"),
    TEXTUP, convention=6)
add(194, "Proposition (8.12.8): 'l'homomorphisme canonique (8.12.3.1) est un isomorphisme'", "(8.12.3.1) upright",
    "italic (proposition environment)", "convention",
    fx("canonique (\\hyperref[II.8.12.3.1-fr]{8.12.3.1}) est un", "canonique \\textup{(\\hyperref[II.8.12.3.1-fr]{8.12.3.1})} est un"),
    TEXTUP, convention=6)
add(194, "end of p. 194 segment: blank line before \\oldpage[II]{195} ('est un isomorphisme (8.6.2) et des | isomorphismes (8.12.5.4)')",
    "the sentence of the proof of (8.12.8) runs on to p. 195", "et des\\n\\n\\oldpage[II]{195}: the blank line starts a new paragraph",
    "other", fx("(\\hyperref[II.8.6.2-fr]{8.6.2}) et des\n\n", "(\\hyperref[II.8.6.2-fr]{8.6.2}) et des\n"),
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The p. 195 checker should check for a blank line after \\oldpage[II]{195}.")


# ---------------------------------------------------------------- checks
def text(p):
    return (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")


ok = True
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    t = text(d["page"])
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], n, repr(d["fix"]["old"]))
    if d["fix"]["old"] == d["fix"]["new"]:
        ok = False
        print("NO CHANGE", i)

# every fix of a page must still apply after any order of the other fixes
for p in sorted({d["page"] for d in F}):
    fixes = [d["fix"] for d in F if d["page"] == p and d["fix"]]
    for trial in range(200):
        order = fixes[:] if trial == 0 else (fixes[::-1] if trial == 1 else random.sample(fixes, len(fixes)))
        t = text(p)
        for f in order:
            if t.count(f["old"]) != 1:
                ok = False
                print("CONFLICT page", p, "trial", trial, repr(f["old"]))
                break
            t = t.replace(f["old"], f["new"], 1)
        else:
            continue
        break

print("findings:", len(F), "all checks ok" if ok else "PROBLEMS")
for p in sorted({d["page"] for d in F}):
    rows = [d for d in F if d["page"] == p]
    print(p, "normal", sum(1 for d in rows if d["kind"] not in ("convention", "misprint_in_print")),
          "convention", sum(1 for d in rows if d["kind"] == "convention"),
          "misprint", sum(1 for d in rows if d["kind"] == "misprint_in_print"))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
