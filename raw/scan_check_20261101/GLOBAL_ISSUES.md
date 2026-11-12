# EGA French: issues that need a document-wide change (not page fixes)

Collected from the checkers; each needs one decision and one change in the preamble or environments, then a check.

1. Statement headings: the print sets the number in bold (Proposition **(1.2.3)**), the environments set it italic.
2. `remark` environment is italic (`\itshape`), but the print sets remarks in roman (e.g. Remarque (2.4.8), p. 103);
   inside it `\emph` words come out upright. Check how other remarks are printed before changing the environment.
3. `notation` environment prints "Notations"; at (2.2.10) the print has "Convention de notations".
4. Bold roman chapter numerals in references, like convention 2 for 0: "(**II**, 2.4.3)" (p. 101); likely also III, IV.
5. Convention 7: the long dash for set difference (X—Y) is a minus sign; redefine `\setmin` as the long dash and use it
   where the print has the dash (only for set difference, not subtraction).
6. Coproduct signs: the print has ∐ / ⨿; the TeX has `\bigsqcup` / `\sqcup` (p. 104).
7. The print's bold Z for the integers; the TeX has `\mathbb{Z}` (p. 90). Probably a preamble mapping.
8. Page splitting: section files that begin mid-page (EGA I: pages 97, 104, 119, 127, 140, 155, 164, 169, 180);
   fixed in prep_batch.py (continuations attached); pages 97, 119, 127 were checked without their continuation.
9. Sharp sign: `ega1-1-fr.tex` writes `^{\#}` (typesets #) where the print has ♯; `ega1-2-fr.tex` uses `\sharp` (13
   occurrences in ega1-1; checker convention 9).
10. Unnumbered-heading statements: (3.2.6.3), (3.2.6.4) are printed as a bold number plus an italic statement; the
   `lemma` environment adds "Lemme (…). —", which the print does not have (p. 107). Needs an environment such as
   `env` with an italic body.
11. Statement titles in parentheses: the print has "Proposition (3.3.9) («…»). — Soient"; the TeX gives
   "Proposition (3.3.9). — («…»). Soient" (p. 109).
12. `proof` environment: it prints "Démonstration. —" before proofs where the print has no heading (pp. 141-144,
   proofs of (6.1.2)-(6.1.4); EGA I uses the environment 61 times). Check how the print introduces proofs elsewhere.
13. Bold italic **P**: the print sets the property letter **P** (pp. 139-140, Remarque (5.5.12)) and the projective
   P of P(E), P^n (findings for pp. 110-129) in bold italic; the TeX has `\mathbf{P}` / `\textbf{P}` (149 times in
   ega2-1-fr.tex). Candidate global change `\mathbf{P}` -> `\boldsymbol{P}` after checking a sample in each volume.
14. `\omega^b` for the print's ω^♭ (pp. 120-129); check for the same flat sign elsewhere.
15. "rg" (rang): printed italic on p. 148 ((6.4.5) and its displays), set upright by \operatorname{rg} / \rg in the TeX; p. 148 fixed locally with \mathit{rg}. Check other pages before a global change.
16. Item labels in italic statements: \item[(i)] comes out italic inside italic statement environments, the print sets roman-numeral labels (i), (ii) upright (pp. 150-154: 18 labels in (6.5.1), (6.5.4), (6.5.5), (6.6.4), (6.6.6), fixed locally with \textup). Lettered labels a), b) are italic in the print (Lemme (1.3.2)). A global rule (roman numerals upright) would cover the rest of the edition.
17. To verify before any change: the introduction checker (pp. 5-9) reports capital letters in formulas printed upright (X->Y, y in Y, A) where the TeX's $X$ is italic. Check a sample of formula pages in each volume before deciding; it may hold for the introduction's typeface only.
18. Chapter 0 (ega0-1-fr.tex): the category letter K is bold italic in the print, \mathbf{K} in the TeX (97 times; pp. 23-25 fixed as page fixes); same decision as item 13.
19. Chapter 0 (ega0-1-fr.tex) writes sheaf letters with \mathcal (about 2,100 times) where the other EGA I files use \mathscr; the print has the script shape. Candidate: \mathcal -> \mathscr in ega0-1 after a sample check.
    Item 17 (upright capitals in formulas) is now reported for pp. 21-25 too.
20. Blank lines around \oldpage at page breaks that fall mid-sentence make paragraph breaks the print does not have (heuristic count: 192 markers, 30 in ega0-1, 91 in ega2-1); the checkers fix them page by page.
21. ega0-1-fr.tex displays formulas that the print sets inline (11 times on pp. 16-20, fixed as page fixes).
22. EGA II: ega2-1-fr.tex writes the radical as r / r_+ where the print has Fraktur \mathfrak{r} (several places); \cdots where the print has baseline dots (30 \cdots in ega2-1). Lettered labels a), b) are not uniform in the print (italic in some statements, upright in others): no global rule for them.
    Item 19 also holds for ega2-1-fr.tex (5,946 \mathcal, no \mathscr). Item 17 also holds for EGA II.
23. The print's long dash is used for subtraction too (EGA II p. 14 x⊗y—y⊗x; 0_I p. 13), not only for set difference: the convention-7 decision must cover minus signs in formulas.
    Item 13 caution: on EGA II pp. 103-104 the projective P is printed bold UPRIGHT (matches \mathbf{P}): no blind global \mathbf{P} -> \boldsymbol{P}.
24. EGA II: bold Gamma in Gamma_* (print bold; TeX plain \Gamma_*, ~90 times; candidate \mathbf{\Gamma}_* after a sample check); (TN) printed all bold in section 3.6 (TeX (\textbf{TN}), 18 times; check 2.7-2.9 first); upsilon vs \nu in (3.5.6.1)-(3.5.6.2) and later uses.
25. EGA II: \mathfrak{I} for the printed Fraktur J on pp. 55, 156, 157, 161 (check); (..)^{\sim} for the tilde after a parenthesis ~70 times in ega2-1 (placement right; make consistent with \supertilde in one pass). ega3-1 has 15 more (^\sim / ^{\sim} after a parenthesis): same pass.
    Item 24 refined: bold Gamma only for the graded O_Y-Module Gamma_* (from 3.3.1.1); plain Gamma_* for the section 2 graded S-module: check occurrence by occurrence, no global replace (pp. 56-58 fixed with \bbGamma_*). Hand-made headings \textit{Remarques (3.2.9). ---} etc. set numbers italic (outside the environment fix).
