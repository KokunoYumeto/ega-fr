import json, pathlib, sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_190_194.json"
NL = "\n"


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def bold0(page, where, num):
    return F(page, where, "bold 0", r"\hyperref[...]{0, " + num + "}", "convention", 2, "high",
             "{0, " + num + "}", r"{\textbf{0}, " + num + "}")


R = []
# ---------------- page 190 ----------------
R.append(F(190, "proof of (10.6.3): 'Il existe un homomorphisme d'anneaux φ_ji : A_i→A_j'",
           "d'anneaux with only 'anneaux' italic; the elided d' is roman",
           r"\emph{d'anneaux}", "italics", None, "high",
           r"\emph{d'anneaux}", r"d'\emph{anneaux}",
           "Checked on a crop at 2x: upright d and apostrophe before the italic word."))
R.append(F(190, "proof of (10.6.3): 'tel que u_ji = φ̃_ji (1.7.3)'",
           "tilde over φ only; the subscript ji stands outside the tilde",
           r"$u_{ji}=\widetilde{\varphi_{ji}}$", "convention", 8, "high",
           r"\widetilde{\varphi_{ji}}$" + NL + "(", r"\widetilde{\varphi}_{ji}$" + NL + "(",
           "Checked on a crop at 3x. 'old' spans the line break before (1.7.3)."))
R.append(F(190, "proof of (10.6.3): 'donc on a aussi u_ji = φ̃_ji, lorsque φ_ji est cette fois considéré'",
           "tilde over φ only; the subscript ji stands outside the tilde",
           r"$u_{ji}=\widetilde{\varphi_{ji}}$", "convention", 8, "high",
           "aussi" + NL + r"$u_{ji}=\widetilde{\varphi_{ji}}$", "aussi" + NL + r"$u_{ji}=\widetilde{\varphi}_{ji}$",
           "Checked on a crop at 3x. 'old' spans the line break after 'aussi'; it does not overlap the comma fix below."))
R.append(F(190, "proof of (10.6.3): 'donc on a aussi u_ji = φ̃_ji, lorsque φ_ji est cette fois considéré'",
           "comma after the formula: 'u_ji = φ̃_ji, lorsque'",
           r"$u_{ji}=\widetilde{\varphi_{ji}}$ lorsque $\varphi_{ji}$", "punctuation", None, "high",
           r" lorsque $\varphi_{ji}$", r", lorsque $\varphi_{ji}$",
           "Checked on a crop at 3x."))
R.append(F(190, "proof of (10.6.3): 'considéré comme homomorphisme de A_i-modules. Alors'",
           "'modules' italic: A_i-*modules* (the contrast with 'homomorphisme d'*anneaux*' above)",
           r"de $A_i$-modules.", "italics", None, "high",
           r"de $A_i$-modules.", r"de $A_i$-\emph{modules}.",
           "Checked on a crop at 2.5x."))
R.append(F(190, "proof of (10.6.3): 'le noyau de u_ji est un O_i-Module quasi-cohérent égal à 𝔍̃_ji'",
           "tilde over the Fraktur J only; the subscript ji stands outside the tilde",
           r"\widetilde{\mathfrak{J}_{ji}}", "convention", 8, "high",
           r"\widetilde{\mathfrak{J}_{ji}}", r"\widetilde{\mathfrak{J}}_{ji}",
           "Checked on a crop at 3x."))
R.append(F(190, "proof of (10.6.3): 'En particulier, on a 𝒥_i = 𝔍̃_i'",
           "tilde over the Fraktur J only; the subscript i stands outside the tilde",
           r"\widetilde{\mathfrak{J}_i}", "convention", 8, "high",
           r"\widetilde{\mathfrak{J}_i}", r"\widetilde{\mathfrak{J}}_i",
           "Checked on a crop at 3x."))
R.append(F(190, "proof of (10.6.3): 'L'hypothèse b) entraîne que 𝒥_i est nilpotent'",
           "label 'b)' italic (letter and parenthesis) in the roman proof",
           r"L'hypothèse b)", "italics", None, "high",
           r"L'hypothèse b)", r"L'hypothèse \emph{b)}",
           "Checked on a crop at 2.5x. Same on p. 192 ('conditions b) et c)')."))
