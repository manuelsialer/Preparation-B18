# Tema 07: Función Cuadrática

Una función cuadrática es una función polinomial real de variable real cuya regla de correspondencia está dada por un polinomio de segundo grado de la forma:

$$
f(x) = ax^2 + bx + c
$$

donde $a, b, c \in \mathbb{R}$ son constantes reales con la condición indispensable de que $a \neq 0$. La variable independiente $x$ toma valores en todo el conjunto de los números reales, por lo que el dominio natural de toda función cuadrática es:

$$
\operatorname{Dom}(f) = \mathbb{R}
$$

### 1.1 ¿Qué es una Parábola? (El Puente Intuitivo del Balón en el Aire)

Cuando un futbolista patea un tiro libre en el estadio de Cusco, el balón no viaja en línea recta: asciende venciendo la resistencia del aire, pierde velocidad progresivamente hasta alcanzar un punto más alto (la cima del vuelo) y luego desciende simétricamente hasta impactar el césped. 

Esa trayectoria curva en forma de "U" invertida es una **parábola**, la gráfica representativa de toda **función cuadrática**:

$$f(x) = ax^2 + bx + c \quad (a \neq 0)$$

#### La Regla Nemotécnica de la Concavidad (¿Feliz o Triste?)
El signo del coeficiente principal $a$ decide de inmediato hacia dónde abren los brazos de la parábola:
* **Si $a > 0$ (positivo):** La parábola tiene forma de **sonrisa o copa $\smile$** (cóncava hacia arriba). El vértice es el fondo de la copa: la función tiene un **VALOR MÍNIMO**.
* **Si $a < 0$ (negativo):** La parábola tiene forma de **puente o arco $\frown$** (cóncava hacia abajo). El vértice es la cumbre del cerro: la función tiene un **VALOR MÁXIMO**.

---

### 1.2 Formas de Representación de la Función Cuadrática


Una función cuadrática puede expresarse algebraicamente en tres formas equivalentes según el contexto de análisis:

### 1.1 Forma Canónica o Polinomial General

$$
f(x) = ax^2 + bx + c, \quad (a \neq 0)
$$

Permite identificar de manera inmediata la intersección con el eje vertical $Y$, la cual ocurre exactamente en el punto $(0, c)$ ya que $f(0) = c$.

### 1.2 Forma Estándar o Vértice

$$
f(x) = a(x - h)^2 + k
$$

donde el par ordenado $V(h, k)$ representa las coordenadas del **vértice** de la parábola. Esta forma se obtiene aplicando el método de completación de cuadrados sobre la forma polinomial:

$$
f(x) = a\left(x^2 + \frac{b}{a}x\right) + c = a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)
$$

Comparando término a término, se deducen las fórmulas universales para las coordenadas del vértice:

$$
h = -\frac{b}{2a}
$$

$$
k = f(h) = c - \frac{b^2}{4a} = -\frac{\Delta}{4a}
$$

donde $\Delta = b^2 - 4ac$ es el discriminante del polinomio cuadrático.

### 1.3 Forma Factorizada

Si el discriminante $\Delta = b^2 - 4ac \geq 0$, el polinomio cuadrático admite raíces reales $x_1$ y $x_2$ (intersecciones con el eje horizontal $X$). En tal caso, la función se descompone en factores lineales:

$$
f(x) = a(x - x_1)(x - x_2)
$$

Por simetría parabólica, la abscisa del vértice $h$ se sitúa exactamente en el punto medio de ambas raíces:

$$
h = \frac{x_1 + x_2}{2}
$$

---

## 2. Elementos Geométricos y Comportamiento de la Parábola

### 2.1 Concavidad y Orientación de las Ramas

El signo del coeficiente principal $a$ define unívocamente hacia dónde abren las ramas de la parábola:

* **Si $a > 0$:** La parábola es **cóncava hacia arriba** (abre hacia $+Y$). El vértice $V(h, k)$ es el punto más bajo de toda la gráfica; por consiguiente, la función alcanza en $x = h$ su **valor mínimo global**, el cual es $f_{mín} = k$. El rango de la función es:
$$
\operatorname{Ran}(f) = [k, +\infty\rangle
$$
* **Si $a < 0$:** La parábola es **cóncava hacia abajo** (abre hacia $-Y$). El vértice $V(h, k)$ es el punto más alto de la gráfica; por consiguiente, la función alcanza en $x = h$ su **valor máximo global**, el cual es $f_{máx} = k$. El rango de la función es:
$$
\operatorname{Ran}(f) = \langle -\infty, k]
$$

### Representación en el Plano Cartesiano

```{figure} ../../assets/algebra/funcion_cuadratica_optimizacion.svg
---
align: center
alt: Concavidad, vértice y rango de la función cuadrática en el plano cartesiano
---
Comportamiento de la parábola según el signo del coeficiente principal $a$: punto mínimo global ($a > 0$) frente a punto máximo global ($a < 0$).
```

### 2.2 Eje de Simetría

La recta vertical que pasa por el vértice divide a la parábola en dos ramas congruentes e idénticas bajo reflexión:

$$
\text{Eje de simetría: } x = h = -\frac{b}{2a}
$$

Para dos puntos con igual ordenada $f(x_A) = f(x_B)$, sus abscisas equidistan del eje de simetría: $\frac{x_A + x_B}{2} = h$.

### 2.3 Intersecciones con los Ejes Coordenados

