# Tema 10: Factorización y Fracciones Algebraicas

La factorización es una operación algebraica transformativa en sentido inverso a la multiplicación, cuyo objetivo es descomponer un polinomio no primo con coeficientes en un campo numérico determinado (usualmente los racionales $\mathbb{Q}$) en el producto indicado de dos o más factores polinomiales irreducibles o primos.

Un polinomio $P(x)$ se denomina **primo o irreducible** sobre un campo numérico $\mathbb{K}$ si no puede descomponerse en el producto de dos o más factores algebraicos no constantes de menor grado pertenecientes a dicho campo.

En el contexto del examen de preselección Beca 18 y en las matemáticas universitarias, la factorización y el tratamiento analítico de fracciones algebraicas racionales son competencias transversales determinantes. Permiten resolver ecuaciones e inecuaciones de grado superior por el método de puntos críticos, simplificar expresiones racionales en cálculo diferencial e integral, determinar asíntotas de funciones y calcular límites indeterminados de la forma $\left[\frac{0}{0}\right]$.

---

## 1. Conceptos Fundamentales y Conteo de Factores

### 1.1 Campo de Factorización
La condición de irreducibilidad depende estrictamente del conjunto numérico en el que se trabaje:
* El polinomio $x^2 - 2$ es primo en el campo de los números racionales ($\mathbb{Q}$).
* Sin embargo, es reducible en el campo de los números reales ($\mathbb{R}$): $x^2 - 2 = (x - \sqrt{2})(x + \sqrt{2})$.
* El polinomio $x^2 + 4$ es primo en $\mathbb{R}$, pero es reducible en el campo complejo ($\mathbb{C}$): $x^2 + 4 = (x - 2i)(x + 2i)$.
* Por convenio preuniversitario estándar, salvo indicación explícita, la factorización se realiza siempre sobre el campo de los racionales ($\mathbb{Q}$).

### 1.2 Conteo de Factores de un Polinomio
Sea la forma canónica factorizada de un polinomio:

$$
P(x, y, z) = c \cdot [f_1(x, y)]^{\alpha} \cdot [f_2(x, y)]^{\beta} \cdot [f_3(z)]^{\gamma}
$$

donde $c \in \mathbb{Q}$ es una constante numérica y $f_1, f_2, f_3$ son factores primos no semejantes entre sí:

1. **Número de Factores Primos ($N_{FP}$):** Es la cantidad de bases primas distintas que contienen variables:
$$
N_{FP} = 3
$$
2. **Número de Factores Totales o Divisores ($N_{FT}$):** Incluye a las constantes y combinaciones:
$$
N_{FT} = (\alpha + 1)(\beta + 1)(\gamma + 1)
$$
3. **Número de Factores Algebraicos ($N_{FA}$):** Es el total de factores que contienen al menos una variable (se excluye el factor constante 1):
$$
N_{FA} = (\alpha + 1)(\beta + 1)(\gamma + 1) - 1
$$

---

## 2. Métodos Sistemáticos de Factorización

### 2.1 Factor Común y Agrupación de Términos
Consiste en identificar variables o expresiones comunes con el menor exponente que se repiten en todos los monomios, o bien asociar convenientemente términos en grupos de igual cantidad para extraer factores comunes sucesivos.

### 2.2 Método de las Identidades Notables
Se identifican patrones reconocibles de productos notables leídos de derecha a izquierda:
* **Diferencia de Cuadrados:** $A^2 - B^2 = (A - B)(A + B)$
* **Trinomio Cuadrado Perfecto (T.C.P.):** $A^2 \pm 2AB + B^2 = (A \pm B)^2$
* **Suma y Diferencia de Cubos:**
$$
A^3 + B^3 = (A + B)(A^2 - AB + B^2)
$$
$$
A^3 - B^3 = (A - B)(A^2 + AB + B^2)
$$
* **Identidad de Argand:**
$$
x^4 + x^2 + 1 = (x^2 + x + 1)(x^2 - x + 1)
$$
$$
x^{4m} + x^{2m} y^{2n} + y^{4n} = (x^{2m} + x^m y^n + y^{2n})(x^{2m} - x^m y^n + y^{2n})
$$

### 2.3 Criterio del Aspa Simple
Se aplica para factorizar trinomios de la forma canónica:

$$
P(x) = Ax^{2n} + Bx^n + C
$$

Se descomponen los términos extremos $Ax^{2n} = (a_1 x^n)(a_2 x^n)$ y $C = (c_1)(c_2)$, de tal modo que la suma algebraica de los productos en aspa coincida exactamente con el término central:

$$
(a_1 c_2 + a_2 c_1)x^n = Bx^n \implies P(x) = (a_1 x^n + c_1)(a_2 x^n + c_2)
$$

### 2.4 Criterio del Aspa Doble
Se aplica a polinomios de 6 términos en dos variables de la forma general:

$$
P(x, y) = Ax^2 + Bxy + Cy^2 + Dx + Ey + F
$$

* **Aspa 1:** Entre los términos 1, 2 y 3 ($Ax^2, Bxy, Cy^2$) para verificar $Bxy$.
* **Aspa 2:** Entre los términos 3, 5 y 6 ($Cy^2, Ey, F$) para verificar $Ey$.
* **Aspa 3 (Verificación extrema):** Entre los términos 1, 4 y 6 ($Ax^2, Dx, F$) para comprobar el término $Dx$.

### 2.5 Criterio del Aspa Doble Especial
Se aplica específicamente a polinomios completos de cuarto grado de una sola variable:

