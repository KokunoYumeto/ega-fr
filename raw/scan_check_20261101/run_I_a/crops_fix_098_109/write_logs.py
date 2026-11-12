"""Write FIXLOG_098_109.jsonl and MISPRINTS_098_109.json for the EGA I pp. 98-109 fix pass, and check every logged
change against the edited release files: the "new" string must occur exactly once in the file and lie on its page
(between \\oldpage[I]{N} and the next marker; a moved marker counts as the start of its page), and "old" must be gone.
usage: python -I write_logs.py"""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
NATIVE = "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega1/"
F2 = NATIVE + "ega1-2-fr.tex"
F3 = NATIVE + "ega1-3-fr.tex"
A = "findings_095_099.json"
B = "findings_100_104.json"
C = "findings_105_109.json"

changes = []


def ch(file, page, old, new, why):
    changes.append(dict(file=file, page=page, old=old, new=new, why=why))


# ---------------- ega1-2-fr.tex, pp. 98-104 (upper part) ----------------
ch(F2, 98, r"$x\longmapsto\overline{\{x\}}$ est donc une bijection", r"$x\to\overline{\{x\}}$ est donc une bijection",
   f"conv. 3: the print has a plain arrow x → {{x}}‾ in Prop. (2.1.5), not ↦ ({A}, p. 98)")
ch(F2, 98, r"(\hyperref[0.2.1.1-fr]{0, 2.1.1} et", r"(\hyperref[0.2.1.1-fr]{\textbf{0}, 2.1.1} et",
   f"conv. 2: bold 0 in (𝟎, 2.1.1 et 2.1.4) ({A}, p. 98)")
ch(F2, 98, r"(\hyperref[0.2.1.3-fr]{0, 2.1.3}).", r"(\hyperref[0.2.1.3-fr]{\textbf{0}, 2.1.3}).",
   f"conv. 2: bold 0 in (𝟎, 2.1.3) ({A}, p. 98)")
ch(F2, 98, r"appelle \emph{morphisme (de préschémas)} de", r"appelle morphisme (de préschémas) de",
   f"conv. 6: 'morphisme (de préschémas)' is in the same italics as the rest of Def. (2.2.1), parentheses included; "
   f"\\emph inside the italic environment set it upright ({A}, p. 98; print checked)")
ch(F2, 99, r"$\theta^x:k(\psi(x))\to k(x)$", r"$\theta^x:\boldsymbol{k}(\psi(x))\to\boldsymbol{k}(x)$",
   f"conv. 1: bold italic k in θ^x : k(ψ(x)) → k(x), both k ({A}, p. 99)")
ch(F2, 99, r"considérer $k(x)$", r"considérer $\boldsymbol{k}(x)$",
   f"conv. 1: bold italic k in 'considérer k(x)' ({A}, p. 99)")
ch(F2, 99, r"du corps $k(\psi(x))$.", r"du corps $\boldsymbol{k}(\psi(x))$.",
   f"conv. 1: bold italic k in 'du corps k(ψ(x))' ({A}, p. 99)")
ch(F2, 99, r"(\hyperref[0.3.5.5-fr]{0, 3.5.5})", r"(\hyperref[0.3.5.5-fr]{\textbf{0}, 3.5.5})",
   f"conv. 2: bold 0 in (𝟎, 3.5.5) ({A}, p. 99)")
ch(F2, 99, r"(\hyperref[0.4.1.2-fr]{0, 4.1.2})", r"(\hyperref[0.4.1.2-fr]{\textbf{0}, 4.1.2})",
   f"conv. 2: bold 0 in (𝟎, 4.1.2) ({A}, p. 99)")
ch(F2, 99, r"(\hyperref[0.4.1.1-fr]{0, 4.1.1})", r"(\hyperref[0.4.1.1-fr]{\textbf{0}, 4.1.1})",
   f"conv. 2: bold 0 in (𝟎, 4.1.1) ({A}, p. 99)")
ch(F2, 99, r"est $(\psi_\alpha,\theta_\alpha)$, et il est", r"est $(\psi_\alpha,\theta_\alpha)$ et il est",
   f"rule 1 (punctuation): no comma after (ψ_α, θ_α) before 'et il est clair' in the print ({A}, p. 99)")
