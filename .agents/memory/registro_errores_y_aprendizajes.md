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



