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
