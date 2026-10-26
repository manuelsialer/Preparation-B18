# Tema 03: Gráficos Estadísticos y Tipos de Variables

## 1. Motivación y Contexto Real

En las publicaciones estadísticas del Instituto Nacional de Estadística e Informática (INEI), en los informes de monitoreo ambiental del OEFA y en los reportes de preselección de PRONABEC, la información cuantitativa rara vez se presenta en listas numéricas desnudas. En su lugar, se utilizan **gráficos estadísticos de alta fidelidad** (histogramas, diagramas de barras, sectores circulares y polígonos de frecuencia) que comunican patrones, tendencias y asimetrías de forma inmediata.

No obstante, un error común consiste en utilizar el gráfico equivocado para un tipo de variable específico (por ejemplo, pretender trazar un histograma contiguo para una variable cualitativa nominal, o usar sectores circulares para series temporales). Para rendir con excelencia en Beca 18, el estudiante debe dominar la **taxonomía rigurosa de las variables** y la **construcción e interpretación geométrica y analítica de cada gráfico**.

---

## 2. Fundamento Teórico

### 2.1 Clasificación Rigurosa de Variables
Una variable estadística es una característica observable o medible en los elementos de una población:

1. **Variables Cualitativas (Categóricas):** Expresan atributos, cualidades o categorías no numéricas.
   * **Nominales:** No admiten orden ni jerarquía natural.  
     *Ejemplos:* Género, región de nacimiento (Puno, Cusco, Piura), tipo de sangre, estado civil.
   * **Ordinales:** Admiten un ordenamiento jerárquico o escala de valoración.  
     *Ejemplos:* Nivel educativo (Primaria, Secundaria, Superior), grado militar, nivel de satisfacción (Bajo, Medio, Alto).

2. **Variables Cuantitativas (Numéricas):** Expresan cantidades susceptibles de operaciones aritméticas.
   * **Discretas:** Surgen de procesos de conteo; toman valores aislados en los números enteros ($\mathbb{Z}_{\ge 0}$).  
     *Ejemplos:* Número de hijos por familia, cantidad de postulantes admitidos, número de cursos aprobados.
   * **Continuas:** Surgen de procesos de medición; pueden tomar infinitos valores intermedios en un intervalo real ($\mathbb{R}$).  
     *Ejemplos:* Estatura, peso corporal, tiempo de viaje en horas, ingreso económico mensual.

### 2.2 Tipos de Gráficos Estadísticos y su Correspondencia