26. EGA II: "(i bis)": bis italic in the print (13 upright in ega2-1; pp. 81-83 fixed, pp. 91-96 unchecked). Parentheses around formulas inside italic statements are upright in the print.
27. EGA II: 16 \cite[...]{...} with an optional argument print ([13, t. I, p. ...]) where the print has ([13], t. I, p. ...); 4 fixed (pp. 120, 122), 12 to do.
28. EGA II: plural "Remarques (n)" printed where ega2-1 sets all 40 remarks with \begin{remark} ("Remarque"); the preamble's remarks environment is unused. Change \begin and \end together per plural remark (e.g. 7.3.9 spans pp. 145-146).
29. EGA II section 8.3-8.5: the indeterminate z of S[z] is printed bold upright (TeX italic $z$); pp. 164-169 partly fixed; check the rest before a global \mathbf{z}. Wrong-font letters (bold italic n, roman Z) are recorded as misprints and reproduced in the diplomatic text.
30. EGA II: \varprojlim_n where the print's lim has no index (7 of 8 on pp. 183-184); diagram labels of leftward arrows on the wrong side (\ar[l]^{..} vs print), pp. 12, 184: check every \ar[l].
31. EGA II section 8.12: the sheaf Proj is printed script P + italic "roj" (page fixes \mathcal{P}\mathit{roj}; \egaShProj exists only in the indexes file and gives upright roj): one macro decision. ^{\wedge} for the raised circumflex (p. 194): a \superhat macro with the \supertilde pass. Plural "Remarques (8.11.8)" on p. 191 still to switch (\begin/\end remarks).
32. Blank printed pages: EGA II pp. 204, 206 have no marker, 212 and 216 do (216 added). Decision: markers for every printed page, blank ones included; add 204 and 206 where the blank page falls (the checkers for 200-211 report the place). Errata headings \paragraph{(...).} carry a full stop the print lacks (p. 217 fixed; pp. 218-222 same pattern).
33. EGA III ch. 0 (ega3-1-fr.tex): category letter C and Ens bold italic in the print (plain $C$ x97, \mathrm{Ens} x23); wavy arrow (\leadsto) where the TeX has \mapsto (64 in the file, check each); final object e bold italic. Item 17 holds for EGA III too.
34. \isoto is \simeq in preamble-base.tex (line 66) but the print has the isomorphism arrow (tilde over an arrow) at its uses on EGA II p. 220 (page-fixed); ega4-20 also uses \isoto: candidate redefinition as \xrightarrow{\sim} after a check.
35. EGA III ch. 0 section 11: the abelian category C is bold italic in the print, \mathcal C in the TeX (188 before \oldpage[III]{81}); in chapter III proper \mathcal C is a sheaf letter (script): no blind replace. $0_{\mathrm I}$ link texts (33 in ega3-1) have a bold 0: one pass with $\mathbf{0}_{\mathrm I}$.
36. ega3-1-fr.tex: 24 statements (11.8.3 to 13.7.5) wrapped whole in \emph inside the itshape statement environments, so they print upright; the print has them italic (pp. 58, 60 page-fixed). Item 19 (\mathcal for script letters: 4,079) and item 21 (displays the print sets inline) hold for ega3-1 too.
37. Čech terms: the print has no check accent on C^.(U,F), H^p(U,F) (15 \check removed on 0_III pp. 50-52); 27 more in ega3-1, 22 in ega3-7, 6 in ega0-1, 3 in ega2-1: check before a global change. Markers placed after \begin{..}\label (ega3-1 pp. 9, 25, 29, 40, 45, 68 to check; 55 done).
    In 12.4.5-12.4.7 (0_III p. 63) the print has plain C^.(U, .) and a bold H^p(U, .). Left in ega3-1 after 0_III p. 65: 14 \check (0_III p. 68: 11; III p. 88: 2; III p. 162: 1).
38. ega3-1: \mathcal K 187 times (0_III pp. 53-64, III pp. 90-162). The 0_III 40-44 checker reports category letters bold italic in the print, but in 12.x \mathcal K^\bullet is a complex of sheaves: check each use, no blind replace (same as item 35 for C).
39. Hyperhomology L bold in the print in 11.6-11.7 (23 page fixes, 0_III pp. 40-44); the derived functors L_pT plain. The hypercohomology R (\mathrm R, 11.4-11.5, pp. 35-39, already applied) still to compare with the print the same way.
40. Remarks headings in ega3-1: (hand-made `\emph{Remarque(s)}` headings inside env: 13-21 by the checkers' counts) `\begin{env}[n] \emph{Remarques}.` gives "(n) Remarques." where the print has "Remarques (n). —". 8 left: 0_III pp. 48, 67, 69; III pp. 97, 101, 125, 134, 138 ((11.7.3), p. 42, converted to \begin{remarks}). One pass with the remarks environment (item 28).
41. Plain itemize lists print bullets; the print has none (Notations (1.2.1), III pp. 85-86; also 0_III pp. 65, 67, 78): one pass (labels removed) after a check of each list.
42. The print has a second, lighter roundhand script H for hypercohomology (0_III pp. 62-64; checker proposed \mathscr H), next to the usual script letters: decide together with item 19 (\mathcal -> \mathscr) so the two alphabets stay distinct; same for the notation-index entries (0, 12.4.1).
44. EGA III §3 (ega3-1): the category letters K, K' (and the set K' of (3.1.2)) and the property letter P are bold
    italic in the print, plain $K$, $K'$, $P$ in the TeX; pp. 115-117 page-fixed with \boldsymbol (41 K, 3 P on
    pp. 115-116 alone): one pass for the rest of §3 after the checkers of pp. 118-136 report.
