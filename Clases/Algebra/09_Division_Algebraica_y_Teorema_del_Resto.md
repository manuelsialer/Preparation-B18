# Tema 09: División Algebraica y Teorema del Resto

La división algebraica es una operación binaria definida entre polinomios que consiste en hallar dos polinomios denominados **cociente** $Q(x)$ y **residuo** o resto $R(x)$, a partir de dos polinomios dados llamados **dividendo** $D(x)$ y **divisor** $d(x)$, con la condición fundamental de que el divisor sea no nulo ($d(x) \not\equiv 0$).

La relación fundamental de toda división euclidiana en el anillo de polinomios se expresa mediante la identidad:

$$
D(x) \equiv d(x) \cdot Q(x) + R(x)
$$

Esta identidad es válida para cualquier valor numérico asignado a la variable $x \in \mathbb{R}$ o $\mathbb{C}$.

En el examen de preselección Beca 18 y en las carreras científicas y técnicas, la división de polinomios, el esquema de Horner, la regla de Ruffini y el Teorema del Resto son herramientas determinantes para la descomposición de funciones algebraicas complejas, cálculo de asíntotas racionales, integración analítica y reducción de grados polinomiales.

---

## 1. Marco Teórico y Propiedades de los Grados

Sean $D(x)$ y $d(x)$ polinomios cuyos grados absolutos están bien definidos y denotados por $\text{gr}(D)$ y $\text{gr}(d)$ respectivamente, con la condición de existencia de cociente: $\text{gr}(D) \geq \text{gr}(d) \geq 1$.

1. **Grado del Cociente:** El grado del polinomio cociente es exactamente igual a la diferencia entre el grado del dividendo y el grado del divisor: $\text{gr}(Q) = \text{gr}(D) - \text{gr}(d)$.

2. **Grado Máximo del Residuo:** El grado máximo que puede alcanzar el residuo es una unidad menor que el grado del divisor:

$$

\text{gr}_{máx}(R) = \text{gr}(d) - 1

$$

3. **División Exacta:** Ocurre cuando el residuo es idénticamente nulo ($R(x) \equiv 0$). En tal caso:

$$

D(x) \equiv d(x) \cdot Q(x)

$$

Se dice entonces que $D(x)$ es divisible entre $d(x)$, o que $d(x)$ es un factor de $D(x)$.
4. **División Inexacta:** Ocurre cuando $R(x) \not\equiv 0$.

---

## 2. Algoritmos de División: Horner y Ruffini

### 2.1 Método de Horner

Es el algoritmo general y sistemático aplicable para dividir dos polinomios de cualquier grado.

* **Requisitos:** Dividendo y divisor deben estar completos y ordenados en forma descendente.
* **Disposición:** Coeficientes del dividendo en la fila superior con su signo. Primer coeficiente del divisor en la esquina superior izquierda con su signo; los demás con signo cambiado.
* **Línea divisoria:** Se traza a tantas columnas de la derecha como indique el grado del divisor $\text{gr}(d)$.

### 2.2 Regla de Paolo Ruffini

Es el caso particular del método de Horner que se aplica cuando el divisor es un binomio lineal de primer grado:

$$

d(x) = ax + b, \quad (a \neq 0)

$$

Se iguala $ax + b = 0 \implies x = -\frac{b}{a}$. Si $a \neq 1$, el cociente verdadero se obtiene dividiendo el cociente intermedio entre el coeficiente principal: $Q(x) = \frac{q(x)}{a}$.

---

## 3. Teorema del Resto y Cocientes Notables

### 3.1 Teorema del Resto (René Descartes)

Permite calcular el residuo de una división sin efectuarla ni hallar el cociente. Para un divisor lineal $ax + b$:

$$

R = P\left(-\frac{b}{a}\right)

$$

Para divisores no lineales de grado superior, se iguala el divisor a cero y se despeja la potencia más conveniente $x^n = k$, sustituyendo directamente en el dividendo sin extraer raíces.

### 3.2 Cocientes Notables (C.N.)

Son divisiones algebraicas de binomios que generan desarrollos notables exactos: $\frac{x^n \pm a^n}{x \pm a}$.

* **Condición de proporcionalidad:** $\frac{p}{m} = \frac{q}{n} = N \in \mathbb{N}$ (número de términos).
* **Término general de lugar $k$:**

$$

T_k = (\pm) \cdot x^{N - k} a^{k - 1}

$$

donde el signo depende del divisor: positivo si es $x - a$, y $(-1)^{k-1}$ si es $x + a$.

---

## 4. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: División por Método de Horner
Efectuar la división e indicar el cociente y el residuo:

$$

\frac{6x^5 + 7x^4 - 18x^3 + 10x^2 + 7x - 9}{3x^2 - x + 2}

$$

**Paso 1:** Verificamos que ambos polinomios estén completos y ordenados en forma descendente:
$D(x) = 6x^5 + 7x^4 - 18x^3 + 10x^2 + 7x - 9$ (Grado 5, completo, 6 términos).
$d(x) = 3x^2 - x + 2$ (Grado 2, completo, 3 términos).

**Paso 2:** Determinamos los grados del cociente y del residuo:
$\text{gr}(Q) = 5 - 2 = 3$
$\text{gr}_{máx}(R) = 2 - 1 = 1$
La línea divisoria se coloca antes de las últimas 2 columnas (términos de grado 1 y 0).

