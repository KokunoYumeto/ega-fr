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

Rédaction et composition produites par IA : OpenAI Codex, GPT-6 Astra, effort Ultra.
Les textes originaux sont d’Alexandre Grothendieck et Jean Dieudonné. Les droits
applicables sont précisés dans `LICENSE.txt` ; aucune approbation des auteurs,
de l’IHÉS ou de NUMDAM n’est revendiquée.

## Droits et disponibilité

Les droits sur les œuvres originales et sur toute contribution protégée à ces traductions et transcriptions dérivées restent ceux de leurs titulaires respectifs. Dans la mesure où l'éditeur détient des droits sur la traduction, la transcription, les corrections et la composition produites par IA, il les dédie au domaine public sous CC0 1.0 Universel (https://creativecommons.org/publicdomain/zero/1.0/deed.fr) ; cela n'affecte pas les droits sur les œuvres originales et n'accorde aucune autorisation de les utiliser. Les mentions de droits de tiers et les autorisations déjà accordées restent applicables.

Ces éditions sont mises à disposition gratuitement, à des fins non commerciales et exclusivement pédagogiques, dans la présomption que les titulaires de droits ne s'opposeraient pas à la libre disponibilité de ces traductions et transcriptions aux côtés des originaux français sur [NUMDAM](https://www.numdam.org/journals/PMIHES/). Cette présomption ne signifie pas qu'une autorisation a été obtenue ; le libre accès aux originaux n'autorise pas, à lui seul, leur traduction, leur adaptation ou leur republication.

Si vous détenez des droits sur un élément présenté ici et vous opposez à sa disponibilité, veuillez [ouvrir une demande sur GitHub](https://github.com/KokunoYumeto/ega-fr/issues). Le responsable de la publication retirera l'élément concerné à la demande du titulaire des droits.

La transcription moderne, les corrections, la composition et les notes mathématiques sont produites par IA. Les travaux documentés comprennent ceux d'OpenAI Codex, GPT-6 Astra, effort Ultra. Les indications de provenance des contributions antérieures restent applicables. Les textes originaux restent l'œuvre d'Alexandre Grothendieck et Jean Dieudonné ; ils ne sont pas attribués à l'IA. Cette édition n'est approuvée ni par les auteurs, ni par l'IHÉS, ni par NUMDAM.
