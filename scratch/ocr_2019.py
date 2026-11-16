"""OCR paralelo del examen Beca 18 2019 (PDF solo-imagenes).

El PDF no tiene capa de texto: el contenido son capturas (tiles) en dos
columnas. Recorre los tiles en orden de lectura (pagina -> columna izquierda
de arriba a abajo -> columna derecha) y aplica OCR (rapidocr-onnxruntime) en
paralelo, volcando el texto a scratch/ocr2019_dump.txt con un marcador por
tile para reconstruir las preguntas.
"""
import io
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import fitz
import numpy as np
from PIL import Image, ImageOps

PDF = r'temarios\2027\EXAMEN BECA 18 - 2019.docx.pdf'
OUT = r'scratch\ocr2019_dump.txt'
SCALE = 2

_ENGINE = None
_DOC = None


def _init():
    global _ENGINE, _DOC
    from rapidocr_onnxruntime import RapidOCR
    _ENGINE = RapidOCR()
    _DOC = fitz.open(PDF)


def _ocr(job):
    tile_no, pno, col, xref, w, h, y0 = job
    pix = fitz.Pixmap(_DOC, xref)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.height, pix.width, pix.n)[..., :3]
    img = Image.fromarray(a).convert('L')
    img = ImageOps.autocontrast(img)
    img = img.resize((img.width * SCALE, img.height * SCALE), Image.LANCZOS)
    res, _ = _ENGINE(np.array(img.convert('RGB')))
    out = ['===== TILE %d  p%d col%s y%.0f (%dx%d) ====='
           % (tile_no, pno + 1, 'LR'[col], y0, w, h)]
    if res:
        for box, txt, score in res:
            out.append('  %s' % txt)
    else:
        out.append('  (sin texto)')
    return tile_no, out


def collect_jobs():
    doc = fitz.open(PDF)
    jobs = []
    meta = []
    tile_no = 0
    for pno in range(doc.page_count):
        infos = doc[pno].get_image_info(xrefs=True)
        tiles = []
        for info in infos:
            r = fitz.Rect(info['bbox'])
            tiles.append((0 if r.x0 < 300 else 1, r.y0, info))
        tiles.sort(key=lambda t: (t[0], t[1]))
        meta.append((pno, len(tiles)))
        for col, y0, info in tiles:
            tile_no += 1
            jobs.append((tile_no, pno, col, info['xref'], info['width'],
                         info['height'], y0))
    doc.close()
    return jobs, meta


def main():
    jobs, meta = collect_jobs()
    print('tiles:', len(jobs))
    results = {}
    with ProcessPoolExecutor(max_workers=6, initializer=_init) as ex:
        for tile_no, out in ex.map(_ocr, jobs):
            results[tile_no] = out
    lines = []
    idx = 0
    for pno, ntiles in meta:
        lines.append('########## PAGINA %d (%d tiles) ##########' % (pno + 1, ntiles))
        for _ in range(ntiles):
            idx += 1
            lines.extend(results[idx])
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('salida:', OUT, 'lineas:', len(lines))


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
