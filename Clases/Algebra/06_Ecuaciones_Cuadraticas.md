# Tema 06: Ecuaciones Cuadráticas

Una ecuación cuadrática o de segundo grado con una incógnita es una igualdad algebraica polinomial reducible a la forma canónica:

$$
ax^2 + bx + c = 0
$$

donde $a, b, c \in \mathbb{R}$ representan los coeficientes de la ecuación, con la condición indispensable de que $a \neq 0$ para garantizar que el grado del polinomio sea exactamente 2. La incógnita $x$ representa el valor o valores numéricos (reales o complejos) que satisfacen simultáneamente la igualdad.

Las ecuaciones cuadráticas constituyen uno de los pilares más determinantes del examen de preselección Beca 18 y de la formación científica y técnica. Su campo de aplicación abarca desde el modelamiento de trayectorias balísticas en física clásica y cálculo de tiempos de vuelo, hasta la optimización de áreas productivas agrícolas en parcelas rurales, dimensionamiento estructural y determinación del punto de equilibrio económico en mercados con elasticidad de demanda.

---

### 1.1 ¿De Dónde Nace una Ecuación Cuadrática? (El Puente Intuitivo)

En la vida real, muchas magnitudes no dependen de una sola dimensión lineal, sino de la interacción de dos dimensiones: el **área**.
Imagina que un campesino en el valle del Mantaro desea cercar un terreno rectangular para sembrar alcachofas. Sabe que el largo del terreno mide 3 metros más que su ancho ($x$).
* El ancho mide: $x$
* El largo mide: $x + 3$
* El área total del terreno es: $\text{Área} = x(x + 3) = x^2 + 3x$

Si el dueño dispone de semillas para cubrir exactamente $40\text{ m}^2$, surge de manera natural la igualdad:

$$x^2 + 3x = 40 \implies x^2 + 3x - 40 = 0$$

Aparece el término $x^2$ (equis al cuadrado). Esta es una **ecuación cuadrática o de segundo grado**. A diferencia de las ecuaciones lineales, una ecuación cuadrática puede admitir **hasta dos soluciones distintas** (en este ejemplo, $x = 5$ y $x = -8$; descartando la negativa por tratarse de una longitud física, el ancho es $5\text{ m}$).

---

### 1.2 Forma Canónica General y Formas Incompletas

Toda ecuación de segundo grado en una variable puede reducirse a su forma canónica:

$$ax^2 + bx + c = 0 \quad (a, b, c \in \mathbb{R}, \ a \neq 0)$$

Donde:
* $a$ es el coeficiente cuadrático (jamás puede ser cero, porque la ecuación dejaría de ser cuadrática).
* $b$ es el coeficiente lineal.
* $c$ es el término independiente.

#### Formas Incompletas (Resolución Rápida sin Fórmula General)

1. **Ecuación Cuadrática Pura ($b = 0, c \neq 0$):**
   $$ax^2 + c = 0 \implies x^2 = -\frac{c}{a} \implies x = \pm \sqrt{-\frac{c}{a}}$$
   *Micro-ejemplo:* $2x^2 - 18 = 0 \implies x^2 = 9 \implies x = \pm 3$. Conjunto solución: $CS = \{-3, 3\}$.

2. **Ecuación Cuadrática Mixta ($b \neq 0, c = 0$):**
   $$ax^2 + bx = 0 \implies x(ax + b) = 0 \implies x_1 = 0 \quad \lor \quad x_2 = -\frac{b}{a}$$
   *Micro-ejemplo:* $3x^2 - 12x = 0 \implies 3x(x - 4) = 0 \implies x_1 = 0 \lor x_2 = 4$. Conjunto solución: $CS = \{0, 4\}$.


### 2.1 Método de Factorización

Se basa en la propiedad algebraica del cuerpo de los reales que establece que si el producto de dos o más factores es nulo, al menos uno de ellos debe ser forzosamente igual a cero:

$$
A \cdot B = 0 \iff A = 0 \quad \lor \quad B = 0
$$

* **Aspa Simple:** Cuando el trinomio $ax^2 + bx + c$ se descompone en $(m x + p)(n x + q) = 0$, obteniéndose de inmediato $x_1 = -\frac{p}{m}$ y $x_2 = -\frac{q}{n}$.
* **Diferencia de Cuadrados:** Para casos donde $c < 0$ y $b = 0$: $x^2 - k^2 = (x - k)(x + k) = 0$.

### 2.2 Método de Completación de Cuadrados

Consiste en transformar la ecuación general dividiendo entre el coeficiente principal $a$ y sumando a ambos lados el cuadrado de la mitad del coeficiente lineal $\left(\frac{b}{2a}\right)^2$:

$$
x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 = -\frac{c}{a} + \left(\frac{b}{2a}\right)^2
$$

$$
\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}
$$

Extrayendo raíz cuadrada en ambos miembros:

$$
x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}
$$

### 2.3 Fórmula General y Análisis del Discriminante

De la completación de cuadrados se desprende la fórmula cuadrática universal:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Se define como **discriminante** de la ecuación cuadrática a la cantidad subradical denotada por la letra griega mayúscula delta ($\Delta$):

$$
\Delta = b^2 - 4ac
$$

El signo y valor del discriminante determina de manera unívoca la naturaleza geométrica y algebraica de las raíces:

1. **Si $\Delta > 0$:** La ecuación admite **dos raíces reales y distintas** ($x_1 \neq x_2 \in \mathbb{R}$).
* Si además $\Delta$ es un cuadrado perfecto ($k^2, k \in \mathbb{Q}$), las raíces son números racionales ($\mathbb{Q}$) y el trinomio es factorizable en $\mathbb{Q}$.
* Si $\Delta$ no es un cuadrado perfecto, las raíces son reales irracionales conjugadas de la forma $p \pm \sqrt{q}$.
2. **Si $\Delta = 0$:** La ecuación admite **una raíz real doble o única** ($x_1 = x_2 = -\frac{b}{2a}$). El trinomio es un Trinomio Cuadrado Perfecto (T.C.P.).
3. **Si $\Delta < 0$:** La ecuación **no tiene raíces reales**. Presenta dos raíces complejas imaginarias conjugadas:
$$
x = -\frac{b}{2a} \pm i \frac{\sqrt{4ac - b^2}}{2a}, \quad (i = \sqrt{-1})
$$

### Interpretación Gráfica en el Plano Cartesiano

Geométricamente, las raíces reales de $ax^2 + bx + c = 0$ corresponden a las abscisas de los puntos donde la parábola $y = ax^2 + bx + c$ corta al eje horizontal $X$:

```{figure} ../../assets/algebra/discriminante_parabolas.svg
---
align: center
alt: Interpretación geométrica del discriminante en el plano cartesiano
---
Relación entre el signo del discriminante $\Delta$, las raíces de la ecuación y la intersección de la parábola con el eje horizontal de las abscisas.
```

---

## 3. Propiedades de las Raíces (Teorema de Cardano-Vieta)

Sean $x_1$ y $x_2$ las raíces de la ecuación canónica $ax^2 + bx + c = 0$ ($a \neq 0$). De acuerdo con las relaciones fundamentales de Cardano-Vieta:

### 3.1 Suma de Raíces ($S$)

$$
S = x_1 + x_2 = -\frac{b}{a}
$$

### 3.2 Producto de Raíces ($P$)

$$
P = x_1 \cdot x_2 = \frac{c}{a}
$$

### 3.3 Diferencia Absoluta de Raíces ($D$)

Aplicando la identidad algebraica de Legendre: $(x_1 + x_2)^2 - (x_1 - x_2)^2 = 4x_1 x_2$, se obtiene:

$$
|x_1 - x_2| = \frac{\sqrt{\Delta}}{|a|} = \frac{\sqrt{b^2 - 4ac}}{|a|}, \quad (\Delta \geq 0)
$$

### 3.4 Suma de Inversas

$$
\frac{1}{x_1} + \frac{1}{x_2} = \frac{x_1 + x_2}{x_1 \cdot x_2} = \frac{-b/a}{c/a} = -\frac{b}{c}, \quad (c \neq 0)
$$

### 3.5 Reconstrucción de la Ecuación Cuadrática

Si se conocen las raíces $x_1$ y $x_2$ (o bien su suma $S$ y su producto $P$), la ecuación cuadrática original mónica se reconstruye directamente como:

$$
x^2 - S x + P = 0 \iff x^2 - (x_1 + x_2)x + (x_1 \cdot x_2) = 0
$$

### 3.6 Raíces Especiales

* **Raíces Simétricas u Opuestas:** Son aquellas cuya suma es nula ($x_1 = -x_2 \iff x_1 + x_2 = 0$).
$$
S = -\frac{b}{a} = 0 \iff b = 0
$$
* **Raíces Recíprocas o Inversas:** Son aquellas cuyo producto es la unidad ($x_1 = \frac{1}{x_2} \iff x_1 \cdot x_2 = 1$).
$$P = \frac{c}{a} = 1 \iff a = c$$

#### Micro-ejemplo 1: Uso veloz de Cardano-Vieta
Dada la ecuación $3x^2 - 12x + 7 = 0$, calcule la suma y producto de raíces sin resolver la ecuación:
* **Suma:** $S = -\frac{b}{a} = -\frac{-12}{3} = \frac{12}{3} = 4$.
* **Producto:** $P = \frac{c}{a} = \frac{7}{3}$.

---

### 3.7 ⚠️ ¡Cuidado con los Errores Clásicos de Admisión!

> ⚠️ **Error 1: Olvidar la solución negativa al extraer raíz cuadrada.**  
> Al resolver $x^2 = 36$, el 40% de postulantes responde $x = 6$. ¡Olvidan que $(-6)^2$ también es $36$! Recuerda: siempre coloca el doble signo $\pm$: $x = \pm \sqrt{36} = \pm 6$.

> ⚠️ **Error 2: El signo de $-b$ en la fórmula general.**  
> Si la ecuación es $x^2 - 6x + 2 = 0$, aquí $b = -6$. Por lo tanto:
> $$-b = -(-6) = +6$$
> Muchos cometen el error de escribir $-6 \pm \sqrt{\dots}$ y fallan la alternativa correcta.

> ⚠️ **Error 3: Creer que $\Delta < 0$ significa que la ecuación es absurda.**  
> Si $\Delta < 0$, la ecuación **NO tiene raíces reales**, pero **SÍ tiene raíces complejas/imaginarias** conjugadas. Si la pregunta de admisión dice: *"Indique el número de raíces reales"*, la respuesta es **cero**; pero si dice: *"Indique el número total de raíces (en el campo complejo)"*, la respuesta es **dos**.


---

## 4. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Factorización por Aspa Simple
Resolver la ecuación cuadrática:
$$
6x^2 - 11x - 35 = 0
$$

**Paso 1:** Descomponemos los extremos para aplicar aspa simple.
Buscamos factores de $6x^2$ y $-35$:
$6x^2 = (2x)(3x)$
$-35 = (+5)(-7)$

