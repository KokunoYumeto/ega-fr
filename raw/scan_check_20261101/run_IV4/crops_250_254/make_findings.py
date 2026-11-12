# Builds findings_250_254.json and checks every "old" against the page files and the current source.
import io
import json
import os

BASE = os.path.join("C:" + os.sep, "user", "Documents", "ega_scan_check_20261101")
RUN = os.path.join(BASE, "run_IV4")
SRC = os.path.join(BASE, "ega-fr", "editions", "2026-10-24-r20", "diplomatic", "packages", "IV4",
                   "native", "ega4", "ega4-20-fr.tex")
OUT = os.path.join(RUN, "findings_250_254.json")

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 250 ----------------
add(250, "Proposition (20.5.3) (i), l. 1: 'et identifie Ps.hom_X/S(X, Y), au sous-ensemble'",
    "comma after Ps.hom_X/S(X, Y) (crop p250_identifie.png)",
    "no comma", "punctuation", None, "high",
    r"identifie $\operatorname{Ps.hom}_{X/S}(X,Y)$ au sous-ensemble",
    r"identifie $\operatorname{Ps.hom}_{X/S}(X,Y)$, au sous-ensemble",
    "Grammatically superfluous, but a comma after a formula is not clearly an error; recorded as the print's punctuation, not as a misprint.")

add(250, "Proposition (20.5.3) (ii): 'Le préfaisceau U ⇝ Ps.hom_U/S(U, Y) sur X'",
    "wavy arrow (crop p250_ii.png)", r"\mapsto", "symbol", None, "high",
    r"Le préfaisceau $U\mapsto", r"Le préfaisceau $U\leadsto")

add(250, "proof of (20.5.3): 'notons que U ⇝ Ps.hom_S(U, Y) est alors un faisceau'",
    "wavy arrow", r"\mapsto", "symbol", None, "high",
    r"notons que $U\mapsto", r"notons que $U\leadsto")

add(250, "after the proof: 'on notera 𝒫s.hom_X/S(X, Y) le sous-faisceau'",
    "script P followed by italic 's.hom' (crop p250_Pshom.png)",
    r"\mathscr{P}\!s.\!\operatorname{hom}: upright 'hom'", "font", None, "high",
    r"on notera $\mathscr{P}\!s.\!\operatorname{hom}_{X/S}(X,Y)$",
    r"on notera $\mathscr{P}\!s.\mathit{hom}_{X/S}(X,Y)$",
    r"Form \mathscr{P}\!s.\mathit{hom} as the coordinator asked (GLOBAL_ISSUES 107).")

add(250, "display after 'le sous-faisceau': 'U ⇝ Ps.hom_U/S(U, Y)'",
    "wavy arrow", r"\mapsto", "symbol", None, "high",
    "  U\\mapsto\\operatorname{Ps.hom}_{U/S}(U,Y)\n\\]",
    "  U\\leadsto\\operatorname{Ps.hom}_{U/S}(U,Y)\n\\]")

add(250, "after the display: 'de 𝒫s.hom_S(X, Y).'",
    "script P followed by italic 's.hom' (crop p250_Pshom2.png)",
    r"\mathscr{P}\!s.\!\operatorname{hom}: upright 'hom'", "font", None, "high",
    "\\]\nde $\\mathscr{P}\\!s.\\!\\operatorname{hom}_S(X,Y)$.",
    "\\]\nde $\\mathscr{P}\\!s.\\mathit{hom}_S(X,Y)$.")

add(250, "paragraph before (20.5.4): 'dom_S(ω) ∩ X_s soit schématiquement dense dans X_s (11.10.10)'",
    "'schématiquement dense dans' italic, 'dans' included (crop p250_densedans.png)",
    r"\emph{schématiquement dense} dans: 'dans' roman", "italics", None, "high",
    r"\emph{schématiquement dense} dans $X_s$", r"\emph{schématiquement dense dans} $X_s$")

add(250, "(20.5.4), end: 'Le faisceau 𝒫s.hom_X/S(X, Y) est un sous-faisceau d'anneaux'",
    "script P followed by italic 's.hom'",
    r"\mathscr{P}\!s.\!\operatorname{hom}: upright 'hom'", "font", None, "high",
    r"Le faisceau $\mathscr{P}\!s.\!\operatorname{hom}_{X/S}(X,Y)$",
    r"Le faisceau $\mathscr{P}\!s.\mathit{hom}_{X/S}(X,Y)$")

# ---------------- page 252 ----------------
add(252, "heading 20.6: 'Fonctions méromorphes relatives.'",
    "full stop after the title (crop p252_title.png)", "no full stop", "punctuation", None, "high",
    r"\subsection{Fonctions méromorphes relatives}",
    r"\subsection{Fonctions méromorphes relatives.}",
    "GLOBAL_ISSUES 43/58; same form as the earlier IV-4 subsection-title page fixes (e.g. 'Composition des pseudo-morphismes.').")

