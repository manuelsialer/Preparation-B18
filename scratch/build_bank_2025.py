"""Extrae el examen 2025 a scratch/exams/banks/2025.json (formato hibrido).

Pipeline (adaptado del extractor 2024):
  1. Todas las fuentes (ArialMT/Arial-Bold/Italic, Calibri-Bold) tienen
     ToUnicode roto: se decodifican por GID contra los TTF del sistema.
  2. Marcadores de pregunta = lineas "PREGUNTA N" (Arial-Bold, linea propia).
  3. Pasajes = lineas "Texto N" (6 textos, 5 preguntas cada uno, Q31-60).
  4. Opciones etiquetadas "a)".."d)" en columna unica; super/subindices como
     bandas satelite (dy ~5.5 en Arial) -> Unicode si mapea, si no crop por
     clusters.
  5. Figuras: rasters + drawings. Figuras pequenas superpuestas a una banda
     de texto -> token inline [[img:...]]. Opciones-imagen (Q7) se adjuntan
     por fila; preguntas sin filas de opciones (Q20, Q26) tienen su imagen
     de opciones partida en 4 recortes segun el perfil de tinta.
  6. Claves de la pagina 28 (pares "1c 31d ...").
"""
import fitz, re, json, os, io, sys, shutil, statistics
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fontTools.ttLib import TTFont

PDF = r'temarios\2027\examen-3-beca-18-convocatoria-2025.pdf'
OUT_JSON = r'scratch\exams\banks\2025.json'
IMG_DIR = os.path.join('_static', 'simulacros', 'img', '2025')
ZOOM = 3
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
if os.path.isdir(IMG_DIR):
    shutil.rmtree(IMG_DIR)
os.makedirs(IMG_DIR, exist_ok=True)

# ==================================================== mapas GID por fuente
FONTS = {}
for path, names in ((r'C:\Windows\Fonts\arial.ttf', ['ArialMT', 'Arial']),
                    (r'C:\Windows\Fonts\arialbd.ttf', ['Arial-BoldMT']),
                    (r'C:\Windows\Fonts\ariali.ttf', ['Arial-ItalicMT']),
                    (r'C:\Windows\Fonts\arialbi.ttf', ['Arial-BoldItalicMT']),
                    (r'C:\Windows\Fonts\calibrib.ttf', ['Calibri-Bold'])):
    f = TTFont(path)
    go = f.getGlyphOrder()
    rev = {}
    for u, g in f.getBestCmap().items():
        rev.setdefault(g, u)
    for n in names:
        FONTS[n] = (go, rev)

# MYingHei (vinetas de listas en Texto 6): gid 3 = vineta
MANUAL_FONTS = {'MYingHeiPRCW48-W4': {3: '\u2022'}}

LIG = {'\ufb01': 'fi', '\ufb02': 'fl', '\ufb00': 'ff', '\ufb03': 'ffi',
       '\ufb04': 'ffl'}
CTRL = re.compile(r'[\x00-\x08\x0b-\x1f\x7f]')

HEADERS = {'COMPETENCIA LECTORA', 'COMPETENCIAS MATEMÁTICAS'}
MARK_RE = re.compile(r'^\s*PREGUNTA\s+(\d{1,2})\s*$')
TEXTO_RE = re.compile(r'^\s*Texto\s+(\d{1,2})\s*$')


def gid_char(font, gid):
    if font in MANUAL_FONTS:
        return MANUAL_FONTS[font].get(gid)
    fr = FONTS.get(font)
    if fr is None or gid is None or not (0 <= gid < len(fr[0])):
        return None
    u = fr[1].get(fr[0][gid])
    return chr(u) if u else None


# ============================================================ carga de paginas
doc = fitz.open(PDF)
pages = []          # pno -> [lineas {pno,y0,x0,x1,y1,text,chars}]
fig_rects = {}      # pno -> [fitz.Rect] de figuras candidatas

