"""Extrae el examen 2024 a scratch/exams/banks/2024.json (formato hibrido).

Pipeline:
  1. Decodifica CambriaMath: rev-cmap de Cambria Math + mapa manual por GID.
  2. Clasifica las figuras de cada pagina: pistas ("Recuerda que"), diagramas
     raster, tablas (cabecera con >=2 lineas -> se extiende a las filas) y
     cajas de numero del margen izquierdo.
  3. Corta el documento en regiones de pasaje ("Lee ...") y segmentos de
     pregunta (marcadores 1..60) por posicion (pno, y), sin depender de x.
  4. Agrupa chars en clusters visuales (solape vertical o barra de fraccion)
     y reconstruye el texto: super/indices en Unicode; fracciones, sistemas y
     construcciones apiladas como recortes [[img:...]].
  5. Claves oficiales de la ultima pagina.
  6. Recorta figuras y recortes de formula a _static/simulacros/img/2024/.
"""
import fitz, re, json, os, io, sys, shutil, statistics
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fontTools.ttLib import TTCollection

PDF = r'temarios\2027\examen-2-beca-18-convocatoria-2024.pdf'
OUT_JSON = r'scratch\exams\banks\2024.json'
IMG_DIR = os.path.join('_static', 'simulacros', 'img', '2024')
ZOOM = 3
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
if os.path.isdir(IMG_DIR):
    shutil.rmtree(IMG_DIR)
os.makedirs(IMG_DIR, exist_ok=True)

# ============================================================ mapa CambriaMath
f = TTCollection(r'C:\Windows\Fonts\cambria.ttc').fonts[1]
go = f.getGlyphOrder()
rev = {}
for u, g in f.getBestCmap().items():
    rev.setdefault(g, u)

# =========================================================== mapa Calibri-Light
# (subsets con ToUnicode roto en algunas paginas: se decodifica por GID)
from fontTools.ttLib import TTFont
fcl = TTFont(r'C:\Windows\Fonts\calibril.ttf')
gocl = fcl.getGlyphOrder()
revcl = {}
for u, g in fcl.getBestCmap().items():
    revcl.setdefault(g, u)

MANUAL = {2868 + i: d for i, d in enumerate('0123456789')}   # 2868..2877 = 0..9
MANUAL.update({2879: '−',      # signo menos
               3051: '𝑥',      # x italic
               3420: '{', 3428: '[', 3432: ']'})

CTRL = re.compile(r'[\x00-\x08\x0b-\x1f\x7f]')


def gid2ch(gid):
    if gid in MANUAL:
        return MANUAL[gid]
    if 0 <= gid < len(go):
        u = rev.get(go[gid])
        if u:
            return chr(u)
    return None


def cal2ch(gid):
    if 0 <= gid < len(gocl):
        u = revcl.get(gocl[gid])
        if u:
            return chr(u)
    return None


def math_gid_map(page):
    """{(ox, oy): gid} de los chars CambriaMath y Calibri-Light (texttrace)."""
    m = {}
    dup = 0
    for sp in page.get_texttrace():
        if 'Cambria' not in sp['font'] and 'Calibri-Light' not in sp['font']:
            continue
        for c in sp['chars']:
            # c = (ucs, gid, origin, bbox)
            ox, oy = c[2]
            k = (round(ox, 1), round(oy, 1))
            if k in m:
                dup += 1
            else:
                m[k] = c[1]
    if dup:
        print('  [aviso] origins duplicados en pagina:', dup)
    return m


def decode_span(span, gmap):
    """Texto de un span; CambriaMath y Calibri-Light usan el mapa de GIDs."""
    font = span.get('font', '')
    is_math = 'CambriaMath' in font or 'Cambria Math' in font
    is_light = 'Calibri-Light' in font
    out = []
    for ch in span.get('chars', []):
        c = ch['c']
        if is_math:
            ox, oy = ch['origin']
            gid = gmap.get((round(ox, 1), round(oy, 1)))
            m = gid2ch(gid) if gid is not None else None
            if m is None:
                m = c if not c.strip() else '?'
            if m == '\x03':
                m = ' '
            out.append(m)
        elif is_light:
            ox, oy = ch['origin']
            gid = gmap.get((round(ox, 1), round(oy, 1)))
            m = cal2ch(gid) if gid is not None else None
            if m is None:
                m = c          # ej. espacios sin contraparte en texttrace
            if m == '\x03':
                m = ' '
            out.append(m)
        else:
            out.append(c)
    t = ''.join(out)
    t = CTRL.sub('', t)
    return t


# ============================================================ carga de paginas
doc = fitz.open(PDF)
pages = []          # lista de listas de lineas: {pno,y0,x0,x1,text,spans}
all_figs = {}       # pno -> lista de figuras clasificadas
marks = []          # (pno, y, numero) de los marcadores 1..60
lee_marks = []      # (pno, y) de los "Lee ..." de pasaje

LEE_RE = re.compile(r'^\s*(Lee (el|los) siguiente|Responde las siguientes)')
NUM_RE = re.compile(r'^\d{1,2}$')


def clusters(rects, gap=10):
    groups = []
    for r in sorted(rects, key=lambda r: (round(r.y0, 1), r.x0)):
        for g in groups:
            if not (r.x0 > g.x1 + gap or r.x1 < g.x0 + gap or
                    r.y0 > g.y1 + gap or r.y1 < g.y0 + gap):
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
                if not (r2.x0 > r1.x1 + gap or r2.x1 < r1.x0 + gap or
                        r2.y0 > r1.y1 + gap or r2.y1 < r1.y0 + gap):
                    r1.include_rect(r2)
                    groups.pop(b)
                    changed = True
                    break
            if changed:
                break
    return groups


