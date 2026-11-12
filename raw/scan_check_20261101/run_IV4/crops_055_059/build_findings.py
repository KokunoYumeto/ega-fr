"""Build findings_055_059.json and check that every fix's old string occurs exactly once."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_055_059.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, fix_null=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if fix_null else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


OM_NOTE = "Sheaf of differentials: italic Omega (\\varOmega) in the print (GLOBAL_ISSUES 92)."
RESP_NOTE = "'(resp.', 'resp.' and ')' are roman inside the italic statement (GLOBAL_ISSUES 96)."
LBL_NOTE = "Roman-numeral label upright in the print (GLOBAL_ISSUES 16)."
OUTSIDE = ("OUTSIDE the page's file segment: this text of printed p. 56 is in ega4-17-fr.tex before "
           "its first marker (\\oldpage[IV-4]{57}, line 32); 'old' is unique there.")

# ---------------------------------------------------------------- page 55
add(55, "Remarques (16.11.3) (i): 'la O_U-Algèbre 𝒟iff_{U/S} soit commutative'",
    "script D followed by italic 'iff' (crop p55_s1_diff_z.png)",
    "\\operatorname{Diff}_{U/S}: roman 'Diff'", "font", None, "high",
    r"$\operatorname{Diff}_{U/S}$ soit", r"$\mathscr{D}\!iff_{U/S}$ soit",
    "The sheaf of operators (an O_U-Algèbre) is the script one; ega4-16 writes it \\mathscr{D}\\!iff in (16.8.6)-(16.8.7), "
    "\\operatorname{Diff} being the group Diff_{X/S}.")
add(55, "Remarques (16.11.3) (ii): 'sont les ε_λ = (ε_λμ)_{μ∈L}'",
    "ε_λ has the same light ε as the components ε_λμ on the same line and as the homomorphism ε of p. 95 "
    "(crops p55_s1_eps_z.png, p55_s1_eps1_z.png, p95_s3_eps_z.png); no bold Greek",
    "\\boldsymbol{\\varepsilon}_\\lambda (bold) against plain \\varepsilon_{\\lambda\\mu}", "font", None, "medium",
    r"$\boldsymbol{\varepsilon}_\lambda" + NL + r"  =(", r"$\varepsilon_\lambda" + NL + r"  =(",
    "The TeX bolds the multi-index ε_λ (like the bold p, q); the print does not distinguish it from ε_λμ.")
add(55, "Remarques (16.11.3) (ii): 'les opérateurs D_{ε_λ}'",
    "light ε in the subscript, as in ε_λ above (crop p55_s1_Deps_z.png)",
    "D_{\\boldsymbol{\\varepsilon}_\\lambda}", "font", None, "medium",
    r"$D_{\boldsymbol{\varepsilon}_\lambda}$", r"$D_{\varepsilon_\lambda}$",
    "Same ε as the previous entry. The italic D (operator) is right.")
add(55, "Remarques (16.11.3) (ii): 'les S-dérivations D_i introduites dans (16.5.7)'",
    "roman D (crop p55_s1_Di_z.png); the operators D_p, D_{ε_λ} on this page are italic",
    "$D_i$: italic D", "font", None, "high",
    r"dérivations $D_i$ introduites", r"dérivations $\mathrm{D}_i$ introduites",
    "The derivations D_i (and D_λ below) are roman in the print, as in (16.5.8) p. 29; the differential operators "
    "D_p italic (GLOBAL_ISSUES 97).")
add(55, "Remarques (16.11.3) (ii): 'combinaison linéaire de puissances des D_i (cf. (16.12))'",
    "roman D (crop p55_s1_Di2_z.png)", "$D_i$: italic D", "font", None, "high",
    r"puissances des $D_i$ (cf.", r"puissances des $\mathrm{D}_i$ (cf.",
    "As the previous D_i.")
add(55, "Remarques (16.11.3) (iii): 'si, dans la condition a), on remplace'",
    "label a) italic, parenthesis included (crop p55_s2_a_z.png)", "plain 'a)' (upright)", "italics", None, "high",
    r"la condition a)", r"la condition \emph{a)}",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88); the remark body is judged as roman.")
add(55, "Remarques (16.11.3) (iii): 'équivalente à la condition b) dans laquelle'",
    "label b) italic (crop p55_s2_b_z.png)", "plain 'b)' (upright)", "italics", None, "high",
    r"la condition b)", r"la condition \emph{b)}", "As a).")
add(55, "Remarques (16.11.3) (iii), display S^m_{O_X}(Ω^1_{X/S}) → 𝒢r_m(𝒫_{X/S})",
    "italic Ω (crop p55_s2_disp_z.png)", "\\Omega (upright)", "font", None, "high",
    r"\mathbf{S}_{\mathcal{O}_X}^m(\Omega_{X/S}^1)", r"\mathbf{S}_{\mathcal{O}_X}^m(\varOmega_{X/S}^1)", OM_NOTE)
add(55, "heading 16.12: '... critère jacobien pour les morphismes différentiellement lisses.'",
    "full stop after the title", "no full stop", "punctuation", None, "high",
    r"morphismes différentiellement lisses}", r"morphismes différentiellement lisses.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same form as the pp. 5-16 page fixes.")
add(55, "(16.12.1): 'est de caractéristique p (0, 21.1.1)'",
    "bold 0, no subscript (crop p55_s3_refs_z.png)", "plain 0", "convention", 2, "high",
    r"(0, 21.1.1)", r"(\textbf{0}, 21.1.1)")
add(55, "(16.12.1): 'Il résulte de (0, 21.1.3)'",
    "bold 0, no subscript (crop p55_s3_refs_z.png)", "plain 0", "convention", 2, "high",
    r"(0, 21.1.3)", r"(\textbf{0}, 21.1.3)")
add(55, "(16.12.1): 'le corps résiduel k(x)'",
    "bold italic k (crop p55_s3_k_z.png)", "plain k", "convention", 1, "high",
    r"le corps résiduel $k(x)$", r"le corps résiduel $\boldsymbol{k}(x)$")
add(55, "Théorème (16.12.2): 'Si Ω^1_{X/S} est un O_X-Module localement libre'",
    "italic Ω", "\\Omega (upright)", "font", None, "high",
    r"$\Omega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement libre",
    r"$\varOmega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement libre", OM_NOTE)
add(55, "proof of (16.12.2): 'soit une base du O_X-Module Ω^1_{X/S}. Appliquant'",
    "italic Ω", "\\Omega (upright)", "font", None, "high",
    r"Module $\Omega_{X/S}^1$." + NL + r"Appliquant", r"Module $\varOmega_{X/S}^1$." + NL + r"Appliquant", OM_NOTE)
add(55, "proof of (16.12.2), display D_p = (p!)^{-1} Π_λ D_λ^{p_λ}",
    "D_p italic, D_λ roman (crop p55_s3_Dp_z.png)", "D_\\lambda italic", "font", None, "high",
    r"\prod_\lambda D_\lambda^{p_\lambda}", r"\prod_\lambda \mathrm{D}_\lambda^{p_\lambda}",
    "The coordinate forms (derivations) D_λ are roman, the operator D_p italic, as for D_i above (GLOBAL_ISSUES 97).")
add(55, "proof of (16.12.2): '(où les D_λ sont les formes coordonnées'",
    "roman D (crop p55_s4_Dl_z.png)", "D_\\lambda italic", "font", None, "high",
    r"(où les $D_\lambda$ sont", r"(où les $\mathrm{D}_\lambda$ sont", "As in the display.")
add(55, "proof of (16.12.2): 'du fait que les D_λ sont des dérivations'",
    "roman D", "D_\\lambda italic", "font", None, "high",
    r"que les $D_\lambda$ sont des dérivations", r"que les $\mathrm{D}_\lambda$ sont des dérivations",
    "As in the display.")
add(55, "Remarques (16.11.3) (i): 'les D_p ne permutant aux produits par les sections de O_U que si n = 0'",
    "'n = 0'", "'n=0': keeps the printed reading", "misprint_in_print", None, "low",
    None, None,
    "n is not defined in (16.11.1)-(16.11.3); the D_p commute with the products by sections only for p = 0 "
    "(D_0 = identity). Possibly the authors' loose notation for the order |p| = n of D_p; check before the corrected "
    "edition changes it. No erratum found in Liste 3.",
    corrected=r"$\mathbf{p}=0$", fix_null=True)

# ---------------------------------------------------------------- page 56
add(56, "(16.12.3), l. 1: 'que Ω^1_{X/S} est de rang 1'",
    "italic Ω (crop p56_s1_omega_z.png)", "\\Omega (upright)", "font", None, "high",
    r"que $\Omega_{X/S}^1$ est de rang", r"que $\varOmega_{X/S}^1$ est de rang", OM_NOTE)
add(56, "(16.12.3): 'jusqu'à l'ordre p—1 (16.11.3, (iii))'",
    "long dash for the minus (crop p56_s1_pm1_z.png)", "-", "convention", 7, "high",
    r"l'ordre $p-1$", r"l'ordre $p\setmin 1$",
    "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(56, "(16.12.3): 'prouve que si Ω^1_{X/S} est localement libre'",
    "italic Ω", "\\Omega (upright)", "font", None, "high",
    r"$\Omega_{X/S}^1$ est localement libre, et si", r"$\varOmega_{X/S}^1$ est localement libre, et si", OM_NOTE)
add(56, "§ 17, introduction: 'les notions étudiées dans (0, 19), exprimées'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"étudiées dans (0, 19), exprimées", r"étudiées dans (\textbf{0}, 19), exprimées", OUTSIDE)
add(56, "§ 17, introduction: 'déjà rencontrées dans (0, 19). Pour des résultats'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"rencontrées dans (0, 19). Pour", r"rencontrées dans (\textbf{0}, 19). Pour", OUTSIDE)
add(56, "heading 17.1: '... morphismes formellement étales.'",
    "full stop after the title", "no full stop", "punctuation", None, "high",
    r"morphismes formellement étales}", r"morphismes formellement étales.}",
    "GLOBAL_ISSUES 43/58. " + OUTSIDE)
add(56, "Définition (17.1.1): 'formellement lisse (resp. formellement non ramifié ou formellement net, resp. "
         "formellement étale) si,'",
    "'(resp.', 'resp.' and ')' roman, like the defined terms; 'ou' italic (crop p56_s2_def2.png)",
    "'(resp.', ', resp.' and ')' italic inside the definition", "convention", 6, "high",
    r"(resp. \emph{formellement non ramifié} ou \emph{formellement net}, resp. \emph{formellement étale}) si,",
    r"\textup{(resp.}\ \emph{formellement non ramifié} ou \emph{formellement net}, \textup{resp.}\ "
    r"\emph{formellement étale}\textup{)} si,",
    RESP_NOTE + " " + OUTSIDE)
add(56, "Définition (17.1.1): 'si, pour tout schéma affine Y', tout sous-schéma fermé'",
    "'schéma affine' roman (emphasized) inside the italic definition (crop p56_s2_schaff_z2.png)",
    "italic like the rest of the definition", "italics", None, "high",
    r"pour tout schéma affine $Y'$", r"pour tout \emph{schéma affine} $Y'$", OUTSIDE)
add(56, "Définition (17.1.1), end: 'est surjective (resp. injective, resp. bijective).'",
    "'est surjective', 'injective', 'bijective' italic like the statement; '(resp.', 'resp.', ')' roman "
    "(crop p56_s3_surj_z.png)",
    "\\emph{surjective} etc. come out upright; '(resp.' and ')' italic", "convention", 6, "high",
    r"est \emph{surjective} (resp. \emph{injective}, resp. \emph{bijective}).",
    r"est surjective \textup{(resp.}\ injective, \textup{resp.}\ bijective\textup{)}.",
    "One edit for two differences: convention 6 for '(resp.', 'resp.' and ')', and the \\emph that sets the three "
    "adjectives upright inside the italic definition (italics). " + OUTSIDE)
add(56, "after (17.1.1): '... resp. formellement étale) sur Y.'",
    "'sur' italic (crop p56_s3_sur_z.png)", "'sur' upright", "italics", None, "high",
    r"étale}) sur $Y$.", r"étale}) \emph{sur} $Y$.",
    OUTSIDE + " The same string occurs once more later in ega4-17-fr.tex: apply in lines 1-31 only.")
add(56, "Remarques (17.1.2) (i): 'En vertu de (0, 19.3.1 et 0, 19.10.1)'",
    "both 0 bold (crop p56_s3_refs_z.png)", "plain 0 twice", "convention", 2, "high",
    r"(0, 19.3.1 et 0, 19.10.1)", r"(\textbf{0}, 19.3.1 et \textbf{0}, 19.10.1)", OUTSIDE)
add(56, "Remarques (17.1.2) (i): 'fait de B une A-algèbre formellement lisse'",
    "'algèbre' italic with 'formellement lisse' (crop p56_s3_alg_z.png)", "'algèbre' roman", "italics", None, "high",
    r"$A$-algèbre \emph{formellement lisse}", r"$A$-\emph{algèbre formellement lisse}",
    "The remark body is judged as roman. " + OUTSIDE)
add(56, "Remarques (17.1.2) (ii): 'l'Idéal 𝒥^{j+1} pour 0≤j≤n—1'",
    "long dash for the minus (crop p56_s4_nm1_z.png)", "-", "convention", 7, "high",
    r"pour $0\leq j\leq n-1$", r"pour $0\leq j\leq n\setmin 1$",
    "Long dash for the minus sign (GLOBAL_ISSUES 23). " + OUTSIDE)
add(56, "Remarques (17.1.2) (ii), last display: 'Hom_Y(Y'_{j+1}, X) → Hom_Y(Y'_j, X)    (0≤j≤n—1)'",
    "space before the condition", "'qquad' without its backslash (prints the letters 'qquad')", "other", None, "high",
    r"X)qquad", r"X)\qquad",
    "GLOBAL_ISSUES 96 (ega4-17-fr.tex line 30). Independent of the next entry (no shared characters). " + OUTSIDE)
add(56, "Remarques (17.1.2) (ii), last display: condition '(0≤j≤n—1)'",
    "long dash for the minus (crop p56_s4_disp_nm1_z.png)", "-", "convention", 7, "high",
    r"(0\leq j\leq n-1)", r"(0\leq j\leq n\setmin 1)",
    "Long dash for the minus sign (GLOBAL_ISSUES 23). " + OUTSIDE)

# ---------------------------------------------------------------- page 57
add(57, "Remarques (17.1.2) (iii): 'du foncteur représentable (0_III, 8.1.8)'",
    "bold 0 with subscript III, text-mode reference (crop p57_s1_ref_z.png)",
    "$(0_{\\mathrm{III}}, 8.1.8)$: plain 0, whole reference in math mode", "convention", 2, "high",
    r"$(0_{\mathrm{III}}, 8.1.8)$", r"($\mathbf{0}_{\mathrm{III}}$, 8.1.8)",
    "Written as the edition's other (0_I, ...) references.")
add(57, "Remarques (17.1.2) (iii), display: 'Y' ⇝ Hom_Y(Y', X)'",
    "wavy arrow (crop p57_s1_leadsto_z.png)", "\\longmapsto", "symbol", None, "high",
    r"Y'\longmapsto\Hom_Y(Y',X)", r"Y'\leadsto\Hom_Y(Y',X)", "Wavy arrow in the print (GLOBAL_ISSUES 33).")
add(57, "Proposition (17.1.3), label (i)", "upright '(i)' (crop p57_s3_l1.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]", LBL_NOTE)
add(57, "Proposition (17.1.3), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", LBL_NOTE)
add(57, "Proposition (17.1.3) (ii): '... formellement lisses (resp. formellement non ramifiés, resp. formellement "
         "étales) est formellement lisse (resp. formellement non ramifié, resp. formellement étale).'",
    "'(resp.', 'resp.' and ')' roman, twice (crops p57_s3_l2.png, p57_s3_l3.png)", "italic", "convention", 6, "high",
    r"lisses (resp. formellement non ramifiés, resp. formellement étales) est formellement lisse "
    r"(resp. formellement non ramifié, resp. formellement étale).",
    r"lisses \textup{(resp.}\ formellement non ramifiés, \textup{resp.}\ formellement étales\textup{)} est "
    r"formellement lisse \textup{(resp.}\ formellement non ramifié, \textup{resp.}\ formellement étale\textup{)}.",
    RESP_NOTE)
add(57, "Proposition (17.1.3), label (iii)", "upright '(iii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(iii)] Si", r"\item[\textup{(iii)}] Si", LBL_NOTE)
add(57, "Proposition (17.1.3) (iii): 'S-morphisme formellement lisse (resp. formellement non ramifié, resp. "
         "formellement étale), il en est'",
    "'(resp.', 'resp.' and ')' roman (crop p57_s3_l4.png)", "italic", "convention", 6, "high",
    r"lisse (resp. formellement non ramifié, resp. formellement étale), il en est de même de $f_{(S')}",
    r"lisse \textup{(resp.}\ formellement non ramifié, \textup{resp.}\ formellement étale\textup{)}, il en est "
    r"de même de $f_{(S')}",
    RESP_NOTE)
add(57, "Proposition (17.1.3), label (iv)", "upright '(iv)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(iv)] Si", r"\item[\textup{(iv)}] Si", LBL_NOTE)
add(57, "Proposition (17.1.3) (iv): 'S-morphismes formellement lisses (resp. formellement non ramifiés, resp. "
         "formellement étales), il en est'",
    "'(resp.', 'resp.' and ')' roman (crop p57_s3_l5.png)", "italic", "convention", 6, "high",
    r"lisses (resp. formellement non ramifiés, resp. formellement étales), il en est de même de $f\times_S g",
    r"lisses \textup{(resp.}\ formellement non ramifiés, \textup{resp.}\ formellement étales\textup{)}, il en est "
    r"de même de $f\times_S g",
    RESP_NOTE)
add(57, "Proposition (17.1.3), label (v)", "upright '(v)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(v)]", r"\item[\textup{(v)}]", LBL_NOTE)
add(57, "Proposition (17.1.3), label (vi)", "upright '(vi)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(vi)]", r"\item[\textup{(vi)}]", LBL_NOTE)
add(57, "after (17.1.3): 'En vertu de (I, 5.5.12)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.5.12)", r"(\textbf{I}, 5.5.12)")

# ---------------------------------------------------------------- page 58
add(58, "page break 57/58 inside 'Z-mor-|phisme': printed p. 58 begins 'phisme u_0 : Z'_0 → X'",
    "p. 57 ends 'considérons un Z-mor-', p. 58 begins 'phisme' (page_057_s4.png, page_058_s1.png)",
    "\\oldpage[IV-4]{58} before '$Z$-morphisme'", "marker", None, "high",
    r"\oldpage[IV-4]{58}" + NL + r"$Z$-morphisme $u_0", r"$Z$-mor%" + NL + r"\oldpage[IV-4]{58}" + NL + r"phisme $u_0",
    "One atomic edit inside the p. 58 segment: moves the marker to the printed word break (as homo%|morphisme, "
    "0_IV-1 p. 138; la fonc%|tion, IV-3 p. 93); \\oldpage ends with \\ignorespaces, so the word prints whole.")
add(58, "proof of (17.1.3) (ii): 'il existe un morphisme u : Z → X tel que f∘u = v'",
    "u : Z → X, no prime on Z (crop p58_s1_uZX_z.png)", "$u:Z'\\to X$: silent correction",
    "misprint_in_print", None, "high",
    r"$u:Z'\to X$ tel que", r"$u:Z\to X$ tel que",
    "v : Z' → Y and u∘j = u_0 with j : Z'_0 → Z', so u is defined on Z'. The diplomatic text restores the printed "
    "Z. No erratum found in Liste 3.",
    corrected=r"$u:Z'\to X$")
add(58, "proof of (17.1.3) (iii): 'on sait alors (I, 3.3.8)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 3.3.8)", r"(\textbf{I}, 3.3.8)")
add(58, "proof of (17.1.3) (iii): 'et Hom_{Y'}(Y''_0, X') à Hom_Y(Y'', X)'",
    "Hom_Y(Y'', X): no subscript 0 (crops p58_s2_hom.png, p58_s2_hom_z.png)",
    "$\\Hom_Y(Y''_0,X)$: silent correction", "misprint_in_print", None, "high",
    r"à $\Hom_Y(Y''_0,X)$", r"à $\Hom_Y(Y'',X)$",
    "Hom_{Y'}(Y''_0, X') identifies with Hom_Y(Y''_0, X); the print repeats Hom_Y(Y'', X) of the first "
    "identification. No erratum found in Liste 3.",
    corrected=r"$\Hom_Y(Y''_0,X)$")
add(58, "Proposition (17.1.4): 'si g∘f est formellement lisse (resp. formellement étale), il en est de même de f'",
    "'(resp.' and ')' roman (crop p58_s2_prop4.png)", "italic", "convention", 6, "high",
    r"lisse (resp. formellement étale), il en est de même de $f$.",
    r"lisse \textup{(resp.}\ formellement étale\textup{)}, il en est de même de $f$.", RESP_NOTE)
add(58, "Corollaire (17.1.5): 'soit formellement lisse (resp. formellement non ramifié, resp. formellement "
         "étale), il faut et il suffit que f le soit'",
    "'(resp.', 'resp.' and ')' roman (crop p58_s3_cor5.png)", "italic", "convention", 6, "high",
    r"lisse (resp. formellement non ramifié, resp. formellement étale), il faut et il suffit que $f$ le soit.",
    r"lisse \textup{(resp.}\ formellement non ramifié, \textup{resp.}\ formellement étale\textup{)}, il faut et il "
    r"suffit que $f$ le soit.",
    RESP_NOTE)
add(58, "Proposition (17.1.6), label (i)", "upright '(i)' (crop p58_s3_prop6.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]", LBL_NOTE)
add(58, "Proposition (17.1.6) (i): 'Pour que f soit formellement lisse (resp. ...), il faut et il suffit que chacun "
         "des morphismes'",
    "'(resp.', 'resp.' and ')' roman (crop p58_s3_prop6.png)", "italic", "convention", 6, "high",
    r"lisse (resp. formellement non ramifié, resp. formellement étale), il faut et il suffit que chacun des",
    r"lisse \textup{(resp.}\ formellement non ramifié, \textup{resp.}\ formellement étale\textup{)}, il faut et il "
    r"suffit que chacun des",
    RESP_NOTE)
add(58, "Proposition (17.1.6), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", LBL_NOTE)
add(58, "Proposition (17.1.6) (ii): 'Pour que f soit formellement lisse (resp. ...), il faut et il suffit que "
         "chacune des restrictions'",
    "'(resp.', 'resp.' and ')' roman (crop p58_s3_prop6ii.png)", "italic", "convention", 6, "high",
    r"lisse (resp. formellement non ramifié, resp. formellement étale), il faut et il suffit que chacune des",
    r"lisse \textup{(resp.}\ formellement non ramifié, \textup{resp.}\ formellement étale\textup{)}, il faut et il "
    r"suffit que chacune des",
    RESP_NOTE)

# ---------------------------------------------------------------- page 59
add(59, "heading 17.2: 'Propriétés différentielles générales.'", "full stop after the title", "no full stop",
    "punctuation", None, "high",
    r"\subsection{Propriétés différentielles générales}", r"\subsection{Propriétés différentielles générales.}",
    "GLOBAL_ISSUES 43/58.")
add(59, "Proposition (17.2.1): 'il faut et il suffit que Ω^1_f = 0'", "italic Ω (crop p59_s3_prop1.png)",
    "\\Omega (upright)", "font", None, "high",
    r"que $\Omega_f^1=0$", r"que $\varOmega_f^1=0$", OM_NOTE)
add(59, "Proposition (17.2.1): '(ce qu'on écrit encore Ω^1_{X/Y} = 0 (16.3.1))'",
    "the whole parenthesis roman inside the italic statement; italic Ω (crop p59_s3_prop1.png)",
    "italic text; \\Omega upright", "convention", 6, "high",
    r"(ce qu'on écrit encore $\Omega_{X/Y}^1=0$ (16.3.1))",
    r"\textup{(ce qu'on écrit encore $\varOmega_{X/Y}^1=0$ (16.3.1))}",
    "One edit for two differences: convention 6 for the roman parenthesis, and the italic Omega of the sheaf of "
    "differentials (font).")
add(59, "proof of (17.2.1): 'résulte alors de (0, 20.7.4)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.7.4)", r"(\textbf{0}, 20.7.4)")
add(59, "proof of (17.2.1): 'l'interprétation de Ω^1_{X/Y} dans ce cas (16.3.7)'", "italic Ω",
    "\\Omega (upright)", "font", None, "high",
    r"l'interprétation de $\Omega_{X/Y}^1$ dans ce cas", r"l'interprétation de $\varOmega_{X/Y}^1$ dans ce cas",
    OM_NOTE)
add(59, "Corollaire (17.2.2): 'l'homomorphisme canonique (16.4.19)'",
    "reference upright (crop p59_s3_cor2.png)", "italic (inside the italic statement)", "convention", 6, "high",
    r"canonique (16.4.19)", r"canonique \textup{(16.4.19)}")
add(59, "Corollaire (17.2.2), display f^*(Ω^1_{Y/Z}) → Ω^1_{X/Z}", "italic Ω twice", "\\Omega (upright) twice",
    "font", None, "high",
    r"f^*(\Omega_{Y/Z}^1)\longrightarrow\Omega_{X/Z}^1" + NL + r"\]",
    r"f^*(\varOmega_{Y/Z}^1)\longrightarrow\varOmega_{X/Z}^1" + NL + r"\]", OM_NOTE)
add(59, "Proposition (17.2.3), label (i)", "upright '(i)' (crop p59_s4_prop3.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]", LBL_NOTE)
add(59, "Proposition (17.2.3) (i): 'Le O_X-Module Ω^1_{X/Y} est localement projectif'", "italic Ω",
    "\\Omega (upright)", "font", None, "high",
    r"-Module $\Omega_{X/Y}^1$ est", r"-Module $\varOmega_{X/Y}^1$ est", OM_NOTE)
add(59, "Proposition (17.2.3) (i): 'localement projectif (16.10.1)'", "reference upright (crop p59_s4_prop3.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"projectif (16.10.1)", r"projectif \textup{(16.10.1)}")
add(59, "Proposition (17.2.3) (i): 'Ω^1_{X/Y} est localement libre de type fini'", "italic Ω",
    "\\Omega (upright)", "font", None, "high",
    r"fini, $\Omega_{X/Y}^1$ est localement libre", r"fini, $\varOmega_{X/Y}^1$ est localement libre", OM_NOTE)
add(59, "Proposition (17.2.3), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", LBL_NOTE)
add(59, "Proposition (17.2.3) (ii): 'la suite (16.4.19) de O_X-Modules'", "reference upright",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"la suite (16.4.19) de", r"la suite \textup{(16.4.19)} de")
add(59, "Proposition (17.2.3), display (17.2.3.1)", "italic Ω three times", "\\Omega (upright) three times",
    "font", None, "high",
    r"0\longrightarrow f^*(\Omega_{Y/Z}^1)\longrightarrow\Omega_{X/Z}^1\longrightarrow\Omega_{X/Y}^1\longrightarrow0",
    r"0\longrightarrow f^*(\varOmega_{Y/Z}^1)\longrightarrow\varOmega_{X/Z}^1\longrightarrow\varOmega_{X/Y}^1"
    r"\longrightarrow0",
    OM_NOTE)
add(59, "Proposition (17.2.3) (ii): 'des homomorphismes de (17.2.3.1) forment'",
    "reference upright (crop p59_s4_prop3b.png)", "italic (inside the italic statement)", "convention", 6, "high",
    r"de (17.2.3.1) forment", r"de \textup{(17.2.3.1)} forment")
add(59, "Proposition (17.2.3) (ii), end: 'forment une suite exacte et scindée.'",
    "'scindée' roman (emphasized) inside the italic statement (crop p59_s4_prop3b.png)",
    "italic like the rest of the statement", "italics", None, "high",
    r"exacte et scindée.", r"exacte et \emph{scindée}.")

# ---------------------------------------------------------------- checks
ok = True
texts = {p: (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(55, 60)}
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    n = texts[f["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print(f"#{i} page {f['page']}: old occurs {n} times: {fx['old']!r}")
# overlapping 'old' spans on the same page
for p in range(55, 60):
    spans = []
    for i, f in enumerate(F):
        if f["page"] == p and f["fix"]:
            s = texts[p].find(f["fix"]["old"])
            spans.append((s, s + len(f["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print(f"overlap page {p}: #{a[2]} and #{b[2]}")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in range(55, 60):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "OK" if ok else "PROBLEMS")
sys.exit(0 if ok else 1)
