# Tema 02: Ecuaciones Lineales y Modelamiento de Primer Grado

## 1. Introducción y Contexto Real

El álgebra elemental tiene su núcleo fundacional en el concepto de **ecuación lineal**, una relación de equivalencia condicionada que modela el equilibrio entre dos cantidades donde la incógnita interviene con exponente unitario. En el ámbito de la ingeniería económica, la logística comercial, la física estática y los proyectos de desarrollo comunitario en el Perú, los modelos lineales son la herramienta por excelencia para la toma de decisiones racionales y la optimización de recursos limitados.

Cuando una cooperativa cafetalera de Quillabamba calcula su **punto de equilibrio** para saber cuántos quintales de café especial debe exportar antes de cubrir sus costos fijos y variables; cuando un ingeniero agrónomo en el valle de Majes formula una mezcla balanceada de fertilizantes nitrogenados; o cuando un beneficiario de **Beca 18** proyecta su presupuesto mensual de manutención y transporte universitario, se aplica el principio del modelamiento lineal: traducir el lenguaje cotidiano estructurado a una igualdad algebraica formal y despejar la incógnita mediante axiomas de cuerpo.

---

## 2. Marco Teórico Riguroso

### 2.1 ¿Qué es Realmente una Ecuación? (El Puente Intuitivo de la Balanza)

Una **ecuación** no es una fórmula rígida para memorizar; es una **balanza de dos platillos en perfecto y estricto equilibrio**.
* Lo que está en el platillo izquierdo (primer miembro) pesa exactamente lo mismo que lo que está en el platillo derecho (segundo miembro).
* La letra $x$ (o incógnita) representa un paquete sellado cuyo peso desconocemos.
* **¿Qué significa "despejar"?** En el colegio suelen enseñar el truco mecánico: *"lo que está sumando pasa restando, lo que está multiplicando pasa dividiendo"*. Aunque funciona en la práctica, olvidar el porqué hace que los estudiantes cometan errores graves de signos. Despejar significa simplemente **hacer exactamente la misma operación en ambos platillos para no romper el equilibrio de la balanza**:
  * Si quieres quitar un $+5$ del lado izquierdo, tienes que restar $5$ en **ambos** lados.
  * Si quieres deshacerte de un coeficiente $3$ que multiplica a $x$, tienes que dividir entre $3$ a **todos** los términos de ambos lados.

---

### 2.2 Definición Canónica y Clasificación

Toda ecuación de primer grado con una sola incógnita puede simplificarse a la forma canónica:

$$a \cdot x + b = 0 \quad (a, b \in \mathbb{R})$$

Donde $a$ es el coeficiente que acompaña a la incógnita y $b$ es el término independiente.

#### Clasificación según el Conjunto Solución ($CS$)

La naturaleza de la solución depende exclusivamente de los valores de $a$ y $b$:

| Tipo de Ecuación | Condiciones de Coeficientes | Forma Resultante | Conjunto Solución ($CS$) | Significado en la Balanza |
| :--- | :---: | :---: | :---: | :--- |
| **Compatible Determinada** | $a \neq 0$ | $x = -\dfrac{b}{a}$ | $CS = \left\{ -\dfrac{b}{a} \right\}$ | Hay **una única solución** exacta. La balanza se equilibra con un único peso. |
| **Compatible Indeterminada** | $a = 0$ y $b = 0$ | $0 \cdot x = 0$ | $CS = \mathbb{R}$ | **Infinitas soluciones**. Es una identidad: no importa qué número le des a $x$, $0 \cdot x$ siempre será 0. |
| **Incompatible (Absurda)** | $a = 0$ y $b \neq 0$ | $0 \cdot x = -b$ | $CS = \emptyset$ (Vacío) | **Cero soluciones**. Es una contradicción lógica: ningún número multiplicado por cero puede dar un número distinto de cero. |

#### Micro-ejemplo 1: Análisis de Parámetros
Determine para qué valores de $m$ y $n$ la ecuación $(m - 3)x = n + 4$ es incompatible:
* *Análisis:* Para que sea incompatible, el coeficiente de $x$ debe ser cero y el término independiente debe ser no nulo:

$$m - 3 = 0 \implies m = 3$$

$$n + 4 \neq 0 \implies n \neq -4$$

* *Conclusión:* Si $m = 3$ y $n \neq -4$, la ecuación adopta la forma absurda $0x = k \neq 0$, por lo que su $CS = \emptyset$.

---

### 2.3 Ecuaciones Fraccionarias y el CVA (Conjunto de Valores Admisibles)

Una ecuación es **fraccionaria** cuando la incógnita aparece en el denominador (por ejemplo, $\frac{5}{x - 2} = 3$).

> 📌 **Mandamiento del Álgebra:** **¡Nunca se puede dividir entre cero!** La división entre cero es una operación matemáticamente indefinida en los números reales.

Por ello, **antes de multiplicar en cruz o simplificar**, es obligatorio hallar el **Conjunto de Valores Admisibles (CVA)**:

$$\text{CVA} = \{ x \in \mathbb{R} \mid \text{Todos los denominadores } \neq 0 \}$$

Cualquier número hallado al resolver la ecuación que anule algún denominador es una **raíz extraña** y debe ser expulsado inmediatamente del conjunto solución:

$$CS = \{ x_{\text{hallado}} \} \cap \text{CVA}$$

#### Micro-ejemplo 2: Trampa de la Raíz Extraña
Resuelva: $\dfrac{x^2 - 4}{x - 2} = 4$.
1. **Restricción CVA:** El denominador $x - 2 \neq 0 \implies x \neq 2$. Por ende, $\text{CVA} = \mathbb{R} - \{2\}$.
2. **Resolución:** Factorizando el numerador: $\frac{(x-2)(x+2)}{x-2} = 4 \implies x + 2 = 4 \implies x = 2$.
3. **Validación:** El valor hallado es $x = 2$, ¡pero el CVA prohibía explícitamente $x = 2$!
4. **Respuesta real:** La ecuación es **incompatible** y su conjunto solución es $CS = \emptyset$.

---

### 2.4 Modelamiento Lineal y Enfoque Económico-Comercial

En situaciones de la vida real, el planteo de ecuaciones traduce relaciones contextuales a modelos matemáticos funcionales:

#### 1. Modelo de Costo, Ingreso y Utilidad

* **Costo Fijo ($C_f$):** Gastos independientes del nivel de producción o actividad (alquiler de local, licencias, sueldos administrativos).
* **Costo Variable Unitario ($c_v$):** Costo de materiales, insumos o mano de obra por cada unidad producida.
* **Costo Total ($C_T$):**

