# -*- coding: utf-8 -*-
"""Deteccion de marcadores de pregunta (numeros al margen) en examenes escaneados.

Los PDF escaneados traen una capa OCR que a menudo pierde los numeros de
pregunta. Este modulo los localiza sobre el raster: en las filas del marcador,
el borde izquierdo de tinta esta desplazado a la izquierda respecto del margen
del cuerpo de texto.

API principal:
    find_markers(doc, pages, bounds) -> list[(page, col, y0, y1)]
"""
import fitz
import numpy as np

# Bounds de columna del libro 2018 (x0, x1) en puntos PDF.
BOUNDS_2018 = [(0, 236), (236, 410), (410, 700)]


def col_of(x, bounds):
    for i, (a, b) in enumerate(bounds):
        if a <= x < b:
            return i
    return len(bounds) - 1


def _left_edges(page, bounds, zoom=4, ytop=28, ybot=812, thr=175):
    """Por columna, devuelve (x0_col, [borde izquierdo de tinta por fila o None])."""
    out = {}
    for c in range(len(bounds)):
        cx0, cx1 = bounds[c]
        pm = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom),
                             clip=fitz.Rect(cx0, ytop, cx1, ybot),
                             colorspace=fitz.csGRAY)
        a = np.frombuffer(pm.samples, dtype=np.uint8).reshape(pm.height, pm.width)
        mask = a < thr
        left = []
        for r in range(mask.shape[0]):
            idx = np.argmax(mask[r])
            left.append(idx if mask[r, idx] else None)
        out[c] = (cx0, left, zoom, ytop)
    return out


def find_markers(doc, pages, bounds=BOUNDS_2018, zoom=4, ytop=28, ybot=812,
                 thr=175, gap_pt=5.0, min_h_pt=2.5):
    """Devuelve [(page, col, y0, y1)] de marcadores candidatos, ordenados."""
    out = []
    for pg in pages:
        page = doc[pg - 1]
        data = _left_edges(page, bounds, zoom=zoom, ytop=ytop, ybot=ybot, thr=thr)
        for c, (cx0, left, z, yt) in data.items():
            xs = [v for v in left if v is not None]
            if not xs:
                continue
            margin = float(np.median(xs)) / z
            # filas cuyo borde izquierdo esta a la izquierda del margen
            off = [i for i, v in enumerate(left)
                   if v is not None and (margin - v / z) >= gap_pt]
            if not off:
                continue
            # agrupar filas contiguas
            groups = []
            for i in off:
                if groups and i - groups[-1][-1] <= 3:
                    groups[-1].append(i)
                else:
                    groups.append([i])
            for g in groups:
                h = (g[-1] - g[0] + 1) / z
                if h < min_h_pt:
                    continue
                out.append((pg, c, round(yt + g[0] / z, 1), round(yt + g[-1] / z, 1)))
    out.sort()
    dedup = []
    for pg, c, y0, y1 in out:
        if dedup and dedup[-1][0] == pg and dedup[-1][1] == c and y0 - dedup[-1][2] < 4:
            continue
        dedup.append((pg, c, y0, y1))
    return dedup
