# Pipeline de simulacros (tools/)

Herramientas para construir los **bancos JSON** que alimentan los simulacros
interactivos del libro. Cada banco vive en `_static/simulacros/banks/<año>.json`
y sus figuras en `_static/simulacros/img/<año>/`.

## Estructura

```
tools/
├── b18/                 paquete reutilizable (núcleo del pipeline)
│   ├── console.py       consola UTF-8 en Windows
│   ├── pdfio.py         PDF: figuras, líneas, texto por columnas/regiones
│   ├── textutil.py      limpieza y parseo de preguntas/opciones
│   ├── crop.py          recortes de figuras/fórmulas a PNG
│   ├── keys.py          extracción de tablas de claves oficiales
│   ├── ocr.py           OCR opcional (rapidocr) para escaneos sin texto
│   └── bank.py          esquema, escritura y validación de bancos
├── exams/               extractores por examen (fuente de cada banco)
│   ├── build_2018.py    + fix_2023.py (parches de calidad 2023)
│   ├── build_2023.py
│   └── build_2024.py
├── qa_bank.py           QA rápido de un banco
├── viewpng.py           vista previa de un PNG en la consola (ASCII)
├── keygrid.py           extracción de grillas de claves por región
├── col_extract.py       volcado de texto por columnas de una página
├── ascii2.py            volcado ASCII de una página del PDF
├── audit_katex.py       auditoría de sintaxis LaTeX en el contenido
└── tikz_to_svg.py       conversión de diagramas TikZ a SVG (assets)
```

## Uso

Los extractores se ejecutan **desde la raíz del repositorio** (leen `temarios/`
y escriben en `_static/` y `scratch/exams/banks/`):

```bash
python tools/exams/build_2018.py            # banco 2018 (Reconstruido)
python tools/exams/build_2023.py            # banco 2023 (paso 1)
python tools/exams/fix_2023.py              # banco 2023 (paso 2: parches) -> publica
python tools/exams/build_2024.py            # banco 2024
```

QA de un banco ya publicado:

```bash
python -c "import sys; sys.path.insert(0,'tools'); import b18; \
print(b18.bank.qa_report(b18.bank.load_bank('_static/simulacros/banks/2023.json')))"
```

## Esquema del banco

```jsonc
{
  "year": 2023,
  "title": "Simulacro Oficial ENP Beca 18 — Convocatoria 2023",
  "duration_min": 120,
  "sections": [{"id": "matematica", "label": "Razonamiento Matemático", "from": 1, "to": 30}],
  "passages": [{"id": 1, "title": null, "html": "…"}],
  "questions": [{
    "id": 1,
    "stem": "Enunciado con fórmulas en LaTeX: \\(x^2+1\\)",
    "options": ["A", "B", "C", "D"],
    "answer": "C",
    "section": "matematica",
    "passage": 1,                  // opcional, 1-based sobre "passages"
    "images": ["q01_f1.png"],      // opcional, figuras tras el enunciado
    "explain": "…"                 // opcional, explicación de la clave
  }]
}
```

- Las figuras de una pregunta se listan en `images` (se pintan tras el enunciado).
- Dentro de `stem`, `options`, `passages[].html` y `explain` puede aparecer el
  token `[[img:archivo.png]]`, que el motor reemplaza por la imagen inline.
- **Fórmulas**: usar LaTeX entre `\(…\)` (inline) o `\[…\]` (bloque). **No** usar
  `$…$`: el símbolo `$` se reserva para la moneda (soles) en los enunciados.

## Notas

- `scratch/` es desechable: contiene exploraciones de un solo uso. El código
  reproducible vive aquí, en `tools/`.
- La reproducción exacta de un banco puede depender de la versión de PyMuPDF y
  de la capa de texto del PDF original; los bancos publicados en
  `_static/simulacros/banks/` son la fuente de verdad.
