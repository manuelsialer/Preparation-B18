# -*- coding: utf-8 -*-
"""Vuelca paginas de transicion/solucionario del PDF 2018."""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

d = fitz.open(r'temarios\2027\2018+ simulacros.pdf')

def dump(i, n=70):
    print('==================== PDF pag %d ====================' % (i + 1))
    t = d[i].get_text('text')
    lines = [l.rstrip() for l in t.splitlines() if l.strip()]
    for l in lines[:n]:
        print('  ', l[:120])
    print()

for i in [5, 6, 9, 10, 13, 14, 17, 18, 21]:
    dump(i)

# Buscar patrones de clave: numero seguido de letra
print('==== PATRONES CLAVE (num + letra) ====')
pat = re.compile(r'^\s*(\d{1,2})\s*[.)\-:]?\s*([ABCD])\s*$')
for i in range(d.page_count):
    for line in d[i].get_text('text').splitlines():
        if pat.match(line.strip()):
            print('  pag %2d: %s' % (i + 1, line.strip()))
