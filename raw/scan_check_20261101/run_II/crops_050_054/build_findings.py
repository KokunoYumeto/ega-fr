# Builds findings_050_054.json for EGA II pp. 50-54 and checks every fix.
# "old"/"new" are written as raw strings; the character ¶ stands for a line break (LF).
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_050_054.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
CUR = pathlib.Path(str(REL).replace("\\diplomatic\\", "\\current\\"))


def nl(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else {"old": nl(old), "new": nl(new)})
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def c6ref(page, where, ref_tex, nofix=False, note=None):
    """A reference printed upright inside an italic statement (convention 6)."""
    add(page, where, "reference printed upright (roman parentheses and figures) inside the italic statement",
        ref_tex + " (italic inside the statement environment)", "convention", 6, "high",
        ref_tex, "\\textup{" + ref_tex + "}",
        note or "Roman item inside an italic statement.", nofix=nofix)


def c2(page, where, ref, old=None, new=None, note="", nofix=False):
    num = ref.split(", ")[0]
    add(page, where, f"({ref}) with bold {num}", f"(\\hyperref[...]{{{ref}}}) with plain {num}",
        "convention", 2, "high",
        old if old is not None else "{" + ref + "}",
        new if new is not None else "{\\textbf{" + num + "}, " + ref.split(", ")[1] + "}",
        note or f"Bold {num} in the printed reference.", nofix=nofix)


# ---------------------------------------------------------------- page 50
c2(50, "(3.1.1), line 1: 'graduée (I, 1.4.3)'", "I, 1.4.3")
c2(50, "(3.1.1): 'S⊗_A A' (I, 1.6.4)'", "I, 1.6.4")
c2(50, "(3.1.1): 'le morphisme structural X_U→U (I, 4.4.1)'", "I, 4.4.1")
add(50, "(3.1.1), last sentence: 'on a ρ_{U'',U}=…'",
    "ρ_{U'',U}=ρ_{U'',U'}∘ρ_{U',U}", r"\rho_{U'',U}=\rho_{U',U}\circ\rho_{U'',U'}",
    "misprint_in_print", None, "high",
    r"\rho_{U'',U}=\rho_{U',U}\circ\rho_{U'',U'}", r"\rho_{U'',U}=\rho_{U'',U'}\circ\rho_{U',U}",
    "The print composes in the wrong order (ρ_{U'',U'}: X_{U''}→X_{U'} has to act first); the TeX silently "
    "corrects it. The fix restores the printed order.",
    corrected=r"\rho_{U'',U}=\rho_{U',U}\circ\rho_{U'',U'}")
add(50, "Proposition (3.1.2): 'il existe un isomorphisme η_U du préschéma induit'",
    "'isomorphisme' in the italic of the statement (no change of face)",
    r"\emph{isomorphisme} (comes out upright inside the italic proposition)",
    "convention", 6, "high", r"un \emph{isomorphisme} $\eta_U$", r"un isomorphisme $\eta_U$",
    "Drop \\emph: the print shows no change of face here.")
add(50, "diagram (3.1.2.1), top arrow f^{-1}(V)→X_V",
    "isomorphism arrow (tilde above the arrow), η_V written above it", r"\ar[r]^{\eta_V} (plain arrow)",
    "symbol", None, "high", r"\ar[r]^{\eta_V}", r"\ar[r]^{\overset{\eta_V}{\sim}}",
    "Missing tilde of the isomorphism arrow.")
add(50, "diagram (3.1.2.1), bottom arrow f^{-1}(U)→X_U",
    "isomorphism arrow (tilde above the arrow), η_U written below it", r"\ar[r]_{\eta_U} (plain arrow)",
    "symbol", None, "high", r"\ar[r]_{\eta_U}", r"\ar[r]^{\sim}_{\eta_U}",
    "Missing tilde of the isomorphism arrow.")
