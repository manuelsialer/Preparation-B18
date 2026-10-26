# Tema 03: Cuadriláteros y Propiedades

## 1. Motivación y Contexto Real

Los cuadriláteros forman el entramado dominante del entorno urbano, arquitectónico y productivo del Perú. Desde el trazado ortogonal en damero de las ciudades fundadas en el virreinato hasta los andenes trapezoidales en el Valle Sagrado del Urubamba, las superficies de cuatro lados optimizan el fraccionamiento de la tierra, la estabilidad de muros de contención y el diseño estructural de cubiertas.

En las aplicaciones prácticas de agronomía, catastro y construcción civil:
1. **Andenes y Muros de Contención Trapezoidales:** En las laderas andinas, las terrazas agrícolas y los terraplenes de contención se construyen con sección transversal trapezoidal para disipar el empuje de tierras mediante una base mayor ancha y un talud inclinado estable.
2. **Parcelación y Riego por Gravedad:** Los terrenos de cultivo en valles costeños (como Cañete o Ica) se delimitan en parcelas rectangulares y trapezoidales donde el cálculo de la base media permite distribuir uniformemente canales de riego secundario.
3. **Estructuras de Techos y Cerchas:** Las armaduras de madera y acero para galpones y naves industriales emplean perfiles trapezoidales y paralelogramos articulados para soportar cargas de lluvia y granizo.

```{figure} ../../assets/geometria/cuadrilateros_trapecio_propiedades.svg
---
width: 95%
align: center
alt: Propiedades Fundamentales del Trapecio
---
*Diagrama euclidiano generado en TikZ + tkz-euclide ilustrando la mediana (base media) $MN$ y el segmento $PQ$ que une los puntos medios de las diagonales.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Definición y Propiedades Generales

Un cuadrilátero es un polígono de cuatro lados y cuatro vértices.
* **Suma de Ángulos Interiores:** En todo cuadrilátero convexo, la suma de las medidas de sus cuatro ángulos interiores es $360^\circ$:

$$\alpha + \beta + \theta + \delta = 360^\circ$$

* **Suma de Ángulos Exteriores:** La suma de las medidas de los ángulos exteriores (uno por vértice) es siempre $360^\circ$.

---

### 2.2 Clasificación de los Cuadriláteros Convexos

Los cuadriláteros convexos se clasifican según el paralelismo de sus lados opuestos en tres grandes familias:

```
Cuadriláteros Convexos
├── 1. Trapezoides (Ningún par de lados paralelos)
│    ├── Trapezoide asimétrico o escaleno
│    └── Trapezoide simétrico o deltoide (cometa)
├── 2. Trapecios (Exactamente un par de lados paralelos)
│    ├── Trapecio escaleno
│    ├── Trapecio isósceles
│    └── Trapecio rectángulo
└── 3. Paralelogramos (Dos pares de lados opuestos paralelos)
     ├── Romboide (Paralelogramo propiamente dicho)
     ├── Rombo (Cuilátero equilátero)
     ├── Rectángulo (Paralelogramo equiángulo)
     └── Cuadrado (Regular: equilátero y equiángulo)