1. **Corte con el Eje $Y$ (Ordenada al origen):** Se evalúa $x = 0 \implies y = c$. La parábola siempre corta al eje $Y$ en exactamente un punto: $(0, c)$.
2. **Cortes con el Eje $X$ (Ceros o raíces):** Se hace $f(x) = 0 \implies ax^2 + bx + c = 0$. El número de intersecciones depende del discriminante $\Delta = b^2 - 4ac$:
* Si $\Delta > 0$: Dos cortes en $(x_1, 0)$ y $(x_2, 0)$.
* Si $\Delta = 0$: Un único corte tangencial en el vértice $(h, 0)$.
* Si $\Delta < 0$: No corta al eje $X$ (la parábola flota por encima del eje si $a > 0$ o yace por debajo si $a < 0$).

---

## 3. Optimización con Funciones Cuadráticas

Muchos fenómenos reales alcanzan condiciones óptimas (rendimiento máximo, gasto mínimo, mayor superficie) regidos por polinomios de segundo grado.

### Procedimiento Sistemático de Optimización:

1. **Identificar la función objetivo:** Determinar la cantidad que se desea maximizar o minimizar (Área, Ingreso, Ganancia, Costo, Energía).
2. **Expresar en términos de una sola variable independiente:** Emplear las restricciones dadas (perímetro, presupuesto, relación de demanda) para despejar una variable en función de la otra y sustituir en la función objetivo.
3. **Identificar la concavidad:** Verificar que el coeficiente cuadrático $a$ confirme el tipo de extremo buscado ($a < 0$ para máximo; $a > 0$ para mínimo).
4. **Calcular el valor crítico en el vértice:**
* La variable independiente óptima es $x_{opt} = h = -\frac{b}{2a}$.
* El valor óptimo resultante (máximo o mínimo) es $k = f(h)$.

---

## 4. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Determinación de Vértice, Eje de Simetría y Rango
Dada la función cuadrática $f(x) = 2x^2 - 8x + 11$, determinar las coordenadas de su vértice, la ecuación de su eje de simetría y su rango.

**Paso 1:** Identificamos los coeficientes de la función:
$a = 2$, $b = -8$, $c = 11$.

**Paso 2:** Calculamos la abscisa del vértice $h$:
$h = -\frac{b}{2a} = -\frac{-8}{2(2)} = \frac{8}{4} = 2$

**Paso 3:** Evaluamos la función en $x = 2$ para hallar la ordenada $k$:
$k = f(2) = 2(2)^2 - 8(2) + 11 = 2(4) - 16 + 11 = 8 - 16 + 11 = 3$
Por lo tanto, el vértice es $V(2, 3)$.

**Paso 4:** Determinamos el eje de simetría:
Es la recta vertical $x = h \implies x = 2$.

