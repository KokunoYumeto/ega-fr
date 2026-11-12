"""Render the stub_replay.pdf pages that contain given phrases to PNG files in this folder.
usage: python render_check.py PHRASE [PHRASE ...]"""
import pathlib
import sys

import pypdfium2 as pdfium

D = pathlib.Path(__file__).resolve().parent
pdf = pdfium.PdfDocument(str(D / "stub_replay.pdf"))
want = sys.argv[1:]
for i in range(len(pdf)):
    page = pdf[i]
    text = page.get_textpage().get_text_range()
    hits = [w for w in want if w in text]
    if hits:
        img = page.render(scale=2.2).to_pil()
        out = D / f"render_p{i + 1}.png"
        img.save(out)
        print(i + 1, hits, out)
