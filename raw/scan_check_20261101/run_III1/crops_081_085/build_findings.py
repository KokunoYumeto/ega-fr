import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_III1'
OUT = RUN + r'\findings_081_085.json'

def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

L = []

# ---------------- page 82 ----------------
L.append(F(82, "Paragraph before § 1: 'propositions préliminaires de (0, 13.4 à 13.7)'",
    "(0, 13.4 à 13.7) with the chapter number 0 in bold",
    "(0, 13.4 à 13.7)", "convention", 2, "high",
    r"(0, 13.4 à 13.7)", r"(\textbf{0}, 13.4 à 13.7)",
    "Bold 0 in the reference to chapter 0."))
L.append(F(82, "(1.1.1), 1st paragraph: 'considéré comme élément du dual (A^r)ˇ'",
    "(A^r) followed by a raised check accent ˇ (háček)",
    r"$(A^r)^\vee$", "symbol", None, "medium",
    r"(A^r)^\vee", r"(A^r)\check{}",
    r"The print sets a check accent after the parenthesis, not the ∨ sign; same treatment as the EGA II precedent (\mathcal{E}^s)^\vee -> (\mathcal{E}^s)\check{}."))
L.append(F(82, "(1.1.1), 2nd paragraph: 'K_n(f_i)=0 pour n≠0,1 : l'opérateur bord est défini'",
    "n≠0,1 : l'opérateur (colon)",
    r"$n\neq0,1$~; l'opérateur (semicolon)", "punctuation", None, "high",
    r"$n\neq0,1$~;", r"$n\neq0,1$~:",
    "Enlarged crop: the print has a colon after 'n≠0,1', not a semicolon."))
L.append(F(82, "(1.1.1), 2nd paragraph: 'le produit tensoriel K_•(f_1)⊗K_•(f_2)⊗...⊗K_•(f_r)'",
    "⊗ . . . ⊗ (dots on the baseline)",
    r"\otimes\cdots\otimes", "symbol", None, "high",
    r"\otimes\cdots\otimes", r"\otimes\ldots\otimes",
    "Baseline dots in the print (GLOBAL_ISSUES item 22)."))
L.append(F(82, "(1.1.2): 'g(i_1, ..., i_k)=g(e_{i_1}∧...∧e_{i_k}),'",
    "∧ . . . ∧ (dots on the baseline)",
    r"\wedge\cdots\wedge", "symbol", None, "high",
    r"\wedge\cdots\wedge", r"\wedge\ldots\wedge",
    "Baseline dots in the print (GLOBAL_ISSUES item 22)."))
L.append(F(82, "(1.1.2.3): 'g(i_1, ..., î_h, ..., i_{k+1})'",
    "circumflex over the i only; the subscript h stands outside it (î_h)",
    r"\widehat{i_h}", "formula", None, "medium",
    r"\widehat{i_h}", r"\widehat{i}_h",
    r"Enlarged crop: the hat covers only i. Same kind as the EGA I precedent \widehat{M'} -> \widehat{M}'."))

# ---------------- page 83 ----------------
L.append(F(83, "(1.1.3.1): 'H_•(f, M)=H_•(K_•(f, M))'",
    "no punctuation after the first display line",
    r"H_\bullet(K_\bullet(\mathbf f,M)),\\", "punctuation", None, "high",
    r"H_\bullet(K_\bullet(\mathbf f,M)),\\", r"H_\bullet(K_\bullet(\mathbf f,M))\\",
    "Enlarged crop: (1.1.3.1) ends without a comma; only (1.1.3.2) has its full stop."))
L.append(F(83, "(1.1.3), 2nd paragraph: 'On définit d'ailleurs un A-isomorphisme'",
    "A-isomorphisme with 'isomorphisme' in italics",
    r"un $A$-isomorphisme (upright)", "italics", None, "high",
    r"un $A$-isomorphisme", r"un $A$-\emph{isomorphisme}",
    "Enlarged crop: 'isomorphisme' is italic in the print."))
