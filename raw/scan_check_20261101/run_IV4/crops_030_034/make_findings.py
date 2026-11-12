"""Build findings_030_034.json for EGA IV-4 pp. 30-34 and check every fix.

Newlines inside old/new strings are written as the pilcrow character and
converted to LF here.  Checks: each old occurs exactly once in its page file;
all fixes of a page apply in the given order and in reverse order with the
same result.  Writes applied_NNN.tex for a compile check.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_030_034.json"
NL = "\u00b6"

F = []


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="",
        corrected=None):
    item = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
            "convention": conv, "confidence": conf}
    if old is None:
        item["fix"] = None
    else:
        item["fix"] = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        item["corrected"] = corrected
    item["note"] = note
    F.append(item)


def c1(page, where, old, new, sub=False, note=""):
    if sub:
        add(page, where, "bold upright k in the subscript", "plain k", "convention",
            old, new, conv=1, note=note or "Subscript: the print's k is bold upright (\\mathbf{k}).")
    else:
        add(page, where, "bold italic k", "plain k", "convention", old, new, conv=1, note=note)


def c2(page, where, numeral, old, new):
    add(page, where, f"bold {numeral}", f"plain {numeral}", "convention", old, new, conv=2)


def c6(page, where, scan, old, new, note=""):
    add(page, where, scan, "italic (inside the italic statement)", "convention", old, new,
        conv=6, note=note)


def om(page, where, old, new, scan="italic Omega (sheaf of differentials)", note=""):
    add(page, where, scan, "upright \\Omega", "font", old, new,
        note=note or "Sheaf of differentials: italic Omega (\\varOmega) in the print.")


# ---------------------------------------------------------------- page 30
p = 30
c6(p, "Proposition (16.5.11), label (i)", "upright '(i)'", r"\item[(i)]", r"\item[\textup{(i)}]")
c6(p, "Proposition (16.5.11) (i): '(resp. localement de présentation finie),'",
   "'(resp.' and ')' upright, the words italic",
   r"(resp.\ localement de présentation finie), l'homomorphisme",
   r"\textup{(resp.}\ localement de présentation finie\textup{)}, l'homomorphisme")
c6(p, "Proposition (16.5.11) (i): 'l'homomorphisme (16.5.10.2) est injectif'",
   "reference upright", r"(16.5.10.2) est injectif", r"\textup{(16.5.10.2)} est injectif")
c6(p, "Proposition (16.5.11) (i), end: '(resp. bijectif).'",
   "'(resp.' and ')' upright, 'bijectif' italic",
   r"(resp.\ bijectif)", r"\textup{(resp.}\ bijectif\textup{)}")
c6(p, "Proposition (16.5.11), label (ii)", "upright '(ii)'", r"\item[(ii)]", r"\item[\textup{(ii)}]")
om(p, "Proposition (16.5.11) (ii): 'Si Ω^1_{X/S} est un O_X-Module localement libre'",
   r"Si $\Omega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement",
   r"Si $\varOmega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement")
c6(p, "Proposition (16.5.11) (ii): 'l'homomorphisme (16.5.10.2) est bijectif'",
   "reference upright", r"(16.5.10.2) est bijectif", r"\textup{(16.5.10.2)} est bijectif")
om(p, "proof of (16.5.11): '(resp. localement de présentation finie), Ω^1_{X/S} est un O_X-Module de type fini'",
   r"finie), $\Omega_{X/S}^1$ est un", r"finie), $\varOmega_{X/S}^1$ est un")
om(p, "(16.5.12), l. 1: 'Puisque Ω^1_{X/S} est un O_X-Module quasi-cohérent'",
   r"Puisque $\Omega_{X/S}^1$", r"Puisque $\varOmega_{X/S}^1$")
om(p, "(16.5.12): 'le fibré vectoriel sur X défini par Ω^1_{X/S}'",
   r"défini par $\Omega_{X/S}^1$", r"défini par $\varOmega_{X/S}^1$")
c2(p, "(16.5.12): '(II, 1.7.8)'", "II", r"(II, 1.7.8)", r"(\textbf{II}, 1.7.8)")
om(p, "display (16.5.12.1): 'T_{X/S}=V(Ω^1_{X/S})'",
   r"\mathbf{V}(\Omega_{X/S}^1)", r"\mathbf{V}(\varOmega_{X/S}^1)")
c2(p, "(16.5.12): 'une bijection canonique (II, 1.7.9)'", "II", r"(II, 1.7.9)", r"(\textbf{II}, 1.7.9)")
om(p, "display after (16.5.12.1): 'Hom_{O_X}(Ω^1_{X/S}, O_X)'",
   r"\operatorname{Hom}_{\mathcal{O}_X}(\Omega_{X/S}^1,\mathcal{O}_X)",
   r"\operatorname{Hom}_{\mathcal{O}_X}(\varOmega_{X/S}^1,\mathcal{O}_X)")
om(p, "(16.5.12): 'f_{X/Y/S} : f^*(Ω^1_{Y/S}) -> Ω^1_{X/S}'",
   r"$f_{X/Y/S}:f^*(\Omega_{Y/S}^1)\to\Omega_{X/S}^1$",
   r"$f_{X/Y/S}:f^*(\varOmega_{Y/S}^1)\to\varOmega_{X/S}^1$", scan="italic Omega (twice)")
om(p, "display 'V(f^*(Ω^1_{Y/S}))=V(Ω^1_{Y/S})×_Y X'",
   r"\mathbf{V}(f^*(\Omega_{Y/S}^1))¶  =\mathbf{V}(\Omega_{Y/S}^1)",
   r"\mathbf{V}(f^*(\varOmega_{Y/S}^1))¶  =\mathbf{V}(\varOmega_{Y/S}^1)", scan="italic Omega (twice)")
c2(p, "same display: '(II, 1.7.11),'", "II", r"\text{(II, 1.7.11),}", r"\text{(\textbf{II}, 1.7.11),}")
c2(p, "(16.5.12): 'T_{X/S}(g∘f)=… (0, 20.5.4.1)'", "0", r"(0, 20.5.4.1)", r"(\textbf{0}, 20.5.4.1)")
c2(p, "(16.5.12), last paragraph: 'Il résulte de (16.5.10.1) et de (II, 1.7.11) que'", "II",
   r"et de (II, 1.7.11) que", r"et de (\textbf{II}, 1.7.11) que")
c1(p, "(16.5.13): 'la fibre T_{X/S}×_X Spec(k(x))'", r"\operatorname{Spec}(k(x))",
   r"\operatorname{Spec}(\boldsymbol{k}(x))")
c1(p, "(16.5.13): 'rationnels sur k(x)'", r"rationnels sur $k(x)$", r"rationnels sur $\boldsymbol{k}(x)$")
c1(p, "display (16.5.13.1): 'Hom_{k(x)}'", r"\operatorname{Hom}_{k(x)}",
   r"\operatorname{Hom}_{\mathbf{k}(x)}", sub=True)
om(p, "display (16.5.13.1): 'Ω^1_{X/S}⊗…'", r"(\Omega_{X/S}^1\otimes", r"(\varOmega_{X/S}^1\otimes")
add(p, "display (16.5.13.1): 'Ω^1_{X/S}⊗_{O_X} k(x)'",
    "⊗_{O_X}: capital roman X under the script O (6x crop p30_s4_otimes.png; the second-level x of "
    "Ω^1_{O_x/O_s} two lines below is a lowercase italic x)",
    r"\otimes_{\mathcal{O}_x}", "formula", r"_{\mathcal{O}_x}", r"_{\mathcal{O}_X}",
    note="The print's notation Ω^1_{X/S}⊗_{O_X}k(x), as in (16.5.8) on p. 29 and twice on p. 31; "
         "the TeX changed it to O_x here. Not a misprint.")
c1(p, "display (16.5.13.1): first argument '…⊗ k(x),'", r"k(x),", r"\boldsymbol{k}(x),")
c1(p, "display (16.5.13.1): second argument 'k(x))'", r"k(x))¶  \tag{16.5.13.1}",
   r"\boldsymbol{k}(x))¶  \tag{16.5.13.1}")
c1(p, "after (16.5.13.1): 'le dual du k(x)-espace vectoriel'", r"du $k(x)$-espace",
   r"du $\boldsymbol{k}(x)$-espace")
add(p, "after (16.5.13.1): 'Ω^1_{O_x/O_s}/m_x.Ω^1_{O_x/O_s}'",
    "baseline period between m_x and Omega (10x crop p30_s4_mdot2.png)", r"\cdot", "symbol",
    r"\mathfrak{m}_x\cdot\Omega", r"\mathfrak{m}_x.\Omega",
    note="GLOBAL_ISSUES 65. Both Omegas of this module are upright in the print (module of differentials), "
         "as the TeX has them.")
om(p, "last lines: 'Lorsque Ω^1_{X/S} est un O_X-Module de type fini'",
   r"Lorsque¶$\Omega_{X/S}^1$", r"Lorsque¶$\varOmega_{X/S}^1$")
c1(p, "last line: 'de rang fini sur k(x)'", r"rang fini sur $k(x)$", r"rang fini sur $\boldsymbol{k}(x)$")

# ---------------------------------------------------------------- page 31
p = 31
c1(p, "display (16.5.13.2): '⊗_{k(x)}'", r"\xrightarrow{\sim}¶  T_{X/S}(x)\otimes_{k(x)}",
   r"\xrightarrow{\sim}¶  T_{X/S}(x)\otimes_{\mathbf{k}(x)}", sub=True)
c1(p, "display (16.5.13.2): 'k(x')'", r"k(x')", r"\boldsymbol{k}(x')")
c1(p, "'Si x est rationnel sur k(s), où s=f(x)'", r"rationnel sur $k(s)$}, où",
   r"rationnel sur $\boldsymbol{k}(s)$}, où")
c1(p, "'(de sorte que k(s) -> k(x) est un isomorphisme)': k(s)", r"$k(s)\to",
   r"$\boldsymbol{k}(s)\to")
c1(p, "'(de sorte que k(s) -> k(x) est un isomorphisme)': k(x)", r"k(x)$ est un isomorphisme",
   r"\boldsymbol{k}(x)$ est un isomorphisme")
c1(p, "display (16.5.13.3): 'T_{X_s/k(s)}'", r"T_{X_s/k(s)}", r"T_{X_s/\mathbf{k}(s)}", sub=True)
c1(p, "display (16.5.13.3): 'Hom_{k(s)}'", r"\operatorname{Hom}_{k(s)}",
   r"\operatorname{Hom}_{\mathbf{k}(s)}", sub=True)
c1(p, "display (16.5.13.3): last argument 'k(s))'", r"{}^2,k(s))", r"{}^2,\boldsymbol{k}(s))")
om(p, "display (16.5.13.4): 'g_{Y/X/S} : g^*(Ω^1_{X/S}) -> Ω^1_{Y/S}'",
   r"g_{Y/X/S}:g^*(\Omega_{X/S}^1)\longrightarrow\Omega_{Y/S}^1",
   r"g_{Y/X/S}:g^*(\varOmega_{X/S}^1)\longrightarrow\varOmega_{Y/S}^1", scan="italic Omega (twice)")
om(p, "display after 'Notons maintenant…': 'g^*(Ω^1_{X/S})⊗…'", r"\[¶  g^*(\Omega_{X/S}^1)",
   r"\[¶  g^*(\varOmega_{X/S}^1)")
c1(p, "same display: '⊗_{O_Y} k(y) ='", r"k(y)¶  =", r"\boldsymbol{k}(y)¶  =")
om(p, "same display: '(Ω^1_{X/S}⊗_{O_X} k(x))'", r"(\Omega_{X/S}^1\otimes", r"(\varOmega_{X/S}^1\otimes")
c1(p, "same display: '(Ω^1_{X/S}⊗_{O_X} k(x))'", r"_{\mathcal{O}_X}k(x))",
   r"_{\mathcal{O}_X}\boldsymbol{k}(x))")
c1(p, "same display: '⊗_{k(x)} k(y)': subscript", r"¶  \otimes_{k(x)}", r"¶  \otimes_{\mathbf{k}(x)}",
   sub=True)
c1(p, "same display: '⊗_{k(x)} k(y)': k(y)", r"k(y)¶\]¶et par suite", r"\boldsymbol{k}(y)¶\]¶et par suite")
om(p, "'et par suite, si Ω^1_{X/S} est un O_X-Module de type fini'", r"si $\Omega_{X/S}^1$ est un",
   r"si $\varOmega_{X/S}^1$ est un")
c1(p, "display 'Hom_{k(y)}(…)': subscript", r"\operatorname{Hom}_{k(y)}",
   r"\operatorname{Hom}_{\mathbf{k}(y)}", sub=True)
om(p, "display 'Hom_{k(y)}(g^*(Ω^1_{X/S})⊗…)'", r"(g^*(\Omega_{X/S}^1)", r"(g^*(\varOmega_{X/S}^1)")
c1(p, "display 'Hom_{k(y)}(…⊗_{O_Y} k(y), k(y))': first k(y)", r"k(y),", r"\boldsymbol{k}(y),")
c1(p, "display 'Hom_{k(y)}(…⊗_{O_Y} k(y), k(y))': second k(y)", r"k(y))¶\]", r"\boldsymbol{k}(y))¶\]")
c1(p, "'à T_{X/S}(x)⊗_{k(x)} k(y).': subscript", r"à $T_{X/S}(x)\otimes_{k(x)}",
   r"à $T_{X/S}(x)\otimes_{\mathbf{k}(x)}", sub=True)
c1(p, "'à T_{X/S}(x)⊗_{k(x)} k(y).': k(y)", r"k(y)$. On déduit", r"\boldsymbol{k}(y)$. On déduit")
c1(p, "'un homomorphisme de k(y)-espaces vectoriels'", r"\emph{$k(y)$-espaces",
   r"\emph{$\boldsymbol{k}(y)$-espaces")
c1(p, "display (16.5.13.5): subscript of ⊗", r"\longrightarrow¶  T_{X/S}(x)\otimes_{k(x)}",
   r"\longrightarrow¶  T_{X/S}(x)\otimes_{\mathbf{k}(x)}", sub=True)
c1(p, "display (16.5.13.5): 'k(y)'", r"k(y)¶  \tag{16.5.13.5}", r"\boldsymbol{k}(y)¶  \tag{16.5.13.5}")
c1(p, "'Lorsque y est rationnel sur k(s)'", r"rationnel sur $k(s)$}, on peut",
   r"rationnel sur $\boldsymbol{k}(s)$}, on peut")
c1(p, "'on peut identifier k(s), k(y) et k(x)': k(s)", r"identifier $k(s)$", r"identifier $\boldsymbol{k}(s)$")
c1(p, "'on peut identifier k(s), k(y) et k(x)': k(y)", r"$k(y)$ et", r"$\boldsymbol{k}(y)$ et")
c1(p, "'on peut identifier k(s), k(y) et k(x)': k(x)", r"$k(x)$ et¶$T_y(g)$",
   r"$\boldsymbol{k}(x)$ et¶$T_y(g)$")
c1(p, "'un homomorphisme de k(s)-espaces vectoriels'", r"de $k(s)$-espaces", r"de $\boldsymbol{k}(s)$-espaces")
om(p, "'g^*(Ω^1_{X/S})⊗_{O_Y} k(y) s'identifie à'", r"$g^*(\Omega_{X/S}^1)", r"$g^*(\varOmega_{X/S}^1)")
c1(p, "'g^*(Ω^1_{X/S})⊗_{O_Y} k(y) s'identifie à'", r"k(y)$ s'identifie", r"\boldsymbol{k}(y)$ s'identifie")
om(p, "'s'identifie à Ω^1_{X/S}⊗_{O_X} k(x)'", r"à¶$\Omega_{X/S}^1", r"à¶$\varOmega_{X/S}^1")
c1(p, "'s'identifie à Ω^1_{X/S}⊗_{O_X} k(x)'", r"k(x)$, et l'homomorphisme",
   r"\boldsymbol{k}(x)$, et l'homomorphisme")
om(p, "'condition de finitude sur Ω^1_{X/S}'", r"finitude sur $\Omega_{X/S}^1$",
   r"finitude sur $\varOmega_{X/S}^1$")
c2(p, "(16.5.14): 'donnée dans (0, 20.1.1)'", "0", r"(0, 20.1.1)", r"(\textbf{0}, 20.1.1)")
add(p, "(16.5.14): 'défini par un Idéal de carré nul J de O_Y'", "'de carré nul' italic (crop p31_s3_carre.png)",
    "upright", "italics", r"Idéal de carré nul", r"Idéal \emph{de carré nul}")

# ---------------------------------------------------------------- page 32
p = 32
add(p, "'tels que le composé B -φ-> C -> C/L soit égal à ψ'",
    "the composite is in the running text (crop p32_s1_compose.png)", "displayed", "other",
    r"\[¶  B\xrightarrow{\varphi}C\longrightarrow C/\mathfrak{L}¶\]",
    r"$B\xrightarrow{\varphi}C\to C/\mathfrak{L}$",
    note="Display vs inline only; no connecting word lost or added.")
c2(p, "'On sait donc (0, 20.1.1) que'", "0", r"(0, 20.1.1)", r"(\textbf{0}, 20.1.1)")
add(p, "'on a un isomorphisme v ⇝ v∘d_{B/A} de Hom_B(Ω^1_{B/A}, L)'", "wavy arrow", r"\mapsto",
    "symbol", r"$v\mapsto v", r"$v\leadsto v")
c2(p, "'sur Dér_A(B, L) (0, 20.4.8)'", "0", r"(0, 20.4.8)", r"(\textbf{0}, 20.4.8)")
om(p, "display (16.5.14.2): 'G = Hom(u_0^*(Ω^1_{X/S}), J);'", r"(u_0^*(\Omega_{X/S}^1),\mathscr{J});",
   r"(u_0^*(\varOmega_{X/S}^1),\mathscr{J});",
   note="Sheaf of differentials italic; the modules Ω^1_{B/A} on this page are upright in the print, as in the TeX.")
om(p, "'du fait que Ω^1_{B/A}=Γ(V, Ω^1_{X/S}) (16.3.7)'", r"\Gamma(V,\Omega_{X/S}^1)",
   r"\Gamma(V,\varOmega_{X/S}^1)", note="Ω^1_{B/A} (module) upright in the print, Ω^1_{X/S} (sheaf) italic.")
add(p, "'il est clair que U_0 ⇝ P(U_0) est un faisceau d'ensembles'", "wavy arrow (crop p32_s3_U0P.png)",
    r"\mapsto", "symbol", r"$U_0\mapsto P(U_0)$", r"$U_0\leadsto P(U_0)$")
add(p, "'l'application h : Γ(U_0, G)×P(U_0) -> P(U_0) définissant la structure de torseur'",
    "in the running text", "displayed", "other",
    r"\[¶  h:\Gamma(U_0,\mathscr{G})\times P(U_0)\longrightarrow P(U_0)¶\]",
    r"$h:\Gamma(U_0,\mathscr{G})\times P(U_0)\to P(U_0)$",
    note="Display vs inline only; no connecting word lost or added.")

# ---------------------------------------------------------------- page 33
p = 33
c2(p, "l. 2: 'du diagramme (0, 20.5.4.2)'", "0", r"(0, 20.5.4.2)", r"(\textbf{0}, 20.5.4.2)")
add(p, "'pour lequel Γ(U_0, P)≠∅, m_{U_0} : Γ(U_0, G)×Γ(U_0, P) -> Γ(U_0, P) soit une loi externe'",
    "in the running text", "displayed", "other",
    r"\[¶  m_{U_0}:\Gamma(U_0,\mathscr{G})\times\Gamma(U_0,\mathscr{P})¶  \longrightarrow\Gamma(U_0,\mathscr{P})¶\]",
    r"$m_{U_0}:\Gamma(U_0,\mathscr{G})\times\Gamma(U_0,\mathscr{P})\to\Gamma(U_0,\mathscr{P})$",
    note="Display vs inline only; no connecting word lost or added.")
add(p, "(16.5.15): 'Γ(U, P)≠∅, m_U : Γ(U, G)×Γ(U, P) -> Γ(U, P) fasse de Γ(U, P) un torseur'",
    "in the running text", "displayed", "other",
    r"\[¶  m_U:\Gamma(U,\mathscr{G})\times\Gamma(U,\mathscr{P})¶  \longrightarrow\Gamma(U,\mathscr{P})¶\]",
    r"$m_U:\Gamma(U,\mathscr{G})\times\Gamma(U,\mathscr{P})\to\Gamma(U,\mathscr{P})$",
    note="Display vs inline only; no connecting word lost or added.")
add(p, "(16.5.15): '(ou faisceau formellement principal homogène) sous le faisceau de groupes G.'",
    "'sous le faisceau de groupes' italic (crop p33_s2_sous.png)", "upright", "italics",
    r"sous le faisceau de groupes", r"\emph{sous le faisceau de groupes}")
add(p, "(16.5.15): '(ou faisceau principal homogène) sous G si de plus'", "'sous' italic", "upright", "italics",
    r"homogène}) sous $\mathscr{G}$", r"homogène}) \emph{sous} $\mathscr{G}$")
add(p, "'(pour un G donné)'", "'donné' italic (crop p33_s2_donne.png)", "upright", "italics",
    r"$\mathscr{G}$ donné)", r"$\mathscr{G}$ \emph{donné})")
add(p, "'tel que γ_{λμ}.(p_μ|U_λ∩U_μ)=p_λ|U_λ∩U_μ; en outre'",
    "in the running text; baseline period after γ_{λμ} (7x crop p33_s2_gammadot2.png)",
    "displayed, with \\cdot", "other",
    r"\[¶  \gamma_{\lambda\mu}\cdot¶  (p_\mu|U_\lambda\cap U_\mu)=p_\lambda|U_\lambda\cap U_\mu;¶\]",
    r"$\gamma_{\lambda\mu}.(p_\mu|U_\lambda\cap U_\mu)=p_\lambda|U_\lambda\cap U_\mu$;",
    note="One edit for two differences: display vs inline, and the print's baseline period for \\cdot "
         "(GLOBAL_ISSUES 65).")
add(p, "'autrement dit (λ, μ) ⇝ γ_{λμ} est un 1-cocycle'", "wavy arrow (crop p33_s3_cocycle2.png)",
    r"\mapsto", "symbol", r"$(\lambda,\mu)\mapsto\gamma_{\lambda\mu}$", r"$(\lambda,\mu)\leadsto\gamma_{\lambda\mu}$")
add(p, "'est un 1-cocycle du recouvrement'", "'1-' upright, only 'cocycle' italic (crop p33_s3_cocycle2.png)",
    r"\emph{1-cocycle}", "italics", r"\emph{1-cocycle}", r"1-\emph{cocycle}", conf="medium",
    note="The old-style 1 is upright (vertical serifs); the roman '1-cocycle' elsewhere on the page matches it.")
add(p, "'tel que p'_λ=β_λ.p_λ, et le 1-cocycle'", "baseline period (7x crop p33_s3_betadot2.png)", r"\cdot",
    "symbol", r"\beta_\lambda\cdot p", r"\beta_\lambda.p", note="GLOBAL_ISSUES 65.")
add(p, "'tel que p'_λ=β_λ.p_λ, et le 1-cocycle'", "comma after the formula (crop p33_s3_betadot.png)",
    "no comma", "punctuation", r"$ et le 1-cocycle", r"$, et le 1-cocycle")
add(p, "'est donné par γ'_{λμ}=β_λγ_{λμ}β_μ^{-1}, autrement dit'", "in the running text", "displayed",
    "other", r"par¶\[¶  \gamma'_{\lambda\mu}=\beta_\lambda\gamma_{\lambda\mu}\beta_\mu^{-1},¶\]",
    r"par $\gamma'_{\lambda\mu}=\beta_\lambda\gamma_{\lambda\mu}\beta_\mu^{-1}$,",
    note="Display vs inline only; no connecting word lost or added.")
add(p, "'à l'aide des automorphismes θ_{λμ} (0_I, 3.3.1)'",
    "(0_I, 3.3.1): bold 0 with subscript I (crop p33_s3_01.png)", "(0, 3.3.1): no subscript I", "missing",
    r"(0, 3.3.1)", r"($\mathbf{0}_{\mathrm I}$, 3.3.1)",
    note="The same edit sets the bold 0 (convention 2). The reference is to EGA 0_I (gluing of sheaves); "
         "EGA IV's own chapter 0 has no section 3.")
add(p, "'si (γ_{λμ}) est un 1-cobord'", "'1-' upright, only 'cobord' italic (crop p33_s4_cobord.png)",
    r"\emph{1-cobord}", "italics", r"\emph{1-cobord}", r"1-\emph{cobord}", conf="medium",
    note="As for '1-cocycle' above: only the word is italic.")
c2(p, "'il résulte de (III, 1.3.1) que l'on a'", "III", r"(III, 1.3.1)", r"(\textbf{III}, 1.3.1)")

# ---------------------------------------------------------------- page 34
p = 34
add(p, "l. 1: 'Revenant au problème considéré en (16.5.13)'", "(16.5.13)", "(16.5.13) (keeps the print)",
    "misprint_in_print", None, None, conf="medium", corrected="(16.5.14)",
    note="The problem (existence of u with u∘j=u_0) is posed in (16.5.14); (16.5.13) is the tangent space. "
         "The TeX keeps the printed reading; the corrected edition should read (16.5.14). No erratum found "
         "in the IV-4 errata list.")
add(p, "Proposition (16.5.17), end: 'sous le O_{Y_0}-Module G = Hom_{O_{Y_0}}(u_0^*(Ω^1_{X/S}), J).'",
    "in the running text (crop p34_s1_Gdef.png); italic Omega", "displayed; upright \\Omega", "other",
    r"\[¶  \mathscr{G}=\mathscr{H}om_{\mathcal{O}_{Y_0}}¶  (u_0^*(\Omega_{X/S}^1),\mathscr{J}).¶\]",
    r"$\mathscr{G}=\mathscr{H}om_{\mathcal{O}_{Y_0}}(u_0^*(\varOmega_{X/S}^1),\mathscr{J})$.",
    note="One edit for two differences: display vs inline, and the italic Omega of the sheaf of differentials.")
c6(p, "Corollaire (16.5.18): 'Avec les notations de (16.5.16),'", "reference upright",
   r"notations de (16.5.16)", r"notations de \textup{(16.5.16)}")
add(p, "Corollaire (16.5.18): 'Avec les notations de (16.5.16)'", "(16.5.16)",
    "(16.5.16) (keeps the print)", "misprint_in_print", None, None, conf="medium", corrected="(16.5.17)",
    note="The notations (Y, Y_0, j, u_0, the S-morphisms, G built from Ω^1_{X/S}) are those of Proposition "
         "(16.5.17); (16.5.16) only has Z and G. The proof's 'en vertu de (16.5.16)' is right. The TeX keeps "
         "the printed reading; in the corrected edition change the number inside the \\textup of the "
         "convention-6 fix above.")
om(p, "Corollaire (16.5.18): 'supposons Y affine et Ω^1_{X/S} de présentation finie'",
   r"affine et $\Omega_{X/S}^1$ de", r"affine et $\varOmega_{X/S}^1$ de")
c2(p, "proof of (16.5.18): 'quasi-cohérent (I, 1.3.12)'", "I", r"(I, 1.3.12)", r"(\textbf{I}, 1.3.12)")
add(p, "(16.6.1): 'la puissance extérieure p-ème (0_I, 4.1.5)'",
    "(0_I, 4.1.5): bold 0 with subscript I (crop p34_s3_01.png)", "(0, 4.1.5): no subscript I", "missing",
    r"$p$-ème} (0, 4.1.5)", r"$p$-ème} ($\mathbf{0}_{\mathrm I}$, 4.1.5)",
    note="The same edit sets the bold 0 (convention 2).")
om(p, "(16.6.1): 'du O_X-Module Ω^1_{X/S}, notée'", r"$\Omega_{X/S}^1$, notée", r"$\varOmega_{X/S}^1$, notée")
om(p, "display (16.6.1.1): 'Ω^p_{X/S} = ∧^p(Ω^1_{X/S}).'", r"\Omega_{X/S}^p=\bigwedge^p(\Omega_{X/S}^1).",
   r"\varOmega_{X/S}^p=\bigwedge^p(\varOmega_{X/S}^1).", scan="italic Omega (twice)")
om(p, "'On a donc Ω^0_{X/S}=O_X, et Ω^p_{X/S}=0 pour p<0'",
   r"$\Omega_{X/S}^0=\mathcal{O}_X$, et $\Omega_{X/S}^p=0$",
   r"$\varOmega_{X/S}^0=\mathcal{O}_X$, et $\varOmega_{X/S}^p=0$", scan="italic Omega (twice)")
om(p, "'les Ω^p_{X/S} sont les composants homogènes'", r"les $\Omega_{X/S}^p$", r"les $\varOmega_{X/S}^p$")
om(p, "'de l'Algèbre extérieure sur Ω^1_{X/S}'", r"sur $\Omega_{X/S}^1$", r"sur $\varOmega_{X/S}^1$")
om(p, "display (16.6.1.2)",
   r"\Omega_{X/S}^{\bullet}=\bigwedge(\Omega_{X/S}^1)¶  =\bigoplus_{p\in\mathbf{Z}}\bigwedge^p(\Omega_{X/S}^1),",
   r"\varOmega_{X/S}^{\bullet}=\bigwedge(\varOmega_{X/S}^1)¶  =\bigoplus_{p\in\mathbf{Z}}\bigwedge^p(\varOmega_{X/S}^1),",
   scan="italic Omega (three times)")
add(p, "'on a Γ(U, Ω^•_{X/S})=∧(Γ(U, Ω^1_{X/S})), où'", "in the running text; italic Omega",
    "displayed; upright \\Omega", "other",
    r"\[¶  \Gamma(U,\Omega_{X/S}^{\bullet})¶  =\bigwedge(\Gamma(U,\Omega_{X/S}^1)),¶\]",
    r"$\Gamma(U,\varOmega_{X/S}^{\bullet})=\bigwedge(\Gamma(U,\varOmega_{X/S}^1))$,",
    note="One edit for two differences: display vs inline, and the italic Omega (twice).")
om(p, "'où Γ(U, Ω^1_{X/S}) est considéré comme Γ(U, O_X)-module'", r"où $\Gamma(U,\Omega_{X/S}^1)$",
   r"où $\Gamma(U,\varOmega_{X/S}^1)$")
add(p, "'B étant donc une A-algèbre, on a (0_I, 4.1.5)'",
    "(0_I, 4.1.5): bold 0 with subscript I (crop p34_s4_01.png)", "(0, 4.1.5): no subscript I", "missing",
    r"on a (0, 4.1.5)", r"on a ($\mathbf{0}_{\mathrm I}$, 4.1.5)",
    note="The same edit sets the bold 0 (convention 2).")
om(p, "'Ω^p_{X/S}=(Ω^p_{B/A})~'", r"$\Omega_{X/S}^p=(\Omega_{B/A}^p)", r"$\varOmega_{X/S}^p=(\Omega_{B/A}^p)",
   note="Only the sheaf Ω^p_{X/S} is italic; the modules Ω^p_{B/A}, Ω^1_{B/A} on this line are upright, as in the TeX.")
om(p, "Théorème (16.6.2): 'du faisceau de groupes additifs Ω^•_{X/S}'", r"$\Omega_{X/S}^{\bullet}$, ayant",
   r"$\varOmega_{X/S}^{\bullet}$, ayant")
c6(p, "Théorème (16.6.2), label (i)", "upright '(i)'", r"\item[(i)]", r"\item[\textup{(i)}]")
c6(p, "Théorème (16.6.2), label (ii)", "upright '(ii)'", r"\item[(ii)]", r"\item[\textup{(ii)}]")


# ---------------------------------------------------------------- checks
def apply(text, fixes):
    for fx in fixes:
        if text.count(fx["old"]) != 1:
            return None, fx["old"]
        text = text.replace(fx["old"], fx["new"], 1)
    return text, None


ok = True
for pg in range(30, 35):
    tex = (RUN / f"page_{pg:03d}.tex").read_text(encoding="utf-8")
    fixes = [x["fix"] for x in F if x["page"] == pg and x["fix"]]
    for fx in fixes:
        n = tex.count(fx["old"])
        if n != 1:
            ok = False
            print(f"p{pg}: old occurs {n} times: {fx['old']!r}")
    # span overlap check
    spans = []
    for fx in fixes:
        i = tex.find(fx["old"])
        spans.append((i, i + len(fx["old"]), fx["old"]))
    spans.sort()
    for (a1, b1, o1), (a2, b2, o2) in zip(spans, spans[1:]):
        if a2 < b1:
            print(f"p{pg}: overlapping spans: {o1!r} / {o2!r}")
    t1, bad1 = apply(tex, fixes)
    t2, bad2 = apply(tex, list(reversed(fixes)))
    if t1 is None or t2 is None or t1 != t2:
        ok = False
        print(f"p{pg}: order-dependent or failing fix: {bad1!r} {bad2!r}")
    else:
        (HERE / f"applied_{pg:03d}.tex").write_text(t1, encoding="utf-8", newline="\n")

counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "convention":
        c[1] += 1
    elif x["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
print("total", len(F), "ok" if ok else "PROBLEMS")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT)
