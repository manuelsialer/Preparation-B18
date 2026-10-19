# Tema 04: Inecuaciones de Primer Grado

## 1. Introducción y Contexto Real

En la modelación matemática de problemas del mundo real, las condiciones operativas rara vez se expresan como igualdades fijas. Los requerimientos de ingeniería civil, la gestión de inventarios, la capacidad de carga de camiones de transporte en carreteras andinas y los presupuestos de proyectos agropecuarios se rigen primordialmente por **cotas, tolerancias y desigualdades**: límites máximos de peso que no deben superarse, temperaturas mínimas para evitar la pérdida de cosechas por heladas en Puno, o metas de ventas que garanticen una ganancia neta positiva.

Una **inecuación de primer grado** es una desigualdad algebraica condicionada donde la incógnita interviene con exponente unitario. Resolver una inecuación significa hallar el conjunto de todos los valores reales que hacen verdadera la desigualdad. En lugar de un valor numérico aislado, el conjunto solución adopta típicamente la forma de un **intervalo de números reales** o una unión de ellos, cuya representación en la recta numérica permite tomar decisiones informadas en situaciones de incertidumbre técnica y económica para el postulante a **Beca 18**.

---

## 2. Marco Teórico Riguroso

### 2.1 Definición Canónica y Desigualdades Fundamentales

Una inecuación lineal o de primer grado en una variable $x$ es toda expresión que puede reducirse a una de las cuatro formas canónicas:

$$
a \cdot x + b > 0 \qquad a \cdot x + b \ge 0
$$

$$
a \cdot x + b < 0 \qquad a \cdot x + b \le 0
$$

donde $a, b \in \mathbb{R}$ con $a \neq 0$.

El **conjunto solución ($CS$)** es el subconjunto de números reales que satisfacen la relación de orden:

$$
CS = \{ x \in \mathbb{R} \mid a \cdot x + b \gtrless 0 \}
$$

---

### 2.2 Axiomas de Orden y Reglas Operatorias Críticas

Para resolver una inecuación lineal preservando la equivalencia del conjunto solución, se aplican estrictamente los axiomas de orden en $\mathbb{R}$:

1. **Monotonía de la Adición:**
Si a ambos miembros de una desigualdad se les suma o resta un mismo número real $c$, el sentido de la desigualdad **se conserva**:

$$
x < y \iff x \pm c < y \pm c \quad (\forall c \in \mathbb{R})
$$

2. **Multiplicación por una Constante Positiva:**
Si ambos miembros se multiplican o dividen por una constante real estrictamente positiva ($k > 0$), el sentido de la desigualdad **se conserva**:

$$
x < y \iff k \cdot x < k \cdot y \quad (k > 0)
$$

3. **Multiplicación por una Constante Negativa (Regla Crítica de Inversión):**
Si ambos miembros se multiplican o dividen por un número real estrictamente negativo ($k < 0$), el sentido de la desigualdad **se invierte obligatoriamente**:

$$
x < y \iff k \cdot x > k \cdot y \quad (k < 0)
$$

> Advertencia Crítica de Rigor: En inecuaciones algebraicas está **estrictamente prohibido multiplicar en aspa o cancelar variables en denominadores** si no se tiene certeza matemática absoluta sobre el signo (positivo o negativo) de la expresión cancelada. Cancelar una expresión que puede ser negativa sin invertir el sentido o que puede anularse invalida todo el análisis.

---

### 2.3 Tipos Especiales de Inecuaciones Lineales

#### 1. Inecuaciones Dobles o Simultáneas
Adoptan la estructura $a \le P(x) \le b$. Se resuelven despejando la variable $x$ mediante operaciones uniformes simultáneas en los tres miembros, o descomponiendo en la conjunción lógica:

$$
a \le P(x) \le b \iff (P(x) \ge a) \ \land \ (P(x) \le b)
$$

El conjunto solución final es la **intersección** de ambos semiplanos o rayos en la recta real.

#### 2. Inecuaciones con Coeficientes Fraccionarios
Se multiplican todos los términos por el Mínimo Común Múltiplo (MCM) de los denominadores. Dado que el MCM de números positivos es siempre un escalar positivo, el sentido de la desigualdad se mantiene inalterado.

#### 3. Inecuaciones Fraccionarias Reducibles a Lineales
Si una inecuación presenta la forma $\frac{P(x)}{k} > 0$ con $k \in \mathbb{R} - \{0\}$ constante:
* Si $k > 0 \implies P(x) > 0$.
* Si $k < 0 \implies P(x) < 0$.

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Despeje y Reglas de Signo)

#### Ejercicio 1: Inecuación Lineal Simple con Multiplicación Negativa
Resuelva en $\mathbb{R}$ la siguiente inecuación lineal y exprese su conjunto solución en notación de intervalo:

$$
7 - 3(2x - 5) \le 4(x + 2) + 14
$$

**Solución paso a paso:**

**Paso 1:** Aplicar la propiedad distributiva para eliminar los paréntesis:
Primer miembro:
$7 - 6x + 15 = 22 - 6x$.
Segundo miembro:
$4x + 8 + 14 = 4x + 22$.
La inecuación se reduce a:

$$
22 - 6x \le 4x + 22
$$

**Paso 2:** Transponer términos:
Restamos $22$ a ambos miembros:

$$
-6x \le 4x
$$

Restamos $4x$ a ambos miembros:

$$
-10x \le 0
$$

**Paso 3:** Aplicar la regla de división por un número negativo:
Dividimos ambos miembros entre $-10$ invirtiendo obligatoriamente el sentido de la desigualdad:

$$
x \ge \frac{0}{-10} \implies x \ge 0
$$

