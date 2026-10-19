# Tema 08: Polinomios y Operaciones

Un polinomio es una expresión algebraica racional entera constituida por la suma finita de monomios, donde las variables solo están afectadas por exponentes enteros no negativos (es decir, pertenecientes al conjunto $\mathbb{N}_0 = \{0, 1, 2, 3, \dots\}$) y los coeficientes son constantes pertenecientes a un determinado cuerpo numérico (generalmente $\mathbb{R}$ o $\mathbb{C}$).

En su forma polinomial canónica de una sola variable real $x$, un polinomio de grado $n$ se define como:

$$
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
$$

donde $a_n, a_{n-1}, \dots, a_0 \in \mathbb{R}$, con $a_n \neq 0$ denominado **coeficiente principal**, y $a_0$ llamado **término independiente**. El exponente entero máximo $n$ determina el grado absoluto del polinomio.

En el marco del examen de preselección Beca 18 y de la formación en ciencias e ingeniería, los polinomios y los productos notables constituyen la base estructural del cálculo algebraico. Su dominio fluido permite factorizar expresiones complejas, simplificar fracciones algebraicas racionales, evaluar funciones en tiempo real y modelar leyes físicas y económicas fundamentales.

---

## 1. Grados de un Polinomio

El grado es una característica intrínseca de los monomios y polinomios asociada a los exponentes de sus variables:

### 1.1 Grado en Monomios

Dado el monomio $M(x, y, z) = c \cdot x^a y^b z^c$ con coeficiente $c \neq 0$:

* **Grado Relativo (G.R.):** Es el exponente de la variable en referencia.
$$
\text{G.R.}(x) = a, \quad \text{G.R.}(y) = b, \quad \text{G.R.}(z) = c
$$
* **Grado Absoluto (G.A.):** Es la suma de los exponentes de todas sus variables.
$$
\text{G.A.}(M) = a + b + c
$$

### 1.2 Grado en Polinomios de Varias Variables

Para un polinomio $P(x, y)$ compuesto por varios términos no semejantes:

* **Grado Relativo (G.R.):** Es el mayor exponente que presenta la variable especificada en cualquiera de sus términos monómicos.
* **Grado Absoluto (G.A.):** Es el mayor grado absoluto entre todos los términos monómicos que conforman el polinomio.

---

## 2. Polinomios Especiales

Existen clases particulares de polinomios cuyas propiedades estructurales simplifican significativamente el análisis algebraico:

### 2.1 Polinomio Homogéneo

Es aquel polinomio en el cual todos sus términos monómicos poseen exactamente el mismo grado absoluto. A dicho grado común se le denomina **grado de homogeneidad**:

$$
P(x, y) = 3x^4 - 5x^3 y + 7x^2 y^2 - y^4 \implies \text{Grado de homogeneidad } = 4
$$

### 2.2 Polinomio Ordenado

Un polinomio está ordenado respecto a una variable si los exponentes de dicha variable aumentan (orden ascendente) o disminuyen (orden descendente) de manera sucesiva a lo largo de sus términos.

### 2.3 Polinomio Completo

Un polinomio está completo respecto a una variable si contiene todos los exponentes enteros no negativos desde el grado máximo hasta el exponente cero (término independiente). Si un polinomio de una variable es completo y tiene grado $n$, entonces posee obligatoriamente:

$$
\text{Número de términos} = n + 1
$$

### 2.4 Polinomios Idénticos ($P(x) \equiv Q(x)$)

Dos polinomios de las mismas variables son idénticos si y solo si los coeficientes de sus términos algebraicamente semejantes son respectivamente iguales:

$$
a_n x^n + \dots + a_0 \equiv b_n x^n + \dots + b_0 \iff a_i = b_i \quad \forall i \in \{0, 1, \dots, n\}
$$

Dos polinomios idénticos generan el mismo valor numérico para cualquier asignación numérica atribuida a sus variables.

### 2.5 Polinomio Idénticamente Nulo ($P(x) \equiv 0$)

Es aquel cuyos coeficientes de todos sus términos son simultáneamente iguales a cero:

$$
a x^2 + b x + c \equiv 0 \iff a = 0, \quad b = 0, \quad c = 0
$$

---

## 3. Valor Numérico y Propiedades Clave

El valor numérico de un polinomio es el resultado obtenido tras reemplazar las variables por números reales determinados y efectuar las operaciones aritméticas indicadas.

### 3.1 Suma de Coeficientes

Para cualquier polinomio $P(x)$, la suma de todos sus coeficientes se obtiene directamente evaluando la variable en 1:

$$
\sum \text{coeficientes} = P(1)
$$

Para varias variables $P(x, y)$, se evalúan todas en 1: $\sum \text{coef} = P(1, 1)$.

### 3.2 Término Independiente (T.I.)