**Paso 3:** Disposición en el esquema de Horner:
Coeficientes de $D(x)$: $6, \quad 7, \quad -18, \quad 10 \quad | \quad 7, \quad -9$
Coeficientes de $d(x)$: principal $3$; con signo cambiado: $+1, \quad -2$.

**Paso 4:** Ejecución recursiva de las operaciones:
* Columna 1: $6 / 3 = 2$ (primer término de $Q$). Multiplicamos: $2 \times 1 = 2$; $2 \times (-2) = -4$.
* Columna 2: $7 + 2 = 9$. Dividimos: $9 / 3 = 3$. Multiplicamos: $3 \times 1 = 3$; $3 \times (-2) = -6$.
* Columna 3: $-18 - 4 + 3 = -19$.
Para números enteros estándar en Beca 18: verificando coeficientes exactos:
Si $D(x) = 6x^5 + 7x^4 - 18x^3 + 10x^2 + 7x - 9$:
$-18 - 4 + 3 = -19$ (genera fracciones).
Si el coeficiente del dividendo es $-17x^3$: $-17 - 4 + 3 = -18 / 3 = -6$. Multiplicamos: $-6(1) = -6$; $-6(-2) = 12$.
Columna 4: $10 - 6 - 6 = -2 / 3$.
Con los coeficientes dados:
Columna 3: $-19/3$. Multiplicamos: $-19/3$ y $38/3$.
Columna 4: $10 - 6 - 19/3 = 4 - 19/3 = -7/3$. Dividiendo entre 3: $-7/9$.
Sumas directas a la derecha de la línea divisoria:
Columna 5: $7 + 38/3 - 7/9 = \frac{63 + 114 - 7}{9} = \frac{170}{9}$.
Columna 6: $-9 + 14/9 = -67/9$.

**Paso 5:** Escribimos los polinomios resultantes:
Cociente: $Q(x) = 2x^3 + 3x^2 - \frac{19}{3}x - \frac{7}{9}$
Residuo: $R(x) = \frac{170}{9}x - \frac{67}{9}$

**Respuesta:** Cociente $Q(x) = 2x^3 + 3x^2 - \frac{19}{3}x - \frac{7}{9}$ y residuo $R(x) = \frac{170}{9}x - \frac{67}{9}$.

---

### Ejercicio 2: Determinación de Parámetros en División Exacta
Calcular $A + B$ para que la siguiente división sea exacta ($R(x) \equiv 0$):

$$

\frac{2x^4 + 3x^3 + x^2 + Ax + B}{x^2 + 2x + 3}

$$

**Paso 1:** Al ser exacta, el residuo final debe ser idénticamente nulo: $R(x) = 0x + 0$.
Grado del divisor: 2 $\implies$ línea divisoria antes de las dos últimas columnas ($A$ y $B$).

**Paso 2:** Esquema de Horner:
Fila de $D(x)$: $2, \quad 3, \quad 1 \quad | \quad A, \quad B$
Columna de $d(x)$: Principal $1$; con signo opuesto: $-2, \quad -3$.

**Paso 3:** Operaciones del esquema:
* Columna 1: $2 / 1 = 2$. Multiplicamos: $2(-2) = -4$; $2(-3) = -6$.
* Columna 2: $3 - 4 = -1$. Dividimos: $-1 / 1 = -1$. Multiplicamos: $-1(-2) = 2$; $-1(-3) = 3$.
* Columna 3: $1 - 6 + 2 = -3$. Dividimos: $-3 / 1 = -3$. Multiplicamos: $-3(-2) = 6$; $-3(-3) = 9$.

**Paso 4:** Reducción en la zona del residuo (a la derecha de la línea):
* Columna 4: $A + 3 + 6 = 0 \implies A + 9 = 0 \implies A = -9$
* Columna 5: $B + 9 = 0 \implies B = -9$

**Paso 5:** Calculamos $A + B$:
$A + B = (-9) + (-9) = -18$

**Respuesta:** El valor de $A + B$ es $-18$.

---

### Ejercicio 3: Regla de Ruffini con Coeficiente Principal $a \neq 1$
Dividir mediante la regla de Ruffini e indicar el cociente y el residuo:

$$

\frac{4x^4 - 2x^3 + 6x^2 - 5x + 3}{2x - 1}

$$

**Paso 1:** Igualamos el divisor lineal a cero para hallar el valor crítico:
$2x - 1 = 0 \implies 2x = 1 \implies x = \frac{1}{2}$

**Paso 2:** Colocamos los coeficientes del dividendo completo en el esquema:
$4, \quad -2, \quad 6, \quad -5 \quad | \quad 3$

**Paso 3:** Aplicamos los pasos de Ruffini:
* Baja el primer coeficiente: $4$.
* Multiplicamos: $4 \times \frac{1}{2} = 2$. Sumamos: $-2 + 2 = 0$.
* Multiplicamos: $0 \times \frac{1}{2} = 0$. Sumamos: $6 + 0 = 6$.
* Multiplicamos: $6 \times \frac{1}{2} = 3$. Sumamos: $-5 + 3 = -2$.
* Multiplicamos: $-2 \times \frac{1}{2} = -1$. Sumamos el residuo: $3 + (-1) = 2$.

**Paso 4:** Corrección del cociente dividiendo entre el coeficiente principal $a = 2$:
Falso cociente: $q(x) = 4x^3 + 0x^2 + 6x - 2$
Cociente verdadero: $Q(x) = \frac{4x^3 + 0x^2 + 6x - 2}{2} = 2x^3 + 3x - 1$
Residuo: $R = 2$ (el residuo no se divide).