for pno in range(doc.page_count):
    page = doc[pno]
    gmap = {}
    for sp in page.get_texttrace():
        base = sp['font'].split('+')[-1]
        for c in sp['chars']:
            ox, oy = c[2]
            gmap[(round(ox, 1), round(oy, 1))] = (base, c[1])
    lines = []
    for b in page.get_text('rawdict')['blocks']:
        if b.get('type') != 0:
            continue
        for ln in b['lines']:
            chars = []
            for s in ln['spans']:
                for ch in s.get('chars', []):
                    ox, oy = ch['origin']
                    font, gid = gmap.get((round(ox, 1), round(oy, 1)),
                                         (s.get('font', '').split('+')[-1],
                                          None))
                    c = gid_char(font, gid)
                    if c is None:
                        c = ch['c']
                    c = LIG.get(c, c)
                    if CTRL.match(c):
                        continue
                    chars.append({'c': c, 'bbox': ch['bbox'], 'oy': oy,
                                  'ox': ox, 'font': font, 'rank': 0})
            text = ''.join(c['c'] for c in chars)
            if not text.strip():
                continue
            bb = ln['bbox']
            lines.append({'pno': pno, 'y0': bb[1], 'y1': bb[3], 'x0': bb[0],
                          'x1': bb[2], 'text': text, 'chars': chars})
    lines.sort(key=lambda l: (round(l['y0'], 1), l['x0']))
    pages.append(lines)

    # ---- figuras: rasters y drawings (sin pie de pagina ni subrayados)
    rasters = [fitz.Rect(i['bbox']) for i in page.get_image_info()]
    draws = []
    for d in page.get_drawings():
        r = d['rect']
        if r.y0 > 780:                       # logo del pie
            continue
        if r.height < 2.5 and r.width > 40:  # subrayados/lineas
            continue
        if r.height < 0.5:                   # linea (p.ej. '=' o fraccion)
            r = fitz.Rect(r.x0, r.y0, r.x1, r.y0 + 1.0)
        if r.width < 0.5:
            r = fitz.Rect(r.x0, r.y0, r.x0 + 1.0, r.y1)
        draws.append(r)
    fig_rects[pno] = {'rasters': rasters, 'draws': draws}


def clusters(rects, gap=10):
    groups = []
    for r in sorted(rects, key=lambda r: (round(r.y0, 1), r.x0)):
        for g in groups:
            if not (r.x0 > g.x1 + gap or r.x1 < g.x0 - gap or
                    r.y0 > g.y1 + gap or r.y1 < g.y0 - gap):
                g.include_rect(r)
                break
        else:
            groups.append(fitz.Rect(r))
    changed = True
    while changed:
        changed = False
        for a in range(len(groups)):
            for b2 in range(a + 1, len(groups)):
                r1, r2 = groups[a], groups[b2]
                if not (r2.x0 > r1.x1 + gap or r2.x1 < r1.x0 - gap or
                        r2.y0 > r1.y1 + gap or r2.y1 < r1.y0 - gap):
                    r1.include_rect(r2)
                    groups.pop(b2)
                    changed = True
                    break
            if changed:
                break
    return groups


PAGE_AREA = doc[2].rect.get_area()
BG_RATIO = 0.85          # por encima de esto se considera fondo de pagina
all_figs = {}
for pno in range(doc.page_count):
    figs = []
    if pno < 2:                              # portada e instrucciones
        all_figs[pno] = figs
        continue
    src = fig_rects[pno]
    # cada raster es una figura independiente (no se fusionan entre si)
    for rr in src['rasters']:
        if rr.get_area() > BG_RATIO * PAGE_AREA:  # fondo de pagina
            continue
        figs.append({'rect': fitz.Rect(rr), 'raster': True})
    # los drawings se agrupan por proximidad y se fusionan con el raster
    # que solapan (graficos con superposicion vectorial)
    for g in clusters(src['draws']):
        if g.y0 > 780 or g.get_area() < 60 or g.get_area() > BG_RATIO * PAGE_AREA:
            continue
        host = None
        for f in figs:
            inter = fitz.Rect(f['rect']) & g
            if inter.get_area() > 0.25 * g.get_area():
                host = f
                break
        if host is not None:
            host['rect'].include_rect(g)
        else:
            figs.append({'rect': g, 'raster': False})
    figs.sort(key=lambda f: (round(f['rect'].y0, 1), f['rect'].x0))
    all_figs[pno] = figs

# ------------------------------------------------ marcadores y textos
marks = []      # (pno, y, n)
textos = []     # (pno, y, n)
for pno, lines in enumerate(pages):
    for ln in lines:
        t = ln['text'].strip()
        m = MARK_RE.match(t)
        if m and ln['x0'] < 150:
            marks.append((pno, ln['y0'], int(m.group(1))))
            continue
        m = TEXTO_RE.match(t)
        if m and ln['x0'] < 150:
            textos.append((pno, ln['y0'], int(m.group(1))))

marks_s = sorted(marks, key=lambda t: (t[0], t[1]))
textos_s = sorted(textos, key=lambda t: (t[0], t[1]))
print('marcadores:', len(marks_s), [m[2] for m in marks_s])
print('textos:', [(t[2], t[0] + 1, round(t[1], 1)) for t in textos_s])

# lineas de cuerpo
def is_body(ln):
    t = ln['text'].strip()
    if ln['y0'] < 60 or ln['y0'] > 780:
        return False
    if ln['pno'] == doc.page_count - 1:      # claves
        return False
    if t in HEADERS:
        return False
    if MARK_RE.match(t) or TEXTO_RE.match(t):
        return False
    return True