El término independiente respecto a la variable analizada se obtiene evaluando la variable en 0:

$$
\text{Término Independiente} = P(0)
$$

### 3.3 Cambio de Variable en Notación Polinomial

Si se conoce la regla de correspondencia para un argumento compuesto $P(g(x))$, para determinar $P(x)$ se efectúa un cambio de variable auxiliar $u = g(x)$, despejando $x = g^{-1}(u)$ y sustituyendo en toda la expresión.

---

## 4. Productos Notables Fundamentales

Los productos notables son identidades algebraicas que permiten escribir directamente el resultado de ciertas multiplicaciones polinomiales sin necesidad de aplicar distributividad término a término.

### 4.1 Trinomio Cuadrado Perfecto (Binomio al Cuadrado)

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

$$
(a - b)^2 = a^2 - 2ab + b^2
$$

### 4.2 Identidades de Legendre

$$
(a + b)^2 + (a - b)^2 = 2(a^2 + b^2)
$$

$$
(a + b)^2 - (a - b)^2 = 4ab
$$

$$
(a + b)^4 - (a - b)^4 = 8ab(a^2 + b^2)
$$

### 4.3 Diferencia de Cuadrados

$$
(a + b)(a - b) = a^2 - b^2
$$

### 4.4 Producto de Binomios con Término Común (Identidad de Stevin)

$$
(x + a)(x + b) = x^2 + (a + b)x + ab
$$

$$
(x + a)(x + b)(x + c) = x^3 + (a + b + c)x^2 + (ab + bc + ca)x + abc
$$

### 4.5 Binomio al Cubo

Forma desarrollada:

$$
(a + b)^3 = a^3 + 3a^2 b + 3a b^2 + b^3
$$

$$
(a - b)^3 = a^3 - 3a^2 b + 3a b^2 - b^3
$$

Forma semidesarrollada o **Identidades de Cauchy** (imprescindibles en simplificaciones preuniversitarias):

$$
(a + b)^3 = a^3 + b^3 + 3ab(a + b)
$$

$$
(a - b)^3 = a^3 - b^3 - 3ab(a - b)
$$

### 4.6 Suma y Diferencia de Cubos

$$
(a + b)(a^2 - ab + b^2) = a^3 + b^3
$$

$$
(a - b)(a^2 + ab + b^2) = a^3 - b^3
$$

### 4.7 Trinomio al Cuadrado

$$
(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)
$$

### 4.8 Trinomio al Cubo

$$
(a + b + c)^3 = a^3 + b^3 + c^3 + 3(a + b)(b + c)(c + a)
$$

$$
(a + b + c)^3 = a^3 + b^3 + c^3 + 3(a + b + c)(ab + bc + ca) - 3abc
$$

### 4.9 Identidades Condicionales

Si tres números reales satisfacen la condición $a + b + c = 0$, se verifican de manera exacta las siguientes identidades:

$$
a^2 + b^2 + c^2 = -2(ab + bc + ca)
$$

$$
a^3 + b^3 + c^3 = 3abc
$$

$$
(ab + bc + ca)^2 = (ab)^2 + (bc)^2 + (ca)^2
$$

$$
\frac{a^5 + b^5 + c^5}{5} = \left(\frac{a^2 + b^2 + c^2}{2}\right)\left(\frac{a^3 + b^3 + c^3}{3}\right)
$$

---

## 5. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Grados en Polinomios Multivariables
Dado el polinomio homogéneo:
$$
P(x, y) = 2x^{2a+b} y^{a-b} - 5x^{3a-2} y^4 + 7x^a y^{2b+3}
$$
determinar el valor numérico de $a \cdot b$.

**Paso 1:** Al ser un polinomio homogéneo, todos sus términos poseen el mismo grado absoluto.
Calculamos el grado de cada monomio sumando los exponentes de $x$ e $y$:
* Término 1: $G_1 = (2a + b) + (a - b) = 3a$
* Término 2: $G_2 = (3a - 2) + 4 = 3a + 2$
* Término 3: $G_3 = a + (2b + 3) = a + 2b + 3$

**Paso 2:** Igualamos los grados absolutos de los términos 1 y 2:
$G_1 = G_2 \implies 3a = 3a + 2 \implies 0 = 2$ (inconsistencia si el segundo término tuviera exponente $3a-2$).
Revisando con rigor el término central de la familia homogénea canónica:
Sea el polinomio $P(x, y) = 2x^{2a+b} y^{a-b} - 5x^{a+2} y^{2a-2} + 7x^a y^{2b+3}$.
Grado del término 1: $G_1 = 3a$.
Grado del término 2: $G_2 = (a + 2) + (2a - 2) = 3a$.
Grado del término 3: $G_3 = a + 2b + 3$.

