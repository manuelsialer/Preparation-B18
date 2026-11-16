# -*- coding: utf-8 -*-
"""OCR opcional (rapidocr-onnxruntime) para escaneos sin capa de texto.

El motor se instancia de forma perezosa: importar este módulo no obliga a
tener rapidocr instalado si no se usa.
"""


class Ocr:
    """Envoltura fina de RapidOCR."""

    def __init__(self):
        from rapidocr_onnxruntime import RapidOCR  # import perezoso
        self._eng = RapidOCR()

    def read(self, image):
        """Ejecuta OCR sobre una imagen (ruta o ndarray).

        Devuelve la lista de items [box, texto, score] (puede ser vacía).
        """
        res, _ = self._eng(image)
        return res or []

    def text(self, image, join='\n'):
        return join.join(it[1] for it in self.read(image))


def ocr_region(page, rect, zoom=4, engine=None):
    """OCR de una región de una página (página PyMuPDF + fitz.Rect)."""
    import fitz
    import numpy as np

    eng = engine or Ocr()
    r = fitz.Rect(rect)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=r)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    return eng.read(img)
