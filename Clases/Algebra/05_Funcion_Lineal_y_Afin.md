# Tema 05: Función Lineal y Función Afín

## 1. Introducción y Contexto Real

El estudio funcional de las matemáticas representa la transición de resolver igualdades estáticas a comprender y modelar **leyes de cambio y dependencia dinámica**. En la física mecánica, la ingeniería económica, la biología poblacional y las políticas tarifarias de servicios públicos en el Perú, el modelo de variación más simple, robusto y ubicuo es la relación de primer grado entre dos magnitudes continuas.

Cuando una empresa prestadora de servicios de saneamiento (como SEDAPAL en Lima o EPS Grau en Piura) factura el consumo de agua mediante un cargo fijo de mantenimiento más un costo proporcional por cada metro cúbico consumido; cuando un taxi por aplicativo calcula el precio de una carrera sumando una tarifa base de arranque a una tasa por kilómetro recorrido; o cuando un ingeniero evalúa la **depreciación lineal** de una maquinaria pesada a lo largo de su vida útil, la estructura matemática subyacente es una **función afín**.

Para el estudiante y postulante a **Beca 18**, dominar la función lineal y afín implica no solo graficar rectas en el plano cartesiano, sino interpretar rigurosamente la **pendiente ($m$)** como una razón de cambio unitaria o velocidad de variación marginal, conectando el álgebra elemental con el cálculo diferencial aplicado.

---

## 2. Marco Teórico Riguroso

### 2.1 Definición General de Función Real de Variable Real

Una función real de variable real es una correspondencia binaria $f: D_f \subseteq \mathbb{R} \to \mathbb{R}$ tal que a cada elemento $x$ del dominio ($D_f$) le corresponde un **único** elemento $y = f(x)$ en el codominio o rango ($R_f$):

$$
(x, y_1) \in f \ \land \ (x, y_2) \in f \implies y_1 = y_2
$$

Geométricamente, una gráfica en el plano cartesiano representa una función si y solo si cualquier recta vertical trazada en el dominio corta a la curva en **a lo sumo un punto** (Criterio de la Recta Vertical).

---

### 2.2 Función Lineal (Proporcionalidad Directa)

Una función $f: \mathbb{R} \to \mathbb{R}$ es estrictamente **lineal** si su regla de correspondencia adopta la forma canónica:

$$
f(x) = m \cdot x \quad (m \in \mathbb{R}, \ m \neq 0)
$$

donde:
* $m$ es la constante de proporcionalidad o **pendiente**.
* Su gráfica es una línea recta que pasa necesariamente por el **origen de coordenadas** $(0, 0)$, puesto que $f(0) = m \cdot 0 = 0$.
* Propiedad aditiva y homogénea: $f(x_1 + x_2) = f(x_1) + f(x_2)$ y $f(k \cdot x) = k \cdot f(x)$.
* Dominio y Rango: $D_f = \mathbb{R}$ y $R_f = \mathbb{R}$.

---

### 2.3 Función Afín (Modelo con Término Independiente)

Una función $g: \mathbb{R} \to \mathbb{R}$ es **afín** si su regla de correspondencia es de primer grado con término independiente no nulo:

$$
g(x) = m \cdot x + b \quad (m, b \in \mathbb{R}, \ m \neq 0, \ b \neq 0)
$$

donde:
* $m$ es la **pendiente** de la recta ($m = \tan \theta$, donde $\theta$ es el ángulo de inclinación respecto al eje positivo de las abscisas).
* $b$ es la **ordenada en el origen**, es decir, el valor donde la recta intersecta al eje vertical $Y$ en el punto $(0, b)$.
* Intersección con el eje horizontal $X$ (raíz o cero de la función): se obtiene resolviendo $g(x) = 0 \implies x = -\frac{b}{m}$, dando el punto $\left(-\frac{b}{m}, 0\right)$.
* Si $m = 0$, la función se transforma en la **función constante** $g(x) = b$, cuya gráfica es una recta horizontal de pendiente nula.

---

### 2.4 Representación en el Plano Cartesiano

```{figure} ../../assets/algebra/funcion_lineal_afin.svg
---
align: center
alt: Comparación gráfica entre Función Lineal y Función Afín en el plano cartesiano
---
Representación geométrica en el plano cartesiano: (Izquierda) La función lineal $f(x) = 1{,}5x$ pasa obligatoriamente por el origen $(0,0)$, mientras que la función afín $g(x) = 1{,}5x + 2$ está desplazada verticalmente cortando al eje $Y$ en $(0, b) = (0, 2)$. (Derecha) La pendiente $m$ define la monotonía de la recta: si $m > 0$ la función es estrictamente creciente; si $m < 0$ la función es estrictamente decreciente.
```

---

### 2.5 La Pendiente como Razón de Cambio Marginal

Dados dos puntos distintos cualesquiera $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ pertenecientes a la recta (con $x_1 \neq x_2$), la pendiente $m$ se calcula como el cociente de incrementos:

$$
m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} = \tan \theta
$$

#### Interpretación de la Monotonía según el Signo de $m$

* **Si $m > 0$ (Pendiente Positiva):** El ángulo de inclinación es agudo ($0^\circ < \theta < 90^\circ$). La función es **estrictamente creciente**: al aumentar $x$, $y$ también aumenta.
* **Si $m < 0$ (Pendiente Negativa):** El ángulo de inclinación es obtuso ($90^\circ < \theta < 180^\circ$). La función es **estrictamente decreciente**: al aumentar $x$, $y$ disminuye.
* **Si $m = 0$ (Pendiente Nula):** Recta horizontal paralela al eje $X$. La función es constante.

---

### 2.6 Formas de la Ecuación de la Recta

1. **Forma Punto - Pendiente:** Si se conoce un punto de paso $P_0(x_0, y_0)$ y la pendiente $m$:

$$
y - y_0 = m(x - x_0)
$$