**Paso 5:** Determinamos el rango:
Dado que $a = 2 > 0$, la parábola abre hacia arriba y el vértice representa el mínimo absoluto:
$\operatorname{Ran}(f) = [k, +\infty\rangle = [3, +\infty\rangle$

**Respuesta:** El vértice es $V(2, 3)$, el eje de simetría es $x = 2$, y el rango es $[3, +\infty\rangle$.

---

### Ejercicio 2: Construcción de la Regla de Correspondencia a partir de Datos
Una parábola tiene su vértice en el punto $V(-1, 5)$ y corta al eje de ordenadas en el punto $(0, 2)$. Hallar la regla de correspondencia de la función en su forma canónica $f(x) = ax^2 + bx + c$.

**Paso 1:** Empleamos la forma vértice $f(x) = a(x - h)^2 + k$:
Con $h = -1$ y $k = 5$:
$f(x) = a(x - (-1))^2 + 5 = a(x + 1)^2 + 5$

**Paso 2:** Determinamos el parámetro $a$ utilizando el punto de corte $(0, 2)$:
$f(0) = 2 \implies a(0 + 1)^2 + 5 = 2$
$a(1) + 5 = 2 \implies a = -3$

**Paso 3:** Desarrollamos la expresión a su forma canónica:
$f(x) = -3(x + 1)^2 + 5 = -3(x^2 + 2x + 1) + 5$
$f(x) = -3x^2 - 6x - 3 + 5$
$f(x) = -3x^2 - 6x + 2$

**Respuesta:** La regla de correspondencia es $f(x) = -3x^2 - 6x + 2$.

---

### Ejercicio 3: Determinación de Intersecciones con los Ejes
Calcular todos los puntos de intersección con los ejes coordenados de la parábola definida por $g(x) = -x^2 + 2x + 8$.

**Paso 1:** Intersección con el eje $Y$:
Evaluamos en $x = 0$:
$g(0) = -(0)^2 + 2(0) + 8 = 8$
Punto de corte con el eje $Y$: $(0, 8)$.

**Paso 2:** Intersecciones con el eje $X$:
Hacemos $g(x) = 0$:
$-x^2 + 2x + 8 = 0 \implies x^2 - 2x - 8 = 0$

**Paso 3:** Factorizamos por aspa simple:
$(x - 4)(x + 2) = 0$
$x_1 = 4 \quad \lor \quad x_2 = -2$
Puntos de corte con el eje $X$: $(4, 0)$ y $(-2, 0)$.

**Respuesta:** Los puntos de intersección son $(0, 8)$ con el eje $Y$, y $(-2, 0)$ y $(4, 0)$ con el eje $X$.

---

### Ejercicio 4: Rango con Dominio Acotado
Sea la función $f(x) = x^2 - 6x + 5$ definida exclusivamente en el intervalo cerrado $[-1, 4]$. Hallar el rango de $f$.

**Paso 1:** Hallamos la abscisa del vértice para verificar si cae dentro del dominio:
$h = -\frac{b}{2a} = -\frac{-6}{2(1)} = 3$
Como $3 \in [-1, 4]$, el vértice forma parte del gráfico analizado.

**Paso 2:** Calculamos el valor de la función en el vértice:
$f(3) = (3)^2 - 6(3) + 5 = 9 - 18 + 5 = -4$
Dado que $a = 1 > 0$, este valor representa el mínimo valor alcanzable en el intervalo.

**Paso 3:** Evaluamos la función en los extremos del dominio $[-1, 4]$:
Para $x = -1$: $f(-1) = (-1)^2 - 6(-1) + 5 = 1 + 6 + 5 = 12$
Para $x = 4$: $f(4) = (4)^2 - 6(4) + 5 = 16 - 24 + 5 = -3$

**Paso 4:** Determinamos el rango comparando los valores obtenidos:
El mínimo es $y_{mín} = -4$ (en $x = 3$).
El máximo es $y_{máx} = 12$ (en $x = -1$).
$\operatorname{Ran}(f) = [-4, 12]$

**Respuesta:** El rango de la función en dicho dominio restringido es $[-4, 12]$.

---

### Ejercicio 5: Optimización Geométrica (Área Máxima de Pastoreo)
Un comunero de Huancayo dispone de $240\text{ m}$ de malla metálica para cercar un corral rectangular de alpacas aprovechando una pared de piedra recta ya existente, por lo que solo necesita cercar los tres lados restantes (dos anchos y un largo). Determinar las dimensiones del corral para que el área encerrada sea máxima, y calcular dicha área.

**Paso 1:** Planteamiento de variables:
Sea $x$ la longitud de cada uno de los dos lados perpendiculares a la pared (ancho).
Sea $y$ la longitud del lado paralelo a la pared (largo).

**Paso 2:** Ecuación de restricción (perímetro de malla):
$2x + y = 240 \implies y = 240 - 2x$
Como las dimensiones son positivas: $x > 0$ y $240 - 2x > 0 \implies 0 < x < 120$.

**Paso 3:** Función objetivo (Área del rectángulo):
$A(x) = x \cdot y = x(240 - 2x) = -2x^2 + 240x$

**Paso 4:** Análisis de optimización cuadrática:
Es una función cuadrática con $a = -2 < 0$, por lo que su vértice corresponde al valor máximo absoluto:
$x_{opt} = h = -\frac{b}{2a} = -\frac{240}{2(-2)} = \frac{240}{4} = 60\text{ m}$

**Paso 5:** Calculamos el largo óptimo y el área máxima:
$y_{opt} = 240 - 2(60) = 240 - 120 = 120\text{ m}$
$A_{máx} = A(60) = 60 \times 120 = 7200\text{ m}^2$

**Respuesta:** Las dimensiones óptimas son $60\text{ m}$ de ancho por $120\text{ m}$ de largo, y el área máxima es de $7200\text{ m}^2$.

---

### Ejercicio 6: Optimización Económica (Maximización de Ingresos en Transporte Comunal)
Una empresa de transporte interprovincial entre Ayacucho y Huanta traslada diariamente a 300 pasajeros cobrando un pasaje de $S/\, 10$. Un estudio de mercado revela que por cada sol de incremento en el precio del pasaje se pierden 15 pasajeros diarios. ¿Cuál debe ser el precio del pasaje para maximizar el ingreso diario y cuál será dicho ingreso?

**Paso 1:** Definición de la variable:
Sea $x$ el número de aumentos de $S/\, 1$ en el precio del pasaje.
Nuevo precio por pasaje: $p(x) = 10 + x$.
Nueva cantidad de pasajeros: $q(x) = 300 - 15x$.

**Paso 2:** Planteamos la función de ingreso diario:
$I(x) = p(x) \cdot q(x) = (10 + x)(300 - 15x)$
$I(x) = 3000 - 150x + 300x - 15x^2 = -15x^2 + 150x + 3000$

**Paso 3:** Hallamos el vértice para maximizar ($a = -15 < 0$):
$x_{opt} = -\frac{b}{2a} = -\frac{150}{2(-15)} = \frac{150}{30} = 5$

**Paso 4:** Determinamos el precio óptimo y el ingreso máximo:
Precio óptimo: $p = 10 + 5 = S/\, 15$.
Cantidad de pasajeros: $q = 300 - 15(5) = 300 - 75 = 225$ pasajeros.
Ingreso máximo: $I_{máx} = 15 \times 225 = S/\, 3375$.

**Respuesta:** El precio del pasaje debe ser de $S/\, 15$ y el ingreso máximo diario es de $S/\, 3375$.

---

### Ejercicio 7: Cinemática y Altura Máxima
Un cohete de sondeo meteorológico lanzado desde la estación de Huancayo describe una trayectoria vertical cuya altura $h$ (en metros) respecto al nivel del suelo en función del tiempo transcurrido $t$ (en segundos) está dada por:
$$
h(t) = -5t^2 + 80t + 25
$$
Calcular: a) El tiempo en el que alcanza la altura máxima, b) La altura máxima alcanzada, c) El tiempo en el que regresa al suelo.

**Paso 1:** Identificamos los parámetros de la función cuadrática:
$a = -5$, $b = 80$, $c = 25$. Como $a = -5 < 0$, la altura máxima se produce en el vértice.

**Paso 2:** Tiempo para la altura máxima:
$t_{vértice} = -\frac{b}{2a} = -\frac{80}{2(-5)} = \frac{80}{10} = 8\text{ segundos}$