**Paso 2:** Verificamos el término central mediante multiplicación cruzada:
$(2x)(-7) + (3x)(+5) = -14x + 15x = +x \quad \text{(No coincide)}$

Probamos con:
$6x^2 = (2x)(3x)$
$-35 = (-7)(+5)$
Multiplicación cruzada:
$(2x)(+5) + (3x)(-7) = 10x - 21x = -11x \quad \text{(Coincide exactamente)}$

**Paso 3:** Escribimos los factores horizontales e igualamos cada uno a cero:
$(2x - 7)(3x + 5) = 0$
$2x - 7 = 0 \implies x_1 = \frac{7}{2}$
$3x + 5 = 0 \implies x_2 = -\frac{5}{3}$

**Respuesta:** El conjunto solución es C.S. $= \left\{ -\frac{5}{3}, \frac{7}{2} \right\}$.

---

### Ejercicio 2: Aplicación del Discriminante para Raíz Única
Determinar los valores reales de $k$ para que la siguiente ecuación tenga raíces reales e iguales (solución única):
$$
(k - 1)x^2 + 2(k + 1)x + (k + 3) = 0
$$

**Paso 1:** Identificamos los coeficientes de la ecuación:
$a = k - 1$ (con la restricción $a \neq 0 \implies k \neq 1$)
$b = 2(k + 1)$
$c = k + 3$

**Paso 2:** Para que la ecuación tenga raíz doble o solución única, su discriminante debe ser estrictamente cero:
$\Delta = b^2 - 4ac = 0$

**Paso 3:** Sustituimos y desarrollamos algebraicamente:
$[2(k + 1)]^2 - 4(k - 1)(k + 3) = 0$
$4(k^2 + 2k + 1) - 4(k^2 + 2k - 3) = 0$

Dividiendo toda la igualdad entre 4:
$(k^2 + 2k + 1) - (k^2 + 2k - 3) = 0$
$k^2 + 2k + 1 - k^2 - 2k + 3 = 0$
$4 = 0 \quad \text{(Contradicción)}$

**Paso 4:** Análisis crítico del resultado.
Los términos de segundo y primer grado en $k$ se cancelan idénticamente para cualquier valor de $k$. Esto indica que para ningún valor finito de $k$ el discriminante puede anularse; en efecto, $\Delta = 4(4) = 16 > 0$ de forma constante e independiente de $k$.

**Respuesta:** No existe ningún valor real de $k$ para el cual la ecuación tenga raíz única (las raíces son reales y distintas para todo $k \in \mathbb{R} \setminus \{1\}$).

---

### Ejercicio 3: Teorema de Cardano-Vieta con Suma de Cuadrados
Si $x_1$ y $x_2$ son las raíces de la ecuación $2x^2 - 6x + 1 = 0$, calcular el valor numérico de la expresión:
$$
M = x_1^2 + x_2^2 + 3(x_1 + x_2)
$$

**Paso 1:** Aplicamos las propiedades de Cardano-Vieta sobre los coeficientes $a = 2$, $b = -6$, $c = 1$:
$S = x_1 + x_2 = -\frac{b}{a} = -\frac{-6}{2} = 3$
$P = x_1 \cdot x_2 = \frac{c}{a} = \frac{1}{2}$

**Paso 2:** Expresamos la suma de cuadrados en función de $S$ y $P$ mediante el binomio al cuadrado:
$(x_1 + x_2)^2 = x_1^2 + 2x_1 x_2 + x_2^2$
$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2(x_1 x_2) = S^2 - 2P$

**Paso 3:** Sustituimos los valores numéricos:
$x_1^2 + x_2^2 = (3)^2 - 2\left(\frac{1}{2}\right) = 9 - 1 = 8$

**Paso 4:** Calculamos la expresión solicitada $M$:
$M = (x_1^2 + x_2^2) + 3(x_1 + x_2) = 8 + 3(3) = 8 + 9 = 17$

**Respuesta:** El valor de la expresión es 17.

---

### Ejercicio 4: Raíces Simétricas y Recíprocas
Hallar los valores de $m$ y $n$ en la ecuación:
$$
(m - 3)x^2 + (2m - 8)x + (n + 5) = 0
$$
sabiendo que sus raíces son simétricas y que al mismo tiempo el producto de sus raíces es igual a 4.

**Paso 1:** Condición de raíces simétricas:
Dos raíces son simétricas si su suma es cero: $x_1 + x_2 = 0$.
Por Cardano-Vieta: $-\frac{b}{a} = 0 \implies b = 0$.
$2m - 8 = 0 \implies 2m = 8 \implies m = 4$

**Paso 2:** Verificamos el coeficiente principal con $m = 4$:
$a = m - 3 = 4 - 3 = 1 \neq 0$ (Condición válida).

**Paso 3:** Condición del producto de raíces:
$P = \frac{c}{a} = 4$
Sustituimos $c = n + 5$ y $a = 1$:
$\frac{n + 5}{1} = 4 \implies n + 5 = 4 \implies n = -1$

**Respuesta:** Los valores pedidos son $m = 4$ y $n = -1$.

---

### Ejercicio 5: Reconstrucción de Ecuaciones Cuadráticas
Formar una ecuación cuadrática mónica con coeficientes enteros cuyas raíces sean el triple de las raíces de la ecuación:
$$
x^2 - 4x + 2 = 0
$$

**Paso 1:** Sean $\alpha$ y $\beta$ las raíces de $x^2 - 4x + 2 = 0$.
Por Cardano-Vieta:
$\alpha + \beta = 4$
$\alpha \cdot \beta = 2$

