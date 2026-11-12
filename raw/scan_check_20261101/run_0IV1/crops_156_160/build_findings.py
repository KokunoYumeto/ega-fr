# Builds findings_156_160.json and checks every fix against its page_NNN.tex.
# In the strings below the pilcrow character stands for a line break (LF).
import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_156_160.json')
NL = '¶'

findings = []

def F(page, where, scan, tex, kind, old, new, note=None, conv=None, conf='high', corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': old.replace(NL, '\n'), 'new': new.replace(NL, '\n')}}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected.replace(NL, '\n') if corrected else corrected
    d['note'] = note
    findings.append(d)

P155 = 'Print p. 155 text placed after the misplaced \\oldpage{156} marker (see the marker finding); the fix applies to the current page_156.tex.'
K_NOTE = ('Wrong letter: the print has Fraktur K (same glyph as the 𝔎 identified on 0_IV p. 52; GLOBAL_ISSUES 63). '
          'All 21 \\mathfrak R of ega0-21-fr.tex are on pp. 157-160 and all are K in the print.')
DER_NOTE = ('The print has Dér; ega0-20 writes \\operatorname{D\\acute{e}r} (101 times). ega0-21 has 8 \\operatorname{Der}: '
            'p. 155 (source line 109, 2), p. 158 (5), p. 160 (1).')

# ---------------- page 156 ----------------
F(156, 'Top of page_156.tex: the marker line',
  "Print p. 156 begins 'est bijectif (0_I, 1.3.4), et comme T⁻¹S est une R_m-algèbre finie'. The proof of (21.1.6) from 'D'après (21.1.5, (iii))', Lemme (21.1.6.1) and the start of its proof down to '…l'homomorphisme (T⁻¹S)⊗_{R_m}(T⁻¹S)→T⁻¹S' end print p. 155.",
  "\\oldpage[0\\textsubscript{IV-1}]{156} stands before 'D'après (21.1.5, (iii))', 25 source lines too early",
  'marker', r"\oldpage[0\textsubscript{IV-1}]{156}¶D'après", r"D'après",
  "Marker move, part 1 of 2: apply together with part 2. After the move the text from 'D'après' to '…\\to T^{-1}S$' lies in the p. 155 segment; the print-p.-155 findings below are written against the current page_156.tex (apply them before the move, or look for their 'old' in the p. 155 segment).")
F(156, "Proof of Lemme (21.1.6.1), before 'est bijectif (0$_I$, 1.3.4)'",
  "The page break of the print falls here: p. 155 ends '…(T⁻¹S)⊗_{R_m}(T⁻¹S)→T⁻¹S', p. 156 starts 'est bijectif'.",
  'No marker here',
  'marker', r"\to T^{-1}S$¶est bijectif", r"\to T^{-1}S$¶\oldpage[0\textsubscript{IV-1}]{156}¶est bijectif",
  'Marker move, part 2 of 2: inserts the marker where print p. 156 begins (mid-sentence; \\oldpage ends with \\ignorespaces, no paragraph break).')
F(156, 'Proof of (21.1.6) (print p. 155)', 'donc il est *nilpotent*;', 'donc il est nilpotent~;',
  'italics', r"donc il est nilpotent~;", r"donc il est \emph{nilpotent}~;", P155)
F(156, 'Proof of (21.1.6) (print p. 155)', 'π : B⊗_A B→B est *bijectif*.', 'est bijectif.',
  'italics', r"B\to B$ est bijectif.", r"B\to B$ est \emph{bijectif}.", P155)
F(156, 'Proof of (21.1.6) (print p. 155)', 'B est *entier* sur A', 'est entier sur',
  'italics', r"$B$ est entier sur", r"$B$ est \emph{entier} sur", P155)
F(156, 'Proof of (21.1.6) (print p. 155)', "c'est une A-algèbre *finie*.", "c'est une $A$-algèbre finie.",
  'italics', r"c'est une $A$-algèbre finie.", r"c'est une $A$-algèbre \emph{finie}.", P155)
F(156, 'Proof of (21.1.6) (print p. 155)', '(où on ne suppose pas que', "(où l'on ne suppose pas que",
  'word', r"(où l'on", r"(où on", P155)
F(156, 'Proof of (21.1.6) (print p. 155)', '*ne suppose pas* in italics', 'ne suppose pas (upright)',
  'italics', r"ne suppose pas", r"\emph{ne suppose pas}", P155)
F(156, 'Proof of Lemme (21.1.6.1) (print p. 155)', 'Il suffit de montrer que pour tout idéal maximal', 'Il suffit de montrer que, pour tout idéal maximal',
  'punctuation', r"montrer que, pour", r"montrer que pour", P155)
F(156, 'Proof of Lemme (21.1.6.1) (print p. 155)', 'T=R—𝔪 (long dash)', '$T=R-\\mathfrak m$',
  'convention', r"T=R-\mathfrak m", r"T=R\setmin\mathfrak m", P155, conv=7)
F(156, 'Proof of Lemme (21.1.6.1) (print p. 155)', 'n° 3 (superscript letter o)', 'n$^\\circ$~3 (degree sign)',
  'symbol', r"n$^\circ$~3", r"n\textsuperscript{o}~3",
  P155 + ' Degree sign against the superscript o; the edition writes n\\textsuperscript{o} (GLOBAL_ISSUES 57); ega0-21 has 3 n$^\\circ$.', conf='low')
F(156, 'Proof of Lemme (21.1.6.1) (print p. 155)', "l'homomorphisme (T⁻¹S)⊗_{R_m}(T⁻¹S)→T⁻¹S",
  '$(T^{-1}S)\\otimes_{R_{\\mathfrak m}}(S/\\mathfrak mS)\\to T^{-1}S$',
  'formula', r"\otimes_{R_{\mathfrak m}}(S/\mathfrak mS)", r"\otimes_{R_{\mathfrak m}}(T^{-1}S)",
  P155 + ' The second factor is T⁻¹S in the print (localization of S⊗_R S→S, cf. (0_I, 1.3.4)); (S/𝔪S) is a transcription error.')
F(156, 'Proof of Lemme (21.1.6.1), first line of p. 156', '(0_I, 1.3.4) with bold 0 and upright subscript I', '(0$_I$, 1.3.4)',
  'convention', r"(0$_I$, 1.3.4)", r"($\mathbf{0}_{\mathrm I}$, 1.3.4)",
  'The TeX form 0$_I$ also sets the subscript I italic; the print has an upright I. ega0-21 writes 0$_I$ three times (pp. 156, 159 twice).', conv=2)
F(156, 'Proof of Lemme (21.1.6.1)', 'un anneau *local*.', 'un anneau local.',
  'italics', r"un anneau local.", r"un anneau \emph{local}.")
F(156, 'Proof of Lemme (21.1.6.1)', "'…anneau local. Désignant encore…' continues the same paragraph", "blank line before 'Désignant encore'",
  'other', r"¶¶Désignant encore", r"¶Désignant encore", 'Paragraph break the print does not have.')
F(156, 'Proof of Lemme (21.1.6.1)', 'R est un *corps*;', 'R est un corps~;',
  'italics', r"est un corps~;", r"est un \emph{corps}~;")
for lab in ('a', 'b', 'c'):
    F(156, 'Proposition (21.1.7), item label %s)' % lab, 'label %s) upright' % lab,
      '\\item[%s)] inside the italic proposition (typeset italic)' % lab,
      'convention', r"\item[%s)]" % lab, r"\item[\textup{%s)}]" % lab, 'GLOBAL_ISSUES 16/22.', conv=6)
F(156, 'Proposition (21.1.7), last sentence', "'Alors les propriétés a) et b)…' starts an indented paragraph after the items",
  'no blank line after \\end{enumerate}',
  'other', r"\end{enumerate}¶Alors les", r"\end{enumerate}¶¶Alors les", 'Paragraph break of the print.')
F(156, 'Proposition (21.1.7), last sentence', 'a) et b) upright in the italic statement', 'a) et b) (italic)',
  'convention', r"propriétés a) et b) sont", r"propriétés \textup{a)} et \textup{b)} sont", 'Two occurrences.', conv=6)
F(156, 'Proposition (21.1.7), last sentence', 'c) upright in the italic statement', 'c) (italic)',
  'convention', r"entraînent c)~;", r"entraînent \textup{c)}~;", None, conv=6)
F(156, 'Proposition (21.1.7), last sentence', 'si en outre B est une A[B^p]-algèbre', 'si, en outre, $B$ est une',
  'punctuation', r"si, en¶outre, $B$", r"si en¶outre $B$")
F(156, 'Proposition (21.1.7), last sentence', 'c), a), b) upright in the italic statement', 'c) … a) et b) (italic)',
  'convention', r"fini, c) est équivalente à a) et b).", r"fini, \textup{c)} est équivalente à \textup{a)} et \textup{b)}.",
  'Three occurrences.', conv=6)
F(156, 'Proof of (21.1.7)', 'Il est clair que *b)* entraîne *a)*, et inversement *a)* entraîne *b)*', 'b), a), a), b) upright',
  'italics', r"que b) entraîne a), et inversement a) entraîne b)",
  r"que \emph{b)} entraîne \emph{a)}, et inversement \emph{a)} entraîne \emph{b)}")
F(156, 'Proof of (21.1.7)', 'm(α)=p.q(α)+r(α) (baseline period)', '$m(\\alpha)=p q(\\alpha)+r(\\alpha)$',
  'symbol', r"=p q(\alpha)", r"=p.q(\alpha)", 'GLOBAL_ISSUES 65.')
F(156, 'Proof of (21.1.7)', 'Le fait que *a)* entraîne *c)*', 'a), c) upright',
  'italics', r"Le fait que a) entraîne c)", r"Le fait que \emph{a)} entraîne \emph{c)}")
F(156, 'Proof of (21.1.7)', "'Supposons inversement…' continues the paragraph (no indent)", "blank line before 'Supposons inversement'",
  'other', r"(20.4.7).¶¶Supposons", r"(20.4.7).¶Supposons", 'Paragraph break the print does not have.')
F(156, 'Proof of (21.1.7)', 'Supposons inversement *c)* vérifiée', 'c) upright',
  'italics', r"inversement c) vérifiée", r"inversement \emph{c)} vérifiée")
F(156, 'Proof of (21.1.7), after the display', '(compte tenu de (21.1.5, (ii)); : the closing parenthesis of the outer bracket is missing',
  '(compte tenu de (21.1.5, (ii)))~;',
  'misprint_in_print', r"(ii)))~;", r"(ii))~;",
  'The TeX silently corrects the print; the fix restores the printed reading.', corrected=r"(21.1.5, (ii)))")
F(156, 'Remarque (21.1.8)', 'Lorsque B est un *corps*,', 'est un corps,',
  'italics', r"est un corps, nous", r"est un \emph{corps}, nous", 'Remark body judged as roman (document-wide remark item).')
F(156, 'Remarque (21.1.8)', 'des propriétés *a)*, *b)* et *c)*', 'a), b) et c) (no emphasis)',
  'italics', r"propriétés a),¶b) et c) sans", r"propriétés \emph{a)},¶\emph{b)} et \emph{c)} sans",
  'Remark body judged as roman (document-wide remark item).')
F(156, 'Définition (21.1.9)', '(resp. upright', '(resp. italic', 'convention',
  r"(resp. un système de $p$-générateurs", r"(\textup{resp.} un système de $p$-générateurs", None, conv=6)
F(156, 'Définition (21.1.9)', 'resp. upright', 'resp. italic', 'convention',
  r"sur $A$, resp. une $p$-base", r"sur $A$, \textup{resp.} une $p$-base", None, conv=6)
F(156, 'Définition (21.1.9)', '(resp. upright', 'resp. italic', 'convention',
  r"libre (resp. un", r"libre (\textup{resp.} un", None, conv=6)
F(156, 'Définition (21.1.9)', 'resp. upright', 'resp. italic', 'convention',
  r"générateurs, resp. une base)", r"générateurs, \textup{resp.} une base)", None, conv=6)
F(156, 'Définition (21.1.9)', '(n(α))_{α∈I} de support fini)', '$(n(\\alpha))_{\\alpha\\in I}$ à support fini)',
  'word', r"à support fini) est", r"de support fini) est")
F(156, 'After Définition (21.1.9)', 'pour un *ensemble* M', 'pour un ensemble $M$',
  'italics', r"pour un ensemble $M$", r"pour un \emph{ensemble} $M$")
F(156, 'After Définition (21.1.9)', 'le *corps premier* F_p', 'le corps premier $\\mathbf F_p$',
  'italics', r"le corps premier", r"le \emph{corps premier}")

# ---------------- page 157 ----------------
F(157, 'Top of p. 157, before Lemme (21.1.10)',
  "Two paragraphs: 'Il est clair que les notions définies dans (21.1.9) ne changent pas lorsqu'on y remplace A par le sous-anneau A[B^p] de B; autrement dit on peut toujours supposer que l'on a B^p⊂A⊂B.' and 'Si M est une partie p-libre de B sur A, il est clair que toute partie de M est p-libre sur A. En outre :'",
  'Absent: the marker is followed directly by \\begin{lemma}[21.1.10]; the text is nowhere in ega0-21-fr.tex',
  'missing', r"\oldpage[0\textsubscript{IV-1}]{157}¶\begin{lemma}[21.1.10]",
  r"\oldpage[0\textsubscript{IV-1}]{157}¶Il est clair que les notions définies dans (21.1.9) ne changent pas lorsqu'on y¶remplace $A$ par le sous-anneau $A[B^p]$ de $B$~; autrement dit on peut toujours¶supposer que l'on a $B^p\subset A\subset B$.¶¶Si $M$ est une partie $p$-libre de $B$ sur $A$, il est clair que toute partie¶de $M$ est $p$-libre sur $A$. En outre~:¶¶\begin{lemma}[21.1.10]",
  'Both paragraphs roman, no italics; a blank line already precedes the marker in the source.')
F(157, 'Lemme (21.1.10), item label (i)', '(i) upright', '\\item[(i)] (italic)', 'convention',
  r"\item[(i)] Si $M$", r"\item[\textup{(i)}] Si $M$", 'GLOBAL_ISSUES 16.', conv=6)
F(157, 'Lemme (21.1.10), item label (ii)', '(ii) upright', '\\item[(ii)] (italic)', 'convention',
  r"\item[(ii)] Supposons que $M$", r"\item[\textup{(ii)}] Supposons que $M$", 'GLOBAL_ISSUES 16.', conv=6)
F(157, 'Proof of (21.1.10)', "l'ensemble des xy,", "l'ensemble des produits $xy$,",
  'extra', r"des¶produits $xy$", r"des¶$xy$")
F(157, 'Proof of (21.1.10)', "'Conservant les mêmes notations' continues the paragraph (no indent)", "blank line before 'Conservant'",
  'other', r"¶¶Conservant les mêmes", r"¶Conservant les mêmes", 'Paragraph break the print does not have.')
F(157, 'Proof of (21.1.10)', '(resp. y_μ)', '(resp. les $y_\\mu$)',
  'extra', r"(resp. les $y_\mu$)", r"(resp. $y_\mu$)")
F(157, 'Proof of (21.1.10)',
  "équivaut à Σ_λ a_{λμ}x_λ=0 pour tout μ, ou encore à a_{λμ}=0 pour tout couple (λ, μ); d'où l'assertion (ii).",
  "équivaut à $a_{\\lambda\\mu}=0$ pour tout couple $(\\lambda,\\mu)$, ou encore à $\\sum_\\lambda a_{\\lambda\\mu}x_\\lambda=0$ pour tout $\\mu$~;",
  'other', r"équivaut à¶$a_{\lambda\mu}=0$ pour tout couple $(\lambda,\mu)$, ou encore à¶$\sum_\lambda a_{\lambda\mu}x_\lambda=0$ pour tout $\mu$~;",
  r"équivaut à¶$\sum_\lambda a_{\lambda\mu}x_\lambda=0$ pour tout $\mu$, ou encore¶à $a_{\lambda\mu}=0$ pour tout couple $(\lambda,\mu)$~;",
  'The two clauses are in the reverse order in the TeX.')
F(157, 'Heading 21.2', '21.2. p-bases et lissité formelle. (bold upright p)', '\\subsection{$p$-bases …} (math italic p, not bold)',
  'font', r"\subsection{$p$-bases", r"\subsection{p-bases", 'Same in the 21.3 heading (p. 160); probably also 21.1 (p. 154).', conf='medium')
F(157, 'Heading 21.2', 'title ends with a full stop', 'no full stop',
  'punctuation', r"lissité formelle}", r"lissité formelle.}", 'GLOBAL_ISSUES 43/58.')
F(157, 'Théorème (21.2.1), item label (i)', '(i) upright', '\\item[(i)] (italic)', 'convention',
  r"\item[(i)] Pour qu'il", r"\item[\textup{(i)}] Pour qu'il", 'GLOBAL_ISSUES 16.', conv=6)
F(157, 'Théorème (21.2.1), item label (ii)', '(ii) upright', '\\item[(ii)] (italic)', 'convention',
  r"\item[(ii)] Lorsque", r"\item[\textup{(ii)}] Lorsque", 'GLOBAL_ISSUES 16.', conv=6)
F(157, 'Théorème (21.2.1) (ii)', 'Lorsque la condition de (i) est satisfaite: (i) upright', '(i) italic', 'convention',
  r"condition de (i) est satisfaite", r"condition de \textup{(i)} est satisfaite", None, conv=6)
F(157, 'Théorème (21.2.1)', '𝔎 son noyau (Fraktur K)', '$\\mathfrak R$ son noyau',
  'symbol', r"$\mathfrak R$ son noyau", r"$\mathfrak K$ son noyau", K_NOTE)
F(157, 'Théorème (21.2.1)', 'supposons que 𝔎^p=0', '$\\mathfrak R^p=0$',
  'symbol', r"que $\mathfrak R^p=0$. Alors", r"que $\mathfrak K^p=0$. Alors", 'Fraktur K (see above).')
F(157, 'Théorème (21.2.1) (i)', "il faut et il suffit que l'on ait u(q(z)^p)=z^p", 'il faut et il suffit que $u(q(z)^p)=z^p$',
  'missing', r"il suffit que¶  $u(q(z)^p)", r"il suffit que l'on ait¶  $u(q(z)^p)")
F(157, 'Proof of (21.2.1)', 'et par définition v(q(z))≡z', 'et, par définition,',
  'punctuation', r"et, par définition,", r"et par définition")
F(157, 'Proof of (21.2.1)', 'v(q(z))≡z (mod. 𝔎)', '\\pmod{\\mathfrak R} (prints "mod" without the full stop, letter R)',
  'symbol', r"\equiv z\pmod{\mathfrak R}$", r"\equiv z$ (mod.~$\mathfrak K$)",
  'One edit for the printed "mod." and the Fraktur K (wrong letter, see above).')
F(157, 'Proof of (21.2.1)', 'puisque 𝔎^p=0;', 'puisque $\\mathfrak R^p=0$~;',
  'symbol', r"puisque $\mathfrak R^p=0$~;", r"puisque $\mathfrak K^p=0$~;", 'Fraktur K (see above).')
F(157, 'Proof of (21.2.1)', "'Or, sous les hypothèses de (ii)' continues the paragraph (no indent)", "blank line before 'Or, sous'",
  'other', r"résultera de (ii).¶¶Or, sous", r"résultera de (ii).¶Or, sous", 'Paragraph break the print does not have.')
F(157, 'Proof of (21.2.1)', '∏_α z_α^{n α)}: the opening parenthesis of the exponent is missing', '\\prod_\\alpha z_\\alpha^{n(\\alpha)}',
  'misprint_in_print', r"z_\alpha^{n(\alpha)}", r"z_\alpha^{n\,\alpha)}",
  'The TeX silently corrects the print; the fix restores the printed reading (gap where the parenthesis is missing).',
  corrected=r"z_\alpha^{n(\alpha)}")
F(157, 'Proof of (21.2.1)', "un homomorphisme d'*anneaux*.", "homomorphisme d'anneaux.",
  'italics', r"homomorphisme d'anneaux.", r"homomorphisme d'\emph{anneaux}.")
F(157, 'Proof of (21.2.1)', '=a.∏_α x_α^{r(α)} (baseline period)', '=a\\prod_\\alpha x_\\alpha^{r(\\alpha)}',
  'symbol', r"=a\prod_\alpha x_\alpha^{r(\alpha)}", r"=a.\prod_\alpha x_\alpha^{r(\alpha)}", 'GLOBAL_ISSUES 65.')
F(157, 'Proof of (21.2.1)', 'r(α)=m(α)+n(α)—p (long dash)', 'm(\\alpha)+n(\\alpha)-p',
  'convention', r"+n(\alpha)-p$", r"+n(\alpha)\setmin p$", 'Long dash for subtraction (GLOBAL_ISSUES 23).', conv=7)

# ---------------- page 158 ----------------
F(158, 'End of the proof of (21.2.1)', "cela résulte de l'hypothèse. C.Q.F.D.", "cela résulte de l'hypothèse. (no C.Q.F.D.)",
  'missing', r"résulte de l'hypothèse.¶\end{proof}", r"résulte de l'hypothèse. C.Q.F.D.¶\end{proof}")
F(158, 'Proof of (21.2.2)', 'En effet, soient E une A-extension', 'Soient $E$ une $A$-extension',
  'missing', r"Soient $E$ une $A$-extension", r"En effet, soient $E$ une $A$-extension")
F(158, 'Proof of (21.2.2)', 'On en déduit que, pour z∈E, on a u(q(z)^p)=…', 'On en déduit, pour $z\\in E$, que $u(q(z)^p)=…',
  'word', r"On en déduit,¶pour $z\in E$, que $u", r"On en déduit que,¶pour $z\in E$, on a $u")
F(158, 'Proof of (21.2.2)', 'mais en vertu de la relation', 'mais, en vertu de',
  'punctuation', r"mais, en vertu de", r"mais en vertu de")
F(158, 'Proof of (21.2.2)', 'v(q(z))—z∈L (long dash)', '$v(q(z))-z\\in L$',
  'convention', r"v(q(z))-z\in L", r"v(q(z))\setmin z\in L", 'Long dash for subtraction (GLOBAL_ISSUES 23).', conv=7)
F(158, 'Proof of (21.2.2)', '(v(q(z)))^p=z^p; la condition', '…=z^p$. La condition',
  'punctuation', r"z^p$. La condition", r"z^p$~; la condition")
F(158, 'Proof of (21.2.2)', 'la condition de (21.2.1, (i)) est donc', 'La condition de (21.2.1), (i), est donc',
  'punctuation', r"de (21.2.1), (i), est donc", r"de (21.2.1, (i)) est donc")
F(158, 'Proof of (21.2.2)', 'est donc satisfaite, et E est', 'est donc satisfaite et $E$ est',
  'punctuation', r"satisfaite et¶$E$", r"satisfaite, et¶$E$")
F(158, 'Proof of (21.2.2), last words', 'et E est B-triviale. (no exponent p)', '$E$ est $B^p$-triviale.',
  'misprint_in_print', r"$B^p$-triviale.¶\end{proof}", r"$B$-triviale.¶\end{proof}",
  "The TeX silently corrects the print; the proof shows E is B^p-triviale ('Dire que E est B^p-triviale' a few lines above).",
  corrected=r"$B^p$-triviale")
F(158, 'Corollaire (21.2.3), item label (i)', '(i) upright', '\\item[(i)] (italic)', 'convention',
  r"\item[(i)] Pour qu'une", r"\item[\textup{(i)}] Pour qu'une", 'GLOBAL_ISSUES 16.', conv=6)
F(158, 'Corollaire (21.2.3), item label (ii)', '(ii) upright', '\\item[(ii)] (italic)', 'convention',
  r"\item[(ii)] Si $D$", r"\item[\textup{(ii)}] Si $D$", 'GLOBAL_ISSUES 16.', conv=6)
F(158, 'Proof of (21.2.3)', 'de la forme x⇝(x, D\'(x)) (wavy arrow)', "$x\\mapsto(x,D'(x))$",
  'symbol', r"$x\mapsto(x,D'(x))$", r"$x\leadsto(x,D'(x))$", 'GLOBAL_ISSUES 33.')
F(158, '(21.2.3.1)', '0→Dér_A(B, L)→Dér_{B^p}(B, L)→Dér_{B^p}(A, L)→0', '\\operatorname{Der} three times',
  'word', r"0\to\operatorname{Der}_A(B,L)\to\operatorname{Der}_{B^p}(B,L)¶\to\operatorname{Der}_{B^p}(A,L)\to0",
  r"0\to\operatorname{D\acute{e}r}_A(B,L)\to\operatorname{D\acute{e}r}_{B^p}(B,L)¶\to\operatorname{D\acute{e}r}_{B^p}(A,L)\to0",
  'Three occurrences. ' + DER_NOTE)
F(158, 'After (21.2.3.1)', '(cf. (20.2.2.1)) est *exacte*,', 'est exacte,',
  'italics', r"est exacte, et que", r"est \emph{exacte}, et que")
F(158, '(21.2.3.2)', "D'⇝(D'(x_α))_{α∈I} (wavy arrow)", "D'\\longmapsto(D'(x_\\alpha))_{\\alpha\\in I}",
  'symbol', r"D'\longmapsto(D'(x_\alpha))", r"D'\leadsto(D'(x_\alpha))", 'GLOBAL_ISSUES 33.')
F(158, 'After (21.2.3.2)', 'est un *isomorphisme* du B-module', 'est un isomorphisme du',
  'italics', r"est un isomorphisme du", r"est un \emph{isomorphisme} du")
F(158, 'After (21.2.3.2)', 'du B-module Dér_A(B, L)', '$\\operatorname{Der}_A(B,L)$',
  'word', r"$B$-module $\operatorname{Der}_A(B,L)$ sur le", r"$B$-module $\operatorname{D\acute{e}r}_A(B,L)$ sur le", DER_NOTE)
F(158, 'After (21.2.3.2)', 'le B-module *produit* L^I', 'le $B$-module produit $L^I$',
  'italics', r"$B$-module produit $L^I$", r"$B$-module \emph{produit} $L^I$")
F(158, 'Corollaire (21.2.4)', 'Sous les hypothèses de (21.2.3), la suite: reference upright', '(21.2.3) italic',
  'convention', r"Sous les hypothèses de (21.2.3), la suite", r"Sous les hypothèses de \textup{(21.2.3)}, la suite", None, conv=6)
F(158, 'Proof of (21.2.4)', 'la formule Dér_A(B, L)=Hom_B(Ω¹_{B/A}, L)', '$\\operatorname{Der}_A(B,L)=…$',
  'word', r"$\operatorname{Der}_A(B,L)=\operatorname{Hom}_B", r"$\operatorname{D\acute{e}r}_A(B,L)=\operatorname{Hom}_B", DER_NOTE)
F(158, 'Proof of (21.2.5)', 'En utilisant (21.1.5, (ii)), on', 'En utilisant (21.1.5), (ii), on',
  'punctuation', r"En utilisant (21.1.5), (ii), on", r"En utilisant (21.1.5, (ii)), on")
F(158, 'Proof of (21.2.5)', 'on se ramène en effet au cas où A=A[B^p]', 'on se ramène au cas où',
  'missing', r"se ramène au cas où $A=A[B^p]$", r"se ramène en effet au cas où $A=A[B^p]$")

# ---------------- page 159 ----------------
F(159, '(21.2.6)', 'on a (avec les notations de (21.1.4)) un diagramme commutatif', 'le diagramme commutatif',
  'word', r"le diagramme commutatif", r"un diagramme commutatif")
F(159, '(21.2.6.1)', 'bottom arrow A→B with its label u below the arrow', '\\ar[r]^{u} (label above)',
  'formula', r"\ar[r]^{u} & B \ar[u]_{F_B}", r"\ar[r]_{u} & B \ar[u]_{F_B}",
  'Top arrow (u above), F_A left and F_B right agree with the TeX.')
F(159, '(21.2.6)', 'On en déduit donc canoniquement', 'On en déduit canoniquement',
  'missing', r"On en déduit canoniquement", r"On en déduit donc canoniquement")
F(159, '(21.2.6)', 'un homomorphisme de B-*algèbres*', 'de $B$-algèbres',
  'italics', r"un homomorphisme de $B$-algèbres", r"un homomorphisme de $B$-\emph{algèbres}")
F(159, 'Théorème (21.2.7), item label (i)', '(i) upright', '\\item[(i)] (italic)', 'convention',
  r"\item[(i)]", r"\item[\textup{(i)}]", 'GLOBAL_ISSUES 16.', conv=6)
F(159, 'Théorème (21.2.7), item label (ii)', '(ii) upright', '\\item[(ii)] (italic)', 'convention',
  r"\item[(ii)]", r"\item[\textup{(ii)}]", 'GLOBAL_ISSUES 16.', conv=6)
F(159, 'Théorème (21.2.7) (i)', "L'homomorphisme (21.2.6.2): reference upright", '(21.2.6.2) italic', 'convention',
  r"(21.2.6.2) déduit", r"\textup{(21.2.6.2)} déduit", None, conv=6)
F(159, 'Théorème (21.2.7)', "'Alors B est une A-algèbre formellement lisse…' starts an indented paragraph after the items",
  'no blank line after \\end{enumerate}',
  'other', r"\end{enumerate}¶Alors $B$", r"\end{enumerate}¶¶Alors $B$", 'Paragraph break of the print.')
F(159, 'Théorème (21.2.7)', '(0_I, 7.1.2) with bold 0, upright', '(0$_I$, 7.1.2) inside the italic statement',
  'convention', r"(0$_I$, 7.1.2)", r"\textup{($\mathbf{0}_{\mathrm I}$, 7.1.2)}",
  'Bold 0 with upright subscript I; the \\textup is the convention-6 part, listed separately with fix null.', conv=2)
F(159, 'Théorème (21.2.7)', '(0_I, 7.1.2) upright inside the italic statement', 'italic', 'convention', None, None,
  'Included in the convention-2 edit of (0$_I$, 7.1.2).', conv=6)
F(159, 'Théorème (21.2.7)', '𝔎 un idéal de définition de E, C=E/𝔎 (Fraktur K)', '$\\mathfrak R$ … $C=E/\\mathfrak R$',
  'symbol', r"$\mathfrak R$ un idéal de définition de $E$, $C=E/\mathfrak R$",
  r"$\mathfrak K$ un idéal de définition de $E$, $C=E/\mathfrak K$", 'Two occurrences. ' + K_NOTE)
F(159, 'Théorème (21.2.7)', "d'éléments de E tels que q(z_α)=v(x_α)", "d'éléments de $E$ telle que",
  'word', r"de $E$ telle que", r"de $E$ tels que")
F(159, 'Proof of (21.2.7)', 'le cas où E est *discret*,', 'est discret,',
  'italics', r"$E$ est discret,", r"$E$ est \emph{discret},")
F(159, 'Proof of (21.2.7)', 'donc 𝔎 nilpotent', '$\\mathfrak R$', 'symbol',
  r"donc $\mathfrak R$ nilpotent", r"donc $\mathfrak K$ nilpotent", 'Fraktur K (see above).')
F(159, 'Proof of (21.2.7)', '𝔎²=0 et par suite 𝔎^p=0', '$\\mathfrak R^2=0$ … $\\mathfrak R^p=0$', 'symbol',
  r"$\mathfrak R^2=0$ et par suite $\mathfrak R^p=0$", r"$\mathfrak K^2=0$ et par suite $\mathfrak K^p=0$",
  'Two occurrences; Fraktur K (see above).')
F(159, 'Proof of (21.2.7)', 'par 𝔎, on peut se borner', 'par $\\mathfrak R$,', 'symbol',
  r"par $\mathfrak R$, on peut", r"par $\mathfrak K$, on peut", 'Fraktur K (see above).')
F(159, 'Proof of (21.2.7)', "F_E : z⇝z^p s'annule dans 𝔎", "s'annule dans $\\mathfrak R$", 'symbol',
  r"s'annule dans $\mathfrak R$, il", r"s'annule dans $\mathfrak K$, il", 'Fraktur K (see above).')
F(159, 'Proof of (21.2.7)', 'considéré comme homomorphisme de B *dans* E^(p)', 'de $B$ dans $E^{(p)}$',
  'italics', r"de $B$ dans $E^{(p)}$", r"de $B$ \emph{dans} $E^{(p)}$")
F(159, 'Proof of (21.2.7), general case', "d'idéaux ouverts de E, et soient E_λ=E/ℑ_λ", 'et posons',
  'word', r"et posons", r"et soient")
F(159, 'Proof of (21.2.7), general case', '𝔎_λ=(𝔎+ℑ_λ)/ℑ_λ', '$\\mathfrak R_\\lambda=(\\mathfrak R+…)$', 'symbol',
  r"$\mathfrak R_\lambda=(\mathfrak R+\mathfrak J_\lambda)/\mathfrak J_\lambda$",
  r"$\mathfrak K_\lambda=(\mathfrak K+\mathfrak J_\lambda)/\mathfrak J_\lambda$", 'Two occurrences; Fraktur K (see above).')
F(159, 'Proof of (21.2.7), general case', 'C_λ=E_λ/𝔎_λ=E/(𝔎+ℑ_λ)', '$\\mathfrak R_\\lambda$, $\\mathfrak R$', 'symbol',
  r"$C_\lambda=E_\lambda/\mathfrak R_\lambda=E/(\mathfrak R+\mathfrak J_\lambda)$",
  r"$C_\lambda=E_\lambda/\mathfrak K_\lambda=E/(\mathfrak K+\mathfrak J_\lambda)$", 'Two occurrences; Fraktur K (see above).')
F(159, 'Proof of (21.2.7), general case', '(0_I, 7.2.2) with bold 0', '(0$_I$, 7.2.2)', 'convention',
  r"(0$_I$, 7.2.2)", r"($\mathbf{0}_{\mathrm I}$, 7.2.2)", 'Also sets the subscript I upright, as printed.', conv=2)

# ---------------- page 160 ----------------
F(160, 'Proof of (21.2.7), end', 'par hypothèse 𝔎_λ est nilpotent', '$\\mathfrak R_\\lambda$', 'symbol',
  r"hypothèse $\mathfrak R_\lambda$ est nilpotent", r"hypothèse $\mathfrak K_\lambda$ est nilpotent", K_NOTE)
F(160, 'Remarque (21.2.8)', 'formellement lisse et de ce que les d_{B/A}(x_α)', 'formellement lisse et que les',
  'missing', r"lisse et que les", r"lisse et de ce que les")
F(160, 'Remarque (21.2.8)', 'au cas où 𝔎²=0;', '$\\mathfrak R^2=0$~;', 'symbol',
  r"au cas où $\mathfrak R^2=0$~;", r"au cas où $\mathfrak K^2=0$~;", 'Fraktur K (see above).')
F(160, 'Remarque (21.2.8)', 'comme Dér_A(B, 𝔎)=Hom_B(Ω¹_{B/A}, 𝔎)', '$\\operatorname{Der}_A(B,\\mathfrak R)=…(\\Omega^1_{B/A},\\mathfrak R)$',
  'word', r"$\operatorname{Der}_A(B,\mathfrak R)=\operatorname{Hom}_B(\Omega^1_{B/A},\mathfrak R)$",
  r"$\operatorname{D\acute{e}r}_A(B,\mathfrak K)=\operatorname{Hom}_B(\Omega^1_{B/A},\mathfrak K)$",
  DER_NOTE + ' The same edit changes the two Fraktur R to K (next finding).')
F(160, 'Remarque (21.2.8)', 'Dér_A(B, 𝔎)=Hom_B(Ω¹_{B/A}, 𝔎): Fraktur K twice', '$\\mathfrak R$ twice', 'symbol', None, None,
  'Included in the Dér edit above.')
F(160, 'Remarque (21.2.8)', '…=Hom_B(Ω¹_{B/A}, 𝔎) par (20.4.8), il existe', '(20.4.8), il existe',
  'missing', r"(20.4.8), il existe", r"par (20.4.8), il existe")
F(160, 'Remarque (21.2.8)', 'une A-dérivation D et une seule de B dans 𝔎', '$D$, et une seule, de $B$',
  'punctuation', r"$D$, et une seule, de $B$", r"$D$ et une seule de $B$")
F(160, 'Remarque (21.2.8)', 'dans 𝔎 telle que', '$\\mathfrak R$ telle que', 'symbol',
  r"dans¶$\mathfrak R$ telle que", r"dans¶$\mathfrak K$ telle que", 'Fraktur K (see above).')
F(160, 'Remarque (21.2.8)', "d'éléments de 𝔎;", "d'éléments de $\\mathfrak R$~;", 'symbol',
  r"d'éléments de $\mathfrak R$~;", r"d'éléments de $\mathfrak K$~;", 'Fraktur K (see above).')
F(160, 'Remarque (21.2.8)', 'la conclusion résulte donc de (20.1.1).', 'la conclusion résulte de (20.1.1).',
  'missing', r"la conclusion résulte de (20.1.1)", r"la conclusion résulte donc de (20.1.1)")
F(160, 'Heading 21.3', '21.3. p-bases et modules d\'imperfection. (bold upright p)', '\\subsection{$p$-bases …} (math italic p, not bold)',
  'font', r"\subsection{$p$-bases", r"\subsection{p-bases", 'As in the 21.2 heading (p. 157).', conf='medium')
F(160, 'Heading 21.3', 'title ends with a full stop', 'no full stop',
  'punctuation', r"modules d'imperfection}", r"modules d'imperfection.}", 'GLOBAL_ISSUES 43/58.')
F(160, '(21.3.1)', "deux homomorphismes d'anneaux tels que l'on ait", "d'anneaux tels que",
  'missing', r"d'anneaux tels que¶\begin{align}", r"d'anneaux tels que l'on ait¶\begin{align}")
F(160, '(21.3.1)', "'Le plus souvent, i sera injectif…' starts an indented paragraph after the displays", 'no blank line after \\end{align}',
  'other', r"\end{align}¶Le plus souvent", r"\end{align}¶¶Le plus souvent", 'Paragraph break of the print (GLOBAL_ISSUES 47).')
F(160, '(21.3.1)', 'i sera *injectif*,', 'sera injectif,',
  'italics', r"sera injectif,", r"sera \emph{injectif},")
F(160, '(21.3.2)', "on a, d'après (21.3.1.1), un diagramme commutatif", "d'après (21.3.1.1) et (21.3.1.2), un diagramme",
  'extra', r"d'après (21.3.1.1) et¶(21.3.1.2), un diagramme", r"d'après (21.3.1.1), un diagramme")
F(160, '(21.3.2.1)', 'bottom arrow A→A^p with its label F_A below the arrow', '\\ar[r]^{F_A} (label above)',
  'formula', r"\ar[r]^{F_A} & A^p", r"\ar[r]_{F_A} & A^p", 'Top arrow (j above), i left and h right agree with the TeX.')
F(160, '(21.3.2)', 'comme un *di-homomorphisme*', 'comme un di-homomorphisme',
  'italics', r"un di-homomorphisme", r"un \emph{di-homomorphisme}")
F(160, '(21.3.2)', 'On en déduit un *homomorphisme canonique de* A-*modules*', 'On en déduit un homomorphisme canonique de $A$-modules',
  'italics', r"On en déduit un homomorphisme canonique de $A$-modules",
  r"On en déduit un \emph{homomorphisme canonique de} $A$-\emph{modules}")
F(160, 'After (21.3.2.2)', 'provient de (21.1.5, (ii))).', 'provient de (21.1.5), (ii)).',
  'punctuation', r"de (21.1.5), (ii)).", r"de (21.1.5, (ii))).")
F(160, 'Before (21.3.2.3)', "'On posera' (indented paragraph) before the displays (21.3.2.3)-(21.3.2.4)", 'absent',
  'missing', r"\begin{align}¶\tag{21.3.2.3}", r"¶On posera¶\begin{align}¶\tag{21.3.2.3}")
F(160, '(21.3.2.3)', 'Θ_{B/A}=Ω¹_{B/A}⊗_B A_{[j]} (no comma)', 'A_{[j]},',
  'punctuation', r"A_{[j]},\\", r"A_{[j]}\\")
F(160, '(21.3.2.4)', 'Ξ_{B/A}=Ker(π_{B/A}) (no full stop)', '\\operatorname{Ker}(\\pi_{B/A}).',
  'punctuation', r"\operatorname{Ker}(\pi_{B/A}).", r"\operatorname{Ker}(\pi_{B/A})")

# ---------------- checks ----------------
ok = True
spans = {}
for i, d in enumerate(findings):
    fx = d['fix']
    if fx is None:
        continue
    path = os.path.join(RUN, 'page_%03d.tex' % d['page'])
    # page extracts are CRLF; the release sources (and the fixes) use LF
    text = open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    n = text.count(fx['old'])
    if n != 1:
        print('NOT UNIQUE (%d) p%d #%d: %r' % (n, d['page'], i, fx['old'])); ok = False
        continue
    if fx['old'] == fx['new']:
        print('NO-OP p%d #%d' % (d['page'], i)); ok = False
    s = text.index(fx['old'])
    spans.setdefault(d['page'], []).append((s, s + len(fx['old']), i))
for page, lst in spans.items():
    lst.sort()
    for (a0, a1, ia), (b0, b1, ib) in zip(lst, lst[1:]):
        if b0 < a1:
            print('OVERLAP p%d: #%d and #%d' % (page, ia, ib)); ok = False

# apply all fixes per page to be sure they compose
for page in sorted(spans):
    path = os.path.join(RUN, 'page_%03d.tex' % page)
    text = open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    for d in findings:
        if d['page'] == page and d['fix']:
            assert text.count(d['fix']['old']) == 1, (page, d['fix']['old'])
            text = text.replace(d['fix']['old'], d['fix']['new'])

counts = {}
for d in findings:
    c = counts.setdefault(d['page'], [0, 0, 0])
    if d['kind'] == 'convention':
        c[1] += 1
    elif d['kind'] == 'misprint_in_print':
        c[2] += 1
    else:
        c[0] += 1
print('counts (normal/convention/misprint):', {k: '/'.join(map(str, v)) for k, v in sorted(counts.items())})
print('total', len(findings), 'ok' if ok else 'PROBLEMS')
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(findings, f, ensure_ascii=False, indent=1)
    print('written', OUT)