2. **Forma Cartesiana (Dos Puntos):** Si se conocen $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:

$$
y - y_1 = \left(\frac{y_2 - y_1}{x_2 - x_1}\right)(x - x_1)
$$

3. **Forma Simétrica o Canónica:** Si corta a los ejes en $(a, 0)$ y $(0, b)$ con $a, b \neq 0$:

$$
\frac{x}{a} + \frac{y}{b} = 1
$$

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Pendiente, Evaluación y Cortes)

#### Ejercicio 1: Cálculo de Pendiente y Regla de Correspondencia
Una recta en el plano cartesiano pasa por los puntos $A(2, 5)$ y $B(6, 17)$.
Determine la pendiente de la recta, su regla de correspondencia funcional y el punto exacto de corte con el eje de las abscisas ($X$).

**Solución paso a paso:**

**Paso 1:** Calcular la pendiente $m$ usando la fórmula del cociente de diferencias:

$$
m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3
$$

La pendiente es $m = 3$ (positiva, función creciente).

**Paso 2:** Determinar la ecuación de la función afín $f(x) = mx + b$:
Usamos el punto de paso $A(2, 5)$ donde $x = 2$ e $y = 5$:

$$
5 = 3(2) + b \implies 5 = 6 + b \implies b = 5 - 6 = -1
$$

La regla de correspondencia es:

$$
f(x) = 3x - 1
$$

**Paso 3:** Hallar el punto de corte con el eje $X$ (haciendo $f(x) = 0$):

$$
3x - 1 = 0 \implies 3x = 1 \implies x = \frac{1}{3}
$$

El punto de corte con el eje $X$ es $\left( \frac{1}{3}, 0 \right)$.

*Respuesta:* La pendiente es $m = 3$, la función es $f(x) = 3x - 1$ y corta al eje $X$ en $\left( \frac{1}{3}, 0 \right)$.

---

#### Ejercicio 2: Evaluación Funcional y Composición Simple
Dada la función afín $g(x) = -2x + 7$, determine el valor de:

$$
E = \frac{g(5) - g(-2)}{g(1)}
$$

**Solución paso a paso:**

**Paso 1:** Evaluar $g(x)$ en cada valor requerido:
Para $x = 5$:

$$
g(5) = -2(5) + 7 = -10 + 7 = -3
$$

Para $x = -2$:

$$
g(-2) = -2(-2) + 7 = 4 + 7 = 11
$$

Para $x = 1$:

$$
g(1) = -2(1) + 7 = -2 + 7 = 5
$$

**Paso 2:** Reemplazar los valores calculados en la expresión $E$:

$$
E = \frac{-3 - 11}{5} = \frac{-14}{5} = -2{,}8
$$

*Respuesta:* El valor de la expresión es $E = -\frac{14}{5} = -2{,}8$.

---

#### Ejercicio 3: Identificación entre Función Lineal y Función Afín
Dadas las siguientes tres relaciones algebraicas:
1) $f_1(x) = 4x$
2) $f_2(x) = 4x - 9$
3) $f_3(x) = 5$
Determine cuál de ellas representa una función estrictamente lineal, cuál una función afín y cuál una función constante, indicando para cada una su pendiente y su ordenada en el origen.

**Solución paso a paso:**

**Paso 1:** Analizar $f_1(x) = 4x$:
Adopta la forma $f(x) = mx$ con $m = 4$ y término independiente $b = 0$.
Pasa por $(0,0)$. Por definición, es una **función lineal**. Su pendiente es $m = 4$ y su ordenada en el origen es $b = 0$.

**Paso 2:** Analizar $f_2(x) = 4x - 9$:
Adopta la forma $g(x) = mx + b$ con $m = 4$ y $b = -9 \neq 0$.
No pasa por $(0,0)$; corta al eje $Y$ en $(0, -9)$. Es una **función afín**. Su pendiente es $m = 4$ y su ordenada en el origen es $b = -9$.

**Paso 3:** Analizar $f_3(x) = 5$:
Tiene pendiente $m = 0$ y $b = 5$. Es una recta horizontal sin inclinación, correspondiente a la **función constante**.

*Respuesta:* $f_1$ es función lineal ($m = 4, b = 0$), $f_2$ es función afín ($m = 4, b = -9$) y $f_3$ es función constante ($m = 0, b = 5$).

---

### Bloque B: Nivel Intermedio (Modelamiento Aplicado y Dominio Acotado)

#### Ejercicio 4: Tarifa de Servicio de Agua Potable y Modelamiento Afín
La empresa prestadora de servicios de agua de una provincia andina aplica un modelo tarifario residencial afín: una tarifa fija de conexión y alcantarillado de $\text{S/ } 14{,}50$ mensuales, más un cargo variable de $\text{S/ } 2{,}80$ por cada metro cúbico ($\text{m}^3$) de agua consumido.
a) Formule la función del costo mensual $C(x)$ en función del volumen consumido $x$.
b) Si una familia beneficiaria de Beca 18 consumió $26\text{ m}^3$ en el mes, ¿cuánto pagó en total?
c) Si en el mes siguiente la factura fue de $\text{S/ } 104{,}10$, ¿cuántos metros cúbicos consumieron?

**Solución paso a paso:**

**Paso 1:** Formular la regla de correspondencia:
Cargo fijo (ordenada en el origen): $b = 14{,}50$.
Costo por unidad de consumo (pendiente): $m = 2{,}80$.
Función afín de costo:

$$
C(x) = 2{,}80x + 14{,}50 \quad (x \ge 0)
$$

**Paso 2:** Calcular el costo para un consumo de $x = 26\text{ m}^3$:

$$
C(26) = 2{,}80(26) + 14{,}50
$$

Efectuamos el producto: $2{,}80 \times 26 = 72{,}80$.

$$
C(26) = 72{,}80 + 14{,}50 = \text{S/ } 87{,}30
$$

