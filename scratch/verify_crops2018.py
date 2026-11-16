# -*- coding: utf-8 -*-
"""Verifica por OCR los recortes generados en _static/simulacros/img/2018."""
import io, sys, os, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

eng = RapidOCR()
files = sorted(glob.glob(r'_static\simulacros\img\2018\*.png'))
for fp in files:
    im = Image.open(fp).convert('RGB')
    # upscale small crops
    if im.width < 500:
        f = 500.0 / im.width
        im = im.resize((int(im.width * f), int(im.height * f)))
    res, _ = eng(np.asarray(im))
    print('#### %s (%dx%d) ####' % (os.path.basename(fp), im.width, im.height))
    if not res:
        print('   (nada)')
        continue
    rows = sorted(res, key=lambda r: (min(p[1] for p in r[0]), min(p[0] for p in r[0])))
    for box, t, s in rows:
        print('   ', t)