body = [ln for pno, lines in enumerate(pages) for ln in lines
        if is_body(ln)]
body.sort(key=lambda ln: (ln['pno'], round(ln['y0'], 1), ln['x0']))

# asignacion por eventos (pregunta / inicio de texto)
events = sorted([(pno, y, ('q', n)) for (pno, y, n) in marks_s] +
                [(pno, y, ('texto', n)) for (pno, y, n) in textos_s],
                key=lambda t: (t[0], t[1]))
assign = {}       # id(linea) -> ('q', n) | ('lee', idx)
passage_of = {}   # n pregunta -> idx pasaje (0 = sin pasaje)
ev_i = -1
cur_q = None
cur_region = None
cur_region_q = None      # region de pasaje activa para las preguntas
n_regions = len(textos_s)
for ln in body:
    key = (ln['pno'], ln['y0'])
    while ev_i + 1 < len(events) and (events[ev_i + 1][0],
                                      events[ev_i + 1][1]) <= (key[0],
                                                               key[1] + 4.5):
        ev_i += 1
        kind, val = events[ev_i][2]
        if kind == 'q':
            passage_of[val] = (cur_region_q + 1) \
                if cur_region_q is not None else 0
            cur_q, cur_region = val, None
        else:
            cur_q = None
            cur_region = textos_s.index(
                (events[ev_i][0], events[ev_i][1], val))
            cur_region_q = cur_region
    if cur_q is not None:
        assign[id(ln)] = ('q', cur_q)
    elif cur_region is not None:
        assign[id(ln)] = ('lee', cur_region)

n_q_lines = {n: 0 for n in range(1, 61)}
n_lee_lines = {i: 0 for i in range(n_regions)}
orphan = 0
for ln in body:
    a = assign.get(id(ln))
    if a is None:
        orphan += 1
    elif a[0] == 'q':
        n_q_lines[a[1]] += 1
    else:
        n_lee_lines[a[1]] += 1
print('lineas sin asignar:', orphan)
print('q con <2 lineas:', {n: c for n, c in n_q_lines.items() if c < 2})
print('pasajes con lineas:', n_lee_lines)

# ================================================================= n u c l e o
bars = {}
for pno in range(doc.page_count):
    bs = []
    sq_bx1 = [c['bbox'][2] for ln in pages[pno] for c in ln['chars']
              if c['c'] == '\u221a']
    for d in doc[pno].get_drawings():
        r = d['rect']
        if 4 <= r.width <= 60 and r.height <= 2 and 60 < r.y0 < 780:
            if any(abs(x - r.x0) < 2.5 for x in sq_bx1):
                continue
            bs.append((r.x0, r.y0, r.x1, r.y1))
    bars[pno] = bs

SUP = {'0': '\u2070', '1': '\u00b9', '2': '\u00b2', '3': '\u00b3',
       '4': '\u2074', '5': '\u2075', '6': '\u2076', '7': '\u2077',
       '8': '\u2078', '9': '\u2079', '+': '\u207a', '\u2212': '\u207b',
       '-': '\u207b', '=': '\u207c', '(': '\u207d', ')': '\u207e',
       'x': '\u02e3', 'n': '\u207f', 'a': '\u1d43', 'b': '\u1d47',
       'c': '\u1d9c', 'd': '\u1d48', 'e': '\u1d49', 'k': '\u1d4f',
       'm': '\u1d50', 'o': '\u1d52', 'p': '\u1d56', 't': '\u1d57',
       'u': '\u1d58', 'v': '\u1d5b'}
SUB = {'0': '\u2080', '1': '\u2081', '2': '\u2082', '3': '\u2083',
       '4': '\u2084', '5': '\u2085', '6': '\u2086', '7': '\u2087',
       '8': '\u2088', '9': '\u2089', '+': '\u208a', '\u2212': '\u208b',
       '-': '\u208b', '=': '\u208c', '(': '\u208d', ')': '\u208e',
       'a': '\u2090', 'e': '\u2091', 'o': '\u2092', 'x': '\u2093',
       'k': '\u2096', 'm': '\u2098', 'n': '\u2099', 'p': '\u209a',
       't': '\u209c', 'v': '\u1d65'}

# ventana de super/subindice para Arial 11pt (dy medido = 5.5)
SUP_DY = (3.5, 6.4)


def render_text(chars):
    return ''.join(c['c'] for c in
                   sorted(chars, key=lambda c: (c['ox'], c.get('rank', 0))))


def clean(s):
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r' +([,.;:!?])', r'\1', s)
    return s.strip()


_SUPSUB = ''.join(sorted(set(SUP.values()) | set(SUB.values())))
_SS_SPACE = re.compile(' ([%s]+)' % re.escape(_SUPSUB))


