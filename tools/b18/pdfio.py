# -*- coding: utf-8 -*-
"""Lectura de PDF: figuras, líneas de texto y extracción por columnas/regiones.

Reúne el código que estaba duplicado en los extractores de exámenes.
"""
import re

import fitz

# Límites de columna (x0) del layout a 3 columnas del PDF 2018.
BOUNDS_3COL = [(0, 236), (236, 410), (410, 700)]


def open_pdf(path):
    """Abre un PDF con PyMuPDF."""
    return fitz.open(path)


def clusters(rects, gap=10, min_area=400, max_area=45000, max_side=520):
    """Agrupa rectángulos próximos en regiones (figuras)."""
    rects = [r for r in rects
             if min_area < r.get_area() < max_area
             and r.width < max_side and r.height < max_side]
    groups = []
    for r in sorted(rects, key=lambda r: (r.y0, r.x0)):
        for g in groups:
            if not (r.x0 > g.x1 + gap or r.x1 < g.x0 - gap
                    or r.y0 > g.y1 + gap or r.y1 < g.y0 - gap):
                g.include_rect(r)
                break
        else:
            groups.append(fitz.Rect(r))
    changed = True
    while changed:
        changed = False
        for a in range(len(groups)):
            for b in range(a + 1, len(groups)):
                r1, r2 = groups[a], groups[b]
                if not (r2.x0 > r1.x1 + gap or r2.x1 < r1.x0 - gap
                        or r2.y0 > r1.y1 + gap or r2.y1 < r1.y0 - gap):
                    r1.include_rect(r2)
                    groups.pop(b)
                    changed = True
                    break
            if changed:
                break
    return groups


def fig_rects(page, **kw):
    """Regiones de figura de una página: imágenes incrustadas + dibujos."""
    rects = [fitz.Rect(info['bbox']) for info in page.get_image_info(xrefs=True)]
    rects += [d['rect'] for d in page.get_drawings()]
    return clusters(rects, **kw)


def inside_fig(bb, figs, frac=0.75):
    """True si la línea cae mayoritariamente dentro de una figura."""
    for f in figs:
        inter = (bb & f).get_area()
        if inter > 0 and inter / max(bb.get_area(), 1) > frac:
            return True
    return False


def page_lines(page, figs=None, top=55, bottom=800, skip=None):
    """Líneas de texto útiles de una página como [(rect, texto)].

    Excluye encabezado/pie, números de página y líneas dentro de figuras.
    `skip` es una lista de patrones (regex) a descartar.
    """
    figs = figs or []
    patterns = [re.compile(p) for p in (skip or [])]
    out = []
    for b in page.get_text('dict')['blocks']:
        if b.get('type') != 0:
            continue
        for line in b['lines']:
            txt = ''.join(s['text'] for s in line['spans']).replace('\u00a0', ' ').strip()
            if not txt:
                continue
            bb = fitz.Rect(line['bbox'])
            if bb.y1 < top or bb.y0 > bottom:
                continue
            if re.fullmatch(r'\d{1,3}', txt) and bb.y0 > 780:
                continue
            if any(p.search(txt) for p in patterns):
                continue
            if inside_fig(bb, figs):
                continue
            out.append((bb, txt))
    return out


def render_page(lines, gap=8):
    """Une líneas en un texto: párrafo si el salto vertical supera `gap`."""
    parts, prev = [], None
    for bb, txt in lines:
        if prev is not None:
            parts.append('\n\n' if bb.y0 - prev > gap else '\n')
        parts.append(txt)
        prev = bb.y1
    return ''.join(parts)


def col_of(x, bounds=BOUNDS_3COL):
    for i, (a, b) in enumerate(bounds):
        if a <= x < b:
            return i
    return len(bounds) - 1


def text_by_columns(page, bounds=BOUNDS_3COL, line_tol=4.0):
    """Devuelve el texto de cada columna como una lista de cadenas."""
    cols = {i: [] for i in range(len(bounds))}
    for x0, y0, x1, y1, t, *_ in page.get_text('words'):
        cols[col_of(x0, bounds)].append((y0, x0, t))
    out = []
    for i in range(len(bounds)):
        ws = sorted(cols[i], key=lambda z: (round(z[0] / 3.0), z[1]))
        lines, cur, cur_y = [], [], None
        for y0, x0, t in ws:
            if cur_y is None or abs(y0 - cur_y) <= line_tol:
                cur.append(t)
                cur_y = y0 if cur_y is None else cur_y
            else:
                lines.append(' '.join(cur))
                cur, cur_y = [t], y0
        if cur:
            lines.append(' '.join(cur))
        out.append('\n'.join(lines))
    return out


def words_in_region(page, x0, y0, x1, y1, row_tol=3.0):
    """Palabras dentro de una región, agrupadas en filas (y ascendente)."""
    ws = [w for w in page.get_text('words') if x0 <= w[0] < x1 and y0 <= w[1] < y1]
    ws.sort(key=lambda w: (round(w[1] / 2.5), w[0]))
    rows, cur, cur_y = [], [], None
    for w in ws:
        y = w[1]
        if cur_y is None or abs(y - cur_y) <= row_tol:
            cur.append((w[0], w[4]))
            cur_y = y if cur_y is None else cur_y
        else:
            rows.append((cur_y, sorted(cur)))
            cur, cur_y = [(w[0], w[4])], y
    if cur:
        rows.append((cur_y, sorted(cur)))
    return rows