**Paso 3:** Altura máxima alcanzada:
$h_{máx} = h(8) = -5(8)^2 + 80(8) + 25 = -5(64) + 640 + 25 = -320 + 640 + 25 = 345\text{ metros}$

**Paso 4:** Tiempo en el que impacta contra el suelo ($h(t) = 0$):
$-5t^2 + 80t + 25 = 0 \implies t^2 - 16t - 5 = 0$
Aplicamos la fórmula general con $a = 1, b = -16, c = -5$:
$t = \frac{16 \pm \sqrt{(-16)^2 - 4(1)(-5)}}{2} = \frac{16 \pm \sqrt{256 + 20}}{2} = \frac{16 \pm \sqrt{276}}{2} = 8 \pm \sqrt{69}$
Tomamos la raíz física positiva ($t > 0$):
$t = 8 + \sqrt{69} \approx 8 + 8.31 = 16.31\text{ s}$

**Respuesta:** La altura máxima es de $345\text{ m}$ a los $8\text{ s}$, y regresa al suelo a los $(8 + \sqrt{69})\text{ s} \approx 16.31\text{ s}$.

---

### Ejercicio 8: Condición de Tangencia y Discriminante Nulo
Hallar los valores de la constante $k$ para que la recta $y = 2x + k$ sea tangente a la parábola $y = x^2 - 4x + 7$.

**Paso 1:** Condición geométrica de tangencia:
La recta y la parábola deben intersecarse en exactamente un único punto. Igualamos ambas ecuaciones:
$x^2 - 4x + 7 = 2x + k$

**Paso 2:** Reducimos a la forma canónica de una ecuación cuadrática:
$x^2 - 6x + (7 - k) = 0$

**Paso 3:** Para que exista un único punto de intersección (solución doble), el discriminante debe ser idénticamente cero:
$\Delta = b^2 - 4ac = 0$
$(-6)^2 - 4(1)(7 - k) = 0$
$36 - 28 + 4k = 0 \implies 8 + 4k = 0 \implies 4k = -8 \implies k = -2$

**Respuesta:** El valor requerido es $k = -2$.

---

### Ejercicio 9: Reconstrucción de Parábola por Tres Puntos
Determinar la función cuadrática $f(x) = ax^2 + bx + c$ cuya gráfica pasa por los puntos $A(1, 4)$, $B(-1, 10)$ y $C(2, 7)$.

**Paso 1:** Planteamos el sistema lineal de tres ecuaciones evaluando cada punto:
1) $f(1) = a(1)^2 + b(1) + c = 4 \implies a + b + c = 4$
2) $f(-1) = a(-1)^2 + b(-1) + c = 10 \implies a - b + c = 10$
3) $f(2) = a(2)^2 + b(2) + c = 7 \implies 4a + 2b + c = 7$

**Paso 2:** Restamos la ecuación (2) de la ecuación (1):
$(a + b + c) - (a - b + c) = 4 - 10 \implies 2b = -6 \implies b = -3$

**Paso 3:** Sustituimos $b = -3$ en las ecuaciones (1) y (3):
De (1): $a - 3 + c = 4 \implies a + c = 7 \implies c = 7 - a$
De (3): $4a + 2(-3) + c = 7 \implies 4a - 6 + c = 7 \implies 4a + c = 13$

**Paso 4:** Restamos las ecuaciones resultantes:
$(4a + c) - (a + c) = 13 - 7 \implies 3a = 6 \implies a = 2$
Luego: $c = 7 - 2 = 5$.

**Respuesta:** La función cuadrática es $f(x) = 2x^2 - 3x + 5$.

---

### Ejercicio 10: Intersección de Dos Parábolas y Área Común
Dadas las parábolas $f(x) = x^2 - 2x + 1$ y $g(x) = -x^2 + 4x + 9$, determinar los puntos de intersección entre ambas curvas y la distancia euclidiana entre dichos puntos.

**Paso 1:** Igualamos las reglas de correspondencia $f(x) = g(x)$:
$x^2 - 2x + 1 = -x^2 + 4x + 9$

**Paso 2:** Transponemos términos a la forma canónica:
$2x^2 - 6x - 8 = 0$
Dividiendo entre 2:
$x^2 - 3x - 4 = 0$

**Paso 3:** Factorizamos por aspa simple:
$(x - 4)(x + 1) = 0 \implies x_1 = 4 \quad \lor \quad x_2 = -1$

**Paso 4:** Calculamos las ordenadas correspondientes usando $f(x) = (x - 1)^2$:
Para $x_1 = 4$: $y_1 = (4 - 1)^2 = 3^2 = 9 \implies P_1(4, 9)$
Para $x_2 = -1$: $y_2 = (-1 - 1)^2 = (-2)^2 = 4 \implies P_2(-1, 4)$

**Paso 5:** Calculamos la distancia entre $P_1(4, 9)$ y $P_2(-1, 4)$:
$d = \sqrt{(4 - (-1))^2 + (9 - 4)^2} = \sqrt{5^2 + 5^2} = \sqrt{25 + 25} = \sqrt{50} = 5\sqrt{2}$

**Respuesta:** Los puntos de intersección son $(-1, 4)$ y $(4, 9)$, y la distancia entre ellos es $5\sqrt{2}$.

---

## 5. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. Determinar el vértice de la parábola $f(x) = x^2 - 6x + 13$:  
A) $(3, 4)$  
B) $(-3, 4)$  
C) $(3, -4)$  
D) $(6, 13)$  
E) $(0, 13)$  

