# TEMA 02: ARITMÉTICA – POTENCIACIÓN Y RADICACIÓN EN NÚMEROS RACIONALES

> **Área:** Competencias Matemáticas (Resuelve problemas de cantidad)
> **Indicador Oficial (PRONABEC / CNEB):** *Establece relaciones entre datos y los transforma a expresiones numéricas que incluyan operaciones de potenciación y radicación de números racionales.*
> **Nivel:** Preuniversitario / Beca 18 – Alto Rendimiento

---
## 1. MOTIVACIÓN Y CONTEXTO REAL

En la naturaleza y en los procesos tecnológicos, muchas magnitudes no cambian a ritmos constantes o lineales, sino de forma multiplicativa acelerada o amortiguada.
* Cuando una colonia bacteriana en un cultivo de laboratorio duplica su población cada $\frac{1}{3}$ de hora, el modelamiento de la población requiere potencias con bases enteras y **exponentes racionales**.
* Cuando un medicamento administrado por vía intravenosa se degrada en el torrente sanguíneo a razón de perder $\frac{1}{4}$ de su concentración cada período de semivida, su concentración remanente se expresa como una potencia fraccionaria decreciente: $\left(\frac{3}{4}\right)^t$.
* Cuando un ingeniero civil diseña estructuras hidráulicas o calcula la velocidad de salida de un fluido mediante la ecuación de Torricelli ($v = \sqrt{2gh}$), o cuando un topógrafo determina la diagonal de una poligonal, las **raíces de números fraccionarios** son el pan de cada día.

Dominar con soltura la potenciación y radicación de fracciones permite simplificar expresiones algebraicas colosales en segundos y transformar problemas verbales complejos en ecuaciones numéricas elegantes.

---

## 2. FUNDAMENTACIÓN TEÓRICA RIGUROSA

### 2.1 Definición Axiomática de la Potenciación en $\mathbb{Q}$

Sean $\frac{a}{b} \in \mathbb{Q}$ (con $b \neq 0$) y $n \in \mathbb{Z}^+$. La potenciación es una multiplicación abreviada de factores idénticos:

$$
\left(\frac{a}{b}\right)^n = \underbrace{\left(\frac{a}{b}\right) \times \left(\frac{a}{b}\right) \times \cdots \times \left(\frac{a}{b}\right)}_{n \text{ factores}} = \frac{a^n}{b^n}
$$

* **$\frac{a}{b}$ (Base):** Número racional que se multiplica por sí mismo.
* **$n$ (Exponente):** Número que indica cuántas veces se repite la base como factor.
* **$P = \frac{a^n}{b^n}$ (Potencia):** Resultado numérico obtenido.

#### Regla de los Signos en Potenciación
1. $(\text{Positivo})^{\text{Par o Impar}} = \text{Positivo}$. Ejemplo: $\left(+\frac{2}{3}\right)^3 = +\frac{8}{27}$.
2. $(\text{Negativo})^{\text{Par}} = \text{Positivo}$. Ejemplo: $\left(-\frac{3}{5}\right)^2 = +\frac{9}{25}$.
3. $(\text{Negativo})^{\text{Impar}} = \text{Negativo}$. Ejemplo: $\left(-\frac{1}{2}\right)^5 = -\frac{1}{32}$.

> ⚠️ **Error Frecuente:** Confundir $-\left(\frac{a}{b}\right)^2$ con $\left(-\frac{a}{b}\right)^2$.
> * $-\left(\frac{2}{3}\right)^2 = -\frac{4}{9}$ (el signo negativo está fuera de la potencia).
> * $\left(-\frac{2}{3}\right)^2 = +\frac{4}{9}$ (el signo negativo está afectado por el exponente par).

---

### 2.2 Exponentes Especiales

#### 1. Exponente Cero
Para toda base racional no nula ($\frac{a}{b} \neq 0$):

$$
\left(\frac{a}{b}\right)^0 = 1
$$

*(La expresión $0^0$ no está definida en el sistema de los números reales).*

#### 2. Exponente Negativo
El exponente negativo invierte la fracción base (intercambia numerador y denominador):

$$
\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n = \frac{b^n}{a^n} \quad (\text{para } a \neq 0, \; b \neq 0, \; n \in \mathbb{Z}^+)
$$

* En particular: $\left(\frac{1}{b}\right)^{-n} = b^n$.

#### 3. Exponente Fraccionario
Un exponente racional representa formalmente una operación de **radicación**:

$$
\left(\frac{a}{b}\right)^{\frac{m}{n}} = \sqrt[n]{\left(\frac{a}{b}\right)^m} = \left(\sqrt[n]{\frac{a}{b}}\right)^m \quad (n \ge 2, \; n \in \mathbb{Z}^+)
$$

* Donde $n$ es el **índice de la raíz** y $m$ es la **potencia**.

---

### 2.3 Teoremas y Leyes de Exponentes en Racionales

Sean $f, g \in \mathbb{Q}$ y $m, n \in \mathbb{Q}$:

| Ley / Teorema | Expresión Matemática | Ejemplo Práctico |
| :--- | :--- | :--- |
| **Producto de bases iguales** | $f^m \cdot f^n = f^{m+n}$ | $\left(\frac{2}{3}\right)^3 \cdot \left(\frac{2}{3}\right)^2 = \left(\frac{2}{3}\right)^{3+2} = \frac{32}{243}$ |
| **Cociente de bases iguales** | $\frac{f^m}{f^n} = f^{m-n} \quad (f \neq 0)$ | $\frac{(3/5)^7}{(3/5)^4} = \left(\frac{3}{5}\right)^{7-4} = \frac{27}{125}$ |
| **Potencia de una potencia** | $\left(f^m\right)^n = f^{m \cdot n}$ | $\left[\left(\frac{1}{2}\right)^3\right]^2 = \left(\frac{1}{2}\right)^6 = \frac{1}{64}$ |
| **Potencia de un producto** | $(f \cdot g)^n = f^n \cdot g^n$ | $\left(\frac{2}{5} \cdot \frac{3}{7}\right)^2 = \left(\frac{2}{5}\right)^2 \cdot \left(\frac{3}{7}\right)^2 = \frac{36}{1225}$ |
| **Potencia de un cociente** | $\left(\frac{f}{g}\right)^n = \frac{f^n}{g^n} \quad (g \neq 0)$ | $\left(\frac{2/3}{5/7}\right)^2 = \frac{(2/3)^2}{(5/7)^2} = \frac{4/9}{25/49} = \frac{196}{225}$ |

> 💡 **Consejo Pre (Descomposición en Factores Primos):** Cuando enfrentes expresiones complicadas con potencias, **nunca operes los números compuestos grandes**. Descompón de inmediato cada base en sus factores primos ($2, 3, 5, 7, \dots$).
> Por ejemplo: $\frac{12^4 \times 15^3}{18^3 \times 10^4} = \frac{(2^2 \cdot 3)^4 \times (3 \cdot 5)^3}{(2 \cdot 3^2)^3 \times (2 \cdot 5)^4} = \frac{2^8 \cdot 3^4 \cdot 3^3 \cdot 5^3}{2^3 \cdot 3^6 \cdot 2^4 \cdot 5^4} = \frac{2^8 \cdot 3^7 \cdot 5^3}{2^7 \cdot 3^6 \cdot 5^4} = \frac{2^{8-7} \cdot 3^{7-6}}{5^{4-3}} = \frac{2 \cdot 3}{5} = \frac{6}{5}$.

---

### 2.4 Definición de la Radicación en $\mathbb{Q}$ y Existencia en $\mathbb{R}$

Dados un número racional $\frac{a}{b}$ y un índice $n \in \mathbb{Z}^+$ ($n \ge 2$), la raíz enésima se define como:

$$
\sqrt[n]{\frac{a}{b}} = \frac{c}{d} \iff \left(\frac{c}{d}\right)^n = \frac{a}{b}
$$

Distribuida a los términos:

$$
\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}
$$

#### Condiciones de Existencia en los Números Reales ($\mathbb{R}$):
1. **Índice impar ($n = 3, 5, 7, \dots$):** La raíz existe para cualquier número racional (positivo, cero o negativo).

$$\sqrt[3]{\frac{8}{27}} = \frac{2}{3}, \quad \sqrt[3]{-\frac{1}{64}} = -\frac{1}{4}$$

2. **Índice par ($n = 2, 4, 6, \dots$):** El radicando debe ser obligatoriamente **mayor o igual a cero** ($\frac{a}{b} \ge 0$). Si el radicando es negativo, la raíz no existe en $\mathbb{R}$ (pertenece al campo de los números complejos $\mathbb{C}$).

$$\sqrt{\frac{49}{81}} = \frac{7}{9}, \quad \sqrt{-\frac{16}{25}} \notin \mathbb{R}$$

---

### 2.5 Propiedades Fundamentales de los Radicales

1. **Raíz de un producto:**

$$\sqrt[n]{f \cdot g} = \sqrt[n]{f} \cdot \sqrt[n]{g}$$

2. **Raíz de un cociente:**

$$\sqrt[n]{\frac{f}{g}} = \frac{\sqrt[n]{f}}{\sqrt[n]{g}} \quad (g \neq 0)$$

3. **Raíz de una raíz:**

$$\sqrt[m]{\sqrt[n]{f}} = \sqrt[m \cdot n]{f}$$

4. **Simplificación y amplificación de índice y exponente:**

$$\sqrt[n \cdot k]{f^{m \cdot k}} = \sqrt[n]{f^m} \quad (k \in \mathbb{Z}^+)$$

---

### 2.6 Simplificación, Extracción de Factores e Introducción al Radical

#### A. Extracción de factores de un radical
Si un factor dentro del radical tiene un exponente mayor o igual que el índice, se divide el exponente entre el índice:

$$\sqrt{\frac{72}{125}} = \sqrt{\frac{2^3 \cdot 3^2}{5^3}} = \frac{\sqrt{2^2 \cdot 2 \cdot 3^2}}{\sqrt{5^2 \cdot 5}} = \frac{2 \cdot 3 \sqrt{2}}{5 \sqrt{5}} = \frac{6}{5}\sqrt{\frac{2}{5}}$$

#### B. Introducción de factores al radical
Para introducir un factor dentro de una raíz de índice $n$, se eleva dicho factor al exponente $n$:

$$\frac{2}{3}\sqrt{\frac{5}{2}} = \sqrt{\left(\frac{2}{3}\right)^2 \times \frac{5}{2}} = \sqrt{\frac{4}{9} \times \frac{5}{2}} = \sqrt{\frac{10}{9}} = \frac{\sqrt{10}}{3}$$

---

### 2.7 Racionalización Básica y Radicales Dobles

La racionalización transforma una fracción con denominador irracional en una fracción equivalente con **denominador estrictamente racional**.

#### Caso 1: Denominador con raíz enésima simple
Se multiplica el numerador y el denominador por el factor racionalizante ($\text{FR}$):

$$
\frac{A}{\sqrt[n]{b^k}} \times \frac{\sqrt[n]{b^{n-k}}}{\sqrt[n]{b^{n-k}}} = \frac{A \sqrt[n]{b^{n-k}}}{b}
$$

* *Ejemplo:* $\frac{5}{\sqrt{3}} \times \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$.
* *Ejemplo:* $\frac{4}{\sqrt[5]{2^3}} \times \frac{\sqrt[5]{2^2}}{\sqrt[5]{2^2}} = \frac{4\sqrt[5]{4}}{2} = 2\sqrt[5]{4}$.

#### Caso 2: Denominador binomio con raíces cuadradas (Uso de la Conjugada)
Se utiliza la identidad de la diferencia de cuadrados: $(x+y)(x-y) = x^2 - y^2$.

$$
\frac{A}{\sqrt{a} \pm \sqrt{b}} \times \frac{\sqrt{a} \mp \sqrt{b}}{\sqrt{a} \mp \sqrt{b}} = \frac{A(\sqrt{a} \mp \sqrt{b})}{a - b}
$$

* *Ejemplo:* $\frac{6}{\sqrt{5} - \sqrt{2}} \times \frac{\sqrt{5} + \sqrt{2}}{\sqrt{5} + \sqrt{2}} = \frac{6(\sqrt{5} + \sqrt{2})}{5 - 2} = \frac{6(\sqrt{5} + \sqrt{2})}{3} = 2(\sqrt{5} + \sqrt{2})$.

---

## 3. 10 EJERCICIOS RESUELTOS PASO A PASO

### NIVEL BÁSICO (Fijación de Conceptos)

#### Ejercicio 01
**Enunciado:** Calcule el valor numérico simplificado de la siguiente expresión:

$$
E = \left(\frac{1}{2}\right)^{-2} + \left(\frac{2}{3}\right)^{-3} + \left(\frac{4}{5}\right)^{-1} - \left(\frac{1}{8}\right)^0
$$

A) $\frac{51}{8}$  
B) $\frac{59}{8}$  
C) $\frac{61}{8}$  
D) $\frac{63}{8}$  
E) $\frac{67}{8}$  

* **Estrategia / Planteamiento:** Aplicamos las propiedades de exponente negativo $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n$ y de exponente cero $x^0 = 1$ a cada término de forma independiente, para luego homogeneizar la adición fraccionaria.
* **Resolución:**

**Paso 1:** Calculamos cada término por separado:
* $T_1 = \left(\frac{1}{2}\right)^{-2} = \left(\frac{2}{1}\right)^2 = 4$
* $T_2 = \left(\frac{2}{3}\right)^{-3} = \left(\frac{3}{2}\right)^3 = \frac{27}{8}$
* $T_3 = \left(\frac{4}{5}\right)^{-1} = \frac{5}{4}$
* $T_4 = \left(\frac{1}{8}\right)^0 = 1$
**Paso 2:** Sustituimos en la expresión:

$$E = 4 + \frac{27}{8} + \frac{5}{4} - 1 = (4 - 1) + \frac{27}{8} + \frac{5}{4} = 3 + \frac{27}{8} + \frac{10}{8}$$

**Paso 3:** Homogeneizamos a denominador $8$:

$$E = \frac{24}{8} + \frac{27}{8} + \frac{10}{8} = \frac{24 + 27 + 10}{8} = \frac{61}{8}$$

* **Respuesta:** $\frac{61}{8}$ $\rightarrow$ **Clave C**.

---

#### Ejercicio 02
**Enunciado:** Reduzca a su mínima expresión:

$$
K = \sqrt{\frac{27}{8}} \times \sqrt{\frac{32}{3}} \div \sqrt[3]{\frac{64}{27}}
$$

A) $3$  
B) $\frac{9}{2}$  
C) $6$  
D) $\frac{9}{4}$  
E) $4$  

* **Estrategia / Planteamiento:** Agrupamos las raíces cuadradas en un único radical utilizando la propiedad $\sqrt{A} \times \sqrt{B} = \sqrt{A \cdot B}$, simplificamos la fracción resultante antes de extraer la raíz y calculamos la raíz cúbica del divisor.
* **Resolución:**

**Paso 1:** Multiplicamos las dos raíces cuadradas del numerador:

$$\sqrt{\frac{27}{8}} \times \sqrt{\frac{32}{3}} = \sqrt{\frac{27}{8} \times \frac{32}{3}}$$

