# Tema 09: Progresiones Aritméticas y Geométricas

**Área:** Aritmética / Regularidad, Patrones y Sucesiones
**Nivel:** Preuniversitario / Beca 18 (ENP)
**Indicador Oficial:** *Emplea diversas estrategias heurísticas, recursos o procedimientos vinculados a progresiones aritméticas o geométricas.*

---

## 1. Motivación y Contexto Real

En la modelación matemática de fenómenos naturales y financieros, las progresiones constituyen el andamiaje cuantitativo del crecimiento y la regularidad. Desde el cálculo de cuotas en un plan de ahorro bancario con aportes escalonados en los Andes, pasando por el crecimiento exponencial de colonias bacterianas en laboratorios de biotecnología o la degradación de fármacos en el torrente sanguíneo, hasta la trayectoria amortiguada de una pelota que rebota sucesivamente sobre el asfalto, las sucesiones permiten predecir el futuro a partir de una ley de formación rigurosa.

En el Examen Nacional de Preselección (ENP) de Beca 18 y en las universidades líderes del país (UNI, San Marcos, PUCP), las preguntas de progresiones evalúan la capacidad para deducir el término general sin tanteos ciegos, calcular la suma de series infinitas convergentes (suma límite) y resolver problemas donde intervienen simultáneamente progresiones aritméticas y geométricas en contextos productivos y científicos.

---

## 2. Fundamentación Teórica Rigurosa

### 2.1 Progresión Aritmética (P.A.)
Una **Progresión Aritmética** (o sucesión lineal) es una secuencia ordenada de números reales en la cual cada término (a excepción del primero) se obtiene sumando al término anterior una cantidad constante llamada **razón aritmética** ($d$ o $r$):

$$a_n = a_{n-1} + d \quad (\forall n \ge 2)$$

#### Clasificación según la Razón:
* **Creciente:** Si $d > 0$ ($a_1 < a_2 < a_3 < \dots$).
* **Constante o Trivial:** Si $d = 0$ ($a_1 = a_2 = a_3 = \dots$).
* **Decreciente:** Si $d < 0$ ($a_1 > a_2 > a_3 > \dots$).

#### Fórmulas Fundamentales de la P.A.:
1. **Término Enésimo o General ($a_n$):**

$$a_n = a_1 + (n - 1) \cdot d$$

2. **Cálculo del Número de Términos ($n$):**

$$n = \frac{a_n - a_1}{d} + 1$$

3. **Suma de los $n$ Primeros Términos ($S_n$):**

$$S_n = \left(\frac{a_1 + a_n}{2}\right) \cdot n$$

Sustituyendo $a_n = a_1 + (n - 1)d$:

$$S_n = \left[\frac{2a_1 + (n - 1)d}{2}\right] \cdot n$$

4. **Término Central ($a_c$) para $n$ impar:**

$$a_c = \frac{a_1 + a_n}{2} \implies S_n = a_c \cdot n$$

5. **Términos Equidistantes:**
En toda P.A. finita, la suma de dos términos equidistantes de los extremos es constante e igual a la suma de los extremos:

$$a_k + a_{n - k + 1} = a_1 + a_n$$

### 2.2 Progresión Geométrica (P.G.)
Una **Progresión Geométrica** es una secuencia ordenada de números reales no nulos en la cual cada término se obtiene multiplicando el término anterior por una constante no nula denominada **razón geométrica** ($q$):

$$t_n = t_{n-1} \cdot q \quad (\forall n \ge 2, \; q \neq 0)$$

#### Clasificación según la Razón ($q$):
* **Creciente:** Si $t_1 > 0$ y $q > 1$.
* **Decreciente:** Si $t_1 > 0$ y $0 < q < 1$.
* **Oscilante o Alternada:** Si $q < 0$ (los signos se alternan sucesivamente).

#### Fórmulas Fundamentales de la P.G.:
1. **Término Enésimo o General ($t_n$):**

$$t_n = t_1 \cdot q^{n - 1}$$

2. **Suma de los $n$ Primeros Términos de una P.G. Finita ($S_n$ con $q \neq 1$):**

$$S_n = \frac{t_1(q^n - 1)}{q - 1} = \frac{t_n \cdot q - t_1}{q - 1}$$

3. **Suma Límite de una P.G. Decreciente e Infinita ($S_\infty$ con $|q| < 1$):**
Cuando el número de términos tiende al infinito ($n \to \infty$) y la razón cumple $-1 < q < 1$, el término $q^n$ tiende a cero ($q^n \to 0$):

$$S_\infty = \frac{t_1}{1 - q}$$

4. **Producto de los $n$ Primeros Términos ($P_n$):**

$$P_n = \sqrt{(t_1 \cdot t_n)^n}$$

5. **Término Central ($t_c$) para $n$ impar:**

$$t_c = \sqrt{t_1 \cdot t_n} \implies P_n = (t_c)^n$$

### 2.3 Interpolación de Medios
* **Medios Aritméticos (Diferenciales):** Interpolar $m$ medios aritméticos entre dos extremos $A$ y $B$ equivale a formar una P.A. de $n = m + 2$ términos, cuya razón es:

$$d = \frac{B - A}{m + 1}$$

* **Medios Geométricos (Proporcionales):** Interpolar $m$ medios geométricos entre dos extremos positivos $A$ y $B$ genera una P.G. de $n = m + 2$ términos, cuya razón es:

$$q = \sqrt[m + 1]{\frac{B}{A}}$$

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Fijación Operativa)

#### Ejercicio 1: Término Enésimo y Suma de una P.A.
En la progresión aritmética: $7, 11, 15, 19, \dots$, determine el término de lugar $25$ y la suma de los primeros $25$ términos.

**Solución paso a paso:**