2. ¿Cuál es el rango de la función cuadrática $f(x) = x^2 + 4$?  
A) $\mathbb{R}$  
B) $[4, +\infty\rangle$  
C) $\langle -\infty, 4]$  
D) $[0, +\infty\rangle$  
E) $[-4, 4]$  

3. Dada la función $g(x) = -2x^2 + 12x - 10$, su valor máximo es:  
A) $3$  
B) $8$  
C) $10$  
D) $-10$  
E) $18$  

4. Hallar el eje de simetría de la función $f(x) = 3x^2 + 18x - 5$:  
A) $x = 3$  
B) $x = -3$  
C) $x = -6$  
D) $x = 6$  
E) $y = -3$  

5. El punto de corte de la gráfica de $f(x) = 5x^2 - 7x - 12$ con el eje de ordenadas $Y$ es:  
A) $(0, 5)$  
B) $(0, -7)$  
C) $(0, -12)$  
D) $(-12, 0)$  
E) $(0, 0)$  

6. Si la gráfica de $f(x) = a(x - 2)^2 + 3$ pasa por el origen de coordenadas $(0, 0)$, ¿cuál es el valor de $a$?  
A) $3/4$  
B) $-3/4$  
C) $4/3$  
D) $-4/3$  
E) $-3$  

7. Determinar las intersecciones con el eje $X$ de la parábola $y = x^2 - 5x + 6$:  
A) $(2, 0)$ y $(3, 0)$  
B) $(-2, 0)$ y $(-3, 0)$  
C) $(1, 0)$ y $(6, 0)$  
D) $(0, 2)$ y $(0, 3)$  
E) $(5, 0)$ y $(6, 0)$  

8. ¿Hacia dónde abren las ramas de la función $f(x) = 8 - 3x - 4x^2$ y cuál es su tipo de extremo?  
A) Hacia arriba; punto mínimo  
B) Hacia abajo; punto mínimo  
C) Hacia abajo; punto máximo  
D) Hacia arriba; punto máximo  
E) Horizontal; no tiene extremo  

9. Si el vértice de una parábola es $V(4, -1)$ y abre hacia arriba con $a = 1$, ¿cuál es su ecuación en forma general?  
A) $y = x^2 - 8x + 15$  
B) $y = x^2 - 8x + 17$  
C) $y = x^2 + 8x + 15$  
D) $y = x^2 - 4x - 1$  
E) $y = x^2 + 4x - 1$  

10. Calcular el valor mínimo de la función $f(x) = 2x^2 - 4x + 9$:  
A) $1$  
B) $7$  
C) $9$  
D) $5$  
E) $3$  

11. ¿En qué intervalo es estrictamente creciente la función $f(x) = x^2 - 10x + 21$?  
A) $\langle -\infty, 5]$  
B) $[5, +\infty\rangle$  
C) $[3, 7]$  
D) $\langle -\infty, 10]$  
E) $[0, +\infty\rangle$  

12. Si una parábola interseca al eje $X$ en $x_1 = -2$ y $x_2 = 8$, ¿cuál es la ecuación de su eje de simetría?  
A) $x = 3$  
B) $x = 5$  
C) $x = 6$  
D) $x = -5$  
E) $x = 4$  

13. Hallar el discriminante de la función $f(x) = 2x^2 - 3x + 5$ e indicar cuántas veces corta al eje $X$:  
A) $\Delta = 49$; dos cortes  
B) $\Delta = 0$; un corte  
C) $\Delta = -31$; ningún corte  
D) $\Delta = 31$; dos cortes  
E) $\Delta = -49$; ningún corte  

14. Si $f(x) = x^2 + bx + 9$ tiene su vértice sobre el eje $X$, ¿qué valores puede tomar $b$?  
A) Solo $6$  
B) Solo $-6$  
C) $\pm 6$  
D) $\pm 9$  
E) $0$  

15. El vértice de la función $f(x) = -(x + 5)^2 - 2$ es:  
A) $(5, -2)$  
B) $(-5, -2)$  
C) $(-5, 2)$  
D) $(5, 2)$  
E) $(0, -27)$  

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Si el rango de la función $f(x) = 2x^2 - 12x + c$ es $[5, +\infty\rangle$, calcular el valor de la constante $c$:  
A) $18$  
B) $23$  
C) $13$  
D) $25$  
E) $15$  

17. Hallar el rango de $f(x) = -x^2 + 4x + 1$ para $x \in [0, 5]$:  
A) $[-4, 5]$  
B) $[1, 5]$  
C) $[-4, 1]$  
D) $[0, 5]$  
E) $[-5, 5]$  

18. Un campesino en Cusco cuenta con $160\text{ m}$ de cerca de alambre para delimitar un terreno rectangular. ¿Cuál es la mayor área en metros cuadrados que puede cercar?  
A) $1200\text{ m}^2$  
B) $1600\text{ m}^2$  
C) $1800\text{ m}^2$  
D) $2000\text{ m}^2$  
E) $6400\text{ m}^2$  

19. La utilidad mensual en soles de una cooperativa de café en Pichanaqui depende de las toneladas $x$ producidas según: $U(x) = -5x^2 + 140x - 480$. ¿Cuántas toneladas deben producirse para maximizar la utilidad y a cuánto asciende dicha ganancia máxima?  
A) $14\text{ tn}; S/\, 500$  
B) $14\text{ tn}; S/\, 520$  
C) $12\text{ tn}; S/\, 480$  
D) $15\text{ tn}; S/\, 515$  
E) $10\text{ tn}; S/\, 420$  