def tidy(s):
    """Reubica el espacio que precede a un super/subindice despues del mismo
    (2 11x -> 2(11) x ; 10 -27 -> 10(-27))."""
    s = _SS_SPACE.sub(lambda m: m.group(1) + ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


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
        solid = [c for c in b['chars'] if c['c'].strip()]
        b['sx0'] = min((c['bbox'][0] for c in solid), default=b['x0'])
    return bands


def find_labels(band):
    """Etiquetas a) b) c) d): letra minuscula + ')' pegados, sin caracter
    pegado antes de la letra (evita 'media)' etc.)."""
    chs = sorted(band['chars'], key=lambda c: c['ox'])
    out = []
    for i, a in enumerate(chs[:-1]):
        b2 = chs[i + 1]
        if a['c'] in 'abcd' and b2['c'] == ')':
            gap = b2['bbox'][0] - a['bbox'][2]
            prev = chs[i - 1] if i else None
            ok_prev = prev is None or prev['c'].strip() == '' or \
                a['bbox'][0] - prev['bbox'][2] > 3.5
            if gap < 2.5 and ok_prev:
                out.append({'letter': a['c'].upper(), 'x0': a['bbox'][0],
                            'x1': b2['bbox'][2]})
    return out


def box_in_raster(pno, x0, x1, oy):
    """True si una caja de texto cae por completo dentro de una imagen raster
    (grafico/tabla); en ese caso es una capa de texto duplicada."""
    for r in fig_rects[pno]['rasters']:
        if r.get_area() > BG_RATIO * PAGE_AREA:
            continue
        if (r.x0 - 1 <= x0 and x1 <= r.x1 + 1 and
                r.y0 - 2 <= oy <= r.y1 + 2):
            return True
    return False


def in_raster(pno, b):
    return box_in_raster(pno, b['x0'], b['x1'], b['oy'])


def bar_between_text(pno, y0, y1, x0, x1, ctx):
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


qinfo = {n: {'stem': [], 'opts': {}, 'rows': [], 'mcount': 0, 'fimgs': []}
         for n in range(1, 61)}
owner_state = {n: None for n in range(1, 61)}

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
    bands = [b for b in bands if not in_raster(pno, b)]
    rows = []
    page_events = []
    for b in bands:
        if not b['labels']:
            continue
        lbs = sorted(b['labels'], key=lambda l: l['x0'])
        opts = []
        for k, lb in enumerate(lbs):
            ox0 = lb['x1'] - 0.5
            ox1 = lbs[k + 1]['x0'] - 2 if k + 1 < len(lbs) else 540.0
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
    consumed = set()
    for b in bands:                      # paso A: constructos con barra
        if b['labels']:
            continue
        cands = []
        for row in rows:
            for o in row['opts']:
                d = abs(b['oy'] - row['oy'])
                if d > 12 or xover(b, o) <= 0:
                    continue
                if b['oy'] < row['oy']:
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
    owner = owner_state[n]               # paso B: posicionales
    for b in bands:
        if b['labels'] or id(b) in consumed:
            continue
        target = None
        can_cont = b['sx0'] >= 78        # continuaciones van identadas
        if rows:
            first, last = rows[0], rows[-1]
            if b['oy'] < first['oy'] - 1e-9:
                if can_cont and first['oy'] - b['oy'] <= 12:
                    target = pick_opt(first, b)
                elif can_cont and owner is not None and owner[0] == 'opt':
                    target = info['opts'][owner[1]]
            elif b['oy'] > last['oy'] + 1e-9:
                if can_cont:
                    target = pick_opt(last, b)
            else:
                nxt = next((r for r in rows if r['oy'] > b['oy'] + 1e-9),
                           None)
                if can_cont and nxt is not None and \
                        nxt['oy'] - b['oy'] <= 12:
                    target = pick_opt(nxt, b)
                elif can_cont:
                    prevr = [r for r in rows if r['oy'] < b['oy'] - 1e-9]
                    target = pick_opt(prevr[-1], b) if prevr \
                        else pick_opt(last, b)
        elif can_cont and owner is not None and owner[0] == 'opt':
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

# ------------------------------------------------------------- recortes
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
    clip = fitz.Rect(rect.x0 - 4, rect.y0 - 4, rect.x1 + 4, rect.y1 + 4) & \
        doc[pno].rect
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
    pix.save(os.path.join(IMG_DIR, name))


def ink_bands(pno, rect, min_gap=3.0):
    """Franjas de contenido (y en coords PDF) de un zona raster."""
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
    w, h, n, px = pix.width, pix.height, pix.n, pix.samples
    rows = []
    for y in range(h):
        rows.append(any(px[(y * w + x) * n] < 128
                        for x in range(0, w, 2)))
    bands = []
    cur = None
    gap = 0
    for y, v in enumerate(rows):
        if v:
            if cur is None:
                cur = [y, y]
            else:
                cur[1] = y
            gap = 0
        elif cur:
            gap += 1
            if gap * 0.5 >= min_gap:
                bands.append(cur)
                cur = None
    if cur:
        bands.append(cur)
    return [(rect.y0 + b[0] / 2.0, rect.y0 + b[1] / 2.0) for b in bands]


def ink_cols(pno, rect, min_gap=12.0):
    """Franjas de contenido (x en coords PDF) de una zona raster."""
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
    w, h, n, px = pix.width, pix.height, pix.n, pix.samples
    cols = []
    for x in range(w):
        cols.append(any(px[(y * w + x) * n] < 128
                        for y in range(0, h, 2)))
    bands = []
    cur = None
    gap = 0
    for x, v in enumerate(cols):
        if v:
            if cur is None:
                cur = [x, x]
            else:
                cur[1] = x
            gap = 0
        elif cur:
            gap += 1
            if gap * 0.5 >= min_gap:
                bands.append(cur)
                cur = None
    if cur:
        bands.append(cur)
    return [(rect.x0 + b[0] / 2.0, rect.x0 + b[1] / 2.0) for b in bands]


def rects_close(a, b, tol=8.0):
    gap = max(a.x0 - b.x1, b.x0 - a.x1, a.y0 - b.y1, b.y0 - a.y1)
    return gap <= tol


def chain_bands(band_list):
    chains = []
    for b in band_list:
        if chains and b['oy'] - chains[-1][-1]['oy'] <= 12:
            chains[-1].append(b)
        else:
            chains.append([b])
    return chains


INLINE_L, INLINE_R = '\ue000', '\ue001'


def render_chain(pno, qid, chain):
    def nsolid(b):
        return len([c for c in b['chars'] if c['c'].strip()])

    if len(chain) == 1:
        return clean(render_text(chain[0]['chars']))
    fulls = [b for b in chain if nsolid(b) >= 8]
    if not fulls:
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
        base = fulls[0]
        return render_base(pno, qid, base,
                           [b for b in chain if b is not base])
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
            if SUP_DY[0] < abs(dy) <= SUP_DY[1] and c['c'] in mp:
                merged.append(dict(c, c=mp[c['c']], rank=1))
            else:
                bad.append(c)
    if not bad:
        return clean(render_text(merged))
    if whole:
        return None
    info = qinfo[qid]
    bad_sorted = sorted(bad, key=lambda c: c['ox'])
    clusters_c = []
    for c in bad_sorted:
        if clusters_c and c['ox'] - clusters_c[-1]['x1'] < 18:
            clusters_c[-1]['chars'].append(c)
            clusters_c[-1]['x1'] = max(clusters_c[-1]['x1'], c['bbox'][2])
        else:
            clusters_c.append({'chars': [c], 'x0': c['ox'],
                               'x1': c['bbox'][2]})
    keep = list(merged)
    tokens = []
    for cl in clusters_c:
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


# ------------------------------------------- render de stems por pregunta
def render_stem(n):
    info = qinfo[n]
    stems = {}
    by_page = {}
    for pno, b in info['stem']:
        if b['x0'] > 512 and len([c for c in b['chars']
                                  if c['c'].strip()]) <= 2:
            continue                       # digitos sueltos del margen
        by_page.setdefault(pno, []).append(b)
    parts = []
    for pno in sorted(by_page):
        for chain in chain_bands(by_page[pno]):
            t = render_chain(pno, n, chain)
            if t:
                parts.append(t)
    return ' '.join(parts)


stems = {n: render_stem(n) for n in range(1, 61)}

# ------------------------------------------------------------------ figuras
def region_at(pno, y):
    """Indice del pasaje cuyo rango (Texto -> primera PREGUNTA) contiene y."""
    for ri, (tp, ty, tn) in enumerate(textos_s):
        nxt = next(((p2, y2) for (p2, y2, k) in events
                    if k[0] == 'q' and (p2, y2) > (tp, ty)), None)
        if nxt is None:
            nxt = (doc.page_count, 1e9)
        if (pno, y) >= (tp, ty - 1) and (pno, y) < nxt:
            return ri
    return None


pfigs = {}
qfigs = {n: [] for n in range(1, 61)}
orphan_figs = 0
for pno in sorted(all_figs):
    if pno >= doc.page_count - 1:
        continue
    for fg in sorted(all_figs[pno], key=lambda f: f['rect'].y0):
        r = fg['rect']
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        ri = region_at(pno, cy)
        if ri is not None:
            k = len(pfigs.get(ri, [])) + 1
            name = 'p%d_f%d.png' % (ri + 1, k)
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
            print('[fig sin dueno] p%d [%6.1f %6.1f %6.1f %6.1f]'
                  % (pno + 1, r.x0, r.y0, r.x1, r.y1))
            continue
        qfigs[own].append({'pno': pno, 'cy': cy, 'cx': cx, 'rect': r,
                           'raster': fg.get('raster', False),
                           'name': 'q%02d_f%d.png' % (own,
                                                      len(qfigs[own]) + 1)})
        crop_fig(pno, r, qfigs[own][-1]['name'])
print('figuras: pasaje', {k: len(v) for k, v in pfigs.items()},
      '| huerfanas:', orphan_figs)

# ---- adjuntar figuras de pregunta:
#      1) inline si es pequena y solapa una banda de texto (stem/cont)
#      2) por fila de opcion si hay filas (Q7)
#      3) si la pregunta no tiene filas: perfil de tinta con 4 franjas ->
#         4 recortes como opciones (Q20, Q26); si no -> q.images
INLINE_MARK = re.compile(INLINE_L + r'([^' + re.escape(INLINE_R) +
                         r']+)' + INLINE_R)
img_names = {}


def split_option_image(n, f):
    """Parte una imagen de opciones en 4 recortes: 4 franjas verticales
    (a,b,c,d) o una rejilla 2x2 (a b / c d). Devuelve True si lo logro."""
    info = qinfo[n]
    r = f['rect']
    vb = ink_bands(f['pno'], r)
    hb = ink_cols(f['pno'], r, min_gap=26.0)
    crops = []
    if len(vb) == 4:
        crops = [(r.x0, vb[k][0], r.x1, vb[k][1]) for k in range(4)]
    elif len(vb) == 2 and len(hb) == 2:
        for (ry0, ry1) in vb:
            for (cx0, cx1) in hb:
                crops.append((cx0, ry0, cx1, ry1))
    if not crops:
        return False
    for k, (cx0, cy0, cx1, cy1) in enumerate(crops):
        nm = 'q%02d_o%d.png' % (n, k + 1)
        clip = fitz.Rect(cx0 - 2, cy0 - 2, cx1 + 2, cy1 + 2) & \
            doc[f['pno']].rect
        pix = doc[f['pno']].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM),
                                       clip=clip)
        pix.save(os.path.join(IMG_DIR, nm))
        info['opts'].setdefault(
            'ABCD'[k], {'letter': 'ABCD'[k], 'imgs': [], 'cont': [],
                        'num': [], 'den': [], 'base': [],
                        'constructo': False, 'pno': f['pno'],
                        'row_oy': cy0, 'x0': cx0, 'x1': cx1})
        info['opts']['ABCD'[k]]['imgs'].append(nm)
    return True


