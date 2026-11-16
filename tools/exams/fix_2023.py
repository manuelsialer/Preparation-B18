"""Parches de calidad para scratch/exams/banks/2023.json (formato hibrido).

Limpieza mecanica + reconstruccion de formulas rotas:
  * elimina caracteres de control (\x03...) y sangrado de etiquetas de figura
  * fracciones apiladas "3 4" -> "3/4"
  * superindices Unicode (x2 -> x², cm3 -> cm³)
  * simbolo pi (S de Symbol) y signos perdidos
  * formula de Q15, ecuacion de Q18 y expresion de Q14 -> imagen recortada
    (token [[img:archivo.png]] que el motor reemplaza por <img>)
"""
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from b18 import bank as b18bank, console, crop as b18crop  # noqa: E402
from b18 import pdfio  # noqa: E402

console.setup_console()

BANK = r'scratch\exams\banks\2023.json'
PUB = r'_static\simulacros\banks\2023.json'
PDF = r'temarios\2027\examen-1-beca-18-convocatoria-2023.pdf'
IMG_DIR = os.path.join('_static', 'simulacros', 'img', '2023')

b = b18bank.load_bank(BANK)
qs = {q['id']: q for q in b['questions']}

# ---------- 1. recortes de formulas irrecuperables ----------
os.makedirs(IMG_DIR, exist_ok=True)
doc = pdfio.open_pdf(PDF)
CROPS = [
    (14, 'q14_expr.png', (118, 114, 276, 158)),    # E = fraccion compuesta
    (15, 'q15_fx.png',   (193, 432, 308, 456)),    # f(x) = x2 - 6x + 10
    (15, 'q15_tbl.png',  (150, 502, 252, 548)),    # tabla x / f(x)
    (15, 'q15_dom.png',  (83, 455, 116, 478)),     # dominio garbado
    (18, 'q18_sys.png',  (148, 100, 240, 143)),    # sistema de ecuaciones
    (18, 'q18_expr.png', (193, 145, 286, 172)),    # expresion a evaluar
]
# pagina por numero de pregunta (mismo metodo que el builder)
qpage = {}
for pno in range(1, doc.page_count - 1):
    for blk in doc[pno].get_text('dict')['blocks']:
        if blk.get('type') != 0:
            continue
        for ln in blk['lines']:
            t = ''.join(s['text'] for s in ln['spans']).strip()
            m = re.fullmatch(r'(\d{1,2})\.', t)
            if m and int(m.group(1)) not in qpage:
                qpage[int(m.group(1))] = pno
for qid, name, rect in CROPS:
    b18crop.crop_box(doc, qpage[qid] + 1, rect, os.path.join(IMG_DIR, name), zoom=3)
    print('crop', name)

# ---------- 2. limpieza mecanica ----------
CTRL = re.compile(r'[\x00-\x08\x0b-\x1f\x7f]')
LABEL = re.compile(r'(?<![\w])([A-Z])(?=\s|$)')   # etiqueta suelta de figura


def strip_labels(text):
    """Corta en la primera letra sola tipo 'A' seguida de tokens cortos (rótulos de figura)."""
    toks = text.split()
    for i, t in enumerate(toks):
        if re.fullmatch(r'[A-Z]', t) and i + 1 < len(toks) and len(toks[i + 1]) <= 3:
            return ' '.join(toks[:i]).strip()
    return text


