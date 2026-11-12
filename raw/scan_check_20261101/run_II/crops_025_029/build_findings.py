import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_025_029.json"
NL = "\n"


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def bold_ref(page, where, label, chap, num):
    old = r"(\hyperref[" + label + "]{" + chap + ", " + num + "})"
    new = r"(\hyperref[" + label + r"]{\textbf{" + chap + "}, " + num + "})"
    return F(page, where, "bold " + chap, old, "convention", 2, "high", old, new)


findings = []

# ---------------- page 25 ----------------
findings += [
    F(25, "proof of (2.2.5), line 3: 'ce qui donne finalement f^{k-n}x=0'",
      "f^{k−n}x=0 (exponent k−n)",
      r"$f^{k-n+1}x=0$",
      "misprint_in_print", None, "high",
      r"f^{k-n+1}x=0", r"f^{k-n}x=0",
      "Read on a zoomed crop: the exponent is k−n. From x=−y_{nd}, y_{(j+1)d}=fy_{jd} and fy_{kd}=0 one gets "
      "y_{kd}=−f^{k−n}x, hence f^{k−n+1}x=0; f^{k−n}x=−y_{kd} need not vanish (k=n, x=−y_{nd} with fy_{nd}=0). "
      "The TeX silently corrects the print; the fix restores the printed reading.",
      corrected=r"f^{k-n+1}x=0"),
    F(25, "proof of (2.2.5), line 1: 'y=y_{hd}+y_{(h+1)d}+...+y_{kd}'",
      "baseline dots: + . . . +",
      r"+\cdots+",
      "formula", None, "high",
      r"y_{(h+1)d}+\cdots+y_{kd}", r"y_{(h+1)d}+\ldots+y_{kd}",
      "Checked on a crop and by ink profile: the dots sit on the baseline of the neighbouring word 'avec', "
      "below the bar of the + signs."),
    bold_ref(25, "(2.2.7): 'On sait (0, 1.4.5) que'", "0.1.4.5-fr", "0", "1.4.5"),
    bold_ref(25, "(2.3.2): 'De (I, 1.1.2) on déduit donc'", "I.1.1.2-fr", "I", "1.1.2"),
    F(25, "display (2.3.2.3): 'V_+(EE')=V_+(E)∪V_+(E').'",
      "final period after the display",
      r"V_+(EE')=V_+(E)\cup V_+(E') (no period)",
      "punctuation", None, "high",
      r"V_+(EE')=V_+(E)\cup V_+(E')", r"V_+(EE')=V_+(E)\cup V_+(E').",
      "Checked on a crop. Minor."),
]

# ---------------- page 26 ----------------
findings += [
    F(26, "display (2.3.2.5): 'V_+(𝔍)=V_+(𝔯_+(𝔍)).'",
      "Fraktur 𝔯_+ (the radical), like the Fraktur 𝔍 beside it",
      r"V_+(r_+(\mathfrak{J}))",
      "font", None, "high",
      r"V_+(r_+(\mathfrak{J}))", r"V_+(\mathfrak{r}_+(\mathfrak{J}))",
      "Checked on a zoomed crop: Fraktur r, not the italic r of f^r x on the same page. Chapter 0 writes the "
      "radical as \\mathfrak{r}, and the preamble's \\rad is \\mathfrak{r}. ega2-1-fr.tex types this letter "
      "as italic r at lines 1617, 1621 (r_+ and r), 1865 and 2016."),
    F(26, "display (2.3.3.1): 'D_+(f)=D(f)∩Proj(S)=Proj(S)—V_+(f)'",
      "long dash for set difference: Proj(S)—V_+(f)",
      r"\operatorname{Proj}(S)\setminus V_+(f)",
      "symbol", None, "high",
      r"\operatorname{Proj}(S)\setminus V_+(f)", r"\operatorname{Proj}(S)\setmin V_+(f)",
      "Checked on a crop. The convention-7 dash, but the TeX has \\setminus (∖) rather than a minus sign, so "
      "it is listed as a symbol difference. \\setmin is the macro earlier fixes use for the print's dash "
      "(preamble-base.tex line 22, '-' for now; GLOBAL_ISSUES item 5). The only \\setminus in ega2-1-fr.tex."),
    bold_ref(26, "(2.3.3): 'pour deux éléments f, g de S (I, 1.1.9.1)'", "I.1.1.9.1-fr", "I", "1.1.9.1"),
    bold_ref(26, "(2.3.5): 'l'anneau de fractions S_f (0, 1.2.6)'", "0.1.2.6-fr", "0", "1.2.6"),
    F(26, "(2.3.5): 'c'est l'ensemble des x/f^n, pour n≥0, x∈𝔭∩S_{nd}'",
      "comma after x/f^n",
      r"des $x/f^n$ pour $n\geq 0$",
      "punctuation", None, "high",
      r"c'est l'ensemble des $x/f^n$ pour", r"c'est l'ensemble des $x/f^n$, pour",
      "Checked on a crop."),
    bold_ref(26, "(2.3.5): 'ω=ω_{fg,f} : S_(f)→S_(fg) (I, 1.2.1)'", "I.1.2.1-fr", "I", "1.2.1"),
    F(26, "proof of (2.3.6): 'donc ψ_f^{-1}(D(h/f^n))=D_+(hf) et notre assertion'",
      "the formula is in the running text",
      r"displayed with \[ ... \]",
      "other", None, "high",
      NL.join([r"donc", r"\[", r"  \psi_f^{-1}(D(h/f^n))=D_+(hf)", r"\]", r"et notre"]),
      NL.join([r"donc $\psi_f^{-1}(D(h/f^n))=D_+(hf)$", r"et notre"]),
      "Layout only (display vs inline); the formula itself matches."),
]

