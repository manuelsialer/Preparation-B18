# Reglas Pedagógicas para Material Preuniversitario y Beca 18 (Estándar Libro Formativo)

## 1. Principio de Andamiaje desde Cero (Scaffolding Inclusivo)
- **Perfil Real del Postulante:** El estudiante de Beca 18 a menudo proviene de escuelas públicas con vacíos severos de formación básica en matemáticas. Por tanto, el material debe **desmitificar la matemática**, explicar con lenguaje cálido, claro y accesible, y construir los puentes conceptuales que el colegio omitió.
- **Cero "pasos mágicos":** Nunca omitir procedimientos algebraicos intermedios diciendo "es obvio" o "despejando directamente". Mostrar la justificación paso a paso (factorizaciones, simplificaciones, leyes de signos).
- **Enfoque Intuitivo antes del Formalismo:** Comenzar cada nuevo concepto con una analogía física, geométrica o de la vida cotidiana antes de introducir la definición matemática formal.
- **Micro-ejemplos puente en la teoría:** Inmediatamente después de enunciar una propiedad o fórmula, incluir un *Micro-ejemplo ilustrativo* de 1 a 2 líneas resuelto al instante para fijar el aprendizaje antes de continuar.
- **Cuadros de Advertencia ("⚠️ ¡Cuidado con el error clásico de admisión!"):** Señalar con precisión quirúrgica dónde tropieza el 80% de postulantes (ej. olvidar invertir la desigualdad con números negativos, simplificar términos sumados en fracciones, signos en distancias o áreas).

## 2. Abundancia y Calidad Gráfica Vectorial (LaTeX TikZ / pgfplots)
- **Estándar de Libro Publicado:** Ninguna propiedad geométrica, trigonométrica, analítica o estadística debe quedar como mera abstracción escrita.
- Todo concepto clave debe contar con su correspondiente figura vectorial SVG generada en **TikZ / tkz-euclide / pgfplots** (planos cartesianos con curvas y asíntotas, figuras con trazos auxiliares punteados y cotas, rectas numéricas coloreadas, círculos trigonométricos con proyecciones y polígonos de frecuencia).

## 3. Gradualidad en la Dificultad
- **Nivel Básico (Fijación):** Aplicación directa de teoremas y definiciones. Debe consolidar la confianza operativa.
- **Nivel Intermedio (Raciocinio):** Requiere combinar 2 o más propiedades, hacer trazos auxiliares o plantear sistemas de ecuaciones.
- **Nivel Avanzado / Contexto Beca 18:** Modelamiento matemático de situaciones reales (comercio, finanzas, ingeniería, agricultura, física). El estudiante debe traducir el enunciado verbal al lenguaje algebraico/geométrico, resolver y contextualizar la respuesta.

## 4. Estructura de Resolución de Ejercicios
Todo ejercicio resuelto debe seguir estrictamente este esquema de 4 partes:
1. **Enunciado Claro:** Con todos los datos numéricos y condiciones explícitas.
2. **Estrategia / Planteamiento:** Explicación breve de 1 o 2 líneas de *qué camino se va a tomar y por qué*.
3. **Resolución Paso a Paso:** Cálculos ordenados, con fórmulas en LaTeX en display aislado y explicaciones intermedias.
4. **Respuesta y Conclusión:** Clave con letra mayúscula (A, B, C, D o E) e interpretación del resultado.

