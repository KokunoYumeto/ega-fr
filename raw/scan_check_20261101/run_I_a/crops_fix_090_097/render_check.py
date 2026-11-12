"""Render pages of the compiled stub PDF that hold given phrases (for a visual check of the edits).
usage: python -I render_check.py PDF PHRASE [PHRASE ...]"""
import pathlib
import sys

import fitz

HERE = pathlib.Path(__file__).resolve().parent
doc = fitz.open(HERE / sys.argv[1])
for k, phrase in enumerate(sys.argv[2:]):
    for i, page in enumerate(doc):
        hits = page.search_for(phrase)
        if hits:
            r = hits[0]
            clip = fitz.Rect(page.rect.x0 + 40, max(page.rect.y0, r.y0 - 30), page.rect.x1 - 40, min(page.rect.y1, r.y1 + 150))
            pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=clip)
            out = HERE / f"render_{k}.png"
            pix.save(out)
            print(phrase, "-> pdf page", i + 1, out.name)
            break
    else:
        print(phrase, "-> not found")
