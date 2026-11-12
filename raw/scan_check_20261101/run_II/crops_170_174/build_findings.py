import json, sys, os

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = os.path.join(RUN, "findings_170_174.json")

HATPRIME = "Same meaning; the analogue of convention 8 for a hat and a prime (as reported for EGA I pp. 66, 196)."
BOLDZ = ("The indeterminate z is bold upright in the print, as everywhere from (8.3.1.1) on (S[z]); "
         "ega2-1-fr.tex writes a plain z throughout (document-wide).")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": (None if old is None else {"old": old, "new": new})}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 170 ----------------
add(170, "Proposition (8.5.2), line 1", "(resp. E') upright in the italic statement",
    "(resp. $E'$) set italic by the proposition environment", "convention", 6, "high",
    r"(resp. $E'$)", r"\textup{(resp. $E'$)}", "Checked on a crop.")
add(170, "Proposition (8.5.2), line 1", "(resp. 𝒮') upright in the italic statement",
    "(resp. $\\mathcal{S}'$) set italic", "convention", 6, "high",
    r"(resp. $\mathcal{S}'$)", r"\textup{(resp. $\mathcal{S}'$)}", "Checked on a crop.")
add(170, "proof of (8.5.2), affine reduction", "𝒮' = S̃' (tilde over S only, prime after it)",
    "\\widetilde{S'}", "convention", 8, "high",
    r"$\mathcal{S}'=\widetilde{S'}$", r"$\mathcal{S}'=\widetilde{S}'$",
    "Checked on a 2x crop: the tilde covers only the S.")
add(170, "proof of (8.5.2), reference (I, 2.2.4.1)", "bold I", "plain I", "convention", 2, "high",
    r"{I, 2.2.4.1}", r"{\textbf{I}, 2.2.4.1}", "")
add(170, "proof of (8.5.2), 'lui-même ((2.8.1) et (2.3.14))'",
    "((2.8.1) et (2.3.14)): both references inside an outer pair of parentheses",
    "(2.8.1) et (2.3.14): outer parentheses missing", "punctuation", None, "high",
    r"(\hyperref[II.2.8.1-fr]{2.8.1}) et (\hyperref[II.2.3.14-fr]{2.3.14}),",
    r"((\hyperref[II.2.8.1-fr]{2.8.1}) et (\hyperref[II.2.3.14-fr]{2.3.14})),",
    "Checked on a crop.")
add(170, "(8.5.3.1)", "φ̂ : 𝒮̂ → 𝒮̂' (hat over 𝒮 only, prime after it)", "\\widehat{\\mathcal{S}'}",
    "formula", None, "high",
    r"\to\widehat{\mathcal{S}'}", r"\to\widehat{\mathcal{S}}'",
    "Checked on a 3x crop. " + HATPRIME)
add(170, "(8.5.3), 'en posant φ̂(z) = z'", "bold z (twice)", "plain z", "font", None, "high",
    r"$\widehat{\varphi}(z)=z$", r"$\widehat{\varphi}(\mathbf{z})=\mathbf{z}$",
    "Checked on a 2x crop. " + BOLDZ)
add(170, "(8.5.3), 'i' : C' → Ĉ''", "Ĉ' (hat over C only, prime after it)", "\\widehat{C'}",
    "formula", None, "high",
    r"$i':C'\to\widehat{C'}$", r"$i':C'\to\widehat{C}'$", HATPRIME)
add(170, "(8.5.3), 'j' : X' → Ĉ''", "Ĉ' (hat over C only, prime after it)", "\\widehat{C'}",
    "formula", None, "high",
    r"$j':X'\to\widehat{C'}$", r"$j':X'\to\widehat{C}'$", "Checked on a 3x crop. " + HATPRIME)
add(170, "last line of the page, before \\oldpage[II]{171}",
    "no paragraph break: 'et que le diagramme' runs on into the display (8.5.3.3) and 'est commutatif.' on p. 171",
    "blank line before the page-171 marker", "other", None, "high",
    "et que le diagramme\n\n", "et que le diagramme\n",
    "Spurious paragraph break before a display at a page break (GLOBAL_ISSUES item 20). "
    "The blank line is the last line of this page's segment, so the p. 171 checker cannot see it.")