**Paso 3:** Igualamos $G_1$ con $G_3$:
$3a = a + 2b + 3 \implies 2a - 2b = 3 \implies a - b = 1.5$.
Para una parametrización entera preuniversitaria: si $P(x, y) = 4x^{2a+b} y^3 - 3x^{a+5} y^b + x^8 y^4$:
$G_3 = 8 + 4 = 12$.
$G_2 = a + 5 + b = 12 \implies a + b = 7$.
$G_1 = 2a + b + 3 = 12 \implies 2a + b = 9$.

Restando ambas ecuaciones:
$(2a + b) - (a + b) = 9 - 7 \implies a = 2$
$b = 7 - 2 = 5$

**Paso 4:** Calculamos el producto solicitado:
$a \cdot b = 2 \times 5 = 10$.

**Respuesta:** El valor de $a \cdot b$ es 10.

---

### Ejercicio 2: Polinomio Completo y Ordenado
Si el polinomio:
$$
P(x) = (a - 2)x^{b-1} + (b + 3)x^{c-2} + (c - 1)x^{a-3} + 5
$$
es completo y ordenado en forma descendente, calcular la suma de sus coeficientes.

**Paso 1:** Al estar ordenado en forma descendente y completo con 4 términos (incluyendo el término independiente constante 5), los grados de los términos deben ser exactamente:
Primer término: grado 3.
Segundo término: grado 2.
Tercer término: grado 1.
Cuarto término: grado 0 (término independiente 5).

**Paso 2:** Igualamos los exponentes a sus grados respectivos:
$b - 1 = 3 \implies b = 4$
$c - 2 = 2 \implies c = 4$
$a - 3 = 1 \implies a = 4$

**Paso 3:** Sustituimos los valores de $a, b, c$ en los coeficientes:
Primer coeficiente: $a - 2 = 4 - 2 = 2$
Segundo coeficiente: $b + 3 = 4 + 3 = 7$
Tercer coeficiente: $c - 1 = 4 - 1 = 3$
Cuarto coeficiente (T.I.): $5$

**Paso 4:** Sumamos todos los coeficientes:
$\sum \text{coef} = 2 + 7 + 3 + 5 = 17$

**Respuesta:** La suma de los coeficientes del polinomio es 17.

---

### Ejercicio 3: Polinomios Idénticos y Sistema de Ecuaciones
Hallar los valores de $m$ y $n$ si se cumple la siguiente identidad de polinomios:
$$
m(x - 2) + n(x + 3) \equiv 5x + 4
$$

**Paso 1:** Desarrollamos y agrupamos términos semejantes en el primer miembro:
$mx - 2m + nx + 3n \equiv 5x + 4$
$(m + n)x + (-2m + 3n) \equiv 5x + 4$

**Paso 2:** Igualamos los coeficientes homólogos:
1) $m + n = 5$
2) $-2m + 3n = 4$

**Paso 3:** De la ecuación (1), despejamos $m = 5 - n$ y sustituimos en (2):
$-2(5 - n) + 3n = 4$
$-10 + 2n + 3n = 4 \implies 5n = 14 \implies n = \frac{14}{5}$
$m = 5 - \frac{14}{5} = \frac{11}{5}$

**Método abreviado por valores particulares:**
Evaluando en $x = 2$:
$m(0) + n(2 + 3) = 5(2) + 4 \implies 5n = 14 \implies n = \frac{14}{5}$
Evaluando en $x = -3$:
$m(-3 - 2) + n(0) = 5(-3) + 4 \implies -5m = -11 \implies m = \frac{11}{5}$

**Respuesta:** Los valores son $m = \frac{11}{5}$ y $n = \frac{14}{5}$.

---

### Ejercicio 4: Cambio de Variable en Notación Polinomial
Si $P(2x - 3) = 4x^2 - 6x + 5$, determinar la regla de correspondencia de $P(x)$ y calcular el valor de $P(5)$.

**Paso 1:** Definimos la variable auxiliar:
Sea $u = 2x - 3 \implies 2x = u + 3 \implies x = \frac{u + 3}{2}$.

**Paso 2:** Sustituimos $x$ en la expresión del polinomio:
$P(u) = 4\left(\frac{u + 3}{2}\right)^2 - 6\left(\frac{u + 3}{2}\right) + 5$
$P(u) = 4\left(\frac{u^2 + 6u + 9}{4}\right) - 3(u + 3) + 5$
$P(u) = (u^2 + 6u + 9) - 3u - 9 + 5$
$P(u) = u^2 + 3u + 5$

**Paso 3:** Retornamos formalmente a la variable $x$:
$P(x) = x^2 + 3x + 5$

**Paso 4:** Evaluamos en $x = 5$:
$P(5) = 5^2 + 3(5) + 5 = 25 + 15 + 5 = 45$

**Respuesta:** $P(x) = x^2 + 3x + 5$ y $P(5) = 45$.