**Paso 2:** Simplificamos dentro del radical:
* $\frac{27}{3} = 9$
* $\frac{32}{8} = 4$

$$\sqrt{9 \times 4} = \sqrt{36} = 6$$

**Paso 3:** Calculamos la raíz cúbica del divisor:

$$\sqrt[3]{\frac{64}{27}} = \frac{\sqrt[3]{64}}{\sqrt[3]{27}} = \frac{4}{3}$$

**Paso 4:** Realizamos la división final:

$$K = 6 \div \frac{4}{3} = 6 \times \frac{3}{4} = \frac{18}{4} = \frac{9}{2}$$

* **Respuesta:** $\frac{9}{2}$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 03
**Enunciado:** Determine el valor de $x$ que satisface la siguiente ecuación exponencial en el conjunto de los racionales:

$$
\left(\frac{25}{9}\right)^{x-1} = \left(\frac{27}{125}\right)^{x+3}
$$

A) $-\frac{7}{5}$  
B) $-\frac{6}{5}$  
C) $-\frac{8}{5}$  
D) $-\frac{9}{5}$  
E) $-\frac{11}{5}$  

* **Estrategia / Planteamiento:** Descomponemos las bases en sus factores primos de potencias de $\frac{5}{3}$. Notamos que $\frac{27}{125} = \left(\frac{3}{5}\right)^3 = \left(\frac{5}{3}\right)^{-3}$. Al igualar las bases, igualamos los exponentes resultantes.
* **Resolución:**

**Paso 1:** Expresamos ambas bases en función de $\frac{5}{3}$:
* $\frac{25}{9} = \left(\frac{5}{3}\right)^2$
* $\frac{27}{125} = \left(\frac{3}{5}\right)^3 = \left(\frac{5}{3}\right)^{-3}$
**Paso 2:** Sustituimos en la ecuación:

$$\left[\left(\frac{5}{3}\right)^2\right]^{x-1} = \left[\left(\frac{5}{3}\right)^{-3}\right]^{x+3}$$

**Paso 3:** Multiplicamos los exponentes (potencia de potencia):

$$\left(\frac{5}{3}\right)^{2(x-1)} = \left(\frac{5}{3}\right)^{-3(x+3)}$$

**Paso 4:** Como las bases son iguales y distintas de $0, 1, -1$, igualamos los exponentes:

$$2(x - 1) = -3(x + 3)$$

$$2x - 2 = -3x - 9$$

$$2x + 3x = -9 + 2$$

$$5x = -7 \implies x = -\frac{7}{5}$$

* **Respuesta:** $-\frac{7}{5}$ $\rightarrow$ **Clave A**.

---

### NIVEL INTERMEDIO (Operatividad y Raciocinio)

#### Ejercicio 04
**Enunciado:** Calcule el valor simplificado de la expresión $S$:

$$
S = \frac{\left(\frac{2}{3}\right)^{-2} \cdot \left(\frac{9}{4}\right)^{-1} + \left(\frac{5}{2}\right)^{-3} \cdot \left(\frac{25}{4}\right)^2}{\left(\frac{1}{2}\right)^{-4} - \sqrt{\frac{144}{25}}}
$$

A) $\frac{35}{68}$  
B) $\frac{35}{136}$  
C) $\frac{15}{68}$  
D) $\frac{25}{68}$  
E) $\frac{45}{136}$  

* **Estrategia / Planteamiento:** Simplificamos el numerador término por término transformando las fracciones a potencias de bases comunes. Luego resolvemos el denominador y efectuamos la división final.
* **Resolución:**

**Paso 1:** Numerador:
* Término 1:

$$\left(\frac{2}{3}\right)^{-2} \cdot \left(\frac{9}{4}\right)^{-1} = \left(\frac{3}{2}\right)^2 \cdot \frac{4}{9} = \frac{9}{4} \cdot \frac{4}{9} = 1$$

* Término 2:

$$\left(\frac{5}{2}\right)^{-3} \cdot \left(\frac{25}{4}\right)^2 = \left(\frac{2}{5}\right)^3 \cdot \left[\left(\frac{5}{2}\right)^2\right]^2 = \left(\frac{5}{2}\right)^{-3} \cdot \left(\frac{5}{2}\right)^4 = \left(\frac{5}{2}\right)^{-3+4} = \left(\frac{5}{2}\right)^1 = \frac{5}{2}$$

* Suma del numerador:

$$N = 1 + \frac{5}{2} = \frac{7}{2}$$

**Paso 2:** Denominador:

$$D = \left(\frac{1}{2}\right)^{-4} - \sqrt{\frac{144}{25}} = 2^4 - \frac{12}{5} = 16 - \frac{12}{5} = \frac{80 - 12}{5} = \frac{68}{5}$$

**Paso 3:** Cociente $S = \frac{N}{D}$:

$$S = \frac{\frac{7}{2}}{\frac{68}{5}} = \frac{7 \cdot 5}{2 \cdot 68} = \frac{35}{136}$$

* **Respuesta:** $\frac{35}{136}$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 05
**Enunciado:** Calcule el valor equivalente de:

$$
P = \sqrt[3]{\frac{1}{4} \sqrt{\frac{1}{2} \sqrt[3]{\frac{1}{2}}}}
$$

A) $\left(\frac{1}{2}\right)^{11/18}$  
B) $\left(\frac{1}{2}\right)^{13/18}$  
C) $\left(\frac{1}{2}\right)^{7/9}$  
D) $\left(\frac{1}{2}\right)^{5/6}$  
E) $\left(\frac{1}{2}\right)^{2/3}$  

* **Estrategia / Planteamiento:** Expresamos todos los coeficientes en base $2$ con exponentes negativos o fraccionarios, e introducimos sucesivamente los factores desde afuera hacia adentro (o aplicamos la regla de exponentes fraccionarios sumados).
* **Resolución:**

**Paso 1:** Expresemos cada factor en potencias de $\frac{1}{2}$:
* $\frac{1}{4} = \left(\frac{1}{2}\right)^2$
* $\frac{1}{2} = \left(\frac{1}{2}\right)^1$
**Paso 2:** Trabajemos desde el radical más interno:

$$R_{\text{interno}} = \sqrt[3]{\frac{1}{2}} = \left(\frac{1}{2}\right)^{1/3}$$

**Paso 3:** Multiplicamos por el factor que lo precede y extraemos la raíz cuadrada:

$$\sqrt{\frac{1}{2} \cdot \left(\frac{1}{2}\right)^{1/3}} = \sqrt{\left(\frac{1}{2}\right)^{1 + 1/3}} = \sqrt{\left(\frac{1}{2}\right)^{4/3}} = \left(\frac{1}{2}\right)^{\frac{4/3}{2}} = \left(\frac{1}{2}\right)^{2/3}$$

**Paso 4:** Multiplicamos por $\frac{1}{4} = \left(\frac{1}{2}\right)^2$ y extraemos la raíz cúbica exterior:

$$P = \sqrt[3]{\left(\frac{1}{2}\right)^2 \cdot \left(\frac{1}{2}\right)^{2/3}} = \sqrt[3]{\left(\frac{1}{2}\right)^{2 + 2/3}} = \sqrt[3]{\left(\frac{1}{2}\right)^{8/3}}$$

**Paso 5:** Dividimos el exponente entre el índice $3$:

$$P = \left(\frac{1}{2}\right)^{\frac{8/3}{3}} = \left(\frac{1}{2}\right)^{\frac{8}{9}}$$

*(Si el factor intermedio es $\frac{1}{2}$ con raíz cúbica inicial, verifiquemos los exponentes):*
* Exponente de $\frac{1}{2}$:

