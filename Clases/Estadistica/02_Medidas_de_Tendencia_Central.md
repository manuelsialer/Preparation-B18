# Tema 02: Medidas de Tendencia Central y Dispersión

## 1. Motivación y Contexto Real

Al analizar el rendimiento de los postulantes de distintas regiones en los simulacros de Beca 18, o al evaluar el ingreso per cápita de familias beneficiarias del programa Juntos, los resúmenes basados en tablas de frecuencias resultan informativos pero no suficientes. Para comparar dos poblaciones de manera sintética, se requiere un valor numérico representativo en torno al cual se concentran los datos: una **medida de tendencia central**.

Sin embargo, limitarse a calcular el promedio o media aritmética puede generar conclusiones distorsionadas si la distribución posee valores extremos atípicos (outliers) o un sesgo pronunciado. Por ello, el análisis estadístico profesional y las preguntas de alta exigencia del examen integran armónicamente la **Media Aritmética ($\bar{x}$)**, la **Mediana ($Me$)** y la **Moda ($Mo$)**, analizando su comportamiento relativo para diagnosticar la asimetría de la distribución y su representatividad real.

---

## 2. Fundamento Teórico

### 2.1 Media Aritmética ($\bar{x}$)
Es el centro de gravedad de la distribución. Se calcula como la suma ponderada de todos los valores dividida entre el tamaño de la muestra:
* **Para datos no agrupados:**
  
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

* **Para datos agrupados en intervalos de clase:**
  
$$\bar{x} = \frac{\sum_{i=1}^{k} x_i f_i}{n} = \sum_{i=1}^{k} x_i h_i$$

  *Donde $x_i$ es la marca de clase del $i$-ésimo intervalo y $f_i$ su frecuencia absoluta.*

### 2.2 Mediana ($Me$)
Es el valor que divide a la muestra ordenada exactamente en dos mitades (50% de las observaciones son menores o iguales a $Me$ y 50% son mayores o iguales).
* **Para datos agrupados:**
  1. Se localiza la **clase mediana**, que es el primer intervalo cuya frecuencia acumulada satisface:
     
$$F_i \ge \frac{n}{2}$$
     
  2. Se aplica la fórmula de interpolación lineal:
     
$$Me = L_i + C \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right)$$
     
     *Donde:*
     * $L_i$: Límite inferior de la clase mediana.
     * $C$: Amplitud de la clase mediana.
     * $n$: Tamaño total de la muestra.
     * $F_{i-1}$: Frecuencia absoluta acumulada del intervalo anterior.
     * $f_i$: Frecuencia absoluta del intervalo mediano.

### 2.3 Moda ($Mo$)
Es el valor que se presenta con mayor frecuencia en la distribución.
* **Para datos agrupados:**
  1. Se localiza la **clase modal**, que es el intervalo con la máxima frecuencia absoluta $f_i$.
  2. Se aplica la fórmula:
     
$$Mo = L_i + C \left( \frac{d_1}{d_1 + d_2} \right)$$
     
     *Donde:*
     * $d_1 = f_i - f_{i-1}$ (diferencia con la frecuencia anterior).
     * $d_2 = f_i - f_{i+1}$ (diferencia con la frecuencia posterior).
     * $L_i, C$: Límite inferior y ancho de la clase modal.

```{figure} ../../assets/estadistica/medidas_tendencia_central_asimetria.svg
---
width: 95%
align: center
alt: Asimetría de Distribuciones
---
*Figura 1: Relación de orden entre Media ($\bar{x}$), Mediana ($Me$) y Moda ($Mo$) según la asimetría de la curva de frecuencias.*
```

### 2.4 Asimetría y Relación entre Medidas
* **Distribución Simétrica:** La curva es perfectamente equilibrada (campana de Gauss).
  
$$\bar{x} = Me = Mo$$

* **Asimetría Positiva (Sesgada a la Derecha):** Cola extendida hacia valores grandes.
  
$$Mo < Me < \bar{x}$$

