# Builds findings_185_189.json and checks every fix["old"] against page_NNN.tex (exact, CRLF)
# and against the release segment (LF), as apply_fixes.py would.
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega1\ega1-10-fr.tex")
OUT = RUN / "findings_185_189.json"
NL = "\r\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


BOLD0 = "Chapter number 0 printed bold; plain in the TeX."
RESP = "'resp.' roman in the print inside the italic statement; italic in the TeX environment. Checked on a crop."

# ---------------- page 185 ----------------
add(185, "proof of (10.3.6), first line: 'en vertu de (10.3.1.1) et de (0, 7.6.12)'",
    "(0, 7.6.12) with the chapter number 0 in bold", "{0, 7.6.12}",
    "convention", 2, "high", "{0, 7.6.12}", r"{\textbf{0}, 7.6.12}", BOLD0)
add(185, "proof of (10.3.6): 'associé au préfaisceau U→(Γ(U, 𝔍^Δ))^n'",
    "plain arrow: U→(Γ(U, 𝔍^Δ))^n", r"$U\mapsto(\Gamma(U,\mathfrak{J}^\Delta))^n$",
    "convention", 3, "high", r"$U\mapsto(\Gamma(U", r"$U\to(\Gamma(U",
    "Checked on a crop at 3x: no bar at the tail of the arrow.")
add(185, "proof of (10.3.6): 'U→(Γ(U, 𝔍^Δ))^n (0, 4.1.6), le corollaire en résulte'",
    "(0, 4.1.6) with the chapter number 0 in bold", "{0, 4.1.6}",
    "convention", 2, "high", "{0, 4.1.6}", r"{\textbf{0}, 4.1.6}", BOLD0)
add(185, "proof of (10.3.6), last line: 'puisque les 𝔇(f) forment une base de la topologie de X.'",
    "roman capital X ('de la topologie de X.'), not the Fraktur 𝔛",
    r"$\mathfrak{D}(f)$ forment une base de la topologie de $\mathfrak{X}$.",
    "misprint_in_print", None, "high",
    r"$\mathfrak{D}(f)$ forment une base de la topologie de $\mathfrak{X}$",
    r"$\mathfrak{D}(f)$ forment une base de la topologie de $X$",
    "The TeX silently corrects the print. Checked on a crop at 3x: an ordinary roman X, unlike the Fraktur 𝔛 "
    "of (10.3.7) just below. The 𝔇(f) form a base of the topology of the formal spectrum 𝔛 = Spf(A); no X "
    "is in play in (10.3.6). Same slip (roman X for 𝔛) on pp. 187, 188 and 189.",
    corrected=r"$\mathfrak{X}$")
add(185, "(10.3.7): 'forment un système fondamental de voisinages de 0 dans A'",
    "italics end after the second 'de'; the 0 (old-style figure) is upright",
    r"\emph{système fondamental" + NL + r"de voisinages de 0}",
    "italics", None, "high", "de voisinages de 0}", "de voisinages de} 0",
    "Checked on a crop at 2.5x: the zero is upright, the preceding 'de voisinages de' is italic. "
    "The env body is roman, so moving the brace sets the 0 roman.")
add(185, "heading of (10.4.1)",
    "'(10.4.1.)' with a period after the last digit, inside the parenthesis",
    r"\begin{env}[10.4.1]",
    "misprint_in_print", None, "medium", r"\begin{env}[10.4.1]", r"\begin{env}[10.4.1.]",
    "The TeX has the normal '(10.4.1)'. Checked on a crop at 3x: the stray period is clear. All other "
    "numbered paragraphs on pp. 185-189 ((10.3.7), (10.4.7), (10.4.8), (10.5.1), (10.5.2), (10.6.1)) have "
    "no period, so this is a slip in the print. Only the printed heading changes; the label is separate.",
    corrected="(10.4.1)")
add(185, "Définition (10.4.2): 'est adique (resp. localement noethérien)'",
    "'(resp.' roman inside the italic definition", "adique (resp. localement",
    "convention", 6, "high", "adique (resp. localement", r"adique \textup{(resp.} localement", RESP)
