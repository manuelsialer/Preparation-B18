# Tema 01: Intervalos en la Recta Real y Operaciones

## 1. Introducción y Contexto Real

En el estudio del análisis matemático y sus aplicaciones en ingeniería, ciencias de la computación y gestión de proyectos, las magnitudes físicas raramente se restringen a valores discretos o aislados. La temperatura de almacenamiento de vacunas en la cadena de frío del Ministerio de Salud (MINSA), la resistencia a la tracción del acero estructural en puentes andinos, el caudal admisible en canales de regadío en la costa peruana y los márgenes de error en la dosificación farmacológica se modelan mediante **conjuntos continuos de números reales**.

Un **intervalo** es un subconjunto de los números reales ($\mathbb{R}$) cuyos elementos se encuentran comprendidos entre dos extremos dados (finitos o infinitos), caracterizándose por la propiedad de convexidad topológica: si dos números pertenecen al intervalo, cualquier número real ubicado entre ellos también forma parte de dicho subconjunto.

Para el postulante a **Beca 18**, dominar las operaciones con intervalos (unión, intersección, diferencia y complemento) es el cimiento insustituible para resolver inecuaciones lineales, cuadráticas, fraccionarias y con valor absoluto, así como para determinar con precisión el dominio y rango de funciones reales de variable real.

---

## 2. Marco Teórico Riguroso

### 2.1 El Sistema de los Números Reales y la Recta Numérica

El conjunto de los números reales ($\mathbb{R}$) es un cuerpo conmutativo, ordenado y **completo** (cumple el axioma del supremo). Esto garantiza una correspondencia biunívoca (biyectiva) entre cada punto geométrico de una recta orientada y un número real exacto:
* A la derecha del origen ($0$) se ubican los reales positivos ($\mathbb{R}^+$).
* A la izquierda se ubican los reales negativos ($\mathbb{R}^-$).
* El orden natural establece que $a < b$ si y solo si la diferencia $(b - a)$ es estrictamente positiva ($b - a > 0$).

---

### 2.2 Clasificación de Intervalos

Sean $a, b \in \mathbb{R}$ dos números reales tales que $a \le b$:

#### 1. Intervalos Acotados (Finitos)

* **Intervalo Abierto:** Subconjunto de números reales comprendidos estrictamente entre $a$ y $b$. Los extremos no pertenecen al conjunto.
Notación: $\langle a, b \rangle$ o $]a, b[$.
Definición conjuntista:

$$
\langle a, b \rangle = \{ x \in \mathbb{R} \mid a < x < b \}
$$

Longitud del intervalo: $L = b - a$.

* **Intervalo Cerrado:** Subconjunto que incluye a ambos extremos $a$ y $b$.
Notación: $[a, b]$.
Definición conjuntista:

$$
[a, b] = \{ x \in \mathbb{R} \mid a \le x \le b \}
$$

Longitud del intervalo: $L = b - a$.

* **Intervalo Semiabierto por la Izquierda (o semicerrado por la derecha):** Excluye al extremo inferior $a$ e incluye al superior $b$.
Notación: $\langle a, b]$.
Definición conjuntista:

$$
\langle a, b] = \{ x \in \mathbb{R} \mid a < x \le b \}
$$

* **Intervalo Semiabierto por la Derecha (o semicerrado por la izquierda):** Incluye al extremo inferior $a$ y excluye al superior $b$.
Notación: $[a, b\rangle$.
Definición conjuntista:

$$
[a, b\rangle = \{ x \in \mathbb{R} \mid a \le x < b \}
$$

* **Intervalo Degenerado:** Si $a = b$, el intervalo cerrado se reduce a un conjunto unitario: $[a, a] = \{a\}$, mientras que $\langle a, a \rangle = \emptyset$.

---

#### 2. Intervalos No Acotados (Infinitos)

Son aquellos que se extienden indefinidamente hacia la derecha ($+\infty$) o hacia la izquierda ($-\infty$):

* Intervalo abierto hacia la derecha:

$$
\langle a, +\infty \rangle = \{ x \in \mathbb{R} \mid x > a \}
$$

* Intervalo cerrado hacia la derecha:

$$
[a, +\infty \rangle = \{ x \in \mathbb{R} \mid x \ge a \}
$$

* Intervalo abierto hacia la izquierda:

$$
\langle -\infty, b \rangle = \{ x \in \mathbb{R} \mid x < b \}
$$

* Intervalo cerrado hacia la izquierda:

$$
\langle -\infty, b] = \{ x \in \mathbb{R} \mid x \le b \}
$$

* Recta real completa:

$$
\langle -\infty, +\infty \rangle = \mathbb{R}
$$

> Nota importante de rigor: El infinito ($+\infty$ o $-\infty$) no es un número real, sino un concepto abstracto de no acotación métrica; por ende, los extremos con $\pm \infty$ siempre se escriben abiertos ($\langle$ o $\rangle$).

---

### 2.3 Operaciones con Intervalos

Dado que los intervalos son conjuntos de números reales, sobre ellos se definen las operaciones estándar de la teoría de conjuntos:

#### 1. Unión ($\cup$)
Reúne todos los elementos que pertenecen al menos a uno de los intervalos:

$$
A \cup B = \{ x \in \mathbb{R} \mid x \in A \lor x \in B \}
$$

#### 2. Intersección ($\cap$)
Formado por todos los números reales comunes a ambos intervalos:

$$
A \cap B = \{ x \in \mathbb{R} \mid x \in A \land x \in B \}
$$

Si $A \cap B = \emptyset$, se dice que $A$ y $B$ son **intervalos disjuntos**.

#### 3. Diferencia Relativa ($A - B$ o $A \setminus B$)
Conjunto de elementos que pertenecen a $A$ pero no pertenecen a $B$:

$$
A - B = \{ x \in \mathbb{R} \mid x \in A \land x \notin B \}
$$

Propiedad del borde crítico: Si $B$ contiene al número $c$ en su extremo cerrado, dicho número se sustrae de $A$, convirtiéndose el extremo resultante en abierto. Si $B$ tenía extremo abierto en $c$, el elemento $c$ permanece en $A$.

#### 4. Complemento ($A^c$ o $A'$)
Es la diferencia entre el conjunto universo ($\mathbb{R}$) y el intervalo $A$:

$$
A^c = \mathbb{R} - A = \{ x \in \mathbb{R} \mid x \notin A \}
$$

Leyes de De Morgan:

$$
(A \cup B)^c = A^c \cap B^c \qquad \text{y} \qquad (A \cap B)^c = A^c \cup B^c
$$

#### 5. Diferencia Simétrica ($A \ \Delta \ B$)
Conjunto de elementos que pertenecen a $A$ o a $B$, pero no a ambos simultáneamente:

$$
A \ \Delta \ B = (A \cup B) - (A \cap B) = (A - B) \cup (B - A)
$$

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Comprensión y Operaciones Directas)

#### Ejercicio 1: Intersección y Unión de Intervalos Acotados
Dados los intervalos en la recta real:
$A = \langle -4, 5]$ y $B = [1, 9\rangle$.
Determine el intervalo resultante de $A \cap B$ y el número de valores enteros que contiene $A \cup B$.

**Solución paso a paso:**

**Paso 1:** Graficar mental o analíticamente los extremos ordenados de menor a mayor en la recta real:
Extremos: $-4 < 1 < 5 < 9$.

**Paso 2:** Calcular la intersección $A \cap B$:
Buscamos los números reales $x$ tales que $x \in A$ y $x \in B$:
$x \in A \implies -4 < x \le 5$.
$x \in B \implies 1 \le x < 9$.
La región simultánea corresponde a los valores mayores o iguales a $1$ y menores o iguales a $5$:

$$
A \cap B = [1, 5]
$$

**Paso 3:** Calcular la unión $A \cup B$:
Buscamos los números reales que pertenecen al menos a uno de los intervalos:

$$
A \cup B = \langle -4, 9\rangle
$$

**Paso 4:** Contar los números enteros en $A \cup B$:
Los enteros estrictamente comprendidos entre $-4$ y $9$ son:
$\{-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8\}$.
Cantidad de enteros: $8 - (-3) + 1 = 12$ enteros.

*Respuesta:* $A \cap B = [1, 5]$ y la unión contiene $12$ números enteros.

---

#### Ejercicio 2: Diferencia de Intervalos y Análisis de Bordes
Sean los intervalos reales:
$M = [-5, 7\rangle$ y $N = \langle 2, 10]$.
Halle el intervalo resultante de $M - N$ y verifique si el número $2$ forma parte de dicho resultado.

**Solución paso a paso:**

**Paso 1:** Aplicar la definición de diferencia de conjuntos:
$M - N = \{ x \in \mathbb{R} \mid x \in M \land x \notin N \}$.

**Paso 2:** Analizar las condiciones analíticas:
$x \in M \implies -5 \le x < 7$.
$x \notin N \implies x \notin \langle 2, 10] \iff x \le 2 \lor x > 10$.

