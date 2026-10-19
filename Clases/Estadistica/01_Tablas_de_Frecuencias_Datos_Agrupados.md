# Tema 01: Tablas de Frecuencias y Datos Agrupados

## 1. Motivación y Contexto Real

En los censos agropecuarios y estudios socioeconómicos del INEI y PRONABEC en diversas regiones del Perú (como el valle del Mantaro o las cooperativas cafetaleras de Quillabamba), los investigadores recopilan miles de registros numéricos: ingresos familiares, hectáreas cultivadas o edades de postulantes. Trabajar con una masa de datos desordenada e individual resulta inviable.

Para extraer información significativa, el primer paso riguroso consiste en **tabular y agrupar los datos en intervalos de clase**. Esto permite transformar miles de observaciones dispersas en una distribución de frecuencias estructurada, calculando marcas de clase, frecuencias relativas porcentuales y acumuladas. Dominar esta técnica es indispensable para la toma de decisiones basada en evidencia y constituye una de las competencias matemáticas más evaluadas en Beca 18.

---

## 2. Fundamento Teórico

### 2.1 Conceptos Fundamentales
* **Población ($N$):** Conjunto total de individuos u objetos con una característica común observable.
* **Muestra ($n$):** Subconjunto representativo de la población.
* **Alcance ($A$):** Intervalo cerrado delimitado por el valor mínimo y máximo:
  
  $$A = [x_{\min}, x_{\max}]$$
  
* **Rango o Recorrido ($R$):** Amplitud total de los datos:
  
  $$R = x_{\max} - x_{\min}$$