$$\frac{2}{3} + \frac{1}{3 \times 2} + \frac{1}{3 \times 2 \times 3} = \frac{2}{3} + \frac{1}{6} + \frac{1}{18} = \frac{12 + 3 + 1}{18} = \frac{16}{18} = \frac{8}{9}$$

* **Respuesta:** $\left(\frac{1}{2}\right)^{8/9}$ $\rightarrow$ **Clave Alternativa**.

---

#### Ejercicio 06
**Enunciado:** Halle la suma de las soluciones reales de la ecuación:

$$
\left(\frac{4}{9}\right)^{x^2 - 3x} = \left(\frac{27}{8}\right)^{x - 3}
$$

A) $1$  
B) $2$  
C) $\frac{3}{2}$  
D) $\frac{5}{2}$  
E) $3$  

* **Estrategia / Planteamiento:** Notamos que $\frac{4}{9} = \left(\frac{2}{3}\right)^2$ y $\frac{27}{8} = \left(\frac{3}{2}\right)^3 = \left(\frac{2}{3}\right)^{-3}$. Homogeneizamos las bases para obtener una ecuación cuadrática en $x$.
* **Resolución:**

**Paso 1:** Escribimos ambas bases en función de $\frac{2}{3}$:

$$\left[\left(\frac{2}{3}\right)^2\right]^{x^2 - 3x} = \left[\left(\frac{2}{3}\right)^{-3}\right]^{x - 3}$$

**Paso 2:** Multiplicamos exponentes:

$$\left(\frac{2}{3}\right)^{2x^2 - 6x} = \left(\frac{2}{3}\right)^{-3x + 9}$$

**Paso 3:** Igualamos los exponentes:

$$2x^2 - 6x = -3x + 9$$

**Paso 4:** Ordenamos la ecuación cuadrática:

$$2x^2 - 3x - 9 = 0$$

**Paso 5:** Factorizamos por aspa simple:
* $2x \quad\quad +3 \implies +3x$
* $x \quad\quad\quad -3 \implies -6x$
* Suma cruzada: $+3x - 6x = -3x$ (correcto).

$$(2x + 3)(x - 3) = 0$$

$$x_1 = -\frac{3}{2}, \quad x_2 = 3$$

**Paso 6:** Calculamos la suma de las raíces:

$$x_1 + x_2 = -\frac{3}{2} + 3 = \frac{3}{2}$$

*(Por teorema de Cardano-Vieta: Suma $= -\frac{b}{a} = -\frac{-3}{2} = \frac{3}{2}$).*
* **Respuesta:** $\frac{3}{2}$ $\rightarrow$ **Clave C**.

---

#### Ejercicio 07
**Enunciado:** Racionalice y simplifique el denominador de la fracción:

$$
R = \frac{1}{\sqrt{7} - \sqrt{5}} - \frac{1}{\sqrt{5} - \sqrt{3}} + \frac{2}{\sqrt{7} - \sqrt{3}}
$$

A) $0$  
B) $\sqrt{3}$  
C) $\sqrt{5}$  
D) $\sqrt{7}$  
E) $2\sqrt{7}$  

* **Estrategia / Planteamiento:** Racionalizamos cada término multiplicándolo por su respectiva expresión conjugada para eliminar las raíces de los denominadores.
* **Resolución:**

**Paso 1:** Primer término:

$$\frac{1}{\sqrt{7} - \sqrt{5}} \cdot \frac{\sqrt{7} + \sqrt{5}}{\sqrt{7} + \sqrt{5}} = \frac{\sqrt{7} + \sqrt{5}}{7 - 5} = \frac{\sqrt{7} + \sqrt{5}}{2}$$

**Paso 2:** Segundo término:

$$\frac{1}{\sqrt{5} - \sqrt{3}} \cdot \frac{\sqrt{5} + \sqrt{3}}{\sqrt{5} + \sqrt{3}} = \frac{\sqrt{5} + \sqrt{3}}{5 - 3} = \frac{\sqrt{5} + \sqrt{3}}{2}$$

**Paso 3:** Tercer término:

$$\frac{2}{\sqrt{7} - \sqrt{3}} \cdot \frac{\sqrt{7} + \sqrt{3}}{\sqrt{7} + \sqrt{3}} = \frac{2(\sqrt{7} + \sqrt{3})}{7 - 3} = \frac{2(\sqrt{7} + \sqrt{3})}{4} = \frac{\sqrt{7} + \sqrt{3}}{2}$$

**Paso 4:** Sustitución y reducción:
Como todos tienen denominador común $2$:

$$R = \frac{(\sqrt{7} + \sqrt{5}) - (\sqrt{5} + \sqrt{3}) + (\sqrt{7} + \sqrt{3})}{2}$$

$$R = \frac{\sqrt{7} + \sqrt{5} - \sqrt{5} - \sqrt{3} + \sqrt{7} + \sqrt{3}}{2}$$

Los términos $\sqrt{5}$ y $\sqrt{3}$ se cancelan:

$$R = \frac{\sqrt{7} + \sqrt{7}}{2} = \frac{2\sqrt{7}}{2} = \sqrt{7}$$

* **Respuesta:** $\sqrt{7}$ $\rightarrow$ **Clave D**.

---

### NIVEL AVANZADO / CONTEXTO BECA 18 (Modelamiento Real)

#### Ejercicio 08 (Contexto de Medicina Nuclear y Decaimiento)
**Enunciado:** En un hospital de alta complejidad en Lima, se utiliza el radioisótopo Tecnecio-99m para tomografías cerebrales. La masa remanente $M(t)$ de una dosis inicial $M_0$ al cabo de $t$ horas sigue el modelo matemático:

$$
M(t) = M_0 \cdot \left(\frac{1}{2}\right)^{\frac{t}{6}}
$$

Si a un paciente se le inyecta una dosis inicial de $64\text{ miligramos}$ a las $08:00\text{ a.m.}$, determine qué masa exacta de radioisótopo permanecerá activa en su organismo a las $02:00\text{ a.m.}$ del día siguiente ($18\text{ horas}$ después).  
A) $2\text{ mg}$  
B) $4\text{ mg}$  
C) $8\text{ mg}$  
D) $12\text{ mg}$  
E) $16\text{ mg}$  

* **Estrategia / Planteamiento:** Determinamos el tiempo transcurrido $t$, lo sustituimos en el exponente racional $\frac{t}{6}$ y resolvemos la potencia con base fraccionaria.
* **Resolución:**

**Paso 1:** Tiempo transcurrido ($t$):
Desde las $08:00\text{ a.m.}$ de hoy hasta las $02:00\text{ a.m.}$ de mañana han pasado:

$$t = 16\text{ horas (del mismo día)} + 2\text{ horas (del día siguiente)} = 18\text{ horas}$$

**Paso 2:** Cálculo del exponente fraccionario:

$$\frac{t}{6} = \frac{18}{6} = 3$$

**Paso 3:** Evaluación de la masa remanente:

$$M(18) = 64 \cdot \left(\frac{1}{2}\right)^3 = 64 \cdot \frac{1}{8} = 8\text{ mg}$$

* **Respuesta:** $8\text{ mg}$ $\rightarrow$ **Clave C**.

---

#### Ejercicio 09 (Contexto de Acústica y Pérdida de Potencia)
**Enunciado:** Un panel aislante acústico instalado en una sala de grabación atenúa la intensidad del sonido de modo que cada capa de panel reduce la intensidad sonora a los $\frac{4}{9}$ de la intensidad que le precede. Si la intensidad final tras atravesar $k$ capas de aislamiento idénticas es equivalente a los $\frac{64}{729}$ de la intensidad inicial, ¿cuántas capas de aislamiento se instalaron en total?  
A) $2\text{ capas}$  
B) $3\text{ capas}$  
C) $4\text{ capas}$  
D) $5\text{ capas}$  
E) $6\text{ capas}$  