**Paso 3:** Intersectar el intervalo $M$ con la condición $x \le 2 \lor x > 10$:
Para $x \le 2$:
$[-5, 7\rangle \cap \langle -\infty, 2] = [-5, 2]$.
Para $x > 10$:
$[-5, 7\rangle \cap \langle 10, +\infty\rangle = \emptyset$.

**Paso 4:** Analizar el punto frontera $x = 2$:
Como en $N = \langle 2, 10]$ el $2$ es abierto ($2 \notin N$), al restar $N$ no se quita el $2$. Por ende, $x = 2$ permanece cerrado en la diferencia:

$$
M - N = [-5, 2]
$$

*Respuesta:* $M - N = [-5, 2]$, y el número $2$ sí pertenece al intervalo resultante.

---

#### Ejercicio 3: Complemento de una Unión de Intervalos
Sea el conjunto universo $U = \mathbb{R}$. Si $P = \langle -\infty, -2]$ y $Q = \langle 6, +\infty\rangle$, determine el complemento de la unión: $(P \cup Q)^c$.

**Solución paso a paso:**

**Paso 1:** Aplicar la primera Ley de De Morgan o la definición de complemento universal:
$(P \cup Q)^c = \mathbb{R} - (P \cup Q)$.

**Paso 2:** Analizar la región ocupada por $P \cup Q$:
Los números en $P \cup Q$ son aquellos tales que $x \le -2$ o $x > 6$.

**Paso 3:** Negar lógicamente la pertenencia a $P \cup Q$:
$x \notin (P \cup Q) \iff \neg(x \le -2 \lor x > 6) \iff (x > -2) \land (x \le 6)$.

**Paso 4:** Expresar en notación de intervalo:

$$
(P \cup Q)^c = \langle -2, 6]
$$

*Respuesta:* $(P \cup Q)^c = \langle -2, 6]$.

---

### Bloque B: Nivel Intermedio (Condiciones Compuestas y Parámetros)

#### Ejercicio 4: Intervalos con Parámetro y Condición de No Vacuidad
Dados los intervalos $A = [2k - 1, 15]$ y $B = [7, 3k + 5\rangle$, determine el conjunto de todos los valores reales de $k$ para los cuales ambos intervalos existen válidamente y su intersección $A \cap B$ no es vacía.

**Solución paso a paso:**

**Paso 1:** Establecer las condiciones de existencia de los intervalos:
Para $A = [2k - 1, 15]$: el extremo inferior debe ser menor o igual al superior:
$2k - 1 \le 15 \implies 2k \le 16 \implies k \le 8$.
Para $B = [7, 3k + 5\rangle$: el extremo inferior debe ser estrictamente menor al superior (dado que el superior es abierto y el intervalo debe ser no vacío):
$7 < 3k + 5 \implies 2 < 3k \implies k > \frac{2}{3}$.

**Paso 2:** Condición para que la intersección sea no vacía ($A \cap B \neq \emptyset$):
Dos intervalos $[a_1, b_1]$ y $[a_2, b_2\rangle$ con $a_1 \le b_1$ y $a_2 < b_2$ se intersectan si y solo si el máximo de los extremos inferiores es menor o igual al mínimo de los extremos superiores:
Extremos inferiores: $2k - 1$ y $7$.
Extremos superiores: $15$ y $3k + 5$.
Debe cumplirse:
1) $2k - 1 < 3k + 5 \implies -6 < k \implies k > -6$.
2) $7 \le 15$ (se cumple trivialmente).
3) $7 < 3k + 5 \implies k > \frac{2}{3}$.
4) $2k - 1 \le 15 \implies k \le 8$.

**Paso 3:** Intersectar todas las desigualdades obtenidas:
$k \le 8 \quad \land \quad k > \frac{2}{3} \quad \land \quad k > -6$.

$$
k \in \left\langle \frac{2}{3}, 8 \right]
$$

*Respuesta:* El conjunto de valores de $k$ es $\langle \frac{2}{3}, 8]$.

---