45. Contents tables: the printed "Pages" column head is missing from the TeX (added as page fixes for EGA II pp. 213-215
    and EGA III part 1 pp. 165-167): check the contents of EGA I, III part 2 and IV and add it the same way.
46b. ega0-21 (EGA IV ch. 0 §21) rewords the print heavily: about 15 places on pp. 154-155, and on pp. 171-173 the
    mathematics itself (k_alpha for k_0 five times, Omega^1_{L/k} for Omega^1_{L/K}, 'nul' for 0, two clauses dropped), all
    restored as page fixes; the word-level comparison of item 46 is most needed for ega0-21 and ega0-19 (19.5.6.5).
46c. ega0-21: two paragraphs at the top of p. 157 were missing from the source (restored by the page check); \operatorname{Der}
    where the print has Dér (8; 6 fixed, 2 at source line 109, p. 155; ega0-20 writes \operatorname{D\acute{e}r}); subsection
    titles with $p$ print a light italic p where the print has a bold upright p (21.2, 21.3 fixed; 21.1 to check); 0$_I$
    (italic I) and n$^\circ$ 3 times each against the edition's $0_{\mathrm I}$ and n\textsuperscript{o}.
46. ega3-1 p. 105: the TeX paraphrased the printed proof of (2.3.4.1) and the end of the proof of (2.3.4) (restored as
    page fixes). The page-by-page check catches such passages; worth a word-level comparison of each file against the
    OCR of the print at the end, to find any paraphrase a checker missed.
47. ega3-1: the raised hat after a parenthesis, (R^nf_*(F))^, is written \widehat{...} over the whole expression
    (pp. 123-125 and 129-130 page-fixed as ^{\widehat{\,}}; about 15 \widehat{...(...)...} left to check): include in
    the \superhat pass of item 31. Also: ega3-1 has no blank line after \] where the print starts a new indented
    paragraph after a display (11 page fixes on pp. 122-126 alone); checkers fix them page by page.
48. Convention 1 caution: in subscripts (\otimes_{k(y)}, EGA III p. 140) the print's k is bold UPRIGHT (\mathbf{k}),
    elsewhere bold italic: no blanket \boldsymbol{k}. Item 13 caution again: the projective P on EGA III p. 158 is bold
    upright. Hand-made "Scholie" headings in env ((2.3.3), (5.4.2)): convert to the scholium environment as (5.1.7).
    Numdam PMIHES 11 has journal pp. 505/506 (printed III pp. 161/162) in swapped order; prep strips for those two
    pages are swapped (the checker compared each with the right image).
49. ega3-1: exponents written ^{,*} / ^{,n} print a comma the print lacks (17 lines; 13 fixed on pp. 153-157; H'^{,n}
    near source lines 10270-10285 to check). Titles written \emph{...} at the start of an env are printed bold followed
    by a new paragraph ((5.2.5), (5.2.6), 5.3.5). Item 23 (long dash for minus) includes the unary minus, O(—n), p. 153.
50. ega3-6 (EGA III part 2): the roundhand hypercohomology H (item 42) occurs 21 times on pp. 138-141 alone, written
    \mathscr H like the ordinary script H: needs the item-42 macro. Item 43 holds for ega3-6 too (6.1-6.3 page-fixed;
    titles at source lines 892, 1128, 1569, 2100, 2972 lack the full stop; print to check).
51. ega3-1 pp. 145, 147: where the transcription turned inline formulas into displays (often joined by \qquad), it lost
    connecting words ("et soit", "avec", "et") and added others ("où", "que", a comma, a repeated M'); fixed as page fixes.
    Worth a scan of the other \qquad-joined displays in all files for the same losses. Convention-2 caution: two
    references keep a wrong-fount light I in the print ((I, 10.9.1 et 10.14.2) p. 144; (II, 4.6.11) p. 146, written
    (\textbf{I}I, ...)): no blind global bolding. Proof-part labels (i), (ii), I), II) are printed upright.