| Tipo de Gráfico | Tipo de Variable Recomendada | Características Estructurales |
| :--- | :--- | :--- |
| **Diagrama de Barras** | Cualitativas y Cuantitativas Discretas | Barras separadas de igual ancho. La altura representa $f_i$ o $h_i$. |
| **Diagrama Circular (Torta)** | Cualitativas y Discretas con pocas categorías ($\le 6$) | Círculo subdividido en sectores de ángulo $\theta_i = h_i \times 360^\circ$. |
| **Histograma** | Cuantitativas Continuas (Datos agrupados) | Rectángulos contiguos levantados sobre intervalos de clase $[L_i, L_s\rangle$. |
| **Polígono de Frecuencias** | Cuantitativas Continuas | Línea poligonal que une las marcas de clase $(x_i, f_i)$ en el tope de cada barra. |
| **Ojiva (Polígono Acumulado)** | Cuantitativas Continuas | Gráfico poligonal creciente que une los límites superiores con las frecuencias acumuladas $(L_s, F_i)$ o $(L_s, H_i\%)$. |

```{figure} ../../assets/estadistica/histograma_poligono_frecuencias.svg
---
width: 90%
align: center
alt: Histograma y Polígono de Frecuencias
---
*Figura 1: Histograma y Polígono de Frecuencias para variables continuas. Nótese la continuidad entre rectángulos y la conexión en las marcas de clase.*
```

### 2.3 Relaciones Geométricas en Diagramas Circulares
Dado que la circunferencia completa abarca $360^\circ$ y representa el 100% de la muestra ($n$ elementos), se cumple la proporción estricta:

$$\frac{\theta_i}{360^\circ} = \frac{f_i}{n} = h_i = \frac{h_i\%}{100\%}$$

$$\theta_i = h_i \times 360^\circ = \left( \frac{h_i\%}{100\%} \right) 360^\circ$$

---

## 3. Ejercicios Resueltos Paso a Paso

### Problema 1: Conversión de Porcentaje a Ángulo en Diagrama Circular
En una encuesta sobre la modalidad de postulación a Beca 18, el 35% de los postulantes pertenece a la modalidad Ordinaria, el 25% a Comunidades Nativas (CNA), el 20% a VRAEM y el resto a Huallaga. Determine la medida del ángulo central del sector correspondiente a Huallaga.

**Solución:**

**Paso 1:** Calcular el porcentaje de postulantes de Huallaga:

$$\%_{\text{Huallaga}} = 100\% - (35\% + 25\% + 20\%) = 100\% - 80\% = 20\%$$

**Paso 2:** Convertir el porcentaje $h_4\% = 20\%$ a ángulo central multiplicando por $360^\circ$:

$$\theta_{\text{Huallaga}} = \frac{20}{100} \times 360^\circ = 0.20 \times 360^\circ = 72^\circ$$

El ángulo central correspondiente es $72^\circ$.

---

### Problema 2: Determinación del Tamaño Muestral a partir de un Ángulo
En un gráfico circular sobre la carrera técnica de preferencia, el sector de Agroindustria abarca un ángulo central de $54^\circ$. Si dicho sector representa a 45 estudiantes, ¿cuál fue el número total de estudiantes encuestados?

**Solución:**

**Paso 1:** Calcular la frecuencia relativa $h$ a partir del ángulo central:

$$h = \frac{\theta}{360^\circ} = \frac{54^\circ}{360^\circ} = \frac{3}{20} = 0.15$$

**Paso 2:** Aplicar la relación $h = \frac{f}{n}$:

$$0.15 = \frac{45}{n} \implies n = \frac{45}{0.15} = \frac{4500}{15} = 300$$

Fueron encuestados 300 estudiantes en total.

---

### Problema 3: Clasificación de Variables
Clasifique rigurosamente cada una de las siguientes cuatro variables:
I. Nivel socioeconómico (Pobre extremo, Pobre no extremo, No pobre).
II. Tiempo empleado en completar la prueba de preselección en minutos.
III. Número de hermanos en edad escolar.
IV. Distrito de residencia habitual.

**Solución:**

**Paso 1:** Variable I: Expresa cualidad con jerarquía de pobreza $\implies$ **Cualitativa ordinal**.

**Paso 2:** Variable II: Expresa medición continua de tiempo $\implies$ **Cuantitativa continua**.

**Paso 3:** Variable III: Expresa conteo de individuos enteros $\implies$ **Cuantitativa discreta**.

**Paso 4:** Variable IV: Expresa categorías geográficas sin jerarquía $\implies$ **Cualitativa nominal**.

---

### Problema 4: Lectura de Histograma de Salarios
Un histograma presenta cuatro rectángulos de igual base $C = 500$:
* $[1000, 1500\rangle$ con altura 20.
* $[1500, 2000\rangle$ con altura 50.
* $[2000, 2500\rangle$ con altura 80.
* $[2500, 3000\rangle$ con altura 30.
¿Cuántos trabajadores ganan S/ 1800 o más?

**Solución:**

**Paso 1:** En $[1500, 2000\rangle$, el subintervalo de 1800 a 2000 mide $2000 - 1800 = 200$. Como el ancho total es 500:

$$f_{[1800, 2000\rangle} = \frac{200}{500} \times 50 = \frac{2}{5} \times 50 = 20$$

**Paso 2:** Los intervalos $[2000, 2500\rangle$ y $[2500, 3000\rangle$ están íntegramente por encima de 1800:

$$f_{[2000, 3000]} = 80 + 30 = 110$$

**Paso 3:** Sumar todas las frecuencias:

$$\text{Total} = 20 + 110 = 130 \text{ trabajadores}$$

---

### Problema 5: Área Bajo el Histograma
Demuestre que el área total encerrada por las barras de un histograma cuya altura es la frecuencia relativa dividida entre la amplitud (densidad de frecuencia $d_i = \frac{h_i}{C}$) es idénticamente igual a 1.

**Solución:**

**Paso 1:** El área de un rectángulo individual de base $C_i$ y altura $d_i$ es:

$$\text{Área}_i = \text{base} \times \text{altura} = C_i \times \left( \frac{h_i}{C_i} \right) = h_i$$

**Paso 2:** El área total es la suma de las áreas de todos los rectángulos:

$$\text{Área Total} = \sum_{i=1}^{k} \text{Área}_i = \sum_{i=1}^{k} h_i$$

**Paso 3:** Por axioma de frecuencias relativas, la suma de todas las $h_i$ es 1:

$$\sum_{i=1}^{k} h_i = 1$$

Por lo tanto, el área total de la curva de densidad es 1.

---

### Problema 6: Reconstrucción de un Gráfico de Barras
En un gráfico de barras sobre consumo de agua, la barra de "Ahorro" es $2.5$ veces la altura de la barra de "Desperdicio". Si entre ambas categorías suman 140 familias, determine cuántas familias pertenecen a "Ahorro".

**Solución:**

**Paso 1:** Sean $x$ las familias de Desperdicio y $2.5x$ las de Ahorro:

$$x + 2.5x = 140 \implies 3.5x = 140$$

**Paso 2:** Despejar $x$:

$$x = \frac{140}{3.5} = 40$$

**Paso 3:** Calcular las familias de Ahorro:

$$2.5 \times 40 = 100 \text{ familias}$$

---

### Problema 7: Estimación de la Mediana en una Ojiva
En una ojiva porcentual acumulada que va desde 0 hasta 100 puntos, la recta une los puntos $(40, 25\%)$ y $(60, 65\%)$. Estime el valor de la mediana.

**Solución:**

**Paso 1:** La mediana se ubica exactamente en el percentil 50 ($H\% = 50\%$).

**Paso 2:** Notar que 50% se encuentra entre 25% y 65%. Aplicar interpolación lineal:

$$\frac{Me - 40}{60 - 40} = \frac{50\% - 25\%}{65\% - 25\%}$$

**Paso 3:** Resolver la proporción:

$$\frac{Me - 40}{20} = \frac{25}{40} = \frac{5}{8}$$

$$Me - 40 = 20 \times \frac{5}{8} = \frac{100}{8} = 12.5 \implies Me = 40 + 12.5 = 52.5 \text{ puntos}$$

---

### Problema 8: Comparación de Dos Sectores Circulares
En un diagrama circular de 500 personas, el sector A tiene un ángulo central de $108^\circ$ y el sector B tiene un ángulo de $72^\circ$. ¿En cuánto excede el número de personas del sector A al sector B?

**Solución:**

**Paso 1:** Calcular la diferencia angular entre ambos sectores:

$$\Delta\theta = 108^\circ - 72^\circ = 36^\circ$$

**Paso 2:** Calcular a qué fracción de la muestra corresponde $36^\circ$:

$$\frac{36^\circ}{360^\circ} = \frac{1}{10} = 0.10 = 10\%$$

**Paso 3:** Multiplicar por el total de personas $n = 500$:

$$\text{Exceso} = 10\% \times 500 = 50 \text{ personas}$$

---

### Problema 9: Error Común en Gráficos de Sectores
Un estudiante presenta un diagrama circular con porcentajes: Categoría A: 40%, Categoría B: 35%, Categoría C: 15%, Categoría D: 20%. ¿Por qué este gráfico es estadísticamente inválido?

**Solución:**

**Paso 1:** Sumar los porcentajes reportados:

$$40\% + 35\% + 15\% + 20\% = 110\%$$

**Paso 2:** En un diagrama circular de partición de una población, la suma de las partes debe ser estrictamente el 100% (o $360^\circ$). Un total de 110% indica categorías solapadas o error de tabulación que invalida el uso del diagrama de sectores.

---

### Problema 10: Polígono de Frecuencias y Área
Si el área bajo un histograma convencional de frecuencias absolutas es igual al producto de la amplitud común por el número total de observaciones ($A = C \cdot n$), determine el área si $C = 5$ y $n = 80$.

**Solución:**

**Paso 1:** Cada rectángulo tiene área $C \cdot f_i$.

**Paso 2:** La suma de todas las áreas es:

$$\sum C \cdot f_i = C \sum f_i = C \cdot n$$

**Paso 3:** Reemplazar valores:

$$\text{Área} = 5 \times 80 = 400 \text{ unidades cuadradas}$$

---

## 4. Práctica Propuesta

### Nivel 1: Conceptos y Clasificación Básica (Ejercicios 1 al 15)

1. El número de hermanos de un estudiante es una variable:  
A) Cualitativa nominal  
B) Cualitativa ordinal  
C) Cuantitativa discreta  
D) Cuantitativa continua  
E) Numérica infinita

2. La temperatura corporal medida con termómetro digital es una variable:  
A) Cuantitativa continua  
B) Cuantitativa discreta  
C) Cualitativa nominal  
D) Cualitativa ordinal  
E) Ficticia