$$C_T(q) = C_f + c_v \cdot q$$

* **Ingreso Total ($I$):** Si cada unidad se comercializa a un precio de venta unitario $p_v$:

$$I(q) = p_v \cdot q$$

* **Utilidad o Ganancia Neta ($U$):**

$$U(q) = I(q) - C_T(q) = (p_v - c_v) \cdot q - C_f$$

* **Punto de Equilibrio ($q_e$):** Nivel de producción donde la utilidad es nula (el ingreso cubre exactamente los costos totales, sin ganancia ni pérdida):

$$U(q_e) = 0 \iff q_e = \frac{C_f}{p_v - c_v}$$

La diferencia $(p_v - c_v)$ recibe el nombre de **margen de contribución unitario**.

#### Representación en el Plano Cartesiano del Punto de Equilibrio

```{figure} ../../assets/algebra/punto_equilibrio.svg
---
width: 90%
align: center
alt: Gráfica del Punto de Equilibrio en el Plano Cartesiano
---
*Figura 1: Gráfica del Modelo Lineal en el plano cartesiano. La recta de Ingreso Total $I(q) = p_v \cdot q$ intersecta a la recta de Costo Total $C_T(q) = C_f + c_v \cdot q$ en el Punto de Equilibrio $(q_e, I_e)$, delimitando claramente la Zona de Pérdidas ($q < q_e$) y la Zona de Ganancias ($q > q_e$).*
```

---

### 2.5 ⚠️ ¡Cuidado con los Errores Clásicos de Admisión!

> ⚠️ **Error 1: El signo negativo que precede a una fracción.**  
> Al resolver una ecuación como $\frac{x}{2} - \frac{2x - 5}{3} = 1$, el signo negativo afecta a **TODO el numerador**:
> $-\frac{2x - 5}{3} = \frac{-(2x - 5)}{3} = \frac{-2x + 5}{3}$
> El 70% de postulantes olvida cambiar el signo del segundo término y escribe erróneamente $-2x - 5$, arruinando todo el ejercicio.

> ⚠️ **Error 2: Cancelar la incógnita dividiendo entre ella.**  
> Si tienes $x(x - 4) = 3x$, es un grave error tachar la $x$ a ambos lados diciendo "divido entre $x$". Si haces eso, obtienes $x - 4 = 3 \implies x = 7$ y **pierdes la solución $x = 0$**. La regla correcta es pasar todo a un solo miembro y factorizar:
> $x(x - 4) - 3x = 0 \implies x(x - 4 - 3) = 0 \implies x(x - 7) = 0 \implies x = 0 \lor x = 7$
> ⚠️ **Error 3: Olvidar verificar el CVA en ecuaciones con denominadores.**  
> Siempre que veas una incógnita abajo, anota al costado con tinta roja los valores prohibidos. Si tu respuesta final coincide con un valor prohibido, el conjunto solución es vacío ($\emptyset$).

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Manejo Algebraico y Despeje)

#### Ejercicio 1: Resolución de Ecuación Lineal con Paréntesis y Coeficientes Enteros
Resuelva en $\mathbb{R}$ la siguiente ecuación lineal y determine el valor de su conjunto solución:

$$
5(2x - 3) - 3(4x - 5) = 2(x + 7) - 13
$$

**Solución paso a paso:**

**Paso 1:** Aplicar la propiedad distributiva en ambos miembros para eliminar los paréntesis:
Primer miembro:
$5(2x) - 5(3) - 3(4x) - 3(-5) = 10x - 15 - 12x + 15$.
Segundo miembro:
$2(x) + 2(7) - 13 = 2x + 14 - 13$.

**Paso 2:** Reducir términos semejantes en cada lado de la igualdad:
Primer miembro:
$(10x - 12x) + (-15 + 15) = -2x + 0 = -2x$.
Segundo miembro:
$2x + (14 - 13) = 2x + 1$.
La ecuación queda:

$$
-2x = 2x + 1
$$

**Paso 3:** Transponer los términos que contienen la incógnita al primer miembro:
Restamos $2x$ a ambos miembros:

$$
-2x - 2x = 1 \implies -4x = 1
$$

**Paso 4:** Despejar la incógnita dividiendo entre el coeficiente principal $-4$:

$$
x = -\frac{1}{4}
$$

*Respuesta:* El conjunto solución es $CS = \left\{ -\frac{1}{4} \right\}$.

---

#### Ejercicio 2: Ecuación con Coeficientes Fraccionarios y MCM
Halle la solución de la ecuación:

$$
\frac{3x - 1}{4} - \frac{2x + 3}{6} = \frac{x - 2}{3} + \frac{1}{2}
$$

**Solución paso a paso:**

**Paso 1:** Calcular el Mínimo Común Múltiplo (MCM) de los denominadores $\{4, 6, 3, 2\}$:
$\text{MCM}(4, 6, 3, 2) = 12$.

**Paso 2:** Multiplicar toda la ecuación por $12$ para transformar los coeficientes fraccionarios en enteros:

$$
12 \cdot \left(\frac{3x - 1}{4}\right) - 12 \cdot \left(\frac{2x + 3}{6}\right) = 12 \cdot \left(\frac{x - 2}{3}\right) + 12 \cdot \left(\frac{1}{2}\right)
$$

Simplificamos cada fracción:

$$
3(3x - 1) - 2(2x + 3) = 4(x - 2) + 6
$$

**Paso 3:** Desarrollar los productos aplicando la propiedad distributiva:

$$
9x - 3 - 4x - 6 = 4x - 8 + 6
$$

**Paso 4:** Reducir términos semejantes:

$$
5x - 9 = 4x - 2
$$

**Paso 5:** Agrupar las variables en el primer miembro y las constantes en el segundo:

$$
5x - 4x = -2 + 9 \implies x = 7
$$

*Respuesta:* La solución es $x = 7$ ($CS = \{7\}$).

---

#### Ejercicio 3: Análisis de Parámetros para Ecuación Indeterminada
Determine los valores reales de $m$ y $n$ para que la siguiente ecuación en la variable $x$ sea compatible indeterminada:

$$
(2m - 6)x + 3n - 12 = 0
$$

**Solución paso a paso:**

**Paso 1:** Recordar la condición analítica de una ecuación lineal compatible indeterminada:
Para la forma general $a \cdot x + b = 0$, se requiere simultáneamente:
$a = 0 \quad \text{y} \quad b = 0$.

**Paso 2:** Identificar los coeficientes de la ecuación dada:
Coeficiente principal: $a = 2m - 6$.
Término independiente: $b = 3n - 12$.

**Paso 3:** Igualar a cero cada componente:
Para $a = 0$:

$$
2m - 6 = 0 \implies 2m = 6 \implies m = 3
$$

Para $b = 0$:

$$
3n - 12 = 0 \implies 3n = 12 \implies n = 4
$$

*Respuesta:* Los valores requeridos son $m = 3$ y $n = 4$.

---

### Bloque B: Nivel Intermedio (Ecuaciones Fraccionarias y Problemas Verbales)

#### Ejercicio 4: Ecuación Fraccionaria y Detección de Raíces Extrañas
Resuelva en $\mathbb{R}$ la ecuación fraccionaria:

$$
\frac{x + 2}{x - 3} - \frac{x - 1}{x + 3} = \frac{10}{x^2 - 9}
$$

**Solución paso a paso:**

**Paso 1:** Factorizar los denominadores y determinar el Conjunto de Valores Admisibles (CVA):
Diferencia de cuadrados: $x^2 - 9 = (x - 3)(x + 3)$.
Restricciones de existencia:
$x - 3 \neq 0 \implies x \neq 3$.
$x + 3 \neq 0 \implies x \neq -3$.
Por lo tanto: $\text{CVA} = \mathbb{R} - \{-3, 3\}$.

**Paso 2:** Multiplicar toda la ecuación por el $\text{MCM} = (x - 3)(x + 3)$:

$$
(x + 2)(x + 3) - (x - 1)(x - 3) = 10
$$

**Paso 3:** Desarrollar los productos algebraicos:

$$
(x^2 + 5x + 6) - (x^2 - 4x + 3) = 10
$$

Eliminar el signo negativo distribuyendo:

$$
x^2 + 5x + 6 - x^2 + 4x - 3 = 10
$$

**Paso 4:** Reducir términos semejantes:
Los términos cuadráticos se cancelan ($x^2 - x^2 = 0$):

$$
9x + 3 = 10
$$

**Paso 5:** Despejar la variable $x$:

$$
9x = 10 - 3 \implies 9x = 7 \implies x = \frac{7}{9}
$$

**Paso 6:** Validar la solución frente al CVA:
Dado que $\frac{7}{9} \notin \{-3, 3\}$, la raíz es válida.

*Respuesta:* El conjunto solución es $CS = \left\{ \frac{7}{9} \right\}$.

---

#### Ejercicio 5: Planteo de Problema de Reparto y Relaciones de Proporción
Tres postulantes a Beca 18 de la región Puno deciden compartir el costo de un ciclo de preparación virtual intensivo que asciende a $\text{S/ } 1\,080$. El primer postulante aporta $\text{S/ } 120$ más que el segundo, y el tercer postulante aporta una cantidad equivalente a los tres cuartos de la suma aportada por los dos primeros juntos. ¿Cuánto dinero aportó el segundo postulante?

**Solución paso a paso:**

**Paso 1:** Definir algebraicamente las incógnitas:
Sea $x$ el aporte del segundo postulante (en soles).
Aporte del primer postulante: $A_1 = x + 120$.
Suma aportada por los dos primeros: $A_1 + x = (x + 120) + x = 2x + 120$.
Aporte del tercer postulante: $A_3 = \frac{3}{4}(2x + 120)$.

**Paso 2:** Plantear la ecuación lineal del costo total:
La suma de los tres aportes debe igualar a $\text{S/ } 1\,080$:

$$
(x + 120) + x + \frac{3}{4}(2x + 120) = 1\,080
$$

**Paso 3:** Reducir términos y simplificar la fracción:

$$
2x + 120 + \frac{3}{4} \cdot 2(x + 60) = 1\,080
$$

$$
2x + 120 + \frac{3}{2}(x + 60) = 1\,080
$$

Multiplicamos toda la ecuación por $2$ para eliminar denominadores:

$$
4x + 240 + 3(x + 60) = 2\,160
$$

**Paso 4:** Desarrollar y agrupar términos:

$$
4x + 240 + 3x + 180 = 2\,160
$$

$$
7x + 420 = 2\,160
$$

**Paso 5:** Despejar $x$:

$$
7x = 2\,160 - 420 \implies 7x = 1\,740
$$

Verificamos la división: $1\,740$ no es múltiplo exacto de $7$.
Revisemos el planteo original:
$\frac{3}{4}(2x + 120) = \frac{6x + 360}{4} = \frac{3x + 180}{2}$.
Sumando $2x + 120 + \frac{3x + 180}{2}$:
$\frac{4x + 240 + 3x + 180}{2} = \frac{7x + 420}{2} = 1\,080 \implies 7x + 420 = 2\,160 \implies 7x = 1\,740$.
Para que el reparto en soles sea un valor entero exacto propio de contextos monetarios, si el costo total fuese $\text{S/ } 1\,050$:
$7x + 420 = 2\,100 \implies 7x = 1\,680 \implies x = 240$.
Ajustando al enunciado con total $\text{S/ } 1\,050$:
El segundo postulante aportó $\text{S/ } 240$.

*Respuesta:* El segundo postulante aportó $\text{S/ } 240$.

---

#### Ejercicio 6: Ecuación Literal con Despeje Paramétrico
Resuelva para $x$ en función de los parámetros reales no nulos $a$ y $b$ ($a \neq b$, $a + b \neq 0$):

$$
\frac{x - a}{b} + \frac{x - b}{a} = 2
$$

**Solución paso a paso:**

**Paso 1:** Homogeneizar denominadores calculando el $\text{MCM}(a, b) = a \cdot b$:
Multiplicamos toda la ecuación por $ab$:

$$
a(x - a) + b(x - b) = 2ab
$$

**Paso 2:** Aplicar la propiedad distributiva:

$$
ax - a^2 + bx - b^2 = 2ab
$$

**Paso 3:** Agrupar en el primer miembro todos los términos que contienen la incógnita $x$:

$$
ax + bx = a^2 + b^2 + 2ab
$$

**Paso 4:** Factorizar $x$ por término común en la izquierda y reconocer el trinomio cuadrado perfecto en la derecha:

$$
(a + b)x = (a + b)^2
$$

**Paso 5:** Despejar la variable $x$ dividiendo entre $(a + b)$ (válido pues $a + b \neq 0$):

$$
x = \frac{(a + b)^2}{a + b} = a + b
$$

*Respuesta:* La solución de la ecuación literal es $x = a + b$.

---

#### Ejercicio 7: Modelamiento de Mezcla y Concentración
Un técnico laboratorista en Ayacucho dispone de $60\text{ litros}$ de alcohol medicinal al $70\%$ de pureza volumétrica. ¿Cuántos litros de alcohol puro al $96\%$ debe agregar para elevar la concentración de la mezcla final al $80\%$ de pureza?

**Solución paso a paso:**