c2(50, "proof of (3.1.2): 'résulte donc de (I, 2.3.1)'", "I, 2.3.1")
c2(50, "(3.1.3): '((2.4.2) et (I, 5.5.5))'", "I, 5.5.5")
c2(50, "(3.1.3): 'de type fini (I, 9.6.2)'", "I, 9.6.2")
add(50, "(3.1.3): 'si 𝒮 est une 𝒪_Y-Algèbre de type fini (I, 9.6.2) Proj(𝒮) est de type fini'",
    "(I, 9.6.2) Proj(𝒮) — no comma after the reference",
    r"(\hyperref[I.9.6.2-fr]{I, 9.6.2}), $\operatorname{Proj}(\mathcal{S})$",
    "punctuation", None, "high",
    r"), $\operatorname{Proj}(\mathcal{S})$ est", r") $\operatorname{Proj}(\mathcal{S})$ est",
    "The TeX adds a comma that the print does not have.")
c2(50, "(3.1.3): '((2.7.1, (ii)) et (I, 6.3.1))'", "I, 6.3.1")
add(50, "page end: 'pour tout ouvert affine U de Y,' continues on p. 51 with 'X_f∩φ^{-1}(U)=…'",
    "one sentence running across the page break", "blank line before \\oldpage[II]{51} (paragraph break)",
    "other", None, "high", r"affine $U$ de $Y$,¶¶", r"affine $U$ de $Y$,¶",
    "Spurious paragraph break at a mid-sentence page break (end of this page's segment; the blank line after "
    "\\oldpage[II]{51} is removed in the p. 51 entry).")

# ---------------------------------------------------------------- page 51
add(51, "page start: Proposition (3.1.4) continues 'X_f∩φ^{-1}(U)=D_+(f|U) dans …'",
    "one sentence running across the page break", "blank line after \\oldpage[II]{51} (paragraph break)",
    "other", None, "high", r"\oldpage[II]{51}¶¶$X_f", r"\oldpage[II]{51}¶$X_f",
    "Spurious paragraph break at a mid-sentence page break (the blank line before the marker is removed in the "
    "p. 50 entry).")
c6ref(51, "Proposition (3.1.4), end of statement: 'Spec(𝒮^{(d)}/(f−1)𝒮^{(d)}) (1.3.1).'",
      r"(\hyperref[II.1.3.1-fr]{1.3.1})")
add(51, "proof of (3.1.4): 's'identifie canoniquement à Spec((Γ(U, 𝒮))_{f|U})'",
    "Spec((Γ(U, 𝒮))_{f|U}) — subscript f|U without parentheses",
    r"\operatorname{Spec}((\Gamma(U,\mathcal{S}))_{(f|U)})",
    "misprint_in_print", None, "high", r"\mathcal{S}))_{(f|U)}", r"\mathcal{S}))_{f|U}",
    "The scheme induced on D_+(f|U) is Spec of the degree-0 ring (·)_{(f|U)} (2.3.6; the next step uses "
    "2.2.5 for that ring); the print drops the parentheses of the subscript. The TeX silently corrects it; "
    "the fix restores the printed reading.",
    corrected=r"\operatorname{Spec}((\Gamma(U,\mathcal{S}))_{(f|U)})")
c2(51, "Corollaire (3.1.6): 'engendré par cette famille (0, 5.1.1)'", "0, 5.1.1",
   old=r"(\hyperref[0.5.1.1-fr]{0, 5.1.1})", new=r"\textup{(\hyperref[0.5.1.1-fr]{\textbf{0}, 5.1.1})}",
   note="Bold 0. The same edit sets the reference upright (convention 6, next entry, fix null).")
c6ref(51, "Corollaire (3.1.6): '(0, 5.1.1)' inside the italic statement", r"(\hyperref[0.5.1.1-fr]{0, 5.1.1})",
      nofix=True, note="Applied by the convention-2 edit of the previous entry, hence fix null.")
add(51, "proof of (3.1.7), last line: 'est canoniquement isomorphe à 𝒜, d'où le corollaire (1.2.2).'",
    "(1.2.2)", r"(\hyperref[II.1.2.2-fr]{1.2.2})", "misprint_in_print", None, "medium", None, None,
    "Wrong reference: (1.2.2) says that a closed subprescheme of S is affine over S. The conclusion "
    "X=X_f≅Spec(𝒮/(f−1)𝒮)≅Spec(𝒜) comes from (3.1.4), which the corrected edition already reads. The TeX "
    "keeps the printed reading.",
    corrected=r"(\hyperref[II.3.1.4-fr]{3.1.4})", nofix=True)
c2(51, "after (3.1.7): 'au sens de (0, 5.5.2)'", "0, 5.5.2")
c2(51, "after (3.1.7): 'A[T]/(gT−1)A[T] (0, 1.2.3)'", "0, 1.2.3")

