import json, sys
sys.stdout.reconfigure(encoding="utf-8")

RUN = r'user\Documents\ega_scan_check_20261101\run_III1'
OUT = RUN + r'\findings_153_157.json'
NL = '\u23ce'  # placeholder for a line break in old/new strings

findings = []


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace(NL, '\n'), "new": new.replace(NL, '\n')}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected.replace(NL, '\n') if corrected is not None else None
    d["note"] = note
    findings.append(d)


def C2(page, where, numeral, old, new, note=None):
    F(page, where, "(" + numeral + ", ...) with the chapter numeral in bold", old, "convention", 2, "high",
      old, new, note or ("Bold " + numeral + " in the reference to chapter " + numeral + "."))


def C7(page, where, scan, old, new, conf="high", note="Set difference printed with the long dash; \\setmin is not yet the long dash (global change pending)."):
    F(page, where, scan, "minus sign", "convention", 7, conf, old, new, note)


BRK20 = "Spurious paragraph break at a page break inside a paragraph (GLOBAL_ISSUES item 20)."

# ---------------------------------------------------------------- p. 153
P = 153
F(P, "top of p. 153: blank line after \\oldpage[III]{153}",
  "p. 153 begins flush left 'de 𝔛; en d'autres termes, ...': the statement of Corollaire (5.2.4) runs on from p. 152",
  "\\oldpage[III]{153} followed by a blank line (new paragraph)", "other", None, "high",
  "\\oldpage[III]{153}" + NL + NL + "de $\\mathfrak X$", "\\oldpage[III]{153}" + NL + "de $\\mathfrak X$",
  BRK20 + " The blank line before the marker (last line of the p. 152 segment) must also go; that edit is in the p. 152 batch.")
C7(P, "Corollaire (5.2.4), end of the statement: '(𝒪_𝔛(—n))^k'",
   "𝒪_𝔛(—n): unary minus printed as the long dash (4x crop: the dash is longer than the n)",
   "(\\mathcal O_{\\mathfrak X}(-n))^k", "(\\mathcal O_{\\mathfrak X}(\\setmin n))^k", conf="medium",
   note="Long dash used for a minus sign, not a set difference (GLOBAL_ISSUES 23); \\setmin as for the subtractions on p. 95, pending the convention-7 decision. The superscript minus signs on these pages (⊗(−n), f^{-1}) are short and are not reported.")
C2(P, "proof of (5.2.4): 'il résulte de l'hypothèse sur ℒ_0 et de (II, 4.5.5)'", "II", "(II, 4.5.5)", "(\\textbf{II}, 4.5.5)")
F(P, "proof of (5.2.4): 'l'homomorphisme Γ(𝔛, ℱ(n))→Γ(𝔛, ℱ_0(n)) soit surjectif'",
  "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\Gamma(\\mathfrak X,\\mathcal F(n))\\longrightarrow" + NL + "\\Gamma(\\mathfrak X,\\mathcal F_0(n))" + NL + "\\]",
  "$\\Gamma(\\mathfrak X,\\mathcal F(n))\\longrightarrow" + NL + "\\Gamma(\\mathfrak X,\\mathcal F_0(n))$",
  "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36).")
C2(P, "proof of (5.2.4): 'engendrent ℱ_0(n) (0_I, 5.2.3)'", "0", "($0_{\\mathrm I}$, 5.2.3)", "($\\mathbf{0}_{\\mathrm I}$, 5.2.3)",
   "Bold 0 (GLOBAL_ISSUES 35: $\\mathbf{0}_{\\mathrm I}$).")
C2(P, "proof of (5.2.4), end: 'engendrent ℱ(n) (0_I, 5.1.1)'", "0", "($0_{\\mathrm I}$, 5.1.1)", "($\\mathbf{0}_{\\mathrm I}$, 5.1.1)",
   "Bold 0 (GLOBAL_ISSUES 35).")
F(P, "heading of (5.2.5)",
  "'(5.2.5) Démonstration du théorème d'existence : cas projectif.': the title is bold, like the number (crop)",
  "\\emph{...}: italic title", "font", None, "high",
  "\\emph{Démonstration du théorème d'existence : cas projectif.}",
  "\\textbf{Démonstration du théorème d'existence : cas projectif.}",
  "Same for (5.2.6) and 5.3.5 (p. 155). Independent of the next finding.")
F(P, "(5.2.5): after the title",
  "the title stands on its own line; 'Les notations étant celles de (5.1.4)' begins a new, indented paragraph",
  "title and text run on in one paragraph", "other", None, "high",
  "cas projectif.}" + NL + "Les notations", "cas projectif.}" + NL + NL + "Les notations",
  "Missing paragraph break after the heading. Independent of the font finding (non-overlapping change).")
F(P, "(5.2.5), l. 1: 'supposons f projectif, de sorte qu'il existe'",
  "'projectif' in italics (crop)", "upright", "italics", None, "high",
  "supposons $f$" + NL + "projectif,", "supposons $f$" + NL + "\\emph{projectif},", "")
C2(P, "(5.2.5): 'un 𝒪_X-Module ample ℒ (I, 5.5.4)'", "I", "(I, 5.5.4)", "(\\textbf{I}, 5.5.4)")
F(P, "(5.2.5): 'est égal au sous-préschéma fermé X_n×_Y Y_n=f^{-1}(Y_n) de X'",
  "X_n×_Y Y_n (subscript n on the first X; 2x crop)", "$X\\times_Y Y_n$ (silently corrected)", "misprint_in_print", None, "high",
  "$X\\times_Y Y_n=f^{-1}(Y_n)$", "$X_n\\times_Y Y_n=f^{-1}(Y_n)$",
  "The TeX silently corrects; the fix restores the printed reading. The closed subprescheme f^{-1}(Y_n) of X is X×_Y Y_n; the printed X_n×_Y Y_n is not a subprescheme of X. Not in the EGA III errata (ega3-7-fr.tex).",
  corrected="$X\\times_Y Y_n=f^{-1}(Y_n)$")
F(P, "(5.2.5): 'si ℒ' est le complété ℒ⊗_{𝒪_X}𝒪_X̂ de ℒ, on a donc'",
  "si ℒ' est le complété ℒ⊗_{𝒪_X}𝒪_X̂ de ℒ (crop)", "si ℒ'=ℒ⊗_{𝒪_X}𝒪_X̂ est le complété de ℒ", "word", None, "high",
  "$\\mathcal L'=\\mathcal L\\otimes_{\\mathcal O_X}\\mathcal O_{\\widehat X}$ est le" + NL + "complété de $\\mathcal L$",
  "$\\mathcal L'$ est le" + NL + "complété $\\mathcal L\\otimes_{\\mathcal O_X}\\mathcal O_{\\widehat X}$ de $\\mathcal L$",
  "Different wording: the print has no '=' and puts the tensor product after 'complété'.")
