import json
import os
import sys

RUN = r"user\Documents\ega_scan_check_20261101\run_0III"
OUT = os.path.join(RUN, "findings_020_024.json")
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def conv2_0I(page, ref, where):
    add(page, where, "(𝟎_I, %s): bold 0" % ref, r"{$0_{\mathrm I}$, %s}" % ref,
        "convention", 2, "high",
        {"old": r"{$0_{\mathrm I}$, %s}" % ref, "new": r"{$\mathbf{0}_{\mathrm I}$, %s}" % ref},
        "Bold chapter number in the print, plain in the TeX.")


# ---------------------------------------------------------------- page 20
add(20, "proof of (10.2.7), first line of p. 20: 'topologie 𝔫-adique, et on sait que cette dernière est séparée'",
    "𝔲-adique: Fraktur u (strokes joined at the bottom)",
    r"$\mathfrak n$-adique",
    "misprint_in_print", None, "high",
    {"old": r"topologie $\mathfrak n$-adique", "new": r"topologie $\mathfrak u$-adique"},
    "Enlarged crops: the letter is a u-shape, unlike the 𝔫 of 'appartient au radical 𝔫 de B' at the foot of p. 19 "
    "(strokes joined at the top), to which this topology refers. 𝔫 is meant. The TeX silently corrects; the fix "
    "restores the printed reading.",
    corrected=r"topologie $\mathfrak n$-adique")
conv2_0I(20, "7.3.5", "proof of (10.2.7): 'cette dernière est séparée (0_I, 7.3.5)'")
conv2_0I(20, "6.1.2", "proof of (10.2.7), after the formula for f^i(M⊗_A N): '(0_I, 6.1.2)'")
add(20, "Proposition (10.2.8): '(donc libre (10.1.3))'",
    "reference (10.1.3) and the closing parentheses upright (roman old-style figures) inside the italic statement",
    r"(\hyperref[0.10.1.3-fr]{10.1.3})) inside the italic proposition environment",
    "convention", 6, "high",
    {"old": r"(\hyperref[0.10.1.3-fr]{10.1.3}))", "new": r"\textup{(\hyperref[0.10.1.3-fr]{10.1.3}))}"},
    "Enlarged crop. The opening parenthesis before 'donc' may be upright as well; it cannot be told apart reliably.")
conv2_0I(20, "6.3.3", "proof of (10.2.8): 'soit un A_𝔪-module plat (0_I, 6.3.3)'")
conv2_0I(20, "1.2.8", "proof of (10.2.8): 'au cas où A est local (0_I, 1.2.8)'")
add(20, "proof of (10.2.8): 'On sait (II, 7.1.7) qu'il existe'",
    "(𝐈𝐈, 7.1.7): bold II", r"{II, 7.1.7}",
    "convention", 2, "high",
    {"old": r"{II, 7.1.7}", "new": r"{\textbf{II}, 7.1.7}"},
    "Bold chapter number in the print, plain in the TeX.")
add(20, "proof of (10.2.8): 'un anneau de valuation discrète B_i ayant même corps des fractions K_i'",
    "B_i ayant (no comma, mid-line)", r"$B_i$, ayant",
    "punctuation", None, "high",
    {"old": r"discrète $B_i$, ayant", "new": r"discrète $B_i$ ayant"},
    "Enlarged crop.")
add(20, "display (10.2.8.1)",
    "rg_{k_i}(M_i⊗_{B_i}k_i)=rg_{K_i}(M_i⊗_{B_i}K_i) with no final period",
    r"\operatorname{rg}_{K_i}(M_i\otimes_{B_i}K_i).",
    "misprint_in_print", None, "medium",
    {"old": r"\operatorname{rg}_{K_i}(M_i\otimes_{B_i}K_i).", "new": r"\operatorname{rg}_{K_i}(M_i\otimes_{B_i}K_i)"},
    "Enlarged crop: nothing after the closing parenthesis. The sentence ends with this display (the next paragraph "
    "begins 'Mais il est clair'), and the other displays on these pages carry their punctuation, so the missing "
    "period is taken as a slip of the print that the TeX silently supplies. Medium: it could also be treated as plain "
    "punctuation (same diplomatic fix).",
    corrected=r"\operatorname{rg}_{K_i}(M_i\otimes_{B_i}K_i).")
