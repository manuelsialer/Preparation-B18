# Registro Histórico de Errores, Lecciones Aprendidas y Mejoras

Este registro acumula todas las fallas detectadas y las lecciones derivadas durante la evolución del proyecto. **Es de consulta obligatoria antes de iniciar la redacción de cualquier nuevo tema.**

---

## 📋 Bitácora de Lecciones Aprendidas

### [ERR-001] Omisión de Temas Clave en la Adaptación Preliminar
* **Fecha:** 2026-10-19
* **Problema:** El temario adaptado inicial omitió puntos notables del triángulo, función afín, triángulos notables y probabilidad clásica con datos agrupados.
* **Causa Raíz:** Simplificación excesiva al resumir los indicadores del CNEB.
* **Invariante / Regla Aprendida:** Toda traducción debe cruzarse línea por línea con los indicadores oficiales de PRONABEC antes de darla por válida.

---

### [ERR-002] Cantidad Insuficiente de Ejercicios Propuestos
* **Fecha:** 2026-10-19
* **Problema:** La propuesta inicial tenía 5 ejercicios por bloque (15 en total), lo cual era insuficiente para un nivel preuniversitario riguroso.
* **Causa Raíz:** Suposición de formato corto tipo guía rápida.
* **Invariante / Regla Aprendida:** Todo fascículo debe contener **mínimo 45 ejercicios propuestos** divididos estrictamente en 3 bloques de 15 (Básico, Intermedio y Avanzado/Beca 18), con 5 alternativas (A, B, C, D, E) y tabla de claves completa.

---

### [ERR-003] Errores de Renderizado en Fórmulas Matemáticas (LaTeX / Markdown)
* **Fecha:** 2026-10-19
* **Problema:** Algunos renderizadores de Markdown (en VS Code, GitHub o KaTeX) fallaban al interpretar fórmulas matemáticas.
* **Causas Raíz:**
  1. Uso de `\dot{b}` o `\dot{2}` para múltiplos (en MathJax no renderiza bien y causa caracteres rotos).
  2. Espacios en blanco accidentales junto a los delimitadores `$`.
  3. Líneas en blanco dentro de bloques `$$ ... $$` que cortaban el bloque de ecuación.
  4. Uso de la barra vertical `|` dentro de fórmulas en tablas Markdown, lo que desalineaba las columnas.
* **Invariante / Regla Aprendida:**
  * Usar `$k \cdot b$` o `\text{múltiplo de } b` en lugar de `\dot{b}`.
  * Mantener bloques `$$` continuos y sin líneas vacías internas.
  * Usar `\mid` o `\vert` en lugar de `|` cuando se escriben conjuntos dentro de tablas.
  * Ejecutar el script `check_latex.py` antes de cualquier commit.

---

### [ERR-004] Formulario Resumen en Texto Plano ASCII
* **Fecha:** 2026-10-19
* **Problema:** El formulario resumen final se generaba dentro de cajas de código ASCII (`┌───┐`), viéndose plano y poco atractivo en la web.
* **Causa Raíz:** Formato heredado de scripts de consola.
* **Invariante / Regla Aprendida:** El formulario resumen debe redactarse **100% en LaTeX y tablas formateadas**, con fórmulas destacadas, viñetas elegantes y formato listo para imprenta o lectura web interactiva.

---

### [ERR-005] Estructura para GitHub Pages sin HTML Manual
* **Fecha:** 2026-10-19
* **Problema:** Duda sobre si se requería programar HTML para publicar en GitHub Pages.
* **Invariante / Regla Aprendida:** Utilizar la arquitectura de **Jupyter Book** (`_config.yml`, `_toc.yml`, `requirements.txt` y `.github/workflows/deploy.yml`). Los contenidos se mantienen en `.md` puro y GitHub Actions genera el HTML de forma automática.

