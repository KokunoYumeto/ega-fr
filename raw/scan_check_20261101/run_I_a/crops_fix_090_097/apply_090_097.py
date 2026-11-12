"""EGA I (ega-fr, release r20, diplomatic), printed pp. 90-97: apply the checked scan findings, write
FIXLOG_090_097.jsonl and MISPRINTS_090_097.json, and check the log.

usage: python -I apply_090_097.py --dry     check every change on in-memory copies, write nothing
       python -I apply_090_097.py --apply   edit the two release files, write the log and the misprint list
       python -I apply_090_097.py --check   replay FIXLOG_090_097.jsonl on the saved unedited copies and compare
       python -I apply_090_097.py --rewrite-logs   rewrite the log texts only (the TeX must already match)

Each "old" string must occur exactly once in its file at the moment it is applied and must lie on its page
(p. N = from \\oldpage[I]{N} to the next marker; p. 97 in ega1-2-fr.tex = the text before \\oldpage[I]{98})."""
import json
import pathlib
import re
import sys
from collections import Counter

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
HERE = pathlib.Path(__file__).resolve().parent
NATIVE = "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega1/"
F1 = NATIVE + "ega1-1-fr.tex"
F2 = NATIVE + "ega1-2-fr.tex"
ORIG = {F1: HERE / "ega1-1-fr.orig.tex", F2: HERE / "ega1-2-fr.orig.tex"}
LOG = E / "FIXLOG_090_097.jsonl"
MIS = E / "MISPRINTS_090_097.json"
A = "findings_090_094.json"
B = "findings_095_099.json"
ERR3 = "errata EGA III (ega3/ega3-7-fr.tex, Errata et Addenda)"
NOTE5 = (f"not in {B}; print checked; same notation as the Ã', M̃' findings of {A} on pp. 93-94 "
         f"(FIX_POLICY conv. 5: tilde on the letter only)")
NOTE9 = (f"not in {A}; print checked; {B} (p. 95) notes that ega1-1-fr.tex writes ^{{\\#}} for the printed ♯ "
         f"throughout; GLOBAL_ISSUES.md item 9")
NOTE6 = (f"not in {A}; print checked; references inside italic statements set upright as on pp. 82, 99 and 105 "
         f"(FIXLOG.jsonl, FIXLOG_098_109.jsonl)")

changes = []  # (file, page, old, new, why, kind)


def ch(file, page, old, new, why, kind):
    changes.append((file, page, old, new, why, kind))


def bold0(page, ref, ctx_before="", ctx_after="", src=A):
    old = ctx_before + "(\\hyperref[0." + ref + "-fr]{0, " + ref + "}" + ctx_after
    new = ctx_before + "(\\hyperref[0." + ref + "-fr]{\\textbf{0}, " + ref + "}" + ctx_after
    ch(F1, page, old, new, f"conv. 2: bold 0 in (𝟎, {ref}) ({src}, p. {page})", "conv2")


# ------------------------------------------------------------------ p. 90
ch(F1, 90, r"canoniquement à $\widetilde{(M\otimes_B N)}$~;", r"canoniquement à $(M\otimes_B N)\supertilde$~;",
   f"conv. 5: the print writes (M⊗_B N)~, tilde after the parenthesis ({A}, p. 90)", "conv5")
ch(F1, 90, r"canoniquement à $\widetilde{(\operatorname{Hom}_B(M,N))}$ lorsque",
   r"canoniquement à $(\operatorname{Hom}_B(M,N))\supertilde$ lorsque",
   f"conv. 5: the print writes (Hom_B(M, N))~ ({A}, p. 90)", "conv5")
ch(F1, 90, r"$\widetilde{(\mathfrak{J}N)}=\widetilde{\mathfrak{J}}\cdot\widetilde{N}$",
   r"$(\mathfrak{J}N)\supertilde=\widetilde{\mathfrak{J}}\cdot\widetilde{N}$",
   f"conv. 5: the print writes (𝔍N)~ = 𝔍̃.Ñ ({A}, p. 90)", "conv5")
ch(F1, 90, r"$A$-algèbre graduée par des sous-$A$-modules", r"$A$-algèbre \emph{graduée} par des sous-$A$-modules",
   f"rule 1 (italics): 'graduée' is italic in the print ({A}, p. 90; print checked)", "italics")
ch(F1, 90, r"des $\widetilde{A}$-Modules $\widetilde{B_n}$", r"des $\widetilde{A}$-Modules $\widetilde{B}_n$",
   f"conv. 5: the print writes B̃_n, tilde on B only ({A}, p. 90)", "conv5")
ch(F1, 90, r"$B_m\otimes_A B_n\to B$", r"$B_m\otimes B_n\to B$",
   f"rule 1 (formula): the print has a bare ⊗ in B_m⊗B_n→B, without the subscript A ({A}, p. 90; print checked)",
   "formula")
ch(F1, 90, r"gradué par les $\widetilde{M_n}$.", r"gradué par les $\widetilde{M}_n$.",
   f"conv. 5: the print writes M̃_n, tilde on M only ({A}, p. 90)", "conv5")