**Paso 1:** Identificar los elementos de la P.A.
* Primer término: $a_1 = 7$.
* Razón aritmética: $d = 11 - 7 = 4$.
* Número de términos: $n = 25$.

**Paso 2:** Calcular el término de lugar 25 ($a_{25}$):

$$a_{25} = a_1 + (25 - 1) \cdot d$$

$$a_{25} = 7 + 24 \cdot 4 = 7 + 96 = 103$$

**Paso 3:** Calcular la suma de los 25 términos ($S_{25}$):

$$S_{25} = \left(\frac{a_1 + a_{25}}{2}\right) \cdot 25$$

$$S_{25} = \left(\frac{7 + 103}{2}\right) \cdot 25 = \left(\frac{110}{2}\right) \cdot 25 = 55 \cdot 25 = 1\,375$$

*Respuesta:* El término $25$ es $103$ y la suma es $1\,375$.

---

#### Ejercicio 2: Término Enésimo de una P.G.
El tercer término de una progresión geométrica es $18$ y el sexto término es $486$. Determine el primer término y la razón de la progresión.

**Solución paso a paso:**

**Paso 1:** Plantear los términos en función de $t_1$ y la razón $q$:
* $t_3 = t_1 \cdot q^{3 - 1} = t_1 \cdot q^2 = 18$
* $t_6 = t_1 \cdot q^{6 - 1} = t_1 \cdot q^5 = 486$

**Paso 2:** Dividir la segunda ecuación entre la primera para eliminar $t_1$:

$$\frac{t_1 \cdot q^5}{t_1 \cdot q^2} = \frac{486}{18}$$

$$q^3 = 27 \implies q = \sqrt[3]{27} = 3$$

**Paso 3:** Hallar el primer término ($t_1$):

$$t_1 \cdot 3^2 = 18 \implies t_1 \cdot 9 = 18 \implies t_1 = \frac{18}{9} = 2$$

*Respuesta:* El primer término es $2$ y la razón es $3$.

---

#### Ejercicio 3: Suma Límite de una Progresión Geométrica Decreciente
Calcule el valor de la siguiente suma infinita convergente:

$$S = 12 + 4 + \frac{4}{3} + \frac{4}{9} + \dots$$

**Solución paso a paso:**

**Paso 1:** Verificar si los términos forman una P.G. decreciente infinita:
* Primer término: $t_1 = 12$.
* Razón: $q = \frac{4}{12} = \frac{1}{3}$.
* Como $|q| = \left|\frac{1}{3}\right| < 1$, la serie es estrictamente convergente.

**Paso 2:** Aplicar la fórmula de la suma límite:

$$S_\infty = \frac{t_1}{1 - q}$$

Sustituimos $t_1 = 12$ y $q = \frac{1}{3}$:

$$S_\infty = \frac{12}{1 - \frac{1}{3}} = \frac{12}{\frac{2}{3}} = \frac{12 \cdot 3}{2} = 6 \cdot 3 = 18$$

*Respuesta:* La suma límite es $18$.

---

### Bloque B: Nivel Intermedio (Sistemas de Ecuaciones y Modelamiento)

#### Ejercicio 4: Determinación de Términos en P.A. Consecutiva
Tres números están en progresión aritmética. La suma de los tres números es $36$ y la suma de sus cuadrados es $450$. Determine el producto de dichos tres números.

**Solución paso a paso:**

**Paso 1:** Representar los tres términos de forma simétrica:
Sea la terna: $x - d$, $x$, $x + d$, donde $d$ es la razón aritmética.

**Paso 2:** Usar el dato de la suma:

$$(x - d) + x + (x + d) = 36$$

$$3x = 36 \implies x = 12$$

El término central es $12$. La terna es: $12 - d$, $12$, $12 + d$.

**Paso 3:** Usar el dato de la suma de los cuadrados:

$$(12 - d)^2 + 12^2 + (12 + d)^2 = 450$$

Desarrollamos los binomios:

$$(144 - 24d + d^2) + 144 + (144 + 24d + d^2) = 450$$

$$432 + 2d^2 = 450$$

$$2d^2 = 450 - 432 = 18 \implies d^2 = 9 \implies d = \pm 3$$

**Paso 4:** Reconstruir los números:
Tomando $d = 3$ (o $d = -3$):
Los números son: $12 - 3 = 9$, $12$, y $12 + 3 = 15$.

**Paso 5:** Calcular el producto pedido:

$$P = 9 \times 12 \times 15 = 108 \times 15 = 1\,620$$

*Respuesta:* El producto de los tres números es $1\,620$.

---

#### Ejercicio 5: Plan de Ahorro Escalonado en P.A.
Una estudiante becaria de Beca 18 decide ahorrar para comprar una computadora portátil. Empieza ahorrando $\text{S/ } 50$ la primera semana y cada semana siguiente incrementa su ahorro en $\text{S/ } 15$ respecto a la anterior. Si ahorra ininterrumpidamente durante $24\text{ semanas}$, ¿cuánto dinero habrá acumulado en total?

**Solución paso a paso:**

**Paso 1:** Identificar la progresión del ahorro semanal:
* $a_1 = 50$ (ahorro de la semana 1).
* $d = 15$ (incremento semanal constante).
* $n = 24$ (número total de semanas).

**Paso 2:** Calcular el ahorro de la última semana ($a_{24}$):

$$a_{24} = a_1 + (24 - 1) \cdot d$$

$$a_{24} = 50 + 23 \cdot 15 = 50 + 345 = \text{S/ } 395$$

**Paso 3:** Calcular el monto total acumulado ($S_{24}$):

$$S_{24} = \left(\frac{a_1 + a_{24}}{2}\right) \cdot n$$

$$S_{24} = \left(\frac{50 + 395}{2}\right) \cdot 24 = \left(\frac{445}{2}\right) \cdot 24 = 445 \cdot 12 = \text{S/ } 5\,340$$

