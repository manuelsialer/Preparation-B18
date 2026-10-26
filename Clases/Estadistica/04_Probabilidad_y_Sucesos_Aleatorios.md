# Tema 04: Probabilidad y Sucesos Aleatorios

## 1. Motivación y Contexto Real

La incertidumbre es una condición inherente al mundo real: desde la predicción de heladas y sequías en la agricultura altoandina de Puno y Cusco, hasta la modelación epidemiológica, el control de calidad en plantas procesadoras de alimentos y la toma de decisiones financieras en proyectos de inversión comunal. En todos estos escenarios, no podemos predecir con certeza absoluta el resultado exacto de un fenómeno, pero sí podemos cuantificar rigurosamente la posibilidad de que ocurra mediante la **teoría de probabilidades**.

En el marco de la prueba de preselección de Beca 18, la competencia evaluada es *"Resuelve problemas de gestión de datos e incertidumbre"*. Dominar el cálculo de probabilidades a través de la **regla de Laplace**, el álgebra de conjuntos para eventos mutuamente excluyentes o solapados, el concepto de eventos independientes y la probabilidad condicional elemental, permite al estudiante estructurar razonamientos lógicos deductivos sólidos y resolver con rapidez problemas situados de alta exigencia académica.

---

## 2. Fundamento Teórico

### 2.1 Experimento Aleatorio y Espacio Muestral
* **Experimento Determinista:** Aquel cuyo resultado se conoce con exactitud de antemano bajo las mismas condiciones (ej. soltar un objeto desde una altura y medir la aceleración de la gravedad).
* **Experimento Aleatorio ($\mathcal{E}$):** Aquel que, repetido bajo idénticas condiciones, produce resultados que dependen del azar y no pueden predecirse con certeza (ej. lanzar dos dados, extraer una bola de una urna).
* **Espacio Muestral ($\Omega$):** Conjunto formado por todos los resultados posibles del experimento aleatorio. Su cardinal se denota $n(\Omega)$.
* **Suceso o Evento ($A$):** Cualquier subconjunto del espacio muestral ($A \subseteq \Omega$).

### 2.2 Regla Clásica de Laplace (Sucesos Equiprobables)
Si todos los sucesos elementales de un espacio muestral finito $\Omega$ tienen la misma posibilidad de ocurrir (son equiprobables), la probabilidad de que ocurra el evento $A$ se define como:

$$P(A) = \frac{\text{Número de casos favorables a } A}{\text{Número total de casos posibles en } \Omega} = \frac{n(A)}{n(\Omega)}$$

```{figure} ../../assets/estadistica/diagrama_arbol_probabilidad.svg
---
width: 90%
align: center
alt: Diagrama de Venn y Regla de Laplace
---
*Figura 1: Espacio muestral $\Omega$, eventos $A$ y $B$, intersección y axiomas fundamentales de probabilidad.*
```

### 2.3 Axiomas y Propiedades Fundamentales
1. **Acotamiento:** Para cualquier suceso $A$:
   
$$0 \le P(A) \le 1$$

2. **Suceso Seguro ($\Omega$):**
   
$$P(\Omega) = 1$$

3. **Suceso Imposible ($\emptyset$):**
   
$$P(\emptyset) = 0$$