def extend_table(fig, page, lines):
    """Encadena a la cabecera de tabla las filas que siguen debajo."""
    cur = fitz.Rect(fig)
    while True:
        nxt = None
        for ln in lines:
            if ln['x0'] < 140:
                continue
            if cur.y1 - 2 <= ln['y0'] <= cur.y1 + 6 and ln['x1'] > cur.x0:
                if nxt is None or ln['y0'] < nxt['y0']:
                    nxt = ln
        if nxt is None:
            break
        cur.include_rect(fitz.Rect(nxt['x0'], nxt['y0'], nxt['x1'], nxt['y1']))
        lines.remove(nxt)
    return cur


for pno in range(doc.page_count):
    page = doc[pno]
    raw = page.get_text('rawdict')
    gmap = math_gid_map(page)
    lines = []
    for b in raw['blocks']:
        if b.get('type') != 0:
            continue
        for ln in b['lines']:
            spans = []
            chars = []
            text = ''
            for s in ln['spans']:
                t = decode_span(s, gmap)
                spans.append({'text': t, 'font': s.get('font', ''),
                              'bbox': s['bbox']})
                # chars decodificados con geometria (para clusters visuales)
                math = 'CambriaMath' in s.get('font', '') or \
                    'Cambria Math' in s.get('font', '')
                light = 'Calibri-Light' in s.get('font', '')
                for ch in s.get('chars', []):
                    c = ch['c']
                    if math:
                        ox, oy = ch['origin']
                        gid = gmap.get((round(ox, 1), round(oy, 1)))
                        m = gid2ch(gid) if gid is not None else None
                        if m is None:
                            m = c if not c.strip() else '?'
                        if m == '\x03':
                            m = ' '
                        c = m
                    elif light:
                        ox, oy = ch['origin']
                        gid = gmap.get((round(ox, 1), round(oy, 1)))
                        m = cal2ch(gid) if gid is not None else None
                        if m is None:
                            m = c
                        if m == '\x03':
                            m = ' '
                        c = m
                    if CTRL.match(c):
                        continue
                    chars.append({'c': c, 'bbox': ch['bbox'],
                                  'oy': ch['origin'][1],
                                  'ox': ch['origin'][0],
                                  'math': math})
                    text += c
                text += ''
            if not text.strip():
                continue
            bb = ln['bbox']
            lines.append({'pno': pno, 'y0': bb[1], 'x0': bb[0], 'x1': bb[2],
                          'y1': bb[3], 'text': text, 'spans': spans,
                          'chars': chars})
    pages.append(lines)

    # ---- figuras (imagenes + dibujos) por pagina ----
    all_info = page.get_image_info(xrefs=True)
    rects = [fitz.Rect(i['bbox']) for i in all_info]
    is_img = {tuple(round(v, 1) for v in i['bbox']) for i in all_info}
    # dibujos con curvas = rectangulos redondeados (cajas de cita/aviso)
    curved = [d['rect'] for d in page.get_drawings()
              if any(it[0] == 'c' for it in d['items'])]
    rects += [d['rect'] for d in page.get_drawings()]
    # excluye lineas decorativas y fondos completos ANTES de agrupar;
    # los rasters grandes (graficas de media pagina, infografias) se conservan
    rects = [r for r in rects
             if (400 < r.get_area() < 60000 and r.width < 520 and r.height < 520)
             or (200 <= r.width <= 540 and 150 <= r.height <= 700)]
    figs = []
    for g in clusters(rects):
        big = 200 <= g.width <= 540 and 150 <= g.height <= 700
        if not big and not (400 < g.get_area() < 60000 and
                            g.width < 520 and g.height < 520):
            continue
        clip_txt = page.get_text(clip=g)
        n_text = sum(1 for ln in lines
                     if ln['y0'] >= g.y0 - 2 and ln['y1'] <= g.y1 + 2
                     and ln['x0'] >= g.x0 - 2 and ln['x1'] <= g.x1 + 2)
        raster = any(
            i['bbox'][0] >= g.x0 - 1 and i['bbox'][2] <= g.x1 + 1 and
            i['bbox'][1] >= g.y0 - 1 and i['bbox'][3] <= g.y1 + 1
            for i in all_info)
        big_img = any(
            i['bbox'][0] >= g.x0 - 1 and i['bbox'][2] <= g.x1 + 1 and
            i['bbox'][1] >= g.y0 - 1 and i['bbox'][3] <= g.y1 + 1 and
            (i['bbox'][2] - i['bbox'][0]) >= 60 and
            (i['bbox'][3] - i['bbox'][1]) >= 40
            for i in all_info)
        if 'Recuerda que' in clip_txt or 'Considera' in clip_txt:
            kind = 'hint'
        elif raster and big_img:
            kind = 'image'           # diagrama con etiquetas (texto interno)
        elif raster and n_text >= 1:
            kind = 'textbg'          # caja de numero / fondo: conservar texto
        elif raster and g.x1 >= 100:
            kind = 'image'           # diagrama raster puro (Q24)
        elif raster:
            kind = 'number'          # caja de numero del margen
        elif n_text >= 2 and g.x1 >= 100:
            if any(r.intersects(g) for r in curved):
                kind = 'quote'       # caja de cita: el texto queda en el body
            else:
                kind = 'table'
        elif n_text == 0 and g.x1 >= 100:
            kind = 'image'
        else:
            kind = 'number'
        figs.append({'rect': g, 'kind': kind, 'n_text': n_text,
                     'raster': raster})
    # extiende tablas a sus filas
    for fg in figs:
        if fg['kind'] == 'table':
            fg['rect'] = extend_table(fg['rect'], page, list(lines))
    all_figs[pno] = figs

    # ---- marcadores de pregunta y de pasaje ----
    for ln in lines:
        if ln['x1'] < 95 and NUM_RE.match(ln['text'].strip()):
            marks.append((pno, ln['y0'], int(ln['text'].strip())))
        elif LEE_RE.match(ln['text'].strip()):
            lee_marks.append((pno, ln['y0'], ln['text'].strip()))

