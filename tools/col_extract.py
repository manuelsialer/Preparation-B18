# -*- coding: utf-8 -*-
"""Extrae texto por columnas de paginas dadas (layout 3 columnas del PDF 2018)."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

PDF = r'temarios\2027\2018+ simulacros.pdf'
d = fitz.open(PDF)

# Limites de columna (x0). Ajustados al layout del libro.
BOUNDS = [(0, 236), (236, 410), (410, 700)]

def col_of(x):
    for i, (a, b) in enumerate(BOUNDS):
        if a <= x < b:
            return i
    return len(BOUNDS) - 1

def extract(page_idx):
    p = d[page_idx]
    words = p.get_text('words')
    cols = {i: [] for i in range(len(BOUNDS))}
    for x0, y0, x1, y1, t, b, l, n in words:
        cols[col_of(x0)].append((y0, x0, t))
    out = []
    for i in range(len(BOUNDS)):
        ws = sorted(cols[i], key=lambda z: (round(z[0] / 3.0), z[1]))
        # agrupar en lineas por y
        lines = []
        cur_y = None
        cur = []
        for y0, x0, t in ws:
            if cur_y is None or abs(y0 - cur_y) <= 4:
                cur.append(t)
                if cur_y is None:
                    cur_y = y0
            else:
                lines.append(' '.join(cur))
                cur = [t]
                cur_y = y0
        if cur:
            lines.append(' '.join(cur))
        out.append('\n'.join(lines))
    return out

if __name__ == '__main__':
    pages = [int(a) for a in sys.argv[1:]] or [8, 9, 10, 11]
    for pg in pages:
        print('########################## PDF pag %d ##########################' % pg)
        for ci, txt in enumerate(extract(pg - 1)):
            print('---------- columna %d ----------' % (ci + 1))
            print(txt)
        print()