add(20, "proof of (10.2.8), after (10.2.8.1): 'l'homomorphisme composé A→A/𝔭_i→B_i est local, donc k est une extension de k, et l'on a'",
    "donc k est une extension de k (no subscript on either k)",
    r"donc $k$ est une extension de $k_i$",
    "misprint_in_print", None, "high",
    {"old": r"donc $k$ est une extension de $k_i$", "new": r"donc $k$ est une extension de $k$"},
    "Enlarged crops of both letters: neither has a subscript i. Since A→B_i is local, the residue field k_i of B_i "
    "is an extension of k (as used in M⊗_A k_i=(M⊗_A k)⊗_k k_i). The TeX reading 'k est une extension de k_i' is "
    "neither the print nor the correct statement (the subscript is on the wrong k). Diplomatic: the printed "
    "'k ... k'; corrected edition: 'k_i ... k'.",
    corrected=r"donc $k_i$ est une extension de $k$")

# ---------------------------------------------------------------- page 21
conv2_0I(21, "6.2.1", "(10.3.1.1), end: 'donc B est un A-module plat (0_I, 6.2.1)'")
conv2_0I(21, "6.2.3", "proof of Lemme (10.3.1.3): 'en vertu de (0_I, 6.2.3)'")
conv2_0I(21, "6.6.2", "proof of Lemme (10.3.1.3): 'fidèlement plat (0_I, 6.6.2)'")
conv2_0I(21, "7.3.5", "proof of Lemme (10.3.1.3): 'sont alors séparées (0_I, 7.3.5)'")
conv2_0I(21, "6.6.1", "proof of Lemme (10.3.1.3): 'est 𝔪_μ^n (0_I, 6.6.1)'")

# ---------------------------------------------------------------- page 22
conv2_0I(22, "6.2.3", "proof of Lemme (10.3.1.3), first line of p. 22: 'Â' est A'-plat (0_I, 6.2.3)'")
conv2_0I(22, "6.6.2", "first paragraph of p. 22: 'A'-module fidèlement plat (0_I, 6.6.2)'")
conv2_0I(22, "6.5.2", "first paragraph of p. 22: 'A' est noethérien (0_I, 6.5.2)'")
conv2_0I(22, "7.2.12", "'Il résulte donc de (0_I, 7.2.12) et (0_I, 7.2.8)'")
conv2_0I(22, "7.2.8", "'Il résulte donc de (0_I, 7.2.12) et (0_I, 7.2.8)'")
add(22, "'Il résulte donc de (0_I, 7.2.12) et (0_I, 7.2.8) que Â' est noethérien.'",
    "noethérien in italics", r"noethérien. On sait (upright)",
    "italics", None, "high",
    {"old": r"noethérien. On sait", "new": r"\emph{noethérien}. On sait"},
    "Enlarged crop.")
conv2_0I(22, "6.2.1", "'est un (A_λ/𝔪_λ^n)-module plat (0_I, 6.2.1)'")
add(22, "end of the proof of Lemme (10.3.1.3): 'et montre que Â' est A_λ-plat. C.Q.F.D.'",
    "A_λ-plat with 'plat' in italics", r"$A_\lambda$-plat (upright)",
    "italics", None, "high",
    {"old": r"est $A_\lambda$-plat. C.Q.F.D.", "new": r"est $A_\lambda$-\emph{plat}. C.Q.F.D."},
    "Enlarged crop.")
add(22, "(10.3.1.4): 'il suffit en effet de considérer une bijection ξ→t_ξ'",
    "plain arrow ξ→t_ξ", r"\xi\mapsto t_\xi",
    "convention", 3, "high",
    {"old": r"\xi\mapsto t_\xi", "new": r"\xi\to t_\xi"},
    "Enlarged crop: no bar at the tail of the arrow.")
add(22, "(10.3.1.4), transcendental case: '(A_ζ[t])_{𝔍A_ζ[t]}; f_ζξ est l'application canonique'",
    "f_{ζξ} (subscripts in the order zeta, xi)", r"$f_{\xi\zeta}$",
    "misprint_in_print", None, "high",
    {"old": r"$f_{\xi\zeta}$ est l'application canonique", "new": r"$f_{\zeta\xi}$ est l'application canonique"},
    "Enlarged crop, compared with 'f_{ξλ}=f_{ξζ}∘f_{ζλ}' on the next line (ξ first there). With f_{μλ}: A_λ→A_μ "
    "the canonical map A_ζ→A_ξ is f_{ξζ}. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$f_{\xi\zeta}$ est l'application canonique")