### 2.2 Reglas de Agrupamiento en Intervalos
Para datos continuos o discretos con amplio rango, se divide el recorrido en $k$ intervalos de clase $[L_i, L_s\rangle$:
1. **Número de Intervalos ($k$):** Comúnmente estimado mediante la **Regla de Sturges**:
   
   $$k = 1 + 3.322 \log_{10}(n)$$
   
   *(El valor de $k$ se redondea al entero más próximo).*
2. **Ancho o Amplitud de Clase ($C$ o $w$):** Longitud de cada intervalo (asumiendo amplitud constante):
   
   $$C = \frac{R}{k}$$

3. **Marca de Clase ($x_i$):** Punto medio del intervalo, representativo de los datos en esa clase:
   
   $$x_i = \frac{L_i + L_s}{2}$$

```{figure} ../../assets/estadistica/histograma_poligono_frecuencias.svg
---
width: 90%
align: center
alt: Histograma y Polígono de Frecuencias
---
*Figura 1: Histograma de datos agrupados y su correspondiente polígono de frecuencias obtenido al unir las marcas de clase ($x_i$).*
```

### 2.3 Tipos de Frecuencias
* **Frecuencia Absoluta ($f_i$):** Número de observaciones pertenecientes al $i$-ésimo intervalo. Cumple:
  
  $$\sum_{i=1}^{k} f_i = n$$

* **Frecuencia Relativa ($h_i$):** Proporción de datos en el intervalo:
  
  $$h_i = \frac{f_i}{n}, \quad \sum_{i=1}^{k} h_i = 1$$

* **Frecuencia Relativa Porcentual ($h_i\%$):**
  
  $$h_i\% = h_i \times 100\%$$

* **Frecuencias Acumuladas:**
  * **Absoluta Acumulada ($F_i$):** $F_i = \sum_{j=1}^{i} f_j = F_{i-1} + f_i$, con $F_k = n$.
  * **Relativa Acumulada ($H_i$):** $H_i = \sum_{j=1}^{i} h_j = H_{i-1} + h_i$, con $H_k = 1$.

---

## 3. Ejercicios Resueltos Paso a Paso

### Problema 1: Reconstrucción de Tabla de Frecuencias
En una muestra de $n = 50$ postulantes a Beca 18, los puntajes se agruparon en 5 intervalos de ancho común. Se sabe que $f_1 = 8$, $h_2 = 0.24$, $F_3 = 35$, y $h_4 = h_5$. Calcule el valor de $f_5$.

**Solución:**

**Paso 1:** Hallar $f_2$ a partir de la frecuencia relativa $h_2$:

$$f_2 = n \cdot h_2 = 50 \cdot 0.24 = 12$$

**Paso 2:** Utilizar la frecuencia acumulada $F_3$ para determinar $f_3$:

$$F_3 = f_1 + f_2 + f_3 \implies 35 = 8 + 12 + f_3 \implies f_3 = 15$$

**Paso 3:** Calcular la suma de las frecuencias restantes:

$$f_1 + f_2 + f_3 = 35 \implies f_4 + f_5 = n - 35 = 50 - 35 = 15$$

**Paso 4:** Dado que $h_4 = h_5$, se cumple $f_4 = f_5$. Por ende:

$$2 f_5 = 15 \implies f_5 = 7.5$$

Si los datos son discretos enteros ajustados, $f_4 + f_5 = 15$ indica frecuencias de 8 y 7 o datos de ponderación continua. Para $f_4 = f_5 = 7.5$ en densidad teórica, el valor es $7.5$.

---

### Problema 2: Cálculo de Marca de Clase e Intervalos
El cuarto intervalo de una distribución de amplitudes iguales es $[40, 50\rangle$. Si hay 6 intervalos en total, determine el valor de la segunda marca de clase ($x_2$).

**Solución:**

**Paso 1:** Determinar la amplitud de clase $C$:

$$C = L_s - L_i = 50 - 40 = 10$$

**Paso 2:** Deducir los límites de los intervalos anteriores restando la amplitud $C = 10$:
* Intervalo 4: $[40, 50\rangle$
* Intervalo 3: $[30, 40\rangle$
* Intervalo 2: $[20, 30\rangle$

**Paso 3:** Calcular la marca de clase $x_2$:

$$x_2 = \frac{20 + 30}{2} = 25$$

---

### Problema 3: Interpolación Lineal en Frecuencias Acumuladas
Dada la siguiente tabla acumulada:

| Intervalo | $f_i$ | $F_i$ |
| :---: | :---: | :---: |
| $[10, 20\rangle$ | 10 | 10 |
| $[20, 30\rangle$ | 25 | 35 |
| $[30, 40\rangle$ | 40 | 75 |
| $[40, 50\rangle$ | 25 | 100 |

Estime cuántas observaciones son menores que 34 mediante interpolación lineal.

**Solución:**

**Paso 1:** Identificar el intervalo donde se encuentra el valor 34. Pertenece al tercer intervalo $[30, 40\rangle$, con $L_i = 30$, $C = 10$, y $f_3 = 40$.

**Paso 2:** Todas las observaciones de los intervalos previos son menores que 30:

$$F_2 = 35$$

**Paso 3:** En el intervalo $[30, 40\rangle$, la fracción de intervalo desde 30 hasta 34 es:

$$\text{Fracción} = \frac{34 - 30}{40 - 30} = \frac{4}{10} = 0.4$$

**Paso 4:** Multiplicar la fracción por la frecuencia del intervalo $f_3 = 40$:

$$\Delta f = 0.4 \times 40 = 16$$

**Paso 5:** Sumar las observaciones previas:

$$\text{Total} = F_2 + \Delta f = 35 + 16 = 51$$

Existen 51 observaciones menores que 34.

---

### Problema 4: Porcentaje de Datos en Rango Específico
A partir de la tabla del Problema 3, ¿qué porcentaje del total de datos se encuentra en el rango $[25, 45\rangle$?

**Solución:**

**Paso 1:** En $[20, 30\rangle$, desde 25 hasta 30 hay una amplitud de 5 de un total de 10:

$$f_{[25, 30\rangle} = \frac{30 - 25}{10} \times 25 = \frac{5}{10} \times 25 = 12.5$$

**Paso 2:** El intervalo $[30, 40\rangle$ está completamente contenido:

$$f_{[30, 40\rangle} = 40$$

**Paso 3:** En $[40, 50\rangle$, desde 40 hasta 45 hay una amplitud de 5 de 10:

$$f_{[40, 45\rangle} = \frac{45 - 40}{10} \times 25 = 12.5$$

**Paso 4:** Sumar todas las frecuencias del rango:

$$f_{\text{total}} = 12.5 + 40 + 12.5 = 65$$

**Paso 5:** Calcular el porcentaje respecto a $n = 100$:

$$\% = \frac{65}{100} \times 100\% = 65\%$$

---

### Problema 5: Relación entre $h_i$ y $H_i$
En una distribución simétrica de 5 intervalos de amplitud constante se tiene que $h_1 = 0.10$ y $H_3 = 0.70$. Calcule el valor de $h_2$.

**Solución:**

**Paso 1:** Por simetría de la distribución:

$$h_1 = h_5 = 0.10, \quad h_2 = h_4$$

**Paso 2:** La suma de todas las frecuencias relativas es 1:

$$h_1 + h_2 + h_3 + h_4 + h_5 = 1 \implies 0.10 + 2h_2 + h_3 + 0.10 = 1 \implies 2h_2 + h_3 = 0.80$$

**Paso 3:** Usar el dato de la frecuencia relativa acumulada $H_3$:

$$H_3 = h_1 + h_2 + h_3 = 0.70 \implies 0.10 + h_2 + h_3 = 0.70 \implies h_2 + h_3 = 0.60$$

**Paso 4:** Restar la segunda ecuación de la primera:

$$(2h_2 + h_3) - (h_2 + h_3) = 0.80 - 0.60 \implies h_2 = 0.20$$

---

### Problema 6: Número Total de Datos a partir de Proporciones
En una empresa agroindustrial, el 30% de los trabajadores gana menos de S/ 1200. Si en la tabla de frecuencias el intervalo $[1000, 1200\rangle$ tiene una frecuencia absoluta acumulada $F_2 = 180$, determine el tamaño de la muestra $n$.

**Solución:**

**Paso 1:** El enunciado indica que el límite superior del segundo intervalo es 1200, por lo que los trabajadores que ganan menos de 1200 corresponden a $F_2$.

**Paso 2:** La frecuencia relativa acumulada correspondiente es $H_2 = 30\% = 0.30$.

**Paso 3:** Aplicar la relación $H_2 = \frac{F_2}{n}$:

$$0.30 = \frac{180}{n} \implies n = \frac{180}{0.30} = 600$$

---

### Problema 7: Reconstrucción con Marcas de Clase
Se tiene una tabla con 4 intervalos donde $x_1 = 15$ y $x_3 = 35$. Si $f_1 = 10$, $f_2 = 20$, $f_3 = 30$, $f_4 = 40$, determine el valor del límite superior del último intervalo.

**Solución:**

**Paso 1:** La diferencia entre marcas de clase consecutivas es igual a la amplitud de clase $C$:

$$x_3 - x_1 = 2C \implies 35 - 15 = 2C \implies 20 = 2C \implies C = 10$$

**Paso 2:** Calcular los límites del primer intervalo $[L_1, L_2\rangle$:

$$x_1 = \frac{L_1 + L_2}{2} = 15, \quad L_2 - L_1 = 10 \implies L_1 = 10, \quad L_2 = 20$$

**Paso 3:** Los límites de los 4 intervalos son:
$[10, 20\rangle, [20, 30\rangle, [30, 40\rangle, [40, 50\rangle$.

El límite superior del último intervalo es 50.

---

### Problema 8: Rango y Regla de Sturges
Para un conjunto de 64 datos cuyo valor mínimo es 22 y el máximo es 86, calcule el ancho de clase sugerido por Sturges.

**Solución:**

**Paso 1:** Calcular el número de intervalos $k$ con $n = 64$:

$$k = 1 + 3.322 \log_{10}(64) \approx 1 + 3.322(1.806) \approx 1 + 6.00 = 7$$

**Paso 2:** Calcular el rango $R$:

$$R = x_{\max} - x_{\min} = 86 - 22 = 64$$

**Paso 3:** Calcular el ancho de clase $C$:

$$C = \frac{R}{k} = \frac{64}{7} \approx 9.14 \implies C \approx 10 \quad \text{(redondeo práctico)}$$

---

### Problema 9: Cálculo de la Suma Ponderada de Marcas de Clase
Dada la distribución:

| Intervalo | $x_i$ | $f_i$ |
| :---: | :---: | :---: |
| $[10, 20\rangle$ | 15 | 4 |
| $[20, 30\rangle$ | 25 | 6 |
| $[30, 40\rangle$ | 35 | 10 |

Calcule $\sum_{i=1}^{3} x_i f_i$.

**Solución:**

**Paso 1:** Multiplicar cada marca de clase por su frecuencia absoluta:
* $x_1 f_1 = 15 \times 4 = 60$
* $x_2 f_2 = 25 \times 6 = 150$
* $x_3 f_3 = 35 \times 10 = 350$

**Paso 2:** Sumar los productos:

$$\sum_{i=1}^{3} x_i f_i = 60 + 150 + 350 = 560$$

---

### Problema 10: Frecuencia Relativa Acumulada
En una tabla de 4 intervalos, se sabe que $h_1 = 0.15$, $H_2 = 0.45$, $h_3 = 0.30$. Calcule $h_4$ y $H_3$.

**Solución:**

**Paso 1:** Calcular $h_2$ a partir de $H_2$:

$$H_2 = h_1 + h_2 \implies 0.45 = 0.15 + h_2 \implies h_2 = 0.30$$

**Paso 2:** Calcular $H_3$:

$$H_3 = H_2 + h_3 = 0.45 + 0.30 = 0.75$$

**Paso 3:** Calcular $h_4$ sabiendo que $H_4 = 1$:

$$h_4 = 1 - H_3 = 1 - 0.75 = 0.25$$

---

## 4. Práctica Propuesta

### Nivel 1: Comprensión y Algoritmos Básicos (Ejercicios 1 al 15)

1. En una distribución de 50 datos agrupados, la frecuencia absoluta del tercer intervalo es 15. ¿Cuál es su frecuencia relativa porcentual?  
A) 25%  
B) 30%  
C) 35%  
D) 20%  
E) 15%

2. Si el rango de un conjunto de datos es 48 y se divide en 6 intervalos de igual amplitud, ¿cuál es el ancho de clase?  
A) 6  
B) 7  
C) 8  
D) 9  
E) 10

3. El intervalo de clase es $[24, 38\rangle$. Su marca de clase es:  
A) 29  
B) 30  
C) 31  
D) 32  
E) 33

4. Si $F_3 = 42$ y $F_2 = 27$, el valor de $f_3$ es:  
A) 12  
B) 14  
C) 15  
D) 16  
E) 17

5. La suma de todas las frecuencias relativas $h_i$ de una distribución siempre es igual a:  
A) 0  
B) 1  
C) 10  
D) 100  
E) Depende de $n$

6. Si $x_1 = 12$ y $x_2 = 18$ en intervalos de ancho constante, la amplitud de clase es:  
A) 4  
B) 5  
C) 6  
D) 7  
E) 8