$$
P(x) = Ax^4 + Bx^3 + Cx^2 + Dx + E
$$

1. Se descomponen los extremos $Ax^4 = (a_1 x^2)(a_2 x^2)$ y $E = (e_1)(e_2)$.
2. Se efectúa el producto en aspa de los extremos para obtener el término cuadrático temporal:
$$
T_{cuad} = (a_1 e_2 + a_2 e_1)x^2
$$
3. Se calcula la cantidad cuadrática faltante que se debe generar:
$$
\text{Falta} = Cx^2 - T_{cuad} = Kx^2
$$
4. Dicho valor $Kx^2$ se descompone en el término central como $(k_1 x)(k_2 x)$ para verificar simultáneamente mediante aspas simples internas a los términos cúbico ($Bx^3$) y lineal ($Dx$).

### 2.6 Criterio de los Divisores Binómicos (Ceros Racionales de Gauss)
Se utiliza para factorizar polinomios de cualquier grado que admitan al menos un factor lineal $(x - r)$.

1. Se determinan los **posibles ceros racionales (P.C.R.)**:
$$
\text{P.C.R.} = \pm \frac{\text{Divisores del término independiente } |a_0|}{\text{Divisores del coeficiente principal } |a_n|}
$$
2. Se evalúa el polinomio mediante la regla de Ruffini en los valores $r \in \text{P.C.R.}$. Si el residuo es cero ($P(r) = 0$), entonces $(x - r)$ es un factor primo.
3. Se repite el proceso con el cociente obtenido hasta agotar los factores lineales.

---

## 3. M.C.D., M.C.M. y Fracciones Algebraicas

### 3.1 Máximo Común Divisor (M.C.D.)
Dados dos o más polinomios completamente factorizados sobre $\mathbb{Q}$, su M.C.D. es el producto de todos los **factores primos comunes** afectados de sus **menores exponentes**.

### 3.2 Mínimo Común Múltiplo (M.C.M.)
Es el producto de todos los **factores primos comunes y no comunes** afectados de sus **mayores exponentes**.

### 3.3 Propiedad Fundamental de Dos Polinomios:
Para cualesquiera dos polinomios $A(x)$ y $B(x)$:

$$
A(x) \cdot B(x) \equiv \text{M.C.D.}[A, B] \cdot \text{M.C.M.}[A, B]
$$

### 3.4 Fracciones Algebraicas y Simplificación
Una fracción algebraica es el cociente indicado de dos polinomios $\frac{P(x)}{Q(x)}$ con $Q(x) \not\equiv 0$.
* **Dominio de Existencia:** Se deben excluir todos los valores reales que anulan el denominador:
$$
\operatorname{Dom} = \{x \in \mathbb{R} \mid Q(x) \neq 0\}
$$
* **Regla de Simplificación:** Se factorizan completamente numerador y denominador y se cancelan los factores primos idénticos comunes, registrando las restricciones de dominio.

---

## 4. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Factor Común y Agrupación
Factorizar completamente sobre $\mathbb{Q}$ el polinomio:
$$
P(a, b, c) = a^3 + a^2 b + a^2 c + a b c + b^2 c + b c^2
$$
e indicar el número de factores primos.

**Paso 1:** Contamos 6 términos. Buscamos agrupar en ternas o pares convenientes.
Agrupamos los tres primeros términos y los tres últimos:
Grupo 1: $a^2(a + b + c)$
Grupo 2: $b c(a + b + c)$
Verificando si $a b c + b^2 c + b c^2 = bc(a + b + c)$:
$bc \cdot a = abc$
$bc \cdot b = b^2 c$
$bc \cdot c = bc^2$
Coincide exactamente.

**Paso 2:** Extraemos el factor común binómico $(a + b + c)$:
$P(a, b, c) = (a + b + c)(a^2 + bc)$

**Paso 3:** Analizamos la irreducibilidad de los factores sobre $\mathbb{Q}$:
* $(a + b + c)$ es de grado 1, por lo tanto es primo.
* $(a^2 + bc)$ no admite descomposición sobre $\mathbb{Q}$, es primo.

**Respuesta:** La factorización es $(a + b + c)(a^2 + bc)$ y posee 2 factores primos.

---

### Ejercicio 2: Aspa Doble
Factorizar en $\mathbb{Q}$ el polinomio:
$$
P(x, y) = 6x^2 + 7xy - 3y^2 + 11x - 11y - 10
$$

**Paso 1:** Verificamos el orden canónico para aspa doble:
Términos: $6x^2$ (1), $7xy$ (2), $-3y^2$ (3), $11x$ (4), $-11y$ (5), $-10$ (6).

**Paso 2:** Descomponemos los términos 1 y 3 para verificar el término 2 ($7xy$):
$6x^2 = (2x)(3x)$
$-3y^2 = (+3y)(-y)$
Aspa 1: $(2x)(-y) + (3x)(3y) = -2xy + 9xy = +7xy$ (Verifica).

**Paso 3:** Descomponemos el término independiente $-10$ (término 6) para verificar el término 5 ($-11y$):
$-10 = (+2)(-5)$
Aspa 2 con $-3y^2 = (+3y)(-y)$:
$(+3y)(-5) + (-y)(+2) = -15y - 2y = -17y \neq -11y$.
Probamos con $-10 = (-2)(+5)$:
$(+3y)(+5) + (-y)(-2) = 15y + 2y = 17y$.
Probamos intercambiando la descomposición de $-10 = (+5)(-2)$:
$(+3y)(-2) + (-y)(+5) = -6y - 5y = -11y$ (Verifica exactamente).