bold0(90, "4.1.3")
ch(F1, 90, r"$\bigotimes_A^n M\to B$", r"$\bigotimes^n M\to B$",
   f"rule 1 (formula): the print has ⊗ with n and no subscript A ({A}, p. 90; print checked)", "formula")
ch(F1, 90, r"\item[\textit{a})] Il existe un $A$-module $M$ tel que", r"\item[\textup{a)}] Il existe un $A$-module $M$ tel que",
   f"conv. 6: the label a) of Théorème (1.4.1) is upright in the print, parenthesis included ({A}, p. 90; print "
   f"checked; label style as on p. 122)", "conv6")
ch(F1, 90, r"\item[\textit{b})] Il existe un recouvrement", r"\item[\textup{b)}] Il existe un recouvrement",
   f"conv. 6: the label b) of Théorème (1.4.1) is upright in the print ({A}, p. 90)", "conv6")
ch(F1, 90, r"$\widetilde{M_i}$, où $M_i$", r"$\widetilde{M}_i$, où $M_i$",
   f"conv. 5: the print writes M̃_i, tilde on M only ({A}, p. 90)", "conv5")
ch(F1, 90, r"\item[\textit{c})] Le faisceau", r"\item[\textup{c)}] Le faisceau",
   f"conv. 6: the label c) of Théorème (1.4.1) is upright in the print ({A}, p. 90)", "conv6")
ch(F1, 90, r"(\hyperref[0.5.1.3-fr]{0, 5.1.3}).", r"\textup{(\hyperref[0.5.1.3-fr]{\textbf{0}, 5.1.3})}.",
   f"conv. 2 + conv. 6: bold 0 in (𝟎, 5.1.3); the reference is upright inside the italic Théorème (1.4.1) c) "
   f"({A}, p. 90; print checked)", "conv2+6")
ch(F1, 90, r"\item[\textit{d})] Les deux", r"\item[\textup{d)}] Les deux",
   f"conv. 6: the label d) of Théorème (1.4.1) is upright in the print ({A}, p. 90)", "conv6")
ch(F1, 90, r"\item[\textit{d}\,1)] Pour tout", r"\item[\textup{d\,1)}] Pour tout",
   f"conv. 6: the label d 1) of Théorème (1.4.1) is upright in the print ({A}, p. 90)", "conv6")
ch(F1, 90, r"\item[\textit{d}\,2)] Pour tout", r"\item[\textup{d\,2)}] Pour tout",
   f"conv. 6: the label d 2) of Théorème (1.4.1) is upright in the print ({A}, p. 90)", "conv6")
ch(F1, 90, r"$\widetilde{A_f}^{(I)}\to", r"$\widetilde{A}_f^{(I)}\to",
   f"conv. 5: the print writes Ã_f^(I), tilde on A only ({A}, p. 90)", "conv5")
ch(F1, 90, r"\to\widetilde{A_f}^{(J)}$", r"\to\widetilde{A}_f^{(J)}$",
   f"conv. 5: the print writes Ã_f^(J), tilde on A only ({A}, p. 90)", "conv5")

# ------------------------------------------------------------------ p. 91
ch(F1, 91, r"$z/1$ de $N_f$, et est par suite", r"$z/1$ de $N_f$ et est par suite",
   f"rule 1 (punctuation): no comma after N_f before 'et est par suite' in the print ({A}, p. 91; print checked)",
   "punctuation")
ch(F1, 91, "vérifie\n" + r"\textit{d}\,1) et", "vérifie\n" + r"\textup{d\,1)} et",
   f"conv. 6: 'd 1)' is upright inside the italic Lemme (1.4.1.1) ({A}, p. 91; print checked)", "conv6")
ch(F1, 91, r"et \textit{d}\,2)~; alors", r"et \textup{d\,2)}~; alors",
   f"conv. 6: 'd 2)' is upright inside the italic Lemme (1.4.1.1) ({A}, p. 91; print checked)", "conv6")
ch(F1, 91, r"\item[\textit{d}'\,1)]", r"\item[\textup{d'\,1)}]",
   f"conv. 6: the label d' 1) of Lemme (1.4.1.1) is upright in the print ({A}, p. 91; print checked)", "conv6")
ch(F1, 91, r"\item[\textit{d}'\,2)]", r"\item[\textup{d'\,2)}]",
   f"conv. 6: the label d' 2) of Lemme (1.4.1.1) is upright in the print ({A}, p. 91)", "conv6")

# ------------------------------------------------------------------ p. 92
bold0(92, "3.2.5")
bold0(92, "1.2.4", ctx_after="), et la vérification")
ch(F1, 92, r"\item[\textit{a})] $\mathscr{F}$ est cohérent.", r"\item[\textup{a)}] $\mathscr{F}$ est cohérent.",
   f"conv. 6: the label a) of Théorème (1.5.1) is upright in the print ({A}, p. 92)", "conv6")