add(252, "(20.6.1): 'par l'équivalence de a) et b) dans (11.3.7)'",
    "labels a) and b) wholly italic (crop p252_ab.png)", "roman 'a)', 'b)'", "italics", None, "high",
    r"l'équivalence de a) et b) dans", r"l'équivalence de \emph{a)} et \emph{b)} dans",
    "GLOBAL_ISSUES 88 (roman running text: whole label italic).")

add(252, "(20.6.1): 'Il est clair que U ⇝ T_X/S(U) est un sous-faisceau'",
    "wavy arrow", r"\mapsto", "symbol", None, "high",
    r"$U\mapsto T_{X/S}(U)$", r"$U\leadsto T_{X/S}(U)$")

add(252, "(20.6.2), after (20.6.2.1): 'leur ensemble est noté M(X/S, F)'",
    "roman F (crop p252_MXSF.png), where (20.1.3) has M(X, 𝓕) with the script 𝓕",
    "M(X/S,F): keeps the printed roman F", "misprint_in_print", None, "high",
    None, None,
    "Wrong letter in the print: the set of meromorphic sections of the sheaf 𝓕, whose notation in (20.1.3) is M(X, 𝓕) with the script 𝓕 (checked on the p. 227 scan). The TeX keeps the printed reading; no diplomatic fix. Not in Err_IV.",
    corrected=r"$M(X/S,\sh{F})$")

add(252, "(20.6.2): 't est (𝓕|U)-régulière;'",
    "'régulière' italic (crop p252_FUreg.png)", "roman 'régulière'", "italics", None, "high",
    r"$(\sh{F}|U)$-régulière", r"$(\sh{F}|U)$-\emph{régulière}")

add(252, "Proposition (20.6.3), l. 3: 'relatives à S (i.e. des pseudo-fonctions'",
    "'(i.e.' upright, 'des' italic (crop p252_ie.png)",
    "'(i.e.' italic (statement environment)", "convention", 6, "high",
    r"(i.e.\ des pseudo-fonctions", r"\textup{(i.e.}\ des pseudo-fonctions",
    "GLOBAL_ISSUES 101: the parenthesis is upright where roman words or a reference stand next to it.")

add(252, "Proposition (20.6.3), end: '... relativement à S (20.5.4)).'",
    "the closing parenthesis after the reference upright (crop p252_endparen.png)",
    "closing parenthesis italic (statement environment)", "convention", 6, "high",
    r"\sref{IV.20.5.4}).", r"\sref{IV.20.5.4}\textup{)}.",
    "Closes the '(i.e.' of the previous finding; does not overlap it.")

# ---------------- page 253 ----------------
add(253, "proof of (20.6.4): 'dont l'espace sous-jacent est X—dom(φ)'",
    "long dash", "minus sign", "convention", 7, "high",
    r"est $X-\operatorname{dom}(\varphi)$.", r"est $X\setmin\operatorname{dom}(\varphi)$.")

add(253, "proof of (20.6.4): '𝒪_X_s,x = 𝒪_X,x ⊗_𝒪S,s k(s)'",
    "bold italic k (crop p253_ks.png)", "plain k", "convention", 1, "high",
    r"\otimes_{\sh{O}_{S,s}}k(s)$", r"\otimes_{\sh{O}_{S,s}}\boldsymbol{k}(s)$")

add(253, "proof of (20.6.4): 'et est par suite régulière dans cet anneau noethérien'",
    "'régulière' italic (crop p253_regul.png)", "roman", "italics", None, "high",
    r"par suite régulière dans", r"par suite \emph{régulière} dans")

add(253, "Remarques (20.6.5) (i): 'φ = π/T est une fonction méromorphe sur S relative à S'",
    "'sur S' (crop p253_surS.png)", "'sur $S$': keeps the printed reading", "misprint_in_print", None, "high",
    None, None,
    "φ = π/T is a meromorphic function on X = S[T] (the remark is about functions on X: dom(φ) = D(T) in X); 'sur S' is a slip for 'sur X'. The TeX keeps the printed reading; no diplomatic fix. Not in Err_IV.",
    corrected=r"une fonction méromorphe sur $X$ relative à $S$")

add(253, "Remarques (20.6.5) (i): 'T est régulier dans Γ(X_a, 𝒪_X_a) = k[T]'",
    "'régulier' (masculine) (crop p253_regulier.png)", "'régulière'", "word", None, "high",
    r"$T$ est régulière dans", r"$T$ est régulier dans",
    "Rewording by the TeX (not a misprint: T as an element).")

# ---------------- page 254 ----------------
add(254, "Remarques (20.6.5) (ii), second paragraph: 'φ ∈ M(X/S) peut être inversible dans M(X)'",
    "'dans' italic (crop p254_dans.png)", "roman", "italics", None, "high",
    r"peut être inversible dans $M(X)$", r"peut être inversible \emph{dans} $M(X)$",
    "Remark body judged as roman (document-wide remark font).")