L.append(F(83, "(1.1.3), 2nd paragraph: 'un A-isomorphisme K_•(f, M) ⥲ K^•(f, M) en faisant correspondre'",
    "K_•(f, M) ⥲ K^•(f, M) (bullet subscript and superscript)",
    r"$K_i(\mathbf f,M)\xrightarrow{\sim}K^{r-i}(\mathbf f,M)$", "formula", None, "high",
    r"$K_i(\mathbf f,M)\xrightarrow{\sim}K^{r-i}(\mathbf f,M)$",
    r"$K_\bullet(\mathbf f,M)\xrightarrow{\sim}K^\bullet(\mathbf f,M)$",
    "Enlarged crop. The print states the degree-reversing isomorphism of the whole complexes; the TeX's K_i -> K^{r-i} is an editorial precision, not a correction of a misprint (the printed statement is correct as written)."))
L.append(F(83, "(1.1.3), 2nd paragraph: 'z=Σ(e_{i_1}∧...∧e_{i_k})⊗z_{i_1...i_k}'",
    "∧ . . . ∧ (dots on the baseline)",
    r"\wedge\cdots\wedge", "symbol", None, "high",
    r"\wedge\cdots\wedge", r"\wedge\ldots\wedge",
    "Baseline dots in the print (GLOBAL_ISSUES item 22)."))
L.append(F(83, "(1.1.3), 4th paragraph: 'il est immédiat (G, I, 2.1) que M⇝H^•(f, M) est un foncteur cohomologique'",
    "M ⇝ H^•(f, M) (wavy arrow)",
    r"$M\mapsto H^\bullet(\mathbf f,M)$", "symbol", None, "high",
    r"$M\mapsto H^\bullet(\mathbf f,M)$", r"$M\leadsto H^\bullet(\mathbf f,M)$",
    "Wavy maps-to arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33."))
L.append(F(83, "Proposition (1.1.4): 'l'homothétie z⇝f_i.z dans M_{i−1}'",
    "z ⇝ f_i.z (wavy arrow)",
    r"$z\mapsto f_i z$", "symbol", None, "high",
    r"$z\mapsto", r"$z\leadsto",
    "Wavy maps-to arrow in the print (\\leadsto). The dot in f_i.z is a separate finding."))
L.append(F(83, "Proposition (1.1.4): 'l'homothétie z⇝f_i.z dans M_{i−1}'",
    "f_i.z (dot between f_i and z)",
    r"f_i z", "formula", None, "high",
    r"f_i z$ dans", r"f_i.z$ dans",
    "Enlarged crop: the print has a dot between f_i and z."))
L.append(F(83, "Proposition (1.1.4): 'M_{i−1}=M/(f_1M+...+f_{i−1}M)'",
    "+ . . . + (dots on the baseline)",
    r"f_1M+\cdots+f_{i-1}M", "symbol", None, "high",
    r"+\cdots+", r"+\ldots+",
    "Baseline dots in the print (GLOBAL_ISSUES item 22)."))

# ---------------- page 84 ----------------
L.append(F(84, "1st paragraph: 'spectrale de Künneth (M, XVII, 5.2 a) et G, I, 5.5.2)'",
    "5.2 a) with 'a)' in italics",
    r"5.2 a) (upright)", "italics", None, "high",
    r"5.2 a) et", r"5.2 \emph{a)} et",
    "Enlarged crop: the letter label a) is italic in the print."))
L.append(F(84, "Long exact homology sequence, start: '... → H_{p+1}(K_1⊗L_•)'",
    ". . . → (dots on the baseline)",
    r"\cdots\longrightarrow H_{p+1}", "symbol", None, "high",
    r"\cdots\longrightarrow H_{p+1}", r"\ldots\longrightarrow H_{p+1}",
    "Baseline dots in the print (GLOBAL_ISSUES item 22)."))
L.append(F(84, "Long exact homology sequence, end: '→ H_{p−1}(K_0⊗L_•) → ...'",
    "→ . . . (baseline dots, no full stop after the display)",
    r"\longrightarrow\cdots.", "punctuation", None, "high",
    r"\longrightarrow\cdots.", r"\longrightarrow\ldots",
    "Enlarged crop: the display ends with baseline dots and no full stop; the fix also turns \\cdots into \\ldots."))