ch(F2, 99, r"(\hyperref[0.5.5.2-fr]{0, 5.5.2})", r"(\hyperref[0.5.5.2-fr]{\textbf{0}, 5.5.2})",
   f"conv. 2: bold 0 in (𝟎, 5.5.2) ({A}, p. 99)")
ch(F2, 99, r"Sous les hypothèses de (\hyperref[I.2.2.4-fr]{2.2.4}), soient",
   r"Sous les hypothèses de \textup{(\hyperref[I.2.2.4-fr]{2.2.4})}, soient",
   f"conv. 6: the reference (2.2.4) is printed upright inside the italic Prop. (2.2.5) (print checked; references in "
   f"italic statements treated as in {C}, p. 105)")
ch(F2, 99, r"$\mathscr{G}$ (resp. $\mathscr{F}$) un", r"$\mathscr{G}$ \textup{(resp. $\mathscr{F}$)} un",
   f"conv. 6: '(resp.' and the closing parenthesis after ℱ are roman inside the italic Prop. (2.2.5) ({A}, p. 99; "
   f"print checked)")
ch(F2, 99, r"$\mathscr{O}_X$-Module (resp. un $\mathscr{O}_S$-Module) quasi-cohérent",
   r"$\mathscr{O}_X$-Module \textup{(resp.} un $\mathscr{O}_S$-Module) quasi-cohérent",
   f"conv. 6: '(resp.' is roman inside the italic Prop. (2.2.5); 'un 𝒪_S-Module)' is italic, closing parenthesis "
   f"included ({A}, p. 99; print checked)")
ch(F2, 100, r"$\mathscr{F}\to\mathscr{G}$ (\hyperref[0.4.4.1-fr]{0, 4.4.1}) et les",
   r"$\mathscr{F}\to\mathscr{G}$ \textup{(\hyperref[0.4.4.1-fr]{\textbf{0}, 4.4.1})} et les",
   f"conv. 2 + conv. 6: bold 0 in (𝟎, 4.4.1); the reference is upright inside the italic Prop. (2.2.5) ({B}, p. 100; "
   f"print checked)")
ch(F2, 100, r"ouverts (resp. fermés, dominants,", r"ouverts \textup{(resp.} fermés, dominants,",
   f"conv. 6: '(resp.' is roman inside the italic Prop. (2.2.7) (i); 'fermés, dominants, surjectifs)' italic, closing "
   f"parenthesis included ({B}, p. 100; print checked)")
ch(F2, 100, r"Pour que $f$ soit ouvert (resp. fermé, surjectif, dominant), il faut",
   r"Pour que $f$ soit ouvert \textup{(resp.} fermé, surjectif, dominant), il faut",
   f"conv. 6: '(resp.' is roman inside the italic Prop. (2.2.8); 'fermé, surjectif, dominant)' italic, closing "
   f"parenthesis included ({B}, p. 100; print checked)")
ch(F2, 100, "soit ouvert (resp. fermé, surjectif,\ndominant).", "soit ouvert \\textup{(resp.} fermé, surjectif,\ndominant).",
   f"conv. 6: '(resp.' is roman inside the italic Prop. (2.2.8) (second occurrence); the rest of the parenthesis "
   f"italic ({B}, p. 100; print checked)")
ch(F2, 100, r"(\hyperref[0.2.1.8-fr]{0, 2.1.8})", r"(\hyperref[0.2.1.8-fr]{\textbf{0}, 2.1.8})",
   f"conv. 2: bold 0 in (𝟎, 2.1.8) ({B}, p. 100)")
ch(F2, 101,
   "\\subsection{Recollement de préschémas}\n\\label{subsection:I.2.3-fr}\n\n\\begin{env}[2.3.1]\n"
   "\\label{I.2.3.1-fr}\n\\oldpage[I]{101}\nIl résulte",
   "\\oldpage[I]{101}\n\\subsection{Recollement de préschémas}\n\\label{subsection:I.2.3-fr}\n\n\\begin{env}[2.3.1]\n"
   "\\label{I.2.3.1-fr}\nIl résulte",
   f"rule 4: printed p. 101 begins with the heading '2.3. Recollement de préschémas.' and '(2.3.1)'; the marker stood "
   f"after the heading and the number ({B}, p. 101)")