**Paso 4:** Expresar el conjunto solución como intervalo:

$$
CS = [0, +\infty\rangle
$$

*Respuesta:* El conjunto solución es $[0, +\infty\rangle$.

---

#### Ejercicio 2: Inecuación con Fracciones y MCM
Determine el menor valor entero que satisface la inecuación:

$$
\frac{3x - 2}{4} - \frac{2x - 1}{3} < \frac{x + 1}{6} - 1
$$

**Solución paso a paso:**

**Paso 1:** Calcular el $\text{MCM}(4, 3, 6) = 12$.
Como $12 > 0$, multiplicamos toda la inecuación por $12$ sin alterar el sentido:

$$
12 \cdot \left(\frac{3x - 2}{4}\right) - 12 \cdot \left(\frac{2x - 1}{3}\right) < 12 \cdot \left(\frac{x + 1}{6}\right) - 12(1)
$$

Simplificamos cada término:

$$
3(3x - 2) - 4(2x - 1) < 2(x + 1) - 12
$$

**Paso 2:** Desarrollar los productos:

$$
9x - 6 - 8x + 4 < 2x + 2 - 12
$$

**Paso 3:** Reducir términos semejantes:

$$
x - 2 < 2x - 10
$$

**Paso 4:** Despejar la variable $x$:
Restamos $x$ a ambos miembros y sumamos $10$:

$$
-2 + 10 < 2x - x \implies 8 < x \iff x > 8
$$

En notación de intervalo: $x \in \langle 8, +\infty\rangle$.

**Paso 5:** Identificar el menor valor entero:
Dado que el extremo en $8$ es abierto ($x > 8$), el menor entero admisible es $x = 9$.

*Respuesta:* El menor valor entero es $9$.

---

#### Ejercicio 3: Inecuación Doble Simultánea
Halle la cantidad de números enteros que verifican la siguiente inecuación continua:

$$
-7 \le \frac{3 - 2x}{5} < 3
$$

**Solución paso a paso:**

**Paso 1:** Multiplicar los tres miembros por $5$ ($5 > 0$, el sentido no cambia):

$$
-7 \cdot 5 \le 3 - 2x < 3 \cdot 5
$$

$$
-35 \le 3 - 2x < 15
$$

**Paso 2:** Restar $3$ a los tres miembros:

$$
-35 - 3 \le -2x < 15 - 3
$$

$$
-38 \le -2x < 12
$$

**Paso 3:** Dividir los tres miembros entre $-2$ e invertir el sentido de todas las desigualdades:

$$
\frac{-38}{-2} \ge \frac{-2x}{-2} > \frac{12}{-2}
$$

$$
19 \ge x > -6 \iff -6 < x \le 19
$$

**Paso 4:** Contar la cantidad de números enteros en el intervalo $\langle -6, 19]$:
Los enteros son $\{-5, -4, -3, \dots, 18, 19\}$.
Cantidad de enteros: $19 - (-5) + 1 = 19 + 5 + 1 = 25$ enteros.

*Respuesta:* Existen $25$ números enteros que satisfacen la inecuación.

---

### Bloque B: Nivel Intermedio (Sistemas de Inecuaciones y Cotas)

#### Ejercicio 4: Sistema de Dos Inecuaciones Lineales
Resuelva el sistema de inecuaciones en la variable $x$:

$$
\begin{cases}
2(x - 3) + 5 > 3x - 7 \quad \text{--- (1)} \\
\frac{x + 4}{3} \ge \frac{2x - 1}{4} \quad \text{--- (2)}
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Resolver la inecuación (1):

$$
2x - 6 + 5 > 3x - 7 \implies 2x - 1 > 3x - 7
$$

Transponemos términos:

$$
-1 + 7 > 3x - 2x \implies 6 > x \iff x < 6
$$

Conjunto solución 1: $CS_1 = \langle -\infty, 6\rangle$.

**Paso 2:** Resolver la inecuación (2):
Multiplicamos por $\text{MCM}(3, 4) = 12$:

$$
4(x + 4) \ge 3(2x - 1)
$$

$$
4x + 16 \ge 6x - 3
$$

Transponemos términos:

$$
16 + 3 \ge 6x - 4x \implies 19 \ge 2x \implies x \le \frac{19}{2} = 9{,}5
$$

Conjunto solución 2: $CS_2 = \langle -\infty; 9{,}5]$.

**Paso 3:** Intersectar ambos conjuntos solución:

$$
CS = CS_1 \cap CS_2 = \langle -\infty, 6\rangle \cap \langle -\infty; 9{,}5] = \langle -\infty, 6\rangle
$$

*Respuesta:* El conjunto solución del sistema es $\langle -\infty, 6\rangle$.

---

#### Ejercicio 5: Límite Presupuestario en un Taller Productivo
Un grupo de artesanos de Chulucanas produce vasijas de cerámica decorativas. El costo de materiales e insumos por cada vasija es de $\text{S/ } 18$ y los costos fijos diarios del taller (electricidad del horno y alquiler) son de $\text{S/ } 120$. Si cada vasija se comercializa a $\text{S/ } 42$, ¿cuál es el número mínimo de vasijas que deben elaborar y vender en un día para obtener una ganancia neta superior a $\text{S/ } 300$?

**Solución paso a paso:**

**Paso 1:** Definir la variable:
Sea $x$ el número de vasijas producidas y vendidas en el día ($x \in \mathbb{Z}^+$).

**Paso 2:** Formular las expresiones de ingresos y costos:
Ingreso diario: $I(x) = 42x$.
Costo total diario: $C_T(x) = 120 + 18x$.
Utilidad diaria:

$$
U(x) = I(x) - C_T(x) = 42x - (120 + 18x) = 24x - 120
$$