7. En una muestra de 80 elementos, $h_3 = 0.35$. ¿Cuántas observaciones pertenecen a dicho intervalo?  
A) 24  
B) 26  
C) 28  
D) 30  
E) 32

8. La marca de clase representa:  
A) La frecuencia absoluta  
B) El punto medio del intervalo  
C) El límite superior  
D) La amplitud de clase  
E) El total acumulado

9. Si el valor mínimo es 14 y el valor máximo es 74, el rango es:  
A) 58  
B) 60  
C) 62  
D) 64  
E) 66

10. Si $H_2 = 0.40$ y $h_3 = 0.25$, el valor de $H_3$ es:  
A) 0.50  
B) 0.55  
C) 0.60  
D) 0.65  
E) 0.70

11. El polígono de frecuencias se construye uniendo mediante segmentos:  
A) Los límites inferiores  
B) Los límites superiores  
C) Las marcas de clase en el tope de cada barra  
D) Los orígenes de coordenadas  
E) Las frecuencias acumuladas

12. Si $f_1 = 8$, $f_2 = 14$, $f_3 = 18$, el valor de $F_2$ es:  
A) 8  
B) 14  
C) 22  
D) 32  
E) 40

13. Para $n = 100$, si $F_4 = 85$, el número de datos mayores o iguales que el límite inferior del quinto intervalo es:  
A) 15  
B) 20  
C) 25  
D) 30  
E) 85