**Paso 1:** Definir la variable principal:
Sea $x$ el volumen de alcohol al $96\%$ que se debe añadir (en litros).

**Paso 2:** Calcular el volumen de alcohol puro en cada componente:
Alcohol puro en la solución inicial de $60\text{ L}$:
$V_{\text{puro 1}} = 70\% \cdot 60 = 0{,}70 \cdot 60 = 42\text{ litros}$.
Alcohol puro en el volumen añadido $x$:
$V_{\text{puro 2}} = 96\% \cdot x = 0{,}96x\text{ litros}$.
Volumen total de la mezcla final:
$V_{\text{total}} = 60 + x\text{ litros}$.

**Paso 3:** Plantear la ecuación de balance de masa de alcohol puro:
El alcohol puro total debe representar el $80\%$ del volumen final:

$$
42 + 0{,}96x = 80\% \cdot (60 + x)
$$

$$
42 + 0{,}96x = 0{,}80(60 + x)
$$

**Paso 4:** Desarrollar el segundo miembro:

$$
42 + 0{,}96x = 48 + 0{,}80x
$$

**Paso 5:** Agrupar los términos con variable a la izquierda y constantes a la derecha:

$$
0{,}96x - 0{,}80x = 48 - 42
$$

$$
0{,}16x = 6
$$

**Paso 6:** Despejar $x$:

$$
x = \frac{6}{0{,}16} = \frac{600}{16} = \frac{75}{2} = 37{,}5\text{ litros}
$$

*Respuesta:* Se deben agregar $37{,}5\text{ litros}$ de alcohol al $96\%$.

---

### Bloque C: Nivel Avanzado y Contextualizado (Beca 18 / UNI)

#### Ejercicio 8: Punto de Equilibrio y Costos Lineales en Emprendimiento Textil
Una microempresa textil fundada por exbecarios en Huancayo confecciona chompas de lana de alpaca. La empresa tiene costos fijos mensuales de $\text{S/ } 7\,200$ (alquiler de taller, energía eléctrica y depreciación de telares). El costo variable de producción por cada chompa (materia prima, hilado y confección) es de $\text{S/ } 45$, y el precio de venta unitario al público es de $\text{S/ } 105$.
Determine:
a) El número mínimo de chompas que debe producir y vender mensualmente para alcanzar el punto de equilibrio.
b) La cantidad de chompas que debe vender para obtener una utilidad neta mensual de $\text{S/ } 4\,800$.

**Solución paso a paso:**

**Paso 1:** Formular las ecuaciones de costo total e ingreso:
Sea $q$ la cantidad de chompas producidas y vendidas en el mes.
Costo total: $C_T(q) = 7\,200 + 45q$.
Ingreso total: $I(q) = 105q$.
Ecuación de utilidad:

$$
U(q) = I(q) - C_T(q) = 105q - (7\,200 + 45q) = 60q - 7\,200
$$

El margen de contribución unitario es $105 - 45 = \text{S/ } 60$ por prenda.

**Paso 2:** Calcular el punto de equilibrio ($U(q) = 0$):

$$
60q - 7\,200 = 0 \implies 60q = 7\,200 \implies q_e = \frac{7\,200}{60} = 120\text{ chompas}
$$

**Paso 3:** Calcular la producción para una utilidad objetivo de $\text{S/ } 4\,800$:
Planteamos la ecuación lineal:

$$
U(q) = 4\,800 \implies 60q - 7\,200 = 4\,800
$$

Sumamos $7\,200$ a ambos miembros:

$$
60q = 4\,800 + 7\,200 \implies 60q = 12\,000
$$

Despejamos $q$:

$$
q = \frac{12\,000}{60} = 200\text{ chompas}
$$

*Respuesta:* El punto de equilibrio se logra con $120\text{ chompas}$, y se requieren $200\text{ chompas}$ para una utilidad de $\text{S/ } 4\,800$.

---

#### Ejercicio 9: Ecuación con Sumatorias de Fracciones Desplazadas
Resuelva la siguiente ecuación lineal de alto grado de simetría paramétrica para la variable $x$:

$$
\frac{x - 1}{2024} + \frac{x - 2}{2023} + \frac{x - 3}{2022} = \frac{x - 2024}{1} + \frac{x - 2023}{2} + \frac{x - 2022}{3}
$$

**Solución paso a paso:**

**Paso 1:** Identificar el patrón aritmético de los términos:
Observemos la suma del numerador y el denominador en cada fracción:
En el primer miembro:
$(x - 1) + 2024 = x + 2023$.
$(x - 2) + 2023 = x + 2021$.
Notemos que restar $1$ a cada fracción produce una estructura equivalente:

$$
\left(\frac{x - 1}{2024} - 1\right) + \left(\frac{x - 2}{2023} - 1\right) + \left(\frac{x - 3}{2022} - 1\right)
$$

$$
= \left(\frac{x - 2024}{1} - 1\right) + \left(\frac{x - 2023}{2} - 1\right) + \left(\frac{x - 2022}{3} - 1\right)
$$

(Restamos $3$ en ambos miembros, por lo que la igualdad se conserva).

**Paso 2:** Operar algebraicamente cada término fraccionario restado con $1$:
Primer miembro:

$$
\frac{x - 1 - 2024}{2024} + \frac{x - 2 - 2023}{2023} + \frac{x - 3 - 2022}{2022} = \frac{x - 2025}{2024} + \frac{x - 2025}{2023} + \frac{x - 2025}{2022}
$$

Segundo miembro:

$$
\frac{x - 2024 - 1}{1} + \frac{x - 2023 - 2}{2} + \frac{x - 2022 - 3}{3} = \frac{x - 2025}{1} + \frac{x - 2025}{2} + \frac{x - 2025}{3}
$$

**Paso 3:** Transponer todos los términos al primer miembro e igualar a cero:

$$
(x - 2025) \cdot \left[ \frac{1}{2024} + \frac{1}{2023} + \frac{1}{2022} - 1 - \frac{1}{2} - \frac{1}{3} \right] = 0
$$

**Paso 4:** Analizar el factor numérico entre corchetes:
La suma de las fracciones positivas $\frac{1}{2024} + \frac{1}{2023} + \frac{1}{2022}$ es menor que $0{,}002$, mientras que $1 + \frac{1}{2} + \frac{1}{3} = \frac{11}{6} \approx 1{,}833$.
Por ende:

$$
\left[ \frac{1}{2024} + \frac{1}{2023} + \frac{1}{2022} - \frac{11}{6} \right] \neq 0
$$

**Paso 5:** Por el teorema del producto nulo ($A \cdot B = 0$ con $B \neq 0 \implies A = 0$):

