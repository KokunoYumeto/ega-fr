import json
import pathlib

RUN = pathlib.Path(r'user\Documents\ega_scan_check_20261101\run_IV3')
OUT = RUN / 'findings_185_189.json'


def F(page, where, scan, tex, kind, old, new, confidence='high', convention=None, note='', corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind, 'convention': convention,
         'confidence': confidence, 'fix': None if old is None else {'old': old, 'new': new}}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d


L = []

# ---------------- page 185 ----------------
L.append(F(185, "proof of (12.3.3), strip 2: 'on a Ker(v)=lim(Ker(v_λ)), Im(u)=lim(Im(u_λ))'",
           "Ker(v)=lim→(Ker(v_λ)): the argument of lim is in parentheses (crop p185_lim.png)",
           r"\operatorname{Ker}(v)=\varinjlim\operatorname{Ker}(v_\lambda)", 'formula',
           r"\operatorname{Ker}(v)=\varinjlim\operatorname{Ker}(v_\lambda)$",
           r"\operatorname{Ker}(v)=\varinjlim(\operatorname{Ker}(v_\lambda))$"))
L.append(F(185, "same sentence: 'Im(u)=lim(Im(u_λ))'",
           "Im(u)=lim→(Im(u_λ)) (same crop)",
           r"\operatorname{Im}(u)=\varinjlim\operatorname{Im}(u_\lambda)", 'formula',
           r"\operatorname{Im}(u)=\varinjlim\operatorname{Im}(u_\lambda)$",
           r"\operatorname{Im}(u)=\varinjlim(\operatorname{Im}(u_\lambda))$"))
L.append(F(185, "after Lemme (12.3.3.1): 'donc on peut, sans changer l'hypothèse ni la conclusion, supposer u injectif'",
           "sans changer l'hypothèse ni la conclusion (crops p185_sans.png, p185_changer.png)",
           "sans changer ni l'hypothèse ni la conclusion", 'extra',
           "sans changer ni l'hypothèse", "sans changer l'hypothèse",
           note="The TeX adds 'ni'."))
L.append(F(185, "same paragraph: 'si R est l'image de v et p : N→R la surjection canonique'",
           "italic p (spur at the top of the stem and foot serif of italic p; not ρ) (crop p185_rho1.png)",
           r"$\rho:N\to R$", 'symbol', r"$\rho:N\to R$", r"$p:N\to R$",
           note="Same letter p in the next three entries (crops p185_rho2.png, p185_rho3.png)."))
L.append(F(185, "same paragraph: 'on a p∘u=0'", "p∘u=0 (italic p)", r"$\rho\circ u=0$", 'symbol',
           r"$\rho\circ u=0$", r"$p\circ u=0$"))
L.append(F(185, "same paragraph: 'le noyau de p⊗1'", "p⊗1 (italic p)", r"$\rho\otimes1$", 'symbol',
           r"$\rho\otimes1$", r"$p\otimes1$"))
L.append(F(185, "last line: 'on a évidemment Ker(p)=Ker(v),'", "Ker(p) (italic p)", r"\operatorname{Ker}(\rho)", 'symbol',
           r"\operatorname{Ker}(\rho)", r"\operatorname{Ker}(p)"))

# ---------------- page 186 ----------------
L.append(F(186, "proof of (12.3.3.3), first pair of displays, line 1: '0→M→Z→H→0'",
           "no punctuation after the display line (crop p186_disp1.png)", r"0\to M\to Z\to H\to0,", 'punctuation',
           r"Z\to H\to0,", r"Z\to H\to0"))
L.append(F(186, "first pair of displays, line 2: '0→Z→N→P→0' (v over the arrow)",
           "no punctuation after the display line (same crop)", r"0\to Z\to N\xrightarrow{v}P\to0,", 'punctuation',
           r"N\xrightarrow{v}P\to0,", r"N\xrightarrow{v}P\to0"))
L.append(F(186, "second pair of displays, line 1: 'M/tM→Z/tZ→H/tH→0' (w' over the first arrow)",
           "no punctuation after the display line (crop p186_disp2.png)", r"M/tM\xrightarrow{w'}Z/tZ\to H/tH\to0,", 'punctuation',
           r"H/tH\to0,", r"H/tH\to0"))