add(185, "Définition (10.4.2): 'affine adique (resp. noethérien). On dit que'",
    "'(resp.' roman inside the italic definition", "(resp. noethérien). On dit",
    "convention", 6, "high", "(resp. noethérien). On dit", r"\textup{(resp.} noethérien). On dit", RESP)
add(185, "Proposition (10.4.3): 'un préschéma formel (resp. localement noethérien)'",
    "'(resp.' roman inside the italic statement", "formel (resp. localement",
    "convention", 6, "high", "formel (resp. localement", r"formel \textup{(resp.} localement", RESP)
add(185, "Proposition (10.4.3): 'ouverts formels affines (resp. affines noethériens)'",
    "'(resp.' roman inside the italic statement", "(resp. affines noethériens)",
    "convention", 6, "high", "(resp. affines noethériens)", r"\textup{(resp.} affines noethériens)", RESP)
add(185, "proof of (10.4.3): 'pour tout f∈A (0, 7.6.11)'",
    "(0, 7.6.11) with the chapter number 0 in bold", "{0, 7.6.11}",
    "convention", 2, "high", "{0, 7.6.11}", r"{\textbf{0}, 7.6.11}", BOLD0)
add(185, "Corollaire (10.4.4), first parenthesis: 'préschéma formel (resp. un préschéma formel localement'",
    "'(resp.' roman inside the italic statement", "formel (resp. un préschéma formel",
    "convention", 6, "high", "formel (resp. un", r"formel \textup{(resp.} un", RESP)
add(185, "Corollaire (10.4.4), first parenthesis: 'localement noethérien, resp. noethérien), l'espace'",
    "second 'resp.' (and its comma) roman inside the italic statement", "noethérien, resp. noethérien), l'espace",
    "convention", 6, "high", "noethérien, resp. noethérien), l'espace",
    r"noethérien, \textup{resp.} noethérien), l'espace", RESP)
add(185, "Corollaire (10.4.4), second parenthesis: 'encore un préschéma formel (resp. un préschéma formel'",
    "'(resp.' roman inside the italic statement", "formel" + NL + "(resp. un",
    "convention", 6, "high", "formel" + NL + "(resp. un", "formel" + NL + r"\textup{(resp.} un",
    RESP + " The 'old' spans the line break after 'formel'.")
add(185, "Corollaire (10.4.4), second parenthesis: 'localement noethérien, resp. noethérien).'",
    "second 'resp.' roman inside the italic statement", "noethérien, resp. noethérien).",
    "convention", 6, "high", "noethérien, resp. noethérien).", r"noethérien, \textup{resp.} noethérien).", RESP)

# ---------------- page 186 ----------------
add(186, "first paragraph: 'd'espaces topologiquement annelés (0, 4.1.1))'",
    "(0, 4.1.1) with the chapter number 0 in bold", "{0, 4.1.1}",
    "convention", 2, "high", "{0, 4.1.1}", r"{\textbf{0}, 4.1.1}", BOLD0)

# ---------------- page 187 ----------------
add(187, "(10.5.1), second paragraph: 'soit un système fondamental d'Idéaux de définition (10.3.6) du schéma formel affine'",
    "(10.3.6)", r"définition (\hyperref[I.10.3.6-fr]{10.3.6}) du schéma formel affine",
    "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading (checked on a crop). 'Système fondamental d'Idéaux de définition' of an "
    "affine formal scheme is defined in (10.3.7) (p. 185), as the next sentence of the print says ('la "
    "définition donnée dans (10.3.7)'); (10.3.6) is the statement (𝔍^Δ)^n = (𝔍^n)^Δ, correctly cited at the "
    "end of the same paragraph. The corrected edition (r20 current) already reads 10.3.7.",
    corrected=r"(\hyperref[I.10.3.7-fr]{10.3.7})")