### `[ERR-006]` Fallo en Action `deploy-book` por falta de `repository:` y versión de build
* **Fecha:** 2026-10-19
* **Problema:** GitHub Actions falló con `ENOENT: no such file or directory, scandir '_build/html'` porque `jupyter-book build .` falló internamente con `ValueError: To use 'repository' buttons, you must specify the repository URL`.
* **Invariante / Regla Aprendida:**
  1. En `_config.yml`, si se activan `use_repository_button` o `use_issues_button`, es OBLIGATORIO definir el bloque `repository: url: ...` apuntando al repositorio de GitHub.
  2. Fijar `jupyter-book~=0.15.1` en `requirements.txt`.
  3. En GitHub Pages: usar el workflow oficial de GitHub Actions (`actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`) y en la configuración del repositorio (**Settings -> Pages -> Build and deployment -> Source**) seleccionar **GitHub Actions**.

### `[ERR-007]` Fórmulas y Fracciones no renderizadas por sangría (Markdown Code Block) e Índices manuales rotos
* **Fecha:** 2026-10-19
* **Problema:** En GitHub Pages, las ecuaciones como `$$E = \dots$$` o `\begin{array}` y las opciones `A) $\frac{132}{65}$` se mostraban como bloques de código gris crudo (`<pre><code>`) o texto sin procesar por MathJax. Asimismo, los índices manuales tenían anclas rotas.
* **Invariante / Regla Aprendida:**
  1. **Prohibido indentar bloques `$$` o alternativas con espacios:** En CommonMark/MyST, si un bloque `$$` o alternativas tienen 3 o más espacios de sangría (por estar debajo de una lista `1.` o `2.`), el motor los convierte en un bloque de código literal (`<pre><code>`), impidiendo que MathJax los compile. Todo bloque `$$` y toda alternativa `A) ...` debe colocarse **a columna 0 (sin sangría)**, con una línea en blanco antes y después del bloque matemático.
  2. **No usar `@{\quad}` en `array`:** MathJax no soporta expresiones `@` en especificaciones de columna por defecto; usar alineaciones estándar `{rl}` o `\begin{aligned}`.
  3. **Eliminar índices manuales de Markdown:** Jupyter Book genera de forma nativa e interactiva el índice lateral derecho de la página. Los índices manuales en markdown generan advertencias de anclas no encontradas y enlaces rotos.
  4. **Denominación:** Usar formalmente el término **Tema** en lugar de "Fascículo".

### `[ERR-008]` Párrafos y notas explicativas con 4+ espacios convertidos en bloques de código
* **Fecha:** 2026-10-19
* **Problema:** Párrafos de notas y sub-ítems explicativos dentro de la solución (ej. `     *(Por teorema de Cardano-Vieta...)*`) tenían 4 o 5 espacios de sangría. En CommonMark, 4 o más espacios definen automáticamente un bloque de código literal (`<pre><code>`), lo cual desactiva el renderizado de MathJax y muestra fórmulas en texto plano crudo con `$`.
* **Invariante / Regla Aprendida:**
  * **Toda línea de texto, nota explicativa, fórmula o alternativa DEBE iniciar en columna 0 (sin sangría de 4 o más espacios).**
  * Para listas con viñetas, usar únicamente `* ` o `  * ` en columna 0 o sangría mínima de 2 espacios.
  * Ninguna línea en todo el markdown debe tener 4 espacios iniciales a menos que se desee explícitamente un bloque de código monospace sin matemáticas.

---

### `[ERR-009]` Fórmulas `$$` pegadas a listas o párrafos sin línea en blanco (desincronización de MathJax)
* **Fecha:** 2026-10-19
* **Problema:** Ecuaciones como `$$I = \frac{C \cdot r \cdot t}{1\,200}$$` se rompían y mostraban signos `$` sueltos y texto desconfigurado en la web.
* **Causa Raíz:** En CommonMark/MyST, si un bloque display math `$$` se coloca inmediatamente en la línea siguiente a un ítem numerado (ej. `2. Aplicar fórmula:\n$$...$$`) o texto sin línea en blanco intermedia, el motor lo procesa como texto inline dentro del ítem `<li><p>`, interpretando el `$$` como dos tokens individuales `$`. Esto rompe el árbol DOM y corrompe MathJax en toda la página.
* **Invariante / Regla Aprendida:**
  1. En las soluciones paso a paso, **NO usar listas numeradas `1. `, `2. `**. Usar párrafos independientes en negrita a columna 0: `**Paso 1:**`, `**Paso 2:**`, `**Paso 3:**`.
  2. **REGLA DE ORO DE ESPACIADO:** Todo bloque de ecuación `$$` debe tener estrictamente **una línea en blanco antes** y **una línea en blanco después**.
  3. Si hay dos fórmulas consecutivas, **debe existir una línea en blanco entre ellas**.