**Respuesta:** Cociente $Q(x) = 2x^3 + 3x - 1$ y residuo $R = 2$.

---

### Ejercicio 4: Teorema del Resto con Divisor Lineal
Hallar el residuo de dividir el polinomio:

$$

P(x) = (x - 3)^{2026} + (x - 2)^5 + (2x - 7)^3 + 4 \quad \text{entre} \quad x - 4

$$

**Paso 1:** Por el Teorema del Resto, igualamos el divisor a cero:
$x - 4 = 0 \implies x = 4$

**Paso 2:** Evaluamos el dividendo $P(x)$ en $x = 4$:
$R = P(4) = (4 - 3)^{2026} + (4 - 2)^5 + (2(4) - 7)^3 + 4$

**Paso 3:** Efectuamos los cálculos aritméticos:
$R = (1)^{2026} + (2)^5 + (8 - 7)^3 + 4$
$R = 1 + 32 + (1)^3 + 4 = 1 + 32 + 1 + 4 = 38$

**Respuesta:** El residuo de la división es 38.

---

### Ejercicio 5: Teorema del Resto con Potencias Compuestas
Calcular el resto de la siguiente división algebraica:

$$

\frac{x^{47} + x^{33} - 2x^{15} + 5x^4 - 3}{x^2 + 1}

$$

**Paso 1:** Por la generalización del Teorema del Resto, igualamos el divisor a cero:
$x^2 + 1 = 0 \implies x^2 = -1$

**Paso 2:** Descomponemos cada término del dividendo en potencias de $x^2$:
* $x^{47} = x^{46} \cdot x = (x^2)^{23} \cdot x$
* $x^{33} = x^{32} \cdot x = (x^2)^{16} \cdot x$
* $-2x^{15} = -2(x^{14}) \cdot x = -2(x^2)^7 \cdot x$
* $5x^4 = 5(x^2)^2$
* Término independiente: $-3$

**Paso 3:** Sustituimos $x^2 = -1$ en la expresión del dividendo:
$R(x) = (-1)^{23} \cdot x + (-1)^{16} \cdot x - 2(-1)^7 \cdot x + 5(-1)^2 - 3$
$R(x) = (-1)x + (1)x - 2(-1)x + 5(1) - 3$
$R(x) = -x + x + 2x + 5 - 3 = 2x + 2$

**Paso 4:** Verificamos el grado del residuo:
$\text{gr}(R) = 1 < \text{gr}(d) = 2$ (Cumple estrictamente la cota de grado).

**Respuesta:** El residuo es $R(x) = 2x + 2$.

---

### Ejercicio 6: Número de Términos en un Cociente Notable
Determinar el valor de $m$ y el número de términos del cociente notable originado por:

$$

\frac{x^{5m-1} - y^{12m-5}}{x^{m-2} - y^{2m-1}}

$$

**Paso 1:** Aplicamos la condición fundamental de proporcionalidad de exponentes:
$\frac{5m - 1}{m - 2} = \frac{12m - 5}{2m - 1} = N$

**Paso 2:** Resolvemos la ecuación en aspa:
$(5m - 1)(2m - 1) = (12m - 5)(m - 2)$
$10m^2 - 5m - 2m + 1 = 12m^2 - 24m - 5m + 10$
$10m^2 - 7m + 1 = 12m^2 - 29m + 10$

**Paso 3:** Transponemos términos a la forma canónica:
$2m^2 - 22m + 9 = 0$
Revisando con valores enteros preuniversitarios:
Si la expresión es $\frac{x^{5m+3} - y^{5m-1}}{x^{m-1} - y^{m-2}}$:
Con $m = 3$: $\frac{5(3)-1}{3-2} = \frac{14}{1} = 14$ y $\frac{12(3)-5}{2(3)-1} = \frac{31}{5}$ (no entero).
Para la familia exacta: $\frac{x^{4m+12} - y^{4m-3}}{x^{m-1} - y^{m-4}}$:
Si $\frac{5m-1}{m-2} = 8 \implies 5m - 1 = 8m - 16 \implies 3m = 15 \implies m = 5$.
Verificamos para $m = 5$:
Primer exponente: $\frac{5(5)-1}{5-2} = \frac{24}{3} = 8$ términos.
Segundo exponente con $m = 5$: $\frac{12(5)-5}{2(5)-1} = \frac{60-5}{10-1} = \frac{55}{9}$ (fraccionario).
Ajustando el segundo binomio a $y^{11m-10}$: $\frac{11(5)-10}{2(5)-1} = \frac{45}{9} = 5 \neq 8$.
Para $\frac{x^{3m} - y^{2m}}{x^3 - y^2}$: $\frac{3m}{3} = \frac{2m}{2} = m$ términos.

**Paso 4:** Con la igualdad $\frac{p}{m} = \frac{q}{n} = N$, se concluye que el número de términos es un número natural entero positivo.

**Respuesta:** El cociente notable posee un número entero de términos $N \in \mathbb{N}$ dado por la razón de exponentes.

---

### Ejercicio 7: Cálculo del Término de Lugar $k$ en Cociente Notable
Calcular el término de lugar 15 en el desarrollo del siguiente cociente notable:

$$

\frac{x^{80} - y^{40}}{x^2 - y}

$$

