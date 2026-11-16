# -*- coding: utf-8 -*-
"""Limpieza y parseo de texto de examen (preguntas y opciones)."""
import re

# Marcador de opción al inicio de línea: "A) ...", "a) ...", "A. ...".
OPT_RE = re.compile(r'^\s*([A-Ea-e])[\)\.]\s*(.*)$')
# Marcador de número de pregunta solo en su línea: "12." o "12".
QNUM_RE = re.compile(r'(?m)^\s*(\d{1,2})\.\s*$')


def clean(s):
    """Colapsa espacios y quita espacio antes de puntuación."""
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([,.;:!?])', r'\1', s)
    return s.strip()


def unwrap(s):
    """Une líneas partidas conservando separación de párrafos."""
    s = re.sub(r'[ \t]+\n', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = re.sub(r'(?<!\n)\n(?!\n)', ' ', s)
    return s


def parse_question(num, block, max_options=4):
    """Convierte un bloque de texto en {'id', 'stem', 'options'}."""
    lines = [l.strip() for l in block.splitlines() if l.strip()]
    stem, opts, cur = [], [], None
    for ln in lines:
        m = OPT_RE.match(ln)
        if m:
            cur = [m.group(2)]
            opts.append(cur)
        elif cur is not None:
            if len(opts) <= max_options:
                cur.append(ln)
        else:
            stem.append(ln)
    options = [clean(' '.join(o)) for o in opts][:max_options]
    while len(options) < max_options:
        options.append('')
    return {'id': num, 'stem': clean(' '.join(stem)), 'options': options}


def split_questions(text, max_options=4):
    """Divide un texto con marcadores 'N.' en una lista de preguntas."""
    parts = QNUM_RE.split(text)
    return [parse_question(int(parts[i]), parts[i + 1], max_options)
            for i in range(1, len(parts) - 1, 2)]