add(187, "Proposition (10.5.3): 'des faisceaux d'anneaux pseudo-discrets (0, 3.8.1) 𝒪_𝔛/𝒥_λ'",
    "reference (0, 3.8.1) upright inside the italic statement",
    r"(\hyperref[0.3.8.1-fr]{0, 3.8.1})",
    "convention", 6, "high", r"(\hyperref[0.3.8.1-fr]{0, 3.8.1})", r"\textup{(\hyperref[0.3.8.1-fr]{0, 3.8.1})}",
    "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop. "
    "Apply before the bold-0 finding for the same reference (that 'old' stays valid after this edit).")
add(187, "Proposition (10.5.3): '(0, 3.8.1)'",
    "(0, 3.8.1) with the chapter number 0 in bold", "{0, 3.8.1}",
    "convention", 2, "high", "{0, 3.8.1}", r"{\textbf{0}, 3.8.1}", BOLD0)
add(187, "proof of (10.5.4): 'du plus grand idéal de définition de A (0, 7.1.6 et 7.1.7)'",
    "(0, 7.1.6 et 7.1.7) with the chapter number 0 in bold", "{0, 7.1.6}",
    "convention", 2, "high", "{0, 7.1.6}", r"{\textbf{0}, 7.1.6}", BOLD0)
add(187, "proof of (10.5.4): 'si U⊃V sont deux ouverts formels affines noethériens de X, le plus grand'",
    "roman capital X, not the Fraktur 𝔛",
    r"noethériens de $\mathfrak{X}$, le plus grand",
    "misprint_in_print", None, "high",
    r"noethériens de $\mathfrak{X}$, le plus grand", r"noethériens de $X$, le plus grand",
    "The TeX silently corrects the print. Checked on a crop at 3x: ordinary roman X. U and V are open formal "
    "affine sets of the formal prescheme 𝔛 of (10.5.4). Same slip as on pp. 185, 188, 189.",
    corrected=r"$\mathfrak{X}$")

# ---------------- page 188 ----------------
add(188, "Proposition (10.5.6): '𝒥 (resp. 𝒦) un Idéal de définition'",
    "'(resp. 𝒦)' roman inside the italic statement", r"$\mathscr{J}$ (resp. $\mathscr{K}$)",
    "convention", 6, "high", r"$\mathscr{J}$ (resp. $\mathscr{K}$)", r"$\mathscr{J}$ \textup{(resp. $\mathscr{K}$)}",
    RESP)
add(188, "Proposition (10.5.6): 'définition de 𝔛 (resp. 𝔜), f : 𝔛→𝔜'",
    "'(resp. 𝔜),' roman inside the italic statement", r"$\mathfrak{X}$ (resp. $\mathfrak{Y}$),",
    "convention", 6, "high", r"$\mathfrak{X}$ (resp. $\mathfrak{Y}$),",
    r"$\mathfrak{X}$ \textup{(resp. $\mathfrak{Y}$)},", RESP)
add(188, "Proposition (10.5.6) (ii): 'où 𝔍 (resp. 𝔎) est un idéal de définition'",
    "'(resp. 𝔎)' roman inside the italic statement", r"$\mathfrak{J}$ (resp." + NL + r"    $\mathfrak{K}$)",
    "convention", 6, "high", r"$\mathfrak{J}$ (resp." + NL + r"    $\mathfrak{K}$)",
    r"$\mathfrak{J}$ \textup{(resp." + NL + r"    $\mathfrak{K}$)}",
    RESP + " The 'old' spans the line break after 'resp.'.")
add(188, "Proposition (10.5.6) (ii): 'idéal de définition de A (resp. B), et f=(ᵃφ, φ̃)'",
    "'(resp. B)' roman inside the italic statement", r"de $A$ (resp. $B$), et",
    "convention", 6, "high", r"de $A$ (resp. $B$), et", r"de $A$ \textup{(resp. $B$)}, et", RESP)
