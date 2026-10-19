---
name: creador-fasciculo
description: Automatiza y estandariza la redacción de fascículos teóricos y prácticos preuniversitarios de alto nivel con ejercicios en 3 niveles, contextualización Beca 18 y loop de aprendizaje continuo.
---

# Skill: Creador de Fascículos Preuniversitarios (Con Loop de Ingeniería)

Esta habilidad guía la creación de fascículos teóricos y prácticos según el temario oficial de Beca 18 / Preuniversitario, incorporando un **bucle de retroalimentación y aprendizaje activo**.

---

## Procedimiento de Redacción en 4 Fases

### 1. Pre-Check (Consulta de Memoria Histórica)
- **Paso obligatorio:** Abrir y revisar `.agents/memory/registro_errores_y_aprendizajes.md` para tener presentes las lecciones aprendidas (sintaxis LaTeX, formato de claves, etc.).
- Consultar el indicador del temario oficial en `temarios/temario_oficial_traducido_enp.md`.
- Extraer referencias conceptuales de los libros conectados en Google Drive (Lumbreras, Cuzcano, Rodo, Uniciencia, San Marcos, Beca 18).

### 2. Desarrollo Teórico y Práctico
- Redactar explicaciones claras, sin pasos mágicos.
- Usar LaTeX estricto (sin espacios en `$ $`, sin líneas vacías en `$$ $$`, sin `\dot{b}`).
- Redactar exactamente **10 problemas resueltos paso a paso** (3 básicos, 4 intermedios, 3 contextualizados Beca 18).
- Redactar exactamente **45 problemas propuestos** clasificados en 3 bloques de 15 con 5 alternativas (A, B, C, D, E).
- Generar el cuadro de claves verificado (1 al 45).
- Elaborar el **Formulario Resumen (Cheat Sheet) 100% en LaTeX**.

### 3. Validación Automatizada (Quality Gate)
- Ejecutar el script `check_latex.py` para asegurar 0 errores tipográficos.
- Verificar que los 45 ejercicios tengan su clave correspondiente en la tabla.

### 4. Post-Mortem y Actualización de Aprendizajes
- Si se detecta un error nuevo durante la revisión del usuario, registrarlo de inmediato en `.agents/memory/registro_errores_y_aprendizajes.md` y ajustar las reglas para blindar el sistema.