L.append(F(186, "second pair of displays, line 2: '0→Z/tZ→N/tN→P/tP→0' (v' over the arrow)",
           "no punctuation after the display line (same crop)", r"0\to Z/tZ\to N/tN\xrightarrow{v'}P/tP\to0,", 'punctuation',
           r"P/tP\to0,", r"P/tP\to0"))
L.append(F(186, "II), l. 3: 'et soit 𝔫 l'idéal 𝔪_s𝒪_{X,x}, qui est contenu dans l'idéal maximal'",
           "comma after 𝒪_{X,x} (crop p186_comma.png)", r"$\mathfrak m_s\mathcal O_{X,x}$ qui est contenu", 'punctuation',
           r"\mathcal O_{X,x}$ qui est contenu", r"\mathcal O_{X,x}$, qui est contenu"))

# ---------------- page 187 ----------------
L.append(F(187, "Corollaire (12.3.4), l. 3: 'des x∈X tels que (ℰxt^n_{𝒪_{X_{f(x)}}}(ℱ_{f(x)}, 𝒢_{f(x)}))_x=0 (resp. ...)'",
           "the formula is set inline in the running text (crop p187_cor_a.png)", r"displayed with \[ ... \]", 'other',
           "tels que\n\\[\n  \\bigl(\\mathscr{E}\\!xt^n_{\\mathcal O_{X_{f(x)}}}\n  (\\mathcal F_{f(x)},\\mathcal G_{f(x)})\\bigr)_x=0\n\\]",
           "tels que\n$\\bigl(\\mathscr{E}\\!xt^n_{\\mathcal O_{X_{f(x)}}}\n(\\mathcal F_{f(x)},\\mathcal G_{f(x)})\\bigr)_x=0$",
           note="Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost. Independent of the convention-6 entry that follows."))
L.append(F(187, "Corollaire (12.3.4), l. 3: '(resp. (𝒯or_n^{𝒪_{X_{f(x)}}}(ℱ_{f(x)}, 𝒢_{f(x)}))_x=0)'",
           "'(resp.' and the closing parenthesis upright (crop p187_cor_b.png)", "italic in the corollary environment",
           'convention', "(resp.\n$\\bigl(\\mathscr{T}\\!or_n^{\\mathcal O_{X_{f(x)}}}\n(\\mathcal F_{f(x)},\\mathcal G_{f(x)})\\bigr)_x=0$)",
           "\\textup{(resp.\n$\\bigl(\\mathscr{T}\\!or_n^{\\mathcal O_{X_{f(x)}}}\n(\\mathcal F_{f(x)},\\mathcal G_{f(x)})\\bigr)_x=0$)}",
           convention=6))
L.append(F(187, "Corollaire (12.3.4), l. 4: 'et l'on a ℰxt^n_{𝒪_X}(ℱ, 𝒢)|U=0 (resp. ...)'",
           "the formula is set inline in the running text (crop p187_cor_c.png)", r"displayed with \[ ... \]", 'other',
           "l'on a\n\\[\n  \\mathscr{E}\\!xt^n_{\\mathcal O_X}(\\mathcal F,\\mathcal G)|U=0\n\\]",
           "l'on a\n$\\mathscr{E}\\!xt^n_{\\mathcal O_X}(\\mathcal F,\\mathcal G)|U=0$",
           note="GLOBAL_ISSUES 21; no connecting word lost. Independent of the next entry."))
L.append(F(187, "Corollaire (12.3.4), l. 4: '(resp. 𝒯or_n^{𝒪_X}(ℱ, 𝒢)|U=0).'",
           "'(resp.' and the closing parenthesis upright (crop p187_cor_c.png)", "italic in the corollary environment",
           'convention', "(resp.\n$\\mathscr{T}\\!or_n^{\\mathcal O_X}(\\mathcal F,\\mathcal G)|U=0$)",
           "\\textup{(resp.\n$\\mathscr{T}\\!or_n^{\\mathcal O_X}(\\mathcal F,\\mathcal G)|U=0$)}", convention=6))