14. En un intervalo $[a, b\rangle$, el límite inferior es:  
A) $a$  
B) $b$  
C) $\frac{a+b}{2}$  
D) $b - a$  
E) $a + b$

15. Si la amplitud es 5 y la marca de clase es 17.5, el intervalo es:  
A) $[10, 15\rangle$  
B) $[12, 17\rangle$  
C) $[15, 20\rangle$  
D) $[16, 21\rangle$  
E) $[17, 22\rangle$

---

### Nivel 2: Aplicación Intermedia y Reconstrucción (Ejercicios 16 al 30)

16. En una tabla de frecuencias de 4 intervalos de igual amplitud, $x_2 = 28$ y $x_4 = 44$. El límite inferior del primer intervalo es:  
A) 16  
B) 18  
C) 20  
D) 22  
E) 24

17. Se tiene una muestra de 120 datos donde $h_1 = 0.15$, $h_2 = 0.25$, $f_3 = 48$. ¿Cuál es el valor de $f_4$ si solo hay 4 intervalos?  
A) 18  
B) 20  
C) 24  
D) 26  
E) 30

18. En una distribución con 5 intervalos simétricos, $f_1 = 12$, $F_3 = 60$, y $n = 80$. Calcule $f_2$.  
A) 16  
B) 18  
C) 20  
D) 22  
E) 24

