# -*- coding: utf-8 -*-
"""Extracción de tablas de claves oficiales.

Soporta los dos formatos encontrados en los exámenes:
  * pares "N" / "A" en líneas consecutivas (exámenes 2023+);
  * grillas de varias columnas con la letra pegada al número (2018).
"""
import re

_NUM = re.compile(r'^(\d{1,2})$')
_NUML = re.compile(r'^(\d{1,2})([A-Da-d])$')
_LET = re.compile(r'^([A-Da-d])$')


def key_pairs_from_page(page, max_q=60):
    """Claves de una página con el patrón 'N' seguido de 'A' (líneas sueltas)."""
    txt = page.get_text()
    pairs = re.findall(r'(?m)^\s*(\d{1,2})\s*$\s*^([A-Da-d])\s*$', txt, re.M)
    return {int(n): a.upper() for n, a in pairs if 1 <= int(n) <= max_q}


def key_pairs_from_region(page, x0, y0, x1, y1, max_q=60, row_tol=4.0):
    """Claves de una grilla dentro de una región.

    Empareja cada número con la letra de su celda (misma fila), ya sea que
    vengan pegados ("1D") o separados ("1  D").
    """
    words = [w for w in page.get_text('words') if x0 <= w[0] < x1 and y0 <= w[1] < y1]
    toks = sorted(((w[1], w[0], w[4]) for w in words),
                  key=lambda t: (round(t[0] / row_tol), t[1]))
    pairs, pending = {}, []
    for y, _x, t in toks:
        m = _NUML.match(t)
        if m:
            n = int(m.group(1))
            if 1 <= n <= max_q:
                pairs[n] = m.group(2).upper()
            continue
        m = _NUM.match(t)
        if m:
            n = int(m.group(1))
            if 1 <= n <= max_q:
                pending.append((y, n))
            continue
        m = _LET.match(t)
        if m and pending:
            y0n, n = min(pending, key=lambda p: abs(p[0] - y))
            if abs(y0n - y) <= row_tol:
                pairs[n] = m.group(1).upper()
                pending = [p for p in pending if p[1] != n]
    return pairs


def merge_key_sources(*dicts):
    """Fusiona varias fuentes de claves (las posteriores no pisan las previas)."""
    out = {}
    for d in dicts:
        for k, v in d.items():
            out.setdefault(k, v)
    return out