print('marcadores:', len(marks), 'lee:', len(lee_marks))
print('marcadores orden:', [m[2] for m in sorted(marks, key=lambda t: t[:2])])

# ====================================================== corte global (pno, y)
marks_s = sorted(marks, key=lambda t: (t[0], t[1]))
lee_s = sorted(lee_marks, key=lambda t: (t[0], t[1]))

# lineas que pertenecen a una figura (caja de numero, raster, tabla, pista)
fig_lines = set()
for pno, figs in all_figs.items():
    for fg in figs:
        if fg['kind'] in ('number', 'textbg'):
            r = fg['rect']
            for ln in pages[pno]:
                if (ln['y0'] >= r.y0 - 3 and ln['y1'] <= r.y1 + 3 and
                        ln['x0'] >= r.x0 - 3 and ln['x1'] <= r.x1 + 3):
                    fig_lines.add(id(ln))
        elif fg['kind'] in ('hint', 'table', 'image'):
            r = fg['rect']
            for ln in pages[pno]:
                cx = (ln['x0'] + ln['x1']) / 2
                cy = (ln['y0'] + ln['y1']) / 2
                if r.x0 - 2 <= cx <= r.x1 + 2 and r.y0 - 2 <= cy <= r.y1 + 2:
                    fig_lines.add(id(ln))

# lineas de pregunta: todas salvo numericas de margen y "Lee/Responde"
def is_body(ln):
    t = ln['text'].strip()
    if ln['y0'] < 60 or ln['y0'] > 780:
        return False
    if ln['pno'] == doc.page_count - 1:          # pagina de claves
        return False
    if LEE_RE.match(t):
        return False
    if id(ln) in fig_lines:
        return False
    if ln['x1'] < 95 and NUM_RE.match(t):
        return False
    return True

# regiones de pasaje: entre un "Lee (el|los) siguiente" y el "Responde" siguiente
passage_regions = []   # (lee_pno, lee_y, resp_pno, resp_y)
for i, (pno, y, txt) in enumerate(lee_s):
    if txt.startswith('Responde'):
        continue
    # buscar el "Responde" mas cercano despues
    for (p2, y2, t2) in lee_s[i + 1:]:
        if t2.startswith('Responde') and (p2, y2) > (pno, y):
            passage_regions.append((pno, y, p2, y2))
            break

print('regiones pasaje:', [(a + 1, round(b, 1), c + 1, round(d, 1))
                           for a, b, c, d in passage_regions])


def in_passage(pno, y):
    for (lp, ly, rp, ry) in passage_regions:
        if (pno, y) > (lp, ly) and (pno, y) <= (rp, ry):
            return True
    return False


# segmentos: de cada marcador al siguiente (o al "Lee" / fin)
bounds = []   # (pno, y, etiqueta) ordenado globalmente
for (pno, y, n) in marks_s:
    bounds.append((pno, y, ('q', n)))
for (pno, y, txt) in lee_s:
    if txt.startswith('Lee'):
        bounds.append((pno, y, ('lee', None)))
bounds.sort(key=lambda t: (t[0], t[1]))

segments = []   # (numero, [lineas])
cur_no = None
cur = []
for (pno, y, tag) in bounds:
    if tag[0] == 'q':
        if cur_no is not None:
            segments.append((cur_no, cur))
        cur_no = tag[1]
        cur = []
    # lineas de esta pagina entre y anterior y este y
    # (se llenan despues; aqui solo guardamos los cortes)

# reconstruccion efectiva: asignar cada linea de cuerpo al ultimo corte <= ella
cuts = [(pno, y, tag) for (pno, y, tag) in bounds]
segments = {n: [] for (_, _, tag) in cuts if tag[0] == 'q'}
lee_lines = {i: [] for i in range(len(passage_regions))}
cur_tag = None
lee_only = [(pno, y, ri) for ri, (pno, y, t) in enumerate(
    [x for x in lee_s if x[2].startswith('Lee')])]
resp_only = [(pno, y, ri) for ri, (pno, y, t) in enumerate(
    [x for x in lee_s if x[2].startswith('Responde')])]
all_events = sorted([(pno, y, ('q', n)) for (pno, y, n) in marks_s] +
                    [(pno, y, ('lee', ri)) for (pno, y, ri) in lee_only] +
                    [(pno, y, ('resp', ri)) for (pno, y, ri) in resp_only],
                    key=lambda t: (t[0], t[1]))

# recorremos lineas de cuerpo en orden global y las asignamos al evento anterior
body = []
for pno, lines in enumerate(pages):
    for ln in lines:
        if is_body(ln):
            body.append(ln)