F(P, "(5.2.5): 'on sait que ℒ'_0 est ample (II, 4.6.13, (i bis))'",
  "'ample' in italics (crop)", "upright", "italics", None, "high",
  "est ample", "est \\emph{ample}", "")
C2(P, "(5.2.5): '(II, 4.6.13, (i bis))'", "II", "(II, 4.6.13,", "(\\textbf{II}, 4.6.13,")
F(P, "(5.2.5): '(II, 4.6.13, (i bis))'", "'bis' in italics, 'i' upright (crop)", "upright 'bis'", "italics", None, "high",
  "(i bis)", "(i \\emph{bis})", "As GLOBAL_ISSUES 26 for EGA II.")
F(P, "(5.2.5): 'isomorphe à un quotient de 𝒢=(ℒ'^{⊗(−n)})^k pour des entiers'",
  "the formula is set inline in the running text (crop)", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\mathcal G=(\\mathcal L'^{\\otimes(-n)})^k" + NL + "\\]",
  "$\\mathcal G=(\\mathcal L'^{\\otimes(-n)})^k$", "Layout: inline in the print.")
C2(P, "(5.2.5): 'le complété de (ℒ^{⊗(−n)})^k (I, 10.8.10)'", "I", "(I, 10.8.10)", "(\\textbf{I}, 10.8.10)")
C2(P, "(5.2.5): 'un 𝒪_X̂-Module cohérent (0_I, 5.3.4)'", "0", "($0_{\\mathrm I}$, 5.3.4)", "($\\mathbf{0}_{\\mathrm I}$, 5.3.4)",
   "Bold 0 (GLOBAL_ISSUES 35).")
F(P, "heading of (5.2.6)",
  "'(5.2.6) Démonstration du théorème d'existence; cas quasi-projectif.': bold title (crop)",
  "\\emph{...}: italic title", "font", None, "high",
  "\\emph{Démonstration du théorème d'existence; cas quasi-projectif.}",
  "\\textbf{Démonstration du théorème d'existence; cas quasi-projectif.}", "As for (5.2.5).")
F(P, "(5.2.6): after the title",
  "the title stands on its own line; 'Les notations étant toujours celles de (5.1.4)' begins a new, indented paragraph",
  "title and text run on in one paragraph", "other", None, "high",
  "cas quasi-projectif.}" + NL + "Les notations", "cas quasi-projectif.}" + NL + NL + "Les notations",
  "Missing paragraph break after the heading.")
F(P, "(5.2.6), l. 2: 'supposons maintenant que f soit quasi-projectif.'",
  "'quasi-projectif' in italics (crop)", "upright", "italics", None, "high",
  "soit quasi-projectif. Il existe", "soit \\emph{quasi-projectif}. Il existe", "")
C2(P, "(5.2.6): 'induit sur un ouvert de Z (II, 5.3.2)'", "II", "(II, 5.3.2)", "(\\textbf{II}, 5.3.2)")
F(P, "(5.2.6): 'si on pose Z'=g^{-1}(Y'), on a X'=X∩Z''",
  "Z'=g ¹(Y'): the minus sign of the exponent did not print; a blank gap stands before the 1 (3x crop)",
  "$Z'=g^{-1}(Y')$ (silently corrected)", "misprint_in_print", None, "medium",
  "$Z'=g^{-1}(Y')$", "$Z'=g^{\\phantom{-}1}(Y')$",
  "Print defect (failed sort or inking), handled like the unprinted periods '8 8 5' (EGA II p. 180). The TeX silently corrects; the fix restores the printed reading with the gap. The same formula g^{-1}(Y') is printed correctly at the foot of the page.",
  corrected="$Z'=g^{-1}(Y')$")
C2(P, "(5.2.6): 'sur l'ouvert X∩Z' de Ẑ (I, 10.8.5)'", "I", "(I, 10.8.5)", "(\\textbf{I}, 10.8.5)")
F(P, "(5.2.6): 'dont le support T' est propre sur Ŷ'",
  "'propre sur' in italics (crop)", "upright", "italics", None, "high",
  "est" + NL + "propre sur $\\widehat Y$", "est" + NL + "\\emph{propre sur} $\\widehat Y$", "")
F(P, "(5.2.6): 'on en conclut que T' est propre sur Y, donc fermé dans Z''",
  "'sur' in italics, 'propre' upright (crop)", "upright", "italics", None, "high",
  "propre sur $Y$, donc", "propre \\emph{sur} $Y$, donc", "")
F(P, "(5.2.6): 'donc fermé dans Z' (II, 5.4.10)'",
  "'fermé dans' in italics (crop)", "upright", "italics", None, "high",
  "donc" + NL + "fermé dans $Z'$", "donc" + NL + "\\emph{fermé dans} $Z'$", "")
C2(P, "(5.2.6): 'donc fermé dans Z' (II, 5.4.10)'", "II", "(II, 5.4.10)", "(\\textbf{II}, 5.4.10)")
F(P, "(5.2.6): 'le faisceau induit sur X̂ par le 𝒪_Z-Module 𝒢' obtenu par recollement'",
  "𝒪_Z-Module 𝒢': subscript Z without a hat (4x crop)", "$\\mathcal O_{\\widehat Z}$ (silently corrected)", "misprint_in_print", None, "high",
  "par le $\\mathcal O_{\\widehat Z}$-Module", "par le $\\mathcal O_Z$-Module",
  "The TeX silently corrects; the fix restores the printed reading. 𝒢' is glued from sheaves on the opens X̂ and Ẑ—T' of Ẑ, so it is an 𝒪_Ẑ-Module (the next sentence applies (5.2.5) to it on Ẑ). The hat may have failed to print. Not in the EGA III errata.",
  corrected="$\\mathcal O_{\\widehat Z}$")
C7(P, "(5.2.6): 'du faisceau 0 sur l'ouvert Ẑ—T' de Ẑ'", "Ẑ—T' with the long dash", "$\\widehat Z-T'$", "$\\widehat Z\\setmin T'$")
C7(P, "(5.2.6): 'dans l'ouvert intersection X̂—T''", "X̂—T' with the long dash", "$\\widehat X-T'$", "$\\widehat X\\setmin T'$")
C2(P, "(5.2.6): 'de sorte que T'=T∩Z' (I, 10.8.12)'", "I", "(I, 10.8.12)", "(\\textbf{I}, 10.8.12)")
F(P, "end of the p. 153 segment: blank line before \\oldpage[III]{154}",
  "p. 154 begins flush left 'Comme h est propre (II, 5.4.2), ...': the paragraph of (5.2.6) runs on",
  "contenant $T'$. + blank line + \\oldpage[III]{154}", "other", None, "high",
  "contenant $T'$." + NL + NL, "contenant $T'$." + NL,
  BRK20 + " Apply together with the p. 154 finding for the blank line after the marker.")

# ---------------------------------------------------------------- p. 154
P = 154
F(P, "top of p. 154: blank line after \\oldpage[III]{154}",
  "'Comme h est propre' starts flush left (no indent): continuation of the paragraph of (5.2.6)",
  "\\oldpage[III]{154} followed by a blank line", "other", None, "high",
  "\\oldpage[III]{154}" + NL + NL + "Comme", "\\oldpage[III]{154}" + NL + "Comme",
  BRK20 + " Second half; see the last p. 153 finding.")
C2(P, "(5.2.6), end: 'Comme h est propre (II, 5.4.2)'", "II", "(II, 5.4.2)", "(\\textbf{II}, 5.4.2)")
C2(P, "(5.2.6), end: 'induit sur X̂ par 𝒢̂ (I, 10.8.4)'", "I", "(I, 10.8.4)", "(\\textbf{I}, 10.8.4)")
F(P, "heading 5.3", "'5.3. Démonstration du théorème d'existence : cas général.' (final full stop)", "no full stop",
  "punctuation", None, "high",
  "\\subsection{Démonstration du théorème d'existence : cas général}",
  "\\subsection{Démonstration du théorème d'existence : cas général.}",
  "As heading 12.4 on p. 62: the \\subsection titles of ega3-1-fr.tex lack the printed full stop.")
F(P, "Lemme (5.3.1): 'Sous les conditions de (5.1.4), si'",
  "(5.1.4) upright inside the italic statement (crop)", "italic (inside the lemma environment)", "convention", 6, "high",
  "(\\hyperref[III.5.1.4-fr]{5.1.4}), si", "\\textup{(\\hyperref[III.5.1.4-fr]{5.1.4})}, si", "")
F(P, "Lemme (5.3.1): 'si 0→ℋ→ℱ→𝒢→0 est une suite exacte'",
  "the sequence is set inline", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "0\\to\\mathcal H\\to\\mathcal F\\to\\mathcal G\\to0" + NL + "\\]",
  "$0\\to\\mathcal H\\to\\mathcal F\\to\\mathcal G\\to0$", "Layout: inline in the print.")
F(P, "proof of (5.3.1): 'un élément du A-module Ext^1_{𝒪_X̂}(X̂; ℬ̂, 𝒞̂) (0, 12.3.2)'",
  "the formula is set inline", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\operatorname{Ext}^1_{\\mathcal O_{\\widehat X}}" + NL + "(\\widehat X;\\widehat{\\mathcal B},\\widehat{\\mathcal C})" + NL + "\\]",
  "$\\operatorname{Ext}^1_{\\mathcal O_{\\widehat X}}" + NL + "(\\widehat X;\\widehat{\\mathcal B},\\widehat{\\mathcal C})$",
  "Layout: inline in the print.")
