# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz, numpy as np
from PIL import Image

d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')
p = d[2]

print('==== words col3 y 575..775 ====')
for x0, y0, x1, y1, t, b, l, n in sorted(p.get_text('words'), key=lambda w: (round(w[1]), w[0])):
    if x0 > 405 and 575 < y0 < 775:
        print('  x0=%6.1f y0=%6.1f x1=%6.1f y1=%6.1f  %s' % (x0, y0, x1, y1, t))

print()
print('==== q30.png con umbral bajo ====')
im = Image.open(r'_static\simulacros\img\2018\q30.png').convert('L')
a = np.asarray(im)
for thr in (200, 235):
    mask = (a < thr).astype(np.float32)
    H, W = mask.shape
    cols = 100
    rows = max(1, int(round(cols * H / W / 2.0)))
    ch = ' .:-=+*#%@'
    print('---- thr=%d ----' % thr)
    for r in range(rows):
        ry0 = int(r * H / rows); ry1 = int((r + 1) * H / rows)
        line = ''
        for c in range(cols):
            cx0 = int(c * W / cols); cx1 = int((c + 1) * W / cols)
            blk = mask[ry0:ry1, cx0:cx1]
            v = blk.mean() if blk.size else 0
            line += ch[min(len(ch) - 1, int(v * len(ch) * 2.6))]
        print(line)