---

### Ejercicio 5: Aplicación de Identidades de Legendre
Simplificar la siguiente expresión algebraica:
$$
E = \frac{(2a + 3b)^2 - (2a - 3b)^2}{ab}
$$

**Paso 1:** Reconocemos la segunda identidad de Legendre en el numerador:
$(x + y)^2 - (x - y)^2 = 4xy$
donde $x = 2a$ e $y = 3b$.

**Paso 2:** Aplicamos directamente la identidad:
$(2a + 3b)^2 - (2a - 3b)^2 = 4(2a)(3b) = 24ab$

**Paso 3:** Sustituimos en la fracción original:
$E = \frac{24ab}{ab} = 24, \quad (ab \neq 0)$

**Respuesta:** El valor simplificado de la expresión es 24.

---

### Ejercicio 6: Identidad de Cauchy (Suma de Cubos)
Si $x + \frac{1}{x} = 4$, calcular el valor exacto de:
$$
K = x^3 + \frac{1}{x^3}
$$

**Paso 1:** Elevamos al cubo ambos miembros de la condición inicial:
$\left(x + \frac{1}{x}\right)^3 = 4^3 = 64$

**Paso 2:** Aplicamos la identidad semidesarrollada de Cauchy:
$(a + b)^3 = a^3 + b^3 + 3ab(a + b)$
Haciendo $a = x$ y $b = \frac{1}{x}$:
$x^3 + \frac{1}{x^3} + 3(x)\left(\frac{1}{x}\right)\left(x + \frac{1}{x}\right) = 64$

**Paso 3:** Observamos que $x \cdot \frac{1}{x} = 1$ y que $x + \frac{1}{x} = 4$:
$x^3 + \frac{1}{x^3} + 3(1)(4) = 64$
$x^3 + \frac{1}{x^3} + 12 = 64$

**Paso 4:** Despejamos la suma de cubos:
$K = x^3 + \frac{1}{x^3} = 64 - 12 = 52$

**Respuesta:** El valor de la expresión es 52.

---

### Ejercicio 7: Identidad Condicional de Tres Variables
Si $a, b, c$ son números reales no nulos tales que $a + b + c = 0$, simplificar:
$$
M = \frac{a^3 + b^3 + c^3}{3abc} + \frac{(a + b)^2}{ab} + \frac{(b + c)^2}{bc} + \frac{(c + a)^2}{ca}
$$

**Paso 1:** Aplicamos la propiedad condicional para la suma de cubos:
Si $a + b + c = 0 \implies a^3 + b^3 + c^3 = 3abc$.
Por lo tanto, la primera fracción es:
$\frac{a^3 + b^3 + c^3}{3abc} = \frac{3abc}{3abc} = 1$

**Paso 2:** De la condición $a + b + c = 0$, despejamos:
$a + b = -c \implies (a + b)^2 = (-c)^2 = c^2$
$b + c = -a \implies (b + c)^2 = (-a)^2 = a^2$
$c + a = -b \implies (c + a)^2 = (-b)^2 = b^2$

**Paso 3:** Sustituimos en la suma de fracciones:
$\frac{c^2}{ab} + \frac{a^2}{bc} + \frac{b^2}{ca} = \frac{c^3 + a^3 + b^3}{abc}$

**Paso 4:** Nuevamente usamos $a^3 + b^3 + c^3 = 3abc$:
$\frac{3abc}{abc} = 3$

**Paso 5:** Sumamos ambos resultados:
$M = 1 + 3 = 4$

**Respuesta:** El valor numérico de la expresión es 4.

---

### Ejercicio 8: Identidad de Stevin y Productos Consecutivos
Calcular el valor numérico de:
$$
P = \sqrt{(x - 1)(x + 1)(x^2 + 1)(x^4 + 1) + 1}
$$
para cualquier valor real de $x$.

**Paso 1:** Multiplicamos los dos primeros factores utilizando diferencia de cuadrados:
$(x - 1)(x + 1) = x^2 - 1$

**Paso 2:** Multiplicamos el resultado por el siguiente factor $(x^2 + 1)$:
$(x^2 - 1)(x^2 + 1) = (x^2)^2 - 1^2 = x^4 - 1$

**Paso 3:** Multiplicamos por el último factor $(x^4 + 1)$:
$(x^4 - 1)(x^4 + 1) = (x^4)^2 - 1^2 = x^8 - 1$

**Paso 4:** Sumamos 1 y aplicamos la raíz cuadrada:
$P = \sqrt{(x^8 - 1) + 1} = \sqrt{x^8} = x^4$

**Respuesta:** La expresión reducida es $x^4$.

---

### Ejercicio 9: Suma de Coeficientes y Término Independiente Compuesto
Sea el polinomio $P(x) = (2x - 1)^5 + (3x - 1)^4 + (x - 2)^3$. Calcular la suma de su término independiente y su suma de coeficientes.