19. Si $f_i / x_i = 2$ constante para tres intervalos cuyas marcas de clase son 10, 20 y 30, calcule el tamaño de muestra $n$.  
A) 80  
B) 100  
C) 120  
D) 140  
E) 160

20. En una tabla acumulada, $F_1 = 15$, $F_2 = 38$, $F_3 = 70$, $F_4 = 90$, $F_5 = 100$. ¿Cuál es el intervalo modal (el de mayor frecuencia absoluta)?  
A) 1  
B) 2  
C) 3  
D) 4  
E) 5

21. Si el 40% de observaciones está en el intervalo $[30, 50\rangle$, cuya marca de clase es 40, y la frecuencia absoluta de ese intervalo es 64, determine $n$.  
A) 140  
B) 150  
C) 160  
D) 180  
E) 200

22. Los datos de una encuesta muestran que $H_3 = 0.65$ y $H_4 = 0.85$. Si la muestra es de 200 personas, ¿cuántas personas pertenecen al cuarto intervalo?  
A) 30  
B) 35  
C) 40  
D) 45  
E) 50

23. Si un intervalo es $[L_i, L_s\rangle$ con $L_s - L_i = 8$ y $x_i = 25$, entonces $L_s$ vale:  
A) 27  
B) 28  
C) 29  
D) 30  
E) 31

24. A partir de una tabla de ingresos: $[400, 600\rangle$ con $f_1 = 30$, $[600, 800\rangle$ con $f_2 = 50$, $[800, 1000\rangle$ con $f_3 = 20$. ¿Cuántos ganan S/ 700 o más suponiendo distribución uniforme?  
A) 35  
B) 40  
C) 45  
D) 50  
E) 55

25. Si $h_1 = k$, $h_2 = 2k$, $h_3 = 3k$, $h_4 = 4k$, determine el valor de la constante $k$.  
A) 0.05  
B) 0.10  
C) 0.15  
D) 0.20  
E) 0.25

26. En el ejercicio anterior, si $n = 250$, ¿cuál es el valor de $f_3$?  
A) 50  
B) 60  
C) 75  
D) 80  
E) 100

27. Un histograma tiene barras contiguas porque:  
A) Las variables son cualitativas  
B) Los intervalos son disjuntos sin orden  
C) La variable es continua y los intervalos son consecutivos  
D) Aumenta la estética gráfica  
E) Representa porcentajes

28. Si el valor de $F_3 = 54$ y $h_4 = 0.28$ con $n = 100$, ¿cuántos datos hay en el quinto y último intervalo?  
A) 12  
B) 14  
C) 16  
D) 18  
E) 20

29. Si la suma de marcas de clase de dos intervalos consecutivos es 74 y la amplitud de clase es 6, calcule la menor de dichas marcas.  
A) 32  
B) 34  
C) 35  
D) 37  
E) 40

30. Si $f_1 = 20$, $f_2 = 30$, $f_3 = 50$, el valor del ángulo correspondiente al tercer intervalo en un diagrama circular es:  
A) $120^\circ$  
B) $150^\circ$  
C) $180^\circ$  
D) $200^\circ$  
E) $90^\circ$

