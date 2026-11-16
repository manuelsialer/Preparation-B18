# -*- coding: utf-8 -*-
"""Extrae texto por columnas (el libro Delta es escaneado a 3 columnas).
Uso: python scratch/col_2018.py <pno0> <pno1> ...   (indices 0-based)
"""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

PDF = r'temarios\2027\2018+ simulacros.pdf'
d = fitz.open(PDF)

COLS = [(60, 236), (236, 410), (410, 600)]


def col_of(x0):
    for i, (a, b) in enumerate(COLS):
        if a <= x0 < b:
            return i
    return 0 if x0 < 236 else (1 if x0 < 410 else 2)


def dump(pno):
    p = d[pno]
    blocks = [b for b in p.get_text('blocks') if b[6] == 0]
    buckets = {0: [], 1: [], 2: []}
    for b in blocks:
        x0, y0, x1, y1, txt, bno, btype = b
        if not txt.strip():
            continue
        buckets[col_of(x0)].append((y0, x0, txt.strip()))
    print('#################### PDFPAGE %d ####################' % (pno + 1))
    for c in range(3):
        print('-------- col %d --------' % (c + 1))
        for y0, x0, txt in sorted(buckets[c]):
            print('[%6.1f] %s' % (y0, txt.replace('\n', ' ')))


if __name__ == '__main__':
    for a in sys.argv[1:]:
        dump(int(a))
