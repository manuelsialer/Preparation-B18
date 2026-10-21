# Tema 01: Puntos y Líneas Notables en el Triángulo

## 1. Motivación y Contexto Real

El triángulo es la única figura poligonal rígida por naturaleza: tres barras unidas por sus extremos no pueden deformarse sin quebrar sus lados. Por esta propiedad estructural inmutable, el triángulo es la base del diseño de puentes reticulados, torres de alta tensión, techos parabólicos y andamiajes mineros a lo largo del territorio peruano.

En la gestión territorial y la ingeniería civil comunitaria:
1. **El Baricentro ($G$):** Representa el centro de masa físico de una placa triangular homogénea. Si un gobierno local planifica construir un almacén comunal centralizado para tres comunidades agrícolas que intercambian cargas iguales, el baricentro minimiza el esfuerzo conjunto de transporte.
2. **El Circuncentro ($O$):** Al equidistar de los tres vértices, define el punto exacto para ubicar una torre repetidora de telecomunicaciones, una antena de radio comunitaria o un pozo matriz de agua potable que abastezca a tres poblados con tuberías de idéntica longitud.
3. **El Incentro ($I$):** Al equidistar de los tres lados del triángulo, permite ubicar un puesto de auxilio rápido o estación de vigilancia que se encuentre a la mínima distancia común de tres carreteras perimétricas.

