"""Build findings_192_196.json for EGA III part 2, pp. 192-196 (checker run_III2).
'¶' in the raw strings below stands for a line break (LF)."""
import json, pathlib, sys

here = pathlib.Path(__file__).resolve().parent
run = here.parent
OUT = run / "findings_192_196.json"


def N(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": N(old), "new": N(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = N(corrected)
    d["note"] = note
    F.append(d)


WAVY = "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33."
LAYOUT = "Layout (GLOBAL_ISSUES item 21): the print sets the formula in the running text; the formula itself matches."
PARA = "The print starts a new indented paragraph here; the TeX has no blank line (GLOBAL_ISSUES item 47)."
KAPPA = ("ega3-7-fr.tex writes \\kappa(x) (77 times in the file) where the print has the residue field k(x) in bold: "
         "bold upright in subscripts, bold italic elsewhere (GLOBAL_ISSUES item 48).")
REMARK = "Judged with the remark body roman (document-wide remark-environment item)."

# ---------------- page 192 ----------------
add(192, "proof of (7.5.6): 'l'homothétie h_f : x→fx de M'", "plain arrow x→fx (enlarged crop)", r"$h_f:x\mapsto fx$",
    "convention", 3, "high", r"$h_f:x\mapsto fx$", r"$h_f:x\to fx$", "Plain arrow printed.")
add(192, "proof of (7.5.6): 'sans torsion (0_I, 6.3.4)'", "bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.3.4)", r"($\mathbf{0}_{\mathrm I}$, 6.3.4)", "Bold 0 in the reference (GLOBAL_ISSUES item 35 form).")
add(192, "proof of (7.5.6): 'la suite exacte 0→A→(h_f)A→k→0, qui fournit'", "in the running text", "displayed",
    "other", None, "high",
    r"la suite exacte¶\[¶  0\longrightarrow A\xrightarrow{h_f}A\longrightarrow k\longrightarrow0,¶\]¶qui fournit",
    r"la suite exacte¶$0\longrightarrow A\xrightarrow{h_f}A\longrightarrow k\longrightarrow0$,¶qui fournit", LAYOUT)
add(192, "proof of (7.5.6): display 'T_p(A)→T_p(k)→T_{p-1}(A)→(h_f)T_{p-1}(A)'", "no full stop after the display (enlarged crop)",
    "ends with a full stop", "punctuation", None, "high",
    r"\xrightarrow{h_f}T_{p-1}(A).", r"\xrightarrow{h_f}T_{p-1}(A)", "Extra full stop in the TeX.")
add(192, "proof of (7.5.6): 'On voit que T_{p-1}(A) est libre'", "new indented paragraph after the display",
    r"no blank line after \]", "other", None, "high", r"\]¶On voit que", r"\]¶¶On voit que", PARA)
add(192, "heading 7.6", "'7.6. Descente ... et critère d'exactitude de Grauert.' with a final full stop",
    r"\subsection{... de Grauert}: no full stop", "punctuation", None, "high",
    r"d'exactitude de Grauert}", r"d'exactitude de Grauert.}",
    "Same pattern as GLOBAL_ISSUES items 43 and 50 (section titles without the printed full stop); holds for ega3-7-fr.tex too.")
add(192, "(7.6.1): 'Sous les conditions de (7.4.1), soit B'", "(7.4.1) upright in the italic statement",
    "italic (statement environment)", "convention", 6, "high",
    r"de (7.4.1), soit $B$", r"de \textup{(7.4.1)}, soit $B$", "Roman reference inside an italic statement.")
add(192, "(7.6.1): 'exact à droite (resp. exact à gauche, exact) il en est de même'",
    "'(resp.' upright; the closing parenthesis italic (enlarged crop)", "italic", "convention", 6, "high",
    r"(resp. exact à gauche, exact) il en", r"\textup{(resp.} exact à gauche, exact) il en",
    "Same form as the p. 141 fix.")
add(192, "proof of (7.6.1): 'supposons d'abord que B soit un A-module plat'", "'plat' italic", "upright",
    "italics", None, "high", r"$A$-module plat. On a", r"$A$-module \emph{plat}. On a", "Italic in the print.")
add(192, "proof of (7.6.1): 'pour tout A-module M, H_•(P_•⊗_A(M⊗_A B))=(H_•(P_•⊗_A M))⊗_A B, ce qui'",
    "in the running text", "displayed", "other", None, "high",
    r"$M$,¶\[¶  H_\bullet\bigl(P_\bullet\otimes_A(M\otimes_A B)\bigr)¶  =¶  \bigl(H_\bullet(P_\bullet\otimes_A M)\bigr)\otimes_A B,¶\]¶ce qui",
    r"$M$,¶$H_\bullet(P_\bullet\otimes_A(M\otimes_A B))=(H_\bullet(P_\bullet\otimes_A M))\otimes_A B$,¶ce qui",
    LAYOUT + r" \bigl/\bigr dropped for the inline setting.")
add(192, "proof of (7.6.1): 'comme M⇝M_(B) est un foncteur exact'", "wavy arrow (enlarged crop)", r"\mapsto",
    "symbol", None, "high", r"$M\mapsto M_{(B)}$", r"$M\leadsto M_{(B)}$", WAVY)
add(192, "proof of (7.6.1): 'propriété d'exactitude (0_I, 6.4.1)'", "bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.4.1)", r"($\mathbf{0}_{\mathrm I}$, 6.4.1)", "Bold 0 in the reference.")
add(192, "(7.6.2): 'Sous les conditions de (7.4.1), on suppose'", "(7.4.1) upright", "italic", "convention", 6, "high",
    r"de (7.4.1), on suppose", r"de \textup{(7.4.1)}, on suppose", "Roman reference inside an italic statement.")
add(192, "(7.6.2): '(resp. exact à gauche, exact), il faut et il suffit'", "'(resp.' upright; closing parenthesis italic",
    "italic", "convention", 6, "high",
    r"(resp. exact à gauche, exact), il faut", r"\textup{(resp.} exact à gauche, exact), il faut",
    "Roman 'resp.' inside an italic statement.")
add(192, "proof of (7.6.2): 'le critère (0, 10.2.8)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0$, 10.2.8)", r"($\mathbf{0}$, 10.2.8)", "Bold 0 in the reference.")

# ---------------- page 193 ----------------
add(193, "proof of (7.6.2): 'B-modules plats (0_I, 6.2.1)'", "bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.2.1)", r"($\mathbf{0}_{\mathrm I}$, 6.2.1)", "Bold 0 in the reference.")
add(193, "proof of (7.6.2): 'on a H_•(P_•⊗_A N)=H_•((P_•⊗_A B)⊗_B N), donc T_p^(B)(N)=H_p((P_•⊗_A B)⊗_B N); appliquant'",
    "both formulas in the running text", "two displays", "other", None, "high",
    r"$N$, on a¶\[¶  H_\bullet(P_\bullet\otimes_A N)¶  =¶  H_\bullet\bigl((P_\bullet\otimes_A B)\otimes_B N\bigr),¶\]¶donc¶\[¶  T_p^{(B)}(N)¶  =¶  H_p\bigl((P_\bullet\otimes_A B)\otimes_B N\bigr);¶\]¶appliquant",
    r"$N$, on a¶$H_\bullet(P_\bullet\otimes_A N)=H_\bullet((P_\bullet\otimes_A B)\otimes_B N)$,¶donc $T_p^{(B)}(N)=H_p((P_\bullet\otimes_A B)\otimes_B N)$;¶appliquant",
    LAYOUT)
add(193, "(7.6.3): 'Sous les conditions de (7.4.1), supposons'", "(7.4.1) upright", "italic", "convention", 6, "high",
    r"de (7.4.1), supposons", r"de \textup{(7.4.1)}, supposons", "Roman reference inside an italic statement.")
add(193, "proof of (7.6.3): the three exact sequences 0→H_p→Z'_p→B_{p-1}→0 etc.",
    "no punctuation after any of the three sequences (enlarged crop)", "commas after the first two, full stop after the third",
    "punctuation", None, "high",
    r"B_{p-1}¶  \longrightarrow0,\\¶  0\longrightarrow B_{p-1}\longrightarrow Z_{p-1}\longrightarrow H_{p-1}¶  \longrightarrow0,\\¶  0\longrightarrow Z_{p-1}\longrightarrow P_{p-1}\longrightarrow B_{p-2}¶  \longrightarrow0.",
    r"B_{p-1}¶  \longrightarrow0\\¶  0\longrightarrow B_{p-1}\longrightarrow Z_{p-1}\longrightarrow H_{p-1}¶  \longrightarrow0\\¶  0\longrightarrow Z_{p-1}\longrightarrow P_{p-1}\longrightarrow B_{p-2}¶  \longrightarrow0",
    "Extra punctuation in the TeX.")
add(193, "proof of (7.6.3): 'Comme P_{p-1} et P_{p-2} sont plats'", "new indented paragraph after the display",
    r"no blank line after \end{gather*}", "other", None, "high", r"\end{gather*}¶Comme", r"\end{gather*}¶¶Comme", PARA)
add(193, "proof of (7.6.3): 'de leurs sous-modules respectifs'", "'sous-modules' italic", "upright", "italics", None, "high",
    r"sous-modules respectifs", r"\emph{sous-modules} respectifs", "Italic in the print.")
add(193, "proof of (7.6.3): 'Par définition, T_p(M)=Ker(d_p⊗1)/Im(d_{p+1}⊗1)'", "new indented paragraph after (7.6.3.4)",
    r"no blank line after \]", "other", None, "high",
    r"\label{III.7.6.3.4.fr}¶\]¶Par définition,", r"\label{III.7.6.3.4.fr}¶\]¶¶Par définition,", PARA)
add(193, "proof of (7.6.3): 'le noyau de l'homomorphisme (P_p⊗M)/Im(d_{p+1}⊗1)→P_{p-1}⊗M obtenu'", "in the running text",
    "displayed", "other", None, "high",
    r"l'homomorphisme¶\[¶  (P_p\otimes M)/\operatorname{Im}(d_{p+1}\otimes1)¶  \longrightarrow P_{p-1}\otimes M¶\]¶obtenu",
    r"l'homomorphisme¶$(P_p\otimes M)/\operatorname{Im}(d_{p+1}\otimes1)\longrightarrow P_{p-1}\otimes M$¶obtenu", LAYOUT)
add(193, "proof of (7.6.3): 'Comme w est injectif d'après (7.6.3.4)'", "new indented paragraph after the display",
    r"no blank line after \]", "other", None, "high", r"\]¶Comme $w$ est injectif", r"\]¶¶Comme $w$ est injectif", PARA)
add(193, "Remarques (7.6.4)(i): 'E^2_{pq}=Tor_q^A(H_q(P_•), M)=Tor_p^A(T_q(A), M)'",
    "the first Tor has the index q: Tor_q^A(H_q(P_•), M) (enlarged crop)", r"\operatorname{Tor}_p^A\bigl(H_q(P_\bullet),M\bigr)",
    "misprint_in_print", None, "high",
    r"\operatorname{Tor}_p^A\bigl(H_q(P_\bullet),M\bigr)", r"\operatorname{Tor}_q^A\bigl(H_q(P_\bullet),M\bigr)",
    "Misprint in the print: E^2_{pq}=Tor_p^A(H_q(P_•),M), as the second member Tor_p^A(T_q(A),M) shows. "
    "The TeX silently corrected it; the fix restores the printed reading.",
    corrected=r"\operatorname{Tor}_p^A\bigl(H_q(P_\bullet),M\bigr)")

# ---------------- page 194 ----------------
add(194, "top of the page, Remarques (7.6.4)(i): 'Or, l'hypothèse sur l'anneau A'",
    "first line indented: new paragraph after the display that ends p. 193", "no blank line (marker right after the \\])",
    "other", None, "high", r"\oldpage[III]{194}¶    Or, l'hypothèse", r"\oldpage[III]{194}¶¶    Or, l'hypothèse",
    PARA + r" Inside \item[(i)] of the remarks.")
add(194, "Remarques (7.6.4)(i): 'quelconques (0_IV, 17.2.2)'", "bold 0", r"$0_{\mathrm{IV}}$", "convention", 2, "high",
    r"($0_{\mathrm{IV}}$, 17.2.2)", r"($\mathbf{0}_{\mathrm{IV}}$, 17.2.2)", "Bold 0 in the reference.")
add(194, "(7.6.5): 'Sous les conditions de (7.4.1), supposons'", "(7.4.1) upright", "italic", "convention", 6, "high",
    r"de (7.4.1), supposons", r"de \textup{(7.4.1)}, supposons", "Roman reference inside an italic statement.")
add(194, "(7.6.5): 'En outre, pour que les termes extrêmes'", "new indented paragraph after (7.6.5.1)",
    r"no blank line after \]", "other", None, "high", r"\]¶En outre, pour que", r"\]¶¶En outre, pour que", PARA)
add(194, "proof of (7.6.5): 'D'autre part, comme T_p(A) est un module'", "new indented paragraph after the display",
    r"no blank line after \]", "other", None, "high", r"\]¶D'autre part, comme", r"\]¶¶D'autre part, comme", PARA)
add(194, "proof of (7.6.5): 'on a par définition T_p(A)⊗_A K=H_p(P_•)⊗_A K=H_p(P_•⊗_A K)=T_p(K). On a donc'",
    "in the running text", "displayed", "other", None, "high",
    r"on a par définition¶\[¶  T_p(A)\otimes_A K¶  =¶  H_p(P_\bullet)\otimes_A K¶  =¶  H_p(P_\bullet\otimes_A K)¶  =¶  T_p(K).¶\]¶On a donc bien",
    r"on a par définition¶$T_p(A)\otimes_A K=H_p(P_\bullet)\otimes_A K=H_p(P_\bullet\otimes_A K)=T_p(K)$.¶On a donc bien",
    LAYOUT)
add(194, "proof of (7.6.5): 'comme on sait (0, 10.1.3)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0$, 10.1.3)", r"($\mathbf{0}$, 10.1.3)", "Bold 0 in the reference.")
add(194, "(7.6.6): 'nous poserons, pour tout x∈Spec(A)' before (7.6.6.1)", "no comma after Spec(A) (enlarged crop)",
    "comma", "punctuation", None, "high",
    r"$x\in\operatorname{Spec}(A)$,¶\[", r"$x\in\operatorname{Spec}(A)$¶\[", "Extra comma in the TeX.")
add(194, "(7.6.6.1): 'd_p(x)=d_p^T(x)=rang_{k(x)} T_p(k(x)).'",
    "bold k: bold upright in the subscript, bold italic in T_p(k(x)) (enlarged crop)", r"\kappa(x) twice",
    "symbol", None, "high",
    r"\operatorname{rang}_{\kappa(x)}T_p(\kappa(x)).", r"\operatorname{rang}_{\mathbf{k}(x)}T_p(\boldsymbol{k}(x)).", KAPPA)
add(194, "(7.6.7): 'l'application correspondante (I, 1.2.1)'",
    "bold I; the parenthesised reference upright inside the italic statement", "plain I, italic", "convention", 2, "high",
    r"(I, 1.2.1)", r"\textup{(\textbf{I}, 1.2.1)}",
    "Also convention 6 (upright reference inside an italic statement); one edit covers both.")
add(194, "(7.6.7): 'Si l'on pose T'_•=T_•^(A') (7.1.3), on a'", "(7.1.3) upright", "italic", "convention", 6, "high",
    r"(7.1.3), on a", r"\textup{(7.1.3)}, on a", "Roman reference inside an italic statement.")

# ---------------- page 195 ----------------
add(195, "proof of (7.6.7): display 'H_•(P_•⊗_A k(x'))=H_•((P_•⊗_A k(x))⊗_{k(x)} k(x'))=H_•(P_•⊗_A k(x))⊗_{k(x)} k(x'),'",
    "bold italic k(x), k(x'); bold upright k(x) in the subscripts of ⊗ (enlarged crop)", r"\kappa (6 times)",
    "symbol", None, "high",
    r"  H_\bullet(P_\bullet\otimes_A\kappa(x'))¶  =¶  H_\bullet\bigl((P_\bullet\otimes_A\kappa(x))¶    \otimes_{\kappa(x)}\kappa(x')\bigr)¶  =¶  H_\bullet(P_\bullet\otimes_A\kappa(x))¶    \otimes_{\kappa(x)}\kappa(x'),",
    r"  H_\bullet(P_\bullet\otimes_A\boldsymbol{k}(x'))¶  =¶  H_\bullet\bigl((P_\bullet\otimes_A\boldsymbol{k}(x))¶    \otimes_{\mathbf{k}(x)}\boldsymbol{k}(x')\bigr)¶  =¶  H_\bullet(P_\bullet\otimes_A\boldsymbol{k}(x))¶    \otimes_{\mathbf{k}(x)}\boldsymbol{k}(x'),",
    KAPPA)
add(195, "proof of (7.6.7): 'puisque k(x') est plat sur k(x)'", "bold italic k", r"\kappa", "symbol", None, "high",
    r"puisque $\kappa(x')$ est plat sur $\kappa(x)$", r"puisque $\boldsymbol{k}(x')$ est plat sur $\boldsymbol{k}(x)$", KAPPA)
add(195, "(7.6.8): 'la fonction x⇝d_p^T(x) sur Spec(A)'", "wavy arrow (enlarged crop)", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto d_p^T(x)$", r"$x\leadsto d_p^T(x)$", WAVY)
add(195, "proof of (7.6.8): 'd_p est constante (0, 9.2.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0$, 9.2.2)", r"($\mathbf{0}$, 9.2.2)", "Bold 0 in the reference.")
add(195, "proof of (7.6.8): 'un anneau noethérien intègre; mais'", "'intègre' italic (enlarged crop)", "upright",
    "italics", None, "high", r"noethérien intègre; mais", r"noethérien \emph{intègre}; mais", "Italic in the print.")
add(195, "(7.6.9): 'soit d_p(x)=rang_{k(x)} T_p(k(x)). Alors :'",
    "in the running text; bold k (upright in the subscript, bold italic in T_p(k(x)))", r"displayed; \kappa(x) twice",
    "symbol", None, "high",
    r"soit¶\[¶  d_p(x)=\operatorname{rang}_{\kappa(x)}T_p(\kappa(x)).¶\]¶Alors :",
    r"soit¶$d_p(x)=\operatorname{rang}_{\mathbf{k}(x)}T_p(\boldsymbol{k}(x))$.¶Alors :",
    KAPPA + " The same edit sets the formula inline, as printed.")
add(195, "(7.6.9)(i): label '(i)'", "upright (enlarged crop)", "italic (statement environment)", "convention", 6, "high",
    r"\item[(i)] La fonction", r"\item[\textup{(i)}] La fonction", "GLOBAL_ISSUES item 16.")
add(195, "(7.6.9)(ii): label '(ii)'", "upright", "italic", "convention", 6, "high",
    r"\item[(ii)] Si $T_p$ est exact", r"\item[\textup{(ii)}] Si $T_p$ est exact", "GLOBAL_ISSUES item 16.")
add(195, "proof of (7.6.9)(i): 'il suffit donc (0, 9.2.4)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0$, 9.2.4)", r"($\mathbf{0}$, 9.2.4)", "Bold 0 in the reference.")
add(195, "proof of (7.6.9)(i): 'un morphisme f : Spec(B)→Spec(A) tels que'", "in the running text", "displayed",
    "other", None, "high",
    r"un morphisme¶    \[¶      f:\operatorname{Spec}(B)\longrightarrow\operatorname{Spec}(A)¶    \]¶    tels que",
    r"un morphisme¶    $f:\operatorname{Spec}(B)\longrightarrow\operatorname{Spec}(A)$¶    tels que", LAYOUT)
add(195, "proof of (7.6.9)(i): 'on ait f(a)=x et f(b)=y (II, 7.1.9)'", "f(b)=y (enlarged crop)", "$f(b)=y$",
    "misprint_in_print", None, "high", None, None,
    "Misprint in the print: the generic point b must map to the generization x' (no y is defined; the inequality "
    "to prove is d_p(x')<=d_p(x)). The TeX keeps the printed reading.",
    corrected=r"$f(b)=x'$")
add(195, "proof of (7.6.9)(i): '(II, 7.1.9)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 7.1.9)", r"(\textbf{II}, 7.1.9)", "Bold chapter number in the reference.")
add(195, "(7.6.10)(i): label '(i)'", "upright (enlarged crop)", "italic", "convention", 6, "high",
    r"\item[(i)] Pour tout", r"\item[\textup{(i)}] Pour tout", "GLOBAL_ISSUES item 16.")
add(195, "(7.6.10): 'En particulier, si A est intègre'", "new indented paragraph",
    r"follows \end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"\end{enumerate}¶En particulier", r"\end{enumerate}¶¶En particulier", PARA)

# ---------------- page 196 ----------------
add(196, "(7.6.10)(ii): label '(ii)'", "upright (enlarged crop)", "italic", "convention", 6, "high",
    r"\item[(ii)] Supposons en outre", r"\item[\textup{(ii)}] Supposons en outre", "GLOBAL_ISSUES item 16.")
add(196, "proof of (7.6.10): 'donc on a d_p(x)≤rang_k T_p(k) pour tout'", "in the running text", "displayed",
    "other", None, "high",
    r"donc on a¶\[¶  d_p(x)\leq\operatorname{rang}_k T_p(k)¶\]¶pour tout",
    r"donc on a¶$d_p(x)\leq\operatorname{rang}_k T_p(k)$¶pour tout", LAYOUT)
add(196, "(7.6.11.1): 'rang_{k(x)} T_p(k(x)) ≥ rang_{k(x)} (T_p(A)⊗_A k(x))'",
    "bold upright k in the subscripts, bold italic k elsewhere (enlarged crop)", r"\kappa (4 times)", "symbol", None, "high",
    r"  \operatorname{rang}_{\kappa(x)}T_p(\kappa(x))¶  \geq¶  \operatorname{rang}_{\kappa(x)}¶    \bigl(T_p(A)\otimes_A\kappa(x)\bigr)",
    r"  \operatorname{rang}_{\mathbf{k}(x)}T_p(\boldsymbol{k}(x))¶  \geq¶  \operatorname{rang}_{\mathbf{k}(x)}¶    \bigl(T_p(A)\otimes_A\boldsymbol{k}(x)\bigr)",
    KAPPA)
add(196, "(7.6.11): 'un anneau local noethérien'", "'local' italic (enlarged crop)", "no emphasis", "italics", None, "high",
    r"anneau local noethérien", r"anneau \emph{local} noethérien", REMARK)
add(196, "(7.6.11): 'les conditions suivantes sont équivalentes :'", "'équivalentes' italic", "no emphasis",
    "italics", None, "high", r"sont¶équivalentes :", r"sont¶\emph{équivalentes} :", REMARK)
add(196, "(7.6.11): label 'a)'", "italic a)", r"\item[a)]", "italics", None, "high",
    r"\item[a)]", r"\item[\emph{a)}]", REMARK + " Lettered labels italic in the print.")
add(196, "(7.6.11) a): 'Pour tout complexe P_•'", "'tout' italic (enlarged crop)", "no emphasis", "italics", None, "high",
    r"Pour tout complexe", r"Pour \emph{tout} complexe", REMARK)
add(196, "(7.6.11.2): 'rang_k(T_p(k)) ≥ rang_k(T_p(A)⊗_A k)'", "parentheses around T_p(k) (enlarged crop)",
    r"\operatorname{rang}_k T_p(k)", "formula", None, "high",
    r"\operatorname{rang}_k T_p(k)¶      \geq", r"\operatorname{rang}_k(T_p(k))¶      \geq", "Missing parentheses in the TeX.")
add(196, "(7.6.11): label 'b)'", "italic b)", r"\item[b)]", "italics", None, "high",
    r"\item[b)]", r"\item[\emph{b)}]", REMARK)
add(196, "(7.6.11): label 'c)'", "italic c)", r"\item[c)]", "italics", None, "high",
    r"\item[c)]", r"\item[\emph{c)}]", REMARK)
add(196, "(7.6.11): 'On notera qu'il revient au même'", "new indented paragraph",
    r"follows \end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"\end{enumerate}¶On notera", r"\end{enumerate}¶¶On notera", PARA)
add(196, "(7.6.11): 'de dire que l'on a, pour tout i≥1' before (7.6.11.5)", "no comma after i≥1 (enlarged crop)", "comma",
    "punctuation", None, "high", r"pour tout $i\geq1$,", r"pour tout $i\geq1$", "Extra comma in the TeX.")
add(196, "(7.6.11): 'Donnons rapidement quelques indications'", "new indented paragraph after (7.6.11.5)",
    r"no blank line after \]", "other", None, "high", r"\]¶Donnons rapidement", r"\]¶¶Donnons rapidement", PARA)
add(196, "(7.6.11): 'Pour voir que a) entraîne b)'", "'a)' and 'b)' italic", "no emphasis", "italics", None, "high",
    r"que a)¶entraîne b), on", r"que \emph{a)}¶entraîne \emph{b)}, on", REMARK)
add(196, "(7.6.11): 'une suite exacte L_1→(d)L_0→M→0 où'", "in the running text", "displayed", "other", None, "high",
    r"suite exacte¶\[¶  L_1\xrightarrow{d}L_0\longrightarrow M\longrightarrow0¶\]¶où",
    r"suite exacte¶$L_1\xrightarrow{d}L_0\longrightarrow M\longrightarrow0$¶où", LAYOUT)
add(196, "(7.6.11): 'et on applique a) au complexe'", "'a)' italic", "no emphasis", "italics", None, "high",
    r"on applique a) au", r"on applique \emph{a)} au", REMARK)
add(196, "(7.6.11): 'au complexe P_1→(td)P_0 avec P_0=Ľ_1, P_1=Ľ_0, les autres termes'",
    "in the running text, with the word 'avec' after P_1→P_0", r"displayed; no 'avec' (a comma and \qquad instead)",
    "missing", None, "high",
    r"\[¶  P_1\xrightarrow{{}^t d}P_0,¶  \qquad¶  P_0=\check L_1,¶  \quad¶  P_1=\check L_0,¶\]¶les autres",
    r"$P_1\xrightarrow{{}^t d}P_0$ avec $P_0=\check L_1$, $P_1=\check L_0$,¶les autres",
    "Missing word 'avec'; the same edit sets the formulas inline, as printed.")
add(196, "(7.6.11): 'T_1(k)=Hom_A(M, k)=Hom_k(M/mM, k), autrement dit'", "in the running text", "displayed",
    "other", None, "high",
    r"et¶\[¶  T_1(k)¶  =¶  \operatorname{Hom}_A(M,k)¶  =¶  \operatorname{Hom}_k(M/\mathfrak mM,k),¶\]¶autrement dit",
    r"et¶$T_1(k)=\operatorname{Hom}_A(M,k)=\operatorname{Hom}_k(M/\mathfrak mM,k)$,¶autrement dit", LAYOUT)
add(196, "(7.6.11): 'Pour prouver que b) entraîne c)'", "'b)' and 'c)' italic (enlarged crop)", "no emphasis",
    "italics", None, "high", r"que b) entraîne c),", r"que \emph{b)} entraîne \emph{c)},", REMARK)
add(196, "(7.6.11): 'nous établirons d'abord le lemme suivant'", "'établirons' (future; enlarged crop)", "'établissons'",
    "word", None, "high", r"établissons", r"établirons", "Wrong tense in the TeX.")
add(196, "(7.6.11.6): 'Étant donné un complexe ...→0→P_1→(d)P_0→0→... de A-modules plats'",
    "in the running text; baseline dots", r"displayed; \cdots", "symbol", None, "high",
    r"complexe¶\[¶  \cdots\longrightarrow0\longrightarrow¶  P_1\xrightarrow{d}P_0¶  \longrightarrow0\longrightarrow\cdots¶\]¶de",
    r"complexe¶$\ldots\longrightarrow0\longrightarrow P_1\xrightarrow{d}P_0\longrightarrow0\longrightarrow\ldots$¶de",
    "Baseline dots in the print (GLOBAL_ISSUES item 22); the same edit sets the complex inline, as printed.")

# ---------------- checks ----------------
ok = True
texts = {p: (run / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(192, 197)}
for p, t in texts.items():
    if "\r" in t:
        print(f"page {p}: CR characters present"); ok = False
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    c = texts[d["page"]].count(fx["old"])
    if c != 1:
        ok = False
        sys.stdout.buffer.write(f"#{i} p{d['page']}: old occurs {c} times: {fx['old']!r}\n".encode("utf-8"))
# overlapping olds on the same page
for p in texts:
    spans = []
    for i, d in enumerate(F):
        if d["page"] == p and d["fix"]:
            s = texts[p].find(d["fix"]["old"])
            spans.append((s, s + len(d["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print(f"page {p}: overlap between findings #{a[2]} and #{b[2]}")
# simulate applying all fixes per page in order
for p in texts:
    t = texts[p]
    for d in F:
        if d["page"] == p and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print(f"page {p}: sequential apply failed")
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(192, 197):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "OK" if ok else "PROBLEMS")