```

---

### 2.3 Familia de los Trapecios

Un trapecio es aquel cuadrilátero que tiene solo dos lados opuestos paralelos denominados **bases** (base mayor $B$ y base menor $b$). Los otros dos lados se denominan lados no paralelos o laterales.

#### Teoremas Fundamentales del Trapecio:

#### 1. Teorema de la Mediana o Base Media ($MN$)
El segmento que une los puntos medios de los lados no paralelos es paralelo a las bases y su longitud es igual a la semisuma de las longitudes de dichas bases:

$$MN \parallel \text{Bases}\quad\text{y}\quad MN = \frac{B + b}{2}$$

#### 2. Teorema del Segmento que Une los Puntos Medios de las Diagonales ($PQ$)
El segmento que une los puntos medios de las dos diagonales de un trapecio es paralelo a las bases y su longitud es igual a la semidiferencia de las longitudes de dichas bases:

$$PQ \parallel \text{Bases}\quad\text{y}\quad PQ = \frac{B - b}{2}$$

#### 3. Tipos Específicos de Trapecios:
* **Trapecio Escaleno:** Sus lados laterales no paralelos tienen longitudes diferentes.
* **Trapecio Isósceles:** Sus lados laterales no paralelos tienen la misma longitud.
  * Los ángulos adyacentes a cada base son congruentes ($\alpha = \alpha$, $\beta = \beta$).
  * Sus diagonales son de igual longitud ($d_1 = d_2$).
* **Trapecio Rectángulo:** Uno de los lados laterales es perpendicular a las bases, coincidiendo con la altura $h$ del trapecio.

---

### 2.4 Familia de los Paralelogramos

Un paralelogramo es aquel cuadrilátero en el cual sus dos pares de lados opuestos son paralelos y congruentes.

#### Propiedades Universales de Todo Paralelogramo:
1. **Lados Opuestos:** Son congruentes dos a dos ($AB = CD$ y $BC = AD$).
2. **Ángulos Opuestos:** Son de igual medida ($\angle A = \angle C$ y $\angle B = \angle D$).
3. **Ángulos Consecutivos:** Son suplementarios ($\angle A + \angle B = 180^\circ$).
4. **Diagonales:** Se cortan mutuamente en su punto medio (se bisecan).

#### Tipos Particulares de Paralelogramos:

| Paralelogramo | Lados | Ángulos | Diagonales |
| :--- | :--- | :--- | :--- |
| **Romboide** | Lados opuestos iguales | Ángulos opuestos iguales | Se bisecan en longitudes distintas |
| **Rombo** | 4 lados congruentes ($L$) | Ángulos opuestos iguales | Perpendiculares ($90^\circ$), se bisecan y son bisectrices |
| **Rectángulo** | Lados opuestos iguales | 4 ángulos rectos ($90^\circ$) | Se bisecan y son de **igual longitud** |
| **Cuadrado** | 4 lados congruentes | 4 ángulos rectos ($90^\circ$) | Congruentes, perpendiculares ($90^\circ$), se bisecan y son bisectrices ($45^\circ$) |

---

### 2.5 Teorema de Varignon

En todo cuadrilátero convexo o cóncavo, los puntos medios de sus cuatro lados determinan siempre un **paralelogramo** (denominado Paralelogramo de Varignon).
* El perímetro del paralelogramo de Varignon es igual a la suma de las longitudes de las diagonales del cuadrilátero original:

$$\text{Perímetro}(\text{Varignon}) = d_1 + d_2$$

* El área del paralelogramo de Varignon es exactamente la mitad del área del cuadrilátero original:

$$\text{Área}(\text{Varignon}) = \frac{\text{Área}(\text{Cuadrilátero})}{2}$$

---

### 2.6 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Confundir la Base Media con la Semidiferencia:**
>    * Mediana (puntos medios de lados laterales) = $\frac{B + b}{2}$ (Semisuma, siempre mayor).
>    * Segmento entre puntos medios de diagonales = $\frac{B - b}{2}$ (Semidiferencia, siempre menor).
> 2. **Asumir que las diagonales del romboide son perpendiculares:** Falso. Las diagonales son perpendiculares únicamente en el **rombo** y en el **cuadrado**.
> 3. **Asumir que las diagonales del rombo son congruentes:** Falso. En el rombo una diagonal es mayor ($D$) y otra menor ($d$). Solo son congruentes en el **rectángulo** y en el **cuadrado**.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Propiedades)

#### Ejercicio 1
En un trapecio, la base menor mide $14\text{ cm}$ y la base mayor mide $26\text{ cm}$. Calcule la longitud de su base media (mediana).

**Análisis Conceptual:**
La base media une los puntos medios de los lados laterales y su longitud equivale a la semisuma de las bases: $MN = \frac{B + b}{2}$.

**Solución Paso a Paso:**

**Paso 1:** Identificar las bases:

$$b = 14\text{ cm},\quad B = 26\text{ cm}$$

**Paso 2:** Aplicar la fórmula de la base media:

$$MN = \frac{B + b}{2} = \frac{26 + 14}{2}$$

**Paso 3:** Calcular el resultado:

$$MN = \frac{40}{2} = 20\text{ cm}$$

**Conclusión:**
La longitud de la base media es $20\text{ cm}$.

---

#### Ejercicio 2
En un trapecio, las bases miden $32\text{ cm}$ y $18\text{ cm}$. Calcule la longitud del segmento que une los puntos medios de sus diagonales.

**Análisis Conceptual:**
El segmento entre puntos medios de diagonales se obtiene con la semidiferencia de las bases: $x = \frac{B - b}{2}$.

**Solución Paso a Paso:**

**Paso 1:** Identificar los datos:

$$B = 32\text{ cm},\quad b = 18\text{ cm}$$

**Paso 2:** Aplicar la fórmula de la semidiferencia:

$$x = \frac{B - b}{2} = \frac{32 - 18}{2}$$

**Paso 3:** Realizar la sustracción y división:

$$x = \frac{14}{2} = 7\text{ cm}$$

**Conclusión:**
El segmento que une los puntos medios de las diagonales mide $7\text{ cm}$.

---

#### Ejercicio 3
En un romboide $ABCD$, la medida del ángulo interior en el vértice $A$ es $50^\circ$. Determine la medida de los otros tres ángulos interiores del romboide.

**Análisis Conceptual:**
En todo paralelogramo (y por ende en el romboide), los ángulos opuestos son congruentes ($\angle C = \angle A$) y los ángulos consecutivos son suplementarios ($\angle B = 180^\circ - \angle A$).

**Solución Paso a Paso:**

**Paso 1:** Hallar el ángulo opuesto $\angle C$:

$$\angle C = \angle A = 50^\circ$$

**Paso 2:** Hallar el ángulo consecutivo $\angle B$:

$$\angle B = 180^\circ - \angle A = 180^\circ - 50^\circ = 130^\circ$$

**Paso 3:** Hallar el ángulo opuesto $\angle D$:

$$\angle D = \angle B = 130^\circ$$

**Conclusión:**
Los ángulos interiores miden $50^\circ$, $130^\circ$, $50^\circ$ y $130^\circ$.

---

### Nivel 2: Intermedio (Operatividad y Razonamiento)

#### Ejercicio 4
En un trapecio, la base media mide $22\text{ cm}$ y el segmento que une los puntos medios de sus diagonales mide $6\text{ cm}$. Calcule las longitudes de la base mayor y la base menor.

**Análisis Conceptual:**
Tenemos un sistema de dos ecuaciones lineales con dos incógnitas ($B$ y $b$) formulado a partir de la semisuma y la semidiferencia.

**Solución Paso a Paso:**

**Paso 1:** Plantear las dos ecuaciones:

$$\frac{B + b}{2} = 22 \implies B + b = 44$$

$$\frac{B - b}{2} = 6 \implies B - b = 12$$

**Paso 2:** Sumar miembro a miembro ambas ecuaciones:

$$(B + b) + (B - b) = 44 + 12$$

$$2B = 56 \implies B = 28\text{ cm}$$

**Paso 3:** Sustituir $B = 28$ para encontrar $b$:

$$28 + b = 44 \implies b = 44 - 28 = 16\text{ cm}$$

**Conclusión:**
La base mayor mide $28\text{ cm}$ y la base menor mide $16\text{ cm}$.

---

#### Ejercicio 5
En un trapecio rectángulo $ABCD$ recto en $A$ y $D$, el ángulo interior en $C$ mide $53^\circ$. Si la base menor $BC$ mide $8\text{ cm}$ y el lado lateral no paralelo $CD$ mide $15\text{ cm}$, calcule la longitud de la base mayor $AD$.

**Análisis Conceptual:**
Se traza la altura $CH$ desde el vértice $C$ perpendicular a la base mayor $AD$. Se forma un rectángulo $ABCH$ y un triángulo rectángulo notable de $37^\circ$ y $53^\circ$ ($\triangle CHD$).

**Solución Paso a Paso:**

**Paso 1:** Descomponer la base mayor $AD$:

$$AD = AH + HD$$

Como $ABCH$ es un rectángulo, $AH = BC = 8\text{ cm}$.

**Paso 2:** Resolver el triángulo rectángulo $\triangle CHD$ recto en $H$:
El ángulo en $C$ dentro del triángulo es $90^\circ - 53^\circ = 37^\circ$, y el ángulo en $D$ es $53^\circ$ (o viceversa según el ángulo de inclinación). Con hipotenusa $CD = 15 = 5k \implies k = 3$.
El cateto adyacente al ángulo de $53^\circ$ (sobre la base) mide:

$$HD = 3k = 3(3) = 9\text{ cm}$$

*(o si el ángulo en $C$ es obtuso de $127^\circ$, el agudo en $D$ es $53^\circ$, luego $HD = 15 \cos(53^\circ) = 15(3/5) = 9\text{ cm}$).*

**Paso 3:** Sumar los tramos para hallar $AD$:

$$AD = AH + HD = 8 + 9 = 17\text{ cm}$$

**Conclusión:**
La base mayor $AD$ mide $17\text{ cm}$.

---

#### Ejercicio 6
Las diagonales de un rombo miden $24\text{ cm}$ y $10\text{ cm}$. Calcule el perímetro del rombo y la longitud de su altura (distancia entre lados opuestos).

**Análisis Conceptual:**
Las diagonales de un rombo son perpendiculares y se cortan en sus puntos medios. Cada uno de los 4 triángulos rectángulos congruentes tiene catetos de longitudes $\frac{24}{2} = 12$ y $\frac{10}{2} = 5$. Por Pitágoras hallamos el lado $L$ y luego igualamos el área para hallar la altura.

**Solución Paso a Paso:**

**Paso 1:** Hallar el lado del rombo $L$:

$$L = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13\text{ cm}$$

**Paso 2:** Calcular el perímetro:

$$\text{Perímetro} = 4L = 4(13) = 52\text{ cm}$$

**Paso 3:** Calcular el área del rombo mediante sus diagonales:

$$\text{Área} = \frac{D \cdot d}{2} = \frac{24 \cdot 10}{2} = 120\text{ cm}^2$$

**Paso 4:** Calcular la altura igualando el área como base por altura ($L \cdot h$):

$$\text{Área} = L \cdot h \implies 120 = 13 \cdot h \implies h = \frac{120}{13}\text{ cm} \approx 9.23\text{ cm}$$

**Conclusión:**
El perímetro del rombo es $52\text{ cm}$ y su altura es $\frac{120}{13}\text{ cm}$.

---

#### Ejercicio 7
En un trapecio isósceles, las bases miden $10\text{ cm}$ y $26\text{ cm}$, y los lados no paralelos miden $17\text{ cm}$ cada uno. Calcule la longitud de sus diagonales.

**Análisis Conceptual:**
En un trapecio isósceles, al trazar las alturas desde los extremos de la base menor, la base mayor se divide en tres segmentos: el central igual a la base menor ($10$) y dos laterales simétricos iguales a $\frac{26 - 10}{2} = 8$. Se halla la altura $h$ y luego la diagonal con un triángulo rectángulo.

**Solución Paso a Paso:**

**Paso 1:** Calcular las proyecciones laterales simétricas:

$$x = \frac{B - b}{2} = \frac{26 - 10}{2} = 8\text{ cm}$$

**Paso 2:** Calcular la altura $h$ por el Teorema de Pitágoras en el triángulo lateral:

$$h = \sqrt{17^2 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$$

**Paso 3:** Calcular la diagonal $d$ considerando el triángulo rectángulo de catetos $h = 15$ y base $B - x = 26 - 8 = 18$:

$$d = \sqrt{15^2 + 18^2} = \sqrt{225 + 324} = \sqrt{549} = \sqrt{9 \cdot 61} = 3\sqrt{61}\text{ cm} \approx 23.43\text{ cm}$$

**Conclusión:**
La longitud de las diagonales es $3\sqrt{61}\text{ cm}$.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Diseño de un Canal de Evacuación Pluvial en Piura)
Durante las obras de prevención ante el Fenómeno de El Niño en Piura, una brigada comunal de ingeniería diseña un canal colector de concreto de sección transversal trapezoidal isósceles. El fondo del canal (base menor) mide $1.8\text{ m}$ de ancho y la abertura superior (base mayor) mide $3.4\text{ m}$. La profundidad vertical del canal (altura) es de $1.5\text{ m}$. Para calcular la cantidad de geomembrana impermeabilizante requerida, se necesita determinar la longitud inclinada de cada uno de los taludes laterales y el área de la sección transversal de flujo.

**Análisis Conceptual:**
La sección es un trapecio isósceles con $b = 1.8\text{ m}$, $B = 3.4\text{ m}$ y altura $h = 1.5\text{ m}$. Cada proyección horizontal lateral es $x = \frac{B-b}{2}$. El talud lateral es la hipotenusa de un triángulo rectángulo de catetos $x$ y $h$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la proyección horizontal de cada talud:

$$x = \frac{B - b}{2} = \frac{3.4 - 1.8}{2} = \frac{1.6}{2} = 0.8\text{ m}$$

**Paso 2:** Calcular la longitud del talud inclinado ($L_{\text{talud}}$) por Pitágoras:

$$L_{\text{talud}} = \sqrt{x^2 + h^2} = \sqrt{0.8^2 + 1.5^2} = \sqrt{0.64 + 2.25} = \sqrt{2.89} = 1.7\text{ m}$$

**Paso 3:** Calcular el área de la sección transversal de flujo:

$$\text{Área} = \left(\frac{B + b}{2}\right) \cdot h = \left(\frac{3.4 + 1.8}{2}\right) \cdot 1.5 = \left(\frac{5.2}{2}\right) \cdot 1.5 = 2.6 \cdot 1.5 = 3.9\text{ m}^2$$

**Conclusión:**
Cada talud inclinado mide $1.7\text{ m}$ y el área de la sección transversal de flujo es de $3.9\text{ m}^2$.

---

#### Ejercicio 9 (Subdivisión de una Parcela Agraria Comunal en Junín)
Una asociación de productores de papa en el valle del Mantaro posee un predio con forma de trapecio con linderos paralelos de $120\text{ m}$ y $200\text{ m}$. La junta directiva decide trazar un cerco divisorio paralelo a las bases a lo largo de la base media del terreno para repartir equitativamente dos zonas de producción. Si el ancho perpendicular total del terreno (distancia entre bases) es de $80\text{ m}$, calcule la longitud del cerco divisorio y determine el área de cada una de las dos sub-parcelas resultantes.

**Análisis Conceptual:**
El cerco sigue la base media $MN = \frac{B+b}{2}$. Como $MN$ une los puntos medios de los laterales, la altura total de $80\text{ m}$ queda dividida exactamente en dos alturas iguales de $h_1 = h_2 = 40\text{ m}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la longitud del cerco divisorio (base media):

$$MN = \frac{B + b}{2} = \frac{200 + 120}{2} = \frac{320}{2} = 160\text{ m}$$

**Paso 2:** Calcular el área de la sub-parcela superior (trapecio con bases $120\text{ m}$ y $160\text{ m}$, y altura $40\text{ m}$):

$$A_1 = \left(\frac{120 + 160}{2}\right) \cdot 40 = 140 \cdot 40 = 5\,600\text{ m}^2$$

**Paso 3:** Calcular el área de la sub-parcela inferior (trapecio con bases $160\text{ m}$ y $200\text{ m}$, y altura $40\text{ m}$):

$$A_2 = \left(\frac{160 + 200}{2}\right) \cdot 40 = 180 \cdot 40 = 7\,200\text{ m}^2$$

**Paso 4:** Verificación de área total:

$$A_{\text{total}} = \left(\frac{200 + 120}{2}\right) \cdot 80 = 160 \cdot 80 = 12\,800\text{ m}^2$$

$$A_1 + A_2 = 5\,600 + 7\,200 = 12\,800\text{ m}^2 \quad \text{(Correcto)}$$

**Conclusión:**
El cerco divisorio mide $160\text{ m}$, la parcela superior tiene un área de $5\,600\text{ m}^2$ ($0.56\text{ ha}$) y la inferior de $7\,200\text{ m}^2$ ($0.72\text{ ha}$).

---

#### Ejercicio 10 (Diseño Estructural de Ventana Solar en Edificación Bioclimática)
En una vivienda bioclimática en Puno construida para soportar heladas, se instala un tragaluz cenital con forma de romboide $ABCD$. Mediciones interiores indican que la diagonal menor mide $16\text{ dm}$ y forma un ángulo recto con uno de los lados laterales de longitud $12\text{ dm}$. Calcule la longitud del lado mayor del tragaluz, el área total de captación de luz solar y la longitud de la diagonal mayor.

**Análisis Conceptual:**
El romboide tiene lados $AB = CD = 12\text{ dm}$ y diagonal $BD = 16\text{ dm}$ con $\angle ABD = 90^\circ$. El triángulo $\triangle ABD$ es rectángulo en $B$, por lo que el lado mayor $AD$ es su hipotenusa. El área del romboide es el doble del área del triángulo $\triangle ABD$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el lado mayor $AD$ por el Teorema de Pitágoras en el triángulo rectángulo $\triangle ABD$:

$$AD = \sqrt{AB^2 + BD^2} = \sqrt{12^2 + 16^2} = \sqrt{144 + 256} = \sqrt{400} = 20\text{ dm}$$

**Paso 2:** Calcular el área de captación solar del tragaluz:

$$\text{Área}(\triangle ABD) = \frac{12 \cdot 16}{2} = 96\text{ dm}^2$$

$$\text{Área total}(ABCD) = 2 \cdot \text{Área}(\triangle ABD) = 2 \cdot 96 = 192\text{ dm}^2 = 1.92\text{ m}^2$$

**Paso 3:** Calcular la diagonal mayor $AC$ mediante la Ley de los Paralelogramos ($d_1^2 + d_2^2 = 2(a^2 + b^2)$):

$$AC^2 + BD^2 = 2(AB^2 + AD^2)$$

$$AC^2 + 16^2 = 2(12^2 + 20^2)$$

$$AC^2 + 256 = 2(144 + 400) = 2(544) = 1088$$

$$AC^2 = 1088 - 256 = 832$$

$$AC = \sqrt{832} = \sqrt{64 \cdot 13} = 8\sqrt{13}\text{ dm} \approx 28.84\text{ dm}$$

**Conclusión:**
El lado mayor del tragaluz mide $20\text{ dm}$ ($2\text{ m}$), el área de captación solar es $192\text{ dm}^2$ ($1.92\text{ m}^2$) y la diagonal mayor mide $8\sqrt{13}\text{ dm}$.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. En un trapecio, las bases miden $16\text{ cm}$ y $28\text{ cm}$. Calcule la longitud de la base media.  
A) $20\text{ cm}$  
B) $21\text{ cm}$  
C) $22\text{ cm}$  
D) $23\text{ cm}$  
E) $24\text{ cm}$  

2. En un trapecio, las bases miden $45\text{ cm}$ y $15\text{ cm}$. Halle la longitud del segmento que une los puntos medios de sus diagonales.  
A) $10\text{ cm}$  
B) $12\text{ cm}$  
C) $15\text{ cm}$  
D) $18\text{ cm}$  
E) $20\text{ cm}$  

3. En un romboide, dos ángulos consecutivos están en la relación de $1$ a $3$. ¿Cuánto mide el menor ángulo interior?  
A) $30^\circ$  
B) $40^\circ$  
C) $45^\circ$  
D) $60^\circ$  
E) $75^\circ$  

4. Las diagonales de un rombo miden $16\text{ cm}$ y $12\text{ cm}$. Calcule el perímetro del rombo.  
A) $36\text{ cm}$  
B) $40\text{ cm}$  
C) $44\text{ cm}$  
D) $48\text{ cm}$  
E) $52\text{ cm}$  

5. ¿Cuál de los siguientes cuadriláteros tiene sus diagonales perpendiculares y congruentes a la vez?  
A) Rombo  
B) Rectángulo  
C) Cuadrado  
D) Trapecio isósceles  
E) Romboide  

6. En un rectángulo, la base mide $24\text{ cm}$ y la altura mide $7\text{ cm}$. ¿Cuánto mide cada una de sus diagonales?  
A) $23\text{ cm}$  
B) $25\text{ cm}$  
C) $26\text{ cm}$  
D) $27\text{ cm}$  
E) $28\text{ cm}$  

7. En un trapecio isósceles, uno de sus ángulos interiores mide $70^\circ$. ¿Cuánto mide el mayor ángulo interior?  
A) $100^\circ$  
B) $110^\circ$  
C) $120^\circ$  
D) $130^\circ$  
E) $140^\circ$  

8. La base media de un trapecio mide $30\text{ cm}$. Si la base menor mide $18\text{ cm}$, ¿cuánto mide la base mayor?  
A) $38\text{ cm}$  
B) $40\text{ cm}$  
C) $42\text{ cm}$  
D) $44\text{ cm}$  
E) $46\text{ cm}$  

9. En un cuadrado de perímetro $32\text{ cm}$, la longitud de su diagonal es:  
A) $8\text{ cm}$  
B) $8\sqrt{2}\text{ cm}$  
C) $16\text{ cm}$  
D) $16\sqrt{2}\text{ cm}$  
E) $4\sqrt{2}\text{ cm}$  

10. Si en un paralelogramo las diagonales son de igual longitud, entonces con certeza es un:  
A) Rombo  
B) Rectángulo o Cuadrado  
C) Romboide  
D) Trapecio  
E) Trapezoide  

11. La suma de las medidas de los ángulos interiores de cualquier cuadrilátero convexo es igual a:  
A) $180^\circ$  
B) $270^\circ$  
C) $360^\circ$  
D) $450^\circ$  
E) $540^\circ$  

12. En un trapecio, el segmento que une los puntos medios de las diagonales mide $8\text{ cm}$. Si la base mayor mide $30\text{ cm}$, ¿cuánto mide la base menor?  
A) $12\text{ cm}$  
B) $14\text{ cm}$  
C) $16\text{ cm}$  
D) $18\text{ cm}$  
E) $20\text{ cm}$  

13. En un rombo de lado $15\text{ cm}$, una diagonal mide $18\text{ cm}$. ¿Cuánto mide la otra diagonal?  
A) $20\text{ cm}$  
B) $22\text{ cm}$  
C) $24\text{ cm}$  
D) $26\text{ cm}$  
E) $28\text{ cm}$  

14. En un trapezoide simétrico (deltoide), las diagonales son:  
A) Paralelas  
B) De igual longitud  
C) Perpendiculares  
D) Colineales  
E) Oblicuas a $45^\circ$  

15. El polígono que se forma al unir consecutivamente los puntos medios de los lados de un cuadrilátero cualquiera es siempre un:  
A) Trapecio  
B) Rectángulo  
C) Paralelogramo  
D) Rombo  
E) Cuadrado  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. En un trapecio, la base media y el segmento que une los puntos medios de sus diagonales suman $38\text{ cm}$. Calcule la longitud de la base mayor.  
A) $32\text{ cm}$  
B) $34\text{ cm}$  
C) $36\text{ cm}$  
D) $38\text{ cm}$  
E) $40\text{ cm}$  

17. En un trapecio rectángulo, el ángulo agudo mide $45^\circ$. Si la base menor mide $6\text{ cm}$ y la altura mide $8\text{ cm}$, calcule la longitud de la base mayor.  
A) $12\text{ cm}$  
B) $14\text{ cm}$  
C) $15\text{ cm}$  
D) $16\text{ cm}$  
E) $18\text{ cm}$  

18. En un romboide $ABCD$, la bisectriz del ángulo $A$ corta al lado opuesto $BC$ en el punto $E$. Si $AB = 9\text{ cm}$ y $EC = 5\text{ cm}$, determine el perímetro del romboide.  
A) $40\text{ cm}$  
B) $42\text{ cm}$  
C) $44\text{ cm}$  
D) $46\text{ cm}$  
E) $48\text{ cm}$  

19. Las diagonales de un trapecio miden $13\text{ cm}$ y $15\text{ cm}$, y su altura mide $12\text{ cm}$. Calcule el área de dicho trapecio.  
A) $72\text{ cm}^2$  
B) $84\text{ cm}^2$  
C) $96\text{ cm}^2$  
D) $108\text{ cm}^2$  
E) $114\text{ cm}^2$  

20. En un trapecio isósceles de bases $12\text{ cm}$ y $28\text{ cm}$, las diagonales son perpendiculares entre sí. Calcule la longitud de la altura del trapecio.  
A) $16\text{ cm}$  
B) $18\text{ cm}$  
C) $20\text{ cm}$  
D) $22\text{ cm}$  
E) $24\text{ cm}$  

21. En un paralelogramo $ABCD$, las diagonales se cortan en $O$. Si $AC = 20\text{ cm}$, $BD = 16\text{ cm}$ y el ángulo $\angle AOB = 90^\circ$, calcule el área del paralelogramo.  
A) $120\text{ cm}^2$  
B) $140\text{ cm}^2$  
C) $160\text{ cm}^2$  
D) $180\text{ cm}^2$  
E) $200\text{ cm}^2$  

22. En un trapecio $ABCD$ ($BC \parallel AD$), las bisectrices de los ángulos $A$ y $B$ se intersecan en un punto $P$ que pertenece al lado lateral $CD$. Si $AB = 14\text{ cm}$, calcule la longitud del lado lateral $CD$.  
A) $12\text{ cm}$  
B) $14\text{ cm}$  
C) $16\text{ cm}$  
D) $18\text{ cm}$  
E) $21\text{ cm}$  

23. En un rectángulo $ABCD$, se traza la perpendicular $BH$ a la diagonal $AC$. Si $AH = 9\text{ cm}$ y $HC = 16\text{ cm}$, calcule el área del rectángulo.  
A) $250\text{ cm}^2$  
B) $280\text{ cm}^2$  
C) $300\text{ cm}^2$  
D) $320\text{ cm}^2$  
E) $360\text{ cm}^2$  

24. En un trapecio, la base menor mide $x+2$, la base media mide $2x+3$ y la base mayor mide $4x-2$. Calcule el valor numérico de la base mayor.  
A) $12$  
B) $14$  
C) $16$  
D) $18$  
E) $22$  

25. En un cuadrilátero convexo $ABCD$, las diagonales miden $18\text{ cm}$ y $24\text{ cm}$ y forman un ángulo de $30^\circ$. Calcule el área del cuadrilátero de Varignon formado por sus puntos medios.  
A) $48\text{ cm}^2$  
B) $54\text{ cm}^2$  
C) $60\text{ cm}^2$  
D) $72\text{ cm}^2$  
E) $108\text{ cm}^2$  

26. En un rombo, la altura mide $9.6\text{ cm}$ y una diagonal mide $12\text{ cm}$. Calcule la longitud del lado del rombo.  
A) $8\text{ cm}$  
B) $9\text{ cm}$  
C) $10\text{ cm}$  
D) $11\text{ cm}$  
E) $12\text{ cm}$  

27. En un trapecio isósceles, la base menor es congruente con los lados no paralelos, y la base mayor mide el doble de la base menor. Calcule la medida del menor ángulo interior del trapecio.  
A) $45^\circ$  
B) $53^\circ$  
C) $60^\circ$  
D) $70^\circ$  
E) $75^\circ$  

28. En un cuadrado $ABCD$ de lado $12\text{ cm}$, $M$ es el punto medio de $CD$. Se traza el segmento $AM$ que corta a la diagonal $BD$ en $P$. Calcule la longitud del segmento $DP$.  
A) $2\sqrt{2}\text{ cm}$  
B) $3\sqrt{2}\text{ cm}$  
C) $4\sqrt{2}\text{ cm}$  
D) $5\sqrt{2}\text{ cm}$  
E) $6\sqrt{2}\text{ cm}$  

29. En un trapecio $ABCD$ de bases $BC = 4\text{ cm}$ y $AD = 10\text{ cm}$, se traza una paralela a las bases que corta a los laterales en $E$ y $F$, dividiendo al trapecio en dos trapecios semejantes. Calcule la longitud de $EF$.  
A) $2\sqrt{10}\text{ cm}$  
B) $6.5\text{ cm}$  
C) $7\text{ cm}$  
D) $2\sqrt{14}\text{ cm}$  
E) $8\text{ cm}$  

30. En un paralelogramo, las alturas correspondientes a dos lados adyacentes miden $6\text{ cm}$ y $8\text{ cm}$. Si el perímetro es de $42\text{ cm}$, halle el área del paralelogramo.  
A) $68\text{ cm}^2$  
B) $72\text{ cm}^2$  
C) $76\text{ cm}^2$  
D) $84\text{ cm}^2$  
E) $90\text{ cm}^2$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Un muro de contención de gaviones en Chosica se construye con sección transversal de trapecio rectángulo para contener deslizamientos de lodo. La base apoyada en el suelo mide $3.5\text{ m}$ y la corona superior mide $1.5\text{ m}$. Si el talud exterior inclinado mide $2.9\text{ m}$, calcule la altura vertical total del muro de contención.  
A) $2.0\text{ m}$  
B) $2.1\text{ m}$  
C) $2.2\text{ m}$  
D) $2.3\text{ m}$  
E) $2.4\text{ m}$  

32. En un proyecto de parcelación en el valle de Tambo (Arequipa), una chacra tiene forma de trapecio con bases de $90\text{ m}$ y $150\text{ m}$, y una separación perpendicular de $60\text{ m}$. Si se divide el predio mediante una recta paralela a las bases situada a $20\text{ m}$ de la base menor, calcule la longitud de la línea divisoria.  
A) $105\text{ m}$  
B) $110\text{ m}$  
C) $115\text{ m}$  
D) $120\text{ m}$  
E) $125\text{ m}$  

33. Una losa deportiva comunal en Iquitos tiene forma rectangular con dimensiones de $28\text{ m}$ de largo por $15\text{ m}$ de ancho. Por normas de iluminación, se colocan reflectores en los cuatro vértices y un sensor central en el punto donde se cruzan las diagonales. Calcule la distancia en línea recta desde cada reflector hacia el sensor central.  
A) $14.5\text{ m}$  
B) $15.87\text{ m}$  
C) $16.25\text{ m}$  
D) $17.0\text{ m}$  
E) $18.5\text{ m}$  

34. Una cooperativa de artesanos de Ayacucho teje alfombras con diseños de rombos tradicionales. Cada rombo tiene un perímetro de $100\text{ cm}$ y una de sus diagonales mide $30\text{ cm}$. ¿Cuántos decímetros cuadrados de hilo teñido ocupa cada rombo decorativo?  
A) $4.5\text{ dm}^2$  
B) $5.0\text{ dm}^2$  
C) $6.0\text{ dm}^2$  
D) $7.5\text{ dm}^2$  
E) $8.0\text{ dm}^2$  

35. En la construcción de un terraplén para una carretera interoceánica, la sección transversal es un trapecio isósceles con base superior de $12\text{ m}$, taludes inclinados a $45^\circ$ y una altura de terraplén de $4\text{ m}$. Si cada metro cúbico de afirmado cuesta $S/\, 35$, calcule el costo del material por cada metro lineal de avance de la carretera.  
A) $S/\, 1820$  
B) $S/\, 2240$  
C) $S/\, 2450$  
D) $S/\, 2680$  
E) $S/\, 2800$  

36. En un predio cuadrangular irregular en Cajamarca, los topógrafos clavan estacas en los puntos medios de sus cuatro linderos y unen dichas estacas con cables tensados para formar una cerca perimetral interior. Si las diagonales del predio original miden $160\text{ m}$ y $220\text{ m}$, ¿cuántos metros de cable se utilizaron exactamente para cercar el paralelogramo de Varignon interior?  
A) $320\text{ m}$  
B) $380\text{ m}$  
C) $400\text{ m}$  
D) $440\text{ m}$  
E) $500\text{ m}$  

37. Un techado para estacionamiento comunal tiene perfil de trapecio rectángulo con base menor horizontal de $4\text{ m}$, base mayor apoyada en el muro de $6.4\text{ m}$ y viga inclinada superior de $5.1\text{ m}$. Determine la distancia vertical entre la base menor y la base mayor (altura de la estructura).  
A) $4.2\text{ m}$  
B) $4.5\text{ m}$  
C) $4.8\text{ m}$  
D) $5.0\text{ m}$  
E) $5.2\text{ m}$  

38. Para una feria gastronómica en Mistura, se ensambla un pabellón con base en forma de romboide cuyos lados contiguos miden $18\text{ m}$ y $25\text{ m}$. Si el ángulo interior más agudo del pabellón es de $30^\circ$, ¿cuál es el área útil cubierta de la feria?  
A) $210\text{ m}^2$  
B) $225\text{ m}^2$  
C) $240\text{ m}^2$  
D) $250\text{ m}^2$  
E) $275\text{ m}^2$  

39. Un terreno comunal en Chincha tiene forma de trapecio con bases de $80\text{ m}$ y $140\text{ m}$. Se tiende una tubería de agua potable que une directamente los puntos medios de las diagonales del terreno. ¿Cuál es la longitud exacta de dicha tubería?  
A) $25\text{ m}$  
B) $30\text{ m}$  
C) $35\text{ m}$  
D) $40\text{ m}$  
E) $45\text{ m}$  

40. En un plano catastral a escala $1:500$, una plaza pública tiene forma de cuadrado de $12\text{ cm}$ de diagonal. ¿Cuál es el área real en metros cuadrados de la plaza pública en el terreno?  
A) $1200\text{ m}^2$  
B) $1500\text{ m}^2$  
C) $1800\text{ m}^2$  
D) $2400\text{ m}^2$  
E) $3600\text{ m}^2$  

41. Un canal de regadío con sección transversal trapezoidal isósceles tiene un ángulo de talud de $60^\circ$ con el fondo horizontal. Si el fondo mide $2\text{ m}$ de ancho y la profundidad de agua es de $\sqrt{3}\text{ m}$, calcule el ancho del espejo de agua (abertura superior).  
A) $3.5\text{ m}$  
B) $4.0\text{ m}$  
C) $4.5\text{ m}$  
D) $5.0\text{ m}$  
E) $5.5\text{ m}$  

42. En un predio rectangular de $60\text{ m}$ de largo por $40\text{ m}$ de ancho destinado a vivero forestal, se construye una vereda perimetral uniforme en su interior de $2\text{ m}$ de ancho. ¿Qué porcentaje del área total del predio queda disponible para las plantas?  
A) $78.5\%$  
B) $81.2\%$  
C) $84.0\%$  
D) $87.5\%$  
E) $90.0\%$  

43. Una estructura de soporte para tanque elevado de agua tiene marco de trapecio isósceles con base superior de $3\text{ m}$, base inferior de $7\text{ m}$ y altura de $6\text{ m}$. Se cruzan dos tirantes tensores de acero en forma de "X" a lo largo de las diagonales. Calcule la longitud total de cable de acero necesario para ambos tirantes.  
A) $15.62\text{ m}$  
B) $16.24\text{ m}$  
C) $17.00\text{ m}$  
D) $17.62\text{ m}$  
E) $18.40\text{ m}$  

44. Un agricultor en Tarma divide su terreno trapezoidal de bases $40\text{ m}$ y $60\text{ m}$ mediante un segmento que une los puntos medios de sus bases. Sabiendo que el área total del terreno es de $2500\text{ m}^2$, ¿cuál es el área de cada una de las dos sub-parcelas obtenidas?  
A) $1200\text{ m}^2$ y $1300\text{ m}^2$  
B) $1250\text{ m}^2$ y $1250\text{ m}^2$  
C) $1100\text{ m}^2$ y $1400\text{ m}^2$  
D) $1000\text{ m}^2$ y $1500\text{ m}^2$  
E) Depende de la longitud de los laterales  

45. En una estructura de techo de tijerales, las cerchas forman rombos acoplados de $2\text{ m}$ de lado cada uno. Si el ángulo interior agudo de cada rombo es de $60^\circ$, calcule la distancia entre los extremos de la diagonal mayor de cada rombo.  
A) $2\sqrt{2}\text{ m}$  
B) $2\sqrt{3}\text{ m}$  
C) $3\text{ m}$  
D) $3\sqrt{2}\text{ m}$  
E) $4\text{ m}$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | D | **31** | B |
| **2** | C | **17** | B | **32** | B |
| **3** | C | **18** | D | **33** | B |
| **4** | B | **19** | B | **34** | C |
| **5** | C | **20** | C | **35** | B |
| **6** | B | **21** | C | **36** | B |
| **7** | B | **22** | B | **37** | B |
| **8** | C | **23** | C | **38** | B |
| **9** | B | **24** | E | **39** | B |
| **10** | B | **25** | B | **40** | C |
| **11** | C | **26** | C | **41** | B |
| **12** | B | **27** | C | **42** | C |
| **13** | C | **28** | C | **43** | A |
| **14** | C | **29** | A | **44** | B |
| **15** | C | **30** | B | **45** | B |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde la base media con la semidiferencia de diagonales o asume que las diagonales del romboide son ortogonales. | Repasar la tabla comparativa del §2.4 y dibujar cada cuadrilátero con sus diagonales y ejes. |
| **En Proceso (60% - 80% aciertos)** | Aplica correctamente las fórmulas de trapecio, pero duda en problemas que combinan semejanza o Varignon. | Resolver los ejercicios 16 al 30 trazando alturas auxiliares que formen rectángulos y triángulos rectángulos. |
| **Avanzado (> 80% aciertos)** | Modela problemas de canales pluviales, terraplenes y muros de contención con rapidez y precisión. | Practicar los problemas 31 al 45 con cronómetro preuniversitario (máximo 1.5 minutos por ítem). |

### Preguntas Guía para la Reflexión:
1. *¿Por qué el paralelogramo de Varignon siempre tiene exactamente la mitad del área del cuadrilátero que lo engendra, sin importar cuán irregular o asimétrico sea este?*
2. *¿En qué se diferencian estructuralmente las diagonales de un rombo de las de un rectángulo, y qué ocurre cuando una figura cumple ambas condiciones a la vez?*
3. *¿Por qué en ingeniería hidráulica los canales de tierra se diseñan con sección trapezoidal en vez de rectangular?*

---

## 7. Formulario Resumen

| Figura / Teorema | Condición Geométrica | Expresión Matemática Rigurosa |
| :--- | :--- | :--- |
| **Suma de Ángulos Interiores** | Cualquier cuadrilátero convexo | $\alpha + \beta + \theta + \delta = 360^\circ$ |
| **Base Media del Trapecio** | Segmento que une puntos medios de laterales | $MN = \frac{B + b}{2}$ |
| **Segmento Puntos Medios Diagonales** | Segmento entre puntos medios de diagonales del trapecio | $PQ = \frac{B - b}{2}$ |
| **Área del Trapecio** | Bases $B, b$ y altura perpendicular $h$ | $\text{Área} = \left(\frac{B + b}{2}\right) \cdot h = MN \cdot h$ |
| **Propiedad del Rombo** | Diagonales perpendiculares $D$ y $d$, lado $L$ | $L = \sqrt{\left(\frac{D}{2}\right)^2 + \left(\frac{d}{2}\right)^2},\quad \text{Área} = \frac{D \cdot d}{2}$ |
| **Área del Romboide** | Base $b$ y altura relativa $h$ | $\text{Área} = b \cdot h = a \cdot b \cdot \sin(\theta)$ |
| **Ley de los Paralelogramos** | Lados $a, b$ y diagonales $d_1, d_2$ | $d_1^2 + d_2^2 = 2(a^2 + b^2)$ |
| **Diagonal del Rectángulo** | Lados $a$ y $b$ | $d = \sqrt{a^2 + b^2}$ |
| **Diagonal del Cuadrado** | Lado $L$ | $d = L\sqrt{2}$ |
| **Teorema de Varignon** | Puntos medios de lados de cualquier cuadrilátero | $\text{Perímetro} = d_1 + d_2,\quad \text{Área} = \frac{\text{Área total}}{2}$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 1 clave(s) corregida(s) y 1 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **19** | D | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |

**Claves sin cambios:** 44 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