**Paso 3:** Plantear la inecuación según la condición del problema:
La ganancia debe ser estrictamente superior a $\text{S/ } 300$:

$$
24x - 120 > 300
$$

**Paso 4:** Despejar $x$:

$$
24x > 420 \implies x > \frac{420}{24} = \frac{35}{2} = 17{,}5
$$

**Paso 5:** Interpretar en el dominio de números enteros:
Como $x$ debe ser un número entero de vasijas y $x > 17{,}5$, el menor entero admisible es $x = 18$.

*Respuesta:* Se deben elaborar y vender como mínimo $18$ vasijas al día.

---

#### Ejercicio 6: Inecuación Fraccionaria con Signo Constante en el Denominador
Resuelva en $\mathbb{R}$ la inecuación:

$$
\frac{5x - 7}{x^2 + 4} \le 0
$$

**Solución paso a paso:**

**Paso 1:** Analizar el signo del denominador:
Para todo número real $x \in \mathbb{R}$, se cumple que $x^2 \ge 0$.
Por lo tanto:

$$
x^2 + 4 \ge 4 > 0 \quad (\forall x \in \mathbb{R})
$$

El denominador es estrictamente positivo para cualquier valor real de $x$ y jamás se anula.

**Paso 2:** Multiplicar toda la inecuación por el denominador $(x^2 + 4)$:
Dado que $(x^2 + 4) > 0$, el sentido de la desigualdad no cambia:

$$
(x^2 + 4) \cdot \left(\frac{5x - 7}{x^2 + 4}\right) \le 0 \cdot (x^2 + 4)
$$

$$
5x - 7 \le 0
$$

**Paso 3:** Despejar la variable $x$:

$$
5x \le 7 \implies x \le \frac{7}{5}
$$

**Paso 4:** Expresar el conjunto solución:

$$
CS = \left\langle -\infty, \frac{7}{5} \right]
$$

*Respuesta:* El conjunto solución es $\left\langle -\infty, \frac{7}{5} \right]$.

---

#### Ejercicio 7: Rango de Variación Inversa
Si se sabe que $x \in [3, 8\rangle$, determine el intervalo de variación de la expresión:

$$
E = \frac{10}{2x - 1}
$$

**Solución paso a paso:**

**Paso 1:** Escribir la desigualdad del dominio de partida:

$$
3 \le x < 8
$$

**Paso 2:** Multiplicar por $2$:

$$
6 \le 2x < 16
$$

**Paso 3:** Restar $1$:

$$
5 \le 2x - 1 < 15
$$

Nótese que todos los términos son estrictamente positivos ($5 > 0$).

**Paso 4:** Invertir los términos (la relación de orden se invierte):

$$
\frac{1}{15} < \frac{1}{2x - 1} \le \frac{1}{5}
$$

**Paso 5:** Multiplicar por $10$ ($10 > 0$, el sentido se mantiene):

$$
10 \cdot \frac{1}{15} < \frac{10}{2x - 1} \le 10 \cdot \frac{1}{5}
$$

Simplificamos cada extremo:

$$
\frac{2}{3} < E \le 2
$$

*Respuesta:* La expresión varía en el intervalo semiabierto $\left\langle \frac{2}{3}, 2 \right]$.

---

### Bloque C: Nivel Avanzado y Contextualizado (Beca 18 / UNI)

#### Ejercicio 8: Restricción de Carga y Capacidad en Transporte Fluvial
Una lancha a motor que realiza viajes por el río Huallaga entre Yurimaguas y Lagunas tiene una capacidad de carga útil máxima de $2\,400\text{ kg}$. En cada viaje, la tripulación fija pesa $240\text{ kg}$ y el combustible con equipo de emergencia pesa $360\text{ kg}$. La lancha transporta pasajeros con un peso promedio de $75\text{ kg}$ (incluido su equipaje de mano) y sacos de granos de cacao de $60\text{ kg}$ cada uno.
Si en un viaje viajan exactamente $12\text{ pasajeros}$, ¿cuál es el número máximo de sacos de cacao que la embarcación puede transportar sin exceder el margen de seguridad náutica?

**Solución paso a paso:**

**Paso 1:** Calcular el peso fijo inicial a bordo:
Tripulación: $240\text{ kg}$.
Combustible y emergencia: $360\text{ kg}$.
Peso fijo total: $240 + 360 = 600\text{ kg}$.

**Paso 2:** Calcular el peso correspondiente a los pasajeros:
$12\text{ pasajeros} \times 75\text{ kg/pasajero} = 900\text{ kg}$.

**Paso 3:** Definir la variable y plantear la inecuación de capacidad máxima:
Sea $n$ el número de sacos de cacao a transportar ($n \in \mathbb{Z}^+$).
El peso total de la carga no debe exceder los $2\,400\text{ kg}$:

$$
600 + 900 + 60n \le 2\,400
$$

$$
1\,500 + 60n \le 2\,400
$$

**Paso 4:** Despejar $n$:

$$
60n \le 2\,400 - 1\,500 \implies 60n \le 900
$$

Dividimos entre $60$:

$$
n \le \frac{900}{60} = 15\text{ sacos}
$$

*Respuesta:* La lancha puede transportar como máximo $15$ sacos de cacao.

---

#### Ejercicio 9: Inecuación Lineal con Parámetros y Raíz Mínima Entera
Dada la inecuación en la variable real $x$:

$$
\frac{ax + 1}{2} - \frac{x - b}{3} > 1
$$

Se sabe que cuando $a = 3$ y $b = 2$, el conjunto solución es $\langle x_0, +\infty\rangle$. Determine el valor de $x_0$ y el menor entero que pertenece al conjunto solución.

