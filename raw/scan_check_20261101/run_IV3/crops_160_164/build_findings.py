# Builds findings_160_164.json for the EGA IV-3 scan check of printed pp. 160-164 and checks every fix.
# TeX strings are raw strings; the character ¶ stands for a line break (LF).
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_160_164.json"


def nl(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if nofix else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 159/160: blank lines around the p. 160 marker (mid-sentence break)
add(159, "end of page_159.tex, before \\oldpage[IV-3]{160}: '... Il existe alors au moins un | point x'∈X' dont les projections ...'",
    "printed p. 160 begins 'point x'∈X' dont les projections dans X_1 et Y' ...' flush left: the sentence of p. 159 runs on, no paragraph break",
    "blank line after the comment line '% IV3_B23_P159_END', just before \\oldpage[IV-3]{160}: a paragraph break mid-sentence",
    "marker", None, "high",
    r"au moins un¶% IV3_B23_P159_END¶¶", r"au moins un¶% IV3_B23_P159_END¶",
    "OUTSIDE pp. 160-164: 'old' lies at the end of page_159.tex (ega4-11-fr.tex, just before the p. 160 marker). Apply together with the p. 160 entry that removes the blank line after the marker (GLOBAL_ISSUES 20). The pp. 155-159 batch may file the same edit; apply it once. The marker position itself is right.")
add(160, "top of p. 160, after \\oldpage[IV-3]{160}",
    "'point x'∈X' dont les projections ...' continues the sentence 'Il existe alors au moins un' of p. 159, flush left",
    "\\oldpage[IV-3]{160} followed by a blank line (and preceded by one at the end of p. 159)",
    "marker", None, "high",
    r"\oldpage[IV-3]{160}¶¶point", r"\oldpage[IV-3]{160}¶point",
    "Apply together with the p. 159 entry (blank line before the marker). Marker position itself is right.")

# ---------------- page 160
add(160, "proof of (11.8.1), case label '(ii) Cas où A est réduit et noethérien. — Soient'",
    "'(ii)' in roman of normal weight (enlarged crop)",
    "\\textbf{(ii)}: bold",
    "font", None, "high",
    r"\noindent\textbf{(ii)} \emph{Cas", r"\noindent(ii) \emph{Cas",
    "The first case label '(i) Cas où A est intègre' is written \\textbf{(i)} too (page_159.tex line 89, outside this batch); GLOBAL_ISSUES 51: proof-part labels are printed upright roman.")
add(160, "proof of (11.8.1) (ii): 'est f''_i-plat en tout point x''_i de X''_i'",
    "'tout' in italics (enlarged crop; the earlier 'en tout point x_i de X_i' is roman, as in the TeX)",
    "'tout' upright",
    "italics", None, "high",
    r"$f''_i$-plat en tout point", r"$f''_i$-plat en \emph{tout} point",
    "")
add(160, "proof of (11.8.1) (ii): 'en tout point x''_i de X''_i sont les projections dans X et Y''_i sont x et le point fermé y''_i'",
    "'de X''_i sont les projections' (enlarged crop): 'sont' for 'dont'",
    "'de $X''_i$ dont les projections': silently corrected",
    "misprint_in_print", None, "high",
    r"de $X''_i$ dont les projections", r"de $X''_i$ sont les projections",
    "The parallel sentences (case (i) on p. 159, 'en tout point x_i de X_i dont les projections' a few lines above) have 'dont'.",
    corrected=r"de $X''_i$ dont les projections")

# ---------------- page 161
add(161, "first paragraph: 'la famille correspondante des u^♯_λ : (f_λ)^*(F) → G_λ'",
    "sharp sign ♯ (enlarged crop)",
    "u^\\#_\\lambda (typesets #)",
    "convention", 9, "high",
    r"u^\#_\lambda", r"u^\sharp_\lambda",
    "")
add(161, "(11.9.2): 'pour tout λ∈L, soit (g_λμ)_{λ∈M} une famille de morphismes g_λμ : Z'_λμ → Z_λ'",
    "index of the family printed λ∈M (enlarged crop)",
    "(g_{\\lambda\\mu})_{\\mu\\in M}: silently corrected",
    "misprint_in_print", None, "high",
    r"(g_{\lambda\mu})_{\mu\in M}", r"(g_{\lambda\mu})_{\lambda\in M}",
    "For fixed λ the family is indexed by μ∈M (cf. (v_λμ)_{μ∈M} later in the same paragraph).",
    corrected=r"(g_{\lambda\mu})_{\mu\in M}")
add(161, "(11.9.3): 'autrement dit on est ramené au cas où les Z_λ sont affines.'",
    "'affines' in italics (enlarged crop)",
    "'affines' upright",
    "italics", None, "high",
    r"les $Z_\lambda$ sont affines.", r"les $Z_\lambda$ sont \emph{affines}.",
    "")
add(161, "(11.9.4): 'car on a alors ∩_{λ∈L} Ker((φ_λ)_s) = (∩_{λ∈L} Ker(φ_λ))_s (0_I, 1.3.2). Mais cette relation ...'",
    "formula and reference in the running text, on the same line as 'Mais cette relation n'est plus exacte en général'; ordinary parentheses",
    "set as a display \\[...\\] with \\left( \\right) and \\quad before the reference",
    "formula", None, "high",
    r"car on a alors¶\[¶\bigcap_{\lambda\in L}\operatorname{Ker}((\varphi_\lambda)_s)¶=\left(\bigcap_{\lambda\in L}\operatorname{Ker}(\varphi_\lambda)\right)_s¶\quad(\mathbf 0_{\mathrm I},1.3.2).¶\]¶Mais",
    r"car on a alors¶$\bigcap_{\lambda\in L}\operatorname{Ker}((\varphi_\lambda)_s)¶=(\bigcap_{\lambda\in L}\operatorname{Ker}(\varphi_\lambda))_s$¶$(\mathbf 0_{\mathrm I},1.3.2)$.¶Mais",
    "The print sets the indices under the two ∩ even in the line (index position ignored).")

# ---------------- page 162
add(162, "(11.9.4), end: 'sont égales à O_x = k(x), corps des fractions de A'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    r"$\mathcal O_x=k(x)$", r"$\mathcal O_x=\boldsymbol{k}(x)$",
    "")
add(162, "(11.9.5): 'G'_λ = G_λ ⊗_{O_X} O_{X'} = g'^*_λ(G_λ), où g'_λ : Z'_λ → Z_λ'",
    "G_λ⊗_{O_X}O_{X'} (enlarged crop)",
    "\\mathcal G_\\lambda\\otimes_{\\mathcal O_{Z_\\lambda}}\\mathcal O_{Z'_\\lambda}",
    "formula", None, "high",
    r"\otimes_{\mathcal O_{Z_\lambda}}¶\mathcal O_{Z'_\lambda}", r"\otimes_{\mathcal O_X}¶\mathcal O_{X'}",
    "The print uses EGA's notation G⊗_{O_X}O_{X'} for the inverse image on Z_λ×_X X' (as for F' = F⊗_{O_X}O_{X'} just before); not a misprint. Independent of the next entry (no overlap).")
add(162, "same formula: '= g'^*_λ(G_λ), où g'_λ : Z'_λ → Z_λ est la projection canonique'",
    "g'^*_λ(G_λ): no parentheses around g'_λ (enlarged crop)",
    "(g'_\\lambda)^*(\\mathcal G_\\lambda)",
    "formula", None, "high",
    r"=(g'_\lambda)^*(\mathcal G_\lambda)$, où", r"=g'^*_\lambda(\mathcal G_\lambda)$, où",
    "In the display defining ψ just below, the print does write (g'_λ)^*(G_λ) with parentheses (matches the TeX); only this occurrence changes.")
add(162, "(11.9.5), display defining u'_λ: 'g^*((f_λ)_*(G_λ)) --g^*(ψ)--> g^*(g_*((f'_λ)_*(G'_λ))) --σ--> (f'_λ)_*(G'_λ)'",
    "g^*(g_*((f'_λ)_*(G'_λ))): parentheses after g^* (enlarged crop)",
    "g^*g_*((f'_\\lambda)_*(\\mathcal G'_\\lambda))",
    "formula", None, "high",
    r"\xrightarrow{g^*(\psi)}g^*g_*((f'_\lambda)_*(\mathcal G'_\lambda))",
    r"\xrightarrow{g^*(\psi)}g^*(g_*((f'_\lambda)_*(\mathcal G'_\lambda)))",
    "")
add(162, "(11.9.5), second paragraph: 'son image canonique t'' par Γ(f_λ^{-1}(U), G_λ) → Γ(g'^{-1}_λ(f_λ^{-1}(U)), G'_λ)'",
    "g'^{-1}_λ(f_λ^{-1}(U)): no parentheses around g'_λ (enlarged crop)",
    "(g'_\\lambda)^{-1}(f_\\lambda^{-1}(U))",
    "formula", None, "high",
    r"\Gamma((g'_\lambda)^{-1}(f_\lambda^{-1}(U))", r"\Gamma(g'^{-1}_\lambda(f_\lambda^{-1}(U))",
    "")
add(162, "same sentence: 'alors u'_λ(t') est la restriction de t'' à f'^{-1}_λ(U')'",
    "f'^{-1}_λ(U'): no parentheses around f'_λ (enlarged crop)",
    "(f'_\\lambda)^{-1}(U')",
    "formula", None, "high",
    r"à $(f'_\lambda)^{-1}(U')$", r"à $f'^{-1}_\lambda(U')$",
    "")
add(162, "end of (11.9.5): 'ρ_{F'} : F' → (j'_λ)_*(j'^*_λ(F')) = (j'_λ)_*(G'_λ)'",
    "j'^*_λ(F'): no parentheses around j'_λ (enlarged crop)",
    "(j'_\\lambda)_*((j'_\\lambda)^*(\\mathcal F'))",
    "formula", None, "high",
    r"(j'_\lambda)_*((j'_\lambda)^*(\mathcal F'))", r"(j'_\lambda)_*(j'^*_\lambda(\mathcal F'))",
    "")
add(162, "(11.9.6): 'si l'on pose Y'_λμ = g'^{-1}_λ(Y_λμ), l'homomorphisme v'_λμ'",
    "g'^{-1}_λ(Y_λμ): no parentheses around g'_λ (enlarged crop)",
    "(g'_\\lambda)^{-1}(Y_{\\lambda\\mu})",
    "formula", None, "high",
    r"=(g'_\lambda)^{-1}(Y_{\lambda\mu})", r"=g'^{-1}_\lambda(Y_{\lambda\mu})",
    "")

# ---------------- page 163
add(163, "top line (end of (11.9.6)): 'ρ_{G'_λ} : G'_λ → (j'_λμ)_*(j'^*_λμ(G'_λ))'",
    "j'^*_λμ(G'_λ): no parentheses around j'_λμ (enlarged crop)",
    "(j'_{\\lambda\\mu})_*((j'_{\\lambda\\mu})^*(\\mathcal G'_\\lambda))",
    "formula", None, "high",
    r"((j'_{\lambda\mu})^*(\mathcal G'_\lambda))$", r"(j'^*_{\lambda\mu}(\mathcal G'_\lambda))$",
    "")
add(163, "Proposition (11.9.7): 'Avec les notations de (11.9.1) et (11.9.5), supposons'",
    "the references (11.9.1) and (11.9.5) upright in the italic statement",
    "set italic by the proposition environment",
    "convention", 6, "high",
    r"notations de (11.9.1) et (11.9.5), supposons", r"notations de \textup{(11.9.1)} et \textup{(11.9.5)}, supposons",
    "Two references, one edit.")
add(163, "proof of (11.9.7): 'qu'on peut se borner au cas où tous les Z_λ sont égaux à X.'",
    "'égaux à' in italics (enlarged crop)",
    "'égaux à' upright (the proof environment is roman)",
    "italics", None, "high",
    r"sont égaux¶à $X$.", r"sont \emph{égaux¶à} $X$.",
    "")
add(163, "Remarque (11.9.8): 'Or, on ne peut appliquer la proposition (11.9.4) à D(h') = Spec(A'_h')'",
    "'la proposition (11.9.4)'",
    "'la proposition (11.9.4)': keeps the printed reading",
    "misprint_in_print", None, "medium",
    None, None,
    "The proposition whose hypothesis (A' projective over A) fails for A'_h' is (11.9.7); (11.9.4) is the criterion paragraph, cited correctly earlier in the same remark ('il faudrait en effet (11.9.4) prouver'). Not in the authors' errata list (ega4-errata-addenda-list3-fr.tex).",
    corrected="la proposition (11.9.7)", nofix=True)
add(163, "Corollaire (11.9.9): 'Soient X un préschéma artinien,'",
    "'artinien' upright in the italic statement",
    "italic (environment)",
    "convention", 6, "high",
    r"préschéma artinien,", r"préschéma \textup{artinien},",
    "")
add(163, "Corollaire (11.9.9): 'g : X'→X un morphisme plat (on notera que ces deux conditions sont satisfaites si X est le spectre d'un corps et g un morphisme quelconque).'",
    "'plat (on notera que ... le spectre d'un' and 'et g un morphisme' upright; 'corps' and 'quelconque' italic; ')' upright",
    "the whole passage italic (environment), so \\emph{corps} and \\emph{quelconque} come out upright",
    "convention", 6, "high",
    r"un morphisme plat (on notera que¶ces deux conditions sont satisfaites si $X$ est le spectre d'un \emph{corps}¶et $g$ un morphisme \emph{quelconque}).",
    r"un morphisme \textup{plat (on notera que¶ces deux conditions sont satisfaites si $X$ est le spectre d'un \emph{corps}¶et $g$ un morphisme \emph{quelconque})}.",
    "Inside \\textup the two \\emph words come out italic, as printed. Does not overlap the 'artinien' edit or the next one.")
add(163, "Corollaire (11.9.9): 'Alors, avec les notations de (11.9.1) et (11.9.5), si la famille (u_λ) est séparante'",
    "the references (11.9.1) and (11.9.5) upright in the italic statement",
    "italic (environment)",
    "convention", 6, "high",
    r"notations de (11.9.1)¶et (11.9.5), si la famille", r"notations de \textup{(11.9.1)}¶et \textup{(11.9.5)}, si la famille",
    "Two references, one edit.")
add(163, "Théorème (11.9.10): '(u_λ) une famille d'homomorphismes (11.9.1.1), g : X'→X un morphisme'",
    "the reference (11.9.1.1) upright in the italic statement",
    "italic (environment)",
    "convention", 6, "high",
    r"d'homomorphismes¶(11.9.1.1),", r"d'homomorphismes¶\textup{(11.9.1.1)},",
    "")
add(163, "Théorème (11.9.10): 'déduite de (u_λ) par le changement de base g (11.9.5).'",
    "the reference (11.9.5) upright in the italic statement",
    "italic (environment)",
    "convention", 6, "high",
    r"base $g$¶(11.9.5).", r"base $g$¶\textup{(11.9.5)}.",
    "")
add(163, "Théorème (11.9.10), item labels (i) (this page) and (ii) (p. 164)",
    "labels (i), (ii) upright",
    "\\begin{enumerate}[label=(\\roman*)] inside the italic theorem: italic labels",
    "convention", 6, "high",
    r"\begin{enumerate}[label=(\roman*)]¶  \item Si $g$", r"\begin{enumerate}[label=\textup{(\roman*)}]¶  \item Si $g$",
    "One edit covers (i) here and (ii) on p. 164 (GLOBAL_ISSUES 16).")

# ---------------- page 164
add(164, "Théorème (11.9.10), label (ii)",
    "'(ii)' upright",
    "italic label of the enumerate begun on p. 163",
    "convention", 6, "high",
    None, None,
    "Covered by the p. 163 edit of the enumerate's label option (that 'old' lies in page_163.tex).", nofix=True)
add(164, "Théorème (11.9.10) (ii): 'et en outre que l'une des deux conditions suivantes soit vérifiée'",
    "\"l'une\" upright in the italic statement (enlarged crop)",
    "italic (environment)",
    "convention", 6, "high",
    r"que l'une des", r"que \textup{l'une} des",
    "The labels a), b) are upright in the print and in the TeX (\\emph inside the italic theorem): no change.")
add(164, "proof of (11.9.10) (i): 'son image t' par l'homomorphisme canonique Γ(ρ) : Γ(U, F) → Γ(g^{-1}(U), g^*(F)) = Γ(U, g_*(g^*(F))) est nulle.'",
    "formula in the running text, on the same line as 'est nulle.'",
    "set as a display \\[...\\]",
    "formula", None, "high",
    r"l'homomorphisme canonique¶  \[¶  \Gamma(\rho):\Gamma(U,\mathcal F)\longrightarrow¶  \Gamma(g^{-1}(U),g^*(\mathcal F))¶  =\Gamma(U,g_*(g^*(\mathcal F)))¶  \]¶  est nulle.",
    r"l'homomorphisme canonique¶  $\Gamma(\rho):\Gamma(U,\mathcal F)\longrightarrow¶  \Gamma(g^{-1}(U),g^*(\mathcal F))¶  =\Gamma(U,g_*(g^*(\mathcal F)))$¶  est nulle.",
    "")
add(164, "same proof: 'par l'homomorphisme Γ(U, (f_λ)_*(G_λ)) → Γ(g^{-1}(U), g^*((f_λ)_*(G_λ))), donc sont nulles'",
    "formula in the running text, on the same line as 'donc sont nulles'",
    "set as a display \\[...\\] with the comma inside it",
    "formula", None, "high",
    r"des $u_\lambda(t)$ par l'homomorphisme¶  \[¶  \Gamma(U,(f_\lambda)_*(\mathcal G_\lambda))\longrightarrow¶  \Gamma(g^{-1}(U),g^*((f_\lambda)_*(\mathcal G_\lambda))),¶  \]¶  donc",
    r"des $u_\lambda(t)$ par l'homomorphisme¶  $\Gamma(U,(f_\lambda)_*(\mathcal G_\lambda))\longrightarrow¶  \Gamma(g^{-1}(U),g^*((f_\lambda)_*(\mathcal G_\lambda)))$,¶  donc",
    "Does not overlap the previous entry.")
add(164, "proof of (11.9.10) (ii): \"A' étant un A-module plat, et à prouver que\"",
    "'plat' in italics (enlarged crop)",
    "'plat' upright",
    "italics", None, "high",
    r"étant un $A$-module plat, et", r"étant un $A$-module \emph{plat}, et",
    "The later 'comme A' est un A-module plat, il résulte' is roman in the print, as in the TeX.")
add(164, "proof (ii) a): 'pour tout λ∈L, et où en outre L est fini.'",
    "'fini' in italics (enlarged crop)",
    "'fini' upright",
    "italics", None, "high",
    r"en outre $L$ est fini.", r"en outre $L$ est \emph{fini}.",
    "")
add(164, "proof (ii) b): 'de sorte que F' = M̃', G'_λ = Ñ'_λ'",
    "tilde over M only, the prime outside (enlarged crop)",
    "\\widetilde{M'}",
    "convention", 8, "high",
    r"\widetilde{M'}", r"\widetilde{M}'",
    "")
add(164, "same: 'G'_λ = Ñ'_λ'",
    "tilde over N only, prime and λ outside (enlarged crop)",
    "\\widetilde{N'_\\lambda}",
    "convention", 8, "high",
    r"\widetilde{N'_\lambda}", r"\widetilde{N}'_\lambda",
    "")
add(164, "proof (ii) b): 'si l'on pose J_i = s_1A + ... + s_iA, et A_i = A_{s_i}/J_{i-1}A_{s_i}' (left-hand side)",
    "𝔍_i: index i (enlarged crop)",
    "\\mathfrak J_k: index k",
    "formula", None, "high",
    r"\mathfrak J_k=", r"\mathfrak J_i=",
    "Second occurrence (s_iA) in the next entry; the dots in the entry after it. The three edits do not overlap.")
add(164, "same formula: '+ s_iA' (last term)",
    "s_iA: index i (enlarged crop)",
    "s_kA: index k",
    "formula", None, "high",
    r"+s_kA$", r"+s_iA$",
    "")
add(164, "same formula: 's_1A + ... + s_iA'",
    "baseline dots '. . .' between the + signs (enlarged crop)",
    "\\cdots",
    "symbol", None, "high",
    r"\cdots", r"\ldots",
    "The only \\cdots on the page.")
add(164, "proof (ii) b): 'Supposons donc i>0 et soit m un multiple commun des m_j'",
    "bold italic i in 'i>0' (wrong fount: stem about 7 px wide against 4 px for the italic i of 'sur i' one line above, same height; enlarged crop)",
    "$i>0$ with an ordinary italic i: silently corrected",
    "misprint_in_print", None, "high",
    r"donc $i>0$", r"donc $\boldsymbol{i}>0$",
    "Wrong-fount letter, reproduced in the diplomatic text like the bold italic n of EGA II (GLOBAL_ISSUES 29). The smaller subscript h's of the next two lines (A_h, B_h, B'_h) have ordinary stroke width (measured): no change there.",
    corrected=r"donc $i>0$")
add(164, "proof (ii) b): 'un multiple commun des m_j pour j≤i—1'",
    "long dash for the minus sign: 41 px wide, the same glyph as the set-difference dash of p. 58 'E=S—g(Y—Z)' (41-42 px); the equals signs of the page are 34-35 px",
    "$j\\leq i-1$ (minus sign)",
    "convention", 7, "medium",
    r"$j\leq i-1$", r"$j\leq i\setmin 1$",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7). The subscript minus signs (J_{i-1}, J_{h-1}, J'_{h-1}) are ordinary short minus signs.")

# ---------------- check every fix
texts = {}
for p in (159, 160, 161, 162, 163, 164):
    texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    n = texts[d["page"]].count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", d["page"], n, repr(d["fix"]["old"]))
# overlap check within a page: spans of the olds must be disjoint
for p in texts:
    spans = []
    for d in F:
        if d["fix"] and d["page"] == p:
            i = texts[p].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP", p, a, b)
# apply all fixes on a copy to be sure they compose
for p in texts:
    t = texts[p]
    for d in F:
        if d["fix"] and d["page"] == p:
            assert t.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t = t.replace(d["fix"]["old"], d["fix"]["new"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
print("written", len(F), "findings; problems:", bad)
for p in (159, 160, 161, 162, 163, 164):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