---

### `[ERR-010]` Fallas de MathJax por `\begin{array}` en el Formulario Resumen y Soluciones
* **Fecha:** 2026-10-19
* **Problema:** En el Formulario Resumen y en ejercicios con sumas alineadas, el navegador mostraba código LaTeX en bruto como `$$\begin{array}{rl} 1\text{ h} & 45\text{ min} ... \end{array}$$`.
* **Causa Raíz:** Sphinx encapsula bloques matemáticos con saltos en `\begin{split}`, y al anidar un `\begin{array}` con `\hline` o alineaciones complejas, MathJax 3 falla en el navegador.
* **Invariante / Regla Aprendida:**
  1. En la sección `## 7. Formulario Resumen`, **PROHIBIDO usar `\begin{array}`**. Se deben usar siempre **Tablas Markdown estándar** (`| Concepto | Expresión Matemática |`) con matemáticas inline `$ ... $`. Las tablas Markdown son 100% nativas en HTML, responsive y totalmente inmunes a fallas de renderizado.
  2. El título de la sección 7 debe ser estricta y únicamente **`## 7. Formulario Resumen`** (sin agregados entre paréntesis ni etiquetas de LaTeX).
  3. Para operaciones aritméticas alineadas en soluciones, estructurarlas en tablas Markdown explicativas en vez de `\begin{array}`.

---

### `[ERR-011]` Reglas horizontales (`---`) debajo de encabezados causan error de transición en Sphinx
* **Fecha:** 2026-10-19
* **Problema:** Advertencias de Sphinx: `ERROR: Document or section may not begin with a transition`.
* **Causa Raíz:** En la especificación de docutils, una sección no puede comenzar inmediatamente con una regla de transición `---`.
* **Invariante / Regla Aprendida:**
  * **NUNCA colocar `---` directamente debajo de un encabezado (`#`, `##`, `###`).**
  * La regla `---` se usa exclusivamente para cerrar o delimitar el final de una sección previa, justo antes del siguiente título.

---

### `[ERR-012]` Salto de línea ausente entre enunciado de pregunta y alternativa A
* **Fecha:** 2026-10-19
* **Problema:** En las preguntas de opción múltiple, la alternativa `A) ...` aparecía pegada en el mismo renglón que el final del enunciado (ej. `1. Calcule la fracción... A) 44/88`), mientras que B, C, D, E sí saltaban a líneas independientes.
* **Causa Raíz:** En Markdown, un salto de línea simple se interpreta como un espacio dentro del mismo párrafo. Las alternativas tenían dos espacios al final (`  \n`), pero la línea del enunciado de la pregunta terminaba en un salto simple sin espacios.
* **Invariante / Regla Aprendida:**
  * **Toda línea de enunciado que precede inmediatamente a la alternativa `A)` debe terminar obligatoriamente con dos espacios (`  \n`).**
  * Esto fuerza el salto de línea `<br />` en el HTML generado, manteniendo la opción `A)` en su propio renglón alineada debajo de la pregunta.

---

### `[ERR-013]` Integración Obligatoria de Gráficos y Diagramas Visuales en Álgebra
* **Fecha:** 2026-10-19
* **Problema:** Los conceptos algebraicos abstractos (punto de equilibrio, posición relativa de rectas, concavidad y raíces de funciones) requieren soporte visual para maximizar la comprensión preuniversitaria.
* **Invariante / Regla Aprendida:**
  * En los temas de Álgebra donde intervenga modelamiento geométrico, económico o funcional, es **obligatorio incluir diagramas visuales** (bloques Mermaid o esquemas SVG/gráficos vectoriales limpios).
  * Aplicaciones obligatorias:
    1. **Punto de Equilibrio (Modelos Lineales):** Esquema de Costo Fijo, Costo Total, Ingreso Total, Punto de Equilibrio, Zona de Pérdidas y Zona de Ganancias.
    2. **Sistemas de Ecuaciones $2 \times 2$:** Interpretación geométrica de rectas secantes (única solución), paralelas (incompatible) y coincidentes (indeterminado).
    3. **Intervalos:** Esquemas de rectas numéricas con regiones de unión, intersección y diferencia.
    4. **Funciones Cuadráticas:** Parábola, vértice, eje de simetría y puntos de corte.