**Paso 2:** Sean $y_1$ y $y_2$ las nuevas raíces deseadas:
$y_1 = 3\alpha, \quad y_2 = 3\beta$

**Paso 3:** Calculamos la nueva suma ($S_{nueva}$) y el nuevo producto ($P_{nueva}$):
$S_{nueva} = y_1 + y_2 = 3\alpha + 3\beta = 3(\alpha + \beta) = 3(4) = 12$
$P_{nueva} = y_1 \cdot y_2 = (3\alpha)(3\beta) = 9(\alpha \cdot \beta) = 9(2) = 18$

**Paso 4:** Reconstruimos la ecuación cuadrática mónica mediante $y^2 - S_{nueva}y + P_{nueva} = 0$:
$y^2 - 12y + 18 = 0$

**Respuesta:** La ecuación cuadrática requerida es $x^2 - 12x + 18 = 0$.

---

### Ejercicio 6: Suma de Inversas y Cubos
Dada la ecuación $x^2 - 5x + 3 = 0$ de raíces $a$ y $b$, calcular el valor de:
$$
K = \frac{1}{a^2} + \frac{1}{b^2}
$$

**Paso 1:** Obtenemos la suma y producto de raíces:
$S = a + b = 5$
$P = a \cdot b = 3$

**Paso 2:** Homogeneizamos la suma de fracciones:
$K = \frac{b^2 + a^2}{a^2 b^2} = \frac{a^2 + b^2}{(ab)^2}$

**Paso 3:** Desarrollamos el numerador $a^2 + b^2 = S^2 - 2P$:
$a^2 + b^2 = (5)^2 - 2(3) = 25 - 6 = 19$

**Paso 4:** Calculamos el denominador $(ab)^2 = P^2 = 3^2 = 9$:
$K = \frac{19}{9}$

**Respuesta:** El valor numérico de la expresión es $\frac{19}{9}$.

---

### Ejercicio 7: Ecuaciones Reducibles a Cuadráticas (Bicuadrada básica)
Resolver en $\mathbb{R}$ la ecuación:
$$
x^4 - 13x^2 + 36 = 0
$$

**Paso 1:** Realizamos el cambio de variable auxiliar:
Sea $u = x^2$ (con la restricción $u \geq 0$ para soluciones reales).
La ecuación se transforma en:
$u^2 - 13u + 36 = 0$

**Paso 2:** Factorizamos el trinomio por aspa simple:
$(u - 9)(u - 4) = 0$
De donde:
$u_1 = 9 \quad \lor \quad u_2 = 4$

**Paso 3:** Retornamos a la variable original $x$:
Para $u_1 = 9 \implies x^2 = 9 \implies x = \pm 3$
Para $u_2 = 4 \implies x^2 = 4 \implies x = \pm 2$

**Paso 4:** Determinamos el conjunto solución completo:
C.S. $= \{-3, -2, 2, 3\}$

**Respuesta:** Las soluciones reales son $x \in \{-3, -2, 2, 3\}$.

---

### Ejercicio 8: Contextualización Física (Lanzamiento Vertical Beca 18)
Desde lo alto de una torre de control en una represa hidroeléctrica en Huancavelica, se lanza un proyectil de señalización verticalmente hacia arriba con una velocidad inicial de $30\text{ m/s}$. La altura $h$ (en metros) sobre el suelo en función del tiempo $t$ (en segundos) está modelada por la ecuación física:
$$
h(t) = -5t^2 + 30t + 80
$$
¿En cuántos segundos impactará el proyectil contra el suelo?

**Paso 1:** Cuando el proyectil impacta contra el suelo, su altura final es cero ($h(t) = 0$):
$-5t^2 + 30t + 80 = 0$

**Paso 2:** Simplificamos la ecuación cuadrática dividiendo entre $-5$:
$t^2 - 6t - 16 = 0$

**Paso 3:** Factorizamos por aspa simple:
$(t - 8)(t + 2) = 0$
$t - 8 = 0 \implies t_1 = 8\text{ s}$
$t + 2 = 0 \implies t_2 = -2\text{ s}$

**Paso 4:** Análisis físico:
El tiempo es una magnitud física estrictamente no negativa ($t \geq 0$). Por lo tanto, descartamos la raíz extraña negativa $t_2 = -2$.

**Respuesta:** El proyectil impactará contra el suelo a los 8 segundos.

---

### Ejercicio 9: Contextualización Económica (Ingresos Máximos y Demanda)
Una asociación comunal de productores de cacao en el VRAEM determina que si fija el precio por kilogramo de cacao en $p$ soles, la cantidad demandada en quintales al mes está dada por la relación lineal $q = 120 - 2p$. Si la asociación necesita generar un ingreso mensual exacto de $S/\, 1600$, determinar el precio o precios de venta por kilogramo que cumplen dicha meta.

**Paso 1:** Planteamos la función de ingreso mensual como el producto del precio por la cantidad vendida:
$\text{Ingreso } I = p \cdot q = p(120 - 2p) = 120p - 2p^2$

**Paso 2:** Igualamos la expresión al ingreso requerido de 1600 soles:
$120p - 2p^2 = 1600$

**Paso 3:** Transponemos todos los términos a un solo miembro para obtener la forma canónica:
$2p^2 - 120p + 1600 = 0$

**Paso 4:** Dividimos entre 2 para simplificar los coeficientes:
$p^2 - 60p + 800 = 0$

**Paso 5:** Factorizamos buscando dos números que multiplicados den 800 y sumados $-60$:
Dichos números son $-20$ y $-40$:
$(p - 20)(p - 40) = 0$
$p_1 = 20 \quad \lor \quad p_2 = 40$

