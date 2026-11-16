"""Extrae el examen 2023 a un banco estructurado con figuras recortadas.

Mejoras frente a build_exam1.py:
  * NO descarta lineas que solo "tocan" una figura (solo las que quedan
    completamente dentro de ella), para no perder pasajes ni enunciados.
  * Recorta las figuras de cada pregunta a _static/simulacros/img/2023/.
  * Extrae las 60 claves oficiales de la ultima pagina.
"""
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fitz  # noqa: E402
from b18 import bank as b18bank, console, crop as b18crop  # noqa: E402
from b18 import keys as b18keys, pdfio, textutil  # noqa: E402

console.setup_console()

PDF = r'temarios\2027\examen-1-beca-18-convocatoria-2023.pdf'
OUT_JSON = r'scratch\exams\banks\2023.json'
IMG_DIR = os.path.join('_static', 'simulacros', 'img', '2023')
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
if os.path.isdir(IMG_DIR):
    shutil.rmtree(IMG_DIR)
os.makedirs(IMG_DIR, exist_ok=True)

doc = pdfio.open_pdf(PDF)

# Encabezado/pie del examen a descartar en la extracción de líneas.
SKIP = [r'Examen Nacional de Preselecci', r'BECA 18 . Convocatoria', r'3iJLQD', r'PAGE']


pages, figs_by_page = [], {}
for pno in range(1, doc.page_count - 1):          # sin portada ni clave
    figs = pdfio.fig_rects(doc[pno])
    figs_by_page[pno + 1] = figs
    pages.append(pdfio.render_page(pdfio.page_lines(doc[pno], figs, skip=SKIP)))

T = '\n\n'.join(pages)


unwrap = textutil.unwrap
clean = textutil.clean
split_questions = textutil.split_questions


i_rm = T.find('RAZONAMIENTO MATEMÁTICO')
i_rv = T.find('RAZONAMIENTO VERBAL')
math_qs = split_questions(T[i_rm:i_rv])

verb = T[i_rv:]
chunks = re.split(r'(?mi)^\s*TEXTO\s*(\d+)\s*$', verb)
passages, verb_qs = {}, []
for k in range(1, len(chunks) - 1, 2):
    pnum, body = int(chunks[k]), chunks[k + 1]
    m = re.search(r'(?m)^\s*(3[1-9]|[45]\d|60)\.\s*$', body)
    ptxt, qtxt = (body[:m.start()], body[m.start():]) if m else ('', body)
    ptxt = unwrap(ptxt)
    if ptxt.strip():
        passages[pnum] = re.sub(r'\n{3,}', '\n\n', ptxt).strip()
    for q in split_questions(qtxt):
        q['passage'] = pnum
        verb_qs.append(q)

# ---- claves oficiales (60) ----
answers = b18keys.key_pairs_from_page(doc[-1], max_q=60)

# ---- deduplicar y, solo si falta, reinsertar la 38 ----
RAW = open('scratch/exams/examen1.txt', encoding='utf-8').read()
_allq = math_qs + verb_qs
seen, allq = set(), []
for q in _allq:
    if q['id'] in seen:
        print('!! duplicada', q['id'], '- se descarta')
        continue
    seen.add(q['id'])
    allq.append(q)

if 38 not in seen:
    print('!! 38 ausente, se re-inserta')
    m38 = re.search(r'(?ms)^\s*38\.\s*\n(.*?)\n\s*A\)', RAW)
    q38_stem = clean(unwrap(m38.group(1))) if m38 else ''
    idx37 = next(i for i, q in enumerate(allq) if q['id'] == 37)
    allq.insert(idx37 + 1, {'id': 38, 'stem': q38_stem, 'passage': 3, 'options': [
        'tendrá que inscribirse a cursos para el desarrollo de habilidades extrovertidas.',
        'buscará ofertas de empleo acordes con sus rasgos psicológicos y físicos.',
        'deberá desarrollar características que no forman parte de su personalidad.',
        'podrá solicitar al empleador la oportunidad de trabajar de manera solitaria.']})

for q in allq:
    q['answer'] = answers.get(q['id'], '')
    q['section'] = 'matematica' if q['id'] <= 30 else 'lectura'

# ---- recorte de figuras por pregunta ----
# posicion de cada pregunta (pagina + y) para asociar figuras
qpos = {}
for pno in range(1, doc.page_count - 1):
    page = doc[pno]
    figs = figs_by_page[pno + 1]
    for b in page.get_text('dict')['blocks']:
        if b.get('type') != 0:
            continue
        for line in b['lines']:
            txt = ''.join(s['text'] for s in line['spans']).strip()
            m = re.fullmatch(r'(\d{1,2})\.', txt)
            if m:
                n = int(m.group(1))
                if 1 <= n <= 60 and n not in qpos:
                    qpos[n] = (pno, fitz.Rect(line['bbox']).y0, figs)

n_img = 0
for i, q in enumerate(allq):
    if q['id'] not in qpos:
        continue
    pno, y0, figs = qpos[q['id']]
    nxt = qpos.get(allq[i + 1]['id']) if i + 1 < len(allq) else None
    y1 = nxt[1] if (nxt and nxt[0] == pno) else 10000
    imgs = []
    for k, f in enumerate(figs):
        if y0 - 5 <= f.y0 and f.y1 <= y1 + 5:
            out = os.path.join(IMG_DIR, "q%02d_f%d.png" % (q['id'], k + 1))
            clip = (f.x0 - 4, f.y0 - 4, f.x1 + 4, f.y1 + 4)
            b18crop.crop_box(doc, pno + 1, clip, out, zoom=3)
            imgs.append(os.path.basename(out))
            n_img += 1
    if imgs:
        q['images'] = imgs

bank = {
    'year': 2023,
    'title': 'Simulacro Oficial ENP Beca 18 — Convocatoria 2023',
    'duration_min': 120,
    'sections': [
        {'id': 'matematica', 'label': 'Razonamiento Matemático', 'from': 1, 'to': 30},
        {'id': 'lectura', 'label': 'Razonamiento Verbal', 'from': 31, 'to': 60},
    ],
    'passages': [{'id': k, 'title': None, 'html': passages[k]} for k in sorted(passages)],
    'questions': allq,
}

bad = [(q['id'], [j for j, o in enumerate(q['options']) if not o]) for q in allq if '' in q['options'] or not q['stem']]
print('preguntas:', len(allq), '| claves:', len(answers), '| pasajes:', len(passages), '| figuras:', n_img)
print('stem vacio u opciones vacias:', bad)
print('sin clave:', [q['id'] for q in allq if not q['answer']])
print('ids:', sorted(q['id'] for q in allq))

b18bank.write_bank(bank, OUT_JSON)
print(b18bank.qa_report(bank))
print('-> ', OUT_JSON)