# ---------------- page 171 ----------------
add(171, "Proposition (8.5.4), line 1", "(resp. Ê') upright; hat over E only, prime after it",
    "(resp. $\\widehat{E'}$) set italic", "convention", 6, "high",
    r"(resp. $\widehat{E'}$)", r"\textup{(resp. $\widehat{E}'$)}",
    "Checked on a crop. The fix also writes the printed Ê' (hat-and-prime analogue of convention 8; not reported separately).")
add(171, "Proposition (8.5.4), line 1", "(resp. 𝒮') upright in the italic statement",
    "(resp. $\\mathcal{S}'$) set italic", "convention", 6, "high",
    r"(resp. $\mathcal{S}'$)", r"\textup{(resp. $\mathcal{S}'$)}", "Checked on a crop.")
add(171, "Proposition (8.5.4), 'Φ̂^{-1}(Ê) ⊂ Ê''", "Ê' (hat over E only)", "\\widehat{E'}",
    "formula", None, "high",
    r"\subset\widehat{E'}$~;", r"\subset\widehat{E}'$~;", "Checked on a crop. " + HATPRIME)
add(171, "Proposition (8.5.4), 'p' : Ê' → X''", "Ê' (hat over E only)", "\\widehat{E'}",
    "formula", None, "high",
    r"$p':\widehat{E'}\to X'$", r"$p':\widehat{E}'\to X'$", "Checked on a crop. " + HATPRIME)
add(171, "Proposition (8.5.4), 'p'(Φ̂^{-1}(Ê)) ⊂ G(...)'", "G(φ̂) (with hat)", "G(\\varphi)",
    "misprint_in_print", None, "high",
    r"$p'(\widehat{\Phi}^{-1}(\widehat{E}))\subset G(\varphi)$",
    r"$p'(\widehat{\Phi}^{-1}(\widehat{E}))\subset G(\widehat{\varphi})$",
    "Checked on a 2.5x crop: the print has G(φ̂). The retraction p' maps Ê' into X', and G(φ) ⊂ X' is the corner "
    "of diagram (8.5.4.1) into which p' maps; G(φ̂) is an open subset of Ĉ'. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$p'(\widehat{\Phi}^{-1}(\widehat{E}))\subset G(\varphi)$")
add(171, "Proposition (8.5.4), last line, 'Φ̂^{-1}(Ê) = Ê''", "Ê' (hat over E only)", "\\widehat{E'}",
    "formula", None, "high",
    r"(\widehat{E})=\widehat{E'}$.", r"(\widehat{E})=\widehat{E}'$.", HATPRIME)
add(171, "proof of (8.5.4), affine reduction", "𝒮' = S̃' (tilde over S only)", "\\widetilde{S'}",
    "convention", 8, "high",
    r"$\mathcal{S}'=\widetilde{S'}$", r"$\mathcal{S}'=\widetilde{S}'$", "")
add(171, "proof of (8.5.4), 'la racine dans (S'[z])_+'", "bold z", "plain z", "font", None, "high",
    r"dans $(S'[z])_+$ de", r"dans $(S'[\mathbf{z}])_+$ de", BOLDZ)
add(171, "proof of (8.5.4), 'engendré par z et les φ(f)'", "bold z", "plain z", "font", None, "high",
    r"par $z$ et les", r"par $\mathbf{z}$ et les", BOLDZ)
add(171, "proof of (8.5.4), 'est (S'[z])_+ lui-même'", "bold z", "plain z", "font", None, "high",
    r"est $(S'[z])_+$ lui-même", r"est $(S'[\mathbf{z}])_+$ lui-même", BOLDZ)
add(171, "proof of (8.5.4), 'que Ê' est réunion'", "Ê' (hat over E only)", "\\widehat{E'}",
    "formula", None, "high",
    r"que $\widehat{E'}$ est réunion", r"que $\widehat{E}'$ est réunion", "Checked on a crop. " + HATPRIME)
add(171, "proof of (8.5.4), 'des Ĉ'_{φ(f)}'", "Ĉ'_{φ(f)} (hat over C only)", "\\widehat{C'}_{\\varphi(f)}",
    "formula", None, "high",
    r"$\widehat{C'}_{\varphi(f)}$", r"$\widehat{C}'_{\varphi(f)}$", "Checked on a crop. " + HATPRIME)
add(171, "Corollaire (8.5.5), first '(resp. au préschéma des sommets)'",
    "'(resp.' and ')' upright, 'au préschéma des sommets' italic", "all italic", "convention", 6, "high",
    "(resp. au\npréschéma des sommets)", "\\textup{(resp.} au\npréschéma des sommets\\textup{)}",
    "Checked on a crop. Form of the fix as for '(resp. un 𝒪_Y-Module)' on p. 9.")