**Respuesta:** La asociación puede fijar el precio en $S/\, 20$ o en $S/\, 40$ por kilogramo.

---

### Ejercicio 10: Geometría de Parcelas y Optimización
Una comunidad campesina en Ayacucho dispone de un terreno rectangular para sembrío de quinua cuya longitud es $10\text{ m}$ mayor que el doble de su ancho. Si el área total cercada del terreno es de $600\text{ m}^2$, calcular el perímetro del terreno.

**Paso 1:** Definimos la variable:
Sea $x$ el ancho del terreno rectangular en metros ($x > 0$).
El largo será: $L = 2x + 10$.

**Paso 2:** Formulamos la ecuación del área rectangular:
$\text{Área} = \text{Ancho} \times \text{Largo} = x(2x + 10) = 600$
$2x^2 + 10x - 600 = 0$

**Paso 3:** Dividimos toda la ecuación entre 2:
$x^2 + 5x - 300 = 0$

**Paso 4:** Factorizamos por aspa simple descomponiendo $-300$ en dos factores que difieran en 5:
$300 = 15 \times 20 \implies (+20)(-15) = -300 \quad \text{y} \quad +20 - 15 = +5$
$(x + 20)(x - 15) = 0$
$x_1 = 15 \quad \lor \quad x_2 = -20$

**Paso 5:** Como las dimensiones geométricas deben ser positivas, tomamos $x = 15\text{ m}$.
El largo es $L = 2(15) + 10 = 30 + 10 = 40\text{ m}$.

**Paso 6:** Calculamos el perímetro del rectángulo:
$\text{Perímetro} = 2(\text{Ancho} + \text{Largo}) = 2(15 + 40) = 2(55) = 110\text{ m}$.

**Respuesta:** El perímetro del terreno es de $110\text{ m}$.

---

## 5. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. Resolver la ecuación $x^2 - 9x + 20 = 0$ e indicar la mayor de sus raíces:  
A) $4$  
B) $5$  
C) $9$  
D) $20$  
E) $1$  

2. Hallar el conjunto solución de la ecuación incompleta pura $3x^2 - 48 = 0$:  
A) $\{4\}$  
B) $\{-4\}$  
C) $\{-4, 4\}$  
D) $\{-16, 16\}$  
E) $\{0, 4\}$  

3. Al resolver $5x^2 - 15x = 0$, la suma de sus soluciones es:  
A) $0$  
B) $3$  
C) $-3$  
D) $5$  
E) $15$  

4. Determinar las raíces de la ecuación cuadrática $2x^2 + 7x + 3 = 0$:  
A) $\{-3, -1/2\}$  
B) $\{3, 1/2\}$  
C) $\{-3, 1/2\}$  
D) $\{3, -1/2\}$  
E) $\{-7, 3\}$  

5. ¿Cuál es el discriminante de la ecuación $3x^2 - 5x + 4 = 0$?  
A) $73$  
B) $49$  
C) $-23$  
D) $-47$  
E) $0$  

6. Si una ecuación cuadrática tiene como raíces a $x_1 = 3$ y $x_2 = -7$, ¿cuál es la ecuación mónica correspondiente?  
A) $x^2 + 4x - 21 = 0$  
B) $x^2 - 4x - 21 = 0$  
C) $x^2 + 4x + 21 = 0$  
D) $x^2 - 10x - 21 = 0$  
E) $x^2 + 10x + 21 = 0$  

7. En la ecuación $x^2 - 8x + k = 0$, una de las raíces es $x = 2$. Hallar el valor de la constante $k$:  
A) $10$  
B) $12$  
C) $16$  
D) $8$  
E) $14$  

8. Calcular la suma y el producto de las raíces de la ecuación $4x^2 - 12x + 5 = 0$:  
A) $S = 3, P = 5/4$  
B) $S = -3, P = 5/4$  
C) $S = 12, P = 5$  
D) $S = 3, P = -5/4$  
E) $S = 4, P = 5/12$  

9. Resolver la ecuación cuadrática $(x - 4)^2 = 25$ e indicar la menor solución:  
A) $9$  
B) $-1$  
C) $-9$  
D) $1$  
E) $-5$  

10. Si el discriminante de $x^2 - mx + 9 = 0$ es igual a cero, ¿cuáles son los posibles valores de $m$?  
A) Solo $6$  
B) Solo $-6$  
C) $\pm 6$  
D) $\pm 3$  
E) $\pm 18$  

11. Resolver por completación de cuadrados $x^2 + 6x - 7 = 0$ e indicar el producto de sus raíces:  
A) $-7$  
B) $7$  
C) $-6$  
D) $6$  
E) $-1$  

12. Hallar la menor raíz de la ecuación $x(x + 5) = 24$:  
A) $3$  
B) $-8$  
C) $8$  
D) $-3$  
E) $-5$  

13. Para qué valor de $c$ la ecuación $x^2 - 4x + c = 0$ tiene solución real única:  
A) $2$  
B) $4$  
C) $-4$  
D) $16$  
E) $8$  

14. Si la suma de dos números es 15 y su producto es 54, determinar el menor de dichos números:  
A) $6$  
B) $9$  
C) $5$  
D) $4$  
E) $3$  

15. Indicar la naturaleza de las raíces de la ecuación $2x^2 - 4x + 7 = 0$:  
A) Reales e iguales  
B) Reales, racionales y distintas  
C) Reales, irracionales y distintas  
D) No reales (complejas conjugadas)  
E) Infinitas soluciones  

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Si $x_1$ y $x_2$ son las raíces de la ecuación $x^2 - 7x + 5 = 0$, calcular el valor de $E = x_1^2 + x_2^2$:  
A) $39$  
B) $49$  
C) $29$  
D) $44$  
E) $34$  