add(254, "Remarques (20.6.5) (iii): 'un élément de Γ(U, 𝓜_X) qui est régulière relative à S'",
    "'régulière relative à' (crop p254_relative.png)", "'régulière relativement à'", "word", None, "high",
    r"qui est \emph{régulière relativement à $S$}", r"qui est \emph{régulière relative à $S$}",
    "Rewording by the TeX; the print has 'relative' here (as in 'φ' est alors aussi régulière relative à S' below).")

add(254, "Remarques (20.6.5) (iii): '𝓛_s = 𝓛 ⊗_𝒪X k(s)'",
    "bold italic k (crop p254_ks.png)", "plain k", "convention", 1, "high",
    r"\otimes_{\sh{O}_X}k(s)$", r"\otimes_{\sh{O}_X}\boldsymbol{k}(s)$")

add(254, "proof of (20.6.6): 'si l'on pose Z = X—dom(φ)'",
    "long dash", "minus sign", "convention", 7, "high",
    r"$Z=X-\operatorname{dom}(\varphi)$", r"$Z=X\setmin\operatorname{dom}(\varphi)$")

add(254, "(20.6.7): 'il est immédiat que U ⇝ T_f(U) est un sous-faisceau'",
    "wavy arrow", r"\mapsto", "symbol", None, "high",
    r"$U\mapsto T_f(U)$", r"$U\leadsto T_f(U)$")

add(254, "(20.6.7): 'c'est un sous-faisceau d'anneaux de 𝓜_X/S, et on déduit canoniquement de θ♯'",
    "'et on déduit canoniquement' (crop p254_deduit.png)", "'et on en déduit canoniquement'", "extra", None, "high",
    r"et on en déduit canoniquement", r"et on déduit canoniquement",
    "Word 'en' added by the TeX. Does not overlap the next finding.")

add(254, "(20.6.7): 'θ♯ : ψ*(𝒪_X) → 𝒪_X′'",
    "sharp sign ♯ (crop p254_deduit.png)", r"^\#", "convention", 9, "high",
    r"$\theta^\#: \psi^*(\sh{O}_X)", r"$\theta^\sharp: \psi^*(\sh{O}_X)")

add(254, "(20.6.7): 'θ′♯ : ψ*(𝓜_X/S,f) → 𝓜_X′/S'",
    "sharp sign ♯", r"'^\#", "convention", 9, "high",
    r"$\theta'^\#: \psi^*(\sh{M}_{X/S,f})", r"$\theta'^\sharp: \psi^*(\sh{M}_{X/S,f})")

add(254, "(20.6.7): 'prolongeant θ♯.'",
    "sharp sign ♯", r"^\#", "convention", 9, "high",
    "prolongeant $\\theta^\\#$.\nSi une", "prolongeant $\\theta^\\sharp$.\nSi une")

add(254, "(20.6.7): 'Γ(θ′♯)(φ) est une fonction méromorphe sur X′'",
    "sharp sign ♯", r"'^\#", "convention", 9, "high",
    r"$\Gamma(\theta'^\#)(\varphi)$", r"$\Gamma(\theta'^\sharp)(\varphi)$")

add(254, "Proposition (20.6.8), l. 2: 'est plat, on a'",
    "'plat' italic like the rest of the statement (crop p254_plat.png)",
    r"\emph{plat} inside the italic environment comes out upright", "convention", 6, "high",
    r"est \emph{plat}, on a", r"est plat, on a",
    r"\emph dropped where the print shows no change of face (FIX_POLICY 2.6). Does not overlap the next finding.")

add(254, "Proposition (20.6.8): 'l'homomorphisme φ ⇝ φ∘f est défini dans M(X/S)'",
    "wavy arrow (crop p254_plat.png)", r"\mapsto", "symbol", None, "high",
    r"$\varphi\mapsto\varphi\circ f$ est défini dans $M(X/S)$",
    r"$\varphi\leadsto\varphi\circ f$ est défini dans $M(X/S)$")

# ---------------- checks ----------------
src = io.open(SRC, encoding="utf-8", newline="").read()
assert "\r" not in src
ok = True
for d in F:
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    pg = io.open(os.path.join(RUN, "page_%d.tex" % d["page"]), encoding="utf-8", newline="").read()
    pg = pg.replace("\r\n", "\n")
    n_pg = pg.count(old)
    n_src = src.count(old)
    if n_pg != 1 or n_src != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n_pg, n_src, repr(old))
    if d["fix"]["new"] == old:
        ok = False
        print("NO CHANGE", repr(old))
# apply all fixes in order to a copy of the source and check each applies once, in sequence
s2 = src
for d in F:
    if d["fix"] is None:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    c = s2.count(old)
    if c != 1:
        ok = False
        print("SEQUENTIAL NOT UNIQUE", d["page"], c, repr(old))
    s2 = s2.replace(old, new, 1)
with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(250, 255):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("ALL OK" if ok else "PROBLEMS", len(F))