C2(P, "proof of (5.3.1): '(0, 12.3.2)'", "0", "($0$, 12.3.2)", "(\\textbf{0}, 12.3.2)")
F(P, "proof of (5.3.1): 'canoniquement isomorphe à Ext^1_{𝒪_X}(X; ℬ, 𝒞) (4.5.2)'",
  "the formula is set inline", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\operatorname{Ext}^1_{\\mathcal O_X}(X;\\mathcal B,\\mathcal C)" + NL + "\\]",
  "$\\operatorname{Ext}^1_{\\mathcal O_X}(X;\\mathcal B,\\mathcal C)$", "Layout: inline in the print.")
F(P, "proof of (5.3.1): 'Mais par définition (compte tenu de (I, 10.8.8, (ii)))'",
  "(I, 10.8.8, (ii)) (2.5x crop)", "(I, 10.8.8, (iii))", "number", None, "high",
  "(I, 10.8.8, (iii))", "(\\textbf{I}, 10.8.8, (ii))",
  "Transcription error: (I, 10.8.8) has only parts (i) and (ii) (ega1-10-fr.tex); (ii), the isomorphism γ^♯: i^*(ℱ)→ℱ_{/X'}, is the part used. One edit for this finding and the next (bold I).")
F(P, "proof of (5.3.1): same reference '(I, 10.8.8, (ii))'", "bold I", "(I, ...)", "convention", 2, "high",
  None, None, "Covered by the edit of the preceding finding.")
F(P, "Corollaire (5.3.2): 'Sous les conditions de (5.1.1), soit'",
  "(5.1.1) upright inside the italic statement (crop)", "italic (inside the corollary environment)", "convention", 6, "high",
  "(\\hyperref[III.5.1.1-fr]{5.1.1}), soit", "\\textup{(\\hyperref[III.5.1.1-fr]{5.1.1})}, soit", "")
F(P, "proof of (5.3.2): 'à la suite exacte 0→Ker (u)→ℱ→Im (u)→0.'",
  "the sequence is set inline, followed by the full stop", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "0\\to\\operatorname{Ker}(u)\\to\\mathcal F\\to\\operatorname{Im}(u)\\to0." + NL + "\\]",
  "$0\\to\\operatorname{Ker}(u)\\to\\mathcal F\\to\\operatorname{Im}(u)\\to0$.", "Layout: inline in the print.")
F(P, "Lemme (5.3.3): 'Sous les conditions de (5.1.1), soient'",
  "(5.1.1) upright inside the italic statement (crop)", "italic (inside the lemma environment)", "convention", 6, "high",
  "(\\hyperref[III.5.1.1-fr]{5.1.1}), soient", "\\textup{(\\hyperref[III.5.1.1-fr]{5.1.1})}, soient", "")
C7(P, "Lemme (5.3.4): 'si U=X—Supp(𝒪_X/ℳ)'", "X—Supp with the long dash",
   "U=X-\\operatorname{Supp}", "U=X\\setmin\\operatorname{Supp}")