R.append(F(190, "proof of (10.6.3): 'en effet, comme X est quasi-compact'",
           "roman X, not Fraktur: 'comme X est quasi-compact'",
           r"comme $\mathfrak{X}$", "misprint_in_print", None, "high",
           r"en effet, comme $\mathfrak{X}$", r"en effet, comme $X$",
           "The TeX silently corrects the print. Checked on a crop at 2x: plain roman X, while 'dans 𝔛' three lines up is Fraktur. "
           "The space of (10.6.3) is 𝔛 and no X is defined; the TeX keeps the same slip 'x∈X' in hypothesis b) on p. 189.",
           corrected=r"$\mathfrak{X}$"))
R.append(F(190, "proof of (10.6.3): 'on peut recouvrir X par un nombre fini d'ouverts U_k'",
           "roman X, not Fraktur",
           r"recouvrir $\mathfrak{X}$ par", "misprint_in_print", None, "high",
           r"recouvrir $\mathfrak{X}$ par", r"recouvrir $X$ par",
           "The TeX silently corrects the print. Checked on a crop at 2x. Same slip as 'comme X est quasi-compact' just before.",
           corrected=r"$\mathfrak{X}$"))
R.append(F(190, "proof of (10.6.3): 'l'anneau A = lim A_i est admissible (0, 7.2.2)'",
           "bold 0", r"(\hyperref[0.7.2.2-fr]{0, 7.2.2})", "convention", 2, "high",
           "{0, 7.2.2}", r"{\textbf{0}, 7.2.2}"))
R.append(F(190, "proof of (10.6.3), general case: 'qui est un ouvert affine pour tous les X_i'",
           "only 'ouvert affine' and 'tous' italic; 'pour' and 'les' roman",
           r"\emph{ouvert affine pour tous les $X_i$}", "italics", None, "high",
           r"\emph{ouvert affine pour tous les $X_i$}", r"\emph{ouvert affine} pour \emph{tous} les $X_i$",
           "Upright 'pour' and 'les' between the italic words, clearly visible in the strip."))
R.append(F(190, "proof of (10.6.3), last sentence: 'montre que (U, 𝒪_X|U) est un préschéma formel'",
           "(U, 𝒪_X|U) with a roman X subscript, not Fraktur",
           r"$(U,\mathscr{O}_{\mathfrak{X}}|U)$", "misprint_in_print", None, "high",
           r"$(U,\mathscr{O}_{\mathfrak{X}}|U)$", r"$(U,\mathscr{O}_X|U)$",
           "The TeX silently corrects the print. Checked on a crop at 2x: small roman X, unlike the Fraktur subscript of 𝒪_𝔛 "
           "elsewhere on the page. Same slip as 'comme X est quasi-compact' above.",
           corrected=r"$(U,\mathscr{O}_{\mathfrak{X}}|U)$"))
# ---------------- page 191 ----------------
R.append(F(191, "Corollaire (10.6.4): 'Si en outre X_0 est localement noethérien (resp. noethérien),'",
           "'(resp.' roman inside the italic statement; 'noethérien' italic",
           "(resp. noethérien),", "convention", 6, "high",
           "(resp. noethérien),", r"\textup{(resp.} noethérien),",
           "Checked on a crop at 3x: the closing parenthesis follows the italic word."))
R.append(F(191, "Corollaire (10.6.4): '𝔛 est localement noethérien (resp. noethérien).'",
           "'(resp.' roman inside the italic statement; 'noethérien' italic",
           "(resp. noethérien).", "convention", 6, "high",
           "(resp. noethérien).", r"\textup{(resp.} noethérien).",
           "Checked on a crop at 3x."))
R.append(F(191, "proof of (10.6.4): 'compte tenu des relations 𝒥_ij = 𝔍̃_ji'",
           "tilde over the Fraktur J only; the subscript ji stands outside the tilde",
           r"$\mathscr{J}_{ij}=\widetilde{\mathfrak{J}_{ji}}$", "convention", 8, "high",
           r"\widetilde{\mathfrak{J}_{ji}}", r"\widetilde{\mathfrak{J}}_{ji}",
           "Checked on a crop at 3x; the subscripts ij and ji are as in the TeX."))
R.append(F(191, "proof of (10.6.4): 'aux assertions correspondantes de (0, 7.2.7 et 7.2.8)'",
           "bold 0", r"(\hyperref[0.7.2.7-fr]{0, 7.2.7} et", "convention", 2, "high",
           "{0, 7.2.7}", r"{\textbf{0}, 7.2.7}"))