4. **Suceso Complementario o Contrario ($A^c$ o $A'$):**
   
$$P(A^c) = 1 - P(A)$$

5. **Regla de la Adición (Unión de Sucesos):**
   * **En general (eventos compatibles):**
     
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
     
   * **Sucesos Mutuamente Excluyentes o Disjuntos ($A \cap B = \emptyset$):**
     
$$P(A \cup B) = P(A) + P(B)$$

### 2.4 Sucesos Independientes y Probabilidad Condicional
* **Probabilidad Condicional ($P(A \mid B)$):** Probabilidad de que ocurra el evento $A$ dado que ya ha ocurrido con certeza el evento $B$ (con $P(B) > 0$):
  
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

* **Sucesos Independientes:** Dos sucesos $A$ y $B$ son independientes si la ocurrencia de uno no altera la probabilidad de ocurrencia del otro. Se cumple estrictamente:
  
$$P(A \cap B) = P(A) \cdot P(B)$$

---

## 3. Ejercicios Resueltos Paso a Paso

### Problema 1: Lanzamiento de Dos Dados Legítimos
Se lanzan simultáneamente dos dados corrientes no cargados de 6 caras. Calcule la probabilidad de que la suma de los puntos obtenidos sea mayor o igual a 9.

**Solución:**

**Paso 1:** Determinar el tamaño del espacio muestral $\Omega$:

$$n(\Omega) = 6 \times 6 = 36$$

**Paso 2:** Identificar los pares ordenados $(d_1, d_2)$ cuya suma sea $\ge 9$:
* Suma = 9: $(3,6), (4,5), (5,4), (6,3) \implies 4 \text{ casos}$
* Suma = 10: $(4,6), (5,5), (6,4) \implies 3 \text{ casos}$
* Suma = 11: $(5,6), (6,5) \implies 2 \text{ casos}$
* Suma = 12: $(6,6) \implies 1 \text{ caso}$

**Paso 3:** Contar los casos favorables $n(A)$:

$$n(A) = 4 + 3 + 2 + 1 = 10$$

**Paso 4:** Aplicar la regla de Laplace:

$$P(A) = \frac{n(A)}{n(\Omega)} = \frac{10}{36} = \frac{5}{18} \approx 0.2778 \quad (27.78\%)$$

---

### Problema 2: Extracción sin Reposición de una Urna
En una urna hay 7 bolas rojas, 5 bolas azules y 8 bolas verdes. Si se extraen sucesivamente 2 bolas al azar sin reposición, calcule la probabilidad de que la primera sea roja y la segunda sea verde.

**Solución:**

**Paso 1:** Calcular el número total inicial de bolas:

$$N = 7 + 5 + 8 = 20 \text{ bolas}$$

**Paso 2:** Probabilidad de que la primera bola sea roja:

$$P(R_1) = \frac{7}{20}$$

**Paso 3:** Como la extracción es sin reposición, quedan 19 bolas en la urna, de las cuales 8 siguen siendo verdes. La probabilidad condicional es:

$$P(V_2 \mid R_1) = \frac{8}{19}$$

**Paso 4:** Aplicar la regla de la multiplicación:

$$P(R_1 \cap V_2) = P(R_1) \cdot P(V_2 \mid R_1) = \frac{7}{20} \times \frac{8}{19} = \frac{56}{380} = \frac{14}{95}$$

---

### Problema 3: Aplicación de la Regla de la Adición
En un grupo de 100 postulantes de una academia preuniversitaria, 60 estudian Matemática, 40 estudian Comunicación y 25 estudian ambas materias. Si se escoge un postulante al azar, calcule la probabilidad de que estudie al menos una de las dos materias.

**Solución:**

**Paso 1:** Identificar las probabilidades individuales:

$$P(M) = \frac{60}{100} = 0.60, \quad P(C) = \frac{40}{100} = 0.40, \quad P(M \cap C) = \frac{25}{100} = 0.25$$

**Paso 2:** Aplicar el principio de adición para la unión:

$$P(M \cup C) = P(M) + P(C) - P(M \cap C)$$

**Paso 3:** Sustituir y calcular:

$$P(M \cup C) = 0.60 + 0.40 - 0.25 = 0.75 \quad (75\%)$$

---

### Problema 4: Probabilidad del Complemento
Se lanzan 4 monedas corrientes al aire. Calcule la probabilidad de obtener al menos una cara.

**Solución:**

**Paso 1:** Determinar el espacio muestral:

$$n(\Omega) = 2^4 = 16$$

**Paso 2:** Definir el evento contrario $A^c$: "No obtener ninguna cara" (es decir, obtener 4 sellos).
El único caso favorable a $A^c$ es $(S, S, S, S)$:

$$n(A^c) = 1 \implies P(A^c) = \frac{1}{16}$$

**Paso 3:** Aplicar la propiedad del complemento:

$$P(A) = 1 - P(A^c) = 1 - \frac{1}{16} = \frac{15}{16} = 0.9375 \quad (93.75\%)$$

---

### Problema 5: Eventos Independientes
Dos tiradores, Tony y Manuel, disparan a un blanco de manera independiente. La probabilidad de que Tony acierte es $\frac{3}{5}$ y la de Manuel es $\frac{2}{3}$. Si ambos disparan simultáneamente, calcule la probabilidad de que el blanco sea impactado al menos una vez.

**Solución:**

**Paso 1:** Utilizar el suceso complementario: "Ninguno acierta el blanco".
* Probabilidad de que Tony falle: $P(T^c) = 1 - \frac{3}{5} = \frac{2}{5}$.
* Probabilidad de que Manuel falle: $P(M^c) = 1 - \frac{2}{3} = \frac{1}{3}$.

**Paso 2:** Por ser eventos independientes:

$$P(T^c \cap M^c) = P(T^c) \cdot P(M^c) = \frac{2}{5} \times \frac{1}{3} = \frac{2}{15}$$

**Paso 3:** Calcular la probabilidad de al menos un impacto:

$$P(\text{Impacto}) = 1 - P(T^c \cap M^c) = 1 - \frac{2}{15} = \frac{13}{15}$$

---

### Problema 6: Probabilidad Condicional en Tablas de Contingencia
La siguiente tabla muestra la distribución de 200 postulantes según procedencia y condición de ingreso:

| Procedencia | Ingresó ($I$) | No Ingresó ($I^c$) | Total |
| :--- | :---: | :---: | :---: |
| Urbana | 50 | 70 | 120 |
| Rural | 40 | 40 | 80 |
| **Total** | **90** | **110** | **200** |

Si se selecciona al azar a un postulante y se sabe que proviene de zona rural, ¿cuál es la probabilidad de que haya ingresado?

**Solución:**

**Paso 1:** El espacio muestral se reduce a los postulantes de zona rural:

$$n(\text{Rural}) = 80$$

**Paso 2:** Casos favorables que ingresaron dentro de esa condición:

$$n(\text{Ingresó y Rural}) = 40$$

**Paso 3:** Calcular la probabilidad condicional:

$$P(I \mid \text{Rural}) = \frac{n(I \cap \text{Rural})}{n(\text{Rural})} = \frac{40}{80} = \frac{1}{2} = 0.50 \quad (50\%)$$

---

### Problema 7: Extracción con Reposición
De una baraja de 52 cartas se extraen sucesivamente dos cartas con reposición. Calcule la probabilidad de que ambas sean figuras (As, J, Q, K).

**Solución:**

**Paso 1:** En una baraja de 52 cartas hay 4 palos, y en cada uno hay 4 figuras (As, J, Q, K). Por tanto, hay $4 \times 4 = 16$ figuras.

**Paso 2:** La probabilidad de extraer una figura en la primera extracción es:

$$P(F_1) = \frac{16}{52} = \frac{4}{13}$$

**Paso 3:** Como la extracción es con reposición, el mazo vuelve a tener 52 cartas y 16 figuras. Por independencia:

$$P(F_2) = \frac{4}{13}$$

**Paso 4:** Multiplicar las probabilidades:

$$P(F_1 \cap F_2) = \frac{4}{13} \times \frac{4}{13} = \frac{16}{169}$$

---

### Problema 8: Urnas con Selecciones Combinatorias
En una caja hay 6 focos buenos y 4 defectuosos. Si se extraen al azar 3 focos simultáneamente, ¿cuál es la probabilidad de que exactamente 2 sean buenos?

**Solución:**

**Paso 1:** Calcular el número total de formas de elegir 3 focos de un total de 10:

$$n(\Omega) = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

**Paso 2:** Calcular las formas favorables de elegir exactamente 2 buenos (de los 6) y 1 defectuoso (de los 4):

$$n(A) = \binom{6}{2} \times \binom{4}{1} = \left( \frac{6 \times 5}{2 \times 1} \right) \times 4 = 15 \times 4 = 60$$

**Paso 3:** Aplicar la regla de Laplace:

$$P(A) = \frac{60}{120} = \frac{1}{2} = 0.50 \quad (50\%)$$

---

### Problema 9: Sucesos Mutuamente Excluyentes
Al extraer una carta de una baraja de 52 cartas, ¿cuál es la probabilidad de obtener un Rey o un As?

**Solución:**

**Paso 1:** Una carta no puede ser simultáneamente Rey y As ($R \cap A = \emptyset$). Son eventos mutuamente excluyentes.

**Paso 2:** Hay 4 Reyes y 4 Ases en la baraja:

$$P(R) = \frac{4}{52}, \quad P(A) = \frac{4}{52}$$

**Paso 3:** Aplicar la regla de adición:

$$P(R \cup A) = P(R) + P(A) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52} = \frac{2}{13}$$