---

### `[ERR-014]` Reemplazo de Mermaid por Figuras Vectoriales LaTeX (TikZ + `tkz-euclide` / `pgfplots`)
* **Fecha:** 2026-10-19
* **Problema:** Los bloques `{mermaid}` fallan en la compilación de Sphinx/Jupyter Book o generan diagramas toscos y no aptos para geometría euclidiana rigurosa.
* **Causa Raíz:** Sphinx requiere dependencias de Node.js externas para compilar Mermaid, y además Mermaid no posee precisión geométrica ni soporte para fuentes tipográficas de LaTeX como Computer Modern.
* **Invariante / Regla Aprendida:**
  1. **NUNCA usar `{mermaid}` en los temas.**
  2. Para figuras geométricas y de funciones, usar exclusivamente **LaTeX nativo** con **TikZ**, **`tkz-euclide`** y **`pgfplots`**.
  3. Las figuras se compilan a SVG vectorial mediante `pdflatex` + `dvisvgm` usando el helper estandarizado `scratch/tikz_to_svg.py`.
  4. Los archivos SVG resultantes se guardan en `assets/<materia>/<nombre_figura>.svg` y se integran en el Markdown mediante la directiva:
     ````markdown
     ```{figure} ../../assets/<materia>/<nombre_figura>.svg
     ---
     width: 90%
     align: center
     alt: Descripción técnica
     ---
     *Leyenda explicativa con notación matemática.*
     ```
     ````

---

### `[ERR-015]` Estructura Jerárquica Obligatoria en `_toc.yml`
* **Fecha:** 2026-10-19
* **Problema:** Una lista plana de archivos en `_toc.yml` desordena el menú lateral de Jupyter Book e impide la navegación agrupada por asignaturas.
* **Causa Raíz:** El usuario requiere una navegación jerárquica con páginas de aterrizaje por curso (landing pages) y secciones anidadas.
* **Invariante / Regla Aprendida:**
  * La estructura en `_toc.yml` debe seguir estrictamente el formato:
    ```yaml
    format: jb-book
    root: index
    chapters:
      - file: Clases/Aritmetica/index
        sections:
          - file: Clases/Aritmetica/01_...
      - file: Clases/Algebra/index
        sections:
          - file: Clases/Algebra/01_...
      - file: Clases/Geometria/index
        sections:
          - file: Clases/Geometria/01_...
    ```
  * Cada asignatura debe contar con su archivo `index.md` que resuma el mapa curricular, competencias e indicadores clave de Beca 18 / CNEB.

---

### `[ERR-016]` Sintaxis de `tkz-euclide` Versión 4 y 5
* **Fecha:** 2026-10-19
* **Problema:** Error `\tkzDrawCircle needs two points (center,point)` al compilar código antiguo de `tkz-euclide`.
* **Causa Raíz:** En `tkz-euclide` v4+, `\tkzDrawCircle[in](A,B,C)` ya no se permite directamente; se debe definir primero el círculo y sus puntos con `\tkzDefCircle[in](A,B,C)\tkzGetPoints{I}{P}` y luego graficar con `\tkzDrawCircle(I,P)`.
* **Invariante / Regla Aprendida:**
  * Círculo inscrito: `\tkzDefCircle[in](A,B,C)\tkzGetPoints{I}{P}` y luego `\tkzDrawCircle(I,P)`.
  * Círculo circunscrito: `\tkzDefCircle[circum](A,B,C)\tkzGetPoints{O}{P}` y luego `\tkzDrawCircle(O,P)`.

---

### `[ERR-017]` Rutas Relativas de Assets en Estructuras de Carpetas Anidadas
* **Fecha:** 2026-10-19
* **Problema:** Imágenes no encontradas (`WARNING: image file not readable: assets/...`) durante `jupyter-book build .`.
* **Causa Raíz:** Los archivos de tema se ubican dos niveles abajo en `Clases/<Materia>/<archivo>.md`, por lo que una referencia `assets/...` o `../assets/...` no resuelve la raíz del proyecto.
* **Invariante / Regla Aprendida:**
  * Desde `Clases/<Materia>/`, la ruta relativa obligatoria hacia `assets/` es:
    ````markdown
    ```{figure} ../../assets/<materia>/<archivo>.svg
    ```
    ````

