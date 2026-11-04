#!/usr/bin/env python3
"""
tikz_to_svg.py

Convierte un archivo .tex que contiene código TikZ/pgfplots/tkz-euclide
en un archivo SVG vectorial, listo para incrustar en Markdown/MyST con {figure}.

Flujo:
    1. Compila el .tex a PDF con pdflatex.
    2. Convierte el PDF a SVG con dvisvgm (o pdf2svg como fallback).
    3. Limpia archivos temporales.

Uso:
    python scratch/tikz_to_svg.py assets/trigonometria/circulo_trigonometrico.tex
    python scratch/tikz_to_svg.py assets/trigonometria/triangulo_30_60_90.tex

Requisitos del sistema:
    - Una distribución de LaTeX instalada (MiKTeX, TeX Live o MacTeX).
    - pdflatex y dvisvgm disponibles en el PATH.

Autor: Material Preuniversitario Beca 18
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd, cwd=None, check=True):
    """Ejecuta un comando y muestra su salida."""
    print(f"[RUN] {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if check and result.returncode != 0:
        raise RuntimeError(f"Comando falló con código {result.returncode}: {' '.join(cmd)}")
    return result


def tex_to_svg(tex_path: Path, output_dir: Path | None = None, keep_temp: bool = False):
    """
    Convierte un archivo .tex con TikZ a SVG.

    Params
    ------
    tex_path : Path
        Ruta al archivo .tex de entrada.
    output_dir : Path | None
        Directorio donde guardar el .svg. Si es None, se usa el mismo del .tex.
    keep_temp : bool
        Si True, conserva los archivos intermedios (.aux, .log, .pdf).
    """
    tex_path = Path(tex_path).resolve()
    if not tex_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {tex_path}")

    if output_dir is None:
        output_dir = tex_path.parent
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    stem = tex_path.stem
    svg_path = output_dir / f"{stem}.svg"

    # Directorio temporal para compilar (evita ensuciar el repo con .aux/.log)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        tmp_tex = tmpdir / tex_path.name

        # Copiar el .tex al directorio temporal
        tmp_tex.write_text(tex_path.read_text(encoding="utf-8"), encoding="utf-8")

        # 1. Compilar a PDF con pdflatex
        print(f"\n=== Compilando {tex_path.name} a PDF ===")
        run([
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory", str(tmpdir),
            str(tmp_tex),
        ])

        pdf_path = tmpdir / f"{stem}.pdf"
        if not pdf_path.exists():
            raise FileNotFoundError(
                f"No se generó el PDF esperado: {pdf_path}. "
                "Revisa errores de compilación arriba."
            )

        # 2. Convertir PDF a SVG con dvisvgm (primera opción) o pdf2svg (fallback)
        print(f"\n=== Convirtiendo {pdf_path.name} a SVG ===")

        # Intentar dvisvgm (más robusto con TikZ)
        try:
            run([
                "dvisvgm",
                "--pdf",
                str(pdf_path),
                "-o", str(svg_path),
            ])
            print(f"\n[OK] SVG generado con dvisvgm: {svg_path}")
        except (FileNotFoundError, RuntimeError):
            print("[WARN] dvisvgm no disponible, intentando pdf2svg...")
            try:
                run([
                    "pdf2svg",
                    str(pdf_path),
                    str(svg_path),
                ])
                print(f"\n[OK] SVG generado con pdf2svg: {svg_path}")
            except (FileNotFoundError, RuntimeError) as e:
                raise RuntimeError(
                    "No se pudo convertir a SVG. Instala dvisvgm o pdf2svg.\n"
                    "Ver: https://github.com/gkiagia/dvisvgm  o  https://github.com/dawbarton/pdf2svg"
                ) from e

    # Limpiar temporales si no se pidió conservar
    if not keep_temp:
        for ext in [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"]:
            f = output_dir / f"{stem}{ext}"
            if f.exists():
                f.unlink()

    print(f"\n[FINAL] SVG listo: {svg_path}")
    return svg_path


def main():
    parser = argparse.ArgumentParser(
        description="Convierte archivos .tex con TikZ a SVG vectorial para Markdown/MyST."
    )
    parser.add_argument(
        "tex",
        nargs="+",
        type=Path,
        help="Uno o más archivos .tex de entrada.",
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=None,
        help="Directorio de salida para los SVG (por defecto: mismo que el .tex).",
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Conserva archivos intermedios (.pdf, .aux, .log) para depuración.",
    )
    args = parser.parse_args()

    for tex_file in args.tex:
        try:
            tex_to_svg(tex_file, output_dir=args.output_dir, keep_temp=args.keep_temp)
        except Exception as exc:
            print(f"[ERROR] {tex_file}: {exc}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
