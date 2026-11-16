# -*- coding: utf-8 -*-
"""Volcado de texto por columnas de un rango de paginas del PDF.

Uso:
    python tools/exams/dump_cols.py 11 15 scratch/exams/s2_raw
"""
import os
import sys

import fitz

PDF = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'temarios', '2027', '2018+ simulacros.pdf')

COLS = [(55, 232), (232, 414), (414, 596)]


def dump(first, last, outdir):
    os.makedirs(outdir, exist_ok=True)
    doc = fitz.open(PDF)
    for pg in range(first, last + 1):
        page = doc[pg - 1]
        words = page.get_text('words')
        lines = []
        for ci, (x0, x1) in enumerate(COLS, 1):
            lines.append('##### PAG %d COL %d #####' % (pg, ci))
            sel = [w for w in words if x0 <= w[0] < x1]
            rows = {}
            for w in sel:
                rows.setdefault(round(w[1] / 3), []).append(w)
            for key in sorted(rows):
                row = sorted(rows[key], key=lambda w: w[0])
                lines.append('  ' + ' '.join(w[4] for w in row))
            lines.append('')
        path = os.path.join(outdir, 'p%d_cols.txt' % pg)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(lines))
        print('%-16s %6d B' % (os.path.basename(path), os.path.getsize(path)))
    doc.close()


if __name__ == '__main__':
    dump(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
