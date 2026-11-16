# -*- coding: utf-8 -*-
"""Paquete b18 — utilidades reutilizables para construir bancos de simulacros.

Extrae el núcleo común de los extractores de exámenes (antes dispersos en
`scratch/`): lectura de PDF, detección de figuras, recortes, OCR, tablas de
claves y esquema/validación de bancos.

Módulos:
    console  — consola UTF-8 y utilidades de impresión
    pdfio    — apertura de PDF, clustering de figuras y texto por columnas
    textutil — limpieza y parseo de texto de examen
    crop     — recortes de figuras y fórmulas a PNG
    keys     — extracción de tablas de claves oficiales
    ocr      — OCR opcional (rapidocr) para escaneos sin capa de texto
    bank     — esquema, construcción, escritura y validación de bancos JSON
"""
from . import console, pdfio, textutil, crop, keys, ocr, bank  # noqa: F401

__all__ = ['console', 'pdfio', 'textutil', 'crop', 'keys', 'ocr', 'bank']

SCHEMA_VERSION = 1