def absorb_into(pno, rect, bands):
    """Incorpora al recorte de una figura vectorial los caracteres que caen
    dentro de su rect (p.ej. el radicando de una raiz o la 'x' de f(x)).
    Devuelve True si absorbio algun caracter."""
    got = False
    for (bpno, b) in bands:
        if bpno != pno:
            continue
        keep = []
        for c in b['chars']:
            if INLINE_L in c['c']:
                keep.append(c)
                continue
            cb = c['bbox']
            inside_x = cb[0] >= rect.x0 - 1 and cb[0] <= rect.x1 + 1
            inside_y = rect.y0 - 1 <= c['oy'] <= rect.y1 + 2
            if c['c'].strip() and inside_x and inside_y:
                rect.x0 = min(rect.x0, cb[0])
                rect.x1 = max(rect.x1, cb[2])
                got = True
            else:
                keep.append(c)
        b['chars'] = keep
    return got


def attach_figs():
    for n in range(1, 61):
        info = qinfo[n]
        # bandas de texto disponibles (stem + conts de opciones)
        bands_all = list(info['stem'])
        for row in info['rows']:
            for o in row['opts']:
                bands_all += [(b['pno'], b) for b in o['cont']]
        for f in qfigs[n]:
            r = f['rect']
            fh = r.y1 - r.y0
            fw = r.x1 - r.x0
            # 1) imagen alineada con una fila de opcion (Q7)
            rows_pg = sorted([row for row in info['rows']
                              if row['pno'] == f['pno']],
                             key=lambda r2: r2['oy'])
            aligned = [row for row in rows_pg
                       if abs(row['oy'] - f['cy']) <= 16]
            if aligned and fh <= 40:
                row = min(aligned, key=lambda r2: abs(r2['oy'] - f['cy']))
                best_o, bo = None, -1e9
                for o in row['opts']:
                    ov = min(f['cx'], o['x1']) - max(f['cx'], o['x0'])
                    if ov > bo:
                        bo, best_o = ov, o
                if best_o is not None and bo > -20:
                    best_o['imgs'].append(f['name'])
                    f['used'] = 'opt:' + best_o['letter']
                    continue
            # 2) figura pequena pegada a una banda de texto -> token inline
            best, bscore = None, 1e9
            fcy = (r.y0 + r.y1) / 2
            for (bpno, b) in bands_all:
                if bpno != f['pno']:
                    continue
                dv = abs(fcy - b['oy'])
                ox = min(b['x1'], r.x1) - max(b['x0'], r.x0)
                gapx = max(0.0, max(b['x0'] - r.x1, r.x0 - b['x1']))
                if ox > 0 or gapx <= 15:
                    score = dv + gapx * 0.4
                    if score < bscore:
                        bscore, best = score, b
            if best is not None and fh <= 26 and fw <= 130 and bscore <= 13:
                if not f['raster'] and absorb_into(f['pno'], r, bands_all):
                    crop_fig(f['pno'], r, f['name'])
                if os.environ.get('DBG') and n in (17, 20):
                    print('INLINE Q%d %s rect[%.1f %.1f %.1f %.1f] raster=%s'
                          % (n, f['name'], r.x0, r.y0, r.x1, r.y1,
                             f['raster']))
                pseudo = {'c': INLINE_L + f['name'] + INLINE_R,
                          'bbox': (r.x0, r.y0, r.x1, r.y1),
                          'oy': fcy, 'ox': r.x0, 'rank': 1}
                best['chars'].append(pseudo)
                img_names[f['name']] = f['name']
                f['used'] = 'inline'
                continue
            # 3) pregunta sin filas de opciones: partir la imagen de opciones
            if not info['rows'] and split_option_image(n, f):
                f['used'] = 'optsplit'
                continue
            # 4) figura del enunciado (se fusiona con otras cercanas luego)
            if not f['raster']:
                absorb_into(f['pno'], r, bands_all)
            info['fimgs'].append({'name': f['name'], 'pno': f['pno'],
                                  'rect': fitz.Rect(r)})
            f['used'] = 'qimg'
    # fusiona figuras del enunciado muy cercanas o solapadas en un recorte
    for n in range(1, 61):
        info = qinfo[n]
        merged = []
        for item in info['fimgs']:
            for m in merged:
                if m['pno'] == item['pno'] and \
                        rects_close(m['rect'], item['rect'], tol=8.0):
                    m['rect'].include_rect(item['rect'])
                    break
            else:
                merged.append({'pno': item['pno'],
                               'rect': fitz.Rect(item['rect'])})
        names = []
        for k, m in enumerate(merged):
            nm = 'q%02d_g%d.png' % (n, k + 1)
            crop_fig(m['pno'], m['rect'], nm)
            names.append(nm)
        info['fimgs'] = names