*Respuesta:* Habrá acumulado en total $\text{S/ } 5\,340$.

---

#### Ejercicio 6: Intersección entre P.A. y P.G.
Tres números positivos forman una progresión geométrica. Si al segundo término se le suma $8$, los tres números pasan a formar una progresión aritmética; y si luego al tercer término de esta nueva P.A. se le suma $64$, vuelve a formarse una progresión geométrica. Halle la suma de los tres números iniciales.

**Solución paso a paso:**

**Paso 1:** Definir los tres números iniciales en P.G.
Sean los números: $a$, $aq$, $aq^2$.

**Paso 2:** Condición 1 (al sumar 8 al segundo se forma una P.A.):
La terna $a$, $aq + 8$, $aq^2$ forma una P.A.
En toda terna aritmética, el doble del término medio es igual a la suma de los extremos:

$$2(aq + 8) = a + aq^2$$

$$2aq + 16 = a + aq^2 \implies aq^2 - 2aq + a = 16 \implies a(q - 1)^2 = 16 \quad \text{--- (Ecuación 1)}$$

**Paso 3:** Condición 2 (al sumar 64 al tercero se forma una P.G.):
La terna $a$, $aq + 8$, $aq^2 + 64$ forma una P.G.
En toda terna geométrica, el cuadrado del término medio es igual al producto de los extremos:

$$(aq + 8)^2 = a(aq^2 + 64)$$

$$a^2q^2 + 16aq + 64 = a^2q^2 + 64a$$

Cancelamos $a^2q^2$ en ambos miembros:

$$16aq + 64 = 64a \implies 16(aq + 4) = 64a \implies aq + 4 = 4a \implies 4a - aq = 4 \implies a(4 - q) = 4 \quad \text{--- (Ecuación 2)}$$

**Paso 4:** Dividir la Ecuación 1 entre la Ecuación 2 para eliminar $a$:

$$\frac{a(q - 1)^2}{a(4 - q)} = \frac{16}{4}$$

$$\frac{(q - 1)^2}{4 - q} = 4$$

$$q^2 - 2q + 1 = 4(4 - q) = 16 - 4q$$

$$q^2 + 2q - 15 = 0$$

Factorizamos por aspa simple:

$$(q + 5)(q - 3) = 0$$

Como los números son positivos, la razón debe ser positiva: $q = 3$.

**Paso 5:** Calcular el valor de $a$:
De la Ecuación 2:

$$a(4 - 3) = 4 \implies a \cdot 1 = 4 \implies a = 4$$

**Paso 6:** Reconstruir los tres números iniciales de la P.G.
* $t_1 = 4$
* $t_2 = 4 \times 3 = 12$
* $t_3 = 4 \times 3^2 = 36$

**Paso 7:** Calcular la suma pedida:

$$\text{Suma} = 4 + 12 + 36 = 52$$

*Respuesta:* La suma de los tres números iniciales es $52$.

---

#### Ejercicio 7: Ley de Rebotes Sucesivos
Una pelota de jebe se deja caer desde una altura de $81\text{ metros}$ sobre una losa deportiva en Tarma. En cada rebote, la pelota se eleva hasta las dos terceras partes ($\frac{2}{3}$) de la altura alcanzada en el rebote anterior. Calcule la distancia total recorrida por la pelota hasta que queda teóricamente en reposo sobre el suelo.

**Solución paso a paso:**

**Paso 1:** Desglosar las trayectorias de descenso y ascenso:
* **Primera caída:** Recorre $H_0 = 81\text{ metros}$ hacia abajo.
* **Primer rebote:** Sube $81 \times \frac{2}{3} = 54\text{ m}$ y baja $54\text{ m}$. (Distancia: $2 \times 54\text{ m}$).
* **Segundo rebote:** Sube $54 \times \frac{2}{3} = 36\text{ m}$ y baja $36\text{ m}$. (Distancia: $2 \times 36\text{ m}$).
* **En general:** Cada altura posterior es $h_k = 81 \cdot \left(\frac{2}{3}\right)^k$, y se recorre dos veces (subida y bajada).

**Paso 2:** Plantear la distancia total recorrida ($D_{\text{total}}$):

$$D_{\text{total}} = H_0 + 2 \cdot \left( h_1 + h_2 + h_3 + \dots \right)$$

La serie dentro del paréntesis es una P.G. infinita:

$$h_1 = 81 \cdot \frac{2}{3} = 54\text{ m}$$

$$q = \frac{2}{3}$$

$$S_{\text{rebotes}} = \frac{h_1}{1 - q} = \frac{54}{1 - \frac{2}{3}} = \frac{54}{\frac{1}{3}} = 54 \times 3 = 162\text{ metros}$$

**Paso 3:** Calcular la distancia total:

$$D_{\text{total}} = 81 + 2(162) = 81 + 324 = 405\text{ metros}$$

*(Fórmula directa de rebotes con fracción $\frac{p}{q}$):*

$$D_{\text{total}} = H_0 \cdot \left(\frac{q + p}{q - p}\right) = 81 \cdot \left(\frac{3 + 2}{3 - 2}\right) = 81 \cdot 5 = 405\text{ metros}$$

*Respuesta:* La pelota recorre en total $405\text{ metros}$.

---

### Bloque C: Nivel Avanzado / Contexto Beca 18 (Alta Demanda Cognitiva)

#### Ejercicio 8: Cultivo Bacteriano y Decaimiento Exponencial
En un biorreactor de fermentación en Trujillo, un cultivo bacteriano de $500$ microorganismos se duplica cada $20\text{ minutos}$ en condiciones óptimas. Al cabo de $2\text{ horas}$, se introduce un bactericida que reduce la población al $75\%$ de su valor cada $10\text{ minutos}$. ¿Cuántas bacterias quedarán vivas en el reactor $40\text{ minutos}$ después de haber aplicado el bactericida?