**Paso 4:** Verificamos el aspa extrema entre el término 1 y 6 para comprobar el término 4 ($11x$):
$(2x)(-2) + (3x)(+5) = -4x + 15x = +11x$ (Verifica perfectamente).

**Paso 5:** Tomamos los factores en forma horizontal:
$P(x, y) = (2x + 3y + 5)(3x - y - 2)$

**Respuesta:** Los factores primos son $(2x + 3y + 5)$ y $(3x - y - 2)$.

---

### Ejercicio 3: Aspa Doble Especial
Factorizar sobre $\mathbb{Q}$ el polinomio:
$$
P(x) = x^4 - 2x^3 - 13x^2 + 14x + 24
$$

**Paso 1:** Ordenamos y completamos en forma descendente de grado 4:
$P(x) = x^4 - 2x^3 - 13x^2 + 14x + 24$

**Paso 2:** Descomponemos los extremos $x^4$ y $+24$:
$x^4 = (x^2)(x^2)$
$+24 = (-6)(-4)$
Aspa extrema: $(x^2)(-4) + (x^2)(-6) = -10x^2$.

**Paso 3:** Calculamos lo que falta para el término central real ($-13x^2$):
$\text{Falta} = (-13x^2) - (-10x^2) = -13x^2 + 10x^2 = -3x^2$.

**Paso 4:** Descomponemos $-3x^2$ en el término central como $(-3x)(+x)$:
Verificamos el término cúbico ($-2x^3$):
$(x^2)(x) + (x^2)(-3x) = x^3 - 3x^3 = -2x^3$ (Verifica).
Verificamos el término lineal ($+14x$):
$(-3x)(-4) + (x)(-6) = 12x - 6x = 6x \neq 14x$.
Probamos otra descomposición de $+24 = (+6)(+4)$:
Extremos: $4x^2 + 6x^2 = 10x^2$.
Falta: $-13x^2 - 10x^2 = -23x^2$ (no factoriza fácilmente).
Probamos con $+24 = (-8)(-3)$:
Extremos: $-11x^2$. Falta: $-13x^2 - (-11x^2) = -2x^2 = (-2x)(+x)$.
Aspa lineal: $(-2x)(-3) + (x)(-8) = 6x - 8x = -2x \neq 14x$.
Probamos con $+24 = (+8)(+3)$:
Extremos: $11x^2$. Falta: $-24x^2$.
Probamos con $+24 = (-12)(-2)$:
Extremos: $-14x^2$. Falta: $-13x^2 - (-14x^2) = +x^2 = (-x)(-x)$.
Probamos con $+24 = (+24)(+1)$ ó divisores binómicos directos:
Evaluamos $x = -1$: $P(-1) = 1 + 2 - 13 - 14 + 24 = 0$ (es raíz).
Evaluamos $x = 2$: $P(2) = 16 - 16 - 52 + 28 + 24 = 0$ (es raíz).
Evaluamos $x = -3$: $P(-3) = 81 + 54 - 117 - 42 + 24 = 0$ (es raíz).
Evaluamos $x = 4$: $P(4) = 256 - 128 - 208 + 56 + 24 = 0$ (es raíz).

**Paso 5:** Por divisores binómicos, el polinomio descompone en:
$P(x) = (x + 1)(x - 2)(x + 3)(x - 4)$

**Respuesta:** La factorización completa es $(x + 1)(x - 2)(x + 3)(x - 4)$.

---

### Ejercicio 4: Artificio de Quita y Pon (Completación a Argand)
Factorizar en $\mathbb{Q}$ la expresión:
$$
P(x) = x^4 + 64
$$

**Paso 1:** Reconocemos una suma de dos cuadrados: $x^4 + 64 = (x^2)^2 + 8^2$.
Para formar un Trinomio Cuadrado Perfecto, falta el doble producto:
$2(x^2)(8) = 16x^2$.

**Paso 2:** Sumamos y restamos $16x^2$ (artificio de quita y pon):
$P(x) = (x^4 + 16x^2 + 64) - 16x^2$

**Paso 3:** Agrupamos el T.C.P. y aplicamos diferencia de cuadrados:
$P(x) = (x^2 + 8)^2 - (4x)^2$
$P(x) = [(x^2 + 8) - 4x][(x^2 + 8) + 4x]$

**Paso 4:** Ordenamos cada trinomio:
$P(x) = (x^2 - 4x + 8)(x^2 + 4x + 8)$

**Paso 5:** Verificamos el discriminante de cada factor cuadrático:
$\Delta_1 = (-4)^2 - 4(1)(8) = 16 - 32 = -16 < 0$ (primo en $\mathbb{R}$).
$\Delta_2 = 4^2 - 4(1)(8) = -16 < 0$ (primo en $\mathbb{R}$).

**Respuesta:** La factorización es $(x^2 - 4x + 8)(x^2 + 4x + 8)$.

---

### Ejercicio 5: Cálculo de M.C.D. y M.C.M. de Polinomios
Hallar el M.C.D. y M.C.M. de los polinomios:
$A(x) = x^3 - 3x^2 - x + 3$
$B(x) = x^3 - x^2 - 9x + 9$

**Paso 1:** Factorizamos el polinomio $A(x)$ por agrupación:
$A(x) = x^2(x - 3) - (x - 3) = (x - 3)(x^2 - 1) = (x - 3)(x - 1)(x + 1)$