attach_figs()

if os.environ.get('DBG'):
    for n in (7, 20, 27):
        info = qinfo[n]
        print('--- Q%d rows=%d opts=%s' % (n, len(info['rows']),
                                           list(info['opts'].keys())))
        for row in info['rows']:
            print('   row p%d oy%.1f opts=%s' % (row['pno'], row['oy'],
                                                 [o['letter'] for o in
                                                  row['opts']]))
        for f in qfigs[n]:
            print('   fig %s p%d cy%.1f rect[%.1f %.1f %.1f %.1f] used=%s'
                  % (f['name'], f['pno'], f['cy'], f['rect'].x0, f['rect'].y0,
                     f['rect'].x1, f['rect'].y1, f.get('used')))
        print('   fimgs=', info['fimgs'])
    for pno in (3, 6, 8, 11, 12):
        print('--- p%d figs:' % (pno + 1))
        for f in all_figs[pno]:
            r = f['rect']
            print('   [%.1f %.1f %.1f %.1f] raster=%s' % (r.x0, r.y0, r.x1,
                                                          r.y1, f['raster']))
        print('   marks:', [(round(y, 1), m) for (p, y, m) in marks_s
                            if p == pno])

# re-render de stems (los tokens inline se insertaron en las bandas)
stems = {n: render_stem(n) for n in range(1, 61)}


