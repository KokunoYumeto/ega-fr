import json
import pathlib
import re

RUN = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_II")
OUT = RUN / "findings_207_211.json"
REL = pathlib.Path(r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega2/ega2-indexes-and-contents-fr.tex")
NL = "\n"


def F(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 207 ----------------
    F(207, "Index des notations, entry 1.7.4 (second item)",
      "S(\u2130), S_A(\u2130) (\u2130 \U0001d49c-Module) : 1.7.4 \u2014 the subscript of the second bold S is a roman A (the body, (1.7.4) on p. 15, prints S with script \U0001d49c)",
      r"\mathbf{S}_{\mathcal{A}}(\mathcal{E})",
      "misprint_in_print", None, "high",
      {"old": r"\mathbf{S}_{\mathcal{A}}(\mathcal{E})", "new": r"\mathbf{S}_A(\mathcal{E})"},
      "Wrong-font letter in the print (E is an A-Module with script A, so the subscript should be script A as in (1.7.4)). "
      "The TeX silently corrects it; the diplomatic text should keep the printed roman A.",
      corrected=r"\mathbf{S}_{\mathcal{A}}(\mathcal{E})"),
    F(207, "entry 2.3.10",
      "i_+(Y) (Y partie de Proj(S)) : 2.3.10 \u2014 a roman i (same glyph as the i of 'partie' in the same line); the body (2.3.10), p. 27, prints Fraktur j_+(Y)",
      r"$\mathfrak j_+(Y)$",
      "misprint_in_print", None, "high",
      {"old": r"$\mathfrak j_+(Y)$", "new": r"$\mathrm{i}_+(Y)$"},
      "Wrong letter/font in the print (roman i for Fraktur j). The TeX silently corrects it; the diplomatic text should keep the roman i.",
      corrected=r"$\mathfrak j_+(Y)$"),
    F(207, "entry 2.5.4",
      "(u homomorphisme de degr\u00e9 0) : 2.5.4 (figure 0, old-style)",
      r"($u$ homomorphisme de degré zéro)",
      "word", None, "high",
      {"old": "de degré zéro", "new": r"de degré $0$"},
      "The print has the figure 0, not the word; written 'de degré $0$' as in the body (2.5.x)."),
    F(207, "entry 2.6.2",
      "\u03b1_n, \u03b1, \u03b1_M (homomorphismes canoniques) : 2.6.2 \u2014 roman M subscript (the graded S-module M of \u00a72)",
      r"\alpha_n,\alpha,\alpha_{\mathcal{M}}",
      "font", None, "high",
      {"old": r"\alpha_{\mathcal{M}}$ (homomorphismes canoniques) : \hyperref[II.2.6.2",
       "new": r"\alpha_M$ (homomorphismes canoniques) : \hyperref[II.2.6.2"},
      "Script M is right only in the 3.3.2 entry (end of the page), which the TeX has correctly."),
    F(207, "entry 3.3.1",
      "bold \u0393: \u0393_*(\u2131) (\u2131 \U0001d4aa_X-Module, X = Proj(\U0001d4ae)) : 3.3.1 (the 2.6.1 entry has a plain \u0393)",
      r"$\Gamma_*(\mathcal{F})$ ($\mathcal{F}$ $\mathcal{O}_X$-Module, $X=\Proj(\mathcal{S})$)",
      "font", None, "high",
      {"old": r"$\Gamma_*(\mathcal{F})$ ($\mathcal{F}$ $\mathcal{O}_X$-Module," + NL + r"$X=\Proj(\mathcal{S})$)",
       "new": r"$\bbGamma_*(\mathcal{F})$ ($\mathcal{F}$ $\mathcal{O}_X$-Module," + NL + r"$X=\Proj(\mathcal{S})$)"},
      "Bold Gamma for the graded O_Y-Module Gamma_* of (3.3.1), as in the body; the 2.6.1 entry stays plain."),
    F(207, r"\newcommand{\egaShProj} at the head of the Index des notations (its uses are on p. 208: entries 8.12.1 and 8.14.6)",
      "\U0001d4abroj_0(\u2133), \U0001d4abroj(\u2133), \U0001d4abroj'(\u2133): script P followed by italic 'roj' (as in the body, p. 192)",
      r"\mathcal{P}\!\operatorname{roj} (upright roj)",
      "font", None, "high",
      {"old": r"\newcommand{\egaShProj}{\mathcal{P}\!\operatorname{roj}}",
       "new": r"\newcommand{\egaShProj}{\mathcal{P}\!\mathit{roj}}"},
      "The difference shows on p. 208; the macro definition lies in p. 207's segment, so the edit is filed under p. 207."),
    # ---------------- page 208 ----------------
    F(208, "entry for the hat of S (8.3.1)",
      "\U0001d4ae^ (\U0001d4ae \U0001d4aa_Y-Alg\u00e8bre gradu\u00e9e) : 3.8.1.",
      r"\hyperref[II.8.3.1-fr]{3.8.1}",
      "misprint_in_print", None, "high", None,
      "Transposed reference in the print (3.8.1 for 8.3.1). The TeX keeps the printed number as link text; its link target is already 8.3.1.",
      corrected=r"\hyperref[II.8.3.1-fr]{8.3.1}"),
    F(208, "entry 6.5.3",
      "(h' homomorphisme de \u212c-modules inversibles) : 6.5.3 \u2014 lowercase 'modules'",
      r"($h'$ homomorphisme de $\mathcal{B}$-modules inversibles)",
      "misprint_in_print", None, "medium", None,
      "The TeX keeps the printed lowercase. The body (6.5.3) and the 6.5.2 entry write B-Modules (sheaves, capital M).",
      corrected=r"$\mathcal{B}$-Modules inversibles"),
    F(208, "entry 8.14.5",
      "bold \u0393: \u0393_*(\u2131) (X = Proj(\U0001d4ae), \u2131 \U0001d4ae_X-Module gradu\u00e9) : 8.14.5",
      r"$\Gamma_*(\mathcal{F})$",
      "font", None, "high",
      {"old": r"$\Gamma_*(\mathcal{F})$", "new": r"$\bbGamma_*(\mathcal{F})$"},
      "Bold Gamma, as for the graded O_Y-Module Gamma_* of section 3."),
    F(208, "entry 8.14.6",
      "bold \u0393 with prime: \u0393'_*(\u2131')",
      r"\Gamma'_*(\mathcal{F}')",
      "font", None, "high",
      {"old": r"\Gamma'_*(\mathcal{F}')", "new": r"\bbGamma'_*(\mathcal{F}')"},
      "Same bold Gamma as in 8.14.5."),
    # ---------------- page 209 ----------------
    F(209, r"\newcommand{\egaTerme} at the head of the Index terminologique (every entry of pp. 209-211)",
      "index terms printed in roman (regular weight), e.g. 'Affine (morphisme) : 1.6.1.'; only (TF)/(TN) in the 3.4.2 and 3.6.1 entries are bold",
      r"\newcommand{\egaTerme}[2]{\textbf{#1} : #2.\par} (every term bold)",
      "font", None, "high",
      {"old": r"\newcommand{\egaTerme}[2]{\textbf{#1} : #2.\par}",
       "new": r"\newcommand{\egaTerme}[2]{#1 : #2.\par}"},
      "One edit for all 105 entries of pp. 209-211; apply together with the bold (TF)/(TN) fixes on pp. 209 and 211."),
    F(209, "entry 'Condition (TF), condition (TN) : 3.4.2'",
      "Condition (TF), condition (TN) : 3.4.2 \u2014 TF and TN bold, parentheses roman (the 2.7.2 entry above is all roman)",
      r"\egaTerme{Condition (TF), condition (TN)}{\hyperref[II.3.4.2-fr]{3.4.2}}",
      "font", None, "high",
      {"old": r"\egaTerme{Condition (TF), condition (TN)}{\hyperref[II.3.4.2-fr]",
       "new": r"\egaTerme{Condition (\textbf{TF}), condition (\textbf{TN})}{\hyperref[II.3.4.2-fr]"},
      r"Visible once the \egaTerme macro no longer sets the whole term bold."),
    # ---------------- page 210 ----------------
    F(210, "entry 4.2.6 (Fibre g\u00e9om\u00e9trique rationnelle ...)",
      "... extension K de k(y) : 4.2.6 \u2014 bold italic k",
      r"$k(y)$",
      "convention", 1, "high",
      {"old": r"$k(y)$", "new": r"$\boldsymbol{k}(y)$"},
      "Residue field with bold italic k."),
    F(210, "entry 4.5.1 (Morphisme canonique G(\u03b5) \u2192 Proj(S) ...)",
      "Morphisme canonique G(\u03b5) \u2192 Proj(S) (S = \u2295_{n\u2a7e0} \u0393(X, \u2112^{\u2297n})) : 4.5.1 \u2014 large parentheses around S = ..., no comma",
      r"\Proj(S)$, $S=\bigoplus_{n\geq0}\Gamma(X,\mathcal{L}^{\otimes n})$",
      "punctuation", None, "high",
      {"old": r"\Proj(S)$, $S=\bigoplus_{n\geq0}\Gamma(X,\mathcal{L}^{\otimes n})$",
       "new": r"\Proj(S)$ $\bigl(S=\bigoplus_{n\geq0}\Gamma(X,\mathcal{L}^{\otimes n})\bigr)$"},
      "The print encloses the definition of S in parentheses; the TeX has a comma instead."),
    # ---------------- page 211 ----------------
    F(211, "entry '(TN)-injectif, (TN)-surjectif, (TN)-bijectif (homomorphisme de S-Modules gradu\u00e9s) : 3.4.2'",
      "the three TN bold, parentheses roman (the 2.7.2 and 2.9.1 entries above are roman)",
      r"(TN)-injectif, (TN)-surjectif, (TN)-bijectif (homomorphisme de $\mathcal{S}$-Modules gradués)",
      "font", None, "high",
      {"old": r"(TN)-injectif, (TN)-surjectif, (TN)-bijectif (homomorphisme de $\mathcal{S}$-Modules",
       "new": r"(\textbf{TN})-injectif, (\textbf{TN})-surjectif, (\textbf{TN})-bijectif (homomorphisme de $\mathcal{S}$-Modules"},
      r"Written (\textbf{TN}) as in the body of section 3.6; apply with the \egaTerme fix on p. 209."),
    F(211, "entry '(TN)-isomorphisme de S-Modules gradu\u00e9s : 3.4.2'",
      "TN bold",
      r"(TN)-isomorphisme de $\mathcal{S}$-Modules gradués",
      "font", None, "high",
      {"old": r"(TN)-isomorphisme de $\mathcal{S}$-Modules",
       "new": r"(\textbf{TN})-isomorphisme de $\mathcal{S}$-Modules"},
      r"Apply with the \egaTerme fix on p. 209."),
    F(211, "entry '(TN)-injectif, (TN)-surjectif, (TN)-bijectif (homomorphisme de O_Y-Alg\u00e8bres gradu\u00e9es) : 3.6.1'",
      "the three TN bold",
      r"(TN)-injectif, (TN)-surjectif, (TN)-bijectif (homomorphisme de $\mathcal{O}_Y$-Algèbres graduées)",
      "font", None, "high",
      {"old": r"(TN)-injectif, (TN)-surjectif, (TN)-bijectif (homomorphisme de $\mathcal{O}_Y$",
       "new": r"(\textbf{TN})-injectif, (\textbf{TN})-surjectif, (\textbf{TN})-bijectif (homomorphisme de $\mathcal{O}_Y$"},
      r"Apply with the \egaTerme fix on p. 209."),
    F(211, "entry '(TN)-isomorphisme de O_Y-Alg\u00e8bres gradu\u00e9es : 3.6.1'",
      "TN bold",
      r"(TN)-isomorphisme de $\mathcal{O}_Y$-Algèbres graduées",
      "font", None, "high",
      {"old": r"(TN)-isomorphisme de $\mathcal{O}_Y$",
       "new": r"(\textbf{TN})-isomorphisme de $\mathcal{O}_Y$"},
      r"Apply with the \egaTerme fix on p. 209."),
]

json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# checks: every "old" occurs exactly once in its page_NNN.tex (CRLF normalised) and in its page segment of the release file
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
seg = {n: rel[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(rel))] for i, (n, s) in enumerate(cuts)}
ok = True
for x in findings:
    if not x["fix"]:
        continue
    old = x["fix"]["old"]
    t = (RUN / f"page_{x['page']}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c1 = t.count(old)
    c2 = seg[x["page"]].count(old)
    if c1 != 1 or c2 != 1:
        ok = False
    print(x["page"], c1, c2, old[:70].replace("\n", "\\n"))
counts = {}
for x in findings:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("ALL UNIQUE" if ok else "PROBLEM", counts)