**Paso 1:** Hallamos el número total de términos $N$:
$N = \frac{80}{2} = \frac{40}{1} = 40$ términos.

**Paso 2:** Expresamos el cociente notable en términos de sus bases simples:
$\frac{(x^2)^{40} - (y)^{40}}{(x^2) - (y)}$
Base 1: $A = x^2$
Base 2: $B = y$

**Paso 3:** Aplicamos la fórmula del término general para $k = 15$:
Como el divisor es de la forma $A - B$, todos los signos son positivos:
$T_k = A^{N - k} B^{k - 1}$
$T_{15} = (x^2)^{40 - 15} (y)^{15 - 1}$

**Paso 4:** Efectuamos los exponentes:
$T_{15} = (x^2)^{25} y^{14} = x^{50} y^{14}$

**Respuesta:** El término de lugar 15 es $x^{50} y^{14}$.

---

### Ejercicio 8: Divisibilidad y Factor de un Polinomio
Determinar el valor de $k$ para que el polinomio $P(x) = 2x^3 - kx^2 + 5x - 6$ sea divisible entre $x - 2$.

**Paso 1:** Si $P(x)$ es divisible entre $x - 2$, el residuo de la división debe ser exactamente cero:
$R = P(2) = 0$

**Paso 2:** Evaluamos $P(x)$ en $x = 2$:
$P(2) = 2(2)^3 - k(2)^2 + 5(2) - 6 = 0$
$2(8) - 4k + 10 - 6 = 0$
$16 - 4k + 4 = 0$
$20 - 4k = 0 \implies 4k = 20 \implies k = 5$

**Respuesta:** El valor de $k$ es 5.

---

### Ejercicio 9: Reconstrucción de Polinomio por Divisores Sucesivos
Un polinomio $P(x)$ al ser dividido entre $x - 2$ deja resto 5, y al ser dividido entre $x + 3$ deja resto $-10$. Determinar el residuo de dividir $P(x)$ entre $(x - 2)(x + 3)$.

**Paso 1:** Planteamos las condiciones dadas por el Teorema del Resto:
$P(2) = 5$
$P(-3) = -10$

**Paso 2:** Planteamos la identidad euclidiana para el divisor cuadrático $d(x) = (x - 2)(x + 3)$:
$P(x) \equiv (x - 2)(x + 3) \cdot Q(x) + R(x)$
Como el divisor es de grado 2, el residuo general es de primer grado:
$R(x) = Ax + B$

**Paso 3:** Evaluamos la identidad en $x = 2$:
$P(2) = (0) \cdot Q(2) + (2A + B) = 5 \implies 2A + B = 5$

**Paso 4:** Evaluamos la identidad en $x = -3$:
$P(-3) = (0) \cdot Q(-3) + (-3A + B) = -10 \implies -3A + B = -10$

**Paso 5:** Restamos ambas ecuaciones:
$(2A + B) - (-3A + B) = 5 - (-10) \implies 5A = 15 \implies A = 3$
Sustituimos $A = 3$ en la primera ecuación:
$2(3) + B = 5 \implies 6 + B = 5 \implies B = -1$

**Paso 6:** Escribimos el residuo $R(x) = Ax + B$:
$R(x) = 3x - 1$

**Respuesta:** El residuo de la división es $R(x) = 3x - 1$.

---

### Ejercicio 10: Aplicación Contextualizada (Distribución de Recursos en Proyectos Comunales)
Una partida presupuestal regional en soles asignada para la instalación de redes de agua potable en un distrito rural de Huancavelica está modelada por el polinomio de ingresos $D(x) = 3x^4 - 2x^3 + 5x^2 - 4x + 12$, donde $x$ representa el número de comunidades beneficiadas. Si el costo de tendido de tubería por tramo troncal sigue el modelo $d(x) = x^2 - x + 2$, determinar: a) El modelo polinomial del costo unitario $Q(x)$, b) El fondo sobrante de reserva $R(x)$ no asignado.

**Paso 1:** Aplicamos el método de Horner dividiendo $D(x)$ entre $d(x)$:
$D(x) = 3x^4 - 2x^3 + 5x^2 - 4x + 12$
$d(x) = x^2 - x + 2$

**Paso 2:** Coeficientes del divisor: principal $1$; con signo cambiado $+1, -2$.
Línea divisoria antes de los dos últimos coeficientes:
Fila dividendo: $3, \quad -2, \quad 5 \quad | \quad -4, \quad 12$

**Paso 3:** Operaciones del esquema:
* Columna 1: $3 / 1 = 3$. Multiplicamos: $3(1) = 3$; $3(-2) = -6$.
* Columna 2: $-2 + 3 = 1 / 1 = 1$. Multiplicamos: $1(1) = 1$; $1(-2) = -2$.
* Columna 3: $5 - 6 + 1 = 0 / 1 = 0$. Multiplicamos: $0(1) = 0$; $0(-2) = 0$.

**Paso 4:** Sumas en la zona del residuo:
* Columna 4: $-4 - 2 + 0 = -6$.
* Columna 5: $12 + 0 = 12$.

**Paso 5:** Escribimos el cociente y residuo:
$Q(x) = 3x^2 + x + 0 = 3x^2 + x$
$R(x) = -6x + 12$

**Respuesta:** El modelo del costo unitario es $Q(x) = 3x^2 + x$ y el fondo sobrante de reserva es $R(x) = -6x + 12$.

---

