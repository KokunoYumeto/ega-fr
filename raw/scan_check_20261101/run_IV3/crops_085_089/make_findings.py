import json, sys

BASE = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = BASE + r"\findings_085_089.json"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 85 ----------------
L.append(F(85, "proof of (9.8.3) (iv): 'est rare dans (Z_i)_η ou dans (Z_j)_η'",
    "'ou' italic (enlarged crop p85_ou.png)",
    "'ou' upright",
    "italics", None, "high",
    "$(Z_i)_\\eta$ ou\ndans", "$(Z_i)_\\eta$ \\emph{ou}\ndans",
    "Emphasised 'ou' (rare in one OR the other)."))
L.append(F(85, "proof of (9.8.3), last part: 'aucun des ensembles {x_isα}‾ ne peut être contenu dans un autre'",
    "overline over the whole set {x_isα} (closure; enlarged crop p85_overline.png)",
    "$\\{x_{is\\alpha}\\}$ without the bar",
    "formula", None, "high",
    "aucun des ensembles $\\{x_{is\\alpha}\\}$", "aucun des ensembles $\\overline{\\{x_{is\\alpha}\\}}$",
    "The closures of the points are meant (adhérence in the next sentence)."))
L.append(F(85, "Corollaire (9.8.4), l. 1: 'étant celles de (9.8.2), il existe'",
    "reference (9.8.2) upright in the italic statement (crop p85_982.png)",
    "(9.8.2) set in the italic corollary environment",
    "convention", 6, "high",
    "celles de (9.8.2), il existe", "celles de \\textup{(9.8.2)}, il existe",
    None))
L.append(F(85, "Proposition (9.8.5), l. 2: 'soit E(s) (resp. E'(s)) l'ensemble fini'",
    "'(resp. E'(s))' upright (crop p85_resp1.png)",
    "set in the italic proposition environment",
    "convention", 6, "high",
    "(resp. $E'(s)$)", "\\textup{(resp. $E'(s)$)}",
    None))
L.append(F(85, "Proposition (9.8.5), l. 3: 'associés à F_s (resp. des cycles premiers maximaux'",
    "'(resp.' upright, 'des cycles premiers maximaux ...' italic (crop p85_resp3.png)",
    "'(resp.' italic",
    "convention", 6, "high",
    "(resp. des cycles premiers", "\\textup{(resp.} des cycles premiers",
    "The closing parenthesis of this clause is the next entry."))
L.append(F(85, "Proposition (9.8.5), l. 4: '... irréductibles de Supp(F_s)). Alors'",
    "the final ')' closing the '(resp. ...' clause is upright like the one of Supp(...) (crop p85_supp.png)",
    "')' in text italic",
    "convention", 6, "medium",
    "\\operatorname{Supp}(\\mathcal F_s)$).", "\\operatorname{Supp}(\\mathcal F_s)$\\textup{)}.",
    "Pairs with the '(resp.' entry above (same form as earlier \\textup{(resp.} ... \\textup{)} fixes)."))
L.append(F(85, "Proposition (9.8.5), l. 3: 'fini (partie de Z∪{—∞})'",
    "long dash for the minus sign (crop p85_Z.png)",
    "$\\mathbf Z\\cup\\{-\\infty\\}$",
    "convention", 7, "high",
    "\\{-\\infty\\}", "\\{\\setmin\\infty\\}",
    "Unary minus printed as the long dash (GLOBAL_ISSUES 23/49); \\setmin pending the convention-7 decision, as in the earlier \\{\\setmin\\infty\\} page fixes."))
L.append(F(85, "Proposition (9.8.5), last line: 'les fonctions s⇝E(s) et s⇝E'(s)'",
    "wavy arrow ⇝ (crop p85_wavy.png)",
    "$s\\mapsto E(s)$",
    "symbol", None, "high",
    "$s\\mapsto E(s)$", "$s\\leadsto E(s)$",
    "Wavy arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3."))
L.append(F(85, "Proposition (9.8.5), last line: 's⇝E'(s)'",
    "wavy arrow ⇝ (crop p85_wavy.png)",
    "$s\\mapsto E'(s)$",
    "symbol", None, "high",
    "$s\\mapsto E'(s)$", "$s\\leadsto E'(s)$",
    "As the previous entry."))