52. ega3-6: remarks set with \begin{namedtheorem}{Remarque(s)} have an italic body; the print sets them roman ((6.3.5),
    (6.3.12), (6.5.7), (6.5.12)): include in the remark-environment decision (items 2, 28, 40). The print has two script
    Tor: the hypertor sheaf heavy (script T, bold italic 'or'), the Tor of modules ((6.4.3)-(6.4.3.3)) light; ega3-6 writes
    \mathscr{T}\!or for both (~60 times; p. 146 page-fixed with \boldsymbol): decide with item 42. Subsection titles:
    ega3-6 6.1-6.6 lack the final full stop, 6.7-6.10 have it; no ega3-7 title has it (item 43, check against the print).
    Items 21 (inline formulas displayed) and 30 (lim indices the print lacks) hold for ega3-6 too.
    Tor mapping in ega3-6 (pp. 150-166): the print's curly hypertor glyph is written \mathfrak{Tor} for the global
    hypertor (and p. 159 (b)) but \mathscr{T}\!or for the local hypertor (p. 150, proof of 6.7.9 p. 162); the thin
    script Tor (p. 159 (a), outer Tor in 6.8.2) is \mathscr{T}\!or too: one mapping decision, then one pass. Item 22
    (\cdots for the print's baseline dots) holds for ega3-6 too.
53. ega3-7: the category Ab is \mathbf{Ab} (47-63 times); the print has it bold italic in running text (pp. 180-191, 9+
    page fixes with \boldsymbol) but bold upright inside the italic statements (7.5.2), (7.5.4): no blind change. Also in
    ega3-7: 22 \widehat{...} over parenthesised expressions (item 47 pass), inline lims printed without index (item 30),
    26 \mapsto + 9 \longmapsto to check for wavy arrows (item 33), 15 \mathcal K for the bold italic category K
    (items 38/44), none of the 9 subsection titles has the final full stop (item 43).
54. ega3-6 symbols, pp. 157-161: \mathfrak{Tor} (55 in the file) prints Fraktur, which the print never has: the print has a
    bold script hypertor and a plain script T with italic 'or'; page fixes write the bold one as
    \boldsymbol{\mathscr{T}\!or} (15 here) and the TeX's choice between the two does not always match the print. The
    lighter roundhand H for hypercohomology was page-fixed as \mathcal H in ega3-6 (whose usual script is \mathscr) but
    as \mathscr H in ega3-1 (whose usual script is \mathcal): item 42 needs one macro for that letter in all files.
    Roman E for the spectral functors of modules ((t)E(X...)), script E for the sheaf versions; roman Tor for termwise
    Tor and Tor of Modules, bold Tor only for the hypertor (ega3-6 has \mathscr E and \mathbf{Tor} throughout; 7 E and
    3 Tor fixed on pp. 157-158; p. 156 and earlier 6.6 pages to recheck). 13 more ($0_{\mathrm I}$, 11.x) references in
    ega3-6 to check (bold 0, no subscript in the print).
55. ega3-7: \kappa(x) 77 times where the print has a bold k(x) (bold upright in subscripts, bold italic elsewhere;
    16 page-fixed on pp. 194-196): one pass with the item-48 distinction. Footnote marks: the print has '(1)' style
    marks (p. 195), the TeX LaTeX's plain superscripts: one preamble decision for all volumes.
56. Errata headings written \textbf{$(0_{\mathrm I},\,...)$} come out in normal weight (math mode ignores \textbf);
    the seven on EGA III p. 217 are page-fixed, the (0_III, ...) headings on the next errata page use the same
    construction; check the errata pages of the other volumes for it.
57. EGA IV chapter 0 (ega0-15, ega0-16, ega0-17): 'no~N' (4, 39, 10 times) where the print has n°; the rest of the
    edition writes n\textsuperscript{o} (673 times): one pass (8 page-fixed on 0_IV pp. 21-25). Items 22 (\cdots, 40 in
    ega0-16), 43 (subsection full stops), 47 (paragraph breaks after displays), 33 (wavy arrows) and the
    markers-after-\begin pattern (item 37) hold for ega0-15/16 too.
58. IV1 preamble: the proof environment takes no optional argument, so \begin{proof}[...] typesets the bracket text
    (6 uses: ega0-16 1 (fixed p. 34), ega0-19 3, ega0-22 2). In ega0-16 the italic definition environment runs on over
    the roman sentences after the printed statement ((16.4.5), (16.4.9) page-fixed): check the other \end{definition}.
    No \subsection title in ega0-14 to ega0-23 (54) has the printed full stop (item 43).
59. ega3-7 pp. 209-211: the module-level functor T^{O_y}, T_i(k(y)) is roman in the print but \mathscr T in the TeX
    (pp. 202-206 have roman T_p already): check after p. 211. EGA III pp. 210 and 212 print '(I, 4.14.5)' (TeX
    '(I, 4.14.5)'); no such item exists in EGA I (1960) or III: unresolved reference, to look up (Err_III?) before
    the corrected edition gives a reading. A convention-7 minus in (7.9.3), p. 208, has no page fix (overlap).
60. EGA IV chapter 0: graded objects carry a raised bullet in the print (S•, gr•); ega0-17, ega0-19, ega0-22 write ^*
    (67 times: \mathbf S_C^*, \gr_J^*, \operatorname{gr}^*); checked in §17 only: check §19, §22, then one pass,
    leaving pullback and dual stars (u^*, v^*, psi_x^*, y_i^*) alone.
61. The printed closing rule at the end of a part (EGA III p. 223, EGA II p. 215) is not reproduced: one decision for
    all parts. Hand-made \emph headings set the statement number italic where the print has bold (Remarque (5.1.11),
    III p. 219) or roman (Proposition (9.3.5), III p. 223): include in the heading/environment pass (items 1, 40).
62. [RESOLVED 2 Nov 05:20: spurious copies removed after scan checks (IV-2 p. 150 second copy; IV-3 ega4-11:1 and ega4-15:9);
    run_IV2 page_150 and run_IV3 pages 116, 223 re-prepared] Duplicated page markers (find_duplicate_markers.py; III 137-167 are parts 1 and 2, expected): IV-2 p. 150
    (ega4-2-fr.tex lines 12330 and 12386), IV-3 p. 116 (ega4-10:1742 and ega4-11:1), IV-3 p. 223 (ega4-14:1684 and
    ega4-15:9). prep_batch.py takes the second copy, so run_IV3 page_116.tex lacks ega4-10 lines 1742-1764 and
    page_223.tex lacks ega4-14 lines 1684-1726: before those batches run, remove the wrong copy (after a scan check) and
    re-prepare the pages. 0_IV-1 p. 12 had the same (ega0-14:565 and ega0-15:12); the ega0-15 copy is removed.
63. WRONG LETTER in EGA IV chapter 0: the print's Fraktur K is written \mathfrak{R} (23 fixed on 0_IV pp. 52-54; 5 more on
    p. 56 in ega0-18; ega0-20 has 199 \mathfrak{R}: check each against the print, since some may be a genuine Fraktur R).
    Also \mathfrak{Q} for the print's Fraktur L (p. 14 fixed by hand after a scan check; pp. 74-75 page-fixed; pp. 84-85,
    105, 117-118, 147 to check). ega0-19 has 193 \mathfrak{R} (pp. 70-92+), ega0-20 199: the checkers were told.
    A third misreading: \mathfrak R for the print's Fraktur N (14 on pp. 92-93). Small-print 'gr' bold on p. 95 (check later
    pages); the hat over B only in B-hat' (\widehat{B'} in the TeX): candidate for convention 8.
    A diagram on p. 53 ((18.1.7.1)) also had wrong targets in the TeX (theta to J' and G where the print has K->G, K->F).
64. ega0-18: the vertical isomorphism sign is written \ar@{}[d]|{\wr}, which draws it on the arrow; the print sets it beside
    the arrow (10 in the file, 3 fixed on 0_IV p. 63). The print's P_n / P_• there is plain roman, the TeX has \mathbf P (18
    times; also roman on p. 66): check the later pages before any change (cf. item 13). Equation numbers printed as
    tags were set as env headings in places ((18.3.6.4), p. 62).