ch(F2, 101, r"(\hyperref[0.4.1.6-fr]{0, 4.1.6})", r"(\hyperref[0.4.1.6-fr]{\textbf{0}, 4.1.6})",
   f"conv. 2: bold 0 in (𝟎, 4.1.6) ({B}, p. 101); the reference itself is a misprint for (𝟎, 4.1.7) (authors' "
   f"errata, EGA III), kept and recorded in MISPRINTS_098_109.json")
ch(F2, 101, r"l'isomorphisme de $B_s$ sur $C_t$ qui,", r"l'isomorphisme de $B$ sur $C$ qui,",
   f"rule 3 (misprint kept in the diplomatic text): the print has 'de B sur C' without subscripts; the TeX had silently "
   f"corrected it to B_s, C_t; printed reading restored, correction recorded in MISPRINTS_098_109.json ({B}, p. 101; "
   f"print checked; errata EGA III, (I, 2.3.2))")
ch(F2, 101, r"(\hyperref[II.2.4.3-fr]{II, 2.4.3})", r"(\hyperref[II.2.4.3-fr]{\textbf{II}, 2.4.3})",
   f"rule 1 (font), as conv. 2: the chapter numeral in (𝐈𝐈, 2.4.3) is bold in the print ({B}, p. 101)")
ch(F2, 101, r"est \emph{isomorphe} à $K$", r"est \emph{isomorphe à} $K$",
   f"rule 1 (italics): 'isomorphe à' is italic in the print, 'à' included ({B}, p. 101)")
ch(F2, 101, r"(\hyperref[0.1.5.1-fr]{0, 1.5.1})", r"(\hyperref[0.1.5.1-fr]{\textbf{0}, 1.5.1})",
   f"conv. 2: bold 0 in (𝟎, 1.5.1) ({B}, p. 101)")
ch(F2, 102,
   "\\begin{proposition}[2.4.2]\n\\label{I.2.4.2-fr}\n\\oldpage[I]{102}\nSoit",
   "\\oldpage[I]{102}\n\\begin{proposition}[2.4.2]\n\\label{I.2.4.2-fr}\nSoit",
   f"rule 4: printed p. 102 begins with 'Proposition (2.4.2). —'; the marker stood after the heading ({B}, p. 102)")
ch(F2, 102, r"(\hyperref[0.2.1.2-fr]{0, 2.1.2})", r"(\hyperref[0.2.1.2-fr]{\textbf{0}, 2.1.2})",
   f"conv. 2: bold 0 in (𝟎, 2.1.2) ({B}, p. 102)")
ch(F2, 102,
   "(autrement dit, des\n\\emph{générisations} de $y$ (\\hyperref[0.2.1.2-fr]{\\textbf{0}, 2.1.2}))~; en outre,",
   "\\textup{(autrement dit, des}\ngénérisations \\textup{de} $y$ "
   "\\textup{(\\hyperref[0.2.1.2-fr]{\\textbf{0}, 2.1.2}))}~; en outre,",
   f"conv. 6: '(autrement dit, des', 'de', the reference and both closing parentheses are roman inside the italic "
   f"Prop. (2.4.2); 'générisations' is italic as printed (the \\emph had set it upright) ({B}, p. 102; print checked)")
ch(F2, 102, r"\emph{On voit donc (\hyperref[I.2.1.5-fr]{2.1.5}) qu'il y a correspondance",
   r"\emph{On voit donc \textup{(\hyperref[I.2.1.5-fr]{2.1.5})} qu'il y a correspondance",
   f"conv. 6: the reference (2.1.5) is printed upright inside the italic sentence 'On voit donc ...' (print checked; "
   f"references in italic text treated as in {C}, p. 105)")
ch(F2, 102, "(autrement dit, que $\\mathscr{O}_y$\nsoit de dimension zéro).",
   "\\textup{(autrement dit, que} $\\mathscr{O}_y$\n\\textup{soit} de dimension zéro).",
   f"conv. 6: '(autrement dit, que' and 'soit' are roman inside the italic Cor. (2.4.3); 'de dimension zéro)' italic, "
   f"closing parenthesis included ({B}, p. 102; print checked)")
