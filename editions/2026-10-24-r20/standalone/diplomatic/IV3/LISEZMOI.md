# EGA IV, partie 3 — texte français

Alexandre Grothendieck et Jean Dieudonné.

Les sources modulaires figurent dans `native/`, le document LaTeX assemblé dans
`direct/`. Ce composant appartient à l’édition française diplomatique.
Les références aux autres volumes utilisent le lecteur cumulatif joint.

La compilation s’effectue avec pdfLaTeX et BibTeX :

```powershell
./BUILD.ps1 -PdfLatex <pdflatex> -BibTeX <bibtex> -SourceForm native -OutputDirectory <nouveau-dossier>
```

L’option `-SourceForm direct` utilise le document assemblé. Les paquets TeX
indiqués dans les préambules doivent être installés au préalable.
Les droits et mentions de licence de l’œuvre originale restent applicables.

## Droits et disponibilité

Les droits sur les œuvres originales et sur toute contribution protégée à ces traductions et transcriptions dérivées restent ceux de leurs titulaires respectifs. Ce projet ne place pas ces œuvres ou contributions dans le domaine public et n'accorde aucune licence sur elles. Les mentions de droits de tiers et les autorisations déjà accordées restent applicables.

Ces éditions sont mises à disposition gratuitement, à des fins non commerciales et exclusivement pédagogiques, dans la présomption que les titulaires de droits ne s'opposeraient pas à la libre disponibilité de ces traductions et transcriptions aux côtés des originaux français sur [NUMDAM](https://www.numdam.org/journals/PMIHES/). Cette présomption ne signifie pas qu'une autorisation a été obtenue ; le libre accès aux originaux n'autorise pas, à lui seul, leur traduction, leur adaptation ou leur republication.

Si vous détenez des droits sur un élément présenté ici et vous opposez à sa disponibilité, veuillez [ouvrir une demande sur GitHub](https://github.com/KokunoYumeto/ega-fr/issues). Le responsable de la publication retirera l'élément concerné à la demande du titulaire des droits.

La transcription moderne, les corrections, la composition et les notes mathématiques sont produites par IA. Les travaux documentés comprennent ceux d'OpenAI Codex, GPT-6 Astra, effort Ultra. Les indications de provenance des contributions antérieures restent applicables. Les textes originaux restent l'œuvre d'Alexandre Grothendieck et Jean Dieudonné ; ils ne sont pas attribués à l'IA. Cette édition n'est approuvée ni par les auteurs, ni par l'IHÉS, ni par NUMDAM.