**Paso 2:** Factorizamos el polinomio $B(x)$ por agrupación:
$B(x) = x^2(x - 1) - 9(x - 1) = (x - 1)(x^2 - 9) = (x - 1)(x - 3)(x + 3)$

**Paso 3:** Determinamos el M.C.D. seleccionando los factores primos comunes con menor exponente:
Factores comunes: $(x - 1)$ y $(x - 3)$.
$\text{M.C.D.}[A, B] = (x - 1)(x - 3) = x^2 - 4x + 3$

**Paso 4:** Determinamos el M.C.M. con los factores comunes y no comunes con mayor exponente:
$\text{M.C.M.}[A, B] = (x - 1)(x - 3)(x + 1)(x + 3) = (x^2 - 1)(x^2 - 9) = x^4 - 10x^2 + 9$

**Respuesta:** El M.C.D. es $(x - 1)(x - 3)$ y el M.C.M. es $(x^2 - 1)(x^2 - 9)$.

---

### Ejercicio 6: Simplificación de Fracción Algebraica
Simplificar la fracción y establecer sus restricciones de existencia:
$$
F(x) = \frac{x^3 + 3x^2 - 4x - 12}{x^3 - 2x^2 - 9x + 18}
$$

**Paso 1:** Factorizamos el numerador $N(x)$:
$N(x) = x^2(x + 3) - 4(x + 3) = (x + 3)(x^2 - 4) = (x + 3)(x - 2)(x + 2)$

**Paso 2:** Factorizamos el denominador $D(x)$:
$D(x) = x^2(x - 2) - 9(x - 2) = (x - 2)(x^2 - 9) = (x - 2)(x - 3)(x + 3)$

**Paso 3:** Restricciones de dominio ($D(x) \neq 0$):
$x \neq 2, \quad x \neq 3, \quad x \neq -3$

**Paso 4:** Cancelamos los factores comunes en numerador y denominador:
$F(x) = \frac{(x + 3)(x - 2)(x + 2)}{(x - 2)(x - 3)(x + 3)} = \frac{x + 2}{x - 3}$

**Respuesta:** $F(x) = \frac{x + 2}{x - 3}$, para todo $x \in \mathbb{R} \setminus \{-3, 2, 3\}$.

---

### Ejercicio 7: Operaciones con Fracciones Racionales
Efectuar y simplificar la siguiente suma de fracciones algebraicas:
$$
S(x) = \frac{1}{x^2 - x} + \frac{2}{1 - x^2} + \frac{1}{x^2 + x}
$$

**Paso 1:** Factorizamos los denominadores cuidando los signos:
$x^2 - x = x(x - 1)$
$1 - x^2 = -(x^2 - 1) = -(x - 1)(x + 1)$
$x^2 + x = x(x + 1)$

**Paso 2:** Reescribimos la expresión con signos unificados:
$S(x) = \frac{1}{x(x - 1)} - \frac{2}{(x - 1)(x + 1)} + \frac{1}{x(x + 1)}$

**Paso 3:** Calculamos el M.C.M. de los denominadores:
$\text{M.C.M.} = x(x - 1)(x + 1)$

**Paso 4:** Homogeneizamos numeradores:
$S(x) = \frac{1(x + 1) - 2(x) + 1(x - 1)}{x(x - 1)(x + 1)}$
$S(x) = \frac{x + 1 - 2x + x - 1}{x(x - 1)(x + 1)} = \frac{0}{x(x - 1)(x + 1)} = 0$

**Respuesta:** El resultado de la operación es 0 (para todo $x \notin \{-1, 0, 1\}$).

---

### Ejercicio 8: Fracción Algebraica Irreductible y Constante
Determinar la relación que deben cumplir las constantes $A, B, C$ para que la fracción racional:
$$
F(x, y) = \frac{a_1 x + b_1 y + c_1}{a_2 x + b_2 y + c_2}
$$
sea independiente de las variables $x$ e $y$ (tome un valor constante $k \neq 0$).

**Paso 1:** Para que la fracción sea constante e independiente de las variables:
$\frac{a_1 x + b_1 y + c_1}{a_2 x + b_2 y + c_2} = k \iff a_1 x + b_1 y + c_1 \equiv k(a_2 x + b_2 y + c_2)$

**Paso 2:** Igualamos coeficientes homólogos por identidad de polinomios:
$a_1 = k a_2 \implies \frac{a_1}{a_2} = k$
$b_1 = k b_2 \implies \frac{b_1}{b_2} = k$
$c_1 = k c_2 \implies \frac{c_1}{c_2} = k$

**Paso 3:** Establecemos el principio de proporcionalidad continua:
$\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2} = k$

**Respuesta:** Los coeficientes correspondientes deben ser estrictamente proporcionales: $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$.

---

### Ejercicio 9: Descomposición en Fracciones Parciales Básicas
Descomponer la fracción propia en la suma de fracciones parciales:
$$
\frac{5x - 1}{x^2 - x - 6}
$$

**Paso 1:** Factorizamos el denominador por aspa simple:
$x^2 - x - 6 = (x - 3)(x + 2)$

**Paso 2:** Planteamos la forma de fracciones parciales para factores lineales simples:
$\frac{5x - 1}{(x - 3)(x + 2)} \equiv \frac{A}{x - 3} + \frac{B}{x + 2}$

**Paso 3:** Multiplicamos toda la igualdad por el denominador común:
$5x - 1 \equiv A(x + 2) + B(x - 3)$