---

### `[ERR-018]` Vectorización Pura SVG en TikZ con `dvisvgm --pdf --exact-bbox`
* **Fecha:** 2026-10-19
* **Problema:** Gráficos vectoriales generados que se cortan en los márgenes o que no escalan uniformemente en diferentes navegadores y resoluciones móviles.
* **Causa Raíz:** Conversiones rasterizadas o bounding boxes imprecisos calculados sin recortar el espacio blanco del PDF compilado.
* **Invariante / Regla Aprendida:**
  * Usar el pipeline estandarizado en `scratch/tikz_to_svg.py`:
    1. Documentclass: `\documentclass[tikz,border=5pt]{standalone}`.
    2. Paquetes: `\usepackage{tikz}`, `\usepackage{tkz-euclide}`, `\usepackage{pgfplots}`, `\usepackage{amsmath,amssymb}`.
    3. Compilar PDF: `pdflatex -interaction=nonstopmode <archivo>.tex`.
    4. Convertir a SVG vectorial: `dvisvgm --pdf --exact-bbox <archivo>.pdf -o <archivo>.svg`.

---

### `[ERR-019]` Formato Estricto de "7. Formulario Resumen" (Markdown Nativo vs `\begin{array}`)
* **Fecha:** 2026-10-19
* **Problema:** En dispositivos móviles y lectores web, los bloques `\begin{array}` causan scroll horizontal desmesurado, no respetan el responsive design y dificultan la lectura rápida.
* **Causa Raíz:** Se utilizaban tablas matemáticas complejas de LaTeX en vez de tablas nativas del Markdown parseadas por MyST.
* **Invariante / Regla Aprendida:**
  * La sección final debe llamarse exactamente **`## 7. Formulario Resumen`**.
  * Toda tabla debe ser una tabla Markdown nativa con columnas claras (`| Concepto / Teorema | Fórmula / Expresión Matemática |`).
  * La matemática debe ir incrustada como inline `$ ... $` dentro de las celdas, sin barras verticales `|` no escapadas.

---

### `[ERR-020]` Salto de Línea Obligatorio de Dos Espacios (`  \n`) en Opciones de Ejercicios
* **Fecha:** 2026-10-19
* **Problema:** El texto del enunciado se fusiona con la alternativa `A)` en una sola línea continua al renderizarse en HTML.
* **Causa Raíz:** En la especificación CommonMark y MyST, un salto de línea simple en el archivo fuente es tratado como un espacio en blanco común.
* **Invariante / Regla Aprendida:**
  * Toda línea de enunciado que precede a la alternativa `A)` DEBE terminar con dos espacios en blanco seguidos de salto de línea (`  \n`), o una línea en blanco intermedia antes de la lista de alternativas.

---

### `[ERR-021]` Orientación de Vértices en Arcos con `\tkzMarkAngle`
* **Fecha:** 2026-10-19
* **Problema:** En figuras de triángulos y polígonos, arcos de ángulo dibujados al exterior del triángulo en lugar de al interior.
* **Causa Raíz:** `tkz-euclide` mide ángulos en sentido antihorario. Si se invierte el orden de los vértices (ej. `(C,B,A)` en lugar de `(A,B,C)`), el arco se proyecta sobre el ángulo reflejo (exterior).
* **Invariante / Regla Aprendida:**
  * Verificar la orientación geométrica: para marcar el ángulo en $B$, el orden de los puntos `(A,B,C)` debe seguir el sentido trigonométrico estándar (antihorario respecto al interior de la figura).

---