---

### Problema 10: Producto de Puntos en Dos Dados
Se lanzan dos dados. ¿Cuál es la probabilidad de que el producto de los números obtenidos sea un número impar?

**Solución:**

**Paso 1:** El producto de dos enteros es impar si y solo si **ambos** números son impares.

**Paso 2:** En un dado, los impares son $\{1, 3, 5\} \implies 3$ casos de 6:

$$P(\text{Impar en dado 1}) = \frac{3}{6} = \frac{1}{2}$$

$$P(\text{Impar en dado 2}) = \frac{3}{6} = \frac{1}{2}$$

**Paso 3:** Como los dados son independientes:

$$P(\text{Producto Impar}) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = 0.25 \quad (25\%)$$

---

## 4. Práctica Propuesta

### Nivel 1: Regla de Laplace y Sucesos Elementales (Ejercicios 1 al 15)

1. Al lanzar una moneda no trucada, la probabilidad de obtener sello es:  
A) 0  
B) 0.25  
C) 0.50  
D) 0.75  
E) 1

2. Al lanzar un dado de 6 caras, la probabilidad de obtener un número primo es:  
A) $\frac{1}{6}$  
B) $\frac{1}{3}$  
C) $\frac{1}{2}$  
D) $\frac{2}{3}$  
E) $\frac{5}{6}$

