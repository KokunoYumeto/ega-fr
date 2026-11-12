"""Build findings_106_110.json for EGA IV-1 chapter 0, pp. 106-110, and check every fix's "old"."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_106_110.json"


def L(*lines):
    return "\n".join(lines)


def F(page, where, scan, tex, kind, conv, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": ({"old": old, "new": new} if old is not None else None)}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


M106 = r"\oldpage[0\textsubscript{IV-1}]{106}"
M107 = r"\oldpage[0\textsubscript{IV-1}]{107}"
M108 = r"\oldpage[0\textsubscript{IV-1}]{108}"

findings = [
    # ---------------- p. 106 ----------------
    F(106, "top of p. 106: page break inside '... ; mais lim_j((B/m^i)⊗_A(C/n^j)) est le séparé complété de ...'",
      "printed p. 106 begins with 'est le séparé complété de (B/𝔪^i)⊗_A C'; 'mais lim_j((B/𝔪^i)⊗_A(C/𝔫^j))' is the last line of printed p. 105 (checked on the p. 105 strip)",
      "\\oldpage[0\\textsubscript{IV-1}]{106} and a blank line stand before 'mais $\\varprojlim_j(...)$'",
      "marker", None, "high",
      L(M106, "", r"mais $\varprojlim_j((B/\mathfrak m^i)\otimes_A(C/\mathfrak n'{}^j))$ est le"),
      L(r"mais $\varprojlim_j((B/\mathfrak m^i)\otimes_A(C/\mathfrak n^j))$", M106, "est le"),
      "One edit inside the p. 106 segment: the marker moves after 'mais $\\varprojlim_j(...)$' (which then ends the p. 105 "
      "segment), and the blank line after it goes (mid-sentence break, GLOBAL_ISSUES 20). The same edit removes the prime "
      "on 𝔫 (next finding). Do not also apply a p. 105 edit that re-inserts 'mais ...'. The blank line after '\\]' at the "
      "end of the p. 105 segment, which then precedes 'mais', is a paragraph break the print lacks (p. 105 segment)."),
    F(106, "the phrase 'mais lim_j((B/m^i)⊗_A(C/n^j))' (printed at the foot of p. 105, TeX in the p. 106 segment)",
      "(C/𝔫^j): Fraktur n without a prime (enlarged crop of p. 105); the print has 𝔫 throughout the proof of (19.7.1.2) on p. 105: Im(B⊗_A𝔫^j), Im(B⊗_A𝔫), (C/𝔫), (𝔫/𝔫²)",
      "(C/\\mathfrak n'{}^j)", "formula", None, "high", None, None,
      "Fix included in the marker edit above. The p. 105 segment writes \\mathfrak n' in the same proof (about 9 times) "
      "where the print has 𝔫: for the p. 105 check."),
    F(106, "'On a donc E = lim_i((B/m^i)⊗_A C). Pour tout entier'",
      "the formula is inline, in the running line", "displayed with \\[ ... \\]", "other", None, "high",
      L("On a donc", r"\[", r"  E=\varprojlim_i((B/\mathfrak m^i)\otimes_A C).", r"\]", "Pour tout"),
      L("On a donc", r"$E=\varprojlim_i((B/\mathfrak m^i)\otimes_A C)$.", "Pour tout"),
      "Layout: inline in the print, displayed in the TeX (GLOBAL_ISSUES 21)."),
    F(106, "'il est évidemment dense dans lim_i(Im(m^h/m^{h+i})⊗_A C)), donc égal à cette dernière limite projective'",
      "the formula is inline, in the running line", "displayed with \\[ ... \\]", "other", None, "high",
      L("dense dans", r"\[", r"  \varprojlim_i", r"  (\operatorname{Im}(\mathfrak m^h/\mathfrak m^{h+i})\otimes_A C),", r"\]", "donc égal"),
      L("dense dans", r"$\varprojlim_i(\operatorname{Im}(\mathfrak m^h/\mathfrak m^{h+i})\otimes_A C)$,", "donc égal"),
      "Layout only. Apply before the misprint finding for this formula (whose 'old' lies inside the formula and is "
      "unchanged by this edit)."),
    F(106, "same formula: 'lim_i(Im(m^h/m^{h+i})⊗_A C))'",
      "lim_i(Im(𝔪^h/𝔪^{h+i})⊗_A C)): two opening and three closing parentheses (enlarged crop)",
      "(\\operatorname{Im}(\\mathfrak m^h/\\mathfrak m^{h+i})\\otimes_A C): balanced, i.e. the surplus ')' silently dropped",
      "misprint_in_print", None, "high",
      r"\mathfrak m^{h+i})\otimes_A C)", r"\mathfrak m^{h+i})\otimes_A C))",
      "The TeX silently corrects the print; the fix restores the printed reading (one more ')'). Correct reading: the "
      "parenthesis missing is the one after Im (the image of (𝔪^h/𝔪^{h+i})⊗_A C in (B/𝔪^{h+i})⊗_A C, as in "
      "Im(𝔪^h⊗_A C) a few lines below); the TeX's balanced form puts ⊗_A C outside Im.",
      r"\varprojlim_i(\operatorname{Im}((\mathfrak m^h/\mathfrak m^{h+i})\otimes_A C))"),
    F(106, "'que E/m^hE est isomorphe à (B/m^h)⊗_A C = (B⊗_A C)/Im(m^h⊗_A C). En particulier'",
      "the formula is inline, in the running line", "displayed with \\[ ... \\]", "other", None, "high",
      L("isomorphe à", r"\[", r"  (B/\mathfrak m^h)\otimes_A C", r"  =(B\otimes_A C)/\operatorname{Im}(\mathfrak m^h\otimes_A C).", r"\]", "En particulier"),
      L("isomorphe à", r"$(B/\mathfrak m^h)\otimes_A C=(B\otimes_A C)/\operatorname{Im}(\mathfrak m^h\otimes_A C)$.", "En particulier"),
      "Layout: inline in the print, displayed in the TeX (GLOBAL_ISSUES 21). Independent of the next finding."),
    F(106, "'En particulier comme Im(m⊗_A C) ⊂ r, cela montre'",
      "no comma after 'particulier' (enlarged crop)", "En particulier, comme", "punctuation", None, "high",
      "En particulier, comme", "En particulier comme", "Comma added in the TeX."),
    F(106, "Lemme (19.7.1.3): 'on suppose que B_0 est un anneau local noethérien, complet et régulier.'",
      "'régulier.' upright (roman) inside the italic statement; 'complet et' italic (enlarged crop)",
      "italic (statement environment)", "convention", 6, "high",
      "complet et régulier.", r"complet et \textup{régulier}.", ""),
    F(106, "Lemme (19.7.1.3): 'qui est un anneau local noethérien complet, un A-module plat, et tel que'",
      "'plat,' upright (roman) at the start of the line, 'A-module' and 'et tel que' italic (enlarged crop)",
      "italic (statement environment)", "convention", 6, "high",
      L("complet, un $A$-module plat,", "et tel que"), L(r"complet, un $A$-module \textup{plat},", "et tel que"), ""),
    F(106, "proof of (19.7.1.3), case I): 'soit C un anneau local noethérien complet qui est un A-module plat et tel que'",
      "A-module *plat* (plat italic; enlarged crop)", "upright", "italics", None, "high",
      "$A$-module plat et tel que", r"$A$-module \emph{plat} et tel que", ""),
    F(106, "proof of (19.7.1.3), case II): 'K est de caractéristique p>0'",
      "*de caractéristique* (both words italic; enlarged crop)", "de \\emph{caractéristique} ('de' upright)", "italics", None, "high",
      r"de \emph{caractéristique}", r"\emph{de caractéristique}", ""),
    F(106, "proof of (19.7.1.3), last paragraph: 'un anneau local noethérien complet et un W(P)-module plat, tel que'",
      "W(P)-module *plat* (plat italic; enlarged crop)", "upright", "italics", None, "high",
      "$W(P)$-module plat, tel que", r"$W(P)$-module \emph{plat}, tel que", ""),
    F(106, "end of the p. 106 segment: '... par platitude (0_I, 6.3.4) et comme' / p. 107 'W(k)/pW(k) = k, ...'",
      "the sentence runs on: p. 107 begins flush left with 'W(k)/pW(k)=k', no new paragraph",
      "blank line before \\oldpage[0\\textsubscript{IV-1}]{107}: paragraph break", "other", None, "high",
      L("6.3.4) et comme", "", ""), L("6.3.4) et comme", ""),
      "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 107 finding removes the blank line after the marker."),
    # ---------------- p. 107 ----------------
    F(107, "top of p. 107: 'W(k)/pW(k) = k, pW(k) est l'idéal maximal'",
      "continues the sentence from p. 106, flush left", "blank line after the marker: new paragraph", "other", None, "high",
      L(M107, "", "$W(k)/pW(k)=k$"), L(M107, "$W(k)/pW(k)=k$"),
      "Mid-sentence page break (GLOBAL_ISSUES 20); pairs with the p. 106 end-of-segment finding."),
    F(107, "proof of (19.7.1.3): 'donc B est en fait un anneau local. Comme B_P'",
      "anneau *local* (local italic; enlarged crop)", "upright", "italics", None, "high",
      "un anneau local. Comme", r"un anneau \emph{local}. Comme", ""),
    F(107, "end of the p. 107 segment: diagram of the proof of (19.7.1.4), followed on p. 108 by 'où A_0 = A/J = gr_0(A), ...'",
      "p. 108 begins flush left with 'où', continuing the sentence after the diagram",
      "blank line after \\] before the p. 108 marker: paragraph break", "other", None, "high",
      L(r"\gr_\bullet(M)", "}", r"\]", "", ""), L(r"\gr_\bullet(M)", "}", r"\]", ""),
      "Page break inside the sentence (GLOBAL_ISSUES 20/47); the p. 108 finding removes the blank line after the marker."),
    # ---------------- p. 108 ----------------
    F(108, "top of p. 108: 'où A_0 = A/J = gr_0(A), et φ_M et φ_N sont les applications canoniques'",
      "continues the sentence after the diagram, flush left", "blank line after the marker: new paragraph", "other", None, "high",
      L(M108, "", "où"), L(M108, "où"),
      "Pairs with the p. 107 end-of-segment finding."),
    F(108, "Lemme (19.7.1.5): conditions 1°, 2°, 3°",
      "run in the statement's paragraph: 'On suppose que : 1° B et B' sont complets ... ; 2° B est ... lisse; 3° B' est un A-module plat. Posons A_0 = A/J, ...'",
      "enumerate list", "other", None, "medium",
      L("On suppose que~:", r"\begin{enumerate}",
        r"  \item[$1^{\mathrm o}$] $B$ et $B'$ sont complets pour les topologies",
        r"  $\mathfrak J$-préadiques~;",
        r"  \item[$2^{\mathrm o}$] $B$ est une $A$-algèbre formellement lisse~;",
        r"  \item[$3^{\mathrm o}$] $B'$ est un $A$-module plat.",
        r"\end{enumerate}", "Posons"),
      L("On suppose que~:",
        r"$1^{\mathrm o}$ $B$ et $B'$ sont complets pour les topologies",
        r"$\mathfrak J$-préadiques~;",
        r"$2^{\mathrm o}$ $B$ est une $A$-algèbre formellement lisse~;",
        r"$3^{\mathrm o}$ $B'$ est un $A$-module plat.",
        "Posons"),
      "Layout: the print runs the three conditions into the statement (enlarged crop: '... que : 1° B et B' sont ...'); "
      "words and formulas agree. Same treatment as Corollaire (6.9.7), EGA III p. 169."),
    F(108, "(19.7.1.6): 'donc tout revient à prouver que B est un A-module plat.'",
      "A-module *plat*. (plat italic; enlarged crop)", "upright", "italics", None, "high",
      "$A$-module plat. Il revient", r"$A$-module \emph{plat}. Il revient", ""),
    F(108, "(19.7.1.6): 'on peut donc se borner au cas où A et B sont complets.'",
      "*complets* italic (enlarged crop)", "upright", "italics", None, "high",
      "sont complets. Comme", r"sont \emph{complets}. Comme", ""),
    F(108, "(19.7.1.6): 'c'est un anneau régulier (19.6.5) et complet'",
      "*régulier* italic (enlarged crop)", "upright", "italics", None, "high",
      "un anneau régulier (19.6.5)", r"un anneau \emph{régulier} (19.6.5)", ""),
    F(108, "(19.7.1.6): 'un anneau local noethérien complet et un A-module plat, un homomorphisme local A→B''",
      "A-module *plat* (plat italic; enlarged crop)", "upright", "italics", None, "high",
      "$A$-module plat, un homomorphisme", r"$A$-module \emph{plat}, un homomorphisme", ""),
    F(108, "(19.7.1.6): 'un k-isomorphisme B_0 ⥲ B'_0 = B'⊗_A k'",
      "isomorphism arrow (arrow with a tilde above; enlarged crop)", "\\simeq", "convention", 4, "high",
      r"$B_0\simeq B'_0=B'\otimes_A k$", r"$B_0\xrightarrow{\sim}B'_0=B'\otimes_A k$", ""),
    F(108, "Théorème (19.7.2): 'un homomorphisme local A→B faisant de B un A-module plat, et un A_0-isomorphisme'",
      "'plat,' upright (roman) inside the italic statement; 'un A-module' and 'et un' italic (enlarged crop)",
      "italic (statement environment)", "convention", 6, "high",
      L("un $A$-module", "plat, et un"), L("un $A$-module", r"\textup{plat}, et un"), ""),
    # ---------------- p. 109 ----------------
    F(109, "proof of (19.7.2): 'qui est un anneau local noethérien complet, un A-module plat, et pour laquelle'",
      "A-module *plat* (plat italic; enlarged crop)", "upright", "italics", None, "high",
      "un $A$-module plat, et pour laquelle", r"un $A$-module \emph{plat}, et pour laquelle", ""),
    F(109, "proof of (19.7.2): 'comme on a un k-isomorphisme u_00 : B⊗_A k = (B⊗_A A_0)⊗_{A_0} k ⥲ B_0⊗_A k = B_00, on déduit'",
      "the formula is inline, in the running line", "displayed with \\[ ... \\]", "other", None, "high",
      L("$k$-isomorphisme", r"\[", r"  u_{00}:B\otimes_A k=(B\otimes_A A_0)\otimes_{A_0}k",
        r"  \xrightarrow{\sim}B_0\otimes_{A_0}k=B_{00},", r"\]", "on déduit"),
      L("$k$-isomorphisme", r"$u_{00}:B\otimes_A k=(B\otimes_A A_0)\otimes_{A_0}k",
        r"\xrightarrow{\sim}B_0\otimes_{A_0}k=B_{00}$,", "on déduit"),
      "Layout: inline in the print, displayed in the TeX (GLOBAL_ISSUES 21). Independent of the next finding."),
    F(109, "same formula, last term: '⥲ B_0⊗_A k = B_00'",
      "B_0⊗_A k: subscript A without 0 (enlarged crops of both strips; the middle term has ⊗_{A_0}k)",
      "B_0\\otimes_{A_0}k", "formula", None, "high",
      r"\xrightarrow{\sim}B_0\otimes_{A_0}k=B_{00}", r"\xrightarrow{\sim}B_0\otimes_A k=B_{00}",
      "Not a misprint: B_00 was defined as B_0⊗_{A_0}k, and ⊗_A and ⊗_{A_0} agree on A_0-modules (A_0 = A/𝔍); the TeX "
      "normalises the print."),
    F(109, "heading 19.8: 'Algèbres de Cohen et p-anneaux de Cohen'",
      "p bold upright, like the rest of the heading (enlarged crop)", "$p$ (math italic, not bold)", "font", None, "high",
      "Cohen et $p$-anneaux", "Cohen et p-anneaux", ""),
    F(109, "heading 19.8: '... application à la structure des anneaux locaux complets.'",
      "final full stop", "no full stop", "punctuation", None, "high",
      "anneaux locaux complets}", "anneaux locaux complets.}",
      "GLOBAL_ISSUES 43/58: no \\subsection title in ega0-14 ... ega0-23 has the printed full stop."),
    F(109, "Définition (19.8.1): 'On dit que B est une A-algèbre de Cohen si elle vérifie'",
      "'A-algèbre de Cohen' italic like the rest of the statement: no change of face (enlarged crop)",
      "\\emph{$A$-algèbre de Cohen}: upright inside the italic definition", "convention", 6, "high",
      r"\emph{$A$-algèbre de Cohen}", "$A$-algèbre de Cohen",
      "Drop \\emph where the print shows no change of face (FIX_POLICY 2.6)."),
    F(109, "Définition (19.8.1)(i): 'B est un anneau complet.'",
      "'complet' italic, no change of face (enlarged crop)", "\\emph{complet}: upright", "convention", 6, "high",
      r"est un anneau \emph{complet}.", "est un anneau complet.", ""),
    F(109, "Définition (19.8.1)(ii): 'B est un A-module plat.'",
      "'plat' italic, no change of face (enlarged crop)", "\\emph{plat}: upright", "convention", 6, "high",
      r"$A$-module \emph{plat}.", "$A$-module plat.", ""),
    F(109, "Définition (19.8.1)(iii): 'B⊗_A k est un corps'",
      "'corps' italic, no change of face (enlarged crop)", "\\emph{corps}: upright", "convention", 6, "high",
      r"un \emph{corps}", "un corps", ""),
    F(109, "Définition (19.8.1)(iii): '(autrement dit, mB est l'idéal maximal de B)'",
      "the parenthetical is roman, with 'l'idéal maximal' italic (enlarged crop)",
      "italic throughout (definition environment)", "convention", 6, "high",
      L("(autrement dit,", r"  $\mathfrak mB$ est l'idéal maximal de $B$)"),
      L(r"\textup{(autrement dit,", r"  $\mathfrak mB$ est \emph{l'idéal maximal} de $B$)}"),
      "Inside \\textup the \\emph makes 'l'idéal maximal' italic, as printed."),
    F(109, "Définition (19.8.1)(iii): 'qui est une extension séparable de k.'",
      "'extension' italic, 'séparable' roman (enlarged crop)", "\\emph{extension séparable}: both words upright",
      "convention", 6, "high",
      L(r"\emph{extension", "  séparable}"), L("extension", r"  \emph{séparable}"),
      "\\emph inside the italic definition gives the printed upright 'séparable'."),
    # ---------------- p. 110 ----------------
    F(110, "Définition (19.8.3): 'On appelle anneau local premier un anneau local de la forme Z_pZ'",
      "'anneau local' italic, only 'premier' roman (enlarged crop)", "\\emph{anneau local premier}: all three words upright",
      "convention", 6, "high",
      r"\emph{anneau local premier}", r"anneau local \emph{premier}", ""),
    F(110, "Définition (19.8.3): 'On appelle anneau local complet premier le complété d'un anneau local premier.'",
      "'anneau local' italic, 'complet premier' roman (enlarged crop)",
      "\\emph{anneau local complet premier}: all four words upright", "convention", 6, "high",
      r"\emph{anneau local complet premier}", r"anneau local \emph{complet premier}", ""),
]

json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- checks: every "old" exactly once in its page file (LF), both in the original and in sequential application ----
pages = {}
for n in range(106, 111):
    pages[n] = (RUN / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
orig = dict(pages)
ok = True
for i, x in enumerate(json.load(open(OUT, encoding="utf-8"))):
    fx = x["fix"]
    if not fx:
        continue
    p, old, new = x["page"], fx["old"], fx["new"]
    c0, c1 = orig[p].count(old), pages[p].count(old)
    flag = "OK" if c1 == 1 else "FAIL"
    if c1 != 1:
        ok = False
    note = "" if c0 == 1 else f" (original count {c0})"
    print(f"{flag} #{i} p.{p} {x['kind']}: seq count {c1}{note}")
    if c1 == 1:
        pages[p] = pages[p].replace(old, new)
print("ALL OK" if ok else "SOME FAILED")
counts = {}
for x in findings:
    k = "convention" if x["kind"] == "convention" else ("misprint" if x["kind"] == "misprint_in_print" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(counts)
# ---- release-file segment check: the page files must equal the current release segments ----
rel = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex")
t = rel.read_text(encoding="utf-8")
import re
mk = re.compile(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(t)]
for j, (n, s) in enumerate(cuts):
    if 106 <= n <= 110:
        e = cuts[j + 1][1] if j + 1 < len(cuts) else len(t)
        body = orig[n].split("\n", 1)[1]
        print(n, "segment matches release file" if t[s:e] == body else "SEGMENT DIFFERS from release file")