* **Asimetría Negativa (Sesgada a la Izquierda):** Cola extendida hacia valores pequeños.
  
$$\bar{x} < Me < Mo$$

---

## 3. Ejercicios Resueltos Paso a Paso

### Problema 1: Cálculo de Media en Datos Agrupados
Calcule la media aritmética de la siguiente distribución de edades de 40 estudiantes:

| Intervalo | $x_i$ | $f_i$ |
| :---: | :---: | :---: |
| $[14, 18\rangle$ | 16 | 10 |
| $[18, 22\rangle$ | 20 | 18 |
| $[22, 26\rangle$ | 24 | 12 |

**Solución:**

**Paso 1:** Calcular los productos $x_i f_i$:
* Intervalo 1: $16 \times 10 = 160$
* Intervalo 2: $20 \times 18 = 360$
* Intervalo 3: $24 \times 12 = 288$

**Paso 2:** Sumar los productos:

$$\sum x_i f_i = 160 + 360 + 288 = 808$$

**Paso 3:** Dividir entre $n = 40$:

$$\bar{x} = \frac{808}{40} = 20.2 \text{ años}$$

---

### Problema 2: Cálculo de la Mediana
A partir de la tabla del Problema 1, calcule el valor exacto de la mediana.

**Solución:**

**Paso 1:** Hallar la posición de la mediana:

$$\frac{n}{2} = \frac{40}{2} = 20$$

**Paso 2:** Determinar la clase mediana observando las frecuencias acumuladas:
* $F_1 = 10 < 20$
* $F_2 = 10 + 18 = 28 \ge 20$

La clase mediana es el segundo intervalo: $[18, 22\rangle$.

**Paso 3:** Identificar los parámetros:
* $L_i = 18$
* $C = 22 - 18 = 4$
* $F_{i-1} = F_1 = 10$
* $f_i = f_2 = 18$

**Paso 4:** Aplicar la fórmula de la mediana:

$$Me = 18 + 4 \left( \frac{20 - 10}{18} \right) = 18 + 4 \left( \frac{10}{18} \right) = 18 + \frac{40}{18} = 18 + 2.22 = 20.22 \text{ años}$$

---

### Problema 3: Cálculo de la Moda
A partir de la tabla del Problema 1, calcule la moda.

**Solución:**

**Paso 1:** Identificar la clase modal (máxima frecuencia). La mayor frecuencia es $f_2 = 18$, perteneciente a $[18, 22\rangle$.

**Paso 2:** Calcular las diferencias $d_1$ y $d_2$:
* $d_1 = f_2 - f_1 = 18 - 10 = 8$
* $d_2 = f_2 - f_3 = 18 - 12 = 6$

**Paso 3:** Aplicar la fórmula de la moda con $L_i = 18$ y $C = 4$:

$$Mo = 18 + 4 \left( \frac{8}{8 + 6} \right) = 18 + 4 \left( \frac{8}{14} \right) = 18 + \frac{32}{14} \approx 18 + 2.29 = 20.29 \text{ años}$$

---

### Problema 4: Diagnóstico de Asimetría
En un examen de admisión, la media de los puntajes fue 68.4, la mediana fue 65.2 y la moda fue 61.0. Determine el tipo de asimetría de la distribución e interprete el resultado.

**Solución:**

**Paso 1:** Comparar las tres medidas en orden:

$$61.0 < 65.2 < 68.4 \implies Mo < Me < \bar{x}$$

**Paso 2:** Identificar el tipo de asimetría:
Corresponde a una **asimetría positiva (sesgada a la derecha)**.

**Paso 3:** Interpretación contextual:
La mayoría de los postulantes obtuvo puntajes concentrados en valores bajos o moderados (la moda es 61), mientras que un grupo selecto de postulantes con puntajes muy altos eleva el promedio hacia 68.4.

---

### Problema 5: Propiedad de Desviaciones respecto a la Media
Demuestre y verifique algebraicamente que la suma de las desviaciones de un conjunto de datos respecto a su media aritmética es idénticamente nula: $\sum_{i=1}^{n} (x_i - \bar{x}) = 0$.

**Solución:**

**Paso 1:** Expandir la sumatoria utilizando linealidad:

$$\sum_{i=1}^{n} (x_i - \bar{x}) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \bar{x}$$

**Paso 2:** La suma de una constante repetida $n$ veces es $n \cdot \bar{x}$:

$$\sum_{i=1}^{n} \bar{x} = n \bar{x}$$

**Paso 3:** Sustituir la definición de la media $\sum x_i = n \bar{x}$:

$$\sum_{i=1}^{n} (x_i - \bar{x}) = n \bar{x} - n \bar{x} = 0$$

Queda formalmente demostrado.

---

### Problema 6: Reconstrucción de Frecuencia Faltante a partir de la Media
Se tiene la siguiente tabla donde se desconoce $f_2$:

| Intervalo | $x_i$ | $f_i$ |
| :---: | :---: | :---: |
| $[10, 20\rangle$ | 15 | 8 |
| $[20, 30\rangle$ | 25 | $k$ |
| $[30, 40\rangle$ | 35 | 12 |

Si la media aritmética de la distribución es 26.25, determine el valor de $k$.

**Solución:**

**Paso 1:** Expresar el número total de datos $n$ en función de $k$:

$$n = 8 + k + 12 = 20 + k$$

**Paso 2:** Expresar la suma de productos $\sum x_i f_i$:

$$\sum x_i f_i = (15 \times 8) + (25 \times k) + (35 \times 12) = 120 + 25k + 420 = 540 + 25k$$

**Paso 3:** Plantear la ecuación de la media:

$$\bar{x} = \frac{540 + 25k}{20 + k} = 26.25$$

**Paso 4:** Resolver para $k$:

$$540 + 25k = 26.25(20 + k) \implies 540 + 25k = 525 + 26.25k$$

$$540 - 525 = 26.25k - 25k \implies 15 = 1.25k \implies k = \frac{15}{1.25} = 12$$

---

### Problema 7: Efecto de una Transformación Lineal en la Media
Si las notas $x_i$ de un aula tienen una media $\bar{x} = 13.5$, y el docente decide aplicar la transformación $y_i = 1.2 x_i + 2$ a cada nota, ¿cuál será la nueva media $\bar{y}$?

**Solución:**

**Paso 1:** Aplicar la propiedad de linealidad de la media aritmética:
Si $y = a x + b$, entonces $\bar{y} = a \bar{x} + b$.

**Paso 2:** Sustituir los valores dados:

$$\bar{y} = 1.2(13.5) + 2$$

**Paso 3:** Calcular:

$$1.2 \times 13.5 = 16.2 \implies \bar{y} = 16.2 + 2 = 18.2$$

---

### Problema 8: Media Ponderada de Grupos Combinados
La sección A de Beca 18 tiene 30 alumnos con una media de 72 puntos, y la sección B tiene 20 alumnos con una media de 82 puntos. ¿Cuál es la media general del conjunto de ambas secciones?

**Solución:**

**Paso 1:** Calcular el puntaje total acumulado de cada sección:
* Sección A: $30 \times 72 = 2160$
* Sección B: $20 \times 82 = 1640$

**Paso 2:** Sumar los puntajes totales y los alumnos:

$$\text{Puntaje total} = 2160 + 1640 = 3800$$

$$N_{\text{total}} = 30 + 20 = 50$$

**Paso 3:** Calcular la media ponderada:

$$\bar{x}_{\text{combinada}} = \frac{3800}{50} = 76 \text{ puntos}$$

---

### Problema 9: Mediana con Datos Simétricos
En una distribución de 5 intervalos simétricos con ancho común $C = 10$, el intervalo central es $[40, 50\rangle$. Calcule el valor de la mediana sin utilizar la fórmula de interpolación.

**Solución:**

**Paso 1:** Por propiedad matemática, en cualquier distribución perfectamente simétrica unimodal, la mediana coincide con el centro geométrico de la distribución.

**Paso 2:** El centro del intervalo central $[40, 50\rangle$ es su marca de clase:

$$x_3 = \frac{40 + 50}{2} = 45$$

Por lo tanto, $Me = 45$.

---

### Problema 10: Rango Medio (Midrange)
Calcule el rango medio de las temperaturas registradas en Puno durante una semana: $-3^\circ\text{C}, 0^\circ\text{C}, 4^\circ\text{C}, 7^\circ\text{C}, 12^\circ\text{C}, 15^\circ\text{C}, 17^\circ\text{C}$.

**Solución:**

**Paso 1:** Identificar el valor mínimo y máximo:
* $x_{\min} = -3$
* $x_{\max} = 17$

**Paso 2:** Aplicar la definición de rango medio:

$$\text{Rango Medio} = \frac{x_{\min} + x_{\max}}{2} = \frac{-3 + 17}{2} = \frac{14}{2} = 7^\circ\text{C}$$

---

## 4. Práctica Propuesta

### Nivel 1: Conceptos y Algoritmos Básicos (Ejercicios 1 al 15)

1. La media de los números 12, 16, 18, 20, 24 es:  
A) 16  
B) 17  
C) 18  
D) 19  
E) 20

2. La mediana de la serie ordenada: 5, 8, 12, 14, 19, 22, 27 es:  
A) 12  
B) 14  
C) 16  
D) 19  
E) 13