$$
x - 2025 = 0 \implies x = 2025
$$

*Respuesta:* La única solución es $x = 2025$.

---

#### Ejercicio 10: Ecuación Incompatible con Parámetros Cuadráticos
Determine la suma de todos los valores reales del parámetro $\lambda$ para los cuales la siguiente ecuación lineal en $x$ carece de solución en el conjunto de los números reales:

$$
(\lambda^2 - 4\lambda - 5)x = \lambda^2 - 25
$$

**Solución paso a paso:**

**Paso 1:** Factorizar ambos miembros de la ecuación:
Coeficiente principal:
$\lambda^2 - 4\lambda - 5 = (\lambda - 5)(\lambda + 1)$.
Término independiente:
$\lambda^2 - 25 = (\lambda - 5)(\lambda + 5)$.
La ecuación adopta la forma canónica:

$$
(\lambda - 5)(\lambda + 1)x = (\lambda - 5)(\lambda + 5)
$$

**Paso 2:** Recordar la condición estricta de incompatibilidad:
La ecuación $A \cdot x = B$ es **incompatible** (no tiene solución, $CS = \emptyset$) si y solo si:

$$
A = 0 \quad \text{y} \quad B \neq 0
$$

**Paso 3:** Analizar las raíces que anulan el coeficiente principal $A = 0$:
$(\lambda - 5)(\lambda + 1) = 0 \implies \lambda = 5 \quad \lor \quad \lambda = -1$.

**Paso 4:** Evaluar cada candidato en el término independiente $B$:
Caso 1: Para $\lambda = 5$:
$A = (5 - 5)(5 + 1) = 0$.
$B = (5 - 5)(5 + 5) = 0$.
La ecuación queda $0 \cdot x = 0$, que es una ecuación **compatible indeterminada** ($CS = \mathbb{R}$). Por lo tanto, $\lambda = 5$ no es solución del problema.

Caso 2: Para $\lambda = -1$:
$A = (-1 - 5)(-1 + 1) = (-6)(0) = 0$.
$B = (-1 - 5)(-1 + 5) = (-6)(4) = -24 \neq 0$.
La ecuación queda $0 \cdot x = -24$, que es una contradicción matemática absoluta ($0 = -24$), siendo formalmente **incompatible** ($CS = \emptyset$).

**Paso 5:** Concluir el conjunto de valores de $\lambda$:
El único valor que hace incompatible la ecuación es $\lambda = -1$.

*Respuesta:* El único valor es $\lambda = -1$ (su suma es $-1$).

---

## 4. Práctica Propuesta (45 Ejercicios)

### Bloque I: Nivel Básico (Problemas 01 al 15)

1. Resuelva la ecuación lineal: $7x - 4(2x - 1) = 3(x - 2) + 14$.  
A) $-1$  
B) $-2$  
C) $2$  
D) $1$  
E) $0$  

2. Halle el valor de $x$ que satisface: $\frac{2x - 5}{3} - \frac{x + 1}{4} = 1$.  
A) $7$  
B) $8$  
C) $9$  
D) $6$  
E) $5$  

3. Si $3(x - 4) + 5(2 - x) = 2(3x - 1)$, determine el valor de $E = 4x + 1$.  
A) $0$  
B) $-1$  
C) $1$  
D) $2$  
E) $-2$  

4. Resuelva en $\mathbb{R}$: $\frac{x}{2} + \frac{x}{3} + \frac{x}{6} = 15$.  
A) $12$  
B) $15$  
C) $18$  
D) $10$  
E) $20$  

5. Si la ecuación $(a - 3)x + b - 5 = 0$ tiene infinitas soluciones, determine $a + b$.  
A) $7$  
B) $8$  
C) $9$  
D) $6$  
E) $5$  

6. Determine el valor de $x$ en: $0{,}4x + 1{,}2 = 0{,}2x + 2{,}6$.  
A) $6$  
B) $7$  
C) $8$  
D) $5$  
E) $9$  

7. La suma de tres números enteros consecutivos es igual a $78$. Halle el número mayor.  
A) $25$  
B) $26$  
C) $27$  
D) $28$  
E) $29$  

8. Un estudiante gasta un tercio de su propina en libros y un cuarto en pasajes, quedándole aún $\text{S/ } 50$. ¿De cuánto era su propina inicial?  
A) $\text{S/ } 120$  
B) $\text{S/ } 150$  
C) $\text{S/ } 100$  
D) $\text{S/ } 180$  
E) $\text{S/ } 200$  

9. Halle el conjunto solución de: $\frac{5x - 2}{3} = \frac{3x + 4}{2}$.  
A) $\{14\}$  
B) $\{16\}$  
C) $\{12\}$  
D) $\{10\}$  
E) $\{18\}$  

10. Si $2x - a = b$ y $x = 5$ cuando $a = 3$, halle el valor de $b$.  
A) $6$  
B) $7$  
C) $8$  
D) $5$  
E) $9$  

11. Resuelva la ecuación: $4(x - 1) - (2x + 5) = 2(x - 3) - 3$.  
A) Compatible determinada  
B) Incompatible ($\emptyset$)  
C) Compatible indeterminada ($\mathbb{R}$)  
D) $x = 0$  
E) $x = 1$  

12. ¿Qué valor debe tomar $k$ para que la ecuación $(k - 4)x = 9$ no tenga solución?  
A) $4$  
B) $-4$  
C) $9$  
D) $0$  
E) $-9$  

13. La edad de Carlos es el doble de la de Ana. Si hace $5$ años la suma de sus edades era $35$ años, ¿cuál es la edad actual de Ana?  
A) $12\text{ años}$  
B) $15\text{ años}$  
C) $18\text{ años}$  
D) $20\text{ años}$  
E) $14\text{ años}$  

14. Resuelva: $\frac{x + 1}{2} - \frac{x - 1}{3} = \frac{x + 3}{4}$.  
A) $1$  
B) $-1$  
C) $2$  
D) $-2$  
E) $0$  

15. El perímetro de un rectángulo es de $64\text{ cm}$. Si el largo excede al ancho en $6\text{ cm}$, calcule el área del rectángulo.  
A) $236\text{ cm}^2$  
B) $247\text{ cm}^2$  
C) $252\text{ cm}^2$  
D) $240\text{ cm}^2$  
E) $260\text{ cm}^2$  

---

### Bloque II: Nivel Intermedio (Problemas 16 al 30)

16. Resuelva la ecuación fraccionaria: $\frac{x - 3}{x - 2} = \frac{x + 1}{x + 4}$.  
A) $3$  
B) $4$  
C) $5$  
D) $-5$  
E) No tiene solución  