**Solución paso a paso:**

**Paso 1:** Analizar la fase de crecimiento (primeras 2 horas):
* Duración de la fase: $2\text{ horas} = 120\text{ minutos}$.
* Como se duplica cada $20\text{ minutos}$, el número de ciclos de duplicación es:

$$n_1 = \frac{120}{20} = 6\text{ ciclos}$$

* Población al final de las 2 horas ($N_1$):

$$N_1 = 500 \cdot 2^6 = 500 \cdot 64 = 32\,000\text{ bacterias}$$

**Paso 2:** Analizar la fase de decaimiento por bactericida ($40\text{ minutos}$ posteriores):
* Como la población se reduce al $75\%$ cada $10\text{ minutos}$, el factor de reducción por ciclo es:

$$q = 75\% = \frac{3}{4} = 0{,}75$$

* El número de ciclos en $40\text{ minutos}$ es:

$$n_2 = \frac{40}{10} = 4\text{ ciclos}$$

**Paso 3:** Calcular la población final ($N_{\text{final}}$):

$$N_{\text{final}} = N_1 \cdot q^4 = 32\,000 \cdot \left(\frac{3}{4}\right)^4$$

Calculamos la potencia:

$$\left(\frac{3}{4}\right)^4 = \frac{81}{256}$$

$$N_{\text{final}} = 32\,000 \cdot \frac{81}{256}$$

Dividimos $32\,000$ entre $256$:

$$\frac{32\,000}{256} = 125$$

$$N_{\text{final}} = 125 \times 81 = 10\,125\text{ bacterias}$$

*Respuesta:* Quedarán exactamente $10\,125\text{ bacterias}$.

---

#### Ejercicio 9: Diseño Estructural de Graderías en P.A.
En el diseño de una tribuna para un coliseo polideportivo comunal en Ayacucho, la primera fila tiene capacidad para $40$ espectadores y cada fila subsiguiente cuenta con $4$ asientos más que la anterior. Si el proyecto exige una capacidad total mínima de $2\,000$ espectadores sentados, determine el número mínimo de filas que debe tener la tribuna y cuántos asientos tendrá exactamente la última fila construida.

**Solución paso a paso:**

**Paso 1:** Modelar la capacidad de las filas como una P.A.
* Primer término: $a_1 = 40$.
* Razón: $d = 4$.
* Capacidad de la fila $n$: $a_n = 40 + (n - 1)4 = 40 + 4n - 4 = 4n + 36$.

**Paso 2:** Plantear la suma total de asientos ($S_n \ge 2\,000$):

$$S_n = \left(\frac{a_1 + a_n}{2}\right) \cdot n = \left(\frac{40 + (4n + 36)}{2}\right) \cdot n$$

$$S_n = \left(\frac{4n + 76}{2}\right) \cdot n = (2n + 38) \cdot n = 2n^2 + 38n$$

**Paso 3:** Establecer la inecuación:

$$2n^2 + 38n \ge 2\,000$$

Dividimos entre 2:

$$n^2 + 19n \ge 1\,000$$

$$n^2 + 19n - 1\,000 \ge 0$$

**Paso 4:** Resolver la ecuación cuadrática asociada para hallar la raíz positiva:

$$n = \frac{-19 + \sqrt{19^2 - 4(1)(-1\,000)}}{2} = \frac{-19 + \sqrt{361 + 4\,000}}{2} = \frac{-19 + \sqrt{4\,361}}{2}$$

Aproximamos la raíz:

$$66^2 = 4\,356 \implies \sqrt{4\,361} \approx 66{,}038$$

$$n \approx \frac{-19 + 66{,}04}{2} = \frac{47{,}04}{2} = 23{,}52$$

**Paso 5:** Determinar el entero mínimo:
Como $n$ debe ser un número entero de filas:

$$n_{\text{mínimo}} = 24\text{ filas}$$

**Paso 6:** Verificar la capacidad con $n = 24$:

$$S_{24} = 2(24)^2 + 38(24) = 2(576) + 912 = 1\,152 + 912 = 2\,064\text{ asientos} \ge 2\,000$$

*(Con 23 filas: $2(529) + 38(23) = 1\,058 + 874 = 1\,932 < 2\,000$).*

**Paso 7:** Calcular la capacidad de la fila 24 ($a_{24}$):

$$a_{24} = 4(24) + 36 = 96 + 36 = 132\text{ asientos}$$

*Respuesta:* Se requieren como mínimo $24\text{ filas}$ y la última fila tendrá $132\text{ asientos}$.

---

#### Ejercicio 10: Sucesiones Anidadas y Fracciones Continuas en Circuitos
En un circuito eléctrico de filtrado analógico en escalera infinita, la impedancia equivalente de cada etapa se modela mediante la suma infinita de aportes resistivos y capacitivos combinados:

$$E = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \frac{5}{32} + \dots + \frac{n}{2^n} + \dots$$

Determine el valor exacto de convergencia de esta suma combinada aritmético-geométrica.

**Solución paso a paso:**

**Paso 1:** Reconocer la estructura de la serie aritmético-geométrica:
Los numeradores forman una P.A.: $1, 2, 3, 4, 5, \dots$ (razón $d = 1$).
Los denominadores forman una P.G.: $2^1, 2^2, 2^3, 2^4, \dots$ (razón $q = \frac{1}{2}$).

**Paso 2:** Aplicar el método de multiplicación por la razón geométrica:
Escribimos la suma original:

$$E = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \frac{5}{32} + \dots \quad \text{--- (1)}$$

Multiplicamos toda la ecuación por la razón $q = \frac{1}{2}$:

$$\frac{1}{2}E = \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + \frac{4}{32} + \dots \quad \text{--- (2)}$$