# ---------------- page 27 ----------------
findings += [
    F(27, "Corollaire (2.3.8), item a)", "label a) italic", r"\item[\rm a)] (upright)",
      "italics", None, "high", r"\item[\rm a)]", r"\item[\textit{a)}]",
      "Checked on a crop. Lettered labels are italic in the print (GLOBAL_ISSUES item 16); \\textit rather "
      "than \\emph because the corollary body is italic."),
    F(27, "Corollaire (2.3.8), item b)", "label b) italic", r"\item[\rm b)] (upright)",
      "italics", None, "high", r"\item[\rm b)]", r"\item[\textit{b)}]", "As for a)."),
    F(27, "Corollaire (2.3.8), item c)", "label c) italic", r"\item[\rm c)] (upright)",
      "italics", None, "high", r"\item[\rm c)]", r"\item[\textit{c)}]", "As for a)."),
    F(27, "proof of (2.3.8): 'Il est clair que c) entraîne b) et que b) entraîne a).'",
      "the four labels c), b), b), a) italic in the roman text",
      "c) entraîne b) et que b) entraîne a) (upright)",
      "italics", None, "high",
      "que c) entraîne b) et que b) entraîne a).",
      r"que \emph{c)} entraîne \emph{b)} et que \emph{b)} entraîne \emph{a)}.",
      "Checked on a crop."),
    F(27, "proof of (2.3.8): 'la condition a) équivaut à V_+(𝔍)=X'",
      "label a) italic", "la condition a) équivaut (upright)",
      "italics", None, "high",
      "la condition a) équivaut", r"la condition \emph{a)} équivaut",
      "Checked on a crop."),
    F(27, "proof of (2.3.8): 'a fortiori, a) entraîne que tout élément'",
      "label a) italic (as is 'a fortiori')", r"\emph{a fortiori}, a) entraîne",
      "italics", None, "high",
      r"\emph{a fortiori}, a) entraîne", r"\emph{a fortiori}, \emph{a)} entraîne",
      "Checked on a crop."),
    F(27, "Corollaire (2.3.9): '𝔯_+(𝔍) est l'intersection des idéaux premiers gradués'",
      "Fraktur 𝔯_+", r"$r_+(\mathfrak{J})$",
      "font", None, "high",
      r"$r_+(\mathfrak{J})$", r"$\mathfrak{r}_+(\mathfrak{J})$",
      "Checked on a zoomed crop; same letter as in (2.3.2.5), p. 26."),
    F(27, "Corollaire (2.3.12): 'les applications décroissantes Y→𝔧_+(Y)'",
      "plain arrow →", r"$Y\longmapsto\mathfrak{j}_+(Y)$",
      "convention", 3, "high",
      r"$Y\longmapsto\mathfrak{j}_+(Y)$", r"$Y\to\mathfrak{j}_+(Y)$"),
    F(27, "Corollaire (2.3.12): '𝔍→V_+(𝔍)'",
      "plain arrow →", r"$\mathfrak{J}\longmapsto V_+(\mathfrak{J})$",
      "convention", 3, "high",
      r"\mathfrak{J}\longmapsto" + NL + r"V_+(\mathfrak{J})$",
      r"\mathfrak{J}\to" + NL + r"V_+(\mathfrak{J})$"),
]