F(P, "Lemme (5.3.4): 'ρ_ℱ : ℱ→f̂_*(f̂^*(ℱ))'",
  "f̂^*(ℱ): superscript star only (crop)", "\\widehat f^{,*}: a comma before the star", "extra", None, "high",
  "\\[" + NL + "\\rho_{\\mathcal F}:\\mathcal F\\longrightarrow" + NL + "\\widehat f_*\\bigl(\\widehat f^{,*}(\\mathcal F)\\bigr)" + NL + "\\]",
  "$\\rho_{\\mathcal F}:\\mathcal F\\longrightarrow" + NL + "\\widehat f_*\\bigl(\\widehat f^{*}(\\mathcal F)\\bigr)$",
  "^{,*} typesets a comma the print does not have (17 such ^{,..} in ega3-1-fr.tex, see final message). One edit for this finding and the next (display set inline).")
F(P, "Lemme (5.3.4): same formula", "set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
  None, None, "Covered by the edit of the preceding finding.")
F(P, "Lemme (5.3.4): '(0_I, 4.4.3) soient annulés'", "(𝟎_I, 4.4.3): bold 0", "($0_{\\mathrm I}$, 4.4.3)",
  "convention", 2, "high", "($0_{\\mathrm I}$, 4.4.3)", "\\textup{($\\mathbf{0}_{\\mathrm I}$, 4.4.3)}",
  "One edit for this finding and the next (convention 6).")
F(P, "Lemme (5.3.4): same reference", "upright inside the italic statement (crop)", "italic (inside the lemma environment)",
  "convention", 6, "high", None, None, "Covered by the edit of the preceding finding.")
F(P, "Lemme (5.3.4), end: 'soient annulés par ℳ̂^n'", "ℳ̂^n (3x crop: no comma)", "\\widehat{\\mathcal M}^{,n}",
  "extra", None, "high", "\\widehat{\\mathcal M}^{,n}", "\\widehat{\\mathcal M}^{n}", "Extra comma in the exponent.")
F(P, "proof of (5.3.4): 'au cas où B est un anneau adique noethérien'",
  "'adique' in italics (crop)", "upright", "italics", None, "high",
  "un anneau adique" + NL + "noethérien", "un anneau \\emph{adique}" + NL + "noethérien", "")
F(P, "end of the p. 154 segment: blank line before \\oldpage[III]{155}",
  "the sentence 'B_1 est donc un | anneau adique noethérien ...' runs on to p. 155",
  "blank line after 'est donc un'", "other", None, "high",
  "$B_1$ est donc un" + NL + NL, "$B_1$ est donc un" + NL,
  BRK20 + " Apply together with the first p. 155 finding.")

# ---------------------------------------------------------------- p. 155
P = 155
F(P, "top of p. 155: blank line after \\oldpage[III]{155}",
  "p. 155 begins flush left 'anneau adique noethérien dont 𝔎_1 ...', mid-sentence",
  "\\oldpage[III]{155} followed by a blank line", "other", None, "high",
  "\\oldpage[III]{155}" + NL + NL + "anneau", "\\oldpage[III]{155}" + NL + "anneau",
  BRK20 + " Second half; see the last p. 154 finding.")
C2(P, "proof of (5.3.4): 'qui est un morphisme propre (II, 5.4.2)'", "II", "(II, 5.4.2)", "(\\textbf{II}, 5.4.2)")
C2(P, "proof of (5.3.4): 'l'application identique de B_1 (I, 10.9.1)'", "I", "(I, 10.9.1)", "(\\textbf{I}, 10.9.1)")
F(P, "proof of (5.3.4): 'Supp(𝒪_{X_1}/ℳ_1)=h^{-1}(Supp(𝒪_X/ℳ)) (I, 9.1.13)'",
  "the formula is set inline", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\operatorname{Supp}(\\mathcal O_{X_1}/\\mathcal M_1)" + NL + "=h^{-1}(\\operatorname{Supp}(\\mathcal O_X/\\mathcal M))" + NL + "\\]",
  "$\\operatorname{Supp}(\\mathcal O_{X_1}/\\mathcal M_1)" + NL + "=h^{-1}(\\operatorname{Supp}(\\mathcal O_X/\\mathcal M))$",
  "Layout: inline in the print.")
C2(P, "proof of (5.3.4): '(I, 9.1.13), donc'", "I", "(I, 9.1.13)", "(\\textbf{I}, 9.1.13)")
C7(P, "proof of (5.3.4): 'si U_1=X_1—Supp(𝒪_{X_1}/ℳ_1)'", "X_1—Supp with the long dash",
   "U_1=X_1-\\operatorname{Supp}", "U_1=X_1\\setmin\\operatorname{Supp}")
C2(P, "proof of (5.3.4): 'est un isomorphisme (I, 3.2.7)'", "I", "(I, 3.2.7)", "(\\textbf{I}, 3.2.7)")
C2(P, "proof of (5.3.4): 's'identifient par ĥ (I, 10.9.5)'", "I", "(I, 10.9.5). Toutes", "(\\textbf{I}, 10.9.5). Toutes")
C2(P, "proof of (5.3.4): 'le 𝒪_X-Module cohérent Ñ (I, 10.10.5)'", "I", "(I, 10.10.5)", "(\\textbf{I}, 10.10.5)")
F(P, "proof of (5.3.4): 'et par suite f̂^*(ℱ)=(f^*(𝒢))^ (I, 10.9.5)'",
  "(f^*(𝒢))^: parenthesis and a circumflex raised after it (crop)", "\\widehat{f^*(\\mathcal G)} (wide hat, no parentheses)",
  "formula", None, "high",
  "\\[" + NL + "\\widehat f^{,*}(\\mathcal F)=\\widehat{f^*(\\mathcal G)}" + NL + "\\]",
  "$\\widehat f^{*}(\\mathcal F)=(f^*(\\mathcal G))^{\\widehat{\\,}}$",
  "Raised circumflex written as in the EGA II p. 194 findings (^{\\widehat{\\,}}; a \\superhat macro is pending, GLOBAL_ISSUES 31). One edit for this finding and the next two (extra comma, display set inline).")
F(P, "same formula: 'f̂^*(ℱ)'", "f̂^* (no comma)", "\\widehat f^{,*}", "extra", None, "high",
  None, None, "Covered by the edit of the preceding finding.")
F(P, "same formula", "set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
  None, None, "Covered by the edit of the preceding finding.")
