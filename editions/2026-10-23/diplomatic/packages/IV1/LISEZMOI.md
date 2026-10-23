# EGA IV, partie 1 — texte français

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