ch(F2, 102, r"(\hyperref[0.1.2.4-fr]{0, 1.2.4})", r"(\hyperref[0.1.2.4-fr]{\textbf{0}, 1.2.4})",
   f"conv. 2: bold 0 in (𝟎, 1.2.4) ({B}, p. 102)")
ch(F2, 102, r"$\mathscr{O}_y/\mathfrak{a}_y=k(y)$", r"$\mathscr{O}_y/\mathfrak{a}_y=\boldsymbol{k}(y)$",
   f"conv. 1: bold italic k in 𝒪_y/𝔞_y = k(y) ({B}, p. 102)")
ch(F2, 103,
   "\\begin{corollary}[2.4.6]\n\\label{I.2.4.6-fr}\n\\oldpage[I]{103}\nSoient",
   "\\oldpage[I]{103}\n\\begin{corollary}[2.4.6]\n\\label{I.2.4.6-fr}\nSoient",
   f"rule 4: printed p. 103 begins with 'Corollaire (2.4.6). —'; the marker stood after the heading ({B}, p. 103)")
ch(F2, 103, r"\operatorname{Spec}(k(\psi(\xi)))", r"\operatorname{Spec}(\boldsymbol{k}(\psi(\xi)))",
   f"conv. 1: bold italic k in Spec(k(ψ(ξ))) ({B}, p. 103)")
ch(F2, 103, r"$k(\psi(\xi))\to K$", r"$\boldsymbol{k}(\psi(\xi))\to K$",
   f"conv. 1: bold italic k in k(ψ(ξ)) → K ({B}, p. 103)")
ch(F2, 103, r"$k(y)\to K$", r"$\boldsymbol{k}(y)\to K$",
   f"conv. 1: bold italic k in k(y) → K ({B}, p. 103)")
ch(F2, 103, r"(\hyperref[0.5.4.1-fr]{0, 5.4.1})", r"(\hyperref[0.5.4.1-fr]{\textbf{0}, 5.4.1})",
   f"conv. 2: bold 0 in (𝟎, 5.4.1) ({B}, p. 103)")
ch(F2, 103, r"ou un \emph{$S$-préschéma}~;", r"ou un $S$-préschéma~;",
   f"conv. 6: 'S-préschéma' is in the same italics as the rest of Def. (2.5.1); \\emph inside the italic environment "
   f"set it upright ({B}, p. 103)")
ch(F2, 103, r"\emph{préschéma de base} du", r"préschéma de base du",
   f"conv. 6: 'préschéma de base' is in the same italics as the rest of Def. (2.5.1); \\emph removed ({B}, p. 103)")
ch(F2, 103, r"le \emph{morphisme structural} du", r"le morphisme structural du",
   f"conv. 6: 'morphisme structural' is in the same italics as the rest of Def. (2.5.1); \\emph removed ({B}, p. 103)")
ch(F2, 103, "est un préschéma\nau-dessus de l'anneau $A$", "est un préschéma\n\\textup{au-dessus de l'anneau} $A$",
   f"conv. 6: 'au-dessus de l'anneau' is roman inside the italic Def. (2.5.1) ({B}, p. 103)")
ch(F2, 104,
   "\\begin{env}[2.5.3]\n\\label{I.2.5.3-fr}\n\\oldpage[I]{104}\nSi",
   "\\oldpage[I]{104}\n\\begin{env}[2.5.3]\n\\label{I.2.5.3-fr}\nSi",
   f"rule 4: printed p. 104 begins with '(2.5.3) Si X est un S-préschéma'; the marker stood after the number "
   f"({B}, p. 104)")

# ---------------- ega1-3-fr.tex, p. 104 (lower part) to p. 109 ----------------
ch(F3, 104, r"que l'on note $\bigsqcup_\alpha X_\alpha$.", r"que l'on note $\coprod_\alpha X_\alpha$.",
   f"rule 1 (symbol): the print has the coproduct sign ∐ (an inverted Π) with α below, not a square cup ({B}, p. 104; "
   f"print checked)")
ch(F3, 104, r"$f\mapsto(f\circ\varphi_\alpha)$", r"$f\to(f\circ\varphi_\alpha)$",
   f"conv. 3: the print has a plain arrow f → (f∘φ_α), not ↦ ({B}, p. 104)")