65. EGA IV ch. 0: the print's baseline period in p.1 is written p\cdot1 (12 in ega0-19b fixed on pp. 111-115; ega0-21 has 1,
    ega0-22 has 7 to check).
66. Pairing brackets: the print sets < > signs (det(<y_i^*, u(x_j)>), 0_IV p. 76), the TeX \langle \rangle; also on 0_III p. 79,
    III p. 85, 0_IV pp. 209-210, IV-4 pp. 29, 41, 53-54, IV p. 334 (print not checked there). Bold N in N^(I) (0_IV p. 80)
    against \mathbb N: with the bold Z/Q/R item (7).
69. ega0-19 §19.5.6: 'gr' printed bold (except arrow labels), roman in 19.5.7-19.5.8; 56 page fixes with \mathbf{gr} on
    pp. 96-98 (and pp. 91-95): a macro decision would be simpler. '$(n+1)$-ième' where the print has (n+1) with a superior e
    (pp. 95-100): check the other -ième. The TeX had rewritten the proof of (19.5.6.5) (names w_lambda/w'_lambda and
    silent corrections): restored to the printed text as page fixes (item 46).
70. ega0-20 is the only IV-1 file using \sref (= (\ref{#1}) in the current font): inside italic statements the reference
    prints italic, the print upright (9 page fixes \textup{\sref{..}} on pp. 146-150): redefine \sref as \textup{(\ref{#1})}
    in the IV-1 preamble.
71. WRONG LETTERS in ega0-22 §22.1: Lambda where the print has A (once the reverse) and B for the printed A in
    Upsilon_{C/A/Lambda}, Upsilon_{K/A/Lambda}: 13 page fixes on 0_IV pp. 183-184; the rest of ega0-22 is worth a check.
72. The authors' errata (Err lists, e.g. Liste 3 in EGA IV part 4) were applied silently in places in the TeX (0_IV pp. 212,
    215: 2 of 4 items); the page checks restore the printed reading as misprints. For the corrected edition, list every
    erratum item and confirm the corrected text applies it (with a reference to the list) once the scan check is complete.
73. ega4-2 (EGA IV part 2): drops the prime on the print's script Z' (Coker notation; 10 in (2.1.9)): check every \mathscr Z;
    writes \otimes_Y where the print has \otimes_{O_Y} (but the print also has bare \otimes_Y: check each); hf', gf for h o f',
    g o f; commas after displays the print lacks; 'Soit' for 'Soient'. Items 33 (wavy arrows) and 21 hold here too.
68. ega0-20: 8 references written \sref{X}, (i) typeset '(X), (i)' where the print has '(X, (i))' (2 fixed on p. 132 as
    (\ref{X}, (ii))): one pass after checking the others.
67. ega0-20: the identity map 1_X is written \mathrm{I}_X (13 times; pp. 118, 125 page-fixed; the others at source lines
    777-1218 to check); ega0-18 writes 1_B. IV errata: Err_IV 12 (IV part 4, p. 347) prints its replacement backwards
    ('remplacer p_2-p_1 par p_1-p_2'); the correct reading of (20.4.6.1) is d_{B/A}=p_2-p_1 (Err_IV 12 second half, Err_IV
    13). ega4-errata-addenda-list3-fr.tex puts \oldpage[IV]{348} before Err_IV 3, but printed p. 348 starts at Err_IV 13:
    run_IVback page_347.tex stops at Err_IV 2; tell that checker (or move the marker first).
43. ega3-1: none of the 53 \subsection titles has the printed final full stop (12.4, 13.1, 13.2 page-fixed): one pass. Item 36 (\emph-wrapped statement bodies): 16 propositions, 5 corollaries and 3 lemmas in r20; checkers fix them page by page; grep for leftovers at the end (lines ~3691-3696 and ~4865-4877 were reported).
74. ega4-2 (IV-2 pp. 145-206): `Cohen--Macaulay` (en dash) where the print has a hyphen; all page-fixed by the checkers
    (2 left on p. 206 for the pp. 205-209 batch). n$^o$ (math italic o) for n\textsuperscript{o}: all page-fixed. The
    bold upright subscript R of U_R (§§ 7.3, 7.9) was \boldsymbol R; page fixes write \mathbf{R} (as \mathbf{k}, item 48),
    though the print's R looks sans-serif (\boldsymbol{\mathsf R} would copy it): decide once.
75. Bars over primed or subscripted letters (A-bar'_{p'}, B-bar'_{q'}, IV-2 pp. 170-174): the print bars the letter only,
    the TeX barred the whole expression; 9 page fixes there. This is a bar version of convention 8: check \overline and
    \bar with primes or subscripts in the other parts.
76. Item labels in proofs written \item[\emph{(ii)}] and hand-made headings \emph{I) ...} come out italic; the print sets
    them upright (fixed page by page on IV-2 pp. 200, 201, 204; 8 such labels in proofs in ega4-2). Another 33 sit in
    remark/remarks/examples environments and will turn italic or upright with the decision on the remark font (item on
    roman remarks).
77. ega4-2 writes the print's single script O both as \mathcal O (about 1,000 times) and \mathscr O (87 times), e.g.
    pp. 180-181 against p. 183: decide together with item 19.
78. ega4-8 (IV-3): EGA IV's own references, printed (1.x.y), are written (I, 1.x.y) (23 in ega4-8, 1 in ega4-14, and
    to check: 6 in ega4-16, 7 in ega4-18), and (1.4.3 et 1.5.4) was misread as (I, 4.3 et I, 5.4); page fixes on
    pp. 26, 30-31, 35-39. A check of every "(I, " against the print would catch the rest.
79. IV-3: wrong Fraktur letters: the print's 𝔒_c, 𝔉_c, 𝔏𝔉_c (Fraktur O and a full-size Fraktur c) are written
    \mathfrak D_c, \mathfrak F_c, \mathfrak{LF}_c (page-fixed pp. 15-16); the notation index has the same at
    ega4-15-terminal-fr.tex lines 186-187 (p. 250). The bold italic category C is \mathbf C in ega4-8 (8.2.4)-(8.2.6)
    (19 uses; the bold upright C on p. 7 is the complex numbers) and \mathcal C in ega4-2 (pp. 114, 220-222).
80. IV-3: text follows \end{enumerate} without a blank line 51 times, so it is set without an indent; in the print
    these are indented new paragraphs (2 page-fixed on p. 44). \text{-alg.} inside displays of italic statements
    comes out italic (12 in ega4-8; page-fixed with \textup in (8.8.2.2-3)).
81. MATHEMATICAL (not transcription): the SGA 3 re-edition (VII_B, around 1.6) says the proof of EGA 0_IV 19.3.5 (v)
    is wrong; the stage 3 agent for VII_B part 2 reports that it confirmed this against the ega-fr transcription.
    Verify, and if so give the corrected edition a mathematical note at 0_IV 19.3.5 (with the counterexample or gap).
82. Letters under a tilde printed heavier: the checkers of IV-3 pp. 133, 136 and 177 see the M of 𝓕 = M̃ (and M̃_λ)
    heavier than an ordinary M, and a III p. 152 checker recorded a bold S̃ as a wrong-fount misprint. Decide once
    whether these are bold letters (\widetilde{\mathbf M}) or heavier inking; until then the edition keeps
    \widetilde M everywhere (the p. 133 page fix was reverted, the p. 177 one held: findings_175_179.json, page 177).
83. ega4-12 (IV-3 §12) has lost most of the print's italics (pp. 173-174: 22 phrases page-fixed); later pages are being
    page-fixed by the checkers. \ker (prints "ker") for the print's "Ker": ega4-11 23, ega4-8 4, ega4-9 2; n$^\circ$ for
    n\textsuperscript{o}: ega4-11 ~29, ega4-10 2; gr^* for the print's gr^\bullet: ega4-11 ~95, ega4-8 24, ega4-12 1
    (item 60); the proof-step labels I)-VI) of ega4-11 are bold in the TeX, normal weight in the print.
