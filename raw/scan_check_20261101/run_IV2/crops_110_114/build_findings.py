"""Build and verify findings_110_114.json (scan check of EGA IV-2 pp. 110-114).

In the raw strings below the pilcrow character stands for a line break (LF).
"""
import json
import sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV2"
OUT = RUN + r"\findings_110_114.json"
NL = "\u00b6"


def n(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": n(old), "new": n(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = n(corrected)
    d["note"] = note
    F.append(d)


C2 = ("bold I", "plain I")
C2_0 = ("bold 0 in (0_I, ...)", "$(0_{\\mathrm I},...)$ with a plain 0")

# ---------------------------------------------------------------- page 110
add(110, "before (5.9.1.3): 'si i : X—Z→X est l'injection canonique'", "long dash X—Z", r"$i:X-Z\to X$ (minus sign)",
    "convention", 7, "high", r"$i:X-Z\to X$", r"$i:X\setmin Z\to X$")
add(110, "(5.9.1.3): 'i_*(ℱ|X—Z)'", "long dash X—Z", r"i_*(\mathcal F|X-Z) (minus sign)",
    "convention", 7, "high", r"(\mathcal F|X-Z)", r"(\mathcal F|X\setmin Z)")
add(110, "Proposition (5.9.2), label (i)", "label (i) upright", r"\item[(i)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(110, "Proposition (5.9.2) (i): 'Le foncteur ℱ ⇝ ℋ⁰_{X/Z}(ℱ)'", "wavy arrow ⇝ (crop)", r"\mathcal F\mapsto\mathcal H^0_{X/Z}(\mathcal F)",
    "symbol", None, "high", r"$\mathcal F\mapsto\mathcal H^0_{X/Z}(\mathcal F)$", r"$\mathcal F\leadsto\mathcal H^0_{X/Z}(\mathcal F)$",
    "Wavy arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3.")
add(110, "Proposition (5.9.2), label (ii)", "label (ii) upright", r"\item[(ii)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(110, "proof of (5.9.2): '(I, 9.2.2)'", *C2, "convention", 2, "high", "(I, 9.2.2)", r"(\textbf{I}, 9.2.2)")
add(110, "proof of (5.9.2): '(I, 1.3.9)'", *C2, "convention", 2, "high", "(I, 1.3.9)", r"(\textbf{I}, 1.3.9)")
add(110, "Remarque (5.9.3), l. 1: 'Si ℱ est une 𝒪_X-Algèbre'", "'Algèbre' italic in the roman remark (crop)",
    r"$\mathcal O_X$-Algèbre without \emph", "italics", None, "high",
    r"$\mathcal O_X$-Algèbre, il en est", r"$\mathcal O_X$-\emph{Algèbre}, il en est",
    "Emphasis judged with the remark body roman (document-wide remark item). The later '𝒪_X-Algèbre quasi-cohérente' and 'la 𝒪_X-Algèbre B̃' are roman in the print.")
add(110, "Remarque (5.9.3): '(0_I, 4.2.4)'", *C2_0, "convention", 2, "high",
    r"$(0_{\mathrm I},4.2.4)$", r"$(\mathbf{0}_{\mathrm I},4.2.4)$")
add(110, "Remarque (5.9.3): '(I, 9.6.1)'", *C2, "convention", 2, "high", "(I, 9.6.1)", r"(\textbf{I}, 9.6.1)")
add(110, "Remarque (5.9.3): 'où A est intègre et noethérien'", "'intègre' italic (crop)", "intègre without \\emph",
    "italics", None, "high", r"$A$ est intègre et", r"$A$ est \emph{intègre} et",
    "Emphasis judged with the remark body roman.")
add(110, "Remarque (5.9.3): '(I, 8.2.1.1)'", *C2, "convention", 2, "high", "(I, 8.2.1.1)", r"(\textbf{I}, 8.2.1.1)")
add(110, "(5.9.4.1), end of the display", "no full stop after the display (crop)", r"... (f^*(\mathcal F)). (full stop)",
    "punctuation", None, "high", r"(f^*(\mathcal F)).¶\tag{5.9.4.1}", r"(f^*(\mathcal F))¶\tag{5.9.4.1}")
add(110, "proof of (5.9.4): 'U'_α = X'—Z'_α = f^{-1}(U_α)'", "long dash X'—Z'_α", r"X'-Z'_\alpha (minus sign)",
    "convention", 7, "high", r"X'-Z'_\alpha", r"X'\setmin Z'_\alpha")
add(110, "proof of (5.9.4): 'l'homomorphisme canonique f^*((i_α)_*(ℱ|U_α)) → (i'_α)_*(f^*(ℱ)|U'_α) est bijectif'",
    "the formula is in the running text", "displayed with \\[ \\]", "formula", None, "high",
    r"canonique¶\[¶f^*((i_\alpha)_*(\mathcal F|U_\alpha))¶\longrightarrow(i'_\alpha)_*(f^*(\mathcal F)|U'_\alpha)¶\]¶est bijectif",
    r"canonique¶$f^*((i_\alpha)_*(\mathcal F|U_\alpha))¶\longrightarrow(i'_\alpha)_*(f^*(\mathcal F)|U'_\alpha)$¶est bijectif",
    "No connecting words lost.")
add(110, "end of page_110.tex (printed p. 111, l. 2): 'un isomorphisme canonique lim_α (f^*((i_α)_*(ℱ|U_α))) ⥲ ℋ⁰_{X'/Z'}(f^*(ℱ)). Mais comme ...'",
    "the formula is in the running text, followed on the same line by 'Mais comme le foncteur f^* ...' (crop of p. 111)",
    "displayed with \\[ \\], followed by a blank line before the p. 111 marker", "formula", None, "high",
    r"canonique¶\[¶\varinjlim_\alpha¶f^*((i_\alpha)_*(\mathcal F|U_\alpha))¶\xrightarrow{\sim}\mathcal H^0_{X'/Z'}(f^*(\mathcal F)).¶\]¶¶",
    r"canonique¶$\varinjlim_\alpha¶(f^*((i_\alpha)_*(\mathcal F|U_\alpha)))¶\xrightarrow{\sim}\mathcal H^0_{X'/Z'}(f^*(\mathcal F))$.¶",
    "One edit: sets the formula inline, restores the outer parentheses of the next finding and drops the blank line at the end of the p. 110 segment; with marker edit 2 (p. 111) no paragraph break remains before 'Mais comme', as printed. Apply before marker edit 1 below.")
add(110, "same formula (printed p. 111, l. 2): 'lim_α (f^*((i_α)_*(ℱ|U_α)))'",
    "outer parentheses around f^*(...): three closing parentheses before ⥲ (crop)",
    r"\varinjlim_\alpha f^*((i_\alpha)_*(\mathcal F|U_\alpha)) without them", "formula", None, "high", None, None,
    "Covered by the edit of the previous finding.")
add(110, "printed p. 111 begins: marker \\oldpage[IV-2]{111} (edit 1 of 2, insert)",
    "printed p. 110 ends with the commutative diagram; p. 111 begins 'est commutatif, on a donc, en passant à la limite, un isomorphisme canonique'",
    "\\oldpage[IV-2]{111} stands after the lim display, before 'Mais comme' (start of page_111.tex): two printed lines of p. 111 sit in the p. 110 segment",
    "marker", None, "high", "est commutatif, on a donc", r"\oldpage[IV-2]{111}¶est commutatif, on a donc",
    "Inserts the marker after the diagram's \\], on its own line, no blank lines. Apply after every other page-110 fix and together with edit 2 (page 111), which removes the misplaced marker.")

# ---------------------------------------------------------------- page 111
add(111, "page start: marker \\oldpage[IV-2]{111} (edit 2 of 2, remove the misplaced marker)", "see the page-110 marker finding",
    "\\oldpage[IV-2]{111} and a blank line directly before 'Mais comme le foncteur'", "marker", None, "high",
    r"\oldpage[IV-2]{111}¶¶Mais comme", "Mais comme",
    "Apply together with, and after, marker edit 1 (page 110). With the page-110 lim edit (which removes the blank line before the old marker), 'Mais comme ...' continues the paragraph, as printed.")
add(111, "'commute aux limites inductives (0_I, 4.3.2)'", *C2_0, "convention", 2, "high",
    r"$(0_{\mathrm I},4.3.2)$", r"$(\mathbf{0}_{\mathrm I},4.3.2)$")
add(111, "l. 3: 'cela donne par définition l'isomorphisme (5.9.1.1) cherché'", "'(5.9.1.1)' (crop)", "(5.9.1.1) (keeps the print)",
    "misprint_in_print", None, "low", None, None,
    "Possibly a misprint: the isomorphism sought is (5.9.4.1), while (5.9.1.1) is the definition of ℋ⁰_{X/Z}; the reference may instead be meant for 'par définition'. Check before correcting.",
    corrected="(5.9.4.1)")
add(111, "Corollaire (5.9.5): 'Sous les hypothèses de (5.9.4)'", "the reference is upright inside the italic statement (crop)",
    "(5.9.4) inside the italic corollary: italic", "convention", 6, "high",
    "hypothèses de (5.9.4), si", r"hypothèses de \textup{(5.9.4)}, si")
add(111, "proof of (5.9.5): '(0_I, 5.3.11)'", *C2_0, "convention", 2, "high",
    r"$(0_{\mathrm I},5.3.11)$", r"$(\mathbf{0}_{\mathrm I},5.3.11)$")
add(111, "(5.9.6.1), end of the display", "no full stop after the display (crop)", r"...(\widetilde{\mathcal F}_x). (full stop)",
    "punctuation", None, "high", r"(\widetilde{\mathcal F}_x).¶\tag{5.9.6.1}", r"(\widetilde{\mathcal F}_x)¶\tag{5.9.6.1}")
add(111, "proof of (5.9.6): '(I, 1.6.5)'", *C2, "convention", 2, "high", "(I, 1.6.5)", r"(\textbf{I}, 1.6.5)")
add(111, "(5.9.7): 'un homomorphisme canonique fonctoriel ℱ→(i_α)^*(ℱ|U_α) (0_I, 4.4.3.2), et ces homomorphismes'",
    "the formula and the reference are in the running text (crop)", "displayed with \\[ \\] (reference inside the display after \\quad)",
    "formula", None, "high",
    r"fonctoriel¶\[¶\mathcal F\longrightarrow(i_\alpha)_*(\mathcal F|U_\alpha)¶\quad(0_{\mathrm I},4.4.3.2),¶\]",
    r"fonctoriel¶$\mathcal F\longrightarrow(i_\alpha)_*(\mathcal F|U_\alpha)$¶$(\mathbf{0}_{\mathrm I},4.4.3.2)$,",
    "The same edit gives the reference its bold 0 (convention-2 finding below). Apply before the misprint fix (i_α)^* below.")
add(111, "(5.9.7): '(0_I, 4.4.3.2)'", *C2_0, "convention", 2, "high", None, None,
    "Covered by the edit of the previous finding.")
add(111, "(5.9.7): 'ℱ→(i_α)^*(ℱ|U_α)'", "the star is raised: (i_α)^* (crop)",
    "(i_\\alpha)_* (the TeX silently corrects)", "misprint_in_print", None, "high",
    r"\longrightarrow(i_\alpha)_*", r"\longrightarrow(i_\alpha)^*",
    "The direct image (i_α)_* is meant (as in (0_I, 4.4.3.2) and (5.9.1.1)). Restores the printed reading; list order: after the display edit above, whose result still contains this old string.",
    corrected=r"(i_\alpha)_*")
add(111, "(5.9.7.1), end of the display", "no full stop after the display (crop)", r"...\mathcal H^0_{X/Z}(\mathcal F). (full stop)",
    "punctuation", None, "high", r"(\mathcal F).¶\tag{5.9.7.1}", r"(\mathcal F)¶\tag{5.9.7.1}")
add(111, "Proposition (5.9.8), label a)", "label a) upright (crop)", r"\item[a)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]")
add(111, "Proposition (5.9.8) a): 'ρ_{X/Z} (5.9.7.1) est injectif'", "the reference is upright (crop)",
    "(5.9.7.1) inside the italic proposition: italic", "convention", 6, "high",
    r"$\rho_{X/Z}$ (5.9.7.1) est injectif¶(resp.", r"$\rho_{X/Z}$ \textup{(5.9.7.1)} est injectif¶(\textup{resp.}",
    "The same edit covers the upright 'resp.' of the next finding.")
add(111, "Proposition (5.9.8) a): '(resp. bijectif)'", "'resp.' upright (crop)", "(resp. ...): italic",
    "convention", 6, "high", None, None, "Covered by the edit of the previous finding.")
add(111, "Proposition (5.9.8), label b)", "label b) upright (crop)", r"\item[b)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]")
add(111, "Proposition (5.9.8) b), after the display: 'est injectif (resp. bijectif)'", "'resp.' upright", "(resp. ...): italic",
    "convention", 6, "high", r"U_\alpha,\mathcal F)¶\]¶est injectif (resp.", r"U_\alpha,\mathcal F)¶\]¶est injectif (\textup{resp.}")
add(111, "Proposition (5.9.8), label a')", "label a') upright (crop)", r"\item[a')] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[a')]", r"\item[\textup{a')}]")
add(111, "Proposition (5.9.8) a'): 'l'homomorphisme canonique (0_I, 4.4.3.2)'", *C2_0, "convention", 2, "high",
    r"canonique $(0_{\mathrm I},4.4.3.2)$", r"canonique $(\mathbf{0}_{\mathrm I},4.4.3.2)$")
add(111, "Proposition (5.9.8) a'), display: 'ℱ → i_*(ℱ|X—T)'", "long dash X—T", r"i_*(\mathcal F|X-T) (minus sign)",
    "convention", 7, "high", r"i_*(\mathcal F|X-T)", r"i_*(\mathcal F|X\setmin T)")
add(111, "Proposition (5.9.8) a'): '(où i : X—T→X est l'injection canonique)'", "long dash X—T (crop)", r"$i:X-T\to X$ (minus sign)",
    "convention", 7, "high", r"$i:X-T\to X$", r"$i:X\setmin T\to X$")
add(111, "Proposition (5.9.8) a'): 'est injectif (resp. bijectif)'", "'resp.' upright (crop)", "(resp. ...): italic",
    "convention", 6, "high", r"canonique) est injectif¶(resp.", r"canonique) est injectif¶(\textup{resp.}")
add(111, "Proposition (5.9.8), label b')", "label b') upright (crop)", r"\item[b')] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[b')]", r"\item[\textup{b')}]")
add(111, "Proposition (5.9.8) b'), display: 'Γ(V, ℱ) → Γ(V∩(X—T), ℱ)'", "long dash X—T", r"V\cap(X-T) (minus sign)",
    "convention", 7, "high", r"\Gamma(V\cap(X-T),\mathcal F)", r"\Gamma(V\cap(X\setmin T),\mathcal F)")
add(111, "Proposition (5.9.8) b'), after the display: 'est injectif (resp. bijectif)'", "'resp.' upright", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. bijectif).¶\end{enumerate}", r"(\textup{resp.} bijectif).¶\end{enumerate}")
add(111, "last line: 'l'équivalence de a) et b) (resp. a') et b'))'", "the labels a), b), a'), b') are italic in the roman text (crop)",
    "plain a) et b) (resp. a') et b'))", "italics", None, "high",
    "l'équivalence de a) et b) (resp. a') et b'))", r"l'équivalence de \emph{a)} et \emph{b)} (resp. \emph{a')} et \emph{b')})",
    "The closing parenthesis of '(resp. ...)' stays upright.")

# ---------------------------------------------------------------- page 112
add(112, "page start: 'résulte de | la définition du foncteur Γ'", "the sentence runs on over the page break; p. 112 begins flush left, no new paragraph",
    "blank line after \\oldpage[IV-2]{112}: paragraph break inside the sentence", "other", None, "high",
    r"\oldpage[IV-2]{112}¶¶la définition", r"\oldpage[IV-2]{112}¶la définition",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20); page_111.tex ends without a blank line, so this edit suffices.")
add(112, "(5.9.8.1): 'Γ(V∩(X—T), ℱ)'", "long dash X—T", r"(X-T) (minus sign)",
    "convention", 7, "high", r"(X-T),\mathcal F)\longrightarrow", r"(X\setmin T),\mathcal F)\longrightarrow")
add(112, "after (5.9.8.1): 'Γ(V, ℱ) → Γ(V∩(X—T), ℱ); d'autre part'", "long dash X—T", r"(X-T) (minus sign)",
    "convention", 7, "high", r"(X-T),\mathcal F)$; d'autre", r"(X\setmin T),\mathcal F)$; d'autre")
add(112, "'le fait que b') implique b) résulte'", "b') and b) italic in the roman text (crop)", "plain b') and b)",
    "italics", None, "high", "fait que b') implique b) résulte", r"fait que \emph{b')} implique \emph{b)} résulte")
add(112, "'Γ(V, ℱ) → Γ(V∩(X—T), ℱ), et pour cela il suffit'", "long dash X—T", r"(X-T) (minus sign)",
    "convention", 7, "high", r"(X-T),\mathcal F)$, et pour", r"(X\setmin T),\mathcal F)$, et pour")
add(112, "'V par U et V∩(X—T) par U''", "long dash X—T", r"$V\cap(X-T)$ (minus sign)",
    "convention", 7, "high", r"$V\cap(X-T)$ par", r"$V\cap(X\setmin T)$ par")
add(112, "Définition (5.9.9): 'Sous les hypothèses de (5.9.8)'", "the reference is upright inside the italic statement (crop)",
    "(5.9.8) inside the italic definition: italic", "convention", 6, "high", "(5.9.8), on dit", r"\textup{(5.9.8)}, on dit")
add(112, "Définition (5.9.9): 'Z-pur (resp. Z-clos) si'", "'resp.' upright (crop)", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. $Z$-clos) si", r"(\textup{resp.} $Z$-clos) si")
add(112, "Définition (5.9.9): 'est injectif (resp. bijectif)'", "'resp.' upright (crop)", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. bijectif).¶\end{definition}", r"(\textup{resp.} bijectif).¶\end{definition}")
add(112, "'On dit que ℱ est Z-pur (resp. Z-clos) en un point x∈X'", "'pur' and 'clos' italic, like 'en un point' (crop)",
    "only 'en un point' in \\emph", "italics", None, "high",
    r"est $Z$-pur (resp. $Z$-clos) \emph{en un point}", r"est $Z$-\emph{pur} (resp. $Z$-\emph{clos}) \emph{en un point}")
add(112, "'(avec les notations de (5.9.6)) ℱ_x est Z_x-pur'", "ℱ_x without a tilde (crop)", r"$\widetilde{\mathcal F}_x$",
    "formula", None, "high", r"$\widetilde{\mathcal F}_x$ est", r"$\mathcal F_x$ est",
    "Not a misprint: by the preceding paragraph a module M is Z-pur when M̃ is, so 'ℱ_x est Z_x-pur' reads correctly.")
add(112, "'l'homomorphisme canonique ℱ_x→(ℋ⁰_{X/Z}(ℱ))_x est injectif'", "the formula is in the running text (crop)",
    "displayed with \\[ \\]", "formula", None, "high",
    r"canonique¶\[¶\mathcal F_x\longrightarrow(\mathcal H^0_{X/Z}(\mathcal F))_x¶\]¶est",
    r"canonique¶$\mathcal F_x\longrightarrow(\mathcal H^0_{X/Z}(\mathcal F))_x$¶est")
add(112, "same sentence: 'est injectif (resp. bijectif)'", "'injectif' and 'bijectif' italic (crop)", "plain injectif, bijectif",
    "italics", None, "high", r"est injectif (resp. bijectif).¶¶On notera", r"est \emph{injectif} (resp. \emph{bijectif}).¶¶On notera")
add(112, "'On notera que pour tout x∈X—Z'", "long dash X—Z (crop)", r"$x\in X-Z$ (minus sign)",
    "convention", 7, "high", r"$x\in X-Z$, $\mathcal F$", r"$x\in X\setmin Z$, $\mathcal F$")
add(112, "same sentence: 'ℱ est Z-clos au point x'", "'clos au point' italic (crop)", "plain clos au point",
    "italics", None, "high", r"$Z$-clos au point $x$", r"$Z$-\emph{clos au point} $x$")
add(112, "Corollaire (5.9.10), label (i)", "label (i) upright (crop)", r"\item[(i)] comes out italic in the italic corollary",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(112, "Corollaire (5.9.10) (i): 'soit Z-pur (resp. Z-clos), il faut'", "'resp.' upright (crop)", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. $Z$-clos), il faut", r"(\textup{resp.} $Z$-clos), il faut")
add(112, "Corollaire (5.9.10) (i): '(resp. (Z∩V_λ)-clos)'", "'resp.' upright (crop)", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. $(Z\cap", r"(\textup{resp.} $(Z\cap")
add(112, "Corollaire (5.9.10), label (ii)", "label (ii) upright", r"\item[(ii)] comes out italic in the italic corollary",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(112, "Corollaire (5.9.10) (ii): 'est Z-pur (resp. Z-clos), il est'", "'resp.' upright", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. $Z$-clos), il est", r"(\textup{resp.} $Z$-clos), il est")
add(112, "Corollaire (5.9.10) (ii): '(resp. Z'-clos)'", "'resp.' upright", "(resp. ...): italic",
    "convention", 6, "high", r"(resp. $Z'$-clos)", r"(\textup{resp.} $Z'$-clos)")
add(112, "'Cela résulte aussitôt de (5.9.8, b'))'", "b') italic (crop)", "plain b')",
    "italics", None, "high", "(5.9.8, b'))", r"(5.9.8, \emph{b')})")
add(112, "Proposition (5.9.11): 'Sous les hypothèses de (5.9.8)'", "the reference is upright inside the italic statement",
    "(5.9.8) inside the italic proposition: italic", "convention", 6, "high",
    r"(5.9.8), les $\mathcal O_X$-Modules", r"\textup{(5.9.8)}, les $\mathcal O_X$-Modules")
add(112, "Proposition (5.9.11): 'u se factorise d'une seule manière en ℱ →(ρ_{X/Z}) ℋ⁰_{X/Z}(ℱ) →(v) ℱ'. Si en outre'",
    "the formula is in the running text (crop)", "displayed with \\[ \\]", "formula", None, "high",
    r"manière en¶\[¶\mathcal F\xrightarrow{\rho_{X/Z}}\mathcal H^0_{X/Z}(\mathcal F)¶\xrightarrow{v}\mathcal F'.¶\]¶Si en outre",
    r"manière en¶$\mathcal F\xrightarrow{\rho_{X/Z}}\mathcal H^0_{X/Z}(\mathcal F)¶\xrightarrow{v}\mathcal F'$.¶Si en outre")
add(112, "proof of (5.9.11): 'pour tout x∈X—Z, on a'", "long dash X—Z", r"$x\in X-Z$ (minus sign)",
    "convention", 7, "high", r"$x\in X-Z$, on a", r"$x\in X\setmin Z$, on a")
add(112, "proof of (5.9.11): 'i.e. que (ρ_{X/Z})_x est bijectif, ou encore que ℱ est Z-pur en x, comme il a été signalé plus haut (5.9.9)'",
    "'Z-pur en x' (crop)", "$Z$-pur en $x$ (keeps the print)", "misprint_in_print", None, "medium", None, None,
    "Bijectivity of (ρ_{X/Z})_x means Z-clos at x (definition after (5.9.9)); Z-pur is only injectivity, and the remark referred to ('On notera que pour tout x∈X—Z, ℱ est Z-clos au point x') says Z-clos.",
    corrected=r"$Z$-clos en $x$")
add(112, "proof of (5.9.11): 'pour un ouvert noethérien V de X, lim_β Γ(V∩U_β, ℋ⁰_{X/Z}(ℱ)) est égale à'",
    "the formula is in the running text", "displayed with \\[ \\]", "formula", None, "high",
    r"de $X$,¶\[¶\varinjlim_\beta¶\Gamma(V\cap U_\beta,\mathcal H^0_{X/Z}(\mathcal F))¶\]¶est égale",
    r"de $X$,¶$\varinjlim_\beta¶\Gamma(V\cap U_\beta,\mathcal H^0_{X/Z}(\mathcal F))$¶est égale")
add(112, "proof of (5.9.11): 'mais par définition Γ(V∩U_β, ℋ⁰_{X/Z}(ℱ)) = lim_α Γ(V∩U_α∩U_β, ℱ). Or, la famille double'",
    "the formula is in the running text ('Or, la famille double ...' follows on the same line)", "displayed with \\[ \\]",
    "formula", None, "high",
    r"définition¶\[¶\Gamma(V\cap U_\beta,\mathcal H^0_{X/Z}(\mathcal F))¶=\varinjlim_\alpha\Gamma(V\cap U_\alpha\cap U_\beta,\mathcal F).¶\]¶Or,",
    r"définition¶$\Gamma(V\cap U_\beta,\mathcal H^0_{X/Z}(\mathcal F))¶=\varinjlim_\alpha\Gamma(V\cap U_\alpha\cap U_\beta,\mathcal F)$.¶Or,")

# ---------------------------------------------------------------- page 113
add(113, "second diagram, right vertical arrow (i_α)_*(ℱ'|U_α) → ℋ⁰_{X/Z}(ℱ')",
    "a plain rule without arrowhead that stops short of ℋ⁰_{X/Z}(ℱ') (crop); the left vertical and both verticals of the first diagram have arrowheads",
    "\\ar[d] (arrowhead: the TeX silently corrects)", "misprint_in_print", None, "medium",
    r"(\mathcal F'|U_\alpha)\ar[d]", r"(\mathcal F'|U_\alpha)\ar@{-}[d]",
    "A printing defect (missing arrowhead) rather than a textual misprint; the coordinator may prefer to record it without reproducing it.",
    corrected=r"(i_\alpha)_*(\mathcal F'|U_\alpha)\ar[d]")
add(113, "'l'homomorphisme correspondant Γ(V, ℋ⁰_{X/Z}(ℱ)) → Γ(V, ℱ') est alors un isomorphisme'",
    "the formula is in the running text", "displayed with \\[ \\]", "formula", None, "high",
    r"correspondant¶\[¶\Gamma(V,\mathcal H^0_{X/Z}(\mathcal F))¶\longrightarrow\Gamma(V,\mathcal F')¶\]¶est alors",
    r"correspondant¶$\Gamma(V,\mathcal H^0_{X/Z}(\mathcal F))¶\longrightarrow\Gamma(V,\mathcal F')$¶est alors")
add(113, "'t_y=0 pour tout y∈V∩(X—Z)'", "long dash X—Z", r"(X-Z) (minus sign)",
    "convention", 7, "high", r"$y\in V\cap(X-Z)$", r"$y\in V\cap(X\setmin Z)$")
add(113, "'un ouvert contenant V∩(X—Z)'", "long dash X—Z", r"(X-Z) (minus sign)",
    "convention", 7, "high", r"contenant $V\cap(X-Z)$", r"contenant $V\cap(X\setmin Z)$")
add(113, "'l'élément 0 de Γ(V, ℋ⁰_{X/Z}(ℱ)). Prouvons maintenant'", "'Prouvons maintenant' continues the same line and paragraph (crop)",
    "blank line before 'Prouvons': new paragraph", "other", None, "high",
    r"(\mathcal F))$.¶¶Prouvons", r"(\mathcal F))$.¶Prouvons")
add(113, "'pour tout x∈V∩(X—Z) il existe'", "long dash X—Z", r"(X-Z) (minus sign)",
    "convention", 7, "high", r"$x\in V\cap(X-Z)$", r"$x\in V\cap(X\setmin Z)$")
add(113, "'deux points quelconques x, x' de V∩(X—Z); les'", "long dash X—Z", r"(X-Z) (minus sign)",
    "convention", 7, "high", r"de $V\cap(X-Z)$; les", r"de $V\cap(X\setmin Z)$; les")
add(113, "'voisinage ouvert U de (X—Z)∩V'", "long dash X—Z", r"(X-Z) (minus sign)",
    "convention", 7, "high", r"$(X-Z)\cap V$", r"$(X\setmin Z)\cap V$")
add(113, "last line: 'est la Z-clôture de ℱ'", "'clôture' italic (crop)", "plain clôture",
    "italics", None, "high", r"la $Z$-clôture de", r"la $Z$-\emph{clôture} de")

# ---------------------------------------------------------------- page 114
FONT_C = ("bold italic C (crop), not the roundhand script of 𝒪_X", r"\mathcal C (script)")
add(114, "Remarques (5.9.12) (i): 'Soit C(X) la catégorie'", *FONT_C, "font", None, "high",
    r"Soit $\mathcal C(X)$", r"Soit $\boldsymbol{C}(X)$",
    "Bold italic category letter, as elsewhere (GLOBAL_ISSUES 35, 44).")
add(114, "(i): 'et soit C_Z(X)'", *FONT_C, "font", None, "high", r"soit $\mathcal C_Z(X)$", r"soit $\boldsymbol{C}_Z(X)$")
add(114, "(i): 'la sous-catégorie de C(X) formée'", *FONT_C, "font", None, "high", r"de $\mathcal C(X)$ formée", r"de $\boldsymbol{C}(X)$ formée")
add(114, "(i): 'le foncteur i^* : C(X) → C(X—Z)'", "both C bold italic (crop)", r"\mathcal C twice", "font", None, "high",
    r"$i^*:\mathcal C(X)\to\mathcal C(", r"$i^*:\boldsymbol{C}(X)\to\boldsymbol{C}(")
add(114, "(i): 'C(X—Z) (où'", "long dash X—Z (crop)", r"(X-Z) (minus sign)", "convention", 7, "high",
    r"(X-Z)$ (où", r"(X\setmin Z)$ (où")
add(114, "(i): '(où i : X—Z→X est l'injection canonique)'", "long dash X—Z (crop)", r"$i:X-Z\to X$ (minus sign)",
    "convention", 7, "high", r"(où $i:X-Z\to X$", r"(où $i:X\setmin Z\to X$")
add(114, "(i): 'définit une équivalence de catégories'", "'équivalence' italic in the roman remark (crop)", "plain équivalence",
    "italics", None, "high", "une équivalence de", r"une \emph{équivalence} de", "Emphasis judged with the remark body roman.")
add(114, "(i): 'de catégories C(X)/C_Z(X) ≈ C(X—Z).'", "the formula ends the line in the running text (crop)",
    "displayed with \\[ \\]", "formula", None, "high",
    r"catégories¶\[¶\mathcal C(X)/\mathcal C_Z(X)\approx\mathcal C(X-Z).¶\]",
    r"catégories¶$\boldsymbol{C}(X)/\boldsymbol{C}_Z(X)\approx\boldsymbol{C}(X\setmin Z)$.",
    "One edit for the three differences in this formula: inline (this finding), bold italic C (next) and the long dash (convention 7, after it).")
add(114, "(i): same formula, the three C", *FONT_C, "font", None, "high", None, None, "Covered by the edit of the previous finding.")
add(114, "(i): same formula, 'C(X—Z)'", "long dash X—Z", r"(X-Z) (minus sign)", "convention", 7, "high", None, None,
    "Covered by the edit of the finding before the previous one.")
add(114, "(ii): 'est équivalente à Supp(ℱ)⊂Z'", "'équivalente' italic (crop)", "plain équivalente",
    "italics", None, "high", "est équivalente à", r"est \emph{équivalente} à", "Emphasis judged with the remark body roman.")
add(114, "(iii): 'désigne le faisceau induit sur le sous-espace'", "'induit' italic (crop)", "plain induit",
    "italics", None, "high", "le faisceau induit sur", r"le faisceau \emph{induit} sur", "Emphasis judged with the remark body roman.")
add(114, "heading 5.10", "'5.10. Propriété (S₂) et Z-clôture.' with a final full stop (crop)",
    r"\subsection{\texorpdfstring{Propriété $(S_2)$ et $Z$-clôture}{...}} without it", "punctuation", None, "high",
    r"et $Z$-clôture}{", r"et $Z$-clôture.}{", "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(114, "(5.10.1.1), end of the display", "no full stop after the display (crop)", r"...\operatorname{prof}(\mathcal F_x). (full stop)",
    "punctuation", None, "high", r"(\mathcal F_x).¶\tag{5.10.1.1}", r"(\mathcal F_x)¶\tag{5.10.1.1}")
add(114, "Proposition (5.10.2), label a)", "label a) upright (crop)", r"\item[a)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]")
add(114, "Proposition (5.10.2), label b)", "label b) upright (crop)", r"\item[b)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]")
add(114, "Proposition (5.10.2), label c)", "label c) upright (crop)", r"\item[c)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]")
add(114, "proof of (5.10.2): 'tout ouvert U⊃X—Z'", "long dash X—Z", r"$U\supset X-Z$ (minus sign)",
    "convention", 7, "high", r"$U\supset X-Z$", r"$U\supset X\setmin Z$")
add(114, "proof of (5.10.2): 'l'homomorphisme de restriction Γ(V, ℱ) → Γ(V∩U, ℱ) est injectif (5.9.8)'",
    "the formula is in the running text (crop)", "displayed with \\[ \\]", "formula", None, "high",
    r"restriction¶\[¶\Gamma(V,\mathcal F)\longrightarrow\Gamma(V\cap U,\mathcal F)¶\]¶est injectif",
    r"restriction¶$\Gamma(V,\mathcal F)\longrightarrow\Gamma(V\cap U,\mathcal F)$¶est injectif")
add(114, "proof of (5.10.2): 'd'où l'équivalence de a) et b)'", "a) and b) italic (crop)", "plain a), b)",
    "italics", None, "high", "l'équivalence de a) et¶b).", r"l'équivalence de \emph{a)} et¶\emph{b)}.")
add(114, "proof of (5.10.2): 'l'équivalence de b) et c)'", "b) and c) italic (crop)", "plain b), c)",
    "italics", None, "high", "l'équivalence de b) et c).", r"l'équivalence de \emph{b)} et \emph{c)}.")
add(114, "Corollaire (5.10.3): 'Soit 0→ℱ'→ℱ→ℱ''→0 une suite exacte'", "the sequence is in the running text (crop)",
    "displayed with \\[ \\]", "formula", None, "high",
    r"Soit¶\[¶0\longrightarrow\mathcal F'\longrightarrow\mathcal F¶\longrightarrow\mathcal F''\longrightarrow0¶\]¶une suite",
    r"Soit¶$0\longrightarrow\mathcal F'\longrightarrow\mathcal F¶\longrightarrow\mathcal F''\longrightarrow0$¶une suite")


# ---------------------------------------------------------------- checks
def page_text(p):
    with open(rf"{RUN}\page_{p}.tex", encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
texts = {p: page_text(p) for p in range(110, 115)}
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    c = texts[d["page"]].count(d["fix"]["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], c, repr(d["fix"]["old"]))

# sequential application, diplomatic (all fixes) and corrected (no misprint fixes)
for mode in ("diplomatic", "corrected"):
    cur = dict(texts)
    for i, d in enumerate(F):
        if d["fix"] is None or (mode == "corrected" and d["kind"] == "misprint_in_print"):
            continue
        t = cur[d["page"]]
        c = t.count(d["fix"]["old"])
        if c != 1:
            ok = False
            print("SEQ FAIL", mode, i, d["page"], c, repr(d["fix"]["old"]))
            continue
        cur[d["page"]] = t.replace(d["fix"]["old"], d["fix"]["new"])
    if mode == "diplomatic":
        with open(RUN + r"\crops_110_114\after_diplomatic.txt", "w", encoding="utf-8") as fh:
            for p in range(110, 115):
                fh.write(f"===== page {p}\n" + cur[p])

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(110, 115):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "OK" if ok else "PROBLEMS")
sys.exit(0 if ok else 1)