ch(F3, 104, r"se note $X\sqcup Y$.", r"se note $X\amalg Y$.",
   f"rule 1 (symbol): the print has the small coproduct sign ⨿ in X ⨿ Y, not ⊔ ({B}, p. 104; print checked)")
ch(F3, 104, r"$Y=\operatorname{Spec}(B)$, $X\sqcup Y$", r"$Y=\operatorname{Spec}(B)$, $X\amalg Y$",
   f"rule 1 (symbol): small coproduct sign ⨿ in X ⨿ Y, second occurrence ({B}, p. 104; print checked)")
ch(F3, 105, r"$f\mapsto(p_1\circ f,p_2\circ f)$", r"$f\to(p_1\circ f,p_2\circ f)$",
   f"conv. 3: the print has a plain arrow f → (p_1∘f, p_2∘f), not ↦ ({C}, p. 105)")
ch(F3, 105, "$T\\to Y$ (autrement dit, une\nbijection\n\\[", "$T\\to Y$ \\textup{(autrement dit, une\nbijection}\n\\[",
   f"conv. 6: '(autrement dit, une bijection' is roman inside the italic Def. (3.2.1) ({C}, p. 105)")
ch(F3, 105, r"\operatorname{Hom}_S(T,X)\times\operatorname{Hom}_S(T,Y)).",
   r"\operatorname{Hom}_S(T,X)\times\operatorname{Hom}_S(T,Y))",
   f"rule 1 (punctuation): the display of Def. (3.2.1) ends without a period in the print ({C}, p. 105; print checked)")
ch(F3, 105, r"correspondant (\hyperref[I.2.2.4-fr]{2.2.4}) aux", r"correspondant \textup{(\hyperref[I.2.2.4-fr]{2.2.4})} aux",
   f"conv. 6: the reference (2.2.4) is upright inside the italic Prop. (3.2.2) ({C}, p. 105; print checked)")
ch(F3, 105, r"$u:b\mapsto b\otimes1$", r"$u:b\to b\otimes1$",
   f"conv. 3: the print has a plain arrow u : b → b⊗1, not ↦ ({C}, p. 105)")
ch(F3, 105, r"$v:c\mapsto1\otimes c$", r"$v:c\to1\otimes c$",
   f"conv. 3: the print has a plain arrow v : c → 1⊗c, not ↦ ({C}, p. 105)")
ch(F3, 105, r"homomorphismes des $A$-algèbres.}", r"homomorphismes de $A$-algèbres.}",
   f"rule 1 (word): the footnote reads 'homomorphismes de A-algèbres', not 'des' ({C}, p. 105; print checked)")
ch(F3, 105, r"homomorphismes de $A$-algèbres.}", r"homomorphismes de $A$-\emph{algèbres}.}",
   f"rule 1 (italics): 'algèbres' is italic in the footnote ({C}, p. 105; print checked)")
ch(F3, 105, r"(resp. $\beta=({}^a\sigma,\widetilde{\sigma})$)", r"\textup{(resp. $\beta=({}^a\sigma,\widetilde{\sigma})$)}",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.3) ({C}, p. 105; print checked)")
ch(F3, 105, r"(resp. $T\to Y$), où", r"\textup{(resp. $T\to Y$)}, où",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.3) ({C}, p. 105; print checked)")
ch(F3, 105, r"$\rho$ (resp. $\sigma$) est", r"$\rho$ \textup{(resp. $\sigma$)} est",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.3) ({C}, p. 105)")
ch(F3, 105, r"(resp. $C$) dans $D$", r"\textup{(resp. $C$)} dans $D$",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.3) ({C}, p. 105)")
ch(F3, 105, r"un monomorphisme de préschémas (T, I, 1.1), $X$", r"un \textup{monomorphisme} de préschémas (T, I, 1.1), $X$",
   f"conv. 6: 'monomorphisme' is set in roman (emphasis) inside the italic Prop. (3.2.4) ({C}, p. 105; print checked)")
ch(F3, 105, r"de préschémas (T, I, 1.1), $X$, $Y$ deux", r"de préschémas \textup{(T, I, 1.1)}, $X$, $Y$ deux",
   f"conv. 6: the reference (T, I, 1.1) is upright inside the italic Prop. (3.2.4) ({C}, p. 105)")
