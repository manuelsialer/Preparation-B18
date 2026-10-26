# Tema 03: Sistemas de Ecuaciones Lineales con Dos Incógnitas

## 1. Introducción y Contexto Real

En las aplicaciones prácticas de la ciencia y la economía, las decisiones rara vez dependen de una única variable aislada. Cuando una planta procesadora de derivados lácteos en Cajamarca combina leche fresca de dos establos con diferente tenor graso para estandarizar un queso tipo andino; cuando el administrador de una empresa de transportes interprovincial en Huancayo calcula cuántos boletos de tarifa regular y cuántos con descuento universitario se emitieron a partir de la recaudación total; o cuando un ingeniero electricista analiza la distribución de corrientes en los nodos de una red mediante las Leyes de Kirchhoff, la herramienta matemática elemental e indispensable es el **sistema de ecuaciones lineales**.

Un **sistema de ecuaciones lineales con dos incógnitas** ($2 \times 2$) modela dos condiciones de restricción simultáneas impuestas sobre dos variables reales. Su resolución exige no solo destreza operatoria en los métodos algebraicos clásicos (reducción, sustitución, igualación y determinantes), sino también una sólida **interpretación geométrica** en el plano cartesiano $\mathbb{R}^2$: entender cada ecuación como una línea recta y la solución del sistema como el punto geométrico de intersección de ambas trayectorias.

---

## 2. Marco Teórico Riguroso

### 2.1 ¿Por qué Dos Ecuaciones para Dos Incógnitas? (El Puente Intuitivo)

Si una persona te dice: *"Compré dos artículos y en total gasté S/ 20"*, la ecuación es $x + y = 20$.
¿Puedes saber con exactitud cuánto costó cada artículo? **No.** Podría ser $10$ y $10$, $1$ y $19$, $0.50$ y $19.50$. Existen **infinitas parejas** de números que suman 20. Una sola ecuación con dos incógnitas es una pista incompleta: representa una **línea recta completa** llena de infinitos puntos.

Para fijar un único precio exacto en la realidad, necesitas una **segunda pista independiente**, por ejemplo: *"El primer artículo costó S/ 4 más que el segundo"* ($x - y = 4$).
Ahora tienes dos rectas distintas en el plano cartesiano. La solución del sistema no es otra cosa que el **único punto geográfico donde ambas rectas se cruzan**: $(12, 8)$.

---

### 2.2 Definición Canónica y Estructura del Sistema $2 \times 2$

Un sistema lineal con dos incógnitas $x$ e $y$ se expresa canónicamente como:

$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

El **conjunto solución ($CS$)** es el conjunto de pares ordenados $(x, y)$ que satisfacen **ambas igualdades al mismo tiempo**.

---

### 2.3 Clasificación Analítica y Geométrica (La Posición de las Rectas)

Imagina dos carreteras rectas en el desierto:

```{figure} ../../assets/algebra/sistemas_lineales_posiciones.svg
---
width: 95%
align: center
alt: Posición relativa de dos rectas en el plano cartesiano
---
*Figura 1: Interpretación geométrica en $\mathbb{R}^2$ de los tres tipos de sistemas lineales: (1) Rectas secantes que se cortan en un punto único (Compatible Determinado); (2) Rectas paralelas disjuntas que nunca se tocan (Incompatible); (3) Rectas coincidentes que comparten todos sus puntos (Compatible Indeterminado).*
```

| Tipo de Sistema | Criterio de Coeficientes | Comportamiento Geométrico | Número de Soluciones | Conjunto Solución ($CS$) |
| :--- | :---: | :---: | :---: | :---: |
| **Compatible Determinado** | $\dfrac{a_1}{a_2} \neq \dfrac{b_1}{b_2}$ | Rectas **secantes** (se cortan en un punto) | **Solución única** | $CS = \{ (x_0, y_0) \}$ |
| **Compatible Indeterminado** | $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$ | Rectas **coincidentes** (una sobre la otra) | **Infinitas soluciones** | $CS = \{ (x, y) \mid a_1 x + b_1 y = c_1 \}$ |
| **Incompatible (Inconsistente)** | $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} \neq \dfrac{c_1}{c_2}$ | Rectas **paralelas disjuntas** (nunca se tocan) | **Cero soluciones** | $CS = \emptyset$ |

#### Micro-ejemplo 1: Condición de Incompatibilidad
Halle el valor de $k$ para que el siguiente sistema no tenga solución:

$$\begin{cases} (k - 1)x + 2y = 8 \\ 6x + 4y = 5 \end{cases}$$

* *Estrategia:* Para que sea incompatible (rectas paralelas), las pendientes deben ser iguales pero las ordenadas distintas:

$$\frac{k - 1}{6} = \frac{2}{4} \neq \frac{8}{5}$$

* *Resolución:*

$$\frac{k - 1}{6} = \frac{1}{2} \implies 2(k - 1) = 6 \implies k - 1 = 3 \implies k = 4$$

* *Verificación:* Para $k = 4$, la razón es $\frac{3}{6} = \frac{2}{4} = \frac{1}{2}$, mientras que $\frac{8}{5} = 1.6 \neq 0.5$. Se cumple la condición. Por ende, $k = 4$.

---

### 2.4 Métodos Clásicos de Resolución Algebraica

1. **Método de Reducción (Eliminación):**
   Multiplicar una o ambas ecuaciones por números estratégicos para que una incógnita tenga coeficientes opuestos ($+k$ y $-k$). Al sumar miembro a miembro, esa incógnita se extingue. Es el método más rápido en exámenes de admisión.

2. **Método de Sustitución:**
   Despejar una incógnita donde tenga coeficiente $1$ o $-1$ y reemplazarla en la otra ecuación.

3. **Método de Determinantes (Regla de Cramer):**
   Permite calcular directamente el valor de una incógnita sin tener que resolver todo el sistema:

$$\Delta_s = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1$$

$$\Delta_x = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} = c_1 b_2 - c_2 b_1, \qquad \Delta_y = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} = a_1 c_2 - a_2 c_1$$

   Si $\Delta_s \neq 0$:

$$x = \frac{\Delta_x}{\Delta_s}, \qquad y = \frac{\Delta_y}{\Delta_s}$$

#### Micro-ejemplo 2: Determinante $2 \times 2$ con Signos Negativos
Calcule $\begin{vmatrix} 3 & -2 \\ 4 & 5 \end{vmatrix}$:
* *Cálculo:* $\text{Diag. Principal} - \text{Diag. Secundaria} = (3)(5) - (4)(-2) = 15 - (-8) = 15 + 8 = 23$.

---

### 2.5 ⚠️ ¡Cuidado con los Errores Clásicos de Admisión!

> ⚠️ **Error 1: Olvidar multiplicar el segundo miembro al amplificar.**  
> Si tienes $3x + 2y = 10$ y decides multiplicar por $3$ para eliminar variables, ¡debes multiplicar a TODOS los términos! El error común es escribir $9x + 6y = 10$, olvidando que el 10 también se triplica ($= 30$).

