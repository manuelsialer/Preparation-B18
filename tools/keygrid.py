# -*- coding: utf-8 -*-
"""Extrae una tabla de claves (grilla) de una region, agrupando por filas."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

PDF = r'temarios\2027\2018+ simulacros.pdf'
d = fitz.open(PDF)

def dump(pg, x0, y0, x1, y1):
    p = d[pg - 1]
    ws = [w for w in p.get_text('words') if x0 <= w[0] < x1 and y0 <= w[1] < y1]
    ws.sort(key=lambda w: (round(w[1] / 2.5), w[0]))
    print('==== pag %d region x[%.0f..%.0f] y[%.0f..%.0f] (%d palabras) ====' % (
        pg, x0, x1, y0, y1, len(ws)))
    cur_y = None
    line = []
    for w in ws:
        y = w[1]
        if cur_y is None or abs(y - cur_y) <= 3.0:
            line.append((w[0], w[4]))
            if cur_y is None:
                cur_y = y
        else:
            print('  y=%6.1f | %s' % (cur_y, '  '.join('%s@%.0f' % (t, x) for x, t in sorted(line))))
            line = [(w[0], w[4])]
            cur_y = y
    if line:
        print('  y=%6.1f | %s' % (cur_y, '  '.join('%s@%.0f' % (t, x) for x, t in sorted(line))))

if __name__ == '__main__':
    a = sys.argv[1:]
    if a:
        dump(int(a[0]), float(a[1]), float(a[2]), float(a[3]), float(a[4]))
    else:
        dump(19, 236, 570, 415, 700)