**Paso 3:** Restar la ecuación (2) de la ecuación (1) término a término desplazado:

$$E - \frac{1}{2}E = \frac{1}{2} + \left(\frac{2}{4} - \frac{1}{4}\right) + \left(\frac{3}{8} - \frac{2}{8}\right) + \left(\frac{4}{16} - \frac{3}{16}\right) + \dots$$

$$\frac{1}{2}E = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \dots$$

**Paso 4:** Calcular la serie geométrica pura resultante del segundo miembro:
Es una P.G. infinita con $t_1 = \frac{1}{2}$ y $q = \frac{1}{2}$:

$$S_\infty = \frac{t_1}{1 - q} = \frac{\frac{1}{2}}{1 - \frac{1}{2}} = \frac{\frac{1}{2}}{\frac{1}{2}} = 1$$

**Paso 5:** Despejar el valor final de $E$:

$$\frac{1}{2}E = 1 \implies E = 2$$

*Respuesta:* El valor exacto de convergencia es $2$.

---

## 4. Práctica Propuesta (45 Ejercicios con Claves)

### Bloque I: Nivel Básico (Ejercicios 01 al 15)

1. En la progresión aritmética $12, 17, 22, 27, \dots$, calcule el término de lugar $30$.  
A) $152$  
B) $157$  
C) $162$  
D) $167$  
E) $172$  

2. ¿Cuántos términos tiene la siguiente progresión aritmética finita: $15, 19, 23, \dots, 131$?  
A) $28$  
B) $29$  
C) $30$  
D) $31$  
E) $32$  

3. Calcule la suma de los primeros $20$ términos de la progresión aritmética: $5, 8, 11, 14, \dots$  
A) $650$  
B) $670$  
C) $700$  
D) $730$  
E) $750$  

4. En una P.G., el primer término es $3$ y la razón es $2$. Determine el octavo término.  
A) $192$  
B) $384$  
C) $768$  
D) $1\,536$  
E) $3\,072$  

5. Calcule la suma de los primeros $6$ términos de la progresión geométrica: $2, 6, 18, 54, \dots$  
A) $726$  
B) $728$  
C) $730$  
D) $732$  
E) $734$  

6. Calcule el valor de la siguiente suma infinita convergente:

$$S = 16 + 8 + 4 + 2 + 1 + \dots$$

A) $30$  
B) $32$  
C) $34$  
D) $36$  
E) $40$  

7. En una P.A., el término de lugar $10$ es $43$ y la razón es $4$. ¿Cuál es el primer término?  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

8. Si los números $x - 2$, $x + 4$ y $3x - 2$ forman una progresión aritmética, halle el valor de $x$.  
A) $4$  
B) $5$  
C) $6$  
D) $7$  
E) $8$  

9. Si los números $y - 1$, $y + 2$ y $2y + 4$ forman una progresión geométrica de términos positivos, determine el valor de $y$.  
A) $2$  
B) $3$  
C) $4$  
D) $5$  
E) $6$  

10. Calcule la suma de los primeros $40$ números enteros positivos impares: $1 + 3 + 5 + \dots + 79$.  
A) $1\,500$  
B) $1\,560$  
C) $1\,600$  
D) $1\,640$  
E) $1\,700$  

11. Interpole $3$ medios aritméticos entre $8$ y $32$. ¿Cuál es el segundo medio aritmético interpolado?  
A) $14$  
B) $16$  
C) $18$  
D) $20$  
E) $22$  

12. Calcule la suma límite de la serie geométrica:

$$M = 27 - 9 + 3 - 1 + \frac{1}{3} - \dots$$

A) $18$  
B) $20$  
C) $20{,}25$  
D) $21$  
E) $22{,}5$  

13. En una P.A. de $15$ términos, el término central es $28$. Calcule la suma de todos los términos de la progresión.  
A) $390$  
B) $405$  
C) $420$  
D) $435$  
E) $450$  

14. El producto de tres términos consecutivos de una P.G. es $216$. ¿Cuál es el término medio?  
A) $4$  
B) $6$  
C) $8$  
D) $9$  
E) $12$  

15. En una P.A., el quinto término es $19$ y el décimo segundo término es $47$. ¿Cuál es la razón de la progresión?  
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) $7$  

---

### Bloque II: Nivel Intermedio (Ejercicios 16 al 30)

16. Calcule la suma de todos los números enteros de tres cifras que son múltiplos exactos de $7$.  
A) $68\,355$  
B) $70\,336$  
C) $72\,140$  
D) $74\,250$  
E) $76\,120$  

17. En una P.A., la suma de los $n$ primeros términos está dada por la función cuadrática: $S_n = 3n^2 + 5n$. Calcule el término de lugar $15$.  
A) $86$  
B) $88$  
C) $90$  
D) $92$  
E) $94$  

18. Tres números están en P.A. creciente. La suma de los tres es $27$ y el producto del primero por el tercero es $77$. Calcule el mayor de los números.  
A) $11$  
B) $12$  
C) $13$  
D) $14$  
E) $15$  

19. Una pelota cae desde $64\text{ metros}$ de altura y en cada rebote se eleva hasta las tres cuartas partes ($\frac{3}{4}$) de la altura precedente. Calcule la distancia total recorrida hasta detenerse teóricamente.  
A) $384\text{ m}$  
B) $412\text{ m}$  
C) $448\text{ m}$  
D) $480\text{ m}$  
E) $512\text{ m}$  

20. En una P.G. de $6$ términos, la suma de los tres primeros términos es $26$ y la suma de los tres últimos es $702$. ¿Cuál es la razón de la progresión?  
A) $2$  
B) $3$  
C) $4$  
D) $5$  
E) $6$  

21. Se intercalan $4$ medios geométricos entre $5$ y $160$. ¿Cuál es el valor del tercer medio geométrico intercalado?  
A) $20$  
B) $40$  
C) $60$  
D) $80$  
E) $100$  