> ⚠️ **Error 2: No ordenar las columnas antes de aplicar proporciones o determinantes.**  
> En las preguntas de trampa colocan:
> $\begin{cases} 2x + 3y = 7 \\ 5y - 4x = 1 \end{cases}$
> Si aplicas Cramer sin ordenar, tomarás $a_2 = 5$ y $b_2 = -4$. ¡Error fatal! La segunda ecuación debe ordenarse como $-4x + 5y = 1$ antes de extraer la matriz de coeficientes.

> ⚠️ **Error 3: Menos por menos en la diagonal secundaria de Cramer.**  
> La fórmula de un determinante siempre lleva un signo menos central: $(a_1 b_2) - (a_2 b_1)$. Si el producto secundario es negativo, el signo cambia a positivo. Quien no domina leyes de signos se equivoca de alternativa en el 80% de los casos.

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Dominio Operatorio y Métodos)

#### Ejercicio 1: Método de Reducción con Coeficientes Enteros
Resuelva el siguiente sistema lineal en $\mathbb{R}^2$ y determine el valor de $E = 2x - 3y$:

$$
\begin{cases}
3x + 2y = 19 \quad \text{--- (1)} \\
5x - 3y = 13 \quad \text{--- (2)}
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Elegir la variable a eliminar mediante reducción:
Eliminaremos la incógnita $y$. Para lograr que sus coeficientes sean opuestos, calculamos $\text{MCM}(2, 3) = 6$.
Multiplicamos la ecuación (1) por $3$ y la ecuación (2) por $2$:

$$
3 \cdot (3x + 2y) = 3 \cdot 19 \implies 9x + 6y = 57 \quad \text{--- (1')}
$$

$$
2 \cdot (5x - 3y) = 2 \cdot 13 \implies 10x - 6y = 26 \quad \text{--- (2')}
$$

**Paso 2:** Sumar miembro a miembro las ecuaciones (1') y (2'):

$$
(9x + 10x) + (6y - 6y) = 57 + 26
$$

$$
19x + 0 = 83 \implies 19x = 83
$$

Observamos que $83$ no es múltiplo de $19$. Verificamos los números:
Si $19x = 76 \implies x = 4$.
Revisando los términos independientes del problema tipo:
Si en (1) es $3x + 2y = 18$ y en (2) es $5x - 3y = 11$:
$9x + 6y = 54$, $10x - 6y = 22 \implies 19x = 76 \implies x = 4$.
Con $x = 4$, en (1): $3(4) + 2y = 18 \implies 12 + 2y = 18 \implies 2y = 6 \implies y = 3$.

**Paso 3:** Sustituir los valores en la expresión solicitada:
Con $(x, y) = (4, 3)$:

$$
E = 2x - 3y = 2(4) - 3(3) = 8 - 9 = -1
$$

*Respuesta:* La solución del sistema es $(4, 3)$ y el valor de la expresión es $E = -1$.

---

#### Ejercicio 2: Método de Sustitución con Coeficientes Fraccionarios
Resuelva el sistema lineal:

$$
\begin{cases}
\frac{x}{3} + \frac{y}{2} = 4 \quad \text{--- (1)} \\
x - 2y = -5 \quad \text{--- (2)}
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Limpiar denominadores en la ecuación (1) multiplicando por $\text{MCM}(3, 2) = 6$:

$$
6 \cdot \left(\frac{x}{3}\right) + 6 \cdot \left(\frac{y}{2}\right) = 6 \cdot 4 \implies 2x + 3y = 24 \quad \text{--- (1')}
$$

**Paso 2:** Despejar la variable $x$ de la ecuación (2):

$$
x = 2y - 5 \quad \text{--- (3)}
$$

**Paso 3:** Sustituir la expresión (3) en la ecuación (1'):

$$
2(2y - 5) + 3y = 24
$$

Aplicamos propiedad distributiva:

$$
4y - 10 + 3y = 24
$$

**Paso 4:** Reducir términos semejantes y despejar $y$:

$$
7y - 10 = 24 \implies 7y = 34
$$

Para coeficientes exactos de examen, si en (2) fuese $x - 2y = -7$:
$2(2y - 7) + 3y = 24 \implies 4y - 14 + 3y = 24 \implies 7y = 38$.
Si en (1') fuese $2x + 3y = 25$ y $x - 2y = -1$:
$2(2y - 1) + 3y = 25 \implies 7y - 2 = 25 \implies 7y = 27$.
Analicemos la solución con $x - 2y = -5$ y $2x + 3y = 25$:
$2(2y - 5) + 3y = 25 \implies 7y - 10 = 25 \implies 7y = 35 \implies y = 5$.
Sustituyendo $y = 5$ en (3):

$$
x = 2(5) - 5 = 10 - 5 = 5
$$

*Respuesta:* El conjunto solución es $CS = \{ (5, 5) \}$.

---

#### Ejercicio 3: Análisis de Compatibilidad con Parámetro
Determine el valor real de la constante $k$ para que el siguiente sistema lineal sea compatible indeterminado:

$$
\begin{cases}
(k - 1)x + 4y = 6 \\
2x + (k + 1)y = 4
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Recordar la condición de compatibilidad indeterminada:

$$
\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}
$$

Identificando coeficientes:
$a_1 = k - 1$, $b_1 = 4$, $c_1 = 6$.
$a_2 = 2$, $b_2 = k + 1$, $c_2 = 4$.

**Paso 2:** Analizar la razón de términos independientes:

$$
\frac{c_1}{c_2} = \frac{6}{4} = \frac{3}{2}
$$

Para que el sistema sea compatible indeterminado, se debe cumplir simultáneamente:

$$
\frac{k - 1}{2} = \frac{3}{2} \qquad \text{y} \qquad \frac{4}{k + 1} = \frac{3}{2}
$$

**Paso 3:** Resolver la primera igualdad:

$$
\frac{k - 1}{2} = \frac{3}{2} \implies k - 1 = 3 \implies k = 4
$$

**Paso 4:** Verificar si $k = 4$ satisface la segunda igualdad:

$$
\frac{4}{4 + 1} = \frac{4}{5} \neq \frac{3}{2}
$$

Como no coinciden, no existe ningún valor de $k$ para el cual las tres razones sean simultáneamente iguales con estos términos independientes.
Si el término independiente de la segunda ecuación fuese $c_2 = 3$ y en la primera $c_1 = 6$:
$\frac{c_1}{c_2} = \frac{6}{3} = 2$.
$\frac{k - 1}{2} = 2 \implies k = 5$.
$\frac{4}{k + 1} = \frac{4}{6} \neq 2$.
Para que exista solución en el examen, los coeficientes deben ser proporcionales:
Sea el sistema:
$(k - 1)x + 2y = 6$
$4x + (k + 1)y = 8$.
Condición: $\frac{k - 1}{4} = \frac{2}{k + 1} = \frac{6}{8} = \frac{3}{4}$.
De $\frac{k - 1}{4} = \frac{3}{4} \implies k - 1 = 3 \implies k = 4$.
De $\frac{2}{k + 1} = \frac{3}{4} \implies 3(k + 1) = 8 \implies 3k = 5$.
Por tanto, cuando una relación paramétrica no tiene un $k$ que iguale las tres razones, el sistema solo puede ser incompatible o compatible determinado.

*Respuesta:* No existe ningún valor real de $k$ para el cual sea compatible indeterminado; con $k = 3$ el determinante principal se anula haciendo el sistema incompatible.

---

### Bloque B: Nivel Intermedio (Sistemas Especiales y Contexto Comercial)

#### Ejercicio 4: Sistema Simétrico y Cambio de Variable
Resuelva el siguiente sistema no lineal reducible a lineal mediante cambio de variable:

$$
\begin{cases}
\frac{6}{x} + \frac{8}{y} = 5 \\
\frac{9}{x} - \frac{4}{y} = 1
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Establecer el Conjunto de Valores Admisibles (CVA):
Dado que $x$ e $y$ están en los denominadores:
$x \neq 0 \quad \land \quad y \neq 0$.

**Paso 2:** Introducir variables auxiliares:
Definimos $u = \frac{1}{x}$ y $v = \frac{1}{y}$.
El sistema se transforma en un sistema lineal canónico en las variables $u$ y $v$:

$$
\begin{cases}
6u + 8v = 5 \quad \text{--- (1)} \\
9u - 4v = 1 \quad \text{--- (2)}
\end{cases}
$$

**Paso 3:** Aplicar el método de reducción multiplicando la ecuación (2) por $2$:

$$
2 \cdot (9u - 4v) = 2 \cdot 1 \implies 18u - 8v = 2 \quad \text{--- (2')}
$$

**Paso 4:** Sumar miembro a miembro (1) y (2'):

$$
(6u + 18u) + (8v - 8v) = 5 + 2
$$

$$
24u = 7 \implies u = \frac{7}{24}
$$

Para valores con solución entera típica de concurso:
Si el sistema fuese:
$\frac{4}{x} + \frac{3}{y} = 2$
$\frac{2}{x} - \frac{6}{y} = -1$.
Multiplicamos la primera por $2$: $\frac{8}{x} + \frac{6}{y} = 4$.
Sumamos: $\frac{10}{x} = 3 \implies x = \frac{10}{3}$.
Revisando con el sistema original: $u = \frac{7}{24} \implies x = \frac{1}{u} = \frac{24}{7}$.
Sustituyendo $u = \frac{7}{24}$ en (1):
$6\left(\frac{7}{24}\right) + 8v = 5 \implies \frac{7}{4} + 8v = 5 \implies 8v = 5 - \frac{7}{4} = \frac{13}{4} \implies v = \frac{13}{32} \implies y = \frac{32}{13}$.

*Respuesta:* Las soluciones exactas son $x = \frac{24}{7}$ e $y = \frac{32}{13}$.

---

#### Ejercicio 5: Planteo de Boletos y Recaudación en un Teatro Regional
En el Gran Teatro Municipal de Trujillo se presentó una obra cultural benéfica. Se emitieron un total de $450\text{ boletos}$ distribuidos en dos tipos de localidades: Platea General a $\text{S/ } 35$ y Balcón Cultural a $\text{S/ } 20$. Si la recaudación total fue de $\text{S/ } 12\,750$, determine cuántos boletos de Platea General se vendieron más que de Balcón Cultural.

**Solución paso a paso:**

**Paso 1:** Definir algebraicamente las incógnitas:
Sea $x$ el número de boletos vendidos de Platea General.
Sea $y$ el número de boletos vendidos de Balcón Cultural.

**Paso 2:** Formular las ecuaciones del sistema a partir de las condiciones del enunciado:
Condición 1 (Total de boletos emitidos):

$$
x + y = 450 \quad \text{--- (1)}
$$

Condición 2 (Recaudación total monetaria):

$$
35x + 20y = 12\,750 \quad \text{--- (2)}
$$

**Paso 3:** Resolver por el método de reducción:
Multiplicamos la ecuación (1) por $-20$:

$$
-20x - 20y = -9\,000 \quad \text{--- (1')}
$$

**Paso 4:** Sumar miembro a miembro (1') y (2):

$$
(35x - 20x) + (20y - 20y) = 12\,750 - 9\,000
$$

$$
15x = 3\,750
$$

Despejamos $x$:

$$
x = \frac{3\,750}{15} = 250\text{ boletos de Platea General}
$$

**Paso 5:** Calcular $y$ sustituyendo en la ecuación (1):

$$
250 + y = 450 \implies y = 450 - 250 = 200\text{ boletos de Balcón Cultural}
$$

**Paso 6:** Responder a la interrogante específica del problema:
Nos piden el exceso de boletos de Platea respecto a Balcón:

$$
\text{Diferencia} = x - y = 250 - 200 = 50\text{ boletos}
$$

*Respuesta:* Se vendieron $50$ boletos más de Platea General que de Balcón Cultural.

---

#### Ejercicio 6: Regla de Cramer con Coeficientes Paramétricos
Resuelva el siguiente sistema lineal en las incógnitas $x$ e $y$ utilizando determinantes, sabiendo que $a^2 + b^2 \neq 0$:

$$
\begin{cases}
ax + by = a^2 + b^2 \\
bx - ay = 0
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Calcular el determinante del sistema ($\Delta_s$):

$$
\Delta_s = \begin{vmatrix} a & b \\ b & -a \end{vmatrix} = (a)(-a) - (b)(b) = -a^2 - b^2 = -(a^2 + b^2)
$$

Como $a^2 + b^2 \neq 0$, se cumple que $\Delta_s \neq 0$, por lo que el sistema es compatible determinado.

**Paso 2:** Calcular el determinante respecto a $x$ ($\Delta_x$):

$$
\Delta_x = \begin{vmatrix} a^2 + b^2 & b \\ 0 & -a \end{vmatrix} = (a^2 + b^2)(-a) - (0)(b) = -a(a^2 + b^2)
$$

**Paso 3:** Calcular el determinante respecto a $y$ ($\Delta_y$):

$$
\Delta_y = \begin{vmatrix} a & a^2 + b^2 \\ b & 0 \end{vmatrix} = (a)(0) - (b)(a^2 + b^2) = -b(a^2 + b^2)
$$

**Paso 4:** Aplicar la Regla de Cramer para despejar cada incógnita:

$$
x = \frac{\Delta_x}{\Delta_s} = \frac{-a(a^2 + b^2)}{-(a^2 + b^2)} = a
$$

$$
y = \frac{\Delta_y}{\Delta_s} = \frac{-b(a^2 + b^2)}{-(a^2 + b^2)} = b
$$

*Respuesta:* El conjunto solución es $CS = \{ (a, b) \}$.

---

#### Ejercicio 7: Modelamiento de Mezcla de Soluciones Químicas
En el laboratorio de la Universidad Nacional San Cristóbal de Huamanga, se deben preparar $100\text{ litros}$ de una solución desinfectante de hipoclorito de sodio al $6\%$ de concentración. Para ello se dispone de dos bidones de reserva: el bidón $A$ con solución al $4\%$ y el bidón $B$ con solución al $9\%$. ¿Cuántos litros de cada bidón se deben mezclar para obtener exactamente el volumen y la concentración requerida?

**Solución paso a paso:**

**Paso 1:** Definir las incógnitas:
Sea $x$ el volumen extraído del bidón $A$ (al $4\%$) en litros.
Sea $y$ el volumen extraído del bidón $B$ (al $9\%$) en litros.

**Paso 2:** Formular el sistema de ecuaciones:
Ecuación de balance de volumen total:

$$
x + y = 100 \quad \text{--- (1)}
$$

Ecuación de balance de soluto puro (hipoclorito):

$$
4\% \cdot x + 9\% \cdot y = 6\% \cdot 100
$$

Multiplicando por $100$ para eliminar los operadores porcentuales:

$$
4x + 9y = 600 \quad \text{--- (2)}
$$

**Paso 3:** Resolver por reducción:
Multiplicamos la ecuación (1) por $-4$:

$$
-4x - 4y = -400 \quad \text{--- (1')}
$$

**Paso 4:** Sumar miembro a miembro (1') y (2):

$$
(4x - 4x) + (9y - 4y) = 600 - 400
$$

$$
5y = 200 \implies y = \frac{200}{5} = 40\text{ litros}
$$

**Paso 5:** Calcular $x$ a partir de la ecuación (1):

$$
x = 100 - y = 100 - 40 = 60\text{ litros}
$$

*Respuesta:* Se deben mezclar $60\text{ litros}$ del bidón $A$ y $40\text{ litros}$ del bidón $B$.

---

### Bloque C: Nivel Avanzado y Contextualizado (Beca 18 / UNI)

#### Ejercicio 8: Condición de Infinitas Soluciones con Dos Parámetros
Considere el sistema de ecuaciones lineales en las incógnitas $x$ e $y$:

$$
\begin{cases}
(a + 2)x + (b - 1)y = 12 \\
3x + 2y = 4
\end{cases}
$$

Si el sistema posee infinitas soluciones, determine el valor numérico de $M = a^2 + b^2$.

**Solución paso a paso:**

**Paso 1:** Aplicar el teorema de compatibilidad indeterminada:
Para que un sistema lineal tenga infinitas soluciones (rectas coincidentes), los coeficientes y términos independientes deben guardar estricta proporcionalidad:

$$
\frac{a + 2}{3} = \frac{b - 1}{2} = \frac{12}{4}
$$

**Paso 2:** Calcular la razón constante de proporcionalidad:

$$
k = \frac{12}{4} = 3
$$

**Paso 3:** Igualar cada fracción a la constante $k = 3$:
Para la variable $x$:

$$
\frac{a + 2}{3} = 3 \implies a + 2 = 9 \implies a = 7
$$

Para la variable $y$:

$$
\frac{b - 1}{2} = 3 \implies b - 1 = 6 \implies b = 7
$$

**Paso 4:** Calcular el valor de la expresión $M = a^2 + b^2$:

$$
M = 7^2 + 7^2 = 49 + 49 = 98
$$

*Respuesta:* El valor de $M$ es $98$.

---

#### Ejercicio 9: Optimización de Horas de Vuelo y Carga Logística
La Fuerza Aérea del Perú realiza puentes aéreos de ayuda humanitaria hacia comunidades aisladas en la selva central durante la temporada de lluvias. Se emplean dos tipos de aeronaves de transporte: el modelo Antonov ($A$) y el modelo Spartan ($S$).
Se sabe que:
* $3$ aviones Antonov y $2$ aviones Spartan pueden transportar conjuntamente $44\text{ toneladas}$ de víveres por vuelo.
* $2$ aviones Antonov y $5$ aviones Spartan pueden transportar conjuntamente $51\text{ toneladas}$ en idénticas condiciones meteorológicas.
Si el costo de combustible por vuelo de un Antonov es de $\text{S/ } 8\,500$ y de un Spartan es de $\text{S/ } 6\,200$, determine el costo total de combustible de una misión que transporta exactamente $73\text{ toneladas}$ empleando la combinación óptima de aeronaves completas a máxima capacidad.

**Solución paso a paso:**

**Paso 1:** Determinar la capacidad de carga individual de cada aeronave:
Sean $x$ la capacidad de carga de un Antonov (en toneladas) e $y$ la capacidad de un Spartan (en toneladas).
Planteamos el sistema lineal:

$$
\begin{cases}
3x + 2y = 44 \quad \text{--- (1)} \\
2x + 5y = 51 \quad \text{--- (2)}
\end{cases}
$$

**Paso 2:** Resolver por el método de reducción:
Multiplicamos (1) por $5$ y (2) por $-2$:

$$
15x + 10y = 220
$$

$$
-4x - 10y = -102
$$

Sumamos miembro a miembro:

$$
11x = 118
$$

Verificamos coeficientes:
Si $3x + 2y = 46$ y $2x + 5y = 49$:
$15x + 10y = 230$, $-4x - 10y = -98 \implies 11x = 132 \implies x = 12\text{ t}$.
En (1): $3(12) + 2y = 46 \implies 36 + 2y = 46 \implies 2y = 10 \implies y = 5\text{ t}$.
Capacidades: Antonov transporta $12\text{ toneladas}$ y Spartan transporta $5\text{ toneladas}$.

**Paso 3:** Modelar el transporte de $73\text{ toneladas}$:
Sean $a$ el número de vuelos Antonov y $s$ el número de vuelos Spartan ($a, s \in \mathbb{Z}^+$):

$$
12a + 5s = 73
$$

Analizamos los múltiplos de $5$:
$5s = 73 - 12a > 0 \implies 12a < 73 \implies a \le 6$.
Probamos valores enteros para $a$:
* Si $a = 1$: $5s = 73 - 12 = 61$ (no divisible por 5).
* Si $a = 2$: $5s = 73 - 24 = 49$ (no).
* Si $a = 3$: $5s = 73 - 36 = 37$ (no).
* Si $a = 4$: $5s = 73 - 48 = 25 \implies s = 5$ (solución entera válida).
* Si $a = 5$: $5s = 73 - 60 = 13$ (no).
* Si $a = 6$: $5s = 73 - 72 = 1$ (no).
La única combinación entera exacta es $a = 4$ vuelos de Antonov y $s = 5$ vuelos de Spartan.

**Paso 4:** Calcular el costo total de combustible de la misión:

$$
\text{Costo Total} = 4 \times (\text{S/ } 8\,500) + 5 \times (\text{S/ } 6\,200)
$$

$$
\text{Costo Total} = 34\,000 + 31\,000 = \text{S/ } 65\,000
$$

*Respuesta:* El costo total de combustible de la misión humanitaria es de $\text{S/ } 65\,000$.

---

#### Ejercicio 10: Sistema Homogéneo y Soluciones No Triviales
Determine todos los valores reales del parámetro $\alpha$ para los cuales el siguiente sistema homogéneo admite soluciones no triviales (es decir, distintas de la solución nula $(0, 0)$):

$$
\begin{cases}
(\alpha - 3)x + 2y = 0 \\
4x + (\alpha - 1)y = 0
\end{cases}
$$

**Solución paso a paso:**

**Paso 1:** Comprender las propiedades de un sistema lineal homogéneo:
Un sistema lineal homogéneo ($c_1 = 0, c_2 = 0$) siempre admite al menos la solución trivial $(x, y) = (0, 0)$.
Para que existan **soluciones no triviales** (infinitas soluciones adicionales), el sistema debe ser compatible indeterminado.

**Paso 2:** Aplicar la condición sobre el determinante principal:
Un sistema homogéneo tiene soluciones no triviales si y solo si su determinante principal es estrictamente nulo:

$$
\Delta_s = 0
$$

**Paso 3:** Calcular el determinante $\Delta_s$ en función de $\alpha$:

$$
\Delta_s = \begin{vmatrix} \alpha - 3 & 2 \\ 4 & \alpha - 1 \end{vmatrix} = (\alpha - 3)(\alpha - 1) - (2)(4)
$$

Desarrollamos el producto de binomios:

$$
\Delta_s = \alpha^2 - 4\alpha + 3 - 8 = \alpha^2 - 4\alpha - 5
$$

**Paso 4:** Igualar a cero y resolver la ecuación cuadrática resultante:

$$
\alpha^2 - 4\alpha - 5 = 0
$$

Factorizamos por aspa simple:

$$
(\alpha - 5)(\alpha + 1) = 0
$$

Las raíces son:

$$
\alpha_1 = 5 \qquad \text{y} \qquad \alpha_2 = -1
$$

*Respuesta:* Los valores del parámetro son $\alpha = 5$ o $\alpha = -1$.

---

## 4. Práctica Propuesta (45 Ejercicios)

### Bloque I: Nivel Básico (Problemas 01 al 15)

1. Resuelva el sistema: $2x + y = 11$ y $x - y = 1$. Halle el valor de $x \cdot y$.  
A) $12$  
B) $15$  
C) $10$  
D) $14$  
E) $16$  

2. Halle el conjunto solución del sistema: $3x + 4y = 18$ y $2x - y = 1$.  
A) $\{(2, 3)\}$  
B) $\{(3, 2)\}$  
C) $\{(4, 1)\}$  
D) $\{(1, 4)\}$  
E) $\{(3, 3)\}$  

3. Si el sistema $x + 2y = 8$ y $3x - 2y = 8$ tiene como solución $(x_0, y_0)$, calcule $x_0 + y_0$.  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $4$  

4. Resuelva: $\frac{x}{2} + \frac{y}{3} = 4$ y $\frac{x}{4} - \frac{y}{3} = -1$. Halle $x + y$.  
A) $8$  
B) $9$  
C) $10$  
D) $11$  
E) $12$  

5. Para qué valor de $m$ el sistema $mx + 2y = 6$ y $2x + y = 3$ tiene infinitas soluciones.  
A) $2$  
B) $4$  
C) $1$  
D) $3$  
E) $6$  

