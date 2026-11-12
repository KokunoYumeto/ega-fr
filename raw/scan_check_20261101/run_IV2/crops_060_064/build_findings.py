"""Build findings_060_064.json; check that every fix's old occurs exactly once
in its page file (CRLF normalised to LF) and that no two olds on a page overlap.
Strings are raw; the sign ⏎ stands for a line break."""
import json
from collections import Counter
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_060_064.json"
NL = "⏎"

F = []


def f(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


RESP = "'(resp.' and the closing parenthesis roman, the words between italic"
RESP_TEX = "all italic inside the statement environment"

# ---------------------------------------------------------------- page 60
p = 60
f(p, "Lemme (4.4.2), label (ii)", "label (ii) upright roman", r"\item[(ii)] comes out italic in the italic lemma",
  "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]")
f(p, "Lemme (4.4.2) (ii): 'est irréductible (resp. connexe).'", RESP, RESP_TEX,
  "convention", 6, "high", r"est irréductible (resp. connexe).⏎\end{enumerate}",
  r"est irréductible \textup{(resp.} connexe\textup{)}.⏎\end{enumerate}")
f(p, "Lemme (4.4.2): 'Alors pour que X' soit irréductible (resp. connexe)'", RESP, RESP_TEX,
  "convention", 6, "high", r"soit irréductible (resp. connexe), il faut",
  r"soit irréductible \textup{(resp.} connexe\textup{)}, il faut")
f(p, "proof of (4.4.2): 'on a donc X_i = X—f(X'—X'_i)', first dash", "X—f(...): long dash", "X-f( (minus sign)",
  "convention", 7, "high", r"$X_i=X-f", r"$X_i=X\setmin f")
f(p, "proof of (4.4.2): 'X_i = X—f(X'—X'_i)', second dash", "X'—X'_i: long dash", "X'-X'_i (minus sign)",
  "convention", 7, "high", r"(X'-X'_i)", r"(X'\setmin X'_i)")
f(p, "Remarque (4.4.3): 'du sous-espace ouvert X—{x_0} de X'", "X—{x_0}: long dash", r"$X-\{x_0\}$ (minus sign)",
  "convention", 7, "high", r"$X-\{x_0\}$", r"$X\setmin\{x_0\}$")
f(p, "Remarque (4.4.3): 'le produit X×_k P'", "P roman, same face and weight as X and S (stem 5-6 px like the roman letters; enlarged crop)",
  r"\mathbf P (bold)", "font", None, "high", r"$X\times_k\mathbf P$", r"$X\times_k P$",
  "The projective line P of this remark is printed with a plain roman capital (not the bold italic P of convention 10); four occurrences on the page, one entry each.")
f(p, "Remarque (4.4.3): 'où P est la droite projective sur k'", "P roman (not bold)", r"\mathbf P",
  "font", None, "high", r"où $\mathbf P$ est", r"où $P$ est", "As the previous entry.")
f(p, "Remarque (4.4.3): 't_0 un point fermé de P'", "P roman (not bold)", r"\mathbf P",
  "font", None, "high", r"point fermé de $\mathbf P$", r"point fermé de $P$", "As the previous entry.")
f(p, "Remarque (4.4.3): 'q : S→P les projections'", "P roman (not bold)", r"\mathbf P",
  "font", None, "high", r"$q:S\to\mathbf P$", r"$q:S\to P$", "As the previous entry.")
f(p, "Théorème (4.4.4): 'Si X est irréductible (resp. connexe)'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexe), il en est de même de $X\otimes_k K$",
  r"\textup{(resp.} connexe\textup{)}, il en est de même de $X\otimes_k K$")
f(p, "proof of (4.4.4): 'Mais le k(x)-préschéma p^{-1}(x)'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"le $k(x)$-préschéma", r"le $\boldsymbol{k}(x)$-préschéma")
f(p, "proof of (4.4.4): 'isomorphe à Spec(k(x)⊗_k K)'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"\operatorname{Spec}(k(x)\otimes_k K)", r"\operatorname{Spec}(\boldsymbol{k}(x)\otimes_k K)")
f(p, "proof of (4.4.4): '(I, 3.6.2)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 3.6.2)", r"(\textbf{I}, 3.6.2)")
f(p, "Corollaire (4.4.5): 'une partie irréductible (resp. connexe) de X'", RESP, RESP_TEX,
  "convention", 6, "high", r"partie irréductible (resp. connexe) de $X$",
  r"partie irréductible \textup{(resp.} connexe\textup{)} de $X$")
f(p, "Corollaire (4.4.5): 'p^{-1}(Z) est irréductible (resp. connexe);'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexe)~; en particulier", r"\textup{(resp.} connexe\textup{)}~; en particulier")
f(p, "Corollaire (4.4.5): '(resp. la composante connexe)'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. la composante connexe)", r"\textup{(resp.} la composante connexe\textup{)}")
f(p, "Corollaire (4.4.5): 'composante irréductible (resp. connexe) de X⊗_k K'", RESP, RESP_TEX,
  "convention", 6, "high", r"composante irréductible (resp. connexe) de $X\otimes_k K$",
  r"composante irréductible \textup{(resp.} connexe\textup{)} de $X\otimes_k K$")
f(p, "end of page, 'Z' = p^{-1}(Z); la' | p. 61 'relation d'équivalence'",
  "the sentence runs on over the page break: p. 61 begins 'relation d'équivalence R définie par p ...' flush left, no new paragraph",
  r"blank line before \oldpage[IV-2]{61} (and after it): paragraph break inside the sentence",
  "other", None, "high", r"$Z'=p^{-1}(Z)$~; la⏎⏎", r"$Z'=p^{-1}(Z)$~; la⏎",
  "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 61 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 61
p = 61
f(p, "top of page", "page begins mid-sentence: 'relation d'équivalence R ...' (no indent, same paragraph as p. 60)",
  r"\oldpage[IV-2]{61} followed by a blank line", "other", None, "high",
  r"\oldpage[IV-2]{61}⏎⏎relation", r"\oldpage[IV-2]{61}⏎relation",
  "Apply together with the p. 60 entry '$Z'=p^{-1}(Z)$~; la' (blank line before the marker).")
f(p, "proof of (4.4.5), last line: 'd'où la première assertion de (4.4.4).'",
  "(4.4.4) (enlarged crop); the sentence ends the proof of Corollaire (4.4.5), whose first assertion it proves",
  "(4.4.4), as printed", "misprint_in_print", None, "medium", None, None,
  "The TeX keeps the printed reading. The proof of (4.4.5) announces 'pour prouver la première' and concludes with Lemme (4.4.2) applied to Z' -> Z; Théorème (4.4.4) has a single assertion. Not in the authors' Liste 3 of errata (ega4-errata-addenda-list3-fr.tex).",
  corrected="(4.4.5)")
f(p, "Corollaire (4.4.6): 'étant celles de (4.4.5)'", "reference (4.4.5) upright inside the italic statement",
  "italic inside the corollary environment", "convention", 6, "high",
  r"celles de (4.4.5), l'application", r"celles de \textup{(4.4.5)}, l'application")
f(p, "Corollaire (4.4.6): 'l'application Z ⇝ p^{-1}(Z)'", "wavy maps-to arrow ⇝ (enlarged crop)", r"\mapsto",
  "symbol", None, "high", r"$Z\mapsto p^{-1}(Z)$", r"$Z\leadsto p^{-1}(Z)$",
  "Not convention 3 (the printed arrow is not plain); \\leadsto as used elsewhere in ega4-2-fr.tex.")
f(p, "Corollaire (4.4.6): 'composantes irréductibles (resp. connexes) de X sur'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexes) de $X$ sur", r"\textup{(resp.} connexes\textup{)} de $X$ sur")
f(p, "Corollaire (4.4.6): '(resp. connexes) de X⊗_k K, dont'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexes) de $X\otimes_k K$, dont",
  r"\textup{(resp.} connexes\textup{)} de $X\otimes_k K$, dont")
f(p, "Corollaire (4.4.6): 'est Z' ⇝ p(Z')'", "wavy maps-to arrow ⇝ (enlarged crop)", r"\mapsto",
  "symbol", None, "high", r"$Z'\mapsto p(Z')$", r"$Z'\leadsto p(Z')$", "As the previous arrow.")
f(p, "heading 4.5", "'4.5. Préschémas géométriquement irréductibles et géométriquement connexes.' (final full stop)",
  r"\subsection{...connexes} (no full stop)", "punctuation", None, "high",
  r"géométriquement⏎connexes}", r"géométriquement⏎connexes.}",
  "As the subsection page fixes elsewhere (GLOBAL_ISSUES 43/58).")
f(p, "Proposition (4.5.1): 'Soit n (resp. n') le cardinal'", RESP, RESP_TEX,
  "convention", 6, "high", r"Soit $n$ (resp. $n'$) le", r"Soit $n$ \textup{(resp.} $n'$\textup{)} le")
f(p, "Proposition (4.5.1): '(resp. des composantes connexes) de X⊗_kΩ'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. des composantes connexes) de⏎$X\otimes_k\Omega$",
  r"\textup{(resp.} des composantes connexes\textup{)} de⏎$X\otimes_k\Omega$")
f(p, "Proposition (4.5.1): '(resp. des composantes connexes) de X⊗_k K est'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. des composantes connexes)⏎de $X\otimes_k K$",
  r"\textup{(resp.} des composantes connexes\textup{)}⏎de $X\otimes_k K$")
f(p, "Proposition (4.5.1): 'est ≤ n (resp. ≤ n').'", "'(resp.' and the closing parenthesis roman", RESP_TEX,
  "convention", 6, "high", r"(resp. $\leqslant n'$)", r"\textup{(resp.} $\leqslant n'$\textup{)}")
f(p, "Définition (4.5.2): 'Le cardinal n (resp. n')'", RESP, RESP_TEX,
  "convention", 6, "high", r"cardinal $n$ (resp. $n'$)", r"cardinal $n$ \textup{(resp.} $n'$\textup{)}")
f(p, "Définition (4.5.2): 'de (4.5.1) s'appelle'", "reference (4.5.1) upright inside the italic definition",
  "italic inside the definition environment", "convention", 6, "high",
  r"de (4.5.1) s'appelle", r"de \textup{(4.5.1)} s'appelle")
f(p, "Définition (4.5.2): 'le nombre géométrique de composantes irréductibles'",
  "italic like the rest of the definition, no change of face (enlarged crop)",
  r"\emph{...} inside the italic definition (comes out upright)", "convention", 6, "high",
  r"\emph{nombre géométrique⏎de composantes irréductibles}", r"nombre géométrique⏎de composantes irréductibles")
f(p, "Définition (4.5.2): '(resp. de composantes connexes)'",
  "'(resp.' and ')' roman; 'de composantes connexes' italic like the rest of the definition",
  r"(resp. \emph{de composantes connexes}): resp. italic, the \emph words upright", "convention", 6, "high",
  r"(resp. \emph{de composantes connexes})", r"\textup{(resp.} de composantes connexes\textup{)}",
  "Two convention-6 items in one edit (roman '(resp.' set italic; italic words set upright by \\emph).")
f(p, "Définition (4.5.2): 'Si n = 1 (resp. n' ≤ 1)'", "'(resp.' and the closing parenthesis roman", RESP_TEX,
  "convention", 6, "high", r"(resp. $n'\leqslant1$)", r"\textup{(resp.} $n'\leqslant1$\textup{)}")
f(p, "Définition (4.5.2): 'k-préschéma géométriquement irréductible'",
  "italic like the rest of the definition, no change of face", r"\emph{...} inside the italic definition (comes out upright)",
  "convention", 6, "high", r"\emph{géométriquement irréductible}", r"géométriquement irréductible")
f(p, "Définition (4.5.2): '(resp. géométriquement connexe).'",
  "'(resp.' and ')' roman; 'géométriquement connexe' italic like the rest",
  r"(resp. \emph{géométriquement connexe}): resp. italic, the \emph words upright", "convention", 6, "high",
  r"(resp. \emph{géométriquement⏎connexe})", r"\textup{(resp.} géométriquement⏎connexe\textup{)}",
  "Two convention-6 items in one edit, as above.")
f(p, "after (4.5.2): 'dans (III, 4.3.4)'", "bold III", "plain III",
  "convention", 2, "high", r"(III, 4.3.4)", r"(\textbf{III}, 4.3.4)")
f(p, "(4.5.3): 'espace sous-jacent (I, 5.2.1)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 5.2.1)", r"(\textbf{I}, 5.2.1)")
f(p, "(4.5.3): 'il résulte de (I, 5.1.8)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 5.1.8)", r"(\textbf{I}, 5.1.8)")
f(p, "Proposition (4.5.4): '(resp. géométriquement connexe), il en est de même'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. géométriquement connexe), il en",
  r"\textup{(resp.} géométriquement connexe\textup{)}, il en")

# ---------------------------------------------------------------- page 62
p = 62
f(p, "proof of (4.5.4): 'est surjectif (I, 3.5.2)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 3.5.2)", r"(\textbf{I}, 3.5.2)")
f(p, "Définition (4.5.5): 'de préschémas est irréductible'", "italic like the rest of the definition, no change of face (enlarged crop)",
  r"\emph{irréductible} inside the italic definition (comes out upright)", "convention", 6, "high",
  r"\emph{irréductible}", r"irréductible")
f(p, "Définition (4.5.5): '(resp. connexe), si,'", "'(resp.' and ')' roman; 'connexe' italic like the rest",
  r"(resp. \emph{connexe}): resp. italic, connexe upright", "convention", 6, "high",
  r"(resp. \emph{connexe})", r"\textup{(resp.} connexe\textup{)}",
  "Two convention-6 items in one edit (roman '(resp.' set italic; italic word set upright by \\emph).")
f(p, "Définition (4.5.5): 'le k(y)-préschéma f^{-1}(y)'", "bold italic k in k(y)", "plain k",
  "convention", 1, "high", r"le $k(y)$-préschéma", r"le $\boldsymbol{k}(y)$-préschéma")
f(p, "Définition (4.5.5): '(resp. géométriquement connexe).'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. géométriquement connexe).", r"\textup{(resp.} géométriquement connexe\textup{)}.")
f(p, "Proposition (4.5.6), label (i)", "label (i) upright roman", r"\item[(i)] comes out italic in the italic proposition",
  "convention", 6, "high", r"\item[(i)] Soient $X$ un", r"\item[\textup{(i)}] Soient $X$ un")
f(p, "Proposition (4.5.6) (i): '(resp. connexes) de X_(K) relativement à K'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexes) de $X_{(K)}$", r"\textup{(resp.} connexes\textup{)} de $X_{(K)}$")
f(p, "Proposition (4.5.6) (i): '(resp. connexes) de X relativement à k'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexes) de $X$ relativement", r"\textup{(resp.} connexes\textup{)} de $X$ relativement")
f(p, "Proposition (4.5.6) (i): '(resp. géométriquement connexe), il faut et il suffit'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp.⏎géométriquement connexe), il faut", r"\textup{(resp.}⏎géométriquement connexe\textup{)}, il faut")
f(p, "Proposition (4.5.6), label (ii)", "label (ii) upright roman", r"\item[(ii)] comes out italic in the italic proposition",
  "convention", 6, "high", r"\item[(ii)] Soient $f", r"\item[\textup{(ii)}] Soient $f")
f(p, "Proposition (4.5.6) (ii): 'Si f est irréductible (resp. connexe)'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexe), il en est de même de $f'$", r"\textup{(resp.} connexe\textup{)}, il en est de même de $f'$")
f(p, "proof of (4.5.6), first paragraph", "'(i) Si Ω est une extension algébriquement close de K, ...' (no 'Pour')",
  "'Pour (i), si Ω est ...'", "extra", None, "high", r"Pour (i), si", r"(i) Si",
  "The TeX adds 'Pour' and a comma; the print opens the paragraph with the label (i).")
f(p, "proof of (4.5.6), second paragraph", "'(ii) Pour tout y'∈Y', si l'on pose ...'",
  "'Pour (ii), pour tout y'∈Y' ...'", "extra", None, "high", r"Pour (ii), pour tout", r"(ii) Pour tout",
  "The TeX adds 'Pour (ii),' before the printed 'Pour tout'; the print opens with the label (ii).")
f(p, "proof of (4.5.6) (ii): subscript of ⊗_{k(y)}", "bold k, upright in the subscript (enlarged crop)", r"\otimes_{k(y)}",
  "convention", 1, "high", r"\otimes_{k(y)}", r"\otimes_{\mathbf{k}(y)}", "Bold upright in subscripts (GLOBAL_ISSUES 48).")
f(p, "proof of (4.5.6) (ii): '⊗_{k(y)} k(y')'", "bold italic k in k(y')", "plain k",
  "convention", 1, "high", r"k(y')$", r"\boldsymbol{k}(y')$", "Adjacent to the previous entry, not overlapping.")
f(p, "proof of (4.5.6) (ii): '(I, 3.6.4)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
f(p, "Proposition (4.5.7): 'surjectif irréductible (resp. connexe),'", RESP, RESP_TEX,
  "convention", 6, "high", r"surjectif irréductible (resp. connexe),", r"surjectif irréductible \textup{(resp.} connexe\textup{)},")
f(p, "Proposition (4.5.7): 'Y' est irréductible (resp. connexe), et f'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. connexe), et $f$ universellement", r"\textup{(resp.} connexe\textup{)}, et $f$ universellement")
f(p, "Proposition (4.5.7): '(resp. plat et quasi-compact, ..., ou universellement fermé)'", RESP, RESP_TEX,
  "convention", 6, "high",
  r"(resp. plat et⏎quasi-compact, ou universellement ouvert, ou universellement fermé)",
  r"\textup{(resp.} plat et⏎quasi-compact, ou universellement ouvert, ou universellement fermé\textup{)}")
f(p, "Proposition (4.5.7): 'alors X' est irréductible (resp. connexe).'", RESP, RESP_TEX,
  "convention", 6, "high", r"$X'$ est irréductible (resp. connexe).", r"$X'$ est irréductible \textup{(resp.} connexe\textup{)}.")
f(p, "Corollaire (4.5.8), label (i)", "label (i) upright roman", r"\item[(i)] comes out italic in the italic corollary",
  "convention", 6, "high", r"\item[(i)] Si $X$ est", r"\item[\textup{(i)}] Si $X$ est")
f(p, "Corollaire (4.5.8) (i): '(resp. géométriquement connexe) et Y'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp. géométriquement⏎connexe) et $Y$", r"\textup{(resp.} géométriquement⏎connexe\textup{)} et $Y$")
f(p, "Corollaire (4.5.8) (i): 'Y irréductible (resp. connexe), alors'", RESP, RESP_TEX,
  "convention", 6, "high", r"irréductible (resp. connexe), alors", r"irréductible \textup{(resp.} connexe\textup{)}, alors")
f(p, "Corollaire (4.5.8) (i): 'X×_kY est irréductible (resp. connexe).'", RESP, RESP_TEX,
  "convention", 6, "high", r"Y$ est⏎irréductible (resp. connexe).", r"Y$ est⏎irréductible \textup{(resp.} connexe\textup{)}.")
f(p, "Corollaire (4.5.8), label (ii)", "label (ii) upright roman", r"\item[(ii)] comes out italic in the italic corollary",
  "convention", 6, "high", r"\item[(ii)] Si $X$ et", r"\item[\textup{(ii)}] Si $X$ et")
f(p, "Corollaire (4.5.8) (ii): '(resp. géométriquement connexes), il en est de même'", RESP, RESP_TEX,
  "convention", 6, "high", r"(resp.⏎géométriquement connexes), il en", r"\textup{(resp.}⏎géométriquement connexes\textup{)}, il en")
f(p, "proof of (4.5.8), first paragraph", "'(i) Le morphisme structural X→Spec(k) ...' (no 'Pour')",
  "'Pour (i), le morphisme structural ...'", "extra", None, "high", r"Pour (i), le morphisme", r"(i) Le morphisme",
  "The TeX adds 'Pour' and a comma; the print opens the paragraph with the label (i).")
f(p, "proof of (4.5.8), second paragraph", "'(ii) Si Ω est une extension algébriquement close de k, ...'",
  "'Pour (ii), si Ω est ...'", "extra", None, "high", r"Pour (ii), si", r"(ii) Si",
  "The TeX adds 'Pour' and a comma; the print opens the paragraph with the label (ii).")
f(p, "proof of (4.5.8) (ii): '(I, 3.3.10)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 3.3.10)", r"(\textbf{I}, 3.3.10)")
f(p, "Proposition (4.5.9), label a)", "label a) upright roman, letter and parenthesis (enlarged crop); the references a), b), c) in the proof are italic",
  r"\item[$a)$] (math italic a)", "font", None, "high", r"\item[$a)$]", r"\item[\textup{a)}]",
  r"\textup because the label stands in the italic proposition environment.")
f(p, "Proposition (4.5.9) a): '(autrement dit, pour toute extension K de k, X⊗_kK est irréductible)'",
  "the whole parenthesis is roman except 'toute', which is italic (enlarged crop)",
  "the parenthesis is italic with the rest of the proposition; 'toute' not distinguished", "convention", 6, "high",
  r"(autrement dit, pour toute⏎extension $K$ de $k$, $X\otimes_k K$ est irréductible)",
  r"\textup{(autrement dit, pour \emph{toute}⏎extension $K$ de $k$, $X\otimes_k K$ est irréductible)}",
  r"Roman words inside the italic statement, with the printed emphasis on 'toute' (\emph inside \textup gives italic).")
f(p, "Proposition (4.5.9), label b)", "label b) upright roman", r"\item[$b)$] (math italic b)",
  "font", None, "high", r"\item[$b)$]", r"\item[\textup{b)}]")
f(p, "Proposition (4.5.9), label c)", "label c) upright roman", r"\item[$c)$] (math italic c)",
  "font", None, "high", r"\item[$c)$]", r"\item[\textup{c)}]")
f(p, "Proposition (4.5.9) c): 'k(x) est une extension primaire de k'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"$k(x)$⏎est une extension primaire", r"$\boldsymbol{k}(x)$⏎est une extension primaire")
f(p, "end of page, 'la projection canonique, les' | p. 63 'points maximaux'",
  "the sentence runs on over the page break: p. 63 begins 'points maximaux de X⊗_kK ...' flush left",
  r"blank line before \oldpage[IV-2]{63} (and after it): paragraph break inside the sentence",
  "other", None, "high", r"projection canonique, les⏎⏎", r"projection canonique, les⏎",
  "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 63 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 63
p = 63
f(p, "top of page", "page begins mid-sentence: 'points maximaux de X⊗_kK sont ceux ...' (no indent)",
  r"\oldpage[IV-2]{63} followed by a blank line", "other", None, "high",
  r"\oldpage[IV-2]{63}⏎⏎points", r"\oldpage[IV-2]{63}⏎points",
  "Apply together with the p. 62 entry 'projection canonique, les' (blank line before the marker).")
f(p, "proof of (4.5.9): 'p^{-1}(x) = Spec(k(x)⊗_k K)'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"\operatorname{Spec}(k(x)\otimes_k K)", r"\operatorname{Spec}(\boldsymbol{k}(x)\otimes_k K)")
f(p, "proof of (4.5.9): '((2.3.4) et (0_I, 2.1.8))'", "bold 0", "plain 0",
  "convention", 2, "high", r"$(0_{\mathrm I},2.1.8)$)~;", r"$(\mathbf{0}_{\mathrm I},2.1.8)$)~;")
f(p, "proof of (4.5.9): 'revient à dire que k(y) est une extension primaire'", "bold italic k in k(y)", "plain k",
  "convention", 1, "high", r"$k(y)$", r"$\boldsymbol{k}(y)$",
  "The printed y is itself a misprint (next entry); this entry changes only the k.")
f(p, "proof of (4.5.9): 'revient à dire que k(y) est une extension primaire de k'",
  "k(y) (enlarged crop); no point y occurs in this proof: the fibre is p^{-1}(x), x the generic point of X, and condition c) concerns k(x)",
  "$k(y)$, as printed", "misprint_in_print", None, "high", None, None,
  "The TeX keeps the printed reading. Correct reading k(x), in the form it takes after the convention-1 entry above.",
  corrected=r"$\boldsymbol{k}(x)$")
f(p, "proof of (4.5.9): 'montre que pour toute extension K de k'", "'toute' italic (emphasis)", "toute roman",
  "italics", None, "high", r"montre que pour toute", r"montre que pour \emph{toute}")
f(p, "Corollaire (4.5.10): 'la fermeture algébrique séparable de k dans k(x)'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"dans $k(x)$, $k''$", r"dans $\boldsymbol{k}(x)$, $k''$")
f(p, "proof of (4.5.10): 'la fibre Spec(k(x)⊗_k k'')'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"\operatorname{Spec}(k(x)\otimes_k k'')", r"\operatorname{Spec}(\boldsymbol{k}(x)\otimes_k k'')")
f(p, "Corollaire (4.5.11): 'k'_i de k dans k(x_i)'", "bold italic k in k(x_i)", "plain k",
  "convention", 1, "high", r"dans $k(x_i)$ soit", r"dans $\boldsymbol{k}(x_i)$ soit")
f(p, "proof of (4.5.11): 'fibres Spec(k(x_i)⊗_k L)'", "bold italic k in k(x_i)", "plain k",
  "convention", 1, "high", r"\operatorname{Spec}(k(x_i)\otimes_k L)", r"\operatorname{Spec}(\boldsymbol{k}(x_i)\otimes_k L)")
f(p, "proof of (4.5.11): 'en vertu de (2.3.4) et (0_I, 2.1.8) appliqué'", "bold 0", "plain 0",
  "convention", 2, "high", r"$(0_{\mathrm I},2.1.8)$ appliqué", r"$(\mathbf{0}_{\mathrm I},2.1.8)$ appliqué")
f(p, "after (4.5.11): 'tout k-préschéma X de type fini sur k'", "'de type fini sur k' italic (enlarged crop)", "roman",
  "italics", None, "high", r"$X$ de⏎type fini sur $k$,", r"$X$ \emph{de⏎type fini sur $k$},")
f(p, "after (4.5.11): 'chacun des k(x_i)'", "bold italic k in k(x_i)", "plain k",
  "convention", 1, "high", r"chacun des $k(x_i)$", r"chacun des $\boldsymbol{k}(x_i)$")
f(p, "after (4.5.11): 'la fermeture algébrique de k dans k(x_i) ([1], ...)'", "bold italic k in k(x_i)", "plain k",
  "convention", 1, "high", r"$k(x_i)$ ([1]", r"$\boldsymbol{k}(x_i)$ ([1]")
f(p, "heading of Remarques (4.5.12)", "'Remarques (4.5.12). —' (plural)", r"\begin{remark}[4.5.12] prints 'Remarque (4.5.12)'",
  "word", None, "high", r"\begin{remark}[4.5.12]", r"\begin{remarks}[4.5.12]",
  r"Apply together with the \end{remark} -> \end{remarks} entry on p. 64, where these remarks end.")
f(p, "Remarques (4.5.12) (i): 'Weil dit d'autre part « absolument irréductible »'", "'absolument irréductible' italic in the roman remark",
  "no emphasis", "italics", None, "high", r"«~absolument irréductible~»", r"«~\emph{absolument irréductible}~»")
f(p, "Remarques (4.5.12) (i): '« absolument connexe »'", "italic", "no emphasis",
  "italics", None, "high", r"«~absolument connexe~»", r"«~\emph{absolument connexe}~»")
f(p, "Remarques (4.5.12) (i): '« absolument normal »'", "italic", "no emphasis",
  "italics", None, "high", r"«~absolument⏎normal~»", r"«~\emph{absolument⏎normal}~»")
f(p, "Remarques (4.5.12) (i): 'une « variété algébrique » V est donnée d'abord'", "'d'abord' italic", "no emphasis",
  "italics", None, "high", r"donnée d'abord", r"donnée \emph{d'abord}")
f(p, "end of page, 'comme un objet' | p. 64 'géométrique au-dessus'",
  "the sentence runs on over the page break: p. 64 begins 'géométrique au-dessus d'un corps ...' flush left",
  r"blank line before \oldpage[IV-2]{64} (and after it): paragraph break inside the sentence",
  "other", None, "high", r"comme un objet⏎⏎", r"comme un objet⏎",
  "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 64 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 64
p = 64
f(p, "top of page", "page begins mid-sentence: 'géométrique au-dessus d'un corps ...' (no indent)",
  r"\oldpage[IV-2]{64} followed by a blank line", "other", None, "high",
  r"\oldpage[IV-2]{64}⏎⏎géométrique", r"\oldpage[IV-2]{64}⏎géométrique",
  "Apply together with the p. 63 entry 'comme un objet' (blank line before the marker).")
f(p, "Remarques (4.5.12) (i), l. 1: 'd'un corps algébriquement clos Ω'", "'algébriquement clos' italic", "no emphasis",
  "italics", None, "high", r"d'un corps algébriquement clos $\Omega$", r"d'un corps \emph{algébriquement clos} $\Omega$")
f(p, "Remarques (4.5.12) (ii): 'son corps de fonctions rationnelles k(x)'", "bold italic k in k(x)", "plain k",
  "convention", 1, "high", r"$k(x)$ est $\mathbf C((T))$", r"$\boldsymbol{k}(x)$ est $\mathbf C((T))$")
f(p, "end of Remarques (4.5.12)", "plural heading 'Remarques (4.5.12)' (p. 63)", r"\end{remark}",
  "word", None, "high", r"\end{enumerate}⏎\end{remark}", r"\end{enumerate}⏎\end{remarks}",
  r"Apply together with the \begin{remark}[4.5.12] -> \begin{remarks}[4.5.12] entry on p. 63.")
f(p, "proof of (4.5.13): '(II, 6.1.10)'", "bold II", "plain II",
  "convention", 2, "high", r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)")
f(p, "proof of (4.5.13): 'on en conclut (I, 3.4.7)'", "bold I", "plain I",
  "convention", 2, "high", r"(I, 3.4.7)", r"(\textbf{I}, 3.4.7)")
f(p, "proof of (4.5.13): 'à l'ensemble ouvert et fermé X'—U''", "X'—U': long dash", "X'-U' (minus sign)",
  "convention", 7, "high", r"ouvert et fermé $X'-U'$", r"ouvert et fermé $X'\setmin U'$")
f(p, "proof of (4.5.13): 'f'^{-1}(X'—U') = Y''", "X'—U': long dash", "X'-U' (minus sign)",
  "convention", 7, "high", r"f'^{-1}(X'-U')", r"f'^{-1}(X'\setmin U')")
f(p, "Corollaire (4.5.13.1), label (i)", "label (i) upright roman", r"\item[(i)] comes out italic in the italic corollary",
  "convention", 6, "high", r"\item[(i)] Soient $X$, $Y$", r"\item[\textup{(i)}] Soient $X$, $Y$")
f(p, "Corollaire (4.5.13.1), label (ii)", "label (ii) upright roman", r"\item[(ii)] comes out italic in the italic corollary",
  "convention", 6, "high", r"\item[(ii)] Soit $X$", r"\item[\textup{(ii)}] Soit $X$")
f(p, "proof of (4.5.13.1), first line", "'(i) On peut supposer Y réduit, ...' (no 'Pour')",
  "'Pour (i), on peut supposer ...'", "extra", None, "high", r"Pour (i), on peut", r"(i) On peut",
  "The TeX adds 'Pour' and a comma; the print opens the paragraph with the label (i).")
f(p, "proof of (4.5.13.1): 'se factorise en f : Y →g X_0 →j X'", "'f :' before Y (enlarged crop)",
  r"$Y\xrightarrow{g}X_0\xrightarrow{j}X$ without 'f:'", "missing", None, "high",
  r"$Y\xrightarrow{g}X_0", r"$f:Y\xrightarrow{g}X_0")
f(p, "end of page, 'X_0' | p. 65 'désignant le sous-préschéma réduit'",
  "the sentence runs on over the page break (p. 64 ends '..., X_0')",
  r"blank line before \oldpage[IV-2]{65} (and after it): paragraph break inside the sentence",
  "other", None, "high", r", $X_0$⏎⏎", r", $X_0$⏎",
  r"Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with removing the blank line after the marker on p. 65: '\oldpage[IV-2]{65}' + blank line + 'désignant' -> '\oldpage[IV-2]{65}' + newline + 'désignant' (p. 65 is outside this batch).")

# ---------------------------------------------------------------- checks
pages = {}
for n in range(60, 65):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

ok = True
spans = {}
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    txt = pages[d["page"]]
    c = txt.count(old)
    if c != 1:
        ok = False
        print(f"COUNT {c}: p.{d['page']} #{i} {old!r}")
        continue
    a = txt.index(old)
    spans.setdefault(d["page"], []).append((a, a + len(old), i))
    if d["fix"]["old"] == d["fix"]["new"]:
        ok = False
        print("no-op fix", i)
for pg, sp in spans.items():
    sp.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(sp, sp[1:]):
        if a2 < b1:
            ok = False
            print(f"OVERLAP p.{pg}: #{i1} and #{i2}")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT, len(F), "entries; checks ok" if ok else "CHECKS FAILED")
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for n in range(60, 65):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