add(171, "Corollaire (8.5.5), second '(resp. au préschéma des sommets)'",
    "'(resp.' and ')' upright, 'au préschéma des sommets' italic", "all italic", "convention", 6, "high",
    "(resp. au préschéma des sommets)", "\\textup{(resp.} au préschéma des sommets\\textup{)}",
    "Checked on a crop.")
add(171, "Corollaire (8.5.5), 'de Ĉ' est l'espace sous-jacent'", "Ĉ' (the print swaps Ĉ' and Ĉ in this statement)",
    "\\widehat{C}", "misprint_in_print", None, "high",
    r"de $\widehat{C}$ est l'espace", r"de $\widehat{C}'$ est l'espace",
    "Checked on a crop: the print reads '... l'image réciproque par Φ̂ ... de Ĉ' est l'espace sous-jacent ... de Ĉ.' "
    "Φ̂ maps G(φ̂) ⊂ Ĉ' to Ĉ, so the inverse image is of a part of Ĉ and is a part of Ĉ': the print swaps Ĉ and Ĉ'. "
    "The TeX silently corrects. Apply together with the next finding (end of the statement).",
    corrected=r"de $\widehat{C}$ est l'espace")
add(171, "Corollaire (8.5.5), last word 'de Ĉ.'", "Ĉ (swapped with Ĉ', see the previous finding)",
    "\\widehat{C'}", "misprint_in_print", None, "high",
    "de $\\widehat{C'}$.\n\\end{corollary}", "de $\\widehat{C}$.\n\\end{corollary}",
    "Second half of the Ĉ/Ĉ' swap; apply together with the previous finding.",
    corrected=r"de $\widehat{C}'$.")
add(171, "(8.6.1.1), summation index of ⊕_{n∈Z}", "n bold italic (n∈Z under ⊕)", "plain italic n",
    "misprint_in_print", None, "medium",
    r"\bigoplus_{n\in\mathbf{Z}}\mathcal{O}_X(n)", r"\bigoplus_{\boldsymbol{n}\in\mathbf{Z}}\mathcal{O}_X(n)",
    "Wrong-font sort, checked on a 3x crop: the index n is clearly heavier than the n of 𝒪_X(n) and than the index "
    "n⩾0 of the sums on pp. 172 and 174 (also normal in (2.6.1.1), p. 36); same slip in (8.6.4), p. 173. "
    "The TeX silently has the normal n (form of the fix as for p. 49).",
    corrected=r"\bigoplus_{n\in\mathbf{Z}}\mathcal{O}_X(n)")
add(171, "last line of the page, before \\oldpage[II]{172}",
    "no paragraph break: p. 172 continues 'qui est une 𝒪_X-Algèbre graduée ...' (not indented)",
    "blank line after (8.6.1.1) before the page-172 marker", "other", None, "high",
    "\\tag{8.6.1.1}\n\\end{equation}\n\n", "\\tag{8.6.1.1}\n\\end{equation}\n",
    "Spurious paragraph break after a display at a page break (GLOBAL_ISSUES item 20). "
    "The blank line is the last line of this page's segment, so the p. 172 checker cannot see it.")

# ---------------- page 172 ----------------
add(172, "(8.6.1.3), Ĉ_X = Proj(𝒮_X^≥[z])", "bold z", "plain z", "font", None, "high",
    r"\operatorname{Proj}(\mathcal{S}_X^{\geq}[z])", r"\operatorname{Proj}(\mathcal{S}_X^{\geq}[\mathbf{z}])", BOLDZ)
add(172, "(8.6.1), 'on notera ... i_X : C → Ĉ_X'", "i_X : C → Ĉ_X (C without the subscript X)", "i_X:C_X\\to\\widehat{C}_X",
    "misprint_in_print", None, "high",
    r"$i_X:C_X\to\widehat{C}_X$", r"$i_X:C\to\widehat{C}_X$",
    "Checked on a 3x crop. i_X is the open immersion of (8.3.2) for 𝒮_X^≥, with source C_X. The TeX silently corrects.",
    corrected=r"$i_X:C_X\to\widehat{C}_X$")
