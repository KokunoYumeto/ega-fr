# Éléments de géométrie algébrique — édition française corrigée

Alexandre Grothendieck et Jean Dieudonné.

Ce projet réunit les volumes I, II, III-1, III-2 et IV-1 à IV-4, avec les
préliminaires EGA 0 associés. Il contient le texte, les formules, les tableaux,
les diagrammes et les références en LaTeX éditable. Les six documents autonomes,
couverture comprise, sont réunis dans `EGA_French_Cumulative_Reader.tex` ;
`reconstruction/split_complete.py` permet de les extraire. Ce conteneur ne doit
pas être compilé comme un document LaTeX unique.

Les sources modulaires et assemblées se trouvent dans `packages/`. Les fichiers
de `reconstruction/` permettent d’assembler les PDF et leurs références internes.
Les dépendances Python figurent dans `requirements.txt`.

```powershell
./BUILD_ALL.ps1 -PdfLatex <pdflatex> -BibTeX <bibtex> -Python <python> -OutputDirectory <nouveau-dossier> -SourceForm native
```

Les droits et mentions de licence de l’œuvre originale restent applicables.
Ce projet n’accorde aucun droit supplémentaire sur cette œuvre.

Préparation des sources et assemblage : OpenAI Codex, GPT-6 Astra, effort Ultra.

[Lecteurs et sources](https://github.com/KokunoYumeto/ega-fr) ·
[Édition anglaise](https://github.com/KokunoYumeto/ega-en)

Les [Notes mathématiques](https://github.com/KokunoYumeto/ega-fr/releases/download/ega-fr-2026-10-23-r16/EGA_French_Mathematical_Notes.pdf) exposent séparément les questions mathématiques et bibliographiques de l’édition corrigée. Leur LaTeX et leur projet source sont disponibles dans la même édition.

## Droits et disponibilité

Les droits sur les œuvres originales et sur toute contribution protégée à ces traductions et transcriptions dérivées restent ceux de leurs titulaires respectifs. Tout ce sur quoi l'éditeur détient des droits dans ces éditions est dédié au domaine public sous CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/deed.fr). Les mentions de droits de tiers et les autorisations déjà accordées restent applicables.

Ces éditions sont mises à disposition gratuitement, à des fins non commerciales et exclusivement pédagogiques, dans la présomption que les titulaires de droits ne s'opposeraient pas à la libre disponibilité de ces traductions et transcriptions aux côtés des originaux français sur [NUMDAM](https://www.numdam.org/journals/PMIHES/). Cette présomption ne signifie pas qu'une autorisation a été obtenue ; le libre accès aux originaux n'autorise pas, à lui seul, leur traduction, leur adaptation ou leur republication.

Si vous détenez des droits sur un élément présenté ici et vous opposez à sa disponibilité, veuillez [ouvrir une demande sur GitHub](https://github.com/KokunoYumeto/ega-fr/issues). Le responsable de la publication retirera l'élément concerné à la demande du titulaire des droits.

La transcription moderne, les corrections, la composition et les notes mathématiques sont produites par IA. Les travaux documentés comprennent ceux d'OpenAI Codex, GPT-6 Astra, effort Ultra. Les indications de provenance des contributions antérieures restent applicables. Les textes originaux restent l'œuvre d'Alexandre Grothendieck et Jean Dieudonné ; ils ne sont pas attribués à l'IA. Cette édition n'est approuvée ni par les auteurs, ni par l'IHÉS, ni par NUMDAM.
