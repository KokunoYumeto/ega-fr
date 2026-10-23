# Éléments de géométrie algébrique — Notes mathématiques

Quarante-neuf notes, réparties entre les volumes I à IV, précisent les hypothèses,
les démonstrations et les références de l’édition française corrigée. Les errata
publiés par les auteurs sont identifiés avec leurs sources. Ce texte est séparé
du témoin diplomatique et des lecteurs cumulatifs.

`native/main.tex` est le document modulaire ; le document autonome se trouve dans
`direct/`. Les deux formes contiennent le même texte et les mêmes formules.

```powershell
./BUILD.ps1 -PdfLatex <pdflatex> -BibTeX <bibtex> -SourceForm native -OutputDirectory <nouveau-dossier>
```

Remplacer `native` par `direct` pour compiler le document autonome. Les paquets
LaTeX standard cités dans le préambule doivent être installés.

Rédaction et composition assistées par OpenAI Codex, GPT-6 Astra, effort Ultra.
Les textes originaux sont d’Alexandre Grothendieck et Jean Dieudonné. Les droits
applicables sont précisés dans `LICENSE.txt` ; aucune approbation des auteurs,
de l’IHÉS ou de NUMDAM n’est revendiquée.