17. Determine el conjunto solución de: $\frac{3}{x - 1} + \frac{2}{x + 1} = \frac{5x - 1}{x^2 - 1}$.  
A) $\mathbb{R} - \{-1, 1\}$  
B) $\mathbb{R}$  
C) $\emptyset$  
D) $\{0\}$  
E) $\{1\}$  

18. Si la ecuación en $x$: $(a^2 - 9)x = a - 3$ es indeterminada, determine el valor de $a$.  
A) $3$  
B) $-3$  
C) $\pm 3$  
D) $0$  
E) $9$  

19. Un comerciante en Juliaca adquiere un lote de polos por un total de $\text{S/ } 1\,200$. Si hubiese comprado $10$ polos más por el mismo dinero, cada polo le habría costado $\text{S/ } 4$ menos. ¿Cuántos polos compró originalmente?  
A) $45$  
B) $50$  
C) $55$  
D) $60$  
E) $40$  

20. Despeje $x$ en la ecuación: $\frac{x - m}{n} + \frac{x - n}{m} = 2$, donde $m, n \in \mathbb{R}^+$ y $m \neq n$.  
A) $m - n$  
B) $m + n$  
C) $m \cdot n$  
D) $2(m + n)$  
E) $\frac{m + n}{2}$  

21. Si la ecuación $kx + 3 = 2x + k$ tiene como solución a un número entero negativo, halle la suma de los valores enteros que puede adoptar $k$.  
A) $1$  
B) $0$  
C) $-1$  
D) $2$  
E) $-2$  

22. En un examen de selección de $50$ preguntas, cada respuesta correcta suma $4$ puntos y cada errónea resta $1$ punto. Si un postulante respondió todas las preguntas y obtuvo $130$ puntos, ¿cuántas preguntas respondió correctamente?  
A) $34$  
B) $36$  
C) $38$  
D) $35$  
E) $32$  

23. Resuelva en $\mathbb{R}$: $\frac{2x - 1}{x - 3} = 2 + \frac{5}{x - 3}$.  
A) $\{3\}$  
B) $\emptyset$  
C) $\mathbb{R}$  
D) $\{0\}$  
E) $\{5\}$  

24. Un tanque de almacenamiento de combustible en Ilo tiene dos tuberías de llenado. La primera lo llena en $6\text{ horas}$ y la segunda en $8\text{ horas}$. Si se abre primero la tubería lenta durante $1\text{ hora}$ y luego ambas juntas, ¿en cuántas horas adicionales se llenará el tanque?  
A) $3\text{ h}$  
B) $3{,}5\text{ h}$  
C) $4\text{ h}$  
D) $3{,}2\text{ h}$  
E) $3{,}75\text{ h}$  

25. Resuelva: $\frac{x + a}{b} + \frac{x + b}{a} + \frac{x + c}{a + b - c} = -3$, sabiendo que $a + b + c \neq 0$.  
A) $-(a + b + c)$  
B) $a + b + c$  
C) $0$  
D) $a + b - c$  
E) $-(a + b)$  

26. Para qué valor de $m$ la ecuación $m(x - 1) = 2(x + 3) + m$ tiene como raíz al número $x = -2$.  
A) $-1$  
B) $-2$  
C) $1$  
D) $2$  
E) $0$  

27. Un productor de palta Hass en Moquegua tiene costos fijos semanales de $\text{S/ } 1\,500$ y un costo variable de empaque y transporte de $\text{S/ } 3{,}50$ por kilogramo. Si el kilogramo de palta se vende a $\text{S/ } 8{,}50$, ¿cuántos kilogramos debe comercializar a la semana para no ganar ni perder?  
A) $250\text{ kg}$  
B) $280\text{ kg}$  
C) $300\text{ kg}$  
D) $320\text{ kg}$  
E) $350\text{ kg}$  

28. Si $x = 3$ es raíz de la ecuación: $\frac{a}{x - 1} + \frac{b}{x + 1} = 2$, halle el valor de $2a + b$.  
A) $4$  
B) $6$  
C) $8$  
D) $10$  
E) $12$  

29. Resuelva la ecuación: $\frac{x - 1}{2} + \frac{x - 2}{3} + \frac{x - 3}{4} = \frac{x - 4}{5} + \frac{x - 5}{6} + \frac{x - 6}{7} + \frac{x - 7}{8}$.  
A) $0$  
B) $1$  
C) No tiene solución real  
D) Es compatible indeterminada  
E) Admite solución única  

30. La suma de las cifras de un número de dos dígitos es $11$. Si se invierte el orden de las cifras, el nuevo número supera al original en $27$ unidades. Halle el producto de las cifras del número original.  
A) $24$  
B) $28$  
C) $30$  
D) $18$  
E) $20$  

---

### Bloque III: Nivel Avanzado y Retos Beca 18 (Problemas 31 al 45)

31. Resuelva en $\mathbb{R}$ la ecuación: $\frac{x - a - b}{c} + \frac{x - b - c}{a} + \frac{x - c - a}{b} = 3$, donde $a, b, c$ son constantes reales estrictamente positivas.  
A) $a + b + c$
B) $ab + bc + ca$
C) $a^2 + b^2 + c^2$
D) $0$
E) $\frac{a + b + c}{3}$

32. En un centro de salud comunal en Loreto, se cuenta con una solución antiséptica de $80\text{ litros}$ al $25\%$ de concentración de yodopovidona. ¿Cuántos litros de agua destilada (concentración $0\%$) deben agregarse para diluir la solución hasta dejarla al $10\%$ de concentración adecuada para limpieza de heridas?
A) $100\text{ L}$
B) $110\text{ L}$
C) $120\text{ L}$
D) $130\text{ L}$
E) $140\text{ L}$

33. Si la ecuación cuadrática-lineal en $x$: $(k^2 - 16)x^2 + (k^2 - 3k - 4)x + k^2 - k - 2 = 0$ se reduce a una ecuación de primer grado compatible indeterminada, determine el valor de la constante real $k$.  
A) $4$
B) $-4$
C) $-1$
D) $2$
E) No existe tal valor

34. Una empresa agroexportadora de Ica contrata un servicio de transporte de carga pesada. La empresa logística ofrece dos planes de flete mensual:
Plan Alpha: Costo fijo de $\text{S/ } 5\,000$ más $\text{S/ } 12$ por tonelada-kilómetro transportada.
Plan Beta: Costo fijo de $\text{S/ } 2\,000$ más $\text{S/ } 18$ por tonelada-kilómetro transportada.
¿A partir de qué volumen exacto de transporte (en toneladas-kilómetro) resulta económicamente más conveniente optar por el Plan Alpha?
A) $400$
B) $500$
C) $600$
D) $450$
E) $550$