def fix_text(text, is_option=True):
    text = CTRL.sub('', text)
    # sangrado de tabla/figura: corta en el primer caracter mojibake
    text = re.split(r'[\u0700-\u0d7f\u0f00-\u0fff]', text)[0]
    if is_option:
        text = strip_labels(text)
    # fraccion apilada: "3 4" / "2,400 49" -> "3/4"
    text = text.strip()
    m = re.fullmatch(r'(\d+(?:[.,]\d+)?)\s+(\d+)', text)
    if m:
        num = m.group(1).replace(',', '') if ',' in m.group(1) and len(m.group(1).replace(',', '')) > 3 else m.group(1)
        text = f'{num}/{m.group(2)}'
    # pi de Symbol: "600S cm3" -> "600π cm³"
    text = re.sub(r'(\d(?:[.,]\d)?)S\b', r'\1π', text)
    # superindices simples
    text = text.replace('cm3', 'cm³').replace('cm2', 'cm²')
    text = re.sub(r'\bx2\b', 'x²', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


for q in b['questions']:
    q['stem'] = fix_text(q['stem'], is_option=False)
    q['options'] = [fix_text(o) for o in q['options']]

# ---------- 3. reconstrucciones puntuales ----------
qs[11]['stem'] = ('Dados los polinomios p(x) = x⁶ + 2x⁴ + 2x² + 1 y '
                  'q(x) = x⁴ + x³ + 2x² + x + 1, calcule el cociente al dividir p(x) entre q(x).')
qs[11]['options'] = ['x² + x + 1', 'x² – x – 1', 'x² + x – 1', 'x² – x + 1']

qs[14]['stem'] = 'Simplificar la expresión: [[img:q14_expr.png]]'
qs[14]['options'] = ['16/15', '4/5', '2/15', '8/15']

qs[15]['stem'] = ('El número de unidades de un artículo A, que los productores están dispuestos a proveer '
                  'al mercado de abastos, cuando el precio de este artículo es x soles, está dada por la '
                  'función [[img:q15_fx.png]] [[img:q15_dom.png]]. En la siguiente tabla se muestran '
                  'algunos valores que toma la función [[img:q15_tbl.png]]. Si el precio del artículo A '
                  'fuese 35 soles ¿con cuántas unidades del artículo A, los productores estarían '
                  'dispuestos a proveer al mercado de abastos?')

qs[15]['options'] = ['631', '847', '1025', '1015']

qs[18]['stem'] = ('Si x es solución de la ecuación [[img:q18_sys.png]], entonces el valor de '
                  '[[img:q18_expr.png]]')

qs[19]['stem'] = qs[19]['stem'].replace('26 250 cm3', '26 250 cm³').replace('26 250 cm³', '26 250 cm³')

qs[21]['options'] = ['600π cm³', '562,5π cm³', '500π cm³', '450π cm³']

qs[24]['stem'] = qs[24]['stem'].replace('AC2 – AB2', 'AC² – AB²')
qs[25]['stem'] = qs[25]['stem'].replace('130 m2 de', '130 m² de')

qs[26]['stem'] = qs[26]['stem'].replace('es 2 64 m, S halle', 'es 64π m², halle')
qs[26]['stem'] = re.sub(r'es\s+[\d\s]*64\s*m,\s*S\s*halle', 'es 64π m², halle', qs[26]['stem'])
qs[26]['options'][3] = '8√2 m'

qs[28]['stem'] = (qs[28]['stem'].replace('rectas /1 y / 2', 'rectas ℓ₁ y ℓ₂')
                  .replace('mNBC = 40º, halle mMBA', 'm∠NBC = 40°, halle m∠MBA'))
qs[29]['stem'] = qs[29]['stem'].replace('ABC ( B = 90°)', 'ABC (∠B = 90°)')

# ---------- 4. verificacion ----------
issues = []
for q in b['questions']:
    txt = q['stem'] + ' ' + ' '.join(q['options'])
    if CTRL.search(txt):
        issues.append((q['id'], 'control-char'))
    if re.search(r'[ݔ݂ሺሻൌଶ௫ξ͵ߨ]', txt):
        issues.append((q['id'], 'mojibake'))
    if re.search(r'\s{2,}', txt):
        issues.append((q['id'], 'doble-espacio'))
    if '' in q['options'] or not q['stem']:
        issues.append((q['id'], 'vacio'))

print('preguntas:', len(b['questions']), '| issues:', issues)
b18bank.write_bank(b, BANK)
shutil.copyfile(BANK, PUB)
print('->', BANK, '|', PUB)