3. La moda del conjunto de datos 4, 7, 7, 8, 9, 7, 10, 11 es:  
A) 4  
B) 7  
C) 8  
D) 9  
E) 10

4. Si en una muestra ordenada de 8 elementos los valores centrales son 14 y 18, la mediana es:  
A) 14  
B) 15  
C) 16  
D) 17  
E) 18

5. ¿Cuál de las siguientes medidas es sensible a valores extremos o atípicos?  
A) Mediana  
B) Moda  
C) Media Aritmética  
D) Cuartil 2  
E) Percentil 50

6. En una distribución simétrica unimodal se cumple siempre que:  
A) $\bar{x} > Me > Mo$  
B) $\bar{x} < Me < Mo$  
C) $\bar{x} = Me = Mo$  
D) $\bar{x} + Mo = 2Me$ pero no son iguales  
E) $Me = 0$

7. La suma de las desviaciones de un conjunto de datos respecto a su media es:  
A) Siempre positiva  
B) Siempre 1  
C) Siempre 0  
D) Igual a la varianza  
E) Negativa

8. Si a todos los datos de una muestra se les suma 5 unidades, su media aritmética:  
A) Se multiplica por 5  
B) Aumenta en 5 unidades  
C) No cambia  
D) Se divide entre 5  
E) Queda elevada al cuadrado