L.append(F(84, "Proof of (1.1.4.1): 'H_p(K_1⊗L_•)=K_1⊗H_{v−1}(L_•) pour tout p'",
    "K_1⊗H_{v−1}(L_•): the subscript letter is an italic v",
    r"K_1\otimes H_{p-1}(L_\bullet) (silently corrected)", "misprint_in_print", None, "high",
    r"K_1\otimes H_{p-1}(L_\bullet)$ pour tout", r"K_1\otimes H_{v-1}(L_\bullet)$ pour tout",
    "Enlarged crop (3x): the print has an italic v without descender where p is meant. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"K_1\otimes H_{p-1}(L_\bullet)"))
L.append(F(84, "Proof of (1.1.4.1): 'de la définition de H_0(K⊗H_p(L_•)) et de H_1(K_•⊗H_{p−1}(L_•))'",
    "H_0(K⊗H_p(L_•)): K without the bullet subscript",
    r"$H_0(K_\bullet\otimes H_p(L_\bullet))$ (silently corrected)", "misprint_in_print", None, "high",
    r"$H_0(K_\bullet\otimes H_p(L_\bullet))$ et de", r"$H_0(K\otimes H_p(L_\bullet))$ et de",
    "Enlarged crop (2x): no bullet under K in the first term (the second term has it). The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"H_0(K_\bullet\otimes H_p(L_\bullet))"))
L.append(F(84, "End of proof of (1.1.4): 'l'hypothèse de récurrence de ce lemme (1.1.4.1) donnent'",
    "l'hypothèse de récurrence de ce lemme ... donnent",
    "l'hypothèse de récurrence et ce lemme (silently corrected)", "misprint_in_print", None, "high",
    "l'hypothèse de récurrence et\nce lemme", "l'hypothèse de récurrence de\nce lemme",
    "Enlarged crop: the print has 'de' where the plural 'donnent' requires 'et'. The TeX silently corrects it; the fix restores the printed reading.",
    corrected="l'hypothèse de récurrence et ce lemme"))
L.append(F(84, "End of proof of (1.1.4): 'le noyau de l'homothétie z⇝f_r.z dans M_{r−1}'",
    "z ⇝ f_r.z (wavy arrow)",
    r"$z\mapsto f_rz$", "symbol", None, "high",
    r"$z\mapsto", r"$z\leadsto",
    "Wavy maps-to arrow in the print (\\leadsto). The dot in f_r.z is a separate finding."))
L.append(F(84, "End of proof of (1.1.4): 'le noyau de l'homothétie z⇝f_r.z dans M_{r−1}'",
    "f_r.z (dot between f_r and z)",
    r"f_rz", "formula", None, "high",
    r"f_rz$", r"f_r.z$",
    "Enlarged crop: the print has a dot between f_r and z."))
L.append(F(84, "(1.1.5): 'l'application A-linéaire (x_1, ..., x_r)⇝(g_1x_1, ..., g_rx_r)'",
    "(x_1, ..., x_r) ⇝ (g_1x_1, ..., g_rx_r) (wavy arrow)",
    r"(x_1,\ldots,x_r)\mapsto(g_1x_1,\ldots,g_rx_r)", "symbol", None, "high",
    r"x_r)\mapsto(", r"x_r)\leadsto(",
    "Wavy maps-to arrow in the print (\\leadsto)."))
L.append(F(84, "(1.1.5): 'est une application A-linéaire, x∈F̌ et y=ᵗu(x)∈Ě'",
    "x ∈ F̌ (check accent above F)",
    r"\mathbf x\in F^\vee", "symbol", None, "high",
    r"\in F^\vee", r"\in\check F",
    "Enlarged crop: the dual is written with a check accent over the letter, not a superscript."))
L.append(F(84, "(1.1.5): 'est une application A-linéaire, x∈F̌ et y=ᵗu(x)∈Ě'",
    "ᵗu(x) ∈ Ě (check accent above E)",
    r"{}^tu(\mathbf x)\in E^\vee", "symbol", None, "high",
    r"\in E^\vee", r"\in\check E",
    "Enlarged crop: the dual is written with a check accent over the letter, not a superscript."))
L.append(F(84, "(1.1.6.2): 'φ_{f^{m−n}} : K^•(f^n, M) → K^•(f^m, M)'",
    "no punctuation after (1.1.6.2)",
    r"K^\bullet(\mathbf f^m,M),\\", "punctuation", None, "high",
    r"K^\bullet(\mathbf f^m,M),\\", r"K^\bullet(\mathbf f^m,M)\\",
    "Enlarged crop: (1.1.6.2) ends without a comma; (1.1.6.3) ends with a full stop."))

# ---------------- page 85 ----------------
L.append(F(85, "(1.1.6.4): 'C^•((f), M) = lim_n K^•(f^n, M)'",
    "no punctuation after (1.1.6.4)",
    r"\varinjlim_n K^\bullet(\mathbf f^n,M),\\", "punctuation", None, "high",
    r"\varinjlim_n K^\bullet(\mathbf f^n,M),\\", r"\varinjlim_n K^\bullet(\mathbf f^n,M)\\",
    "Enlarged crop: no comma after (1.1.6.4)."))
L.append(F(85, "(1.1.6.5): 'H^•((f), M)=H^•(C^•((f), M))=lim_n H^•(f^n, M)'",
    "no punctuation after (1.1.6.5)",
    r"=\varinjlim_n H^\bullet(\mathbf f^n,M),", "punctuation", None, "high",
    r"=\varinjlim_n H^\bullet(\mathbf f^n,M),", r"=\varinjlim_n H^\bullet(\mathbf f^n,M)",
    "Enlarged crop: no comma after (1.1.6.5); the text continues 'la dernière égalité ...'."))
L.append(F(85, "(1.1.6), last paragraph: 'Il est clair que M⇝C^•((f), M) est un foncteur A-linéaire exact'",
    "M ⇝ C^•((f), M) (wavy arrow)",
    r"$M\mapsto C^\bullet((\mathbf f),M)$", "symbol", None, "high",
    r"$M\mapsto C^\bullet", r"$M\leadsto C^\bullet",
    "Wavy maps-to arrow in the print (\\leadsto)."))
L.append(F(85, "(1.1.6), last paragraph: 'et M⇝H^•((f), M) un foncteur cohomologique'",
    "M ⇝ H^•((f), M) (wavy arrow)",
    r"$M\mapsto H^\bullet((\mathbf f),M)$", "symbol", None, "high",
    r"$M\mapsto H^\bullet", r"$M\leadsto H^\bullet",
    "Wavy maps-to arrow in the print (\\leadsto)."))
L.append(F(85, "Remarque (1.1.10), display, start: '... → H^p_Y(X, F)'",
    ". . . → (dots on the baseline)",
    r"\cdots\longrightarrow H_Y^p", "symbol", None, "high",
    r"\cdots\longrightarrow H_Y^p", r"\ldots\longrightarrow H_Y^p",
    "Baseline dots in the print (GLOBAL_ISSUES item 22)."))
L.append(F(85, "Remarque (1.1.10), display: 'H^p(X—Y, F)'",
    "X—Y with the long dash",
    r"H^p(X-Y,\mathcal F)", "convention", 7, "high",
    r"H^p(X-Y,\mathcal F)", r"H^p(X\setmin Y,\mathcal F)",
    "Set difference printed with the long dash."))
L.append(F(85, "Remarque (1.1.10), display, end: '→ H^{p+1}_Y(X, F) → ...'",
    "→ . . . (baseline dots, no full stop after the display)",
    r"\longrightarrow\cdots.", "punctuation", None, "high",
    r"\longrightarrow\cdots.", r"\longrightarrow\ldots",
    "Enlarged crop: the display ends with baseline dots and no full stop; the fix also turns \\cdots into \\ldots."))

# ---------------- checks ----------------
ok = True
pages = {}
for n in range(81, 86):
    pages[n] = open(RUN + r'\page_%03d.tex' % n, encoding='utf-8', newline='').read().replace('\r\n', '\n')
# each old occurs exactly once in its original page file
for x in L:
    if x['fix'] is None:
        continue
    c = pages[x['page']].count(x['fix']['old'])
    if c != 1:
        ok = False
        print('NOT UNIQUE', x['page'], c, repr(x['fix']['old']))
# sequential application on each page (as apply_fixes.py does) keeps every old unique
work = dict(pages)
for x in L:
    if x['fix'] is None:
        continue
    t = work[x['page']]
    c = t.count(x['fix']['old'])
    if c != 1:
        ok = False
        print('SEQ FAIL', x['page'], c, repr(x['fix']['old']))
        continue
    work[x['page']] = t.replace(x['fix']['old'], x['fix']['new'])
if not ok:
    sys.exit(1)
json.dump(L, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in L:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    cnt[(x['page'], k)] += 1
for n in range(81, 86):
    print(n, cnt[(n, 'normal')], cnt[(n, 'convention')], cnt[(n, 'misprint')])
print('total', len(L), 'written to', OUT)
