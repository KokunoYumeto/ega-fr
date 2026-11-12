# Builds findings_165_169.json; in the strings below the pilcrow stands for a line break (LF).
import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_165_169.json')
NL = '¶'

def f(page, where, scan, tex, kind, conv, conf, old=None, new=None, note='', corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": (None if old is None else {"old": old.replace(NL, '\n'), "new": new.replace(NL, '\n')})}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    return d

F = []

# ---------------- p. 165 ----------------
F.append(f(165, "proof of (11.9.10), l. 5-6: 'Soit v_λ = Hom(1, u_λ) : Hom_A(A/𝔍_{i-1}, M) → Hom_A(A/𝔍_{i-1}, N_λ) l'homomorphisme déduit de u_λ'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"Soit¶  \[¶  v_\lambda=\operatorname{Hom}(1,u_\lambda):¶  \operatorname{Hom}_A(A/\mathfrak J_{i-1},M)\longrightarrow¶  \operatorname{Hom}_A(A/\mathfrak J_{i-1},N_\lambda)¶  \]¶  l'homomorphisme",
    r"Soit¶  $v_\lambda=\operatorname{Hom}(1,u_\lambda):¶  \operatorname{Hom}_A(A/\mathfrak J_{i-1},M)\longrightarrow¶  \operatorname{Hom}_A(A/\mathfrak J_{i-1},N_\lambda)$¶  l'homomorphisme",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."))
F.append(f(165, "same proof, l. 7: 'on a (Hom_A(A/𝔍_{i-1}, M))_t = Hom_{A_t}(A_t/(𝔍_{i-1})_t, M_t) et de même en remplaçant M par N_λ'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"on a¶  \[¶  (\operatorname{Hom}_A(A/\mathfrak J_{i-1},M))_t¶  =\operatorname{Hom}_{A_t}(A_t/(\mathfrak J_{i-1})_t,M_t)¶  \]¶  et de même",
    r"on a¶  $(\operatorname{Hom}_A(A/\mathfrak J_{i-1},M))_t¶  =\operatorname{Hom}_{A_t}(A_t/(\mathfrak J_{i-1})_t,M_t)$¶  et de même",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."))
F.append(f(165, "same proof, l. 14: 'tel que A'_s soit un A_s-module libre.'",
    "'libre' in italics (enlarged crop p165_s2_libre.png)", "'libre' upright", "italics", None, "high",
    r"$A_s$-module libre.", r"$A_s$-module \emph{libre}."))
F.append(f(165, "same proof, l. 15: 'Or la famille des (u_λ)_s : M_s → (N_λ)_s est séparante par hypothèse'",
    "'séparante' in italics (same crop)", "'séparante' upright", "italics", None, "high",
    r"est séparante par hypothèse", r"est \emph{séparante} par hypothèse"))
F.append(f(165, "Remarque (11.9.11), l. 5-6: 'pour tout point fermé x de X, et tout entier n ⩾ 0, 𝔪_x^n𝓕 est un 𝒪_X-Module cohérent de support contenu dans {x}'",
    "𝔪_x^n𝓕 est un 𝒪_X-Module cohérent de support contenu dans {x} (enlarged crop p165_s2_mxF.png)",
    "$\\mathfrak m_x^n\\mathcal F$ est un ... (the printed reading)", "misprint_in_print", None, "high",
    note="The TeX keeps the printed reading. 𝔪_x^n𝓕 coincides with 𝓕 outside x, so its support is not contained in {x}; the quotient 𝓕/𝔪_x^n𝓕, target of the canonical maps of the next sentence, is meant. The corrected edition (r20 current, ega4-11-fr.tex) already reads $\\mathcal F/\\mathfrak m_x^n\\mathcal F$.",
    corrected=r"\mathcal F/\mathfrak m_x^n\mathcal F"))
F.append(f(165, "Lemme (11.9.12), l. 1: 'Les notations étant celles de (11.9.1) et (11.9.5)'",
    "(11.9.1) upright in the italic statement", "plain text in the italic lemma environment: italic", "convention", 6, "high",
    r"celles de (11.9.1)", r"celles de \textup{(11.9.1)}"))
F.append(f(165, "Lemme (11.9.12), l. 1: same sentence, '(11.9.5)'",
    "(11.9.5) upright in the italic statement", "italic", "convention", 6, "high",
    r"(11.9.5), supposons la famille", r"\textup{(11.9.5)}, supposons la famille"))
F.append(f(165, "Lemme (11.9.12), l. 4: 'supposons enfin que les 𝓖_λ soient S-plats.'",
    "'plats' set in roman inside the italic statement (enlarged crop p165_s3_splats.png)",
    "$S$-plats inside the italic lemma environment: italic", "convention", 6, "high",
    r"$S$-plats.", r"$S$-\textup{plats}.",
    "In the statements (11.9.15) and (11.9.16), p. 167, 'plats' is italic, as the TeX gives it."))

# ---------------- p. 166 ----------------
F.append(f(166, "proof of (11.9.12), l. 4: 'Quitte à remplacer S, X, ... par S''_α, U''_α, f''^{-1}_{αλ}(U''_α) et les restrictions'",
    "f''^{-1}_{αλ}(U''_α): no parentheses around f''_{αλ}; primes and exponent -1 together over the subscript αλ (enlarged crop p166_s1_quitte.png)",
    "$(f''_{\\alpha\\lambda})^{-1}(U''_\\alpha)$", "formula", None, "high",
    r"$(f''_{\alpha\lambda})^{-1}(U''_\alpha)$", r"$f^{\prime\prime-1}_{\alpha\lambda}(U''_\alpha)$",
    "f''^{-1} would be a double superscript; written with \\prime\\prime-1 as earlier fixes write f^{\\prime-1}."))
F.append(f(166, "same proof, l. 8: 'l'homomorphisme 𝒪_S → p_*(𝒪_{S'}) intervenant dans la définition de p est injectif.'",
    "'injectif' in italics (enlarged crop p166_s1_quitte.png; the earlier 'A → A' est injectif' is roman)",
    "'injectif' upright", "italics", None, "high",
    r"est injectif. Il en résulte", r"est \emph{injectif}. Il en résulte"))
F.append(f(166, "same proof, l. 11: 'ρ : 𝓖_λ → (g'_λ)_*(𝓖'_λ) est lui aussi injectif.'",
    "'injectif' in italics (enlarged crop p166_s2_inj.png)", "'injectif' upright", "italics", None, "high",
    r"injectif. Mais", r"\emph{injectif}. Mais"))
F.append(f(166, "Proposition (11.9.13), l. 1: 'Les notations étant celles de (11.9.1) et (11.9.5)'",
    "(11.9.1) upright in the italic statement", "plain text in the italic proposition environment: italic", "convention", 6, "high",
    r"celles de (11.9.1)", r"celles de \textup{(11.9.1)}"))
F.append(f(166, "Proposition (11.9.13), l. 1: same sentence, '(11.9.5)'",
    "(11.9.5) upright in the italic statement", "italic", "convention", 6, "high",
    r"(11.9.5), supposons que", r"\textup{(11.9.5)}, supposons que"))
F.append(f(166, "proof of (11.9.13), l. 3: 'les conditions d'application de (11.9.10, (ii), b))'",
    "'b)' in italics (enlarged crop p166_s3_b.png)", "'b)' upright", "italics", None, "high",
    r"(11.9.10, (ii), b)). Dans", r"(11.9.10, (ii), \emph{b)}). Dans"))
F.append(f(166, "proof of (11.9.13), l. 5: 'le résultat de (11.9.10, (ii), b));'",
    "'b)' in italics (same crop)", "'b)' upright", "italics", None, "high",
    r"(11.9.10, (ii), b))~;", r"(11.9.10, (ii), \emph{b)})~;"))
F.append(f(166, "(11.9.14), l. 2-3: 'où S' → S est un morphisme quelconque, la famille (u'_λ) correspondante'",
    "'quelconque' in italics (enlarged crop p166_s3_quelc.png)", "'quelconque' upright", "italics", None, "high",
    r"un morphisme quelconque, la famille", r"un morphisme \emph{quelconque}, la famille"))

# ---------------- p. 167 ----------------
F.append(f(167, "Proposition (11.9.15), l. 3: 'un Idéal quasi-cohérent nilpotent 𝒥 de 𝒪_s, tel que les (𝒪_S/𝒥)-Modules'",
    "𝒪_s with a lower-case italic s (enlarged crops p167_s1_Os.png, p167_s1_Os_zoom.png); the next (𝒪_S/𝒥) has the capital S",
    "$\\mathcal O_S$ (silent correction)", "misprint_in_print", None, "high",
    r"$\mathcal J$ de $\mathcal O_S$,", r"$\mathcal J$ de $\mathcal O_s$,",
    "Wrong letter in the print: 𝒥 is an Ideal of 𝒪_S (no point s occurs here). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"\mathcal O_S"))
F.append(f(167, "Proposition (11.9.15), l. 1: 'Les notations étant celles de (11.9.1), supposons que X soit un S-préschéma'",
    "(11.9.1) upright in the italic statement", "plain text in the italic proposition environment: italic", "convention", 6, "high",
    r"(11.9.1), supposons que $X$ soit un¶$S$-préschéma, les", r"\textup{(11.9.1)}, supposons que $X$ soit un¶$S$-préschéma, les"))
F.append(f(167, "Proposition (11.9.15), l. 5: 'est séparante (resp. universellement séparante relativement à S_0), la famille'",
    "'(resp.' and the closing parenthesis upright; 'universellement séparante relativement à' italic (enlarged crop p167_s1_prop.png)",
    "'(resp.' and ')' italic in the italic environment", "convention", 6, "high",
    r"séparante (resp. universellement séparante relativement à $S_0$)", r"séparante \textup{(resp.} universellement séparante relativement à $S_0$\textup{)}"))
F.append(f(167, "Proposition (11.9.15), l. 6: 'la famille (u_λ) est séparante (resp. universellement séparante relativement à S).'",
    "'(resp.' and the closing parenthesis upright (same crop)", "italic", "convention", 6, "high",
    r"séparante (resp. universellement séparante relativement à¶$S$).", r"séparante \textup{(resp.} universellement séparante relativement à¶$S$\textup{)}."))
F.append(f(167, "proof of (11.9.15), l. 2-3: 'un idéal quasi-cohérent nilpotent 𝒥' de 𝒪_{S'} tel que 𝒥'^k/𝒥'^{k+1} soit'",
    "no comma after 𝒪_{S'} (enlarged crop p167_s2_OS_zoom.png)", "'$\\mathcal O_{S'}$, tel que' (comma)", "punctuation", None, "high",
    r"de $\mathcal O_{S'}$, tel que", r"de $\mathcal O_{S'}$ tel que"))
F.append(f(167, "proof of (11.9.15), l. 17-18: 'on peut donc écrire t = Σ_α e_α t^0_α, avec t^0_α ∈ A/𝔍, nul sauf pour un nombre fini d'indices'",
    "t^0_α ∈ A/𝔍 (enlarged crop p167_s3_t0.png)", "$t^0_\\alpha\\in M/\\mathfrak JM$ (silent correction)", "misprint_in_print", None, "high",
    r"$t^0_\alpha\in M/\mathfrak JM$", r"$t^0_\alpha\in A/\mathfrak J$",
    "t lies in 𝔍^nM, which is 𝔍^n ⊗_{A/𝔍} (M/𝔍M), and the next lines apply u_{λ0} : M/𝔍M → N_λ/𝔍N_λ to the t^0_α, so t^0_α ∈ M/𝔍M is meant. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"t^0_\alpha\in M/\mathfrak JM"))
F.append(f(167, "proof of (11.9.15), l. 19-20: 'et l'on peut par suite écrire u_λ(t) = Σ_α e_α u_{λ0}(t^0_α) = Σ_α e_α ⊗ u_{λ0}(t^0_α).'",
    "the formula is set inline at the end of the line, followed by its full stop", "displayed with \\[ ... \\]", "other", None, "high",
    r"écrire¶\[¶u_\lambda(t)=\sum_\alpha e_\alpha u_{\lambda0}(t^0_\alpha)¶=\sum_\alpha e_\alpha\otimes u_{\lambda0}(t^0_\alpha).¶\]¶Comme",
    r"écrire¶$u_\lambda(t)=\sum_\alpha e_\alpha u_{\lambda0}(t^0_\alpha)¶=\sum_\alpha e_\alpha\otimes u_{\lambda0}(t^0_\alpha)$.¶Comme",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost. Independent of the misprint fix two lines above."))
F.append(f(167, "Théorème (11.9.16), l. 1: 'Les notations étant celles de (11.9.1), supposons que X soit un S-préschéma localement noethérien'",
    "(11.9.1) upright in the italic statement", "plain text in the italic theorem environment: italic", "convention", 6, "high",
    r"(11.9.1), supposons que $X$ soit un¶$S$-préschéma localement", r"\textup{(11.9.1)}, supposons que $X$ soit un¶$S$-préschéma localement"))
F.append(f(167, "Théorème (11.9.16), l. 4: 'X_s = X ×_S Spec(k(s)) → X'",
    "bold italic k (enlarged crop p167_s3_thm.png)", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))"))

# ---------------- p. 168 ----------------
F.append(f(168, "proof of (11.9.16), l. 18: 'il résulte de (11.9.13) appliqué à X_s et à X'_{s'} = X_s ⊗_{k(s)} k(s')'",
    "X'_{s'}: X with a prime (enlarged crop p168_s2_Xs_zoom.png)", "$X_{s'}$ (no prime)", "formula", None, "high",
    r"$X_{s'}=X_s", r"$X'_{s'}=X_s",
    "X'_{s'} is the fibre at s' of X' = X ×_S S', named in the line before."))
F.append(f(168, "same formula: the subscript of ⊗, k(s)",
    "bold upright k in the subscript (same crop)", "plain k", "convention", 1, "high",
    r"\otimes_{k(s)}", r"\otimes_{\mathbf{k}(s)}",
    "Bold upright in a subscript, as GLOBAL_ISSUES 48."))
F.append(f(168, "same formula: the factor k(s')",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    r"k(s')$", r"\boldsymbol{k}(s')$"))
F.append(f(168, "same proof, l. 19: 'pour tout s' ∈ S', la famille (u'_λ)_{s'} est séparante'",
    "(u'_λ)_{s'}: one pair of parentheses (enlarged crop p168_s2_ufam.png)", "$((u'_\\lambda)_{s'})$ (outer parentheses added)", "formula", None, "high",
    r"$((u'_\lambda)_{s'})$", r"$(u'_\lambda)_{s'}$"))
F.append(f(168, "end of the proof of (11.9.16): 'il suffit d'appliquer ce qui précède et le lemme (11.9.5) pour terminer la démonstration'",
    "le lemme (11.9.5)", "keeps the printed '(11.9.5)'", "misprint_in_print", None, "high",
    note="Wrong reference in the print: (11.9.5) is the paragraph introducing the base-change notation, not a lemma; the step (A' as inductive limit of its sub-A-algebras of finite type, the 𝓖_λ S-flat) is Lemme (11.9.12), cited for the same step in the proof of (11.9.13), p. 166. The TeX keeps the printed reading; the corrected edition (r20 current) already reads (11.9.12).",
    corrected="(11.9.12)"))
F.append(f(168, "Proposition (11.9.17), l. 4: 'soient X_s la fibre X ×_S Spec(k(s))'",
    "bold italic k (enlarged crop p168_s3_prop.png)", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))"))
F.append(f(168, "Proposition (11.9.17), l. 4: '𝓕_s = 𝓕 ⊗_{𝒪_S} k(s)'",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    r"\otimes_{\mathcal O_S}k(s)", r"\otimes_{\mathcal O_S}\boldsymbol{k}(s)"))
F.append(f(168, "proof of (11.9.17), heading of step A): 'A) Cas où U est quasi-compact. — Nous utiliserons le lemme suivant :'",
    "'A)' upright, 'Cas où U est quasi-compact.' italic (enlarged crop p168_s3_A.png)",
    "\\emph{A) Cas où $U$ est quasi-compact.}: the label A) italic as well", "italics", None, "high",
    r"\emph{A) Cas où $U$ est quasi-compact.}", r"A) \emph{Cas où $U$ est quasi-compact.}",
    "Hand-made heading label upright in the print (GLOBAL_ISSUES 76 pattern); B) on p. 169 likewise."))
F.append(f(168, "Lemme (11.9.17.1), l. 1: 'Sous les hypothèses générales de (11.9.17), et en supposant en outre'",
    "(11.9.17) upright in the italic statement", "plain text in the italic lemma environment: italic", "convention", 6, "high",
    r"générales de (11.9.17),", r"générales de \textup{(11.9.17)},"))

# ---------------- p. 169 ----------------
F.append(f(169, "proof of (11.9.17), step A), l. 6-7: 'et posons X_α = X_0 ×_{S_0} S_α, U_α = U_0 ×_{S_0} S_α, 𝓕_α = 𝓕_0 ⊗_{S_0} S_α;'",
    "the list begins with X_α = X_0 ×_{S_0} S_α; the print has no 'S_α = Spec(A_α)' (enlarged crop p169_s1_posons.png)",
    "'$S_\\alpha=\\operatorname{Spec}(A_\\alpha)$,' added before $X_\\alpha$", "extra", None, "high",
    r"et posons¶$S_\alpha=\operatorname{Spec}(A_\alpha)$,¶$X_\alpha", r"et posons¶$X_\alpha"))
F.append(f(169, "same proof, l. 13: 'Mais le lemme (11.9.17.1) appliqué à u_α, montre que E_α est constructible dans S_α'",
    "comma after u_α (enlarged crop p169_s2_lemme.png)", "no comma", "punctuation", None, "high",
    r"appliqué à $u_\alpha$ montre", r"appliqué à $u_\alpha$, montre"))
F.append(f(169, "proof of (11.9.17), heading of step B): 'B) Cas général. — L'ouvert U est réunion'",
    "'B)' upright, 'Cas général.' italic (enlarged crop p169_s2_B.png)",
    "\\emph{B) Cas général.}: the label B) italic as well", "italics", None, "high",
    r"\emph{B) Cas général.}", r"B) \emph{Cas général.}",
    "As A) on p. 168 (GLOBAL_ISSUES 76 pattern)."))
F.append(f(169, "step B), l. 2: 'u_λ : 𝓕 → (j_λ)_*((j_λ)^*(𝓕)) l'homomorphisme correspondant'",
    "(j_λ)_*((j_λ)^*(𝓕)): j_λ in parentheses before the star as well (same crop)",
    "(j_\\lambda)_*(j_\\lambda^*(\\mathcal F))", "formula", None, "high",
    r"(j_\lambda)_*(j_\lambda^*(\mathcal F))", r"(j_\lambda)_*((j_\lambda)^*(\mathcal F))"))
F.append(f(169, "Remarque (11.9.18), b): 'l'homomorphisme u ⊗ 1_{k(x)}'",
    "bold upright k in the subscript (enlarged crop p169_s3_b.png)", "plain k", "convention", 1, "high",
    r"1_{k(x)}", r"1_{\mathbf{k}(x)}",
    "Bold upright in a subscript, as GLOBAL_ISSUES 48."))
F.append(f(169, "Remarque (11.9.18), b): '𝓕 ⊗_{𝒪_X} k(x)'",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    r"\mathcal F\otimes_{\mathcal O_X}k(x)", r"\mathcal F\otimes_{\mathcal O_X}\boldsymbol{k}(x)"))
F.append(f(169, "Remarque (11.9.18), b): '𝓖 ⊗_{𝒪_X} k(x)'",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    r"\mathcal G\otimes_{\mathcal O_X}k(x)", r"\mathcal G\otimes_{\mathcal O_X}\boldsymbol{k}(x)"))
F.append(f(169, "Remarque (11.9.18), after the list: 'En effet, il est clair que c) entraîne a) et que a) entraîne b).'",
    "the letters c), a), a), b) in italics (enlarged crop p169_s4_effet.png)",
    "upright (remark body judged as roman)", "italics", None, "high",
    r"que c) entraîne a) et que a) entraîne b).", r"que \emph{c)} entraîne \emph{a)} et que \emph{a)} entraîne \emph{b)}.",
    "Inside the remark environment (italic in the TeX); judged as a roman body, as the print sets remarks."))
F.append(f(169, "same paragraph: 'Le fait que b) entraîne c) résulte de (0, 19.1.12)'",
    "the letters b), c) in italics (same crop)", "upright (remark body judged as roman)", "italics", None, "high",
    r"b) entraîne c) résulte", r"\emph{b)} entraîne \emph{c)} résulte"))

# ---------------- checks ----------------
ok = True
texts = {}
for p in sorted({x['page'] for x in F}):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        texts[p] = fh.read().replace('\r\n', '\n')
for x in F:
    if x['fix'] is None:
        continue
    n = texts[x['page']].count(x['fix']['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE/ABSENT', x['page'], n, repr(x['fix']['old'])[:120])
# edits on one page must not overlap
for p, t in texts.items():
    spans = []
    for x in F:
        if x['page'] == p and x['fix']:
            i = t.find(x['fix']['old'])
            spans.append((i, i + len(x['fix']['old']), x['where'][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print('OVERLAP', p, a, b)

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

from collections import Counter
c = Counter()
for x in F:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    c[(x['page'], k)] += 1
for p in sorted(texts):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('total', len(F), 'checks ok' if ok else 'CHECK FAILURES')
