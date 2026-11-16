# -*- coding: utf-8 -*-
"""Mapa de examenes y localizacion de tablas de clave en el PDF 2018."""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')
pat = re.compile(r'^\s*(\d{1,2})\s*[.)\-:]?\s*([ABCD])\s*$')

for i in range(d.page_count):
    p = d[i]
    words = p.get_text('words')
    hits = []
    for x0, y0, x1, y1, t, b, l, n in words:
        if pat.match(t.strip()):
            hits.append((x0, y0, t.strip()))
    if hits:
        xs = [h[0] for h in hits]
        ys = [h[1] for h in hits]
        print('pag %2d: %2d items  x[%.0f..%.0f] y[%.0f..%.0f]  %s' % (
            i + 1, len(hits), min(xs), max(xs), min(ys), max(ys),
            ' '.join(h[2] for h in sorted(hits, key=lambda z: (z[1], z[0])))[:160]))
