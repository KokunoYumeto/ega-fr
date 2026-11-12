# French corrected edition: places to recheck against the print (reported by the English hand pass)

The English differs from the French here, and the English reading is the one the mathematics needs. Check the print:
a misprint of the print goes to MISPRINTS.json and the corrected edition; a transcription error to both editions.
- 0_IV-1 p. 17 (15.1.15): French (1<=i<=n) twice, English (1<=i<=n+1); the proof needs n+1.
- 0_IV-1 p. 25 proof of (16.2.2.2): French M'_n = M' ∩ q^n M', English M' ∩ q^n M (the correct filtration).
- 0_IV-1 p. 49 proof of (17.3.4): French cites (16.4.6, (i)), English (16.4.6, (ii)), which is the statement used.
- 0_IV-1 p. 62 (18.3.6): French refers to the functor (18.3.4.1), English (18.3.5.1), which makes sense.

**Checked against the print, 5 Nov:** all four are misprints of the print; the French TeX of both editions follows the
print, as a diplomatic text should. p. 26 (16.2.2.2) and p. 62 (18.3.6) were already corrected in the corrected
edition (MISPRINTS entries 525, 536). p. 17 (15.1.15, both displays: n+1) and p. 49 (17.3.4: (16.4.6, (ii))) were
corrected now (apply_french_recheck.py; FIXLOG_CURRENT source french_recheck; MISPRINTS entries added), carried into
the Spanish corrected edition IV-1 (apply_recheck_es.py), and pushed (ega-fr 2a16c38, ega-fga-es 5971923).

**Further candidates (reported by the English slips agents, 5 Nov), to check against the print and the mathematics:**
- IV-4 p. 221, proof of (19.8.2) (i) (FIXLOG ids 22725, 22727): ⊗_{O_X} k(s), where ⊗_{O_S} k(s) seems meant.
- IV §19, proof of (19.6.4) (i): "sous-…-algèbre" where a sub-module seems meant.
- 0_IV p. 89 (proof of 19.4.7): the print has the Fraktur K of B₀/𝔎B₀ throughout; the French TeX kept \mathfrak R three
  times (a transcription error): corrected in both French and both Spanish editions on 5 Nov (fix_0IV_p89.py).
- 0_IV (21.2.2), last words of the proof: the corrected French reads "E est B^p-triviale" (the misprint pass corrected
  the print's "B-triviale", MISPRINTS p. 158); the slips agent argues that applying (21.2.1, (i)) gives an
  A-homomorphism right inverse, so the conclusion (definition 19.9.1) should be "A-triviale" and the print's B is a
  misprint for A. The English keeps "B-trivial" until this is settled.
- Editorial footnotes: the corrected French has five footnotes the print does not (I p. 175, I p. 184, 0_IV p. 17,
  IV-2 p. 177, IV-4 p. 216); the two without a label are now labelled "Précision éditoriale" / "Correction
  éditoriale" (label_editorial_footnotes.py). The English does not carry them yet.
- EGA III (slips agent of §§2-6, 5 Nov): places where the corrected French follows the print although it looks wrong
  (the English now translates them as printed): 5.4.1 "(p∘i)^ = w" (read literally the inverse of w; ĝ = w meant?);
  6.6.4 Card(σ) = −(h+1), Card(τ) = −(k+1), Card(σ)+Card(τ) = −h−2 (the old English had 1−h, 1−k, 2−h).
- EGA IV errata and §21 (slips agent of §§20-21, 5 Nov): print readings the corrected French keeps, which the English
  corrects: (Err_IV, 19) K = k[T_1,...,T_n] where k(T_1,...,T_n) is meant (scan checked: the print has brackets);
  (Err_IV, 44) "toute partie fermée" where an irreducible closed subset is meant; proof of (21.14.1) "tout idéal
  premier q de B non contenu dans p" (the English adds "of height one").
- EGA IV-2 (slips agent of §§2-5, 5 Nov): (5.7.3) (v) cites (5.8.5), but Serre's criterion is (5.8.6) (the English
  cites 5.8.6 with a footnote); end of the proof of (4.2.1): "première ... seconde relation (4.2.1.1)", while the
  relation computed is the second as typeset (the English says "second ... first").
- Chapter 0 (slips agent of §§9-13, 5 Nov): 0_III (12.3.3) proof writes "p\setmin 1" for p - 1 in the corrected French
  (\setmin is for set difference; check the print's sign); (12.1.4) "(M, V, 1.1. a))": the corrected French has a
  period after 1.1 where (12.1.7) and elsewhere write "1.1 a)": check the print.

**Decided and applied, 5 Nov (RECHECK_DECISIONS.json, apply_recheck_decisions.py):** 15 misprints corrected in the
corrected French (35 edits with the English and Spanish), 3 not misprints (0_IV p. 89 was a transcription error, the
editorial footnotes, 0_III 12.3.3 and 12.1.4); 0_IV (21.2.2) now reads A-triviale. Pushed ega-fr 7c6065e, ega-en 9e13cf2,
ega-fga-es ec9dd92. Open: the Spanish standalone package editions/IV3_reproducible lags behind editions/IV3 (it had
diverged before 5 Nov; it has none of the 5 Nov corrections): decide whether to regenerate it from editions/IV3.