ch(F1, 92, r"\item[\textit{b})] $\mathscr{F}$ est de type fini", r"\item[\textup{b)}] $\mathscr{F}$ est de type fini",
   f"conv. 6: the label b) of Théorème (1.5.1) is upright in the print ({A}, p. 92)", "conv6")
ch(F1, 92, r"\item[\textit{c})] Il existe un $A$-module $M$ de type fini",
   r"\item[\textup{c)}] Il existe un $A$-module $M$ de type fini",
   f"conv. 6: the label c) of Théorème (1.5.1) is upright in the print ({A}, p. 92)", "conv6")

# ------------------------------------------------------------------ p. 93
bold0(93, "2.2.3")
ch(F1, 93, r"\varinjlim\widetilde{M_\lambda}|V", r"\varinjlim\widetilde{M}_\lambda|V",
   f"conv. 5: the print writes lim M̃_λ|V, tilde on M only ({A}, p. 93)", "conv5")
ch(F1, 93, r"$\mathscr{F}=\widetilde{M_\lambda}|V$", r"$\mathscr{F}=\widetilde{M}_\lambda|V$",
   f"conv. 5: the print writes ℱ = M̃_λ|V, tilde on M only ({A}, p. 93)", "conv5")
bold0(93, "5.2.3", ctx_after=").\n\nMontrons enfin")
ch(F1, 93, r"$\widetilde{A^n}\to\widetilde{M}$", r"$\widetilde{A}^n\to\widetilde{M}$",
   f"conv. 5: the print writes Ã^n, tilde on A only and exponent outside ({A}, p. 93)", "conv5")
ch(F1, 93, r"Sous les hypothèses de (\hyperref[I.1.5.1-fr]{1.5.1}), le faisceau",
   r"Sous les hypothèses de \textup{(\hyperref[I.1.5.1-fr]{1.5.1})}, le faisceau",
   f"conv. 6: the reference (1.5.1) is printed upright inside the italic Cor. (1.5.2) ({NOTE6})", "conv6-extra")
ch(F1, 93, r"Sous les hypothèses de (\hyperref[I.1.5.1-fr]{1.5.1}), tout faisceau",
   r"Sous les hypothèses de \textup{(\hyperref[I.1.5.1-fr]{1.5.1})}, tout faisceau",
   f"conv. 6: the reference (1.5.1) is printed upright inside the italic Cor. (1.5.3) ({NOTE6})", "conv6-extra")
ch(F1, 93, "Sous les hypothèses de (\\hyperref[I.1.5.1-fr]{1.5.1}), tout\n",
   "Sous les hypothèses de \\textup{(\\hyperref[I.1.5.1-fr]{1.5.1})}, tout\n",
   f"conv. 6: the reference (1.5.1) is printed upright inside the italic Cor. (1.5.4) ({NOTE6})", "conv6-extra")
ch(F1, 93, r"$\Gamma(D(f'),\widetilde{A'})$ et $\Gamma(D(f),\widetilde{A})$",
   r"$\Gamma(D(f'),\widetilde{A}')$ et $\Gamma(D(f),\widetilde{A})$",
   f"conv. 5: the print writes Γ(D(f'), Ã'), tilde on A only, prime outside ({A}, p. 93)", "conv5")
bold0(93, "1.5.1", ctx_after="), autrement dit")
ch(F1, 93, r"  \Gamma(D(f'),\widetilde{A'})\to", r"  \Gamma(D(f'),\widetilde{A}')\to",
   f"conv. 5: Ã' with the prime outside the tilde, left side of the display of (1.6.1) ({A}, p. 93)", "conv5")
ch(F1, 93, r"  =\Gamma(D(f'),{}^a\varphi_*(\widetilde{A})).", r"  =\Gamma(D(f'),{}^a\varphi_*(\widetilde{A}))",
   f"rule 1 (punctuation): the display of (1.6.1) ends without a period in the print ({A}, p. 93; print checked)",
   "punctuation")

# ------------------------------------------------------------------ p. 94
ch(F1, 94, r"    \Gamma(D(f'),\widetilde{A'})\ar[r]\ar[d] &", r"    \Gamma(D(f'),\widetilde{A}')\ar[r]\ar[d] &",
   f"conv. 5: Ã' with the prime outside the tilde, top left of the diagram of (1.6.1) ({A}, p. 94)", "conv5")
ch(F1, 94, r"    \Gamma(D(g'),\widetilde{A'})\ar[r] &", r"    \Gamma(D(g'),\widetilde{A}')\ar[r] &",
   f"conv. 5: Ã' with the prime outside the tilde, bottom left of the diagram of (1.6.1) ({A}, p. 94)", "conv5")
bold0(94, "1.5.1", ctx_after=")~; on a donc")
bold0(94, "3.2.3", ctx_after="). Le couple")
bold0(94, "4.1.1", ctx_after=").\n\nNotons en outre")
ch(F1, 94, r"$\widetilde{\varphi}_x^\#$ (\hyperref", r"$\widetilde{\varphi}_x^{\sharp}$ (\hyperref",
   f"rule 1 (symbol): the print has the sharp sign ♯ in φ̃_x^♯, not # ({NOTE9})", "sharp-extra")