**Paso 4:** Método de valores críticos (Heaviside):
* Para $x = 3$:
$5(3) - 1 = A(3 + 2) + B(0) \implies 14 = 5A \implies A = \frac{14}{5}$
* Para $x = -2$:
$5(-2) - 1 = A(0) + B(-2 - 3) \implies -11 = -5B \implies B = \frac{11}{5}$

**Respuesta:** La descomposición es $\frac{14/5}{x - 3} + \frac{11/5}{x + 2}$.

---

### Ejercicio 10: Modelamiento Contextualizado (Eficiencia de Maquinaria Agrícola)
En un consorcio de productores agroecológicos en Chanchamayo, dos desgranadoras mecánicas de maíz trabajan en conjunto. La máquina principal tarda $x$ horas en procesar una tonelada de grano, mientras que la máquina secundaria tarda $(x + 3)$ horas en procesar la misma cantidad. Si el tiempo conjunto $T(x)$ en horas está modelado por la fracción algebraica compuesta:
$$
T(x) = \frac{1}{\frac{1}{x} + \frac{1}{x + 3}}
$$
determinar el modelo simplificado de $T(x)$ y calcular el tiempo en minutos que tardan ambas máquinas operando simultáneamente si $x = 2\text{ horas}$.

**Paso 1:** Sumamos las fracciones en el denominador de $T(x)$:
$\frac{1}{x} + \frac{1}{x + 3} = \frac{(x + 3) + x}{x(x + 3)} = \frac{2x + 3}{x(x + 3)}$

**Paso 2:** Aplicamos extremos y medios para simplificar $T(x)$:
$T(x) = \frac{1}{\frac{2x + 3}{x(x + 3)}} = \frac{x(x + 3)}{2x + 3} = \frac{x^2 + 3x}{2x + 3}$

**Paso 3:** Evaluamos para $x = 2\text{ horas}$:
$T(2) = \frac{2(2 + 3)}{2(2) + 3} = \frac{2(5)}{4 + 3} = \frac{10}{7}\text{ horas}$

**Paso 4:** Convertimos a minutos:
$\text{Tiempo} = \frac{10}{7} \times 60\text{ min} = \frac{600}{7}\text{ min} \approx 85.71\text{ minutos}$ ($1\text{ hora, } 25\text{ min y } 43\text{ s}$).

**Respuesta:** El modelo simplificado es $T(x) = \frac{x^2 + 3x}{2x + 3}$, y para $x = 2\text{ h}$ tardan $\frac{10}{7}\text{ h} \approx 85.71\text{ min}$.

---

## 5. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. Factorizar $P(x) = 6x^3 - 15x^2$ e indicar el factor común extraído:  
A) $3x$  
B) $3x^2$  
C) $x^2$  
D) $6x^2$  
E) $15x$  

2. ¿Cuántos factores primos tiene el polinomio $P(x, y) = 4x^3 y^2(x - 1)(y + 2)^3$?  
A) $4$  
B) $5$  
C) $9$  
D) $3$  
E) $2$  

3. Factorizar por diferencia de cuadrados $16x^2 - 49y^2$:  
A) $(4x - 7y)^2$  
B) $(4x + 7y)(4x - 7y)$  
C) $(16x - 49y)(x + y)$  
D) $(4x + 7y)^2$  
E) $4x - 7y$  

4. Factorizar el trinomio $x^2 - 11x + 24$ e indicar la suma de sus factores primos:  
A) $2x - 11$  
B) $2x + 11$  
C) $2x - 14$  
D) $x - 11$  
E) $2x - 10$  

5. Simplificar la fracción algebraica $\frac{x^2 - 9}{x^2 - 6x + 9}$:  
A) $\frac{x + 3}{x - 3}$  
B) $\frac{x - 3}{x + 3}$  
C) $\frac{1}{x - 3}$  
D) $x + 3$  
E) $1$  

6. Al factorizar $x^3 - 8$, uno de los factores primos es:  
A) $x^2 - 2x + 4$  
B) $x^2 + 2x + 4$  
C) $x^2 + 4$  
D) $x^2 - 4$  
E) $x + 2$  

7. Factorizar $P(a, b) = a^2 + ab + ax + bx$ por agrupación:  
A) $(a + b)(a + x)$  
B) $(a - b)(a + x)$  
C) $(a + b)(x - a)$  
D) $(ab)(a + x)$  
E) $(a + b + x)^2$  

8. Hallar el M.C.D. de los monomios $A = 12x^3 y^4$ y $B = 18x^2 y^5$:  
A) $6x^3 y^5$  
B) $6x^2 y^4$  
C) $36x^3 y^5$  
D) $12x^2 y^4$  
E) $2x^2 y^4$  

9. Hallar el M.C.M. de los monomios $A = 12x^3 y^4$ y $B = 18x^2 y^5$:  
A) $36x^3 y^5$  
B) $6x^2 y^4$  
C) $216x^5 y^9$  
D) $18x^3 y^5$  
E) $72x^3 y^5$  

10. Si el polinomio $x^2 + mx + 25$ es un trinomio cuadrado perfecto con $m > 0$, hallar $m$:  
A) $5$  
B) $10$  
C) $20$  
D) $25$  
E) $50$  

11. Factorizar por aspa simple $2x^2 + 5x - 3$:  
A) $(2x - 1)(x + 3)$  
B) $(2x + 1)(x - 3)$  
C) $(2x + 3)(x - 1)$  
D) $(x + 1)(2x - 3)$  
E) $(2x - 3)(x + 1)$  