ch(F3, 106, r"f(T)\subset p^{-1}(U)\cap q^{-1}(V)=W,", r"f(T)\subset p^{-1}(U)\cap q^{-1}(V)=W",
   f"rule 1 (punctuation): no comma after the display f(T) ⊂ p⁻¹(U) ∩ q⁻¹(V) = W in the print ({C}, p. 106)")
ch(F3, 106, "$f_{\\alpha\\lambda}$ et\n$f_{\\beta\\mu}$ à", "$f_{\\alpha\\lambda}$ et de\n$f_{\\beta\\mu}$ à",
   f"rule 1 (missing word): the print reads 'les restrictions de f_αλ et de f_βμ' ({C}, p. 106; print checked)")
ch(F3, 106, "   q^{-1}(V_\\lambda\\cap V_\\mu),\n\\]", "   q^{-1}(V_\\lambda\\cap V_\\mu)\n\\]",
   f"rule 1 (punctuation): no comma after the display W_αλ ∩ W_βμ = ... in the print ({C}, p. 106)")
ch(F3, 106, "constituent un produit de\n$U_\\alpha\\cap U_\\beta$", "constituent un \\emph{produit} de\n$U_\\alpha\\cap U_\\beta$",
   f"rule 1 (italics): 'produit' is italic in the print ({C}, p. 106)")
ch(F3, 107, r"$V_\lambda\cap V_\mu\cap V_\nu$, dans $U_\beta$", r"$V_\lambda\cap V_\mu\cap V_\nu$ dans $U_\beta$",
   f"rule 1 (punctuation): no comma before 'dans U_β et V_μ respectivement' in the print ({C}, p. 107; print checked)")
ch(F3, 107, r"\subset S_i\cap S_j$, d'après la définition", r"\subset S_i\cap S_j$ d'après la définition",
   f"rule 1 (punctuation): no comma before 'd'après la définition' in the print ({C}, p. 107; print checked)")
