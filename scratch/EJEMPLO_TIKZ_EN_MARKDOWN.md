# Ejemplo: Cómo se ven las figuras TikZ en el sitio Markdown

Una vez que compiles los archivos `.tex` a `.svg` con el script `scratch/tikz_to_svg.py`,
los referencias en tu `.md` exactamente igual que haces ahora con las imágenes,
pero el origen es código TikZ vectorial, no un PNG/JPG.

## 1. Generar los SVG (una sola vez por figura)

Desde la raíz del proyecto:

```powershell
# Circunferencia trigonométrica
python scratch/tikz_to_svg.py assets/trigonometria/circulo_trigonometrico.tex

# Triángulo rectángulo notable
python scratch/tikz_to_svg.py assets/trigonometria/triangulo_30_60_90.tex
```

Esto produce:
- `assets/trigonometria/circulo_trigonometrico.svg`
- `assets/trigonometria/triangulo_30_60_90.svg`

## 2. Incrustar en tu archivo `.md`

Usa la directiva `{figure}` de MyST (la misma que ya usas):

```markdown
## Circunferencia Goniométrica

```{figure} ../../assets/trigonometria/circulo_trigonometrico.svg
---
width: 85%
align: center
alt: Circunferencia goniométrica con seno, coseno y ángulo θ
---
*Figura vectorial generada con TikZ. Muestra la relación $(x,y) = (\cos\theta,\ \sin\theta)$ sobre la circunferencia unitaria.*
```

## Triángulo Rectángulo Notables 30°-60°-90°

```{figure} ../../assets/trigonometria/triangulo_30_60_90.svg
---
width: 80%
align: center
alt: Triángulo rectángulo notable con lados k, k√3 y 2k
---
*Figura vectorial generada con TikZ. Proporciones exactas del triángulo $30^\circ-60^\circ-90^\circ$.*
```
```

## 3. Resultado en el sitio web

- En **HTML**: el navegador muestra el SVG directamente (nítido al hacer zoom, sin pixelar).
- En **PDF** (si exportas): el SVG se incrusta como gráfico vectorial.
- **No hay imágenes `.png` ni `.jpg` sueltas** que mantener.

---

## Requisitos en Windows

Para que `tikz_to_svg.py` funcione necesitas instalar:

1. **MiKTeX** (recomendado en Windows): https://miktex.org/download
   - Durante la instalación, marca la opción para agregar MiKTeX al PATH.
2. Verifica en PowerShell:
   ```powershell
   pdflatex --version
   dvisvgm --version
   ```

Si `dvisvgm` no viene con tu MiKTeX, instálalo desde el administrador de paquetes de MiKTeX o usa `pdf2svg` como alternativa (el script ya lo contempla como fallback).

---

## Estándar del proyecto

Este flujo cumple con lo definido en `.agents/rules/formato_latex.md`:
- ✅ TikZ / tkz-euclide / pgfplots para figuras geométricas.
- ✅ Compilación nativa a SVG vectorial.
- ✅ Archivos guardados en `assets/<materia>/`.
- ✅ Referenciados con `{figure}` en Markdown.
- ✅ Sin usar Mermaid ni imágenes de baja resolución.
