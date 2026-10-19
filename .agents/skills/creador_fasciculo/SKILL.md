---
name: creador-fasciculo
description: Automatiza y estandariza la redacción de temas teóricos y prácticos preuniversitarios de alto nivel con ejercicios en 3 niveles, contextualización Beca 18 y loop de aprendizaje continuo.
---

# Skill: Creador de Temas Preuniversitarios (Con Loop de Ingeniería)

Esta habilidad guía la creación de temas teóricos y prácticos según el temario oficial de Beca 18 / Preuniversitario, incorporando un **bucle de retroalimentación y aprendizaje activo**.

---

## Procedimiento de Redacción en 4 Fases

### 1. Pre-Check (Consulta Obligatoria de Memoria Histórica)
- **Paso obligatorio:** Abrir y revisar `.agents/memory/registro_errores_y_aprendizajes.md` para cumplir todas las invariantes acumuladas (`[ERR-001]` a `[ERR-011]`).
- Consultar el indicador del temario oficial en `temarios/temario_oficial_traducido_enp.md`.
- Extraer referencias conceptuales de los libros conectados en Google Drive (Lumbreras, Cuzcano, Rodo, Uniciencia, San Marcos, Beca 18).

### 2. Estructura y Reglas Críticas de Redacción
- **Denominación:** Nombrar siempre **Tema XX** (nunca "Fascículo").
- **Índices:** Prohibido agregar secciones manuales de índice en markdown; Jupyter Book genera el índice interactivo automáticamente.
- **Columna 0 Obligatoria:** Todas las líneas de texto, fórmulas `$$`, notas y alternativas (`A) ...`) deben iniciar en **columna 0** (cero espacios iniciales) para evitar que CommonMark las convierta en bloques de código `<pre><code>`.
- **Espaciado en Ecuaciones `$$`:** Todo bloque de display math `$$` debe tener estrictamente **una línea en blanco antes** y **una línea en blanco después**.
- **Soluciones Paso a Paso:** En las soluciones de los 10 ejercicios, **no usar listas numeradas `1. `, `2. `**; usar párrafos en negrita a columna 0: `**Paso 1:**`, `**Paso 2:**`, `**Paso 3:**`.
- **Sección 7:** Titulada estricta y únicamente **`## 7. Formulario Resumen`**. Debe estructurarse con **Tablas Markdown estándar** (`| Concepto | Expresión Matemática |`) con matemáticas inline `$ ... $`. **Prohibido usar `\begin{array}`**.
- **Reglas horizontales (`---`):** Nunca colocar `---` directamente debajo de un título de sección (`#`, `##`, `###`).
- **LaTeX Estricto:** Sin espacios en delimitadores `$ $`, sin líneas vacías internas en `$$ $$`, sin `\dot{b}` (usar `$k \cdot b$`).
- **Ejercicios Resueltos:** Exactamente **10 problemas resueltos paso a paso** (3 básicos, 4 intermedios, 3 contextualizados Beca 18).
- **Ejercicios Propuestos:** Exactamente **45 problemas propuestos** clasificados en 3 bloques de 15 con 5 alternativas (A, B, C, D, E) y tabla de claves completa (1 al 45).

### 3. Validación Automatizada (Quality Gate)
- Ejecutar `python scratch/strip_all_accidental_spaces.py` para verificar sangrías.
- Ejecutar `jupyter-book build .` localmente y verificar **0 errores y 0 advertencias**.
- Verificar que los 45 ejercicios tengan su clave correspondiente en la tabla.

### 4. Post-Mortem y Actualización de Aprendizajes
- Si se detecta un error nuevo durante la revisión del usuario, registrarlo de inmediato en `.agents/memory/registro_errores_y_aprendizajes.md` y ajustar las reglas para blindar el sistema.
