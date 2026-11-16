# -*- coding: utf-8 -*-
"""Detecta figuras (blobs de tinta que no son texto) en una pagina escaneada.
Uso: python scratch/figdetect.py <pagina_1based> [min_area]
"""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz, numpy as np
from PIL import Image
from scipy import ndimage

PDF = r'temarios\2027\2018+ simulacros.pdf'
ZOOM = 4.0
d = fitz.open(PDF)


def detect(pno, min_area=600):
    p = d[pno]
    pm = p.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), colorspace=fitz.csGRAY)
    im = Image.frombytes('L', (pm.width, pm.height), pm.samples)
    a = np.asarray(im).astype(np.uint8)
    ink = a < 128
    # quitar texto: usar bboxes de bloques de texto (type 0)
    textmask = np.zeros_like(ink)
    for b in p.get_text('blocks'):
        if b[6] != 0:
            continue
        x0, y0, x1, y1 = b[:4]
        X0, Y0 = int(x0 * ZOOM), int(y0 * ZOOM)
        X1, Y1 = int(x1 * ZOOM), int(y1 * ZOOM)
        textmask[max(0, Y0):Y1, max(0, X0):X1] = True
    textmask = ndimage.binary_dilation(textmask, iterations=6)
    fig = ink & ~textmask
    # quitar estructuras muy finas (bordes de pagina, separadores)
    lbl, n = ndimage.label(fig)
    print('componentes:', n)
    objs = ndimage.find_objects(lbl)
    res = []
    for i, sl in enumerate(objs):
        if sl is None:
            continue
        ys, xs = sl
        area = int((lbl[sl] == (i + 1)).sum())
        if area < min_area:
            continue
        x0, y0 = xs.start / ZOOM, ys.start / ZOOM
        x1, y1 = xs.stop / ZOOM, ys.stop / ZOOM
        res.append((area, x0, y0, x1, y1))
    res.sort(reverse=True)
    for area, x0, y0, x1, y1 in res[:60]:
        print('area=%-7d bbox=[%6.1f %6.1f %6.1f %6.1f]  w=%5.1f h=%5.1f' %
              (area, x0, y0, x1, y1, x1 - x0, y1 - y0))


def detect2(pno, xmin=0, ymin=0, xmax=600, ymax=850, minw=8, minh=8, min_area=100):
    p = d[pno]
    pm = p.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), colorspace=fitz.csGRAY)
    im = Image.frombytes('L', (pm.width, pm.height), pm.samples)
    a = np.asarray(im).astype(np.uint8)
    ink = a < 128
    textmask = np.zeros_like(ink)
    for b in p.get_text('blocks'):
        if b[6] != 0:
            continue
        x0, y0, x1, y1 = b[:4]
        textmask[int(y0 * ZOOM):int(y1 * ZOOM), int(x0 * ZOOM):int(x1 * ZOOM)] = True
    textmask = ndimage.binary_dilation(textmask, iterations=6)
    fig = ink & ~textmask
    lbl, n = ndimage.label(fig)
    objs = ndimage.find_objects(lbl)
    res = []
    for i, sl in enumerate(objs):
        if sl is None:
            continue
        ys, xs = sl
        x0, y0 = xs.start / ZOOM, ys.start / ZOOM
        x1, y1 = xs.stop / ZOOM, ys.stop / ZOOM
        if not (xmin <= x0 and ymin <= y0 and x1 <= xmax and y1 <= ymax):
            continue
        if (x1 - x0) < minw or (y1 - y0) < minh:
            continue
        area = int((lbl[sl] == (i + 1)).sum())
        if area < min_area:
            continue
        res.append((y0, x0, x1, y1, area))
    res.sort()
    print('### p%d region x[%g,%g] y[%g,%g] -> %d blobs' % (pno + 1, xmin, xmax, ymin, ymax, len(res)))
    for y0, x0, x1, y1, area in res:
        print('  bbox=[%6.1f %6.1f %6.1f %6.1f] w=%5.1f h=%5.1f area=%d' %
              (x0, y0, x1, y1, x1 - x0, y1 - y0, area))


if __name__ == '__main__':
    if len(sys.argv) > 5:
        detect2(int(sys.argv[1]) - 1, *map(float, sys.argv[2:6]),
                minw=float(sys.argv[6]) if len(sys.argv) > 6 else 8,
                minh=float(sys.argv[7]) if len(sys.argv) > 7 else 8,
                min_area=int(sys.argv[8]) if len(sys.argv) > 8 else 100)
    else:
        pno = int(sys.argv[1]) - 1
        ma = int(sys.argv[2]) if len(sys.argv) > 2 else 600
        detect(pno, ma)
