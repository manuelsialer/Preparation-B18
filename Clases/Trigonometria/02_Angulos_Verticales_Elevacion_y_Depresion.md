# Tema 02: Ángulos Verticales: Elevación y Depresión

## 1. Motivación y Contexto Real

Los problemas de ángulos verticales constituyen el núcleo de las preguntas de modelamiento trigonométrico contextualizado en el **Examen Nacional de Preselección (ENP) Beca 18**. Ningún topógrafo escala una montaña para medir su altitud, ningún piloto desciende con una cinta métrica hacia la pista y ningún navegante salta al mar para medir la distancia a un acantilado: todos utilizan teodolitos, clinómetros y sextantes que miden ángulos respecto a la línea horizontal.

En la realidad geográfica y productiva del Perú:
1. **Topografía de Acantilados y Laderas:** En la Costa Verde de Lima o en las quebradas de la sierra central, calcular el ángulo de depresión desde lo alto de un barranco permite delimitar zonas de seguridad contra derrumbes y diseñar muros de contención en la base.
2. **Navegación Marítima y Faros Costeros:** Los capitanes de embarcaciones pesqueras en Chimbote, Paita o Ilo divisan la luz de un faro bajo un ángulo de elevación para calcular instantáneamente a cuántas millas náuticas se encuentran de los arrecifes costeros.
3. **Ingeniería Forestal y Telecomunicaciones:** Medir la altura de árboles centenarios en la Amazonía o determinar la altura necesaria de una torre de telefonía rural sobre un cerro para librar la línea de vista forestal.