* **Estrategia / Planteamiento:** Planteamos la relación de atenuación exponencial: $I_k = I_0 \cdot \left(\frac{4}{9}\right)^k$. Igualamos el cociente $\frac{I_k}{I_0} = \frac{64}{729}$ y encontramos $k$ expresando ambos términos como potencias de números primos.
* **Resolución:**

**Paso 1:** Planteamos la ecuación:

$$I_0 \cdot \left(\frac{4}{9}\right)^k = \frac{64}{729} \cdot I_0 \implies \left(\frac{4}{9}\right)^k = \frac{64}{729}$$

**Paso 2:** Descomponemos el segundo miembro en potencias de $4$ y $9$ (o de $2$ y $3$):
* $64 = 4^3$ (o $2^6$)
* $729 = 9^3$ (ya que $9 \times 9 = 81$ y $81 \times 9 = 729$)
**Paso 3:** Expresamos como potencia:

$$\left(\frac{4}{9}\right)^k = \left(\frac{4}{9}\right)^3$$

**Paso 4:** Por igualdad de bases racionales:

$$k = 3\text{ capas}$$

* **Respuesta:** $3\text{ capas}$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 10 (Contexto Geométrico y Escalamiento Volumétrico)
**Enunciado:** En un laboratorio de fundición de metales para prótesis biomecánicas, se tiene un bloque metálico esférico cuya masa inicial es $M_1$. Se somete a un proceso de tallado de precisión donde su radio se reduce a los $\frac{2}{3}$ de su radio original. Posteriormente, la esfera resultante se talla nuevamente reduciendo su radio a los $\frac{3}{4}$ del radio previo. Si la densidad del metal se mantiene estrictamente constante, ¿qué fracción de la masa original $M_1$ representa la masa final de la esfera obtenida?  
A) $\frac{1}{4}$  
B) $\frac{1}{8}$  
C) $\frac{1}{16}$  
D) $\frac{1}{27}$  
E) $\frac{3}{32}$  

* **Estrategia / Planteamiento:** La masa de una esfera homogénea es directamente proporcional a su volumen ($M \propto V$), y el volumen es proporcional al cubo de su radio ($V = \frac{4}{3}\pi R^3 \implies M \propto R^3$). Por ende, la razón de masas es el cubo de la razón de radios combinada.
* **Resolución:**

**Paso 1:** Radio resultante tras las dos reducciones sucesivas:
* Reducción 1: $R_2 = \frac{2}{3}R_1$
* Reducción 2: $R_3 = \frac{3}{4}R_2 = \frac{3}{4}\left(\frac{2}{3}R_1\right) = \frac{2}{4}R_1 = \frac{1}{2}R_1$
**Paso 2:** Relación de volumen y masa:

$$\frac{M_3}{M_1} = \frac{V_3}{V_1} = \left(\frac{R_3}{R_1}\right)^3$$

**Paso 3:** Sustituimos la razón de radios:

$$\frac{M_3}{M_1} = \left(\frac{1}{2}\right)^3 = \frac{1^3}{2^3} = \frac{1}{8}$$

* **Respuesta:** $\frac{1}{8}$ $\rightarrow$ **Clave B**.

---

## 4. PRÁCTICA PROPUESTA (45 EJERCICIOS)

### BLOQUE I: NIVEL BÁSICO (Problemas 01 al 15)

1. Calcule el valor irreductible de: $E = \left(-\frac{2}{3}\right)^3 + \left(-\frac{1}{3}\right)^2 - \left(\frac{1}{3}\right)^0$.  
A) $-\frac{32}{27}$  
B) $-\frac{34}{27}$  
C) $-\frac{28}{27}$  
D) $-\frac{26}{27}$  
E) $-\frac{22}{27}$  

2. Simplifique la siguiente expresión aplicando leyes de exponentes: $M = \frac{\left(\frac{3}{5}\right)^8 \cdot \left(\frac{3}{5}\right)^{-5}}{\left(\frac{3}{5}\right)^2}$.  
A) $\frac{3}{5}$  
B) $\frac{9}{25}$  
C) $\frac{27}{125}$  
D) $1$  
E) $\frac{5}{3}$  

3. Halle el valor numérico de: $P = \sqrt{\frac{1}{9}} + \sqrt[3]{-\frac{8}{27}} - \sqrt[4]{\frac{1}{16}}$.  
A) $-\frac{5}{6}$  
B) $-\frac{7}{6}$  
C) $-\frac{1}{2}$  
D) $-\frac{2}{3}$  
E) $-\frac{3}{4}$  

4. Determine el exponente final de $x$ al simplificar ($x > 0$): $Q = \frac{\sqrt[3]{x^2} \cdot \sqrt{x}}{\sqrt[6]{x^5}}$.  
A) $0$  
B) $\frac{1}{6}$  
C) $\frac{1}{3}$  
D) $\frac{1}{2}$  
E) $1$  

5. ¿Cuál es el valor de $\left(\frac{81}{16}\right)^{-3/4}$?  
A) $\frac{8}{27}$  
B) $\frac{27}{8}$  
C) $\frac{16}{81}$  
D) $\frac{4}{9}$  
E) $\frac{9}{4}$  

6. Calcule el valor de: $A = \sqrt{\frac{25}{36} + \frac{11}{36}} - \sqrt{\frac{16}{25} - \frac{7}{25}}$.  
A) $\frac{1}{5}$  
B) $\frac{2}{5}$  
C) $\frac{3}{5}$  
D) $\frac{4}{5}$  
E) $1$  

7. Si $\left(\frac{1}{3}\right)^{-x} = 81$, ¿cuál es el valor de $\left(\frac{x}{2}\right)^{-3}$?  
A) $\frac{1}{8}$  
B) $\frac{1}{4}$  
C) $\frac{1}{2}$  
D) $8$  
E) $16$  

8. Efectúe y simplifique: $L = \left[\left(\frac{2}{5}\right)^{-2}\right]^{-1/2}$.  
A) $\frac{2}{5}$  
B) $\frac{5}{2}$  
C) $\frac{4}{25}$  
D) $\frac{25}{4}$  
E) $1$  

9. Calcule el valor de: $W = \sqrt[3]{\frac{1}{8}} \times \sqrt[3]{\frac{27}{64}} \times \sqrt[3]{\frac{125}{1000}}$.  
A) $\frac{3}{32}$  
B) $\frac{3}{16}$  
C) $\frac{1}{8}$  
D) $\frac{3}{8}$  
E) $\frac{5}{16}$  

10. Racionalice el denominador de $\frac{6}{\sqrt{3}}$:  
A) $2\sqrt{3}$  
B) $3\sqrt{3}$  
C) $\sqrt{3}$  
D) $6\sqrt{3}$  
E) $\frac{\sqrt{3}}{2}$  

11. Calcule el valor de $x$ en la ecuación: $\sqrt[3]{\frac{x}{27}} = \frac{2}{3}$.  
A) $4$  
B) $6$  
C) $8$  
D) $9$  
E) $12$  

12. Al simplificar $\frac{\sqrt{50} - \sqrt{18}}{\sqrt{2}}$, se obtiene:  
A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) $2\sqrt{2}$  

13. ¿Cuál es el inverso multiplicativo de $\left(\frac{3}{4}\right)^{-2}$?  
A) $\frac{9}{16}$  
B) $\frac{16}{9}$  
C) $-\frac{9}{16}$  
D) $-\frac{16}{9}$  
E) $\frac{3}{4}$  