17. En la ecuación $2x^2 - 8x + 3 = 0$, calcular la suma de las inversas de sus raíces $\frac{1}{x_1} + \frac{1}{x_2}$:  
A) $8/3$  
B) $4/3$  
C) $3/8$  
D) $-8/3$  
E) $2/3$  

18. Hallar el valor de $m$ para que la ecuación $(m - 2)x^2 - (2m - 1)x + m - 1 = 0$ tenga raíces recíprocas:  
A) $1$  
B) $2$  
C) No existe tal valor  
D) $3$  
E) $0$  

19. Si las raíces de la ecuación $(a + 1)x^2 + (b - 2)x + 12 = 0$ son simétricas y recíprocas al mismo tiempo, calcular $a + b$:  
A) $11$  
B) $13$  
C) $9$  
D) $15$  
E) $14$  

20. Si $x_1$ y $x_2$ son las raíces de $x^2 - 3x + 1 = 0$, calcular el valor de $M = x_1^3 + x_2^3$:  
A) $18$  
B) $27$  
C) $15$  
D) $24$  
E) $21$  

21. Determinar el valor positivo de $k$ para el cual la diferencia de las raíces de la ecuación $x^2 - kx + 12 = 0$ sea igual a 1:  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

22. Si una de las raíces de la ecuación $x^2 - (k + 3)x + 3k = 0$ es el triple de la otra, calcular el mayor valor de $k$:  
A) $1$  
B) $3$  
C) $9$  
D) $6$  
E) $12$  

23. Formar la ecuación cuadrática cuyas raíces sean el inverso aditivo y multiplicativo de las raíces de $x^2 - 6x + 4 = 0$, es decir, raíces $-\frac{1}{x_1}$ y $-\frac{1}{x_2}$:  
A) $4x^2 + 6x + 1 = 0$  
B) $4x^2 - 6x + 1 = 0$  
C) $x^2 + 6x + 4 = 0$  
D) $4x^2 + 6x - 1 = 0$  
E) $2x^2 + 3x + 2 = 0$  

24. Un agricultor de café en Junín cerca una parcela rectangular de $180\text{ m}^2$. Si el largo excede al ancho en $3\text{ m}$, ¿cuántos metros de alambre se necesitan para darle una vuelta completa al perímetro?  
A) $54\text{ m}$  
B) $48\text{ m}$  
C) $52\text{ m}$  
D) $60\text{ m}$  
E) $45\text{ m}$  

25. Un grupo de estudiantes postulantes a Beca 18 deciden alquilar un bus para visitar la feria vocacional universitaria en Lima por un costo total de $S/\, 720$, repartido en partes iguales. Al momento de viajar, 4 estudiantes desisten, por lo que cada uno de los restantes debe pagar $S/\, 6$ adicionales. ¿Cuántos estudiantes viajaron finalmente?  
A) $20$  
B) $24$  
C) $16$  
D) $18$  
E) $22$  

26. Resolver en $\mathbb{R}$ la ecuación racional fraccionaria $\frac{x}{x - 2} + \frac{2}{x + 2} = \frac{8}{x^2 - 4}$:  
A) $\{-2, 2\}$  
B) $\{2\}$  
C) $\{-2\}$  
D) $\emptyset$ (No tiene solución)  
E) $\{0\}$  

27. Resolver la ecuación irracional $\sqrt{2x + 7} = x + 2$ e indicar la suma de sus soluciones reales:  
A) $1$  
B) $-1$  
C) $-3$  
D) $0$  
E) $3$  

28. Si la ecuación cuadrática en $x$: $x^2 - 2(a - 1)x + a^2 - 2a = 0$ tiene raíces reales, ¿qué condición debe cumplir el parámetro $a$?  
A) $a \geq 1$  
B) $a \leq 1$  
C) $a \in \mathbb{R}$ (Se cumple para todo $a$ real)  
D) $a > 0$  
E) $a \in \emptyset$  

29. Determinar el valor de $k$ para que las raíces de la ecuación $x^2 - (k - 5)x + (k - 2) = 0$ difieran en 3 unidades:  
A) $6$ ó $10$  
B) $4$ ó $8$  
C) $5$ ó $9$  
D) $3$ ó $7$  
E) $2$ ó $6$  

30. Hallar el producto de todas las raíces reales de la ecuación $(x^2 - 5x)^2 - 2(x^2 - 5x) - 24 = 0$:  
A) $24$  
B) $-24$  
C) $36$  
D) $-36$  
E) $18$  

31. Un microempresario textil de Huancayo produce mantas tradicionales. El costo fijo mensual es de $S/\, 1200$ y el costo variable unitario es de $S/\, 20$. Si vende cada manta a un precio $p = 100 - x$ soles, donde $x$ es la cantidad de mantas producidas y vendidas, ¿cuántas mantas debe vender para obtener una ganancia neta de $S/\, 400$?  
A) $40$ mantas  
B) $20$ ó $60$ mantas  
C) $50$ mantas  
D) $30$ mantas  
E) $10$ ó $70$ mantas  

32. Si las raíces de $x^2 + px + q = 0$ son el doble de las raíces de $x^2 + mx + n = 0$, hallar la relación que existe entre $q$ y $n$:  
A) $q = 2n$  
B) $q = 4n$  
C) $q = n/2$  
D) $q = n/4$  
E) $q = 8n$  