body.sort(key=lambda ln: (ln['pno'], round(ln['y0'], 1), ln['x0']))

ev_i = -1
cur_q = None
cur_region = None
assign = {}   # id(ln) -> ('q', n) | ('lee', i)
for ln in body:
    key = (ln['pno'], ln['y0'])
    while ev_i + 1 < len(all_events) and (
            all_events[ev_i + 1][0], all_events[ev_i + 1][1]) <= (
            key[0], key[1] + 4.5):
        ev_i += 1
        if all_events[ev_i][2][0] == 'q':
            cur_q = all_events[ev_i][2][1]
            cur_region = None
        elif all_events[ev_i][2][0] == 'lee':
            cur_q = None
            cur_region = all_events[ev_i][2][1]
        else:                      # "Responde ...": cierra el pasaje
            cur_q = None
            cur_region = None
    if cur_q is not None:
        assign[id(ln)] = ('q', cur_q)
    elif cur_region is not None:
        assign[id(ln)] = ('lee', cur_region)

n_q_lines = {n: 0 for n in range(1, 61)}
n_lee_lines = {i: 0 for i in range(len(passage_regions))}
orphan = 0
for ln in body:
    a = assign.get(id(ln))
    if a is None:
        orphan += 1
        continue
    if a[0] == 'q':
        n_q_lines[a[1]] += 1
    else:
        n_lee_lines[a[1]] += 1
print('lineas sin asignar:', orphan)
print('q con <2 lineas:', {n: c for n, c in n_q_lines.items() if c < 2})
print('regiones con 0 lineas:', {i: c for i, c in n_lee_lines.items() if c < 2})

# ================================================================ n u c l e o
# barras de fraccion (drawings finos horizontales); se excluyen los vinculos
# de raiz (el trazo superior del simbolo √, alineado con su extremo izquierdo)
bars = {}
for pno in range(doc.page_count):
    bs = []
    sq_bx1 = [c['bbox'][2] for ln in pages[pno]
              for c in ln['chars'] if c['c'] == '√']
    for d in doc[pno].get_drawings():
        r = d['rect']
        if 4 <= r.width <= 60 and r.height <= 2 and 60 < r.y0 < 780:
            if any(abs(x - r.x0) < 2.5 for x in sq_bx1):
                continue          # vinculo de raiz, no es fraccion
            bs.append((r.x0, r.y0, r.x1, r.y1))
    bars[pno] = bs

# ---------------------------------------------------- super/subindices unicode
SUP = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶',
       '7': '⁷', '8': '⁸', '9': '⁹', '+': '⁺', '−': '⁻', '-': '⁻', '=': '⁼',
       '(': '⁽', ')': '⁾', 'x': 'ˣ', 'n': 'ⁿ', 'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ',
       'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
       'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'o': 'ᵒ', 'p': 'ᵖ', 'r': 'ʳ', 's': 'ˢ',
       't': 'ᵗ', 'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'y': 'ʸ', 'z': 'ᶻ',
       '𝑎': 'ᵃ', '𝑏': 'ᵇ', '𝑐': 'ᶜ', '𝑑': 'ᵈ', '𝑒': 'ᵉ', '𝑓': 'ᶠ', '𝑔': 'ᵍ',
       'ℎ': 'ʰ', '𝑖': 'ⁱ', '𝑗': 'ʲ', '𝑘': 'ᵏ', '𝑙': 'ˡ', '𝑚': 'ᵐ', '𝑛': 'ⁿ',
       '𝑜': 'ᵒ', '𝑝': 'ᵖ', '𝑟': 'ʳ', '𝑠': 'ˢ', '𝑡': 'ᵗ', '𝑢': 'ᵘ', '𝑣': 'ᵛ',
       '𝑤': 'ʷ', '𝑥': 'ˣ', '𝑦': 'ʸ', '𝑧': 'ᶻ'}
SUB = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆',
       '7': '₇', '8': '₈', '9': '₉', '+': '₊', '−': '₋', '-': '₋', '=': '₌',
       '(': '₍', ')': '₎', 'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ',
       'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ', 'p': 'ₚ', 'r': 'ᵣ',
       's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ', 'v': 'ᵥ', 'x': 'ₓ',
       '𝑎': 'ₐ', '𝑒': 'ₑ', 'ℎ': 'ₕ', '𝑖': 'ᵢ', '𝑗': 'ⱼ', '𝑘': 'ₖ', '𝑙': 'ₗ',
       '𝑚': 'ₘ', '𝑛': 'ₙ', '𝑜': 'ₒ', '𝑝': 'ₚ', '𝑟': 'ᵣ', '𝑠': 'ₛ', '𝑡': 'ₜ',
       '𝑢': 'ᵤ', '𝑣': 'ᵥ', '𝑥': 'ₓ'}


# ------------------------------------------------------------------ render
def render_text(chars):
    return ''.join(c['c'] for c in sorted(chars, key=lambda c: c['ox']))


def clean(s):
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r' +([,.;:!?])', r'\1', s)
    return s.strip()


def make_bands(chars):
    chars = sorted(chars, key=lambda c: (round(c['oy'], 1), c['ox']))
    bands = []
    for c in chars:
        if bands and c['oy'] - bands[-1]['max'] <= 3:
            bands[-1]['chars'].append(c)
            if c['oy'] > bands[-1]['max']:
                bands[-1]['max'] = c['oy']
        else:
            bands.append({'chars': [c], 'max': c['oy']})
    for b in bands:
        solid = [c for c in b['chars'] if c['c'].strip()]
        b['oy'] = statistics.median([c['oy'] for c in solid]) if solid \
            else b['chars'][0]['oy']
        b['x0'] = min(c['bbox'][0] for c in b['chars'])
        b['x1'] = max(c['bbox'][2] for c in b['chars'])
    return bands