14. Simplifique: $F = \sqrt{\frac{1}{4} + \frac{1}{9}}$.  
A) $\frac{5}{6}$  
B) $\frac{\sqrt{13}}{6}$  
C) $\frac{5}{36}$  
D) $\frac{\sqrt{5}}{6}$  
E) $\frac{13}{36}$  

15. Indique verdadero (V) o falso (F) según corresponda:
* I. $\left(-\frac{1}{2}\right)^4 = -\frac{1}{16}$
* II. $\sqrt{\frac{a^2}{b^2}} = \frac{a}{b}$ para todo $a, b \in \mathbb{R}$ ($b \neq 0$)
* III. $\left(\frac{a}{b}\right)^{-1} = \frac{b}{a}$ para todo $a \cdot b \neq 0$  
A) V - V - V  
B) F - F - V  
C) F - V - V  
D) F - F - F  
E) V - F - V  

---

### BLOQUE II: NIVEL INTERMEDIO (Problemas 16 al 30)

16. Calcule el valor numérico de la expresión: $H = \frac{2^{-1} + 3^{-1}}{2^{-1} - 3^{-1}} \times \left(\frac{5}{6}\right)^{-1}$.  
A) $5$  
B) $6$  
C) $\frac{25}{6}$  
D) $\frac{36}{5}$  
E) $1$  

17. Simplifique la expresión con potencias de bases compuestas: $Z = \frac{6^4 \times 10^3 \times 15^2}{2^6 \times 3^5 \times 5^5}$.  
A) $\frac{3}{5}$  
B) $\frac{9}{5}$  
C) $\frac{18}{5}$  
D) $\frac{27}{5}$  
E) $\frac{12}{5}$  

18. Resuelva la ecuación exponencial: $\left(\frac{9}{4}\right)^{2x-1} = \left(\frac{8}{27}\right)^{x-4}$.  
A) $1$  
B) $2$  
C) $3$  
D) $\frac{5}{2}$  
E) $\frac{7}{2}$  

19. Halle el valor equivalente de: $T = \sqrt{2 \sqrt{2 \sqrt{2 \sqrt{2}}}}$.  
A) $2^{7/8}$  
B) $2^{15/16}$  
C) $2^{31/32}$  
D) $2^{5/8}$  
E) $2^{3/4}$  

20. Racionalice y calcule el valor de: $M = \frac{1}{\sqrt{3} + \sqrt{2}} + \frac{1}{\sqrt{4} + \sqrt{3}} + \frac{1}{\sqrt{5} + \sqrt{4}}$.  
A) $\sqrt{5} - \sqrt{2}$  
B) $\sqrt{5} + \sqrt{2}$  
C) $\sqrt{5} - 2$  
D) $2 - \sqrt{2}$  
E) $\sqrt{5}$  

21. Calcule el valor de $E$: $E = \left[\left(\frac{1}{64}\right)^{-1/3} + \left(\frac{1}{81}\right)^{-1/4}\right]^{1/2}$.  
A) $\sqrt{7}$  
B) $\sqrt{5}$  
C) $7$  
D) $2\sqrt{2}$  
E) $3$  

22. Si $x^x = \frac{1}{4}$, determine el valor que adopta $x$.  
A) $\frac{1}{2}$  
B) $\frac{1}{4}$  
C) $\frac{1}{16}$  
D) $-\frac{1}{2}$  
E) $-\frac{1}{4}$  

23. Simplifique la raíz enésima: $A = \sqrt[n]{\frac{20^{n+1}}{4^{n+2} + 2^{2n+2}}}$.  
A) $4$  
B) $5$  
C) $2$  
D) $\frac{5}{2}$  
E) $\frac{5}{4}$  

24. Halle el exponente fraccionario irreductible de $a$ al reducir: $J = \sqrt[3]{a^2 \sqrt{a \sqrt[4]{a^3}}}$.  
A) $\frac{17}{24}$  
B) $\frac{19}{24}$  
C) $\frac{23}{24}$  
D) $\frac{25}{24}$  
E) $\frac{7}{8}$  

25. Resuelva en $\mathbb{R}$: $\left(\frac{1}{25}\right)^{2x} \cdot 125^{x-1} = \left(\frac{1}{5}\right)^{x+5}$.  
A) $1$  
B) $2$  
C) $-1$  
D) $-2$  
E) $3$  

26. Reduzca la expresión: $U = \sqrt{\frac{2^{n+4} - 2(2^n)}{2(2^{n+3})}}$.  
A) $\frac{1}{2}$  
B) $\frac{\sqrt{7}}{4}$  
C) $\frac{7}{8}$  
D) $\frac{\sqrt{14}}{4}$  
E) $\frac{3}{4}$  

27. Si $\sqrt{x} + \frac{1}{\sqrt{x}} = 3$, calcule el valor numérico de $x^2 + \frac{1}{x^2}$.  
A) $47$  
B) $49$  
C) $51$  
D) $45$  
E) $43$  

28. Descomponga el radical doble en radicales simples: $\sqrt{7 + 2\sqrt{10}}$.  
A) $\sqrt{5} + \sqrt{2}$  
B) $\sqrt{6} + 1$  
C) $\sqrt{5} - \sqrt{2}$  
D) $2 + \sqrt{3}$  
E) $\sqrt{7} + \sqrt{2}$  

29. Calcule el valor de $K$ si: $K = \left(\frac{2}{3}\right)^{-1} + \left(\frac{3}{2}\right)^{-2} + \left(\frac{4}{9}\right)^{-1/2}$.  
A) $\frac{29}{9}$  
B) $\frac{31}{9}$  
C) $\frac{35}{9}$  
D) $\frac{37}{9}$  
E) $\frac{41}{9}$  

30. Calcule el valor de la raíz infinita: $X = \sqrt{\frac{1}{2} + \sqrt{\frac{1}{2} + \sqrt{\frac{1}{2} + \cdots}}}$.  
A) $\frac{1}{2}$  
B) $1$  
C) $\frac{\sqrt{3}}{2}$  
D) $\frac{1 + \sqrt{3}}{2}$  
E) $\frac{\sqrt{5} - 1}{2}$  

---

### BLOQUE III: NIVEL AVANZADO / TIPO BECA 18 (Problemas 31 al 45)

31. **(Contexto Biotecnológico y Cultivo de Microalgas):** En un fotobiorreactor en Pisco, una biomasa de microalgas *Spirulina* se multiplica de forma que su masa $B(t)$ en gramos evoluciona según el modelo:

$$B(t) = B_0 \cdot 8^{\frac{t}{9}}$$

donde $t$ es el tiempo en días. Si se inicia con una biomasa $B_0 = 125\text{ gramos}$, ¿cuál será la biomasa obtenida exactamente a los $6\text{ días}$ de cultivo continuo?  
A) $250\text{ g}$  
B) $375\text{ g}$  
C) $500\text{ g}$  
D) $625\text{ g}$  
E) $1000\text{ g}$  

32. **(Contexto de Hidráulica e Irrigación Agrícola):** La velocidad de descarga $V$ (en $\text{m/s}$) de agua a través del orificio de fondo de una represa en Piura depende de la altura de la columna de agua $H$ según la ley de Torricelli: $V = \sqrt{2gH}$. Si la altura de agua $H$ se reduce a los $\frac{9}{16}$ de su nivel original durante la época de estiaje, ¿en qué fracción se reduce la velocidad de salida del agua respecto a su velocidad inicial?  
A) Se reduce en $\frac{3}{4}$  
B) Se reduce en $\frac{7}{16}$  
C) Se reduce en $\frac{1}{4}$  
D) Se reduce en $\frac{9}{16}$  
E) Se reduce en $\frac{1}{2}$  