### `[ERR-022]` Denominación "Tema XX" y Supresión de Índices Manuales
* **Fecha:** 2026-10-19
* **Problema:** Títulos inconsistentes (`Fascículo XX`) y bloques artificiales `🧭 ÍNDICE` que duplican la barra de navegación nativa del tema web de Jupyter Book.
* **Causa Raíz:** Residuos de plantillas para documentos impresos monofásicos no adaptados al estándar interactivo de Jupyter Book.
* **Invariante / Regla Aprendida:**
  * Título nivel 1 estricto: `# Tema XX: [Nombre del Tema]`.
  * Queda terminantemente prohibido incluir bloques manuales de índice (`🧭 ÍNDICE` o enlaces manuales ancla `#`). La navegación lateral e interna la gestiona automáticamente Sphinx/Jupyter Book.

---

### `[ERR-023]` Teoría Comprimida y Falta de Andamiaje para el Perfil Beca 18
* **Fecha:** 2026-10-19
* **Problema:** Teorías condensadas en listas de fórmulas abstractas sin puentes intuitivos ni explicaciones progresivas, lo cual resulta inaccesible para estudiantes de colegios públicos con formación matemática deficitaria.
* **Causa Raíz:** Priorizar la cobertura rápida del temario y los ejercicios sobre la labor formativa de un libro de texto integral.
* **Invariante / Regla Aprendida:**
  1. **Andamiaje desde Cero:** Explicar el concepto con lenguaje intuitivo y analogías antes de formalizar.
  2. **Micro-ejemplos Ilustrativos:** Incluir un mini-ejemplo de aplicación de 1 a 2 líneas inmediatamente después de cada teorema o fórmula en la teoría.
  3. **Alertas de Errores Comunes:** Incluir en cada tema la sección `> ⚠️ **¡Cuidado con el error clásico de admisión!**` explicando dónde falla la mayoría de postulantes.
  4. **Abundancia Gráfica en TikZ:** Cada concepto fundamental (planos, trazos auxiliares, rectas numéricas, diagramas) debe tener su figura vectorial propia.

---

### `[ERR-024]` SVGs en Blanco por `opacity` y `pattern` de TikZ en `dvisvgm`
* **Fecha:** 2026-10-19
* **Problema:** Los archivos SVG generados con `pdflatex` + `dvisvgm 3.4.3` (ej. `assets/algebra/intervalos_recta_real_operaciones.svg` y `assets/algebra/inecuaciones_regla_signos.svg`) se muestran totalmente en blanco en navegadores web.
* **Causa Raíz:**
  1. El uso del modificador `opacity=...` (ej. `[fill=blue!20, opacity=0.6]`) en TikZ provoca que `dvisvgm` interprete el grupo de transparencia PDF inyectando atributos globales `stroke-opacity='0'` y `fill-opacity='0'` en todos los trazados SVG subsiguientes.
  2. El uso de la librería `patterns` de TikZ (ej. `[pattern=north east lines]`) también genera grupos de transparencia/máscaras en el PDF, lo que activa el mismo fallo en `dvisvgm`.
* **Invariante / Regla Aprendida:**
  * **PROHIBIDO** usar `opacity=...`, `fill opacity=...` o `stroke opacity=...` en el código TikZ destinado a exportación SVG con `dvisvgm`.
  * **PROHIBIDO** usar tramas de `pattern=...` de TikZ.
  * Para lograr tonos tenues, usar exclusivamente **mezcla de colores sólidos** de xcolor: `fill=blue!15`, `fill=red!20`, `fill=purple!22`.
  * Si se requieren líneas diagonales o rayado para intersecciones, implementarlas mediante trazado explícito con bucles manuales acotados:
    ```latex
    \begin{scope}
        \clip (1,0) rectangle (4,1.2);
        \foreach \s in {0.5, 0.8, ..., 5.5} {
            \draw[thin, purple!60] (\s, -0.2) -- (\s+1.2, 1.4);
        }
    \end{scope}
    ```
  * Tras toda compilación de SVG, verificar con script o `grep` que no existan atributos `opacity='0'` en el SVG resultante.

---