#### Ejercicio 5: Diferencia Simétrica y Longitud Total
Sean los intervalos $J = \langle -6, 4]$ y $K = [-1, 8\rangle$. Calcule la suma de las longitudes de los intervalos disjuntos que componen la diferencia simétrica $J \ \Delta \ K$.

**Solución paso a paso:**

**Paso 1:** Recordar la definición de diferencia simétrica:
$J \ \Delta \ K = (J - K) \cup (K - J)$.

**Paso 2:** Calcular $J - K$:
$J = \langle -6, 4]$, $K = [-1, 8\rangle$.
Restamos de $J$ todos los valores que pertenecen a $K$ (desde $-1$ inclusive hasta $4$ inclusive):
$J - K = \langle -6, -1\rangle$.
(Nótese que el $-1$ pertenecía a $K$, luego al restar se extrae y queda abierto en $-1$).

**Paso 3:** Calcular $K - J$:
Restamos de $K$ los valores que están en $J$ (desde $-1$ hasta $4$ inclusive):
$K - J = \langle 4, 8\rangle$.
(Nótese que el $4$ pertenecía a $J$, luego al restar se extrae y queda abierto en $4$).

**Paso 4:** Ensamblar $J \ \Delta \ K$ y calcular sus longitudes:

$$
J \ \Delta \ K = \langle -6, -1\rangle \cup \langle 4, 8\rangle
$$

Longitud del primer intervalo: $L_1 = -1 - (-6) = 5$.
Longitud del segundo intervalo: $L_2 = 8 - 4 = 4$.
Suma total de longitudes: $L_T = 5 + 4 = 9$.

*Respuesta:* $J \ \Delta \ K = \langle -6, -1\rangle \cup \langle 4, 8\rangle$, y la suma de sus longitudes es $9$.

---

#### Ejercicio 6: Variación de una Expresión Racional en un Intervalo
Si $x \in [2, 5\rangle$, determine el intervalo exacto de variación de la expresión racional:

$$
f(x) = \frac{3x - 1}{x + 2}
$$

**Solución paso a paso:**

**Paso 1:** Descomponer la fracción para aislar la variable en el denominador:
Efectuamos la división algebraica:

$$
\frac{3x - 1}{x + 2} = \frac{3(x + 2) - 7}{x + 2} = 3 - \frac{7}{x + 2}
$$

**Paso 2:** Construir la expresión paso a paso a partir del intervalo de partida $x \in [2, 5\rangle$:

$$
2 \le x < 5
$$

**Paso 3:** Sumar $2$ a cada miembro:

$$
4 \le x + 2 < 7
$$

**Paso 4:** Invertir la desigualdad (dado que todos los miembros son estrictamente positivos, el orden se invierte):

$$
\frac{1}{7} < \frac{1}{x + 2} \le \frac{1}{4}
$$

**Paso 5:** Multiplicar por $-7$ (al ser número negativo, se invierte nuevamente el sentido):

$$
-7 \cdot \frac{1}{4} \le -\frac{7}{x + 2} < -7 \cdot \frac{1}{7}
$$

$$
-\frac{7}{4} \le -\frac{7}{x + 2} < -1
$$

**Paso 6:** Sumar $3 = \frac{12}{4}$ a todos los miembros:

$$
3 - \frac{7}{4} \le 3 - \frac{7}{x + 2} < 3 - 1
$$

$$
\frac{5}{4} \le f(x) < 2
$$

*Respuesta:* La expresión varía en el intervalo $\left[ \frac{5}{4}, 2 \right\rangle$.

---

#### Ejercicio 7: Sistema de Restricciones Simultáneas
Halle el número de soluciones enteras que satisfacen simultáneamente el sistema de intervalos:
$x \in A \cap B^c$, donde $A = \{ x \in \mathbb{R} \mid -8 \le 2x + 4 < 16 \}$ y $B = \langle -3, 3]$.

**Solución paso a paso:**

**Paso 1:** Despejar $x$ en el conjunto $A$:
$-8 \le 2x + 4 < 16$.
Restamos $4$:
$-12 \le 2x < 12$.
Dividimos entre $2$:
$-6 \le x < 6 \implies A = [-6, 6\rangle$.

**Paso 2:** Determinar el complemento de $B$:
$B = \langle -3, 3] \implies B^c = \langle -\infty, -3] \cup \langle 3, +\infty\rangle$.

**Paso 3:** Realizar la intersección $A \cap B^c$:
$A \cap B^c = [-6, 6\rangle \cap (\langle -\infty, -3] \cup \langle 3, +\infty\rangle)$.
Distribuimos:
$([-6, 6\rangle \cap \langle -\infty, -3]) \cup ([-6, 6\rangle \cap \langle 3, +\infty\rangle) = [-6, -3] \cup \langle 3, 6\rangle$.

**Paso 4:** Identificar los valores enteros en el conjunto solución:
En $[-6, -3]$: $\{-6, -5, -4, -3\}$ ($4$ enteros).
En $\langle 3, 6\rangle$: $\{4, 5\}$ ($2$ enteros).
Total de soluciones enteras: $4 + 2 = 6$ enteros.

*Respuesta:* Hay $6$ soluciones enteras.

---

### Bloque C: Nivel Avanzado y Contextualizado (Beca 18 / UNI)

#### Ejercicio 8: Margen de Tolerancia en Sensores de Oxígeno Hospitalario
En una unidad de cuidados intensivos en Cusco, un sensor biomédico debe operar dentro de un rango de tolerancia de presión $P$ en kilopascales ($\text{kPa}$). El rango óptimo de operación es $O = [94{,}5; 102{,}8]$, el rango seguro ampliado con respaldo eléctrico es $S = \langle 91{,}2; 105{,}0\rangle$, y la zona de sobrecarga que dispara la válvula de alivio es $V = [101{,}5; 108{,}0]$.
Determine el intervalo de presiones que pertenece al rango seguro ampliado, pero que al mismo tiempo **no** es óptimo y **tampoco** dispara la válvula de alivio.

**Solución paso a paso:**

**Paso 1:** Traducir las condiciones verbales a operaciones de conjuntos:
Buscamos las presiones $P$ tales que:
$P \in S$ (rango seguro ampliado).
$P \notin O$ (no es óptimo).
$P \notin V$ (no dispara la válvula).
Esto equivale formalmente a:

$$
R = S - (O \cup V)
$$

**Paso 2:** Calcular la unión $O \cup V$:
$O = [94{,}5; 102{,}8]$ y $V = [101{,}5; 108{,}0]$.
Dado que $101{,}5 < 102{,}8$, los intervalos se solapan:

$$
O \cup V = [94{,}5; 108{,}0]
$$

**Paso 3:** Restar dicha unión del intervalo seguro $S = \langle 91{,}2; 105{,}0\rangle$:
$R = \langle 91{,}2; 105{,}0\rangle - [94{,}5; 108{,}0]$.
Los valores de $S$ menores a $94{,}5$ no forman parte de $O \cup V$.
Dado que $94{,}5$ está cerrado en $O \cup V$, al sustraerlo se excluye de $R$:

$$
R = \langle 91{,}2; 94{,}5\rangle
$$

Los valores mayores a $108{,}0$ no existen en $S$ pues $S$ termina en $105{,}0$.

*Respuesta:* El intervalo de presiones requerido es $\langle 91{,}2; 94{,}5\rangle\text{ kPa}$.

---

#### Ejercicio 9: Optimización de Horarios de Riego en Comunidades Campesinas
En una comunidad agrícola del Valle del Mantaro, se dispone de dos canales de regadío comunitarios ($C_1$ y $C_2$) cuyos turnos horarios permitidos (expresados en horas del día $t \in [0, 24]$) vienen dados por:
Canal 1: $C_1 = [4{,}5; 12{,}0] \cup [16{,}0; 21{,}5]$.
Canal 2: $C_2 = [8{,}0; 18{,}5]$.
Para evitar la erosión hídrica, la asamblea comunal establece que solo se debe regar cuando **exactamente uno** de los dos canales esté en funcionamiento. Determine el número de horas continuas o discontinuas durante el día en las cuales se cumple dicha disposición.

**Solución paso a paso:**

**Paso 1:** Modelar la condición "exactamente uno de los dos canales":
En teoría de conjuntos, la condición de que un elemento pertenezca a $C_1$ o a $C_2$, pero no a ambos a la vez, corresponde a la **diferencia simétrica**:

$$
T_{\text{riego}} = C_1 \ \Delta \ C_2 = (C_1 - C_2) \cup (C_2 - C_1)
$$

**Paso 2:** Calcular $C_1 - C_2$:
$C_1 = [4{,}5; 12{,}0] \cup [16{,}0; 21{,}5]$.
$C_2 = [8{,}0; 18{,}5]$.
Restamos $C_2$:
Del tramo $[4{,}5; 12{,}0]$, sustraemos $[8{,}0; 12{,}0]$, quedando $[4{,}5; 8{,}0\rangle$.
Del tramo $[16{,}0; 21{,}5]$, sustraemos $[16{,}0; 18{,}5]$, quedando $\langle 18{,}5; 21{,}5]$.
Por tanto:

$$
C_1 - C_2 = [4{,}5; 8{,}0\rangle \cup \langle 18{,}5; 21{,}5]
$$

**Paso 3:** Calcular $C_2 - C_1$:
De $C_2 = [8{,}0; 18{,}5]$, sustraemos los intervalos de $C_1$ que caen dentro:
$C_1$ contiene $[8{,}0; 12{,}0]$ y $[16{,}0; 18{,}5]$.
Al quitar ambos tramos, sobrevive el intervalo intermedio:

$$
C_2 - C_1 = \langle 12{,}0; 16{,}0\rangle
$$

**Paso 4:** Unir los resultados y sumar las duraciones:

$$
C_1 \ \Delta \ C_2 = [4{,}5; 8{,}0\rangle \cup \langle 12{,}0; 16{,}0\rangle \cup \langle 18{,}5; 21{,}5]
$$

Duración del tramo 1: $8{,}0 - 4{,}5 = 3{,}5\text{ horas}$.
Duración del tramo 2: $16{,}0 - 12{,}0 = 4{,}0\text{ horas}$.
Duración del tramo 3: $21{,}5 - 18{,}5 = 3{,}0\text{ horas}$.
Tiempo total de riego permitido:

$$
T_{\text{total}} = 3{,}5 + 4{,}0 + 3{,}0 = 10{,}5\text{ horas}
$$

*Respuesta:* El tiempo total es de $10{,}5\text{ horas}$ (o $10\text{ horas y } 30\text{ minutos}$).

---

#### Ejercicio 10: Intersección Generalizada y Punto de Acumulación
Para cada número natural $n \in \mathbb{N} = \{1, 2, 3, \dots\}$, se define una familia infinita de intervalos reales encajados mediante:

$$
I_n = \left[ 1 - \frac{1}{n}, \ 3 + \frac{2}{n} \right\rangle
$$

Determine el conjunto exacto resultante de la intersección infinita de todos los intervalos:

$$
S = \bigcap_{n=1}^\infty I_n
$$

**Solución paso a paso:**

**Paso 1:** Evaluar los primeros intervalos para observar el comportamiento:
Para $n = 1$: $I_1 = [0, 5\rangle$.
Para $n = 2$: $I_2 = \left[ \frac{1}{2}, 4 \right\rangle$.
Para $n = 3$: $I_3 = \left[ \frac{2}{3}, 3{,}\widehat{6} \right\rangle$.

**Paso 2:** Analizar el comportamiento del extremo inferior:
Sea $a_n = 1 - \frac{1}{n}$.
A medida que $n$ crece ($n \to \infty$), el término $\frac{1}{n}$ decrece hacia $0$:
$a_1 = 0 \le a_2 = \frac{1}{2} \le a_3 = \frac{2}{3} \le \dots \to 1$.
Para que un número $x$ pertenezca a todos los $I_n$, debe ser mayor o igual a todos los extremos inferiores:
$x \ge 1 - \frac{1}{n}$ para todo $n \ge 1$.
El límite superior de estos extremos es $\lim_{n \to \infty} \left(1 - \frac{1}{n}\right) = 1$.
Por tanto, debe cumplirse necesariamente $x \ge 1$.

**Paso 3:** Analizar el comportamiento del extremo superior:
Sea $b_n = 3 + \frac{2}{n}$.
A medida que $n$ crece, $b_n$ decrece estrictamente hacia $3$:
$b_1 = 5 > b_2 = 4 > b_3 = 3{,}\widehat{6} > \dots \to 3$.
Para que $x$ esté en todos los $I_n$, debe cumplirse $x < 3 + \frac{2}{n}$ para todo $n \in \mathbb{N}$.
¿Puede $x = 3$?
Si $x = 3$, como $\frac{2}{n} > 0$ para todo $n \in \mathbb{N}$, siempre ocurre que $3 < 3 + \frac{2}{n}$.
Por lo tanto, $x = 3$ pertenece a **todos** los $I_n$.
Sin embargo, si $x > 3$, por la propiedad arquimediana de los números reales existe un $n_0$ suficientemente grande tal que $\frac{2}{n_0} < x - 3$, lo que haría que $x \notin I_{n_0}$.
Por ende, la cota superior exacta que pertenece a la intersección es $x \le 3$.

**Paso 4:** Concluir el intervalo cerrado resultante:

$$
S = \bigcap_{n=1}^\infty I_n = [1, 3]
$$

*Respuesta:* El conjunto intersección es el intervalo cerrado $[1, 3]$.

---

## 4. Práctica Propuesta (45 Ejercicios)

### Bloque I: Nivel Básico (Problemas 01 al 15)

1. Si $A = \langle -5, 4]$ y $B = [-2, 8\rangle$, determine el intervalo resultante de $A \cap B$.
A) $\langle -2, 4]$  
B) $[-2, 4]$  
C) $[-2, 4\rangle$  
D) $\langle -5, 8\rangle$  
E) $[-5, 8]$  

2. Dados los conjuntos $M = [1, 7\rangle$ y $N = \langle 3, 10]$, halle la cantidad de números enteros en $M \cup N$.
A) $8$  
B) $9$  
C) $10$  
D) $11$  
E) $7$  