C2(P, "proof of (5.3.4): '(I, 10.9.5). En outre'", "I", "(I, 10.9.5). En outre", "(\\textbf{I}, 10.9.5). En outre")
F(P, "proof of (5.3.4): '(4.1.5), f̂_*((f^*(𝒢))^) s'identifie canoniquement à (f_*(f^*(𝒢)))^, et l'homomorphisme'",
  "words 's'identifie canoniquement à' between the two formulas, all inline (crop)",
  "displayed '... \\simeq ...,': the words are replaced by \\simeq", "missing", None, "high",
  "\\[" + NL + "\\widehat f_*\\bigl(\\widehat{f^*(\\mathcal G)}\\bigr)" + NL + "\\simeq\\widehat{f_*\\bigl(f^*(\\mathcal G)\\bigr)}," + NL + "\\]",
  "$\\widehat f_*((f^*(\\mathcal G))^{\\widehat{\\,}})$ s'identifie canoniquement à" + NL + "$(f_*(f^*(\\mathcal G)))^{\\widehat{\\,}}$,",
  "One edit for this finding and the next two (raised circumflexes, display set inline). The print's parentheses are of ordinary size.")
F(P, "same passage: '(f^*(𝒢))^' and '(f_*(f^*(𝒢)))^'", "circumflex raised after the closing parenthesis (twice)",
  "\\widehat{f^*(\\mathcal G)}, \\widehat{f_*\\bigl(f^*(\\mathcal G)\\bigr)}", "formula", None, "high",
  None, None, "Covered by the edit of the preceding finding.")
F(P, "same passage", "set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
  None, None, "Covered by the edit of the preceding finding.")
F(P, "proof of (5.3.4): 'le conoyau ℛ de ρ_𝒢 : 𝒢→f_*(f^*(𝒢)) sont des 𝒪_X-Modules'",
  "the formula is set inline", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\rho_{\\mathcal G}:\\mathcal G\\longrightarrow f_*\\bigl(f^*(\\mathcal G)\\bigr)" + NL + "\\]",
  "$\\rho_{\\mathcal G}:\\mathcal G\\longrightarrow f_*\\bigl(f^*(\\mathcal G)\\bigr)$", "Layout: inline in the print.")
F(P, "proof of (5.3.4): 'leurs restrictions à U sont évidemment nuls'",
  "'nuls' (crop)", "'nulles' (silently corrected)", "misprint_in_print", None, "high",
  "évidemment nulles", "évidemment nuls",
  "Agreement error in the print (the subject is 'restrictions'). The TeX silently corrects; the fix restores the printed reading.",
  corrected="évidemment nulles")
C2(P, "proof of (5.3.4): 'ℳ^n𝒫=ℳ^nℛ=0 (I, 9.3.4)'", "I", "(I, 9.3.4)", "(\\textbf{I}, 9.3.4)")
F(P, "proof of (5.3.4), end: 'ℳ̂^n𝒫̂=ℳ̂^nℛ̂=0', first term", "ℳ̂^n (crop: no comma)", "\\widehat{\\mathcal M}^{,n}",
  "extra", None, "high", "\\widehat{\\mathcal M}^{,n}\\widehat{\\mathcal P}", "\\widehat{\\mathcal M}^{n}\\widehat{\\mathcal P}",
  "Extra comma in the exponent.")
F(P, "proof of (5.3.4), end: 'ℳ̂^n𝒫̂=ℳ̂^nℛ̂=0', second term", "ℳ̂^n (crop: no comma)", "\\widehat{\\mathcal M}^{,n}",
  "extra", None, "high", "\\widehat{\\mathcal M}^{,n}\\widehat{\\mathcal R}", "\\widehat{\\mathcal M}^{n}\\widehat{\\mathcal R}",
  "Extra comma in the exponent.")
C2(P, "proof of (5.3.4), end: '(I, 10.8.8 et 10.8.10)'", "I", "(I, 10.8.8 et 10.8.10)", "(\\textbf{I}, 10.8.8 et 10.8.10)")
F(P, "heading 5.3.5: number",
  "'5.3.5. Fin de la démonstration du théorème d'existence.': number without parentheses, followed by a full stop, set like the heading '5.3.' (crop); (5.2.5) and (5.2.6) have parentheses",
  "\\begin{env}[5.3.5] prints '(5.3.5)'", "other", None, "high",
  "\\begin{env}[5.3.5]" + NL + "\\label{III.5.3.5-fr}" + NL,
  "\\par\\medskip\\noindent\\textbf{5.3.5.}\\ \\label{III.5.3.5-fr}" + NL,
  "Part 1 of 2: apply together with the p. 156 finding that replaces the matching \\end{env} (after C.Q.F.D.) by \\par. The env environment cannot print the number without parentheses; the edit writes the environment's own opening code by hand. Independent of the next two findings.")
F(P, "heading 5.3.5: title", "bold title (crop)", "\\emph{...}: italic title", "font", None, "high",
  "\\emph{Fin de la démonstration du théorème d'existence.}",
  "\\textbf{Fin de la démonstration du théorème d'existence.}", "As for (5.2.5) and (5.2.6).")
F(P, "5.3.5: after the title",
  "the title stands on its own line; 'Les hypothèses étant celles de (5.1.4)' begins a new, indented paragraph",
  "title and text run on in one paragraph", "other", None, "high",
  "théorème d'existence.}" + NL + "Les hypothèses", "théorème d'existence.}" + NL + NL + "Les hypothèses",
  "Missing paragraph break after the heading.")
C2(P, "5.3.5: 'le principe de récurrence noethérienne (0_I, 2.2.2)'", "0", "($0_{\\mathrm I}$, 2.2.2)", "($\\mathbf{0}_{\\mathrm I}$, 2.2.2)",
   "Bold 0 (GLOBAL_ISSUES 35).")
C2(P, "5.3.5: 'le lemme de Chow (II, 5.6.1)'", "II", "(II, 5.6.1)", "(\\textbf{II}, 5.6.1)")
C7(P, "5.3.5: 'un sous-préschéma fermé d'espace sous-jacent X—U'", "X—U with the long dash",
   "sous-jacent $X-U$", "sous-jacent $X\\setmin U$")
C2(P, "5.3.5: '(I, 5.2.2), et soit ℱ'", "I", "(I, 5.2.2)", "(\\textbf{I}, 5.2.2)")
F(P, "5.3.5: 'Alors ĝ^*(ℱ) est un 𝒪_Ẑ-Module cohérent'", "ĝ^* (no comma)", "\\widehat g^{,*}", "extra", None, "high",
  "Alors $\\widehat g^{,*}(\\mathcal F)$", "Alors $\\widehat g^{*}(\\mathcal F)$", "Extra comma in the exponent.")