def find_labels(band):
    chs = sorted(band['chars'], key=lambda c: c['ox'])
    out = []
    for a, b2 in zip(chs, chs[1:]):
        if (a['c'] in 'ABCD' and b2['c'] == ')' and not a['math']
                and not b2['math']
                and a['bbox'][3] - a['bbox'][1] > 10
                and b2['bbox'][0] - a['bbox'][2] < 3):
            out.append({'letter': a['c'], 'x0': a['bbox'][0],
                        'x1': b2['bbox'][2]})
    return out


def bar_between(pno, y0, y1, x0, x1):
    """True si hay una barra de fraccion con y0 en [y0,y1] y x solapando."""
    for (bx0, by0, bx1, by1) in bars.get(pno, []):
        if y0 <= by0 <= y1 and bx1 > x0 and bx0 < x1:
            return True
    return False


def bar_between_text(pno, y0, y1, x0, x1, ctx):
    """Barra de fraccion REAL: exige chars arriba y abajo de la barra
    (las barras huerfanas sin texto no son fracciones)."""
    for (bx0, by0, bx1, by1) in bars.get(pno, []):
        if not (y0 <= by0 <= y1 and bx1 > x0 and bx0 < x1):
            continue
        above = any(c['bbox'][2] > bx0 - 2 and c['bbox'][0] < bx1 + 2 and
                    by0 - 12 <= c['oy'] < by0 for c in ctx)
        below = any(c['bbox'][2] > bx0 - 2 and c['bbox'][0] < bx1 + 2 and
                    by0 < c['oy'] <= by0 + 12 for c in ctx)
        if above and below:
            return True
    return False


def xover(band, o):
    return min(band['x1'], o['x1']) - max(band['x0'], o['x0'])


def pick_opt(row, band):
    best, bo = None, -1e9
    for o in row['opts']:
        v = xover(band, o)
        if v > bo:
            bo, best = v, o
    return best


# ----------------------------------------- reconstruccion por (pregunta, pag)
qinfo = {n: {'stem': [], 'opts': {}, 'rows': [], 'mcount': 0, 'fimgs': []}
         for n in range(1, 61)}
owner_state = {n: None for n in range(1, 61)}   # None (stem) o ('opt', letra)

q_lines = {}
for ln in body:
    a = assign.get(id(ln))
    if a is not None and a[0] == 'q':
        q_lines.setdefault((a[1], ln['pno']), []).append(ln)

for (n, pno) in sorted(q_lines):
    info = qinfo[n]
    chars = [c for ln in q_lines[(n, pno)] for c in ln['chars']]
    bands = make_bands(chars)
    for b in bands:
        b['pno'] = pno
        b['labels'] = find_labels(b)
    # --- filas de opciones
    rows = []
    page_events = []      # (oy, owner) para el owner_state de fin de pagina
    for b in bands:
        if not b['labels']:
            continue
        lbs = sorted(b['labels'], key=lambda l: l['x0'])
        opts = []
        for k, lb in enumerate(lbs):
            ox0 = lb['x1'] - 0.5
            ox1 = lbs[k + 1]['x0'] - 2 if k + 1 < len(lbs) else 545.0
            o = {'letter': lb['letter'], 'x0': ox0, 'x1': ox1, 'pno': pno,
                 'row_oy': b['oy'], 'grid': len(lbs) >= 2,
                 'base': [c for c in b['chars']
                          if ox0 <= c['bbox'][0] < ox1],
                 'num': [], 'den': [], 'cont': [], 'imgs': [],
                 'constructo': False}
            if bar_between_text(pno, b['oy'] - 12, b['oy'] + 2, ox0, ox1,
                                chars):
                o['constructo'] = True
            opts.append(o)
        rows.append({'oy': b['oy'], 'pno': pno, 'opts': opts,
                     'grid': len(lbs) >= 2})
    for row in rows:
        info['rows'].append(row)
        for o in row['opts']:
            info['opts'].setdefault(o['letter'], o)
        page_events.append((b['oy'], ('opt', row['opts'][-1]['letter'])))
    # --- paso A: bandas apiladas de constructos (num arriba, den abajo)
    consumed = set()
    for b in bands:
        if b['labels']:
            continue
        cands = []
        for row in rows:
            for o in row['opts']:
                d = abs(b['oy'] - row['oy'])
                if d > 12 or xover(b, o) <= 0:
                    continue
                if b['oy'] < row['oy']:
                    # numerador: exige barra REAL entre la banda y la fila
                    if not o['num'] and bar_between_text(
                            pno, b['oy'], row['oy'], o['x0'], o['x1'], chars):
                        cands.append((d, 'num', o))
                else:
                    if o['constructo'] and not o['den']:
                        cands.append((d, 'den', o))
        if cands:
            cands.sort(key=lambda t: (t[1], t[0]))
            d, rol, o = cands[0]
            o[rol].append(b)
            consumed.add(id(b))
            page_events.append((b['oy'], ('opt', o['letter'])))
    # --- paso B: bandas posicionales (stem / continuaciones)
    owner = owner_state[n]      # continuidad de la pagina anterior
    for b in bands:
        if b['labels'] or id(b) in consumed:
            continue
        target = None
        if rows:
            first, last = rows[0], rows[-1]
            if b['oy'] < first['oy'] - 1e-9:
                if first['oy'] - b['oy'] <= 12:
                    target = pick_opt(first, b)
                elif owner is not None and owner[0] == 'opt':
                    target = info['opts'][owner[1]]
            elif b['oy'] > last['oy'] + 1e-9:
                target = pick_opt(last, b)
            else:
                nxt = next((r for r in rows if r['oy'] > b['oy'] + 1e-9), None)
                if nxt is not None and nxt['oy'] - b['oy'] <= 12:
                    target = pick_opt(nxt, b)
                else:
                    prevr = [r for r in rows if r['oy'] < b['oy'] - 1e-9]
                    target = pick_opt(prevr[-1], b) if prevr else pick_opt(last, b)
        elif owner is not None and owner[0] == 'opt':
            target = info['opts'][owner[1]]
        if target is not None:
            target['cont'].append(b)
            owner = ('opt', target['letter'])
        else:
            info['stem'].append((pno, b))
            owner = None
        page_events.append((b['oy'], owner))
    owner_state[n] = max(page_events, key=lambda t: t[0])[1] \
        if page_events else owner


