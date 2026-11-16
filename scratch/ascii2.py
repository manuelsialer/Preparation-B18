# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz, numpy as np

d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')
p = d[2]

def ascii_art(x0, y0, x1, y1, cols=100, mx=6, thr=225):
    pm = p.get_pixmap(matrix=fitz.Matrix(mx, mx), clip=fitz.Rect(x0, y0, x1, y1), colorspace=fitz.csGRAY)
    a = np.frombuffer(pm.samples, dtype=np.uint8).reshape(pm.height, pm.width)
    mask = (a < thr).astype(np.float32)
    H, W = mask.shape
    rows = max(1, int(round(cols * (y1 - y0) / (x1 - x0) / 2.0)))
    ch = ' .:-=+*#%@'
    print('   x0=%.0f x1=%.0f thr=%d' % (x0, x1, thr))
    for r in range(rows):
        ry0 = int(r * H / rows); ry1 = int((r + 1) * H / rows)
        line = ''
        for c in range(cols):
            cx0 = int(c * W / cols); cx1 = int((c + 1) * W / cols)
            blk = mask[ry0:ry1, cx0:cx1]
            v = blk.mean() if blk.size else 0
            line += ch[min(len(ch) - 1, int(v * len(ch) * 2.2))]
        ymid = y0 + (r + 0.5) * (y1 - y0) / rows
        print('%6.1f|%s' % (ymid, line))

for thr in (225, 245):
    print('==================== Q30 thr=%d ====================' % thr)
    ascii_art(400, 772, 600, 862, cols=100, thr=thr)
    print()