C2(P, "5.3.5: 'donc propre (II, 5.4.6)'", "II", "(II, 5.4.6)", "(\\textbf{II}, 5.4.6)")
F(P, "5.3.5: 'Comme h est quasi-projectif, ĝ^*(ℱ) est algébrisable'", "ĝ^* (no comma)", "\\widehat g^{,*}", "extra", None, "high",
  "quasi-projectif, $\\widehat g^{,*}(\\mathcal F)$", "quasi-projectif, $\\widehat g^{*}(\\mathcal F)$", "Extra comma in the exponent.")
F(P, "end of the p. 155 segment: blank line before \\oldpage[III]{156}",
  "the sentence 'On en conclut | que ĝ_*(ĝ^*(ℱ)) est ...' runs on to p. 156", "blank line after 'On en conclut'",
  "other", None, "high", "On en conclut" + NL + NL, "On en conclut" + NL,
  BRK20 + " Apply together with the first p. 156 finding.")

# ---------------------------------------------------------------- p. 156
P = 156
F(P, "top of p. 156: blank line after \\oldpage[III]{156}",
  "p. 156 begins flush left 'que ĝ_*(ĝ^*(ℱ)) est un ...', mid-sentence", "\\oldpage[III]{156} followed by a blank line",
  "other", None, "high", "\\oldpage[III]{156}" + NL + NL + "que", "\\oldpage[III]{156}" + NL + "que",
  BRK20 + " Second half; see the last p. 155 finding.")
F(P, "5.3.5, l. 1: 'que ĝ_*(ĝ^*(ℱ)) est un 𝒪_X̂-Module algébrisable'", "ĝ^* (no comma)", "\\widehat g^{,*}", "extra", None, "high",
  "\\widehat g^{,*}(\\mathcal F)\\bigr)$ est un", "\\widehat g^{*}(\\mathcal F)\\bigr)$ est un", "Extra comma in the exponent.")
F(P, "5.3.5, l. 2: 'appliquer à ℱ et à g le résultat de (5.2.4) : le noyau 𝒫'",
  "(5.2.4) (crop)", "(\\hyperref[III.5.3.4-fr]{5.3.4}) (silently corrected)", "misprint_in_print", None, "high",
  "(\\hyperref[III.5.3.4-fr]{5.3.4})~: le noyau", "(\\hyperref[III.5.2.4-fr]{5.2.4})~: le noyau",
  "The result applied (kernel and cokernel of ρ_ℱ killed by a power ℳ̂^n) is Lemme (5.3.4); (5.2.4) is the corollary on quotients of 𝒪_𝔛(−n)^k. The TeX silently corrects; the fix restores the printed reading (link target as printed, as in the EGA II p. 129 finding). Not in the EGA III errata.",
  corrected="(\\hyperref[III.5.3.4-fr]{5.3.4})")
F(P, "5.3.5: 'ρ_ℱ : ℱ→ĝ_*(ĝ^*(ℱ)) sont annulés'", "ĝ^* (no comma)", "\\widehat g^{,*}", "extra", None, "high",
  "\\widehat g^{,*}(\\mathcal F)\\bigr)$ sont annulés", "\\widehat g^{*}(\\mathcal F)\\bigr)$ sont annulés", "Extra comma in the exponent.")
F(P, "5.3.5: 'par une puissance ℳ̂^n'", "ℳ̂^n (no comma)", "\\widehat{\\mathcal M}^{,n}", "extra", None, "high",
  "puissance $\\widehat{\\mathcal M}^{,n}$", "puissance $\\widehat{\\mathcal M}^{n}$", "Extra comma in the exponent.")
C7(P, "5.3.5: 'ayant X—U pour espace sous-jacent'", "X—U with the long dash", "ayant $X-U$ pour", "ayant $X\\setmin U$ pour")
C2(P, "5.3.5: 'est l'injection canonique (I, 10.14.7). On peut'", "I", "(I, 10.14.7). On", "(\\textbf{I}, 10.14.7). On")
F(P, "5.3.5: '𝒫=ĵ_*(ĵ^*(𝒫)))', inner term", "ĵ^* (no comma)", "\\widehat j^{,*}", "extra", None, "high",
  "\\bigl(\\widehat j^{,*}(\\mathcal P)", "\\bigl(\\widehat j^{*}(\\mathcal P)", "Extra comma in the exponent.")
F(P, "5.3.5: 'On peut donc écrire 𝒫=ĵ_*(ĵ^*(𝒫))) et ℛ=ĵ_*(ĵ^*(ℛ))'",
  "𝒫=ĵ_*(ĵ^*(𝒫))): three closing parentheses (3x crop; the ℛ formula has two)",
  "two closing parentheses (silently corrected)", "misprint_in_print", None, "high",
  "\\bigr)$ et" + NL + "$\\mathcal R=", "\\bigr))$ et" + NL + "$\\mathcal R=",
  "Extra closing parenthesis in the print. The TeX silently corrects; the fix restores the printed reading. Independent of the comma finding before it.",
  corrected="$\\mathcal P=\\widehat j_*\\bigl(\\widehat j^{*}(\\mathcal P)\\bigr)$")
F(P, "5.3.5: 'ℛ=ĵ_*(ĵ^*(ℛ))'", "ĵ^* (no comma)", "\\widehat j^{,*}", "extra", None, "high",
  "\\bigl(\\widehat j^{,*}(\\mathcal R)", "\\bigl(\\widehat j^{*}(\\mathcal R)", "Extra comma in the exponent.")
F(P, "5.3.5: 'que ĵ^*(𝒫) et ĵ^*(ℛ) sont des 𝒪_T̂-Modules', first term", "ĵ^* (no comma)", "\\widehat j^{,*}", "extra", None, "high",
  "$\\widehat j^{,*}(\\mathcal P)$", "$\\widehat j^{*}(\\mathcal P)$", "Extra comma in the exponent.")
F(P, "5.3.5: 'que ĵ^*(𝒫) et ĵ^*(ℛ) sont des 𝒪_T̂-Modules', second term", "ĵ^* (no comma)", "\\widehat j^{,*}", "extra", None, "high",
  "$\\widehat j^{,*}(\\mathcal R)$", "$\\widehat j^{*}(\\mathcal R)$", "Extra comma in the exponent.")