3. Si $P = [-3, 6]$ y $Q = \langle 1, 9\rangle$, ¿cuál es el intervalo equivalente a $P - Q$?
A) $[-3, 1]$  
B) $[-3, 1\rangle$  
C) $\langle -3, 1]$  
D) $[1, 6]$  
E) $\langle 1, 6]$  

4. Sean los intervalos $E = \langle -\infty, 5]$ y $F = \langle -2, +\infty\rangle$. Determine $E \cap F$.
A) $[-2, 5]$  
B) $\langle -2, 5\rangle$  
C) $\langle -2, 5]$  
D) $[-2, 5\rangle$  
E) $\mathbb{R}$  

5. Dado el intervalo $A = \langle -7, 2]$, halle su complemento con respecto a los números reales ($A^c$).
A) $\langle -\infty, -7] \cup \langle 2, +\infty\rangle$  
B) $\langle -\infty, -7\rangle \cup [2, +\infty\rangle$  
C) $\langle -\infty, -7] \cup [2, +\infty\rangle$  
D) $[-7, 2\rangle$  
E) $\langle -\infty, 2\rangle$  

6. Si $x \in [-1, 4]$, ¿a qué intervalo pertenece la expresión $y = 3x + 5$?
A) $[2, 17]$  
B) $\langle 2, 17\rangle$  
C) $[2, 12]$  
D) $[-3, 17]$  
E) $[5, 17]$  