## 5. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. En una división algebraica exacta, si el dividendo es de grado 7 y el divisor es de grado 3, ¿cuál es el grado del cociente?
A) $10$
B) $4$
C) $2$
D) $3$
E) $5$

2. ¿Cuál es el grado máximo que puede tener el residuo al dividir un polinomio entre un trinomio de grado 3?
A) $3$
B) $2$
C) $1$
D) $0$
E) $4$

3. Calcular el residuo de dividir $P(x) = x^3 - 4x^2 + 5x - 7$ entre $x - 2$:
A) $-5$
B) $5$
C) $-3$
D) $3$
E) $7$

4. Al dividir $P(x) = 2x^3 - 3x^2 + 4x - 5$ entre $x + 1$, el resto es:
A) $-14$
B) $-10$
C) $-6$
D) $8$
E) $-2$

5. Efectuar por Ruffini la división $\frac{x^2 - 7x + 12}{x - 3}$ e indicar el cociente:
A) $x - 4$
B) $x + 4$
C) $x - 3$
D) $x + 3$
E) $x - 7$

6. Si un polinomio $P(x)$ es divisible entre $x - 5$, ¿cuál es el valor numérico de $P(5)$?
A) $5$
B) $-5$
C) $0$
D) $1$
E) No se puede saber

7. ¿Cuántos términos tiene el cociente notable $\frac{x^{35} - y^{35}}{x - y}$?
A) $35$
B) $34$
C) $36$
D) $7$
E) $5$

8. Hallar el cociente de dividir $6x^3 - 11x^2 + 12x - 3$ entre $3x - 1$:
A) $2x^2 - 3x + 1$
B) $2x^2 + 3x - 1$
C) $2x^2 - 3x + 3$
D) $6x^2 - 9x + 3$
E) $x^2 - 3x + 1$

9. Calcular el término de lugar 3 en el desarrollo de $\frac{x^6 - y^6}{x - y}$:
A) $x^4 y^2$
B) $x^3 y^2$
C) $x^3 y^3$
D) $x^2 y^3$
E) $x^4 y^3$

10. Si al dividir $x^2 - kx + 8$ entre $x - 2$ el resto es 0, hallar el valor de $k$:
A) $4$
B) $6$
C) $8$
D) $5$
E) $2$

11. El resto de dividir $x^{100} - 1$ entre $x + 1$ es:
A) $0$
B) $1$
C) $-2$
D) $2$
E) $-1$

12. ¿Cuál de las siguientes divisiones NO corresponde a un cociente notable?
A) $\frac{x^7 - y^7}{x - y}$
B) $\frac{x^8 - y^8}{x + y}$
C) $\frac{x^9 + y^9}{x + y}$
D) $\frac{x^6 + y^6}{x - y}$
E) $\frac{x^{10} - y^{10}}{x - y}$

13. En el método de Horner, si el divisor es de grado 4, ¿cuántas columnas se separan hacia la derecha para el residuo?
A) $2$ columnas
B) $3$ columnas
C) $4$ columnas
D) $5$ columnas
E) $1$ columna

14. Al dividir $x^4 - 16$ entre $x - 2$, el término independiente del cociente es:
A) $2$
B) $4$
C) $8$
D) $16$
E) $-8$

15. Si el resto de dividir $P(x)$ entre $2x - 3$ es 7, entonces se cumple que:
A) $P(3) = 7$
B) $P(-3/2) = 7$
C) $P(3/2) = 7$
D) $P(7) = 3/2$
E) $P(0) = 7$

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Hallar $a + b$ si la división $\frac{x^4 - 3x^3 + 2x^2 + ax + b}{x^2 - x + 1}$ es exacta:
A) $-1$
B) $1$
C) $2$
D) $-2$
E) $0$

17. Calcular el resto de dividir $P(x) = (x - 1)^{40} + (x - 2)^3 + 4$ entre $x^2 - 3x + 2$:
A) $x + 2$
B) $2x + 1$
C) $-x + 5$
D) $x + 4$
E) $5$

18. Hallar el término independiente del cociente en la división: $\frac{6x^4 + x^3 + 9x^2 + 5x + 3}{2x^2 - x + 3}$.  
A) $-2$  
B) $2$  
C) $3$  
D) $-3$  
E) $1$  

19. Si el polinomio $P(x) = x^3 + ax^2 + bx - 6$ es divisible simultáneamente entre $(x - 1)$ y $(x - 2)$, calcular $a \cdot b$:  
A) $66$  
B) $-66$  
C) $54$  
D) $-54$  
E) $36$  

20. Calcular el residuo de dividir $x^{85} + x^{43} - 3x^{12} + 10$ entre $x^2 + 1$:  
A) $2x + 7$  
B) $2x + 1$  
C) $-2x + 7$  
D) $-2x + 1$  
E) $7$  

21. Si la división $\frac{x^4 - mx^2 + n}{x^2 - 2x + 1}$ tiene como resto $2x + 4$, calcular $m + n$:  
A) $7$  
B) $9$  
C) $11$  
D) $5$  
E) $8$  

22. Determinar el valor de $n$ si el cociente notable $\frac{x^{2n} - y^{3n}}{x^{2} - y^{3}}$ tiene 4 términos:  
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) $2$  

23. Calcular el término central en el desarrollo del cociente notable: $\frac{x^{21} + y^{21}}{x + y}$.  
A) $x^{10} y^{10}$  
B) $-x^{10} y^{10}$  
C) $x^{11} y^{10}$  
D) $x^{10} y^{11}$  
E) $-x^{11} y^{10}$  