F(P, "end of 5.3.5 (after C.Q.F.D.)", "(see the 5.3.5 heading finding on p. 155)", "\\end{env}", "other", None, "high",
  "\\hfill C.Q.F.D." + NL + "\\end{env}", "\\hfill C.Q.F.D." + NL + "\\par",
  "Part 2 of 2 of the 5.3.5 heading edit (p. 155): apply both or neither. \\par is the environment's own closing code.")
F(P, "heading 5.4", "'... Schémas formels algébrisables.' (final full stop)", "no full stop", "punctuation", None, "high",
  "Schémas formels algébrisables}", "Schémas formels algébrisables.}", "As heading 5.3 (p. 154).")
F(P, "Théorème (5.4.1), end: 'l'application f⇝f̂ est une bijection'", "f ⇝ f̂ (wavy arrow, crop)", "$f\\mapsto\\widehat f$",
  "symbol", None, "high", "l'application $f\\mapsto\\widehat f$", "l'application $f\\leadsto\\widehat f$",
  "Wavy maps-to arrow in the print (\\leadsto; GLOBAL_ISSUES 33).")
F(P, "proof of (5.4.1): 'Montrons d'abord que f⇝f̂ est injective'", "f ⇝ f̂ (wavy arrow, crop)", "$f\\mapsto\\widehat f$",
  "symbol", None, "high", "Montrons d'abord que $f\\mapsto\\widehat f$", "Montrons d'abord que $f\\leadsto\\widehat f$",
  "Wavy maps-to arrow (\\leadsto).")
C2(P, "proof of (5.4.1): 'On sait alors (I, 10.9.4)'", "I", "(I, 10.9.4)", "(\\textbf{I}, 10.9.4)")
F(P, "proof of (5.4.1): 'Prouvons maintenant que f⇝f̂ est surjective'", "f ⇝ f̂ (wavy arrow, crop)", "$f\\mapsto\\widehat f$",
  "symbol", None, "high", "Prouvons maintenant que $f\\mapsto\\widehat f$", "Prouvons maintenant que $f\\leadsto\\widehat f$",
  "Wavy maps-to arrow (\\leadsto).")
C2(P, "proof of (5.4.1): 'Z est de type fini sur S (I, 6.3.4)'", "I", "(I, 6.3.4)", "(\\textbf{I}, 6.3.4)")
C2(P, "proof of (5.4.1): 'les prolongements p̂ et q̂ (I, 10.9.7)'", "I", "(I, 10.9.7)", "(\\textbf{I}, 10.9.7)")
C2(P, "proof of (5.4.1): 'Ŷ est séparé sur Ŝ (I, 10.15.7)'", "I", "(I, 10.15.7)", "(\\textbf{I}, 10.15.7)")
F(P, "proof of (5.4.1): 'le morphisme graphe Γ_h=(1_X̂, h) : X̂→Ẑ est une immersion fermée'",
  "the formula is set inline", "displayed with \\[ ... \\]", "other", None, "high",
  "\\[" + NL + "\\Gamma_h=(1_{\\widehat X},h):\\widehat X\\to\\widehat Z" + NL + "\\]",
  "$\\Gamma_h=(1_{\\widehat X},h):\\widehat X\\to\\widehat Z$", "Layout: inline in the print.")
C2(P, "proof of (5.4.1): 'une immersion fermée (I, 10.15.4)'", "I", "(I, 10.15.4)", "(\\textbf{I}, 10.15.4)")
C2(P, "proof of (5.4.1): 'est un isomorphisme (I, 10.14.3)'", "I", "(I, 10.14.3)", "(\\textbf{I}, 10.14.3)")
C2(P, "proof of (5.4.1): 'l'injection canonique T→Z (I, 10.14.7). Alors'", "I", "(I, 10.14.7). Alors", "(\\textbf{I}, 10.14.7). Alors")
F(P, "proof of (5.4.1), last line: 'car il en est ainsi de (p∘i)^=p̂∘î par hypothèse'",
  "(p∘i)^: circumflex raised after the parenthesis (crop)", "\\widehat{p\\circ i}", "formula", None, "high",
  "$\\widehat{p\\circ i}=\\widehat p\\circ\\widehat i$", "$(p\\circ i)^{\\widehat{\\,}}=\\widehat p\\circ\\widehat i$",
  "Raised circumflex as in the EGA II p. 194 findings.")
F(P, "end of the p. 156 segment: blank line before \\oldpage[III]{157}",
  "the sentence 'et il suffit d'appliquer | (4.6.8) en notant ...' runs on to p. 157", "blank line after 'd'appliquer'",
  "other", None, "high", "d'appliquer" + NL + NL, "d'appliquer" + NL,
  BRK20 + " Apply together with the first p. 157 finding.")

# ---------------------------------------------------------------- p. 157
P = 157
F(P, "top of p. 157: blank line after \\oldpage[III]{157}",
  "p. 157 begins flush left '(4.6.8) en notant comme ci-dessus ...', mid-sentence", "\\oldpage[III]{157} followed by a blank line",
  "other", None, "high", "\\oldpage[III]{157}" + NL + NL + "(4.6.8)", "\\oldpage[III]{157}" + NL + "(4.6.8)",
  BRK20 + " Second half; see the last p. 156 finding.")
F(P, "proof of (5.4.1): 'l'isomorphisme réciproque de (p∘i)^=w'", "(p∘i)^ (raised circumflex, crop)", "\\widehat{p\\circ i}",
  "formula", None, "high", "$\\widehat{p\\circ i}=w$", "$(p\\circ i)^{\\widehat{\\,}}=w$", "Raised circumflex after the parenthesis.")
F(P, "proof of (5.4.1): 'on a (Γ_f)^=î∘ĝ=j∘w=Γ_h.'",
  "(Γ_f)^ with a raised circumflex; the formula is set inline (crop)", "displayed \\widehat{\\Gamma_f}=...", "formula", None, "high",
  "\\[" + NL + "\\widehat{\\Gamma_f}=\\widehat i\\circ\\widehat g=j\\circ w=\\Gamma_h." + NL + "\\]",
  "$(\\Gamma_f)^{\\widehat{\\,}}=\\widehat i\\circ\\widehat g=j\\circ w=\\Gamma_h$.",
  "One edit for this finding and the next (display set inline).")
F(P, "same formula", "set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
  None, None, "Covered by the edit of the preceding finding.")