3. De una bolsa con 4 bolas blancas y 6 bolas negras se extrae una bola al azar. ¿Cuál es la probabilidad de que sea blanca?  
A) 0.2  
B) 0.3  
C) 0.4  
D) 0.5  
E) 0.6

4. Si la probabilidad de que llueva mañana en Huancayo es 0.35, la probabilidad de que NO llueva es:  
A) 0.35  
B) 0.55  
C) 0.65  
D) 0.75  
E) 0.85

5. La probabilidad de un suceso seguro siempre es igual a:  
A) 0  
B) 0.5  
C) 1  
D) 100  
E) $\infty$

6. Al lanzar dos monedas al aire, la probabilidad de obtener dos caras es:  
A) $\frac{1}{4}$  
B) $\frac{1}{2}$  
C) $\frac{3}{4}$  
D) $\frac{1}{3}$  
E) $\frac{2}{3}$

7. En una baraja de 52 cartas, ¿cuál es la probabilidad de extraer un trébol?  
A) $\frac{1}{52}$  
B) $\frac{1}{13}$  
C) $\frac{1}{4}$  
D) $\frac{1}{2}$  
E) $\frac{4}{13}$

8. Si $A$ y $B$ son sucesos mutuamente excluyentes, entonces $P(A \cap B)$ es:  
A) 1  
B) $0.5$  
C) 0  
D) $P(A) \cdot P(B)$  
E) $P(A) + P(B)$

9. Al lanzar un dado, ¿cuál es la probabilidad de obtener un múltiplo de 3?  
A) $\frac{1}{6}$  
B) $\frac{1}{3}$  
C) $\frac{1}{2}$  
D) $\frac{2}{3}$  
E) $\frac{5}{6}$

10. De una urna con los números del 1 al 20, se extrae una ficha. ¿Cuál es la probabilidad de que sea un número par menor que 10?  
A) $\frac{1}{5}$  
B) $\frac{1}{4}$  
C) $\frac{3}{10}$  
D) $\frac{2}{5}$  
E) $\frac{1}{2}$