# ---------------------------------------------------------------- page 23
conv2_0I(23, "7.3.3", "after (10.3.1.5): 'puisque B̂ est un B-module plat (0_I, 7.3.3)'")
conv2_0I(23, "6.2.1", "after (10.3.1.5): 'donc un A-module plat (0_I, 6.2.1)'")
add(23, "(11.1.1): 'dans une catégorie abélienne C un système E'",
    "bold italic C (not a script letter)", r"$\mathcal C$",
    "font", None, "high",
    {"old": r"abélienne $\mathcal C$", "new": r"abélienne $\boldsymbol{C}$"},
    "Enlarged crop. Same letter at every mention of the abelian category on pp. 23-24.")
for lab in "abcd":
    add(23, "(11.1.1), item label %s)" % lab,
        "%s) (italic letter and parenthesis, no opening parenthesis)" % lab, r"\item[(%s)]" % lab,
        "punctuation", None, "high",
        {"old": r"\item[(%s)]" % lab, "new": r"\item[$%s)$]" % lab},
        "Form as on the neighbouring pages (e.g. \\item[$a)$] in (10.2.4), p. 19).")
add(23, "(11.1.1) a): 'd'objets de C définis pour p∈Z'",
    "bold italic C", r"$\mathcal C$",
    "font", None, "high",
    {"old": r"d'objets de $\mathcal C$ définis", "new": r"d'objets de $\boldsymbol{C}$ définis"},
    "Enlarged crop.")
add(23, "(11.1.1) b): 'On pose Z_{r+1}(E_r^{pq})=Ker(d_r^{pq}), B_{r+1}(E_r^{pq})=Im(d_r^{p+r,q-r+1})'",
    "B_{r+1}(E_r^{pq})=Im(d_r^{p+r,q-r+1})", r"\operatorname{Im}(d_r^{p-r,q+r-1})",
    "misprint_in_print", None, "high",
    {"old": r"\operatorname{Im}(d_r^{p-r,q+r-1})", "new": r"\operatorname{Im}(d_r^{p+r,q-r+1})"},
    "Enlarged crop: the superscript is p+r, q-r+1, the same as that of the target of d_r^{pq}. B_{r+1}(E_r^{pq}) "
    "is the image of the differential arriving at E_r^{pq}, d_r^{p-r,q+r-1}: E_r^{p-r,q+r-1}→E_r^{pq}. The TeX "
    "silently corrects; the fix restores the printed reading.",
    corrected=r"\operatorname{Im}(d_r^{p-r,q+r-1})")
add(23, "(11.1.1), after c): 'comme images réciproques, par le morphisme canonique E_r^{pq}→E_r^{pq}/B_{r+1}(E_r^{pq}) des sous-objets de ce quotient'",
    "no comma after B_{r+1}(E_r^{pq}) (end of the line)", r"$, des sous-objets",
    "misprint_in_print", None, "medium",
    {"old": r"B_{r+1}(E_r^{pq})$, des sous-objets", "new": r"B_{r+1}(E_r^{pq})$ des sous-objets"},
    "Enlarged crop, right margin included: no comma. The comma closing the inserted 'par le morphisme canonique ...' "
    "is expected, so the omission is taken as a slip of the print that the TeX silently corrects.",
    corrected=r"B_{r+1}(E_r^{pq})$, des sous-objets")
add(23, "display (11.1.1.1): 'Z_k(E_r^{pq})/B_k(E_r^{pq})=E_k^{pq}   pour k≥r+1'",
    "pour k≥r+1 with no comma after it", r"\text{pour }k\geq r+1,",
    "punctuation", None, "high",
    {"old": r"\text{pour }k\geq r+1,", "new": r"\text{pour }k\geq r+1"},
    "Enlarged crop. The next line begins 'et, si on pose encore'.")
add(23, "display (11.1.1.1)",
    "a stray vertical rule printed between E_k^{pq} and 'pour k≥r+1'", "no such mark",
    "other", None, "high", None,
    "Printing artifact (a spacing lead or rule that took ink), not text; no change proposed.")
add(23, "(11.1.1) d): 'et, pour tout k≥2' before the display",
    "k≥2 with no comma", r"pour tout $k\geq2$,",
    "punctuation", None, "high",
    {"old": r"pour tout $k\geq2$,", "new": r"pour tout $k\geq2$"},
    "Enlarged crop.")