3. En un diagrama circular, un sector que representa el 25% de los datos tiene un ángulo central de:  
A) $45^\circ$  
B) $60^\circ$  
C) $75^\circ$  
D) $90^\circ$  
E) $120^\circ$

4. ¿Cuál de los siguientes gráficos es el más adecuado para representar la evolución temporal del precio del dólar?  
A) Diagrama circular  
B) Gráfico de líneas o serie temporal  
C) Histograma  
D) Gráfico de tallo y hojas  
E) Diagrama de dispersión

5. En un gráfico de barras, la separación entre barras indica que:  
A) Los datos son erróneos  
B) Las variables no son continuas o son categorías cualitativas  
C) El gráfico está incompleto  
D) La suma es menor a 100  
E) Hay valores negativos

6. Un ángulo central de $180^\circ$ en un gráfico circular representa al:  
A) 25%  
B) 33.3%  
C) 50%  
D) 75%  
E) 100%

7. La variable "Grado de satisfacción con la atención médica" es:  
A) Cualitativa nominal  
B) Cualitativa ordinal  
C) Cuantitativa discreta  
D) Cuantitativa continua  
E) Dependiente

8. El gráfico de rectángulos unidos levantados sobre intervalos continuos se denomina:  
A) Ojiva  
B) Pictograma  
C) Histograma  
D) Gráfico de torta  
E) Cartograma