**Paso 3:** Determinar el volumen consumido cuando la factura es $C(x) = 104{,}10$:

$$
2{,}80x + 14{,}50 = 104{,}10
$$

Restamos $14{,}50$ a ambos miembros:

$$
2{,}80x = 104{,}10 - 14{,}50 = 89{,}60
$$

Despejamos $x$:

$$
x = \frac{89{,}60}{2{,}80} = \frac{896}{28} = 32\text{ m}^3
$$

*Respuesta:* La función es $C(x) = 2{,}80x + 14{,}50$; por $26\text{ m}^3$ pagó $\text{S/ } 87{,}30$; y la factura de $\text{S/ } 104{,}10$ correspondió a $32\text{ m}^3$.

---

#### Ejercicio 5: Determinación del Rango en un Dominio Restringido
Sea la función afín $f: [-3, 4\rangle \to \mathbb{R}$ definida por $f(x) = -3x + 5$.
Determine el rango exacto de la función ($R_f$) y calcule la suma del menor y mayor valor entero que pertenecen al rango.

**Solución paso a paso:**

**Paso 1:** Identificar el dominio y la monotonía de la función:
Dominio: $x \in [-3, 4\rangle \iff -3 \le x < 4$.
La pendiente es $m = -3 < 0$, por lo que la función es **estrictamente decreciente**. Esto significa que al tomar valores mayores de $x$, la función produce valores menores de $y$.

**Paso 2:** Construir la expresión de $f(x)$ paso a paso a partir de la desigualdad del dominio:

$$
-3 \le x < 4
$$

Multiplicamos por $-3$ invirtiendo obligatoriamente el sentido de las desigualdades:

$$
-3(-3) \ge -3x > -3(4) \implies 9 \ge -3x > -12 \iff -12 < -3x \le 9
$$

Sumamos $5$ a todos los miembros:

$$
-12 + 5 < -3x + 5 \le 9 + 5
$$

$$
-7 < f(x) \le 14
$$

**Paso 3:** Expresar el rango en notación de intervalo:

$$
R_f = \langle -7, 14]
$$

**Paso 4:** Identificar los valores enteros extremos del rango:
El menor entero en $\langle -7, 14]$ es $-6$ (dado que $-7$ es abierto).
El mayor entero en $\langle -7, 14]$ es $14$ (cerrado).
Suma de ambos enteros:

$$
\text{Suma} = -6 + 14 = 8
$$

*Respuesta:* El rango es $R_f = \langle -7, 14]$ y la suma requerida es $8$.

---

#### Ejercicio 6: Intersección de dos Funciones Afines y Punto de Quiebre
En un mercado regional, dos empresas de transporte de encomiendas tienen las siguientes tarifas para envíos interprovinciales en función del peso $p$ (en kilogramos):
Empresa Expreso Andino: $T_A(p) = 4p + 25$.
Empresa Transportes del Centro: $T_B(p) = 6{,}5p + 10$.
Determine para qué peso de encomienda ambas empresas cobran exactamente la misma tarifa y cuál de ellas resulta más conveniente si se desea enviar un paquete de $10\text{ kg}$.

**Solución paso a paso:**

**Paso 1:** Igualar ambas funciones de costo para hallar el punto de intersección:

$$
T_A(p) = T_B(p)
$$

$$
4p + 25 = 6{,}5p + 10
$$

**Paso 2:** Despejar el peso $p$:

$$
25 - 10 = 6{,}5p - 4p
$$

$$
15 = 2{,}5p \implies p = \frac{15}{2{,}5} = 6\text{ kg}
$$

A los $6\text{ kg}$, ambas cobran: $T(6) = 4(6) + 25 = 24 + 25 = \text{S/ } 49$.

**Paso 3:** Evaluar para un paquete de $p = 10\text{ kg}$ ($10 > 6$):
Para Expreso Andino:
$T_A(10) = 4(10) + 25 = 40 + 25 = \text{S/ } 65$.
Para Transportes del Centro:
$T_B(10) = 6{,}5(10) + 10 = 65 + 10 = \text{S/ } 75$.
Como $\text{S/ } 65 < \text{S/ } 75$, Expreso Andino es más económica.

*Respuesta:* Ambas cobran igual a los $6\text{ kg}$ ($\text{S/ } 49$), y para $10\text{ kg}$ conviene Expreso Andino (ahorro de $\text{S/ } 10$).

---

#### Ejercicio 7: Depreciación Lineal de Maquinaria Agroindustrial
Una asociación de productores de cacao en San Martín adquiere una máquina seleccionadora de grano por un valor inicial de $\text{US\$\; } 24\,000$. Los peritos contables determinan que la máquina tiene una vida útil de $10\text{ años}$, al término de los cuales su valor de rescate o chatarra será de $\text{US\$\; } 4\,000$. Asumiendo una depreciación lineal constante:
a) Determine la regla de correspondencia del valor contable de la máquina $V(t)$ en función de los años transcurridos $t \in [0, 10]$.
b) Calcule el valor contable de la máquina al cabo de $6\text{ años}$ de uso.

**Solución paso a paso:**

**Paso 1:** Identificar los puntos coordenados $(t, V)$ en el plano cartesiano:
En el momento de compra ($t = 0$): $V(0) = 24\,000 \implies P_0(0, 24\,000)$.
Al cabo de $10\text{ años}$ ($t = 10$): $V(10) = 4\,000 \implies P_1(10, 4\,000)$.

**Paso 2:** Calcular la tasa de depreciación anual (pendiente $m$):

$$
m = \frac{V_1 - V_0}{t_1 - t_0} = \frac{4\,000 - 24\,000}{10 - 0} = \frac{-20\,000}{10} = -2\,000\text{ US\$/año}
$$

La máquina pierde un valor constante de $\text{US\$\; } 2\,000$ por cada año transcurrido.