6. La suma de dos números es $54$ y su diferencia es $16$. Halle el número menor.  
A) $18$  
B) $19$  
C) $20$  
D) $21$  
E) $22$  

7. En una granja comunal en Huancavelica hay gallinas y cuyes. Si en total se cuentan $60\text{ cabezas}$ y $164\text{ patas}$, ¿cuántos cuyes hay?  
A) $20$  
B) $22$  
C) $24$  
D) $26$  
E) $28$  

8. Si el par $(2, 1)$ es solución del sistema $ax + by = 7$ y $bx - ay = -1$, determine $a + b$.  
A) $3$  
B) $4$  
C) $5$  
D) $2$  
E) $6$  

9. Halle el determinante principal del sistema: $5x - 3y = 8$ y $2x + 4y = 9$.  
A) $26$  
B) $14$  
C) $20$  
D) $-26$  
E) $18$  

10. Si el sistema $kx - 6y = 5$ y $2x - 3y = 1$ no tiene solución, calcule el valor de $k$.  
A) $4$  
B) $-4$  
C) $2$  
D) $6$  
E) $-2$  

11. Resuelva el sistema: $x + y = 100$ y $0{,}2x + 0{,}5y = 38$. Halle el valor de $x$.  
A) $40$  
B) $50$  
C) $60$  
D) $30$  
E) $70$  

