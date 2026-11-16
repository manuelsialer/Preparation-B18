# -*- coding: utf-8 -*-
"""Recortes de figuras y fórmulas a PNG."""
import os

import fitz

DEFAULT_ZOOM = 3


def render_clip(page, rect, zoom=DEFAULT_ZOOM, pad=0):
    """Pixmap de una región (con margen opcional), lista para guardar."""
    r = fitz.Rect(rect)
    if pad:
        r = fitz.Rect(r.x0 - pad, r.y0 - pad, r.x1 + pad, r.y1 + pad)
    return page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=r)


def crop_box(doc, page_no, rect, out_path, zoom=DEFAULT_ZOOM, pad=0):
    """Recorta una región (página 1-based) y la guarda en `out_path`."""
    page = doc[page_no - 1]
    pix = render_clip(page, rect, zoom=zoom, pad=pad)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    pix.save(out_path)
    return pix.width, pix.height


def crop_boxes(doc, boxes, out_dir, zoom=DEFAULT_ZOOM, pad=0, verbose=True):
    """Recorta varias regiones.

    boxes: iterable de (nombre, pagina_1based, x0, y0, x1, y1).
    Devuelve la lista de nombres creados.
    """
    os.makedirs(out_dir, exist_ok=True)
    names = []
    for name, pg, x0, y0, x1, y1 in boxes:
        path = os.path.join(out_dir, name)
        w, h = crop_box(doc, pg, (x0, y0, x1, y1), path, zoom=zoom, pad=pad)
        names.append(name)
        if verbose:
            print('crop %-14s %4dx%-4d %7d bytes' % (name, w, h, os.path.getsize(path)))
    return names