def subst_inline(s):
    return INLINE_MARK.sub(lambda m: '[[img:%s]]' % m.group(1), s)


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
            rest = list(o['cont'])
        else:
            # la banda base se trata como una banda mas para poder fusionar
            # con sus satelites (super/subindices) por posicion x
            base_chars = list(o['base'])
            base_band = {'chars': base_chars, 'oy': o['row_oy'],
                         'pno': o['pno'], 'max': o['row_oy'],
                         'x0': min((c['bbox'][0] for c in base_chars),
                                   default=o['x0']),
                         'x1': max((c['bbox'][2] for c in base_chars),
                                   default=o['x1'])}
            rest = [base_band] + list(o['cont'])
        by_page = {}
        for b in rest:
            by_page.setdefault(b['pno'], []).append(b)
        for pno2 in sorted(by_page):
            bs = sorted(by_page[pno2], key=lambda b: b['oy'])
            for chain in chain_bands(bs):
                t = render_chain(pno2, n, chain)
                if t:
                    oparts.append(t)
        txt = tidy(subst_inline(' '.join(p for p in oparts if p)))
        if o['imgs']:
            txt = (txt + ' ' + ' '.join('[[img:%s]]' % i
                                        for i in o['imgs'])).strip()
        options[n][letter] = txt