# ---------------------------------------------------------------- page 52
add(52, "Proposition (3.1.8) (ii): 'somme directe de 𝒪_Y et des 𝒮_n (n⩾0)'",
    "(n⩾0)", r"($n\geq0$)", "misprint_in_print", None, "high", None, None,
    "As in (2.4.8), which the proof invokes, the degree-0 part is 𝒪_Y and 𝒮_n is taken for n>0; with n⩾0 the "
    "sum would contain 𝒮_0 as well. The TeX keeps the printed reading; the corrected edition already reads n>0.",
    corrected=r"($n>0$)", nofix=True)
c2(52, "Proposition (3.1.8) (iii): '𝒪_Y-Module inversible (0, 5.4.1)'", "0, 5.4.1",
   old=r"(\hyperref[0.5.4.1-fr]{0, 5.4.1})", new=r"\textup{(\hyperref[0.5.4.1-fr]{\textbf{0}, 5.4.1})}",
   note="Bold 0. The same edit sets the reference upright (convention 6, next entry, fix null).")
c6ref(52, "Proposition (3.1.8) (iii): '(0, 5.4.1)' inside the italic statement", r"(\hyperref[0.5.4.1-fr]{0, 5.4.1})",
      nofix=True, note="Applied by the convention-2 edit of the previous entry, hence fix null.")
add(52, "proof of (3.1.8): 'x_n→x_n⊗c^{⊗n} est un A-isomorphisme'",
    "plain arrow x_n→x_n⊗c^{⊗n}", r"x_n\mapsto x_n\otimes c^{\otimes n}",
    "convention", 3, "high", r"x_n\mapsto x_n", r"x_n\to x_n", "Plain arrow in the print.")
add(52, "proof of (3.1.8): 'φ_c : S→S_{(L)}=⊕_{n⩾0}S_n⊗L^{⊗n}. Soit alors'",
    "formula set inline in the running text", r"displayed formula \[ … \]",
    "other", None, "high",
    r"graduées¶\[¶  \varphi_c:S\longrightarrow S_{(L)}¶  =\bigoplus_{n\geq0}S_n\otimes L^{\otimes n}.¶\]¶Soit alors",
    r"graduées¶$\varphi_c:S\to S_{(L)}¶=\bigoplus_{n\geq0}S_n\otimes L^{\otimes n}$.¶Soit alors",
    "Display in the TeX, inline in the print.")
add(52, "proof of (3.1.8): '(x⊗c^{nd})/(f⊗c^d)^n=(x⊗(εc)^{nd})/(f⊗(εc)^d)^n pour tout élément inversible'",
    "inline, slash fractions, exponents nd and d without ⊗: (x⊗c^{nd})/(f⊗c^d)^n=(x⊗(εc)^{nd})/(f⊗(εc)^d)^n",
    r"displayed \frac{x\otimes c^{\otimes nd}}{(f\otimes c^{\otimes d})^n}=\frac{x\otimes(\varepsilon c)^{\otimes nd}}{(f\otimes(\varepsilon c)^{\otimes d})^n}",
    "formula", None, "high",
    r"\[¶  \frac{x\otimes c^{\otimes nd}}{(f\otimes c^{\otimes d})^n}¶  =\frac{x\otimes(\varepsilon c)^{\otimes nd}}¶  {(f\otimes(\varepsilon c)^{\otimes d})^n}¶\]",
    r"$(x\otimes c^{nd})/(f\otimes c^d)^n¶=(x\otimes(\varepsilon c)^{nd})/(f\otimes(\varepsilon c)^d)^n$",
    "The print writes the powers of c without ⊗ here (as in (f⊗c^d) of the next line, which the TeX keeps) "
    "and sets the equation inline with slashes.")
add(52, "(3.1.9): 'Rappelons (0, 4.1.3 et I, 1.3.14) que'",
    "(0, 4.1.3 et I, 1.3.14) — one pair of parentheses; bold 0 and I",
    r"((\hyperref[0.4.1.3-fr]{0, 4.1.3}) et (\hyperref[I.1.3.14-fr]{I, 1.3.14}))",
    "punctuation", None, "high",
    r"((\hyperref[0.4.1.3-fr]{0, 4.1.3}) et¶(\hyperref[I.1.3.14-fr]{I, 1.3.14}))",
    r"(\hyperref[0.4.1.3-fr]{\textbf{0}, 4.1.3} et¶\hyperref[I.1.3.14-fr]{\textbf{I}, 1.3.14})",
    "The TeX has a pair of parentheses around each reference. This edit also makes the bold 0 and I of "
    "convention 2; the two convention entries for these references therefore carry fix null.")