11. Si se escoge una letra al azar de la palabra "BECA", ¿cuál es la probabilidad de que sea una vocal?  
A) $\frac{1}{4}$  
B) $\frac{1}{2}$  
C) $\frac{3}{4}$  
D) 1  
E) 0

12. Un suceso imposible tiene probabilidad:  
A) 0  
B) 1  
C) Negativa  
D) $0.001$  
E) Indeterminada

13. Al lanzar dos dados, ¿cuántos elementos tiene el espacio muestral $\Omega$?  
A) 12  
B) 24  
C) 36  
D) 48  
E) 64

14. Si $P(A) = 0.4$ y $P(B) = 0.3$ con $A$ y $B$ disjuntos, entonces $P(A \cup B)$ es:  
A) 0.12  
B) 0.50  
C) 0.70  
D) 0.85  
E) 1.00

15. En un salón de 15 mujeres y 25 varones, se elige un delegado al azar. ¿Cuál es la probabilidad de que sea mujer?  
A) $\frac{3}{8}$  
B) $\frac{5}{8}$  
C) $\frac{1}{4}$  
D) $\frac{1}{2}$  
E) $\frac{3}{5}$

---

### Nivel 2: Eventos Compuestos y Probabilidad Condicional (Ejercicios 16 al 30)

16. Al lanzar dos dados, ¿cuál es la probabilidad de que la suma de sus caras sea exactamente 7?  
A) $\frac{1}{12}$  
B) $\frac{1}{9}$  
C) $\frac{1}{6}$  
D) $\frac{5}{36}$  
E) $\frac{7}{36}$

17. En una caja hay 5 fichas rojas y 3 azules. Se extraen dos fichas sin reposición. ¿Cuál es la probabilidad de que ambas sean rojas?  
A) $\frac{5}{14}$  
B) $\frac{5}{16}$  
C) $\frac{25}{64}$  
D) $\frac{5}{28}$  
E) $\frac{15}{56}$

18. En el problema anterior, si la extracción es con reposición, ¿cuál es la probabilidad de que ambas sean rojas?  
A) $\frac{25}{64}$  
B) $\frac{5}{14}$  
C) $\frac{15}{64}$  
D) $\frac{9}{64}$  
E) $\frac{1}{2}$

19. Si $P(A) = 0.6$, $P(B) = 0.5$ y $P(A \cap B) = 0.3$, calcule $P(A \cup B)$:  
A) 0.7  
B) 0.8  
C) 0.9  
D) 1.0  
E) 0.65

20. Con los datos del problema anterior, calcule la probabilidad condicional $P(A \mid B)$:  
A) 0.50  
B) 0.60  
C) 0.75  
D) 0.80  
E) 0.30

21. Se lanzan 3 monedas. ¿Cuál es la probabilidad de obtener exactamente dos caras?  
A) $\frac{1}{8}$  
B) $\frac{1}{4}$  
C) $\frac{3}{8}$  
D) $\frac{1}{2}$  
E) $\frac{5}{8}$

22. Al extraer una carta de una baraja de 52 cartas, ¿cuál es la probabilidad de que sea un Rey o una carta de Corazones?  
A) $\frac{4}{13}$  
B) $\frac{17}{52}$  
C) $\frac{8}{52}$  
D) $\frac{15}{52}$  
E) $\frac{1}{4}$

23. Se lanzan dos dados. ¿Cuál es la probabilidad de que ambos dados muestren el mismo número (dobles)?  
A) $\frac{1}{36}$  
B) $\frac{1}{12}$  
C) $\frac{1}{6}$  
D) $\frac{5}{36}$  
E) $\frac{1}{4}$

24. Si dos eventos independientes $A$ y $B$ tienen $P(A) = 0.5$ y $P(B) = 0.4$, el valor de $P(A \cap B)$ es:  
A) 0.1  
B) 0.2  
C) 0.3  
D) 0.9  
E) 0.45