R.append(F(191, "proof of (10.6.5): 'donc est adique et noethérien (0, 7.2.8)'",
           "bold 0", r"(\hyperref[0.7.2.8-fr]{0, 7.2.8})", "convention", 2, "high",
           "{0, 7.2.8}", r"{\textbf{0}, 7.2.8}"))
# ---------------- page 192 ----------------
R.append(F(192, "(10.6.8): 'satisfaisant aux conditions b) et c) de (10.6.3)'",
           "labels 'b)' and 'c)' italic in the roman paragraph",
           "conditions b) et c) de", "italics", None, "high",
           "conditions b) et c) de", r"conditions \emph{b)} et \emph{c)} de",
           "Checked on a crop at 2.5x."))
R.append(F(192, "Proposition (10.6.9): '𝒥 (resp. 𝒦) un Idéal de définition de 𝔛'",
           "'(resp. 𝒦)' roman inside the italic statement",
           r"(resp. $\mathscr{K}$) un Idéal", "convention", 6, "high",
           r"(resp. $\mathscr{K}$) un Idéal", r"\textup{(resp. $\mathscr{K}$)} un Idéal",
           "Checked on a crop: 'resp.' and both parentheses upright."))
R.append(F(192, "Proposition (10.6.9): 'de 𝔛 (resp. 𝔜) ; l'application'",
           "'(resp. 𝔜)' roman inside the italic statement",
           r"(resp. $\mathfrak{Y}$)~;", "convention", 6, "high",
           r"(resp. $\mathfrak{Y}$)~;", r"\textup{(resp. $\mathfrak{Y}$)}~;",
           "Checked on a crop."))
R.append(F(192, "Proposition (10.6.9): 'l'application f→(f_n) définie dans (10.6.7)'",
           "plain arrow f→(f_n)",
           r"$f\mapsto(f_n)$", "convention", 3, "high",
           r"$f\mapsto(f_n)$", r"$f\to(f_n)$",
           "Checked on a crop at 3x: no bar at the tail of the arrow."))
R.append(F(192, "Proposition (10.6.9): 'définie dans (10.6.7)'",
           "(10.6.7) upright inside the italic statement",
           r"(\hyperref[I.10.6.7-fr]{10.6.7})", "convention", 6, "high",
           r"(\hyperref[I.10.6.7-fr]{10.6.7})", r"\textup{(\hyperref[I.10.6.7-fr]{10.6.7})}",
           "Checked on a crop at 2.5x."))
R.append(F(192, "Proposition (10.6.9): 'rendant commutatifs les diagrammes (10.6.7.1).'",
           "(10.6.7.1) upright inside the italic statement",
           r"(\hyperref[I.10.6.7.1-fr]{10.6.7.1}).", "convention", 6, "high",
           r"(\hyperref[I.10.6.7.1-fr]{10.6.7.1}).", r"\textup{(\hyperref[I.10.6.7.1-fr]{10.6.7.1})}.",
           "Checked on a crop at 2x."))
R.append(F(192, "proof of (10.6.9): 'f_n = (^aφ_n, φ̃_n)'",
           "tilde over φ only; the subscript n stands outside the tilde",
           r"\widetilde{\varphi_n}", "convention", 8, "high",
           r"\widetilde{\varphi_n}", r"\widetilde{\varphi}_n",
           "Checked on a crop at 3x."))
R.append(F(192, "Corollaire (10.6.10): '𝒯 le plus grand Idéal de définition de 𝔛 (10.5.4).'",
           "(10.5.4) upright inside the italic statement",
           r"(\hyperref[I.10.5.4-fr]{10.5.4})", "convention", 6, "high",
           r"(\hyperref[I.10.5.4-fr]{10.5.4})", r"\textup{(\hyperref[I.10.5.4-fr]{10.5.4})}"))
R.append(F(192, "Corollaire (10.6.10) (ii): 'rendant commutatifs les diagrammes (10.6.7.1), où X_n = ...'",
           "(10.6.7.1) upright inside the italic statement",
           r"(\hyperref[I.10.6.7.1-fr]{10.6.7.1}), où", "convention", 6, "high",
           r"(\hyperref[I.10.6.7.1-fr]{10.6.7.1}), où", r"\textup{(\hyperref[I.10.6.7.1-fr]{10.6.7.1})}, où"))