# -------------------------------------------------------------- recortes
def crop_chars(pno, chars, name):
    x0 = min(c['bbox'][0] for c in chars)
    y0 = min(c['bbox'][1] for c in chars)
    x1 = max(c['bbox'][2] for c in chars)
    y1 = max(c['bbox'][3] for c in chars)
    clip = fitz.Rect(x0 - 3, y0 - 3, x1 + 3, y1 + 3) & doc[pno].rect
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
    pix.save(os.path.join(IMG_DIR, name))
    return '[[img:%s]]' % name


def crop_fig(pno, rect, name):
    clip = fitz.Rect(rect.x0 - 4, rect.y0 - 4, rect.x1 + 4, rect.y1 + 4) & doc[pno].rect
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
    pix.save(os.path.join(IMG_DIR, name))


def chain_bands(band_list):
    chains = []
    for b in band_list:
        if chains and b['oy'] - chains[-1][-1]['oy'] <= 12:
            chains[-1].append(b)
        else:
            chains.append([b])
    return chains


def render_chain(pno, qid, chain):
    def nsolid(b):
        return len([c for c in b['chars'] if c['c'].strip()])

    if len(chain) == 1:
        return clean(render_text(chain[0]['chars']))
    fulls = [b for b in chain if nsolid(b) >= 8]
    if not fulls:
        # cadena de fragmentos: probar mapeo super/sub; si algo no mapea,
        # crop de toda la cadena (stack de formula)
        base = max(chain, key=nsolid)
        t = render_base(pno, qid, base,
                        [b for b in chain if b is not base], whole=True)
        if t is not None:
            return t
        info = qinfo[qid]
        info['mcount'] += 1
        name = 'q%02d_m%d.png' % (qid, info['mcount'])
        return crop_chars(pno, [c for b in chain for c in b['chars']], name)
    if len(fulls) == 1:
        base = fulls[0] if fulls else max(chain, key=nsolid)
        return render_base(pno, qid, base,
                           [b for b in chain if b is not base])
    # varias lineas completas en la cadena (ej. dos renglones con sus
    # superindices): cada satelite va a la linea completa mas cercana
    sats = [b for b in chain if b not in fulls]
    fulls.sort(key=lambda b: b['oy'])
    parts = []
    for base in fulls:
        mine = [b for b in sats
                if min(fulls, key=lambda f: abs(f['oy'] - b['oy'])) is base]
        t = render_base(pno, qid, base, mine)
        if t:
            parts.append(t)
    return ' '.join(parts)


def render_base(pno, qid, base, sats, whole=False):
    """Renderiza una banda base con sus bandas satelite (super/subindices
    Unicode si es posible). Con whole=True devuelve None si algo no mapea
    (el llamador cropea la cadena completa)."""
    solid = [c for c in base['chars'] if c['c'].strip()]
    base_med = statistics.median([c['oy'] for c in solid]) if solid \
        else base['oy']
    merged = list(base['chars'])
    bad = []
    for b in sats:
        for c in b['chars']:
            if not c['c'].strip():
                continue
            dy = c['oy'] - base_med
            mp = SUP if dy < 0 else SUB
            if 3.5 < abs(dy) <= 5.2 and c['c'] in mp:
                merged.append(dict(c, c=mp[c['c']]))
            else:
                bad.append(c)
    if not bad:
        return clean(render_text(merged))
    if whole:
        return None
    # crop por clusters: cada zona no mapeable (fraccion, sistema) genera un
    # crop propio; el texto de la base entre clusters queda seleccionable
    info = qinfo[qid]
    bad_sorted = sorted(bad, key=lambda c: c['ox'])
    clusters = []
    for c in bad_sorted:
        if clusters and c['ox'] - clusters[-1]['x1'] < 18:
            clusters[-1]['chars'].append(c)
            clusters[-1]['x1'] = max(clusters[-1]['x1'], c['bbox'][2])
        else:
            clusters.append({'chars': [c], 'x0': c['ox'],
                             'x1': c['bbox'][2]})
    keep = list(merged)          # texto conservado (base + sup/sub mapeados)
    tokens = []
    for cl in clusters:
        cx0, cx1 = cl['x0'] - 2, cl['x1'] + 2
        anch = [c for c in keep
                if c['bbox'][2] > cx0 and c['bbox'][0] < cx1]
        cropc = list(cl['chars']) + anch
        cx0 = min([c['ox'] for c in cropc]) - 2
        cx1 = max([c['bbox'][2] for c in cropc]) + 2
        info['mcount'] += 1
        name = 'q%02d_m%d.png' % (qid, info['mcount'])
        tokens.append((cx0, cx1, crop_chars(pno, cropc, name)))
        keep = [c for c in keep
                if not (c['bbox'][2] > cx0 and c['bbox'][0] < cx1)]
    parts_txt = []
    for (tx0, tx1, tok) in sorted(tokens, key=lambda t: t[0]):
        pre = [c for c in keep if c['bbox'][2] <= tx0 + 2]
        keep = [c for c in keep if c['bbox'][2] > tx0 + 2]
        t_pre = clean(render_text(pre))
        if t_pre:
            parts_txt.append(t_pre)
        parts_txt.append(tok)
    t_rest = clean(render_text(keep))
    if t_rest:
        parts_txt.append(t_rest)
    return ' '.join(parts_txt)