add(172, "Proposition (8.6.2), line 1, 'est un isomorphisme'", "'isomorphisme' upright (emphasis in the italic statement)",
    "italic", "convention", 6, "high",
    r"est un isomorphisme, et", r"est un \textup{isomorphisme}, et", "Checked on a crop.")
add(172, "Proposition (8.6.2), 'sont des isomorphismes sur Ê et E'", "'isomorphismes' upright (emphasis in the italic statement)",
    "italic", "convention", 6, "high",
    "sont des\nisomorphismes sur", "sont des\n\\textup{isomorphismes} sur", "Checked on a crop.")

# ---------------- page 173 ----------------
add(173, "Corollaire (8.6.4), summation index of ⊕_{n∈Z}", "n bold italic (n∈Z under ⊕)", "plain italic n",
    "misprint_in_print", None, "medium",
    r"\bigoplus_{n\in\mathbf{Z}}(\mathcal{O}_X(1))^{\otimes n}",
    r"\bigoplus_{\boldsymbol{n}\in\mathbf{Z}}(\mathcal{O}_X(1))^{\otimes n}",
    "Same wrong-font sort as in (8.6.1.1), p. 171; checked on a 2x crop: the index n is heavier than the exponent n of ⊗n. "
    "The TeX silently has the normal n.",
    corrected=r"\bigoplus_{n\in\mathbf{Z}}(\mathcal{O}_X(1))^{\otimes n}")
add(173, "Corollaire (8.6.4), '(3.2.5 et 3.2.7))'", "parentheses and reference numbers upright, 'et' italic",
    "all italic (corollary environment)", "convention", 6, "high",
    "(\\hyperref[II.3.2.5-fr]{3.2.5} et\n\\hyperref[II.3.2.7-fr]{3.2.7}))",
    "\\textup{(\\hyperref[II.3.2.5-fr]{3.2.5}} et\n\\textup{\\hyperref[II.3.2.7-fr]{3.2.7}))}",
    "Checked on a 4x crop.")
add(173, "last line of the page, before \\oldpage[II]{174}",
    "no paragraph break: p. 174 continues 'en vertu de (8.5.1.3) et (8.5.3.2)' (not indented)",
    "blank line after (8.7.1.1) before the page-174 marker", "other", None, "high",
    "\\tag{8.7.1.1}\n\\end{equation}\n\n", "\\tag{8.7.1.1}\n\\end{equation}\n",
    "Spurious paragraph break after a display at a page break (GLOBAL_ISSUES item 20). "
    "The blank line is the last line of this page's segment, so the p. 174 checker cannot see it.")

# ---------------- page 174 ----------------
add(174, "(8.7.1), 'complémentaire Ĉ_X — i_X(ε_X(X))'", "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"$\widehat{C}_X-i_X(\varepsilon_X(X))$", r"$\widehat{C}_X\setmin i_X(\varepsilon_X(X))$",
    "\\setmin is not yet the long dash (global change pending).")
add(174, "(8.7.1), 'complémentaire Ĉ — i(ε(Y))'", "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"$\widehat{C}-i(\varepsilon(Y))$", r"$\widehat{C}\setmin i(\varepsilon(Y))$", "As above.")
add(174, "(8.7.2.4)", "ℐ_n = (𝒮_[n])~ with no final period", "(\\mathcal{S}_{[n]})^{\\sim}. (period added)",
    "punctuation", None, "high",
    r"(\mathcal{S}_{[n]})^{\sim}.", r"(\mathcal{S}_{[n]})^{\sim}",
    "Checked on a 3x crop: nothing follows the tilde; the sentence goes on after the display ('On déduit alors ...' starts a new paragraph).")

# ---------------- verify ----------------
bad = 0
cache = {}
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    p = d["page"]
    if p not in cache:
        with open(os.path.join(RUN, "page_%03d.tex" % p), "rb") as fh:
            cache[p] = fh.read().decode("utf-8").replace("\r\n", "\n")
    n = cache[p].count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE (%d) p.%d: %r" % (n, p, fx["old"]))

# overlap check between fixes on the same page
for p in sorted(cache):
    spans = []
    for d in F:
        if d["page"] != p or d["fix"] is None:
            continue
        i = cache[p].find(d["fix"]["old"])
        spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP p.%d: %s | %s" % (p, a[2], b[2]))

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(170, 175):
    print(p, "normal", cnt[(p, "normal")], "convention", cnt[(p, "convention")], "misprint", cnt[(p, "misprint")])
print("total", len(F), "bad", bad)
if bad == 0:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