L.append(F(187, "proof of (12.3.4), l. 9-10: 'ℒ'_•=ℒ_•⊗_S S' est encore une résolution gauche de ℱ''",
           "'ℒ'_•=ℒ_•⊗_S S' est encore une résolution gauche' (crop p187_Lprime.png)",
           r"'$\mathcal L'_\bullet=\mathcal L_\bullet\otimes_SS'$, $\mathcal L'_\bullet$ est encore'", 'extra',
           r"\otimes_SS'$, $\mathcal L'_\bullet$ est encore", r"\otimes_SS'$ est encore",
           note="The TeX repeats the subject ', ℒ'_•' before 'est encore'."))
L.append(F(187, "proof of (12.3.4), l. 11-12: '(resp. 𝒩'_•=... est égal à ℒ'_•⊗_{𝒪_{X'}}𝒢') d'après ce qui précède'",
           "no comma after the closing parenthesis (crop p187_dapres.png)", "'), d'après'", 'punctuation',
           r"\mathcal G'$), d'après", r"\mathcal G'$) d'après"))
L.append(F(187, "proof of (12.3.4), l. 12: 'pour tout s∈S, ℰxt^n_{𝒪_{X_s}}(ℱ_s, 𝒢_s)=ℋ^n((ℳ^•)_s) (resp. ...)'",
           "the formula is set inline in the running text", r"displayed with \[ ... \]", 'other',
           "pour tout $s\\in S$,\n\\[\n  \\mathscr{E}\\!xt^n_{\\mathcal O_{X_s}}(\\mathcal F_s,\\mathcal G_s)\n  =\\mathcal H^n((\\mathcal M^\\bullet)_s)\n\\]",
           "pour tout $s\\in S$,\n$\\mathscr{E}\\!xt^n_{\\mathcal O_{X_s}}(\\mathcal F_s,\\mathcal G_s)\n=\\mathcal H^n((\\mathcal M^\\bullet)_s)$",
           note="GLOBAL_ISSUES 21; no connecting word lost."))
L.append(F(187, "§ 13 introduction, l. 4: 'la fonction x⇝dim_x f^{-1}(f(x)) est toujours semi-continue'",
           "wavy arrow (crop p187_wavy.png)", r"\mapsto", 'symbol', "que la fonction\n$x\\mapsto", "que la fonction\n$x\\leadsto",
           note="Wavy arrow (GLOBAL_ISSUES 33), \\leadsto as in the earlier IV-3 page fixes; not convention 3. OUTSIDE the page segment: ega4-13-fr.tex, before its first page marker."))
L.append(F(187, "same formula: 'dim_x f^{-1}(f(x))'",
           "no parentheses around f^{-1}(f(x)) after dim_x (same crop)", r"\dim_x(f^{-1}(f(x)))", 'formula',
           r"\dim_x(f^{-1}(f(x)))$ est toujours", r"\dim_x f^{-1}(f(x))$ est toujours",
           note="OUTSIDE the page segment: ega4-13-fr.tex, before its first page marker. Independent of the previous entry. (Théorème (13.1.3) on p. 189 does print the parentheses.)"))
L.append(F(187, "end of p. 187 / top of p. 188: '... cette fonction est localement constante. Malheureuse-|ment la notion'",
           "one paragraph: the page break falls inside 'Malheureusement'",
           r"blank line before \oldpage[IV-3]{188} (paragraph break)", 'marker',
           "\\emph{localement constante}.\n\n", "\\emph{localement constante}.\n",
           note="OUTSIDE the page segment: ega4-13-fr.tex lines 11-12, the end of the text before its first marker (the old string ends right before \\oldpage[IV-3]{188}). The marker before the split word is right; only the blank line goes (GLOBAL_ISSUES 20)."))

