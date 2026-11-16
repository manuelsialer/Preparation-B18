"""Extrae el examen 2025 a scratch/exams/banks/2025.json (formato hibrido).

Particularidades del ENP 2025 vs 2024:
  - Fuentes Arial (decodificacion por GID contra los TTF del sistema; el
    rawdict se usa como fallback). No hay CambriaMath: las expresiones
    matematicas son rasters pequenos o trazos vectoriales incrustados.
  - Marcadores "PREGUNTA N" (negrita) y pasajes "Texto N" (negrita, con
    titulo centrado en negrita debajo).
  - Etiquetas de opcion en minuscula: a) b) c) d).
  - Super/subindices: chars posicionales (dy ~5.5-6) -> Unicode SUP/SUB;
    ventana de satelite 3.0-6.9 (la linea vecina queda a 7.2+).
  - Clusters pequenos (h <= 34) = formulas inline: los raster se recortan
    tal cual; los vectoriales absorben los chars de formula (size < 10.6)
    cercanos en la misma linea, iterativamente.
  - P27: opciones 100% raster (4 tablas en una sola imagen) -> division
    2x2 por el punto medio del rect.

Pipeline:
  1. Decodifica texto por GID (arial*.ttf).
  2. Clusters de figuras por pagina (imagenes + drawings; excluye pie de
     pagina y subrayados decorativos h=0).
  3. Corte por marcadores PREGUNTA / Texto; asignacion de lineas por
     posicion (pno, y).
  4. Bandas de chars por pregunta: opciones (etiquetas a-d), satelites
     super/sub -> Unicode; formulas inline -> crops [[img:...]].
  5. Pasajes: lineas + figuras en orden y; titulo centrado.
  6. Claves de la ultima pagina.
  7. Recortes a _static/simulacros/img/2025/.
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

# ================================================== mapas GID de fuentes Arial
maps = {}
for path, names in ((r'C:\Windows\Fonts\arial.ttf', ['ArialMT', 'Arial']),
                    (r'C:\Windows\Fonts\arialbd.ttf', ['Arial-BoldMT']),
                    (r'C:\Windows\Fonts\ariali.ttf', ['Arial-ItalicMT']),
                    (r'C:\Windows\Fonts\arialbi.ttf',
                     ['Arial-BoldItalicMT'])):
    f = TTFont(path)
    go = f.getGlyphOrder()
    rev = {}
    for u, g in f.getBestCmap().items():
        rev.setdefault(g, u)
    for n in names:
        maps[n] = (go, rev)

LIG = {'\ufb01': 'fi', '\ufb02': 'fl', '\ufb00': 'ff', '\ufb03': 'ffi',
       '\ufb04': 'ffl'}
CTRL = re.compile(r'[\x00-\x08\x0b-\x1f\x7f]')


def gid2ch(font, gid):
    mr = maps.get(font)
    if mr is None or gid is None:
        return None
    go, rev = mr
    if 0 <= gid < len(go):
        u = rev.get(go[gid])
        if u:
            return chr(u)
    return None


doc = fitz.open(PDF)
NP = doc.page_count
FIRST_P = 2                 # 0-based: paginas 1-2 son portada
KEYS_P = NP - 1             # ultima pagina: claves
INLINE_H = 34               # altura maxima de formula inline
INLINE_W = 430              # ancho maximo de formula inline


def decode_page(pno):
    """Lineas de la pagina con chars decodificados por GID."""
    lines = []
    raw = doc[pno].get_text('rawdict')
    gmap = {}
    for sp in doc[pno].get_texttrace():
        base = sp['font'].split('+')[-1]
        for c in sp['chars']:
            ox, oy = c[2]
            gmap[(round(ox, 1), round(oy, 1))] = (base, c[1])
    for b in raw['blocks']:
        if b.get('type') != 0:
            continue
        for ln in b['lines']:
            chars = []
            for s in ln['spans']:
                base = s.get('font', '').split('+')[-1]
                hei = 'MYingHei' in base
                for ch in s.get('chars', []):
                    ox, oy = ch['origin']
                    font, gid = gmap.get((round(ox, 1), round(oy, 1)),
                                         (base, None))
                    c = gid2ch(font, gid)
                    if c is None:
                        c = ch['c']
                    c = LIG.get(c, c)
                    if hei:
                        c = '•'          # vinetas de la Matriz de Eisenhower
                    if CTRL.match(c):
                        continue
                    chars.append({'c': c, 'bbox': ch['bbox'], 'oy': oy,
                                  'ox': ox, 'font': font,
                                  'size': round(s.get('size', 0), 1)})
            txt = ''.join(c['c'] for c in chars)
            if txt.strip():
                bb = ln['bbox']
                lines.append({'pno': pno, 'y0': bb[1], 'y1': bb[3],
                              'x0': bb[0], 'x1': bb[2], 'chars': chars,
                              'text': txt})
    lines.sort(key=lambda l: (round(l['y0'], 1), l['x0']))
    return lines


# ======================================================== clusters de figuras
def clusters(rects, gap=10):
    groups = []
    for r in sorted(rects, key=lambda r: (round(r.y0, 1), r.x0)):
        for g in groups:
            if not (r.x0 > g.x1 + gap or r.x1 < g.x0 - gap or
                    r.y0 > g.y1 + gap or r.y1 < g.y0 - gap):
                g.include_rect(fitz.Rect(r))
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


pages = {}          # pno -> lineas
page_figs = {}      # pno -> [{'rect','has_img','inline','chars'}]
for pno in range(FIRST_P, KEYS_P):
    lines = decode_page(pno)
    pages[pno] = lines
    rects = []
    info = doc[pno].get_image_info()
    for i in info:
        rects.append(fitz.Rect(i['bbox']))
    for d in doc[pno].get_drawings():
        r = d['rect']
        if r.y0 > 785:                    # icono del pie de pagina
            continue
        rects.append(r)
    figs = []
    for g in clusters(rects):
        if g.y0 > 780:
            continue
        hi = any(i['bbox'][0] >= g.x0 - 1 and i['bbox'][2] <= g.x1 + 1 and
                 i['bbox'][1] >= g.y0 - 1 and i['bbox'][3] <= g.y1 + 1
                 for i in info)
        if g.height < 2 and not hi:       # subrayado decorativo
            continue
        if g.get_area() < 150:
            continue
        figs.append({'rect': g, 'has_img': hi, 'chars': [],
                     'inline': g.height <= INLINE_H and g.width <= INLINE_W})
    page_figs[pno] = figs

# =============================== formulas inline: absorcion y consumo chars
fig_of_char = {}
excluded_lines = set()
for pno, figs in page_figs.items():
    chars = [c for ln in pages[pno] for c in ln['chars']]
    for fg in figs:
        r = fitz.Rect(fg['rect'])
        if fg['inline']:
            if not fg['has_img']:
                # formula vectorial: absorbe chars de formula (size chico)
                # cercanos en la misma linea, iterativamente
                pending = [c for c in chars
                           if c['c'].strip() and c['size'] < 10.6]
                for _ in range(8):
                    zone = fitz.Rect(r.x0 - 3, r.y0 - 2.5,
                                     r.x1 + 10, r.y1 + 2.5)
                    new = [c for c in pending
                           if r.y0 - 2.5 <= (c['bbox'][1] + c['bbox'][3]) / 2
                           <= r.y1 + 2.5 and
                           zone.x0 <= (c['bbox'][0] + c['bbox'][2]) / 2
                           <= zone.x1]
                    if not new:
                        break
                    for c in new:
                        pending.remove(c)
                        fg['chars'].append(c)
                        fig_of_char[id(c)] = fg
                    for c in new:
                        r.include_rect(fitz.Rect(c['bbox']))
            # nucleo: cualquier char (incl. espacios) con centro dentro +2
            core = fitz.Rect(fg['rect'].x0 - 2, fg['rect'].y0 - 2,
                             fg['rect'].x1 + 2, fg['rect'].y1 + 2)
            for c in chars:
                if id(c) in fig_of_char:
                    continue
                cx = (c['bbox'][0] + c['bbox'][2]) / 2
                cy = (c['bbox'][1] + c['bbox'][3]) / 2
                if core.x0 <= cx <= core.x1 and core.y0 <= cy <= core.y1:
                    fg['chars'].append(c)
                    fig_of_char[id(c)] = fg
            fg['rect'] = r
        else:
            for ln in pages[pno]:
                cy = (ln['y0'] + ln['y1']) / 2
                cx = (ln['x0'] + ln['x1']) / 2
                t = ln['text'].strip()
                if r.x0 - 2 <= cx <= r.x1 + 2 and r.y0 - 2 <= cy <= r.y1 + 2:
                    if re.match(r'^[a-d]\)', t):
                        continue        # etiquetas dentro de figuras: quedan
                    excluded_lines.add(id(ln))
            fg['rect'] = r

# ============================================================== marcadores
PRE_G_RE = re.compile(r'^\s*PREGUNTA\s+(\d{1,2})\s*$')
TEXTO_RE = re.compile(r'^\s*Texto\s+(\d{1,2})\s*$')

marks = []          # (pno, y, n)
textos = []         # (pno, y, n)
for pno in range(FIRST_P, KEYS_P):
    for ln in pages[pno]:
        t = ln['text'].strip()
        m = PRE_G_RE.match(t)
        if m:
            marks.append((pno, ln['y0'], int(m.group(1))))
            continue
        m = TEXTO_RE.match(t)
        if m:
            textos.append((pno, ln['y0'], int(m.group(1))))
marks.sort(key=lambda t: (t[0], t[1]))
textos.sort(key=lambda t: (t[0], t[1]))
print('marcadores:', len(marks), [m[2] for m in marks])
print('textos:', [(t[2], t[0] + 1, round(t[1], 1)) for t in textos])

# region de pasaje: del marcador Texto N al primer PREGUNTA posterior
passage_regions = []
for (pno, y, n) in textos:
    end = (KEYS_P, 1e9)
    for (mp, my, mn) in marks:
        if (mp, my) > (pno, y):
            end = (mp, my)
            break
    passage_regions.append({'n': n, 'pno': pno, 'y': y, 'end': end})


def region_at(pno, y):
    for r in passage_regions:
        if (pno, y) > (r['pno'], r['y']) and (pno, y) < r['end']:
            return r['n']
    return None


# ------------------------------------------------------- titulos de pasajes
passage_title = {}
title_line_ids = set()
for r in passage_regions:
    pno, y0 = r['pno'], r['y']
    prev = None
    for ln in pages[pno]:
        if ln['y0'] <= y0 + 2:
            continue
        if ln['y0'] > y0 + 48:
            break
        solid = [c for c in ln['chars'] if c['c'].strip()]
        if not solid:
            continue
        bold = all(c['font'] == 'Arial-BoldMT' for c in solid)
        centered = ln['x0'] > 100
        if bold and centered:
            passage_title[r['n']] = (passage_title.get(r['n'], '') + ' ' +
                                     ln['text'].strip()).strip()
            title_line_ids.add(id(ln))
            prev = ln
            continue
        if prev is not None and ln['y0'] - prev['y0'] > 20:
            break
        prev = ln

# ============================================ lineas de cuerpo y asignacion
is_marker = set()
for pno in range(FIRST_P, KEYS_P):
    for ln in pages[pno]:
        t = ln['text'].strip()
        if PRE_G_RE.match(t) or TEXTO_RE.match(t):
            is_marker.add(id(ln))


def is_body(ln):
    if not (60 < ln['y0'] < 785):
        return False
    if id(ln) in is_marker or id(ln) in title_line_ids:
        return False
    return True


body = []
for pno in sorted(pages):
    for ln in pages[pno]:
        if is_body(ln):
            body.append(ln)

# eventos: marcadores de pregunta y de texto
events = sorted([(pno, y, ('q', n)) for (pno, y, n) in marks] +
                [(pno, y, ('texto', n)) for (pno, y, n) in textos],
                key=lambda t: (t[0], t[1]))

assign = {}           # id(line) -> ('q', n) | ('texto', n)
ev_i = -1
cur = None
for ln in sorted(body, key=lambda l: (l['pno'], round(l['y0'], 1), l['x0'])):
    if id(ln) in excluded_lines:
        continue
    key = (ln['pno'], ln['y0'])
    while ev_i + 1 < len(events) and \
            (events[ev_i + 1][0], events[ev_i + 1][1]) <= (key[0], key[1] + 4.5):
        ev_i += 1
        cur = events[ev_i][2]
    if cur is not None:
        assign[id(ln)] = cur

# ================================================== bandas y render de texto
SUP = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶',
       '7': '⁷', '8': '⁸', '9': '⁹', '+': '⁺', '−': '⁻', '-': '⁻', '=': '⁼',
       '(': '⁽', ')': '⁾', 'x': 'ˣ', 'n': 'ⁿ', 'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ',
       'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
       'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'o': 'ᵒ', 'p': 'ᵖ', 'r': 'ʳ', 's': 'ˢ',
       't': 'ᵗ', 'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'y': 'ʸ', 'z': 'ᶻ'}
SUB = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆',
       '7': '₇', '8': '₈', '9': '₉', '+': '₊', '−': '₋', '-': '₋', '=': '₌',
       '(': '₍', ')': '₎', 'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ',
       'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ', 'p': 'ₚ', 'r': 'ᵣ',
       's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ', 'v': 'ᵥ', 'x': 'ₓ'}
SAT_LO, SAT_HI = 3.0, 6.9      # ventana |dy| de super/subindices


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
        b['toks'] = []
        b['sats'] = []
        b['nsolid'] = len(solid)
    # satelites: banda pequena cerca (|dy| <= 6.9) de una con mas chars
    for s in bands:
        if s['nsolid'] >= 8:
            continue
        best, bd = None, 1e9
        for b in bands:
            if b is s or b['nsolid'] <= s['nsolid']:
                continue
            d = abs(b['oy'] - s['oy'])
            if SAT_LO < d <= SAT_HI and d < bd:
                best, bd = b, d
        if best is not None:
            best['sats'].append(s)
            s['is_sat'] = True
    return bands


def find_labels(band):
    """Etiquetas a) b) c) d); x0 < 95 o grilla (2+ etiquetas consecutivas)."""
    chs = sorted(band['chars'], key=lambda c: c['ox'])
    out = []
    for a, b2 in zip(chs, chs[1:]):
        if (a['c'] in 'abcd' and b2['c'] == ')'
                and b2['bbox'][0] - a['bbox'][2] < 3):
            out.append({'letter': a['c'].upper(), 'x0': a['bbox'][0],
                        'x1': b2['bbox'][2]})
    if len(out) == 1 and out[0]['x0'] >= 95:
        return []
    return out


def clean(s):
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r' +([,.;:!?])', r'\1', s)
    return s.strip()


mcount = {n: 0 for n in range(1, 61)}
fcount = {n: 0 for n in range(1, 61)}
pcount = {}


def crop_chars(pno, chars, name, extra_rect=None):
    xs0 = [c['bbox'][0] for c in chars]
    ys0 = [c['bbox'][1] for c in chars]
    xs1 = [c['bbox'][2] for c in chars]
    ys1 = [c['bbox'][3] for c in chars]
    if extra_rect is not None:
        xs0.append(extra_rect.x0); ys0.append(extra_rect.y0)
        xs1.append(extra_rect.x1); ys1.append(extra_rect.y1)
    clip = fitz.Rect(min(xs0) - 3, min(ys0) - 3, max(xs1) + 3, max(ys1) + 3) \
        & doc[pno].rect
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
    pix.save(os.path.join(IMG_DIR, name))
    return name


def crop_zone(pno, rect, name):
    clip = fitz.Rect(rect.x0 - 3, rect.y0 - 3, rect.x1 + 3, rect.y1 + 3) \
        & doc[pno].rect
    pix = doc[pno].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
    pix.save(os.path.join(IMG_DIR, name))
    return name


def render_chars(chars, toks):
    parts = [(t['x'], 'tok', t) for t in toks]
    parts += [(c['bbox'][0], 'c', c) for c in chars]
    parts.sort(key=lambda t: t[0])
    out = []
    for _, kind, v in parts:
        if kind == 'tok':
            out.append('[[img:%s]]' % v['name'])
        else:
            out.append(v['c'])
    return ''.join(out)


def render_full(qid, pno, band):
    """Banda + satelites (SUP/SUB unicode) + tokens inline por x."""
    solid = [c for c in band['chars'] if c['c'].strip()]
    base_med = statistics.median([c['oy'] for c in solid]) if solid \
        else band['oy']
    merged = list(band['chars'])
    bad = []
    for s in band['sats']:
        for c in s['chars']:
            if not c['c'].strip():
                continue
            dy = c['oy'] - base_med
            mp = SUP if dy < 0 else SUB
            if SAT_LO < abs(dy) <= SAT_HI and c['c'] in mp:
                merged.append(dict(c, c=mp[c['c']]))
            else:
                bad.append(c)
    toks = list(band['toks'])
    if bad:
        mcount[qid] += 1
        name = 'q%02d_m%d.png' % (qid, mcount[qid])
        crop_chars(pno, bad, name)
        toks = toks + [{'x': 1e9, 'name': name}]
    return clean(render_chars(merged, toks))


# ============================ ensamblado por pregunta (bandas + figuras)
qinfo = {n: {'stem': [], 'rows': [], 'opts': {}, 'fimgs': [],
             'figs_pool': []}
         for n in range(1, 61)}
owner_state = {n: None for n in range(1, 61)}    # None | ('opt', letra)

q_lines = {}
for ln in body:
    a = assign.get(id(ln))
    if a is not None and a[0] == 'q':
        q_lines.setdefault((a[1], ln['pno']), []).append(ln)

q_figs = {}
for pno, figs in page_figs.items():
    for fg in figs:
        r = fg['rect']
        cy = (r.y0 + r.y1) / 2
        rn = region_at(pno, cy)
        if rn is not None:
            q_figs.setdefault('p%d' % rn, []).append(
                {'pno': pno, 'rect': fitz.Rect(r), 'cy': cy, 'fig': fg})
            continue
        own = None
        for (mp, my, mn) in marks:
            if (mp, my) <= (pno, cy + 3):
                own = mn
            else:
                break
        if own is None:
            print('[fig sin dueno] p%d [%6.1f %6.1f %6.1f %6.1f]'
                  % (pno + 1, r.x0, r.y0, r.x1, r.y1))
            continue
        q_figs.setdefault(own, []).append(
            {'pno': pno, 'rect': fitz.Rect(r), 'cy': cy, 'fig': fg})


def xover(b, x0, x1):
    return min(b['x1'], x1) - max(b['x0'], x0)


for (n, pno) in sorted(q_lines):
    if os.environ.get('DBG_STEMS') and n <= 4:
        print('DBG q_lines Q%d p%d: %d lineas' % (n, pno,
                                                  len(q_lines[(n, pno)])))
    info = qinfo[n]
    chars = [c for ln in q_lines[(n, pno)] for c in ln['chars']
             if id(c) not in fig_of_char]
    figs = sorted([f for f in q_figs.get(n, []) if f['pno'] == pno],
                  key=lambda f: f['cy'])
    bands = make_bands(chars)
    for b in bands:
        b['labels'] = find_labels(b)
    if os.environ.get('DBG_STEMS') and n <= 4:
        for b in bands:
            print('   banda oy%6.1f nsolid%2d sat%s lab%s | %r' % (
                b['oy'], b['nsolid'], b.get('is_sat', False),
                [l['letter'] for l in b['labels']],
                ''.join(c['c'] for c in b['chars'])[:45]))
    rows = []
    for b in bands:
        if not b['labels']:
            continue
        lbs = sorted(b['labels'], key=lambda l: l['x0'])
        opts = []
        for k, lb in enumerate(lbs):
            ox0 = lb['x1'] - 0.5
            ox1 = lbs[k + 1]['x0'] - 2 if k + 1 < len(lbs) else 545.0
            opts.append({'letter': lb['letter'], 'x0': ox0, 'x1': ox1,
                         'pno': pno, 'row_oy': b['oy'], 'band': b,
                         'cont': [], 'cont_toks': [], 'quad': None})
        rows.append({'oy': b['oy'], 'pno': pno, 'opts': opts})
    for row in rows:
        info['rows'].append(row)
        for o in row['opts']:
            info['opts'].setdefault(o['letter'], o)
    # --- figuras inline: token en su banda (|dy| <= 15 y solape x)
    toks_free = []
    for f in figs:
        if not f['fig']['inline']:
            info['figs_pool'].append(f)
            continue
        best, bov = None, -1e9
        for b in bands:
            if abs(b['oy'] - f['cy']) <= 15:
                ov = xover(b, f['rect'].x0 - 4, f['rect'].x1 + 4)
                if ov > bov:
                    bov, best = ov, b
        if best is not None and bov > 0:
            mcount[n] += 1
            name = 'q%02d_m%d.png' % (n, mcount[n])
            crop_chars(pno, f['fig']['chars'], name, extra_rect=f['rect'])
            best['toks'].append({'x': f['rect'].x0, 'name': name})
        else:
            mcount[n] += 1
            name = 'q%02d_m%d.png' % (n, mcount[n])
            crop_chars(pno, f['fig']['chars'], name, extra_rect=f['rect'])
            toks_free.append({'y': f['rect'].y0 - 0.5, 'name': name})
    # --- bandas restantes: continuacion de opcion o stem
    page_events = []
    owner = owner_state[n]
    for b in sorted(bands, key=lambda b: b['oy']):
        if b['labels'] or b.get('is_sat'):
            continue
        target = None
        if rows:
            first, last = rows[0], rows[-1]
            if b['oy'] < first['oy'] - 1e-9:
                if owner is not None and owner[0] == 'opt':
                    target = info['opts'][owner[1]]
            else:
                src = last
                if b['oy'] < last['oy'] - 1e-9:
                    nxt = next((r for r in rows
                                if r['oy'] > b['oy'] + 1e-9), None)
                    if nxt is not None and nxt['oy'] - b['oy'] <= 15:
                        src = nxt
                    else:
                        prevr = [r for r in rows if r['oy'] < b['oy'] - 1e-9]
                        src = prevr[-1] if prevr else last
                dx, bo = -1e9, None
                for o in src['opts']:
                    v = xover(b, o['x0'], o['x1'])
                    if v > dx:
                        dx, bo = v, o
                target = bo if dx > 0 else None
        elif owner is not None and owner[0] == 'opt':
            target = info['opts'][owner[1]]
        if target is not None:
            target['cont'].append(b)
            owner = ('opt', target['letter'])
        else:
            info['stem'].append((pno, 'band', b))
            owner = None
        page_events.append((b['oy'], owner))
    for t in sorted(toks_free, key=lambda t: t['y']):
        if owner is not None and owner[0] == 'opt':
            o = info['opts'][owner[1]]
            if t['y'] > o['row_oy'] - 1:
                o['cont_toks'].append(t)
                owner = ('opt', owner[1])
                page_events.append((t['y'], owner))
                continue
        info['stem'].append((pno, 'tok', t))
        owner = None
        page_events.append((t['y'], owner))
    owner_state[n] = max(page_events, key=lambda t: t[0])[1] \
        if page_events else owner

# -------------------- post-pass: figuras grandes y opciones 100% raster
if os.environ.get('DBG_STEMS'):
    for n in range(1, 8):
        print('DBG Q%d: stem=%d rows=%d opts=%s fpool=%d' % (
            n, len(qinfo[n]['stem']), len(qinfo[n]['rows']),
            sorted(qinfo[n]['opts']), len(qinfo[n]['figs_pool'])))
        for (pno, kind, obj) in qinfo[n]['stem'][:6]:
            if kind == 'band':
                print('    band p%d oy%.1f x[%6.1f,%6.1f] %r' % (
                    pno, obj['oy'], obj['x0'], obj['x1'],
                    ''.join(c['c'] for c in obj['chars'])[:50]))
            else:
                print('    tok  p%d %r' % (pno, obj))
for n in range(1, 61):
    info = qinfo[n]
    pool = sorted(info['figs_pool'], key=lambda f: (f['pno'], f['cy']))
    if not info['opts'] and len(pool) == 1:
        r = pool[0]['rect']
        if r.width > 120 and r.height > 80:
            # opciones 100% raster (P27): division 2x2 por puntos medios
            xm, ym = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
            quads = [('A', fitz.Rect(r.x0, r.y0, xm, ym)),
                     ('B', fitz.Rect(xm, r.y0, r.x1, ym)),
                     ('C', fitz.Rect(r.x0, ym, xm, r.y1)),
                     ('D', fitz.Rect(xm, ym, r.x1, r.y1))]
            for letter, q in quads:
                mcount[n] += 1
                name = 'q%02d_m%d.png' % (n, mcount[n])
                crop_zone(pool[0]['pno'], q, name)
                info['opts'][letter] = {
                    'letter': letter, 'quad': name, 'cont': [],
                    'cont_toks': [], 'band': None, 'x0': 0, 'x1': 0,
                    'row_oy': 0, 'pno': pool[0]['pno']}
            pool = []
    for f in pool:
        fcount[n] += 1
        name = 'q%02d_f%d.png' % (n, fcount[n])
        crop_zone(f['pno'], f['rect'], name)
        info['fimgs'].append(name)

# --------------------------------------------------------------- stems
stems = {}
for n in range(1, 61):
    parts = []
    for (pno, kind, obj) in sorted(qinfo[n]['stem'],
                                   key=lambda t: (t[0], t[2].get(
                                       'oy', t[2].get('y', 0)))):
        if kind == 'band':
            parts.append(render_full(n, pno, obj))
        else:
            parts.append('[[img:%s]]' % obj['name'])
    stems[n] = ' '.join(p for p in parts if p)

# -------------------------------------------------------------- opciones
options = {}
for n in range(1, 61):
    options[n] = {}
    for letter in 'ABCD':
        o = qinfo[n]['opts'].get(letter)
        if o is None:
            options[n][letter] = ''
            continue
        if o.get('quad'):
            options[n][letter] = '[[img:%s]]' % o['quad']
            continue
        items = []
        b = o['band']
        base_chars = [c for c in b['chars'] if c['bbox'][0] >= o['x0'] - 0.5]
        base_toks = [t for t in b['toks'] if t['x'] >= o['x0'] - 4]
        bb = {'chars': base_chars, 'oy': b['oy'], 'x0': b['x0'],
              'x1': b['x1'], 'toks': base_toks, 'sats': b['sats']}
        items.append((o['pno'], 'band', bb))
        for cb in o['cont']:
            ctoks = [t for t in cb['toks'] if t['x'] >= o['x0'] - 4]
            items.append((cb.get('pno', o['pno']), 'band',
                          {'chars': cb['chars'], 'oy': cb['oy'],
                           'x0': cb['x0'], 'x1': cb['x1'], 'toks': ctoks,
                           'sats': cb['sats']}))
        for t in o['cont_toks']:
            items.append((o['pno'], 'tok', t))
        items.sort(key=lambda it: (it[0], it[2]['oy'] if it[1] == 'band'
                                   else it[2].get('y', it[2]['oy'])))
        parts = []
        for (pno2, kind, obj) in items:
            if kind == 'band':
                parts.append(render_full(n, pno2, obj))
            else:
                parts.append('[[img:%s]]' % obj['name'])
        options[n][letter] = ' '.join(p for p in parts if p)

# --------------------------------------------------------------- pasajes
passage_html = {}
for r in passage_regions:
    n = r['n']
    items = []
    for ln in body:
        a = assign.get(id(ln))
        if a is not None and a[0] == 'texto' and a[1] == n:
            items.append((ln['pno'], ln['y0'], 0,
                          ' '.join(c['c'] for c in ln['chars'])))
    for f in q_figs.get('p%d' % n, []):
        pcount[n] = pcount.get(n, 0) + 1
        name = 'p%d_f%d.png' % (n, pcount[n])
        crop_zone(f['pno'], f['rect'], name)
        items.append((f['pno'], f['cy'], 1, '[[img:%s]]' % name))
    items.sort(key=lambda t: (t[0], t[1], t[2]))
    parts = [clean(t[3]) if not t[3].startswith('[[img:') else t[3]
             for t in items]
    passage_html[n] = '\n\n'.join(p for p in parts if p)

# ----------------------------------------------------------------- claves
ktxt = doc[KEYS_P].get_text()
pairs = re.findall(r'(?m)^\s*(\d{1,2})\s*\n\s*([a-dA-D])\s*$', ktxt)
answers = {int(num): le.upper() for num, le in pairs}
print('claves:', len(answers))

# ------------------------------------------------- pasaje de cada pregunta
passage_of = {}
last_texto = None
for (pno, y, tag) in events:
    if tag[0] == 'texto':
        last_texto = tag[1]
    elif tag[0] == 'q':
        passage_of[tag[1]] = last_texto

# ------------------------------------------------------------- banco final
GARB = re.compile(r'[\u0100-\u024f\u0400-\u052f\u0750-\u075f\u0d00-\u0d7f'
                  r'\u0d45]')
LABEL_RE = re.compile(r'(?:^|\s)[a-d]\)')
bank = {'year': 2025,
        'title': 'Simulacro Oficial ENP Beca 18 — Convocatoria 2025',
        'duration_min': 120,
        'sections': [
            {'id': 'matematica', 'label': 'Competencia Matemática',
             'from': 1, 'to': 30},
            {'id': 'lectura', 'label': 'Competencia Lectora', 'from': 31,
             'to': 60}],
        'passages': [{'id': r['n'],
                      'title': passage_title.get(r['n']),
                      'html': passage_html[r['n']]}
                     for r in passage_regions],
        'questions': []}
flags = []
for n in range(1, 61):
    q = {'id': n, 'stem': stems[n],
         'options': [options[n][L] for L in 'ABCD'],
         'answer': answers.get(n, ''),
         'section': 'matematica' if n <= 30 else 'lectura'}
    if passage_of.get(n):
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

for p in bank['passages']:
    print('pasaje %d (%s): %d chars%s' % (
        p['id'], (p['title'] or '')[:40], len(p['html']),
        '  [CORTO]' if len(p['html']) < 300 else ''))

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
        print('     %s) %s' % ('abcd'[k], o[:64]))