9. Si a todos los datos de una muestra se les multiplica por 3, su mediana:  
A) No varía  
B) Se triplica  
C) Aumenta en 3  
D) Se divide por 3  
E) Queda al cubo

10. Para encontrar la clase mediana en datos agrupados con $n = 60$, se busca el primer intervalo donde:  
A) $f_i \ge 30$  
B) $F_i \ge 30$  
C) $h_i \ge 0.50$  
D) $x_i \ge 30$  
E) $C \ge 30$

11. La clase modal en una distribución agrupada es aquel intervalo que posee:  
A) La mayor marca de clase  
B) La mayor frecuencia acumulada  
C) La mayor frecuencia absoluta  
D) El mayor ancho de clase  
E) El menor límite inferior

12. Si una distribución presenta dos modas con igual frecuencia máxima, se denomina:  
A) Amodal  
B) Unimodal  
C) Bimodal  
D) Simétrica  
E) Dispersa

13. Para la serie 2, 4, 6, 8, la media es:  
A) 4  
B) 5  
C) 6  
D) 7  
E) 4.5

14. Si la media de 6 números es 15, la suma total de dichos números es:  
A) 60  
B) 75  
C) 90  
D) 105  
E) 120

15. El percentil 50 de una distribución continua equivale exactamente a:  
A) La Media  
B) La Mediana  
C) La Moda  
D) El Rango  
E) La Desviación Media