c2(52, "(3.1.9): '(0, 4.1.3 et …)'", "0, 4.1.3", nofix=True,
   note="Bold 0; applied by the (3.1.9) parentheses fix (punctuation entry above), hence fix null.")
c2(52, "(3.1.9): '(… et I, 1.3.14)'", "I, 1.3.14", nofix=True,
   note="Bold I; applied by the (3.1.9) parentheses fix (punctuation entry above), hence fix null.")
c6ref(52, "Corollaire (3.1.11): 'Sous les hypothèses de (3.1.10), Proj(𝒮) est'",
      r"(\hyperref[II.3.1.10-fr]{3.1.10})")
F[-1]["fix"] = {"old": r"hypothèses de (\hyperref[II.3.1.10-fr]{3.1.10})",
                "new": r"hypothèses de \textup{(\hyperref[II.3.1.10-fr]{3.1.10})}"}
F[-1]["note"] = "Roman item inside an italic statement (the (3.1.10) of the following proof is in roman text)."
c2(52, "(3.1.12): 'on sait (I, 5.1.1) que son nilradical'", "I, 5.1.1",
   old=r"{I, 5.1.1}) que son", new=r"{\textbf{I}, 5.1.1}) que son")
c2(52, "(3.1.12): '(𝒮_+)_y=(𝒮_y)_+ (I, 5.1.1). On dit'", "I, 5.1.1",
   old=r"{I, 5.1.1}). On dit", new=r"{\textbf{I}, 5.1.1}). On dit")
add(52, "page end: 'ce qui équivaut' continues on p. 53 with 'à dire que'",
    "one sentence running across the page break", "blank line before \\oldpage[II]{53} (paragraph break)",
    "other", None, "high", r"ce qui équivaut¶¶", r"ce qui équivaut¶",
    "Spurious paragraph break at a mid-sentence page break (end of this page's segment).")

# ---------------------------------------------------------------- page 53
add(53, "page start: (3.1.12) continues 'à dire que 𝒮_y est …'",
    "one sentence running across the page break", "blank line after \\oldpage[II]{53} (paragraph break)",
    "other", None, "high", r"\oldpage[II]{53}¶¶à dire", r"\oldpage[II]{53}¶à dire",
    "Spurious paragraph break at a mid-sentence page break (the blank line before the marker is removed in the "
    "p. 52 entry).")
c2(53, "proof of (3.1.13): 'd'où la conclusion (I, 5.1.2)'", "I, 5.1.2")
c6ref(53, "Proposition (3.1.14) (i): 'Si 𝒮 est intègre (3.1.12), alors'", r"(\hyperref[II.3.1.12-fr]{3.1.12})")
c2(53, "proof of (3.1.14) (i): 'donc que X est irréductible (0, 2.1.4)'", "0, 2.1.4")
c2(53, "proof of (3.1.14) (i): 'où A est intègre (I, 5.1.4)'", "I, 5.1.4")
add(53, "proof of (3.1.14) (i): 'on a alors pour tout z∈Y, (a/1)(f/1)=0'",
    "'tout' printed italic", "'pour tout' upright",
    "convention", 6, "high", r"alors pour tout¶    $z\in Y$", r"alors pour \emph{tout}¶    $z\in Y$",
    "Printed italic word left upright.")
c2(53, "proof of (3.1.14) (ii): 'S lui-même est réduit (I, 5.1.1)'", "I, 5.1.1")
add(53, "page end: 'l'annulateur 𝔍 de S_+ dans A=S_0 est réduit' continues on p. 54 with 'à 0 (2.1.11)'",
    "one sentence running across the page break", "blank line before \\oldpage[II]{54} (paragraph break)",
    "other", None, "high", r"$A=S_0$ est réduit¶¶", r"$A=S_0$ est réduit¶",
    "Spurious paragraph break inside item (ii) of the proof at a mid-sentence page break (end of this page's "
    "segment).")