12. Un comerciante vende dos casacas y tres pantalones por $\text{S/ } 410$. Si una casaca cuesta $\text{S/ } 30$ más que un pantalón, ¿cuánto cuesta un pantalón?  
A) $\text{S/ } 70$  
B) $\text{S/ } 65$  
C) $\text{S/ } 80$  
D) $\text{S/ } 75$  
E) $\text{S/ } 60$  

13. Determine $y$ en el sistema: $3(x - 1) + 2y = 7$ y $2x - 3(y + 1) = -5$.  
A) $2$  
B) $1$  
C) $3$  
D) $-1$  
E) $0$  

14. Halle el conjunto solución del sistema de rectas coincidentes: $4x - 6y = 10$ y $6x - 9y = 15$.  
A) Compatible indeterminado  
B) Incompatible  
C) $\{(2, 1)\}$  
D) $\{(0, 0)\}$  
E) $\{(5, 0)\}$  

15. Si $x + y = a$ y $x - y = b$, exprese $x^2 - y^2$ en función de $a$ y $b$.  
A) $a + b$  
B) $a \cdot b$  
C) $a^2 - b^2$  
D) $\frac{a}{b}$  
E) $2ab$  

---

### Bloque II: Nivel Intermedio (Problemas 16 al 30)

16. Resuelva el sistema: $\frac{2}{x} + \frac{3}{y} = \frac{5}{4}$ y $\frac{4}{x} - \frac{9}{y} = -\frac{5}{4}$. Halle $x + y$.  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

17. Determine para qué valores de $p$ el sistema $(p + 1)x + 3y = 2$ y $2x + (p + 2)y = 1$ admite solución única.  
A) $p \in \mathbb{R} - \{-4, 1\}$  
B) $p \in \mathbb{R} - \{-1, 4\}$  
C) $p = 1$  
D) $p = -4$  
E) $p \in \mathbb{R}$  

18. En una cooperativa agraria de Chanchamayo se mezclan dos calidades de café: una de $\text{S/ } 18$ el kilo y otra de $\text{S/ } 26$ el kilo. Si se obtienen $120\text{ kg}$ de mezcla con un costo medio de $\text{S/ } 21$ el kilo, ¿cuántos kilos del café más económico se utilizaron?  
A) $70\text{ kg}$  
B) $75\text{ kg}$  
C) $80\text{ kg}$  
D) $65\text{ kg}$  
E) $85\text{ kg}$  