add(188, "Proposition (10.5.6) (ii): 'et f' est alors le morphisme (ᵃφ', φ̃')'",
    "tilde over φ only, prime outside: φ̃'", r"\widetilde{\varphi'}",
    "convention", 8, "high", r"morphisme $({}^a\varphi',\widetilde{\varphi'})$",
    r"morphisme $({}^a\varphi',\widetilde{\varphi}')$",
    "Checked on a crop at 2.5x: the tilde covers the φ and the prime follows it. The exponent here is a prime.")
add(188, "proof of (10.5.6) (i): 'est contenue dans 𝒥 (0, 4.3.5)'",
    "(0, 4.3.5) with the chapter number 0 in bold", "{0, 4.3.5}",
    "convention", 2, "high", "{0, 4.3.5}", r"{\textbf{0}, 4.3.5}", BOLD0)
add(188, "proof of (10.5.6) (i): display 'ω : ψ*(𝒪_𝔜/𝒦) = ψ*(𝒪_𝔜)/ψ*(𝒦) → 𝒪_𝔛/𝒥'",
    "the display ends with 𝒪_𝔛/𝒥, no semicolon; the text goes on 'en outre, ...'",
    r"\to\mathscr{O}_{\mathfrak{X}}/\mathscr{J}~;",
    "punctuation", None, "high", r"\to\mathscr{O}_{\mathfrak{X}}/\mathscr{J}~;",
    r"\to\mathscr{O}_{\mathfrak{X}}/\mathscr{J}",
    "Checked on crops of the whole display line: nothing follows 𝒥. The TeX adds the semicolon.")
add(188, "proof of (10.5.6) (i): 'en outre, comme pour tout x∈X, θ_x^♯ est un homomorphisme local'",
    "roman capital X: x∈X, not x∈𝔛", r"comme pour tout $x\in\mathfrak{X}$,",
    "misprint_in_print", None, "high", r"comme pour tout $x\in\mathfrak{X}$,", r"comme pour tout $x\in X$,",
    "The TeX silently corrects the print. Checked on a crop at 2.5x. The points x are those of the formal "
    "prescheme 𝔛 (f : 𝔛→𝔜); same slip as on pp. 185, 187, 189.",
    corrected=r"$x\in\mathfrak{X}$")
add(188, "proof of (10.5.6) (i): 'Le morphisme d'espaces annelés (ψ, ω^♭) est donc (2.2.1)'",
    "ω with a flat sign ♭ as exponent", r"$(\psi,\omega^b)$",
    "symbol", None, "high", r"$(\psi,\omega^b)$", r"$(\psi,\omega^\flat)$",
    "Checked on a crop at 3x: the flat sign, not a letter b (GLOBAL_ISSUES item 14; earlier pages fixed with \\flat).")
add(188, "proof of (10.5.6) (ii): 'entraîne que l'on a f'=(ᵃφ', φ̃'), où φ' : B/𝔎→A/𝔍'",
    "tilde over φ only, prime outside: φ̃'", r"\widetilde{\varphi'}",
    "convention", 8, "high", r"$f'=({}^a\varphi',\widetilde{\varphi'})$, où",
    r"$f'=({}^a\varphi',\widetilde{\varphi}')$, où",
    "Checked on a crop at 2x.")
add(188, "proof of (10.5.6) (ii): 'et posant f'=(ᵃφ', φ̃'), il est clair'",
    "tilde over φ only, prime outside: φ̃'", r"\widetilde{\varphi'}",
    "convention", 8, "high", r"$f'=({}^a\varphi',\widetilde{\varphi'})$, il est",
    r"$f'=({}^a\varphi',\widetilde{\varphi}')$, il est",
    "Checked on a crop at 2.5x.")
add(188, "last paragraph: 'la correspondance f→f' définie ci-dessus est fonctorielle'",
    "plain arrow: f→f'", r"$f\mapsto f'$",
    "convention", 3, "high", r"$f\mapsto f'$", r"$f\to f'$", "Checked on a crop at 3x.")