F(P, "proof of (5.4.1): 'Mais on sait que (Γ_f)^=Γ_f̂ (I, 10.9.8)'", "(Γ_f)^ (raised circumflex, crop)", "\\widehat{\\Gamma_f}",
  "formula", None, "high", "$\\widehat{\\Gamma_f}=\\Gamma_{\\widehat f}$", "$(\\Gamma_f)^{\\widehat{\\,}}=\\Gamma_{\\widehat f}$",
  "Raised circumflex after the parenthesis.")
C2(P, "proof of (5.4.1): '(I, 10.9.8), d'où finalement'", "I", "(I, 10.9.8)", "(\\textbf{I}, 10.9.8)")
F(P, "after (5.4.1): 'que le foncteur X⇝X̂ est pleinement fidèle'", "X ⇝ X̂ (wavy arrow)", "$X\\mapsto\\widehat X$",
  "symbol", None, "high", "$X\\mapsto\\widehat X$", "$X\\leadsto\\widehat X$", "Wavy maps-to arrow (\\leadsto).")
F(P, "after (5.4.1): 'est pleinement fidèle (0, 8.1.6)'", "'pleinement fidèle' in italics (crop)", "upright",
  "italics", None, "high", "est pleinement fidèle", "est \\emph{pleinement fidèle}", "")
C2(P, "after (5.4.1): '(0, 8.1.6)'", "0", "($0$, 8.1.6)", "(\\textbf{0}, 8.1.6)")
F(P, "after (5.4.1): 'une sous-catégorie de la seconde'", "'sous-catégorie' in italics (crop)", "upright",
  "italics", None, "high", "sous-catégorie de la seconde", "\\emph{sous-catégorie} de la seconde", "")
F(P, "heading of (5.4.2)",
  "'Scholie (5.4.2). — Avec les notations ...': a statement heading ('Scholie' italic, number, '. —'), body roman (crop)",
  "\\begin{env}[5.4.2] + \\emph{Scholie.}: '(5.4.2) Scholie. Avec ...' (no dash, order reversed)", "other", None, "high",
  "\\begin{env}[5.4.2]" + NL + "\\label{III.5.4.2-fr}" + NL + "\\emph{Scholie.}" + NL,
  "\\begin{scholium}[5.4.2]" + NL + "\\label{III.5.4.2-fr}" + NL,
  "Part 1 of 2: apply together with the finding 'end of Scholie (5.4.2)' (\\end{env} -> \\end{scholium}). The preamble's scholium environment prints 'Scholie (n). ---' with a roman body, as the print (number font: document-wide).")
F(P, "Scholie (5.4.2): 'se donner un S-morphisme f : X→Y équivaut à se donner'", "'équivaut' in italics (crop)", "upright",
  "italics", None, "high", "f:X\\to Y$ équivaut", "f:X\\to Y$ \\emph{équivaut}", "")
C2(P, "Scholie (5.4.2): 'et de (I, 10.12.3)'", "I", "(I, 10.12.3)", "(\\textbf{I}, 10.12.3)")
C2(P, "Scholie (5.4.2): 'système inductif adique (I, 10.12.2)'", "I", "(I, 10.12.2)", "(\\textbf{I}, 10.12.2)")
F(P, "end of Scholie (5.4.2)", "(see the heading finding)", "\\end{env}", "other", None, "high",
  "$f_n:X_n\\to Y_n$." + NL + "\\end{env}", "$f_n:X_n\\to Y_n$." + NL + "\\end{scholium}",
  "Part 2 of 2 of the (5.4.2) heading edit: apply both or neither.")
F(P, "Remarque (5.4.3): 'et qui ne sont pas algébrisables (tout comme'",
  "'ne sont pas algébrisables' in italics in the roman remark (crop)", "no \\emph", "italics", None, "high",
  "et qui ne sont pas algébrisables", "et qui \\emph{ne sont pas algébrisables}",
  "Judged with the remark body as roman (document-wide remark item).")
F(P, "proof of (5.4.4): 'la fibre f^{-1}(y) soit finie (4.8.11)'", "'finie' in italics (crop)", "upright",
  "italics", None, "high", "soit finie (", "soit \\emph{finie} (", "")
F(P, "end of the p. 157 segment: blank line before \\oldpage[III]{158}",
  "p. 158 begins flush left 'Soit ℒ un 𝒪_𝔛-Module inversible, et supposons ...' (italic): the statement of Théorème (5.4.5) runs on",
  "blank line after '=ℱ/𝔍^{k+1}ℱ.'", "other", None, "high",
  "\\mathcal F/\\mathfrak J^{k+1}\\mathcal F$." + NL + NL, "\\mathcal F/\\mathfrak J^{k+1}\\mathcal F$." + NL,
  BRK20 + " The blank line after \\oldpage[III]{158} (p. 158 batch) must also go; top of p. 158 checked on page_158_s1.png.")

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for p in (153, 154, 155, 156, 157):
    with open(RUN + r'\page_%d.tex' % p, encoding='utf-8', newline='') as fh:
        texts[p] = fh.read().replace('\r\n', '\n')

# 1) each old occurs exactly once in its page file
for i, d in enumerate(findings):
    fx = d['fix']
    if fx is None:
        continue
    n = texts[d['page']].count(fx['old'])
    if n != 1:
        ok = False
        print('COUNT', n, 'page', d['page'], repr(fx['old'])[:120])

# 2) sequential application on each page (order of the list) keeps every old unique at its turn
for p in texts:
    t = texts[p]
    for d in findings:
        if d['page'] != p or d['fix'] is None:
            continue
        o, nw = d['fix']['old'], d['fix']['new']
        c = t.count(o)
        if c != 1:
            ok = False
            print('SEQ', c, 'page', p, repr(o)[:120])
            continue
        t = t.replace(o, nw)
    # reverse order too
    t = texts[p]
    for d in reversed([x for x in findings if x['page'] == p and x['fix'] is not None]):
        o, nw = d['fix']['old'], d['fix']['new']
        c = t.count(o)
        if c != 1:
            ok = False
            print('REV', c, 'page', p, repr(o)[:120])
            continue
        t = t.replace(o, nw)

# counts per page
for p in (153, 154, 155, 156, 157):
    ds = [d for d in findings if d['page'] == p]
    conv = sum(1 for d in ds if d['kind'] == 'convention')
    mis = sum(1 for d in ds if d['kind'] == 'misprint_in_print')
    print(p, 'normal', len(ds) - conv - mis, 'convention', conv, 'misprint', mis)

print('ALL OK' if ok else 'PROBLEMS')
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(findings, fh, ensure_ascii=False, indent=1)
    print('written', OUT, len(findings))