# ---------------------------------------------------------------- page 54
add(54, "page start: proof of (3.1.14) (ii) continues 'à 0 (2.1.11). Dans le cas contraire'",
    "one sentence running across the page break", "blank line after \\oldpage[II]{54} (paragraph break)",
    "other", None, "high", r"\oldpage[II]{54}¶¶    à $0$", r"\oldpage[II]{54}¶    à $0$",
    "Spurious paragraph break at a mid-sentence page break (the blank line before the marker is removed in the "
    "p. 53 entry).")
c2(54, "(3.2.1): 'ce qui revient au même (I, 9.6.1)'", "I, 9.6.1")
add(54, "(3.2.1): 'le 𝒪_{X_U}-Module quasi-cohérent (Γ(U, ℳ))~;'",
    "(Γ(U, ℳ))~ — tilde after the parenthesised expression", r"\widetilde{\Gamma(U,\mathcal{M})}",
    "convention", 5, "high", r"$\widetilde{\Gamma(U,\mathcal{M})}$~;", r"$(\Gamma(U,\mathcal{M}))\supertilde$~;",
    "Printed with outer parentheses and a following tilde.")
c2(54, "(3.2.1): 'Γ(U, ℳ)⊗_A A' (I, 1.6.4)'", "I, 1.6.4")
add(54, "Proposition (3.2.2): 'on ait η^*_U((Γ(U, ℳ))~)=ℳ̃|f^{-1}(U) (en désignant …'",
    "formula set inline in the running text", r"displayed formula \[ … \]",
    "other", None, "high",
    r"on ait¶\[¶  \eta_U^*(\widetilde{\Gamma(U,\mathcal{M})})¶  =\widetilde{\mathcal{M}}|f^{-1}(U)¶\]¶(en",
    r"on ait¶$\eta_U^*((\Gamma(U,\mathcal{M}))\supertilde)¶=\widetilde{\mathcal{M}}|f^{-1}(U)$¶(en",
    "Display in the TeX, inline in the print. This edit also makes the convention-5 tilde (Γ(U, ℳ))~ of the "
    "same formula; the convention entry for it carries fix null.")
add(54, "Proposition (3.2.2): 'η^*_U((Γ(U, ℳ))~)'",
    "(Γ(U, ℳ))~ — tilde after the parenthesised expression", r"\eta_U^*(\widetilde{\Gamma(U,\mathcal{M})})",
    "convention", 5, "high", None, None,
    "Applied by the display-to-inline fix of (3.2.2) (entry above), hence fix null.", nofix=True)
c2(54, "proof of (3.2.2): 'principe de recollement des faisceaux (0, 3.3.1)'", "0, 3.3.1")
c6ref(54, "Proposition (3.2.3): 'Z_f=Spec(𝒮^{(d)}/(f−1)𝒮^{(d)}) (3.1.4),'", r"(\hyperref[II.3.1.4-fr]{3.1.4})")
c6ref(54, "Proposition (3.2.3), end of statement: '(…)~ (1.4.3).'", r"(\hyperref[II.1.4.3-fr]{1.4.3})")
add(54, "Proposition (3.2.3): 'est le 𝒪_{Z_f}-Module (ℳ^{(l)}/(f−1)ℳ^{(d)})~ (1.4.3)'",
    "(…)~ — tilde after the parenthesised expression",
    r"\widetilde{\mathcal{M}^{(d)}/(f-1)\mathcal{M}^{(d)}}",
    "convention", 5, "high",
    r"$\widetilde{\mathcal{M}^{(d)}/(f-1)\mathcal{M}^{(d)}}$",
    r"$(\mathcal{M}^{(d)}/(f-1)\mathcal{M}^{(d)})\supertilde$",
    "Printed with outer parentheses and a following tilde. Apply before the ℳ^{(l)} misprint entry below "
    "(this 'old' contains its text).")