```{figure} ../../assets/trigonometria/angulos_verticales.svg
---
width: 95%
align: center
alt: Ángulos Verticales - Elevación y Depresión
---
*Diagrama vectorial generado en TikZ que define con precisión geométrica la línea horizontal del observador, el ángulo de elevación $\alpha$ (hacia arriba) y el ángulo de depresión $\beta$ (hacia abajo).*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Elementos del Sistema de Observación Vertical

En todo problema de ángulos verticales intervienen tres elementos geométricos situados en un mismo plano vertical:

1. **Punto de Observación ($O$):** Posición del ojo del observador o del instrumento de medición (teodolito, estación total).
2. **Línea Horizontal ($\mathcal{L}_H$):** Recta imaginaria que pasa por el punto de observación y es estrictamente paralela al nivel del suelo horizontal o al nivel del mar.
3. **Línea Visual ($\mathcal{L}_V$):** Recta imaginaria trazada desde el ojo del observador hacia el punto específico del objeto que se está observando.
4. **Plano Vertical:** Plano imaginario perpendicular al suelo horizontal que contiene simultáneamente a la línea visual y a la línea horizontal.

---

### 2.2 Clasificación de los Ángulos Verticales

#### 1. Ángulo de Elevación ($\alpha$)
Es el ángulo vertical formado entre la **línea horizontal** y la **línea visual**, cuando el objeto observado se encuentra **por encima** del nivel del observador:

$$\text{Línea Visual está sobre la Línea Horizontal} \implies \text{Ángulo de Elevación } \alpha$$

#### 2. Ángulo de Depresión ($\beta$)
Es el ángulo vertical formado entre la **línea horizontal** y la **línea visual**, cuando el objeto observado se encuentra **por debajo** del nivel del observador:

$$\text{Línea Visual está debajo de la Línea Horizontal} \implies \text{Ángulo de Depresión } \beta$$

#### 3. Ángulo de Observación o de Visibilidad ($\theta$)
Es el ángulo comprendido entre **dos líneas visuales** dirigidas hacia los dos extremos (superior e inferior) de un mismo objeto:

$$\theta = \alpha + \beta \quad (\text{si el objeto cruza la horizontal}) \quad\text{ó}\quad \theta = \alpha_2 - \alpha_1$$

---

### 2.3 Teorema de Reciprocidad Angular (Alternos Internos)

Dado que todas las líneas horizontales son paralelas entre sí, por el teorema de ángulos alternos internos entre paralelas:
> **Principio de Reciprocidad:** El ángulo de depresión con que un observador $A$ divisa un punto $B$ en el suelo es **exactamente igual** al ángulo de elevación con que un observador situado en $B$ divisa al observador $A$:
> $\beta_{\text{depresión}}(A \to B) = \alpha_{\text{elevación}}(B \to A)$
---

### 2.4 Dos Casos Clásicos de Planteo en Exámenes

#### Caso A: Consideración de la Estatura del Observador
* **Estatura Despreciable:** Si el problema no menciona la altura del observador, se considera un punto en el suelo ($h_{\text{obs}} = 0$).
* **Estatura Explícita ($h$):** Si el problema indica que la persona mide $h$ metros (ejemplo: $1.70\text{ m}$), la altura total del edificio o torre será:

$$H_{\text{total}} = y + h = d\tan(\alpha) + h$$

  *(donde $y$ es el cateto opuesto del triángulo rectángulo y $d$ es la distancia horizontal).*

#### Caso B: Desplazamiento del Observador (Acercamiento o Alejamiento)
Un observador divisa la cúspide de una torre de altura $H$ con un ángulo de elevación $\alpha$. Si camina una distancia $d$ hacia la torre, el nuevo ángulo de elevación es $\beta$ ($\beta > \alpha$).
* En el primer triángulo: $d + x = H \cot(\alpha)$
* En el segundo triángulo: $x = H \cot(\beta)$
* Restando ambas ecuaciones:

$$d = H(\cot\alpha - \cot\beta) \implies H = \frac{d}{\cot\alpha - \cot\beta}$$

---

### 2.5 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Medir el ángulo de depresión respecto a la vertical:** El error más común es medir el ángulo de depresión respecto a la pared o acantilado vertical. **El ángulo de depresión se mide SIEMPRE respecto a la línea horizontal imaginaria.**
> 2. **Olvidar sumar la estatura del observador:** Si el enunciado dice *"un estudiante de $1.60\text{ m}$ de estatura..."*, la respuesta final debe sumar $1.60\text{ m}$ al cateto calculado.
> 3. **Confundir acercarse con alejarse:** Al acercarse al objeto observado, el ángulo de elevación **aumenta** ($\beta > \alpha$). Al alejarse, el ángulo **disminuye**.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Conceptos)

#### Ejercicio 1
Desde un punto en el suelo ubicado a $40\text{ m}$ de la base de un edificio, se observa su parte más alta con un ángulo de elevación de $37^\circ$. Calcule la altura del edificio.

**Análisis Conceptual:**
La distancia horizontal es el cateto adyacente ($40\text{ m}$) y la altura es el cateto opuesto ($H$). Usamos la razón tangente del triángulo notable de $37^\circ$ ($\tan 37^\circ \approx \frac{3}{4}$).

**Solución Paso a Paso:**

**Paso 1:** Plantear la razón trigonométrica tangente:

$$\tan(37^\circ) = \frac{\text{Altura } H}{\text{Distancia horizontal } d}$$

**Paso 2:** Reemplazar los valores conocidos:

$$\frac{3}{4} = \frac{H}{40}$$

**Paso 3:** Despejar la altura $H$:

$$H = \frac{3 \cdot 40}{4} = 3 \cdot 10 = 30\text{ m}$$

**Conclusión:**
La altura del edificio es de $30\text{ m}$.

---

#### Ejercicio 2
Desde la azotea de un faro costero de $48\text{ m}$ de altura sobre el nivel del mar, se divisa una lancha con un ángulo de depresión de $53^\circ$. ¿A qué distancia de la base del faro se encuentra la lancha?

**Análisis Conceptual:**
Por el principio de alternos internos, el ángulo de elevación desde la lancha hacia el faro es también de $53^\circ$. La altura del faro es el cateto opuesto ($48\text{ m}$) y la distancia horizontal en el mar es el cateto adyacente ($d$). Usamos $\tan 53^\circ \approx \frac{4}{3}$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la relación con la tangente:

$$\tan(53^\circ) = \frac{\text{Altura del faro}}{\text{Distancia } d}$$

**Paso 2:** Sustituir los valores:

$$\frac{4}{3} = \frac{48}{d}$$

**Paso 3:** Despejar la distancia $d$:

$$4d = 48 \cdot 3 = 144 \implies d = \frac{144}{4} = 36\text{ m}$$

**Conclusión:**
La lancha se encuentra a $36\text{ m}$ de la base del faro.

---

#### Ejercicio 3
Una persona de $1.70\text{ m}$ de estatura observa la cúspide de un poste de alumbrado con un ángulo de elevación de $45^\circ$. Si la persona está a $8.30\text{ m}$ del poste, calcule la altura total del poste.

**Análisis Conceptual:**
En el triángulo rectángulo formado sobre la línea horizontal del ojo, como el ángulo es $45^\circ$, el cateto opuesto vertical es igual al cateto adyacente horizontal ($y = 8.30\text{ m}$). La altura total es $H = y + h_{\text{obs}}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la altura del triángulo por encima de los ojos:

$$y = d \cdot \tan(45^\circ) = 8.30 \cdot 1 = 8.30\text{ m}$$

**Paso 2:** Sumar la estatura del observador:

$$H_{\text{total}} = y + h_{\text{obs}} = 8.30 + 1.70 = 10.00\text{ m}$$

**Conclusión:**
La altura total del poste de alumbrado es de $10\text{ m}$.

---

### Nivel 2: Intermedio (Cambio de Posición y Antenas)

#### Ejercicio 4
Una persona observa la parte superior de una torre con un ángulo de elevación de $30^\circ$. Si camina $40\text{ m}$ en línea recta hacia la torre, el nuevo ángulo de elevación es de $60^\circ$. Calcule la altura de la torre.

**Análisis Conceptual:**
Aplicamos la fórmula de cambio de posición con los ángulos notables $30^\circ$ y $60^\circ$: $H = \frac{d}{\cot\alpha - \cot\beta}$.

**Solución Paso a Paso:**

**Paso 1:** Identificar los valores trigonométricos:

$$\cot(30^\circ) = \sqrt{3},\quad \cot(60^\circ) = \frac{\sqrt{3}}{3}$$

**Paso 2:** Plantear la ecuación con el desplazamiento $d = 40\text{ m}$:

$$H(\cot 30^\circ - \cot 60^\circ) = 40$$

$$H\left(\sqrt{3} - \frac{\sqrt{3}}{3}\right) = 40$$

**Paso 3:** Simplificar la resta de fracciones:

$$H\left(\frac{2\sqrt{3}}{3}\right) = 40$$

**Paso 4:** Despejar la altura $H$:

$$H = \frac{40 \cdot 3}{2\sqrt{3}} = \frac{60}{\sqrt{3}} = \frac{60\sqrt{3}}{3} = 20\sqrt{3}\text{ m} \approx 34.64\text{ m}$$

**Conclusión:**
La altura de la torre es de $20\sqrt{3}\text{ m}$ (aproximadamente $34.64\text{ m}$).

---

#### Ejercicio 5
Sobre el techo de un edificio de $24\text{ m}$ de altura se encuentra instalada una antena de radio. Desde un punto en el suelo, se observa la base de la antena con un ángulo de elevación de $37^\circ$ y la parte superior de la antena con un ángulo de elevación de $45^\circ$. Calcule la longitud de la antena.

**Análisis Conceptual:**
Desde el mismo punto en el suelo a distancia $d$:
1. Para la base de la antena (techo del edificio): $\tan 37^\circ = \frac{24}{d}$.
2. Para la cúspide de la antena: $\tan 45^\circ = \frac{24 + L}{d} = 1 \implies d = 24 + L$.

**Solución Paso a Paso:**

**Paso 1:** Hallar la distancia horizontal $d$ usando la base de la antena:

$$\tan(37^\circ) = \frac{24}{d} \implies \frac{3}{4} = \frac{24}{d}$$

$$3d = 24 \cdot 4 = 96 \implies d = \frac{96}{3} = 32\text{ m}$$

**Paso 2:** Plantear la ecuación para la cúspide de la antena con el ángulo de $45^\circ$:

$$\tan(45^\circ) = \frac{24 + L}{d} \implies 1 = \frac{24 + L}{32}$$

**Paso 3:** Despejar la longitud de la antena $L$:

$$24 + L = 32 \implies L = 32 - 24 = 8\text{ m}$$

**Conclusión:**
La longitud de la antena de radio es de $8\text{ m}$.

---

#### Ejercicio 6
Desde lo alto de una colina de $120\text{ m}$ de altura, se observan dos automóviles estacionados en la misma dirección con ángulos de depresión de $37^\circ$ y $53^\circ$. Calcule la distancia que separa a ambos automóviles.

**Análisis Conceptual:**
Ambos autos están en una línea recta horizontal. Las distancias horizontales desde el pie de la colina son $d_1 = H \cot(37^\circ)$ (el más lejano) y $d_2 = H \cot(53^\circ)$ (el más cercano). La distancia entre ellos es $\Delta d = d_1 - d_2$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la distancia al auto más lejano ($37^\circ$):

$$d_1 = 120 \cdot \cot(37^\circ) = 120 \cdot \frac{4}{3} = 40 \cdot 4 = 160\text{ m}$$

**Paso 2:** Calcular la distancia al auto más cercano ($53^\circ$):

$$d_2 = 120 \cdot \cot(53^\circ) = 120 \cdot \frac{3}{4} = 30 \cdot 3 = 90\text{ m}$$

**Paso 3:** Calcular la separación entre los automóviles:

$$\Delta d = d_1 - d_2 = 160 - 90 = 70\text{ m}$$

**Conclusión:**
La distancia que separa a los dos automóviles es de $70\text{ m}$.

---

#### Ejercicio 7
Un observador situado en un punto $A$ divisa la cúspide de un monumento con un ángulo de elevación $\alpha$ tal que $\tan\alpha = \frac{1}{3}$. Si avanza $20\text{ m}$ hacia el monumento, el nuevo ángulo de elevación es $\beta$ tal que $\tan\beta = \frac{1}{2}$. Calcule la altura del monumento.

**Análisis Conceptual:**
Sea $H$ la altura del monumento. Las cotangentes son $\cot\alpha = 3$ y $\cot\beta = 2$. Usamos la relación $d = H(\cot\alpha - \cot\beta)$.

**Solución Paso a Paso:**

**Paso 1:** Identificar las cotangentes de los ángulos:

$$\cot\alpha = \frac{1}{\tan\alpha} = 3$$

$$\cot\beta = \frac{1}{\tan\beta} = 2$$

**Paso 2:** Aplicar la ecuación del desplazamiento:

$$d = H(\cot\alpha - \cot\beta)$$

$$20 = H(3 - 2)$$

**Paso 3:** Despejar la altura $H$:

$$20 = H(1) \implies H = 20\text{ m}$$

**Conclusión:**
La altura del monumento es de $20\text{ m}$.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Rescate de Guardacostas frente a los Acantilados de Paracas)
Desde un puesto de vigía de la Marina de Guerra en lo alto de un acantilado en Paracas a $84\text{ m}$ sobre el nivel del mar, un oficial divisa dos embarcaciones pesqueras artesanales que solicitan auxilio mecánico. Ambas lanchas se encuentran alineadas directamente hacia el oeste del vigía. La primera lancha se observa con un ángulo de depresión de $16^\circ$ ($\tan 16^\circ \approx \frac{7}{24}$) y la segunda lancha con un ángulo de depresión de $37^\circ$ ($\tan 37^\circ \approx \frac{3}{4}$). Una patrullera rápida debe navegar entre ambas lanchas para asistirlas; determine la distancia en línea recta en el mar que separa a ambas embarcaciones.

**Análisis Conceptual:**
La altura del acantilado es $H = 84\text{ m}$. Las distancias horizontales en el mar son $d_1 = H \cot(16^\circ)$ y $d_2 = H \cot(37^\circ)$. La distancia entre las lanchas es la diferencia $d_1 - d_2$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la distancia a la lancha más alejada ($16^\circ$):

$$d_1 = 84 \cdot \cot(16^\circ) = 84 \cdot \frac{24}{7}$$

Simplificando $84$ entre $7$: $\frac{84}{7} = 12$.

$$d_1 = 12 \cdot 24 = 288\text{ m}$$

**Paso 2:** Calcular la distancia a la lancha más cercana ($37^\circ$):

$$d_2 = 84 \cdot \cot(37^\circ) = 84 \cdot \frac{4}{3}$$

Simplificando $84$ entre $3$: $\frac{84}{3} = 28$.

$$d_2 = 28 \cdot 4 = 112\text{ m}$$

**Paso 3:** Calcular la distancia de separación entre las embarcaciones:

$$\Delta d = d_1 - d_2 = 288 - 112 = 176\text{ m}$$

**Conclusión:**
La distancia en el mar que separa a ambas embarcaciones es de $176\text{ m}$.

---

#### Ejercicio 9 (Monitoreo de Emisión Volcánica en el Ubinas, Moquegua)
Una estación sismológica del IGP monitorea la columna de ceniza emitida por el volcán Ubinas. Desde un campamento base ubicado a $3\,600\text{ m.s.n.m.}$, el cráter del volcán se divisa con un ángulo de elevación de $37^\circ$ a una distancia horizontal de $4\,000\text{ m}$. Durante una explosión freática, la cúspide de la pluma de cenizas volcánicas se observa desde el mismo campamento con un ángulo de elevación de $53^\circ$. Calcule la altitud del cráter y la altura vertical que alcanzó la columna de cenizas sobre el cráter.

**Análisis Conceptual:**
La distancia horizontal es $d = 4\,000\text{ m}$.
1. La altura del cráter sobre el campamento es $y_1 = d \tan(37^\circ)$.
2. La altura de la pluma de ceniza sobre el campamento es $y_2 = d \tan(53^\circ)$.
3. La altura de la columna de cenizas sobre el cráter es $\Delta y = y_2 - y_1$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el desnivel del cráter respecto al campamento ($y_1$):

$$y_1 = 4\,000 \cdot \tan(37^\circ) = 4\,000 \cdot \frac{3}{4} = 3\,000\text{ m}$$

Altitud del cráter: $3\,600 + 3\,000 = 6\,600\text{ m.s.n.m.}$

**Paso 2:** Calcular la altura de la cúspide de la nube de ceniza ($y_2$):

$$y_2 = 4\,000 \cdot \tan(53^\circ) = 4\,000 \cdot \frac{4}{3} = \frac{16\,000}{3} \approx 5\,333.33\text{ m}$$

**Paso 3:** Calcular la altura de la columna de ceniza sobre el cráter:

$$\Delta y = y_2 - y_1 = \frac{16\,000}{3} - 3\,000 = \frac{16\,000 - 9\,000}{3} = \frac{7\,000}{3} \approx 2\,333.33\text{ m}$$

**Conclusión:**
El cráter se encuentra a $3\,000\text{ m}$ sobre el campamento ($6\,600\text{ m.s.n.m.}$) y la columna de cenizas alcanzó una altura vertical de aproximadamente $2\,333\text{ m}$ sobre el cráter.

---

#### Ejercicio 10 (Instalación de Puente Colgante Comunal en Huancavelica)
Para tender la pasarela de un puente colgante sobre un cañón de $120\text{ m}$ de profundidad, dos brigadistas topógrafos se ubican en extremos opuestos del barranco. El brigadista en el borde superior $A$ divisa la base de anclaje inferior $B$ del estribo opuesto con un ángulo de depresión de $\frac{53^\circ}{2} \approx 26.5^\circ$ ($\tan(53^\circ/2) = \frac{1}{2}$). Calcule el ancho horizontal del cañón y la longitud total del cable de acero tensor principal necesario para conectar directamente $A$ con $B$.

**Análisis Conceptual:**
La profundidad vertical es el cateto opuesto $h = 120\text{ m}$. El ángulo de depresión es $\theta = \frac{53^\circ}{2}$, por lo que el ángulo de elevación desde $B$ hacia $A$ es $\frac{53^\circ}{2}$. La relación de catetos es de $1$ a $2$ ($\tan\theta = \frac{1}{2}$). La longitud del cable es la hipotenusa.

**Solución Paso a Paso:**

**Paso 1:** Calcular el ancho horizontal del cañón ($d$):

$$\tan\left(\frac{53^\circ}{2}\right) = \frac{\text{Profundidad}}{d} = \frac{1}{2}$$

$$\frac{120}{d} = \frac{1}{2} \implies d = 2 \cdot 120 = 240\text{ m}$$

**Paso 2:** Calcular la longitud del cable de acero tensor ($L$) por Pitágoras:

$$L = \sqrt{120^2 + 240^2} = \sqrt{120^2(1 + 2^2)} = 120\sqrt{1 + 4} = 120\sqrt{5}\text{ m}$$

Aproximando con $\sqrt{5} \approx 2.236$:

$$L \approx 120(2.236) \approx 268.33\text{ m}$$

**Conclusión:**
El ancho horizontal del cañón es de $240\text{ m}$ y el cable tensor principal mide $120\sqrt{5}\text{ m} \approx 268.33\text{ m}$.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. Desde un punto en el suelo ubicado a $30\text{ m}$ de la base de un árbol, se observa su copa con un ángulo de elevación de $45^\circ$. ¿Cuál es la altura del árbol?  
A) $15\text{ m}$  
B) $20\text{ m}$  
C) $30\text{ m}$  
D) $45\text{ m}$  
E) $30\sqrt{2}\text{ m}$  

2. Desde la cima de un muro de $20\text{ m}$ de altura, se observa un objeto en el suelo con un ángulo de depresión de $37^\circ$. ¿A qué distancia de la base del muro está el objeto?  
A) $24\text{ m}$  
B) $\frac{80}{3}\text{ m}$  
C) $28\text{ m}$  
D) $30\text{ m}$  
E) $32\text{ m}$  

3. Un niño de $1.20\text{ m}$ de estatura observa la cúspide de una torre con un ángulo de elevación de $53^\circ$. Si el niño se encuentra a $15\text{ m}$ de la torre, ¿cuál es la altura de la torre?  
A) $20.00\text{ m}$  
B) $21.20\text{ m}$  
C) $22.50\text{ m}$  
D) $23.20\text{ m}$  
E) $24.00\text{ m}$  

4. Desde un punto en el suelo se observa la parte alta de un poste con un ángulo de elevación de $30^\circ$. Si la visual mide $40\text{ m}$, calcule la altura del poste.  
A) $15\text{ m}$  
B) $20\text{ m}$  
C) $20\sqrt{3}\text{ m}$  
D) $25\text{ m}$  
E) $30\text{ m}$  

5. El ángulo de elevación con que se observa la cúspide de un edificio es de $60^\circ$. Si la distancia horizontal al edificio es de $10\text{ m}$, ¿cuánto mide la altura del edificio?  
A) $10\text{ m}$  
B) $10\sqrt{3}\text{ m}$  
C) $20\text{ m}$  
D) $20\sqrt{3}\text{ m}$  
E) $30\text{ m}$  

6. Un avión vuela horizontalmente a $1\,500\text{ m}$ de altura sobre el suelo. Desde la torre de control se le observa con un ángulo de elevación de $37^\circ$. ¿Cuál es la distancia en línea recta (visual) entre la torre y el avión?  
A) $2\,000\text{ m}$  
B) $2\,500\text{ m}$  
C) $2\,800\text{ m}$  
D) $3\,000\text{ m}$  
E) $3\,200\text{ m}$  

7. Si un observador ve un objeto con un ángulo de depresión de $28^\circ$, ¿con qué ángulo de elevación ve el objeto al observador?  
A) $28^\circ$  
B) $62^\circ$  
C) $72^\circ$  
D) $90^\circ$  
E) $152^\circ$  

8. Desde la cúspide de un faro de $50\text{ m}$ de altura se observa un barco con un ángulo de depresión de $45^\circ$. ¿A qué distancia del pie del faro está el barco?  
A) $25\text{ m}$  
B) $35\text{ m}$  
C) $50\text{ m}$  
D) $50\sqrt{2}\text{ m}$  
E) $100\text{ m}$  

9. Una cometa queda atrapada en la rama superior de un árbol. La cuerda tensa de la cometa mide $50\text{ m}$ y forma con el suelo horizontal un ángulo de $53^\circ$. ¿A qué altura del suelo está la cometa?  
A) $30\text{ m}$  
B) $35\text{ m}$  
C) $40\text{ m}$  
D) $45\text{ m}$  
E) $48\text{ m}$  

10. Un teodolito de $1.50\text{ m}$ de altura se ubica a $24\text{ m}$ de una pared vertical y mide un ángulo de elevación de $16^\circ$ hacia la corona del muro. Calcule la altura del muro ($\tan 16^\circ \approx \frac{7}{24}$).  
A) $7.00\text{ m}$  
B) $7.50\text{ m}$  
C) $8.00\text{ m}$  
D) $8.50\text{ m}$  
E) $9.20\text{ m}$  

11. El ángulo vertical formado por la línea visual hacia arriba respecto a la línea horizontal recibe el nombre de:  
A) Ángulo de depresión  
B) Ángulo de elevación  
C) Ángulo de tiro  
D) Ángulo azimutal  
E) Ángulo cenital  

12. Desde un punto en el suelo se observa lo alto de una torre con un ángulo de elevación $\alpha$. Si el observador camina alejándose de la torre, el ángulo de elevación:  
A) Aumenta  
B) Disminuye  
C) Se mantiene constante  
D) Se hace recto  
E) Se duplica  

13. Un barco navega hacia un acantilado. Si el vigía del barco divisa la cima del acantilado bajo un ángulo de elevación de $30^\circ$ y el acantilado tiene $60\text{ m}$ de altura, ¿a qué distancia está el barco?  
A) $60\text{ m}$  
B) $60\sqrt{3}\text{ m}$  
C) $120\text{ m}$  
D) $90\sqrt{3}\text{ m}$  
E) $30\sqrt{3}\text{ m}$  

14. Una persona de $1.80\text{ m}$ de estatura proyecta una sombra en el suelo de $2.40\text{ m}$. Calcule la tangente del ángulo de elevación del Sol en ese momento.  
A) $0.60$  
B) $0.75$  
C) $0.80$  
D) $1.25$  
E) $1.33$  

15. Desde lo alto de una torre de $30\text{ m}$ se observa un punto en el suelo con un ángulo de depresión de $60^\circ$. ¿A qué distancia de la base de la torre se encuentra dicho punto?  
A) $10\text{ m}$  
B) $10\sqrt{3}\text{ m}$  
C) $15\sqrt{3}\text{ m}$  
D) $20\text{ m}$  
E) $30\sqrt{3}\text{ m}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. Un observador divisa la cúspide de una antena con un ángulo de elevación de $37^\circ$. Si se acerca $14\text{ m}$ en línea recta hacia la antena, el nuevo ángulo de elevación es de $45^\circ$. Calcule la altura de la antena.  
A) $36\text{ m}$  
B) $40\text{ m}$  
C) $42\text{ m}$  
D) $48\text{ m}$  
E) $56\text{ m}$  

17. Desde lo alto de un edificio de $60\text{ m}$ de altura, los ángulos de depresión hacia dos objetos alineados en el suelo son de $45^\circ$ y $30^\circ$. Calcule la distancia entre los dos objetos.  
A) $60(\sqrt{3} - 1)\text{ m}$  
B) $60(\sqrt{3} + 1)\text{ m}$  
C) $30(\sqrt{3} - 1)\text{ m}$  
D) $60\sqrt{3}\text{ m}$  
E) $45\text{ m}$  

18. En lo alto de un edificio de $40\text{ m}$ se encuentra una asta de bandera. Desde un punto en el suelo se observa la base del asta con un ángulo de elevación de $53^\circ$ y la punta del asta con un ángulo de elevación de $60^\circ$. Calcule la longitud aproximada del asta. ($\text{use } \sqrt{3} \approx 1.732$).  
A) $10.5\text{ m}$  
B) $11.96\text{ m}$  
C) $12.8\text{ m}$  
D) $14.2\text{ m}$  
E) $15.0\text{ m}$  

19. Un observador ve la cúspide de un cerro con un ángulo de elevación $\alpha$ tal que $\tan\alpha = \frac{2}{5}$. Si retrocede $30\text{ m}$, el nuevo ángulo es $\beta$ tal que $\tan\beta = \frac{1}{4}$. Calcule la altura del cerro.  
A) $18\text{ m}$  
B) $20\text{ m}$  
C) $24\text{ m}$  
D) $25\text{ m}$  
E) $30\text{ m}$  

20. Desde un helicóptero suspendido a $600\text{ m}$ de altitud se divisan dos puestos de control militar con ángulos de depresión de $53^\circ$ y $37^\circ$. Si ambos puestos y el helicóptero están en el mismo plano vertical a lados opuestos del helicóptero, ¿cuál es la distancia entre los dos puestos?  
A) $1\,100\text{ m}$  
B) $1\,200\text{ m}$  
C) $1\,250\text{ m}$  
D) $1\,350\text{ m}$  
E) $1\,400\text{ m}$  

21. Una persona colocada a $20\text{ m}$ de una pared observa la parte alta de la pared con un ángulo de elevación $\alpha$. Si retrocede $10\text{ m}$ el ángulo es $\beta$. Si $\tan\alpha + \tan\beta = 1$, halle la altura de la pared.  
A) $10\text{ m}$  
B) $12\text{ m}$  
C) $14\text{ m}$  
D) $15\text{ m}$  
E) $18\text{ m}$  

22. Desde lo alto de una torre de $40\text{ m}$ de altura se observa la azotea de un edificio más bajo con un ángulo de depresión de $37^\circ$ y la base de dicho edificio con un ángulo de depresión de $53^\circ$. Calcule la altura del edificio observado.  
A) $15.5\text{ m}$  
B) $16.0\text{ m}$  
C) $17.5\text{ m}$  
D) $18.0\text{ m}$  
E) $20.0\text{ m}$  

23. Un agrimensor observa la cima de una colina con un ángulo de elevación de $30^\circ$. Avanza $100\text{ m}$ en terreno horizontal hacia ella y el ángulo de elevación pasa a ser de $45^\circ$. Determine la altura de la colina.  
A) $50(\sqrt{3} + 1)\text{ m}$  
B) $50(\sqrt{3} - 1)\text{ m}$  
C) $100(\sqrt{3} - 1)\text{ m}$  
D) $50\sqrt{3}\text{ m}$  
E) $100\sqrt{3}\text{ m}$  

24. Desde la base de un edificio se observa la punta de una torre con un ángulo de elevación de $60^\circ$, y desde la azotea del edificio (de $24\text{ m}$ de altura) se observa la misma punta con un ángulo de elevación de $45^\circ$. Calcule la altura de la torre.  
A) $12(3 + \sqrt{3})\text{ m}$  
B) $24(2 + \sqrt{3})\text{ m}$  
C) $36\text{ m}$  
D) $48\text{ m}$  
E) $12(3 - \sqrt{3})\text{ m}$  

25. Un globo aerostático cautivo se eleva verticalmente. Un observador a $120\text{ m}$ de la base de despegue lo observa primero con un ángulo de elevación de $37^\circ$ y minutos después con un ángulo de elevación de $53^\circ$. ¿Cuántos metros ascendió el globo en ese intervalo?  
A) $60\text{ m}$  
B) $70\text{ m}$  
C) $75\text{ m}$  
D) $80\text{ m}$  
E) $90\text{ m}$  

26. Desde el extremo superior de un faro de $45\text{ m}$ de altura se divisan dos boyas en el mar en la misma dirección con ángulos de depresión de $53^\circ/2$ y $37^\circ/2$. Calcule la distancia entre ambas boyas.  
A) $40\text{ m}$  
B) $45\text{ m}$  
C) $50\text{ m}$  
D) $60\text{ m}$  
E) $75\text{ m}$  

27. Una persona de $1.60\text{ m}$ de estatura observa la parte superior de un monumento con un ángulo de elevación de $37^\circ$. Si camina $7\text{ m}$ hacia el monumento, el ángulo pasa a ser de $45^\circ$. Calcule la altura total del monumento.  
A) $21.00\text{ m}$  
B) $22.60\text{ m}$  
C) $23.20\text{ m}$  
D) $24.40\text{ m}$  
E) $25.60\text{ m}$  

28. Desde un punto del suelo se ve la cúspide de una torre con ángulo de elevación $\theta$. Si nos acercamos una distancia igual al triple de la altura de la torre, el nuevo ángulo es el complemento de $\theta$. Calcule $\tan\theta$.  
A) $\frac{\sqrt{13} - 3}{2}$  
B) $\frac{\sqrt{5} - 1}{2}$  
C) $\frac{1}{3}$  
D) $\frac{1}{2}$  
E) $\sqrt{3} - 1$  

29. Dos edificios de alturas $20\text{ m}$ y $35\text{ m}$ distan $20\text{ m}$ entre sí. Desde la azotea del edificio menor se observa la azotea del mayor con un ángulo de elevación $\alpha$. Calcule $\tan\alpha$.  
A) $0.60$  
B) $0.75$  
C) $0.80$  
D) $1.00$  
E) $1.25$  

30. Un avión vuela en línea recta horizontal a una velocidad de $180\text{ km/h}$ ($50\text{ m/s}$). En un instante, un observador en tierra lo divisa con un ángulo de elevación de $53^\circ$. Diez segundos después, lo divisa en la dirección contraria con un ángulo de elevación de $37^\circ$. Calcule la altitud de vuelo del avión.  
A) $\frac{3000}{7}\text{ m}$  
B) $\frac{6000}{7}\text{ m}$  
C) $\frac{12000}{7}\text{ m}$  
D) $800\text{ m}$  
E) $1\,000\text{ m}$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Un equipo de rescate minero en Cerro de Pasco se encuentra al borde de una chimenea vertical de ventilación. Con un clinómetro digital observan el fondo de la chimenea con un ángulo de depresión de $74^\circ$ respecto a la horizontal. Si el cable guía tensado hasta el fondo mide $250\text{ m}$, calcule la profundidad vertical de la chimenea y la desviación horizontal de la base ($\sin 74^\circ \approx \frac{24}{25}$).  
A) $220\text{ m}$ y $60\text{ m}$  
B) $240\text{ m}$ y $70\text{ m}$  
C) $240\text{ m}$ y $80\text{ m}$  
D) $230\text{ m}$ y $75\text{ m}$  
E) $245\text{ m}$ y $65\text{ m}$  

32. Desde la torre de control del aeropuerto Jorge Chávez a $45\text{ m}$ sobre el suelo, un controlador aéreo divisa un Boeing en aproximación final con un ángulo de elevación de $16^\circ$ ($\tan 16^\circ \approx \frac{7}{24}$). Simultáneamente, el radar indica que la distancia horizontal del avión a la torre es de $2\,400\text{ m}$. Calcule la altitud absoluta del avión respecto al nivel del suelo de la pista.  
A) $700\text{ m}$  
B) $745\text{ m}$  
C) $765\text{ m}$  
D) $780\text{ m}$  
E) $800\text{ m}$  

33. Un ingeniero agrónomo proyecta un sistema de riego por gravedad en una ladera en Abancay. Desde la toma de agua $A$ se observa la parcela inferior $B$ con un ángulo de depresión de $30^\circ$. Si se instala una tubería de polietileno de $160\text{ m}$ que sigue en línea recta la pendiente visual entre $A$ y $B$, ¿cuál es el desnivel hidrostático vertical que generará la presión del agua?  
A) $60\text{ m}$  
B) $70\text{ m}$  
C) $80\text{ m}$  
D) $80\sqrt{3}\text{ m}$  
E) $100\text{ m}$  

34. Una brigada del SERNANP en el Parque Nacional del Manu mide la altura de un árbol de castaña gigante sin talarlo ni escalarlo. El teodolito, situado a $1.50\text{ m}$ del suelo, se emplaza a $36\text{ m}$ de la base del tronco. El ángulo de elevación a la copa del árbol es de $53^\circ$. Calcule la altura biológica total del árbol de castaña.  
A) $46.50\text{ m}$  
B) $48.00\text{ m}$  
C) $49.50\text{ m}$  
D) $51.20\text{ m}$  
E) $52.50\text{ m}$  

35. Desde un bote oceanográfico de IMARPE anclado frente a Huarmey, se divisa el faro de la isla con un ángulo de elevación de $37^\circ$. El barco se aleja $140\text{ m}$ mar adentro en línea recta y el nuevo ángulo de elevación pasa a ser de $16^\circ$ ($\tan 16^\circ \approx \frac{7}{24}$). Calcule la altura del faro sobre el nivel del mar.  
A) $56\text{ m}$  
B) $63\text{ m}$  
C) $70\text{ m}$  
D) $77\text{ m}$  
E) $84\text{ m}$  

36. En una represa hidroeléctrica en Huancayo, una cámara de monitoreo en la corona del dique a $100\text{ m}$ de altura sobre el lecho del río vigila dos compuertas de descarga situadas en el mismo cauce con ángulos de depresión de $45^\circ$ y $53^\circ$. Calcule la distancia que separa a ambas compuertas en el lecho del río.  
A) $20\text{ m}$  
B) $25\text{ m}$  
C) $30\text{ m}$  
D) $35\text{ m}$  
E) $40\text{ m}$  

37. Para instalar una tirolesa turística sobre una quebrada en Tarapoto, el punto de lanzamiento en la cima de un cerro se encuentra a $90\text{ m}$ de altura vertical sobre la plataforma de llegada. Si el ángulo de depresión visual hacia la plataforma es de $37^\circ$, ¿cuántos metros de cable de acero como mínimo se requerirán para la tirolesa sin considerar holgura de tensión?  
A) $120\text{ m}$  
B) $135\text{ m}$  
C) $150\text{ m}$  
D) $165\text{ m}$  
E) $180\text{ m}$  

38. Desde una lancha patrullera en el lago Titicaca, se observa la cúspide de una torre de telecomunicación en la orilla con un ángulo de elevación de $8^\circ$ ($\tan 8^\circ \approx \frac{1}{7}$). Si la torre tiene una altura de $35\text{ m}$, calcule la distancia náutica aproximada en metros que separa a la patrullera de la base de la torre.  
A) $210\text{ m}$  
B) $245\text{ m}$  
C) $280\text{ m}$  
D) $315\text{ m}$  
E) $350\text{ m}$  

39. En un proyecto de saneamiento en Cajamarca, se diseña un colector de aguas pluviales subterráneo. Un topógrafo parado en el punto $A$ a ras del suelo observa el fondo del buzón de inicio $B$ con un ángulo de depresión de $45^\circ$ a $6\text{ m}$ de distancia horizontal. Luego gira $180^\circ$ y observa el fondo del buzón final $C$ con un ángulo de depresión de $37^\circ$ a $8\text{ m}$ de distancia horizontal. ¿Cuál es el desnivel vertical total entre el fondo de ambos buzones?  
A) $0\text{ m (están al mismo nivel)}$  
B) $1\text{ m}$  
C) $2\text{ m}$  
D) $3\text{ m}$  
E) $4\text{ m}$  

40. Un globo de monitoreo meteorológico del SENAMHI en Junín asciende verticalmente. A las 8:00 a.m. se observa desde una estación terrena con ángulo de elevación de $30^\circ$, y a las 8:05 a.m. con ángulo de elevación de $60^\circ$. Si la estación terrena dista horizontalmente $600\text{ m}$ del punto de lanzamiento, calcule la velocidad media de ascenso del globo en metros por minuto.  
A) $60\sqrt{3}\text{ m/min}$  
B) $80\sqrt{3}\text{ m/min}$  
C) $100\sqrt{3}\text{ m/min}$  
D) $120\sqrt{3}\text{ m/min}$  
E) $140\sqrt{3}\text{ m/min}$  

41. Desde un punto del suelo $P$, se observa el extremo inferior de una antena situada sobre un pedestal con ángulo de elevación de $37^\circ$ y el extremo superior de la antena con ángulo de elevación de $53^\circ$. Si la antena mide $14\text{ m}$ de longitud, calcule la altura del pedestal de soporte.  
A) $15\text{ m}$  
B) $18\text{ m}$  
C) $20\text{ m}$  
D) $24\text{ m}$  
E) $25\text{ m}$  

42. Un dron policial patrulla una carretera recta en Trujillo volando a velocidad constante de $20\text{ m/s}$ y altitud constante de $120\text{ m}$. En un instante enfoca un automóvil infractor con un ángulo de depresión de $53^\circ$ (hacia adelante). Diez segundos más tarde, enfoca al mismo automóvil con un ángulo de depresión de $37^\circ$ (hacia atrás, tras haberlo sobrepasado). Calcule la velocidad constante del automóvil en metros por segundo.  
A) $5\text{ m/s}$  
B) $10\text{ m/s}$  
C) $12\text{ m/s}$  
D) $15\text{ m/s}$  
E) $18\text{ m/s}$  

43. Una persona colocada entre dos postes de alumbrado de igual altura de $12\text{ m}$ observa sus cúspides con ángulos de elevación de $37^\circ$ y $53^\circ$. Calcule la distancia total que separa a ambos postes en la calle.  
A) $21\text{ m}$  
B) $23\text{ m}$  
C) $25\text{ m}$  
D) $28\text{ m}$  
E) $30\text{ m}$  

44. Desde la cúspide de un edificio de $36\text{ m}$ de altura, un observador divisa la cúspide de una torre más alta con ángulo de elevación de $30^\circ$ y la base de la misma torre con ángulo de depresión de $60^\circ$. Calcule la altura total de la torre observada.  
A) $42\text{ m}$  
B) $45\text{ m}$  
C) $48\text{ m}$  
D) $52\text{ m}$  
E) $54\text{ m}$  

45. En la selva de Chanchamayo, un puente peatonal de tablas se extiende entre dos peñascos a diferente altura. Desde el peñasco más bajo se observa el extremo superior del puente con un ángulo de elevación de $\frac{37^\circ}{2} \approx 18.5^\circ$ ($\tan(37^\circ/2) = \frac{1}{3}$). Si el largo total de la pasarela del puente es de $10\sqrt{10}\text{ m}$, calcule la diferencia de altitud vertical entre ambos peñascos.  
A) $8\text{ m}$  
B) $10\text{ m}$  
C) $12\text{ m}$  
D) $15\text{ m}$  
E) $20\text{ m}$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | C | **31** | B |
| **2** | B | **17** | A | **32** | B |
| **3** | B | **18** | B | **33** | C |
| **4** | B | **19** | B | **34** | C |
| **5** | B | **20** | C | **35** | C |
| **6** | B | **21** | B | **36** | B |
| **7** | A | **22** | B | **37** | C |
| **8** | C | **23** | A | **38** | B |
| **9** | C | **24** | A | **39** | A |
| **10** | D | **25** | B | **40** | B |
| **11** | B | **26** | B | **41** | B |
| **12** | B | **27** | B | **42** | A |
| **13** | B | **28** | A | **43** | C |
| **14** | B | **29** | B | **44** | C |
| **15** | B | **30** | B | **45** | B |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Mide el ángulo de depresión respecto a la vertical o no suma la estatura del observador. | Trazar siempre la línea horizontal discontinua antes de ubicar el ángulo de elevación o depresión. |
| **En Proceso (60% - 80% aciertos)** | Resuelve problemas directos de un solo triángulo, pero se equivoca en problemas de acercamiento/alejamiento. | Practicar la deducción de la fórmula $H = \frac{d}{\cot\alpha - \cot\beta}$ resolviendo los ejercicios 16 al 30. |
| **Avanzado (> 80% aciertos)** | Modela situaciones complejas con dos móviles, antenas sobre pedestales y aeronaves con destreza. | Resolver los problemas 31 al 45 con límite de 1.5 minutos por problema sin calculadora. |

### Preguntas Guía para la Reflexión:
1. *¿Por qué el ángulo de depresión de un observador es exactamente igual al ángulo de elevación con que el objeto ve al observador?*
2. *¿Cómo influye la altura del instrumento de medición (estación total o teodolito) en la precisión del cálculo de altitudes de montañas?*
3. *¿Por qué cuando un móvil se aleja de una torre a velocidad constante, el ángulo de elevación no decrece de forma lineal sino a través de una función cotangente?*

---

## 7. Formulario Resumen

| Concepto / Configuración | Definición Geométrica | Relación Matemática Rigurosa |
| :--- | :--- | :--- |
| **Línea Horizontal ($\mathcal{L}_H$)** | Paralela al suelo por el ojo del observador | Eje de referencia angular ($0^\circ$) |
| **Ángulo de Elevación ($\alpha$)** | Objeto sobre la horizontal ($\mathcal{L}_V > \mathcal{L}_H$) | $\tan\alpha = \frac{\text{Altura vertical } y}{\text{Distancia horizontal } d}$ |
| **Ángulo de Depresión ($\beta$)** | Objeto bajo la horizontal ($\mathcal{L}_V < \mathcal{L}_H$) | $\tan\beta = \frac{\text{Desnivel vertical } h}{\text{Distancia horizontal } d}$ |
| **Reciprocidad Angular** | Alternos internos entre horizontales paralelas | $\beta_{\text{depresión}}(A \to B) = \alpha_{\text{elevación}}(B \to A)$ |
| **Estatura de Observador ($h_{\text{obs}}$)** | Corrección por cota del ojo | $H_{\text{total}} = d\tan\alpha + h_{\text{obs}}$ |
| **Desplazamiento Horizontal ($d$)** | Acercamiento hacia la torre ($\beta > \alpha$) | $H = \frac{d}{\cot\alpha - \cot\beta}$ |
| **Alejamiento Horizontal ($d$)** | Distancia recorrida alejándose | $d = H(\cot\alpha_{\text{final}} - \cot\alpha_{\text{inicial}})$ |
| **Antena sobre Edificio** | Altura edificio $H_1$, total con antena $H_2$ | $L_{\text{antena}} = d(\tan\alpha_2 - \tan\alpha_1)$ |
| **Notable $37^\circ$ y $53^\circ$** | Proporciones $3k, 4k, 5k$ | $\tan 37^\circ = 3/4,\quad \tan 53^\circ = 4/3$ |
| **Notable $16^\circ$ y $74^\circ$** | Proporciones $7k, 24k, 25k$ | $\tan 16^\circ = 7/24,\quad \tan 74^\circ = 24/7$ |
| **Notable $\frac{53^\circ}{2}$** | Proporciones $1, 2, \sqrt{5}$ | $\tan(53^\circ/2) = 1/2$ |
| **Notable $\frac{37^\circ}{2}$** | Proporciones $1, 3, \sqrt{10}$ | $\tan(37^\circ/2) = 1/3$ |