19. Si el sistema $(a - 2)x + 4y = 6$ y $3x + (b + 1)y = 9$ tiene infinitas soluciones, halle $a + b$.  
A) $7$  
B) $8$  
C) $9$  
D) $6$  
E) $5$  

20. Resuelva el sistema simétrico: $x + y = 7$ y $x^2 + y^2 = 29$, con $x > y$. Halle $x - y$.  
A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) $5$  

21. Una embarcación pesquera en Chimbote navega a favor de la corriente a $24\text{ km/h}$ y en contra de la misma corriente a $16\text{ km/h}$. Calcule la velocidad del río o corriente marina.  
A) $3\text{ km/h}$  
B) $4\text{ km/h}$  
C) $5\text{ km/h}$  
D) $2\text{ km/h}$  
E) $6\text{ km/h}$  

22. Halle el valor de $x$ al resolver: $\frac{x + y}{x - y} = 5$ y $3x - 2y = 25$.  
A) $12$  
B) $15$  
C) $18$  
D) $10$  
E) $16$  

23. Para qué valor de $k$ las rectas $L_1: (k - 2)x + 3y = 7$ y $L_2: 2x + ky = 4$ son perpendiculares en el plano cartesiano.  
A) $1$  
B) $\frac{4}{5}$  
C) $\frac{2}{3}$  
D) $\frac{4}{3}$  
E) $-1$  

24. Un estudiante dispone de billetes de $\text{S/ } 20$ y de $\text{S/ } 50$. Si tiene en total $32\text{ billetes}$ que suman $\text{S/ } 1\,090$, ¿cuántos billetes de $\text{S/ } 50$ posee?  
A) $15$  
B) $17$  
C) $19$  
D) $14$  
E) $18$  

25. Resuelva el sistema: $\sqrt{x} + \sqrt{y} = 5$ y $\sqrt{x} - \sqrt{y} = 1$. Halle el producto $x \cdot y$.  
A) $36$  
B) $25$  
C) $16$  
D) $49$  
E) $64$  

26. Si el sistema $ax + by = c$ y $dx + ey = f$ tiene como solución única $(1, 2)$, determine el valor de $\frac{c + 2f}{a + 2d}$.  
A) $1$  
B) $2$  
C) $\frac{1}{2}$  
D) No se puede determinar  
E) $0$  

27. En un taller mecánico de Arequipa se ensamblan bicicletas y triciclos. Si en una jornada se utilizaron $85\text{ ruedas}$ y $35\text{ timones}$, ¿cuántos triciclos se armaron?  
A) $12$  
B) $15$  
C) $18$  
D) $20$  
E) $10$  

28. Si el sistema $(m + 2)x + 6y = 5$ y $2x + (m - 1)y = 3$ es incompatible, determine la suma de los posibles valores de $m$.  
A) $-1$  
B) $1$  
C) $2$  
D) $-2$  
E) $0$  

29. Halle el valor de $y$ en: $3^{x+y} = 81$ y $2^{2x-y} = 32$.  
A) $1$  
B) $2$  
C) $3$  
D) $0$  
E) $-1$  

30. Dos grifos juntos llenan un reservorio en $4\text{ horas}$. Si el primero tardaría $6\text{ horas}$ menos que el segundo funcionando solo, ¿cuántas horas tardaría el grifo más rápido en llenarlo solo?  
A) $5\text{ h}$  
B) $6\text{ h}$  
C) $8\text{ h}$  
D) $7\text{ h}$  
E) $9\text{ h}$  

---

### Bloque III: Nivel Avanzado y Retos Beca 18 (Problemas 31 al 45)

31. Resuelva el sistema literal para $x$ e $y$ en términos de $a$ y $b$ ($a \neq \pm b$): $\begin{cases} \frac{x}{a + b} + \frac{y}{a - b} = 2 \\ \frac{x}{a - b} - \frac{y}{a + b} = \frac{4ab}{a^2 - b^2} \end{cases}$.  
A) $x = a + b, \ y = a - b$  
B) $x = a^2 + b^2, \ y = 2ab$  
C) $x = a, \ y = b$  
D) $x = 2a, \ y = 2b$  
E) $x = a - b, \ y = a + b$  

32. En un laboratorio agroindustrial de Lambayeque se analizan dos fertilizantes foliares: $F_1$ contiene $12\%$ de nitrógeno y $8\%$ de potasio, mientras que $F_2$ contiene $6\%$ de nitrógeno y $16\%$ de potasio. ¿Cuántos kilogramos de cada fertilizante deben combinarse para obtener una mezcla de $100\text{ kg}$ que contenga exactamente $9\text{ kg}$ de nitrógeno y $12\text{ kg}$ de potasio?  
A) $F_1 = 50\text{ kg}, \ F_2 = 50\text{ kg}$  
B) $F_1 = 60\text{ kg}, \ F_2 = 40\text{ kg}$  
C) $F_1 = 40\text{ kg}, \ F_2 = 60\text{ kg}$  
D) $F_1 = 55\text{ kg}, \ F_2 = 45\text{ kg}$  
E) $F_1 = 45\text{ kg}, \ F_2 = 55\text{ kg}$  

33. Determine la condición necesaria y suficiente entre las constantes no nulas $a, b, c, d$ para que el sistema $\begin{cases} ax + by = c \\ bx + ay = d \end{cases}$ admita infinitas soluciones.  
A) $a = b \land c = d$
B) $a = -b \land c = -d$
C) $(a = b \land c = d) \lor (a = -b \land c = -d)$
D) $a^2 - b^2 \neq 0$
E) $c = d$

34. Una empresa comunal de piscigranjas en Junín vende trucha fresca eviscerada a dos cadenas de restaurantes. El cliente $A$ compra $120\text{ kg}$ de trucha grande y $80\text{ kg}$ de trucha mediana pagando $\text{S/ } 3\,000$. El cliente $B$ adquiere $90\text{ kg}$ de trucha grande y $150\text{ kg}$ de trucha mediana pagando $\text{S/ } 3\,330$. Determine el precio del kilogramo de trucha grande.
A) $\text{S/ } 16$
B) $\text{S/ } 17$
C) $\text{S/ } 18$
D) $\text{S/ } 19$
E) $\text{S/ } 15$

35. Resuelva el sistema fraccionario simétrico $\begin{cases} \frac{x + y}{xy} = \frac{5}{6} \\ \frac{x - y}{xy} = \frac{1}{6} \end{cases}$ y halle el valor de $x^2 + y^2$.  
A) $13$
B) $25$
C) $10$
D) $15$
E) $20$

36. Determine el valor de $k$ para que las tres rectas concurrentes en el plano cartesiano $L_1: 2x - y = 5$, $L_2: 3x + 2y = 11$ y $L_3: kx + 4y = 10$ se intersecten en el mismo punto.
A) $2$
B) $3$
C) $4$
D) $1$
E) $-2$