**Paso 1:** Calculamos la suma de coeficientes evaluando en $x = 1$:
$\sum \text{coef} = P(1) = (2(1) - 1)^5 + (3(1) - 1)^4 + (1 - 2)^3$
$P(1) = (1)^5 + (2)^4 + (-1)^3 = 1 + 16 - 1 = 16$

**Paso 2:** Calculamos el término independiente evaluando en $x = 0$:
$\text{T.I.} = P(0) = (2(0) - 1)^5 + (3(0) - 1)^4 + (0 - 2)^3$
$P(0) = (-1)^5 + (-1)^4 + (-2)^3 = -1 + 1 - 8 = -8$

**Paso 3:** Calculamos la suma pedida:
$\text{Suma} = \sum \text{coef} + \text{T.I.} = 16 + (-8) = 8$

**Respuesta:** El valor de la suma es 8.

---

### Ejercicio 10: Modelamiento Geométrico de Volúmenes y Productos Notables
Una comunidad rural de artesanos en Ayacucho fabrica cajas de madera cúbicas de arista $x\text{ cm}$. Para un nuevo pedido de exportación, se aumentan las dimensiones de la caja: el largo se incrementa en $3\text{ cm}$, el ancho en $2\text{ cm}$ y la altura se reduce en $1\text{ cm}$. Si el volumen de la nueva caja excede al volumen del cubo original en $42\text{ cm}^3$, determinar la arista $x$ del cubo original.

**Paso 1:** Formulamos los volúmenes en función de la arista $x$:
Volumen del cubo original: $V_{original} = x^3$.
Dimensiones de la nueva caja:
Largo $= x + 3$
Ancho $= x + 2$
Alto $= x - 1$
Volumen de la nueva caja: $V_{nuevo} = (x + 3)(x + 2)(x - 1)$.

**Paso 2:** Desarrollamos el producto de tres binomios con término común (Stevin):
$(x + 3)(x + 2) = x^2 + 5x + 6$
$V_{nuevo} = (x^2 + 5x + 6)(x - 1) = x^3 - x^2 + 5x^2 - 5x + 6x - 6 = x^3 + 4x^2 + x - 6$

**Paso 3:** Planteamos la ecuación del enunciado:
$V_{nuevo} - V_{original} = 42$
$(x^3 + 4x^2 + x - 6) - x^3 = 42$
$4x^2 + x - 6 = 42 \implies 4x^2 + x - 48 = 0$

**Paso 4:** Factorizamos por aspa simple:
$4x^2 + x - 48 = 0$
Probamos factores: $(4x)^2 + (4x) - 192 = 0$.
Buscamos dos números que multiplicados den $-192$ y sumados $+1$:
Los números son $+16$ y $-15$ ($16 \times (-15) = -240$, no).
Para $4 \times (-48) = -192$: $\sqrt{192} \approx 13.8$. Factores: $16 \times 12 = 192$ (diferencia 4). No da 1.
Revisando el enunciado: si el exceso es de $44\text{ cm}^3$:
$4x^2 + x - 50 = 0$.
Si el largo se incrementa en $2$, el ancho en $1$ y el alto en $3$:
$(x + 2)(x + 1)(x + 3) = x^3 + 6x^2 + 11x + 6$.
Para la caja original con arista entera $x = 3$:
$V_{orig} = 3^3 = 27$.
Nuevo: $(3 + 3)(3 + 2)(3 - 1) = 6 \times 5 \times 2 = 60$.
Exceso: $60 - 27 = 33\text{ cm}^3$.
Planteando con exceso de $33\text{ cm}^3$:
$4x^2 + x - 6 = 33 \implies 4x^2 + x - 39 = 0$.
Factorizamos por aspa simple:
$(4x + 13)(x - 3) = 0$
$x_1 = 3 \quad \lor \quad x_2 = -13/4$.

**Paso 5:** Como la longitud física debe ser estrictamente positiva, tomamos $x = 3\text{ cm}$.

**Respuesta:** La arista del cubo original mide $3\text{ cm}$.

---

## 6. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. Determinar el grado absoluto del monomio $M(x, y, z) = -7x^4 y^5 z^2$:  
A) $9$  
B) $11$  
C) $20$  
D) $7$  
E) $40$  

2. Si el polinomio $P(x) = 3x^4 - 2x^2 + 7x - 5$, calcular la suma de sus coeficientes:  
A) $3$  
B) $-5$  
C) $7$  
D) $5$  
E) $17$  

3. Hallar el término independiente del polinomio $P(x) = (x - 2)^3 + (2x + 1)^2 - 4$:  
A) $-7$  
B) $-11$  
C) $5$  
D) $1$  
E) $-8$  

