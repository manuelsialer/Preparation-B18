# -*- coding: utf-8 -*-
"""Esquema, construcción, escritura y validación de bancos de simulacros.

Esquema JSON de un banco:
    {
      "year": int,
      "title": str,
      "duration_min": int,
      "sections": [{"id", "label", "from", "to"}],
      "passages": [{"id": int, "title": str|null, "html": str}],
      "questions": [{
          "id": int, "stem": str, "options": [str, str, str, str],
          "answer": "A".."D", "section": str,
          "passage": int|omitido,        # 1-based en bank["passages"]
          "images": [str, ...]|omitido,  # figuras tras el enunciado
          "explain": str|omitido         # explicación opcional
      }]
    }
"""
import json
import os

LETTERS = ('A', 'B', 'C', 'D')

SECTIONS_DEFAULT = [
    {'id': 'matematica', 'label': 'Razonamiento Matemático', 'from': 1, 'to': 30},
    {'id': 'lectura', 'label': 'Razonamiento Verbal', 'from': 31, 'to': 60},
]


def section_of(sections, qid):
    for s in sections:
        if s['from'] <= qid <= s['to']:
            return s
    return sections[0] if sections else None


def make_bank(year, title, questions, passages=None, sections=None,
              duration_min=120, extra=None):
    """Construye el dict del banco y asigna la sección a cada pregunta."""
    sections = sections or [dict(s) for s in SECTIONS_DEFAULT]
    for q in questions:
        sec = section_of(sections, q['id'])
        if sec:
            q['section'] = sec['id']
    bank = {
        'year': year,
        'title': title,
        'duration_min': duration_min,
        'sections': sections,
        'passages': passages or [],
        'questions': questions,
    }
    if extra:
        bank.update(extra)
    return bank


def write_bank(bank, path, indent=1):
    """Escribe el banco como JSON UTF-8 (no-ASCII sin escapar)."""
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(bank, fh, ensure_ascii=False, indent=indent)
    return path


def load_bank(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def validate_bank(bank, expected=60, expect_options=4):
    """Devuelve una lista de problemas (vacía = banco válido)."""
    issues = []
    qs = bank.get('questions', [])
    if len(qs) != expected:
        issues.append('se esperaban %d preguntas, hay %d' % (expected, len(qs)))

    ids = [q.get('id') for q in qs]
    if sorted(ids) != list(range(1, expected + 1)):
        missing = sorted(set(range(1, expected + 1)) - set(ids))
        dup = sorted({i for i in ids if ids.count(i) > 1})
        issues.append('ids incompletos (faltan %s, duplicados %s)' % (missing, dup))

    n_pass = len(bank.get('passages', []))
    for q in qs:
        qid = q.get('id')
        if not (q.get('stem') or '').strip():
            issues.append('pregunta %s: enunciado vacío' % qid)
        opts = q.get('options') or []
        if len(opts) != expect_options:
            issues.append('pregunta %s: %d opciones (se esperan %d)'
                          % (qid, len(opts), expect_options))
        # Las opciones pueden estar vacías si vienen dentro de una figura
        # (recorte del examen); solo es un problema sin figuras o si faltan
        # unas y otras no.
        has_img = bool(q.get('images'))
        empty = [j for j, o in enumerate(opts) if not (o or '').strip()]
        if empty and (not has_img or len(empty) != len(opts)):
            for j in empty:
                issues.append('pregunta %s: opción %s vacía'
                              % (qid, LETTERS[j] if j < 4 else j))
        if q.get('answer') not in LETTERS:
            issues.append('pregunta %s: clave inválida %r' % (qid, q.get('answer')))
        if q.get('passage') is not None and not (1 <= q['passage'] <= n_pass):
            issues.append('pregunta %s: pasaje %r fuera de rango (hay %d)'
                          % (qid, q['passage'], n_pass))

    # cobertura de secciones
    covered = set()
    for s in bank.get('sections', []):
        covered |= set(range(s['from'], s['to'] + 1))
    if covered and covered != set(range(1, expected + 1)):
        issues.append('las secciones no cubren 1..%d' % expected)

    return issues


def qa_report(bank, expected=60):
    """Resumen legible del banco (para imprimir en consola)."""
    qs = bank.get('questions', [])
    with_img = sum(1 for q in qs if q.get('images'))
    with_pass = sum(1 for q in qs if q.get('passage'))
    lines = [
        'año: %s | título: %s' % (bank.get('year'), bank.get('title')),
        'preguntas: %d | con figuras: %d | con pasaje: %d | pasajes: %d'
        % (len(qs), with_img, with_pass, len(bank.get('passages', []))),
    ]
    issues = validate_bank(bank, expected=expected)
    if issues:
        lines.append('PROBLEMAS (%d):' % len(issues))
        lines += ['  - ' + i for i in issues]
    else:
        lines.append('OK: banco válido')
    return '\n'.join(lines)