### `[ERR-025]` Manejo de Libros Masivos (>100 MB) y Optimización de PDFs Escaneados
* **Fecha:** 2026-10-21
* **Problema:** Archivos escaneados originales de gran peso (ej. Biblia Rodo de 772 MB y 595 MB, total ~1.4 GB) casi bloquean el repositorio de Git (que rechaza commits >100 MB) y resultarían imposibles de descargar para postulantes con datos móviles.
* **Causa Raíz:** Documentos compuestos por imágenes escaneadas sin comprimir (PNGs de más de 7 MB por página y resoluciones superiores a 3400×2400 px).
* **Invariante / Regla Aprendida:**
  1. Ignorar inmediatamente en `.gitignore` cualquier carpeta de material fuente bruto pesado (`Libros/`).
  2. Implementar un pipeline de optimización automatizada con `PyMuPDF` (`fitz`) y `Pillow`:
     * Renderizado o escalado a DPI 140 (aprox. 1600 px de ancho), lo cual garantiza nitidez absoluta en fracciones, exponentes pequeños y subíndices de fórmulas matemáticas.
     * Compresión en JPEG calidad 68–72 con `optimize=True`.
     * Esto logra una reducción superior al 91% (de 1.36 GB a ~118 MB en total para más de 620 páginas), permitiendo su alojamiento dentro de los límites estándar de Git y la web.

---

### `[ERR-026]` Conflicto de Workflows de GitHub Actions (Jekyll vs Jupyter Book) y Redirecciones Residuales
* **Fecha:** 2026-10-21
* **Problema:** Tras cambiar la fuente de GitHub Pages, se generaron flujos sugeridos por la interfaz (`jekyll-gh-pages.yml` y `static.yml`), provocando la desaparición del tema interactivo de 3 columnas de Jupyter Book (las 2 barras laterales) y mostrando texto plano. Asimismo, un archivo residual `docs/index.html` provocaba un error 404 al redirigir al dominio raíz.
* **Causa Raíz:**
  1. Jekyll sobrescribía el artefacto compilado por Sphinx/Jupyter Book, convirtiendo el sitio en un blog plano sin `sphinx-book-theme`.
  2. La presencia de `docs/index.html` con `<meta http-equiv="refresh" content="0; url=../index.html">` rompía la navegación cuando GitHub Pages intentaba servir desde rama.
* **Invariante / Regla Aprendida:**
  1. En `.github/workflows/`, solo debe existir el workflow oficial `deploy.yml` configurado para Jupyter Book.
  2. Eliminar cualquier carpeta `/docs` residual para evitar conflictos de origen.
  3. En GitHub (**Settings -> Pages -> Source**), la fuente debe ser estrictamente **GitHub Actions**.
  4. Incluir siempre `workflow_dispatch:` en `deploy.yml` para permitir lanzamientos manuales desde la interfaz de GitHub Actions si fuese necesario.

---

### `[ERR-027]` Visores Embebidos en Pantalla para Compendios en lugar de Descargas Forzadas
* **Fecha:** 2026-10-21
* **Problema:** Enlaces de descarga directa de compendios de 50+ MB obligaban al estudiante a saturar el almacenamiento de su dispositivo o salir de la web para estudiar.
* **Causa Raíz:** No proporcionar interfaces de lectura en línea dentro de la jerarquía de capítulos del compendio.
* **Invariante / Regla Aprendida:**
  1. Para compendios y formularios, crear páginas de visor interactivo dedicadas en Markdown estructuradas con bloques `{raw} html` que contengan un `<iframe>` de altura completa (`height: 85vh; min-height: 720px;`) con parámetros `#toolbar=1&navpanes=1`.
  2. El visor debe permitir navegación por miniaturas, zoom (`+` / `-`) y búsqueda interna (`Ctrl + F`) de forma nativa en el navegador, sin necesidad de descargar el archivo.
  3. En `deploy.yml`, asegurar que el paso de compilación copie los archivos PDF directamente a la carpeta de salida (`_build/html/Formularios/`) para mantener rutas relativas limpias y estables.

---

### `[ERR-028]` Diseño de Favicons y Branding para Portales Educativos
* **Fecha:** 2026-10-21
* **Problema:** Favicons generados con ilustraciones 3D, sombras o texturas complejas se ven borrosos e irreconocibles en pestañas pequeñas de 16×16 o 32×32 píxeles.
* **Causa Raíz:** Tratar el favicon como una ilustración artística en lugar de un pictograma vectorial minimalista de alto contraste.
* **Invariante / Regla Aprendida:**
  1. Los favicons deben basarse en **siluetas geométricas planas (flat design) de máximo contraste** (ej. silueta blanca nítida sobre círculo de color sólido distintivo como azul rey o rojo carmesí).
  2. El archivo `assets/favicon.ico` debe generarse con canal alfa transparente y almacenar los tamaños multi-resolución: 16×16, 32×32, 48×48 y 64×64 píxeles.
  3. Vincular formalmente en `_config.yml` tanto `html: favicon: "assets/favicon.ico"` como `html: logo: "assets/logo.png"` para garantizar una identidad visual coherente tanto en la pestaña del navegador como en la cabecera del menú lateral.