# ---------------- page 86 ----------------
L.append(F(86, "Proposition (9.8.6), l. 1: 'Avec les hypothèses et notations de (9.8.2), soit'",
    "reference (9.8.2) upright in the italic statement (crop p86_prop_a.png)",
    "(9.8.2) set in the italic proposition environment",
    "convention", 6, "high",
    "notations de (9.8.2), soit", "notations de \\textup{(9.8.2)}, soit",
    None))
L.append(F(86, "Proposition (9.8.6), l. 4: '(relative à k(s)) (4.7.5) est égale'",
    "reference (4.7.5) upright in the italic statement (crop p86_prop_a.png)",
    "(4.7.5) set in the italic proposition environment",
    "convention", 6, "high",
    "(4.7.5) est égale", "\\textup{(4.7.5)} est égale",
    None))
L.append(F(86, "proof of (9.8.6): 'F' = F⊗_{O_S}O_{S'} et soit η' le point générique'",
    "no comma after O_{S'} (enlarged crop p86_comma.png)",
    "'\\mathcal O_{S'}$, et soit'",
    "punctuation", None, "high",
    "\\mathcal O_{S'}$, et soit", "\\mathcal O_{S'}$ et soit",
    "Extra comma."))
L.append(F(86, "proof of (9.8.6): 'les composantes irréductibles T'_j de T_{(k(s'))}'",
    "bold UPRIGHT k in the subscript (enlarged crop p86_ksub2.png)",
    "T_{(\\boldsymbol{k}(s'))} (bold italic)",
    "font", None, "high",
    "T_{(\\boldsymbol{k}(s'))}", "T_{(\\mathbf{k}(s'))}",
    "In subscripts the print's k is bold upright (GLOBAL_ISSUES 48), hence \\mathbf{k}."))
L.append(F(86, "proof of (9.8.6): 'Soit 𝔮 l'unique élément de Ass(M_(K))'",
    "Fraktur 𝔮, upright, unlike the roman q of 'unique' next to it (enlarged crop p86_q_a.png)",
    "$q$ (math italic)",
    "symbol", None, "high",
    "Soit $q$ l'unique", "Soit $\\mathfrak q$ l'unique",
    "Prime ideal letter, same Fraktur alphabet as the 𝔭 (\\mathfrak p) in the same sentence."))
L.append(F(86, "proof of (9.8.6): 'image réciproque de 𝔮.'",
    "Fraktur 𝔮 (enlarged crop p86_q_b.png)",
    "$q$ (math italic)",
    "symbol", None, "high",
    "réciproque de $q$.", "réciproque de $\\mathfrak q$.",
    "As the previous entry."))

# ---------------- page 87 ----------------
L.append(F(87, "Corollaire (9.8.7), l. 4: 'pour F_s (4.7.8). Alors'",
    "reference (4.7.8) upright in the italic statement (crop p87_cor.png)",
    "(4.7.8) set in the italic corollary environment",
    "convention", 6, "high",
    "(4.7.8). Alors", "\\textup{(4.7.8)}. Alors",
    None))
L.append(F(87, "Corollaire (9.8.7), l. 4: 'la fonction s⇝M(s)'",
    "wavy arrow ⇝ (crop p87_cor.png)",
    "$s\\mapsto M(s)$",
    "symbol", None, "high",
    "$s\\mapsto M(s)$", "$s\\leadsto M(s)$",
    "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."))
L.append(F(87, "Proposition (9.8.8), l. 4: 'Supp(F_s) (4.7.12). Alors'",
    "reference (4.7.12) upright in the italic statement (crop p87_prop.png)",
    "(4.7.12) set in the italic proposition environment",
    "convention", 6, "high",
    "(4.7.12). Alors", "\\textup{(4.7.12)}. Alors",
    None))
L.append(F(87, "Proposition (9.8.8), l. 4: 'la fonction s⇝l(s)'",
    "wavy arrow ⇝ (crop p87_prop.png)",
    "$s\\mapsto l(s)$",
    "symbol", None, "high",
    "$s\\mapsto l(s)$", "$s\\leadsto l(s)$",
    "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."))
L.append(F(87, "proof of (9.8.8): 'la longueur géométrique de F_s en x_isα est également à celle de F_η en x_i'",
    "'est également à celle de' (crop p87_egalement.png)",
    "'est également à celle de': keeps the printed reading",
    "misprint_in_print", None, "medium",
    None, None,
    "Ungrammatical: 'également' for 'égale' (the statement (9.8.6) used here says 'est égale à la longueur géométrique'). Not in the errata list of EGA IV part 4. The current edition also keeps 'également'.",
    corrected="est égale à celle de"))