33. Si $\alpha$ es una raíz de la ecuación $x^2 - 3x + 1 = 0$, calcular el valor de $\alpha^4 + \frac{1}{\alpha^4}$:  
A) $47$  
B) $49$  
C) $51$  
D) $45$  
E) $43$  

34. Dos grifos abiertos simultáneamente llenan un reservorio de agua potable comunal en 6 horas. Si el grifo secundario tarda 5 horas más que el grifo principal en llenarlo funcionando solo, ¿cuántas horas tardaría el grifo principal en llenar el reservorio por sí solo?  
A) $10\text{ h}$  
B) $12\text{ h}$  
C) $15\text{ h}$  
D) $8\text{ h}$  
E) $14\text{ h}$  

35. Resolver el sistema simétrico de ecuaciones:
$$
\begin{cases} x + y = 10 \\ x y = 21 \end{cases}
$$
e indicar el valor absoluto de la diferencia $|x - y|$:  
A) $2$  
B) $3$  
C) $4$  
D) $5$  
E) $6$  

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Si las ecuaciones cuadráticas:
$$
(m - 1)x^2 - (m + 2)x + 6 = 0 \quad \text{y} \quad (n - 2)x^2 - (2n + 1)x + 18 = 0
$$
tienen las mismas raíces (son ecuaciones equivalentes), calcular el valor de $m + n$:  
A) $10$  
B) $12$  
C) $14$  
D) $16$  
E) $8$  

37. Dada la ecuación cuadrática $x^2 - 2x + 5 = 0$, cuyas raíces son $x_1$ y $x_2$. Calcular el valor exacto de:
$$
T = \frac{x_1^4 + x_2^4 + 14}{(x_1 - x_2)^2}
$$
A) $1$  
B) $2$  
C) $-2$  
D) $-1$  
E) $0$  

38. Sea la ecuación $x^2 - bx + c = 0$ con raíces reales $\alpha$ y $\beta$. Si $\alpha^2 + \beta^2 = 27$ y $\alpha^3 + \beta^3 = 90$, y sabiendo que $b > 0$, calcular el valor de $b + c$:  
A) $12$  
B) $15$  
C) $11$  
D) $14$  
E) $17$  

39. Si las raíces de $x^2 - px + q = 0$ son números enteros positivos y uno de ellos es un número primo, y se sabe que la suma de raíces es 11 y el producto es 24, determinar la diferencia positiva de dichas raíces:  
A) $5$  
B) $7$  
C) $3$  
D) $1$  
E) $2$  

40. Hallar todos los valores reales de $k$ para los cuales la ecuación:
$$
(k^2 - 4)x^2 + 2(k - 2)x + 1 = 0
$$
tiene exactamente una única solución en $\mathbb{R}$:  
A) $k = 2$  
B) $k = -2$  
C) $k = 2$ ó $k = -2$  
D) No existe solución única  
E) $k = 0$  

41. **(Reto)** Si $x_1$ y $x_2$ son raíces de $x^2 - x - 1 = 0$, demostrar que $x_n = x_1^n + x_2^n$ genera la sucesión de Lucas (asociada a Fibonacci). Calcular el valor de $x_5 = x_1^5 + x_2^5$:  
A) $11$  
B) $9$  
C) $13$  
D) $15$  
E) $7$  

42. **(Reto)** Para qué valores reales del parámetro $m$ las dos raíces de la ecuación $x^2 - 2(m - 1)x + (2m + 1) = 0$ son ambas estrictamente positivas:  
A) $m \geq 4$  
B) $m > 1$  
C) $m \in \langle -\infty, -1/2 \rangle$  
D) $m \in \langle 4, +\infty \rangle$  
E) $m \geq 4 \lor m \leq 0$  

43. **(Reto)** Resolver en $\mathbb{R}$ la ecuación:
$$
\sqrt{x^2 - 3x + 6} + \sqrt{x^2 - 3x - 1} = 7
$$
A) $\{-2, 5\}$  
B) $\{-1, 4\}$  
C) $\{2, 3\}$  
D) $\{1, -4\}$  
E) $\{-3, 6\}$  

44. **(Reto)** Si la ecuación cuadrática $x^2 + ax + b = 0$ tiene por raíces a $\tan(\theta)$ y $\tan(\phi)$, y la ecuación $x^2 + cx + d = 0$ tiene por raíces a $\cot(\theta)$ y $\cot(\phi)$, expresar $c$ y $d$ en función de $a$ y $b$:  
A) $c = \frac{a}{b}, d = \frac{1}{b}$  
B) $c = -\frac{a}{b}, d = \frac{1}{b}$  
C) $c = \frac{b}{a}, d = b$  
D) $c = -\frac{b}{a}, d = \frac{1}{b}$  
E) $c = a b, d = b^2$  

45. **(Reto)** Un canal de irrigación para parcelas comunales tiene sección transversal en forma de trapecio isósceles con base menor de $2\text{ m}$ y lados inclinados en ángulo de $45^\circ$. Si el área de la sección transversal debe ser de $12\text{ m}^2$ para permitir el caudal requerido en épocas de estiaje, ¿cuál debe ser la profundidad del canal en metros?  
A) $2\text{ m}$  
B) $3\text{ m}$  
C) $4\text{ m}$  
D) $2.5\text{ m}$  
E) $3.5\text{ m}$  

---

## 6. Claves de Respuestas y Pistas Estratégicas

### Claves de Respuestas

