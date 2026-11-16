# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz, numpy as np
from PIL import Image, ImageOps
from rapidocr_onnxruntime import RapidOCR

d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')
eng = RapidOCR()

REG = [
    ('Q12-expr',    3, 236, 255, 412, 300, 8),
    ('Q12-cond',    3, 236, 288, 412, 320, 8),
    ('Q13-eq',      3, 236, 344, 412, 384, 8),
    ('Q24-fig',     3, 448, 370, 560, 446, 8),
    ('Q10-c1bot',   3,  62, 684, 236, 782, 6),
    ('Q10-c2top',   3, 238,  36, 412, 134, 6),
]
for name, pg, x0, y0, x1, y1, mx in REG:
    p = d[pg - 1]
    pm = p.get_pixmap(matrix=fitz.Matrix(mx, mx), clip=fitz.Rect(x0, y0, x1, y1), colorspace=fitz.csGRAY)
    im = Image.frombytes('L', (pm.width, pm.height), pm.samples).convert('RGB')
    im = ImageOps.autocontrast(im)
    res, _ = eng(np.asarray(im))
    print('#### %s (%dx%d) ####' % (name, pm.width, pm.height))
    if not res:
        print('   (nada)'); continue
    rows = sorted(res, key=lambda r: (min(p[1] for p in r[0]), min(p[0] for p in r[0])))
    for box, t, s in rows:
        y = min(p[1] for p in box) / mx + y0
        x = min(p[0] for p in box) / mx + x0
        print('  [y=%6.1f x=%6.1f] %s' % (y, x, t))