add(23, "(11.1.1), label e) printed as the first line of p. 24",
    "e) (italic letter and parenthesis, no opening parenthesis)", r"\item[(e)]",
    "punctuation", None, "high",
    {"old": r"\item[(e)]", "new": r"\item[$e)$]"},
    "Filed under p. 23 because \\item[(e)] stands before \\oldpage[0\\textsubscript{III}]{24} in the source (p. 23 "
    "segment). The marker itself is in place: it is a margin note on the line of e).")

# ---------------------------------------------------------------- page 24
add(24, "(11.1.1) e): 'Une famille (E^n) d'objets de C, dont chacun'",
    "bold italic C", r"$\mathcal C$",
    "font", None, "high",
    {"old": r"d'objets de $\mathcal C$, dont", "new": r"d'objets de $\boldsymbol{C}$, dont"},
    "Enlarged crop.")
add(24, "(11.1.1), item label f)",
    "f) (italic letter and parenthesis, no opening parenthesis)", r"\item[(f)]",
    "punctuation", None, "high",
    {"old": r"\item[(f)]", "new": r"\item[$f)$]"},
    "As for a)-e) on p. 23.")
add(24, "(11.1.1): 'est appelée l'aboutissement de la suite spectrale E'",
    "l' upright, aboutissement italic", r"\emph{l'aboutissement}",
    "italics", None, "high",
    {"old": r"\emph{l'aboutissement}", "new": r"l'\emph{aboutissement}"},
    "Enlarged crop.")
add(24, "(11.1.1): 'Supposons que la catégorie C admette des sommes directes infinies'",
    "bold italic C", r"$\mathcal C$",
    "font", None, "high",
    {"old": r"catégorie $\mathcal C$ admette", "new": r"catégorie $\boldsymbol{C}$ admette"},
    "")
add(24, "(11.1.1): 'est un complexe E_r^{(•)} dans C, à opérateur de dérivation'",
    "bold italic C", r"$\mathcal C$",
    "font", None, "high",
    {"old": r"dans $\mathcal C$, à opérateur", "new": r"dans $\boldsymbol{C}$, à opérateur"},
    "Enlarged crop.")
add(24, "(11.1.1): 'et il résulte de c) que'",
    "c) in italics (letter and parenthesis)", r"de c) que (upright)",
    "italics", None, "high",
    {"old": r"il résulte de c) que", "new": r"il résulte de \emph{c)} que"},
    "Enlarged crop.")
add(24, "(11.1.1): 'il résulte de c) que H^n(E_n^{(•)}) est isomorphe à E_{r+1}^{(n)}'",
    "H^n(E_n^{(•)}): subscript n", r"\mathrm H^n(E_r^{(\bullet)})",
    "misprint_in_print", None, "high",
    {"old": r"\mathrm H^n(E_r^{(\bullet)})", "new": r"\mathrm H^n(E_n^{(\bullet)})"},
    "Enlarged crop (6x): the subscript is n, not r. The complex is E_r^{(•)} (defined in the same sentence). The TeX "
    "silently corrects; the fix restores the printed reading.",
    corrected=r"\mathrm H^n(E_r^{(\bullet)})")
add(24, "(11.1.1): 'est isomorphe à E_{r+1}^{(n)} pour tout r≥2'",
    "'isomorphe' (end of line) and 'à' (start of next line) both in italics", r"est isomorphe à (upright)",
    "italics", None, "high",
    {"old": r"est isomorphe à $E_{r+1}^{(n)}$", "new": r"est \emph{isomorphe à} $E_{r+1}^{(n)}$"},
    "Enlarged crop.")
add(24, "(11.1.2): 'u_2^{pq} donne alors un morphisme u_∞^{pq}: E_∞^{pq}→E'_∞^{pq}'",
    "u'_∞^{pq} (prime on u) : E_∞^{pq}→E'_∞^{pq}", r"$u_\infty^{pq}:E_\infty^{pq}\to E_\infty^{\prime pq}$",
    "misprint_in_print", None, "high",
    {"old": r"$u_\infty^{pq}:E_\infty^{pq}\to E_\infty^{\prime pq}$",
     "new": r"$u_\infty^{\prime pq}:E_\infty^{pq}\to E_\infty^{\prime pq}$"},
    "Enlarged crop. The same primed u labels the top arrow of the following diagram (next finding). The map is "
    "u_∞^{pq}, without prime, like u_r^{pq} and u_2^{pq}; p. 26 prints 'il en est de même de u_∞^{pq}' without "
    "prime. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$u_\infty^{pq}:E_\infty^{pq}\to E_\infty^{\prime pq}$")
