# Vérification de la transcription française d'EGA sur les pages imprimées (1er–5 novembre 2026) : registres

Ce dossier contient les registres bruts de la vérification page par page de la transcription LaTeX d'EGA (chapitres 0
à IV, environ 1 800 pages imprimées des *Publications mathématiques de l'IHÉS* 4, 8, 11, 17, 20, 24, 28 et 32) sur
les numérisations Numdam des fascicules. Les textes de méthode sont en anglais, comme ils ont été rédigés.

## Ce qui a été vérifié, et comment

- **Texte vérifié :** les deux éditions de ce dépôt, `editions/2026-10-24-r20/diplomatic` (le texte imprimé, coquilles
  comprises) et `editions/2026-10-24-r20/current` (l'édition corrigée).
- **Unité de travail :** un lot de cinq pages imprimées. Pour chaque page, le LaTeX de la page (d'un repère
  `\oldpage` au suivant) et la numérisation à 300 dpi, recadrée et coupée en quatre bandes horizontales.
- **Vérificateurs :** des sous-agents Claude Opus 5.5 (Anthropic), lancés dans Claude Code, un par lot, avec la
  consigne `CHECKER_PROMPT.txt` : comparer mot à mot et symbole à symbole, signaler chaque écart comme une
  modification exacte `{old, new}` du LaTeX de la page, la classer, et distinguer les erreurs de transcription des
  coquilles de l'imprimé. La consigne a été revue en boucle pendant le travail (`METHODOLOGY.md`, § 2).
- **Règles de correction :** `FIX_POLICY.md` ; questions communes à tout le document : `GLOBAL_ISSUES.md`.
- **Application :** par script ; une modification n'est appliquée que si son `old` figure une seule fois sur la page,
  sinon elle est résolue à la main (`MANUAL_*.json`). Les repères de page et la compilation sont vérifiés après chaque
  lot.
- **Coquilles de l'imprimé :** l'édition diplomatique garde la leçon imprimée ; chaque coquille est consignée dans
  `MISPRINTS.json` (page, endroit, leçon imprimée, leçon correcte). Une seconde passe (`MISPRINT_PROMPT.txt`,
  `misprint_batches/`, `MISPRINT_PASS_LOG.jsonl`) a donné à chacune sa leçon correcte dans l'édition corrigée, après
  examen des mathématiques du passage ; les 21 cas incertains sont dans `MISPRINT_KEEP.md`. Les endroits signalés par
  la traduction anglaise sont examinés dans `FRENCH_RECHECK.md`, `RECHECK_AGENT_PROMPT.txt` et
  `RECHECK_DECISIONS.json`.

## Résultat (5 novembre 2026)

- 327 lots vérifiés et appliqués (EGA 0–IV, pages liminaires et finales).
- 25 385 modifications de l'édition diplomatique, sur 1 697 pages imprimées (`FIXLOG.jsonl`) ; 24 623 modifications
  rejouées ou faites dans l'édition corrigée (`FIXLOG_CURRENT.jsonl`).
- 1 217 coquilles de l'imprimé consignées ; 245 d'entre elles demandaient une correction dans l'édition corrigée.
- Détail, incidents et corrections de méthode : `METHODOLOGY.md`.

## Où sont allées les corrections

Dans ce dépôt, `editions/2026-10-24-r20/{diplomatic,current}/packages/*/native/`, par les commits 62b2460, c05c23b,
eca7115, 87f36d9, f07f234, 85fa992, ced3e1e, 1b4682b (vérification page par page), c11c63a, 2a16c38, 2764f74 et
7c6065e (coquilles de l'imprimé dans l'édition corrigée), du 1er au 5 novembre 2026, puis dans les copies des volumes
autonomes d'EGA IV (`editions/2026-10-24-r20/standalone/*/IV*/native/`, commit du 12 novembre 2026). Les lecteurs
assemblés (`EGA_French_Cumulative_Reader.tex`, `direct/`) et les PDF de la version r20 (24 octobre 2026) ne contiennent
pas encore ces corrections.

Les corrections ont ensuite été portées dans la traduction anglaise
([ega-en](https://github.com/KokunoYumeto/ega-en)) et espagnole
([ega-fga-es](https://github.com/KokunoYumeto/ega-fga-es)) ; les registres de ces portages sont publiés dans ces
dépôts.

## Contenu

- À la racine : consignes (`*_PROMPT.txt`), méthode (`METHODOLOGY.md`, `FIX_POLICY.md`, `GLOBAL_ISSUES.md`),
  journaux des modifications (`FIXLOG*.jsonl`), coquilles (`MISPRINTS*.json`, `MISPRINT_*`), résolutions manuelles
  (`MANUAL_*.json`, `CURRENT_ITEMS_*.json`, `LEFT_DECISIONS_*.json`, `REPLAY_*.json`), file d'attente des lots
  (`QUEUE.json`), inventaires de pages (`page_inventory*.json`) et scripts (`*.py`).
- `run_*/` : un dossier par partie, avec les constats de chaque lot (`findings_*.json`) ; dans `crops_NNN_MMM/`, les
  extraits de pages et les scripts écrits par l'agent du lot. `pilot/`, `pilot2/` : le lot pilote (pp. 80–89 d'EGA I).
- `misprint_batches/` : les lots de la passe des coquilles.

Ne sont pas publiés : les numérisations, les images et découpes de pages, les PDF, les journaux de compilation et les
fichiers d'essai de compilation (`test_*`, `stub_*`), et trois copies de `preamble-base.tex` faites pour ces essais.
Les chemins locaux sont réécrits (`user`).

## Droits

Les droits sur l'œuvre originale appartiennent à son auteur ou à ses représentants ou ayants droit. Dans la mesure où
nous détenons des droits sur ces registres, la transcription, les corrections et la composition produites par IA, ils
sont dédiés au domaine public sous [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr). Cette édition
est publiée à des fins éducatives et non lucratives ; nous ne revendiquons aucun droit que nous ne détenons pas. Si
vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir une demande sur GitHub
et nous la retirerons.