# ---------------- page 188 ----------------
L.append(F(188, "heading 13.1: 'Le théorème de semi-continuité de Chevalley.'", "final full stop",
           "no full stop", 'punctuation',
           r"\subsection{Le théorème de semi-continuité de Chevalley}",
           r"\subsection{Le théorème de semi-continuité de Chevalley.}",
           note="GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))
L.append(F(188, "Lemme (13.1.1): 'Soit ξ (resp. η) le point générique'",
           "'(resp. η)' upright (crop p188_resp.png)", "italic in the lemma environment", 'convention',
           r"(resp. $\eta$)", r"\textup{(resp. $\eta$)}", convention=6))
L.append(F(188, "Lemme (13.1.1): 'de X (resp. Y) et soit'",
           "'(resp. Y)' upright (same crop)", "italic in the lemma environment", 'convention',
           r"(resp. $Y$)", r"\textup{(resp. $Y$)}", convention=6))
L.append(F(188, "proof of (13.1.1): 'Il n'est pas évident a priori que le préschéma X_0 soit intègre, mais'",
           "'intègre' in italics (crop p188_integre.png); the later 'intègre' on this page are upright",
           "'intègre' upright", 'italics', "soit intègre, mais", "soit \\emph{intègre}, mais"))
L.append(F(188, "proof of (13.1.1): 'f^{-1}(η)=f_0^{-1}(η_0)⊗_{k(η_0)}k(η)', subscript",
           "bold upright k in the subscript (crop p188_k.png)", "plain k", 'convention',
           r"\otimes_{k(\eta_0)}", r"\otimes_{\mathbf{k}(\eta_0)}", convention=1,
           note="Bold upright in subscripts (GLOBAL_ISSUES 48), hence \\mathbf{k}."))
L.append(F(188, "same formula: '⊗ k(η)' on the line",
           "bold italic k (same crop)", "plain k", 'convention',
           r"k(\eta)$, et comme", r"\boldsymbol{k}(\eta)$, et comme", convention=1,
           note="Independent of the previous entry."))
L.append(F(188, "Lemme (13.1.2): 'rencontrant f_0^{-1}(η_0) (0_I, 2.1.8), et désignons'",
           "the reference (parentheses and figures) upright (crop p188_ref.png)", "italic in the lemma environment",
           'convention', r"($\mathbf 0_{\mathrm I}$, 2.1.8)", r"\textup{($\mathbf 0_{\mathrm I}$, 2.1.8)}", convention=6))
L.append(F(188, "end of p. 188 / top of p. 189: 'donc un anneau universellement | caténaire (5.6.4)'",
           "mid-sentence page break", r"blank line before \oldpage[IV-3]{189} (paragraph break)", 'marker',
           "anneau universellement\n\n", "anneau universellement\n",
           note="The old string ends the p. 188 segment (right before \\oldpage[IV-3]{189}); the marker itself is in the right place (GLOBAL_ISSUES 20)."))

# ---------------- page 189 ----------------
L.append(F(189, "proof of (13.1.1), l. 2: 'pour tout y_0∈f_0(X_0), toutes les composantes irréductibles de f^{-1}(y) ont une dimension ≥e'",
           "f^{-1}(y): no subscript 0 on f or on y (crop p189_f0y.png)", r"$f_0^{-1}(y)$", 'misprint_in_print',
           r"$f_0^{-1}(y)$", r"$f^{-1}(y)$", corrected=r"$f_0^{-1}(y_0)$",
           note="Misprint in the print: the sentence is about the fibres of f_0 over the points y_0∈f_0(X_0) (f^{-1}(y) is handled in the next sentence), so the correct reading is f_0^{-1}(y_0). The TeX silently half-corrects it (adds the 0 on f, keeps y); the fix restores the printed f^{-1}(y). Note for the corrected edition: its current f_0^{-1}(y) is still wrong; it needs f_0^{-1}(y_0)."))
L.append(F(189, "Théorème (13.1.3): 'la fonction x⇝dim_x(f^{-1}(f(x))) est semi-continue supérieurement'",
           "wavy arrow", r"\mapsto", 'symbol', "dit, la fonction\n$x\\mapsto", "dit, la fonction\n$x\\leadsto",
           note="Wavy arrow (GLOBAL_ISSUES 33), \\leadsto as in the earlier IV-3 page fixes; not convention 3."))
L.append(F(189, "proof of (13.1.3) I): 'on ait X=X_0×_{Y_0}Y, f=f_0×1_Y, où f_0 : X_0→Y_0 correspond'",
           "both formulas inline in the running text, same paragraph (crop p189_ait.png)",
           r"displayed with \[ ... \] (joined by \qquad), with a blank line before and after", 'other',
           "on ait\n\n\\[\n  X=X_0\\times_{Y_0}Y,\\qquad f=f_0\\times 1_Y,\n\\]\n\noù",
           "on ait $X=X_0\\times_{Y_0}Y$, $f=f_0\\times 1_Y$,\noù",
           note="GLOBAL_ISSUES 21; no connecting word lost. The blank lines also made two paragraph breaks the print does not have."))
L.append(F(189, "same proof: 'on sait que f^{-1}(y)=f_0^{-1}(y_0)⊗_{k(y_0)}k(y)', subscript",
           "bold upright k in the subscript (crop p189_proj.png)", "plain k", 'convention',
           r"\otimes_{k(y_0)}", r"\otimes_{\mathbf{k}(y_0)}", convention=1,
           note="Bold upright in subscripts (GLOBAL_ISSUES 48), hence \\mathbf{k}."))
L.append(F(189, "same formula: '⊗ k(y)' on the line", "bold italic k (same crop)", "plain k", 'convention',
           r"k(y)$, et il résulte", r"\boldsymbol{k}(y)$, et il résulte", convention=1,
           note="Independent of the previous entry."))
L.append(F(189, "same proof: 'si p est la projection canonique f^{-1}(y)→f^{-1}(y_0)'",
           "target printed f^{-1}(y_0), without the subscript 0 on f (crop p189_proj.png; the line above has f_0^{-1}(y_0))",
           r"$f^{-1}(y)\to f_0^{-1}(y_0)$", 'misprint_in_print',
           r"\to f_0^{-1}(y_0)$", r"\to f^{-1}(y_0)$", corrected=r"$f^{-1}(y)\to f_0^{-1}(y_0)$",
           note="Misprint in the print (y_0 is a point of Y_0, so the fibre is f_0^{-1}(y_0)); the TeX silently corrects it, the fix restores the printed reading."))
L.append(F(189, "same proof: 'autrement dit, on peut supposer X irréductible.'",
           "'irréductible' in italics (crop p189_irred.png)", "'irréductible' upright", 'italics',
           "supposer $X$ irréductible.", "supposer $X$ \\emph{irréductible}."))
L.append(F(189, "same proof: 'f se factorise en X→Z→Y (g, i over the arrows), où j est l'injection canonique'",
           "the label over the second arrow is an italic i: dot and a short stroke ending on the baseline, no descender, beside the descending g; same shape as the subscript i of X_i on this page (crops p189_arrows.png, p189_label_zoom.png, 600-dpi render p189_label600.png)",
           r"\xrightarrow{j}", 'misprint_in_print', r"\xrightarrow{j}Y", r"\xrightarrow{i}Y",
           confidence='medium', corrected=r"X\xrightarrow{g}Z\xrightarrow{j}Y",
           note="Misprint in the print: the text names the injection j. The TeX silently writes j; the fix restores the printed i. Medium only because the label is heavily inked; no trace of a j descender at 600 dpi."))
L.append(F(189, "same proof: 'tel que F_n(X)⊂f^{-1}(Y—U)'", "long dash for set difference (crop p189_YU.png)", "minus sign",
           'convention', r"f^{-1}(Y-U)$", r"f^{-1}(Y\setmin U)$", convention=7,
           note="\\setmin is defined in the IV-3 preamble."))
L.append(F(189, "same proof: 'comme Y—U≠Y'", "long dash for set difference (crop p189_ferme.png)", "minus sign",
           'convention', r"$Y-U\neq Y$", r"$Y\setmin U\neq Y$", convention=7))
L.append(F(189, "end of p. 189 / top of p. 190: 'donc de la forme | B=A[T_1,...,T_n]/𝔍'",
           "mid-sentence page break", r"blank line before \oldpage[IV-3]{190} (paragraph break)", 'marker',
           "donc de la forme\n\n", "donc de la forme\n",
           note="The old string ends the p. 189 segment (right before \\oldpage[IV-3]{190}); the marker itself is in the right place (GLOBAL_ISSUES 20)."))

OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote', len(L), 'findings')