7. Si $x \in \langle -2, 3\rangle$, determine el intervalo en el cual varía $z = 4 - 2x$.
A) $\langle -2, 8\rangle$  
B) $\langle -8, 2\rangle$  
C) $[-2, 8]$  
D) $\langle -2, 6\rangle$  
E) $\langle 0, 8\rangle$  

8. Dados $A = \langle -6, 1]$ y $B = [-4, 5\rangle$, halle el número de elementos enteros que pertenecen a $B - A$.
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) $2$  

9. Sean los intervalos $I = [-8, -1]$ y $J = \langle -3, 4\rangle$. Determine $I \ \Delta \ J$.
A) $[-8, -3] \cup [-1, 4\rangle$  
B) $[-8, -3\rangle \cup \langle -1, 4\rangle$  
C) $\langle -8, -3\rangle \cup [-1, 4]$  
D) $[-8, 4\rangle$  
E) $[-3, -1]$  

10. Si $A = \langle -\infty, 4\rangle$ y $B = [-1, +\infty\rangle$, determine $(A \cup B)^c$.
A) $\emptyset$  
B) $\mathbb{R}$  
C) $[-1, 4\rangle$  
D) $\langle -\infty, -1\rangle$  
E) $\langle 4, +\infty\rangle$  

11. Si la longitud del intervalo $I = [2a - 3, 5a + 1]$ es igual a $16$, halle el valor real de $a$.
A) $4$  
B) $5$  
C) $6$  
D) $3$  
E) $7$  

12. ¿Cuántos números enteros no negativos pertenecen al intervalo $K = \langle -4{,}8; \ 6{,}2]$?
A) $6$  
B) $7$  
C) $8$  
D) $5$  
E) $11$  

13. Si $x \in [3, 8\rangle$, determine el menor valor que puede tomar la expresión $E = 2x - 7$.
A) $-1$  
B) $0$  
C) $1$  
D) $-7$  
E) $9$  

14. Si $A = [-2, 5]$ y $B = \langle 0, 7]$, determine la suma del menor y mayor entero que pertenecen a $A \cap B$.
A) $5$  
B) $6$  
C) $7$  
D) $4$  
E) $8$  

15. Halle el intervalo correspondiente a los números reales que son mayores que $-3$ pero como máximo iguales a $11$.
A) $\langle -3, 11]$  
B) $[-3, 11\rangle$  
C) $\langle -3, 11\rangle$  
D) $[-3, 11]$  
E) $\langle -\infty, 11]$  

---

### Bloque II: Nivel Intermedio (Problemas 16 al 30)

16. Si $x \in \langle 1, 4]$, determine el intervalo exacto de variación de $f(x) = \frac{12}{x + 2}$.
A) $[2, 4\rangle$  
B) $\langle 2, 4]$  
C) $[2, 4]$  
D) $\langle 2, 6\rangle$  
E) $[3, 4\rangle$  

17. Dados los intervalos $A = [3k - 2, 14]$ y $B = [4, 2k + 8\rangle$, halle la suma de los valores enteros de $k$ para los cuales $A \subset B$.
A) $6$  
B) $7$  
C) $9$  
D) $11$  
E) $5$  

18. Sean $P = \{ x \in \mathbb{R} \mid -5 < 2x - 1 \le 7 \}$ y $Q = \{ x \in \mathbb{R} \mid x^2 \le 16 \}$. Determine el intervalo $P \cap Q$.
A) $\langle -2, 4]$  
B) $[-4, 4]$  
C) $\langle -2, 4\rangle$  
D) $[-4, -2\rangle$  
E) $[0, 4]$  

19. Si $x \in [-3, 2\rangle$, ¿en qué intervalo varía la expresión $g(x) = x^2 - 4x + 7$?
A) $[3, 28]$  
B) $\langle 3, 28]$  
C) $[3, 28\rangle$  
D) $[7, 28]$  
E) $\langle -3, 7]$  

