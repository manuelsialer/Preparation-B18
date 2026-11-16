# -*- coding: utf-8 -*-
"""Render ASCII de los PNG generados para verificarlos sin ver la imagen."""
import io, sys, os, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import numpy as np
from PIL import Image

def art(fp, cols=100):
    im = Image.open(fp).convert('L')
    a = np.asarray(im)
    mask = (a < 190).astype(np.float32)
    H, W = mask.shape
    rows = max(1, int(round(cols * H / W / 2.0)))
    ch = ' .:-=+*#%@'
    print('#### %s (%dx%d) ####' % (os.path.basename(fp), W, H))
    for r in range(rows):
        ry0 = int(r * H / rows); ry1 = int((r + 1) * H / rows)
        line = ''
        for c in range(cols):
            cx0 = int(c * W / cols); cx1 = int((c + 1) * W / cols)
            blk = mask[ry0:ry1, cx0:cx1]
            v = blk.mean() if blk.size else 0
            line += ch[min(len(ch) - 1, int(v * len(ch) * 2.4))]
        print(line)
    print()

for name in sys.argv[1:] or ['q10a', 'q10b', 'q21', 'q22', 'q23', 'q24', 'q28', 'q29', 'q30',
                             'q07_o', 'q12_f', 'q13_f', 'q15_f', 'q18_f', 'q20_f', 'q22_o', 'q29_o']:
    fp = r'_static\simulacros\img\2018\%s.png' % name
    if os.path.exists(fp):
        art(fp, cols=90)