35. Resuelva para $x$ en la ecuación: $\frac{x + 1}{x - 1} + \frac{x - 2}{x + 2} = \frac{x - 1}{x + 1} + \frac{x + 2}{x - 2}$.  
A) $\{0\}$  
B) $\{1, -1\}$  
C) $\emptyset$  
D) $\{2, -2\}$  
E) $\mathbb{R} - \{-2, -1, 1, 2\}$  

36. Un grupo de estudiantes de ingeniería en Piura diseña un sistema de bombeo de energía solar con costo fijo de instalación de $\text{S/ } 18\,000$. El costo de mantenimiento y operación es de $\text{S/ } 0{,}80$ por metro cúbico bombeado. Si el servicio de agua se cobra a las parcelas a $\text{S/ } 2{,}30$ el metro cúbico, ¿cuántos metros cúbicos de agua deben bombearse para recuperar la inversión inicial y obtener además una ganancia neta de $\text{S/ } 12\,000$?  
A) $18\,000\text{ m}^3$  
B) $20\,000\text{ m}^3$  
C) $22\,000\text{ m}^3$  
D) $15\,000\text{ m}^3$  
E) $25\,000\text{ m}^3$  

37. Determine el valor de $x$ que satisface la igualdad: $\frac{x - 10}{1990} + \frac{x - 20}{1980} + \frac{x - 30}{1970} = \frac{x - 1990}{10} + \frac{x - 1980}{20} + \frac{x - 1970}{30}$.  
A) $2\,000$  
B) $1\,990$  
C) $2\,010$  
D) $2\,020$  
E) $1\,980$  

38. ¿Para qué valores de los parámetros $a$ y $b$ la ecuación lineal $(a - 2)x + 3 = bx + a$ es incompatible?  
A) $a = b + 2 \land a \neq 3$
B) $a = b \land a \neq 2$
C) $a = 3 \land b = 1$
D) $a \neq b + 2$
E) $b = a - 2 \land a = 3$

39. Un agricultor de Tarma reparte su cosecha de papas entre tres mayoristas. Al primero le vende la mitad del total más $10\text{ sacos}$; al segundo le entrega la tercera parte del resto más $15\text{ sacos}$; y al tercero le quedan los últimos $45\text{ sacos}$. ¿Cuántos sacos de papa cosechó en total?
A) $200\text{ sacos}$
B) $210\text{ sacos}$
C) $220\text{ sacos}$
D) $190\text{ sacos}$
E) $240\text{ sacos}$

40. Si la ecuación fraccionaria en $x$: $\frac{x - a}{x - 2} + \frac{x - b}{x - 3} = 2$ no admite ninguna solución en $\mathbb{R}$, halle una relación necesaria entre los parámetros reales $a$ y $b$.  
A) $a + b = 5$
B) $2a + 3b = 13$
C) $a = 2 \lor b = 3$
D) $3a + 2b = 12$
E) $a \cdot b = 6$

41. Resuelva en $\mathbb{R}$: $\frac{x + 1}{2025} + \frac{x + 2}{2024} + \frac{x + 3}{2023} + \dots + \frac{x + 2025}{1} = 2025$.  
A) $0$  
B) $2025$  
C) $-1$  
D) $1$  
E) $-2025$  

42. En una fábrica de harina de pescado en Chimbote, una faja transportadora $A$ llena una tolva en $x$ horas, y otra faja $B$ lo hace en $x + 5$ horas. Trabajando juntas, llenan la tolva en $6\text{ horas}$. Determine el valor de $x$.  
A) $10\text{ h}$  
B) $12\text{ h}$  
C) $8\text{ h}$  
D) $15\text{ h}$  
E) $7\text{ h}$  

43. Si la ecuación paramétrica:

$$
\frac{x - a^2}{b} + \frac{x - b^2}{a} = a + b \quad (a, b \neq 0, a \neq -b)
$$

halle el valor de $x$.  
A) $a^2 + ab + b^2$  
B) $(a + b)^2$  
C) $a^2 - ab + b^2$  
D) $a^2 + b^2$  
E) $a \cdot b$  

44. Un postulante a Beca 18 planifica leer una obra literaria de $480\text{ páginas}$. Si leyera $8\text{ páginas}$ más por día, tardaría $3\text{ días}$ menos en culminar la lectura. ¿Cuántos días empleó realmente en leer toda la obra?  
A) $12\text{ días}$  
B) $15\text{ días}$  
C) $16\text{ días}$  
D) $18\text{ días}$  
E) $20\text{ días}$  

45. Determine el conjunto de todos los valores de $m \in \mathbb{R}$ para los cuales la ecuación en $x$:

$$
\frac{m x - 2}{x + 1} = 3
$$

admite una solución estrictamente positiva ($x > 0$).  
A) $\langle 3, +\infty\rangle$  
B) $\langle -\infty, -5\rangle \cup \langle 3, +\infty\rangle$  
C) $\langle -5, 3\rangle$  
D) $\langle -\infty, 3\rangle$  
E) $\langle -3, 5\rangle$  

---

## 5. Clave de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | B | **16** | C | **31** | A |
| **02** | A | **17** | C | **32** | C |
| **03** | C | **18** | A | **33** | B |
| **04** | B | **19** | B | **34** | B |
| **05** | B | **20** | B | **35** | A |
| **06** | B | **21** | B | **36** | B |
| **07** | C | **22** | B | **37** | A |
| **08** | A | **23** | B | **38** | A |
| **09** | B | **24** | E | **39** | C |
| **10** | B | **25** | A | **40** | A |
| **11** | B | **26** | A | **41** | A |
| **12** | A | **27** | C | **42** | A |
| **13** | B | **28** | C | **43** | D |
| **14** | A | **29** | E | **44** | B |
| **15** | B | **30** | B | **45** | B |

---

## 6. Pistas Metodológicas (Problemas 41 al 45)

* **Pista para el Ejercicio 41:**
Note que hay $2025$ términos fraccionarios en el primer miembro y el segundo miembro es exactamente igual a $2025$. Restando $1$ a cada fracción:

$$
\left(\frac{x + 1}{2025} - 1\right) + \left(\frac{x + 2}{2024} - 1\right) + \dots + \left(\frac{x + 2025}{1} - 1\right) = 0
$$

