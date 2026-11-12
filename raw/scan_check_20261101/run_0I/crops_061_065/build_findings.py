"""Build findings_061_065.json for EGA I chapter 0, pp. 61-65, and check that every fix's "old" occurs exactly once
in its page_NNN.tex. '<NL>' in old/new stands for a line break (LF)."""
import json
import pathlib
import sys

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_061_065.json"
NL = "<NL>"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 61 ----------------
    F(61, "Définition (7.1.2), continued at the top of the page: '(ce qu'on exprime, par abus de langage, en disant que "
          "la suite (𝔍^n) tend vers 0)'",
      "the whole parenthesis is roman inside the italic definition; only 'tend vers' is italic",
      "the parenthesis is plain text inside the italic definition environment (all italic)",
      "convention", 6, "high",
      r"(ce qu'on exprime, par abus de langage, en disant<NL>que la suite $(\mathfrak J^n)$ tend vers $0$)",
      r"\textup{(ce qu'on exprime, par abus de langage, en disant<NL>que la suite $(\mathfrak J^n)$ \emph{tend vers} $0$)}",
      "Enlarged crop. \\emph inside \\textup keeps 'tend vers' italic."),
    F(61, "Définition (7.1.2): 'On dit qu'un anneau linéairement topologisé A est préadmissible s'il existe'",
      "the defined term 'préadmissible' is roman inside the italic definition",
      "préadmissible italic (definition environment)",
      "convention", 6, "high",
      r"$A$ est préadmissible s'il", r"$A$ est \emph{préadmissible} s'il",
      "Enlarged crop. The later 's'il est préadmissible' is italic in the print, as in the TeX. \\emph in the italic "
      "environment sets the word upright."),
    F(61, "Définition (7.1.2): 'on dit que A est admissible s'il est préadmissible'",
      "the defined term 'admissible' is roman inside the italic definition",
      "admissible italic (definition environment)",
      "convention", 6, "high",
      r"$A$ est admissible s'il", r"$A$ est \emph{admissible} s'il",
      "Enlarged crop."),
    F(61, "paragraph after (7.1.2): 'forment donc un système fondamental de voisinages de 0'",
      "'système fondamental de voisinages de' in italics ('0' roman)",
      "système fondamental de voisinages de (upright)",
      "italics", None, "high",
      r"donc un système fondamental de voisinages de $0$", r"donc un \emph{système fondamental de voisinages de} $0$",
      ""),
    F(61, "Corollaire (7.1.6): 'Les notations et hypothèses étant celles de (7.1.4), les propriétés'",
      "reference (7.1.4) roman inside the italic statement",
      "(7.1.4) plain text inside the italic corollary environment",
      "convention", 6, "high",
      r"celles de (7.1.4), les", r"celles de \textup{(7.1.4)}, les",
      "Enlarged crop: parentheses and old-style figures upright."),

    # ---------------- page 62 ----------------
    F(62, "Définition (7.1.9): 'On dit qu'un anneau préadmissible A est préadique s'il existe'",
      "the defined term 'préadique' is roman inside the italic definition",
      "préadique italic (definition environment)",
      "convention", 6, "high",
      r"$A$ est préadique s'il", r"$A$ est \emph{préadique} s'il",
      "Enlarged crop."),
    F(62, "Définition (7.1.9): '(ou, ce qui revient au même, tel que les 𝔍^n soient ouverts)'",
      "the parenthesis is roman inside the italic definition; only 'ouverts' is italic",
      "the parenthesis is plain text inside the italic definition environment (all italic)",
      "convention", 6, "high",
      r"(ou, ce qui revient au même, tel que<NL>les $\mathfrak J^n$ soient ouverts)",
      r"\textup{(ou, ce qui revient au même, tel que<NL>les $\mathfrak J^n$ soient \emph{ouverts})}",
      "Enlarged crop."),
    F(62, "Définition (7.1.9): 'On appelle anneau adique un anneau préadique séparé et complet.'",
      "the defined term 'adique' is roman inside the italic definition",
      "adique italic (definition environment)",
      "convention", 6, "high",
      r"On appelle anneau adique un anneau", r"On appelle anneau \emph{adique} un anneau",
      "Enlarged crop."),
    F(62, "(7.2.1), first sentence: 'Toute limite projective d'anneaux discrets est évidemment'",
      "'discrets' in italics",
      "discrets (upright; the env environment is roman)",
      "italics", None, "high",
      r"d'anneaux discrets est", r"d'anneaux \emph{discrets} est",
      ""),

    # ---------------- page 63 ----------------
    F(63, "(7.2.1), continued: 'si A est séparé, φ est un isomorphisme topologique'",
      "'séparé' in italics",
      "séparé (upright)",
      "italics", None, "high",
      r"si $A$ est séparé,", r"si $A$ est \emph{séparé},",
      ""),
    F(63, "(7.2.1), continued: 'si, en outre, A est complet, φ est un isomorphisme'",
      "'complet' in italics",
      "complet (upright)",
      "italics", None, "high",
      r"$A$ est complet, $\varphi$", r"$A$ est \emph{complet}, $\varphi$",
      ""),
    F(63, "(7.2.1), last line: 'φ est un isomorphisme topologique de A sur lim A/𝔍_λ.'",
      "'sur' in italics",
      "sur (upright)",
      "italics", None, "high",
      r"de $A$ sur<NL>$\varprojlim", r"de $A$ \emph{sur}<NL>$\varprojlim",
      "Enlarged crop. The earlier 'de A sur un sous-anneau' is roman, as in the TeX."),
    F(63, "(7.2.3), first line: 'Soient A un anneau topologique admissible, 𝔍 un idéal de A'",
      "'admissible' in italics",
      "admissible (upright; env environment)",
      "italics", None, "high",
      r"anneau topologique admissible,", r"anneau topologique \emph{admissible},",
      "Enlarged crop."),
    F(63, "(7.2.3): 'donc la topologie 𝔍-préadique sur A est séparée ; soit Â = lim A/𝔍^n'",
      "'séparée' in italics",
      "séparée (upright)",
      "italics", None, "high",
      r"est séparée~;", r"est \emph{séparée}~;",
      "Enlarged crop."),
    F(63, "Corollaire (7.2.5): 'Sous les hypothèses de (7.2.3), les conditions suivantes'",
      "reference (7.2.3) roman inside the italic statement",
      "(7.2.3) plain text inside the italic corollary environment",
      "convention", 6, "high",
      r"Sous les hypothèses de (7.2.3)", r"Sous les hypothèses de \textup{(7.2.3)}",
      ""),
    F(63, "Corollaire (7.2.5), item label 'a) L'homomorphisme u est continu'",
      "label 'a)' upright (roman a)",
      r"\item[$a)$] (math italic a)",
      "font", None, "high",
      r"\item[$a)$] L'homomorphisme", r"\item[{\upshape a)}] L'homomorphisme",
      "Enlarged crop. The labels of (7.2.5) and (7.2.7) are upright, unlike those of (7.1.6) on p. 61, which are "
      "italic as in the TeX."),

    # ---------------- page 64 ----------------
    F(64, "Corollaire (7.2.5), item label 'b) L'homomorphisme v est bicontinu'",
      "label 'b)' upright",
      r"\item[$b)$] (math italic b)",
      "font", None, "high",
      r"\item[$b)$] L'homomorphisme", r"\item[{\upshape b)}] L'homomorphisme",
      "Enlarged crop."),
    F(64, "Corollaire (7.2.5), item label 'c) A est un anneau 𝔍-adique'",
      "label 'c)' upright",
      r"\item[$c)$] (math italic c)",
      "font", None, "high",
      r"\item[$c)$]", r"\item[{\upshape c)}]",
      "Enlarged crop."),
    F(64, "proof of (7.2.6): 'le soit ([1], p. 18-07, th. 4)'",
      "[1] (old-style figure 1), the bibliography number of Cartan-Chevalley",
      "[I] (capital letter I)",
      "number", None, "high",
      r"([I], p.~18-07, th.~4)", r"([1], p.~18-07, th.~4)",
      "The bibliography is numbered (bib-fr.tex: \\bibitem{I-1} = Cartan-Chevalley); the old-style 1 was read as a "
      "roman numeral. \\cite{I-1}, as in the EGA I chapter files, would print the same [1]."),
    F(64, "Proposition (7.2.7), item label 'a) Pour i ≤ j, u_ij est surjectif'",
      "label 'a)' upright",
      r"\item[$a)$] (math italic a)",
      "font", None, "high",
      r"\item[$a)$] Pour", r"\item[{\upshape a)}] Pour",
      "Enlarged crop."),
    F(64, "Proposition (7.2.7) a): '(donc A_i est isomorphe à A_j/𝔍_j^{i+1})'",
      "the parenthesis is roman inside the italic statement",
      "the parenthesis is plain text inside the italic proposition environment (all italic)",
      "convention", 6, "high",
      r"(donc $A_i$ est isomorphe à<NL>    $A_j/\mathfrak J_j^{i+1}$)",
      r"\textup{(donc $A_i$ est isomorphe à<NL>    $A_j/\mathfrak J_j^{i+1}$)}",
      "Enlarged crop."),
    F(64, "Proposition (7.2.7), item label 'b) 𝔍_1/𝔍_1^2 (=𝔍_1) est un module de type fini'",
      "label 'b)' upright",
      r"\item[$b)$] (math italic b)",
      "font", None, "high",
      r"\item[$b)$] $\mathfrak J_1", r"\item[{\upshape b)}] $\mathfrak J_1",
      "Enlarged crop."),
    F(64, "Proposition (7.2.7), item label '(i) A est un anneau adique'",
      "label '(i)' upright",
      r"\item[(i)] inside the italic proposition environment (comes out italic)",
      "font", None, "high",
      r"\item[(i)]", r"\item[{\upshape(i)}]",
      "Enlarged crop. Form as in Lemme (7.1.3) on p. 61; see GLOBAL_ISSUES item 16."),
    F(64, "Proposition (7.2.7), item label '(ii) On a 𝔍^{(n)} = 𝔍^n'",
      "label '(ii)' upright",
      r"\item[(ii)] inside the italic proposition environment (comes out italic)",
      "font", None, "high",
      r"\item[(ii)]", r"\item[{\upshape(ii)}]",
      "Enlarged crop."),
    F(64, "Proposition (7.2.7), item label '(iii) 𝔍/𝔍^2 est isomorphe à 𝔍_1'",
      "label '(iii)' upright",
      r"\item[(iii)] inside the italic proposition environment (comes out italic)",
      "font", None, "high",
      r"\item[(iii)]", r"\item[{\upshape(iii)}]",
      "Enlarged crop."),
    F(64, "proof of (7.2.7): 'en outre, l'hypothèse a) implique que 𝔍_j^{j+1} = 0'",
      "'a)' upright (roman a) in the roman proof text",
      r"$a)$ (math italic a)",
      "font", None, "high",
      r"l'hypothèse $a)$ implique", r"l'hypothèse a) implique",
      "Enlarged crop."),
    F(64, "proof of (7.2.7), last line: 'pour la filtration précédente ([1], p. 18-06, lemme)'",
      "[1] (old-style figure 1)",
      "[I] (capital letter I)",
      "number", None, "high",
      r"([I], p.~18-06, lemme)", r"([1], p.~18-06, lemme)",
      "Same as the reference in the proof of (7.2.6) on this page."),

    # ---------------- page 65 ----------------
    F(65, "Corollaire (7.2.8): 'Sous les conditions de (7.2.7), pour que A soit noethérien'",
      "reference (7.2.7) roman inside the italic statement",
      "(7.2.7) plain text inside the italic corollary environment",
      "convention", 6, "high",
      r"Sous les conditions de (7.2.7)", r"Sous les conditions de \textup{(7.2.7)}",
      "Enlarged crop."),
    F(65, "Proposition (7.2.9): 'Supposons vérifiées les hypothèses de (7.2.7) : pour tout entier i'",
      "reference (7.2.7) roman inside the italic statement",
      "(7.2.7) plain text inside the italic proposition environment",
      "convention", 6, "high",
      r"les hypothèses de (7.2.7)~:", r"les hypothèses de \textup{(7.2.7)}~:",
      "Enlarged crop."),
    F(65, "Proposition (7.2.9), end: '(de sorte que M_n s'identifie à M/𝔍^{n+1}M = M⊗_A(A/𝔍^{n+1}))'",
      "the parenthesis is roman inside the italic statement",
      "the parenthesis is plain text inside the italic proposition environment (all italic)",
      "convention", 6, "high",
      r"(de sorte que $M_n$ s'identifie à<NL>$M/\mathfrak J^{n+1}M=M\otimes_A(A/\mathfrak J^{n+1})$)",
      r"\textup{(de sorte que $M_n$ s'identifie à<NL>$M/\mathfrak J^{n+1}M=M\otimes_A(A/\mathfrak J^{n+1})$)}",
      "Enlarged crop."),
    F(65, "proof of (7.2.9): 'On est donc ramené à montrer que les classes des z_h mod. M^{(0)} engendrent le module "
          "gradué grad(M)'",
      "mod. M^{(0)} (enlarged crop: superscript (0))",
      r"mod. $M^{(0)}$ (keeps the printed reading)",
      "misprint_in_print", None, "medium",
      None, None,
      "The proof defines M^{(n)} as the y = (y_k) with y_k = 0 for k < n, so M^{(0)} = M and every class mod. M^{(0)} "
      "is zero; the degree-0 part of grad(M) is M^{(0)}/M^{(1)} = M_0, generated by the z_h0. The printed reading is "
      "certain; the correction follows from that definition.",
      corrected=r"mod. $M^{(1)}$"),
    F(65, "proof of (7.2.9): '... ([1], p. 18-06, lemme) ; pour cela'",
      "[1] (old-style figure 1)",
      "[I] (capital letter I)",
      "number", None, "high",
      r"([I], p.~18-06, lemme)", r"([1], p.~18-06, lemme)",
      "Same reference as on p. 64."),
    F(65, "proof of (7.2.9), last sentence: 'autrement dit que 𝔍^{(n)}M = 𝔍^nM est le noyau de M → M_n.'",
      "est le noyau de M→M_n",
      r"est le noyau de $M\to M_n$ (keeps the printed reading)",
      "misprint_in_print", None, "medium",
      None, None,
      "Index slip in the original: with M^{(n)} = {y : y_k = 0 for k < n} (and 𝔍^{(n+1)} = ker(A → A_n), (7.2.7)), "
      "M^{(n)} = 𝔍^nM is the kernel of M → M_{n-1}; the kernel of v_n : M → M_n is 𝔍^{n+1}M, as the statement says. "
      "Equivalent correction: '𝔍^{(n+1)}M = 𝔍^{n+1}M est le noyau de M → M_n'. The printed reading is certain.",
      corrected=r"est le noyau de $M\to M_{n-1}$"),
    F(65, "Corollaire (7.2.10): 'vérifiant les conditions de (7.2.9), et soit N = lim N_i'",
      "reference (7.2.9) roman inside the italic statement",
      "(7.2.9) plain text inside the italic corollary environment",
      "convention", 6, "high",
      r"conditions de (7.2.9)", r"conditions de \textup{(7.2.9)}",
      ""),
]

ok = True
for f in findings:
    if f["fix"] is None:
        continue
    t = (RUN / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    if "\r" in t:
        print("CR in page", f["page"])
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print(f"page {f['page']}: old occurs {n} times: {f['fix']['old']!r}")
    after = t.replace(f["fix"]["old"], f["fix"]["new"])
    if after == t:
        ok = False
        print("no change for", f["fix"]["old"])

counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0, 0])
    if f["kind"] == "misprint_in_print":
        c[2] += 1
    elif f["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts normal/convention/misprint:", {p: "/".join(map(str, c)) for p, c in sorted(counts.items())})
if not ok:
    sys.exit(1)
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT, len(findings), "findings")