**Solución paso a paso:**

**Paso 1:** Reemplazar los parámetros $a = 3$ y $b = 2$ en la inecuación:

$$
\frac{3x + 1}{2} - \frac{x - 2}{3} > 1
$$

**Paso 2:** Multiplicar toda la inecuación por $\text{MCM}(2, 3) = 6$:

$$
3(3x + 1) - 2(x - 2) > 6
$$

**Paso 3:** Desarrollar los productos:

$$
9x + 3 - 2x + 4 > 6
$$

$$
7x + 7 > 6
$$

**Paso 4:** Despejar $x$:

$$
7x > 6 - 7 \implies 7x > -1 \implies x > -\frac{1}{7}
$$

**Paso 5:** Identificar $x_0$ y el menor entero:
El extremo inferior es $x_0 = -\frac{1}{7} \approx -0{,}1428$.
El conjunto solución es $CS = \left\langle -\frac{1}{7}, +\infty \right\rangle$.
Los números enteros pertenecientes al intervalo son $\{0, 1, 2, 3, \dots\}$.
El menor número entero que pertenece al conjunto solución es $x = 0$.

*Respuesta:* $x_0 = -\frac{1}{7}$ y el menor entero solución es $0$.

---

#### Ejercicio 10: Inecuación Condicionada a un Subconjunto y Supremo
Determine el supremo (mínima cota superior) del conjunto de todos los valores reales de $k$ para los cuales la inecuación:

$$
(k^2 + 1)x - 2k \le 4x + 3
$$

se verifica para todo $x \in \langle -\infty, 1]$.

**Solución paso a paso:**

**Paso 1:** Agrupar los términos con la variable $x$ a un solo miembro:

$$
(k^2 + 1)x - 4x \le 2k + 3
$$

Factorizamos $x$:

$$
(k^2 - 3)x \le 2k + 3
$$

**Paso 2:** Analizar la condición de cumplimiento para todo $x \in \langle -\infty, 1]$:
Para que la inecuación se cumpla para valores arbitrariamente negativos de $x$ ($x \to -\infty$), el coeficiente $(k^2 - 3)$ no puede ser negativo, pues si fuese negativo, al dividir entre él la desigualdad se invertiría a $x \ge \text{constante}$, lo cual excluiría a la región $\langle -\infty, \dots\rangle$.
Tampoco puede ser cero con $2k + 3 < 0$.
Si $k^2 - 3 > 0$, al dividir se tiene:

$$
x \le \frac{2k + 3}{k^2 - 3}
$$

El conjunto solución de esta inecuación es $\left\langle -\infty, \frac{2k + 3}{k^2 - 3} \right]$.

**Paso 3:** Exigir la contención del intervalo dato:
Para que todo $x \in \langle -\infty, 1]$ satisfaga la desigualdad, el intervalo dato debe estar contenido en el conjunto solución:

$$
\langle -\infty, 1] \subseteq \left\langle -\infty, \frac{2k + 3}{k^2 - 3} \right] \iff 1 \le \frac{2k + 3}{k^2 - 3}
$$

**Paso 4:** Resolver la desigualdad resultante (recordando que $k^2 - 3 > 0$):
Multiplicamos por el denominador positivo $(k^2 - 3)$:

$$
k^2 - 3 \le 2k + 3
$$

Transponemos al primer miembro:

$$
k^2 - 2k - 6 \le 0
$$

Hallamos las raíces de la ecuación cuadrática asociada mediante fórmula general:

$$
k = \frac{2 \pm \sqrt{(-2)^2 - 4(1)(-6)}}{2} = \frac{2 \pm \sqrt{4 + 24}}{2} = \frac{2 \pm \sqrt{28}}{2} = 1 \pm \sqrt{7}
$$

Por el método de zonas, la solución de $k^2 - 2k - 6 \le 0$ es:

$$
1 - \sqrt{7} \le k \le 1 + \sqrt{7}
$$

Cruzamos con la condición previa $k^2 - 3 > 0 \implies k > \sqrt{3} \approx 1{,}732$ (dado que buscamos el supremo positivo):
Como $1 + \sqrt{7} \approx 1 + 2{,}645 = 3{,}645 > \sqrt{3}$, el valor máximo admisible es $k = 1 + \sqrt{7}$.

*Respuesta:* El supremo del conjunto de valores de $k$ es $1 + \sqrt{7}$.

---

## 4. Práctica Propuesta (45 Ejercicios)

### Bloque I: Nivel Básico (Problemas 01 al 15)

1. Resuelva la inecuación lineal: $5x - 3 > 2x + 9$.  
A) $\langle 4, +\infty\rangle$  
B) $[4, +\infty\rangle$  
C) $\langle -\infty, 4\rangle$  
D) $\langle 2, +\infty\rangle$  
E) $[2, +\infty\rangle$  

2. Halle el conjunto solución de: $4(x - 2) \le 2(3x + 1) - 4$.  
A) $[-3, +\infty\rangle$  
B) $\langle -\infty, -3]$  
C) $[-2, +\infty\rangle$  
D) $\langle -\infty, -2]$  
E) $[3, +\infty\rangle$  

3. ¿Cuántos números enteros positivos satisfacen la inecuación: $3x - 14 < 0$?  
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) Infinitos  

4. Resuelva en $\mathbb{R}$: $\frac{x}{3} - \frac{x}{2} \ge 1$.  
A) $\langle -\infty, -6]$  
B) $[-6, +\infty\rangle$  
C) $\langle -\infty, 6]$  
D) $[6, +\infty\rangle$  
E) $\langle -\infty, -1]$  