add(188, "page end, (10.6.1): '... définit un morphisme' / p. 189 'canonique f_μλ : ...'",
    "one sentence running across the page break: p. 189 begins 'canonique f_μλ' flush left, as a continuation line",
    "définit un morphisme + blank line + \\oldpage[I]{189} + blank line + canonique",
    "other", None, "high", "définit un morphisme" + NL + NL, "définit un morphisme" + NL,
    "Spurious paragraph break inside the sentence '... définit un morphisme canonique f_μλ ...'. The blank "
    "line before the marker is in this page's segment; the one after it is removed by the p. 189 finding. "
    "\\oldpage ends with \\ignorespaces, so the two edits give 'morphisme canonique'.")

# ---------------- page 189 ----------------
add(189, "page start, (10.6.1): 'canonique f_μλ : (𝔛, 𝒪_𝔛/𝒥_λ) → ...'",
    "'canonique' starts flush left: continuation of the sentence from p. 188, not a new paragraph",
    r"\oldpage[I]{189} + blank line + canonique",
    "other", None, "high", r"\oldpage[I]{189}" + NL + NL + "canonique", r"\oldpage[I]{189}" + NL + "canonique",
    "Second half of the spurious paragraph break; see the last p. 188 finding.")
add(189, "(10.6.1): 'constituent donc (en vertu de (10.4.8)) un système inductif'",
    "(en vertu de (10.4.8)): the reference has its own parentheses", r"(en vertu de" + NL + r"\hyperref[I.10.4.8-fr]{10.4.8})",
    "punctuation", None, "high", r"(en vertu de" + NL + r"\hyperref[I.10.4.8-fr]{10.4.8})",
    r"(en vertu de" + NL + r"(\hyperref[I.10.4.8-fr]{10.4.8}))",
    "Inner pair of parentheses missing in the TeX (checked on a crop).")
add(189, "Proposition (10.6.2): 'Avec les notations de (10.6.1), le préschéma formel'",
    "reference (10.6.1) upright inside the italic statement", r"(\hyperref[I.10.6.1-fr]{10.6.1})",
    "convention", 6, "high", r"(\hyperref[I.10.6.1-fr]{10.6.1})", r"\textup{(\hyperref[I.10.6.1-fr]{10.6.1})}",
    "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop.")
add(189, "Proposition (10.6.2): 'une limite inductive (T, I, 1.8) du système'",
    "reference (T, I, 1.8) upright inside the italic statement", "(T, I, 1.8)",
    "convention", 6, "high", "(T, I, 1.8)", r"\textup{(T, I, 1.8)}",
    "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop.")
add(189, "proof of (10.6.2): 'les homomorphismes θ_λ^♯ : ψ*(𝒪_𝔜) → 𝒪_{X_i} = 𝒪_𝔛/𝒥_λ'",
    "subscript X_i (index i, not λ)", r"\mathscr{O}_{X_\lambda}=",
    "misprint_in_print", None, "high", r"\mathscr{O}_{X_\lambda}=", r"\mathscr{O}_{X_i}=",
    "The TeX silently corrects the print. Checked on a crop at 3x: italic i under the X. Everything else in "
    "(10.6.1)-(10.6.2) is indexed by λ (X_λ = (𝔛, 𝒪_𝔛/𝒥_λ)).",
    corrected=r"\mathscr{O}_{X_\lambda}")
add(189, "proof of (10.6.2): 'on en déduit donc un homomorphisme ω : ψ*(𝒪_𝔜) → lim 𝒪_𝔛/𝒥_λ = 𝒪_𝔛, et il est clair'",
    "the formula is set inline in the running text, not displayed",
    r"\[ \omega:\psi^*(\mathscr{O}_{\mathfrak{Y}})\to \varprojlim\mathscr{O}_{\mathfrak{X}}/\mathscr{J}_\lambda =\mathscr{O}_{\mathfrak{X}}, \]",
    "other", None, "low",
    r"\[" + NL + r"  \omega:\psi^*(\mathscr{O}_{\mathfrak{Y}})\to" + NL
    + r"  \varprojlim\mathscr{O}_{\mathfrak{X}}/\mathscr{J}_\lambda" + NL
    + r"  =\mathscr{O}_{\mathfrak{X}}," + NL + r"\]" + NL + "et il est clair",
    r"$\omega:\psi^*(\mathscr{O}_{\mathfrak{Y}})\to" + NL
    + r"  \varprojlim\mathscr{O}_{\mathfrak{X}}/\mathscr{J}_\lambda" + NL
    + r"  =\mathscr{O}_{\mathfrak{X}}$," + NL + "et il est clair",
    "Layout only (display vs inline); the formula itself matches. In the print the line reads "
    "'ω : ψ*(𝒪_𝔜) → lim 𝒪_𝔛/𝒥_λ = 𝒪_𝔛, et il est clair que le morphisme g = (ψ, ω^♭) d'espaces annelés'.")