20. La trayectoria de un balón de fútbol pateado por un estudiante está dada por $y = -\frac{1}{20}x^2 + 2x$, donde $x$ e $y$ están en metros. ¿Cuál es el alcance horizontal total del balón hasta que vuelve a tocar el suelo?  
A) $20\text{ m}$  
B) $30\text{ m}$  
C) $40\text{ m}$  
D) $50\text{ m}$  
E) $80\text{ m}$  

21. Si la parábola $y = ax^2 + bx + c$ pasa por los puntos $(0, 3)$, $(1, 2)$ y $(2, 3)$, hallar el valor de $a + b + c$:  
A) $2$  
B) $3$  
C) $4$  
D) $1$  
E) $5$  

22. Determinar el valor de $m$ para que la recta $y = 4x + m$ sea tangente a la parábola $y = x^2 + 2x + 6$:  
A) $5$  
B) $6$  
C) $4$  
D) $7$  
E) $3$  

23. Sea la función cuadrática $f(x) = x^2 - 2(k - 1)x + 2k + 1$. Hallar el menor valor entero de $k$ para que la parábola corte al eje $X$ en dos puntos distintos:  
A) $4$  
B) $5$  
C) $0$  
D) $-1$  
E) $6$  

24. Un puesto del mercado modelo de Huamanga vende cuyes a $S/\, 30$ la unidad, logrando vender 80 unidades a la semana. Por cada sol de descuento en el precio, logra vender 5 cuyes adicionales. ¿A qué precio debe vender cada cuy para maximizar el ingreso semanal?  
A) $S/\, 21$  
B) $S/\, 23$  
C) $S/\, 25$  
D) $S/\, 22$  
E) $S/\, 24$  

25. Si los puntos $P(2, 7)$ y $Q(8, 7)$ pertenecen a la gráfica de una función cuadrática $f$, ¿cuál es la abscisa de su vértice?  
A) $4$  
B) $5$  
C) $6$  
D) $4.5$  
E) $5.5$  

26. La función de costo total de producción de pantalones en un taller de Gamarra es $C(x) = 2x^2 - 80x + 1500$, donde $x$ es el número de docenas. ¿Cuántas docenas minimizan el costo y cuál es el costo mínimo?  
A) $20\text{ docenas}; S/\, 700$  
B) $20\text{ docenas}; S/\, 800$  
C) $25\text{ docenas}; S/\, 750$  
D) $15\text{ docenas}; S/\, 900$  
E) $40\text{ docenas}; S/\, 700$  

27. Hallar la ecuación cuadrática cuya gráfica tiene su vértice en $(3, -2)$ y su ordenada al origen es $(0, 16)$:  
A) $y = 2x^2 - 12x + 16$  
B) $y = 2x^2 - 6x + 16$  
C) $y = x^2 - 6x + 16$  
D) $y = 2x^2 + 12x + 16$  
E) $y = 3x^2 - 18x + 16$  

28. ¿Cuál es la distancia euclidiana entre los puntos de intersección de la parábola $y = x^2 - 4x$ con la recta $y = 2x - 5$?  
A) $2\sqrt{5}$  
B) $4\sqrt{5}$  
C) $3\sqrt{5}$  
D) $5\sqrt{2}$  
E) $\sqrt{5}$  

29. Sea $f(x) = -2x^2 + 8x - 3$. Determinar el conjunto de valores de $x$ para los cuales la función es estrictamente positiva ($f(x) > 0$):  
A) $\left\langle 2 - \frac{\sqrt{10}}{2}, 2 + \frac{\sqrt{10}}{2} \right\rangle$  
B) $\left\langle 2 - \sqrt{5}, 2 + \sqrt{5} \right\rangle$  
C) $\langle 1, 3 \rangle$  
D) $\left\langle -\frac{\sqrt{10}}{2}, \frac{\sqrt{10}}{2} \right\rangle$  
E) $\mathbb{R}$  

30. Se divide un alambre de $60\text{ cm}$ en dos pedazos para formar dos cuadrados. ¿Cuál debe ser la longitud del lado del primer cuadrado para que la suma de las áreas de ambos cuadrados sea mínima?  
A) $7.5\text{ cm}$  
B) $10\text{ cm}$  
C) $15\text{ cm}$  
D) $5\text{ cm}$  
E) $12.5\text{ cm}$  

31. Hallar los puntos comunes a las curvas $y = x^2 - 3x + 2$ e $y = -x^2 + 5x - 4$:  
A) $(1, 0)$ y $(3, 2)$  
B) $(1, 0)$ y $(3, -2)$  
C) $(2, 0)$ y $(4, 6)$  
D) $(-1, 6)$ y $(3, 2)$  
E) $(0, 2)$ y $(3, 2)$  

32. Si el vértice de la parábola $y = ax^2 + 4x + c$ se ubica en el segundo cuadrante, ¿cuáles deben ser los signos de $a$ y $c$?  
A) $a > 0, c > 0$  
B) $a < 0, c > 0$  
C) $a > 0, c < 0$  
D) $a < 0, c < 0$  
E) $a > 0$, cualquier $c$  

33. Determinar el área del triángulo cuyos vértices son los dos puntos de corte con el eje $X$ y el vértice de la parábola $y = -x^2 + 4x$:  
A) $4\text{ u}^2$  
B) $8\text{ u}^2$  
C) $16\text{ u}^2$  
D) $12\text{ u}^2$  
E) $6\text{ u}^2$  