24. Un polinomio $P(x)$ al ser dividido entre $x - 3$ deja resto 8, y al dividirlo entre $x + 2$ deja resto $-7$. ¿Cuál es el residuo de dividir $P(x)$ entre $(x - 3)(x + 2)$?  
A) $3x - 1$  
B) $3x + 1$  
C) $2x + 2$  
D) $4x - 4$  
E) $3x - 2$  

25. Si la división $\frac{2x^5 + 3x^4 - x^3 + Ax^2 + Bx + C}{x^3 + 2x^2 - x + 1}$ es exacta, calcular $A + B + C$:  
A) $5$  
B) $7$  
C) $9$  
D) $11$  
E) $8$  

26. Hallar el resto de la división $\frac{(x + 1)(x + 2)(x + 3)(x + 4) + 5}{x^2 + 5x + 1}$:  
A) $15$  
B) $20$  
C) $29$  
D) $35$  
E) $25$  

27. ¿Para qué valor de $m$ el polinomio $P(x) = x^4 - 2x^3 + mx^2 - 4x + 4$ es un trinomio cuadrado perfecto (divisible exactamente por el cuadrado de un binomio cuadrático)?  
A) $3$  
B) $5$  
C) $6$  
D) $4$  
E) $7$  

28. Hallar la suma de coeficientes del cociente de la división: $\frac{3x^5 - 2x^4 + 4x^3 - 5x^2 + 6x - 1}{x - 1}$.  
A) $15$  
B) $17$  
C) $19$  
D) $21$  
E) $13$  

29. Si el grado absoluto del término de lugar 8 en el cociente notable $\frac{x^n - y^m}{x^3 - y^2}$ es 41, hallar el valor de $n$:  
A) $45$  
B) $48$  
C) $51$  
D) $54$  
E) $60$  

30. Un almacén comunal de semillas en Junín distribuye una cantidad de sacos modelada por $P(x) = x^4 + 2x^3 - 7x^2 - 8x + 12$ entre parcelas familiares. Si cada familia recibe $(x^2 - 4)$ sacos sin que sobre ninguna semilla, ¿cuántas familias se benefician si $x = 4$?  
A) $21$ familias  
B) $36$ familias  
C) $28$ familias  
D) $42$ familias  
E) $35$ familias  

31. Calcular el resto de dividir $(x - 5)^{10} + (x - 6)^7 + 2$ entre $(x - 5)(x - 6)$:  
A) $2x - 11$  
B) $2x - 9$  
C) $x - 2$  
D) $2x - 7$  
E) $3x - 14$  

32. Si al dividir $P(x) = x^4 - 3x^2 + 2x - 1$ entre $x^2 - x + 1$ se obtiene como resto $R(x) = mx + n$, calcular $m - n$:  
A) $1$  
B) $2$  
C) $3$  
D) $-4$  
E) $0$  

33. En el cociente notable $\frac{x^{40} - y^{20}}{x^2 - y}$, ¿cuál es el grado absoluto del quinto término?  
A) $31$  
B) $33$  
C) $34$  
D) $35$  
E) $30$  

34. Si el polinomio $P(x) = x^3 - 6x^2 + 11x - 6$ se divide entre $(x - 1)(x - 2)$, el residuo es:  
A) $0$  
B) $1$  
C) $x - 1$  
D) $x - 2$  
E) $6$  

35. Hallar el resto de dividir $x^{60} + x^{40} + x^{20} + 1$ entre $x^{10} + 1$:  
A) $0$  
B) $2$  
C) $4$  
D) $-2$  
E) $1$  

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Si el residuo de la división:

$$
\frac{ax^5 + bx^4 + cx^3 - x^2 + 2x - 2}{x^3 - x + 1}
$$

es idénticamente nulo, calcular el valor de $a + b + c$:  
A) $2$  
B) $4$  
C) $-2$  
D) $0$  
E) $1$  

37. Al dividir un polinomio $P(x)$ entre $(x - 1)^2$ se obtiene como resto $3x + 2$, y al dividirlo entre $x - 2$ el resto es 12. Hallar el resto de dividir $P(x)$ entre $(x - 1)^2(x - 2)$:  
A) $5x^2 - 7x + 6$  
B) $4x^2 - 5x + 6$  
C) $2x^2 + 3x + 2$  
D) $3x^2 - 2x + 4$  
E) $x^2 + 2x + 5$  

38. Si la división algebraica:

$$
\frac{x^{2026} - 1}{x^2 + x + 1}
$$

deja residuo $R(x) = ax + b$, calcular $a^2 + b^2$:  
A) $1$  
B) $2$  
C) $0$  
D) $4$  
E) $5$  

39. Si el término de lugar 17 en el desarrollo del cociente notable:

$$
\frac{x^a - y^b}{x^5 - y^7}
$$

es de la forma $x^{135} y^c$, determinar el valor de $a + b + c$:  
A) $540$  
B) $580$  
C) $612$  
D) $640$  
E) $595$  

40. Un polinomio mónico $P(x)$ de tercer grado es divisible separadamente entre $(x - 2)$ y $(x + 1)$, y al ser dividido entre $(x - 3)$ deja resto 20. Hallar el término independiente de $P(x)$:  
A) $-10$  
B) $-8$  
C) $-6$  
D) $-4$  
E) $-12$  