---

### Nivel 3: Problemas Tipo Examen Beca 18 (Ejercicios 31 al 45)

31. En una investigación socioeconómica en Huancavelica, los gastos semanales de 200 familias se tabularon con ancho de clase común. Se tiene: $f_1 = 30$, $h_2 = 0.25$, $F_3 = 140$, $h_4 = 0.15$ y el resto en el quinto intervalo. ¿Qué porcentaje del total gasta un monto perteneciente a los dos últimos intervalos?  
A) 25%  
B) 30%  
C) 35%  
D) 40%  
E) 45%

32. En una tabla de frecuencias con 5 intervalos simétricos, la marca de clase central es $x_3 = 45$ y el ancho común es $C = 10$. Si $f_1 = 15$, $f_2 = 25$ y $n = 120$, calcule la suma de las frecuencias acumuladas $F_1 + F_2 + F_3 + F_4 + F_5$.  
A) 360  
B) 410  
C) 425  
D) 440  
E) 480

33. Se evalúan 400 postulantes cuyos puntajes van de 0 a 100 distribuidos uniformemente en 5 intervalos iguales. Si se aprueba con 65 puntos o más, y las frecuencias son $f_1 = 40, f_2 = 60, f_3 = 120, f_4 = 100, f_5 = 80$, ¿cuántos postulantes aprobaron?  
A) 155  
B) 160  
C) 165  
D) 170  
E) 175

34. Si en una distribución unimodal simétrica el tercer intervalo es $[50, 70\rangle$ y concentra al 40% de los datos con $f_3 = 80$, determine la frecuencia absoluta acumulada $F_2$.  
A) 40  
B) 50  
C) 60  
D) 70  
E) 80

35. Un estudio agrícola clasifica la producción de café en quintales: $[20, 30\rangle, [30, 40\rangle, [40, 50\rangle, [50, 60\rangle$. Las marcas de clase multiplicadas por sus frecuencias relativas arrojan: $x_1 h_1 = 5$, $x_2 h_2 = 10.5$, $x_3 h_3 = 13.5$. Calcule $h_4$.  
A) 0.10  
B) 0.15  
C) 0.20  
D) 0.25  
E) 0.30

36. En una tabla con $n = 500$ y 4 intervalos de amplitud constante, se cumple que $h_1 = h_4 = 0.12$ y $f_3 - f_2 = 40$. Determine el valor de $f_3$.  
A) 170  
B) 180  
C) 190  
D) 210  
E) 220

37. Al construir una ojiva (polígono de frecuencias acumuladas), el punto en el eje horizontal donde la ojiva alcanza el 50% de la muestra acumulada corresponde a:  
A) La media aritmética  
B) La mediana  
C) La moda  
D) El rango medio  
E) El desvío estándar

38. La siguiente tabla muestra los pesos de estudiantes: $[40, 50\rangle$ (10), $[50, 60\rangle$ (20), $[60, 70\rangle$ (30), $[70, 80\rangle$ (40). ¿Qué porcentaje pesa al menos 55 kg pero menos de 75 kg?  
A) 55%  
B) 60%  
C) 65%  
D) 70%  
E) 75%

39. Si el ancho de clase se duplica manteniendo el mismo rango y número de datos, el número de intervalos de clase $k$:  
A) Se duplica  
B) Se reduce a la mitad  
C) Se mantiene constante  
D) Se multiplica por 4  
E) No se puede determinar

40. En una distribución con 4 intervalos de amplitudes $C_1 = 5, C_2 = 10, C_3 = 10, C_4 = 15$, la densidad de frecuencia del segundo intervalo con $f_2 = 30$ es:  
A) 2  
B) 3  
C) 4  
D) 5  
E) 6

41. Sabiendo que $x_2 = 25, x_4 = 45$, y la tabla tiene 5 intervalos de clase con $f_i$ proporcional a $i^2$. Si $n = 110$, halle $f_3$.  
A) 12  
B) 18  
C) 24  
D) 36  
E) 45