R.append(F(192, "proof of (10.6.10): 'topologiquement nilpotents (0, 7.1.4, (ii))'",
           "bold 0", r"(\hyperref[0.7.1.4-fr]{0, 7.1.4, (ii)})", "convention", 2, "high",
           "{0, 7.1.4, (ii)}", r"{\textbf{0}, 7.1.4, (ii)}"))
R.append(F(192, "proof of (10.6.10): 'éléments topologiquement nilpotents de A (0, 7.1.6)'",
           "bold 0", r"(\hyperref[0.7.1.6-fr]{0, 7.1.6})", "convention", 2, "high",
           "{0, 7.1.6}", r"{\textbf{0}, 7.1.6}"))
R.append(F(192, "Corollaire (10.6.11): 'Soit 𝒥 (resp. 𝒦, ℒ) un Idéal de définition'",
           "'(resp. 𝒦, ℒ)' roman inside the italic statement",
           r"(resp. $\mathscr{K}$, $\mathscr{L}$)", "convention", 6, "high",
           r"(resp. $\mathscr{K}$, $\mathscr{L}$)", r"\textup{(resp. $\mathscr{K}$, $\mathscr{L}$)}",
           "Checked on a crop: 'resp.' and both parentheses upright."))
R.append(F(192, "Corollaire (10.6.11): 'un Idéal de définition de 𝔖 (resp. 𝔛, 𝔜), et supposons que'",
           "'(resp. 𝔛, 𝔜)' roman inside the italic statement",
           r"(resp. $\mathfrak{X}$," + NL + r"$\mathfrak{Y}$)", "convention", 6, "high",
           r"(resp. $\mathfrak{X}$," + NL + r"$\mathfrak{Y}$)", r"\textup{(resp. $\mathfrak{X}$," + NL + r"$\mathfrak{Y}$)}",
           "'old' spans the line break after the comma."))
# ---------------- page 193 ----------------
R.append(F(193, "Corollaire (10.6.11), end: 'rendant commutatifs les diagrammes (10.6.7.1).'",
           "(10.6.7.1) upright inside the italic statement",
           r"(\hyperref[I.10.6.7.1-fr]{10.6.7.1}).", "convention", 6, "high",
           r"(\hyperref[I.10.6.7.1-fr]{10.6.7.1}).", r"\textup{(\hyperref[I.10.6.7.1-fr]{10.6.7.1})}."))
R.append(F(193, "Proposition (10.7.2): 'les 𝔖-morphismes correspondant (10.2.2) aux A-homomorphismes'",
           "(10.2.2) upright inside the italic statement",
           r"(\hyperref[I.10.2.2-fr]{10.2.2})", "convention", 6, "high",
           r"(\hyperref[I.10.2.2-fr]{10.2.2})", r"\textup{(\hyperref[I.10.2.2-fr]{10.2.2})}",
           "'(continus)' on the same line is italic in the print, as in the TeX (checked on a crop)."))
R.append(F(193, "proof of (10.7.2): 'la propriété universelle du produit tensoriel complété (0, 7.7.6)'",
           "bold 0", r"(\hyperref[0.7.7.6-fr]{0, 7.7.6})", "convention", 2, "high",
           "{0, 7.7.6}", r"{\textbf{0}, 7.7.6}"))
R.append(F(193, "(10.7.4), last line of the page: 'un sous-préschéma fermé de S_μ (resp. X_μ, Y_μ) ayant même [espace sous-jacent]'",
           "'même' italic; 'espace sous-jacent' at the top of p. 194 is roman",
           r"$Y_\mu$) ayant même", "italics", None, "high",
           r"$Y_\mu$) ayant même", r"$Y_\mu$) ayant \emph{même}",
           "Checked on crops of p. 193 and the top of p. 194. The earlier 'ayant même ensemble d'indices' in (10.7.4) is roman, as in the TeX."))
# ---------------- page 194 ----------------
R.append(F(194, "(10.7.4): 'un sous-préschéma fermé de X_μ ×_{S_μ} Y_μ ayant même espace sous-jacent (4.3.1)'",
           "'même' italic",
           "ayant même espace sous-jacent", "italics", None, "high",
           "ayant même espace", r"ayant \emph{même} espace",
           "Checked on a crop at 1.6x."))