---

### Nivel 2: Cálculos con Tablas y Propiedades (Ejercicios 16 al 30)

16. En la siguiente distribución: $[20, 30\rangle$ (5), $[30, 40\rangle$ (15), $[40, 50\rangle$ (10). La media aritmética es:  
A) 34.67  
B) 35.00  
C) 36.67  
D) 37.50  
E) 38.00

17. En la distribución anterior con $n = 30$, la clase mediana es:  
A) $[20, 30\rangle$  
B) $[30, 40\rangle$  
C) $[40, 50\rangle$  
D) No existe  
E) Entre el primer y segundo intervalo

18. Calcule la mediana de la distribución del problema 16:  
A) 35.00  
B) 36.67  
C) 37.00  
D) 38.25  
E) 36.00

19. Si $Mo = 24$, $Me = 28$ y $\bar{x} = 30$, la distribución presenta:  
A) Asimetría negativa  
B) Distribución normal  
C) Asimetría positiva  
D) Simetría perfecta  
E) Varianza nula

20. En un salón de 20 mujeres y 30 varones, el promedio de notas de las mujeres es 16 y el de los varones es 14. La media del aula es:  
A) 14.5  
B) 14.8  
C) 15.0  
D) 15.2  
E) 15.4

21. Si la media de 5 números es 12 y se retira el número 20, la nueva media de los 4 números restantes es:  
A) 9  
B) 10  
C) 11  
D) 11.5  
E) 12

22. En una tabla de 3 intervalos de amplitud 10, con marcas de clase 15, 25, 35 y frecuencias relativas 0.20, 0.50, 0.30, la media es:  
A) 24  
B) 25  
C) 26  
D) 27  
E) 28

23. Si la clase modal es $[40, 60\rangle$ con $f_{modal} = 25$, $f_{anterior} = 15$ y $f_{posterior} = 20$, calcule la moda:  
A) 45.0  
B) 48.0  
C) 50.0  
D) 53.3  
E) 55.0

24. La media geométrica de los números 2, 4, 8 es:  
A) 3  
B) 4  
C) 5  
D) 6  
E) 8

25. La media armónica de los números 2, 3 y 6 es:  
A) 2.5  
B) 3.0  
C) 3.5  
D) 4.0  
E) 4.5

26. Para dos cantidades positivas $a$ y $b$, siempre se cumple que:  
A) $MA \le MG \le MH$  
B) $MH \le MG \le MA$  
C) $MG \le MH \le MA$  
D) $MA = MG \cdot MH$  
E) $MA \le MH \le MG$

27. Si el producto de dos números positivos es 64 y su media aritmética es 10, su media armónica es:  
A) 5.8  
B) 6.4  
C) 7.2  
D) 8.0  
E) 8.5

28. En una prueba, 10 alumnos sacaron 12, 15 alumnos sacaron 15 y 5 alumnos sacaron 18. La moda es:  
A) 12  
B) 14  
C) 15  
D) 16  
E) 18

29. Si la suma de 10 datos es 140 y al agregar un dato $x$ la media pasa a ser 15, el valor de $x$ es:  
A) 15  
B) 20  
C) 22  
D) 25  
E) 28

30. La mediana de los sueldos en una empresa es S/ 2500. Si a todos los empleados se les concede un aumento del 10% más una bonificación fija de S/ 100, la nueva mediana es:  
A) S/ 2600  
B) S/ 2750  
C) S/ 2850  
D) S/ 2900  
E) S/ 3000

---

### Nivel 3: Problemas Avanzados Tipo Beca 18 (Ejercicios 31 al 45)

31. En una distribución de ingresos con 4 intervalos de amplitud constante, se sabe que $x_1 = 300, x_4 = 600$, $f_1 = 20, f_2 = 40, f_3 = 30, f_4 = 10$. Calcule el valor de la mediana.  
A) 416.7  
B) 425.0  
C) 433.3  
D) 440.0  
E) 450.0