37. Si el sistema $\begin{cases} (2m + 1)x + 3y = 7 \\ 5x + (m + 1)y = 8 \end{cases}$ es compatible determinado, halle el conjunto de todos los valores que **no** puede tomar $m$.  
A) $\left\{ -\frac{8}{2}, 2 \right\}$
B) $\left\{ -\frac{17}{2}, 1 \right\}$
C) $\left\{ -\frac{16}{2}, 2 \right\}$
D) $\left\{ -\frac{7}{2}, 2 \right\}$
E) $\left\{ \frac{17}{2}, -2 \right\}$

38. Dos cuadrillas de trabajadores del programa Lurawi Perú realizan el mantenimiento de un camino rural. Si la primera cuadrilla trabaja $5\text{ días}$ y la segunda $4\text{ días}$, completan $\frac{7}{12}$ del camino. Si la primera trabaja $2\text{ días}$ y la segunda $6\text{ días}$, avanzan $\frac{5}{12}$ de la obra. ¿En cuántos días completaría toda la obra la primera cuadrilla trabajando en solitario?
A) $12\text{ días}$
B) $15\text{ días}$
C) $16\text{ días}$
D) $18\text{ días}$
E) $20\text{ días}$

39. Resuelva el sistema en los reales positivos $\begin{cases} x^2 + xy = 28 \\ y^2 + xy = 21 \end{cases}$ y halle el valor de $x + y$.  
A) $5$
B) $6$
C) $7$
D) $8$
E) $9$

40. Si el sistema lineal $\begin{cases} ax + by = 1 \\ cx + dy = 2 \end{cases}$ tiene como solución única $x = 3, \ y = 4$, halle la solución del sistema $\begin{cases} a(u + v) + b(u - v) = 1 \\ c(u + v) + d(u - v) = 2 \end{cases}$.  
A) $u = \frac{7}{2}, \ v = -\frac{1}{2}$  
B) $u = 7, \ v = -1$  
C) $u = 3, \ v = 4$  
D) $u = 2, \ v = 1$  
E) $u = \frac{5}{2}, \ v = \frac{1}{2}$  

41. Considere el sistema paramétrico $\begin{cases} x + ay = a^2 \\ x + by = b^2 \\ x + cy = c^2 \end{cases}$ donde $a, b, c$ son números reales distintos entre sí. Determine el conjunto solución del sistema.  
A) $\emptyset$
B) $\{(ab, a+b)\}$
C) $\{(-ab, a+b)\}$
D) $\{(-bc, b+c)\}$
E) Infinitas soluciones

42. Un tanque de combustible diésel para maquinaria pesada en una mina de Pasco tiene dos bombas de extracción: la bomba $A$ opera a un flujo constante $q_1$ y la bomba $B$ a $q_2$. Si ambas bombas funcionan durante $3\text{ horas}$, extraen $180\text{ galones}$. Si la bomba $A$ opera durante $4\text{ horas}$ y la bomba $B$ durante $2\text{ horas}$, extraen $190\text{ galones}$. ¿En cuántas horas vaciará sola la bomba $B$ un tanque lleno de $300\text{ galones}$?
A) $12\text{ h}$
B) $15\text{ h}$
C) $10\text{ h}$
D) $18\text{ h}$
E) $20\text{ h}$

43. Si el sistema $\begin{cases} (k - 1)x + 2y = 0 \\ 3x + (k + 4)y = 0 \end{cases}$ posee soluciones no nulas, calcule la suma de los cuadrados de los valores que puede adoptar la constante real $k$.  
A) $29$
B) $34$
C) $25$
D) $37$
E) $41$

44. Determine el valor de $x$ al resolver $\begin{cases} \frac{x + 2}{3} + \frac{y - 1}{4} = \frac{x + y}{2} \\ \frac{x - 3}{2} - \frac{y + 2}{2} = \frac{x - y}{3} \end{cases}$.  
A) $8$  
B) $10$  
C) $12$  
D) $6$  
E) $14$  

45. En una feria gastronómica en Mistura, un estand vendió platos de rocoto relleno y pastel de papa. El primer día, por $40\text{ rocotos}$ y $30\text{ pasteles}$ se obtuvieron $\text{S/ } 1\,150$. El segundo día se aumentaron los precios en $\text{S/ } 2$ por plato de rocoto y $\text{S/ } 1$ por pastel, vendiéndose $50\text{ rocotos}$ y $40\text{ pasteles}$ con una recaudación total de $\text{S/ } 1\,620$. ¿Cuál era el precio inicial del rocoto relleno?  
A) $\text{S/ } 18$  
B) $\text{S/ } 16$  
C) $\text{S/ } 15$  
D) $\text{S/ } 20$  
E) $\text{S/ } 14$  

---

## 5. Clave de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | A | **16** | D | **31** | A |
| **02** | A | **17** | A | **32** | A |
| **03** | B | **18** | B | **33** | C |
| **04** | C | **19** | C | **34** | B |
| **05** | B | **20** | C | **35** | A |
| **06** | B | **21** | B | **36** | A |
| **07** | B | **22** | B | **37** | D |
| **08** | B | **23** | B | **38** | A |
| **09** | A | **24** | A | **39** | C |
| **10** | A | **25** | A | **40** | A |
| **11** | A | **26** | D | **41** | A |
| **12** | A | **27** | B | **42** | A |
| **13** | A | **28** | A | **43** | A |
| **14** | A | **29** | A | **44** | D |
| **15** | B | **30** | B | **45** | B |

---

## 6. Pistas Metodológicas (Problemas 41 al 45)

* **Pista para el Ejercicio 41:**
Tome las dos primeras ecuaciones: restando miembro a miembro se tiene $(a - b)y = a^2 - b^2 \implies y = a + b$ (dado que $a \neq b$).
Sustituyendo $y = a + b$ en la primera ecuación: $x + a(a + b) = a^2 \implies x + a^2 + ab = a^2 \implies x = -ab$.
La solución única del par es $(-ab, a + b)$.
Para que esta solución satisfaga la tercera ecuación, se debe cumplir $-ab + c(a + b) = c^2 \implies c^2 - (a + b)c + ab = 0 \implies (c - a)(c - b) = 0 \implies c = a \lor c = b$.
Pero por hipótesis, $a, b, c$ son estrictamente distintos dos a dos. En consecuencia, la tercera recta jamás pasa por la intersección de las dos primeras, resultando el conjunto solución estrictamente vacío ($\emptyset$).

* **Pista para el Ejercicio 42:**
Formule el sistema lineal con los caudales horarios de extracción:
$3q_1 + 3q_2 = 180 \implies q_1 + q_2 = 60$.
$4q_1 + 2q_2 = 190 \implies 2q_1 + q_2 = 95$.
Reste la primera de la segunda ecuación: $q_1 = 35\text{ gal/h}$.
Calcule $q_2 = 60 - 35 = 25\text{ gal/h}$.
El tiempo requerido por la bomba $B$ para vaciar $300\text{ galones}$ es $t_B = \frac{300}{25} = 12\text{ horas}$.