20. Dados los conjuntos de números reales $A = \langle -\infty, 2] \cup [6, +\infty\rangle$ y $B = \langle -1, 8\rangle$, halle el número de soluciones enteras del conjunto $(A \cap B)^c \cap \mathbb{Z}$ comprendidas en el intervalo cerrado $[-5, 10]$.
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) $7$  

21. Si $A = \left\langle \frac{m - 1}{2}, 5 \right]$ y $B = [2, 2m + 1\rangle$, ¿para qué valores de $m$ se verifica que $A \cap B = \emptyset$?
A) $m \ge 5 \lor m \le \frac{1}{2}$  
B) $m \ge 5 \lor m < \frac{1}{2}$  
C) $m > 5 \lor m \le 0$  
D) $m \ge 5$  
E) $m < \frac{1}{2}$  

22. Sean los intervalos $I = [-4, 6]$ y $J = \langle 1, 9\rangle$. Si $K = (I - J) \cup (J - I)$, determine el producto de los números enteros que pertenecen a $K$ y están en el intervalo $[-2, 3]$.
A) $0$  
B) $-2$  
C) $2$  
D) $-1$  
E) No existen enteros  

23. Si $x \in \langle 2, 6]$, determine el mayor valor que puede asumir la expresión racional $R(x) = \frac{2x + 5}{x - 1}$.
A) $9$  
B) $\frac{17}{5}$  
C) $8$  
D) $7$  
E) No tiene máximo  

24. Para qué valores reales de $p$ se cumple que el intervalo $J = [p^2 - 4, 3p + 6]$ no es vacío y su longitud máxima es $16$.
A) $[-1, 5]$  
B) $[0, 5]$  
C) $[-2, 5]$  
D) $[1, 4]$  
E) $[-2, 4]$  

25. Se tienen los intervalos $A_k = \left[ \frac{1}{k}, 2 - \frac{1}{k} \right]$ para $k \in \{2, 3, 4\}$. Determine la longitud del intervalo resultante de $A_2 \cup A_3 \cup A_4$.
A) $\frac{3}{2}$  
B) $\frac{5}{4}$  
C) $\frac{7}{4}$  
D) $1$  
E) $2$  

26. Si $x \in [-2, 3]$, halle el intervalo de variación de $H(x) = 5 - \sqrt{x + 3}$.
A) $[5 - \sqrt{6}, 4]$  
B) $[5 - \sqrt{6}, 5]$  
C) $[4, 5]$  
D) $[0, 5]$  
E) $\langle 4, 5 - \sqrt{6}\rangle$  

27. Dados los intervalos $A = \langle -6, 2]$ y $B = [-2, 8\rangle$. Se define el conjunto $C = (A^c \cap B^c)^c$. Halle la suma de los valores enteros positivos que no pertenecen a $C$.
A) $0$  
B) $8$  
C) $15$  
D) $9$  
E) $12$  

28. Si el conjunto $S = \{ x \in \mathbb{R} \mid |x - 3| \le 5 \}$ y el conjunto $T = \langle 1, 10]$, determine la longitud de $S \cap T$.
A) $7$  
B) $8$  
C) $9$  
D) $6$  
E) $5$  

29. Si $x \in \langle -4, 1]$, determine el intervalo de variación de $E = x^2 + 6x - 2$.
A) $[-11, 5]$  
B) $[-11, 7]$  
C) $\langle -10, 5]$  
D) $[-2, 5]$  
E) $\langle -11, 5]$  

30. Si $A = \langle -\infty, a]$ y $B = [b, +\infty\rangle$ son tales que $A \cup B = \mathbb{R}$ y $A \cap B = [-1, 4]$, halle el valor de $E = a^2 + b^2$.
A) $17$  
B) $25$  
C) $16$  
D) $15$  
E) $20$  

---

### Bloque III: Nivel Avanzado y Retos Beca 18 (Problemas 31 al 45)

31. En un laboratorio de biotecnología en Arequipa, se monitorea la temperatura $T$ (en ${}^\circ\text{C}$) de una cámara de cultivo bacteriano. El sistema activa ventilación si $T \in A = [24{,}5; 38{,}0\rangle$, activa calefacción si $T \in B = \langle 15{,}0; 26{,}2]$ y activa desinfección ultravioleta si $T \in C = [22{,}0; 30{,}5]$. Determine el intervalo de temperatura donde la ventilación y la desinfección operan simultáneamente pero la calefacción está apagada.
A) $\langle 26{,}2; 30{,}5]$  
B) $[26{,}2; 30{,}5]$  
C) $[24{,}5; 26{,}2]$  
D) $\langle 26{,}2; 38{,}0\rangle$  
E) $[22{,}0; 24{,}5\rangle$  

32. Si $x \in \langle -3, 2\rangle$, determine el intervalo exacto de variación de:

$$
F(x) = \frac{x^2 + 2}{x^2 + 1}
$$

A) $\left\langle 1, \frac{11}{10} \right\rangle$  
B) $\left\langle 1, 2 \right]$  
C) $\left] \frac{11}{10}, 2 \right]$  
D) $[1, 2]$  
E) $\left\langle 1, \frac{6}{5} \right]$  

33. Sean los intervalos $I_n = \left\langle -\frac{1}{n}, 2 + \frac{1}{n} \right]$ para todo $n \in \mathbb{N} = \{1, 2, 3, \dots\}$. Halle el conjunto resultante de la unión infinita:

$$
U = \bigcup_{n=1}^\infty I_n
$$

A) $[0, 2]$  
B) $\langle -1, 3]$  
C) $[-1, 3]$  
D) $\langle 0, 2]$  
E) $\langle -1, 2]$  

34. En la construcción del puente Huánuco-Tingo María, la viga principal de concreto soporta un esfuerzo de deformación admisible $\sigma$ comprendido en el intervalo $D = [12{,}4; 28{,}6]\text{ MPa}$. Si la carga viva induce una solicitación $S_1 = [8{,}0; 20{,}5]$ y el viento lateral induce $S_2 = [16{,}0; 32{,}0]$, determine la longitud del intervalo de esfuerzos en los cuales la estructura está sometida a viento lateral sin presencia de carga viva, pero manteniéndose en zona segura admisible.
A) $8{,}1\text{ MPa}$  
B) $6{,}5\text{ MPa}$  
C) $7{,}2\text{ MPa}$  
D) $9{,}0\text{ MPa}$  
E) $5{,}4\text{ MPa}$  