bold0(94, "3.7.1", ctx_after=") n'est autre")
bold0(94, "1.5.1", ctx_after="). En effet, tout")
ch(F1, 94, r"$\Gamma(D(f'),\widetilde{A'})\to", r"$\Gamma(D(f'),\widetilde{A}')\to",
   f"conv. 5: Ã' with the prime outside the tilde ({A}, p. 94)", "conv5")
ch(F1, 94, r"$s'\in\Gamma(D(f'),\widetilde{A'})$", r"$s'\in\Gamma(D(f'),\widetilde{A}')$",
   f"conv. 5: Ã' with the prime outside the tilde ({A}, p. 94)", "conv5")
ch(F1, 94, r"$\widetilde{\varphi}_x^\#(z')", r"$\widetilde{\varphi}_x^{\sharp}(z')",
   f"rule 1 (symbol): the print has ♯ in φ̃_x^♯(z'), not # ({NOTE9})", "sharp-extra")
ch(F1, 94, r"$\widetilde{\varphi}_y^\#:\mathscr{O}_x", r"$\widetilde{\varphi}_y^{\sharp}:\mathscr{O}_x",
   f"rule 1 (symbol): the print has ♯ in φ̃_y^♯ (Exemple (1.6.2)), not # ({NOTE9})", "sharp-extra")
bold0(94, "1.2.6", ctx_after=")~; autrement dit")
ch(F1, 94, r"$\Gamma(D(f'),\widetilde{M'})$ et $\Gamma(D(f),\widetilde{M})$",
   r"$\Gamma(D(f'),\widetilde{M}')$ et $\Gamma(D(f),\widetilde{M})$",
   f"conv. 5: M̃' with the prime outside the tilde ({A}, p. 94)", "conv5")
bold0(94, "1.5.2")
ch(F1, 94, r"$\Gamma(D(f'),\widetilde{A'})$-Modules~:", r"$\Gamma(D(f'),\widetilde{A}')$-Modules~:",
   f"conv. 5: Ã' with the prime outside the tilde ({A}, p. 94)", "conv5")
ch(F1, 94, r"$\Gamma(D(f'),\widetilde{A}')$-Modules~:", r"$\Gamma(D(f'),\widetilde{A}')$-modules~:",
   f"rule 1 (word): the print has lower-case 'modules' in 'de Γ(D(f'), Ã')-modules :' ({A}, p. 94; print checked)",
   "word")
ch(F1, 94, r"$\Gamma(D(f'),\widetilde{M'})\xrightarrow{\sim}", r"$\Gamma(D(f'),\widetilde{M}')\xrightarrow{\sim}",
   f"conv. 5: M̃' with the prime outside the tilde ({A}, p. 94)", "conv5")
bold0(94, "1.5.6", ctx_after="), donc définissent")
ch(F1, 94, r"pour toute $A$-algèbre $B$,", r"pour toute $A$-\emph{algèbre} $B$,",
   f"rule 1 (italics): 'algèbre' is italic in 'pour toute A-algèbre B' ({A}, p. 94; print checked)", "italics")

# ------------------------------------------------------------------ p. 95
ch(F1, 95, r"$(B_{[\varphi]})^{\sim}\xrightarrow{\sim}\Phi_*(\widetilde{B})$",
   r"$(B_{[\varphi]})^{\sim}\to\Phi_*(\widetilde{B})$",
   f"rule 1 (symbol): the print has a plain arrow in (B_[φ])~ → Φ_*(B̃); only the next formula has the "
   f"isomorphism arrow ({B}, p. 95; print checked)", "symbol")
ch(F1, 95, r"$\mathscr{O}_{X'}$-Algèbres~; si $M$", r"$\mathscr{O}_{X'}$-\emph{Algèbres}~; si $M$",
   f"rule 1 (italics): 'Algèbres' in 𝒪_X'-Algèbres is italic in the print ({B}, p. 95; print checked)", "italics")