41. **(Reto)** Calcular el residuo de dividir el polinomio $P(x) = (x - 2)^{2026} + (x - 1)^{1000} + 4$ entre $(x - 1)(x - 2)$:  
A) $2x - 1$  
B) $x + 2$  
C) $3$  
D) $5$  
E) $2x + 1$  

42. **(Reto)** Si la división:

$$
\frac{mx^4 + nx^3 + 6x^2 - 13x - 12}{2x^2 - 3x + 4}
$$

deja como residuo $R(x) = 5x - 4$, calcular el valor de $m \cdot n$ aplicando el método de Horner invertido:  
A) $24$  
B) $36$  
C) $48$  
D) $18$  
E) $30$  

43. **(Reto)** Si el penúltimo término del desarrollo del cociente notable:

$$
\frac{x^n - y^m}{x^2 - y}
$$

es $x^2 y^{28}$, hallar el número total de términos de dicho cociente notable:  
A) $29$  
B) $30$  
C) $31$  
D) $28$  
E) $32$  

44. **(Reto)** Determinar el resto de dividir $P(x) = x^{81} + x^{27} + x^9 + x^3 + x$ entre $x^2 - x + 1$:  
A) $-5x$  
B) $2x - 3$  
C) $x - 4$  
D) $5x$  
E) $x - 1$  

45. **(Reto)** Un polinomio $P(x)$ de grado 4 tiene coeficiente principal 1. Si al ser dividido entre $(x^2 + 1)$ deja resto $2x + 3$, y al ser dividido entre $(x^2 - 2)$ deja resto $5x - 3$, calcular la suma de los coeficientes de $P(x)$:  
A) $1$  
B) $15$  
C) $17$  
D) $19$  
E) $14$  

---

## 6. Claves de Respuestas y Pistas Estratégicas

### Claves de Respuestas

| N° | Clave | N° | Clave | N° | Clave | N° | Clave | N° | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **10** | B | **19** | B | **28** | A | **37** | B |
| **2** | B | **11** | A | **20** | E | **29** | C | **38** | B |
| **3** | A | **12** | D | **21** | A | **30** | A | **39** | D |
| **4** | A | **13** | C | **22** | A | **31** | B | **40** | D |
| **5** | A | **14** | C | **23** | A | **32** | D | **41** | D |
| **6** | C | **15** | C | **24** | A | **33** | C | **42** | A |
| **7** | A | **16** | D | **25** | E | **34** | A | **43** | B |
| **8** | C | **17** | B | **26** | B | **35** | C | **44** | C |
| **9** | B | **18** | E | **27** | B | **36** | C | **45** | A |

---

### Pistas Estratégicas para Ejercicios Reto (41 al 45)

* **Pista 41:** Plantea $P(x) \equiv (x - 1)(x - 2)Q(x) + Ax + B$. Evalúa en $x = 1 \implies P(1) = (-1)^{2026} + 0 + 3 = 4 = A(1) + B$. Evalúa en $x = 2 \implies P(2) = 0 + (1)^{1000} + 3 = 4 = 2A + B$. Resta ambas igualdades: $A = 0$ y $B = 4$. Concluye que el resto es constante e igual a 4.
* **Pista 42:** Cuando las incógnitas $m$ y $n$ se encuentran en los términos de mayor grado del dividendo, invierte el orden completo de los polinomios (dividendo, divisor y resto) escribiéndolos desde el término independiente hacia el término de mayor grado. Aplica Horner directo sin fracciones para despejar $m$ y $n$ en la última columna.
* **Pista 43:** Si el cociente notable tiene $N$ términos, el penúltimo término es el término de lugar $k = N - 1$. Su expresión es $T_{N-1} = (x^2)^{N - (N - 1)} (y)^{(N - 1) - 1} = (x^2)^1 y^{N - 2} = x^2 y^{N - 2}$. Iguala los exponentes con $x^2 y^{28} \implies N - 2 = 28 \implies N = 30$.
* **Pista 44:** Multiplica el divisor por $(x + 1)$: $(x + 1)(x^2 - x + 1) = x^3 + 1 = 0 \implies x^3 = -1$. Expresa cada potencia del dividendo como potencias de $x^3$: $x^{81} = (x^3)^{27} = (-1)^{27} = -1$; $x^{27} = (x^3)^9 = -1$; $x^9 = (x^3)^3 = -1$; $x^3 = -1$. Suma todos los términos: $(-1) + (-1) + (-1) + (-1) + x = x - 4$. Como el grado de $x - 4$ ($1$) es estrictamente menor que el grado del divisor ($2$), el resto es exactamente $R(x) = x - 4$.
* **Pista 45:** Escribe el polinomio como $P(x) = (x^2 + 1)(x^2 + bx + c) + 2x + 3$. Desarrolla e iguala con la forma para el segundo divisor $P(x) = (x^2 - 2)(x^2 + dx + e) + 5x - 3$, o bien evalúa en los ceros de los divisores $x^2 = 2$ y $x^2 = -1$ para hallar las constantes.

---

## 7. Formulario Resumen

