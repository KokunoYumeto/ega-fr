# EGA French (ega-fr): fix policy for the scan check

ega-fr is a diplomatic edition: it says what the 1960–67 printing says, page for page.

1. **Transcription errors** (wrong or missing word, symbol, formula, sub/superscript, prime, letter shape, punctuation,
   italics, missing or added text): change the TeX to match the print.
2. **Systematic conventions**: match the print, occurrence by occurrence, after looking at the print:
   1. residue field with bold italic k: `\boldsymbol{k}(x)`;
   2. bold 0 in references to chapter 0: link text `\textbf{0}, 1.4.6`;
   3. plain arrow printed: `\to` / `\rightarrow` / `\longrightarrow` (keep `\mapsto` only where the print has ↦);
   4. isomorphism arrow (arrow with a tilde above): `\xrightarrow{\sim}` (not `\simeq`);
   5. tilde written after a closing parenthesis, (…)~: `(\Gamma(v))\supertilde` (macro in preamble-base.tex);
      Ã^n: `\widetilde{A}^n`;
   6. roman words inside an italic statement: `\textup{...}`; printed italic words left upright: `\emph{...}` (inside an
      italic environment, drop `\emph` where the print shows no change of face);
   7. long dash for set difference X—Y: `X\setmin Y` only after `\setmin` is redefined as the long dash
      (not yet done: leave convention 7 for a later global pass).
3. **Misprints in the print** (user, 1 Nov 2026: "we have the diplomatic edition and the corrected editions ... keeping
   printed errors in the diplomatic"): the diplomatic text keeps the printed error. If the diplomatic TeX silently
   corrected a misprint, change it back to the printed reading. Record every misprint in `MISPRINTS.json` (page, where,
   print, correct reading, what the TeX did) so the corrected edition (`editions/<release>/current`) and the
   translations get the correction. Transcription fixes (rules 1-2) apply to both editions; FIXLOG.jsonl keeps exact
   old/new strings so they can be replayed on the corrected edition's sources.
4. **Page markers**: an `\oldpage[...]{N}` marker must stand where printed page N begins; move it if it is misplaced.
5. Every change is logged in `FIXLOG.jsonl` (file, page, old, new, finding source). Change only what a finding
   supports; keep the line structure; never rewrite surrounding text.
6. After each batch: compile the touched section with the stub (`stub_<file>.tex`) and fix any error you introduced.
