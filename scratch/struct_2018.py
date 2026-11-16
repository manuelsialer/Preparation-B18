# -*- coding: utf-8 -*-
"""Vuelca el texto completo de las paginas clave del PDF 2018 (contenido + inicios)."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')
for i in [2, 7, 8, 11, 12, 15, 16, 19, 20]:
    p = d[i]
    print('==================== PDF pag %d ====================' % (i + 1))
    txt = p.get_text('text')
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    for l in lines[:45]:
        print('  ', l[:110])
    print()
