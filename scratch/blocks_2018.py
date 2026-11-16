# -*- coding: utf-8 -*-
"""Vuelca los bloques (texto e imagen) con bbox de las paginas del examen
reconstruido 2018 para localizar figuras y limpiar el texto."""
import io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

PDF = r'temarios\2027\2018+ simulacros.pdf'
OUT = os.path.join(os.path.dirname(__file__), 'img2018')
os.makedirs(OUT, exist_ok=True)

d = fitz.open(PDF)
for pno in (2, 3, 4, 5):   # 0-based -> paginas 3..6 (examen reconstruido)
    p = d[pno]
    print('#################### PAGE %d (rect %s)' % (pno + 1, p.rect))
    blocks = p.get_text('blocks')  # x0,y0,x1,y1,text,block_no,block_type
    for b in sorted(blocks, key=lambda b: (round(b[1], 1), b[0])):
        x0, y0, x1, y1, txt, bno, btype = b
        kind = 'IMG' if btype == 1 else 'txt'
        t = txt.strip().replace('\n', ' / ')
        print('  %s [%6.1f %6.1f %6.1f %6.1f] %s' % (kind, x0, y0, x1, y1, t[:80]))