5. Determine el conjunto solución de la inecuación doble: $-3 \le 2x + 1 \le 7$.  
A) $[-2, 3]$  
B) $\langle -2, 3\rangle$  
C) $[-1, 3]$  
D) $[-2, 4]$  
E) $\langle -1, 4]$  

6. Si $x \in \langle -1, 4]$, ¿a qué intervalo pertenece la expresión $y = 5 - 2x$?  
A) $[-3, 7\rangle$  
B) $\langle -3, 7]$  
C) $[-3, 7]$  
D) $\langle -7, 3]$  
E) $[-7, 3\rangle$  

7. Halle el mayor número entero que verifica: $\frac{2x - 1}{5} < 3$.  
A) $6$  
B) $7$  
C) $8$  
D) $9$  
E) $5$  

8. Resuelva: $2(x - 5) - 3(2x + 1) > 4 - 5x$.  
A) $\langle 17, +\infty\rangle$  
B) $\langle -\infty, 17\rangle$  
C) $\langle 13, +\infty\rangle$  
D) $\langle -\infty, -17\rangle$  
E) $\langle -17, +\infty\rangle$  

9. Un estudiante tiene $\text{S/ } 80$. Si compra cuadernos de $\text{S/ } 6$ cada uno, ¿cuántos cuadernos como máximo puede comprar si debe conservar al menos $\text{S/ } 14$ para sus pasajes?  
A) $10$  
B) $11$  
C) $12$  
D) $9$  
E) $13$  

10. Resuelva la inecuación fraccionaria: $\frac{x - 4}{-3} \ge 2$.  
A) $\langle -\infty, -2]$  
B) $[-2, +\infty\rangle$  
C) $\langle -\infty, 2]$  
D) $[2, +\infty\rangle$  
E) $\langle -\infty, -10]$  

11. Si la inecuación $mx + 4 > 2$ tiene como conjunto solución a $\langle -\infty, 2\rangle$, halle el valor de $m$.  
A) $-1$  
B) $1$  
C) $-2$  
D) $2$  
E) $-\frac{1}{2}$  

12. ¿Cuál es el menor valor entero de $x$ que satisface: $\frac{x + 1}{2} + \frac{x - 1}{3} > 2$?  
A) $2$  
B) $3$  
C) $4$  
D) $1$  
E) $5$  

13. El triple de la cantidad de libros que tiene Sofía, disminuido en $7$, es menor que $38$. ¿Cuántos libros como máximo puede tener Sofía?  
A) $13$  
B) $14$  
C) $15$  
D) $12$  
E) $16$  

14. Resuelva en los números enteros no negativos: $4x - 5 \le 2x + 7$.  
A) $\{0, 1, 2, 3, 4, 5, 6\}$  
B) $\{1, 2, 3, 4, 5, 6\}$  
C) $\{0, 1, 2, 3, 4, 5\}$  
D) $\{0, 1, 2, 3, 4, 5, 6, 7\}$  
E) $\{1, 2, 3, 4, 5\}$  

15. Halle el intervalo solución de: $1 - \frac{x}{4} < \frac{2x - 3}{2}$.  
A) $\left\langle \frac{10}{5}, +\infty \right\rangle$  
B) $\langle 2, +\infty\rangle$  
C) $\left\langle \frac{8}{5}, +\infty \right\rangle$  
D) $\left\langle \frac{2}{5}, +\infty \right\rangle$  
E) $\left\langle -\infty, \frac{8}{5} \right\rangle$  

---

### Bloque II: Nivel Intermedio (Problemas 16 al 30)

16. Resuelva el sistema de inecuaciones: $3x - 2 \le 4x + 1$ y $2x + 5 > x + 8$.  
A) $\langle 3, +\infty\rangle$  
B) $[-3, +\infty\rangle$  
C) $[-3, 3\rangle$  
D) $\langle 3, 5]$  
E) $\emptyset$  

17. Determine el número de enteros que satisfacen simultáneamente:

$$
-4 < \frac{2x - 6}{3} \le 2
$$

A) $7$  
B) $8$  
C) $9$  
D) $10$  
E) $6$  

18. Si $x \in [-2, 5\rangle$, determine el intervalo de variación de $W = \frac{12}{2x + 5}$.  
A) $\left\langle \frac{4}{5}, 12 \right]$  
B) $\left[ \frac{4}{5}, 12 \right]$  
C) $\left\langle \frac{4}{5}, 12 \right\rangle$  
D) $\left[ \frac{4}{5}, 6 \right]$  
E) $\left\langle \frac{2}{5}, 12 \right]$  

19. Un agricultor de Canta dispone de una furgoneta para transportar sacos de papa de $50\text{ kg}$ y sacos de zanahoria de $30\text{ kg}$. Si debe transportar en total $40\text{ sacos}$ y la carga total no puede superar los $1\,500\text{ kg}$, ¿cuál es el número máximo de sacos de papa que puede cargar?  
A) $14$  
B) $15$  
C) $16$  
D) $12$  
E) $18$  

20. Si el conjunto solución de $(a - 2)x + 3 \le 2x + b$ es $[2, +\infty\rangle$, determine el valor de $b - 2a$.  
A) $-1$  
B) $1$  
C) $-2$  
D) $2$  
E) $0$  

21. Resuelva en $\mathbb{R}$: $\frac{2x - 5}{3} - \frac{x + 2}{4} \ge \frac{x - 3}{2} - 1$.  
A) $\langle -\infty, 4]$  
B) $[4, +\infty\rangle$  
C) $\langle -\infty, -4]$  
D) $[-4, +\infty\rangle$  
E) $\langle -\infty, 2]$  

22. Halle la suma de todos los números enteros que verifican la inecuación:

$$
-5 \le 1 - 3x < 10
$$

A) $-3$  
B) $-1$  
C) $0$  
D) $1$  
E) $3$  

23. Una empresa de telecomunicaciones ofrece dos planes de telefonía móvil:
Plan A: Cargo fijo de $\text{S/ } 25$ más $\text{S/ } 0{,}10$ por minuto de llamada.
Plan B: Cargo fijo de $\text{S/ } 40$ más $\text{S/ } 0{,}05$ por minuto de llamada.
¿A partir de cuántos minutos mensuales resulta más económico contratar el Plan B?  
A) Más de $300\text{ minutos}$  
B) Más de $250\text{ minutos}$  
C) Más de $280\text{ minutos}$  
D) Más de $320\text{ minutos}$  
E) Más de $350\text{ minutos}$  

24. Si $x \in \langle 1, 4]$, determine el intervalo al que pertenece $f(x) = \frac{3x + 2}{x + 1}$.  
A) $\left[ \frac{14}{5}, \frac{5}{2} \right\rangle$  
B) $\left\langle \frac{5}{2}, \frac{14}{5} \right]$  
C) $\left[ \frac{5}{2}, \frac{14}{5} \right]$  
D) $\left\langle 2, \frac{14}{5} \right]$  
E) $\left[ \frac{5}{2}, 3 \right\rangle$  

25. Halle el menor valor real de $M$ tal que para todo $x \in [2, 6]$ se cumpla que $4x - 7 \le M$.  
A) $15$  
B) $16$  
C) $17$  
D) $18$  
E) $19$  

26. Resuelva el sistema lineal de inecuaciones:

$$
\begin{cases}
\frac{x - 1}{2} < \frac{x + 2}{3} \\
\frac{x + 1}{4} \le \frac{x - 2}{3}
\end{cases}
$$

A) $[11, +\infty\rangle$  
B) $\langle -\infty, 7\rangle$  
C) $[7, 11\rangle$  
D) $\emptyset$  
E) $\langle -\infty, 11]$  

27. Una distribuidora de gas doméstico en Chiclayo tiene un costo operativo diario de $\text{S/ } 240$ más $\text{S/ } 32$ por balón envasado. Si vende cada balón a $\text{S/ } 48$, ¿cuántos balones debe vender al día como mínimo para obtener una utilidad no menor a $\text{S/ } 400$?  
A) $38$  
B) $40$  
C) $42$  
D) $45$  
E) $36$  

28. Determine el conjunto solución de: $\frac{x - 3}{x^2 + 2x + 5} \le 0$.  
A) $\langle -\infty, 3]$  
B) $[3, +\infty\rangle$  
C) $\langle -\infty, -1]$  
D) $\emptyset$  
E) $\mathbb{R}$  

29. Si $-2 \le x \le 3$, halle la longitud del intervalo en el que varía $P = 7 - 3x$.  
A) $12$  
B) $15$  
C) $14$  
D) $16$  
E) $18$  

30. ¿Cuántos números enteros impares satisfacen la inecuación: $2x - 7 < 3x - 1 \le 2x + 6$?  
A) $6$  
B) $7$  
C) $5$  
D) $8$  
E) $4$  

---

### Bloque III: Nivel Avanzado y Retos Beca 18 (Problemas 31 al 45)

31. Un ingeniero agrónomo en Tacna formula un abono líquido para olivos. Para no quemar las raíces, la concentración de sales $C$ (en gramos por litro) debe verificar:

$$
1{,}8 \le \frac{3C + 2{,}4}{4} < 3{,}6
$$

Determine la suma de los valores enteros de $C$ que cumplen con el rango de seguridad agronómica.  
A) $7$  
B) $9$  
C) $12$  
D) $15$  
E) $10$  

32. Determine todos los valores de $a \in \mathbb{R}$ para los cuales la inecuación:

$$
(a^2 - 4)x + a - 2 > 0
$$

tiene como conjunto solución a todo el conjunto de los números reales ($CS = \mathbb{R}$).  
A) $a = 2$  
B) $a = -2$  
C) $a > 2$  
D) $a < -2$  
E) No existe tal valor  

33. Un camión de transporte de carga pesada cruza el puente colgante de Paucartambo, cuya estructura admite una carga máxima total de $18\text{ toneladas}$. El camión vacío pesa $6{,}5\text{ toneladas}$. Si transporta $80\text{ sacos}$ de café de $50\text{ kg}$ cada uno y el resto de la carga se compone de cajas de fruta de $25\text{ kg}$, ¿cuál es el número máximo de cajas de fruta que puede transportar con seguridad?  
A) $280\text{ cajas}$  
B) $300\text{ cajas}$  
C) $320\text{ cajas}$  
D) $260\text{ cajas}$  
E) $350\text{ cajas}$  

34. Si $x \in \langle -3, 2]$, determine el intervalo exacto de variación de:

$$
R(x) = \frac{4 - 3x}{2x + 7}
$$

A) $\left[ -\frac{2}{11}, 13 \right\rangle$  
B) $\left\langle -\frac{2}{11}, 13 \right]$  
C) $\left[ -\frac{2}{11}, 7 \right\rangle$  
D) $\left\langle -1, 13 \right]$  
E) $\left[ 0, 13 \right\rangle$  

35. Resuelva en $\mathbb{R}$ la inecuación fraccionaria:

$$
\frac{2x - 1}{x + 3} \ge 2
$$

A) $\langle -\infty, -3\rangle$  
B) $[-3, +\infty\rangle$  
C) $\langle -3, +\infty\rangle$  
D) $\emptyset$  
E) $\mathbb{R} - \{-3\}$  