---

### `[ERR-029]` Colisiones de KaTeX por Display Math (`$$`) Pegado a Alternativas `A)` y `$$` Huérfanos
* **Fecha:** 2026-10-21
* **Problema:** En el visor / preview de Markdown y en KaTeX web, aparecía el error crítico:
  `ParseError: KaTeX parse error: Can't use function '$' in math mode at position XX: ...\cot(45^\circ)}$$ A) $\frac{1…`
  y en otras secciones el texto normal en español quedaba atrapado en cursiva sin espacios dentro de fórmulas matemáticas (runaway math mode: `*(Siseplanteabaconx=30...)*`).
* **Causa Raíz:**
  1. Cuando un enunciado de problema propuesto terminaba con `$$fórmula$$` (especialmente con dos espacios finales `  \n`) y la siguiente línea era `A) $alternativa$`, CommonMark une ambas líneas en el mismo párrafo (`<p>$$...$$<br>A) $...$</p>`). El parser de inline math empareja el primer `$` de `$$` con el `$` de `A)`, dejando el segundo `$` dentro del modo matemático e invocando a KaTeX con texto y símbolos `$`, provocando el `ParseError`.
  2. La presencia de delimitadores `$$` huérfanos o fórmulas inline con `$` sin cerrar invertía por completo el estado matemático en el resto del archivo: el texto regular se interpretaba como LaTeX y las ecuaciones reales como texto.
* **Invariante / Regla Aprendida:**
  1. En las 45 preguntas propuestas, la fórmula final del enunciado DEBE escribirse como **matemática inline en la misma línea del número de pregunta**:
     `18. Calcule el valor simplificado de: $W = \frac{\sin(30^\circ) + \cos(60^\circ)}{\tan(45^\circ) + \cot(45^\circ)}$.  \nA) ...`
  2. Queda estrictamente PROHIBIDO colocar un bloque `$$` inmediatamente antes de la alternativa `A)`.
  3. Todo bloque display math `$$` (teoría y ejercicios resueltos) debe estar a columna 0 y contar obligatoriamente con **una línea en blanco antes y una después**.
  4. Nunca dejar delimitadores `$$` impares ni expresiones `$ ... $` abiertas a lo largo del documento.
  5. Ejecutar el validador riguroso `python scratch/audit_katex_syntax_rigorous.py` garantizando **0 errores** antes de publicar.

---

### `[ERR-030]` Vinculación Hipertextual Obligatoria en Tablas de Índices Curriculares
* **Fecha:** 2026-10-21
* **Problema:** En módulos como *Estadística y Probabilidad* y *Competencia Lectora*, la tabla de contenidos curricular en `index.md` mostraba los títulos en texto plano o con directivas `{table}` sin enlaces hipertextuales clicables, rompiendo la coherencia de navegación con el resto de cursos (Aritmética, Álgebra, Geometría, Trigonometría).
* **Causa Raíz:** Falta de estandarización en la plantilla del archivo `index.md` de cada asignatura al momento de redactar nuevos módulos.
* **Invariante / Regla Aprendida:**
  1. Todo archivo `Clases/<Curso>/index.md` debe incluir una tabla estándar en Markdown nativo:
     `| Tema | Título del Contenido / Denominación Oficial | Competencia Clave |`
  2. La columna del título debe contener un **enlace relativo directo al archivo `.md` del tema**:
     `| **01** | [Tablas de Frecuencias y Datos Agrupados](01_Tablas_de_Frecuencias_Datos_Agrupados.md) | ... |`
  3. Evitar secuencias de escape no deseadas (como `\b` en `\bar{x}`) asegurando que los símbolos matemáticos dentro de las tablas (`\bar{x}`, `\Omega`) se escriban correctamente sin caracteres de control ASCII.
