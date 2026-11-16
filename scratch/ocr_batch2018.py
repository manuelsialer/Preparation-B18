# -*- coding: utf-8 -*-
"""OCR por lotes de varias regiones (una sola carga del modelo)."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz, numpy as np
from PIL import Image, ImageOps
from rapidocr_onnxruntime import RapidOCR

eng = RapidOCR()
d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')

REGIONS = [
    ('Q22opts', 3, 538, 200, 585, 285),
    ('Q23opts', 3, 536, 305, 580, 345),
    ('Q24opts', 3, 426, 378, 460, 425),
    ('Q28opts', 3, 536, 592, 580, 650),
    ('Q29opts', 3, 528, 700, 585, 752),
    ('Q30opts', 3, 410, 752, 585, 782),
    ('Q13', 3, 240, 340, 410, 412),
    ('Q14', 3, 240, 410, 410, 450),
    ('Q16', 3, 240, 520, 410, 570),
    ('Q17', 3, 240, 568, 410, 612),
    ('Q18', 3, 240, 612, 410, 676),
    ('Q21opts', 3, 428, 160, 520, 190),
]

for name, pg, x0, y0, x1, y1 in REGIONS:
    p = d[pg - 1]
    pm = p.get_pixmap(matrix=fitz.Matrix(6, 6), clip=fitz.Rect(x0, y0, x1, y1), colorspace=fitz.csGRAY)
    im = Image.frombytes('L', (pm.width, pm.height), pm.samples).convert('RGB')
    im = ImageOps.autocontrast(im)
    res, _ = eng(np.asarray(im))
    print('### %s' % name)
    if res:
        for box, t, s in res:
            print('   ', t)
    else:
        print('    (nada)')