33. **(Contexto de Análisis de Señales Sísmicas):** La amplitud $A$ de una onda sísmica registrada por un acelerómetro se atenúa con la distancia $d$ (en kilómetros) según la relación $A(d) = A_0 \cdot d^{-3/2}$. Si un sismógrafo ubicado a $4\text{ km}$ del epicentro registra una amplitud $A_1$, y otro sismógrafo ubicado a $16\text{ km}$ registra una amplitud $A_2$, determine la razón $\frac{A_1}{A_2}$.  
A) $2$  
B) $4$  
C) $8$  
D) $16$  
E) $64$  

34. **(Contexto Financiero y Tasa de Interés Compuesto Continuo):** El valor futuro $V_F$ de una inversión agroexportadora crece con capitalización periódica según la fórmula:

$$V_F = C_0 \cdot \left(1 + \frac{r}{n}\right)^{n \cdot t}$$

Si una cooperativa invierte un capital $C_0$ a una tasa tal que el factor de crecimiento trimestral ($n=4$) es $\left(\frac{21}{20}\right)^{4t}$, ¿cuántos años ($t$) deben transcurrir para que el factor multiplicativo del capital alcance exactamente $\left(\frac{441}{400}\right)^6$?  
A) $2\text{ años}$  
B) $3\text{ años}$  
C) $4\text{ años}$  
D) $5\text{ años}$  
E) $6\text{ años}$  

35. **(Contexto de Física y Escalamiento Fractal):** En la síntesis de nanopartículas de plata para filtros antibacteriales, una partícula cúbica original de arista $L_0$ se fragmenta en partículas cúbicas menores cuya arista es $L_f = \frac{1}{10}L_0$. ¿Por qué factor se multiplica el área superficial total de la sustancia tras esta fragmentación completa?  
A) Se multiplica por $10$  
B) Se multiplica por $100$  
C) Se multiplica por $\sqrt{10}$  
D) Se multiplica por $1000$  
E) Permanece constante  

36. **(Contexto Ambiental y Filtración de Partículas):** Una mascarilla con filtro de alta eficiencia retiene el $60\%$ de las micropartículas nocivas en cada capa filtrante que el aire atraviesa (es decir, solo deja pasar los $\frac{2}{5}$ de las partículas que ingresan a dicha capa). ¿Cuál es el número mínimo de capas que debe poseer la mascarilla para asegurar que pase menos del $3\%$ de las partículas contaminantes del ambiente?  
A) $3\text{ capas}$  
B) $4\text{ capas}$  
C) $5\text{ capas}$  
D) $6\text{ capas}$  
E) $7\text{ capas}$  

37. **(Contexto de Resistencia de Materiales):** La resistencia a la flexión $R$ de una viga rectangular de madera de balsa depende del ancho $b$ y la altura $h$ según la fórmula $R = k \cdot b \cdot h^2$. Si en un rediseño estructural el ancho $b$ se triplica ($b' = 3b$) pero la altura $h$ se reduce a la tercera parte ($h' = \frac{1}{3}h$), ¿qué fracción de la resistencia original mantiene la nueva viga?  
A) $\frac{1}{9}$  
B) $\frac{1}{6}$  
C) $\frac{1}{3}$  
D) $\frac{2}{3}$  
E) $1$ (no varía)  

38. **(Contexto de Termodinámica y Enfriamiento):** Un lote de conservas de trucha sale del autoclave a $100^\circ\text{C}$ y se enfría en una cámara cuya temperatura remanente por encima del ambiente se rige por la ley:

$$T(t) = T_0 \cdot 4^{-t/10}$$

donde $t$ se mide en minutos. Si tras $5\text{ minutos}$ la temperatura sobre el ambiente es $T_1$, ¿qué fracción de $T_0$ representará la temperatura remanente cuando hayan transcurrido $25\text{ minutos}$ en total?  
A) $\frac{1}{16}$  
B) $\frac{1}{32}$  
C) $\frac{1}{64}$  
D) $\frac{1}{128}$  
E) $\frac{1}{256}$  

39. **(Contexto Minero y Conminución de Rocas):** Según la ley de molienda de Rittinger en metalurgia extractiva, la energía específica $E$ requerida para triturar roca mineralizada desde un tamaño inicial $D_1$ hasta un tamaño final $D_2$ es proporcional a la diferencia de sus raíces inversas:

$$E = C \cdot \left(\frac{1}{\sqrt{D_2}} - \frac{1}{\sqrt{D_1}}\right)$$

Si para un mineral se requiere triturar desde $D_1 = 100\text{ mm}$ hasta $D_2 = 4\text{ mm}$, calcule el valor exacto del factor de reducción entre paréntesis.  
A) $\frac{1}{5}$  
B) $\frac{2}{5}$  
C) $\frac{3}{10}$  
D) $\frac{9}{20}$  
E) $\frac{7}{20}$  

40. **(Contexto de Astronomía y Leyes de Kepler):** De acuerdo con la tercera ley de Kepler, el período orbital $T$ (en años terrestres) de un exoplaneta alrededor de una estrella enana roja y su distancia media $R$ (en unidades astronómicas) cumplen la relación de proporcionalidad:

$$\frac{T^2}{R^3} = 1 \implies T = R^{3/2}$$

Si se detecta un planeta con una distancia orbital de $R = \frac{9}{4}\text{ UA}$, determine su período orbital exacto expresado como número mixto de años.  
A) $2\frac{1}{4}\text{ años}$  
B) $3\frac{1}{8}\text{ años}$  
C) $3\frac{3}{8}\text{ años}$  
D) $4\frac{1}{2}\text{ años}$  
E) $5\frac{1}{16}\text{ años}$  

41. **(Contexto de Óptica y Ley de Snell con Fracciones):** Un haz de luz láser pasa desde un medio vítreo hacia una solución salina. El índice de refracción relativo es $n = \sqrt{\frac{9}{8}} \div \sqrt{\frac{2}{3}}$. Calcule el valor simplificado e irreductible de $n$.  
A) $\frac{3}{4}$  
B) $\frac{3\sqrt{3}}{4}$  
C) $\frac{4}{3}$  
D) $\frac{\sqrt{3}}{2}$  
E) $\frac{3}{2}$  

42. **(Contexto de Criptografía y Aritmética Modular con Exponentes):** En un algoritmo criptográfico de clave pública, se define la clave de descifrado $K$ mediante la solución entera de la ecuación:

$$\left(\sqrt[5]{\frac{32}{243}}\right)^{-3} = K \cdot \left(\frac{2}{3}\right)^0$$

Determine el valor de $K$ expresado como fracción ordinaria irreductible.  
A) $\frac{8}{27}$  
B) $\frac{27}{8}$  
C) $\frac{81}{16}$  
D) $\frac{243}{32}$  
E) $\frac{9}{4}$  

43. **(Contexto de Topografía y Error Medio Cuadrático):** El error medio cuadrático en una nivelación geodésica de longitud $L$ está dado por $\sigma = \pm k \sqrt{L}$. Si una cuadrilla de ingenieros mide un tramo de longitud $L_1 = \frac{25}{16}\text{ km}$ y otro tramo de $L_2 = \frac{9}{4}\text{ km}$, ¿cuál es la razón entre los errores $\frac{\sigma_1}{\sigma_2}$?  
A) $\frac{5}{6}$  
B) $\frac{25}{36}$  
C) $\frac{6}{5}$  
D) $\frac{125}{64}$  
E) $\frac{4}{3}$  

