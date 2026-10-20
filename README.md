# 📚 Compendio Preuniversitario de Alto Nivel – Beca 18

[![Jupyter Book](https://img.shields.io/badge/built%20with-Jupyter%20Book-orange.svg)](https://jupyterbook.org)
[![Deploy GitHub Pages](https://github.com/manuelsialer/Preparation-B18/actions/workflows/deploy.yml/badge.svg)](https://github.com/manuelsialer/Preparation-B18/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRONABEC](https://img.shields.io/badge/Enfoque-Beca%2018%20%2F%20CNEB-success.svg)](https://www.pronabec.gob.pe)

Repositorio de código abierto y libro interactivo de texto preuniversitario desarrollado específicamente para el **Examen Nacional de Preselección (ENP - Beca 18 / PRONABEC)** y las pruebas de admisión de mayor exigencia del Perú (UNI, UNMSM, UNALM, PUCP).

📖 **Lectura en línea del libro:** [https://manuelsialer.github.io/Preparation-B18/](https://manuelsialer.github.io/Preparation-B18/)

---

## 🎯 Enfoque Pedagógico: Cerrando la Brecha Educativa

Este material fue concebido para abordar las deficiencias formativas de estudiantes de colegios públicos y zonas rurales que postulan a becas de pregrado. El contenido se estructura bajo cuatro pilares metodológicos:

1. **Andamiaje desde Cero (Puentes Intuitivos):** Todo concepto matemático o lingüístico se introduce mediante analogías de la vida cotidiana o física antes de formalizar teoremas y fórmulas.
2. **Abundancia Gráfica Vectorial (LaTeX TikZ / SVG):** Gráficos geométricos, diagramas de flujo y esquemas conceptuales vectoriales con precisión milimétrica, sin imágenes pixeladas ni distorsiones de escala.
3. **Micro-ejemplos y Advertencias de Admisión:** Ejemplos breves de aplicación inmediata y recuadros de alerta: `> ⚠️ ¡Cuidado con el error clásico de admisión!` explicando las trampas frecuentes de los evaluadores.
4. **Gradualidad en la Práctica:** Problemas clasificados en Nivel Básico (fijación), Nivel Intermedio (operatividad) y Nivel Avanzado (contextualizado a situaciones reales peruanas).

---

## 🗺️ Mapa Curricular del Compendio

El compendio cubre integralmente las dos áreas evaluadas en el Examen Nacional de Preselección:

```
Preparation-B18/
├── 📐 MÓDULO I: MATEMÁTICAS
│   ├── 1. Álgebra (12 temas)
│   │   └── Intervalos, ecuaciones, inecuaciones, sistemas lineales, funciones afines/cuadráticas,
│   │       polinomios, división algebraica, factorización, radicación y logaritmos.
│   ├── 2. Aritmética (9 temas)
│   │   └── Fracciones y razones, potenciación/radicación, redondeo, notación científica,
│   │       sistemas de unidades, porcentajes, interés simple, magnitudes y progresiones.
│   ├── 3. Estadística y Probabilidad (4 temas)
│   │   └── Tablas para datos agrupados, medidas de tendencia central, gráficos y regla de Laplace.
│   ├── 4. Geometría (6 temas)
│   │   └── Puntos notables, relaciones métricas, cuadriláteros, polígonos regulares,
│   │       circunferencia y cuerpos de revolución (cilindro, cono y esfera).
│   └── 5. Trigonometría (3 temas)
│       └── Razones trigonométricas en triángulos rectángulos, ángulos verticales e identidades.
│
└── 📖 MÓDULO II: COMPETENCIA LECTORA (10 temas)
    ├── 1. Arquitectura Textual: Tema central, idea principal, subtemas y título.
    ├── 2. Formatos Textuales: Textos continuos, discontinuos (infografías y tablas) y mixtos.
    ├── 3. Tipología Discursiva: Textos expositivos, narrativos e instructivos.
    ├── 4. Nivel Literal: Localización explícita e integración de información dispersa.
    ├── 5. Nivel Inferencial: Relaciones de causa-efecto y problema-solución.
    ├── 6. Sentido Figurado: Metáforas, giros retóricos, ironías y tono del autor.
    ├── 7. Inferencia Global: Conclusiones, extrapolación a escenarios nuevos y propósito.
    ├── 8. Textos Argumentativos: Tesis, argumentos de soporte y objeciones.
    ├── 9. Textos Dialécticos: Análisis comparativo de posturas opuestas (Texto A vs. Texto B).
    └── 10. Lectura Crítica: Detección de falacias lógicas, sesgos y credibilidad de fuentes.
```

---

## 🛠️ Instalación y Compilación Local

Si deseas compilar o contribuir al libro localmente en tu computadora:

### Requisitos Previos
* **Python 3.10 o superior**
* **Git**
* *(Opcional para recompilar gráficos TikZ)*: Distribución LaTeX (TeX Live / MiKTeX) con `dvisvgm`.

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/manuelsialer/Preparation-B18.git
cd Preparation-B18

# 2. Crear y activar entorno virtual
python -m venv .venv
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1
# En Linux / macOS:
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Compilar el libro en HTML
jupyter-book build .

# 5. Visualizar en tu navegador
# Abre el archivo _build/html/index.html en cualquier navegador web.
```

---

## 🚀 Despliegue Continuo (CI/CD)

El libro cuenta con un flujo de integración continua automatizado mediante **GitHub Actions** ([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)):
* Con cada `push` a la rama `main`, el entorno instala las dependencias, construye los artefactos estáticos mediante `jupyter-book build .` e inyecta la configuración `.nojekyll` requerida por GitHub Pages.
* El despliegue se publica sin intervención manual en la URL oficial del proyecto.

---

## 🤖 Arquitectura del Sistema de Agentes (.agents)

Este libro incorpora en su carpeta `.agents/` un sistema modular de ingeniería pedagógica y aseguramiento de la calidad basado en agentes de IA:

* **`.agents/rules/`:** Directrices explícitas de pedagogía preuniversitaria (andamiaje desde cero, contextualización con la realidad peruana, rigor en notación matemática y tipografía).
* **`.agents/skills/`:** Procedimientos estandarizados para la construcción de fascículos, generación de diagramas TikZ vectoriales y ensamblaje de prácticas graduadas.
* **`.agents/memory/`:** Registro histórico y acumulativo de errores técnicos y aprendizajes (`registro_errores_y_aprendizajes.md`) para garantizar que las figuras, formatos y sintaxis mantengan una invariante de calidad constante.


---

## 📄 Licencia


Este proyecto se distribuye bajo los términos de la Licencia **MIT**. Eres libre de usar, estudiar, compartir y adaptar este material con fines educativos y de impacto social.

---

*Desarrollado con dedicación para los futuros becarios y profesionales del Perú.*