25. En una ruleta de 36 números (del 1 al 36), ¿cuál es la probabilidad de que caiga en un número par o mayor que 27?  
A) $\frac{19}{36}$  
B) $\frac{22}{36}$  
C) $\frac{23}{36}$  
D) $\frac{24}{36}$  
E) $\frac{25}{36}$

26. De un grupo de 10 personas (6 hombres y 4 mujeres) se eligen 2 al azar. ¿Cuál es la probabilidad de que ambos sean mujeres?  
A) $\frac{1}{15}$  
B) $\frac{2}{15}$  
C) $\frac{4}{15}$  
D) $\frac{1}{3}$  
E) $\frac{2}{5}$

27. Si se lanzan dos dados, ¿cuál es la probabilidad de que la suma sea menor o igual a 4?  
A) $\frac{1}{12}$  
B) $\frac{1}{6}$  
C) $\frac{5}{36}$  
D) $\frac{7}{36}$  
E) $\frac{2}{9}$

28. La probabilidad de que un estudiante apruebe Matemática es 0.7 y de que apruebe Física es 0.6. Si ambos sucesos son independientes, ¿cuál es la probabilidad de que apruebe al menos uno de los dos cursos?  
A) 0.88  
B) 0.90  
C) 0.92  
D) 0.95  
E) 0.84

29. En una urna con 3 bolas rojas, 4 azules y 5 verdes, se extrae una bola que resulta NO ser roja. ¿Cuál es la probabilidad de que sea verde?  
A) $\frac{5}{12}$  
B) $\frac{5}{9}$  
C) $\frac{4}{9}$  
D) $\frac{1}{2}$  
E) $\frac{5}{7}$

30. Un candado tiene 3 discos, cada uno con dígitos del 0 al 9. Si se desconoce la clave, ¿cuál es la probabilidad de acertarla en el primer intento?  
A) 0.01  
B) 0.003  
C) 0.001  
D) 0.0001  
E) 0.03

---

### Nivel 3: Problemas Tipo Examen Beca 18 (Ejercicios 31 al 45)

31. En una comunidad nativa del VRAEM, el 70% de las familias cultiva cacao, el 50% cultiva café y el 30% cultiva ambos. Si se elige una familia al azar y se verifica que cultiva café, ¿cuál es la probabilidad de que también cultive cacao?  
A) 0.40  
B) 0.50  
C) 0.60  
D) 0.70  
E) 0.75

32. Se tienen dos cajas: la Caja 1 contiene 4 esferas blancas y 2 negras; la Caja 2 contiene 3 blancas y 5 negras. Se elige una caja al azar con igual probabilidad y de ella se extrae una esfera. Calcule la probabilidad de que la esfera extraída sea blanca.  
A) $\frac{23}{48}$  
B) $\frac{25}{48}$  
C) $\frac{27}{48}$  
D) $\frac{29}{48}$  
E) $\frac{31}{48}$

33. Tres máquinas A, B y C de una planta procesadora producen el 50%, 30% y 20% de los envases respectivamente. Los porcentajes de envases defectuosos son 2%, 3% y 5% respectivamente. Si se elige un envase al azar de la producción total, ¿cuál es la probabilidad de que sea defectuoso?  
A) 0.025  
B) 0.029  
C) 0.031  
D) 0.035  
E) 0.040

34. En el problema anterior, si el envase seleccionado resultó ser defectuoso, ¿cuál es la probabilidad de que haya sido producido por la máquina A?  
A) $\frac{10}{29}$  
B) $\frac{9}{29}$  
C) $\frac{12}{29}$  
D) $\frac{15}{29}$  
E) $\frac{18}{29}$

35. Se lanzan simultáneamente 5 monedas corrientes. ¿Cuál es la probabilidad de obtener más caras que sellos?  
A) $\frac{1}{4}$  
B) $\frac{3}{8}$  
C) $\frac{1}{2}$  
D) $\frac{5}{8}$  
E) $\frac{5}{16}$