**Paso 3:** Formular la función afín:
Con ordenada en el origen $b = 24\,000$:

$$
V(t) = -2\,000t + 24\,000 \quad (0 \le t \le 10)
$$

**Paso 4:** Calcular el valor a los $t = 6\text{ años}$:

$$
V(6) = -2\,000(6) + 24\,000 = -12\,000 + 24\,000 = \text{US\$\; } 12\,000
$$

*Respuesta:* La función de depreciación es $V(t) = -2\,000t + 24\,000$, y a los $6\text{ años}$ su valor es $\text{US\$\; } 12\,000$.

---

### Bloque C: Nivel Avanzado y Contextualizado (Beca 18 / UNI)

#### Ejercicio 8: Composición Funcional e Inversa de una Función Afín
Dada la función afín biyectiva $f(x) = \frac{3x - 5}{4}$, determine la regla de correspondencia de su función inversa $f^{-1}(x)$ y halle el punto geométrico de intersección entre las rectas correspondientes a $f(x)$ y a su inversa $f^{-1}(x)$ en el plano cartesiano.

**Solución paso a paso:**

**Paso 1:** Hallar la función inversa despejando $x$ en función de $y$:
Sea $y = \frac{3x - 5}{4}$.
Multiplicamos por $4$:

$$
4y = 3x - 5 \implies 3x = 4y + 5 \implies x = \frac{4y + 5}{3}
$$

Intercambiando variables, la función inversa es:

$$
f^{-1}(x) = \frac{4x + 5}{3} = \frac{4}{3}x + \frac{5}{3}
$$

**Paso 2:** Recordar la propiedad de simetría de las funciones inversas:
La gráfica de una función y la de su inversa son reflexiones simétricas respecto a la recta identidad $y = x$.
Por tanto, si las rectas se intersecan, su punto de corte debe pertenecer necesariamente a la recta $y = x$, lo que implica $f(x) = x$.

**Paso 3:** Resolver la ecuación $f(x) = x$:

$$
\frac{3x - 5}{4} = x \implies 3x - 5 = 4x \implies 4x - 3x = -5 \implies x = -5
$$

**Paso 4:** Determinar la ordenada del punto de corte:
Como $y = x \implies y = -5$.
El punto de intersección es $P(-5, -5)$.

*Respuesta:* La inversa es $f^{-1}(x) = \frac{4x + 5}{3}$ y se intersecan en el punto $(-5, -5)$.

---

#### Ejercicio 9: Área de la Región Triangular Determinada por los Ejes Coordenados
Una función afín $h(x) = mx + b$ tiene pendiente negativa $m = -\frac{3}{4}$ y determina junto con los semiejes positivos de coordenadas un triángulo rectángulo cuya área es igual a $24\text{ u}^2$.
Determine la regla de correspondencia de $h(x)$ y las coordenadas de sus puntos de corte con los ejes.

**Solución paso a paso:**

**Paso 1:** Encontrar las intersecciones de la recta con los ejes en función de $b$:
Corte con el eje $Y$:
$x = 0 \implies y = h(0) = b$.
Dado que el triángulo está en el primer cuadrante con semiejes positivos, $b > 0$. Punto: $(0, b)$.
Corte con el eje $X$:
$y = 0 \implies -\frac{3}{4}x + b = 0 \implies \frac{3}{4}x = b \implies x = \frac{4b}{3}$.
Punto: $\left( \frac{4b}{3}, 0 \right)$.

**Paso 2:** Formular el área del triángulo rectángulo:
Los catetos del triángulo sobre los ejes son la base $B = \frac{4b}{3}$ y la altura $H = b$:

$$
\text{Área} = \frac{B \cdot H}{2} = \frac{\left(\frac{4b}{3}\right) \cdot b}{2} = \frac{4b^2}{6} = \frac{2b^2}{3}
$$

**Paso 3:** Igualar al área dada ($24\text{ u}^2$) y despejar $b$:

$$
\frac{2b^2}{3} = 24 \implies 2b^2 = 72 \implies b^2 = 36
$$

Como $b > 0$:

$$
b = 6
$$

**Paso 4:** Calcular la base y formular la función:
Base: $x = \frac{4(6)}{3} = 8$.
La regla de correspondencia es:

$$
h(x) = -\frac{3}{4}x + 6
$$

Los puntos de corte son $(8, 0)$ en el eje $X$ y $(0, 6)$ en el eje $Y$.

*Respuesta:* La función es $h(x) = -\frac{3}{4}x + 6$, con cortes en $(8, 0)$ y $(0, 6)$.

---

#### Ejercicio 10: Función Afín a Trozos y Continuidad Operativa
En un parque tecnológico de innovación en Arequipa, el consumo de energía eléctrica industrial se factura bajo un esquema escalonado continuo:
Para los primeros $500\text{ kWh}$, la tarifa sigue la función afín $f_1(x) = 0{,}60x + 50$.
Para consumos superiores a $500\text{ kWh}$, la empresa aplica una tarifa reducida por consumo masivo dada por $f_2(x) = 0{,}40x + K$.
Determine el valor exacto de la constante $K$ para que el modelo de facturación sea continuo (es decir, no exista un salto brusco de precio al superar exactamente los $500\text{ kWh}$) y calcule el costo de un consumo de $850\text{ kWh}$.

**Solución paso a paso:**

**Paso 1:** Imponer la condición de continuidad en el punto de transición $x = 500$:
Para que no haya salto en $x = 500$, ambas funciones deben generar exactamente el mismo importe en dicho punto:

$$
f_1(500) = f_2(500)
$$

**Paso 2:** Calcular $f_1(500)$:

$$
f_1(500) = 0{,}60(500) + 50 = 300 + 50 = 350\text{ soles}
$$

**Paso 3:** Igualar con $f_2(500)$ y despejar $K$:

$$
0{,}40(500) + K = 350
$$

$$
200 + K = 350 \implies K = 350 - 200 = 150
$$

La función para consumos mayores a $500\text{ kWh}$ es $f_2(x) = 0{,}40x + 150$.

**Paso 4:** Calcular el costo para un consumo de $x = 850\text{ kWh}$:
Como $850 > 500$, aplicamos $f_2(x)$:

$$
C(850) = f_2(850) = 0{,}40(850) + 150
$$

Efectuamos el producto: $0{,}40 \times 850 = 340$.

$$
C(850) = 340 + 150 = \text{S/ } 490
$$

*Respuesta:* La constante requerida es $K = 150$ y el costo por $850\text{ kWh}$ es de $\text{S/ } 490$.

---

## 4. Práctica Propuesta (45 Ejercicios)

### Bloque I: Nivel Básico (Problemas 01 al 15)

1. Calcule la pendiente de la recta que pasa por los puntos $P(1, 4)$ y $Q(5, 16)$.  
A) $2$  
B) $3$  
C) $4$  
D) $5$  
E) $6$  

2. Si $f(x) = 5x - 8$, halle el valor de $f(3) + f(0)$.  
A) $-1$  
B) $0$  
C) $1$  
D) $7$  
E) $-8$  

3. ¿Cuál es el punto de corte con el eje $Y$ de la función afín $g(x) = -3x + 11$?  
A) $(0, 11)$  
B) $(11, 0)$  
C) $(0, -3)$  
D) $(-3, 0)$  
E) $(0, -11)$  

4. Halle la raíz o cero de la función $h(x) = 2x - 14$.  
A) $5$  
B) $6$  
C) $7$  
D) $-7$  
E) $14$  

5. Si una recta de pendiente $m = -2$ pasa por el punto $(3, 1)$, ¿cuál es su ordenada en el origen?  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $-5$  

6. Determine cuál de las siguientes funciones es estrictamente decreciente para todo $x \in \mathbb{R}$.  
A) $f(x) = 3x - 5$  
B) $g(x) = -4x + 1$  
C) $h(x) = 0{,}5x + 2$  
D) $p(x) = 7$  
E) $q(x) = x$  

7. Una función lineal $f(x) = mx$ cumple que $f(4) = 28$. Halle el valor de $f(-2)$.  
A) $-14$  
B) $-7$  
C) $14$  
D) $-28$  
E) $7$  

8. Si la gráfica de $f(x) = ax + b$ pasa por $(0, 3)$ y $(2, 7)$, calcule $a \cdot b$.  
A) $6$  
B) $8$  
C) $10$  
D) $12$  
E) $5$  

9. Un ciclista viaja a una velocidad constante de $18\text{ km/h}$. Si parte del kilómetro $5$ de la carretera, ¿qué función modela su posición $s(t)$ en kilómetros tras $t$ horas?  
A) $s(t) = 5t + 18$  
B) $s(t) = 18t + 5$  
C) $s(t) = 18t - 5$  
D) $s(t) = 13t$  
E) $s(t) = 23t$  

10. Si $f(x) = 2x + k$ y se sabe que $f(5) = 17$, determine el valor de la constante $k$.  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

11. Halle el ángulo de inclinación $\theta$ de la recta correspondiente a la función $f(x) = x + 4$.  
A) $30^\circ$  
B) $45^\circ$  
C) $60^\circ$  
D) $90^\circ$  
E) $0^\circ$  

12. Calcule la distancia entre el punto de corte con el eje $X$ y el punto de corte con el eje $Y$ de la función $f(x) = -\frac{4}{3}x + 4$.  
A) $3\text{ u}$  
B) $4\text{ u}$  
C) $5\text{ u}$  
D) $6\text{ u}$  
E) $7\text{ u}$  

13. Si $f$ es una función lineal tal que $f(a + b) = f(a) + f(b)$, y $f(3) = 15$, calcule $f(1) + f(2)$.  
A) $10$  
B) $12$  
C) $15$  
D) $20$  
E) $18$  

14. Determine la pendiente de la recta cuya ecuación general es $3x + 2y - 8 = 0$.  
A) $\frac{3}{2}$  
B) $-\frac{3}{2}$  
C) $\frac{2}{3}$  
D) $-\frac{2}{3}$  
E) $4$  

15. Si el dominio de la función $f(x) = 2x - 3$ es $[1, 5]$, ¿cuál es su rango?  
A) $[-1, 7]$  
B) $\langle -1, 7\rangle$  
C) $[1, 7]$  
D) $[-1, 5]$  
E) $[0, 7]$  

---

### Bloque II: Nivel Intermedio (Problemas 16 al 30)

16. Si una función afín satisface $f(2) = 7$ y $f(5) = 16$, calcule el valor de $f(10)$.  
A) $28$  
B) $30$  
C) $31$  
D) $32$  
E) $35$  

17. Determine el rango de la función afín $g(x) = -4x + 3$ definida en el intervalo $x \in \langle -2, 3]$.  
A) $[-9, 11\rangle$  
B) $\langle -9, 11]$  
C) $[-9, 11]$  
D) $\langle -11, 9]$  
E) $[-11, 9\rangle$  

18. En una ciudad de la selva peruana, el servicio de mototaxi cobra una tarifa base de $\text{S/ } 2{,}50$ más $\text{S/ } 1{,}20$ por cada kilómetro recorrido. Si un pasajero pagó $\text{S/ } 10{,}90$, ¿cuántos kilómetros recorrió?  
A) $6\text{ km}$  
B) $7\text{ km}$  
C) $8\text{ km}$  
D) $7{,}5\text{ km}$  
E) $8{,}5\text{ km}$  

19. Dadas las rectas $L_1: y = 2x - 4$ y $L_2: y = -x + 5$. Halle las coordenadas del punto de intersección.  
A) $(3, 2)$  
B) $(2, 3)$  
C) $(3, 1)$  
D) $(1, 4)$  
E) $(4, 1)$  