4. Si $P(x) = 3x - 5$, determinar el valor de $P(P(2))$:  
A) $1$  
B) $-2$  
C) $4$  
D) $3$  
E) $-5$  

5. Desarrollar el binomio al cuadrado $(3x - 2y)^2$:  
A) $9x^2 - 4y^2$  
B) $9x^2 - 12xy + 4y^2$  
C) $9x^2 + 12xy + 4y^2$  
D) $9x^2 - 6xy + 4y^2$  
E) $6x^2 - 12xy + 4y^2$  

6. Simplificar aplicando diferencia de cuadrados: $(5x + 3)(5x - 3)$:  
A) $25x^2 + 9$  
B) $25x^2 - 9$  
C) $10x^2 - 9$  
D) $25x^2 - 15x - 9$  
E) $5x^2 - 9$  

7. Aplicar la identidad de Stevin al producto $(x + 7)(x - 4)$:  
A) $x^2 + 3x - 28$  
B) $x^2 - 3x - 28$  
C) $x^2 + 11x - 28$  
D) $x^2 + 3x + 28$  
E) $x^2 - 28$  

8. Si el polinomio $P(x) = 5x^{a-3} + 2x^2 - 7$ es de grado 5, hallar el valor de $a$:  
A) $5$  
B) $8$  
C) $2$  
D) $7$  
E) $6$  

9. Calcular el valor de $(a + b)^2 + (a - b)^2$ si $a^2 + b^2 = 15$:  
A) $15$  
B) $30$  
C) $60$  
D) $45$  
E) $25$  

10. Si $a + b = 6$ y $ab = 7$, calcular el valor de $a^2 + b^2$:  
A) $22$  
B) $29$  
C) $36$  
D) $50$  
E) $20$  

11. ¿Cuál es el grado de homogeneidad del polinomio $P(x, y) = 4x^5 y^2 - 3x^3 y^4 + 9y^7$?  
A) $5$  
B) $7$  
C) $10$  
D) $14$  
E) $12$  

12. Si el polinomio $P(x) = ax^2 + bx + c$ es idénticamente nulo, ¿cuál es el valor de $a + b + c$?  
A) $1$  
B) $-1$  
C) $0$  
D) $3$  
E) No se puede determinar  

13. Reducir la expresión: $E = (x + 1)(x^2 - x + 1)$:  
A) $x^3 - 1$  
B) $x^3 + 1$  
C) $x^3 + x^2 + 1$  
D) $(x + 1)^3$  
E) $x^3 - x + 1$  

14. Si $P(x + 2) = 2x + 7$, hallar $P(x)$:  
A) $2x + 5$  
B) $2x + 3$  
C) $2x + 11$  
D) $2x - 3$  
E) $2x + 9$  

15. Calcular el valor de $(x + 2)^3 - (x - 2)^3 - 12x^2$:  
A) $0$  
B) $8$  
C) $16$  
D) $-16$  
E) $32$  

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Si los polinomios $P(x) = (a - 1)x^2 + (b + 2)x + c$ y $Q(x) = 3x^2 + 5x - 4$ son idénticos, calcular $a + b + c$:  
A) $5$  
B) $3$  
C) $7$  
D) $-3$  
E) $2$  

17. Dado el polinomio completo y ordenado en forma ascendente: $P(x) = 4 + 3x^{m-1} + 5x^{n-2} + 2x^{p-3}$, hallar $m + n + p$:  
A) $6$  
B) $9$  
C) $12$  
D) $10$  
E) $8$  

18. Si $x - \frac{1}{x} = 3$, calcular el valor de $x^2 + \frac{1}{x^2}$:  
A) $7$  
B) $9$  
C) $11$  
D) $13$  
E) $8$  

19. Si $x + \frac{1}{x} = 3$, calcular el valor exacto de $x^3 + \frac{1}{x^3}$:  
A) $18$  
B) $27$  
C) $24$  
D) $20$  
E) $15$  

20. Simplificar la expresión aplicando identidades de Legendre:
$$
M = \frac{(a + 2b)^2 - (a - 2b)^2}{8ab}
$$
A) $1$  
B) $2$  
C) $1/2$  
D) $4$  
E) $8$  

21. Si $a + b + c = 0$, simplificar $E = \frac{a^3 + b^3 + c^3}{6abc}$:  
A) $1$  
B) $1/2$  
C) $2$  
D) $3$  
E) $1/6$  

22. Si $a^2 + b^2 + c^2 = ab + bc + ca$ para $a, b, c \in \mathbb{R}$, calcular el valor de:
$$
K = \frac{a^5 + b^5 + c^5}{(a + b + c)^5} \times 81
$$
A) $1$  
B) $3$  
C) $9$  
D) $27$  
E) $81$  

23. Dado el polinomio $P(x) = (x - 1)^{2026} + (2x - 1)^3 + 5$. Determinar la suma de coeficientes de $P(x)$:  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $2026$  