34. Una ventana normanda consta de un rectángulo coronado por un semicírculo. Si el perímetro total es de $10\text{ m}$, ¿cuál debe ser el radio del semicírculo para permitir el ingreso máximo de luz (área máxima)?  
A) $\frac{10}{\pi + 4}\text{ m}$  
B) $\frac{10}{2\pi + 4}\text{ m}$  
C) $\frac{5}{\pi + 2}\text{ m}$  
D) $\frac{20}{\pi + 4}\text{ m}$  
E) $\frac{10}{\pi + 2}\text{ m}$  

35. Si la función $f(x) = mx^2 + (m - 3)x + m$ tiene como rango $\langle -\infty, 1]$, calcular el valor de la constante $m$:  
A) $-1$  
B) $-3$  
C) $1$  
D) $-1/3$  
E) $-2$  

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Determinar el valor mínimo que toma la expresión $E(x, y) = x^2 + 2y^2 - 4x + 4y + 15$ para cualesquiera números reales $x, y$:  
A) $7$  
B) $9$  
C) $11$  
D) $5$  
E) $13$  

37. Sea $f(x) = ax^2 + bx + c$. Si $f(x) \geq 0$ para todo $x \in \mathbb{R}$, y se sabe que $f(2) = 0$ y $f(3) = 2$, calcular el valor de $f(5)$:  
A) $14$  
B) $16$  
C) $18$  
D) $20$  
E) $12$  

38. La parábola $P_1: y = x^2 - 2x + 3$ se traslada vectorialmente de modo que su nuevo vértice coincide con el punto de corte con el eje $Y$ de la parábola $P_2: y = -2x^2 + 8x - 5$. Hallar la ecuación de la parábola trasladada:  
A) $y = x^2 - 5$  
B) $y = (x - 2)^2 - 5$  
C) $y = x^2 + 5$  
D) $y = (x + 2)^2 - 5$  
E) $y = 2x^2 - 5$  

39. Si el conjunto solución de la inecuación cuadrática $f(x) \leq 0$ es el intervalo unitario $\{3\}$, y además $f(0) = 18$, calcular el valor de $f(-1)$:  
A) $30$  
B) $32$  
C) $36$  
D) $28$  
E) $24$  

40. Hallar el valor del parámetro $k$ para que el vértice de la parábola $y = x^2 - 2kx + k^2 + 2k - 8$ pertenezca a la recta $y = 3x - 14$:  
A) $4$  
B) $6$  
C) $5$  
D) $3$  
E) $7$  

41. **(Reto)** Un túnel ferroviario en la sierra central tiene sección parabólica de $6\text{ m}$ de altura en su punto medio y $8\text{ m}$ de ancho en la base del suelo. Se desea instalar una tubería transversal horizontal de soporte a una altura de $4\text{ m}$ sobre el suelo. ¿Cuál es la longitud exacta que debe tener dicha tubería transversal?  
A) $\frac{8\sqrt{3}}{3}\text{ m}$  
B) $4\sqrt{2}\text{ m}$  
C) $5\text{ m}$  
D) $\frac{8\sqrt{6}}{3}\text{ m}$  
E) $6\text{ m}$  

42. **(Reto)** Sea la familia de parábolas $y = x^2 - 2tx + t^2 + 3t$. Determinar la ecuación de la curva que describe el lugar geométrico de todos sus vértices al variar el parámetro real $t$:  
A) $y = 3x$  
B) $y = 3x^2$  
C) $y = x^2 + 3x$  
D) $y = -3x$  
E) $y = 2x + 3$  

43. **(Reto)** Se inscribe un rectángulo dentro de un triángulo isósceles cuya base mide $12\text{ cm}$ y cuya altura relativa a dicha base mide $10\text{ cm}$, con uno de los lados del rectángulo descansando sobre la base del triángulo. ¿Cuál es el área máxima que puede tener dicho rectángulo inscrito?  
A) $25\text{ cm}^2$  
B) $30\text{ cm}^2$  
C) $35\text{ cm}^2$  
D) $40\text{ cm}^2$  
E) $20\text{ cm}^2$  

44. **(Reto)** Hallar la distancia mínima que existe entre la recta $L: y = 2x - 8$ y la parábola $P: y = x^2$:  
A) $\frac{7\sqrt{5}}{5}$  
B) $\frac{7}{5}$  
C) $\frac{9\sqrt{5}}{5}$  
D) $\sqrt{5}$  
E) $\frac{8\sqrt{5}}{5}$  

45. **(Reto)** Un estudiante del COAR analiza la función cuadrática $f(x) = ax^2 + bx + c$ ($a \neq 0$) y nota que $f(x + 1) - f(x) = 8x + 3$ para todo $x \in \mathbb{R}$, y además $f(0) = 5$. Determinar el valor mínimo absoluto que alcanza $f(x)$ en todo su dominio:  
A) $33/8$  
B) $31/8$  
C) $35/8$  
D) $29/8$  
E) $4$  

---

## 6. Claves de Respuestas y Pistas Estratégicas

### Claves de Respuestas

| N° | Clave | N° | Clave | N° | Clave | N° | Clave | N° | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | A | **10** | B | **19** | B | **28** | B | **37** | C |
| **2** | B | **11** | B | **20** | C | **29** | A | **38** | A |
| **3** | B | **12** | A | **21** | A | **30** | A | **39** | B |
| **4** | B | **13** | C | **22** | A | **31** | A | **40** | B |
| **5** | C | **14** | C | **23** | B | **32** | A | **41** | A |
| **6** | B | **15** | B | **24** | B | **33** | B | **42** | A |
| **7** | A | **16** | B | **25** | B | **34** | A | **43** | B |
| **8** | C | **17** | A | **26** | A | **35** | A | **44** | A |
| **9** | A | **18** | B | **27** | A | **36** | B | **45** | B |

