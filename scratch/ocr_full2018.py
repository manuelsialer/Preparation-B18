# -*- coding: utf-8 -*-
"""OCR de columnas completas del examen reconstruido 2018 (una carga de modelo)."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz, numpy as np
from PIL import Image, ImageOps
from rapidocr_onnxruntime import RapidOCR

eng = RapidOCR()
d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')

# (etiqueta, pagina 1-based, x0,y0,x1,y1)
REGIONS = [
    ('P3-col1', 3, 60, 40, 236, 841),
    ('P3-col2', 3, 236, 40, 410, 841),
    ('P3-col3', 3, 410, 40, 600, 841),
    ('P4-col1', 4, 55, 40, 236, 841),
    ('P4-col2', 4, 236, 40, 410, 841),
    ('P4-col3', 4, 410, 40, 600, 841),
    ('P5-col1', 5, 55, 40, 236, 841),
    ('P5-col2', 5, 236, 40, 410, 841),
    ('P5-col3', 5, 410, 40, 600, 841),
    ('P6-col1', 6, 55, 40, 236, 841),
    ('P6-col2', 6, 236, 40, 410, 841),
    ('P6-col3', 6, 410, 40, 600, 841),
    ('P7-col1', 7, 55, 40, 236, 841),
    ('P7-col2', 7, 236, 40, 410, 841),
    ('P7-col3', 7, 410, 40, 600, 841),
]

for name, pg, x0, y0, x1, y1 in REGIONS:
    p = d[pg - 1]
    pm = p.get_pixmap(matrix=fitz.Matrix(5, 5), clip=fitz.Rect(x0, y0, x1, y1), colorspace=fitz.csGRAY)
    im = Image.frombytes('L', (pm.width, pm.height), pm.samples).convert('RGB')
    im = ImageOps.autocontrast(im)
    res, _ = eng(np.asarray(im))
    print('#################### %s ####################' % name)
    if not res:
        print('  (nada)')
        continue
    rows = sorted(res, key=lambda r: (min(pt[1] for pt in r[0]), min(pt[0] for pt in r[0])))
    for box, t, s in rows:
        y = min(pt[1] for pt in box) / 5 + y0
        x = min(pt[0] for pt in box) / 5 + x0
        print('[y=%6.1f x=%6.1f] %s' % (y, x, t))