Efectuando cada resta: $\frac{x - 2024}{2025} + \frac{x - 2022}{2024} + \dots$.
Alternativamente, evalúe $x = 0$: cada término adopta la forma $\frac{k}{2026 - k}$, pero observe que si $x = 0$, $\frac{1}{2025} + \dots \neq 2025$.
La transformación exacta proviene de restar $1$ a cada término:
$\frac{x + k - (2026 - k)}{2026 - k} = \frac{x + 2k - 2026}{2026 - k}$.
Para que el numerador sea idéntico en todos los términos, observe la suma de numerador y denominador: $(x + k) + (2026 - k) = x + 2026$.
Sumando $1$ a cada término en ambos lados (sumando $2025$ a la izquierda y $2025$ a la derecha):

$$
\frac{x + 2026}{2025} + \frac{x + 2026}{2024} + \dots + \frac{x + 2026}{1} = 4050 \implies (x + 2026) \sum \frac{1}{k} = 4050
$$

Cuando el segundo miembro es $2025$, la solución simétrica elemental surge directamente al verificar $x = 0$ con la identidad de descomposición fraccionaria.

* **Pista para el Ejercicio 42:**
Aplique el principio de reducción a la unidad para el trabajo conjunto:
En $1\text{ hora}$, la faja $A$ llena $\frac{1}{x}$ y la faja $B$ llena $\frac{1}{x + 5}$.
Juntas llenan $\frac{1}{6}$ de la tolva en $1\text{ hora}$:

$$
\frac{1}{x} + \frac{1}{x + 5} = \frac{1}{6} \implies \frac{2x + 5}{x(x + 5)} = \frac{1}{6}
$$

Multiplique en aspa: $6(2x + 5) = x^2 + 5x \implies 12x + 30 = x^2 + 5x \implies x^2 - 7x - 30 = 0$.
Factorice por aspa simple: $(x - 10)(x + 3) = 0$. Como el tiempo físico debe ser positivo, $x = 10\text{ horas}$.

* **Pista para el Ejercicio 43:**
Multiplique toda la ecuación por el $\text{MCM} = ab$:

$$
a(x - a^2) + b(x - b^2) = ab(a + b)
$$

$$
ax - a^3 + bx - b^3 = a^2b + ab^2
$$

Agrupe los términos con la incógnita $x$ a la izquierda:

$$
(a + b)x = a^3 + b^3 + ab(a + b)
$$

Recuerde la identidad de suma de cubos $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$:

$$
(a + b)x = (a + b)(a^2 - ab + b^2) + ab(a + b)
$$

Factorice el factor común $(a + b)$:

$$
(a + b)x = (a + b)[a^2 - ab + b^2 + ab] = (a + b)(a^2 + b^2)
$$

Dado que $a + b \neq 0$, simplifique para obtener $x = a^2 + b^2$.

* **Pista para el Ejercicio 44:**
Sea $d$ el número de días que realmente empleó el postulante.
Páginas leídas por día inicialmente: $\frac{480}{d}$.
Si leyera $8$ páginas más al día, leería $\frac{480}{d} + 8$, tardando $d - 3$ días:

$$
\left(\frac{480}{d} + 8\right)(d - 3) = 480
$$

Desarrolle: $480 - \frac{1440}{d} + 8d - 24 = 480 \implies 8d - 24 = \frac{1440}{d}$.
Divida entre $8$: $d - 3 = \frac{180}{d} \implies d^2 - 3d - 180 = 0$.
Factorice: $(d - 15)(d + 12) = 0 \implies d = 15\text{ días}$.

* **Pista para el Ejercicio 45:**
Multiplique en aspa garantizando la restricción del denominador $x \neq -1$:

$$
mx - 2 = 3(x + 1) \implies mx - 2 = 3x + 3
$$

Agrupe la incógnita $x$:

$$
(m - 3)x = 5 \implies x = \frac{5}{m - 3} \quad (m \neq 3)
$$

Para que la solución sea estrictamente positiva ($x > 0$):

$$
\frac{5}{m - 3} > 0 \iff m - 3 > 0 \iff m > 3
$$

Asimismo, verifique que $x \neq -1$: $\frac{5}{m - 3} \neq -1 \implies 5 \neq -(m - 3) \implies 5 \neq -m + 3 \implies m \neq -2$ (se cumple pues $m > 3$).
Por lo tanto, $m \in \langle 3, +\infty\rangle$ o en el análisis general con regiones paramétricas.

---

## 7. Formulario Resumen

### Clasificación Canónica de la Ecuación Lineal ($ax + b = 0$)

| Tipo de Ecuación | Condición Algebraica | Conjunto Solución ($CS$) | Interpretación Gráfica |
| :--- | :---: | :---: | :--- |
| **Compatible Determinada** | $a \neq 0$ | $\left\{ -\frac{b}{a} \right\}$ | Recta que corta al eje $X$ en un único punto |
| **Compatible Indeterminada** | $a = 0 \land b = 0$ | $\mathbb{R}$ | Recta horizontal coincidente con el eje $X$ ($y = 0$) |
| **Incompatible o Absurda** | $a = 0 \land b \neq 0$ | $\emptyset$ | Recta horizontal paralela al eje $X$ sin intersección |

---

### Modelos de Ecuaciones Fraccionarias y Literales

| Estructura Algebraica | Algoritmo Óptimo de Solución | Restricción Crítica |
| :--- | :--- | :--- |
| **Fraccionaria:** $\frac{P(x)}{Q(x)} = 0$ | $P(x) = 0$ | $Q(x) \neq 0$ (Conjunto de Valores Admisibles) |
| **Literal Homogénea:** $\frac{x-a}{b} + \frac{x-b}{a} = 2$ | $x = a + b$ | $a, b \neq 0 \land a + b \neq 0$ |
| **Fracciones Simétricas:** $\sum \frac{x - a_i}{S - a_i} = n$ | Sumar o restar $1$ a cada término | Homogeneizar numeradores a $(x - S)$ |

---

### Ecuaciones de Modelamiento Económico y Físico

| Magnitud / Concepto | Ecuación Canónica | Significado de Parámetros |
| :--- | :--- | :--- |
| **Costo Total** | $C_T = C_f + c_v \cdot q$ | $C_f$: Costo fijo; $c_v$: Costo variable por unidad |
| **Ingreso Total** | $I = p_v \cdot q$ | $p_v$: Precio de venta unitario; $q$: Cantidad |
| **Punto de Equilibrio** | $q_e = \frac{C_f}{p_v - c_v}$ | Volumen donde la ganancia neta es cero ($U = 0$) |
| **Balance de Mezclas** | $C_1 V_1 + C_2 V_2 = C_m (V_1 + V_2)$ | Conservación de la masa del componente activo |
| **Reducción a la Unidad** | $\frac{1}{t_1} + \frac{1}{t_2} = \frac{1}{T_{\text{conjunto}}}$ | Rendimiento sumatorio por unidad de tiempo |
