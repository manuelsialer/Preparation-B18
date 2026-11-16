# -*- coding: utf-8 -*-
"""Recorta las figuras del examen reconstruido 2018 (pagina 3 del PDF Delta)
y las guarda en _static/simulacros/img/2018/."""
import io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

PDF = r'temarios\2027\2018+ simulacros.pdf'
OUT = r'_static\simulacros\img\2018'
os.makedirs(OUT, exist_ok=True)
d = fitz.open(PDF)

# (nombre, pagina 1-based, x0,y0,x1,y1)
BOXES = [
    ('q10.png', 3, 238, 44, 408, 131),
    ('q21.png', 3, 428, 83, 546, 167),
    ('q22.png', 3, 418, 203, 540, 286),
    ('q23.png', 3, 440, 297, 512, 348),
    ('q24.png', 3, 458, 380, 548, 452),
    ('q28.png', 3, 428, 588, 537, 656),
    ('q29.png', 3, 424, 692, 530, 748),
    ('q30.png', 3, 410, 795, 575, 841),
]

for name, pg, x0, y0, x1, y1 in BOXES:
    p = d[pg - 1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pm = p.get_pixmap(matrix=fitz.Matrix(4, 4), clip=clip)
    path = os.path.join(OUT, name)
    pm.save(path)
    print('%-10s %dx%d  %d bytes' % (name, pm.width, pm.height, os.path.getsize(path)))
