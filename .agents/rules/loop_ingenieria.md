# Loop de Ingeniería y Aprendizaje Continuo (Feedback Loop)

Este documento define el mecanismo de **aprendizaje a partir de errores (Engineering Feedback Loop)** que rige la creación de material y código en este proyecto.

---

## 🔄 Las 4 Fases del Loop de Ingeniería

```
  ┌─────────────────────────────────────────────────────────┐
  │ 1. PRE-CHECK: Consultar Registro de Aprendizajes        │
  │    (Verificar lecciones pasadas para no reincidir)      │
  └───────────────────────────┬─────────────────────────────┘
                              ▼
  ┌─────────────────────────────────────────────────────────┐
  │ 2. EJECUCIÓN: Redacción y Desarrollo Estandarizado      │
  │    (Aplicar reglas de pedagogía, LaTeX y estructura)    │
  └───────────────────────────┬─────────────────────────────┘
                              ▼
  ┌─────────────────────────────────────────────────────────┐
  │ 3. VALIDACIÓN AUTOMATIZADA: Auditoría y Quality Gate    │
  │    (Correr scripts de verificación de LaTeX y formato)   │
  └───────────────────────────┬─────────────────────────────┘
                              ▼
  ┌─────────────────────────────────────────────────────────┐
  │ 4. POST-MORTEM & APRENDIZAJE: Si hay error o feedback,  │
  │    documentar causa raíz y registrar nueva regla        │
  └─────────────────────────────────────────────────────────┘
```

---

## 📌 Protocolo de las 4 Fases

### Fase 1: Pre-Check (Antes de redactar)
* Leer obligatoriamente el archivo `.agents/memory/registro_errores_y_aprendizajes.md`.
* Activar las alertas preventivas asociadas a errores históricos (ej. problemas de sintaxis LaTeX, formatos de tablas, omisión de puntos notables, etc.).

### Fase 2: Ejecución
* Redactar el contenido siguiendo fielmente la estructura de 5 partes:
  1. Teoría rigurosa.
  2. 10 problemas resueltos paso a paso.
  3. 45 problemas propuestos con alternativas A-B-C-D-E.
  4. Tabla de claves completa.
  5. Formulario resumen (Cheat Sheet) **íntegramente en LaTeX**.

### Fase 3: Validación Automatizada (Quality Gate)
* Ejecutar el script de auditoría matemática (`check_latex.py` o equivalente).
* Comprobar:
  * 0 advertencias de líneas en blanco dentro de bloques `$$`.
  * Número par de caracteres `$` en cada línea.
  * Sin caracteres de barra vertical `|` que rompan tablas Markdown.
  * Claves de los 45 ejercicios completas y correlativas.

### Fase 4: Registro Inmediato de Aprendizaje (Error Logging)
Cada vez que el usuario haga una corrección o se detecte una falla:
1. Registrar la incidencia en `.agents/memory/registro_errores_y_aprendizajes.md` con:
   * **Fecha y contexto del error.**
   * **Causa raíz identificada.**
   * **Solución aplicada.**
   * **Invariante o regla preventiva adoptada.**
2. Actualizar las reglas correspondientes en `.agents/rules/` para que la falla quede blindada en futuras iteraciones.