22. La suma de los infinitos términos de una P.G. decreciente es $16$ y la suma de sus cuadrados es $153{,}6$. ¿Cuál es el primer término?  
A) $6$  
B) $8$  
C) $9{,}6$  
D) $10$  
E) $12$  

23. Un atleta decide entrenar durante $30\text{ días}$. El primer día corre $800\text{ metros}$ y cada día posterior corre $150\text{ metros}$ más que el día anterior. ¿Cuántos kilómetros en total corrió al culminar su entrenamiento?  
A) $84\text{ km}$  
B) $86{,}5\text{ km}$  
C) $89{,}25\text{ km}$  
D) $92\text{ km}$  
E) $95\text{ km}$  

24. En una P.A., el término que ocupa el lugar $p$ es $q$ y el término que ocupa el lugar $q$ es $p$ (con $p \neq q$). ¿Cuál es el valor del término de lugar $p + q$?  
A) $0$  
B) $1$  
C) $p + q$  
D) $pq$  
E) $-(p + q)$  

25. Halle el valor de la suma infinita convergente:

$$E = \frac{2}{3} + \frac{4}{9} + \frac{6}{27} + \frac{8}{81} + \dots$$

A) $1$  
B) $\frac{3}{2}$  
C) $\frac{4}{3}$  
D) $\frac{5}{3}$  
E) $2$  

26. Cuatro números enteros forman una P.A. creciente. La suma de los cuatro es $24$ y el producto de los cuatro es $945$. Calcule la razón de la progresión.  
A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) $5$  

27. Una colonia de termitas se triplica cada semana. Si al cabo de $5\text{ semanas}$ la colonia cuenta con $486$ individuos, ¿cuántas termitas había al inicio?  
A) $2$  
B) $3$  
C) $4$  
D) $6$  
E) $9$  

28. En una P.A. se conoce que $a_4 + a_8 = 38$ y $a_6 + a_{12} = 58$. Determine el valor del vigésimo término ($a_{20}$).  
A) $65$  
B) $68$  
C) $71$  
D) $74$  
E) $77$  

29. Si se suman $n$ términos de la serie geométrica $1 + 2 + 4 + 8 + \dots$, el resultado es $1\,023$. Calcule el valor de $n$.  
A) $8$  
B) $9$  
C) $10$  
D) $11$  
E) $12$  

30. Las medidas de los tres ángulos internos de un triángulo están en progresión aritmética. Si el menor de los ángulos mide $20^\circ$, ¿cuánto mide el ángulo mayor?  
A) $80^\circ$  
B) $90^\circ$  
C) $100^\circ$  
D) $110^\circ$  
E) $120^\circ$  

---

### Bloque III: Nivel Avanzado / Contexto Beca 18 (Ejercicios 31 al 45)

31. Un tanque de almacenamiento de agua potable de $1\,000\text{ litros}$ se contamina con una sustancia química disuelta a una concentración de $20\text{ g/L}$. Para descontaminarlo, se extrae cada hora el $20\%$ de la mezcla y se reemplaza inmediatamente con agua destilada pura. ¿Cuántos gramos de contaminante quedarán en el tanque al cabo de $5\text{ horas}$?  
A) $6\,250\text{ g}$  
B) $6\,553{,}6\text{ g}$  
C) $6\,800\text{ g}$  
D) $7\,120\text{ g}$  
E) $7\,250\text{ g}$  

32. En un proyecto de reforestación en la selva central, se plantan árboles en filas de modo que la primera fila tiene $15$ plantones, la segunda tiene $19$, la tercera tiene $23$ y así sucesivamente. Si se dispone de un lote de $1\,215$ plantones y se desea utilizar todos ellos en filas completas, ¿cuántas filas se lograrán plantar en total?  
A) $20\text{ filas}$  
B) $21\text{ filas}$  
C) $22\text{ filas}$  
D) $23\text{ filas}$  
E) $24\text{ filas}$  

33. Una maquinaria pesada adquirida para una obra vial en Huánuco cuesta $\$ 160\,000$ nueva. Al final de cada año de operación pierde el $15\%$ del valor que tenía al inicio de ese año por depreciación técnica acelerada. ¿Cuál será su valor residual contable al culminar el cuarto año de uso?  
A) $\$ 81\,420$  
B) $\$ 83\,521$  
C) $\$ 85\,240$  
D) $\$ 88\,150$  
E) $\$ 92\,000$  

34. Calcule el valor exacto de convergencia de la serie infinita:

$$S = \frac{1}{5} + \frac{3}{25} + \frac{5}{125} + \frac{7}{625} + \dots + \frac{2n - 1}{5^n} + \dots$$

A) $\frac{1}{3}$  
B) $\frac{3}{8}$  
C) $\frac{5}{16}$  
D) $\frac{7}{20}$  
E) $\frac{1}{2}$  

35. Los lados de un triángulo rectángulo están en progresión aritmética. Si el perímetro del triángulo es de $108\text{ metros}$, determine la longitud del cateto mayor y el área del triángulo.  
A) $36\text{ m} \;; 486\text{ m}^2$  
B) $36\text{ m} \;; 540\text{ m}^2$  
C) $40\text{ m} \;; 486\text{ m}^2$  
D) $45\text{ m} \;; 540\text{ m}^2$  
E) $36\text{ m} \;; 432\text{ m}^2$  

36. En un experimento de física ondulatoria, una cuerda vibrante vibra de modo que la amplitud de oscilación de cada ciclo es el $80\%$ de la amplitud del ciclo anterior. Si la amplitud del primer ciclo fue de $25\text{ milímetros}$, ¿cuál es la distancia total vertical recorrida por el punto central de la cuerda al cabo de infinitos ciclos oscilatorios completos (subida y bajada en cada ciclo)?  
A) $200\text{ mm}$  
B) $225\text{ mm}$  
C) $250\text{ mm}$  
D) $275\text{ mm}$  
E) $300\text{ mm}$  