84. EGA misprints reported by the SGA 3 stage 3 agents (check each against the scan and MISPRINTS.json for the corrected
    edition): IV 11.9.16, last line of the proof, prints 11.9.5 for 11.9.12 (SGA IX part B agent, checked in the
    diplomatic text). See also item 81 (0_IV 19.3.5 (v)).

85. EGA IV p. 229: the print refers to "(15.2.4, (vi))", but Remarques (15.2.4) has only (i)-(v). The diplomatic text
    keeps it. Corrected edition: probably (15.2.4, (v)) (checker 225-229, medium confidence, no erratum found): verify
    against the content of (v) before changing.
86. EGA IV p. 238: the print has v(y), v(y') five times where v(z), v(z') is meant; the TeX keeps it. Possibly the
    authors' slip: check the errata (Err_IV) before the corrected edition changes it.
87. EGA IV-3 corrected edition, errata not applied (see item 72): (14.5.7) on p. 218 cites (14.5.5) for (14.5.6)
    (misprint list); Err_IV 43 (p. 215, l. 15-16) corrects (14.4.10)(i) mathematically.
88. Condition labels written $\a)$ in running text give an italic letter with an upright parenthesis. The print sets
    the whole label italic in roman text (\emph{a)}) and upright inside italic statements (\textup{a)}). ega4-13 is
    fixed (pp. 190-194); ega4-14 had ~97 and ega4-15 ~18, page-fixed by the checkers from p. 190 on; one pass for any
    left. Hand-set \item[b$'$)] labels inside italic statements need \textup (same as item 16).
89. ega4-15 writes the residue-field k as \mathbf{k} 64 times; the print has bold italic outside subscripts (item 48
    distinction). Page-fixed from p. 223 on; one pass with the item 48 rule for the rest.
90. ega4-14/ega4-15 write ($\mathbf{0}_{\mathrm{IV}}$, ...) where the print has a bare bold 0 (pp. 210, 214, 225 fixed;
    p. 230 shows the same; p. 231 to check).

91. EGA IV-4 (ega4-16): the print's script J and Fraktur J are written \mathscr{I} (229) and \mathfrak{I} (132; no
    \mathfrak{J} in the file); ega4-17/18 use J. Page-fixed on pp. 10-14; one pass over ega4-16 after checking pp. 5-9.
92. EGA IV-4: the print's Ω for differentials is italic; the TeX has upright \Omega (ega4-16: 138, ega4-17: 197,
    ega4-18: 219). Fixed on p. 14 with \varOmega; a global change is a candidate (check other parts first).
93. EGA IV-4 (ega4-16): the symmetric algebra S is written \mathscr{S} (42); the print has bold upright S
    (\mathbf{S}, as in the other IV-4 files). Fixed on pp. 10, 14; one pass for the rest. ega4-16 also writes the sharp
    sign as ^\# (26) where convention 9 has \sharp.
94. EGA IV-4 preamble: the examples environment set its whole body italic; the print's body is roman (fixed on p. 6 in
    the preamble, both editions).
95. EGA IV-4 p. 6, corrected edition: in the sentence on the transition maps n and m are swapped in the print; correct
    reading (J_f/J_f^{m+1})^{n+1}, the augmentation Ideal of O_{Y(m)}, kernel of phi_{0m} (checker 005-009).
    Caution to items 91-93 (checker 020-024): p. 20 prints BOTH script letters; I is correct in Lemme (16.4.8.3) and its
    proof (12 \mathscr{I} stay), so no blind I->J pass over ega4-16. (16.4.16.2) shows the sheaf Omega^1_{X/S} italic
    and the modules Omega^1_{O_x/O_s}, Omega^1_{K/k} upright: a global \varOmega pass must tell sheaf from module.
    The 30 \mathscr{S} on p. 20 were the last in ega4-16 (item 93 closed). Item 65 (\cdot for the baseline period)
    also holds in ega4-16 (16 left).
96. EGA IV-4: 'qquad' written without its backslash prints as letters (three fixed in ega4-16 on pp. 37-38;
    ega4-17-fr.tex line 30 has the same). Corrected edition, p. 36: the print's (16.5.9.1) should read (16.5.10.1)
    (inside \textup{...}). Parentheses inside italic statements are upright in the print also around italic words
    ((16.6.3), (16.8.1)): extends item 26 beyond formulas.
