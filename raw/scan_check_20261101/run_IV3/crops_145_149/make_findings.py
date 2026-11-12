import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_145_149.json"


def F(old, new):
    return {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}


def E(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


DISP = "formula inline in the running text"
DISPT = "displayed (\\[ ... \\])"
DISPN = "Display vs inline (GLOBAL_ISSUES 21); no connecting word lost or added."
NO = "The edition's usual form is n\\textsuperscript{o} (as in the pp. 120-124 findings)."

L = []

# ---------------- page 145 ----------------
# (the blank lines around \oldpage[IV-3]{145} were removed by the applied pp. 140-144 batch)
L.append(E(145, "proof of (11.4.1), l. 3: 'Tout revient donc à prouver que ⋂_{λ∈L}(M_0⊗_{A_0}R_λ)=0. Or, par définition'",
           DISP, DISPT, "formula",
           F(r"que¶\[¶\bigcap_{\lambda\in L}(M_0\otimes_{A_0}R_\lambda)=0.¶\]¶Or, par",
             r"que¶$\bigcap_{\lambda\in L}(M_0\otimes_{A_0}R_\lambda)=0$.¶Or, par"), DISPN))
L.append(E(145, "proof of (11.4.1): 'des homomorphismes 𝔍_nA/𝔍_{n+1}A→𝔍^nB_λ/𝔍^{n+1}B_λ, lorsque λ parcourt L'",
           DISP, DISPT, "formula",
           F(r"homomorphismes¶\[¶\mathfrak J_nA/\mathfrak J_{n+1}A¶\longrightarrow\mathfrak J^nB_\lambda/\mathfrak J^{n+1}B_\lambda,¶\]¶lorsque",
             r"homomorphismes¶$\mathfrak J_nA/\mathfrak J_{n+1}A¶\longrightarrow\mathfrak J^nB_\lambda/\mathfrak J^{n+1}B_\lambda$,¶lorsque"), DISPN))
L.append(E(145, "proof of (11.4.1): 'on voit aussitôt que l'on a M_0⊗_{A_0}(⋂_{λ∈L}R_λ)=⋂_{λ∈L}(M_0⊗_{A_0}R_λ), d'où la proposition'",
           DISP + "; text-size parentheses", DISPT, "formula",
           F(r"l'on a¶\[¶M_0\otimes_{A_0}\Big(\bigcap_{\lambda\in L}R_\lambda\Big)¶=\bigcap_{\lambda\in L}(M_0\otimes_{A_0}R_\lambda),¶\]¶d'où",
             r"l'on a¶$M_0\otimes_{A_0}(\bigcap_{\lambda\in L}R_\lambda)¶=\bigcap_{\lambda\in L}(M_0\otimes_{A_0}R_\lambda)$,¶d'où"),
           DISPN + " \\Big dropped with the display."))
L.append(E(145, "proof of (11.4.3): 'l'intersection des noyaux des homomorphismes A_i→A→(u_λ)B_λ est réduite à 0'",
           DISP, DISPT, "formula",
           F(r"homomorphismes¶\[¶A_i\longrightarrow A\xrightarrow{u_\lambda}B_\lambda¶\]¶est réduite",
             r"homomorphismes¶$A_i\longrightarrow A\xrightarrow{u_\lambda}B_\lambda$¶est réduite"), DISPN))
L.append(E(145, "proof of (11.4.3): 'si l'on pose 𝔍_λ=𝔍B_λ, (M⊗_AB_λ)⊗_{B_λ}(B_λ/𝔍_λ)=(M⊗_A(A/𝔍))⊗_{A/𝔍}(B_λ/𝔍_λ) est un (B_λ/𝔍_λ)-module libre'",
           DISP, DISPT, "formula",
           F(r"\[¶(M\otimes_A B_\lambda)\otimes_{B_\lambda}(B_\lambda/\mathfrak J_\lambda)¶=(M\otimes_A(A/\mathfrak J))\otimes_{A/\mathfrak J}¶ (B_\lambda/\mathfrak J_\lambda)¶\]¶est un",
             r"$(M\otimes_A B_\lambda)\otimes_{B_\lambda}(B_\lambda/\mathfrak J_\lambda)¶=(M\otimes_A(A/\mathfrak J))\otimes_{A/\mathfrak J}¶ (B_\lambda/\mathfrak J_\lambda)$¶est un"), DISPN))
L.append(E(145, "proof of (11.4.3), l. 3: 'un nombre fini d'anneaux locaux A_i dont le radical est nilpotent'",
           "'locaux' italic (enlarged crop)", "roman", "italics",
           F(r"d'anneaux locaux $A_i$", r"d'anneaux \emph{locaux} $A_i$")))
L.append(E(145, "proof of (11.4.3): 'On peut donc se borner au cas où A est en outre local.'",
           "'local' italic (enlarged crop)", "roman", "italics",
           F(r"est en outre¶local.", r"est en outre¶\emph{local}.")))
L.append(E(145, "proof of (11.4.3): 'M⊗_AB_λ est un B_λ-module libre, en vertu de (11.4.1)'",
           "'libre' italic (enlarged crop)", "roman", "italics",
           F(r"$B_\lambda$-module libre, en vertu", r"$B_\lambda$-module \emph{libre}, en vertu")))
L.append(E(145, "proof of (11.4.3): '(Bourbaki, Alg. comm., chap. II, § 3, nº 5, prop. 16)'",
           "n with a superior letter o (enlarged crop)", "n$^\\circ$ (degree ring)", "symbol",
           F(r"n$^\circ$~5", r"n\textsuperscript{o}~5"), NO))
L.append(E(145, "proof of (11.4.3): '(loc. cit., § 4, nº 3, cor. 1 de la prop. 15)'",
           "n with a superior letter o", "n$^\\circ$ (degree ring)", "symbol",
           F(r"n$^\circ$~3", r"n\textsuperscript{o}~3"), NO))
L.append(E(145, "end of Corollaire (11.4.4) on p. 145 (structural move, edit 1 of 3)",
           "the statement of (11.4.4) does not end on p. 145: p. 146 opens with its second sentence 'Pour qu'un homomorphisme u : A→A' soit tel que M⊗_AA' soit un A'-module libre (resp. un A'-module plat), il faut et il suffit que u se factorise en A→A/𝔎_0→A' (ou encore que 𝔎_0A'=0).', italic and flush left (same paragraph); the proof begins with the indented paragraph 'Le fait que l'intersection 𝔎_0 ...'",
           "\\end{corollary} at the end of p. 145; that sentence is the first paragraph of the proof (roman, after the proof heading)", "other",
           F(r").¶\end{corollary}¶¶", r").¶"),
           "Apply together with the two p. 146 structural entries (\\begin{proof} removed at the top of p. 146; \\end{corollary} and \\begin{proof} inserted before 'Le fait que'). Order on this page: apply this edit BEFORE the convention-6 entry for '(qui est aussi ... plat)' that follows; that entry's 'old' still matches afterwards, not the other way round."))
L.append(E(145, "Corollaire (11.4.4), last line of p. 145: '(qui est aussi le plus petit des idéaux 𝔎 tels que M⊗_A(A/𝔎) soit un (A/𝔎)-module plat)'",
           "the whole parenthesis roman, with 'plat' italic (enlarged crop)", "italic like the statement; 'plat' not set off",
           "convention", F(r"(qui est aussi le plus petit¶des idéaux $\mathfrak K$ tels que $M\otimes_A(A/\mathfrak K)$ soit un¶$(A/\mathfrak K)$-module plat)",
                           r"\textup{(qui est aussi le plus petit¶des idéaux $\mathfrak K$ tels que $M\otimes_A(A/\mathfrak K)$ soit un¶$(A/\mathfrak K)$-module \emph{plat})}"),
           "Apply after the structural entry just above.", convention=6))

# ---------------- page 146 ----------------
L.append(E(146, "top of p. 146 (structural move, edit 2 of 3): 'Pour qu'un homomorphisme u : A→A' soit tel que ...'",
           "continues the italic statement of (11.4.4), flush left, no proof heading",
           "\\begin{proof} (after a blank line) opens before this sentence", "other",
           F(r"\oldpage[IV-3]{146}¶¶\begin{proof}¶Pour qu'un", r"\oldpage[IV-3]{146}¶Pour qu'un"),
           "Apply together with the end-of-p.-145 edit (\\end{corollary} removed there) and the p. 146 edit before 'Le fait que'. The blank line goes too: the print continues the paragraph of p. 145."))
L.append(E(146, "(11.4.4), second sentence, l. 1: 'soit un A'-module libre (resp. un A'-module plat)'",
           "'(resp.' roman; 'un A'-module plat' italic (enlarged crop)", "roman throughout (inside the proof); italic once moved into the corollary",
           "convention", F(r"libre (resp. un $A'$-module plat)", r"libre \textup{(resp.} un $A'$-module plat)"),
           "Takes effect with the structural move of this sentence into the corollary; harmless otherwise.", convention=6))
L.append(E(146, "(11.4.4), second sentence, end: '(ou encore que 𝔎_0A'=0).'",
           "roman (enlarged crop)", "roman inside the proof; italic once moved into the corollary",
           "convention", F(r"(ou encore que¶$\mathfrak K_0A'=0$)", r"\textup{(ou encore que¶$\mathfrak K_0A'=0$)}"),
           "As the previous entry. Does not overlap the structural edit that follows (which starts at the full stop).", convention=6))
L.append(E(146, "p. 146, before 'Le fait que l'intersection 𝔎_0 des idéaux 𝔎' (structural move, edit 3 of 3)",
           "the proof of (11.4.4) begins here (indented paragraph)", "the proof began before 'Pour qu'un homomorphisme'", "other",
           F(r".¶¶Le fait que l'intersection", r".¶\end{corollary}¶¶\begin{proof}¶Le fait que l'intersection"),
           "Apply together with the other two structural edits (end of p. 145, top of p. 146)."))
L.append(E(146, "proof of (11.4.4): 'Si A' est une (A/𝔎_0)-algèbre, on a M⊗_AA'=(M⊗_A(A/𝔎_0))⊗_{A/𝔎_0}A', donc'",
           DISP, DISPT, "formula",
           F(r"on a¶\[¶M\otimes_A A'=¶(M\otimes_A(A/\mathfrak K_0))\otimes_{A/\mathfrak K_0}A',¶\]¶donc",
             r"on a¶$M\otimes_A A'=¶(M\otimes_A(A/\mathfrak K_0))\otimes_{A/\mathfrak K_0}A'$,¶donc"), DISPN))
L.append(E(146, "proof of (11.4.4): 'à l'idéal nilpotent 𝔍𝔎/𝔎 et à l'homomorphisme injectif A/𝔎→A''",
           "𝔍𝔎/𝔎: the two Fraktur letters side by side, no plus sign, no parentheses (enlarged crop)",
           "$(\\mathfrak J+\\mathfrak K)/\\mathfrak K$: silent correction", "misprint_in_print",
           F(r"$(\mathfrak J+\mathfrak K)/\mathfrak K$", r"$\mathfrak J\mathfrak K/\mathfrak K$"),
           "The ideal meant is the image of the nilpotent ideal 𝔍 in A/𝔎, (𝔍+𝔎)/𝔎; 𝔍𝔎 lies inside 𝔎. Not in the Err_IV list (ega4-errata-addenda-list3).",
           corrected=r"(\mathfrak J+\mathfrak K)/\mathfrak K"))
L.append(E(146, "proof of (11.4.4): 'et à l'homomorphisme injectif A/𝔎→A''",
           "'injectif' italic (enlarged crop)", "roman", "italics",
           F(r"l'homomorphisme injectif¶$A/\mathfrak K", r"l'homomorphisme \emph{injectif}¶$A/\mathfrak K")))
L.append(E(146, "proof of (11.4.4): '(en conservant naturellement l'hypothèse que M⊗_A(A/𝔍) est un (A/𝔍)-module libre)'",
           "'libre' italic (enlarged crop)", "roman", "italics",
           F(r"$(A/\mathfrak J)$-module libre) résulte", r"$(A/\mathfrak J)$-module \emph{libre}) résulte")))
L.append(E(146, "proof of (11.4.5), l. 3: 'tels que f=f_(Y) et 𝓕=𝓕_1⊗_{𝒪_{Y_1}}𝒪_Y'",
           "f=f_(Y): the second f has no index 1 (enlarged crop; no gap where it would stand)",
           "$f=(f_1)_{(Y)}$: silent correction", "misprint_in_print",
           F(r"$f=(f_1)_{(Y)}$", r"$f=f_{(Y)}$"),
           "f is the base change of f_1 : X_1→Y_1 (cf. 𝓕=𝓕_1⊗_{𝒪_{Y_1}}𝒪_Y in the same clause).",
           corrected=r"f=(f_1)_{(Y)}"))
L.append(E(146, "proof of (11.4.5): 'supposer que les M_{i0} soient des A_0-modules libres.'",
           "'libres' italic (enlarged crop)", "roman", "italics",
           F(r"des $A_0$-modules¶libres.", r"des $A_0$-modules¶\emph{libres}.")))
L.append(E(146, "last line of p. 146: '... il y a donc pour chaque i un idéal 𝔍_i⊂𝔑 tel' | p. 147 'que les A-algèbres A' ...'",
           "mid-sentence page break; p. 147 starts flush left", "blank line before \\oldpage[IV-3]{147}", "other",
           F(r"\subset\mathfrak N$ tel¶¶", r"\subset\mathfrak N$ tel¶"),
           "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 147 entry that removes the blank line after the marker."))

# ---------------- page 147 ----------------
L.append(E(147, "top of p. 147: 'que les A-algèbres A' pour lesquelles ...' continues the last sentence of p. 146",
           "flush left, no indent", "blank line after \\oldpage[IV-3]{147}", "other",
           F(r"\oldpage[IV-3]{147}¶¶que les", r"\oldpage[IV-3]{147}¶que les"),
           "GLOBAL_ISSUES 20. Apply together with the last p. 146 entry (blank line before the marker)."))
SETMIN = "Set difference; \\setmin of the IV-3 preamble (convention-7 decision pending)."
L.append(E(147, "Corollaire (11.4.6): 'alors il existe t∈A—𝔭 tel que M_t soit un A_t-module libre'",
           "long dash A—𝔭 (enlarged crop)", "A-\\mathfrak p", "convention",
           F(r"$t\in A-\mathfrak p$ tel que $M_t$", r"$t\in A\setmin\mathfrak p$ tel que $M_t$"), SETMIN, convention=7))
L.append(E(147, "proof of (11.4.6): '(en remplaçant au besoin A par A_h, où h∈A—𝔭)'",
           "long dash A—𝔭 (enlarged crop)", "A-\\mathfrak p", "convention",
           F(r"$h\in A-\mathfrak p$", r"$h\in A\setmin\mathfrak p$"), SETMIN, convention=7))
L.append(E(147, "proof of (11.4.6): 'il existe t∈A—𝔭 tel que 𝔍_t=0'",
           "long dash A—𝔭 (enlarged crop)", "A-\\mathfrak p", "convention",
           F(r"$t\in A-\mathfrak p$ tel que¶$\mathfrak J_t", r"$t\in A\setmin\mathfrak p$ tel que¶$\mathfrak J_t"), SETMIN, convention=7))
L.append(E(147, "proof of (11.4.7): 'l'intersection des noyaux des homomorphismes A/𝔍_n→A_{𝔭_i}/𝔭_i^nA_{𝔭_i} est nulle dans A/𝔍_n'",
           DISP, DISPT, "formula",
           F(r"des homomorphismes¶\[¶A/\mathfrak J_n\longrightarrow¶A_{\mathfrak p_i}/\mathfrak p_i^nA_{\mathfrak p_i}¶\]¶est nulle",
             r"des homomorphismes¶$A/\mathfrak J_n\longrightarrow¶A_{\mathfrak p_i}/\mathfrak p_i^nA_{\mathfrak p_i}$¶est nulle"), DISPN))
L.append(E(147, "proof of (11.4.7): 'de vérifier que M⊗_A(A_{𝔭_i}/𝔭_i^nA_{𝔭_i}) est un (A_{𝔭_i}/𝔭_i^nA_{𝔭_i})-module plat'",
           DISP, DISPT, "formula",
           F(r"de vérifier que¶\[¶M\otimes_A(A_{\mathfrak p_i}/\mathfrak p_i^nA_{\mathfrak p_i})¶\]¶est un",
             r"de vérifier que¶$M\otimes_A(A_{\mathfrak p_i}/\mathfrak p_i^nA_{\mathfrak p_i})$¶est un"), DISPN))
L.append(E(147, "Remarque (11.4.8): 'pour tout n assez grand, Ass(A/𝔍^n) est contenu dans l'ensemble des 𝔭_i'",
           "'est contenu dans l'ensemble des' italic in the roman remark (enlarged crop)", "no \\emph", "italics",
           F(r"est contenu dans l'ensemble des", r"\emph{est contenu dans l'ensemble des}"),
           "Judged as if the remark body were roman (document-wide remark font)."))
L.append(E(147, "Corollaire (11.4.9): 'Pour que M soit un A-module plat (resp. libre), il faut'",
           "'(resp.' roman, 'libre' italic (enlarged crop)", "italic", "convention",
           F(r"plat (resp. libre), il faut", r"plat \textup{(resp.} libre), il faut"), "", convention=6))
L.append(E(147, "Corollaire (11.4.9): 'soit un (A/𝔍)-module plat (resp. libre) et que'",
           "'(resp.' roman, 'libre' italic (enlarged crop)", "italic", "convention",
           F(r"plat (resp. libre) et que", r"plat \textup{(resp.} libre) et que"), "", convention=6))

# ---------------- page 148 ----------------
L.append(E(148, "Corollaire (11.4.10), end: 'et que pour tout 𝔭∈Ass(A/𝔍), M_𝔭 soit un A_𝔭-module plat'",
           "no comma after 'que' (enlarged crop)", "'et que, pour tout'", "punctuation",
           F(r"et que, pour tout $\mathfrak p\in", r"et que pour tout $\mathfrak p\in")))
L.append(E(148, "proof of (11.4.10): '(Bourbaki, Alg. comm., chap. III, § 2, nº 8, cor. 1 du th. 1)'",
           "n with a superior letter o", "n$^\\circ$ (degree ring)", "symbol",
           F(r"n$^\circ$~8", r"n\textsuperscript{o}~8"), NO))
L.append(E(148, "proof of (11.4.10): '(Bourbaki, Alg. comm., chap. II, § 1, nº 1, prop. 2)'",
           "n with a superior letter o", "n$^\\circ$ (degree ring)", "symbol",
           F(r"n$^\circ$~1", r"n\textsuperscript{o}~1"), NO))
L.append(E(148, "Proposition (11.4.11), l. 5: 'Soit x un point de X, et supposcns vérifiées les conditions suivantes :'",
           "'supposcns': the letter before the final 'ns' is an italic c with the top terminal of the c of 'conditions' in the same line (enlarged crops), not a broken o",
           "supposons: silent correction", "misprint_in_print",
           F(r"et supposons vérifiées", r"et supposcns vérifiées"), "", corrected="supposons"))
L.append(E(148, "Proposition (11.4.11), label (i)", "labels (i), (ii), (iii) upright",
           "label=(\\roman*) inside the italic statement: italic labels", "convention",
           F(r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]"),
           "One edit of the label option covers (i)-(iii) (GLOBAL_ISSUES 16).", convention=6))
L.append(E(148, "Proposition (11.4.11), label (ii)", "upright", "italic", "convention", None,
           "Included in the label-option edit for (i).", convention=6))
L.append(E(148, "Proposition (11.4.11), label (iii)", "upright", "italic", "convention", None,
           "Included in the label-option edit for (i).", convention=6))
L.append(E(148, "Proposition (11.4.11) (ii): 'L'extension k(x) du corps résiduel k de A'",
           "bold italic k in k(x); the k of 'corps résiduel k' is plain (enlarged crop)", "$k(x)$", "convention",
           F(r"L'extension $k(x)$", r"L'extension $\boldsymbol{k}(x)$"), "", convention=1))
L.append(E(148, "Proposition (11.4.11) (ii): 'est primaire (4.3.1)'",
           "reference upright (enlarged crop)", "plain text inside the italic statement: italic", "convention",
           F(r"primaire (4.3.1)", r"primaire \textup{(4.3.1)}"), "", convention=6))
L.append(E(148, "Proposition (11.4.11): 'Dans ces conditions, 𝓕 est f-plat au point x.' after item (iii)",
           "indented new paragraph", "text right after \\end{enumerate} without a blank line: no indent", "other",
           F(r"\end{enumerate}¶Dans ces conditions", r"\end{enumerate}¶¶Dans ces conditions"),
           "Paragraph indent only (GLOBAL_ISSUES 80)."))
L.append(E(148, "proof of (11.4.11): step label 'I) Réduction au cas où A'_α est un anneau local ...'",
           "'I)' roman of normal weight (enlarged crop)", "\\textbf{I)}", "font",
           F(r"\noindent\textbf{I)} \emph{Réduction", r"\noindent I) \emph{Réduction"),
           "As on p. 124 (ega4-11 sets its step labels bold)."))
L.append(E(148, "proof of (11.4.11), I): 'A' est aussi limite inductive de ses sous-anneaux locaux B'_λ=(B_λ)_{𝔫_λ}'",
           "'locaux' italic (enlarged crop)", "roman", "italics",
           F(r"sous-anneaux locaux", r"sous-anneaux \emph{locaux}")))
L.append(E(148, "proof of (11.4.11), I): 'la projection de x'_λ sur Z'_λ étant le point fermé z'_λ de Z'_λ'",
           "'point fermé' italic (enlarged crop)", "roman", "italics",
           F(r"étant le¶point fermé $z'_\lambda$", r"étant le¶\emph{point fermé} $z'_\lambda$")))
L.append(E(148, "proof of (11.4.11), I): 'il existe un point t'∈T' dont les projections dans Z' et X sont z' et x'",
           "the t' of t'∈T' (start of the line) is bold italic, against the light italic t' of 'au point t'.' on the next line (enlarged crops)",
           "$t'\\in T'$, light italic: silent correction", "misprint_in_print",
           F(r"$t'\in T'$", r"$\boldsymbol{t}'\in T'$"),
           "Wrong-fount letter, recorded as a misprint like the bold italic n of EGA II (GLOBAL_ISSUES 29).",
           corrected=r"t'\in T'"))
L.append(E(148, "last line of p. 148: '... est ouvert dans T' (11.1.1) et contient t', donc' | p. 149 'V=U∩T'_1 est ouvert ...'",
           "mid-sentence page break; p. 149 starts flush left", "blank line before \\oldpage[IV-3]{149}", "other",
           F(r"contient $t'$, donc¶¶", r"contient $t'$, donc¶"),
           "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 149 entry that removes the blank line after the marker."))

# ---------------- page 149 ----------------
L.append(E(149, "top of p. 149: 'V=U∩T'_1 est ouvert non vide dans T'_1.' continues the last sentence of p. 148",
           "flush left, no indent", "blank line after \\oldpage[IV-3]{149}", "other",
           F(r"\oldpage[IV-3]{149}¶¶$V=U", r"\oldpage[IV-3]{149}¶$V=U"),
           "GLOBAL_ISSUES 20. Apply together with the last p. 148 entry (blank line before the marker)."))
L.append(E(149, "proof of (11.4.11), I): 'son image z'_0 dans Z'_1 est un point fermé de Z'_1 (10.4.7)'",
           "'fermé' italic (enlarged crop)", "roman", "italics",
           F(r"est un point fermé de $Z'_1$", r"est un point \emph{fermé} de $Z'_1$")))
L.append(E(149, "proof of (11.4.11), I): 'Soient f_1 la restriction de f à X_1, f'_1 : T'_1→Z'_1 la projection canonique'",
           "a comma after X_1 (enlarged crop)", "'et' after X_1", "word",
           F(r"à $X_1$ et $f'_1:T'_1\to Z'_1$", r"à $X_1$, $f'_1:T'_1\to Z'_1$")))
L.append(E(149, "proof of (11.4.11), I): 'f_1^{-1}(y)⊗_{k(y)}k(z'_0)', the subscript k(y)",
           "bold upright k in the subscript (enlarged crop)", "\\otimes_{k(y)}", "convention",
           F(r"\otimes_{k(y)}", r"\otimes_{\mathbf{k}(y)}"), "Bold upright k in subscripts (GLOBAL_ISSUES 48).", convention=1))
L.append(E(149, "same formula: 'k(z'_0)' after the tensor sign",
           "bold italic k (enlarged crop)", "$k(z'_0)$", "convention",
           F(r"k(z'_0)$, et comme", r"\boldsymbol{k}(z'_0)$, et comme"), "Does not overlap the subscript edit.", convention=1))
L.append(E(149, "proof of (11.4.11), I): 'Enfin, k(z'_0) est une extension finie de k (I, 6.4.2)'",
           "bold italic k (enlarged crop)", "$k(z'_0)$", "convention",
           F(r"Enfin, $k(z'_0)$", r"Enfin, $\boldsymbol{k}(z'_0)$"), "", convention=1))
L.append(E(149, "same sentence: 'une extension finie de k (I, 6.4.2)'",
           "'finie' italic (enlarged crop)", "roman", "italics",
           F(r"extension finie de $k$ (\textbf I, 6.4.2)", r"extension \emph{finie} de $k$ (\textbf I, 6.4.2)")))
L.append(E(149, "proof of (11.4.11): step label 'II) Réduction au cas où les A'_α sont en nombre fini ...'",
           "'II)' roman of normal weight", "\\textbf{II)}", "font",
           F(r"\noindent\textbf{II)} \emph{Réduction", r"\noindent II) \emph{Réduction"), "As step I) on p. 148."))
L.append(E(149, "proof of (11.4.11), II): 'l'intersection des 𝔪'^n_α est 0 (0_I, 7.3.5)'",
           "(0_I, 7.3.5): bold 0 with subscript I (enlarged crop)", "(\\textbf I, 7.3.5): a reference to EGA I", "number",
           F(r"$0$ (\textbf I, 7.3.5)", r"$0$ $(\mathbf 0_{\mathrm I},7.3.5)$"),
           "Krull's intersection theorem is in chapter 0_I, 7.3; written like the edition's other 0_I references (p. 145)."))
L.append(E(149, "proof of (11.4.11), II): 'il y a un nombre fini de ces idéaux'",
           "'fini' italic (enlarged crop)", "roman", "italics",
           F(r"un nombre¶fini de ces", r"un nombre¶\emph{fini} de ces")))
L.append(E(149, "proof of (11.4.11), II): 'A''_i=A'_i/𝔪'^{n_i}_i est une A-algèbre finie et un anneau local artinien'",
           "'finie' italic (enlarged crop)", "roman", "italics",
           F(r"est une $A$-algèbre finie et un anneau", r"est une $A$-algèbre \emph{finie} et un anneau")))
L.append(E(149, "proof of (11.4.11): step label 'III) Fin de la démonstration.'",
           "'III)' roman of normal weight", "\\textbf{III)}", "font",
           F(r"\noindent\textbf{III)} \emph{Fin", r"\noindent III) \emph{Fin"), "As step I) on p. 148."))
L.append(E(149, "proof of (11.4.11), III): 'l'image réciproque de x dans X'_i est réduite au seul point x'_i (4.3.2)'",
           "'au seul point' italic (enlarged crop)", "roman", "italics",
           F(r"est réduite au seul point $x'_i$", r"est réduite \emph{au seul point} $x'_i$")))
L.append(E(149, "proof of (11.4.11), III): 'Soient Y' le préschéma somme des Y'_i'",
           "this 'somme' italic; the next one ('somme des X'_i') roman (enlarged crop)", "roman", "italics",
           F(r"le préschéma somme des $Y'_i$", r"le préschéma \emph{somme} des $Y'_i$")))
L.append(E(149, "proof of (11.4.11), III): 'il existe par suite un ouvert U'⊃p^{-1}(x)'",
           "'ouvert' italic (enlarged crop)", "roman", "italics",
           F(r"un¶ouvert $U'\supset", r"un¶\emph{ouvert} $U'\supset")))
L.append(E(149, "proof of (11.4.11), III): 'le morphisme Y'→Y est fini puisque les A'_i'",
           "'fini' italic (enlarged crop)", "roman", "italics",
           F(r"est fini puisque", r"est \emph{fini} puisque")))
L.append(E(149, "proof of (11.4.11), III): 'donc p est un morphisme fini (II, 6.1.5), par suite fermé (II, 6.1.10)'",
           "'fermé' italic; the 'fini' before it roman (enlarged crop)", "roman", "italics",
           F(r"par suite fermé", r"par suite \emph{fermé}")))
L.append(E(149, "proof of (11.4.11), III): 'où M est un B-module, et par hypothèse M'=M⊗_AA' est un A'-module plat'",
           "comma after 'B-module'; none after 'et' or 'hypothèse' (enlarged crop)", "'$B$-module et, par hypothèse,'", "punctuation",
           F(r"$B$-module et, par hypothèse, $M'", r"$B$-module, et par hypothèse $M'")))
L.append(E(149, "proof of (11.4.11), III): 'est un A'-module plat (2.1.2)'",
           "'plat' italic (enlarged crop)", "roman", "italics",
           F(r"$A'$-module plat¶(2.1.2)", r"$A'$-module \emph{plat}¶(2.1.2)")))
L.append(E(149, "Proposition (11.4.12), label (i)", "labels (i), (ii) upright",
           "label=(\\roman*) inside the italic statement: italic labels", "convention",
           F(r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]"),
           "One edit of the label option covers (i) and (ii) (GLOBAL_ISSUES 16).", convention=6))
L.append(E(149, "Proposition (11.4.12), label (ii)", "upright", "italic", "convention", None,
           "Included in the label-option edit for (i).", convention=6))
L.append(E(149, "Proposition (11.4.12) (ii): '𝓕'_α est f'_α-plat en tous les points x'_α∈X'_α'",
           "'tous' roman in the italic statement (emphasis; enlarged crop)", "italic", "convention",
           F(r"plat en tous¶  les points", r"plat en \textup{tous}¶  les points"), "", convention=6))
L.append(E(149, "Proposition (11.4.12) (ii): 'dont les projections respectives dans X et Y' sont x et le point fermé y'_α de Y'_α'",
           "Y' without the index α (clean, no trace; enlarged crop)", "$Y'_\\alpha$: silent correction", "misprint_in_print",
           F(r"$X$ et $Y'_\alpha$ sont $x$", r"$X$ et $Y'$ sont $x$"),
           "The same clause in (11.4.11)(iii), p. 148, has Y'_α.", corrected=r"Y'_\alpha"))
L.append(E(149, "Proposition (11.4.12): 'Alors 𝓕 est f-plat au point x.' after item (ii)",
           "indented new paragraph", "text right after \\end{enumerate} without a blank line: no indent", "other",
           F(r"\end{enumerate}¶Alors", r"\end{enumerate}¶¶Alors"), "Paragraph indent only (GLOBAL_ISSUES 80)."))
L.append(E(149, "end of p. 149 / start of p. 150: proof of (11.4.12) (edit 1 of 2)",
           "p. 149 ends with the statement; the proof text begins at the top of p. 150 ('Par hypothèse, ...')",
           "\\begin{proof} stands before \\oldpage[IV-3]{150}, followed by blank lines: the TeX's proof heading falls on p. 149 as a paragraph of its own",
           "marker", F(r"\begin{proof}¶% IV3_B22_P149_ANCHOR¶", r"% IV3_B22_P149_ANCHOR¶"),
           "Apply together with the page-150 entry below, which opens the proof after the marker. The anchor comment stays where it is.",
           confidence="medium"))
L.append(E(150, "start of page_150.tex: proof of (11.4.12) (edit 2 of 2)",
           "proof text 'Par hypothèse, l'intersection des noyaux ...' at the top of p. 150",
           "the proof environment was opened before the marker", "marker",
           F(r"\oldpage[IV-3]{150}¶¶Par hypothèse", r"\oldpage[IV-3]{150}¶\begin{proof}¶Par hypothèse"),
           "OUTSIDE pages 145-149: 'old' lies in page_150.tex and in the live p. 150 segment (checked unique in both; the applied pp. 150-154 batch left the top of p. 150 unchanged). Second half of the p. 149 marker entry; apply both or neither.",
           confidence="medium"))

OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")

# uniqueness check against the page copies (CRLF normalised to LF) and the current release segments
import re
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")
rt = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-3\]\{(\d+)\}", rt)]
segs = {n: rt[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(rt))] for i, (n, s) in enumerate(cuts)}
bad = 0
for x in L:
    fx = x["fix"]
    if not fx:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(fx["old"])
    m = segs[x["page"]].count(fx["old"])
    if n != 1 or m != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], n, m, repr(fx["old"][:80]))
print("entries", len(L), "bad", bad)
from collections import Counter
c = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in sorted({x["page"] for x in L}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