20. Si la función $f(x) = (2m - 6)x + m + 1$ es una función constante, halle el valor de $f(100)$.  
A) $3$  
B) $4$  
C) $7$  
D) $0$  
E) $1$  

21. Halle el área de la región triangular que forma la recta de la función $f(x) = 2x - 6$ con los ejes coordenados.  
A) $6\text{ u}^2$  
B) $8\text{ u}^2$  
C) $9\text{ u}^2$  
D) $12\text{ u}^2$  
E) $18\text{ u}^2$  

22. Si $f(x) = mx + b$ pasa por el punto $(1, 4)$ y su gráfica es paralela a la recta $y = 3x - 10$, determine el valor de $b$.  
A) $1$  
B) $2$  
C) $3$  
D) $-1$  
E) $4$  

23. Una piscina de $48\text{ m}^3$ de capacidad se desagua mediante una bomba a razón constante de $3\text{ m}^3/\text{h}$. ¿Cuál es la regla de correspondencia que modela el volumen restante $V(t)$ tras $t$ horas y en cuántas horas se vacía totalmente?  
A) $V(t) = 48 - 3t; \ 16\text{ h}$  
B) $V(t) = 48 + 3t; \ 16\text{ h}$  
C) $V(t) = 48 - 4t; \ 12\text{ h}$  
D) $V(t) = 48 - 2t; \ 24\text{ h}$  
E) $V(t) = 16 - 3t; \ 5{,}3\text{ h}$  

24. Si la función afín $f(x) = ax + b$ cumple que $f(f(x)) = 9x + 8$ con $a > 0$, determine el valor de $a + b$.  
A) $4$  
B) $5$  
C) $6$  
D) $7$  
E) $8$  

25. Halle la ecuación de la recta perpendicular a la gráfica de $f(x) = 2x - 3$ que pasa por el punto $(4, 1)$.  
A) $y = -\frac{1}{2}x + 3$  
B) $y = -\frac{1}{2}x + 2$  
C) $y = -2x + 9$  
D) $y = \frac{1}{2}x - 1$  
E) $y = -\frac{1}{2}x + 1$  

26. Si $f(x) = 3x - 2$, determine el valor de la pendiente de la función inversa $f^{-1}(x)$.  
A) $3$  
B) $-3$  
C) $\frac{1}{3}$  
D) $-\frac{1}{3}$  
E) $\frac{2}{3}$  

27. Una fotocopiadora industrial tiene un costo de alquiler de $\text{S/ } 150$ al mes más un costo de $\text{S/ } 0{,}05$ por cada copia realizada. Si en un mes el costo total fue de $\text{S/ } 385$, ¿cuántas copias se sacaron?  
A) $4\,500$  
B) $4\,700$  
C) $4\,800$  
D) $5\,000$  
E) $5\,200$  

28. Si los puntos $A(-1, 3)$, $B(2, 9)$ y $C(k, 15)$ son colineales (pertenecen a la misma recta), determine el valor de $k$.  
A) $4$  
B) $5$  
C) $6$  
D) $3$  
E) $7$  

29. Halle el punto de la recta $y = 2x - 5$ cuya ordenada es el triple de su abscisa.  
A) $(-5, -15)$  
B) $(5, 15)$  
C) $(-3, -9)$  
D) $(2, 6)$  
E) $(1, 3)$  

30. Si la función $f(x) = ax + b$ cumple que $f(1) = 5$ y la recta corta al eje $X$ en $x = -4$, calcule $a - b$.  
A) $-3$  
B) $3$  
C) $-2$  
D) $2$  
E) $0$  

---

### Bloque III: Nivel Avanzado y Retos Beca 18 (Problemas 31 al 45)

31. Un sensor de temperatura industrial calibrado en grados Celsius ($C$) envía lecturas a un sistema informático en grados Fahrenheit ($F$) mediante la relación afín estándar $F(C) = \frac{9}{5}C + 32$. Si la temperatura en un reactor químico varía en el intervalo cerrado $[-15^\circ\text{C}, 45^\circ\text{C}]$, determine la longitud del intervalo correspondiente en la escala Fahrenheit.  
A) $100^\circ\text{F}$  
B) $108^\circ\text{F}$  
C) $112^\circ\text{F}$  
D) $116^\circ\text{F}$  
E) $96^\circ\text{F}$  

32. Si la función $f(x) = mx + b$ satisface que la suma de sus intersecciones con los ejes coordenados es igual a $10$, y su pendiente es $m = -\frac{2}{3}$, determine el valor de $f(6)$.  
A) $12$  
B) $14$  
C) $16$  
D) $18$  
E) $20$  

33. Una cooperativa de ahorro y crédito en Huancavelica remunera depósitos a plazo fijo según una función lineal del capital $C$: el interés anual es $I(C) = 0{,}085C$. Si un socio incrementa su depósito en $\text{S/ } 12\,000$, su interés anual aumenta en:  
A) $\text{S/ } 980$  
B) $\text{S/ } 1\,020$  
C) $\text{S/ } 1\,050$  
D) $\text{S/ } 1\,080$  
E) $\text{S/ } 1\,120$  

34. Sean las funciones afines $f(x) = 2x + 3$ y $g(x) = -x + 9$. Determine el área de la región poligonal delimitada por las gráficas de $f(x)$, $g(x)$ y el eje horizontal de las abscisas ($X$).  
A) $36{,}75\text{ u}^2$  
B) $35{,}50\text{ u}^2$  
C) $38{,}25\text{ u}^2$  
D) $32{,}00\text{ u}^2$  
E) $40{,}50\text{ u}^2$  