32. En una prueba diagnóstica nacional, las notas de 100 postulantes se agruparon en 5 intervalos simétricos con $C = 4$. Si la moda coincide con la media y es igual a 14, determine la suma de los límites del tercer intervalo.  
A) 24  
B) 26  
C) 28  
D) 30  
E) 32

33. Un grupo de estudiantes rinde un examen donde la media es 54 con desvío 12. Si el profesor estandariza las notas para que la nueva media sea 70 mediante $y = a x + b$, sabiendo que un alumno con nota 54 pasa a tener 70 y uno con 70 pasa a tener 90, halle $a + b$.  
A) 18.25  
B) 17.50  
C) 18.75  
D) 16.00  
E) 19.25

34. En una tabla acumulada de 5 intervalos de amplitud 10, se conoce: $F_1 = 12, F_2 = 30, F_3 = 55, F_4 = 80, F_5 = 100$. Si $L_1 = 20$, calcule la mediana:  
A) 45.0  
B) 46.5  
C) 48.0  
D) 49.2  
E) 50.0

35. Calcule la moda para los datos del problema anterior:  
A) 45.0  
B) 46.2  
C) 47.5  
D) 48.0  
E) 50.0

36. La media de 50 números es 38. Si se eliminan dos números que son 45 y 55, ¿en cuánto varía la media aritmética de los restantes?  
A) Disminuye en 0.5  
B) Disminuye en 0.25  
C) Aumenta en 0.5  
D) Disminuye en 0.75  
E) No varía

37. En una comunidad campesina de Cusco, la producción mensual de quinua por parcela (en kg) sigue una distribución con asimetría positiva moderada donde $\bar{x} = 420$ y $Mo = 360$. Utilizando la relación empírica de Pearson: $\bar{x} - Mo \approx 3(\bar{x} - Me)$, estime el valor de la mediana:  
A) 380  
B) 390  
C) 400  
D) 410  
E) 415

38. Se sabe que la media armónica y la media aritmética de dos números enteros positivos son 3.2 y 5 respectivamente. Calcule la diferencia positiva de dichos números.  
A) 4  
B) 5  
C) 6  
D) 7  
E) 8

39. En una tabla con 4 intervalos de amplitud $C$, el intervalo modal es $[30, 40\rangle$. Si $f_{modal} = 40$, $f_{anterior} = 20$, $f_{posterior} = 20$, calcule la moda:  
A) 33.3  
B) 34.0  
C) 35.0  
D) 36.5  
E) 37.2

40. Si la media aritmética de $x_1, x_2, \dots, x_n$ es $\bar{x}$, determine el valor de $\sum_{i=1}^{n} (x_i - \bar{x} + 4)$:  
A) $4\bar{x}$  
B) $4n$  
C) 0  
D) $n(\bar{x} + 4)$  
E) $4$

41. En una empresa los sueldos tienen una media de S/ 1800. Si los hombres (el 60% del personal) ganan en promedio S/ 2000, ¿cuál es el sueldo promedio de las mujeres?  
A) S/ 1400  
B) S/ 1500  
C) S/ 1600  
D) S/ 1650  
E) S/ 1700

42. Si las marcas de clase de tres intervalos son 10, 20 y 30 con frecuencias relativas $h_1, h_2, h_3$ que forman una progresión aritmética creciente con razón $r = 0.1$, determine la media aritmética:  
A) 20  
B) 21  
C) 22  
D) 23  
E) 24

43. Una muestra de 80 datos tiene $Me = 42$. Si se añaden 10 datos todos iguales a 60, la nueva mediana:  
A) Sigue siendo 42 o se desplaza a la derecha  
B) Disminuye obligatoriamente  
C) Es 51  
D) Es 60  
E) Se duplica

44. Para un conjunto de datos agrupados, si todos los intervalos tienen la misma frecuencia $f_i = k$ (distribución uniforme continua en $[A, B\rangle$), la media y la mediana son iguales a:  
A) $\frac{B - A}{2}$  
B) $\frac{A + B}{2}$  
C) $\sqrt{AB}$  
D) $k$  
E) $B - A$