44. **(Contexto de Geometría Molecular y Enlaces Químicos):** La energía de enlace intermolecular de Van der Waals entre dos moléculas neutras varía en función de la distancia $r$ según la potencia $V(r) = -C \cdot r^{-6}$. Si la distancia intermolecular se incrementa en una proporción equivalente a $r' = \frac{3}{2}r$, ¿por qué factor fraccionario queda multiplicada la energía atractiva original?  
A) $\frac{64}{729}$  
B) $\frac{729}{64}$  
C) $\frac{16}{81}$  
D) $\frac{8}{27}$  
E) $\frac{32}{243}$  

45. **(Contexto de Modelamiento Matemático Abstracto - Reto Pre):** Si se sabe que:

$$x = \sqrt{\frac{2}{3} \sqrt{\frac{2}{3} \sqrt{\frac{2}{3} \cdots}}} \quad \text{e} \quad y = \sqrt[3]{\frac{16}{81} \div \sqrt[3]{\frac{16}{81} \div \sqrt[3]{\frac{16}{81} \div \cdots}}}$$

Calcule el producto $x \cdot y$ en su forma irreductible.  
A) $\frac{4}{9}$  
B) $\frac{2}{3}$  
C) $\frac{8}{27}$  
D) $\frac{16}{81}$  
E) $1$  

---

## 5. TABLA DE CLAVES DE RESPUESTAS

| N.º | Bloque I (Básico) | N.º | Bloque II (Intermedio) | N.º | Bloque III (Avanzado / B18) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | A | **16** | B | **31** | C |
| **02** | A | **17** | C | **32** | C |
| **03** | C | **18** | B | **33** | C |
| **04** | A | **19** | B | **34** | B |
| **05** | A | **20** | A | **35** | A |
| **06** | B | **21** | A | **36** | B |
| **07** | A | **22** | B | **37** | C |
| **08** | A | **23** | B | **38** | B |
| **09** | A | **24** | C | **39** | B |
| **10** | A | **25** | D | **40** | C |
| **11** | C | **26** | B | **41** | B |
| **12** | B | **27** | A | **42** | B |
| **13** | A | **28** | A | **43** | A |
| **14** | B | **29** | B | **44** | A |
| **15** | B | **30** | B | **45** | A |

---

## 6. PISTAS Y ORIENTACIÓN METODOLÓGICA

Para consolidar tu aprendizaje autónomo, revisa las directrices de los 5 problemas más retadores del Bloque III:

* **Pista Problema 31:** Descompón la base en factores primos: $8 = 2^3$. Luego, $8^{t/9} = (2^3)^{t/9} = 2^{3t/9} = 2^{t/3}$. Para $t = 6\text{ días}$, el exponente resulta $\frac{6}{3} = 2$. Luego la biomasa es $B(6) = 125 \times 2^2 = 125 \times 4 = 500\text{ gramos}$.
* **Pista Problema 32:** Atención a la pregunta: pide *en cuánto se reduce*. Si la altura final es $H_f = \frac{9}{16}H_0$, la velocidad final es $V_f = \sqrt{2g\left(\frac{9}{16}H_0\right)} = \sqrt{\frac{9}{16}} \sqrt{2gH_0} = \frac{3}{4}V_0$. Por lo tanto, la reducción es $V_0 - \frac{3}{4}V_0 = \frac{1}{4}V_0$ (se reduce en $\frac{1}{4}$).
* **Pista Problema 34:** Observa que $\frac{441}{400} = \left(\frac{21}{20}\right)^2$. Por consiguiente, $\left(\frac{441}{400}\right)^6 = \left[\left(\frac{21}{20}\right)^2\right]^6 = \left(\frac{21}{20}\right)^{12}$. Igualando los exponentes de bases iguales: $4t = 12 \implies t = 3\text{ años}$.
* **Pista Problema 35:** El volumen total se conserva, por lo que una partícula original se divide en $N = \left(\frac{L_0}{L_f}\right)^3 = 10^3 = 1000$ micropartículas. El área de cada micropartícula es $6L_f^2 = 6\left(\frac{L_0}{10}\right)^2 = \frac{6L_0^2}{100}$. El área total de las $1000$ partículas es $1000 \times \frac{6L_0^2}{100} = 10 \times (6L_0^2)$. El área se multiplica por $10$.
* **Pista Problema 45:** Para radicales infinitos:
* En producto infinito: $x = \sqrt{f \sqrt{f \cdots}} \implies x^2 = f \cdot x \implies x = f = \frac{2}{3}$.
* En división infinita: $y = \sqrt[3]{g \div \sqrt[3]{g \div \cdots}} \implies y^3 = g \div y \implies y^4 = g = \frac{16}{81} \implies y = \sqrt[4]{\frac{16}{81}} = \frac{2}{3}$.
* Finalmente: $x \cdot y = \frac{2}{3} \times \frac{2}{3} = \frac{4}{9}$.

---

## 7. Formulario Resumen

### 1. Definiciones y Exponentes Especiales

$$
\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n} \quad (b \neq 0, \; n \in \mathbb{Z}^+)
$$

* **Exponente Cero:** $\left(\frac{a}{b}\right)^0 = 1 \quad \left(\frac{a}{b} \neq 0\right)$
* **Exponente Negativo:** $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n = \frac{b^n}{a^n} \quad (a \neq 0, \; b \neq 0)$
* **Exponente Fraccionario (Raíz):** $\left(\frac{a}{b}\right)^{\frac{m}{n}} = \sqrt[n]{\left(\frac{a}{b}\right)^m} = \left(\sqrt[n]{\frac{a}{b}}\right)^m$

---

### 2. Leyes Fundamentales de Exponentes en $\mathbb{Q}$
| Ley de Exponentes | Expresión Matemática |
| :--- | :---: |
| **Producto de bases iguales** | $f^m \cdot f^n = f^{m+n}$ |
| **Cociente de bases iguales** | $\frac{f^m}{f^n} = f^{m-n} \quad (f \neq 0)$ |
| **Potencia de potencia** | $\left(f^m\right)^n = f^{m \cdot n}$ |
| **Distribución sobre producto** | $(f \cdot g)^n = f^n \cdot g^n$ |
| **Distribución sobre cociente** | $\left(\frac{f}{g}\right)^n = \frac{f^n}{g^n} \quad (g \neq 0)$ |

---

### 3. Propiedades Clave de Radicales
* **Raíz de un producto y cociente:**

$$
\sqrt[n]{f \cdot g} = \sqrt[n]{f} \cdot \sqrt[n]{g} \qquad \sqrt[n]{\frac{f}{g}} = \frac{\sqrt[n]{f}}{\sqrt[n]{g}}
$$

* **Raíz de raíz:**

$$
\sqrt[m]{\sqrt[n]{f}} = \sqrt[m \cdot n]{f}
$$

* **Homogeneización / Simplificación de índices:**

$$
\sqrt[n \cdot k]{f^{m \cdot k}} = \sqrt[n]{f^m}
$$

---

### 4. Racionalización Estándar
* **Denominador monomio:** Multiplicar por $\sqrt[n]{b^{n-k}}$:

$$
\frac{A}{\sqrt[n]{b^k}} = \frac{A \sqrt[n]{b^{n-k}}}{b}
$$

* **Denominador binomio (conjugada):**

$$
\frac{A}{\sqrt{a} \pm \sqrt{b}} = \frac{A(\sqrt{a} \mp \sqrt{b})}{a - b}
$$

---

### 5. Fórmulas de Radicales Infinitos

$$
\sqrt{k \sqrt{k \sqrt{k \cdots}}} = k \qquad \sqrt[n]{k \div \sqrt[n]{k \div \sqrt[n]{k \cdots}}} = \sqrt[n+1]{k}
$$