35. Si $x \in [3, 7]$, determine el intervalo al que pertenece la expresión:

$$
E = \frac{x^2 - 2x + 5}{x - 1}
$$

A) $[4, 7]$  
B) $\left[ 4, \frac{20}{3} \right]$  
C) $[5, 8]$  
D) $\left[ \frac{16}{3}, 7 \right]$  
E) $[4, 8]$  

36. Sean los conjuntos $A = \{ x \in \mathbb{R} \mid |2x - 3| < 7 \}$ y $B = \{ x \in \mathbb{R} \mid x^2 - 5x - 6 \le 0 \}$. Determine la suma de todos los enteros que pertenecen a la diferencia simétrica $A \ \Delta \ B$.
A) $10$  
B) $11$  
C) $5$  
D) $6$  
E) $9$  

37. Para cada $k \in \mathbb{Z}^+$, se define el intervalo $J_k = \left[ \frac{k}{k+1}, \frac{k+2}{k+1} \right\rangle$. Determine la intersección infinita $\bigcap_{k=1}^\infty J_k$.
A) $\{1\}$  
B) $[1, 2\rangle$  
C) $\emptyset$  
D) $\left[ \frac{1}{2}, 1 \right]$  
E) $\langle 1, 2\rangle$  

38. Se tiene un tanque reservorio en Moquegua. El caudal de entrada permite operar con volúmenes de agua $V$ (en $\text{m}^3$) pertenecientes al intervalo $E = [120, 480]$, y el caudal de salida opera en $S = [200, 600]$. Si una válvula de seguridad restringe el volumen a $R = [150, 350]$, determine el intervalo de volúmenes en los cuales ambos caudales pueden operar conjuntamente dentro del rango permitido por la válvula de seguridad.
A) $[200, 350]$  
B) $[150, 480]$  
C) $[200, 480]$  
D) $[120, 350]$  
E) $[150, 200]$  

39. Si $x \in \langle -2, 4\rangle$ e $y \in [-3, 5]$, determine el intervalo de variación del producto $P = x \cdot y$.
A) $\langle -10, 20\rangle$  
B) $[-12, 20\rangle$  
C) $\langle -12, 20\rangle$  
D) $[-10, 20]$  
E) $\langle -6, 20\rangle$  

40. Si $x \in [2, 6]$, halle el conjunto imagen de la función:

$$
h(x) = \frac{x^2 - 4x + 8}{x - 2 + \sqrt{x - 2} + 1}
$$

A) $[2, 4]$  
B) $[1, 5]$  
C) $[2, 5]$  
D) $[0, 4]$  
E) $[1, 4]$  

41. Considere los intervalos $A = [m, m + 4]$ y $B = [2m - 3, 2m + 5]$. Si se sabe que la longitud del intervalo intersección $A \cap B$ es exactamente $3$, halle la suma de los posibles valores reales de $m$.
A) $6$  
B) $4$  
C) $5$  
D) $3$  
E) $7$  

42. Si $x, y \in \mathbb{R}$ tales que $x \in [1, 3]$ e $y \in [2, 5]$, determine el intervalo en el cual varía la expresión:

$$
W = \frac{x + y}{x \cdot y}
$$

A) $\left[ \frac{7}{15}, \frac{3}{2} \right]$  
B) $\left[ \frac{8}{15}, \frac{4}{3} \right]$  
C) $\left[ \frac{2}{5}, 1 \right]$  
D) $\left[ \frac{7}{15}, 1 \right]$  
E) $\left[ \frac{1}{3}, \frac{3}{2} \right]$  

43. Sean $A = \langle -5, 2]$ y $B = [-1, 6\rangle$. Si el conjunto $X$ satisface $(A \cup X) \subset B$ y $(B \cap X) = A \cap B$, determine el número de intervalos cerrados no triviales de longitud entera que pueden ser solución para $X$.
A) Infinitos  
B) $0$  
C) $1$  
D) $3$  
E) $5$  

44. En el análisis de un microchip de telecomunicaciones en la UNI, tres señales de voltaje $V_1, V_2, V_3$ (en voltios) deben satisfacer que sus rangos operativos son $R_1 = [-1{,}5; 3{,}5]$, $R_2 = [0{,}5; 4{,}8\rangle$ y $R_3 = \langle -0{,}8; 2{,}4]$. Determine la longitud del intervalo donde la señal $1$ o la señal $2$ están activas, pero la señal $3$ se encuentra inactiva.
A) $3{,}7\text{ V}$  
B) $3{,}1\text{ V}$  
C) $2{,}8\text{ V}$  
D) $4{,}0\text{ V}$  
E) $2{,}5\text{ V}$  

45. Para cada $n \in \mathbb{N}$, sea el intervalo $K_n = \left[ \frac{2n - 1}{n}, \frac{3n + 4}{n} \right]$. Calcule la longitud del intervalo resultante de:

$$
\left( \bigcup_{n=1}^\infty K_n \right) - \left( \bigcap_{n=1}^\infty K_n \right)
$$

A) $4$  
B) $5$  
C) $3$  
D) $6$  
E) $2$  

---

## 5. Clave de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | B | **16** | A | **31** | A |
| **02** | C | **17** | B | **32** | B |
| **03** | A | **18** | A | **33** | B |
| **04** | C | **19** | B | **34** | A |
| **05** | A | **20** | A | **35** | B |
| **06** | A | **21** | B | **36** | B |
| **07** | A | **22** | A | **37** | C |
| **08** | B | **23** | E | **38** | A |
| **09** | B | **24** | C | **39** | C |
| **10** | A | **25** | A | **40** | A |
| **11** | C | **26** | A | **41** | A |
| **12** | B | **27** | A | **42** | B |
| **13** | A | **28** | A | **43** | B |
| **14** | B | **29** | A | **44** | B |
| **15** | A | **30** | A | **45** | B |

---

## 6. Pistas Metodológicas (Problemas 41 al 45)

* **Pista para el Ejercicio 41:**
La intersección de $A = [m, m + 4]$ y $B = [2m - 3, 2m + 5]$ depende de cuál extremo izquierdo es mayor. Se presentan dos configuraciones posibles:
Caso 1: $m \le 2m - 3 \implies m \ge 3$. Aquí el extremo inferior de la intersección es $2m - 3$. Para que la longitud sea $3$, el extremo superior debe ser $m + 4$, cumpliéndose $(m + 4) - (2m - 3) = 3 \implies 7 - m = 3 \implies m = 4$.
Caso 2: $2m - 3 < m \implies m < 3$. Aquí el extremo inferior es $m$. El extremo superior de la intersección es $2m + 5$, por lo que $(2m + 5) - m = 3 \implies m + 5 = 3 \implies m = -2$. Verifique la validez en cada caso y sume los valores encontrados ($4 + 2 = 6$).