# ------------------------------------- render de stems y opciones por pregunta
stems = {}
options = {}
for n in range(1, 61):
    info = qinfo[n]
    # stem: bandas por pagina -> cadenas
    by_page = {}
    for pno, b in info['stem']:
        by_page.setdefault(pno, []).append(b)
    parts = []
    for pno in sorted(by_page):
        for chain in chain_bands(by_page[pno]):
            t = render_chain(pno, n, chain)
            if t:
                parts.append(t)
    stems[n] = ' '.join(parts)


# opciones: se renderizan DESPUES del attach inline de figuras (ver mas abajo)

def region_at(pno, y):
    for ri, (lp, ly, rp, ry) in enumerate(passage_regions):
        if (pno, y) > (lp, ly) and (pno, y) <= (rp, ry):
            return ri
    return None


pfigs = {}
qfigs = {n: [] for n in range(1, 61)}
fcount_p = {}
orphan_figs = 0
for pno in sorted(all_figs):
    if pno >= doc.page_count - 1:      # portada/portada y pagina de claves
        continue
    for fg in sorted(all_figs[pno], key=lambda f: f['rect'].y0):
        if fg['kind'] in ('number', 'textbg', 'quote'):
            continue
        r = fg['rect']
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        ri = region_at(pno, cy)
        if ri is not None:
            fcount_p[ri] = fcount_p.get(ri, 0) + 1
            name = 'p%d_f%d.png' % (ri + 1, fcount_p[ri])
            crop_fig(pno, r, name)
            pfigs.setdefault(ri, []).append({'pno': pno, 'cy': cy,
                                            'name': name})
            continue
        own = None
        for (mp, my, mn) in marks_s:
            if (mp, my) <= (pno, cy + 3):
                own = mn
            else:
                break
        if own is None:
            orphan_figs += 1
            print('[fig sin dueno] p%d %s [%6.1f %6.1f %6.1f %6.1f]'
                  % (pno + 1, fg['kind'], r.x0, r.y0, r.x1, r.y1))
            continue
        qfigs[own].append({'pno': pno, 'cy': cy, 'cx': cx, 'rect': r,
                           'name': 'q%02d_f%d.png' % (own, len(qfigs[own]))})
        crop_fig(pno, r, qfigs[own][-1]['name'])

# attach inline en filas grid (2+ columnas), resto -> q.images
for n in range(1, 61):
    info = qinfo[n]
    rows_by_page = {}
    for row in info['rows']:
        rows_by_page.setdefault(row['pno'], []).append(row)
    for f in qfigs[n]:
        rows_pg = sorted(rows_by_page.get(f['pno'], []), key=lambda r: r['oy'])
        attached = False
        if any(r['grid'] for r in rows_pg):
            for row in rows_pg:
                if not row['grid']:
                    continue
                nxt = next((r2['oy'] for r2 in rows_pg
                            if r2['oy'] > row['oy'] + 1e-9), 1e9)
                if row['oy'] - 15 <= f['cy'] < nxt - 15:
                    best, bo = None, -1e9
                    for o in row['opts']:
                        if o['x0'] <= f['cx'] <= o['x1']:
                            ov = 1e6        # punto dentro de la columna
                        else:
                            ov = min(f['cx'], o['x1']) - max(f['cx'], o['x0'])
                        if ov > bo:
                            bo, best = ov, o
                    if best is not None and bo > 0:
                        best['imgs'].append(f['name'])
                        attached = True
                    break
        if not attached:
            info['fimgs'].append(f['name'])