37. La suma de los tres términos de una P.G. creciente es $70$. Si los extremos se multiplican por $4$ y el término medio por $5$, los nuevos números forman una progresión aritmética. Halle la razón de la P.G. original.  
A) $2$  
B) $2{,}5$  
C) $3$  
D) $4$  
E) $5$  

38. Se colocan $30$ postes telefónicos a lo largo de una carretera rectilínea. El primer poste dista $20\text{ metros}$ de la central de operaciones, y la distancia entre cada par de postes consecutivos es de $15\text{ metros}$. Un camión grúa que transporta un solo poste por viaje sale de la central y regresa a ella tras plantar cada poste. ¿Cuántos kilómetros en total recorre el camión para plantar los $30$ postes si al inicio de la jornada parte de la central y al culminar el último poste regresa a la misma?  
A) $12{,}85\text{ km}$  
B) $13{,}65\text{ km}$  
C) $14{,}25\text{ km}$  
D) $14{,}85\text{ km}$  
E) $15{,}15\text{ km}$  

39. Si $S_1, S_2, S_3, \dots, S_p$ representan las sumas de los $n$ primeros términos de $p$ progresiones aritméticas cuyos primeros términos son $1, 2, 3, \dots, p$ y cuyas razones son $1, 3, 5, \dots, (2p - 1)$ respectivamente, determine el valor de la suma total:

$$E = S_1 + S_2 + S_3 + \dots + S_p$$

A) $\frac{np(np + 1)}{2}$  
B) $\frac{n(p + 1)}{2}$  
C) $\frac{p(n + 1)}{2}$  
D) $n^2 \cdot p^2$  
E) $\frac{np(n + p)}{2}$  

40. En una presa hidroeléctrica en el río Mantaro, el caudal de desagüe durante el mantenimiento programado se reduce a razón de una progresión geométrica: el primer día desaloja $81\text{ millones de m}^3$, el segundo día $54\text{ millones}$, el tercer día $36\text{ millones}$ y así sucesivamente. ¿Cuál es el volumen total de agua que se evacúa si el proceso se prolonga indefinidamente?  
A) $225\text{ millones de m}^3$  
B) $243\text{ millones de m}^3$  
C) $256\text{ millones de m}^3$  
D) $270\text{ millones de m}^3$  
E) $288\text{ millones de m}^3$  

41. En una P.A. creciente, el producto del primer y cuarto término es $85$, y el producto del segundo y tercer término es $117$. Calcule la suma de los diez primeros términos de la progresión.  
A) $220$  
B) $230$  
C) $240$  
D) $250$  
E) $260$  

42. Un pozo de exploración minera de $120\text{ metros}$ de profundidad se perfora mediante una cuadrilla que cobra $\text{S/ } 50$ por el primer metro perforado, $\text{S/ } 65$ por el segundo metro, $\text{S/ } 80$ por el tercer metro, y así sucesivamente en P.A. ¿Cuál es el costo total presupuestado para la perforación completa del pozo?  
A) $\text{S/ } 108\,500$  
B) $\text{S/ } 111\,200$  
C) $\text{S/ } 113\,100$  
D) $\text{S/ } 115\,400$  
E) $\text{S/ } 117\,600$  

43. Cuatro números positivos forman una progresión geométrica. La suma de los dos primeros términos es $15$ y la suma de los dos últimos términos es $60$. Determine el valor del cuarto término de la progresión.  
A) $32$  
B) $36$  
C) $40$  
D) $45$  
E) $48$  

44. Determine el número de términos comunes que presentan las siguientes dos progresiones aritméticas:

$$P_1: 14, 19, 24, 29, \dots, 514$$

$$P_2: 11, 18, 25, 32, \dots, 501$$

A) $12$  
B) $13$  
C) $14$  
D) $15$  
E) $16$  

45. Calcule el valor de la suma límite de los productos de términos consecutivos de una progresión geométrica infinita:

$$E = 1 \cdot \frac{1}{3} + \frac{1}{3} \cdot \frac{1}{9} + \frac{1}{9} \cdot \frac{1}{27} + \frac{1}{27} \cdot \frac{1}{81} + \dots$$

A) $\frac{3}{8}$  
B) $\frac{1}{4}$  
C) $\frac{3}{10}$  
D) $\frac{1}{3}$  
E) $\frac{2}{7}$  

---

## 5. Tabla de Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | B | **31** | B |
| **2** | C | **17** | D | **32** | B |
| **3** | B | **18** | C | **33** | B |
| **4** | B | **19** | C | **34** | B |
| **5** | B | **20** | B | **35** | A |
| **6** | B | **21** | B | **36** | C |
| **7** | C | **22** | C | **37** | B |
| **8** | C | **23** | C | **38** | C |
| **9** | A | **24** | A | **39** | A |
| **10** | C | **25** | B | **40** | B |
| **11** | D | **26** | B | **41** | B |
| **12** | C | **27** | A | **42** | C |
| **13** | C | **28** | B | **43** | C |
| **14** | B | **29** | C | **44** | C |
| **15** | B | **30** | C | **45** | A |

---

## 6. Pistas y Orientación Metodológica

Orientaciones analíticas para los cinco problemas más desafiantes del Bloque III:

* **Pista para el Ejercicio 34:**
Multiplique la suma $S$ por la razón geométrica $q = \frac{1}{5}$:

$$\frac{1}{5}S = \frac{1}{25} + \frac{3}{125} + \frac{5}{625} + \dots$$

Reste $S - \frac{1}{5}S = \frac{4}{5}S$:

$$\frac{4}{5}S = \frac{1}{5} + \left(\frac{2}{25} + \frac{2}{125} + \frac{2}{625} + \dots\right)$$

La serie dentro del paréntesis es una P.G. infinita con $t_1 = \frac{2}{25}$ y $q = \frac{1}{5}$. Su suma es $\frac{2/25}{1 - 1/5} = \frac{2/25}{4/5} = \frac{2}{20} = \frac{1}{10}$.
Luego: $\frac{4}{5}S = \frac{1}{5} + \frac{1}{10} = \frac{3}{10} \implies S = \frac{3}{10} \times \frac{5}{4} = \frac{3}{8}$.

* **Pista para el Ejercicio 35:**
Todo triángulo rectángulo cuyos lados están en P.A. es semejante al triángulo notable de lados $3k, 4k, 5k$ (razón $d = k$).
El perímetro es $3k + 4k + 5k = 12k = 108\text{ m} \implies k = 9\text{ m}$.
Los lados son: cateto menor $= 3(9) = 27\text{ m}$; cateto mayor $= 4(9) = 36\text{ m}$; hipotenusa $= 5(9) = 45\text{ m}$.
El área es $\frac{27 \times 36}{2} = 27 \times 18 = 486\text{ m}^2$.

* **Pista para el Ejercicio 38:**
El camión viaja de ida y vuelta para cada poste. Para el poste $k$, la distancia desde la central es $D_k = 20 + 15(k - 1)$. Como el viaje es de ida y vuelta, recorre $2 \cdot D_k = 40 + 30(k - 1)$.
La distancia total es la suma de una P.A. de $30$ términos:

$$D_{\text{total}} = \sum_{k=1}^{30} [40 + 30(k - 1)] = 30 \times 40 + 30 \times \frac{29 \times 30}{2} = 1\,200 + 30 \times 435 = 1\,200 + 13\,050 = 14\,250\text{ m} = 14{,}25\text{ km}$$

* **Pista para el Ejercicio 39:**
La suma de una P.A. de $n$ términos con primer término $k$ y razón $2k - 1$ es:

$$S_k = \frac{n}{2}[2k + (n - 1)(2k - 1)] = \frac{n}{2}[2k + 2nk - n - 2k + 1] = \frac{n}{2}[(2n)k - (n - 1)]$$

Sumando desde $k = 1$ hasta $p$:

$$\sum_{k=1}^p S_k = \frac{n}{2} \left[ 2n \sum_{k=1}^p k - p(n - 1) \right] = \frac{n}{2} \left[ 2n \cdot \frac{p(p + 1)}{2} - p(n - 1) \right] = \frac{np}{2}[n(p + 1) - (n - 1)] = \frac{np(np + 1)}{2}$$

* **Pista para el Ejercicio 44:**
Halle el término general de cada progresión:
* $P_1$: $a_n = 14 + 5(n - 1) = 5n + 9$. Los términos tienen la forma $5\dot{x} + 4$.
* $P_2$: $b_m = 11 + 7(m - 1) = 7m + 4$. Los términos tienen la forma $7\dot{y} + 4$.
Los términos comunes son de la forma $\text{MCM}(5, 7)k + 4 = 35k + 4$.
El primer término común para $k \ge 1$: con $k = 1 \implies 39$. Verifique si $39 \in P_1$ ($39 = 5(6) + 9$, sí) y $39 \in P_2$ ($39 = 7(5) + 4$, sí).
El último término común no debe superar el menor de los topes: $\min(514, 501) = 501$.

$$35k + 4 \le 501 \implies 35k \le 497 \implies k \le \frac{497}{35} = 14{,}2$$

Como $k$ va desde $1$ hasta $14$, existen exactamente $14$ términos comunes.

---

## 7. Formulario Resumen

### Progresión Aritmética (P.A.)

| Magnitud en P.A. | Fórmula Canónica |
| :--- | :--- |
| **Término General** | $a_n = a_1 + (n - 1)d$ |
| **Número de Términos** | $n = \frac{a_n - a_1}{d} + 1$ |
| **Suma de los $n$ Términos** | $S_n = \left(\frac{a_1 + a_n}{2}\right) \cdot n = \left[\frac{2a_1 + (n - 1)d}{2}\right] \cdot n$ |
| **Término Central ($n$ impar)** | $a_c = \frac{a_1 + a_n}{2} \implies S_n = a_c \cdot n$ |
| **Interpolación Aritmética** | $d = \frac{B - A}{m + 1} \quad (m \text{ medios})$ |

---

### Progresión Geométrica (P.G.)

| Magnitud en P.G. | Fórmula Canónica |
| :--- | :--- |
| **Término General** | $t_n = t_1 \cdot q^{n - 1}$ |
| **Suma Finita ($q \neq 1$)** | $S_n = \frac{t_1(q^n - 1)}{q - 1} = \frac{t_n \cdot q - t_1}{q - 1}$ |
| **Suma Límite ($|q| < 1$)** | $S_\infty = \frac{t_1}{1 - q}$ |
| **Producto de Términos** | $P_n = \sqrt{(t_1 \cdot t_n)^n} = (t_c)^n$ |
| **Interpolación Geométrica** | $q = \sqrt[m + 1]{\frac{B}{A}} \quad (m \text{ medios})$ |

---

### Modelos y Series Especiales

| Modelo Físico / Financiero | Ecuación Representativa |
| :--- | :--- |
| **Ley de Rebotes Sucesivos** | $D_{\text{total}} = H_0 \cdot \left(\frac{q + p}{q - p}\right) \quad \text{donde } h_{k+1} = \frac{p}{q} \cdot h_k$ |
| **Serie Aritmético-Geométrica** | $S_\infty = \sum_{k=1}^\infty \frac{k}{q^k} = \frac{q}{(q - 1)^2} \quad (|q| > 1)$ |