R.append(F(194, "(10.7.4): 'du produit tensoriel complété de deux algèbres (0, 7.7.1)'",
           "bold 0", r"(\hyperref[0.7.7.1-fr]{0, 7.7.1})", "convention", 2, "high",
           "{0, 7.7.1}", r"{\textbf{0}, 7.7.1}"))
R.append(F(194, "(10.8.1): 'Soient X un préschéma (usuel) localement noethérien, X' une partie fermée'",
           "'localement noethérien' italic in the roman paragraph",
           "(usuel) localement noethérien,", "italics", None, "high",
           "(usuel) localement noethérien", r"(usuel) \emph{localement noethérien}",
           "Checked on a crop."))
R.append(F(194, "(10.8.1): 'l'ensemble des faisceaux cohérents d'idéaux 𝒥 dans O_X'",
           "'cohérents' italic",
           "faisceaux cohérents d'idéaux", "italics", None, "high",
           "faisceaux cohérents d'idéaux", r"faisceaux \emph{cohérents} d'idéaux",
           "Checked on a crop."))
R.append(F(194, "proof of (10.8.2): 'et l'on a 𝒥_x = (𝒥_1)_x ∩ (𝒥_2)_x, pour tout x ∈ X'",
           "comma after (𝒥_2)_x",
           r"$\mathscr{J}_x=(\mathscr{J}_1)_x\cap(\mathscr{J}_2)_x$ pour tout", "punctuation", None, "high",
           r"(\mathscr{J}_2)_x$ pour tout", r"(\mathscr{J}_2)_x$, pour tout",
           "Checked on a crop at 2x."))
R.append(F(194, "proof of (10.8.2): 'puisque O_X est cohérent (6.1.1 et 0, 5.3.4)'",
           "bold 0", r"\hyperref[0.5.3.4-fr]{0, 5.3.4})", "convention", 2, "high",
           "{0, 5.3.4}", r"{\textbf{0}, 5.3.4}"))
R.append(F(194, "(10.8.3): 'Soit maintenant ℱ un O_X-Module cohérent ; pour tout 𝒥 ∈ Φ'",
           "'cohérent' italic",
           r"$\mathscr{O}_X$-Module cohérent~; pour", "italics", None, "high",
           "Module cohérent~; pour", r"Module \emph{cohérent}~; pour",
           "Checked on a crop at 1.6x. The second 'cohérent' of (10.8.3) ('Module cohérent (9.1.1)') is roman, as in the TeX."))
R.append(F(194, "Définition (10.8.4): 'on appelle complété de ℱ le long de X' et on désigne'",
           "'complété de ℱ le long de X'' in italics like the rest of the definition (no change of face)",
           r"\emph{complété de $\mathscr{F}$ le long de $X'$}", "convention", 6, "high",
           r"\emph{complété de $\mathscr{F}$ le long de $X'$}", r"complété de $\mathscr{F}$ le long de $X'$",
           "\\emph inside the italic definition environment sets the words upright; drop the \\emph. Checked on a crop."))

# ---------------- validation ----------------
ok = True
pages = {}
for p in range(190, 195):
    pages[p] = (RUN / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
spans = {}
for i, x in enumerate(R):
    fx = x["fix"]
    if not fx:
        continue
    t = pages[x["page"]]
    c = t.count(fx["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", c, x["page"], repr(fx["old"]))
        continue
    s = t.index(fx["old"])
    spans.setdefault(x["page"], []).append((s, s + len(fx["old"]), i))
for p, L in spans.items():
    L.sort()
    for a, b in zip(L, L[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP on page", p, R[a[2]]["fix"]["old"], "|", R[b[2]]["fix"]["old"])
# sequential application test (as apply_fixes.py does)
for p in range(190, 195):
    t = pages[p]
    for x in R:
        if x["page"] == p and x["fix"]:
            if t.count(x["fix"]["old"]) != 1:
                ok = False
                print("SEQUENTIAL FAIL", p, repr(x["fix"]["old"]))
            t = t.replace(x["fix"]["old"], x["fix"]["new"])
if not ok:
    sys.exit(1)
json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in R:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(190, 195):
    print(p, {k: cnt[(p, k)] for k in ("normal", "convention", "misprint")})
print("total", len(R), "written to", OUT)