# ------------------------------------------- render de opciones por pregunta
options = {}
for n in range(1, 61):
    info = qinfo[n]
    options[n] = {}
    for letter in 'ABCD':
        o = info['opts'].get(letter)
        if o is None:
            options[n][letter] = ''
            continue
        oparts = []
        if o['constructo'] or o['num'] or o['den']:
            allc = list(o['base'])
            for b in o['num'] + o['den']:
                allc += b['chars']
            if allc:
                info['mcount'] += 1
                oparts.append(crop_chars(
                    o['pno'], allc, 'q%02d_m%d.png' % (n, info['mcount'])))
            # la base ya esta en el crop: solo las continuaciones van a texto
            items = [{'pno': b['pno'], 'oy': b['oy'], 'chars': b['chars']}
                     for b in o['cont']]
        else:
            items = [{'pno': o['pno'], 'oy': o['row_oy'], 'chars': o['base']}] + \
                [{'pno': b['pno'], 'oy': b['oy'], 'chars': b['chars']}
                 for b in o['cont']]
        # agrupar por pagina (las continuaciones pueden cruzar de pagina)
        items.sort(key=lambda x: (x['pno'], x['oy']))
        groups = []
        for it in items:
            if groups and groups[-1][0] == it['pno']:
                groups[-1][1].append(it)
            else:
                groups.append((it['pno'], [it]))
        for pno2, grp in groups:
            for chain in chain_bands(grp):
                t = render_chain(pno2, n, chain)
                if t:
                    oparts.append(t)
        txt = ' '.join(p for p in oparts if p)
        if o['imgs']:
            txt = (txt + ' ' + ' '.join('[[img:%s]]' % i for i in o['imgs'])).strip()
        options[n][letter] = txt


# ------------------------------------------------------------------ pasajes
passage_items = {ri: [] for ri in range(len(passage_regions))}
for ln in body:
    a = assign.get(id(ln))
    if a is not None and a[0] == 'lee':
        passage_items[a[1]].append((ln['pno'], ln['y0'], 0, 'line', ln))
for ri, fl in pfigs.items():
    for f in fl:
        passage_items[ri].append((f['pno'], f['cy'], 1, 'fig',
                                  '[[img:%s]]' % f['name']))
passage_html = {}
for ri in range(len(passage_regions)):
    items = sorted(passage_items[ri], key=lambda t: (t[0], t[1], t[2]))
    parts = []
    for it in items:
        if it[3] == 'fig':
            parts.append(it[4])
        else:
            t = clean(render_text(it[4]['chars']))
            if t:
                parts.append(t)
    passage_html[ri] = '\n\n'.join(parts)


# ------------------------------------------------------------------- claves
ktxt = doc[doc.page_count - 1].get_text()
pairs = re.findall(r'(?m)^\s*(\d{1,2})\s*\n\s*([A-Da-d])\s*$', ktxt)
answers = {}
for num, le in pairs:
    answers[int(num)] = le.upper()
print('claves:', len(answers))


# ----------------------------------------------------- pasaje de cada preg.
passage_of = {}
last_resp = None
for (pno, y, tag) in sorted(all_events, key=lambda t: (t[0], t[1])):
    if tag[0] == 'resp':
        last_resp = tag[1]
    elif tag[0] == 'q':
        passage_of[tag[1]] = (last_resp + 1) if last_resp is not None else 0


# ------------------------------------------------------------- banco final
GARB = re.compile(r'[\u0100-\u024f\u0400-\u052f\u0750-\u075f\u0d00-\u0d7f'
                  r'\u0d45]')
LABEL_RE = re.compile(r'(?:^|\s)[A-D]\)')
bank = {'year': 2024,
        'title': 'Simulacro Oficial ENP Beca 18 — Convocatoria 2024',
        'duration_min': 120,
        'sections': [
            {'id': 'matematica', 'label': 'Competencia Matemática',
             'from': 1, 'to': 30},
            {'id': 'lectura', 'label': 'Competencia Lectora', 'from': 31,
             'to': 60}],
        'passages': [{'id': ri + 1, 'title': None, 'html': passage_html[ri]}
                     for ri in range(len(passage_regions))],
        'questions': []}
flags = []
for n in range(1, 61):
    q = {'id': n, 'stem': stems[n],
         'options': [options[n][L] for L in 'ABCD'],
         'answer': answers.get(n, ''),
         'section': 'matematica' if n <= 30 else 'lectura'}
    if passage_of.get(n, 0):
        q['passage'] = passage_of[n]
    if qinfo[n]['fimgs']:
        q['images'] = qinfo[n]['fimgs']
    bank['questions'].append(q)
    if not q['stem']:
        flags.append('Q%d stem vacio' % n)
    for k, o in enumerate(q['options']):
        if not o:
            flags.append('Q%d opción %s vacía' % (n, 'ABCD'[k]))
        elif n >= 31 and '[[img:' in o:
            flags.append('Q%d opción %s es crop (lectura)' % (n, 'ABCD'[k]))
        elif LABEL_RE.search(o):
            flags.append('Q%d opción %s con label interno' % (n, 'ABCD'[k]))
        if GARB.search(o):
            flags.append('Q%d opción %s con chars basura: %r'
                         % (n, 'ABCD'[k], GARB.search(o).group(0)))
    if GARB.search(q['stem']):
        flags.append('Q%d stem con chars basura' % n)

for ri, p in enumerate(bank['passages']):
    n = len(p['html'])
    print('pasaje %d: %d chars%s' % (ri + 1, n, '  [CORTO]' if n < 300 else ''))

print('flags QA (%d):' % len(flags))
for f in flags:
    print('   -', f)

with open(OUT_JSON, 'w', encoding='utf-8') as fh:
    json.dump(bank, fh, ensure_ascii=False, indent=1)
print('banco escrito:', OUT_JSON)
print()
print('--- muestra de stems/opciones ---')
for n in range(1, 61):
    q = bank['questions'][n - 1]
    print('Q%-2d [%s] %s' % (n, q['answer'],
                             q['stem'][:66].replace('\n', ' ')))
    for k, o in enumerate(q['options']):
        print('     %s) %s' % ('ABCD'[k], o[:64]))