---

### Pistas Estratégicas para Ejercicios Reto (41 al 45)

* **Pista 41:** Ubica el origen de coordenadas $(0, 0)$ en el centro de la base del túnel. El vértice de la parábola estará en $(0, 6)$ y los extremos de la base en $(-4, 0)$ y $(4, 0)$. La ecuación simétrica es $y = -a x^2 + 6$. Determina $a$ con el punto $(4, 0) \implies 0 = -a(16) + 6 \implies a = 3/8$. Luego iguala la altura $y = 4$ y despeja la anchura total $2x$.
* **Pista 42:** Determina las coordenadas del vértice en función del parámetro $t$: $h(t) = -\frac{b}{2a} = t$ y $k(t) = f(t) = t^2 - 2t^2 + t^2 + 3t = 3t$. Al eliminar el parámetro igualando $x = t$, se sustituye directamente en la ordenada $y = 3t \implies y = 3x$.
* **Pista 43:** Establece el sistema con el vértice superior del triángulo en $(0, 10)$ y la base sobre el eje $X$ desde $x = -6$ hasta $x = 6$. La ecuación de la recta del lado derecho es $y - 0 = -\frac{10}{6}(x - 6) \implies y = 10 - \frac{5}{3}x$. El área del rectángulo de ancho $2x$ y altura $y$ es $A(x) = 2x\left(10 - \frac{5}{3}x\right) = 20x - \frac{10}{3}x^2$. Halla el vértice de esta parábola.
* **Pista 44:** El punto de la parábola más cercano a la recta tangente con pendiente $m = 2$ ocurre donde la recta paralela es tangente a $y = x^2$. Plantea la recta tangente $y = 2x + k$, iguala con $x^2 \implies x^2 - 2x - k = 0$ y haz $\Delta = 0 \implies k = -1$. El punto de contacto es $(1, 1)$. Aplica la fórmula de distancia de un punto a una recta: $d = \frac{|2(1) - (1) - 8|}{\sqrt{2^2 + (-1)^2}} = \frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{5}$.
* **Pista 45:** Desarrolla $f(x + 1) - f(x) = a(x + 1)^2 + b(x + 1) + c - (ax^2 + bx + c) = 2ax + a + b$. Compara coeficientes con $8x + 3$: $2a = 8 \implies a = 4$ y $a + b = 3 \implies 4 + b = 3 \implies b = -1$. Como $f(0) = c = 5$, la función es $f(x) = 4x^2 - x + 5$. Su valor mínimo es $k = f\left(\frac{1}{8}\right) = 4\left(\frac{1}{64}\right) - \frac{1}{8} + 5 = \frac{1}{16} - \frac{2}{16} + 5 = 5 - \frac{1}{16} = \frac{79}{16} \implies$ verifica cuidadosamente la fracción.

---

## 7. Formulario Resumen

| Concepto / Propiedad | Expresión Matemática | Notas y Condiciones |
| :--- | :--- | :--- |
| **Forma Canónica** | $f(x) = ax^2 + bx + c$ | $a \neq 0$; corte con eje $Y$ en $(0, c)$ |
| **Forma Vértice** | $f(x) = a(x - h)^2 + k$ | Vértice en $V(h, k)$ |
| **Abscisa del Vértice ($h$)** | $h = -\frac{b}{2a}$ | Eje de simetría vertical: recta $x = h$ |
| **Ordenada del Vértice ($k$)** | $k = f(h) = c - \frac{b^2}{4a} = -\frac{\Delta}{4a}$ | Extremo absoluto de la función |
| **Concavidad Superior ($a > 0$)** | Parábola abre hacia $+Y$ | Vértice es mínimo global; $\operatorname{Ran}(f) = [k, +\infty\rangle$ |
| **Concavidad Inferior ($a < 0$)** | Parábola abre hacia $-Y$ | Vértice es máximo global; $\operatorname{Ran}(f) = \langle -\infty, k]$ |
| **Forma Factorizada** | $f(x) = a(x - x_1)(x - x_2)$ | Requiere $\Delta \geq 0$; raíces $x_1, x_2$ en eje $X$ |
| **Eje de Simetría** | $x = \frac{x_1 + x_2}{2} = h$ | Equidistancia para puntos con igual ordenada |
| **Discriminante $\Delta > 0$** | $\Delta = b^2 - 4ac > 0$ | Dos puntos de corte distintos con el eje $X$ |
| **Discriminante $\Delta = 0$** | $\Delta = b^2 - 4ac = 0$ | Parábola tangente al eje $X$ en su vértice $(h, 0)$ |
| **Discriminante $\Delta < 0$** | $\Delta = b^2 - 4ac < 0$ | No corta al eje $X$ (curva totalmente externa) |
| **Optimización de Área** | $A(x) = x(P/2 - x)$ | Rectángulo de área máxima es el cuadrado ($x = P/4$) |
| **Ingreso Cuadrático** | $I(x) = p(x) \cdot q(x)$ | Relación lineal precio-demanda produce parábola cóncava |
| **Utilidad Neta** | $U(x) = I(x) - C(x)$ | Vértice en $x = -\frac{b_U}{2a_U}$ maximiza ganancias |