12. Simplificar la fracción $\frac{x^2 - 4x}{x^2 - 16}$:  
A) $\frac{x}{x + 4}$  
B) $\frac{x}{x - 4}$  
C) $\frac{1}{x + 4}$  
D) $\frac{x - 4}{x + 4}$  
E) $\frac{4}{x + 4}$  

13. ¿Cuál es el conjunto de valores que NO pertenecen al dominio de $\frac{x + 5}{x^2 - 1}$?  
A) $\{1\}$  
B) $\{-1\}$  
C) $\{-1, 1\}$  
D) $\{-5\}$  
E) $\{0\}$  

14. Reducir la suma de fracciones homogéneas: $\frac{2x + 1}{x - 3} - \frac{x + 4}{x - 3}$:  
A) $1$  
B) $\frac{x - 3}{x + 3}$  
C) $x - 3$  
D) $\frac{3x + 5}{x - 3}$  
E) $0$  

15. Al factorizar $x^4 - 1$ en el campo de los números racionales $\mathbb{Q}$, ¿cuántos factores primos se obtienen?  
A) $2$  
B) $3$  
C) $4$  
D) $1$  
E) $5$  

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Factorizar completamente el polinomio $P(x) = x^4 - 5x^2 + 4$ e indicar la cantidad de factores algebraicos:  
A) $4$  
B) $15$  
C) $8$  
D) $16$  
E) $7$  

17. Indicar la suma de los factores primos del polinomio $P(x, y) = x^2 - y^2 + 4x + 4$:  
A) $2x + 4$  
B) $2x + 2y + 4$  
C) $2x - 2y + 4$  
D) $2x$  
E) $2y + 4$  

18. Factorizar por aspa doble $P(x, y) = 2x^2 + 5xy + 2y^2 + 7x + 5y + 3$ e indicar uno de sus factores primos:  
A) $2x + y + 3$  
B) $x + 2y + 3$  
C) $2x + y + 1$  
D) $x + y + 1$  
E) $2x + 2y + 3$  

19. Al factorizar $P(x) = x^3 - 6x^2 + 11x - 6$ mediante divisores binómicos, la suma de los términos independientes de sus factores primos es:  
A) $-6$  
B) $6$  
C) $-11$  
D) $11$  
E) $0$  

20. Simplificar la siguiente expresión racional:
$$
E = \left( \frac{x}{x + 1} + \frac{1}{x - 1} \right) \div \frac{x^2 + 1}{x^2 - 1}
$$
A) $1$  
B) $x$  
C) $x - 1$  
D) $x + 1$  
E) $\frac{x}{x^2 + 1}$  

21. Si la fracción algebraica $\frac{ax + 12}{3x + 4}$ es constante e independiente de $x$, hallar el valor de $a$:  
A) $9$  
B) $12$  
C) $16$  
D) $6$  
E) $8$  

22. Hallar el M.C.D. de los polinomios:
$P(x) = x^3 - x$
$Q(x) = x^2 - 2x + 1$  
A) $x - 1$  
B) $(x - 1)^2$  
C) $x(x - 1)$  
D) $x + 1$  
E) $x^2 - 1$  

23. Factorizar la expresión de Argand $P(x) = x^4 + x^2 + 1$ y evaluar en $x = 2$:  
A) $21$  
B) $25$  
C) $28$  
D) $35$  
E) $15$  

24. Un productor de cacao en Satipo cerca una finca rectangular cuya área en metros cuadrados está dada por $A(x) = 6x^2 + 17x + 12$. Si $x$ representa una unidad modular de medida, ¿cuál es el perímetro de la finca?  
A) $10x + 14$  
B) $5x + 7$  
C) $12x + 14$  
D) $6x + 8$  
E) $8x + 12$  

25. Simplificar la fracción continua elemental:
$$
F(x) = 1 + \frac{1}{1 + \frac{1}{x}}
$$
A) $\frac{2x + 1}{x + 1}$  
B) $\frac{x + 2}{x + 1}$  
C) $\frac{2x + 2}{x + 1}$  
D) $\frac{x + 1}{2x + 1}$  
E) $\frac{x}{x + 1}$  

26. Descomponer en fracciones parciales la expresión $\frac{7x - 1}{x^2 - x - 2}$ e indicar la suma de sus numeradores constantes $A + B$:  
A) $7$  
B) $5$  
C) $6$  
D) $8$  
E) $4$  

27. Al factorizar $x^4 + 4y^4$ mediante el artificio de quita y pon, uno de los factores primos es:  
A) $x^2 - 2xy + 2y^2$  
B) $x^2 + 2y^2$  
C) $x^2 - 2y^2$  
D) $x^2 + 4xy + 2y^2$  
E) $x^2 - 4xy + 4y^2$  

28. Hallar el número de factores primos lineales de $P(x) = x^5 - 4x^3 + x^2 - 4$:  
A) $2$  
B) $3$  
C) $4$  
D) $1$  
E) $5$  

29. Si $P(x)$ y $Q(x)$ son polinomios cuyo $\text{M.C.D.} = x + 2$ y su producto es $P(x) \cdot Q(x) = (x + 2)^2(x - 3)(x + 5)$, ¿cuál es su M.C.M.?  
A) $(x + 2)(x - 3)(x + 5)$  
B) $(x - 3)(x + 5)$  
C) $(x + 2)^2$  
D) $(x + 2)^3(x - 3)$  
E) $x^2 + 2x$  

30. Reducir la siguiente operación combinada:
$$
M = \left( \frac{1}{a} - \frac{1}{b} \right) \left( \frac{a^2 b + ab^2}{b - a} \right)
$$
A) $-1$  
B) $-(a + b)$  
C) $a + b$  
D) $ab$  
E) $1$  