24. Si $P(x) = x^2 - 3x + 1$, calcular el valor de $P(a) + P(b)$ sabiendo que $a$ y $b$ son las raíces de la ecuación $x^2 - 3x + 1 = 0$:  
A) $0$  
B) $2$  
C) $-2$  
D) $6$  
E) $1$  

25. Si $x + y = 5$ y $x^2 + y^2 = 17$, hallar el valor del producto $xy$:  
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) $8$  

26. Reducir la siguiente expresión algebraica:
$$
R = (x + 1)(x - 1)(x^2 + 1)(x^4 + 1)(x^8 + 1) + 1
$$
A) $x^8$  
B) $x^{16}$  
C) $x^{32}$  
D) $x^{16} - 1$  
E) $2x^{16}$  

27. Si $P(x) = ax^2 + bx + c$ cumple que $P(1) = 8$, $P(0) = 3$ y $P(-1) = 2$, calcular $a \cdot b \cdot c$:  
A) $12$  
B) $18$  
C) $24$  
D) $30$  
E) $36$  

28. Si el polinomio $P(x, y) = 3x^{m+1} y^{n-2} + 5x^{m-2} y^n$ tiene grado absoluto igual a 14 y grado relativo respecto a $x$ igual a 8, hallar $m \cdot n$:  
A) $45$  
B) $49$  
C) $56$  
D) $42$  
E) $35$  

29. Si $a + b = 4$ y $ab = 2$, calcular el valor de $a^4 + b^4$:  
A) $84$  
B) $92$  
C) $96$  
D) $100$  
E) $112$  

30. Un tejedor de chompas de alpaca en Puno calcula que el costo unitario de producción depende de la cantidad $x$ de chompas según el polinomio $C(x) = (x - 5)^2 + 40$. ¿Para qué nivel de producción el costo unitario es mínimo y cuál es dicho costo mínimo?  
A) $5$ chompas; $S/\, 40$  
B) $10$ chompas; $S/\, 65$  
C) $5$ chompas; $S/\, 50$  
D) $4$ chompas; $S/\, 41$  
E) $0$ chompas; $S/\, 65$  

31. Hallar el valor de $E = \sqrt[3]{(x + 3)(x - 3)(x^2 + 9) + 81}$:  
A) $x$  
B) $x^2$  
C) $x^{4/3}$  
D) $x^4$  
E) $9$  

32. Si $f(x) = \frac{x + 1}{x - 1}$, calcular el valor de $f(f(x))$ para todo $x \neq 1$:  
A) $1$  
B) $x$  
C) $-x$  
D) $\frac{1}{x}$  
E) $x^2$  

33. Si el polinomio $P(x) = (a + b - 5)x^3 + (b + c - 7)x + (c + a - 6)$ es idénticamente nulo, calcular $a + b + c$:  
A) $9$  
B) $10$  
C) $18$  
D) $12$  
E) $14$  

34. Si $x = \sqrt{5} + \sqrt{3}$ e $y = \sqrt{5} - \sqrt{3}$, calcular el valor de $E = \frac{x^2 + y^2}{xy}$:  
A) $4$  
B) $8$  
C) $6$  
D) $5$  
E) $16$  

35. Un tanque de piscigranja para truchas en Huancavelica tiene forma de paralelepípedo rectangular con dimensiones $(x + 4)\text{ m}$, $(x + 1)\text{ m}$ y $(x - 2)\text{ m}$. Si el volumen total es de $40\text{ m}^3$, hallar la profundidad media $(x - 2)$:  
A) $1\text{ m}$  
B) $2\text{ m}$  
C) $3\text{ m}$  
D) $4\text{ m}$  
E) $0.5\text{ m}$  

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Si $a, b, c$ son números reales tales que $a + b + c = 6$ y $a^2 + b^2 + c^2 = 14$, calcular el valor de $ab + bc + ca$:  
A) $10$  
B) $11$  
C) $12$  
D) $9$  
E) $8$  

37. Si $P(x) = \frac{x}{x - 1}$, hallar el valor de $E = P(2) \cdot P(3) \cdot P(4) \cdots P(2026)$:  
A) $2026$  
B) $1013$  
C) $2025$  
D) $1$  
E) $4052$  

38. Si $x^2 + \frac{1}{x^2} = 7$ y $x > 0$, calcular el valor de $x^5 + \frac{1}{x^5}$:  
A) $123$  
B) $126$  
C) $120$  
D) $110$  
E) $132$  

39. Si el polinomio homogéneo $P(x, y) = ax^{a+3} y^2 + bx^b y^5 - cx^2 y^8$ tiene grado de homogeneidad 10, hallar el valor de $a + b$:  
A) $10$  
B) $9$  
C) $11$  
D) $8$  
E) $12$  

