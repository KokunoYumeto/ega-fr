"""Build findings_066_070.json for EGA III ch. 0 pp. 66-70 and check every fix.

Strings use the pilcrow as a stand-in for a line break (the TeX contains none)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "findings_066_070.json"
RELEASE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                       r"\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex")
PART = r"0\textsubscript{III}"


def L(s):
    return None if s is None else s.replace("\u00b6", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else dict(old=L(old), new=L(new)))
    if kind == "misprint_in_print":
        d["corrected"] = L(corrected)
    d["note"] = note
    F.append(d)


C6UNWRAP = ("The proposition environment is \\itshape, so this \\emph{...} wrapper sets the statement text upright "
            "in the compiled output; the print sets it italic. Dropping the wrapper restores italic. Apply before "
            "the \\textup fixes listed after it for the same statement.")

# ---------------------------------------------------------------- page 66
add(66, "end of proof of (13.2.1): 'On en déduit y_α=g_{αλ}(y_λ)+u_α(f_{αβ}(x_β)) ;'",
    "formula set inline in the text line", "displayed \\[...\\]", "other", None, "high",
    r"On en déduit¶\[¶y_\alpha=g_{\alpha\lambda}(y_\lambda)¶+u_\alpha(f_{\alpha\beta}(x_\beta))~;¶\]¶mais comme",
    r"On en déduit¶$y_\alpha=g_{\alpha\lambda}(y_\lambda)+u_\alpha(f_{\alpha\beta}(x_\beta))$~;¶mais comme",
    "Inline in the print (line 1 of the page).")
add(66, "end of proof of (13.2.1): 'et finalement y_α=...'",
    "et finalement y_α=g_{αλ}(y_λ+u_λ(x_λ))∈g_{αλ}(B_λ), ce qui achève (inline, no middle term)",
    "display with an extra middle term =g_{αλ}(y_λ)+u_α(f_{αλ}(x_λ))", "extra", None, "high",
    r"et finalement¶\[¶y_\alpha¶=g_{\alpha\lambda}(y_\lambda)+u_\alpha(f_{\alpha\lambda}(x_\lambda))¶=g_{\alpha\lambda}(y_\lambda+u_\lambda(x_\lambda))¶\in g_{\alpha\lambda}(B_\lambda),¶\]¶ce qui achève",
    r"et finalement¶$y_\alpha=g_{\alpha\lambda}(y_\lambda+u_\lambda(x_\lambda))\in g_{\alpha\lambda}(B_\lambda)$,¶ce qui achève",
    "The intermediate term is not printed (checked on an enlarged crop); the fix also sets the formula inline as printed.")
add(66, "(13.2.2), statement, first sentence 'Soit I un ensemble ... dénombrable. Soit'",
    "italic statement text", "\\emph{Soit $I$ ... dénombrable. Soit} inside the \\itshape proposition environment (comes out upright)",
    "convention", 6, "high",
    r"\emph{Soit $I$ un ensemble ordonné filtrant ayant une partie cofinale¶dénombrable. Soit}",
    r"Soit $I$ un ensemble ordonné filtrant ayant une partie cofinale¶dénombrable. Soit",
    C6UNWRAP)
add(66, "(13.2.2), statement: 'cofinale dénombrable. Soit'",
    "'dénombrable.' printed in roman (upright) inside the italic statement; 'Soit' italic",
    "no font change for 'dénombrable.' (whole block in one \\emph; italic once the wrapper is dropped: silent correction)",
    "misprint_in_print", None, "high",
    r"cofinale¶dénombrable. Soit", r"cofinale¶\textup{dénombrable.} Soit",
    "Wrong-font word in the print (enlarged crop: upright 'dénombrable.', italic 'Soit'). Apply after the unwrapping fix above.",
    corrected=r"cofinale¶dénombrable. Soit")
add(66, "(13.2.2), statement: 'une suite exacte ... la condition (ML), la suite'",
    "italic statement text", "\\emph{...} inside the \\itshape environment (comes out upright)", "convention", 6, "high",
    r"\emph{une suite exacte de systèmes projectifs de groupes abéliens ayant¶$I$ pour ensemble d'indices. Si $(A_\alpha)$ satisfait à la condition¶(ML), la suite}",
    r"une suite exacte de systèmes projectifs de groupes abéliens ayant¶$I$ pour ensemble d'indices. Si $(A_\alpha)$ satisfait à la condition¶(ML), la suite",
    C6UNWRAP)
add(66, "(13.2.2), statement: 'la condition (ML), la suite'", "(ML) upright in the italic statement",
    "(ML) italic once the statement is italic", "convention", 6, "high",
    r"condition¶(ML), la suite", r"condition¶\textup{(ML)}, la suite",
    "Apply after the unwrapping fix above.")
add(66, "(13.2.2), statement: 'est exacte.'", "italic", "\\emph{est exacte.} (upright in the \\itshape environment)",
    "convention", 6, "high", r"\emph{est exacte.}", r"est exacte.", C6UNWRAP)
add(66, "proof of (13.2.2): 'l'homomorphisme v=lim v_α : lim B_α→lim C_α est surjectif'",
    "formula set inline", "displayed \\[...\\]", "other", None, "high",
    r"l'homomorphisme¶\[¶v=\varprojlim v_\alpha:\varprojlim B_\alpha\longrightarrow¶\varprojlim C_\alpha¶\]¶est surjectif.",
    r"l'homomorphisme¶$v=\varprojlim v_\alpha:\varprojlim B_\alpha\to\varprojlim C_\alpha$¶est surjectif.",
    "Inline in the print.")
add(66, "proof of (13.2.2): 'on a y'_β—y_β=x_β∈A_β'", "long dash (the print's set-difference dash) for the minus",
    "y'_\\beta-y_\\beta (minus sign)", "convention", 7, "high",
    r"$y'_\beta-y_\beta=x_\beta\in A_\beta$", r"$y'_\beta\setmin y_\beta=x_\beta\in A_\beta$",
    "Subtraction, not set difference (GLOBAL_ISSUES item 23); \\setmin still typesets '-', so this changes nothing until the convention-7 decision.")
add(66, "(13.2.3), statement, first part 'Les hypothèses sur I ... canonique fonctoriel'",
    "italic statement text", "\\emph{...} inside the \\itshape environment (comes out upright)", "convention", 6, "high",
    r"\emph{Les hypothèses sur $I$ étant celles de¶(\hyperref[0.13.2.2-fr]{13.2.2}), soit¶$(K_\alpha^\bullet)_{\alpha\in I}$ un système projectif de complexes de¶groupes abéliens¶$K_\alpha^\bullet=(K_\alpha^n)_{n\in\mathbb Z}$ dont l'opérateur de¶dérivation est de degré $+1$. Pour chaque $n$, il existe un homomorphisme¶canonique fonctoriel}",
    r"Les hypothèses sur $I$ étant celles de¶(\hyperref[0.13.2.2-fr]{13.2.2}), soit¶$(K_\alpha^\bullet)_{\alpha\in I}$ un système projectif de complexes de¶groupes abéliens¶$K_\alpha^\bullet=(K_\alpha^n)_{n\in\mathbb Z}$ dont l'opérateur de¶dérivation est de degré $+1$. Pour chaque $n$, il existe un homomorphisme¶canonique fonctoriel",
    C6UNWRAP)
add(66, "(13.2.3), statement: 'étant celles de (13.2.2), soit'", "reference (13.2.2) upright in the italic statement",
    "reference italic once the statement is italic", "convention", 6, "high",
    r"(\hyperref[0.13.2.2-fr]{13.2.2}), soit", r"\textup{(\hyperref[0.13.2.2-fr]{13.2.2})}, soit",
    "Apply after the unwrapping fix above.")
add(66, "(13.2.3), after (13.2.3.1): 'Si, pour tout degré n, ...'",
    "new indented paragraph", "continues the paragraph after \\end{equation} (no indent)", "other", None, "medium",
    r"\end{equation}¶", r"\end{equation}¶¶", "Paragraph break of the print.")
add(66, "(13.2.3), statement, second part 'Si, pour tout degré n, ... est bijectif.'",
    "italic statement text", "\\emph{...} inside the \\itshape environment (comes out upright)", "convention", 6, "high",
    r"\emph{Si, pour tout degré $n$, le système projectif de groupes abéliens¶$(K_\alpha^n)_{\alpha\in I}$ vérifie (ML), alors tous les homomorphismes¶$h_n$ sont surjectifs. Si en outre, pour un degré $n$, le système¶projectif $(H^{n-1}(K_\alpha^\bullet))_{\alpha\in I}$ vérifie (ML),¶l'homomorphisme $h_n$ est bijectif.}",
    r"Si, pour tout degré $n$, le système projectif de groupes abéliens¶$(K_\alpha^n)_{\alpha\in I}$ vérifie (ML), alors tous les homomorphismes¶$h_n$ sont surjectifs. Si en outre, pour un degré $n$, le système¶projectif $(H^{n-1}(K_\alpha^\bullet))_{\alpha\in I}$ vérifie (ML),¶l'homomorphisme $h_n$ est bijectif.",
    C6UNWRAP)
add(66, "(13.2.3), statement: 'vérifie (ML), alors'", "(ML) upright", "italic once the statement is italic",
    "convention", 6, "high", r"vérifie (ML), alors", r"vérifie \textup{(ML)}, alors", "Apply after the unwrapping fix above.")
add(66, "(13.2.3), statement: 'vérifie (ML), l'homomorphisme'", "(ML) upright", "italic once the statement is italic",
    "convention", 6, "high", r"vérifie (ML),¶l'homomorphisme", r"vérifie \textup{(ML)},¶l'homomorphisme",
    "Apply after the unwrapping fix above.")
add(66, "proof of (13.2.3), diagram", "baseline dots ... at both ends of both rows", "\\cdots (centred, 4 times)",
    "symbol", None, "high",
    r"\cdots\ar[r]&K^{n-1}\ar[r]\ar[d]&K^n\ar[r]\ar[d]¶&K^{n+1}\ar[r]\ar[d]&\cdots\\¶\cdots\ar[r]&K_\alpha^{n-1}\ar[r]&K_\alpha^n\ar[r]¶&K_\alpha^{n+1}\ar[r]&\cdots",
    r"\ldots\ar[r]&K^{n-1}\ar[r]\ar[d]&K^n\ar[r]\ar[d]¶&K^{n+1}\ar[r]\ar[d]&\ldots\\¶\ldots\ar[r]&K_\alpha^{n-1}\ar[r]&K_\alpha^n\ar[r]¶&K_\alpha^{n+1}\ar[r]&\ldots",
    "Enlarged crop: the dots sit on the baseline, below the arrows.")

# ---------------------------------------------------------------- page 67
add(67, "proof of (13.2.3), display (**_n)", "0→Z^{n-1}(K_α)→K_α^{n-1}→B^n(K_α)→0 (no full stop)",
    "…\\longrightarrow0. (full stop)", "punctuation", None, "high",
    r"\mathrm B^n(K_\alpha^\bullet)\longrightarrow0.", r"\mathrm B^n(K_\alpha^\bullet)\longrightarrow0",
    "Enlarged crop: nothing after the final 0.")
add(67, "proof of (13.2.3): 'L'hypothèse et la prop. (13.2.1, (i))'", "new indented paragraph after the displays",
    "continues the paragraph", "other", None, "medium",
    r"\]¶L'hypothèse et la prop.", r"\]¶¶L'hypothèse et la prop.", "Paragraph break of the print.")
add(67, "proof of (13.2.3): 'Or il est clair que lim B^n(K_α) s'identifie'", "inline lim with no index",
    "\\varprojlim_\\alpha", "formula", None, "high",
    r"$\varprojlim_\alpha\mathrm B^n(K_\alpha^\bullet)$ s'identifie",
    r"$\varprojlim\mathrm B^n(K_\alpha^\bullet)$ s'identifie",
    "The print's inline lim on this page carries no α (the displays do).")
add(67, "proof of (13.2.3): 'par suite, h_n est surjective.'", "surjective", "surjectif", "word", None, "high",
    r"par suite, $h_n$ est surjectif.", r"par suite, $h_n$ est surjective.",
    "The print has the feminine form here and in 'h_n est injective' below (agreement with an implied 'application'); the TeX normalises it.")
add(67, "proof of (13.2.3): 'et que lim Z^n(K_α) s'identifie'", "inline lim with no index", "\\varprojlim_\\alpha",
    "formula", None, "high",
    r"$\varprojlim_\alpha\mathrm Z^n(K_\alpha^\bullet)$ s'identifie",
    r"$\varprojlim\mathrm Z^n(K_\alpha^\bullet)$ s'identifie", "")
add(67, "proof of (13.2.3): 'comme lim B^n(K_α)⊃B^n(K)'", "inline lim with no index", "\\varprojlim_\\alpha",
    "formula", None, "high",
    r"$\varprojlim_\alpha\mathrm B^n(K_\alpha^\bullet)¶\supset", r"$\varprojlim\mathrm B^n(K_\alpha^\bullet)¶\supset", "")
add(67, "proof of (13.2.3): 'l'injection lim B^n(K_α)→K^n'", "inline lim with no index", "\\varprojlim_\\alpha",
    "formula", None, "high",
    r"$\varprojlim_\alpha\mathrm B^n(K_\alpha^\bullet)\to K^n$", r"$\varprojlim\mathrm B^n(K_\alpha^\bullet)\to K^n$", "")
add(67, "proof of (13.2.3): 'entraîne lim B^n(K_α)=B^n(K)'", "inline lim with no index", "\\varprojlim_\\alpha",
    "formula", None, "high",
    r"$\varprojlim_\alpha\mathrm B^n(K_\alpha^\bullet)¶=\mathrm B^n(K^\bullet)$",
    r"$\varprojlim\mathrm B^n(K_\alpha^\bullet)¶=\mathrm B^n(K^\bullet)$", "")
add(67, "proof of (13.2.3): 'donc h_n est injective. C.Q.F.D.'", "injective", "injectif", "word", None, "high",
    r"donc $h_n$ est injectif.", r"donc $h_n$ est injective.", "See 'surjective' above.")
add(67, "(13.2.4) heading", "Remarques (13.2.4). — (i) …", "\\emph{Remarques} (13.2.4). (no dash)",
    "punctuation", None, "medium",
    r"\emph{Remarques} (13.2.4).", r"\emph{Remarques} (13.2.4). ---",
    "Hand-made heading inside env; env also prints a bold (13.2.4) before it, so the number appears twice (document-wide heading issue).")
add(67, "(13.2.4) (i), item label", "(i) upright", "\\item[\\emph{(i)}] (italic: env body is upright)", "italics",
    None, "high", r"\item[\emph{(i)}]¶Le raisonnement", r"\item[(i)]¶Le raisonnement", "")
add(67, "(13.2.4) (i), condition label (ML')", "(ML′) in ordinary roman, with a prime",
    "\\textbf{(ML')} (bold, text apostrophe)", "font", None, "high",
    r"\item[\textbf{(ML')}]", r"\item[(ML$'$)]",
    "Stroke widths measured on the scan equal those of (ML) in running text: not bold. The mark after L is a prime.")
add(67, "(13.2.4) (ii), item label", "(ii) upright", "\\item[\\emph{(ii)}] (italic)", "italics", None, "high",
    r"\item[\emph{(ii)}]¶Il est possible", r"\item[(ii)]¶Il est possible", "")
add(67, "(13.2.4) (ii): 'les foncteurs dérivés à droite lim^{(n)} du foncteur lim'",
    "both lim printed with a RIGHT arrow underneath (inductive limit)",
    "$\\varinjlim^{(n)}$ du foncteur $\\varinjlim$ (keeps the printed reading)", "misprint_in_print", None, "high",
    None, None,
    "The right derived functors meant are those of the projective limit (Roos [28], 'Sur les foncteurs dérivés de lim←'); lim→ of abelian groups over a filtered set is exact. Diplomatic text keeps the print.",
    corrected=r"$\varprojlim^{(n)}$ du foncteur $\varprojlim$", nofix=True)
add(67, "end of the page segment: heading 13.3 and the opening of Proposition (13.3.1)",
    "13.3 heading and Proposition (13.3.1) begin at the top of printed p. 68",
    "placed before \\oldpage[0\\textsubscript{III}]{68}", "marker", None, "high",
    r"\subsection{Application : cohomologie d'une limite projective de faisceaux}¶\label{subsection:0.13.3-fr}¶¶\begin{proposition}[13.3.1]¶\label{0.13.3.1-fr}¶",
    "",
    "Moves the text to page 68; apply together with the p. 68 marker finding (insert after \\oldpage{68}).")

# ---------------------------------------------------------------- page 68
add(68, "page start: heading 13.3 and Proposition (13.3.1)", "printed p. 68 begins with '13.3. Application : ...'",
    "the heading is in the p. 67 segment", "marker", None, "high",
    r"\oldpage[0\textsubscript{III}]{68}¶",
    r"\oldpage[0\textsubscript{III}]{68}¶\subsection{Application : cohomologie d'une limite projective de faisceaux}¶\label{subsection:0.13.3-fr}¶¶\begin{proposition}[13.3.1]¶\label{0.13.3.1-fr}¶",
    "Apply together with the p. 67 marker finding (which removes the same lines there).")
add(68, "(13.3.1), statement opening 'Soient X ... conditions suivantes :'", "italic statement text",
    "\\emph{...} inside the \\itshape environment (comes out upright)", "convention", 6, "high",
    r"\emph{Soient $X$ un espace topologique,¶$(\mathcal F_k)_{k\in\mathbb N}$ un système projectif de faisceaux de¶groupes abéliens sur $X$, et soit¶$\mathcal F=\varprojlim_k\mathcal F_k$. On suppose vérifiées les conditions¶suivantes :}",
    r"Soient $X$ un espace topologique,¶$(\mathcal F_k)_{k\in\mathbb N}$ un système projectif de faisceaux de¶groupes abéliens sur $X$, et soit¶$\mathcal F=\varprojlim_k\mathcal F_k$. On suppose vérifiées les conditions¶suivantes :",
    C6UNWRAP)
add(68, "(13.3.1), statement: 'et soit F=lim F_k'", "lim with no index", "\\varprojlim_k", "formula", None, "high",
    r"$\mathcal F=\varprojlim_k\mathcal F_k$", r"$\mathcal F=\varprojlim\mathcal F_k$",
    "Enlarged crop: no k under the arrow. Apply after the unwrapping fix above.")
add(68, "(13.3.1) (i)", "italic statement text", "\\emph{...} (upright in the \\itshape environment)", "convention", 6,
    "high",
    r"\emph{Il existe une base $\mathfrak B$ de la topologie de $X$ telle que,¶pour tout $U\in\mathfrak B$ et tout $i\geq0$, le système projectif¶$(H^i(U,\mathcal F_k))_{k\in\mathbb N}$ vérifie (ML).}",
    r"Il existe une base $\mathfrak B$ de la topologie de $X$ telle que,¶pour tout $U\in\mathfrak B$ et tout $i\geq0$, le système projectif¶$(H^i(U,\mathcal F_k))_{k\in\mathbb N}$ vérifie (ML).",
    C6UNWRAP)
add(68, "(13.3.1) (i): 'vérifie (ML).'", "(ML) upright", "italic once the statement is italic", "convention", 6, "high",
    r"vérifie (ML).", r"vérifie \textup{(ML)}.", "Apply after the unwrapping fix above.")
add(68, "(13.3.1) (ii), first part", "italic statement text", "\\emph{...} (upright in the \\itshape environment)",
    "convention", 6, "high",
    r"\emph{Pour tout $x\in X$ et tout $i>0$, on a}", r"Pour tout $x\in X$ et tout $i>0$, on a", C6UNWRAP)
add(68, "(13.3.1) (ii): 'on a lim_U(lim_k H^i(U,F_k))=0 lorsque'", "formula set inline in the line",
    "displayed \\[...\\]", "other", None, "high",
    r"\[¶\varinjlim_U\bigl(\varprojlim_k H^i(U,\mathcal F_k)\bigr)=0¶\]",
    r"$\varinjlim_U\bigl(\varprojlim_k H^i(U,\mathcal F_k)\bigr)=0$", "Inline in the print.")
add(68, "(13.3.1) (ii), second part", "italic statement text", "\\emph{...} (upright in the \\itshape environment)",
    "convention", 6, "high",
    r"\emph{lorsque $U$ parcourt l'ensemble des voisinages de $x$ appartenant à¶$\mathfrak B$.}",
    r"lorsque $U$ parcourt l'ensemble des voisinages de $x$ appartenant à¶$\mathfrak B$.", C6UNWRAP)
add(68, "(13.3.1) (iii)", "italic statement text", "\\emph{...} (upright in the \\itshape environment)",
    "convention", 6, "high",
    r"\emph{Les homomorphismes¶$u_{hk}:\mathcal F_k\to\mathcal F_h$ $(h\leq k)$ définissant le système¶projectif $(\mathcal F_k)$ sont surjectifs.}",
    r"Les homomorphismes¶$u_{hk}:\mathcal F_k\to\mathcal F_h$ $(h\leq k)$ définissant le système¶projectif $(\mathcal F_k)$ sont surjectifs.",
    C6UNWRAP)
add(68, "(13.3.1): 'Dans ces conditions, ...'", "new indented paragraph after (iii)",
    "continues after \\end{enumerate} (no indent)", "other", None, "medium",
    r"\end{enumerate}¶", r"\end{enumerate}¶¶", "Paragraph break of the print.")
add(68, "(13.3.1): 'Dans ces conditions, ... canonique'", "italic statement text",
    "\\emph{...} (upright in the \\itshape environment)", "convention", 6, "high",
    r"\emph{Dans ces conditions, pour tout $i>0$, l'homomorphisme canonique}",
    r"Dans ces conditions, pour tout $i>0$, l'homomorphisme canonique", C6UNWRAP)
add(68, "(13.3.1): 'est surjectif; ... h_i est bijectif.'", "italic statement text",
    "\\emph{...} (upright in the \\itshape environment)", "convention", 6, "high",
    r"\emph{est surjectif~; si en outre, pour une valeur de $i$, le système¶projectif $(H^{i-1}(X,\mathcal F_k))_{k\in\mathbb N}$ vérifie (ML), $h_i$¶est bijectif.}",
    r"est surjectif~; si en outre, pour une valeur de $i$, le système¶projectif $(H^{i-1}(X,\mathcal F_k))_{k\in\mathbb N}$ vérifie (ML), $h_i$¶est bijectif.",
    C6UNWRAP)
add(68, "(13.3.1): 'vérifie (ML), h_i'", "(ML) upright", "italic once the statement is italic", "convention", 6,
    "high", r"vérifie (ML), $h_i$", r"vérifie \textup{(ML)}, $h_i$", "Apply after the unwrapping fix above.")
add(68, "proof of (13.3.1) a): 'les F_k sont flasques'", "flasques in italics", "upright", "italics", None, "high",
    r"sont flasques¶ainsi", r"sont \emph{flasques}¶ainsi", "")
add(68, "proof of (13.3.1) a): 'ainsi que les noyaux N_hk'", "noyaux in italics", "upright", "italics", None, "high",
    r"les noyaux $\mathcal N_{hk}$", r"les \emph{noyaux} $\mathcal N_{hk}$", "")
add(68, "proof of (13.3.1) a): 'pour tout ouvert U de X'", "first 'tout' in italics", "upright", "italics", None,
    "high", r"pour tout ouvert¶$U$ de $X$", r"pour \emph{tout} ouvert¶$U$ de $X$", "Enlarged crop.")
add(68, "proof of (13.3.1) a): 'on a H^i(𝔘,F)=0 pour i>0'", "H with no check accent (cohomology of the covering)",
    "\\check H^i(\\mathfrak U,...)", "formula", None, "high",
    r"on a $\check H^i(\mathfrak U,\mathcal F)=0$", r"on a $H^i(\mathfrak U,\mathcal F)=0$",
    "Enlarged crop: no háček; the print reserves Ȟ for Ȟ^i(U,F) two lines below (kept).")
add(68, "proof of (13.3.1) a): 'on a H^i(𝔘,F_k)=0 pour i>0'", "no check accent", "\\check H", "formula", None, "high",
    r"on a $\check H^i(\mathfrak U,\mathcal F_k)=0$", r"on a $H^i(\mathfrak U,\mathcal F_k)=0$", "")
add(68, "proof of (13.3.1) a): 'le complexe C^•(𝔘,F_k) des cochaînes'", "C with no check accent", "\\check C",
    "formula", None, "high",
    r"$\check C^\bullet(\mathfrak U,\mathcal F_k)$ des", r"$C^\bullet(\mathfrak U,\mathcal F_k)$ des", "")
add(68, "proof of (13.3.1) a): 'les applications C^•(𝔘,F_k)→C^•(𝔘,F_h)'", "no check accents", "\\check C twice",
    "formula", None, "high",
    r"$\check C^\bullet(\mathfrak U,\mathcal F_k)\to¶\check C^\bullet(\mathfrak U,\mathcal F_h)$",
    r"$C^\bullet(\mathfrak U,\mathcal F_k)\to¶C^\bullet(\mathfrak U,\mathcal F_h)$", "")
add(68, "proof of (13.3.1) a): '(h≤k) sont surjectives.'", "surjectives in italics", "upright", "italics", None,
    "high", r"$(h\leq k)$ sont surjectives.¶Il suffit", r"$(h\leq k)$ sont \emph{surjectives}.¶Il suffit", "")
add(68, "proof of (13.3.1) a): 'mais la suite 0→N_hk→F_k→F_h→0 étant exacte'", "formula set inline",
    "displayed \\[...\\]", "other", None, "high",
    r"suite¶\[¶0\longrightarrow\mathcal N_{hk}\longrightarrow\mathcal F_k¶\longrightarrow\mathcal F_h\longrightarrow0¶\]¶étant exacte",
    r"suite¶$0\to\mathcal N_{hk}\to\mathcal F_k\to\mathcal F_h\to0$¶étant exacte", "Inline in the print.")
add(68, "proof of (13.3.1) a): 'Le système projectif (C^•(𝔘,F_k))_{k∈N}'", "no check accent", "\\check C",
    "formula", None, "high",
    r"$(\check C^\bullet(\mathfrak U,\mathcal F_k))_{k\in\mathbb N}$",
    r"$(C^\bullet(\mathfrak U,\mathcal F_k))_{k\in\mathbb N}$", "")
add(68, "proof of (13.3.1) a): 'de même de (H^i(𝔘,F_k))_{k∈N}'", "no check accent", "\\check H", "formula", None,
    "high", r"$(\check H^i(\mathfrak U,\mathcal F_k))_{k\in\mathbb N}$",
    r"$(H^i(\mathfrak U,\mathcal F_k))_{k\in\mathbb N}$", "")
add(68, "proof of (13.3.1) a): 'et comme H^0(𝔘,F_k)=Γ(U,F_k)'", "no check accent", "\\check H^0", "formula", None,
    "high", r"$\check H^0(\mathfrak U,\mathcal F_k)", r"$H^0(\mathfrak U,\mathcal F_k)", "")
add(68, "proof of (13.3.1) a), last formula 'H^i(𝔘,F)=lim_k H^i(𝔘,F_k)=0 pour tout i>0.'",
    "no check accents; formula at the start of a text line (inline)",
    "\\check H twice, displayed with \\quad\\hbox{pour tout }i>0", "formula", None, "high",
    r"qui montre que¶\[¶\check H^i(\mathfrak U,\mathcal F)¶=\varprojlim_k\check H^i(\mathfrak U,\mathcal F_k)=0¶\quad\hbox{pour tout }i>0.¶\]",
    r"qui montre que¶$H^i(\mathfrak U,\mathcal F)=\varprojlim_k H^i(\mathfrak U,\mathcal F_k)=0$ pour tout $i>0$.",
    "Checks removed and the formula set inline as printed (it starts flush left in the text).")
add(68, "proof of (13.3.1) b): 'la résolution canonique'", "résolution canonique in italics", "upright",
    "italics", None, "high",
    r"la résolution canonique¶$\mathcal C^\bullet(X,\mathcal F_k)",
    r"la \emph{résolution canonique}¶$\mathcal C^\bullet(X,\mathcal F_k)", "")
add(68, "end of page: 'mon-' (hyphenated 'mon-|trons')",
    "printed p. 68 ends with 'mon-'; p. 69 begins 'trons qu'il satisfait aux conditions de a).'",
    "'qu'il satisfait aux conditions de \\emph{a)}.' stands before \\oldpage{69}", "marker", None, "high",
    r"montrons qu'il satisfait aux conditions de¶\emph{a)}.¶", r"montrons¶",
    "Keeps the split word 'montrons' on p. 68 and moves the rest to p. 69; apply together with the p. 69 marker finding.")

# ---------------------------------------------------------------- page 69
add(69, "page start", "printed p. 69 begins 'trons qu'il satisfait aux conditions de a). En effet,'",
    "begins 'En effet,'", "marker", None, "high",
    r"\oldpage[0\textsubscript{III}]{69}¶En effet,",
    r"\oldpage[0\textsubscript{III}]{69}¶qu'il satisfait aux conditions de¶\emph{a)}. En effet,",
    "Apply together with the p. 68 marker finding (which removes the same words there).")
add(69, "proof of (13.3.1) b): 'la suite 0→N_hk→F_k→F_h→0 est exacte d'après (iii)'", "formula set inline",
    "displayed \\[...\\]", "other", None, "high",
    r"la¶suite¶\[¶0\longrightarrow\mathcal N_{hk}\longrightarrow\mathcal F_k¶\longrightarrow\mathcal F_h\longrightarrow0¶\]¶est exacte",
    r"la¶suite¶$0\to\mathcal N_{hk}\to\mathcal F_k\to\mathcal F_h\to0$¶est exacte", "Inline in the print.")
add(69, "proof of (13.3.1) b): 'le foncteur 𝒜⇝𝒞^i(X,𝒜) est exact'", "wavy arrow", "\\mapsto", "symbol", None,
    "high", r"$\mathcal A\mapsto\mathcal C^i(X,\mathcal A)$", r"$\mathcal A\leadsto\mathcal C^i(X,\mathcal A)$",
    "Enlarged crop.")
add(69, "proof of (13.3.1) b): 'est une résolution du faisceau F'", "résolution in italics", "upright", "italics",
    None, "high", r"une¶résolution du faisceau", r"une¶\emph{résolution} du faisceau", "")
add(69, "proof of (13.3.1) b): 'comme H^j(X,𝒢^•)=0 pour j>0'", "𝒢 with superscript bullet",
    "\\mathcal G^i", "formula", None, "high",
    r"$H^j(X,\mathcal G^i)=0$ pour $j>0$, la", r"$H^j(X,\mathcal G^\bullet)=0$ pour $j>0$, la", "Enlarged crop.")
add(69, "proof of (13.3.1) b), display '0→F_k→𝒞^0(X,F_k)→𝒞^1(X,F_k)→...'", "baseline dots", "\\cdots",
    "symbol", None, "high",
    r"\longrightarrow\mathcal C^1(X,\mathcal F_k)\longrightarrow\cdots",
    r"\longrightarrow\mathcal C^1(X,\mathcal F_k)\longrightarrow\ldots", "")
add(69, "proof of (13.3.1) b), display '0→F→𝒢^0→𝒢^1→...'", "baseline dots, no full stop", "\\cdots.",
    "symbol", None, "high",
    r"\longrightarrow\mathcal G^1\longrightarrow\cdots.", r"\longrightarrow\mathcal G^1\longrightarrow\ldots",
    "Also removes the full stop after the dots (three dots only in the print).")
add(69, "proof of (13.3.1) b): 'Pour prouver notre assertion'", "new indented paragraph", "continues the paragraph",
    "other", None, "medium", r"\]¶Pour prouver notre assertion", r"\]¶¶Pour prouver notre assertion",
    "Paragraph break of the print.")
add(69, "proof of (13.3.1) b): 'le préfaisceau U⇝H^i(Γ(U,𝒢^•))'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$U\mapsto H^i(\Gamma(U,\mathcal G^\bullet))$", r"$U\leadsto H^i(\Gamma(U,\mathcal G^\bullet))$",
    "Enlarged crop.")
add(69, "proof of (13.3.1) b): '(Γ(U,𝒞^•(X,F_k)))_{k∈N} (0_I, 3.2.6)'", "formula set inline",
    "displayed \\[...\\]", "other", None, "high",
    r"abéliens¶\[¶(\Gamma(U,\mathcal C^\bullet(X,\mathcal F_k)))_{k\in\mathbb N}¶\]¶",
    r"abéliens¶$(\Gamma(U,\mathcal C^\bullet(X,\mathcal F_k)))_{k\in\mathbb N}$¶", "Inline in the print.")
add(69, "proof of (13.3.1) b): '(0_I, 3.2.6). On a vu'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 3.2.6). On a vu", r"(\textbf{0}\textsubscript{I}, 3.2.6). On a vu", "")
add(69, "proof of (13.3.1) b): '(h≤k) sont surjectives; d'autre part'", "surjectives in italics", "upright",
    "italics", None, "high", r"sont surjectives~;¶d'autre part", r"sont \emph{surjectives}~;¶d'autre part", "")
add(69, "proof of (13.3.1) b): 'et on a donc H^i(Γ(U,𝒢^•))=lim_k H^i(U,F_k) pour tout i≥0. L'hypothèse (ii)'",
    "formula inline at the start of a text line, sentence continues on the same line", "displayed \\[...\\]",
    "other", None, "high",
    r"donc¶\[¶H^i(\Gamma(U,\mathcal G^\bullet))¶=\varprojlim_k H^i(U,\mathcal F_k)¶\quad\hbox{pour tout }i\geq0.¶\]¶L'hypothèse (ii)",
    r"donc¶$H^i(\Gamma(U,\mathcal G^\bullet))=\varprojlim_k H^i(U,\mathcal F_k)$ pour tout $i\geq0$. L'hypothèse (ii)",
    "Inline in the print.")
add(69, "proof of (13.3.1): 'On a alors pour tout i≥0, H^i(X,F)=H^i(Γ(X,𝒢^•)) et'",
    "first equation inline, followed by 'et'; only Γ(X,𝒢^•)=lim_k Γ(X,𝒞^•(X,F_k)). is displayed",
    "both equations in one display joined by \\quad\\hbox{et}\\quad", "other", None, "high",
    r"On a alors pour tout $i\geq0$,¶\[¶H^i(X,\mathcal F)=H^i(\Gamma(X,\mathcal G^\bullet))¶\quad\hbox{et}\quad¶\Gamma(X,\mathcal G^\bullet)",
    r"On a alors pour tout $i\geq0$,¶$H^i(X,\mathcal F)=H^i(\Gamma(X,\mathcal G^\bullet))$ et¶\[¶\Gamma(X,\mathcal G^\bullet)",
    "")
add(69, "(13.3.2) (i): 'sans hypothèse (0_I, 3.2.6).'", "bold 0", "plain 0", "convention", 2, "high",
    r"sans hypothèse¶(0\textsubscript{I}, 3.2.6).", r"sans hypothèse¶(\textbf{0}\textsubscript{I}, 3.2.6).", "")
add(69, "(13.3.2) heading", "Remarques (13.3.2). — (i) …", "\\emph{Remarques} (13.3.2). (no dash)",
    "punctuation", None, "medium",
    r"\emph{Remarques} (13.3.2).", r"\emph{Remarques} (13.3.2). ---",
    "Hand-made heading inside env; env also prints a bold (13.3.2) before it (number twice; document-wide).")
add(69, "(13.3.2) (i), item label", "(i) upright", "\\item[\\emph{(i)}] (italic)", "italics", None, "high",
    r"\item[\emph{(i)}]¶L'énoncé", r"\item[(i)]¶L'énoncé", "")
add(69, "(13.3.2) (ii), item label", "(ii) upright", "\\item[\\emph{(ii)}] (italic)", "italics", None, "high",
    r"\item[\emph{(ii)}]¶Les conditions", r"\item[(ii)]¶Les conditions", "")
add(69, "(13.3.2) (ii): 'sont surjectives. Ce sera'", "surjectives in italics", "upright", "italics", None, "high",
    r"sont surjectives. Ce sera", r"sont \emph{surjectives}. Ce sera", "")
add(69, "(13.4.1): 'dans une catégorie abélienne C ;'", "bold italic C", "plain $C$", "font", None, "high",
    r"catégorie abélienne $C$~; nous dirons", r"catégorie abélienne $\boldsymbol{C}$~; nous dirons",
    "Category letter, edition point for this file.")
add(69, "(13.4.1): 'Nous définirons sur chaque A_k'", "new indented paragraph", "continues the paragraph",
    "other", None, "medium", r"pour $k<k_0$. Nous définirons", r"pour $k<k_0$.¶¶Nous définirons",
    "Paragraph break of the print.")
add(69, "(13.4.1.1)", "brace before two full equations 'F^p(A_k)=Ker(A_k→A_{p-1}) pour p≤k+1' / 'F^p(A_k)=0 pour p≥k+1', no comma, no full stop",
    "F^p(A_k)= factored before the brace; comma after the first line, full stop after the second", "formula",
    None, "high",
    r"\mathrm F^p(A_k)=¶\begin{cases}¶\operatorname{Ker}(A_k\longrightarrow A_{p-1})&\text{pour }p\leq k+1,\\¶0&\text{pour }p\geq k+1.¶\end{cases}",
    r"\begin{cases}¶\mathrm F^p(A_k)=\operatorname{Ker}(A_k\longrightarrow A_{p-1})&\text{pour }p\leq k+1\\¶\mathrm F^p(A_k)=0&\text{pour }p\geq k+1¶\end{cases}",
    "Enlarged crop.")

# ---------------------------------------------------------------- page 70
add(70, "(13.4.1): 'Les définitions précédentes montrent en outre'", "new indented paragraph",
    "continues after \\end{equation}", "other", None, "medium",
    r"\end{equation}¶Les définitions précédentes", r"\end{equation}¶¶Les définitions précédentes",
    "Paragraph break of the print.")
add(70, "(13.4.3), statement opening 'Soit A=(A_k) ... équivalentes :'", "italic statement text",
    "\\emph{...} inside the \\itshape environment (comes out upright)", "convention", 6, "high",
    r"\emph{Soit $\mathbf A=(A_k)_{k\in\mathbb Z}$ un système projectif limité¶inférieurement dans une catégorie abélienne $C$. Les deux conditions¶suivantes sont équivalentes :}",
    r"Soit $\mathbf A=(A_k)_{k\in\mathbb Z}$ un système projectif limité¶inférieurement dans une catégorie abélienne $C$. Les deux conditions¶suivantes sont équivalentes :",
    C6UNWRAP)
add(70, "(13.4.3): 'dans une catégorie abélienne C.'", "bold italic C", "plain $C$", "font", None, "high",
    r"abélienne $C$. Les deux", r"abélienne $\boldsymbol{C}$. Les deux",
    "Category letter. Apply after the unwrapping fix above.")
add(70, "(13.4.3) a)", "italic statement text", "\\emph{...} (upright in the \\itshape environment)", "convention",
    6, "high", r"\emph{$\mathbf A$ vérifie la condition (ML).}", r"$\mathbf A$ vérifie la condition (ML).",
    C6UNWRAP)
add(70, "(13.4.3) a): 'la condition (ML).'", "(ML) upright", "italic once the statement is italic", "convention", 6,
    "high", r"la condition (ML).", r"la condition \textup{(ML)}.", "Apply after the unwrapping fix above.")
add(70, "(13.4.3) b)", "italic statement text", "\\emph{...} (upright in the \\itshape environment)", "convention",
    6, "high",
    r"\emph{Pour tout $p\in\mathbb Z$, le système projectif¶$(\operatorname{gr}^p(A_k))_{k\in\mathbb Z}$ est essentiellement constant.}",
    r"Pour tout $p\in\mathbb Z$, le système projectif¶$(\operatorname{gr}^p(A_k))_{k\in\mathbb Z}$ est essentiellement constant.",
    C6UNWRAP)
add(70, "(13.4.3): 'En outre, lorsque ...'", "new indented paragraph after b)",
    "continues after \\end{enumerate}", "other", None, "medium",
    r"\end{enumerate}¶", r"\end{enumerate}¶¶", "Paragraph break of the print.")
add(70, "(13.4.3): 'En outre, ... un isomorphisme canonique'", "italic statement text",
    "\\emph{...} (upright in the \\itshape environment)", "convention", 6, "high",
    r"\emph{En outre, lorsque ces conditions sont satisfaites, on a pour tout¶$p\in\mathbb Z$ un isomorphisme canonique}",
    r"En outre, lorsque ces conditions sont satisfaites, on a pour tout¶$p\in\mathbb Z$ un isomorphisme canonique",
    C6UNWRAP)


# ---------------------------------------------------------------- checks
def page_text(n):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    return t.replace("\r\n", "\n")


ok = True
# 1. every old occurs exactly once in its page_NNN.tex
for x in F:
    if x["fix"] is None:
        continue
    c = page_text(x["page"]).count(x["fix"]["old"])
    if c != 1:
        ok = False
        print("PAGE-FILE COUNT", c, x["page"], repr(x["fix"]["old"][:80]))

# 2. sequential application on each page file, in list order
texts = {n: page_text(n) for n in range(66, 71)}
for x in F:
    if x["fix"] is None:
        continue
    t = texts[x["page"]]
    c = t.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print("SEQUENTIAL COUNT", c, x["page"], repr(x["fix"]["old"][:80]))
        continue
    texts[x["page"]] = t.replace(x["fix"]["old"], x["fix"]["new"])

# 3. simulate apply_fixes.py on the release file (segments located by markers at each step)
rel = RELEASE.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[" + re.escape(PART) + r"\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None


# the page files must equal the release segments (after the first comment line)
for n in range(66, 71):
    s, e = locate(rel, n)
    seg = rel[s:e]
    pf = page_text(n).split("\n", 1)[1]
    if seg != pf:
        print("SEGMENT DIFFERS FROM PAGE FILE", n, len(seg), len(pf), repr(seg[-60:]), repr(pf[-60:]))

t = rel
for x in F:
    if x["fix"] is None:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print("RELEASE COUNT", c, x["page"], repr(x["fix"]["old"][:80]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]

# brace balance of the simulated pages
for n in range(66, 71):
    s, e = locate(t, n)
    seg = t[s:e]
    if seg.count("{") != seg.count("}"):
        print("BRACES", n, seg.count("{"), seg.count("}"))
        ok = False

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(66, 71):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("total", len(F), "checks ok" if ok else "CHECKS FAILED")
# write the simulated pages for inspection
for n in range(66, 71):
    s, e = locate(t, n)
    (RUN / "crops_066_070" / f"sim_page_{n:03d}.tex").write_text(t[s:e], encoding="utf-8")