add(189, "proof of (10.6.2): 'le morphisme g=(ψ, ω^♭) d'espaces annelés'",
    "ω with a flat sign ♭ as exponent", r"$g=(\psi,\omega^b)$",
    "symbol", None, "high", r"$g=(\psi,\omega^b)$", r"$g=(\psi,\omega^\flat)$",
    "Checked on a crop: the flat sign, as on p. 188 (GLOBAL_ISSUES item 14).")
add(189, "Proposition (10.6.3), condition a)",
    "label 'a)' upright (roman) before the italic condition", r"\item[a)]",
    "italics", None, "high", r"\item[a)]", r"\item[\textup{a)}]",
    "Checked on a crop at 1.8x: the labels a), b), c) of (10.6.3) are roman. Inside the italic proposition "
    "environment \\item[a)] comes out italic (cf. GLOBAL_ISSUES item 16, where lettered labels were italic in "
    "Lemme (1.3.2); here they are upright).")
add(189, "Proposition (10.6.3), condition b)",
    "label 'b)' upright (roman)", r"\item[b)]",
    "italics", None, "high", r"\item[b)]", r"\item[\textup{b)}]", None)
add(189, "Proposition (10.6.3), condition c)",
    "label 'c)' upright (roman)", r"\item[c)]",
    "italics", None, "high", r"\item[c)]", r"\item[\textup{c)}]", None)
add(189, "Proposition (10.6.3) b): 'Pour tout x∈X et tout i, il existe un voisinage ouvert U_i de x dans 𝔛'",
    "roman capital X: x∈X", r"Pour tout $x\in X$ et tout $i$",
    "misprint_in_print", None, "medium", None, None,
    "The TeX keeps the printed reading. The space in (10.6.3) is 𝔛 (U_i is a neighbourhood 'de x dans 𝔛'; "
    "no X is defined there). Same roman-X-for-𝔛 slip as on pp. 185, 187, 188, where the TeX corrected it "
    "silently. The corrected edition (r20 current) still has x∈X.",
    corrected=r"Pour tout $x\in\mathfrak{X}$ et tout $i$")

# ---------------- checks ----------------
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = rel[s: cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]

ok = True
for x in F:
    if not x["fix"]:
        continue
    page_txt = (RUN / f"page_{x['page']}.tex").read_bytes().decode("utf-8")
    old = x["fix"]["old"]
    c1 = page_txt.count(old)
    c2 = seg[x["page"]].count(old.replace("\r\n", "\n"))
    if c1 != 1 or c2 != 1:
        ok = False
        print("PROBLEM", x["page"], repr(old), c1, c2)

# sequential application check within each release segment (as apply_fixes.py would do)
for p in sorted(set(x["page"] for x in F)):
    s = seg[p]
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        o = x["fix"]["old"].replace("\r\n", "\n")
        n = x["fix"]["new"].replace("\r\n", "\n")
        if s.count(o) != 1:
            ok = False
            print("SEQ PROBLEM", p, repr(o), s.count(o))
            continue
        s = s.replace(o, n)

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
print("all checks ok" if ok else "CHECK FAILURES")
for p in range(185, 190):
    print(p, {k: cnt[(p, k)] for k in ("normal", "convention", "misprint")})
print("total", len(F))