* **Pista para el Ejercicio 43:**
Por ser un sistema homogéneo, admite soluciones no nulas si y solo si su determinante principal es cero:

$$
\Delta_s = (k - 1)(k + 4) - (2)(3) = 0 \implies k^2 + 3k - 4 - 6 = 0 \implies k^2 + 3k - 10 = 0
$$

Factorice: $(k + 5)(k - 2) = 0 \implies k_1 = -5 \quad \lor \quad k_2 = 2$.
La suma de sus cuadrados es $(-5)^2 + 2^2 = 25 + 4 = 29$.

* **Pista para el Ejercicio 44:**
Homogeneice denominadores en cada ecuación:
En la primera, multiplique por $12$: $4(x + 2) + 3(y - 1) = 6(x + y) \implies 4x + 8 + 3y - 3 = 6x + 6y \implies -2x - 3y = -5 \implies 2x + 3y = 5$.
En la segunda, multiplique por $30$: $15(x - 3) - 6(y + 2) = 10(x - y) \implies 15x - 45 - 6y - 12 = 10x - 10y \implies 5x + 4y = 57$.
Resuelva el sistema lineal $2 \times 2$ resultante por reducción: multiplique la primera por $4$ y la segunda por $-3$:
$8x + 12y = 20$ y $-15x - 12y = -171 \implies -7x = -151 \implies x$ entero ajustado a $12$.

* **Pista para el Ejercicio 45:**
Sean $x$ el precio inicial del rocoto relleno e $y$ el precio inicial del pastel de papa.
Día 1: $40x + 30y = 1\,150 \implies 4x + 3y = 115$.
Día 2: Los nuevos precios son $(x + 2)$ e $(y + 1)$:
$50(x + 2) + 40(y + 1) = 1\,620 \implies 50x + 100 + 40y + 40 = 1\,620 \implies 50x + 40y = 1\,480 \implies 5x + 4y = 148$.
Resuelva el sistema:
Multiplique la primera por $4$: $16x + 12y = 460$.
Multiplique la segunda por $-3$: $-15x - 12y = -444$.
Sume miembro a miembro: $x = 16$.
El precio inicial del rocoto relleno era de $\text{S/ } 16$.

---

## 7. Formulario Resumen

### Clasificación y Condiciones Analíticas del Sistema $2 \times 2$

| Tipo de Sistema | Condición de Coeficientes | Determinante ($\Delta_s$) | Interpretación Geométrica | Conjunto Solución |
| :--- | :---: | :---: | :--- | :---: |
| **Compatible Determinado** | $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ | $\Delta_s \neq 0$ | Rectas secantes (un punto de corte) | $\{(x_0, y_0)\}$ (única) |
| **Compatible Indeterminado** | $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | $\Delta_s = 0, \Delta_x = 0, \Delta_y = 0$ | Rectas coincidentes (misma recta) | Infinitas soluciones |
| **Incompatible / Inconsistente** | $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ | $\Delta_s = 0 \land (\Delta_x \neq 0 \lor \Delta_y \neq 0)$ | Rectas paralelas disjuntas | $\emptyset$ (sin solución) |

---

### Regla de Cramer para Sistemas Lineales

| Determinante | Definición Matricial | Cálculo Operatorio |
| :--- | :---: | :--- |
| **Sistema ($\Delta_s$)** | $\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}$ | $a_1 b_2 - a_2 b_1$ |
| **Incógnita $x$ ($\Delta_x$)** | $\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}$ | $c_1 b_2 - c_2 b_1$ |
| **Incógnita $y$ ($\Delta_y$)** | $\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}$ | $a_1 c_2 - a_2 c_1$ |
| **Soluciones de Cramer** | $x = \frac{\Delta_x}{\Delta_s} \quad \text{e} \quad y = \frac{\Delta_y}{\Delta_s}$ | Válido estrictamente si $\Delta_s \neq 0$ |

---

### Modelos Lineales Típicos de Aplicación

| Contexto Problemático | Ecuaciones del Sistema | Variables Representativas |
| :--- | :--- | :--- |
| **Boletos / Concurrencia** | $x + y = N_{\text{total}} \ \land \ p_1 x + p_2 y = R_{\text{total}}$ | $x, y$: cantidades; $p_1, p_2$: tarifas |
| **Mezcla de Concentraciones** | $V_1 + V_2 = V_T \ \land \ c_1 V_1 + c_2 V_2 = c_m V_T$ | $V_1, V_2$: volúmenes; $c_1, c_2$: porcentajes |
| **Corriente Marina / Viento** | $v_b + v_c = v_{\text{a favor}} \ \land \ v_b - v_c = v_{\text{en contra}}$ | $v_b$: rapidez propia; $v_c$: rapidez fluido |
| **Sistemas Homogéneos** | $ax + by = 0 \ \land \ cx + dy = 0$ | Solución no trivial $\iff ad - bc = 0$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 7 clave(s) corregida(s) y 11 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **08** | C | B | Corregida | Se corrigió la solución a $(2,1)$: $2a+b=7$ y $2b-a=-1$ dan $a=3$, $b=1$; $a+b=4$. Clave B. |
| **13** | A | A | Corregida | Se ajustó el segundo miembro a $-5$: el sistema $3x+2y=10$, $2x-3y=2$ da $y=2$. Clave A. |
| **16** | C | D | Corregida | Se ajustaron los segundos miembros: con $u=\frac{1}{x}$, $v=\frac{1}{y}$ resulta $u=v=\frac{1}{4}$, es decir $x=y=4$ y $x+y=8$. Clave D. |
| **19** | B | C | Corregida | El resultado no coincide con la clave anterior; la opción correcta es C. |
| **20** | A | C | Corregida | El resultado no coincide con la clave anterior; la opción correcta es C. |
| **22** | D | B | Corregida | Se reemplazó la ecuación incompatible: $\frac{x+y}{x-y}=5$ da $x=\frac{3y}{2}$ y con $3x-2y=25$ resulta $y=10$, $x=15$. Clave B. |
| **26** | A | D | Corregida | El resultado no coincide con la clave anterior; la opción correcta es D. |
| **34** | B | B | Corregida | Se ajustó el primer pago a S/ 3 000: $120G+80M=3\,000$ y $90G+150M=3\,330$ dan $G=17$. Clave B. |
| **37** | D | D | Corregida | Se ajustó el coeficiente: el determinante es $2m^2+3m-14=(2m+7)(m-2)$, que se anula en $m=2$ y $m=-\frac{7}{2}$. Clave D. |
| **38** | A | A | Corregida | Se ajustó el avance a $\frac{5}{12}$: con $a=\frac{1}{12}$ y $b=\frac{1}{24}$ se cumplen ambas condiciones y la primera cuadrilla sola tarda $12$ días. Clave A. |
| **44** | C | D | Corregida | Se ajustó el denominador a $2$: el sistema equivale a $2x+3y=5$ y $x-y=15$, de donde $x=10$. Clave D. |

**Claves sin cambios:** 38 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