add(24, "(11.1.2), second diagram, label of the top arrow E_∞^{pq}→E'_∞^{pq}",
    "u'_∞^{pq} (prime on u)", r"\ar[r]^-{u_\infty^{pq}}",
    "misprint_in_print", None, "high",
    {"old": r"\ar[r]^-{u_\infty^{pq}}", "new": r"\ar[r]^-{u_\infty^{\prime pq}}"},
    "Enlarged crop. Same misprint as in the text just above.",
    corrected=r"\ar[r]^-{u_\infty^{pq}}")
add(24, "(11.1.2), second diagram, bottom row: left node gr_p(E^{p+q}) and the arrow label gr_p(u^{p+q})",
    "the subscript p of gr is bold italic in both (the superscript p is ordinary)",
    r"\operatorname{gr}_p(E^{p+q}) and \operatorname{gr}_p(u^{p+q})",
    "misprint_in_print", None, "medium",
    {"old": r"\operatorname{gr}_p(E^{p+q})" + NL + r"      \ar[r]_{\operatorname{gr}_p(u^{p+q})}",
     "new": r"\operatorname{gr}_{\boldsymbol{p}}(E^{p+q})" + NL + r"      \ar[r]_{\operatorname{gr}_{\boldsymbol{p}}(u^{p+q})}"},
    "Wrong-font letters (cf. GLOBAL_ISSUES 29). 6x side-by-side crops: these p's have the heavy stem and small counter "
    "of the bold italic, unlike the p's of the top row and the superscript p's (ink counts about 150-160 against "
    "120-135 px). Text-mode gr_p(E^{p+q}) in f) is ordinary.",
    corrected=r"\operatorname{gr}_p(E^{p+q})" + NL + r"      \ar[r]_{\operatorname{gr}_p(u^{p+q})}")
add(24, "(11.1.2), second diagram, bottom row: right node gr_p(E'^{p+q})",
    "subscript p and the p of the exponent p+q bold italic (q ordinary)",
    r"\operatorname{gr}_p(E^{\prime p+q})",
    "misprint_in_print", None, "medium",
    {"old": r"\operatorname{gr}_p(E^{\prime p+q})",
     "new": r"\operatorname{gr}_{\boldsymbol{p}}(E^{\prime\boldsymbol{p}+q})"},
    "Wrong-font letters, as in the previous finding; the exponent's p carries about 1.5 times the ink of the q beside it.",
    corrected=r"\operatorname{gr}_p(E^{\prime p+q})")
add(24, "(11.1.2), last paragraph: 'si l'on sait en outre que u_2^{pq}(B_∞(E_2^{pq}))=...'",
    "'si l'on sait en outre' in italics, 'que' upright", r"\emph{si l'on sait en outre que}",
    "italics", None, "high",
    {"old": r"\emph{si l'on sait en outre que}", "new": r"\emph{si l'on sait en outre} que"},
    "Enlarged crop.")
add(24, "(11.1.2), last paragraph: 'et que les u^n sont des isomorphismes, alors on peut conclure'",
    "'et que les u^n sont des' upright, only 'isomorphismes' in italics", r"\emph{et que les $u^n$ sont des isomorphismes}",
    "italics", None, "high",
    {"old": r"\emph{et que les" + NL + r"$u^n$ sont des isomorphismes}",
     "new": r"et que les" + NL + r"$u^n$ sont des \emph{isomorphismes}"},
    "Enlarged crop.")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    path = os.path.join(RUN, "page_%03d.tex" % d["page"])
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    n = text.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, d["page"], repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("SAME", d["page"], repr(fx["old"]))
# overlapping olds on the same page
for i, a in enumerate(F):
    for b in F[i + 1:]:
        if a["page"] == b["page"] and a["fix"] and b["fix"]:
            if a["fix"]["old"] in b["fix"]["old"] or b["fix"]["old"] in a["fix"]["old"]:
                print("OVERLAP", a["page"], repr(a["fix"]["old"]), repr(b["fix"]["old"]))

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
print("total", len(F), "ok" if ok else "PROBLEMS")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