| N° | Clave | N° | Clave | N° | Clave | N° | Clave | N° | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **10** | C | **19** | B | **28** | C | **37** | A |
| **2** | C | **11** | A | **20** | A | **29** | C | **38** | C |
| **3** | B | **12** | B | **21** | C | **30** | A | **39** | A |
| **4** | A | **13** | B | **22** | B | **31** | B | **40** | B |
| **5** | C | **14** | A | **23** | A | **32** | B | **41** | A |
| **6** | A | **15** | D | **24** | A | **33** | A | **42** | A |
| **7** | B | **16** | A | **25** | A | **34** | A | **43** | A |
| **8** | A | **17** | A | **26** | D | **35** | C | **44** | A |
| **9** | B | **18** | C | **27** | A | **36** | C | **45** | B |

---

### Pistas Estratégicas para Ejercicios Reto (41 al 45)

* **Pista 41:** Observa que de la ecuación $x^2 = x + 1$, multiplicando por $x^{n-2}$ se cumple $x^n = x^{n-1} + x^{n-2}$. Sumando para ambas raíces se tiene la relación de recurrencia lineal $x_n = x_{n-1} + x_{n-2}$. Como $x_1 = S = 1$ y $x_2 = S^2 - 2P = 1 - 2(-1) = 3$, calcula inductivamente $x_3 = 4$, $x_4 = 7$ y $x_5 = 11$.
* **Pista 42:** Para que ambas raíces sean estrictamente positivas deben cumplirse tres condiciones simultáneas:
1) $\Delta \geq 0$ (raíces reales),
2) $S = x_1 + x_2 > 0$ (suma positiva),
3) $P = x_1 \cdot x_2 > 0$ (producto positivo).
Interseca los tres intervalos resultantes.
* **Pista 43:** Sea $y = x^2 - 3x$. Observa que la diferencia entre los radicandos es $(y + 6) - (y - 1) = 7$. Multiplica y divide por la expresión conjugada o eleva al cuadrado mediante el cambio de variable auxiliar $u = \sqrt{y + 6}$ y $v = \sqrt{y - 1}$.
* **Pista 44:** Recuerda que $\cot(\theta) + \cot(\phi) = \frac{\tan(\theta) + \tan(\phi)}{\tan(\theta)\tan(\phi)} = \frac{-a}{b}$. Por Cardano-Vieta en la segunda ecuación, la suma es $-c$, luego $-c = \frac{-a}{b} \implies c = \frac{a}{b}$. Del mismo modo, el producto es $\cot(\theta)\cot(\phi) = \frac{1}{\tan(\theta)\tan(\phi)} = \frac{1}{b} = d$.
* **Pista 45:** Si la profundidad del canal es $h$, debido a los ángulos de $45^\circ$, cada ensanchamiento lateral en la superficie es $h$. Por tanto, la base mayor del trapecio es $B = 2 + 2h$. La fórmula del área del trapecio es $\text{Área} = \frac{(B + b)}{2} \cdot h = \frac{(2 + 2h + 2)}{2} \cdot h = (h + 2)h = 12$. Resuelve la ecuación cuadrática $h^2 + 2h - 12 = 0$.

---

## 7. Formulario Resumen

| Concepto / Teorema | Expresión Matemática | Condiciones y Notas |
| :--- | :--- | :--- |
| **Forma Canónica** | $ax^2 + bx + c = 0$ | $a, b, c \in \mathbb{R}$, con $a \neq 0$ obligatoriamente |
| **Fórmula Cuadrática** | $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ | Válida para cualquier ecuación cuadrática en $\mathbb{C}$ |
| **Discriminante ($\Delta$)** | $\Delta = b^2 - 4ac$ | Determina la naturaleza y multiplicidad de las raíces |
| **Dos Raíces Reales Distintas** | $\Delta > 0$ | La parábola interseca al eje $X$ en dos puntos |
| **Raíz Real Doble (Única)** | $\Delta = 0$ | $x_1 = x_2 = -\frac{b}{2a}$, trinomio cuadrado perfecto |
| **Raíces Complejas Conjugadas** | $\Delta < 0$ | No existen raíces en $\mathbb{R}$, parábola no toca eje $X$ |
| **Cardano: Suma de Raíces ($S$)** | $x_1 + x_2 = -\frac{b}{a}$ | Relación lineal entre coeficientes |
| **Cardano: Producto de Raíces ($P$)** | $x_1 \cdot x_2 = \frac{c}{a}$ | Relación con el término independiente |
| **Diferencia de Raíces ($D$)** | $\|x_1 - x_2\| = \frac{\sqrt{\Delta}}{\|a\|}$ | Se deduce de la identidad de Legendre para $\Delta \geq 0$ |
| **Suma de Inversas** | $\frac{1}{x_1} + \frac{1}{x_2} = -\frac{b}{c}$ | Requiere $c \neq 0$ (ninguna raíz nula) |
| **Suma de Cuadrados** | $x_1^2 + x_2^2 = S^2 - 2P$ | Deducción de $(x_1 + x_2)^2 = x_1^2 + 2x_1 x_2 + x_2^2$ |
| **Suma de Cubos** | $x_1^3 + x_2^3 = S^3 - 3PS$ | Deducción de $(x_1 + x_2)^3$ |
| **Reconstrucción de Ecuación** | $x^2 - Sx + P = 0$ | Ecuación mónica a partir de suma y producto conocidos |
| **Raíces Simétricas (Opuestas)** | $x_1 + x_2 = 0 \iff b = 0$ | Ecuación cuadrática pura sin término lineal |
| **Raíces Recíprocas (Inversas)** | $x_1 \cdot x_2 = 1 \iff a = c$ | Coeficiente principal igual al término independiente |
| **Ecuaciones Equivalentes** | $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Comparten exactamente el mismo conjunto solución |