45. En una distribución con media 50, mediana 48 y moda 44, se afirma:  
I. La distribución presenta sesgo a la derecha.  
II. La mitad de las observaciones es menor o igual a 48.  
III. La cola más larga se extiende hacia valores menores a 44.  
¿Cuáles afirmaciones son verdaderas?  
A) Solo I  
B) Solo II  
C) I y II  
D) II y III  
E) Todas

---

## 5. Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | C | **31** | A |
| **2** | B | **17** | B | **32** | C |
| **3** | B | **18** | B | **33** | C |
| **4** | C | **19** | C | **34** | C |
| **5** | C | **20** | B | **35** | A |
| **6** | C | **21** | B | **36** | B |
| **7** | C | **22** | C | **37** | C |
| **8** | B | **23** | D | **38** | C |
| **9** | B | **24** | B | **39** | C |
| **10** | B | **25** | B | **40** | B |
| **11** | C | **26** | B | **41** | B |
| **12** | C | **27** | B | **42** | C |
| **13** | B | **28** | C | **43** | A |
| **14** | C | **29** | D | **44** | B |
| **15** | B | **30** | C | **45** | C |

---

## 6. Autoevaluación y Metacognición

Reflexiona sobre tu proceso de resolución respondiendo a los siguientes criterios:

```{table} Rúbrica de Logro del Aprendizaje
:widths: 20 40 40

| Criterio de Logro | Nivel Alcanzado (Inicial / Autónomo) | Evidencia de Aprendizaje |
| :--- | :--- | :--- |
| **Cálculo de la Media** | ¿Calculo la media en datos sueltos y agrupados reconociendo el rol de las ponderaciones? | Resuelve promedios de grupos combinados y reconstruye frecuencias incógnitas. |
| **Interpolación de Mediana y Moda** | ¿Aplico con fluidez las fórmulas de interpolación identificando correctamente $L_i, C, F_{i-1}, d_1, d_2$? | Encuentra la mediana y moda sin confundir frecuencias absolutas con acumuladas. |
| **Diagnóstico de Asimetría** | ¿Reconozco el tipo de sesgo de una distribución comparando el orden de $\bar{x}, Me$ y $Mo$? | Interpreta gráficos de campana o histogramas asimétricos con rigor técnico. |
| **Propiedades Algebraicas** | ¿Aplico las propiedades de sumatoria de desviaciones y transformaciones lineales ($y = ax+b$)? | Determina cambios en la media y mediana ante aumentos porcentuales y constantes. |
```

---

## 7. Formulario Resumen

| Concepto / Teorema | Fórmula / Expresión Matemática |
| :--- | :--- |
| **Media para Datos Agrupados ($\bar{x}$)** | $\bar{x} = \dfrac{\sum x_i f_i}{n} = \sum x_i h_i$ |
| **Mediana para Datos Agrupados ($Me$)** | $Me = L_i + C \left( \dfrac{\frac{n}{2} - F_{i-1}}{f_i} \right)$ |
| **Moda para Datos Agrupados ($Mo$)** | $Mo = L_i + C \left( \dfrac{d_1}{d_1 + d_2} \right)$ |
| **Diferencias Modales ($d_1, d_2$)** | $d_1 = f_i - f_{i-1}, \quad d_2 = f_i - f_{i+1}$ |
| **Distribución Simétrica** | $\bar{x} = Me = Mo$ |
| **Asimetría Positiva (Derecha)** | $Mo < Me < \bar{x}$ |
| **Asimetría Negativa (Izquierda)** | $\bar{x} < Me < Mo$ |
| **Transformación Lineal ($y = ax + b$)** | $\bar{y} = a\bar{x} + b, \quad Me_y = a Me_x + b$ |
| **Suma de Desviaciones a la Media** | $\sum_{i=1}^{n} (x_i - \bar{x}) = 0$ |
| **Relación Empírica de Pearson** | $\bar{x} - Mo \approx 3(\bar{x} - Me)$ |