* **Pista para el Ejercicio 42:**
Descomponga la expresión $W = \frac{x + y}{xy}$ dividiendo término a término:

$$
W = \frac{1}{y} + \frac{1}{x}
$$

A partir de $x \in [1, 3]$ se tiene $\frac{1}{x} \in \left[ \frac{1}{3}, 1 \right]$, y de $y \in [2, 5]$ se deduce $\frac{1}{y} \in \left[ \frac{1}{5}, \frac{1}{2} \right]$. Sume miembro a miembro los extremos para obtener el valor mínimo $\frac{1}{3} + \frac{1}{5} = \frac{8}{15}$ y el máximo $1 + \frac{1}{2} = \frac{3}{2}$.

* **Pista para el Ejercicio 43:**
Observe la condición $(A \cup X) \subset B$. Para que la unión esté contenida en $B$, necesariamente debe ocurrir que $A \subset B$. Sin embargo, $A = \langle -5, 2]$ posee elementos estrictamente menores que $-1$ (como $-4, -3$), mientras que $B = [-1, 6\rangle$ solo contiene números mayores o iguales a $-1$. Como $A \not\subset B$, no existe ningún conjunto $X$ que pueda satisfacer simultáneamente dicha inclusión. Por lo tanto, el número de soluciones es exactamente cero.

* **Pista para el Ejercicio 44:**
La unión de las dos primeras señales es $R_1 \cup R_2 = [-1{,}5; 4{,}8\rangle$. Restar la señal $R_3 = \langle -0{,}8; 2{,}4]$ equivale a extraer este segmento central. La diferencia $(R_1 \cup R_2) - R_3$ se fragmenta en dos intervalos disjuntos: $[-1{,}5; -0{,}8]$ de longitud $0{,}7\text{ V}$, y $[2{,}4; 4{,}8\rangle$ de longitud $2{,}4\text{ V}$. La longitud total combinada es $0{,}7 + 2{,}4 = 3{,}1\text{ V}$.

* **Pista para el Ejercicio 45:**
Analice los límites y cotas de $K_n = \left[ 2 - \frac{1}{n}, 3 + \frac{4}{n} \right]$.
Para la unión $\bigcup K_n$: el extremo inferior mínimo se da cuando $n = 1$, siendo $2 - 1 = 1$; el extremo superior máximo también se da cuando $n = 1$, siendo $3 + 4 = 7$. Por tanto, $\bigcup_{n=1}^\infty K_n = [1, 7]$.
Para la intersección $\bigcap K_n$: a medida que $n \to \infty$, $2 - \frac{1}{n} \to 2$ por la izquierda y $3 + \frac{4}{n} \to 3$ por la derecha, resultando el núcleo común $[2, 3]$.
La diferencia entre la unión y la intersección es $[1, 7] - [2, 3] = [1, 2\rangle \cup \langle 3, 7]$. La longitud total es $(2 - 1) + (7 - 3) = 1 + 4 = 5$.

---

## 7. Formulario Resumen

### Notación y Tipos de Intervalos en $\mathbb{R}$

| Tipo de Intervalo | Notación Estándar | Definición Conjuntista | Longitud ($L$) |
| :--- | :---: | :--- | :---: |
| **Abierto** | $\langle a, b \rangle$ | $\{ x \in \mathbb{R} \mid a < x < b \}$ | $b - a$ |
| **Cerrado** | $[a, b]$ | $\{ x \in \mathbb{R} \mid a \le x \le b \}$ | $b - a$ |
| **Semiabierto a Izquierda** | $\langle a, b]$ | $\{ x \in \mathbb{R} \mid a < x \le b \}$ | $b - a$ |
| **Semiabierto a Derecha** | $[a, b\rangle$ | $\{ x \in \mathbb{R} \mid a \le x < b \}$ | $b - a$ |
| **Infinito hacia Derecha** | $[a, +\infty\rangle$ | $\{ x \in \mathbb{R} \mid x \ge a \}$ | $\infty$ |
| **Infinito hacia Izquierda** | $\langle -\infty, b]$ | $\{ x \in \mathbb{R} \mid x \le b \}$ | $\infty$ |
| **Recta Real Completa** | $\langle -\infty, +\infty \rangle$ | $\mathbb{R}$ | $\infty$ |

---

### Operaciones Fundamentales con Intervalos

| Operación | Símbolo | Condición Lógica | Interpretación Gráfica |
| :--- | :---: | :--- | :--- |
| **Unión** | $A \cup B$ | $x \in A \lor x \in B$ | Todo lo que pertenece a $A$, a $B$ o a ambos |
| **Intersección** | $A \cap B$ | $x \in A \land x \in B$ | Zona de solapamiento común exclusiva |
| **Diferencia Relativa** | $A - B$ | $x \in A \land x \notin B$ | Lo que queda de $A$ tras sustraer $B$ |
| **Complemento** | $A^c = \mathbb{R} - A$ | $x \notin A$ | Todo el universo real exterior a $A$ |
| **Diferencia Simétrica** | $A \ \Delta \ B$ | $(A \cup B) - (A \cap B)$ | Solo en $A$ o solo en $B$ (excluye intersección) |

---

### Reglas Críticas para Desigualdades y Operaciones

| Caso Operativo | Propiedad Algebraica | Condición Necesaria |
| :--- | :--- | :--- |
| **Inversión Multiplicativa** | $a \le x \le b \implies \frac{1}{b} \le \frac{1}{x} \le \frac{1}{a}$ | $a$ y $b$ con el **mismo signo** ($a \cdot b > 0$) |
| **Multiplicación Negativa** | $a \le x \le b \implies -k \cdot b \le -k \cdot x \le -k \cdot a$ | $k > 0$ (el sentido de la desigualdad se invierte) |
| **Elevación al Cuadrado** | $0 \le x^2 \le \max(a^2, b^2)$ | Si $a < 0 < b$ (el intervalo contiene al cero) |
| **Elevación al Cuadrado** | $a^2 \le x^2 \le b^2$ | Si $0 \le a \le b$ (ambos extremos positivos) |
| **Borde en Diferencia** | $x \in [a, b] - [c, d\rangle \implies$ extremo en $c$ abierto | Si el sustraendo incluye a $c$, la resta lo elimina |