```{figure} ../../assets/geometria/puntos_notables_triangulo.svg
---
width: 95%
align: center
alt: Puntos Notables en el Triángulo - Baricentro e Incentro
---
*Representación vectorial euclidiana del Baricentro ($G$) con división proporcional $2:1$ y del Incentro ($I$) con circunferencia inscrita de radio de contacto $r$.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Propiedades Fundamentales del Triángulo

Para todo triángulo de vértices $A$, $B$ y $C$ con lados opuestos de longitudes $a$, $b$ y $c$, y ángulos interiores $\alpha$, $\beta$ y $\theta$:

1. **Suma de Ángulos Interiores:**

$$\alpha + \beta + \theta = 180^\circ$$

2. **Teorema del Ángulo Exterior:**
   La medida de un ángulo exterior es igual a la suma de las medidas de los dos ángulos interiores no adyacentes a él:

$$\angle \text{ext}_C = \alpha + \beta$$

3. **Existencia del Triángulo (Desigualdad Triangular):**
   La longitud de cualquier lado es estrictamente mayor que la diferencia positiva de los otros dos y menor que su suma:

$$|b - c| < a < b + c$$

4. **Correspondencia (Lado-Ángulo):**
   Al ángulo interior de mayor medida se opone el lado de mayor longitud, y viceversa.

---

### 2.2 Las Cuatro Líneas Notables

#### 1. Mediana
Segmento de recta que une un vértice con el punto medio del lado opuesto. Todo triángulo posee tres medianas.

#### 2. Altura
Segmento de recta perpendicular trazado desde un vértice hacia la recta que contiene al lado opuesto. En un triángulo acutángulo las alturas son interiores; en un triángulo rectángulo dos alturas coinciden con los catetos; en un obtusángulo dos alturas caen en las prolongaciones exteriores de los lados.

#### 3. Bisectriz Interior y Exterior
Rayo o segmento que biseca un ángulo interior o exterior.
* **Teorema de la Bisectriz Interior:** Si $BD$ es bisectriz interior del ángulo $B$, divide al lado opuesto $AC$ en segmentos proporcionales a los lados adyacentes:

$$\frac{c}{a} = \frac{AD}{DC}$$

#### 4. Mediatriz
Recta perpendicular trazada en el punto medio de un lado del triángulo. No necesariamente pasa por el vértice opuesto (solo en triángulos isósceles respecto a la base o en equiláteros).

---

### 2.3 Los Cuatro Puntos Notables

#### 1. Baricentro o Gravicentro ($G$)
* **Definición:** Punto de concurrencia de las tres medianas.
* **Propiedad de Centro de Masa:** Siempre es un punto interior al triángulo.
* **Propiedad Fundamental $2:1$:** El baricentro divide a cada mediana en dos segmentos tales que la distancia del vértice al baricentro es el doble de la distancia del baricentro al punto medio del lado opuesto:

$$BG = 2 \cdot GM \iff \frac{BG}{GM} = 2$$

$$AG = 2 \cdot GN \iff \frac{AG}{GN} = 2$$

$$CG = 2 \cdot GP \iff \frac{CG}{GP} = 2$$

#### 2. Incentro ($I$)
* **Definición:** Punto de concurrencia de las tres bisectrices interiores.
* **Propiedad:** Es el centro de la circunferencia inscrita (*incírculo*), tangente a los tres lados.
* **Equidistancia:** Equidista de los tres lados del triángulo a una distancia igual al inradio $r$.
* **Ángulo entre Bisectrices Interiores:** El ángulo formado por las bisectrices de dos ángulos interiores mide:

$$\angle AIC = 90^\circ + \frac{\angle B}{2}$$

#### 3. Circuncentro ($O$)
* **Definición:** Punto de concurrencia de las mediatrices de los tres lados.
* **Propiedad:** Es el centro de la circunferencia circunscrita (*circuncírculo*) que pasa por los tres vértices.
* **Equidistancia:** Equidista de los tres vértices:

$$OA = OB = OC = R \quad (\text{circunradio})$$

* **Posición según el tipo de triángulo:**
  * En un triángulo **acutángulo**, $O$ es interior.
  * En un triángulo **rectángulo**, $O$ es el **punto medio de la hipotenusa** ($R = \frac{c}{2}$).
  * En un triángulo **obtusángulo**, $O$ es exterior.
* **Ángulo Central:** El ángulo subentendido desde el circuncentro hacia un lado es el doble del ángulo del vértice opuesto:

$$\angle AOC = 2 \cdot \angle B$$

#### 4. Ortocentro ($H$)
* **Definición:** Punto de concurrencia de las rectas que contienen a las tres alturas.
* **Posición según el triángulo:**
  * Acutángulo: $H$ es estrictamente interior.
  * Rectángulo: $H$ coincide exactamente con el **vértice del ángulo recto**.
  * Obtusángulo: $H$ es un punto exterior, ubicado detrás del ángulo obtuso.

---

### 2.4 Puntos Notables en Triángulos Especiales

| Triángulo | Particularidad de las Líneas y Puntos Notables |
| :--- | :--- |
| **Isósceles** | La altura relativa a la base coincide con la mediana, bisectriz y mediatriz. Los puntos $G, I, O, H$ son colineales en dicho eje. |
| **Equilátero** | Los cuatro puntos notables **coinciden en un único punto** ($G = I = O = H$). Las alturas son medianas y bisectrices de longitud $h = \frac{L\sqrt{3}}{2}$, con $R = \frac{2}{3}h$ y $r = \frac{1}{3}h$ ($R = 2r$). |
| **Rectángulo** | El ortocentro está en el vértice recto; el circuncentro en el punto medio de la hipotenusa. La mediana relativa a la hipotenusa mide la mitad de esta: $m_c = \frac{c}{2} = R$. |

---

### 2.5 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Confundir Baricentro con Incentro o Circuncentro:**
>    * El *Incentro* equidista de los **lados**.
>    * El *Circuncentro* equidista de los **vértices**.
>    * El *Baricentro* divide a la mediana en relación $2:1$, pero **no** equidista de lados ni de vértices salvo que el triángulo sea equilátero.
> 2. **Olvidar la relación $2:1$:** En la mediana de longitud total $m$, la parte mayor mide $\frac{2}{3}m$ y la parte menor mide $\frac{1}{3}m$. Si $GM = 4\text{ cm}$, entonces $BG = 8\text{ cm}$ y la mediana completa mide $12\text{ cm}$.
> 3. **Asumir que la mediatriz pasa por el vértice opuesto:** Falso en general; solo pasa por el vértice en triángulos isósceles (respecto a la base) o equiláteros.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Conceptos)

#### Ejercicio 1
En un triángulo $ABC$, la mediana $BM$ mide $24\text{ cm}$ y $G$ es su baricentro. Calcule la longitud del segmento $BG$.

**Análisis Conceptual:**
El baricentro divide a la mediana en razón $2:1$, donde el segmento que conecta el vértice con el baricentro ($BG$) equivale a las dos terceras partes del total de la mediana.

**Solución Paso a Paso:**

**Paso 1:** Identificar la relación métrica del baricentro sobre la mediana:

$$BM = BG + GM$$

$$BG = 2 \cdot GM \implies GM = \frac{BG}{2}$$

**Paso 2:** Expresar la mediana en función de $BG$:

$$BM = BG + \frac{BG}{2} = \frac{3}{2}BG$$

**Paso 3:** Sustituir el valor numérico conocido ($BM = 24$):

$$24 = \frac{3}{2}BG \implies BG = \frac{24 \cdot 2}{3} = \frac{48}{3} = 16\text{ cm}$$

**Conclusión:**
La longitud del segmento $BG$ es $16\text{ cm}$.

---

#### Ejercicio 2
En un triángulo $ABC$, el ángulo interior en el vértice $B$ mide $70^\circ$. Si $I$ es el incentro del triángulo, determine la medida del ángulo $\angle AIC$.

**Análisis Conceptual:**
El incentro es el punto donde concurren las bisectrices interiores. El ángulo formado por las bisectrices de dos vértices interiores cumple el teorema: $\angle AIC = 90^\circ + \frac{\angle B}{2}$.

**Solución Paso a Paso:**

**Paso 1:** Aplicar el teorema del ángulo formado por dos bisectrices interiores:

$$\angle AIC = 90^\circ + \frac{\angle B}{2}$$

**Paso 2:** Reemplazar el valor del ángulo interior $\angle B = 70^\circ$:

$$\angle AIC = 90^\circ + \frac{70^\circ}{2}$$

$$\angle AIC = 90^\circ + 35^\circ = 125^\circ$$

**Conclusión:**
La medida del ángulo $\angle AIC$ es $125^\circ$.

---

#### Ejercicio 3
En un triángulo rectángulo cuya hipotenusa mide $30\text{ cm}$, se traza la mediana relativa a la hipotenusa. Calcule la distancia entre el ortocentro y el circuncentro del triángulo.

**Análisis Conceptual:**
En un triángulo rectángulo:
- El ortocentro ($H$) se ubica exactamente en el vértice del ángulo recto.
- El circuncentro ($O$) se ubica en el punto medio de la hipotenusa.
- La distancia entre $H$ y $O$ es la longitud de la mediana relativa a la hipotenusa.

**Solución Paso a Paso:**

**Paso 1:** Recordar la propiedad de la mediana relativa a la hipotenusa en un triángulo rectángulo:

$$m_h = \frac{\text{Hipotenusa}}{2}$$

**Paso 2:** Sustituir la medida de la hipotenusa ($30\text{ cm}$):

$$m_h = \frac{30}{2} = 15\text{ cm}$$

**Paso 3:** Conectar geométricamente los puntos notables:
El segmento que une el vértice recto ($H$) con el punto medio de la hipotenusa ($O$) es precisamente dicha mediana:

$$d(H, O) = m_h = 15\text{ cm}$$

**Conclusión:**
La distancia entre el ortocentro y el circuncentro es $15\text{ cm}$.

---

### Nivel 2: Intermedio (Operatividad y Propiedades)

#### Ejercicio 4
En un triángulo $ABC$, las medianas $AM$ y $CN$ son perpendiculares entre sí y se cortan en el baricentro $G$. Si $AG = 8\text{ cm}$ y $CG = 6\text{ cm}$, determine la longitud del lado $AC$.

**Análisis Conceptual:**
Dado que las medianas son perpendiculares, el triángulo $AGC$ formado por los segmentos de las medianas y el lado $AC$ es un triángulo rectángulo en $G$.

**Solución Paso a Paso:**

**Paso 1:** Representar las condiciones en el punto de corte $G$:
Las medianas son perpendiculares $\implies \angle AGC = 90^\circ$.

**Paso 2:** Aplicar el Teorema de Pitágoras en el triángulo rectángulo $AGC$:

$$AC^2 = AG^2 + CG^2$$

**Paso 3:** Sustituir las medidas dadas:

$$AC^2 = 8^2 + 6^2 = 64 + 36 = 100$$

$$AC = \sqrt{100} = 10\text{ cm}$$

**Conclusión:**
La longitud del lado $AC$ es $10\text{ cm}$.

---

#### Ejercicio 5
En un triángulo acutángulo $ABC$, $O$ es el circuncentro. Si la medida del ángulo $\angle AOC = 130^\circ$, calcule la medida del ángulo interior $\angle B$.

**Análisis Conceptual:**
El circuncentro es el centro de la circunferencia circunscrita. El ángulo $\angle AOC$ es un ángulo central que subtiende el arco $AC$, mientras que el ángulo $\angle B$ es un ángulo inscrito que subtiende el mismo arco.

**Solución Paso a Paso:**

**Paso 1:** Relacionar el ángulo central con el ángulo inscrito:
En la circunferencia circunscrita:

$$\text{Medida del arco } \widehat{AC} = \angle AOC = 130^\circ$$

**Paso 2:** Calcular el ángulo inscrito $\angle B$:

$$\angle B = \frac{\text{arco } \widehat{AC}}{2} = \frac{130^\circ}{2} = 65^\circ$$

**Conclusión:**
El ángulo interior $\angle B$ mide $65^\circ$.

---

#### Ejercicio 6
En un triángulo $ABC$, el lado $AB = 12\text{ cm}$ y el lado $BC = 18\text{ cm}$. Se traza la bisectriz interior $BD$. Si el segmento $AC$ mide $25\text{ cm}$, calcule la longitud del segmento menor $AD$.

**Análisis Conceptual:**
El Teorema de la Bisectriz Interior establece que el pie de la bisectriz divide al lado opuesto en partes proporcionales a los lados adyacentes: $\frac{AD}{DC} = \frac{AB}{BC}$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la proporción con las medidas conocidas:

$$\frac{AD}{DC} = \frac{12}{18} = \frac{2}{3}$$

Esto significa que $AD = 2k$ y $DC = 3k$.

**Paso 2:** Usar la longitud total del lado $AC$:

$$AC = AD + DC = 2k + 3k = 5k$$

$$5k = 25 \implies k = 5\text{ cm}$$

**Paso 3:** Calcular la longitud de $AD$:

$$AD = 2k = 2(5) = 10\text{ cm}$$

$$DC = 3k = 3(5) = 15\text{ cm}$$

**Conclusión:**
La longitud del segmento menor $AD$ es $10\text{ cm}$.

---

#### Ejercicio 7
En un triángulo equilátero $ABC$ de lado $12\sqrt{3}\text{ cm}$, determine la distancia entre el baricentro y cualquiera de sus vértices (circunradio $R$), así como la longitud del inradio $r$.

**Análisis Conceptual:**
En un triángulo equilátero, los puntos notables coinciden. La altura mide $h = \frac{L\sqrt{3}}{2}$. La distancia de un vértice al baricentro es $R = \frac{2}{3}h$, y la distancia del baricentro a los lados es $r = \frac{1}{3}h$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la altura del triángulo equilátero:

$$h = \frac{L\sqrt{3}}{2} = \frac{(12\sqrt{3})\sqrt{3}}{2} = \frac{12 \cdot 3}{2} = 18\text{ cm}$$

**Paso 2:** Determinar la distancia del vértice al baricentro ($R$):

$$R = \frac{2}{3}h = \frac{2}{3}(18) = 12\text{ cm}$$

**Paso 3:** Determinar el inradio ($r$):

$$r = \frac{1}{3}h = \frac{1}{3}(18) = 6\text{ cm}$$

**Conclusión:**
La distancia de cualquier vértice al baricentro es $12\text{ cm}$ y el inradio es $6\text{ cm}$.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Logística de Telecomunicaciones en la Sierra)
Una empresa de telecomunicaciones implementa el servicio de internet en tres comunidades campesinas ubicadas en los vértices de una región triangular $A$, $B$ y $C$. En un mapa a escala, las distancias entre las comunidades son $AB = 13\text{ km}$, $BC = 14\text{ km}$ y $AC = 15\text{ km}$. Para asegurar una señal homogénea con el menor costo de enlace, se debe instalar una antena repetidora en un punto que equidiste de las tres localidades. Determine el radio de cobertura necesario de la antena (circunradio $R$).

**Análisis Conceptual:**
El punto que equidista de los tres vértices de un triángulo es el **circuncentro**. El radio necesario es el circunradio $R$. Se puede calcular mediante la relación de área y circunradio:

$$\text{Área} = \frac{a \cdot b \cdot c}{4R} \implies R = \frac{a \cdot b \cdot c}{4 \cdot \text{Área}}$$

El área se calcula con la fórmula de Herón: $\text{Área} = \sqrt{p(p-a)(p-b)(p-c)}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el semiperímetro $p$:

$$p = \frac{13 + 14 + 15}{2} = \frac{42}{2} = 21\text{ km}$$

**Paso 2:** Calcular el área por la fórmula de Herón:

$$\text{Área} = \sqrt{21(21 - 13)(21 - 14)(21 - 15)}$$

$$\text{Área} = \sqrt{21 \cdot 8 \cdot 7 \cdot 6}$$

Descomponiendo en factores primos:

$$21 \cdot 8 \cdot 7 \cdot 6 = (3 \cdot 7) \cdot (2^3) \cdot (7) \cdot (2 \cdot 3) = 2^4 \cdot 3^2 \cdot 7^2$$

$$\text{Área} = \sqrt{2^4 \cdot 3^2 \cdot 7^2} = 2^2 \cdot 3 \cdot 7 = 4 \cdot 21 = 84\text{ km}^2$$

**Paso 3:** Despejar el circunradio $R$:

$$R = \frac{a \cdot b \cdot c}{4 \cdot \text{Área}} = \frac{13 \cdot 14 \cdot 15}{4 \cdot 84}$$

Simplificando: $14$ y $84$ tienen catorceava ($84 / 14 = 6$):

$$R = \frac{13 \cdot 15}{4 \cdot 6} = \frac{13 \cdot 5}{4 \cdot 2} = \frac{65}{8} = 8.125\text{ km}$$

**Conclusión:**
La antena debe ubicarse en el circuncentro y contar con un radio de cobertura de $8.125\text{ km}$ (ó $8\frac{1}{8}\text{ km}$).

---

#### Ejercicio 9 (Distribución de Tuberías en Sistema Agrícola de Riego)
Tres parcelas comunales de cultivo de quinua en Puno forman una distribución triangular con linderos de $150\text{ m}$, $200\text{ m}$ y $250\text{ m}$. La junta de regantes requiere construir un pozo de bombeo dentro del terreno de modo que se puedan conectar tuberías de distribución perpendiculares a cada uno de los tres linderos perimétricos con la misma longitud para optimizar la presión hídrica. Determine la longitud requerida de dichas tuberías (inradio $r$) y verifique el punto geométrico correspondiente.

**Análisis Conceptual:**
El punto interior que equidista de los tres lados (linderos) de un triángulo es el **incentro** ($I$), y la distancia común a los lados es el **inradio** ($r$). Observemos que las dimensiones $150, 200, 250$ son proporcionales a $3, 4, 5$, por lo que se trata de un triángulo rectángulo. En todo triángulo rectángulo se cumple el Teorema de Poncelet:

$$a + b = c + 2r$$

**Solución Paso a Paso:**

**Paso 1:** Verificar la naturaleza del triángulo:

$$150^2 + 200^2 = 22\,500 + 40\,000 = 62\,500$$

$$250^2 = 62\,500$$

Se trata de un triángulo rectángulo con catetos $a = 150\text{ m}$, $b = 200\text{ m}$ e hipotenusa $c = 250\text{ m}$.

**Paso 2:** Aplicar el Teorema de Poncelet:

$$\text{Suma de catetos} = \text{Hipotenusa} + 2 \cdot (\text{inradio})$$

$$150 + 200 = 250 + 2r$$

$$350 = 250 + 2r$$

**Paso 3:** Despejar el inradio $r$:

$$2r = 350 - 250 = 100 \implies r = 50\text{ m}$$

**Conclusión:**
El pozo debe ubicarse en el incentro del terreno triangular y cada tubería tendrá una longitud de $50\text{ m}$.

---

#### Ejercicio 10 (Centro de Acopio en Cooperativa Cafetalera)
Una cooperativa de café en Chanchamayo posee tres centros de recolección en los puntos $A$, $B$ y $C$. En el plano, la distancia en línea recta de $A$ al centro $B$ es $18\text{ km}$. La mediana que parte de $C$ hacia el punto medio $M$ de $AB$ mide $27\text{ km}$. La cooperativa decide construir la planta procesadora principal en el baricentro $G$ del triángulo para equilibrar los costos de flete terrestre. Calcule la distancia en línea recta desde la comunidad $C$ hasta la planta procesadora $G$, y desde $G$ hasta el punto de control medio $M$.

**Análisis Conceptual:**
El baricentro $G$ divide a la mediana $CM$ en dos segmentos tales que $CG = 2 \cdot GM$. La longitud total de la mediana es $CM = CG + GM = 3 \cdot GM$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la ecuación con la longitud de la mediana:

$$CM = 27\text{ km}$$

$$CG = \frac{2}{3} \cdot CM$$

$$GM = \frac{1}{3} \cdot CM$$

**Paso 2:** Calcular la distancia de $C$ a la planta $G$:

$$CG = \frac{2}{3}(27) = 18\text{ km}$$

**Paso 3:** Calcular la distancia de la planta $G$ al punto medio $M$:

$$GM = \frac{1}{3}(27) = 9\text{ km}$$

**Conclusión:**
La distancia desde la comunidad $C$ a la planta procesadora $G$ es $18\text{ km}$, y desde la planta hasta el punto de control medio $M$ es de $9\text{ km}$.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. En un triángulo $ABC$, la mediana $AD$ mide $36\text{ cm}$. Si $G$ es el baricentro, halle la longitud de $GD$.  
A) $9\text{ cm}$  
B) $12\text{ cm}$  
C) $18\text{ cm}$  
D) $24\text{ cm}$  
E) $6\text{ cm}$  

2. En un triángulo $PQR$, el ángulo interior en $Q$ mide $80^\circ$. Si $I$ es el incentro del triángulo, ¿cuánto mide el ángulo $\angle PIR$?  
A) $100^\circ$  
B) $120^\circ$  
C) $130^\circ$  
D) $140^\circ$  
E) $150^\circ$  

3. Un triángulo rectángulo tiene catetos de longitudes $18\text{ cm}$ y $24\text{ cm}$. Calcule el radio de la circunferencia circunscrita (circunradio).  
A) $12\text{ cm}$  
B) $15\text{ cm}$  
C) $20\text{ cm}$  
D) $25\text{ cm}$  
E) $30\text{ cm}$  

4. En un triángulo equilátero, la distancia del baricentro a uno de sus lados es de $5\text{ cm}$. ¿Cuál es la longitud de la altura del triángulo?  
A) $10\text{ cm}$  
B) $12\text{ cm}$  
C) $15\text{ cm}$  
D) $20\text{ cm}$  
E) $25\text{ cm}$  

5. ¿Cuál es el punto notable de un triángulo que siempre coincide con el centro de gravedad físico de una lámina triangular homogénea?  
A) Ortocentro  
B) Incentro  
C) Circuncentro  
D) Baricentro  
E) Excentro  

6. En un triángulo obtusángulo, ¿cuáles de los siguientes puntos notables se encuentran en la región exterior del triángulo?  
A) Baricentro e Incentro  
B) Ortocentro y Circuncentro  
C) Solo el Baricentro  
D) Solo el Incentro  
E) Ortocentro e Incentro  

7. En un triángulo $ABC$, la bisectriz interior del ángulo $A$ divide al lado opuesto $BC$ en dos segmentos que miden $6\text{ cm}$ y $9\text{ cm}$. Si el lado $AB = 10\text{ cm}$, halle la longitud del lado $AC$.  
A) $12\text{ cm}$  
B) $14\text{ cm}$  
C) $15\text{ cm}$  
D) $16\text{ cm}$  
E) $18\text{ cm}$  

8. En un triángulo rectángulo, la hipotenusa mide $40\text{ cm}$. ¿Cuánto mide la mediana relativa a la hipotenusa?  
A) $15\text{ cm}$  
B) $20\text{ cm}$  
C) $25\text{ cm}$  
D) $30\text{ cm}$  
E) $35\text{ cm}$  

9. Si en un triángulo $ABC$ el circuncentro es un punto interior y $\angle B = 55^\circ$, halle la medida del ángulo central $\angle AOC$.  
A) $55^\circ$  
B) $90^\circ$  
C) $110^\circ$  
D) $125^\circ$  
E) $145^\circ$  

10. Las tres alturas de un triángulo rectángulo concurren en:  
A) El punto medio de la hipotenusa  
B) El baricentro  
C) El vértice del ángulo recto  
D) El incentro  
E) Un punto exterior al triángulo  

11. En un triángulo $ABC$, la mediana $BM$ corta a la mediana $AN$ en $G$. Si $BG = 14\text{ cm}$, halle la longitud de $GM$.  
A) $7\text{ cm}$  
B) $14\text{ cm}$  
C) $21\text{ cm}$  
D) $28\text{ cm}$  
E) $3.5\text{ cm}$  

12. En un triángulo rectángulo de catetos $6\text{ cm}$ y $8\text{ cm}$, aplique el Teorema de Poncelet para calcular el radio de la circunferencia inscrita (inradio).  
A) $1\text{ cm}$  
B) $2\text{ cm}$  
C) $3\text{ cm}$  
D) $4\text{ cm}$  
E) $2.5\text{ cm}$  

13. La recta perpendicular a un lado de un triángulo en su punto medio recibe el nombre de:  
A) Altura  
B) Mediana  
C) Bisectriz  
D) Mediatriz  
E) Ceviana interior  

14. Si el ángulo formado por dos bisectrices interiores mide $135^\circ$, ¿cuánto mide el tercer ángulo interior del triángulo?  
A) $60^\circ$  
B) $75^\circ$  
C) $80^\circ$  
D) $90^\circ$  
E) $100^\circ$  

15. En un triángulo equilátero cuyo inradio mide $4\text{ cm}$, ¿cuánto mide el circunradio?  
A) $4\text{ cm}$  
B) $6\text{ cm}$  
C) $8\text{ cm}$  
D) $10\text{ cm}$  
E) $12\text{ cm}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. En un triángulo $ABC$, las medianas $AM$ y $CP$ son perpendiculares entre sí en el baricentro $G$. Si $AG = 12\text{ cm}$ y $CG = 5\text{ cm}$, calcule la longitud del lado $AC$.  
A) $13\text{ cm}$  
B) $15\text{ cm}$  
C) $17\text{ cm}$  
D) $19\text{ cm}$  
E) $20\text{ cm}$  

17. En un triángulo $ABC$, $I$ es el incentro y el ángulo $\angle AIC = 140^\circ$. Calcule la medida del ángulo interior en el vértice $B$.  
A) $70^\circ$  
B) $80^\circ$  
C) $90^\circ$  
D) $100^\circ$  
E) $110^\circ$  

18. En un triángulo rectángulo, la distancia del baricentro al circuncentro es de $6\text{ cm}$. Calcule la longitud de la hipotenusa de dicho triángulo.  
A) $18\text{ cm}$  
B) $24\text{ cm}$  
C) $36\text{ cm}$  
D) $48\text{ cm}$  
E) $30\text{ cm}$  

19. En un triángulo $ABC$, los lados miden $AB = 9\text{ cm}$, $BC = 15\text{ cm}$ y $AC = 16\text{ cm}$. Si se traza la bisectriz interior $BD$, halle la longitud del segmento $DC$.  
A) $6\text{ cm}$  
B) $8\text{ cm}$  
C) $10\text{ cm}$  
D) $12\text{ cm}$  
E) $11\text{ cm}$  

20. En un triángulo acutángulo $ABC$, el ortocentro es $H$ y el ángulo $\angle B = 65^\circ$. Calcule la medida del ángulo $\angle AHC$.  
A) $115^\circ$  
B) $125^\circ$  
C) $130^\circ$  
D) $135^\circ$  
E) $145^\circ$  

21. En un triángulo $ABC$, $O$ es el circuncentro. Si $\angle BAO = 35^\circ$, calcule la medida del ángulo interior $\angle C$.  
A) $45^\circ$  
B) $50^\circ$  
C) $55^\circ$  
D) $65^\circ$  
E) $70^\circ$  

22. En un triángulo rectángulo de catetos $9\text{ cm}$ y $12\text{ cm}$, halle la distancia entre el ortocentro y el baricentro.  
A) $3\text{ cm}$  
B) $5\text{ cm}$  
C) $7.5\text{ cm}$  
D) $10\text{ cm}$  
E) $4.5\text{ cm}$  

23. En un triángulo equilátero de lado $6\text{ cm}$, calcule la suma de las distancias desde el baricentro hacia sus tres lados.  
A) $3\text{ cm}$  
B) $3\sqrt{3}\text{ cm}$  
C) $6\text{ cm}$  
D) $6\sqrt{3}\text{ cm}$  
E) $2\sqrt{3}\text{ cm}$  

24. En un triángulo $ABC$, se sabe que $AB = 8\text{ cm}$, $BC = 12\text{ cm}$ y la mediana $BM = 7\text{ cm}$. Utilice el teorema de la mediana para determinar la longitud del lado $AC$.  
A) $8\text{ cm}$  
B) $10\text{ cm}$  
C) $12\text{ cm}$  
D) $14\text{ cm}$  
E) $16\text{ cm}$  

25. En un triángulo $ABC$, la mediatriz del lado $AC$ interseca al lado $BC$ en el punto $P$. Si $AB = 8\text{ cm}$, $BP = 3\text{ cm}$ y $PC = 10\text{ cm}$, calcule el perímetro del triángulo $ABP$.  
A) $18\text{ cm}$  
B) $19\text{ cm}$  
C) $21\text{ cm}$  
D) $23\text{ cm}$  
E) $25\text{ cm}$  

26. En un triángulo rectángulo, la hipotenusa mide $50\text{ cm}$ y el inradio mide $10\text{ cm}$. Calcule el perímetro del triángulo.  
A) $100\text{ cm}$  
B) $110\text{ cm}$  
C) $120\text{ cm}$  
D) $130\text{ cm}$  
E) $140\text{ cm}$  

27. En un triángulo $ABC$, $I$ es el incentro y $E$ es el excentro relativo al lado $BC$. Si $\angle BIC = 118^\circ$, halle la medida del ángulo $\angle BEC$.  
A) $56^\circ$  
B) $59^\circ$  
C) $62^\circ$  
D) $64^\circ$  
E) $68^\circ$  

28. En un triángulo $ABC$, las medianas miden $9\text{ cm}$, $12\text{ cm}$ y $15\text{ cm}$. ¿Qué tipo de triángulo forman los segmentos que van del baricentro a los puntos medios?  
A) Equilátero  
B) Isósceles  
C) Rectángulo  
D) Obtusángulo  
E) Acutángulo no rectángulo  

29. Si el baricentro de un triángulo $ABC$ dista $8\text{ cm}$, $10\text{ cm}$ y $12\text{ cm}$ de los vértices $A$, $B$ y $C$ respectivamente, calcule la suma de las longitudes de las tres medianas.  
A) $30\text{ cm}$  
B) $35\text{ cm}$  
C) $40\text{ cm}$  
D) $45\text{ cm}$  
E) $50\text{ cm}$  

30. En un triángulo rectángulo $ABC$ recto en $B$, se traza la altura $BH$ y la mediana $BM$. Si el ángulo $\angle A = 50^\circ$, calcule la medida del ángulo $\angle HBM$ comprendido entre la altura y la mediana.  
A) $10^\circ$  
B) $15^\circ$  
C) $20^\circ$  
D) $25^\circ$  
E) $30^\circ$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Una posta de salud de emergencia debe ubicarse en un valle interandino para atender a tres pueblos aislados $A$, $B$ y $C$. Las distancias entre los pueblos son $AB = 25\text{ km}$, $BC = 39\text{ km}$ y $AC = 56\text{ km}$. La posta debe instalarse exactamente en el punto que equidiste de los tres pueblos. Calcule la distancia máxima de traslado en línea recta desde la posta hacia cualquiera de los tres pueblos.  
A) $31.25\text{ km}$  
B) $32.5\text{ km}$  
C) $34.125\text{ km}$  
D) $35.5\text{ km}$  
E) $36.25\text{ km}$  

32. En una reserva forestal comunal en Madre de Dios, tres guardabosques recorren los linderos perimétricos que delimitan una parcela triangular con lados de longitudes $1300\text{ m}$, $1400\text{ m}$ y $1500\text{ m}$. Se requiere cavar un reservorio de agua circular tangente a los tres linderos. Calcule la longitud del radio de dicho reservorio (inradio del terreno).  
A) $350\text{ m}$  
B) $400\text{ m}$  
C) $450\text{ m}$  
D) $500\text{ m}$  
E) $380\text{ m}$  

33. Un ingeniero proyecta la estructura de un puente colgante utilizando un marco triangular de acero $ABC$ donde $G$ es su centro de gravedad (baricentro). Si la masa total de la estructura se equilibra cuando la barra mediana inferior $CM$ soporta esfuerzos hasta un punto $G$, y se sabe que la sección $CG$ mide $4.2\text{ m}$, ¿cuál es la longitud total de la viga mediana $CM$?  
A) $5.6\text{ m}$  
B) $6.3\text{ m}$  
C) $7.0\text{ m}$  
D) $8.4\text{ m}$  
E) $6.8\text{ m}$  

34. Una cooperativa agraria en el valle de Majes delimita un terreno triangular $ABC$ para riego tecnificado con $AB = 80\text{ m}$, $BC = 100\text{ m}$ y $AC = 120\text{ m}$. Se traza un canal alimentador a lo largo de la bisectriz interior que parte del vértice $B$ y desemboca en $D$ sobre el lindero $AC$. ¿A qué distancia del vértice $A$ se encuentra el punto de toma de agua $D$?  
A) $48\text{ m}$  
B) $53.33\text{ m}$  
C) $56\text{ m}$  
D) $60\text{ m}$  
E) $64\text{ m}$  

35. En un terreno triangular rectangular destinado a un biohuerto escolar, los catetos miden $20\text{ m}$ y $21\text{ m}$. La dirección del colegio instala un aspersor de riego en el incentro del terreno que cubre exactamente la zona circular inscrita. ¿Cuál es el área de la región de riego cubierta por el aspersor? ($\text{use } \pi \approx 3.14$).  
A) $78.5\text{ m}^2$  
B) $113.04\text{ m}^2$  
C) $153.86\text{ m}^2$  
D) $200.96\text{ m}^2$  
E) $95.4\text{ m}^2$  

36. En un sistema de navegación costera cerca al puerto de Ilo, tres boyas flotantes forman un triángulo $ABC$ con $AB = 15\text{ millas}$, $BC = 20\text{ millas}$ y $AC = 25\text{ millas}$. Una lancha de rescate se encuentra anclada en el ortocentro del sistema triangular. ¿A qué distancia se encuentra la lancha de la boya $B$?  
A) $0\text{ millas (la lancha está en la misma boya } B)$  
B) $5\text{ millas}$  
C) $10\text{ millas}$  
D) $12\text{ millas}$  
E) $15\text{ millas}$  

37. Tres caseríos rurales en Ayacucho están enlazados por caminos rectos de longitudes $7\text{ km}$, $8\text{ km}$ y $9\text{ km}$. Para el tendido de fibra óptica, se instala un nodo central en el baricentro $G$. Si el nodo debe conectarse mediante cable subterráneo hasta el caserío $B$ (opuesto al lado de $8\text{ km}$), halle la longitud aproximada del cable de enlace $BG$.  
A) $4.0\text{ km}$  
B) $4.5\text{ km}$  
C) $4.9\text{ km}$  
D) $5.2\text{ km}$  
E) $5.8\text{ km}$  

38. En una plaza cívica triangular equilátera de $30\text{ m}$ de lado, la municipalidad desea sembrar un jardín circular inscrito y colocar baldosas en el resto de la superficie. ¿Qué porcentaje aproximado de la plaza ocupará el jardín circular inscrito? ($\text{use } \pi \approx 3.1416, \sqrt{3} \approx 1.732$).  
A) $50.3\%$  
B) $55.8\%$  
C) $60.5\%$  
D) $68.2\%$  
E) $72.4\%$  

39. Un dron topográfico sobrevuela un predio triangular $ABC$ a velocidad constante. En el plano de vuelo se ubica el punto $H$ (ortocentro) y el punto $O$ (circuncentro). Si el triángulo es rectángulo e isósceles con hipotenusa de $80\text{ m}$, calcule la distancia en línea recta entre el ortocentro y el circuncentro.  
A) $20\text{ m}$  
B) $30\text{ m}$  
C) $40\text{ m}$  
D) $40\sqrt{2}\text{ m}$  
E) $50\text{ m}$  

40. Tres postes de alumbrado en un parque delimitan un triángulo $ABC$ con ángulos interiores en proporción $1 : 2 : 3$. Se coloca un reflector en el circuncentro del triángulo. Si la distancia del reflector al poste más cercano es de $12\text{ m}$, ¿cuál es la distancia entre los dos postes más alejados entre sí?  
A) $12\text{ m}$  
B) $18\text{ m}$  
C) $24\text{ m}$  
D) $24\sqrt{3}\text{ m}$  
E) $36\text{ m}$  

41. En una estructura de soporte para paneles solares con forma de triángulo isósceles $ABC$ ($AB = BC = 10\text{ m}$ y $AC = 12\text{ m}$), se refuerza la armadura uniendo el vértice $B$ con el baricentro $G$. ¿Cuál es la longitud del tirante de refuerzo $BG$?  
A) $4.50\text{ m}$  
B) $5.00\text{ m}$  
C) $5.33\text{ m}$  
D) $6.00\text{ m}$  
E) $6.67\text{ m}$  

42. Un agricultor divide su terreno triangular en dos sectores mediante una cerca recta que sigue la trayectoria de la bisectriz interior desde el vértice con ángulo de $60^\circ$. Si los linderos adyacentes a dicho vértice miden $60\text{ m}$ y $40\text{ m}$, ¿cuál es la longitud de la cerca divisoria?  
A) $24\sqrt{3}\text{ m}$  
B) $20\sqrt{3}\text{ m}$  
C) $30\sqrt{3}\text{ m}$  
D) $25\text{ m}$  
E) $48\text{ m}$  

43. Una antena de radio instalada en el incentro $I$ de un terreno triangular emite señales de emergencia hacia las tres vías perimetrales. Si los ángulos formados por las líneas que conectan la antena con los vértices son $\angle AIB = 110^\circ$ y $\angle BIC = 130^\circ$, ¿cuánto mide el mayor ángulo interior del terreno triangular?  
A) $70^\circ$  
B) $80^\circ$  
C) $85^\circ$  
D) $90^\circ$  
E) $100^\circ$  

44. En un plano catastral a escala $1:1000$, un polígono de protección hídrica tiene vértices $A, B, C$. Se determina que la distancia de Euler entre el baricentro $G$ y el circuncentro $O$ es de $3\text{ cm}$. Sabiendo que en todo triángulo el ortocentro $H$, el baricentro $G$ y el circuncentro $O$ se encuentran sobre la **Recta de Euler** con la relación $HG = 2 \cdot GO$, ¿cuál es la distancia real en el terreno entre el ortocentro y el circuncentro?  
A) $60\text{ m}$  
B) $90\text{ m}$  
C) $120\text{ m}$  
D) $150\text{ m}$  
E) $180\text{ m}$  

45. En una faena comunal se distribuyen sacos de fertilizante en una parcela triangular $ABC$. Las medianas $AM$ y $BN$ se intersecan perpendicularmente en el baricentro $G$. Si los linderos $BC$ y $AC$ miden $10\text{ m}$ y $8\text{ m}$ respectivamente, halle la longitud del lindero $AB$.  
A) $2\sqrt{5}\text{ m}$  
B) $4\sqrt{5}\text{ m}$  
C) $6\sqrt{5}\text{ m}$  
D) $2\sqrt{10}\text{ m}$  
E) $4\sqrt{10}\text{ m}$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | A | **31** | C |
| **2** | C | **17** | D | **32** | B |
| **3** | B | **18** | C | **33** | B |
| **4** | C | **19** | C | **34** | B |
| **5** | D | **20** | A | **35** | B |
| **6** | B | **21** | C | **36** | A |
| **7** | C | **22** | B | **37** | C |
| **8** | B | **23** | B | **38** | C |
| **9** | C | **24** | B | **39** | C |
| **10** | C | **25** | C | **40** | C |
| **11** | A | **26** | C | **41** | C |
| **12** | B | **27** | C | **42** | A |
| **13** | D | **28** | C | **43** | E |
| **14** | D | **29** | D | **44** | B |
| **15** | C | **30** | A | **45** | D |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde baricentro con incentro o no recuerda la relación $2:1$. | Repasar la tabla comparativa de líneas y puntos notables y dibujar cada uno en papel milimetrado. |
| **En Proceso (60% - 80% aciertos)** | Domina la teoría pero se equivoca en la aplicación del teorema de la bisectriz o Poncelet. | Resolver los ejercicios 1 a 15 prestando especial atención a las proporciones métricas. |
| **Avanzado (> 80% aciertos)** | Modela problemas de contexto real con equidistancias, centros de masa y la Recta de Euler. | Proponer variaciones numéricas de los problemas 31 al 45 y practicar con límite de tiempo (1.5 min por pregunta). |

### Preguntas Guía para la Reflexión:
1. *¿Por qué el baricentro siempre es un punto interior al triángulo, mientras que el ortocentro y el circuncentro pueden ser exteriores?*
2. *¿En qué situaciones de la vida real es indispensable usar el incentro en vez del circuncentro?*
3. *¿Cómo influye la relación de Euler ($HG = 2 \cdot GO$) en el alineamiento de estructuras de ingeniería?*

---

## 7. Formulario Resumen

| Concepto / Línea / Punto | Definición Geométrica | Propiedad Matemática Central |
| :--- | :--- | :--- |
| **Suma de Ángulos Interiores** | Propiedad angular euclidiana | $\alpha + \beta + \theta = 180^\circ$ |
| **Ángulo Exterior** | Ángulo formado por un lado y la prolongación del adyacente | $\angle \text{ext}_C = \alpha + \beta$ |
| **Desigualdad Triangular** | Condición de existencia física | $\|b - c\| < a < b + c$ |
| **Mediana** | Segmento del vértice al punto medio opuesto | Concurren en el Baricentro ($G$) |
| **Baricentro ($G$)** | Centro de gravedad de la región triangular | $BG = 2 \cdot GM \implies BG = \frac{2}{3}BM$ |
| **Bisectriz Interior** | Rayo que biseca el ángulo interior | Teorema: $\frac{c}{a} = \frac{AD}{DC}$ |
| **Incentro ($I$)** | Centro de la circunferencia inscrita ($r$) | Equidista de lados; $\angle AIC = 90^\circ + \frac{\angle B}{2}$ |
| **Circuncentro ($O$)** | Centro de la circunferencia circunscrita ($R$) | Equidista de vértices; $\angle AOC = 2\angle B$ |
| **Ortocentro ($H$)** | Intersección de las tres alturas | Interior (acutángulo), vértice recto (rectángulo), exterior (obtusángulo) |
| **Mediana a la Hipotenusa** | Mediana trazada desde el ángulo recto | $m_h = \frac{c}{2} = R$ |
| **Teorema de Poncelet** | Triángulo rectángulo con inradio $r$ | $a + b = c + 2r$ |
| **Recta de Euler** | Recta que contiene a $H, G$ y $O$ | $HG = 2 \cdot GO$ |