36. En una bolsa hay 10 caramelos de fresa y 15 de limón. Si un niño extrae 3 caramelos al azar uno por uno sin reposición, ¿cuál es la probabilidad de que los tres sean de fresa?  
A) $\frac{12}{115}$  
B) $\frac{9}{115}$  
C) $\frac{6}{115}$  
D) $\frac{8}{115}$  
E) $\frac{3}{23}$

37. La probabilidad de que un proyectil impacte en el blanco es 0.4. ¿Cuántos disparos independientes como mínimo se deben realizar para que la probabilidad de acertar al menos una vez sea mayor o igual al 90%?  
A) 3  
B) 4  
C) 5  
D) 6  
E) 7

38. Se colocan al azar 4 cartas rotuladas con las letras B, E, C, A en una fila. ¿Cuál es la probabilidad de que formen exactamente la palabra "BECA"?  
A) $\frac{1}{12}$  
B) $\frac{1}{16}$  
C) $\frac{1}{24}$  
D) $\frac{1}{36}$  
E) $\frac{1}{48}$

39. Si $A$ y $B$ son dos sucesos tales que $P(A \cup B) = \frac{5}{6}$, $P(A \cap B) = \frac{1}{3}$ y $P(A^c) = \frac{1}{2}$, determine el valor de $P(B)$:  
A) $\frac{1}{3}$  
B) $\frac{1}{2}$  
C) $\frac{2}{3}$  
D) $\frac{3}{4}$  
E) $\frac{5}{12}$

40. En una mesa circular se sientan 5 amigos al azar. ¿Cuál es la probabilidad de que dos amigos específicos (Ana y Beto) se sienten juntos?  
A) $\frac{1}{4}$  
B) $\frac{1}{3}$  
C) $\frac{1}{2}$  
D) $\frac{2}{5}$  
E) $\frac{3}{5}$

41. De un lote de 12 computadoras portátiles donde 3 tienen fallas de fabricación, se seleccionan 2 al azar para una escuela rural de Apurímac. ¿Cuál es la probabilidad de que al menos una tenga fallas?  
A) $\frac{10}{22}$  
B) $\frac{17}{22}$  
C) $\frac{9}{22}$  
D) $\frac{13}{22}$  
E) $\frac{7}{22}$

42. Dos personas acuerdan encontrarse en la plaza de armas de Huamanga entre las 3:00 p.m. y las 4:00 p.m. Cada una esperará a la otra como máximo 15 minutos. Si sus llegadas son independientes y uniformemente distribuidas en esa hora, ¿cuál es la probabilidad de que se encuentren?  
A) $\frac{7}{16}$  
B) $\frac{9}{16}$  
C) $\frac{5}{16}$  
D) $\frac{1}{2}$  
E) $\frac{3}{8}$

43. Se lanzan dos dados normales. Sabiendo que la suma de sus puntos fue un número par, ¿cuál es la probabilidad de que la suma haya sido exactamente 8?  
A) $\frac{5}{18}$  
B) $\frac{5}{36}$  
C) $\frac{1}{6}$  
D) $\frac{2}{9}$  
E) $\frac{1}{3}$

44. En una urna hay 4 fichas numeradas del 1 al 4. Se extraen dos fichas simultáneamente. Calcule la probabilidad de que la suma de las cifras sea impar.  
A) $\frac{1}{3}$  
B) $\frac{1}{2}$  
C) $\frac{2}{3}$  
D) $\frac{3}{4}$  
E) $\frac{5}{6}$

45. Se tiene un circuito con dos interruptores conectados en paralelo, cada uno de los cuales funciona independientemente con probabilidad $p = 0.9$. La probabilidad de que la corriente fluya a través del circuito es:  
A) 0.81  
B) 0.90  
C) 0.95  
D) 0.99  
E) 0.85

---