# ---------------- page 28 ----------------
enum_old = NL.join([
    r"\begin{enumerate}",
    r"  \item[\rm a)] $D_+(f)\subset\bigcup_\alpha D_+(f_\alpha)$~;",
    r"  \item[\rm b)] $V_+(f)\supset\bigcap_\alpha V_+(f_\alpha)$~;",
    r"  \item[\rm c)] une puissance de $f$ appartient à l'idéal engendré par les",
    r"    $f_\alpha$.",
    r"\end{enumerate}",
])
enum_new = NL.join([
    r"\textit{a)} $D_+(f)\subset\bigcup_\alpha D_+(f_\alpha)$~;",
    r"\textit{b)} $V_+(f)\supset\bigcap_\alpha V_+(f_\alpha)$~;",
    r"\textit{c)} une puissance de $f$ appartient à l'idéal engendré par les",
    r"$f_\alpha$.",
])
findings += [
    F(28, "Corollaire (2.3.15): the three relations a), b), c)",
      "run-in in the statement paragraph ('... sont équivalentes : a) D_+(f)⊂... ; b) ... ; c) ...'), "
      "with italic labels a), b), c)",
      r"enumerate list with \item[\rm a)] etc. (upright labels on separate lines)",
      "other", None, "high", enum_old, enum_new,
      "Checked on a crop. One edit for both differences (run-in layout and italic labels)."),
    F(28, "Corollaire (2.3.17): 'décrite dans (2.3.12), aux parties fermées'",
      "(2.3.12) upright in the italic statement",
      r"(\hyperref[II.2.3.12-fr]{2.3.12}) inside the italic corollary",
      "convention", 6, "high",
      r"(\hyperref[II.2.3.12-fr]{2.3.12})",
      r"\textup{(\hyperref[II.2.3.12-fr]{2.3.12})}"),
    F(28, "Corollaire (2.3.17): 'les idéaux gradués premiers dans S_+'",
      "'premiers' roman (emphasis) in the italic statement",
      "premiers (italic like the rest)",
      "italics", None, "high",
      "gradués premiers dans", r"gradués \emph{premiers} dans",
      "Checked on a crop."),
    bold_ref(28, "(2.4.1): 'est une immersion ouverte (I, 1.3.6)'", "I.1.3.6-fr", "I", "1.3.6"),
    bold_ref(28, "proof of (2.4.2): 'Il suffit (I, 5.5.6) de montrer'", "I.5.5.6-fr", "I", "5.5.6"),
]