35. Si la función afín $h(x)$ cumple que $h(x + 2) - h(x - 1) = 12$ para todo $x \in \mathbb{R}$, y además $h(1) = 7$, determine la regla de correspondencia de $h(x)$.  
A) $h(x) = 4x + 3$  
B) $h(x) = 4x - 3$  
C) $h(x) = 3x + 4$  
D) $h(x) = 6x + 1$  
E) $h(x) = 2x + 5$  

36. En una planta procesadora de espárragos en Ica, el costo total de operar $t$ horas al día es una función afín $C(t) = mt + b$. Por $4\text{ horas}$ de operación el costo es de $\text{S/ } 3\,800$, y por $9\text{ horas}$ el costo asciende a $\text{S/ } 7\,550$. ¿Cuál es el costo fijo diario de la planta cuando las máquinas están apagadas ($t = 0$)?  
A) $\text{S/ } 750$  
B) $\text{S/ } 800$  
C) $\text{S/ } 850$  
D) $\text{S/ } 900$  
E) $\text{S/ } 950$  

37. Si $f(x)$ es una función afín tal que $f^{-1}(2) = 1$ y $f^{-1}(8) = 4$, determine el valor de $f(7)$.  
A) $12$  
B) $14$  
C) $15$  
D) $16$  
E) $18$  

38. Se tiene la función $f(x) = ax + b$. Si se define la sucesión de valores $y_n = f(n)$ para $n \in \{1, 2, 3, \dots\}$, demuestre que $\{y_n\}$ constituye una progresión aritmética y determine su razón común $d$.  
A) $d = a$  
B) $d = b$  
C) $d = a + b$  
D) $d = 2a$  
E) $d = \frac{a}{b}$  

39. Determine el valor de $k$ para que la recta correspondiente a la función afín $f(x) = (k - 1)x + 2k + 6$ pase por el punto de intersección de las rectas $y = 3x - 1$ e $y = -2x + 9$.  
A) $1$  
B) $-1$  
C) $0$  
D) $2$  
E) $-2$  

40. Si la gráfica de $f(x) = mx + b$ no pasa por el cuarto cuadrante del plano cartesiano, ¿qué condiciones deben cumplir los parámetros $m$ y $b$?  
A) $m > 0 \land b > 0$  
B) $m \ge 0 \land b \ge 0$  
C) $m \le 0 \land b \ge 0$  
D) $m > 0 \land b \le 0$  
E) $m < 0 \land b < 0$  

41. Sean $f$ y $g$ dos funciones afines tales que $(f \circ g)(x) = 6x - 7$ y $g(x) = 2x + 1$. Determine la regla de correspondencia de $f(x)$.  
A) $f(x) = 3x - 10$  
B) $f(x) = 3x - 4$  
C) $f(x) = 3x + 10$  
D) $f(x) = 4x - 5$  
E) $f(x) = 3x - 8$  

42. La recta $L$ correspondiente a $f(x) = mx + b$ forma con los ejes coordenados en el segundo cuadrante un triángulo isósceles de área $18\text{ u}^2$. Halle el valor de $b - m$.  
A) $5$  
B) $7$  
C) $6$  
D) $8$  
E) $4$  

43. Una empresa de paneles solares estima que la potencia de salida $P(t)$ (en vatios) de un módulo durante las primeras horas de la mañana responde a la función afín $P(t) = 45t + 30$ ($t$ en horas, con $t = 0$ a las 6:00 a.m.). Si la energía total generada entre las 6:00 a.m. y las 10:00 a.m. se calcula geométricamente como el área bajo la recta en el plano $(t, P)$, ¿cuántos vatios-hora ($\text{W}\cdot\text{h}$) se produjeron en ese lapso de $4\text{ horas}$?  
A) $440\text{ W}\cdot\text{h}$  
B) $460\text{ W}\cdot\text{h}$  
C) $480\text{ W}\cdot\text{h}$  
D) $500\text{ W}\cdot\text{h}$  
E) $520\text{ W}\cdot\text{h}$  

44. Si $f(x)$ es una función afín decreciente tal que $(f \circ f)(x) = 16x - 15$, halle el valor de $f(2)$.  
A) $-5$  
B) $-7$  
C) $-3$  
D) $5$  
E) $-9$  

45. Determine el conjunto de todos los valores de $a \in \mathbb{R}$ para los cuales las tres rectas $L_1: y = 2x + 1$, $L_2: y = -x + 7$ y $L_3: y = ax + 3$ no forman un triángulo en el plano cartesiano.  
A) $\{-1, 2, 1\}$  
B) $\{-1, 2\}$  
C) $\left\{ -1, 2, \frac{1}{2} \right\}$  
D) $\left\{ -1, 2, \frac{2}{3} \right\}$  
E) $\{1, 2\}$  

---

## 5. Clave de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | B | **16** | C | **31** | B |
| **02** | A | **17** | A | **32** | C |
| **03** | A | **18** | B | **33** | B |
| **04** | C | **19** | A | **34** | A |
| **05** | C | **20** | B | **35** | A |
| **06** | B | **21** | C | **36** | B |
| **07** | A | **22** | A | **37** | B |
| **08** | A | **23** | A | **38** | A |
| **09** | B | **24** | B | **39** | B |
| **10** | C | **25** | A | **40** | B |
| **11** | B | **26** | C | **41** | A |
| **12** | C | **27** | B | **42** | A |
| **13** | C | **28** | B | **43** | C |
| **14** | B | **29** | A | **44** | A |
| **15** | A | **30** | A | **45** | A |

---

## 6. Pistas Metodológicas (Problemas 41 al 45)

* **Pista para el Ejercicio 41:**
Sea $f(u) = mu + b$. La composición es $(f \circ g)(x) = f(g(x)) = f(2x + 1) = m(2x + 1) + b = 2mx + m + b$.
Igualamos con $6x - 7$:
$2m = 6 \implies m = 3$.
$m + b = -7 \implies 3 + b = -7 \implies b = -10$.
Por tanto, la regla de correspondencia es $f(x) = 3x - 10$.