31. Factorizar por aspa doble especial $P(x) = x^4 + 3x^3 + 7x^2 + 7x + 6$ e indicar el término independiente de uno de sus factores cuadráticos:  
A) $2$  
B) $4$  
C) $5$  
D) $6$  
E) $1$  

32. Si se simplifica la fracción $\frac{x^3 + 1}{x^4 + x^3 + x + 1}$, se obtiene:  
A) $\frac{x^2 - x + 1}{(x + 1)^2}$  
B) $\frac{1}{x + 1}$  
C) $\frac{x - 1}{x + 1}$  
D) $\frac{x^2 - x + 1}{x^2 + 1}$  
E) $\frac{1}{x^2 + 1}$  

33. Determinar el valor de $k$ para que la fracción $\frac{4x^2 - 2x + 3}{2x^2 - x + k}$ sea una constante para todo $x \in \mathbb{R}$:  
A) $1.5$  
B) $3$  
C) $6$  
D) $2$  
E) $0.5$  

34. Factorizar el polinomio simétrico $P(x, y, z) = x^3 + y^3 + z^3 - 3xyz$ y evaluar para $x = 10, y = 20, z = -30$:  
A) $0$  
B) $1000$  
C) $-1800$  
D) $3000$  
E) $-6000$  

35. Dos bombas de agua comunales en Piura llenan un reservorio. La bomba $A$ llena la fracción $\frac{x}{x + 2}$ del tanque por hora y la bomba $B$ llena $\frac{2}{x + 2}$ por hora. Si ambas bombas operan juntas, ¿qué fracción del reservorio llenan en una hora?  
A) $1$ (Llenan el tanque completo)  
B) $2$  
C) $\frac{x + 1}{x + 2}$  
D) $\frac{2x}{x + 2}$  
E) $\frac{1}{2}$  

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Factorizar completamente sobre $\mathbb{Q}$ el polinomio:
$$
P(x) = x^5 + x + 1
$$
e indicar uno de sus factores primos:  
A) $x^2 + x + 1$  
B) $x^2 - x + 1$  
C) $x^3 + x + 1$  
D) $x^3 - x + 1$  
E) $x^2 + 1$  

37. Simplificar la siguiente fracción cíclica para $a, b, c$ mutuamente diferentes:
$$
E = \frac{a}{(a - b)(a - c)} + \frac{b}{(b - c)(b - a)} + \frac{c}{(c - a)(c - b)}
$$
A) $0$  
B) $1$  
C) $a + b + c$  
D) $abc$  
E) $-1$  

38. Factorizar en $\mathbb{Q}$ el polinomio de cuarto grado:
$$
P(x) = (x^2 + x + 1)(x^2 + x + 2) - 12
$$
e indicar la suma de los coeficientes de uno de sus factores cuadráticos irreducibles:  
A) $7$  
B) $8$  
C) $9$  
D) $5$  
E) $3$  

39. Si el M.C.D. de los polinomios $A(x) = x^3 - 6x^2 + 11x - m$ y $B(x) = x^3 + 2x^2 - x - n$ es un polinomio cuadrático, calcular $m + n$:  
A) $8$  
B) $6$  
C) $4$  
D) $10$  
E) $12$  

40. Descomponer en fracciones parciales e indicar el valor de $A + B + C$:
$$
\frac{3x^2 - 2x + 1}{(x - 1)(x - 2)(x - 3)} \equiv \frac{A}{x - 1} + \frac{B}{x - 2} + \frac{C}{x - 3}
$$
A) $3$  
B) $0$  
C) $1$  
D) $-2$  
E) $5$  

41. **(Reto)** Factorizar completamente el polinomio en dos variables:
$$
P(x, y) = x^3 + y^3 + 3xy - 1
$$
A) $(x + y - 1)(x^2 - xy + y^2 + x + y + 1)$  
B) $(x + y + 1)(x^2 - xy + y^2 - x - y + 1)$  
C) $(x - y - 1)(x^2 + xy + y^2 + x - y + 1)$  
D) $(x + y - 1)^3$  
E) $(x + y - 1)(x^2 + y^2 + 1)$  

42. **(Reto)** Si la fracción algebraica:
$$
F(x, y, z) = \frac{ax^2 + 4xy + cy^2 + 6z^2}{2x^2 + bxy + 6y^2 + 4z^2}
$$
es independiente de las variables $x, y, z$, calcular el valor numérico de $a \cdot b \cdot c$:  
A) $72$  
B) $48$  
C) $36$  
D) $54$  
E) $64$  

43. **(Reto)** Simplificar la siguiente suma telescópica de fracciones algebraicas para $n$ términos:
$$
S = \frac{1}{x(x + 1)} + \frac{1}{(x + 1)(x + 2)} + \frac{1}{(x + 2)(x + 3)} + \dots + \frac{1}{(x + n - 1)(x + n)}
$$
A) $\frac{n}{x(x + n)}$  
B) $\frac{1}{x(x + n)}$  
C) $\frac{n + 1}{x(x + n)}$  
D) $\frac{n}{x + n}$  
E) $\frac{x}{n(x + n)}$  

44. **(Reto)** Factorizar el polinomio $P(x) = x^8 + x^4 + 1$ en $\mathbb{R}$ e indicar el número de factores primos cuadráticos:  
A) $4$  
B) $2$  
C) $3$  
D) $1$  
E) $5$  