9. En un diagrama circular, si un sector tiene un ángulo de $36^\circ$, su frecuencia relativa es:  
A) 0.05  
B) 0.10  
C) 0.15  
D) 0.20  
E) 0.25

10. Un polígono de frecuencias se obtiene al unir:  
A) Los puntos medios superiores de las barras de un histograma  
B) Los orígenes de cada intervalo  
C) Los extremos finales del gráfico circular  
D) Las frecuencias acumuladas únicamente  
E) El eje vertical con el horizontal

11. La variable "Distrito de procedencia" es:  
A) Cualitativa nominal  
B) Cualitativa ordinal  
C) Cuantitativa continua  
D) Cuantitativa discreta  
E) Aleatoria uniforme

12. Si una muestra tiene 60 personas y un sector circular abarca $120^\circ$, ¿cuántas personas representa?  
A) 15  
B) 20  
C) 25  
D) 30  
E) 40

13. La ojiva es una representación gráfica de:  
A) Las frecuencias relativas simples  
B) Las frecuencias acumuladas ($F_i$ o $H_i$)  
C) La varianza  
D) La moda únicamente  
E) Los valores atípicos

14. Un gráfico donde se utilizan dibujos o figuras alusivas para representar cantidades se denomina:  
A) Histograma  
B) Diagrama de dispersión  
C) Pictograma  
D) Boxplot  
E) Pirámide poblacional

15. El ángulo correspondiente al 1% en un diagrama de sectores es:  
A) $1^\circ$  
B) $1.8^\circ$  
C) $3.6^\circ$  
D) $7.2^\circ$  
E) $0.36^\circ$

---

### Nivel 2: Interpretación y Geometría Estadística (Ejercicios 16 al 30)