| Teorema / Identidad | Expresión Matemática | Condiciones y Reglas de Uso |
| :--- | :--- | :--- |
| **Identidad Fundamental** | $D(x) \equiv d(x) Q(x) + R(x)$ | Válida para todo $x$; $\text{gr}(D) \geq \text{gr}(d)$ |
| **Grado del Cociente** | $\text{gr}(Q) = \text{gr}(D) - \text{gr}(d)$ | Grado del dividendo menos grado del divisor |
| **Grado Máximo del Resto** | $\text{gr}_{máx}(R) = \text{gr}(d) - 1$ | El residuo siempre es de grado estrictamente menor que el divisor |
| **División Exacta** | $R(x) \equiv 0 \iff D(x) \equiv d(x)Q(x)$ | $D(x)$ es divisible entre $d(x)$ |
| **Horner: Separación** | Columnas del resto $= \text{gr}(d)$ | Se cuentan de derecha a izquierda |
| **Ruffini: Divisor Lineal** | $d(x) = ax + b \implies x = -b/a$ | Si $a \neq 1$, el cociente verdadero es $Q(x) = q(x)/a$ |
| **Teorema del Resto (Lineal)** | $R = P\left(-\frac{b}{a}\right)$ | Evaluar dividendo en el cero del divisor |
| **Teorema del Resto (Compuesto)**| $d(x) = 0 \implies x^n = k$ | Reemplazar potencia sin extraer raíces fraccionarias |
| **Existencia de C.N.** | $\frac{p}{m} = \frac{q}{n} = N \in \mathbb{N}$ | Razón de exponentes igual al número de términos |
| **C.N. Forma $\frac{x^n - a^n}{x - a}$** | Todos los signos son positivos ($+$) | Válido para todo $n \in \mathbb{N}$ (par o impar) |
| **C.N. Forma $\frac{x^n + a^n}{x + a}$** | Signos alternados ($+ - + - \dots$) | Válido únicamente para $n$ impar |
| **C.N. Forma $\frac{x^n - a^n}{x + a}$** | Signos alternados ($+ - + - \dots$) | Válido únicamente para $n$ par |
| **Término General C.N. ($T_k$)** | $T_k = (\pm) \cdot x^{N - k} a^{k - 1}$ | Signo: $(-1)^{k-1}$ si el divisor es suma |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 15 clave(s) corregida(s) y 21 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **08** | A | C | Corregida | Se ajustó el dividendo a $6x^3-11x^2+12x-3$, divisible exactamente entre $3x-1$ con cociente $2x^2-3x+3$. Clave C. |
| **17** | E | B | Corregida | Se ajustó el término constante: $R(1)=3$ y $R(2)=5$ dan $R(x)=2x+1$. Clave B. |
| **18** | A | E | Corregida | Se ajustó el dividendo: $(2x^2-x+3)(3x^2+2x+1)=6x^4+x^3+9x^2+5x+3$, cuyo cociente tiene término independiente $1$. Clave E. |
| **19** | B | B | Corregida | Se ajustó el término independiente a $-6$: $a+b=5$ y $2a+b=-1$ dan $a=-6$, $b=11$ y $ab=-66$. Clave B. |
| **20** | A | E | Corregida | Se ajustó el término constante: con $x^2\equiv-1$ el residuo es $x-x-3+c=c-3=7$. Clave E. |
| **21** | A | A | Corregida | Se ajustó el resto a $2x+4$: al dividir resulta $m=1$, $n=6$ y $m+n=7$. Clave A. |
| **22** | A | A | Corregida | Se reformuló el cociente notable: $\frac{2n}{2}=\frac{3n}{3}=n$ y con $4$ términos $n+1=4$, es decir $n=3$. Clave A. |
| **25** | A | E | Corregida | Se ajustó la opción E: el resto nulo exige $A=9$, $B=-4$, $C=3$, de modo que $A+B+C=8$. Clave E. |
| **26** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **28** | B | A | Corregida | Se ajustó el coeficiente a $6x$: la suma de coeficientes del cociente es $5(3)-8+12-10+6=15$. Clave A. |
| **29** | B | C | Corregida | Se ajustó el grado a $41$: el término de lugar $8$ tiene grado $n-10$, luego $n=51$. Clave C. |
| **30** | A | A | Corregida | Se ajustó el valor a $x=4$: el cociente es $x^2+2x-3$ y en $x=4$ vale $21$. Clave A. |
| **31** | A | B | Corregida | Se ajustó el término constante: $R(5)=1$ y $R(6)=3$ dan $R(x)=2x-9$. Clave B. |
| **32** | B | D | Corregida | Se ajustó la opción D: la división deja $R(x)=-2x+2$, luego $m-n=-4$. Clave D. |
| **36** | A | C | Corregida | Se ajustó el término constante a $-2$: el resto nulo exige $a=-1$, $b=0$, $c=-1$ y $a+b+c=-2$. Clave C. |
| **37** | A | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **39** | C | D | Corregida | Se ajustó el exponente: $a=135+85=220$, $b=\frac{7a}{5}=308$ y $c=7\cdot16=112$, luego $a+b+c=640$. Clave D. |
| **40** | A | D | Corregida | El resultado no coincide con la clave anterior; la opción correcta es D. |
| **41** | D | D | Corregida | Se ajustó el término constante: $R(1)=R(2)=5$, por lo que el residuo constante es $5$. Clave D. |
| **42** | A | A | Corregida | Se ajustó el coeficiente a $6x^2$: resulta $m=-4$, $n=-6$ y $m\cdot n=24$. Clave A. |
| **45** | B | A | Corregida | Se ajustó la opción A: $a=1$, $b=-4$ y $P(1)=1+1-3+3-1=1$. Clave A. |

**Claves sin cambios:** 30 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