L.append(F(87, "Remarque (9.8.9): 'd la fonction x⇝dim {x}‾ sur P'",
    "wavy arrow ⇝ (enlarged crop p87_wavy_dim.png)",
    "$x\\mapsto\\dim\\overline{\\{x\\}}$",
    "symbol", None, "high",
    "$x\\mapsto\\dim", "$x\\leadsto\\dim",
    "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."))
L.append(F(87, "Remarque (9.8.9): 'm la fonction x⇝long_{O_x} F_x'",
    "wavy arrow ⇝ (enlarged crop p87_wavy_long.png)",
    "$x\\mapsto\\operatorname{long}_{\\mathcal O_x}\\mathcal F_x$",
    "symbol", None, "high",
    "$x\\mapsto\\operatorname{long}", "$x\\leadsto\\operatorname{long}",
    "As the previous entry."))
L.append(F(87, "end of p. 87 / top of p. 88 (Remarque (9.8.9)): 'le type primaire de F' est indépendant de | l'extension algébriquement close k' de k considérée'",
    "page break inside the sentence; p. 88 begins 'l'extension algébriquement close' flush left (page_088_s1.png)",
    "blank line between 'indépendant de' and \\oldpage[IV-3]{88} (last line of page_087.tex)",
    "marker", None, "high",
    "est indépendant de\n\n", "est indépendant de\n",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place. Apply together with the p. 88 entry removing the blank line after \\oldpage[IV-3]{88}."))

# ---------------- page 88 ----------------
L.append(F(88, "top of p. 88: 'l'extension algébriquement close k' de k considérée' continues the sentence of p. 87",
    "first line flush left, no new paragraph",
    "\\oldpage[IV-3]{88} followed by a blank line (and preceded by one at the end of p. 87)",
    "marker", None, "high",
    "\\oldpage[IV-3]{88}\n\nl'extension", "\\oldpage[IV-3]{88}\nl'extension",
    "Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 87 entry (blank line before the marker)."))
L.append(F(88, "Remarque (9.8.9), statement (9.8.9.1) 'Soient f : X→S ... localement constructible dans S.' (edit 1 of 2)",
    "the whole statement (9.8.9.1) is italic, the remark around it roman (page_088_s1.png)",
    "no italics: inside the remark it follows the environment's font, which is to be roman (document-wide remark item)",
    "italics", None, "high",
    "\\textbf{(9.8.9.1)} Soient", "\\textbf{(9.8.9.1)} \\textit{Soient",
    "Opens \\textit{...}; apply together with the next entry, which closes it. \\textit (not \\emph) so that the statement stays italic whatever the remark font."))
L.append(F(88, "statement (9.8.9.1), end (edit 2 of 2)",
    "italic up to 'dans S.'; 'Compte tenu des remarques' roman, new paragraph",
    "see previous entry",
    "italics", None, "high",
    "constructible dans $S$.\n\nCompte tenu", "constructible dans $S$.}\n\nCompte tenu",
    "Closes the \\textit opened by the previous entry; apply both together."))
L.append(F(88, "statement (9.8.9.1): 'la fonction s⇝T(s)'",
    "wavy arrow ⇝ (page_088_s1.png)",
    "$s\\mapsto T(s)$",
    "symbol", None, "high",
    "$s\\mapsto T(s)$", "$s\\leadsto T(s)$",
    "Wavy arrow (GLOBAL_ISSUES 33); not convention 3. Independent of the two \\textit entries (no overlap)."))
L.append(F(88, "subsection heading 9.9",
    "'9.9. Constructibilité des propriétés locales des fibres.' with a final full stop (crop p88_heading.png)",
    "\\subsection{Constructibilité des propriétés locales des fibres} (no full stop)",
    "punctuation", None, "high",
    "\\subsection{Constructibilité des propriétés locales des fibres}",
    "\\subsection{Constructibilité des propriétés locales des fibres.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same fix as the earlier IV-3 headings."))
for lab in ["i", "ii", "iii"]:
    L.append(F(88, "Proposition (9.9.1), item label (%s)" % lab,
        "label (%s) upright before the italic item" % lab,
        "\\item[(%s)] inside the italic proposition environment: italic" % lab,
        "convention", 6, "high",
        "\\item[(%s)]" % lab, "\\item[\\textup{(%s)}]" % lab,
        "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES 16)."))
L.append(F(88, "after (9.9.1): 'les fonctions x⇝dim_x(Z_{f(x)}) et'",
    "wavy arrow ⇝ (crop p88_wavy_0III.png)",
    "$x\\mapsto\\dim_x(Z_{f(x)})$",
    "symbol", None, "high",
    "$x\\mapsto\\dim_x(Z_{f(x)})$", "$x\\leadsto\\dim_x(Z_{f(x)})$",
    "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."))
L.append(F(88, "after (9.9.1): 'et x⇝codim_x(Z_{f(x)}, X_{f(x)}) sont localement constructibles'",
    "wavy arrow ⇝ (crop p88_wavy_0III.png)",
    "$x\\mapsto\\operatorname{codim}_x(Z_{f(x)},X_{f(x)})$",
    "symbol", None, "high",
    "$x\\mapsto\\operatorname{codim}_x", "$x\\leadsto\\operatorname{codim}_x",
    "As the previous entry."))
L.append(F(88, "proof of (9.9.1): 'on a X_s=(X_0)_{s_0}⊗_{k(s_0)}k(s), et h_s est la projection' (edit 1 of 2)",
    "formula in the running text of the line 'si s_0 est la projection de s dans S_0=Spec(A_0), on a X_s=... , et h_s est la' (crop p88_kk.png)",
    "displayed with \\[ ... \\]",
    "formula", None, "high",
    "on a\n\\[\nX_s=", "on a\n$X_s=",
    "Display vs inline; no connecting word lost. Opens the inline math: apply together with the next entry. The two convention-1 entries below touch neither string."))
L.append(F(88, "same formula (edit 2 of 2)",
    "', et h_s' follows on the same line",
    "'k(s),' then \\] and 'et $h_s$' on a new line",
    "formula", None, "high",
    ",\n\\]\net $h_s$", "$,\net $h_s$",
    "Closes the inline math opened by the previous entry; apply both together."))
L.append(F(88, "same formula: '⊗_{k(s_0)}'",
    "bold upright k in the subscript (enlarged crop p88_kk.png)",
    "\\otimes_{k(s_0)} (plain k)",
    "convention", 1, "high",
    "\\otimes_{k", "\\otimes_{\\mathbf{k}",
    "Bold upright in subscripts (GLOBAL_ISSUES 48), hence \\mathbf{k}."))
L.append(F(88, "same formula: '... k(s),'",
    "bold italic k (enlarged crop p88_kk.png)",
    "k(s) (plain k)",
    "convention", 1, "high",
    "}k(s)", "}\\boldsymbol{k}(s)",
    None))
L.append(F(88, "end of p. 88 / top of p. 89: 'X_s^(α) les composantes irréductibles de X_s | contenant x, on a'",
    "page break inside the sentence; p. 89 begins 'contenant x, on a' flush left (page_089_s1.png)",
    "blank line between '$X_s$' and \\oldpage[IV-3]{89} (last line of page_088.tex)",
    "marker", None, "high",
    "composantes irréductibles de $X_s$\n\n", "composantes irréductibles de $X_s$\n",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place. Apply together with the p. 89 entry removing the blank line after \\oldpage[IV-3]{89}."))

# ---------------- page 89 ----------------
L.append(F(89, "top of p. 89: 'contenant x, on a codim_x(Z_s, X_s) = ...' continues the sentence of p. 88",
    "first line flush left, no new paragraph",
    "\\oldpage[IV-3]{89} followed by a blank line (and preceded by one at the end of p. 88)",
    "marker", None, "high",
    "\\oldpage[IV-3]{89}\n\ncontenant", "\\oldpage[IV-3]{89}\ncontenant",
    "Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 88 entry (blank line before the marker)."))
L.append(F(89, "proof of (9.9.1), l. 1: 'on a codim_x(Z_s, X_s) = inf_β(sup_α(codim(Z_s^(β), X_s^(α)))), (α, β) variant dans'",
    "formula in the running text of the first line, with ordinary parentheses (page_089_s1.png)",
    "displayed with \\[ ... \\], with \\left( \\right) and \\bigl( \\bigr)",
    "formula", None, "high",
    "on a\n\\[\n\\operatorname{codim}_x(Z_s,X_s)=\n\\inf_\\beta\\left(\\sup_\\alpha\n\\bigl(\\operatorname{codim}(Z_s^{(\\beta)},X_s^{(\\alpha)})\\bigr)\\right),\n\\]\n$(\\alpha,\\beta)$",
    "on a $\\operatorname{codim}_x(Z_s,X_s)=\n\\inf_\\beta(\\sup_\\alpha\n(\\operatorname{codim}(Z_s^{(\\beta)},X_s^{(\\alpha)})))$,\n$(\\alpha,\\beta)$",
    "Display vs inline; no connecting word lost. The print sets β, α under inf, sup (index position: ignorable)."))
L.append(F(89, "(9.9.1.1): 'dim(X_s^(α)) — dim(Z_s^(β))'",
    "long dash for the minus sign (enlarged crop p89_dash.png)",
    "\\dim(X_s^{(\\alpha)})-\\dim(Z_s^{(\\beta)})",
    "convention", 7, "high",
    "\\dim(X_s^{(\\alpha)})-\\dim", "\\dim(X_s^{(\\alpha)})\\setmin\\dim",
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
L.append(F(89, "proof of (9.9.1): 'l'ensemble des couples (dim(Z^(β)_{f(x')}), dim(X^(α)_{f(x')})) pour les couples formés'",
    "formula in the running text at the start of the line, followed by 'pour les couples formés d'une composante irréductible X^(α)_{f(x')}' (page_089_s2.png)",
    "displayed with \\[ \\bigl( ... \\bigr) \\]",
    "formula", None, "high",
    "des couples\n\\[\n\\bigl(\\dim(Z_{f(x')}^{(\\beta)}),\\dim(X_{f(x')}^{(\\alpha)})\\bigr)\n\\]\npour les couples",
    "des couples\n$(\\dim(Z_{f(x')}^{(\\beta)}),\\dim(X_{f(x')}^{(\\alpha)}))$\npour les couples",
    "Display vs inline; no connecting word lost."))
L.append(F(89, "proof of (9.9.1): 'appliqué suivant la méthode de (8.1.2, a))'",
    "'a)' italic (enlarged crop p89_a.png)",
    "'(8.1.2, a))' all upright",
    "italics", None, "high",
    "(8.1.2, a))", "(8.1.2, \\emph{a)})",
    "Same form as '(3.1.3, \\emph{c')})' on p. 85."))
L.append(F(89, "end of p. 89 / top of p. 90: '(X_i)_η ne contient pas le | point générique de (Z_j)_η, donc'",
    "page break inside the sentence; p. 90 begins 'point générique de (Z_j)_η' flush left (crop p90_top.png)",
    "blank line between 'pas le' and \\oldpage[IV-3]{90} (last line of page_089.tex)",
    "marker", None, "high",
    "ne contient pas le\n\n", "ne contient pas le\n",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 90 marker itself is in the right place. Pairs with removing the blank line after \\oldpage[IV-3]{90} ('\\oldpage[IV-3]{90}\\n\\npoint générique'), which lies in page_090.tex (pp. 90-94 batch); that batch may file this same edit: apply it once."))


# ---------------- checks ----------------
def load(p):
    with open(BASE + r"\page_%03d.tex" % p, "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")

texts = {p: load(p) for p in range(85, 90)}
bad = 0
for i, f in enumerate(L):
    if f["fix"] is None:
        if f["kind"] != "misprint_in_print":
            print("NO FIX on non-misprint", i); bad += 1
        continue
    old = f["fix"]["old"]
    n = texts[f["page"]].count(old)
    if n != 1:
        print("COUNT", n, "page", f["page"], repr(old)); bad += 1
# overlap check per page
for p in range(85, 90):
    spans = []
    for f in L:
        if f["page"] == p and f["fix"]:
            s = texts[p].find(f["fix"]["old"])
            spans.append((s, s + len(f["fix"]["old"]), f["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP page", p, repr(a[2]), repr(b[2])); bad += 1
# also check misprint 'old' text exists
for f in L:
    if f["kind"] == "misprint_in_print":
        assert texts[f["page"]].count("est également à celle") == 1
from collections import Counter
c = Counter()
for f in L:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in range(85, 90):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("bad", bad, "total", len(L))
if bad == 0:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