# ---------------- page 29 ----------------
findings += [
    bold_ref(29, "Exemple (2.4.3): 'décrit dans (I, 2.3.2) (cf. (7.4.14))'", "I.2.3.2-fr", "I", "2.3.2"),
    F(29, "Proposition (2.4.4)(i): 'le nilradical de S_+ (2.1.10), le schéma X_red'",
      "(2.1.10) upright in the italic statement",
      r"(\hyperref[II.2.1.10-fr]{2.1.10}) inside the italic proposition",
      "convention", 6, "high",
      r"(\hyperref[II.2.1.10-fr]{2.1.10})",
      r"\textup{(\hyperref[II.2.1.10-fr]{2.1.10})}"),
    F(29, "Proposition (2.4.4)(i): 'si S est essentiellement réduit, Proj(S) est réduit'",
      "essentiellement réduit", "essentiellement réduite",
      "word", None, "high",
      "essentiellement réduite,", "essentiellement réduit,",
      "Checked on a crop."),
    F(29, "proof of (2.4.4)(i): 'désignons par x→x̄ l'homomorphisme canonique'",
      "plain arrow →", r"$x\mapsto\overline{x}$",
      "convention", 3, "high",
      r"$x\mapsto\overline{x}$", r"$x\to\overline{x}$"),
    F(29, "proof of (2.4.4)(i): 'l'homomorphisme canonique S_f→S̄_{f̄} (0, 1.5.1)'",
      "S_f→S̄ with no subscript f̄; a short vertical tick follows the S̄ at cap height (end of the line)",
      r"$S_f\to\overline{S}_{\overline{f}}$",
      "misprint_in_print", None, "medium",
      r"$S_f\to\overline{S}_{\overline{f}}$", r"$S_f\to\overline{S}'$",
      "Checked on zoomed and high-contrast crops: no trace of the subscript. The tick sits where a prime "
      "would, but it is thinner and more upright than the print's prime (E' on p. 25); if the coordinator "
      "reads it as a stray mark, the printed reading is $S_f\\to\\overline{S}$. The TeX silently corrects "
      "the print (the localisation of S̄ at f̄ is meant).",
      corrected=r"$S_f\to\overline{S}_{\overline{f}}$"),
    bold_ref(29, "proof of (2.4.4)(i): 'S_f→S̄_{f̄} (0, 1.5.1) est surjectif'", "0.1.5.1-fr", "0", "1.5.1"),
    F(29, "proof of (2.4.4)(i): 'A cet homomorphisme correspond donc'",
      "A without accent", "À cet",
      "word", None, "high",
      "À cet", "A cet",
      "Checked on a crop: the print does not accent the capital (as in 'A fortiori' elsewhere in the "
      "file). ega2-1-fr.tex has one more 'À' at line 1135 ('À un homomorphisme surjectif')."),
    F(29, "proof of (2.4.4)(i): 'à (D_+(f))_red (I, 5.1.2), et est en particulier'",
      "bold I", r"(\hyperref[I.5.1.2-fr]{I, 5.1.2})",
      "convention", 2, "high",
      r"$(D_+(f))_{\mathrm{red}}$ (\hyperref[I.5.1.2-fr]{I, 5.1.2})",
      r"$(D_+(f))_{\mathrm{red}}$ (\hyperref[I.5.1.2-fr]{\textbf{I}, 5.1.2})",
      "First of two identical references on the page; 'old' includes the preceding formula to be unique."),
    F(29, "proof of (2.4.4)(i), diagram: lower right corner S̄_{(f̄ḡ)}",
      "two separate bars, over f and over g: S̄_(f̄ ḡ)",
      r"\overline{S}_{(\overline{fg})} (one bar over fg)",
      "formula", None, "high",
      r"\overline{S}_{(\overline{fg})}", r"\overline{S}_{(\overline{f}\overline{g})}",
      "Checked on a zoomed crop and pixel map: the bar is interrupted between f and g."),
    F(29, "proof of (2.4.4)(i): 'd'où la conclusion (I, 5.1.2)'",
      "bold I", r"(\hyperref[I.5.1.2-fr]{I, 5.1.2})",
      "convention", 2, "high",
      "la conclusion" + NL + r"    (\hyperref[I.5.1.2-fr]{I, 5.1.2})",
      "la conclusion" + NL + r"    (\hyperref[I.5.1.2-fr]{\textbf{I}, 5.1.2})",
      "Second of two identical references on the page; 'old' includes the preceding words to be unique."),
]

# ---------------- verification ----------------
texts = {}
ok = True
for f in findings:
    p = f["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    fx = f["fix"]
    if fx is None:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", p, n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("NO-OP", p, repr(fx["old"]))

# apply all fixes per page on a copy to make sure they do not collide
for p, t in texts.items():
    s = t
    for f in findings:
        if f["page"] == p and f["fix"]:
            if s.count(f["fix"]["old"]) != 1:
                ok = False
                print("COLLISION", p, repr(f["fix"]["old"]))
            s = s.replace(f["fix"]["old"], f["fix"]["new"], 1)

from collections import Counter
cnt = Counter()
for f in findings:
    k = "convention" if f["kind"] == "convention" else ("misprint" if f["kind"] == "misprint_in_print" else "normal")
    cnt[(f["page"], k)] += 1
for p in sorted({f["page"] for f in findings}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("all unique:", ok, "total:", len(findings))

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