42. En un sondeo a 300 jóvenes sobre horas semanales de estudio digital, $F_1 = 45$, $h_2 = 0.20$, $F_3 = 180$, y los dos intervalos restantes tienen igual frecuencia. ¿Cuántos jóvenes estudian en el quinto intervalo?  
A) 50  
B) 55  
C) 60  
D) 65  
E) 70

43. Si $L_1 = 10$, $C = 8$, y la tabla contiene 6 intervalos, la suma de las marcas de clase $x_1 + x_6$ es:  
A) 64  
B) 68  
C) 72  
D) 76  
E) 80

44. Un fabricante de baterías para paneles solares en Puno prueba 80 celdas. La tabla registra: $[2, 4\rangle$ (12), $[4, 6\rangle$ (28), $[6, 8\rangle$ (24), $[8, 10\rangle$ (16). Si las celdas con duración mayor a 7 años califican como óptimas, ¿cuántas celdas son óptimas?  
A) 24  
B) 26  
C) 28  
D) 30  
E) 32

45. En una tabla de distribución simétrica de 7 intervalos de ancho constante, se cumple que $x_4 = 50$, $f_4 = 30$ y $n = 150$. Si $f_1 = 5, f_2 = 15$, determine $f_3$.  
A) 25  
B) 30  
C) 35  
D) 40  
E) 45

---

## 5. Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | C | **31** | C |
| **2** | C | **17** | C | **32** | B |
| **3** | C | **18** | A | **33** | A |
| **4** | C | **19** | C | **34** | C |
| **5** | B | **20** | C | **35** | C |
| **6** | C | **21** | C | **36** | D |
| **7** | C | **22** | C | **37** | B |
| **8** | B | **23** | C | **38** | D |
| **9** | B | **24** | C | **39** | B |
| **10** | D | **25** | B | **40** | B |
| **11** | C | **26** | C | **41** | B |
| **12** | C | **27** | C | **42** | C |
| **13** | A | **28** | D | **43** | B |
| **14** | A | **29** | B | **44** | C |
| **15** | C | **30** | C | **45** | D |

---

## 6. Autoevaluación y Metacognición

Reflexiona sobre tu proceso de resolución respondiendo a los siguientes criterios:

```{table} Rúbrica de Logro del Aprendizaje
:widths: 20 40 40

| Criterio de Logro | Nivel Alcanzado (Inicial / Autónomo) | Evidencia de Aprendizaje |
| :--- | :--- | :--- |
| **Construcción de Tablas** | ¿Determino con precisión el rango, número de intervalos (Sturges) y amplitud de clase? | Deduce límites y marcas de clase en problemas de reconstrucción. |
| **Manejo de Frecuencias** | ¿Diferencio claramente entre $f_i, F_i, h_i, H_i$ y aplico sus propiedades algebraicas? | Resuelve sistemas con proporciones acumuladas sin confundir cantidades. |
| **Interpolación Lineal** | ¿Puedo estimar la cantidad de observaciones en subintervalos continuos? | Calcula percentiles o conteos en rangos fraccionarios con precisión. |
| **Pensamiento Crítico** | ¿Interpreto los resultados en contextos reales de Beca 18 y políticas públicas? | Relaciona porcentajes acumulados con toma de decisiones socioeconómicas. |
```

---

## 7. Formulario Resumen

| Concepto / Teorema | Fórmula / Expresión Matemática |
| :--- | :--- |
| **Rango o Recorrido ($R$)** | $R = x_{\max} - x_{\min}$ |
| **Regla de Sturges ($k$)** | $k = 1 + 3.322 \log_{10}(n)$ |
| **Amplitud de Clase ($C$)** | $C = \dfrac{R}{k} = L_s - L_i$ |
| **Marca de Clase ($x_i$)** | $x_i = \dfrac{L_i + L_s}{2}$ |
| **Frecuencia Relativa ($h_i$)** | $h_i = \dfrac{f_i}{n}, \quad \sum h_i = 1$ |
| **Frecuencia Absoluta Acumulada ($F_i$)** | $F_i = F_{i-1} + f_i, \quad F_k = n$ |
| **Frecuencia Relativa Acumulada ($H_i$)** | $H_i = H_{i-1} + h_i, \quad H_k = 1$ |
| **Interpolación en Subintervalo** | $f_{[L_i, x]} = \dfrac{x - L_i}{C} \cdot f_i$ |