16. En un diagrama circular de 180 postulantes, los ángulos de tres carreras son $120^\circ$, $160^\circ$ y $\alpha$. Calcule el número de postulantes de la tercera carrera.  
A) 30  
B) 35  
C) 40  
D) 45  
E) 50

17. En un histograma con tres intervalos $[10, 20\rangle, [20, 30\rangle, [30, 40\rangle$, las alturas son 15, 25 y 20 respectivamente. ¿Qué porcentaje de las observaciones es mayor o igual a 20?  
A) 60%  
B) 65%  
C) 70%  
D) 75%  
E) 80%

18. Si en un gráfico circular el sector A mide $144^\circ$, el sector B mide $108^\circ$ y el sector C el resto, ¿cuál es el porcentaje del sector C?  
A) 25%  
B) 30%  
C) 35%  
D) 40%  
E) 45%

19. El polígono de frecuencias corta al eje horizontal en:  
A) Los límites exactos del primer y último intervalo  
B) Las marcas de clase de intervalos ficticios adyacentes de frecuencia cero  
C) El origen $(0,0)$  
D) La mediana  
E) El valor de la moda

20. Si se encuestó a 400 personas y el ángulo del sector "Prefiere estudiar de noche" es $54^\circ$, ¿cuántas personas prefieren esa opción?  
A) 45  
B) 50  
C) 54  
D) 60  
E) 75

21. En un diagrama de barras de frecuencias relativas, la suma de las alturas de todas las barras es:  
A) 100  
B) $360$  
C) 1  
D) $n$  
E) Variable según la escala

22. Si en un histograma el rectángulo del intervalo $[40, 60\rangle$ tiene una altura de 24 observaciones, asumiendo distribución uniforme, ¿cuántas observaciones caen en $[45, 55\rangle$?  
A) 10  
B) 12  
C) 14  
D) 16  
E) 18

23. Un gráfico de sectores muestra cuatro categorías proporcionales a 2, 3, 5 y 8. El ángulo del sector mayor es:  
A) $140^\circ$  
B) $150^\circ$  
C) $160^\circ$  
D) $170^\circ$  
E) $180^\circ$

24. En el problema anterior, ¿cuántos grados mide el sector menor?  
A) $30^\circ$  
B) $35^\circ$  
C) $40^\circ$  
D) $45^\circ$  
E) $50^\circ$

25. Un diagrama de dispersión es especialmente útil para:  
A) Analizar la distribución de una variable cualitativa  
B) Evaluar la relación o correlación entre dos variables cuantitativas  
C) Calcular frecuencias acumuladas  
D) Comparar partes de un todo  
E) Definir el tamaño muestral

26. La ojiva siempre tiene una trayectoria:  
A) Oscilante  
B) Estrictamente decreciente  
C) No decreciente (monótona creciente)  
D) Constante  
E) Parabólica

27. Si un sector circular abarca $126^\circ$, el porcentaje de la población correspondiente es:  
A) 32%  
B) 35%  
C) 36%  
D) 38%  
E) 40%

28. En un histograma con amplitud común 4, las marcas de clase son 12, 16, 20. El límite superior del tercer intervalo es:  
A) 20  
B) 21  
C) 22  
D) 24  
E) 26

29. Si las barras de un histograma tienen áreas 20, 50, 80 y 50, y el total de datos es $n = 200$, la amplitud común $C$ de los intervalos es:  
A) 1  
B) 2  
C) 4  
D) 5  
E) 10

30. Si el 70% de postulantes aprobó un simulacro, el ángulo central del sector de los que NO aprobaron es:  
A) $72^\circ$  
B) $84^\circ$  
C) $96^\circ$  
D) $108^\circ$  
E) $120^\circ$

---

### Nivel 3: Problemas Avanzados Tipo Beca 18 (Ejercicios 31 al 45)

31. El siguiente gráfico de sectores muestra la distribución de postulantes por departamento: Lima ($144^\circ$), Junín ($90^\circ$), Cusco ($72^\circ$) y Ayacucho el resto. Si Ayacucho tiene 150 postulantes, ¿cuántos postulantes tiene Junín?  
A) 200  
B) 225  
C) 250  
D) 275  
E) 300