ch(F3, 108, r"$\varphi$ (resp. $\psi$) le morphisme", r"$\varphi$ \textup{(resp. $\psi$)} le morphisme",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.7) ({C}, p. 108; print checked)")
ch(F3, 108, r"structural de $X$ (resp. $Y$). Soient", r"structural de $X$ \textup{(resp. $Y$)}. Soient",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.7) ({C}, p. 108)")
ch(F3, 108, "$U$\n(resp. $V$) une partie", "$U$\n\\textup{(resp. $V$)} une partie",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.7) ({C}, p. 108)")
ch(F3, 108, r"de $X$ (resp. $Y$) contenue dans", r"de $X$ \textup{(resp. $Y$)} contenue dans",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.7) ({C}, p. 108)")
ch(F3, 108, r"(resp. $\psi^{-1}(S')$). Alors", r"\textup{(resp. $\psi^{-1}(S')$)}. Alors",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Cor. (3.2.7) ({C}, p. 108)")
ch(F3, 108, r"la première (resp. seconde) projection", r"la première \textup{(resp.} seconde) projection",
   f"conv. 6: '(resp.' is roman inside the italic Prop. (3.3.3); 'seconde)' italic, closing parenthesis included "
   f"({C}, p. 108; print checked)")
ch(F3, 108, r"$X\times_S S$ (resp. $S\times_S X$) est un isomorphisme",
   r"$X\times_S S$ \textup{(resp. $S\times_S X$)} est un isomorphisme",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Prop. (3.3.3) ({C}, p. 108)")
ch(F3, 108, r"$X\times_S S$ (resp. $S\times_S X$) sur $X$", r"$X\times_S S$ \textup{(resp. $S\times_S X$)} sur $X$",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Prop. (3.3.3) ({C}, p. 108)")
ch(F3, 108, r"(resp. $(\varphi,1_X)_S$), en désignant", r"\textup{(resp. $(\varphi,1_X)_S$)}, en désignant",
   f"conv. 6: '(resp.' and the closing parenthesis are roman inside the italic Prop. (3.3.3) ({C}, p. 108)")
ch(F3, 109, r"(X_1\times_S X_2\times_S\cdots\times_S X_{n-1})", r"(X_1\times_S X_2\times\cdots\times_S X_{n-1})",
   f"rule 1 (formula): the product sign after X_2 has no subscript S in the print ({C}, p. 109; print checked)")
ch(F3, 109, r"$X_1\times_S X_2\times_S X_3$", r"$X_1\times X_2\times X_3$",
   f"rule 1 (formula): the print writes X_1 × X_2 × X_3 without subscript S ({C}, p. 109; print checked)")
ch(F3, 109, r"$(X_1\times_S X_2)\times_S X_3$", r"$(X_1\times X_2)\times X_3$",
   f"rule 1 (formula): the print writes (X_1 × X_2) × X_3 without subscript S ({C}, p. 109; print checked)")
ch(F3, 109, r"la projection dans $X_1\times_S X_2$ est", r"la projection dans $X_1\times X_2$ est",
   f"rule 1 (formula): the print writes X_1 × X_2 without subscript S ({C}, p. 109; print checked)")
ch(F3, 109, "dans $X$ et $S'$,\nrespectivement.", "dans $X$ et $S'$\nrespectivement.",
   f"rule 1 (punctuation): no comma before 'respectivement' in the print ({C}, p. 109)")
ch(F3, 109, r"X_{(S')}\to Y_{(S')}$, et on dit", r"X_{(S')}\to Y_{(S)}$, et on dit",
   f"rule 3 (misprint kept in the diplomatic text): the print has the target Y_(S); the TeX had silently corrected it to "
   f"Y_(S'); printed reading restored, correction recorded in MISPRINTS_098_109.json ({C}, p. 109; print checked; "
   f"errata EGA III, (I, 3.3.7))")

ERR3 = "errata EGA III (ega3/ega3-7-fr.tex, Errata et Addenda)"
misprints = [
    dict(page=98,
         where="proof of Prop. (2.1.5), last sentence: 'L'unicité du point générique de X résulte de (2.1.4) et de "
               "(0, 2.1.3)'",
         print="L'unicité du point générique de $X$",
         correct="L'unicité du point générique de $Y$ (Y is the irreducible closed part whose generic point the proof "
                 "has just constructed; X itself need not be irreducible)",
         tex_did="keeps the printed reading",
         source="noticed during this fix pass (print checked); not in the scan findings and not in the authors' errata "
                "lists (EGA II list 1, EGA III list 2)",
         confidence="medium",
         note="Possibly loose wording rather than a misprint; check before correcting."),
    dict(page=101,
         where="(2.3.1): 'obtenu par recollement de préschémas (0, 4.1.6)'",
         print="(\\textbf{0}, 4.1.6)",
         correct="(\\textbf{0}, 4.1.7) (link target 0.4.1.7-fr)",
         tex_did="keeps the printed reading (\\hyperref[0.4.1.6-fr]; bold 0 added in this pass, convention 2)",
         source=ERR3 + ": '(I, 2.3.1) Ligne 3 du bas de la p. 101, remplacer (0, 4.1.6) par (0, 4.1.7)'; not among the "
                "scan findings",
         note="The reference stands on line 3 from the top of p. 101 (the erratum says 'du bas'); it is the only "
              "reference to (0, 4.1.6) on the page."),
    dict(page=101,
         where="Exemple (2.3.2): 'Soit u_12 l'isomorphisme de préschémas U_21 → U_12 correspondant (2.2.4) à "
               "l'isomorphisme de B sur C qui, à f(s)/s^m fait correspondre ...'",
         print="l'isomorphisme de $B$ sur $C$",
         correct="l'isomorphisme de $B_s$ sur $C_t$",
         tex_did="had silently corrected it to '$B_s$ sur $C_t$'; changed back to the printed '$B$ sur $C$' in this pass",
         source="findings_100_104.json (p. 101); " + ERR3 + ": '(I, 2.3.2) Ligne 11 de la p. 101, remplacer B par B_s "
                "et C par C_t'"),
    dict(page=104,
         where="(2.5.4), first sentence: 'pour tout S'-préschéma, le morphisme composé X → S' → S définit X comme "
               "S-préschéma'",
         print="pour tout $S'$-préschéma, le morphisme composé $X\\to S'\\to S$",
         correct="pour tout $S'$-préschéma $X$, le morphisme composé $X\\to S'\\to S$",
         tex_did="keeps the printed reading",
         source="findings_100_104.json (p. 104); not in the authors' errata lists",
         confidence="low",
         note="X is used without being named; this may be the authors' elliptical wording rather than a misprint."),
    dict(page=104,
         where="(2.5.5): 'Si X est un S-morphisme, φ : X → S le morphisme structural'",
         print="Si $X$ est un $S$-morphisme",
         correct="Si $X$ est un $S$-préschéma",
         tex_did="keeps the printed reading",
         source="findings_100_104.json (p. 104); " + ERR3 + ": '(I, 2.5.5) Ligne 19 de la p. 104, remplacer "
                "S-morphisme par S-préschéma'"),
    dict(page=109,
         where="(3.3.7): 'on note encore f_(S') le S'-morphisme f ×_S 1 : X_(S') → Y_(S)'",
         print="$f\\times_S 1:X_{(S')}\\to Y_{(S)}$",
         correct="$f\\times_S 1:X_{(S')}\\to Y_{(S')}$",
         tex_did="had silently corrected it to $Y_{(S')}$; changed back to the printed $Y_{(S)}$ in this pass",
         source="findings_105_109.json (p. 109); " + ERR3 + ": '(I, 3.3.7) Ligne 17 de la p. 109, remplacer Y_(S) par "
                "Y_(S')'"),
    dict(page=109,
         where="(3.3.8), end: 'comme il résulte de la définition du produit appliquée aux S-morphismes f et "
               "ψ : T → S' (morphisme structural de T)'",
         print="appliquée aux $S$-morphismes $f$ et $\\psi:T\\to S'$",
         correct="appliquée aux $S$-morphismes $g$ et $\\psi:T\\to S'$",
         tex_did="keeps the printed reading",
         source="findings_105_109.json (p. 109); not in the authors' errata lists",
         note="The definition of the product X ×_S S' is applied to the given pair g : T → X, ψ : T → S'; f is the "
              "S'-morphism it produces."),
]

# ---------------- checks: replay the log on the unedited text and compare with the edited files ----------------
# The unedited section text is embedded unchanged in the release's assembled reader (same release, not edited here).
READER = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/direct/EGA_I_III_French_Base_Reader.tex"
lines = READER.read_text(encoding="utf-8").split("\n")
orig = {F2: "\n".join(lines[8026:8618]) + "\n", F3: "\n".join(lines[8623:9905]) + "\n"}
assert orig[F2].startswith("\\section{Préschémas et morphismes de préschémas}")
assert orig[F3].startswith("\\section{Produit de préschémas}")
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def page_span(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    starts = [s for n, s in cuts if n == page]
    if not starts:  # p. 104 continues at the top of ega1-3-fr.tex, before \oldpage[I]{105}
        nxt = [s for n, s in cuts if n == page + 1]
        return (0, nxt[0]) if nxt else None
    s = starts[0]
    later = [p for n, p in cuts if p > s]
    return s, (later[0] if later else len(t))


problems = 0
replay = dict(orig)
for c in changes:
    t = replay[c["file"]]
    if t.count(c["old"]) != 1:
        print("old string occurs", t.count(c["old"]), "times:", c["page"], repr(c["old"][:60])); problems += 1; continue
    pos = t.index(c["old"])
    if "\\oldpage" not in c["old"]:  # a moved marker starts on the previous page by construction
        span = page_span(t, c["page"])
        if span is None or not (span[0] <= pos < span[1]):
            print("old string not on its page:", c["page"], repr(c["old"][:60])); problems += 1
    replay[c["file"]] = t.replace(c["old"], c["new"], 1)
for f in (F2, F3):
    if replay[f] != (E / f).read_text(encoding="utf-8"):
        print("replayed log does not reproduce", f); problems += 1
for f, n in ((F2, 101), (F2, 102), (F2, 103), (F2, 104)):
    t = replay[f]
    after = t[t.index("\\oldpage[I]{%d}" % n):][:60]
    print("marker", n, "->", repr(after))
print(len(changes), "changes,", problems, "problems,", len(misprints), "misprints")
if problems == 0:
    with open(E / "FIXLOG_098_109.jsonl", "w", encoding="utf-8", newline="\n") as fh:
        for c in changes:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    (E / "MISPRINTS_098_109.json").write_text(json.dumps(misprints, ensure_ascii=False, indent=1) + "\n",
                                              encoding="utf-8", newline="\n")
    print("written")