36. En una empresa de confecciones en Gamarra, el costo de producir $q$ camisas está dado por $C(q) = 1\,800 + 22q$ soles. Si las camisas se venden a $\text{S/ } 45$ cada una pero se otorgan comisiones del $5\%$ sobre las ventas a los promotores, ¿cuál es el número mínimo de camisas que deben venderse para obtener una utilidad neta de al menos $\text{S/ } 3\,000$?  
A) $232$  
B) $230$  
C) $231$  
D) $235$  
E) $240$  

37. Halle el conjunto de valores de $k$ para los cuales el sistema de inecuaciones en $x$:

$$
\begin{cases}
2x - 3 \le 5 \\
3x + k > 4
\end{cases}
$$

admite exactamente $3$ soluciones enteras.  
A) $\langle -5, -2]$  
B) $[-5, -2\rangle$  
C) $\langle -8, -5]$  
D) $[-8, -5\rangle$  
E) $\langle -6, -3]$  

38. Si se sabe que $a < b < 0$, resuelva en la variable $x$ la inecuación:

$$
\frac{x - a}{b} < \frac{x - b}{a}
$$

A) $\langle a + b, +\infty\rangle$  
B) $\langle -\infty, a + b\rangle$  
C) $\langle 0, a + b\rangle$  
D) $\langle -\infty, 0\rangle$  
E) $\mathbb{R}$  

39. Un reservorio de agua potable en Moquegua tiene capacidad para $50\,000\text{ litros}$. A las 6:00 a.m. contiene $14\,000\text{ litros}$. Si ingresa agua a razón de $3\,200\text{ L/h}$ y simultáneamente se distribuye a la población a razón de $1\,400\text{ L/h}$, ¿durante cuántas horas completas de bombeo continuo el reservorio mantendrá un volumen de agua inferior al $90\%$ de su capacidad total?  
A) $16\text{ horas}$  
B) $17\text{ horas}$  
C) $18\text{ horas}$  
D) $15\text{ horas}$  
E) $19\text{ horas}$  

40. Si la inecuación $\frac{ax + 3}{5} - \frac{bx - 1}{2} \ge 1$ tiene como conjunto solución a $\langle -\infty, 1]$, determine una relación necesaria entre los coeficientes $a$ y $b$.  
A) $2a - 5b = -1$  
B) $2a - 5b = 1$  
C) $5a - 2b = 1$  
D) $2a + 5b = 1$  
E) $a - b = 2$  

41. Determine el número de enteros que verifican la inecuación compuesta:

$$
\frac{x - 1}{2} < \frac{2x + 1}{3} \le \frac{3x - 2}{4}
$$

A) Infinitos  
B) $0$  
C) $5$  
D) $10$  
E) $7$  

42. Para qué valores reales del parámetro $m$ la inecuación $(m^2 - 9)x + m + 3 \le 0$ es satisfecha por todo número real $x \in \mathbb{R}$.  
A) $m = 3$  
B) $m = -3$  
C) $m \in \{-3, 3\}$  
D) $m < -3$  
E) No existe tal valor  

43. Un postulante a Beca 18 rinde una prueba de $60$ preguntas donde cada acierto suma $4$ puntos, cada error resta $1$ punto y las preguntas no respondidas no suman ni restan. Si respondió al menos $50$ preguntas y obtuvo un puntaje estrictamente mayor a $150$ puntos, ¿cuál es el número mínimo de preguntas que respondió correctamente?  
A) $39$  
B) $40$  
C) $41$  
D) $42$  
E) $38$  

44. Si $x \in \langle 2, 5]$, determine el conjunto al que pertenece:

$$
E = \frac{x^2 - 4x + 7}{x - 1}
$$

A) $\left[ \frac{11}{4}, 4 \right\rangle$  
B) $\left[ 2\sqrt{3} - 2, 4 \right]$  
C) $\left\langle 2\sqrt{3} - 2, 4 \right]$  
D) $[2, 4]$  
E) $\langle 2, 5]$  

45. Sean $a, b \in \mathbb{R}^+$ tales que $a + b = 1$. Determine el menor valor real de $k$ tal que para todo par de números reales positivos se verifique:

$$
\frac{1}{a} + \frac{1}{b} \ge k
$$

A) $2$  
B) $3$  
C) $4$  
D) $5$  
E) $6$  

---

## 5. Clave de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | A | **16** | A | **31** | B |
| **02** | A | **17** | C | **32** | E |
| **03** | B | **18** | A | **33** | B |
| **04** | A | **19** | B | **34** | A |
| **05** | A | **20** | A | **35** | A |
| **06** | A | **21** | A | **36** | A |
| **07** | C | **22** | A | **37** | A |
| **08** | A | **23** | A | **38** | A |
| **09** | B | **24** | B | **39** | B |
| **10** | A | **25** | C | **40** | A |
| **11** | A | **26** | A | **41** | A |
| **12** | B | **27** | B | **42** | B |
| **13** | B | **28** | A | **43** | C |
| **14** | A | **29** | B | **44** | B |
| **15** | C | **30** | A | **45** | C |

---

## 6. Pistas Metodológicas (Problemas 41 al 45)