32. A partir de un polígono de frecuencias con vértices $(25, 20), (35, 45), (45, 60), (55, 35), (65, 15)$, determine qué porcentaje de las observaciones se ubica en el intervalo cuya marca de clase es 45.  
A) 30%  
B) 32.5%  
C) 34.3%  
D) 35.0%  
E) 37.5%

33. En un estudio sobre rendimiento académico, una ojiva de frecuencias relativas acumuladas pasa por los puntos $(12, 0.30)$ y $(16, 0.70)$. Mediante interpolación lineal, determine el puntaje correspondiente al percentil 60 ($H = 0.60$).  
A) 14.5  
B) 14.8  
C) 15.0  
D) 15.2  
E) 15.5

34. En una prueba con 300 alumnos, el histograma muestra 4 intervalos de amplitudes iguales: $[0, 5\rangle$ (30), $[5, 10\rangle$ (90), $[10, 15\rangle$ (120), $[15, 20\rangle$ (60). Si la nota mínima aprobatoria es 11, ¿cuántos alumnos aprobaron?  
A) 144  
B) 156  
C) 160  
D) 168  
E) 172

35. Un diagrama circular representa los gastos de una cooperativa comunal. Si el sector de "Semillas" tiene un ángulo $\alpha$, "Fertilizantes" tiene $2\alpha$, "Riego" tiene $3\alpha$ y "Transporte" tiene $90^\circ$, determine el valor del ángulo de "Riego".  
A) $108^\circ$  
B) $120^\circ$  
C) $135^\circ$  
D) $144^\circ$  
E) $150^\circ$

36. En el problema anterior, si el presupuesto total es de S/ 48 000, ¿cuánto se destina al rubro de "Fertilizantes"?  
A) S/ 9 600  
B) S/ 10 800  
C) S/ 12 000  
D) S/ 14 400  
E) S/ 16 000

37. Al analizar un gráfico de caja y bigotes (boxplot), la línea intermedia dentro de la caja representa exactamente:  
A) La media aritmética  
B) La mediana  
C) El percentil 75  
D) La moda  
E) El rango intercuartílico

38. En un boxplot, la longitud de la caja central (distancia entre el primer y tercer cuartil) se define como:  
A) Desviación estándar  
B) Varianza muestral  
C) Rango intercuartílico ($RIC = Q_3 - Q_1$)  
D) Rango medio  
E) Coeficiente de variación

39. En un histograma con intervalos de amplitudes desiguales $C_1 = 5, C_2 = 10, C_3 = 20$ y frecuencias $f_1 = 20, f_2 = 60, f_3 = 80$, para que las áreas representen fielmente a las frecuencias, las alturas deben ser proporcionales a las densidades $f_i / C_i$. El orden de alturas de menor a mayor es:  
A) $h_1 < h_2 < h_3$  
B) $h_1 = h_3 < h_2$  
C) $h_3 < h_1 < h_2$  
D) $h_2 < h_1 = h_3$  
E) Todas iguales

40. Si la ojiva de frecuencias absolutas acumuladas de 200 estudiantes corta la línea de $F = 100$ en la abscisa 64, se deduce con certeza que:  
A) La media de los estudiantes es 64  
B) La mediana de los estudiantes es 64  
C) La moda es 64  
D) Todos sacaron menos de 64  
E) La desviación estándar es cero

41. En un gráfico de barras, si se reduce la escala del eje vertical a la mitad pero los datos se mantienen, las alturas visuales de las barras:  
A) Se duplican  
B) Se reducen a la mitad  
C) No cambian  
D) Se cuadruplican  
E) Se distorsionan de forma no lineal

42. En una encuesta a 600 pobladores amazónicos, el sector de "Lengua materna originaria" abarca $216^\circ$. ¿Cuántos pobladores tienen dicha condición?  
A) 320  
B) 340  
C) 360  
D) 380  
E) 400

43. Una distribución de tiempos de espera en ventanilla presenta un histograma con fuerte sesgo a la derecha. ¿Cuál de los siguientes gráficos de resumen complementa mejor este tipo de datos?  
A) Solo la media aritmética  
B) Diagrama de caja (Boxplot) con mediana y cuartiles  
C) Gráfico circular únicamente  
D) Pictograma simple  
E) Gráfico de dispersión bidimensional