* **Pista para el Ejercicio 42:**
En el segundo cuadrante, la recta corta al eje $X$ en un valor negativo $x_0 = -k$ ($k > 0$) y al eje $Y$ en un valor positivo $y_0 = k$ para que sea isósceles.
El área del triángulo es $\frac{k \cdot k}{2} = 18 \implies k^2 = 36 \implies k = 6$.
Puntos de corte: $(-6, 0)$ y $(0, 6)$.
Pendiente: $m = \frac{6 - 0}{0 - (-6)} = 1$.
Ordenada en el origen: $b = 6$.
El valor de $b - m$ es $6 - 1 = 5$.

* **Pista para el Ejercicio 43:**
El área bajo la recta $P(t) = 45t + 30$ desde $t = 0$ hasta $t = 4$ corresponde a un trapecio rectángulo:
Base menor: $P(0) = 30\text{ W}$.
Base mayor: $P(4) = 45(4) + 30 = 180 + 30 = 210\text{ W}$.
Altura: $h = 4 - 0 = 4\text{ horas}$.
Área (energía total generada):

$$
E = \left(\frac{B + b}{2}\right) \cdot h = \left(\frac{210 + 30}{2}\right) \cdot 4 = 120 \times 4 = 480\text{ W}\cdot\text{h}
$$

* **Pista para el Ejercicio 44:**
Sea $f(x) = ax + b$. Como $f$ es decreciente, $a < 0$.
$(f \circ f)(x) = a(ax + b) + b = a^2x + ab + b = 16x - 15$.
Igualando coeficientes:
$a^2 = 16 \implies a = -4$ (dado que $a < 0$).
$ab + b = -15 \implies -4b + b = -15 \implies -3b = -15 \implies b = 5$.
La función es $f(x) = -4x + 5$.
Evaluando en $x = 2$: $f(2) = -4(2) + 5 = -8 + 5 = -5$.

* **Pista para el Ejercicio 45:**
Tres rectas no forman un triángulo si ocurren dos situaciones posibles:
1) Al menos dos de ellas son paralelas (tienen la misma pendiente):
Pendiente de $L_1$ es $2 \implies a = 2$.
Pendiente de $L_2$ es $-1 \implies a = -1$.
2) Las tres rectas son concurrentes (se intersectan exactamente en el mismo punto):
Punto de corte de $L_1$ y $L_2$:
$2x + 1 = -x + 7 \implies 3x = 6 \implies x = 2 \implies y = 2(2) + 1 = 5$.
Punto de corte: $(2, 5)$.
Para que $L_3: y = ax + 3$ pase por $(2, 5)$:
$5 = a(2) + 3 \implies 2a = 2 \implies a = 1$.
Por lo tanto, los valores donde no forman un triángulo son $a \in \{-1, 1, 2\}$.

---

## 7. Formulario Resumen

### Clasificación y Propiedades de la Función Lineal y Afín

| Tipo de Función | Regla de Correspondencia | Punto de Paso Obligatorio | Pendiente ($m$) | Gráfica en $\mathbb{R}^2$ |
| :--- | :---: | :---: | :---: | :--- |
| **Función Lineal** | $f(x) = m \cdot x$ | $(0, 0)$ (Origen de coordenadas) | $m = \frac{f(x)}{x} \neq 0$ | Recta que pasa por el centro |
| **Función Afín** | $g(x) = m \cdot x + b$ | $(0, b)$ (Ordenada en el origen) | $m = \frac{\Delta y}{\Delta x} \neq 0$ | Recta trasladada verticalmente |
| **Función Constante** | $h(x) = b$ | $(0, b)$ | $m = 0$ | Recta horizontal paralela al eje $X$ |
| **Función Identidad** | $I(x) = x$ | $(0, 0)$ | $m = 1 \ (\theta = 45^\circ)$ | Bisectriz de los cuadrantes I y III |

---

### Expresiones de la Pendiente y Relaciones entre Rectas

| Concepto Geométrico | Expresión Matemática | Condición Analítica |
| :--- | :--- | :--- |
| **Pendiente por Dos Puntos** | $m = \frac{y_2 - y_1}{x_2 - x_1} = \tan \theta$ | $x_1 \neq x_2$ ($\theta$: ángulo de inclinación) |
| **Rectas Paralelas ($L_1 \parallel L_2$)** | $m_1 = m_2$ | Misma inclinación geométrica |
| **Rectas Perpendiculares ($L_1 \perp L_2$)** | $m_1 \cdot m_2 = -1$ | Producto de pendientes igual a $-1$ |
| **Cero / Raíz de la Función** | $x_0 = -\frac{b}{m}$ | Punto de corte con el eje $X$: $\left(-\frac{b}{m}, 0\right)$ |
| **Área con los Ejes Coordenados** | $A = \frac{\vert b \cdot x_0 \vert}{2} = \frac{b^2}{2\vert m \vert}$ | Triángulo rectángulo en el plano cartesiano |

---

### Modelos de Variación Lineal en Contexto Real

| Ámbito de Aplicación | Función Modelo | Significado Físico / Económico |
| :--- | :--- | :--- |
| **Tarifa de Servicio Público** | $T(x) = c_u \cdot x + C_{\text{fijo}}$ | $c_u$: costo unitario por consumo; $C_{\text{fijo}}$: cargo base |
| **Depreciación Lineal** | $V(t) = -d \cdot t + V_0$ | $V_0$: valor de compra; $d$: depreciación anual constante |
| **Cinemática (MRU)** | $x(t) = v \cdot t + x_0$ | $v$: velocidad constante; $x_0$: posición inicial |
| **Escala de Temperatura** | $F(C) = \frac{9}{5}C + 32$ | Razón de cambio: $1{,}8^\circ\text{F}$ por cada $1^\circ\text{C}$ |
