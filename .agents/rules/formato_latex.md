# Reglas de Formato Tipográfico y Validación Rigurosa de LaTeX Matemático

Este documento define las normas obligatorias para asegurar que toda fórmula matemática se interprete y renderice con **100% de compatibilidad** en GitHub, VS Code, MathJax, KaTeX y Jupyter Book.

---

## 1. Sintaxis Estricta de Delimitadores ($ y $$)
1. **Sin espacios en los bordes internos:**
   * ✅ Correcto: `$x \in \mathbb{Q}$`, `$\frac{a}{b}$`
   * ❌ Incorrecto: `$ x \in \mathbb{Q} $`, `$ \frac{a}{b} $` *(Muchos renderizadores de Markdown no activan el modo matemático si hay un espacio junto al `$`).*
2. **Prohibidas las líneas en blanco dentro de bloques `$$ ... $$`:**
   * Los bloques de ecuación destacada deben ser continuos. Si se deja una línea en blanco dentro de `$$`, MathJax/KaTeX corta la ecuación y muestra código crudo o mensaje de error.
   ```latex
   <!-- ✅ Correcto -->
   $$
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   $$

   <!-- ❌ Incorrecto (causa fallo de parseo) -->
   $$
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

   y = 2x
   $$
   ```
3. **Cierre correlativo de `$`:***
   * En cada línea de texto, el conteo total de caracteres `$` (descontando los bloques `$$`) debe ser siempre un número **par**.
4. **Líneas en blanco obligatorias ANTES y DESPUÉS de bloques `$$ ... $$`:**
   * En Markdown y MyST (Jupyter Book / GitHub Pages), los bloques de ecuaciones `$$` deben tener obligatoriamente una línea en blanco anterior y una posterior. Si se colocan pegados al párrafo anterior sin línea en blanco, el analizador lo trata como texto dentro de `<p>`, rompiendo la interpretación de MathJax e insertando caracteres `$` crudos.

---

## 2. Compatibilidad Universal de Macros y Caracteres Especiales
1. **Notación de Divisibilidad y Múltiplos:**
   * ❌ No usar `\dot{b}` o `\dot{2}` para múltiplos (en LaTeX es derivada temporal y en MathJax genera caracteres rotos).
   * ✅ Usar: `$k \cdot b$`, `\text{múltiplo de } b` o `$b \mid a$` (b divide a a).
2. **Tablas Markdown vs. Barras de Conjunto (`|`):**
   * En las filas de una tabla Markdown, el carácter `|` define columnas. Si se escribe `$A = \{x \in \mathbb{Z} | x > 0\}$` dentro de una tabla, la tabla se romperá visualmente.
   * ✅ Usar siempre `\mid` o `\vert` dentro de tablas: `$A = \{x \in \mathbb{Z} \mid x > 0\}$`.
3. **Texto con tildes y espacios dentro de fórmulas:**
   * Usar siempre `\text{...}` con espacio inicial cuando acompaña a un número:
     * ✅ `$120\text{ litros}$`, `$25\text{ m/s}$`
     * ❌ `$120\text{litros}$`, `$120 litros$` *(en matemáticas puras "litros" se interpreta como el producto $l \cdot i \cdot t \cdot r \cdot o \cdot s$).*
4. **Conjuntos numéricos canónicos:**
   * Usar `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{Q}`, `\mathbb{R}`, `\mathbb{C}`.

---

## 3. Protocolo de Verificación Pre-Commit
Antes de finalizar cualquier fascículo:
1. Ejecutar el script de auditoría `check_latex.py`.
2. Verificar que no haya advertencias de líneas en blanco, dólares impares ni comandos no estándar.