add(54, "Proposition (3.2.3): first numerator 'ℳ^{(l)}' in (ℳ^{(l)}/(f−1)ℳ^{(d)})~",
    "ℳ^{(l)} — the superscript is an italic l, not d (checked at 7× zoom)",
    r"\mathcal{M}^{(d)}", "misprint_in_print", None, "high",
    r"\mathcal{M}^{(d)}/", r"\mathcal{M}^{(l)}/",
    "Wrong letter (or wrong sort) in the print; the statement concerns ℳ^{(d)}/(f−1)ℳ^{(d)} (cf. 3.1.4, 2.2.5). "
    "The TeX silently corrects it; the fix restores the printed reading. Apply after the convention-5 entry above.",
    corrected=r"\mathcal{M}^{(d)}/(f-1)\mathcal{M}^{(d)}")
c2(54, "proof of (3.2.4): 'se ramène à (I, 1.3.11 et 1.3.9)'", "I, 1.3.11")
add(54, "proof of (3.2.4): '(I, 1.3.11 et 1.3.9)'",
    "second reference printed '1.3.9' without 'I,'", r"\hyperref[I.1.3.9-fr]{I, 1.3.9}",
    "extra", None, "high", r"{I, 1.3.9}", r"{1.3.9}",
    "The TeX repeats the chapter numeral that the print gives once for both references.")
add(54, "(3.2.4.1): left side '(ℐℳ)~'",
    "(ℐℳ)~ — tilde after the parenthesised expression", r"\widetilde{\mathcal{I}\mathcal{M}}",
    "convention", 5, "high", r"\widetilde{\mathcal{I}\mathcal{M}}", r"(\mathcal{I}\mathcal{M})\supertilde",
    "Printed with parentheses and a following tilde.")
add(54, "(3.2.4.1): right side 'ℐ.ℳ̃'",
    "baseline dot ℐ.ℳ̃", r"\mathcal{I}\cdot\widetilde{\mathcal{M}} (centred dot)",
    "symbol", None, "high", r"\mathcal{I}\cdot", r"\mathcal{I}.",
    "The print has a full stop on the baseline (notation of 0, 4.3.5), not a centred dot.")
c2(54, "after (3.2.4.1): 'le sens défini en (0, 4.3.5)'", "0, 4.3.5")
add(54, "page end: 'ℳ=M̃,' continues on p. 55 with 'où M est un S-module gradué'",
    "one sentence running across the page break", "blank line before \\oldpage[II]{55} (paragraph break)",
    "other", None, "high", r"$\mathcal{M}=\widetilde{M}$,¶¶", r"$\mathcal{M}=\widetilde{M}$,¶",
    "Spurious paragraph break at a mid-sentence page break (end of this page's segment; the blank line after "
    "\\oldpage[II]{55} belongs to p. 55).")

# ---------------------------------------------------------------- checks
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def segments(path):
    t = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    seg = {}
    for i, (n, s) in enumerate(cuts):
        seg[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    return seg


rel, cur = segments(REL), segments(CUR)
ok = True
for p in range(50, 55):
    page = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = page.split("\n", 1)[1]
    if body.rstrip("\n") != rel[p].rstrip("\n"):
        print(f"p{p}: page file and release segment differ:")
        import difflib
        for ln in difflib.unified_diff(body.splitlines(), rel[p].splitlines(), lineterm="", n=0):
            print("   ", ln)
    if rel[p] != cur[p]:
        print(f"p{p}: diplomatic and current segments differ")
    sd, sc = rel[p], cur[p]
    for x in [f for f in F if f["page"] == p]:
        fx = x["fix"]
        if not fx:
            continue
        n0 = page.count(fx["old"])
        if n0 != 1:
            ok = False
            print(f"p{p} {x['where'][:50]}: old occurs {n0} times in page file")
        if sd.count(fx["old"]) != 1:
            ok = False
            print(f"p{p} {x['where'][:50]}: sequential diplomatic count {sd.count(fx['old'])}")
        else:
            sd = sd.replace(fx["old"], fx["new"])
        if x["kind"] != "misprint_in_print":
            if sc.count(fx["old"]) != 1:
                ok = False
                print(f"p{p} {x['where'][:50]}: sequential current count {sc.count(fx['old'])}")
            else:
                sc = sc.replace(fx["old"], fx["new"])
    (RUN / "crops_050_054" / f"p{p:03d}_after_fixes.tex").write_text(sd, encoding="utf-8")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
cnt = {}
for x in F:
    k = "convention" if x["kind"] == "convention" else ("misprint" if x["kind"] == "misprint_in_print" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("all checks passed" if ok else "CHECK FAILURES")
print(cnt)