ch(F1, 95, r"$\widetilde{M'}$ un foncteur exact", r"$\widetilde{M}'$ un foncteur exact",
   f"conv. 5: M̃' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"-Module $\Phi^*(\widetilde{N'})$ sur", r"-Module $\Phi^*(\widetilde{N}')$ sur",
   f"conv. 5: Ñ' with the prime outside the tilde, Prop. (1.6.5) ({NOTE5})", "conv5-extra")
ch(F1, 95, r"$j:z'\mapsto z'\otimes 1$", r"$j:z'\to z'\otimes 1$",
   f"conv. 3: the print has a plain arrow j : z' → z'⊗1, not ↦ ({B}, p. 95)", "conv3")
ch(F1, 95, r"dans $N_{[\varphi]}$~; en effet", r"dans $N_{[\varphi]}$~: en effet",
   f"rule 1 (punctuation): the print has a colon after N_[φ], not a semicolon ({B}, p. 95; print checked)",
   "punctuation")
ch(F1, 95, r"$\widetilde{j}:\widetilde{N'}\to", r"$\widetilde{j}:\widetilde{N}'\to",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"applique $\widetilde{N'}$ dans", r"applique $\widetilde{N}'$ dans",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"$h=\widetilde{j}^{\#}$", r"$h=\widetilde{j}^{\sharp}$",
   f"rule 1 (symbol): the print has the sharp sign ♯ in h = j̃^♯, not # ({B}, p. 95; print checked)", "sharp")
ch(F1, 95, r"de $\Phi^*(\widetilde{N'})$ dans $\widetilde{N}$", r"de $\Phi^*(\widetilde{N}')$ dans $\widetilde{N}$",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
bold0(95, "4.4.3", ctx_after=")~; on va voir", src=B)
ch(F1, 95, r"$\Gamma(D(f'),\widetilde{N'})$ à $N_f$", r"$\Gamma(D(f'),\widetilde{N}')$ à $N_f$",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"$s'\in\Gamma(D(f'),\widetilde{N'})$", r"$s'\in\Gamma(D(f'),\widetilde{N}')$",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
bold0(95, "4.4.3", ctx_after="). Mais on peut", src=B)
bold0(95, "1.5.4", src=B)
ch(F1, 95, r"$y\mapsto t_y\cdot s_y$", r"$y\to t_y\cdot s_y$",
   f"conv. 3: the print has a plain arrow y → t_y.s_y, not ↦ ({B}, p. 95)", "conv3")
bold0(95, "1.5.6", ctx_after=") montrent", src=B)
ch(F1, 95, r"(A_x)_{[\varphi_x]}", r"(A_x)_{[\varphi_{x'}]}",
   f"rule 3 (misprint kept in the diplomatic text; rule 1 if it is not a misprint): the print has (A_x)_[φ_x'] "
   f"in (1.6.5.1); the TeX had φ_x; printed reading restored; recorded with low confidence in "
   f"MISPRINTS_090_097.json ({B}, p. 95; print checked)", "misprint")
ch(F1, 95, r"$\Phi^*(\widetilde{B'})$ sur", r"$\Phi^*(\widetilde{B}')$ sur",
   f"conv. 5: B̃' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"canonique de $\Phi^*(\widetilde{N'})$ sur", r"canonique de $\Phi^*(\widetilde{N}')$ sur",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"$\Phi^*(\widetilde{B'})$-Modules.", r"$\Phi^*(\widetilde{B}')$-Modules.",
   f"conv. 5: B̃' with the prime outside the tilde ({NOTE5})", "conv5-extra")
ch(F1, 95, r"Les sections de $\Phi^*(\widetilde{N'})$", r"Les sections de $\Phi^*(\widetilde{N}')$",
   f"conv. 5: Ñ' with the prime outside the tilde, Cor. (1.6.6) ({NOTE5})", "conv5-extra")
ch(F1, 95, r"le $A'$-module $\Gamma(\widetilde{N'})$,", r"le $A'$-module $\Gamma(\widetilde{N}')$,",
   f"conv. 5: Ñ' with the prime outside the tilde, Cor. (1.6.6) ({NOTE5})", "conv5-extra")
ch(F1, 95, r"$\Gamma(\Phi^*(\widetilde{N'}))$.", r"$\Gamma(\Phi^*(N'))$.",
   f"rule 3 (misprint kept in the diplomatic text): the print ends Cor. (1.6.6) with Γ(Φ*(N')), without the "
   f"tilde; the TeX had silently corrected it; printed reading restored, recorded in MISPRINTS_090_097.json "
   f"({B}, p. 95; print checked)", "misprint")
ch(F1, 95, r"à $\Gamma(\widetilde{N'})$ et", r"à $\Gamma(\widetilde{N}')$ et",
   f"conv. 5: Ñ' with the prime outside the tilde ({NOTE5})", "conv5-extra")
bold0(95, "4.4.3.2", src=B)
ch(F1, 95, r"$\rho:\widetilde{N'}\to\Phi_*(\Phi^*(\widetilde{N'}))$",
   r"$\rho:\widetilde{N}'\to\Phi_*(\Phi^*(\widetilde{N}'))$",
   f"conv. 5: Ñ' with the prime outside the tilde, twice ({NOTE5})", "conv5-extra")

# ------------------------------------------------------------------ p. 96
ch(F1, 96, r"$z'\mapsto z'\otimes 1$. De même", r"$z'\to z'\otimes 1$. De même",
   f"conv. 3: the print has a plain arrow z' → z'⊗1, not ↦ ({B}, p. 96)", "conv3")
bold0(96, "4.4.3.3", src=B)
bold0(96, "3.7.1", ctx_after=",\n", src=B)
ch(F1, 96, "\\hyperref[0.4.4.3-fr]{0, 4.4.3}, et", "\\hyperref[0.4.4.3-fr]{\\textbf{0}, 4.4.3}, et",
   f"conv. 2: bold 0 in (𝟎, 3.7.1, 𝟎, 4.4.3, et 𝐈, 1.3.7) ({B}, p. 96)", "conv2")
ch(F1, 96, r"\hyperref[I.1.3.7-fr]{I, 1.3.7})", r"\hyperref[I.1.3.7-fr]{\textbf{I}, 1.3.7})",
   f"rule 1 (font), as conv. 2: the chapter numeral in (..., et 𝐈, 1.3.7) is bold in the print ({B}, p. 96; "
   f"written as on p. 101)", "font")
ch(F1, 96, r"On en conclut (\hyperref[0.4.4.3-fr]{0, 4.4.3} et", r"On en conclut (\hyperref[0.4.4.3-fr]{\textbf{0}, 4.4.3} et",
   f"conv. 2: bold 0 in (𝟎, 4.4.3 et 3.5.4.4) ({B}, p. 96)", "conv2")
ch(F1, 96, r"$\widetilde{v}^{\#}=", r"$\widetilde{v}^{\sharp}=",
   f"rule 1 (symbol): the print has ♯ in ṽ^♯ = (v⊗1)~, not # ({B}, p. 96)", "sharp")
bold0(96, "4.4.6", src=B)
ch(F1, 96, r"\mathscr{H}\!om_{\widetilde{A'}}", r"\mathscr{H}\!om_{\widetilde{A}'}",
   f"conv. 5: ℋom_Ã' with the prime outside the tilde, display of (1.6.8) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"(\widetilde{N'_1},\widetilde{N'_2})\bigr)", r"(\widetilde{N}'_1,\widetilde{N}'_2)\bigr)",
   f"conv. 5: Ñ'_1, Ñ'_2 with prime and index outside the tilde, display of (1.6.8) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"\bigl(\Phi^*(\widetilde{N'_1}),\Phi^*(\widetilde{N'_2})\bigr)",
   r"\bigl(\Phi^*(\widetilde{N}'_1),\Phi^*(\widetilde{N}'_2)\bigr)",
   f"conv. 5: Ñ'_1, Ñ'_2 with prime and index outside the tilde, display of (1.6.8) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"définition $\widetilde{\mathfrak{J}'}\widetilde M$", r"définition $\widetilde{\mathfrak{J}}'\widetilde M$",
   f"conv. 5: 𝔍̃' with the prime outside the tilde, (1.6.9) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"$\Phi^*(\widetilde{\mathfrak{J}'})\otimes_{\widetilde A}", r"$\Phi^*(\widetilde{\mathfrak{J}}')\otimes_{\widetilde A}",
   f"conv. 5: 𝔍̃' with the prime outside the tilde, (1.6.9) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"$\widetilde{\mathfrak{J}'}\widetilde M$ s'identifie", r"$\widetilde{\mathfrak{J}}'\widetilde M$ s'identifie",
   f"conv. 5: 𝔍̃' with the prime outside the tilde, (1.6.9) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"$\Phi^*(\widetilde{\mathfrak{J}'})\widetilde A$", r"$\Phi^*(\widetilde{\mathfrak{J}}')\widetilde A$",
   f"conv. 5: 𝔍̃' with the prime outside the tilde, (1.6.9) ({NOTE5})", "conv5-extra")
ch(F1, 96, r"$\widetilde{\varphi''}=\widetilde\varphi\circ\widetilde{\varphi'}$",
   r"$\widetilde{\varphi}''=\widetilde\varphi\circ\widetilde{\varphi}'$",
   f"conv. 5: φ̃'' and φ̃' with the primes outside the tilde, (1.6.10) ({NOTE5})", "conv5-extra")
bold0(96, "1.5.7", src=B)
ch(F1, 96, r"$(X,\mathscr{O}_X)$ est un \emph{schéma affine}", r"$(X,\mathscr{O}_X)$ est un schéma affine",
   f"conv. 6: 'schéma affine' is in the same italics as the rest of Déf. (1.7.1); \\emph inside the italic "
   f"environment set it upright ({B}, p. 96; print checked)", "conv6")
ch(F1, 96, r"(\hyperref[I.1.3.7-fr]{1.3.7}) est l'anneau du schéma affine",
   r"\textup{(\hyperref[I.1.3.7-fr]{1.3.7})} est l'anneau du schéma affine",
   f"conv. 6: the reference (1.3.7) is printed upright inside the italic Déf. (1.7.1) ({NOTE6})", "conv6-extra")
ch(F1, 96, r"d'anneaux $A(Y)\to A(X)$, il faut", r"d'anneaux~: $A(Y)\to A(X)$, il faut",
   f"rule 1 (punctuation): the print has a colon in 'homomorphisme d'anneaux : A(Y) → A(X)' ({B}, p. 96; print "
   f"checked)", "punctuation")
ch(F1, 96, r"$\theta_x^{\#}$ soit un homomorphisme local~:", r"$\theta_x^{\sharp}$ soit un homomorphisme local~:",
   f"rule 1 (symbol): the print has ♯ in θ_x^♯ (Théorème (1.7.3)), not # ({B}, p. 96)", "sharp")
ch(F1, 96, r"soit un homomorphisme local~:", r"soit un homomorphisme \textup{local}~:",
   f"conv. 6: 'local' is printed in roman inside the italic Théorème (1.7.3) ({B}, p. 96; print checked)", "conv6")

# ------------------------------------------------------------------ p. 97 (ega1-1-fr.tex)
ch(F1, 97, r"que $\widetilde\varphi_x^{\#}$ est", r"que $\widetilde\varphi_x^{\sharp}$ est",
   f"rule 1 (symbol): the print has ♯ in φ̃_x^♯, not # ({B}, p. 97)", "sharp")
ch(F1, 97, r"L'hypothèse sur $\theta_x^{\#}$", r"L'hypothèse sur $\theta_x^{\sharp}$",
   f"rule 1 (symbol): the print has ♯ in θ_x^♯, not # ({B}, p. 97)", "sharp")
ch(F1, 97, r"$k(\psi(x))$ dans le corps des restes", r"$\boldsymbol{k}(\psi(x))$ dans le corps des restes",
   f"conv. 1: bold italic k in 'du corps des restes k(ψ(x))' ({B}, p. 97)", "conv1")
ch(F1, 97, r"dans le corps des restes $k(x)$, tel que", r"dans le corps des restes $\boldsymbol{k}(x)$, tel que",
   f"conv. 1: bold italic k in 'dans le corps des restes k(x)' ({B}, p. 97)", "conv1")
ch(F1, 97, r"\ar[r]_{\theta_x^{\#}} & A_x", r"\ar[r]_{\theta_x^{\sharp}} & A_x",
   f"rule 1 (symbol): the print has ♯ in the diagram label θ_x^♯, not # ({B}, p. 97)", "sharp")
bold0(97, "3.7.2", src=B)
ch(F1, 97, r"$\theta_x^{\#}$ est égal", r"$\theta_x^{\sharp}$ est égal",
   f"rule 1 (symbol): the print has ♯ in θ_x^♯, not # ({B}, p. 97)", "sharp")
bold0(97, "1.5.1", ctx_after="). Comme la donnée", src=B)
ch(F1, 97, r"Comme la donnée des $\theta_x^{\#}$", r"Comme la donnée des $\theta_x^{\sharp}$",
   f"rule 1 (symbol): the print has ♯ in θ_x^♯, not # ({B}, p. 97)", "sharp")
ch(F1, 97, r"complètement $\theta^{\#}$, et", r"complètement $\theta^{\sharp}$, et",
   f"rule 1 (symbol): the print has ♯ in θ^♯, not # ({B}, p. 97)", "sharp")
bold0(97, "3.7.1", ctx_after="), on en conclut", src=B)
ch(F1, 97, r"$\varphi_x^{\#}:B_{{}^a\varphi(x)}\to A_x$", r"$\varphi_x^{\sharp}:B_{{}^a\varphi(x)}\to A_x$",
   f"rule 1 (symbol): the print has ♯ in φ_x^♯ (proof of Cor. (1.7.5)), not # ({B}, p. 97)", "sharp")
bold0(97, "1.5.1", ctx_after=")~; d'où la conclusion", src=B)
bold0(97, "4.1.1", ctx_before="d'où la conclusion\n", ctx_after=").", src=B)

# ------------------------------------------------------------------ p. 97 (ega1-2-fr.tex, before \oldpage[I]{98})
ch(F2, 97, r"On appelle \emph{préschéma} un espace annelé", r"On appelle préschéma un espace annelé",
   f"conv. 6: 'préschéma' is in the same italics as the rest of Déf. (2.1.2); \\emph inside the italic environment "
   f"set it upright ({B}, p. 97; print checked)", "conv6")

misprints = [
    dict(page=90,
         where="proof of Théorème (1.4.1), c) ⇒ b), second line from the bottom of the page: 'donc au faisceau "
               "associé au module Ñ, conoyau de l'homomorphisme A_f^(I) → A_f^(J) correspondant'",
         print="associé au module $\\widetilde{N}$",
         correct="associé au module $N$ (N is the cokernel of A_f^(I) → A_f^(J); Ñ is the sheaf associated with it)",
         tex_did="keeps the printed reading",
         source=f"{A} (p. 90); {ERR3}: '(I, 1.4.1) Ligne 2 du bas de la p. 90, remplacer Ñ par N'"),
    dict(page=95,
         where="display (1.6.5.1): N'_x' ⊗_{A'_x'} (A_x)_[φ_x'] ⥲ N_x = (N' ⊗_A' A_[φ])_x",
         print="(A_x)_{[\\varphi_{x'}]}",
         correct="(A_x)_{[\\varphi_x]} (the homomorphism φ_x : A'_x' → A_x of (1.6.1), p. 94)",
         tex_did="had silently written $\\varphi_x$; changed back to the printed $\\varphi_{x'}$ in this pass",
         source=f"{B} (p. 95); not in the authors' errata lists (EGA II list 1, EGA III list 2)",
         confidence="low",
         note="The printed φ_x' is certain (print checked). (1.6.1), p. 94, names this homomorphism φ_x : A'_x' → A_x, "
              "which makes φ_x' look like a misprint; but the same proof writes (A_f)_[φ_f'] with the index f' of the "
              "source ring (and (0, 1.5.1) writes φ^{S'}), so φ_x' may be the authors' deliberate analogue. Check "
              "before correcting; if it is not a misprint, the corrected edition should read φ_x' as well."),
    dict(page=95,
         where="Corollaire (1.6.6), end of the statement: 'engendrent le A-module Γ(Φ*(N'))'",
         print="$\\Gamma(\\Phi^*(N'))$",
         correct="$\\Gamma(\\Phi^*(\\widetilde{N}'))$ (Φ* is applied to the sheaf Ñ', as earlier in the statement)",
         tex_did="had silently corrected it to $\\Gamma(\\Phi^*(\\widetilde{N'}))$; changed back to the printed "
                 "$\\Gamma(\\Phi^*(N'))$ in this pass",
         source=f"{B} (p. 95); not in the authors' errata lists (EGA II list 1, EGA III list 2)"),
]

marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def page_span(t, file, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    if file == F2 and page == 97:
        nxt = [s for n, s in cuts if n == 98]
        return 0, nxt[0]
    s = [p for n, p in cuts if n == page][0]
    later = [p for n, p in cuts if p > s]
    return s, (later[0] if later else len(t))


def replay(texts, items):
    """apply items to texts in order; return (texts, problems)"""
    problems = []
    texts = dict(texts)
    for it in items:
        f, page, old, new = it[0], it[1], it[2], it[3]
        t = texts[f]
        n = t.count(old)
        if n != 1:
            problems.append(f"p. {page}: old occurs {n} times in {f.split('/')[-1]}: {old[:70]!r}")
            continue
        pos = t.index(old)
        s, e = page_span(t, f, page)
        if not (s <= pos < e):
            problems.append(f"p. {page}: old not on its page: {old[:70]!r}")
        texts[f] = t.replace(old, new, 1)
    return texts, problems


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--dry"
    orig = {f: p.read_text(encoding="utf-8") for f, p in ORIG.items()}
    if mode in ("--dry", "--apply"):
        current = {f: (E / f).read_text(encoding="utf-8") for f in (F1, F2)}
        for f in (F1, F2):
            if current[f] != orig[f]:
                sys.exit(f"{f} differs from the saved unedited copy; stop")
        edited, problems = replay(current, changes)
        for p in problems:
            print("PROBLEM", p)
        kinds = Counter(c[5] for c in changes)
        print(len(changes), "changes;", dict(sorted(kinds.items())))
        if problems:
            sys.exit("not applied")
        if mode == "--apply":
            for f in (F1, F2):
                with open(E / f, "w", encoding="utf-8", newline="") as h:
                    h.write(edited[f])
            with open(LOG, "w", encoding="utf-8", newline="\n") as h:
                for f, page, old, new, why, kind in changes:
                    h.write(json.dumps(dict(file=f, page=page, old=old, new=new, why=why), ensure_ascii=False) + "\n")
            with open(MIS, "w", encoding="utf-8", newline="\n") as h:
                json.dump(misprints, h, ensure_ascii=False, indent=1)
                h.write("\n")
            print("applied; wrote", LOG.name, "and", MIS.name)
    elif mode == "--rewrite-logs":
        # rewrite the log and the misprint list from this script, without touching the TeX, after checking that the
        # change list replayed on the unedited copies gives exactly the current release files
        edited, problems = replay(orig, changes)
        same = all(edited[f] == (E / f).read_text(encoding="utf-8") for f in (F1, F2))
        if problems or not same:
            sys.exit(f"change list does not reproduce the current files ({problems}); logs not rewritten")
        with open(LOG, "w", encoding="utf-8", newline="\n") as h:
            for f, page, old, new, why, kind in changes:
                h.write(json.dumps(dict(file=f, page=page, old=old, new=new, why=why), ensure_ascii=False) + "\n")
        with open(MIS, "w", encoding="utf-8", newline="\n") as h:
            json.dump(misprints, h, ensure_ascii=False, indent=1)
            h.write("\n")
        print("rewrote", LOG.name, "and", MIS.name)
    elif mode == "--check":
        items = [json.loads(l) for l in open(LOG, encoding="utf-8") if l.strip()]
        items = [(d["file"], d["page"], d["old"], d["new"]) for d in items]
        edited, problems = replay(orig, items)
        for p in problems:
            print("PROBLEM", p)
        for f in (F1, F2):
            now = (E / f).read_text(encoding="utf-8")
            print(f.split("/")[-1], "replay reproduces the edited file:", edited[f] == now)
        # nothing outside pp. 90-97 changed
        t0, t1 = orig[F1], (E / F1).read_text(encoding="utf-8")
        k = "\\oldpage[I]{90}"
        print("ega1-1-fr.tex unchanged before p. 90:", t0[:t0.index(k)] == t1[:t1.index(k)])
        t0, t1 = orig[F2], (E / F2).read_text(encoding="utf-8")
        k = "\\oldpage[I]{98}"
        print("ega1-2-fr.tex unchanged from p. 98 on:", t0[t0.index(k):] == t1[t1.index(k):])
        print(len(items), "log lines")


if __name__ == "__main__":
    main()
