# EGA: where the newest French text is, and what changed (for the Chinese, Japanese and Korean translations)

The French EGA has been checked page by page against the printed original (Publ. Math. IHÉS, 1960–1967), 1–5 November
2026. Translate from the result, not from older copies.

## Translate from

**The corrected French edition** (the correct reading wherever the print has a misprint):

    user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\
        BASE\native\   EGA 0, I, II, III (folders ega1, ega2, ega3; preamble-base.tex; EGA_FR.tex)
        IV1\native\ega4\   EGA IV, part 1 (chapter 0 §§14–23, chapter IV §1)
        IV2\native\ega4\   EGA IV, part 2
        IV3\native\ega4\   EGA IV, part 3
        IV4\native\ega4\   EGA IV, part 4, with its end matter

GitHub has the same text (`KokunoYumeto/ega-fr`, commit 2a16c38 of 5 November, with the misprint corrections); a fresh
clone works as well. Read the local copy; do not edit it (it is the working copy of the check). The diplomatic edition, which keeps the
print's misprints, is the same tree with `diplomatic` for `current`.

## If you translated from an older French version

Every change is logged, one JSON object per line, with the file, the part, the printed page, and the exact old and new
text:

    user\Documents\ega_scan_check_20261101\FIXLOG_CURRENT.jsonl   (corrected edition: 24788 edits)
    user\Documents\ega_scan_check_20261101\FIXLOG.jsonl           (diplomatic edition)

Find the entries for the pages you have translated (fields `part` and `page`, the same as the `\oldpage[PART]{N}`
markers) and carry the changes that affect your translation: formulas, letters, indices, references, numbers, missing or
wrong words. Most entries are French typography (italics, spacing, punctuation) and need nothing in a translation that
does not reproduce it. Misprints of the print and their correct readings are listed in `MISPRINTS.json` in the same
folder; `MISPRINT_KEEP.md` lists the 21 places where the print's reading was kept because the correction is not certain.

## Keep in your translation

- The page markers `\oldpage[PART]{N}` at the same places: corrections are carried into the translations by printed page.
- The `\label` keys, the reference commands and the macro names of the French TeX (do not translate TeX commands).
- The mathematics exactly as in the corrected French: symbols, indices, references, numbering. The French now follows the
  print's typography (bold chapter numbers in references, bold residue field k, upright parentheses inside italic
  statements, `\setmin` for set difference); keep those where your edition renders them.

## The English is not a reliable intermediate

The English EGA (`user\Documents\ega_scan_check_20261101\ega-en\tex`) is being brought up to date with the same
corrections, and its own translation errors are being collected in `ENGLISH_SLIPS.md` (omitted sentences, paraphrased or
replaced proofs, wrong references, for example in EGA III §7, 0_IV §§18–21, IV §§6, 8, 19, 21). Translate from the French;
if you used the English for a passage, check that passage against the French.
