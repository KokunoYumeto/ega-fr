"""Build findings_055_059.json for EGA II pp. 55-59 and check every fix's "old" against its page_NNN.tex.
In the strings below, the character ¶ stands for a line break (LF)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_055_059.json"


def s(x):
    return None if x is None else x.replace("¶", "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": s(tex), "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if nofix else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- page 54 (end of segment) / page 55
L.append(F(55, "top of the page: 'où M est un S-module gradué, et ℐ=𝔍̃' (continuation of the sentence of p. 54)",
           "flush left, continues the sentence; no paragraph break",
           r"\oldpage[II]{55}¶¶où $M$ est", "other", None, "high",
           r"\oldpage[II]{55}¶¶où $M$ est", r"\oldpage[II]{55}¶où $M$ est",
           "Spurious paragraph break. The blank line before the marker (end of the p. 54 segment) is removed by the p. 54 entry of findings_050_054.json (already in FIXLOG.jsonl); this edit removes the one after it."))
L.append(F(55, "first line: 'ℐ=𝔍̃, où 𝔍 est un idéal de A'",
           "Fraktur capital 𝔍 (twice), the same glyph as 'h≠0 dans 𝔍' on p. 54 and as on p. 85",
           r"$\mathcal{I}=\widetilde{\mathfrak{I}}$, où $\mathfrak{I}$", "symbol", None, "medium",
           r"$\mathcal{I}=\widetilde{\mathfrak{I}}$, où $\mathfrak{I}$", r"$\mathcal{I}=\widetilde{\mathfrak{J}}$, où $\mathfrak{J}$",
           "Checked on a crop at 5x. The edition writes this printed Fraktur glyph as \\mathfrak{J} (p. 54, 98 times in ega2-1-fr.tex, all of EGA I after the p. 120 fix); \\mathfrak{I} renders as a different letter. The script letter here is the print's script I (no descender, as for the ideal of 𝒪_Y on p. 54), so \\mathcal{I} stays."))
L.append(F(55, "line 3: '(𝔍M)_(f)=𝔍.M_(f)'",
           "same Fraktur glyph 𝔍 (twice)",
           r"$(\mathfrak{I}M)_{(f)}=\mathfrak{I}\cdot M_{(f)}$", "symbol", None, "medium",
           r"$(\mathfrak{I}M)_{(f)}=\mathfrak{I}", r"$(\mathfrak{J}M)_{(f)}=\mathfrak{J}",
           "Same letter as the previous finding; does not overlap the product-dot finding that follows."))
L.append(F(55, "line 3: '𝔍.M_(f)'",
           "product dot on the baseline (full-stop height): 𝔍.M_(f)",
           r"\mathfrak{I}\cdot M_{(f)}", "symbol", None, "high",
           r"\cdot M_{(f)}", r".M_{(f)}",
           "Checked on a crop: a full stop on the baseline, not a centred dot; same notation and same fix as ℐ.ℳ̃ in (3.2.4.1) on p. 54 (findings_050_054.json)."))
L.append(F(55, "line 4: 'vu (I, 1.3.13 et 1.6.9)'",
           "bold I", r"(\hyperref[I.1.3.13-fr]{I, 1.3.13} et", "convention", 2, "high",
           r"{I, 1.3.13}", r"{\textbf{I}, 1.3.13}", "Chapter numeral printed bold."))
L.append(F(55, "line 4: 'vu (I, 1.3.13 et 1.6.9)'",
           "'et 1.6.9': the chapter numeral is not repeated before 1.6.9",
           r"\hyperref[I.1.6.9-fr]{I, 1.6.9}", "extra", None, "high",
           r"\hyperref[I.1.6.9-fr]{I, 1.6.9}", r"\hyperref[I.1.6.9-fr]{1.6.9}",
           "The TeX adds 'I, ' to the second reference; the link target stays."))
L.append(F(55, "Proposition (3.2.5), first sentence: 'pour tout n∈Z. En particulier'",
           "the Z is a light roman capital, not the bold Z of the integers (the same statement ends with a bold 'n∈𝐙.')",
           r"$n\in\mathbf{Z}$. En particulier", "misprint_in_print", None, "high",
           r"$n\in\mathbf{Z}$. En particulier", r"$n\in\mathrm{Z}$. En particulier",
           "Font slip in the print, checked on a crop at 3x against the bold Z two lines below. The TeX silently corrects it; the fix restores the printed roman Z (\\mathrm keeps it upright; a plain $Z$ would follow the edition's treatment of upright capitals).",
           corrected=r"$n\in\mathbf{Z}$"))
L.append(F(55, "Proposition (3.2.5): 'le (𝒪_X|X_f)-Module (𝒮(nd))~|X_f'",
           "(𝒮(nd))~|X_f: tilde written after the closing parenthesis", r"$\widetilde{\mathcal{S}(nd)}|X_f$", "convention", 5, "high",
           r"$\widetilde{\mathcal{S}(nd)}|X_f$", r"$(\mathcal{S}(nd))\supertilde|X_f$",
           "The TeX also drops the printed parentheses."))
L.append(F(55, "Proposition (3.2.5): 'engendrée par 𝒮_1 (3.1.9), les 𝒪_X-Modules'",
           "reference (3.1.9) upright inside the italic statement", r"(\hyperref[II.3.1.9-fr]{3.1.9}), les", "convention", 6, "high",
           r"(\hyperref[II.3.1.9-fr]{3.1.9}), les", r"\textup{(\hyperref[II.3.1.9-fr]{3.1.9})}, les",
           "Checked on a crop."))
L.append(F(55, "Proposition (3.2.5): 'les 𝒪_X-Modules (𝒮(n))~ sont inversibles'",
           "(𝒮(n))~", r"$\widetilde{\mathcal{S}(n)}$ sont inversibles", "convention", 5, "high",
           r"$\widetilde{\mathcal{S}(n)}$ sont inversibles", r"$(\mathcal{S}(n))\supertilde$ sont inversibles",
           "The TeX also drops the printed parentheses."))
L.append(F(55, "proof of (3.2.5): 'un isomorphisme canonique de (𝒮(nd))~|(X_f∩φ⁻¹(U))'",
           "(𝒮(nd))~|(X_f∩φ⁻¹(U))", r"$\widetilde{\mathcal{S}(nd)}|(X_f\cap\varphi^{-1}(U))$", "convention", 5, "high",
           r"$\widetilde{\mathcal{S}(nd)}|(X_f", r"$(\mathcal{S}(nd))\supertilde|(X_f",
           "The TeX also drops the printed parentheses."))
L.append(F(55, "(3.2.5.1): '𝒪_X(n)=(𝒮(n))~'",
           "(𝒮(n))~", r"\mathcal{O}_X(n)=\widetilde{\mathcal{S}(n)}", "convention", 5, "high",
           r"\mathcal{O}_X(n)=\widetilde{\mathcal{S}(n)}", r"\mathcal{O}_X(n)=(\mathcal{S}(n))\supertilde",
           "The TeX also drops the printed parentheses."))
L.append(F(55, "display after (3.2.5.2): '((𝒮|U)(n))~=𝒪_X(n)|f⁻¹(U)'",
           "((𝒮|U)(n))~", r"\widetilde{(\mathcal{S}|U)(n)}", "convention", 5, "high",
           r"\widetilde{(\mathcal{S}|U)(n)}", r"((\mathcal{S}|U)(n))\supertilde",
           "The TeX also drops the outer printed parentheses."))
L.append(F(55, "(3.2.6.1): 'λ : M̃⊗_{𝒪_X}Ñ → (ℳ⊗_𝒮𝒩)~'",
           "(ℳ⊗_𝒮𝒩)~", r"\widetilde{\mathcal{M}\otimes_{\mathcal{S}}\mathcal{N}}", "convention", 5, "high",
           r"\widetilde{\mathcal{M}\otimes_{\mathcal{S}}\mathcal{N}}", r"(\mathcal{M}\otimes_{\mathcal{S}}\mathcal{N})\supertilde",
           "The TeX also drops the printed parentheses."))
L.append(F(55, "(3.2.6.2): 'μ : (ℋom_𝒮(ℳ, 𝒩))~ → ℋom_{𝒪_X}(M̃, Ñ)'",
           "(ℋom_𝒮(ℳ, 𝒩))~", r"\widetilde{\mathcal{H}om_{\mathcal{S}}(\mathcal{M},\mathcal{N})}", "convention", 5, "high",
           r"\widetilde{\mathcal{H}om_{\mathcal{S}}(\mathcal{M},\mathcal{N})}", r"(\mathcal{H}om_{\mathcal{S}}(\mathcal{M},\mathcal{N}))\supertilde",
           "The TeX also drops the printed parentheses."))
L.append(F(55, "Proposition (3.2.6), last sentence: 'engendrée par 𝒮_1 (3.1.9), λ est un isomorphisme'",
           "reference (3.1.9) upright inside the italic statement", r"(\hyperref[II.3.1.9-fr]{3.1.9}), $\lambda$", "convention", 6, "high",
           r"(\hyperref[II.3.1.9-fr]{3.1.9}), $\lambda$", r"\textup{(\hyperref[II.3.1.9-fr]{3.1.9})}, $\lambda$",
           "Checked on a crop."))
L.append(F(55, "Proposition (3.2.6), last sentence: 'une présentation finie (3.1.1), μ est un isomorphisme'",
           "reference (3.1.1) upright inside the italic statement", r"(\hyperref[II.3.1.1-fr]{3.1.1}), $\mu$", "convention", 6, "high",
           r"(\hyperref[II.3.1.1-fr]{3.1.1}), $\mu$", r"\textup{(\hyperref[II.3.1.1-fr]{3.1.1})}, $\mu$",
           "Checked on a crop."))
# ---------------------------------------------------------------- page 56
L.append(F(56, "Proposition (3.2.10): 'Proj(𝒮) (3.1.8, (iii)). Pour tout entier'",
           "reference (3.1.8, (iii)) upright inside the italic statement", r"(\hyperref[II.3.1.8-fr]{3.1.8, (iii)}). Pour", "convention", 6, "high",
           r"(\hyperref[II.3.1.8-fr]{3.1.8, (iii)}). Pour", r"\textup{(\hyperref[II.3.1.8-fr]{3.1.8, (iii)})}. Pour",
           "Checked on a crop."))
L.append(F(56, "Proposition (3.2.10): 'Pour tout entier n∈Z, g_*(...)'",
           "the Z is a light roman capital, not the bold Z (bold elsewhere on the page: (3.2.8), (3.2.9) (ii), (3.3.1.1))",
           r"entier $n\in\mathbf{Z}$", "misprint_in_print", None, "high",
           r"entier $n\in\mathbf{Z}$", r"entier $n\in\mathrm{Z}$",
           "Font slip in the print, checked on a crop at 2x; same slip as in (3.2.5) on p. 55. The TeX silently corrects it.",
           corrected=r"$n\in\mathbf{Z}$"))
L.append(F(56, "proof of (3.2.10): 'sur (S_(L)(n))_(f⊗c^d)'",
           "subscript (f⊗c^d): plain exponent d, no ⊗ in the exponent", r"(S_{(L)}(n))_{(f\otimes c^{\otimes d})}", "formula", None, "high",
           r"_{(f\otimes c^{\otimes d})}", r"_{(f\otimes c^d)}",
           "Checked on a crop at 4x. The print writes c^d, c^n, c^{n+kd}, c^d in this proof; the TeX adds ⊗ to all four exponents (four findings)."))
L.append(F(56, "proof of (3.2.10): 'en faisant correspondre à (x/f^k)⊗c^n'",
           "(x/f^k)⊗c^n: plain exponent n", r"$(x/f^k)\otimes c^{\otimes n}$", "formula", None, "high",
           r"(x/f^k)\otimes c^{\otimes n}", r"(x/f^k)\otimes c^n", "Checked on a crop."))
L.append(F(56, "proof of (3.2.10): 'où x∈S_{kd+n} l'élément'",
           "no comma after S_{kd+n} (the incidental clause opened by ', où' is not closed)",
           r"où $x\in S_{kd+n}$, l'élément", "misprint_in_print", None, "high",
           r"où $x\in S_{kd+n}$, l'élément", r"où $x\in S_{kd+n}$ l'élément",
           "Checked on a crop: no comma mid-line. The TeX silently supplies it; the diplomatic text keeps the printed punctuation.",
           corrected=r"où $x\in S_{kd+n}$, l'élément"))
L.append(F(56, "proof of (3.2.10): 'l'élément (x⊗c^{n+kd})/(f⊗c^d)^k'",
           "x⊗c^{n+kd}: plain exponent n+kd", r"(x\otimes c^{\otimes(n+kd)})", "formula", None, "high",
           r"c^{\otimes(n+kd)}", r"c^{n+kd}", "Checked on a crop."))
L.append(F(56, "proof of (3.2.10): 'l'élément (x⊗c^{n+kd})/(f⊗c^d)^k'",
           "(f⊗c^d)^k: plain exponent d", r"/(f\otimes c^{\otimes d})^k", "formula", None, "high",
           r"/(f\otimes c^{\otimes d})^k", r"/(f\otimes c^d)^k", "Checked on a crop."))
L.append(F(56, "3.3, opening sentence: 'On suppose dans tout ce numéro que ... engendrée par 𝒮_1 (3.1.9).'",
           "the italic sentence ends at 𝒮_1; the reference (3.1.9) is upright", r"$\mathcal{S}_1$¶(\hyperref[II.3.1.9-fr]{3.1.9}).}", "convention", 6, "high",
           r"$\mathcal{S}_1$¶(\hyperref[II.3.1.9-fr]{3.1.9}).}", r"$\mathcal{S}_1$}¶(\hyperref[II.3.1.9-fr]{3.1.9}).",
           "Checked on a crop. The \\emph is closed before the reference instead of adding \\textup."))
L.append(F(56, "(3.3.1.1): 'Γ_*(ℱ)=⊕_{n∈Z} p_*(ℱ(n))'",
           "bold Γ in Γ_*", r"\Gamma_*(\mathcal{F})", "font", None, "high",
           r"\Gamma_*(\mathcal{F})", r"\bbGamma_*(\mathcal{F})",
           "Checked on a crop at 3x. The bold Γ is notation, not decoration: (3.3.1.1) defines the graded 𝒪_Y-Module 𝚪_*(ℱ) with a bold Γ, while the graded S-module Γ_*(ℱ) of §2 (e.g. (2.6.4.2) on p. 38) and its use in the last line of the (3.3.4) chain on p. 58 are printed with the ordinary Γ. The TeX writes both as \\Gamma_*. \\bbGamma (=\\boldsymbol{\\Gamma}) is defined in preamble-base.tex and used for this functor in ega3-1-fr.tex."))
L.append(F(56, "end of the page: blank line after the (3.3.1.1) display, before \\oldpage[II]{57}",
           "the sentence continues on p. 57 ('et en particulier', flush left)", r"\tag{3.3.1.1}¶\]¶¶", "other", None, "high",
           r"\tag{3.3.1.1}¶\]¶¶", r"\tag{3.3.1.1}¶\]¶",
           "Spurious paragraph break at the page boundary; apply together with the p. 57 finding that removes the blank line after \\oldpage[II]{57}."))
# ---------------------------------------------------------------- page 57
L.append(F(57, "top of the page: 'et en particulier'",
           "flush left, continues the sentence of (3.3.1)", r"\oldpage[II]{57}¶¶et en particulier", "other", None, "high",
           r"\oldpage[II]{57}¶¶et en particulier", r"\oldpage[II]{57}¶et en particulier",
           "Spurious paragraph break; apply together with the p. 56 finding that removes the blank line before the marker."))
L.append(F(57, "(3.3.1.2): 'Γ_*(𝒪_X)=⊕ p_*(𝒪_X(n)).'",
           "bold Γ in Γ_*", r"  \Gamma_*(\mathcal{O}_X)¶  =\bigoplus", "font", None, "high",
           r"  \Gamma_*(\mathcal{O}_X)¶  =\bigoplus", r"  \bbGamma_*(\mathcal{O}_X)¶  =\bigoplus", "Checked on a crop."))
L.append(F(57, "after (3.3.1.2): 'On sait (0, 4.2.2) qu'il existe'",
           "new paragraph (first line indented)", r"\]¶On sait", "other", None, "high",
           r"\]¶On sait", r"\]¶¶On sait", "Missing paragraph break."))
L.append(F(57, "'On sait (0, 4.2.2)'", "bold 0", r"(\hyperref[0.4.2.2-fr]{0, 4.2.2})", "convention", 2, "high",
           r"{0, 4.2.2}", r"{\textbf{0}, 4.2.2}", "Chapter numeral printed bold."))
L.append(F(57, "'on déduit donc de (3.2.7.1) que Γ_*(𝒪_X) est muni'", "bold Γ in Γ_*",
           r"$\Gamma_*(\mathcal{O}_X)$ est muni", "font", None, "high",
           r"$\Gamma_*(\mathcal{O}_X)$ est muni", r"$\bbGamma_*(\mathcal{O}_X)$ est muni", "Checked on a crop."))
L.append(F(57, "'définit de même sur Γ_*(ℱ) une structure'", "bold Γ in Γ_*",
           r"$\Gamma_*(\mathcal{F})$ une structure", "font", None, "high",
           r"$\Gamma_*(\mathcal{F})$ une structure", r"$\bbGamma_*(\mathcal{F})$ une structure", "Checked on a crop."))
L.append(F(57, "'structure de Module gradué sur Γ_*(𝒪_X).'", "bold Γ in Γ_*",
           r"$\Gamma_*(\mathcal{O}_X)$.¶¶En vertu", "font", None, "high",
           r"$\Gamma_*(\mathcal{O}_X)$.¶¶En vertu", r"$\bbGamma_*(\mathcal{O}_X)$.¶¶En vertu", "Checked on a crop."))
L.append(F(57, "'du foncteur p_* (0, 4.2.1)'", "bold 0", r"(\hyperref[0.4.2.1-fr]{0, 4.2.1})", "convention", 2, "high",
           r"{0, 4.2.1}", r"{\textbf{0}, 4.2.1}", "Chapter numeral printed bold."))
L.append(F(57, "'(0, 4.2.1), Γ_*(ℱ) est un foncteur covariant'", "bold Γ in Γ_*",
           r"$\Gamma_*(\mathcal{F})$ est un foncteur", "font", None, "high",
           r"$\Gamma_*(\mathcal{F})$ est un foncteur", r"$\bbGamma_*(\mathcal{F})$ est un foncteur", "Checked on a crop."))
L.append(F(57, "'dans 𝒪_X, Γ_*(𝒥) s'identifie'", "bold Γ in Γ_*",
           r"$\Gamma_*(\mathcal{J})$", "font", None, "high",
           r"$\Gamma_*(\mathcal{J})$", r"$\bbGamma_*(\mathcal{J})$", "Checked on a crop."))
L.append(F(57, "end of (3.3.1): 'faisceau gradué d'idéaux de Γ_*(𝒪_X).'", "bold Γ in Γ_*",
           r"de $\Gamma_*(\mathcal{O}_X)$.¶\end{env}", "font", None, "high",
           r"de $\Gamma_*(\mathcal{O}_X)$.¶\end{env}", r"de $\bbGamma_*(\mathcal{O}_X)$.¶\end{env}", "Checked on a crop."))
L.append(F(57, "after (3.3.2.1): 'Appliquant ce résultat à chacun des ℳ_n'",
           "new paragraph (first line indented)", r"\]¶Appliquant", "other", None, "high",
           r"\]¶Appliquant", r"\]¶¶Appliquant", "Missing paragraph break."))
L.append(F(57, "(3.3.2.3): 'α : ℳ → Γ_*(M̃)'", "bold Γ in Γ_*",
           r"\alpha:\mathcal{M}\longrightarrow\Gamma_*(\widetilde{\mathcal{M}})", "font", None, "high",
           r"\alpha:\mathcal{M}\longrightarrow\Gamma_*(\widetilde{\mathcal{M}})", r"\alpha:\mathcal{M}\longrightarrow\bbGamma_*(\widetilde{\mathcal{M}})", "Checked on a crop."))
L.append(F(57, "'on vérifie que α : 𝒮 → Γ_*(𝒪_X) est un homomorphisme'", "bold Γ in Γ_*",
           r"$\alpha:\mathcal{S}\to\Gamma_*(\mathcal{O}_X)$", "font", None, "high",
           r"\alpha:\mathcal{S}\to\Gamma_*(\mathcal{O}_X)", r"\alpha:\mathcal{S}\to\bbGamma_*(\mathcal{O}_X)", "Checked on a crop."))
L.append(F(57, "'il correspond (0, 4.4.3) un homomorphisme canonique'", "bold 0", r"(\hyperref[0.4.4.3-fr]{0, 4.4.3})", "convention", 2, "high",
           r"{0, 4.4.3}", r"{\textbf{0}, 4.4.3}", "Chapter numeral printed bold."))
L.append(F(57, "after (3.3.2.4): 'On vérifie sans peine que cet homomorphisme'",
           "new paragraph (first line indented)", r"\]¶On vérifie sans peine", "other", None, "high",
           r"\]¶On vérifie sans peine", r"\]¶¶On vérifie sans peine", "Missing paragraph break."))
L.append(F(57, "before (3.3.2.5): '(de degré 0) de 𝒪_Y-Modules gradués'",
           "'gradués' in italics", r"(de degré $0$) de $\mathcal{O}_Y$-Modules gradués", "italics", None, "high",
           r"(de degré $0$) de $\mathcal{O}_Y$-Modules gradués", r"(de degré $0$) de $\mathcal{O}_Y$-Modules \emph{gradués}",
           "Checked on a crop: only the word 'gradués' (alone on its line) is italic."))
L.append(F(57, "end of the page: blank line after the (3.3.2.5) display, before \\oldpage[II]{58}",
           "the sentence continues on p. 58 ('où la graduation du second membre ...', flush left)", r"\tag{3.3.2.5}¶\]¶¶", "other", None, "high",
           r"\tag{3.3.2.5}¶\]¶¶", r"\tag{3.3.2.5}¶\]¶",
           "Spurious paragraph break at the page boundary; apply together with the p. 58 finding that removes the blank line after \\oldpage[II]{58}."))
# ---------------------------------------------------------------- page 58
L.append(F(58, "top of the page: 'où la graduation du second membre provient naturellement'",
           "flush left, continues the sentence of (3.3.2)", r"\oldpage[II]{58}¶¶où la graduation", "other", None, "high",
           r"\oldpage[II]{58}¶¶où la graduation", r"\oldpage[II]{58}¶où la graduation",
           "Spurious paragraph break; apply together with the p. 57 finding that removes the blank line before the marker."))
L.append(F(58, "'compte tenu de (I, 1.6.7)'", "bold I", r"(\hyperref[I.1.6.7-fr]{I, 1.6.7})", "convention", 2, "high",
           r"{I, 1.6.7}", r"{\textbf{I}, 1.6.7}", "Chapter numeral printed bold."))
L.append(F(58, "'correspond (I, 1.3.8) à l'homomorphisme'", "bold I", r"(\hyperref[I.1.3.8-fr]{I, 1.3.8})", "convention", 2, "high",
           r"{I, 1.3.8}", r"{\textbf{I}, 1.3.8}", "Chapter numeral printed bold."))
L.append(F(58, "'qui, à x⊗1 (x∈M_n) fait correspondre x/1'",
           "no comma after (x∈M_n) (the incidental 'à x⊗1 (x∈M_n)' opened by 'qui,' is not closed)",
           r"($x\in M_n$), fait", "misprint_in_print", None, "high",
           r"($x\in M_n$), fait", r"($x\in M_n$) fait",
           "Checked on a crop: the line ends with the closing parenthesis at the margin, no comma. The TeX silently supplies it.",
           corrected=r"($x\in M_n$), fait"))
L.append(F(58, "Proposition (3.3.3): 'ne s'annule pas (0, 5.5.2).'",
           "reference (0, 5.5.2) upright inside the italic statement", r"(\hyperref[0.5.5.2-fr]{0, 5.5.2})", "convention", 6, "high",
           r"(\hyperref[0.5.5.2-fr]{0, 5.5.2})", r"\textup{(\hyperref[0.5.5.2-fr]{0, 5.5.2})}",
           "Checked on a crop. Listed before the convention-2 fix of the same reference: apply this one first."))
L.append(F(58, "Proposition (3.3.3): '(0, 5.5.2)'", "bold 0", r"(\hyperref[0.5.5.2-fr]{0, 5.5.2})", "convention", 2, "high",
           r"{0, 5.5.2}", r"{\textbf{0}, 5.5.2}", "Chapter numeral printed bold. Apply after the convention-6 fix of the same reference (listed just before)."))
L.append(F(58, "proof of (3.3.3): 'au-dessus de X (0, 4.2.1))'", "bold 0", r"(\hyperref[0.4.2.1-fr]{0, 4.2.1}))", "convention", 2, "high",
           r"{0, 4.2.1}", r"{\textbf{0}, 4.2.1}", "Chapter numeral printed bold."))
L.append(F(58, "(3.3.4): 'par suite Γ_*(ℱ)=⊕ p_*(ℱ(n)) est aussi'", "bold Γ in Γ_*",
           r"$\Gamma_*(\mathcal{F})=\bigoplus_{n\in\mathbf{Z}}p_*(\mathcal{F}(n))$", "font", None, "high",
           r"$\Gamma_*(\mathcal{F})=\bigoplus", r"$\bbGamma_*(\mathcal{F})=\bigoplus", "Checked on a crop."))
L.append(F(58, "(3.3.4): 'quasi-cohérent (I, 1.4.1 et 1.3.9)'", "bold I", r"(\hyperref[I.1.4.1-fr]{I, 1.4.1} et", "convention", 2, "high",
           r"{I, 1.4.1}", r"{\textbf{I}, 1.4.1}", "Chapter numeral printed bold."))
L.append(F(58, "(3.3.4): 'quasi-cohérent (I, 1.4.1 et 1.3.9);'",
           "'et 1.3.9': the chapter numeral is not repeated", r"\hyperref[I.1.3.9-fr]{I, 1.3.9})~;", "extra", None, "high",
           r"\hyperref[I.1.3.9-fr]{I, 1.3.9})~;", r"\hyperref[I.1.3.9-fr]{1.3.9})~;",
           "The TeX adds 'I, ' to the second reference; the link target stays."))
L.append(F(58, "(3.3.4): 'si X est de type fini sur Y (I, 9.2.2)'", "bold I", r"(\hyperref[I.9.2.2-fr]{I, 9.2.2})", "convention", 2, "high",
           r"{I, 9.2.2}", r"{\textbf{I}, 9.2.2}", "Chapter numeral printed bold."))
L.append(F(58, "(3.3.4): 'On en conclut que (Γ_*(ℱ))~ est défini'", "bold Γ in Γ_*",
           r"$(\Gamma_*(\mathcal{F}))^{\sim}$ est défini", "font", None, "high",
           r"$(\Gamma_*(\mathcal{F}))^{\sim}$ est défini", r"$(\bbGamma_*(\mathcal{F}))^{\sim}$ est défini", "Checked on a crop."))
L.append(F(58, "(3.3.4): 'Pour tout ouvert affine U de Y, on a ((I, 1.3.9) et (2.5.4))'",
           "each reference has its own parentheses inside the outer pair: ((I, 1.3.9) et (2.5.4))",
           r"a (\hyperref[I.1.3.9-fr]{I, 1.3.9} et¶\hyperref[II.2.5.4-fr]{2.5.4})", "punctuation", None, "high",
           r"a (\hyperref[I.1.3.9-fr]{I, 1.3.9} et¶\hyperref[II.2.5.4-fr]{2.5.4})",
           r"a ((\hyperref[I.1.3.9-fr]{I, 1.3.9}) et¶(\hyperref[II.2.5.4-fr]{2.5.4}))",
           "Checked on a crop. Listed before the convention-2 fix of the same reference: apply this one first (the convention-2 'old' survives this edit, not the reverse)."))
L.append(F(58, "(3.3.4): 'on a ((I, 1.3.9) et (2.5.4))'", "bold I", r"(\hyperref[I.1.3.9-fr]{I, 1.3.9} et", "convention", 2, "high",
           r"(\hyperref[I.1.3.9-fr]{I, 1.3.9}", r"(\hyperref[I.1.3.9-fr]{\textbf{I}, 1.3.9}",
           "Chapter numeral printed bold. Apply after the punctuation fix just above."))
L.append(F(58, "(3.3.4.1): 'β : (Γ_*(ℱ))~ → ℱ'", "bold Γ in Γ_*",
           r"\beta:(\Gamma_*(\mathcal{F}))^{\sim}\longrightarrow\mathcal{F}", "font", None, "high",
           r"\beta:(\Gamma_*(\mathcal{F}))^{\sim}", r"\beta:(\bbGamma_*(\mathcal{F}))^{\sim}", "Checked on a crop."))
L.append(F(58, "(3.3.5.1): 'M̃ → (Γ_*(M̃))~ → M̃'", "bold Γ in Γ_*",
           r"(\Gamma_*(\widetilde{\mathcal{M}}))^{\sim}", "font", None, "high",
           r"(\Gamma_*(\widetilde{\mathcal{M}}))^{\sim}", r"(\bbGamma_*(\widetilde{\mathcal{M}}))^{\sim}", "Checked on a crop."))
L.append(F(58, "(3.3.5.2): 'Γ_*(ℱ) → Γ_*((Γ_*(ℱ))~) → Γ_*(ℱ)', arrow label Γ_*(β)",
           "bold Γ in all five Γ_*, including the arrow label",
           r"  \Gamma_*(\mathcal{F})\xrightarrow{\alpha}¶  \Gamma_*((\Gamma_*(\mathcal{F}))^{\sim})¶  \xrightarrow{\Gamma_*(\beta)}\Gamma_*(\mathcal{F})",
           "font", None, "high",
           r"  \Gamma_*(\mathcal{F})\xrightarrow{\alpha}¶  \Gamma_*((\Gamma_*(\mathcal{F}))^{\sim})¶  \xrightarrow{\Gamma_*(\beta)}\Gamma_*(\mathcal{F})",
           r"  \bbGamma_*(\mathcal{F})\xrightarrow{\alpha}¶  \bbGamma_*((\bbGamma_*(\mathcal{F}))^{\sim})¶  \xrightarrow{\bbGamma_*(\beta)}\bbGamma_*(\mathcal{F})",
           "Checked on a crop at 2.5x; five occurrences in one edit."))
L.append(F(58, "end of page_058.tex: heading '3.4. Conditions de finitude.'",
           "printed p. 58 ends with '... on est ramené à (2.6.5).'; the heading 3.4 is the first line of p. 59",
           r"\subsection{Conditions de finitude.}¶\label{subsection:II.3.4-fr}¶¶\oldpage[II]{59}", "marker", None, "high",
           r"\subsection{Conditions de finitude.}¶\label{subsection:II.3.4-fr}¶¶", "",
           "Two-part move: this edit deletes the heading from the end of the p. 58 segment; the p. 59 finding re-inserts it after \\oldpage[II]{59}. Apply both or neither."))
# ---------------------------------------------------------------- page 59
L.append(F(59, "start of page_059.tex: heading '3.4. Conditions de finitude.'",
           "p. 59 begins with the heading", r"\oldpage[II]{59}¶¶\begin{proposition}[3.4.1]", "marker", None, "high",
           r"\oldpage[II]{59}¶¶\begin{proposition}[3.4.1]",
           r"\oldpage[II]{59}¶¶\subsection{Conditions de finitude.}¶\label{subsection:II.3.4-fr}¶¶\begin{proposition}[3.4.1]",
           "Second half of the move begun by the p. 58 marker finding. Apply both or neither."))
L.append(F(59, "Proposition (3.4.1): 'engendrée par 𝒮_1 (3.1.9); on suppose'",
           "reference (3.1.9) upright inside the italic statement", r"(\hyperref[II.3.1.9-fr]{3.1.9})~;", "convention", 6, "high",
           r"(\hyperref[II.3.1.9-fr]{3.1.9})~;", r"\textup{(\hyperref[II.3.1.9-fr]{3.1.9})}~;", "Checked on a crop."))
L.append(F(59, "proof of (3.4.1): '(I, 1.3.9 et 1.3.12)'", "bold I", r"(\hyperref[I.1.3.9-fr]{I, 1.3.9} et", "convention", 2, "high",
           r"{I, 1.3.9} et", r"{\textbf{I}, 1.3.9} et", "Chapter numeral printed bold."))
L.append(F(59, "proof of (3.4.1): '(I, 1.3.9 et 1.3.12)'",
           "'et 1.3.12': the chapter numeral is not repeated", r"\hyperref[I.1.3.12-fr]{I, 1.3.12}", "extra", None, "high",
           r"\hyperref[I.1.3.12-fr]{I, 1.3.12}", r"\hyperref[I.1.3.12-fr]{1.3.12}",
           "The TeX adds 'I, ' to the second reference; the link target stays."))
L.append(F(59, "(3.4.2): 'et compte tenu de (I, 1.3.9); lorsque u est'", "bold I", r"(\hyperref[I.1.3.9-fr]{I, 1.3.9})~; lorsque", "convention", 2, "high",
           r"{I, 1.3.9})~; lorsque", r"{\textbf{I}, 1.3.9})~; lorsque", "Chapter numeral printed bold."))
L.append(F(59, "(3.4.2), last line: 'on dit aussi que u est un (TN)-isomorphisme.'",
           "'isomorphisme' in roman (the earlier '(TN)-injectif', '-surjectif', '-bijectif' are italic)",
           r"(\textbf{TN})-\emph{isomorphisme}", "italics", None, "high",
           r"(\textbf{TN})-\emph{isomorphisme}", r"(\textbf{TN})-isomorphisme",
           "Checked on a crop at 2.5x. The print may have meant italics for the defined term, but the printed word is roman."))
L.append(F(59, "Proposition (3.4.3) (i): 'Si ℳ vérifie la condition (TF),'",
           "(TF) upright bold inside the italic statement", r"la condition (\textbf{TF})", "convention", 6, "high",
           r"la condition (\textbf{TF})", r"la condition \textup{(\textbf{TF})}",
           "Checked on a crop. In the italic environment \\textbf gives bold italic and italic parentheses."))
L.append(F(59, "Proposition (3.4.3) (ii): 'Supposons que ℳ vérifie (TF);'",
           "(TF) upright bold inside the italic statement", r"(\textbf{TF})~; pour que", "convention", 6, "high",
           r"(\textbf{TF})~; pour que", r"\textup{(\textbf{TF})}~; pour que", "Checked on a crop."))
L.append(F(59, "Proposition (3.4.3) (ii): 'il faut et il suffit que ℳ vérifie (TN).'",
           "(TN) upright bold inside the italic statement", r"vérifie (\textbf{TN}).", "convention", 6, "high",
           r"vérifie (\textbf{TN}).", r"vérifie \textup{(\textbf{TN})}.", "Checked on a crop."))
L.append(F(59, "Théorème (3.4.4): 'l'homomorphisme canonique β (3.3.4) est un isomorphisme'",
           "reference (3.3.4) upright inside the italic statement", r"$\beta$ (\hyperref[II.3.3.4-fr]{3.3.4})", "convention", 6, "high",
           r"$\beta$ (\hyperref[II.3.3.4-fr]{3.3.4})", r"$\beta$ \textup{(\hyperref[II.3.3.4-fr]{3.3.4})}", "Checked on a crop."))
L.append(F(59, "Corollaire (3.4.5): 'Sous les hypothèses de (3.4.4), tout'",
           "reference (3.4.4) upright inside the italic statement", r"(\hyperref[II.3.4.4-fr]{3.4.4})", "convention", 6, "high",
           r"(\hyperref[II.3.4.4-fr]{3.4.4})", r"\textup{(\hyperref[II.3.4.4-fr]{3.4.4})}", "Checked on a crop."))

# ---------------------------------------------------------------- checks
ok = True
for x in L:
    fx = x["fix"]
    if fx is None:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", x["page"], n, repr(fx["old"]))
    if "\r" in fx["old"] or "\r" in fx["new"]:
        ok = False
        print("CR in fix", x["page"], x["where"])
json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in range(54, 60):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("all unique" if ok else "PROBLEMS", len(L), "findings ->", OUT)
