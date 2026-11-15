"""Extrae el examen 2023 a un banco estructurado con figuras recortadas.

Mejoras frente a build_exam1.py:
  * NO descarta lineas que solo "tocan" una figura (solo las que quedan
    completamente dentro de ella), para no perder pasajes ni enunciados.
  * Recorta las figuras de cada pregunta a _static/simulacros/img/2023/.
  * Extrae las 60 claves oficiales de la ultima pagina.
"""
import fitz, re, json, os, io, sys, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PDF = r'temarios\2027\examen-1-beca-18-convocatoria-2023.pdf'
OUT_JSON = r'scratch\exams\banks\2023.json'
IMG_DIR = os.path.join('_static', 'simulacros', 'img', '2023')
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
if os.path.isdir(IMG_DIR):
    shutil.rmtree(IMG_DIR)
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(PDF)


def clusters(rects, gap=10):
    rects = [r for r in rects if 400 < r.get_area() < 45000 and r.width < 520 and r.height < 520]
    groups = []
    for r in sorted(rects, key=lambda r: (r.y0, r.x0)):
        for g in groups:
            if not (r.x0 > g.x1 + gap or r.x1 < g.x0 - gap or r.y0 > g.y1 + gap or r.y1 < g.y0 - gap):
                g.include_rect(r)
                break
        else:
            groups.append(fitz.Rect(r))
    changed = True
    while changed:
        changed = False
        for a in range(len(groups)):
            for b in range(a + 1, len(groups)):
                r1, r2 = groups[a], groups[b]
                if not (r2.x0 > r1.x1 + gap or r2.x1 < r1.x0 - gap or r2.y0 > r1.y1 + gap or r2.y1 < r1.y0 - gap):
                    r1.include_rect(r2)
                    groups.pop(b)
                    changed = True
                    break
            if changed:
                break
    return groups


def fig_rects(page):
    rects = []
    for info in page.get_image_info(xrefs=True):
        rects.append(fitz.Rect(info['bbox']))
    for d in page.get_drawings():
        rects.append(d['rect'])
    return clusters(rects)


def inside_fig(bb, figs, frac=0.75):
    """True si la linea cae mayoritariamente dentro de una figura (texto de diagrama)."""
    for f in figs:
        inter = (bb & f).get_area()
        if inter > 0 and inter / max(bb.get_area(), 1) > frac:
            return True
    return False


def page_lines(page, figs):
    out = []
    for b in page.get_text('dict')['blocks']:
        if b.get('type') != 0:
            continue
        for line in b['lines']:
            txt = ''.join(s['text'] for s in line['spans']).replace('\u00a0', ' ').strip()
            if not txt:
                continue
            bb = fitz.Rect(line['bbox'])
            if bb.y1 < 55 or bb.y0 > 800:          # encabezado / pie
                continue
            if re.fullmatch(r'\d{1,3}', txt) and bb.y0 > 780:
                continue
            if re.search(r'Examen Nacional de Preselecci|BECA 18 . Convocatoria|3iJLQD|PAGE', txt):
                continue
            if inside_fig(bb, figs):
                continue
            out.append((bb, txt))
    return out


def render_page(lines):
    parts, prev = [], None
    for bb, txt in lines:
        if prev is not None:
            parts.append('\n\n' if bb.y0 - prev > 8 else '\n')
        parts.append(txt)
        prev = bb.y1
    return ''.join(parts)


pages, figs_by_page = [], {}
for pno in range(1, doc.page_count - 1):          # sin portada ni clave
    figs = fig_rects(doc[pno])
    figs_by_page[pno + 1] = figs
    pages.append(render_page(page_lines(doc[pno], figs)))

T = '\n\n'.join(pages)


def unwrap(s):
    s = re.sub(r'[ \t]+\n', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = re.sub(r'(?<!\n)\n(?!\n)', ' ', s)
    return s


OPT_RE = re.compile(r'^\s*([A-E])\)\s*(.*)$')


def clean(s):
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    return s.strip()


def parse_question(num, block):
    lines = [l.strip() for l in block.splitlines() if l.strip()]
    stem, opts, cur = [], [], None
    for ln in lines:
        m = OPT_RE.match(ln)
        if m:
            cur = [m.group(2)]
            opts.append(cur)
        elif cur is not None:
            if len(opts) <= 4:
                cur.append(ln)
        else:
            stem.append(ln)
    options = [clean(' '.join(o)) for o in opts][:4]
    while len(options) < 4:
        options.append('')
    return {'id': num, 'stem': clean(' '.join(stem)), 'options': options}


def split_questions(text):
    parts = re.split(r'(?m)^\s*(\d{1,2})\.\s*$', text)
    return [parse_question(int(parts[i]), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


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
key_txt = doc[-1].get_text()
pairs = re.findall(r'(?m)^\s*(\d{1,2})\s*$\s*^([A-Da-d])\s*$', key_txt, re.M)
answers = {int(n): a.upper() for n, a in pairs}

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
            out = os.path.join(IMG_DIR, f"q{q['id']:02d}_f{k + 1}.png")
            clip = fitz.Rect(f.x0 - 4, f.y0 - 4, f.x1 + 4, f.y1 + 4)
            pix = doc[pno].get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip)
            pix.save(out)
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

json.dump(bank, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('-> ', OUT_JSON)