44. Si en un diagrama circular con 5 categorías los ángulos forman una progresión aritmética cuya suma es $360^\circ$, el ángulo del término central necesariamente es:  
A) $60^\circ$  
B) $68^\circ$  
C) $72^\circ$  
D) $75^\circ$  
E) $80^\circ$

45. En una muestra de 120 postulantes, se representan los puntajes con un histograma donde $x_1 = 20, x_2 = 40, x_3 = 60, x_4 = 80$. Si el polígono de frecuencias encierra un área total de 2400 unidades cuadradas con el eje horizontal, la escala del eje de frecuencias es consistente con una amplitud común $C$ igual a:  
A) 10  
B) 15  
C) 20  
D) 25  
E) 30

---

## 5. Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | C | **31** | C |
| **2** | A | **17** | D | **32** | C |
| **3** | D | **18** | B | **33** | C |
| **4** | B | **19** | B | **34** | B |
| **5** | B | **20** | D | **35** | C |
| **6** | C | **21** | C | **36** | C |
| **7** | B | **22** | B | **37** | B |
| **8** | C | **23** | C | **38** | C |
| **9** | B | **24** | C | **39** | B |
| **10** | A | **25** | B | **40** | B |
| **11** | A | **26** | C | **41** | B |
| **12** | B | **27** | B | **42** | C |
| **13** | B | **28** | C | **43** | B |
| **14** | C | **29** | A | **44** | C |
| **15** | C | **30** | D | **45** | C |

---

## 6. Autoevaluación y Metacognición

Reflexiona sobre tu proceso de resolución respondiendo a los siguientes criterios:

```{table} Rúbrica de Logro del Aprendizaje
:widths: 20 40 40

| Criterio de Logro | Nivel Alcanzado (Inicial / Autónomo) | Evidencia de Aprendizaje |
| :--- | :--- | :--- |
| **Taxonomía de Variables** | ¿Diferencio con precisión entre variables cualitativas (nominal/ordinal) y cuantitativas (discreta/continua)? | Clasifica variables complejas en contextos socioeconómicos y científicos. |
| **Diagramas Circulares** | ¿Convierto ágilmente entre frecuencias absolutas, porcentajes y ángulos centrales ($\theta = 3.6 \times h\%$)? | Resuelve incógnitas angulares y proporciones en gráficos de sectores. |
| **Histogramas y Polígonos** | ¿Interpreto áreas, alturas y densidades de frecuencia en datos continuos sin confundir barras contiguas con separadas? | Estima proporciones acumuladas y percentiles en histogramas y polígonos. |
| **Lectura de Ojivas** | ¿Determino visual y algebraicamente la mediana y percentiles a partir del cruce con la curva acumulada? | Aplica interpolaciones lineales rigurosas en ojivas de frecuencias. |
```

---

## 7. Formulario Resumen

| Concepto / Teorema | Fórmula / Expresión Matemática |
| :--- | :--- |
| **Ángulo Central en Sector Circular ($\theta_i$)** | $\theta_i = h_i \times 360^\circ = \left( \dfrac{h_i\%}{100\%} \right) 360^\circ$ |
| **Conversión de Frecuencia a Grados** | $\theta_i = \dfrac{f_i}{n} \cdot 360^\circ$ |
| **Área Total de Histograma de Densidad** | $\text{Área} = \sum C_i \left( \dfrac{h_i}{C_i} \right) = \sum h_i = 1$ |
| **Densidad de Frecuencia ($d_i$)** | $d_i = \dfrac{f_i}{C_i}$ |
| **Rango Intercuartílico ($RIC$)** | $RIC = Q_3 - Q_1$ |
| **Condición de Partición Circular** | $\sum \theta_i = 360^\circ, \quad \sum h_i\% = 100\%$ |
| **Posición de la Mediana en Ojiva** | Abscisa $x$ tal que $F(x) = \dfrac{n}{2}$ o $H(x) = 50\%$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. La tabla de claves es correcta en su totalidad: todos los ejercicios tienen solución y su respuesta figura entre las opciones A–E, por lo que no se modificó ninguna clave.