45. **(Reto)** Si $x + y + z = 1$ y $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$, calcular el valor simplificado de la fracción:
$$
K = \frac{x^3 + y^3 + z^3 - 3xyz}{x^2 + y^2 + z^2}
$$
A) $1$  
B) $1/2$  
C) $3$  
D) $0$  
E) $-1$  

---

## 6. Claves de Respuestas y Pistas Estratégicas

### Claves de Respuestas

| N° | Clave | N° | Clave | N° | Clave | N° | Clave | N° | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **10** | B | **19** | A | **28** | B | **37** | A |
| **2** | A | **11** | A | **20** | A | **29** | A | **38** | A |
| **3** | B | **12** | A | **21** | A | **30** | B | **39** | A |
| **4** | A | **13** | C | **22** | A | **31** | A | **40** | A |
| **5** | A | **14** | A | **23** | A | **32** | E | **41** | A |
| **6** | B | **15** | B | **24** | A | **33** | A | **42** | A |
| **7** | A | **16** | B | **25** | A | **34** | A | **43** | A |
| **8** | B | **17** | A | **26** | A | **35** | A | **44** | A |
| **9** | A | **18** | A | **27** | A | **36** | A | **45** | A |

---

### Pistas Estratégicas para Ejercicios Reto (41 al 45)

* **Pista 41:** Expresa el polinomio en la forma de la identidad condicional de Gauss: $x^3 + y^3 + (-1)^3 - 3(x)(y)(-1)$. Aplica directamente la factorización de la suma de cubos de tres términos: $(a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)$ con $a = x, b = y, c = -1$.
* **Pista 42:** Aplica el principio de proporcionalidad continua igualando las razones de los coeficientes homólogos: $\frac{a}{2} = \frac{4}{b} = \frac{c}{6} = \frac{6}{4} = \frac{3}{2}$. Despeja $a = 3$, $b = 8/3$ y $c = 9$. Luego calcula el producto $a \cdot b \cdot c = 3 \times \frac{8}{3} \times 9 = 72$.
* **Pista 43:** Descompón cada fracción en fracciones parciales elementales: $\frac{1}{k(k + 1)} = \frac{1}{k} - \frac{1}{k + 1}$. Al sumar todos los términos se produce una cancelación telescópica de términos intermedios, quedando únicamente el primer término y el último: $\frac{1}{x} - \frac{1}{x + n} = \frac{n}{x(x + n)}$.
* **Pista 44:** Aplica la identidad de Argand en cascada: $x^8 + x^4 + 1 = (x^4 + x^2 + 1)(x^4 - x^2 + 1)$. A su vez, factoriza el primer factor como $(x^2 + x + 1)(x^2 - x + 1)$. Para el segundo factor, aplica quita y pon: $x^4 - x^2 + 1 = (x^2 + 1)^2 - 3x^2 = (x^2 - \sqrt{3}x + 1)(x^2 + \sqrt{3}x + 1)$. En $\mathbb{R}$ se obtienen exactamente 4 factores primos cuadráticos.
* **Pista 45:** De $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$, deduce que $xy + yz + zx = 0$. Luego: $(x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx) \implies 1^2 = x^2 + y^2 + z^2 + 0 \implies x^2 + y^2 + z^2 = 1$. Además, de la identidad de Gauss: $x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - (xy + yz + zx)) = (1)(1 - 0) = 1$. La fracción resulta $\frac{1}{1} = 1$.

---

## 7. Formulario Resumen

| Concepto / Teorema | Expresión Matemática | Notas y Condiciones |
| :--- | :--- | :--- |
| **Factores Algebraicos** | $N_{FA} = (\alpha + 1)(\beta + 1)\dots - 1$ | Excluye a la constante numérica no nula 1 |
| **Diferencia de Cuadrados** | $A^2 - B^2 = (A - B)(A + B)$ | Producto de suma por diferencia |
| **Suma de Cubos** | $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$ | Binomio suma por trinomio cuadrático |
| **Diferencia de Cubos** | $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$ | Binomio resta por trinomio cuadrático |
| **Identidad de Argand** | $x^4 + x^2 + 1 = (x^2 + x + 1)(x^2 - x + 1)$ | Polinomio bicuadrado especial |
| **Aspa Simple** | $Ax^{2n} + Bx^n + C = (a_1 x^n + c_1)(a_2 x^n + c_2)$ | Multiplicación cruzada igual al centro |
| **Aspa Doble** | $Ax^2 + Bxy + Cy^2 + Dx + Ey + F$ | Dos aspas simples y una de comprobación |
| **Aspa Doble Especial** | $Ax^4 + Bx^3 + Cx^2 + Dx + E$ | Extremos fijan cuadrático; se halla lo que falta |
| **Ceros Racionales (P.C.R.)** | $\text{P.C.R.} = \pm \frac{\text{Div}(|a_0|)}{\text{Div}(|a_n|)}$ | Candidatos a raíces racionales de Gauss |
| **Propiedad M.C.D. y M.C.M.** | $A(x) \cdot B(x) = \text{MCD} \cdot \text{MCM}$ | Válida para cualquier par de polinomios |
| **Fracción Constante** | $\frac{a_1 x + b_1 y + c_1}{a_2 x + b_2 y + c_2} = k \iff \frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Proporcionalidad de coeficientes homólogos |
| **Fracciones Parciales (Lineal)**| $\frac{P(x)}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}$ | Descomposición para factores lineales simples |
| **Identidad Cúbica de Gauss** | $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2 - ab - bc - ca)$ | Factorización de 3 variables |