97. EGA IV-4 (checker 040-044): item 17 caution - the print has an italic D for the differential operator and a roman
    D for the map on modules (pp. 40, 43): a global upright-capitals change must keep the operator italic. Small
    sub- and superscripts print heavier than the light ones (pp. 42-43); treated as small-type weight, not wrong
    fount, while the bold exponent n on p. 38 was recorded as a misprint: one decision needed. Bold italic "est"
    (p. 42) and "rentiel" (p. 43) recorded as misprints.
98. EGA IV-4 (checker 055-059): derivations D_i, D_lambda print roman, the operators D_p italic; fixed on p. 55 with
    \mathrm{D}. The roman D_i and D of (16.5.8) on p. 29 were left italic (see item 97). Section 16.11 writes
    \operatorname{Diff} where the print has the script sheaf Diff (fixed on p. 55; p. 54 line 54 also script in the
    print; page_054 line 93 and page_053 line 98 to check). The TeX bolds the Greek multi-index epsilon_lambda where the
    print has a light epsilon (fixed on p. 55); the \boldsymbol{\zeta} of 16.11 on p. 54 also looks light: check
    before a global change.
    Checked 4 Nov: the print has roman Diff (modules) where the TeX keeps operatorname{Diff}, e.g. p. 53
    (D in Diff^m_{U/S}); the 15 on pp. 40-46 were passed by their checkers. The zeta^p on p. 53 is bold in the print.
    Checker 050-054: on p. 54 the print sets an upright Omega for the sheaf Omega^1_{U/S} (recorded as a misprint the
    TeX keeps): a global varOmega pass must skip it. p. 53 '(I, 4.3.1)' is the print's (1.4.3.1); the 16.11 title's
    S-prescheme has a bold upright S in the print (pattern of item 46c).
99. EGA IV-4 (checker 065-069): in ega4-17 every marker from p. 59 on has a blank line before it (item 20 pattern);
    by the TeX the break is mid-sentence at pp. 61, 64, 71, 73-75, 77, 78, 80-82, 84 (unchecked against the print);
    fixed at 66, 67, 70; later checkers are told. The blank line before marker 65 splits 'que A est une | k-algebre
    finie' (p. 64 segment: replace 'que $A$ est une' + blank line). ega4-17 line 183 (p. 61) '(I, 4.3.1)' is the
    print's (1.4.3.1), as on p. 65.
    DECIDED 4 Nov (item 97; the user left it to Claude): small sub- and superscripts all print a little heavier
    because the small sizes of the typeface are cut heavier relative to their size (and ink spreads more at small
    sizes); that is the font, not bold: no markup, not reported. A single letter that is visibly bolder than the same
    letter at the same size nearby (side-by-side crop), as the exponent n on p. 38, is a wrong-fount letter: recorded
    as a misprint under item 29 (diplomatic as printed, corrected edition normal). No global change.
    Checkers 070-074 / 075-079: from marker 72 on, the ega4-17 markers also have a blank line AFTER them; at a mid-
    sentence break both blank lines must go (\oldpage ends with \ignorespaces, which does not skip a \par). Checked
    against the print: 71, 73, 74, 75, 77, 78, 80 are mid-sentence; 72 starts with the 17.7 heading (blank lines stay).
    All fixed through marker 80. Also the item 80 pattern in ega4-17: text right after \end{enumerate} without a blank
    line loses the print's indent (two page-fixed on p. 73).
100. Decided 4 Nov 2026 (Claude; the user asked for the correct rule, 'do whatever the correct thing is'): heavier
    letters at the END of a line, together with the punctuation or superscript next to them, whose shapes are
    unchanged, are heavy impression of the line's last sorts, not a wrong fount: not recorded, not reproduced.
    A wrong fount is recorded only where the letter's shape differs or the heaviness is isolated mid-line (item 97).
    Applied on p. 114 (the n over the wedge with the u after it, the final e of 'module', 'etale,'): the three
    entries were dropped from findings_110_114.json; findings_110_114.json.orig keeps them.
101. EGA IV-4 (checker 140-144), caution on item 96: in (18.6.14) (i)-(iii), p. 141, parentheses around wholly
    italic phrases are printed italic; they are upright where 'resp.' or a reference stands next to them. Item 96
    (upright parentheses inside italic statements) must not be applied globally; fix each by the print.
102. EGA IV-4 (checker 165-169): sections 18.10-18.11 of ega4-18 reword the print in many places (item 46):
    renamed variables (y' for z, t_i for s_i), rewritten notation (X x_Y Y' for X_(Y'), Z|_U for g(U), f|_Z for
    f|Z, O_{Y,f(x)} for O_{Y,y}), 'c'est-a-dire' for 'i.e.', an added x', dropped '(17.5.7)' and 'donc', a whole
    sentence missing before (18.10.21), K/k_0 for the print's K/k in (18.11.1). Fixed on pp. 165-169; the English
    and other translations made from this French will carry the same rewordings until the port pass.
    Headings A)-D) of 18.10 set the label italic where the print has it upright (item 76).
103. EGA IV-4 (checker 180-184): the item 78 misreading also takes the form (II, x.y): on p. 182 the TeX has
    "(II, 3.1)" where the print has EGA IV's own (11.3.1). Check every "(II, " and "(I, " reference in ega4-18 and
    later files against the print; real EGA I and II references (bold numeral in the print) also occur.