* **Pista para el Ejercicio 41:**
Descomponga la inecuación compuesta en dos inecuaciones simultáneas:
Parte 1: $\frac{x - 1}{2} < \frac{2x + 1}{3} \implies 3(x - 1) < 2(2x + 1) \implies 3x - 3 < 4x + 2 \implies x > -5$.
Parte 2: $\frac{2x + 1}{3} \le \frac{3x - 2}{4} \implies 4(2x + 1) \le 3(3x - 2) \implies 8x + 4 \le 9x - 6 \implies x \ge 10$.
La intersección es $(x > -5) \land (x \ge 10) \implies x \in [10, +\infty\rangle$.
El intervalo tiene una cantidad infinita de números enteros.

* **Pista para el Ejercicio 42:**
Para que la desigualdad $(m^2 - 9)x + m + 3 \le 0$ sea satisfecha por todo $x \in \mathbb{R}$, el coeficiente de $x$ debe ser nulo:
$m^2 - 9 = 0 \implies m = 3 \lor m = -3$.
Si $m = 3$: $(0)x + 3 + 3 \le 0 \implies 6 \le 0$ (falso, no se cumple para ningún $x$).
Si $m = -3$: $(0)x + (-3) + 3 \le 0 \implies 0 \le 0$ (verdadero para todo $x \in \mathbb{R}$).
Por tanto, el único valor que cumple la condición es $m = -3$.

* **Pista para el Ejercicio 43:**
Sean $c$ el número de respuestas correctas e $i$ el de incorrectas.
Como respondió al menos $50$ preguntas: $c + i \ge 50 \implies i \ge 50 - c$.
Puntaje: $P = 4c - i > 150 \implies i < 4c - 150$.
Combinando ambas cotas para $i$:
$50 - c \le i < 4c - 150 \implies 50 - c < 4c - 150 \implies 5c > 200 \implies c > 40$.
El menor número entero de respuestas correctas es $c = 41$.

* **Pista para el Ejercicio 44:**
Descomponga algebraicamente la expresión dividiendo por $(x - 1)$:
$x^2 - 4x + 7 = (x - 1)(x - 3) + 4 = (x - 1)^2 - 2(x - 1) + 4$.
Sea $u = x - 1$. Como $x \in \langle 2, 5]$, se deduce $u \in \langle 1, 4]$.
La expresión queda $E = u - 2 + \frac{4}{u} = \left(u + \frac{4}{u}\right) - 2$.
Por la desigualdad de las medias, para $u > 0$: $u + \frac{4}{u} \ge 2\sqrt{u \cdot \frac{4}{u}} = 4$, alcanzándose el mínimo en $u = 2$ ($x = 3 \in \langle 2, 5]$).
El valor mínimo es $4 - 2 = 2$.
En el extremo $u = 4$ ($x = 5$): $E = 4 - 2 + 1 = 3$. En $u \to 1$: $E \to 1 - 2 + 4 = 3$.
Por consiguiente, el rango exacto es $[2, 3]$ o cerrado en función de la función continua.

* **Pista para el Ejercicio 45:**
Utilice la desigualdad de Cauchy-Schwarz o la media aritmética y armónica (MA $\ge$ MH):
Para $a, b > 0$: $\frac{a + b}{2} \ge \frac{2}{\frac{1}{a} + \frac{1}{b}} \implies \frac{1}{a} + \frac{1}{b} \ge \frac{4}{a + b}$.
Dado que $a + b = 1$:

$$
\frac{1}{a} + \frac{1}{b} \ge \frac{4}{1} = 4
$$

La igualdad se verifica cuando $a = b = \frac{1}{2}$. Por lo tanto, el menor valor de $k$ es $4$.

---

## 7. Formulario Resumen

### Axiomas de Orden y Reglas de Despeje en Inecuaciones

| Operación en Desigualdad | Regla Algebraica | Sentido de la Desigualdad |
| :--- | :--- | :---: |
| **Sumar o Restar $c$** | $A \le B \iff A \pm c \le B \pm c$ | Se mantiene inalterado |
| **Multiplicar por $k > 0$** | $A \le B \iff k \cdot A \le k \cdot B$ | Se mantiene inalterado |
| **Multiplicar por $k < 0$** | $A \le B \iff k \cdot A \ge k \cdot B$ | **Se invierte obligatoriamente** |
| **Inversión ($A, B > 0$)** | $0 < A \le x \le B \iff \frac{1}{B} \le \frac{1}{x} \le \frac{1}{A}$ | **Se invierte obligatoriamente** |

---

### Inecuaciones Dobles y Sistemas Lineales

| Estructura | Método Canónico | Conjunto Solución |
| :--- | :--- | :---: |
| **Inecuación Doble:** $a \le P(x) \le b$ | Despeje simultáneo o $P(x) \ge a \ \land \ P(x) \le b$ | Intersección de intervalos |
| **Sistema:** $A_1(x) \ge 0 \ \land \ A_2(x) \le 0$ | Resolver cada inecuación por separado | $CS = CS_1 \cap CS_2$ |
| **Denominador Constante Positivo:** $\frac{P(x)}{k} \le 0 \ (k > 0)$ | Multiplicar por $k$: $P(x) \le 0$ | Mismo sentido |
| **Denominador Constante Negativo:** $\frac{P(x)}{k} \le 0 \ (k < 0)$ | Multiplicar por $k$: $P(x) \ge 0$ | Sentido invertido |

---

### Modelos de Restricción Económica y Capacidad

| Aplicación Práctica | Inecuación Modelo | Condición de Optimización |
| :--- | :--- | :--- |
| **Ganancia Mínima** | $U(q) = (p_v - c_v)q - C_f \ge U_{\text{mín}}$ | $q \ge \frac{C_f + U_{\text{mín}}}{p_v - c_v}$ (entero superior) |
| **Capacidad de Carga** | $P_{\text{fijo}} + \sum w_i n_i \le W_{\text{máx}}$ | $n_i \le \text{capacidad neta}$ (entero inferior) |
| **Límite Presupuestario** | $C_{\text{fijo}} + c_{\text{unit}} \cdot x \le \text{Presupuesto}$ | $x \le \text{gasto admisible}$ (entero inferior) |
