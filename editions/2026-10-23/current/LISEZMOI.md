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

Les [Notes mathématiques](https://github.com/KokunoYumeto/ega-fr/releases/download/ega-fr-2026-10-23-r15/EGA_French_Mathematical_Notes.pdf) exposent séparément les questions mathématiques et bibliographiques de l’édition corrigée. Leur LaTeX et leur projet source sont disponibles dans la même édition.
