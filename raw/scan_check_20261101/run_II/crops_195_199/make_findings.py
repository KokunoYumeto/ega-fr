# Builds findings_195_199.json and checks that every fix's "old" occurs exactly once
# in its page_NNN.tex (read with universal newlines, i.e. LF).
import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = os.path.join(RUN, "findings_195_199.json")
NL = "<NL>"

def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}

def F(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

PROJ = r"\mathcal{P}\mathit{roj}"
PNOTE = ("Script 𝒫roj (script P, italic roj) in the print: the sheaf 𝒫roj/𝒫roj_0 of a graded Module, "
         "distinct from the roman Proj of the scheme Proj(𝒮). Document-wide in ega2-1 (see final report).")
ZNOTE = "Bold upright z in the print (the homogenising indeterminate). Document-wide in ega2-1 (see final report)."
GNOTE = "Bold Γ in Γ_* (graded 𝒪_Y-Module of 8.14.5.2); \\bbGamma as on pp. 56-58."

f = []

# ---------------- page 195 ----------------
f.append(F(195, "proof of (8.12.8): p_X^*(𝒫roj_0(ℳ_X^≥)) → (ℳ_X^≥)^□|E_X",
    "(ℳ_X^≥)^□|E_X — E without hat", r"(\mathcal{M}_X^{\geq})^{\square}|\widehat{E}_X",
    "misprint_in_print", None, "high",
    fx(r"|\widehat{E}_X$", r"|E_X$"),
    "Checked on a 2.5x crop: no hat on E (the hats of Ĉ on the same page are clear). The TeX silently corrects the print; the fix restores the printed reading. Correct reading Ê_X: p_X is defined on Ê_X (8.6.3: p_X : Ê_X → X'), and the reduction uses (8.12.6.1), whose target is (ℳ_X^≥)^□|Ê_X.",
    r"(\mathcal{M}_X^{\geq})^{\square}|\widehat{E}_X"))
f.append(F(195, "proof of (8.12.8): p_X^*(𝒫roj_0(ℳ_X^≥))", "script 𝒫roj_0", r"\operatorname{Proj}_0",
    "font", None, "high", fx(r"p_X^*(\operatorname{Proj}_0", r"p_X^*(" + PROJ + "_0"),
    "Checked on a crop. " + PNOTE + " Proj(𝒮^♮) later on this page is roman and correct."))
f.append(F(195, "(8.12.10.1): 𝒫roj_0(ℳ^♮) ⥲ ℳ̃_X", "script 𝒫roj_0", r"\operatorname{Proj}_0",
    "font", None, "high",
    fx(r"\operatorname{Proj}_0(\mathcal{M}^{\natural})", PROJ + r"_0(\mathcal{M}^{\natural})"), PNOTE))
f.append(F(195, "(8.13.1): 'est un 𝒪_Ĉ-Module quasi-cohérent (I, 9.4.2)'", "quasi-cohérent in italics",
    "quasi-cohérent upright", "italics", None, "high",
    fx(r"Module quasi-cohérent<NL>(", r"Module \emph{quasi-cohérent}<NL>("),
    "Checked on a crop. Independent of the convention-2 edit of the same reference."))
f.append(F(195, "(8.13.1): (I, 9.4.2)", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 9.4.2}", r"{\textbf{I}, 9.4.2}"), ""))
f.append(F(195, "(8.13.2): 'Désignons par 𝒩'_n ..., qui est un sous-𝒮-Module quasi-cohérent de ⊕_{i≤n} ℳ_i'",
    "sous-𝒮-Module (script S)", r"sous-$\mathcal{O}_Y$-Module", "misprint_in_print", None, "high",
    fx(r"qui est un sous-$\mathcal{O}_Y$-Module", r"qui est un sous-$\mathcal{S}$-Module"),
    "Checked on a crop: script 𝒮. The TeX silently corrects the print; the fix restores the printed reading. ⊕_{i≤n} ℳ_i is not an 𝒮-Module (not stable under 𝒮_1), and 𝒩'_n, the inverse image of 𝒩 under an 𝒪_Y-linear map into ℳ, is a sub-𝒪_Y-Module: correct reading sous-𝒪_Y-Module (the TeX's).",
    r"qui est un sous-$\mathcal{O}_Y$-Module"))
f.append(F(195, "(8.13.2): ℳ̂ = ℳ[z]", "bold z", "z", "font", None, "high",
    fx(r"\mathcal{M}[z]", r"\mathcal{M}[\mathbf{z}]"), "Checked on a crop. " + ZNOTE))
f.append(F(195, "(8.13.2): Σ_{i≤n} s_i z^{n−i}", "bold z", "z", "font", None, "high",
    fx(r"s_i z^{n-i}", r"s_i \mathbf{z}^{n-i}"), ZNOTE))
f.append(F(195, "(8.13.2): « variable homogénéisante » z", "bold z", "z", "font", None, "high",
    fx(r"homogénéisante~» $z$", r"homogénéisante~» $\mathbf{z}$"), ZNOTE))
f.append(F(195, "page break 195/196 inside the sentence 'On notera | que si 𝒩 est déjà ...'",
    "p. 196 continues the sentence (no new paragraph)", r"blank line before \oldpage[II]{196}",
    "other", None, "high", fx("On notera<NL><NL>", "On notera<NL>"),
    "GLOBAL_ISSUES item 20. The blank line is the last line of this segment, before the page-196 marker."))

# ---------------- page 196 ----------------
f.append(F(196, "(8.13.2), end: 𝒩̂ = 𝒩[z]", "bold z", "z", "font", None, "high",
    fx(r"\mathcal{N}[z]", r"\mathcal{N}[\mathbf{z}]"), ZNOTE))
f.append(F(196, "Proposition (8.13.3): 'Le 𝒪_Ĉ-Module 𝒫roj_0(𝒩̄) est le prolongement canonique'",
    "script 𝒫roj_0", r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\operatorname{Proj}_0(\overline{\mathcal{N}})$ est le", PROJ + r"_0(\overline{\mathcal{N}})$ est le"), PNOTE))
f.append(F(196, "proof of (8.13.3): (I, 9.4.1)", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 9.4.1}", r"{\textbf{I}, 9.4.1}"), ""))
f.append(F(196, "proof of (8.13.3): 'ouverts affines Ĉ_z = C'", "subscript bold z", "\\widehat{C}_z",
    "font", None, "high", fx(r"\widehat{C}_z=C", r"\widehat{C}_{\mathbf{z}}=C"), "Checked on a crop. " + ZNOTE))
f.append(F(196, "proof of (8.13.3), 1°: 'la restriction de 𝒫roj_0(𝒩̄) à C est 𝒩̃'", "script 𝒫roj_0",
    r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\operatorname{Proj}_0(\overline{\mathcal{N}})$ à $C$", PROJ + r"_0(\overline{\mathcal{N}})$ à $C$"), PNOTE))
f.append(F(196, "proof of (8.13.3), 2°: 'la restriction de 𝒫roj_0(𝒩̄) à chaque Ĉ_f'", "script 𝒫roj_0",
    r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\operatorname{Proj}_0(\overline{\mathcal{N}})$ à chaque", PROJ + r"_0(\overline{\mathcal{N}})$ à chaque"), PNOTE))
f.append(F(196, "proof of (8.13.3): '𝒫roj_0(𝒩̄)|C s'identifie à'", "script 𝒫roj_0", r"\operatorname{Proj}_0",
    "font", None, "high",
    fx(r"\operatorname{Proj}_0(\overline{\mathcal{N}})|C$", PROJ + r"_0(\overline{\mathcal{N}})|C$"), PNOTE))
f.append(F(196, "proof of (8.13.3): (N̄_(z))~", "bold z in the subscript", "z", "font", None, "high",
    fx(r"(\overline{N}_{(z)})^{\sim}", r"(\overline{N}_{(\mathbf{z})})^{\sim}"), "Checked on a crop. " + ZNOTE))
f.append(F(196, "proof of (8.13.3): 'or N̄_(z) s'identifie'", "bold z in the subscript", "z", "font", None, "high",
    fx(r"or $\overline{N}_{(z)}$", r"or $\overline{N}_{(\mathbf{z})}$"), ZNOTE))
f.append(F(196, "proof of (8.13.3): M̂/(z — 1)M̂", "bold z", "z", "font", None, "high",
    fx(r"\widehat{M}/(z-1)", r"\widehat{M}/(\mathbf{z}-1)"),
    "Checked on a crop. " + ZNOTE + " The minus is the print's 38 px dash (GLOBAL_ISSUES item 23), left as it is here."))
f.append(F(196, "proof of (8.13.3), second point: 'l'injection i : C∩Ĉ_f → Ĉ correspond à l'injection canonique S_f^≤ → S_f'",
    "i : C∩Ĉ_f → Ĉ (target without f)", r"i:C\cap\widehat{C}_f\to\widehat{C}_f",
    "misprint_in_print", None, "high",
    fx(r"\to\widehat{C}_f$ correspond", r"\to\widehat{C}$ correspond"),
    "Checked on a 2.5x crop: target Ĉ, no subscript. The TeX silently corrects the print; the fix restores the printed reading. Correct reading Ĉ_f: by (8.3.2.6) the restriction C_f → Ĉ_f of i corresponds to the injection S_f^≤ → S_f.",
    r"$i:C\cap\widehat{C}_f\to\widehat{C}_f$"))
f.append(F(196, "proof of (8.13.3): (I, 9.4.2)", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 9.4.2}", r"{\textbf{I}, 9.4.2}"), ""))
f.append(F(196, "proof of (8.13.3): 'l'image réciproque de N_f par l'injection canonique'", "no comma after N_f",
    r"de $N_f$, par", "punctuation", None, "high", fx(r"de $N_f$, par", r"de $N_f$ par"), "Checked on a crop."))
f.append(F(196, "proof of (8.13.3): Σ_{k≤md} x_k z^{md−k}/f^m", "bold z", "z", "font", None, "high",
    fx(r"x_kz^{md-k}", r"x_k\mathbf{z}^{md-k}"), ZNOTE))
f.append(F(196, "Remarques (8.13.4) (i): (I, 9.5.10)", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 9.5.10}", r"{\textbf{I}, 9.5.10}"), ""))
f.append(F(196, "Remarques (8.13.4) (i): Ŝ = 𝒮[z]", "bold z", "z", "font", None, "high",
    fx(r"\mathcal{S}[z]", r"\mathcal{S}[\mathbf{z}]"), ZNOTE))
f.append(F(196, "Remarques (8.13.4) (ii): h(x, k) = z^k Σ x_i z^{d(x)−i}", "bold z (twice)", "z", "font", None, "high",
    fx(r"h(x,k)=z^k\sum_{i\leqslant d(x)}x_i z^{d(x)-i}", r"h(x,k)=\mathbf{z}^k\sum_{i\leqslant d(x)}x_i \mathbf{z}^{d(x)-i}"),
    "Checked on a crop. " + ZNOTE))
f.append(F(196, "Remarques (8.13.4) (ii): Ŝ = S[z]", "bold z", "z", "font", None, "high",
    fx(r"\widehat{S}=S[z]", r"\widehat{S}=S[\mathbf{z}]"), ZNOTE))
f.append(F(196, "Remarques (8.13.4) (ii), display h(x, 0) = Σ x_i z^{d(x)−i}.", "bold z", "z", "font", None, "high",
    fx(r"x_i z^{d(x)-i}.", r"x_i \mathbf{z}^{d(x)-i}."), "Checked on a crop. " + ZNOTE))
f.append(F(196, "page break 196/197 after the display h(x, 0) = ...; p. 197 begins 'On dit que h(x, 0) ...'",
    "'On dit que' continues the paragraph (flush left like the following lines, no indent)",
    r"blank line between \] and \oldpage[II]{197}", "other", None, "medium",
    fx(r"  \]<NL><NL>", r"  \]<NL>"),
    "Checked on page_197_s1.png. GLOBAL_ISSUES item 20. The blank line is the last line of this segment."))

# ---------------- page 197 ----------------
f.append(F(197, "Remarques (8.13.4) (ii), end: « variable homogénéisante » z", "bold z", "z", "font", None, "high",
    fx(r"homogénéisante~» $z$", r"homogénéisante~» $\mathbf{z}$"), ZNOTE))
f.append(F(197, "(8.14.1): 'quasi-cohérente à degrés positifs'", "'à degrés positifs' all italic (italic à)",
    r"à \emph{degrés positifs}", "italics", None, "high",
    fx(r"à \emph{degrés positifs}", r"\emph{à degrés positifs}"), "Checked on a 2x crop: single-storey italic à."))
f.append(F(197, "(8.14.1): 'un foncteur ℳ_X = 𝒫roj(ℳ) en ℳ'", "script 𝒫roj", r"\operatorname{Proj}",
    "font", None, "high",
    fx(r"\mathcal{M}_X=\operatorname{Proj}(\mathcal{M})", r"\mathcal{M}_X=" + PROJ + r"(\mathcal{M})"),
    "Checked on a crop. " + PNOTE + " X = Proj(𝒮) two lines above is roman (correct)."))
f.append(F(197, "(8.14.1.1): 𝒫roj(ℳ(n)) = (𝒫roj(ℳ))(n)", "script 𝒫roj (twice)", r"\operatorname{Proj}",
    "font", None, "high",
    fx(r"\operatorname{Proj}(\mathcal{M}(n))<NL>  =(\operatorname{Proj}(\mathcal{M}))(n)",
       PROJ + r"(\mathcal{M}(n))<NL>  =(" + PROJ + r"(\mathcal{M}))(n)"), PNOTE))
f.append(F(197, "(8.14.2): 'aux 𝒮_X-Modules de la forme 𝒫roj(ℳ)'", "script 𝒫roj", r"\operatorname{Proj}",
    "font", None, "high", fx(r"$\operatorname{Proj}(\mathcal{M})$ les", "$" + PROJ + r"(\mathcal{M})$ les"), PNOTE))
f.append(F(197, "(8.14.2.1)", "script 𝒫roj_0 (three times)", r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\lambda_{mn}:\operatorname{Proj}_0(\mathcal{M}(m))<NL>  \otimes_{\mathcal{O}_X}\operatorname{Proj}_0(\mathcal{N}(n))<NL>  \to\operatorname{Proj}_0",
       r"\lambda_{mn}:" + PROJ + r"_0(\mathcal{M}(m))<NL>  \otimes_{\mathcal{O}_X}" + PROJ + r"_0(\mathcal{N}(n))<NL>  \to" + PROJ + "_0"),
    PNOTE))
f.append(F(197, "(8.14.2.2), source", "script 𝒫roj_0", r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\mu_{mn}:\operatorname{Proj}_0", r"\mu_{mn}:" + PROJ + "_0"),
    PNOTE + " The minus in (n—m) is the print's 38 px dash (GLOBAL_ISSUES item 23), left as it is."))
f.append(F(197, "(8.14.2.2), target", "script 𝒫roj_0 (twice)", r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"(\operatorname{Proj}_0(\mathcal{M}(m)),<NL>   \operatorname{Proj}_0(\mathcal{N}(n)))",
       "(" + PROJ + r"_0(\mathcal{M}(m)),<NL>   " + PROJ + r"_0(\mathcal{N}(n)))"), PNOTE))
f.append(F(197, "display μ_k, source", "script 𝒫roj_0", r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\mu_k:\operatorname{Proj}_0", r"\mu_k:" + PROJ + "_0"), PNOTE))
f.append(F(197, "display μ_k, target (ℋom_{𝒮_X}(𝒫roj(ℳ), 𝒫roj(𝒩)))_k", "script 𝒫roj (twice)",
    r"\operatorname{Proj}", "font", None, "high",
    fx(r"(\operatorname{Proj}(\mathcal{M}),\operatorname{Proj}(\mathcal{N})))_k",
       "(" + PROJ + r"(\mathcal{M})," + PROJ + r"(\mathcal{N})))_k"), PNOTE))
f.append(F(197, "'à tout u ∈ Γ(U, 𝒫roj_0((ℋom_𝒮(ℳ, 𝒩))(k)))'", "script 𝒫roj_0", r"\operatorname{Proj}_0",
    "font", None, "high", fx(r"u\in\Gamma(U,\operatorname{Proj}_0", r"u\in\Gamma(U," + PROJ + "_0"), PNOTE))
f.append(F(197, "'Γ(U, 𝒫roj(ℳ)) → Γ(U, 𝒫roj(𝒩))'", "script 𝒫roj (twice)", r"\operatorname{Proj}",
    "font", None, "high",
    fx(r"\Gamma(U,\operatorname{Proj}(\mathcal{M}))\to<NL>\Gamma(U,\operatorname{Proj}(\mathcal{N}))",
       r"\Gamma(U," + PROJ + r"(\mathcal{M}))\to<NL>\Gamma(U," + PROJ + r"(\mathcal{N}))"), PNOTE))
f.append(F(197, "'dans chaque Γ(U, 𝒫roj_0(ℳ(m)))'", "script 𝒫roj_0", r"\operatorname{Proj}_0", "font", None, "high",
    fx(r"\Gamma(U,\operatorname{Proj}_0(\mathcal{M}(m)))", r"\Gamma(U," + PROJ + r"_0(\mathcal{M}(m)))"), PNOTE))
f.append(F(197, "before (8.14.2.3): 'définissent un homomorphisme de 𝒮_X-Modules gradués'",
    "'Modules gradués' in italics", "upright", "italics", None, "high",
    fx(r"définissent un homomorphisme de $\mathcal{S}_X$-Modules gradués",
       r"définissent un homomorphisme de $\mathcal{S}_X$-\emph{Modules gradués}"), "Checked on a 2x crop."))
f.append(F(197, "(8.14.2.3), source 𝒫roj(ℋom_𝒮(ℳ, 𝒩))", "script 𝒫roj", r"\operatorname{Proj}", "font", None, "high",
    fx(r"\operatorname{Proj}<NL>  (\mathcal{H}om", PROJ + r"<NL>  (\mathcal{H}om"), PNOTE))
f.append(F(197, "(8.14.2.3), target ℋom_{𝒮_X}(𝒫roj(ℳ), 𝒫roj(𝒩)).", "script 𝒫roj (twice)", r"\operatorname{Proj}",
    "font", None, "high",
    fx(r"(\operatorname{Proj}(\mathcal{M}),\operatorname{Proj}(\mathcal{N})).",
       "(" + PROJ + r"(\mathcal{M})," + PROJ + r"(\mathcal{N}))."), PNOTE))
f.append(F(197, "before (8.14.2.4): 'donnent un homomorphisme de 𝒮_X-Modules gradués'",
    "'Modules gradués' in italics", "upright", "italics", None, "high",
    fx(r"donnent un homomorphisme de<NL>$\mathcal{S}_X$-Modules gradués",
       r"donnent un homomorphisme de<NL>$\mathcal{S}_X$-\emph{Modules gradués}"), "Checked on a 2x crop."))
f.append(F(197, "(8.14.2.4)", "script 𝒫roj (three times)", r"\operatorname{Proj}", "font", None, "high",
    fx(r"\lambda:\operatorname{Proj}(\mathcal{M})<NL>  \otimes_{\mathcal{S}_X}\operatorname{Proj}(\mathcal{N})<NL>  \to\operatorname{Proj}(\mathcal{M}\otimes_{\mathcal{S}}\mathcal{N}).",
       r"\lambda:" + PROJ + r"(\mathcal{M})<NL>  \otimes_{\mathcal{S}_X}" + PROJ + r"(\mathcal{N})<NL>  \to" + PROJ + r"(\mathcal{M}\otimes_{\mathcal{S}}\mathcal{N})."),
    PNOTE))

# ---------------- page 198 ----------------
f.append(F(198, "proof of (8.14.3), first displayed homomorphism (2.5.11.1)",
    "M(m)_(f)⊗_{S_(f)}N(n)_(f) → (M⊗_S N)(m+n)_(f) with no comma", r"(m+n)_{(f)},\\",
    "punctuation", None, "high", fx(r"(m+n)_{(f)},\\", r"(m+n)_{(f)}\\"),
    "Checked on a crop. The minus in (n—m) of the second line is the print's 38 px dash (GLOBAL_ISSUES item 23), left as it is."))
f.append(F(198, "proof of (8.14.3): (0, 1.3.4)", "bold 0", "plain 0", "convention", 2, "high",
    fx(r"{0, 1.3.4}", r"{\textbf{0}, 1.3.4}"), ""))
f.append(F(198, "proof of (8.14.3): 'l'homomorphisme canonique (0, 1.3.5)'", "bold 0", "plain 0", "convention", 2, "high",
    fx(r"canonique (\hyperref[0.1.3.5-fr]{0, 1.3.5}", r"canonique (\hyperref[0.1.3.5-fr]{\textbf{0}, 1.3.5}"), ""))
f.append(F(198, "proof of (8.14.3): 'entraîne alors (0, 1.3.5)'", "bold 0", "plain 0", "convention", 2, "high",
    fx(r"alors (\hyperref[0.1.3.5-fr]{0, 1.3.5}", r"alors (\hyperref[0.1.3.5-fr]{\textbf{0}, 1.3.5}"), ""))
f.append(F(198, "(8.14.5.1): α_n : ℳ_n → q_*(𝒫roj_0(ℳ(n)))", "script 𝒫roj_0", r"\operatorname{Proj}_0",
    "font", None, "high",
    fx(r"q_*(\operatorname{Proj}_0(\mathcal{M}(n)))", r"q_*(" + PROJ + r"_0(\mathcal{M}(n)))"), PNOTE))
f.append(F(198, "(8.14.5): 'pour tout 𝒮_X-Module gradué ℱ'", "'Module gradué' in italics", "upright", "italics", None, "high",
    fx(r"pour tout $\mathcal{S}_X$-Module gradué", r"pour tout $\mathcal{S}_X$-\emph{Module gradué}"),
    "Checked on a 2x crop."))
f.append(F(198, "(8.14.5): '... gradué ℱ' before (8.14.5.2)", "no comma after ℱ", r"$\mathcal{F}$,",
    "punctuation", None, "high", fx(r"$\mathcal{F}$,", r"$\mathcal{F}$"),
    "Checked on a crop up to the right edge of the strip."))
f.append(F(198, "(8.14.5.2): Γ_*(ℱ) = ⊕ q_*(ℱ_n)", "bold Γ", r"\Gamma_*", "font", None, "high",
    fx(r"\Gamma_*(\mathcal{F})=", r"\bbGamma_*(\mathcal{F})="), "Checked on a crop. " + GNOTE))
f.append(F(198, "'En particulier, Γ_*(𝒮_X) = ⊕ q_*(𝒪_X(n))'", "bold Γ", r"\Gamma_*", "font", None, "high",
    fx(r"$\Gamma_*(\mathcal{S}_X)=", r"$\bbGamma_*(\mathcal{S}_X)="), GNOTE))
f.append(F(198, "'notée Γ_*(𝒪_X) dans (3.3.1.2)'", "bold Γ", r"\Gamma_*", "font", None, "high",
    fx(r"$\Gamma_*(\mathcal{O}_X)$", r"$\bbGamma_*(\mathcal{O}_X)$"), GNOTE))
f.append(F(198, "'il est clair que Γ_*(ℱ) est ...'", "bold Γ", r"\Gamma_*", "font", None, "high",
    fx(r"que<NL>$\Gamma_*(\mathcal{F})$", r"que<NL>$\bbGamma_*(\mathcal{F})$"), GNOTE))
f.append(F(198, "'il est clair que Γ_*(ℱ) est une Γ_*(𝒮_X)-Algèbre graduée (0, 4.2.2)'",
    "est une 𝚪_*(𝒮_X)-Algèbre graduée (italic 'Algèbre graduée', bold Γ)",
    r"est un $\Gamma_*(\mathcal{S}_X)$-Module gradué", "misprint_in_print", None, "high",
    fx(r"un $\Gamma_*(\mathcal{S}_X)$-Module gradué", r"une $\bbGamma_*(\mathcal{S}_X)$-\emph{Algèbre graduée}"),
    "Checked on a crop. The TeX silently corrects the print; the fix restores the printed reading and also carries this Γ's bold and the print's italics (no separate findings for them). ℱ is an arbitrary graded 𝒮_X-Module, so Γ_*(ℱ) is a graded Γ_*(𝒮_X)-Module, not an Algebra; p. 199 then calls it 'un 𝒮-Module gradué'. 'corrected' keeps the bold Γ and the italics.",
    r"un $\bbGamma_*(\mathcal{S}_X)$-\emph{Module gradué}"))
f.append(F(198, "(8.14.5): (0, 4.2.2)", "bold 0", "plain 0", "convention", 2, "high",
    fx(r"{0, 4.2.2}", r"{\textbf{0}, 4.2.2}"), ""))
f.append(F(198, "page break 198/199 inside the sentence 'Lorsque | dans les homomorphismes (8.14.5.1) ...'",
    "p. 199 continues the sentence (no new paragraph)", r"blank line before \oldpage[II]{199}",
    "other", None, "high", fx("Lorsque<NL><NL>", "Lorsque<NL>"),
    "GLOBAL_ISSUES item 20. The blank line is the last line of this segment, before the page-199 marker."))

# ---------------- page 199 ----------------
f.append(F(199, "(8.14.5.3): α : 𝒮 → Γ_*(𝒮_X)", "bold Γ", r"\Gamma_*", "font", None, "high",
    fx(r"\alpha:\mathcal{S}\to\Gamma_*(\mathcal{S}_X)", r"\alpha:\mathcal{S}\to\bbGamma_*(\mathcal{S}_X)"), GNOTE))
f.append(F(199, "'qui fait donc de Γ_*(ℱ) un 𝒮-Module gradué'", "bold Γ", r"\Gamma_*", "font", None, "high",
    fx(r"$\Gamma_*(\mathcal{F})$ un", r"$\bbGamma_*(\mathcal{F})$ un"), GNOTE))
f.append(F(199, "'un 𝒮-Module gradué; les homomorphismes'", "'Module gradué' in italics", "upright", "italics", None, "high",
    fx(r"$\mathcal{S}$-Module gradué~;", r"$\mathcal{S}$-\emph{Module gradué}~;"), "Checked on a crop."))
f.append(F(199, "'un homomorphisme (de degré 0) de 𝒮-Modules gradués' before (8.14.5.4)",
    "'Modules gradués' in italics", "upright", "italics", None, "high",
    fx(r"(de<NL>degré $0$) de $\mathcal{S}$-Modules gradués", r"(de<NL>degré $0$) de $\mathcal{S}$-\emph{Modules gradués}"),
    "Checked on a crop."))
f.append(F(199, "(8.14.5.4): α : ℳ → Γ_*(𝒫roj(ℳ)).", "bold Γ and script 𝒫roj", r"\Gamma_*(\operatorname{Proj}(...))",
    "font", None, "high",
    fx(r"\alpha:\mathcal{M}\to\Gamma_*(\operatorname{Proj}(\mathcal{M})).", r"\alpha:\mathcal{M}\to\bbGamma_*(" + PROJ + r"(\mathcal{M}))."),
    "One edit for both differences. " + GNOTE + " " + PNOTE))
f.append(F(199, "(8.14.6): 'le 𝒮-Module gradué Γ_*(ℱ) soit nécessairement quasi-cohérent'", "bold Γ", r"\Gamma_*",
    "font", None, "high", fx(r"$\Gamma_*(\mathcal{F})$ soit", r"$\bbGamma_*(\mathcal{F})$ soit"), GNOTE))
f.append(F(199, "(8.14.6): (I, 9.2.2, b))", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 9.2.2,", r"{\textbf{I}, 9.2.2,"), "Independent of the italic b) edit of the same reference."))
f.append(F(199, "(8.14.6): (I, 9.2.2, b))", "italic b)", "upright b)", "italics", None, "high",
    fx(r"9.2.2, b)}", r"9.2.2, \emph{b)}}"), "Checked on a crop. Independent of the bold-I edit (either order works)."))
f.append(F(199, "(8.14.6.2): Γ'_*(ℱ') = ⊕ q'_*(ℱ'_n)", "bold Γ'", r"\Gamma'_*", "font", None, "high",
    fx(r"\Gamma'_*(\mathcal{F}')=<NL>", r"\bbGamma'_*(\mathcal{F}')=<NL>"), GNOTE))
f.append(F(199, "'Γ'_*(ℱ') est un 𝒮-Module gradué quasi-cohérent (I, 9.6.1)'", "bold Γ'", r"\Gamma'_*", "font", None, "high",
    fx(r"$\Gamma'_*(\mathcal{F}')$ est un", r"$\bbGamma'_*(\mathcal{F}')$ est un"), GNOTE))
f.append(F(199, "'est un 𝒮-Module gradué quasi-cohérent (I, 9.6.1)'", "quasi-cohérent in italics", "upright",
    "italics", None, "high", fx(r"Module gradué quasi-cohérent<NL>(", r"Module gradué \emph{quasi-cohérent}<NL>("),
    "Checked on a crop. Independent of the convention-2 edit of the same reference."))
f.append(F(199, "(I, 9.6.1)", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 9.6.1}", r"{\textbf{I}, 9.6.1}"), ""))
f.append(F(199, "(I, 6.6.4, (v))", "bold I", "plain I", "convention", 2, "high",
    fx(r"{I, 6.6.4,", r"{\textbf{I}, 6.6.4,"), ""))
f.append(F(199, "(8.14.6.3): Γ'_*(ℱ') = Γ_*(ℱ).", "bold Γ' and Γ", r"\Gamma'_*, \Gamma_*", "font", None, "high",
    fx(r"\Gamma'_*(\mathcal{F}')=\Gamma_*(\mathcal{F}).", r"\bbGamma'_*(\mathcal{F}')=\bbGamma_*(\mathcal{F})."), GNOTE))
f.append(F(199, "(8.14.6.4): 𝒫roj'(ℳ) = 𝒫roj(ℳ)|X'", "script 𝒫roj', 𝒫roj", r"\operatorname{Proj}", "font", None, "high",
    fx(r"\operatorname{Proj}'(\mathcal{M})<NL>  =\operatorname{Proj}(\mathcal{M})|X'",
       PROJ + r"'(\mathcal{M})<NL>  =" + PROJ + r"(\mathcal{M})|X'"), PNOTE))
f.append(F(199, "display 𝒫roj(ℳ) → j_*(𝒫roj'(ℳ))", "script 𝒫roj, 𝒫roj'", r"\operatorname{Proj}", "font", None, "high",
    fx(r"\operatorname{Proj}(\mathcal{M})\to<NL>  j_*(\operatorname{Proj}'(\mathcal{M}))",
       PROJ + r"(\mathcal{M})\to<NL>  j_*(" + PROJ + r"'(\mathcal{M}))"), PNOTE))
f.append(F(199, "(0, 4.4.3)", "bold 0", "plain 0", "convention", 2, "high",
    fx(r"{0, 4.4.3}", r"{\textbf{0}, 4.4.3}"), ""))
f.append(F(199, "'un homomorphisme canonique Γ_*(𝒫roj(ℳ)) → Γ'_*(𝒫roj'(ℳ))'", "bold Γ, Γ' and script 𝒫roj, 𝒫roj'",
    r"\Gamma_*, \Gamma'_*, \operatorname{Proj}", "font", None, "high",
    fx(r"$\Gamma_*(\operatorname{Proj}(\mathcal{M}))\to<NL>\Gamma'_*(\operatorname{Proj}'(\mathcal{M}))$",
       r"$\bbGamma_*(" + PROJ + r"(\mathcal{M}))\to<NL>\bbGamma'_*(" + PROJ + r"'(\mathcal{M}))$"),
    "One edit for both differences. " + GNOTE + " " + PNOTE))
f.append(F(199, "(8.14.6.5): α' : ℳ → Γ'_*(𝒫roj'(ℳ)).", "bold Γ' and script 𝒫roj'", r"\Gamma'_*, \operatorname{Proj}'",
    "font", None, "high",
    fx(r"\alpha':\mathcal{M}\to<NL>  \Gamma'_*(\operatorname{Proj}'(\mathcal{M})).",
       r"\alpha':\mathcal{M}\to<NL>  \bbGamma'_*(" + PROJ + r"'(\mathcal{M}))."),
    "One edit for both differences. " + GNOTE + " " + PNOTE))
f.append(F(199, "(8.14.7): 'et soit ℱ' un 𝒮_X'-Module gradué quasi-cohérent, de sorte que'",
    "'Module gradué quasi-cohérent' in italics", "upright", "italics", None, "high",
    fx(r"Module gradué quasi-cohérent, de sorte", r"\emph{Module gradué quasi-cohérent}, de sorte"), "Checked on a crop."))
f.append(F(199, "(8.14.7): '𝒫roj'(Γ'_*(ℱ')) est aussi un'", "script 𝒫roj' and bold Γ'", r"\operatorname{Proj}'(\Gamma'_*(...))",
    "font", None, "high",
    fx(r"$\operatorname{Proj}'(\Gamma'_*(\mathcal{F}'))$ est aussi", "$" + PROJ + r"'(\bbGamma'_*(\mathcal{F}'))$ est aussi"),
    "One edit for both differences. " + GNOTE + " " + PNOTE))
f.append(F(199, "(8.14.7): page break 199/200 inside 'quasi-|cohérent' ('... est aussi un 𝒮_X'-Module gradué quasi-' ends p. 199)",
    "p. 199 ends with italic 'quasi-'; p. 200 begins with italic 'cohérent.', then 'Nous allons définir ...' and (8.14.7.1)",
    r"\oldpage[II]{200} after the display (8.14.7.1); 'quasi-cohérent' upright", "marker", None, "high",
    fx(r"gradué quasi-cohérent. Nous allons", r"gradué \emph{quasi-\oldpage[II]{200}cohérent}. Nous allons"),
    "Checked on page_199_s4.png and page_200_s1.png. Part 1 of 2: inserts the marker inside the word (mid-word markers exist, e.g. 'consi\\oldpage[III]{149}dérés'; precedent 0_I p. 41) and adds the print's italics. Part 2 (page-200 entry) deletes the old marker; apply both together. Italics alone, without the move: new = 'gradué \\emph{quasi-cohérent}. Nous allons'."))
f.append(F(199, "(8.14.7.1): β' : 𝒫roj'(Γ'_*(ℱ')) → ℱ' (printed at the top of p. 200)", "script 𝒫roj' and bold Γ'",
    r"\operatorname{Proj}'(\Gamma'_*(...))", "font", None, "high",
    fx(r"\beta':\operatorname{Proj}'(\Gamma'_*(\mathcal{F}'))\to", r"\beta':" + PROJ + r"'(\bbGamma'_*(\mathcal{F}'))\to"),
    "Printed on p. 200 (lines 1-3 there, checked on page_200_s1.png) but in this segment until the marker moves; the page-200 checker does not see it. " + GNOTE + " " + PNOTE))

# ---------------- page 200 (second half of the marker move) ----------------
f.append(F(200, "start of the page-200 segment: \\oldpage[II]{200} before 'Supposons d'abord'",
    "p. 200 begins with 'cohérent. Nous allons définir ...' and (8.14.7.1); 'Supposons d'abord' is its fourth line",
    r"\oldpage[II]{200} directly before 'Supposons d'abord'", "marker", None, "high",
    fx(r"\oldpage[II]{200}<NL>Supposons d'abord", r"Supposons d'abord"),
    "Part 2 of 2 of the page-200 marker move (part 1 is the page-199 marker entry); apply both together. The blank line before the old marker stays and keeps the paragraph break before 'Supposons d'abord' (indented on p. 200)."))

# ---------------- checks ----------------
bad = 0
texts = {}
for d in f:
    p = d["page"]
    if p not in texts:
        with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8") as fh:
            texts[p] = fh.read()          # universal newlines: CRLF -> LF
    if d["fix"] is None:
        continue
    n = texts[p].count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE (%d) p.%d: %r" % (n, p, d["fix"]["old"]))
    if d["fix"]["old"] == d["fix"]["new"]:
        bad += 1
        print("NO-OP p.%d: %r" % (p, d["fix"]["old"]))

# overlap check per page (fix regions must not overlap)
for p, t in texts.items():
    spans = []
    for d in f:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP p.%d: [%s] / [%s]" % (p, a[2], b[2]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(f, fh, ensure_ascii=False, indent=1)

from collections import Counter
c = Counter()
for d in f:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted(set(d["page"] for d in f)):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(f), "bad", bad)