104. EGA IV-4 (checkers 195-199, 200-204): the rewording of item 102 continues in § 19.4-19.5 of ega4-18:
    rewritten notation (rg subscripts, (u(E))^n_(t), t_j renamed t_i, the print's λ_00 written λ_{𝟎,0}), silent
    corrections of the print (Proj(⊕𝔍^n), 'de même l'image', u_X) and five inline formulas set as displays; all
    fixed by the print on pp. 195-204. After p. 204 ega4-18 still had 82 gr^* where the print has gr• (items 60, 83)
    and many \mathfrak R where the print has a Fraktur K (item 63); the checkers fix each by the print, no global
    replacement. The corrected edition rewrites the proof of (19.4.6) (i) (a mathematical correction): the
    diplomatic italics fixes there were not carried over (resolve_replay_left_20261104.py).
105. EGA IV-4 (checker 205-209): § 19 writes 'M-régulière' with a text-mode M; inside italic statements it prints
    italic, while the print has it upright like every formula capital. Part of item 17 (still open): a decision on
    upright capitals must cover text-mode letters too.
106. EGA IV-4 (checker 215-219): the Fraktur letters of § 19.7 need a letter-by-letter check: of the 136 \mathfrak R
    on pp. 215-219, 134 are the print's Fraktur K and 2 (the gr^d on p. 217) its Fraktur L; the TeX also writes \mathfrak J^h
    for the print's Fraktur L^h ((19.7.1.19), p. 218). \cdots stands for the print's baseline dots (10 on these pages).
    The proofs of (19.7.3)-(19.7.5) stood inside the italic corollary environments (moved); other § 19 corollaries may
    have the same fault. The print repeats the inclusion sign at the line break of (19.7.1.15) and (19.7.1.17): the same
    open question as run_III2 p. 169. Text that continues a sentence after an env display prints indented where the
    print continues flush left: not reported page by page; one global decision needed (\noindent after such
    displays, or no paragraph break after the env). Corrected edition: the end of the proof of (19.7.1.16) is rewritten
    there (with a correction note), and p. 219 reads gr(O_{X,z}) for the print's gr(F_z); the typographic fixes were
    adapted to that wording (resolve_replay_left_20261104b.py).
107. EGA IV-4 (checker 230-234), ega4-20 (§ 20): \vphi is defined as \phi in preamble-base.tex (the stemmed
    phi) while the print has the curly phi (\varphi): 54 in ega4-20, 31 in ega2-errata-addenda, 8 in ega2-indexes;
    one preamble change once the EGA II pages are checked, no page fixes. \sref prints its own parentheses, so
    (\sref...) comes out doubled: left at ega4-20 lines 13, 30, 383, 728, 729 and ega4-21b lines 81, 223, 358, 657, 917.
    \sref[0\textsubscript{I}] sets the subscript I bold (the print's is light); \mathscr{P}\!s.\!\operatorname{hom} sets hom
    upright (the print: italic s.hom, 14 in ega4-20); \sref{...}[(d)] prints (d) where the print has an italic label
    without opening parenthesis; ega4-20 has 25 \mapsto and no \leadsto, and all 8 on pp. 230-233 are wavy
    arrows in the print. The running checkers of § 20 were told (4 Nov) to page-fix all but \vphi.
    Decided 4 Nov: the EGA II print (p. 218, errata) has the curly phi too; \vphi is now \varphi in the r20 preambles
    (BASE, IV4, standalone; both editions) and in source/preamble-base.tex. Older release snapshots unchanged.
108. EGA IV-4 (checkers 225-229, 235-239), § 20 conventions agreed for the checkers: the print's bold 0 with a light
    subscript I is \sref[$\mathbf{0}_{\mathrm I}$]{...} (0\textsubscript{I} bolds the I; plain \sref[0] drops it: 3 in
    ega4-20 fixed, 15 in ega4-21b to check); italic s.hom is \mathscr{P}\!s.\mathit{hom}; where \sref adds parentheses
    to bare printed numbers (n^os 21.1 à 21.7) the reference is set with \hyperref, while the print's real double
    parentheses stay (p. 235, p. 226). ega4-20 writes -module where the print has -Module (12; 10 fixed on pp. 226-229);
    its 4 \isoto are \simto (item 34).
109. EGA IV-4 § 21 (checkers 255-269), decided 4 Nov: the print sets Y(D) (from (21.2.12) on) with a heavy sans-serif Y
    (crop run_IV4/crops_260_264/p262s3_YD.png): written \boldsymbol{\mathsf{Y}}; a bare Y stays roman. The \mathsf{Y} page-fixed
    on pp. 260-267 before the decision get one replacement pass after the § 21 checkers finish; the same rule answers
    item 74's question on the sans-serif R of U_R (IV-2), to be applied in the same pass. The print's script I (Id.inv_X,
    I_X, I_U) is written \sh{J} in ega4-21 (fixed by the checkers); the print keeps script J for general Idéaux. Section titles
    in ega4-21a lacked the print's final full stop (fixed). ega4-21 has 45 \mapsto where the print has wavy arrows.
110. EGA IV-4 (checker 295-299): the print numbers both the Lemme on p. 294 and the Proposition on p. 295 (21.10.13); the
    diplomatic edition keeps the duplicate (recorded as a misprint, fix null). The corrected edition needs an editorial
    number for one of them, after checking which one the later references to (21.10.13) mean (ega4-21b has one label
    IV.21.10.13). Also in ega4-21b: commas after displays where the print has none (item 73) and missing paragraph
    breaks after displays (item 47), fixed page by page. The corrected edition rewrites the end of the proof of
    (21.10.16) (p. 297); two print fixes there were resolved by hand (LEFT_DECISIONS_IV4_297.json).
    Item 109, applied 5 Nov: the 9 bare sans-serif Y left from before the decision (pp. 262, 267) are now bold in both
    editions (boldsfY.py; logged per page in both FIXLOGs). Port: the English needs the same replacement. Item 74's
    U_R (IV-2) is NOT yet changed: each needs a look at the print first.
111. EGA IV-4 end matter (run_IVback, 5 Nov): the printed rules (closing rules under the index, p. 339, and the contents,
    p. 343; the rule above the colophon, p. 361) were held out of the findings pending item 61; the .orig findings files
    keep them (findings_338_343.json.orig entries 1 and 17, findings_360_361.json.orig entry 18). Corrected edition only,
    checked against the main text: index 'Suite de sections transversalement régulière' 19.1.2 -> 19.2.1; contents
    17.4 65 -> 63, § 20 and 20.0 223 -> 225, 20.1 224 -> 226 (current_items_endmatter.json). The errata file's
    {\hyperlink...} references take the italic of italic statements where the print has them upright (fixed with \textup).