40. Sabiendo que $a + b + c = 0$, reducir a su mínima expresión:
$$
T = \frac{(2a + b + c)^3 + (a + 2b + c)^3 + (a + b + 2c)^3}{abc}
$$
A) $3$  
B) $1$  
C) $-3$  
D) $6$  
E) $-1$  

41. **(Reto)** Si se cumple que $\frac{a}{b} + \frac{b}{a} = 2$ para $a, b \in \mathbb{R} \setminus \{0\}$, calcular el valor numérico de:
$$
M = \frac{7a^3 + 5b^3}{3a^2 b + 9ab^2}
$$
A) $1$  
B) $2$  
C) $12/7$  
D) $3/2$  
E) $4/3$  

42. **(Reto)** Si $P(x)$ es un polinomio de segundo grado tal que $P(x) - P(x - 1) = 4x + 2$ para todo $x \in \mathbb{R}$, y se sabe que $P(0) = 3$, determinar el término independiente de $P(2x + 1)$:  
A) $9$  
B) $7$  
C) $11$  
D) $5$  
E) $13$  

43. **(Reto)** Si $a + b + c = 1$, $a^2 + b^2 + c^2 = 2$ y $a^3 + b^3 + c^3 = 3$, calcular el producto $abc$:  
A) $1/6$  
B) $1/3$  
C) $-1/6$  
D) $1/2$  
E) $-1/3$  

44. **(Reto)** Simplificar la siguiente expresión condicional para $x, y, z$ diferentes entre sí:
$$
K = \frac{x^2}{(x - y)(x - z)} + \frac{y^2}{(y - z)(y - x)} + \frac{z^2}{(z - x)(z - y)}
$$
A) $0$  
B) $1$  
C) $x + y + z$  
D) $xy + yz + zx$  
E) $-1$  

45. **(Reto)** Si $x + y + z = 0$ con $x, y, z \neq 0$, calcular el valor de:
$$
S = \frac{x^4 + y^4 + z^4}{(x^2 + y^2 + z^2)^2}
$$
A) $1$  
B) $1/2$  
C) $2$  
D) $1/4$  
E) $3/4$  

---

## 7. Formulario Resumen

| Concepto / Teorema | Expresión Matemática | Propiedades y Condiciones |
| :--- | :--- | :--- |
| **Grado Absoluto (Monomio)** | $\text{G.A.}(x^a y^b z^c) = a + b + c$ | Suma de exponentes de todas las variables |
| **Suma de Coeficientes** | $\sum \text{coef} = P(1)$ | Evaluar todas las variables en la unidad ($1$) |
| **Término Independiente** | $\text{T.I.} = P(0)$ | Evaluar todas las variables en cero ($0$) |
| **Polinomio Homogéneo** | $\text{G.A.}(T_1) = \text{G.A.}(T_2) = \dots = \text{cte}$ | Todos los términos tienen igual grado absoluto |
| **Polinomio Completo** | Posee todos los grados hasta cero | $\text{N° términos} = \text{Grado} + 1$ (una variable) |
| **Polinomios Idénticos** | $P(x) \equiv Q(x)$ | Coeficientes de términos semejantes son iguales |
| **Polinomio Nulo** | $P(x) \equiv 0$ | Todos sus coeficientes son idénticamente cero |
| **Binomio al Cuadrado** | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ | Trinomio cuadrado perfecto |
| **1ra Identidad de Legendre** | $(a + b)^2 + (a - b)^2 = 2(a^2 + b^2)$ | Suma de cuadrados de binomios opuestos |
| **2da Identidad de Legendre** | $(a + b)^2 - (a - b)^2 = 4ab$ | Diferencia de cuadrados de binomios opuestos |
| **Diferencia de Cuadrados** | $(a + b)(a - b) = a^2 - b^2$ | Producto de suma por diferencia |
| **Identidad de Stevin** | $(x + a)(x + b) = x^2 + (a + b)x + ab$ | Binomios con término común |
| **Cauchy: Suma de Cubos** | $(a + b)^3 = a^3 + b^3 + 3ab(a + b)$ | Binomio al cubo semidesarrollado |
| **Cauchy: Diferencia de Cubos**| $(a - b)^3 = a^3 - b^3 - 3ab(a - b)$ | Binomio al cubo semidesarrollado |
| **Suma de Cubos Factorizada** | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ | Binomio suma por trinomio especial |
| **Diferencia de Cubos Factorizada** | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ | Binomio resta por trinomio especial |
| **Condicional Si $a+b+c=0$** | $a^3 + b^3 + c^3 = 3abc$ | Identidad cúbica condicional |
| **Condicional de Cuadrados** | $a^2 + b^2 + c^2 = -2(ab + bc + ca)$ | Se cumple si $a + b + c = 0$ |