stems = {n: tidy(subst_inline(s)) for n, s in stems.items()}

# ------------------------------------------------------------------ pasajes
passage_items = {ri: [] for ri in range(n_regions)}
for ln in body:
    a = assign.get(id(ln))
    if a is not None and a[0] == 'lee':
        if box_in_raster(ln['pno'], ln['x0'], ln['x1'], ln['y0']):
            continue
        passage_items[a[1]].append((ln['pno'], ln['y0'], 0, 'line', ln))
for ri, fl in pfigs.items():
    for f in fl:
        passage_items[ri].append((f['pno'], f['cy'], 1, 'fig',
                                  '[[img:%s]]' % f['name']))
passage_html = {}
for ri in range(n_regions):
    items = sorted(passage_items[ri], key=lambda t: (t[0], t[1], t[2]))
    parts = []
    for it in items:
        if it[3] == 'fig':
            parts.append(it[4])
        else:
            t = tidy(clean(render_text(it[4]['chars'])))
            if t:
                parts.append(t)
    passage_html[ri] = '\n\n'.join(parts)

# ------------------------------------------------------------------- claves
# la pagina de claves (tabla 1..30 | 31..60) tiene ToUnicode correcto:
# se parsea con get_text y se emparejan numero+letra en orden de lectura
ktxt = doc[doc.page_count - 1].get_text('text')
answers = {}
for num, le in re.findall(r'(\d{1,2})\s+([a-d])\b', ktxt):
    if 1 <= int(num) <= 60 and int(num) not in answers:
        answers[int(num)] = le.upper()
print('claves:', len(answers))

# ------------------------------------------------------------- banco final
GARB = re.compile(r'[\u0100-\u024f\u0400-\u052f\u0750-\u075f\u0d00-\u0d7f'
                  r'\u0d45]')
LABEL_RE = re.compile(r'(?:^|\s)[A-D]\)')
bank = {'year': 2025,
        'title': 'Simulacro Oficial ENP Beca 18 — Convocatoria 2025',
        'duration_min': 120,
        'sections': [
            {'id': 'matematica', 'label': 'Competencia Matemática',
             'from': 1, 'to': 30},
            {'id': 'lectura', 'label': 'Competencia Lectora', 'from': 31,
             'to': 60}],
        'passages': [{'id': ri + 1, 'title': 'Texto %d' % (ri + 1),
                      'html': passage_html[ri]}
                     for ri in range(n_regions)],
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
    if 'PREGUNTA' in q['stem']:
        flags.append('Q%d stem con marcador' % n)
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
    nch = len(p['html'])
    print('pasaje %d: %d chars%s' % (ri + 1, nch,
                                     '  [CORTO]' if nch < 300 else ''))
print('flags QA (%d):' % len(flags))
for f in flags:
    print('   -', f)

with open(OUT_JSON, 'w', encoding='utf-8') as fh:
    json.dump(bank, fh, ensure_ascii=False, indent=1)
print('banco escrito:', OUT_JSON)

# ---- limpieza: borra recortes no referenciados por el banco
used_imgs = set()


def _scan(s):
    used_imgs.update(m.group(1)
                     for m in re.finditer(r'\[\[img:([^\]]+)\]\]', s))


for p in bank['passages']:
    _scan(p['html'])
for q in bank['questions']:
    _scan(q['stem'])
    for o in q['options']:
        _scan(o)
    for im in q.get('images', []):
        used_imgs.add(im)
removed = 0
for fn in os.listdir(IMG_DIR):
    if fn not in used_imgs:
        os.remove(os.path.join(IMG_DIR, fn))
        removed += 1
print('recortes usados:', len(used_imgs), '| eliminados (huerfanos):',
      removed)
print()
print('--- muestra ---')
for n in range(1, 61):
    q = bank['questions'][n - 1]
    print('Q%-2d [%s] %s' % (n, q['answer'],
                             q['stem'][:66].replace('\n', ' ')))
    for k, o in enumerate(q['options']):
        print('     %s) %s' % ('ABCD'[k], o[:64]))