## 5. Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | C | **31** | C |
| **2** | C | **17** | A | **32** | B |
| **3** | C | **18** | A | **33** | B |
| **4** | C | **19** | B | **34** | A |
| **5** | C | **20** | B | **35** | C |
| **6** | A | **21** | C | **36** | C |
| **7** | C | **22** | A | **37** | C |
| **8** | C | **23** | C | **38** | C |
| **9** | B | **24** | B | **39** | C |
| **10** | A | **25** | B | **40** | C |
| **11** | B | **26** | B | **41** | A |
| **12** | A | **27** | B | **42** | A |
| **13** | C | **28** | A | **43** | A |
| **14** | C | **29** | B | **44** | C |
| **15** | A | **30** | C | **45** | D |

---

## 6. Autoevaluación y Metacognición

Reflexiona sobre tu proceso de resolución respondiendo a los siguientes criterios:

```{table} Rúbrica de Logro del Aprendizaje
:widths: 20 40 40

| Criterio de Logro | Nivel Alcanzado (Inicial / Autónomo) | Evidencia de Aprendizaje |
| :--- | :--- | :--- |
| **Regla de Laplace** | ¿Identifico con precisión el espacio muestral $\Omega$ y los casos favorables sin duplicidades? | Resuelve extracciones combinatorias con y sin reposición con rigor. |
| **Axiomas y Complemento** | ¿Utilizo el evento contrario $P(A) = 1 - P(A^c)$ en problemas de "al menos uno"? | Simplifica cálculos complejos de probabilidades múltiples eficientemente. |
| **Eventos Independientes y Condicionales** | ¿Diferencio con certeza cuándo dos sucesos son independientes frente a eventos condicionados? | Aplica $P(A \cap B) = P(A)P(B)$ o $P(A \mid B)$ en tablas de contingencia y urnas. |
| **Probabilidad Total y Bayes** | ¿Descompongo problemas de múltiples etapas (máquinas, urnas compuestas) mediante árboles lógicos? | Calcula probabilidades de causas a posteriori en situaciones productivas reales. |
```

---

## 7. Formulario Resumen

| Concepto / Teorema | Fórmula / Expresión Matemática |
| :--- | :--- |
| **Regla Clásica de Laplace** | $P(A) = \dfrac{n(A)}{n(\Omega)} = \dfrac{\text{Casos favorables}}{\text{Casos posibles}}$ |
| **Acotamiento Fundamental** | $0 \le P(A) \le 1, \quad P(\emptyset) = 0, \quad P(\Omega) = 1$ |
| **Suceso Contrario o Complementario** | $P(A^c) = 1 - P(A)$ |
| **Regla de la Adición General** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Sucesos Mutuamente Excluyentes** | $P(A \cup B) = P(A) + P(B) \quad (A \cap B = \emptyset)$ |
| **Probabilidad Condicional** | $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} \quad (P(B) > 0)$ |
| **Sucesos Independientes** | $P(A \cap B) = P(A) \cdot P(B)$ |
| **Teorema de la Probabilidad Total** | $P(B) = \sum_{i=1}^{k} P(A_i) \cdot P(B \mid A_i)$ |
| **Teorema de Bayes** | $P(A_j \mid B) = \dfrac{P(A_j) \cdot P(B \mid A_j)}{\sum_{i=1}^{k} P(A_i) \cdot P(B \mid A_i)}$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 2 clave(s) corregida(s) y 5 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **17** | A | A | Corregida | La opción B repetía el valor de A ($\frac{10}{28}=\frac{5}{14}$); se reemplazó por un distractor distinto. Respuesta: $\frac{5}{14}$ (A). |
| **22** | A | A | Corregida | La opción C repetía el valor de A ($\frac{16}{52}=\frac{4}{13}$); se reemplazó. Respuesta: $\frac{16}{52}=\frac{4}{13}$ (A). |
| **25** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **36** | C | C | Corregida | La opción B era equivalente a A ($\frac{24}{230}=\frac{12}{115}$); se reemplazó por un distractor. $P=\frac{10}{25}\cdot\frac{9}{24}\cdot\frac{8}{23}=\frac{6}{115}$. Clave C. |
| **41** | D | A | Corregida | Se ajustó la opción A: $1-\frac{\binom{9}{2}}{\binom{12}{2}}=\frac{5}{11}=\frac{10}{22}$. Clave A. |

**Claves sin cambios:** 43 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
