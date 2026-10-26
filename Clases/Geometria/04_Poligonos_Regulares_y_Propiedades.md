# Tema 04: Polígonos Regulares y Propiedades

## 1. Motivación y Contexto Real

Los polígonos regulares son las formas geométricas más simétricas y eficientes del universo físico. En la naturaleza, las abejas construyen sus panales con prismas de base hexagonal regular porque es la figura geométrica que tesela el plano cubriendo la máxima área de almacenamiento de miel con el mínimo gasto perimétrico de cera. Este principio es la base estructural del diseño moderno de fuselajes de aviones, satélites espaciales y chalecos antibalas.

En el Perú y en las aplicaciones prácticas de ingeniería, manufactura y vialidad:
1. **Pernos, Tuercas y Herramientas Mecánicas:** La cabeza de pernos y tuercas estandarizadas es un hexágono regular de $n=6$ lados, lo que permite que una llave mecánica o llave Allen ejerza un par de torsión homogéneo cada $60^\circ$ de giro sin deformar las aristas del metal.
2. **Arquitectura y Teselados:** Desde los pisos de mosaicos en plazas coloniales hasta los muros incaicos donde los bloques poligonales labrados encajan con precisión milimétrica sin mortero (como la célebre piedra de los doce ángulos en Cusco).
3. **Seguridad y Señalización Vial:** El Ministerio de Transportes y Comunicaciones (MTC) estipula señales octogonales regulares para el "PARE", triángulos equiláteros para "CEDA EL PASO" y cuadrados o rombos para prevención, optimizando la visibilidad angular y el reconocimiento instantáneo por parte de conductores a gran velocidad.

```{figure} ../../assets/geometria/poligonos_regulares_propiedades.svg
---
width: 95%
align: center
alt: Elementos y Fórmulas de Polígonos Regulares
---
*Diagrama euclidiano generado en TikZ con el hexágono regular inscrito, apotema ($a_p$), circunradio ($R$), lado ($L_n$) y el compendio analítico de fórmulas métricas y angulares.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Definición y Elementos Fundamentales

Un **polígono regular** es aquel polígono convexo que es simultáneamente **equilátero** (todos sus lados tienen la misma longitud $L_n$) y **equiángulo** (todos sus ángulos interiores tienen la misma medida $\angle_i$).
Todo polígono regular es inscriptible y circunscriptible a dos circunferencias concéntricas.

#### Elementos Clave:
* **Centro ($O$):** Centro común de las circunferencias inscrita y circunscrita.
* **Circunradio ($R$):** Radio de la circunferencia circunscrita (distancia del centro a cualquiera de los vértices).
* **Inradio o Apotema ($a_p$):** Segmento perpendicular trazado desde el centro hacia el punto medio de cualquiera de sus lados (distancia del centro a los lados). Es el radio de la circunferencia inscrita.
* **Lado ($L_n$):** Longitud de cada uno de los $n$ segmentos que forman el contorno perimétrico.
* **Ángulo Central ($\angle_c$):** Ángulo subtendido por un lado desde el centro del polígono.

---

### 2.2 Fórmulas Angulares Universales

Para cualquier polígono convexo de $n$ lados ($n \ge 3$):

1. **Suma de las medidas de los ángulos interiores ($S_i$):**

$$S_i = 180^\circ(n - 2)$$

2. **Medida de un solo ángulo interior en polígono equiángulo o regular ($\angle_i$):**

$$\angle_i = \frac{180^\circ(n - 2)}{n}$$

3. **Suma de las medidas de los ángulos exteriores ($S_e$):**

$$S_e = 360^\circ \quad (\text{constante para todo } n)$$

4. **Medida de un solo ángulo exterior en polígono regular ($\angle_e$):**

$$\angle_e = \frac{360^\circ}{n}$$

5. **Medida del ángulo central en polígono regular ($\angle_c$):**

$$\angle_c = \frac{360^\circ}{n}$$

   *Identidad clave:* $\angle_e = \angle_c$ y $\angle_i + \angle_e = 180^\circ$.

---

### 2.3 Fórmulas de Diagonales

1. **Número de diagonales trazadas desde un solo vértice ($d_1$):**

$$d_1 = n - 3$$

   *(No se puede trazar diagonales hacia sí mismo ni hacia los dos vértices adyacentes).*

2. **Número total de diagonales de un polígono de $n$ lados ($D$):**

$$D = \frac{n(n - 3)}{2}$$

3. **Número de diagonales trazadas desde los primeros $v$ vértices consecutivos ($D_v$):**

$$D_v = v \cdot n - \frac{(v + 1)(v + 2)}{2}$$

---

### 2.4 Polígonos Regulares Notables en Función del Circunradio $R$

| Polígono Regular | N° Lados ($n$) | Lado ($L_n$) | Apotema ($a_p$) | Ángulo Central ($\angle_c$) | Ángulo Interior ($\angle_i$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Triángulo Equilátero** | $3$ | $R\sqrt{3}$ | $\frac{R}{2}$ | $120^\circ$ | $60^\circ$ |
| **Cuadrado** | $4$ | $R\sqrt{2}$ | $\frac{R\sqrt{2}}{2}$ | $90^\circ$ | $90^\circ$ |
| **Pentágono Regular** | $5$ | $\frac{R}{2}\sqrt{10 - 2\sqrt{5}}$ | $\frac{R}{4}(\sqrt{5} + 1)$ | $72^\circ$ | $108^\circ$ |
| **Hexágono Regular** | $6$ | $R$ | $\frac{R\sqrt{3}}{2}$ | $60^\circ$ | $120^\circ$ |
| **Octógono Regular** | $8$ | $R\sqrt{2 - \sqrt{2}}$ | $\frac{R}{2}\sqrt{2 + \sqrt{2}}$ | $45^\circ$ | $135^\circ$ |
| **Decágono Regular** | $10$ | $\frac{R}{2}(\sqrt{5} - 1)$ | $\frac{R}{4}\sqrt{10 + 2\sqrt{5}}$ | $36^\circ$ | $144^\circ$ |
| **Dodecágono Regular** | $12$ | $R\sqrt{2 - \sqrt{3}}$ | $\frac{R}{2}\sqrt{2 + \sqrt{3}}$ | $30^\circ$ | $150^\circ$ |

---

### 2.5 Perímetro y Área de un Polígono Regular

* **Perímetro ($2p$):** Suma de todos sus lados:

$$2p = n \cdot L_n \implies p = \frac{n \cdot L_n}{2} \quad (\text{semiperímetro})$$

* **Área de la Región Poligonal Regular:** Producto del semiperímetro por la apotema:

$$\text{Área} = p \cdot a_p = \frac{n \cdot L_n \cdot a_p}{2}$$

* **Área en función del circunradio y el ángulo central:**

$$\text{Área} = \frac{n}{2} R^2 \sin\left(\frac{360^\circ}{n}\right)$$

---

### 2.6 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Confundir Apotema ($a_p$) con Radio ($R$):**
>    * El *Radio ($R$)* une el centro con un vértice.
>    * La *Apotema ($a_p$)* une el centro con el punto medio de un lado (perpendicular al lado).
>    * Siempre se cumple en el triángulo rectángulo elemental: $a_p^2 + \left(\frac{L_n}{2}\right)^2 = R^2$. Por tanto, $a_p < R$.
> 2. **Olvidar dividir entre 2 en las diagonales:** La fórmula total es $\frac{n(n-3)}{2}$. Olvidar el denominador $2$ duplica el número real de diagonales al contar cada diagonal dos veces (una por cada extremo).
> 3. **Confundir polígono regular con equiángulo:** Un rectángulo es equiángulo pero no regular (no es equilátero). Un rombo es equilátero pero no regular (no es equiángulo). Para ser regular debe cumplir **ambas** condiciones.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Fórmulas y Ángulos)

#### Ejercicio 1
Calcule la suma de los ángulos interiores y el número total de diagonales de un icoságono regular ($20$ lados).

**Análisis Conceptual:**
Se aplica la fórmula de la suma de ángulos interiores $S_i = 180^\circ(n-2)$ y la fórmula del total de diagonales $D = \frac{n(n-3)}{2}$ para $n = 20$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la suma de ángulos interiores con $n = 20$:

$$S_i = 180^\circ(20 - 2) = 180^\circ(18) = 3\,240^\circ$$

**Paso 2:** Calcular el número total de diagonales:

$$D = \frac{20(20 - 3)}{2} = \frac{20(17)}{2} = 10 \cdot 17 = 170$$

**Conclusión:**
La suma de ángulos interiores es $3\,240^\circ$ y el número total de diagonales es $170$.

---

#### Ejercicio 2
La medida de un ángulo interior de un polígono regular es de $144^\circ$. Determine el nombre del polígono y cuántas diagonales posee en total.

**Análisis Conceptual:**
Es más rápido trabajar con el ángulo exterior complementario: $\angle_e = 180^\circ - \angle_i$. Con $\angle_e = \frac{360^\circ}{n}$, se despeja el número de lados $n$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la medida del ángulo exterior:

$$\angle_e = 180^\circ - 144^\circ = 36^\circ$$

**Paso 2:** Despejar el número de lados $n$:

$$\angle_e = \frac{360^\circ}{n} \implies 36^\circ = \frac{360^\circ}{n} \implies n = \frac{360}{36} = 10\text{ lados}$$

El polígono es un **decágono regular**.

**Paso 3:** Calcular el número total de diagonales:

$$D = \frac{10(10 - 3)}{2} = \frac{10(7)}{2} = 35$$

**Conclusión:**
El polígono es un decágono regular y posee $35$ diagonales.

---

#### Ejercicio 3
En una circunferencia de radio $R = 12\text{ cm}$, se encuentra inscrito un hexágono regular. Calcule la longitud de su lado, su apotema y su área.

**Análisis Conceptual:**
En el hexágono regular ($n=6$), el lado es exactamente igual al circunradio ($L_6 = R$) y la apotema es $a_p = \frac{R\sqrt{3}}{2}$.

**Solución Paso a Paso:**

**Paso 1:** Determinar la longitud del lado $L_6$:

$$L_6 = R = 12\text{ cm}$$

**Paso 2:** Calcular la apotema $a_p$:

$$a_p = \frac{R\sqrt{3}}{2} = \frac{12\sqrt{3}}{2} = 6\sqrt{3}\text{ cm}$$

**Paso 3:** Calcular el área del hexágono regular:

$$\text{Perímetro } 2p = 6 \cdot 12 = 72\text{ cm} \implies p = 36\text{ cm}$$

$$\text{Área} = p \cdot a_p = 36 \cdot 6\sqrt{3} = 216\sqrt{3}\text{ cm}^2 \approx 374.12\text{ cm}^2$$

**Conclusión:**
El lado mide $12\text{ cm}$, la apotema mide $6\sqrt{3}\text{ cm}$ y el área es $216\sqrt{3}\text{ cm}^2$.

---

### Nivel 2: Intermedio (Propiedades y Ecuaciones)

#### Ejercicio 4
Si el número de lados de un polígono regular aumenta en $3$, el número de diagonales aumenta en $24$. Calcule la medida del ángulo interior del polígono original.

**Análisis Conceptual:**
Sea $n$ el número de lados del polígono original. Planteamos la ecuación con la fórmula de diagonales para $n$ y $n+3$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la ecuación algebraica de diagonales:

$$D(n+3) - D(n) = 24$$

$$\frac{(n + 3)[(n + 3) - 3]}{2} - \frac{n(n - 3)}{2} = 24$$

$$\frac{(n + 3)(n)}{2} - \frac{n(n - 3)}{2} = 24$$

**Paso 2:** Multiplicar por $2$ y simplificar:

$$(n^2 + 3n) - (n^2 - 3n) = 48$$

$$6n = 48 \implies n = 8\text{ lados}$$

El polígono original es un **octógono regular**.

**Paso 3:** Calcular la medida de su ángulo interior:

$$\angle_i = \frac{180^\circ(8 - 2)}{8} = \frac{180^\circ(6)}{8} = \frac{1080^\circ}{8} = 135^\circ$$

**Conclusión:**
El ángulo interior del polígono original mide $135^\circ$.

---

#### Ejercicio 5
En un polígono regular, la relación entre la medida de un ángulo interior y la medida de su ángulo exterior es de $5$ a $1$. ¿Cuántas diagonales en total tiene dicho polígono?

**Análisis Conceptual:**
Sabemos que $\angle_i + \angle_e = 180^\circ$. Con la razón dada hallamos el ángulo exterior y de allí el número de lados $n$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la proporción:

$$\angle_i = 5k,\quad \angle_e = 1k$$

$$\angle_i + \angle_e = 5k + k = 6k = 180^\circ \implies k = 30^\circ$$

Por tanto: $\angle_e = 30^\circ$.

**Paso 2:** Calcular el número de lados $n$:

$$\angle_e = \frac{360^\circ}{n} \implies 30^\circ = \frac{360^\circ}{n} \implies n = \frac{360}{30} = 12\text{ lados (dodecágono)}$$

**Paso 3:** Calcular el total de diagonales:

$$D = \frac{12(12 - 3)}{2} = \frac{12(9)}{2} = 6 \cdot 9 = 54$$

**Conclusión:**
El polígono tiene $54$ diagonales en total.

---

#### Ejercicio 6
En un triángulo equilátero y un hexágono regular inscritos en la misma circunferencia de radio $R$, determine la razón entre el área del hexágono y el área del triángulo equilátero.

**Análisis Conceptual:**
Un hexágono regular inscrito está compuesto exactamente por $6$ triángulos equiláteros congruentes de lado $R$. El triángulo equilátero inscrito está compuesto por $3$ triángulos iguales a los anteriores (la mitad).

**Solución Paso a Paso:**

**Paso 1:** Calcular el área del triángulo equilátero inscrito en función de $R$:
Lado $L_3 = R\sqrt{3}$.

$$\text{Área}(\triangle) = \frac{L_3^2 \sqrt{3}}{4} = \frac{(R\sqrt{3})^2 \sqrt{3}}{4} = \frac{3R^2 \sqrt{3}}{4}$$

**Paso 2:** Calcular el área del hexágono regular inscrito en función de $R$:
Lado $L_6 = R$. Compuesto por $6$ triángulos equiláteros de lado $R$:

$$\text{Área}(\text{Hexágono}) = 6 \cdot \frac{R^2 \sqrt{3}}{4} = \frac{6R^2 \sqrt{3}}{4}$$

**Paso 3:** Calcular la razón entre ambas áreas:

$$\frac{\text{Área}(\text{Hexágono})}{\text{Área}(\triangle)} = \frac{\frac{6R^2\sqrt{3}}{4}}{\frac{3R^2\sqrt{3}}{4}} = \frac{6}{3} = 2$$

**Conclusión:**
El área del hexágono regular es exactamente el doble ($2$ veces) del área del triángulo equilátero inscrito en la misma circunferencia.

---

#### Ejercicio 7
Calcule el número de diagonales que se pueden trazar desde los primeros $5$ vértices consecutivos en un decágono ($n=10$).

**Análisis Conceptual:**
Se aplica la fórmula para $v$ vértices consecutivos: $D_v = v \cdot n - \frac{(v+1)(v+2)}{2}$, con $n = 10$ y $v = 5$.

**Solución Paso a Paso:**

**Paso 1:** Reemplazar los valores $n = 10$ y $v = 5$:

$$D_5 = 5(10) - \frac{(5 + 1)(5 + 2)}{2}$$

**Paso 2:** Realizar las operaciones:

$$D_5 = 50 - \frac{6 \cdot 7}{2} = 50 - \frac{42}{2} = 50 - 21 = 29$$

**Conclusión:**
Desde los primeros $5$ vértices consecutivos de un decágono se pueden trazar $29$ diagonales.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Diseño de Señalética Vial de Tránsito "PARE")
Una fábrica de señalización vial en Lima manufactura placas metálicas para la señal reglamentaria de "PARE", la cual tiene forma de octógono regular ($n=8$). Por normativa del Ministerio de Transportes y Comunicaciones (MTC), la placa debe inscribirse dentro de un círculo de radio $R = 40\text{ cm}$. Para calcular el costo de la lámina reflectiva roja, determine el perímetro exterior de la señal y el área total de la placa reflectiva. ($\text{use } \sqrt{2} \approx 1.414, \sin(45^\circ) \approx 0.707$).

**Análisis Conceptual:**
En el octógono regular inscrito, el ángulo central es $\angle_c = \frac{360^\circ}{8} = 45^\circ$.
El lado es $L_8 = R\sqrt{2 - \sqrt{2}}$. El área total es $8$ veces el área del triángulo isósceles central: $\text{Área} = \frac{n}{2}R^2 \sin(45^\circ) = 4R^2 \sin(45^\circ) = 4R^2 \frac{\sqrt{2}}{2} = 2\sqrt{2}R^2$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el lado del octógono regular:

$$L_8 = 40 \sqrt{2 - 1.414} = 40 \sqrt{0.586} \approx 40(0.7655) \approx 30.62\text{ cm}$$

**Paso 2:** Calcular el perímetro de la señal ($8$ lados):

$$2p = 8 \cdot L_8 = 8(30.62) \approx 244.96\text{ cm} \approx 2.45\text{ m}$$

**Paso 3:** Calcular el área total del octógono regular:

$$\text{Área} = 2\sqrt{2} R^2 = 2(1.414)(40^2) = 2(1.414)(1600) = 3200(1.414) = 4\,524.8\text{ cm}^2 \approx 0.452\text{ m}^2$$

**Conclusión:**
El perímetro exterior de la señal es de aproximadamente $245\text{ cm}$ ($2.45\text{ m}$) y el área de lámina reflectiva es de aproximadamente $4\,525\text{ cm}^2$ ($0.45\text{ m}^2$).

---

#### Ejercicio 9 (Estructura de Domo Geodésico y Paneles de Abeja en Almacén Minero)
En la ampliación de una planta concentradora en Moquegua, se construye una nave de almacenamiento con cubierta autoportante basada en una celosía de hexágonos regulares de acero. Cada módulo hexagonal tiene una apotema de $a_p = 3\sqrt{3}\text{ m}$. Si el metro cuadrado de policarbonato traslúcido reforzado para la cubierta cuesta $S/\, 80$, determine el costo total de cerramiento para un módulo hexagonal completo.

**Análisis Conceptual:**
En un hexágono regular, $a_p = \frac{R\sqrt{3}}{2}$. Dado $a_p = 3\sqrt{3}\text{ m}$, despejamos el circunradio $R$ (que es igual al lado $L_6$). Con ello se calcula el área y luego el costo total.

**Solución Paso a Paso:**

**Paso 1:** Despejar el radio $R$ (lado $L_6$) a partir de la apotema:

$$\frac{R\sqrt{3}}{2} = 3\sqrt{3} \implies \frac{R}{2} = 3 \implies R = 6\text{ m}$$

Por tanto, el lado del hexágono es $L_6 = 6\text{ m}$.

**Paso 2:** Calcular el semiperímetro $p$:

$$p = \frac{6 \cdot 6}{2} = 18\text{ m}$$

**Paso 3:** Calcular el área del módulo hexagonal:

$$\text{Área} = p \cdot a_p = 18 \cdot (3\sqrt{3}) = 54\sqrt{3}\text{ m}^2 \approx 54(1.732) \approx 93.53\text{ m}^2$$

**Paso 4:** Calcular el costo total de cerramiento:

$$\text{Costo} = 93.53\text{ m}^2 \times S/\, 80 = S/\, 7\,482.40$$

**Conclusión:**
Cada módulo hexagonal tiene un área de $54\sqrt{3}\text{ m}^2 \approx 93.53\text{ m}^2$ y un costo de cerramiento de $S/\, 7\,482.40$.

---

#### Ejercicio 10 (Diseño de una Plaza Central Decagonal en Puno)
La municipalidad provincial de Huancané planifica remodelar su plaza cívica diseñándola como un decágono regular ($n=10$) inscrito en un área circular de radio $R = 20\text{ m}$. La parte central contará con una pileta que coincide con el polígono regular estrellado formado al prolongar los lados del decágono. Calcule la medida del ángulo interior del decágono, el número de diagonales que pueden trazarse en total en la plaza para el tendido de luces aéreas, y la longitud exacta de cada lindero perimétrico de la plaza utilizando la razón áurea ($\phi = \frac{\sqrt{5}+1}{2}$).

**Análisis Conceptual:**
Para $n=10$:
- Ángulo interior: $\angle_i = \frac{180^\circ(10-2)}{10} = 144^\circ$.
- Diagonales totales: $D = \frac{10(7)}{2} = 35$.
- El lado del decágono regular inscrito está ligado a la sección áurea del radio: $L_{10} = \frac{R(\sqrt{5}-1)}{2}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el ángulo interior del decágono:

$$\angle_i = \frac{180^\circ(8)}{10} = 144^\circ$$

**Paso 2:** Calcular el número de diagonales totales (cables de luces):

$$D = \frac{10(10 - 3)}{2} = \frac{10 \cdot 7}{2} = 35\text{ diagonales}$$

**Paso 3:** Calcular la longitud exacta de cada lindero perimétrico ($L_{10}$):

$$L_{10} = \frac{R}{2}(\sqrt{5} - 1) = \frac{20}{2}(\sqrt{5} - 1) = 10(\sqrt{5} - 1)\text{ m}$$

Aproximando con $\sqrt{5} \approx 2.236$:

$$L_{10} \approx 10(1.236) \approx 12.36\text{ m}$$

**Conclusión:**
El ángulo interior mide $144^\circ$, se pueden tender $35$ líneas diagonales de iluminación y cada lindero de la plaza mide $10(\sqrt{5}-1)\text{ m} \approx 12.36\text{ m}$.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. Calcule la suma de los ángulos interiores de un dodecágono ($12$ lados).  
A) $1440^\circ$  
B) $1620^\circ$  
C) $1800^\circ$  
D) $1980^\circ$  
E) $2160^\circ$  

2. ¿Cuántas diagonales en total tiene un octógono convexo ($8$ lados)?  
A) $16$  
B) $18$  
C) $20$  
D) $22$  
E) $24$  

3. ¿Cuánto mide el ángulo exterior de un pentágono regular?  
A) $60^\circ$  
B) $72^\circ$  
C) $80^\circ$  
D) $90^\circ$  
E) $108^\circ$  

4. Si el ángulo interior de un polígono regular mide $120^\circ$, ¿cuántos lados tiene dicho polígono?  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

5. ¿Cuál es el polígono regular cuyo número de diagonales es igual a su número de lados?  
A) Cuadrado  
B) Pentágono  
C) Hexágono  
D) Heptágono  
E) Octógono  

6. En un hexágono regular de lado $10\text{ cm}$, ¿cuál es la longitud de su apotema?  
A) $5\text{ cm}$  
B) $5\sqrt{2}\text{ cm}$  
C) $5\sqrt{3}\text{ cm}$  
D) $10\text{ cm}$  
E) $10\sqrt{3}\text{ cm}$  

7. En un cuadrado inscrito en una circunferencia de radio $8\text{ cm}$, calcule la longitud de su lado.  
A) $8\text{ cm}$  
B) $8\sqrt{2}\text{ cm}$  
C) $16\text{ cm}$  
D) $4\sqrt{2}\text{ cm}$  
E) $12\text{ cm}$  

8. ¿Cuántas diagonales se pueden trazar desde un solo vértice en un nonágono ($9$ lados)?  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

9. La suma de los ángulos exteriores de un polígono de $100$ lados es:  
A) $180^\circ$  
B) $360^\circ$  
C) $720^\circ$  
D) $1800^\circ$  
E) $18000^\circ$  

10. Si el ángulo central de un polígono regular mide $40^\circ$, ¿cuántos lados tiene el polígono?  
A) $8$  
B) $9$  
C) $10$  
D) $12$  
E) $15$  

11. El perímetro de un triángulo equilátero inscrito en una circunferencia de radio $6\text{ cm}$ es:  
A) $12\sqrt{3}\text{ cm}$  
B) $18\text{ cm}$  
C) $18\sqrt{3}\text{ cm}$  
D) $24\sqrt{3}\text{ cm}$  
E) $36\text{ cm}$  

12. ¿Cuál es la suma de los ángulos interiores de un heptágono ($7$ lados)?  
A) $720^\circ$  
B) $900^\circ$  
C) $1080^\circ$  
D) $1260^\circ$  
E) $1440^\circ$  

13. En un polígono regular de $n$ lados, el ángulo interior y el ángulo exterior son siempre:  
A) Complementarios  
B) Suplementarios  
C) Iguales  
D) Conjugados  
E) Rectos  

14. En un decágono regular, ¿cuánto mide su ángulo central?  
A) $30^\circ$  
B) $36^\circ$  
C) $40^\circ$  
D) $45^\circ$  
E) $60^\circ$  

15. Si la apotema de un triángulo equilátero mide $4\text{ cm}$, ¿cuánto mide el circunradio?  
A) $4\text{ cm}$  
B) $6\text{ cm}$  
C) $8\text{ cm}$  
D) $10\text{ cm}$  
E) $12\text{ cm}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. Si a un polígono regular se le aumenta un lado, la suma de sus ángulos interiores aumenta en:  
A) $90^\circ$  
B) $120^\circ$  
C) $180^\circ$  
D) $360^\circ$  
E) $540^\circ$  

17. En un polígono regular, el número de diagonales es igual al triple del número de lados. Calcule la medida del ángulo exterior.  
A) $30^\circ$  
B) $36^\circ$  
C) $40^\circ$  
D) $45^\circ$  
E) $60^\circ$  

18. En un hexágono regular $ABCDEF$, se traza la diagonal $AC$. Si el lado del hexágono mide $6\text{ cm}$, determine la longitud de $AC$.  
A) $6\sqrt{2}\text{ cm}$  
B) $6\sqrt{3}\text{ cm}$  
C) $12\text{ cm}$  
D) $8\sqrt{3}\text{ cm}$  
E) $9\text{ cm}$  

19. Calcule el número de diagonales que se pueden trazar desde los primeros $4$ vértices consecutivos en un octógono regular.  
A) $14$  
B) $15$  
C) $17$  
D) $19$  
E) $20$  

20. En un polígono equiángulo, la medida de un ángulo interior es el quíntuple de la medida de su ángulo exterior. ¿Cuántos lados tiene el polígono?  
A) $10$  
B) $12$  
C) $14$  
D) $15$  
E) $16$  

21. Si la diferencia entre el número de diagonales y el número de vértices de un polígono regular es $18$, ¿cuál es la medida de su ángulo central?  
A) $36^\circ$  
B) $40^\circ$  
C) $45^\circ$  
D) $60^\circ$  
E) $72^\circ$  

22. En un octógono regular $ABCDEFGH$, calcule la medida del ángulo formado por las prolongaciones de los lados $AB$ y $ED$.  
A) $60^\circ$  
B) $75^\circ$  
C) $45^\circ$  
D) $105^\circ$  
E) $120^\circ$  

23. Un hexágono regular y un triángulo equilátero tienen el mismo perímetro de $72\text{ cm}$. Calcule la razón entre el área del hexágono y el área del triángulo.  
A) $1.2$  
B) $1.5$  
C) $1.8$  
D) $2.0$  
E) $2.4$  

24. ¿En qué polígono regular se cumple que la medida de su ángulo interior es el triple de la medida de su ángulo central?  
A) Hexágono  
B) Octógono  
C) Decágono  
D) Dodecágono  
E) Pentadecágono  

25. Calcule el número total de diagonales de un polígono regular si se sabe que la suma de sus ángulos interiores es igual a $14$ ángulos rectos.  
A) $20$  
B) $27$  
C) $35$  
D) $44$  
E) $54$  

26. En un cuadrado de lado $8\text{ cm}$, se unen los puntos medios de sus cuatro lados para formar un nuevo cuadrado, y en este se repite el proceso sucesivamente. ¿Cuál es el área del tercer cuadrado interior formado?  
A) $4\text{ cm}^2$  
B) $8\text{ cm}^2$  
C) $16\text{ cm}^2$  
D) $24\text{ cm}^2$  
E) $32\text{ cm}^2$  

27. Si el número de lados de un polígono disminuye en $2$, el número de diagonales disminuye en $15$. Calcule el número de lados original.  
A) $8$  
B) $9$  
C) $10$  
D) $11$  
E) $12$  

28. En un dodecágono regular ($n=12$), la longitud del lado es $L_{12} = R\sqrt{2 - \sqrt{3}}$. Calcule el área del dodecágono regular en función de su circunradio $R$.  
A) $2R^2$  
B) $3R^2$  
C) $4R^2$  
D) $\frac{3\sqrt{3}}{2}R^2$  
E) $6R^2$  

29. Si se duplica el número de lados de un polígono regular, la medida de su ángulo exterior disminuye en $18^\circ$. ¿Cuántos lados tenía el polígono inicial?  
A) $8$  
B) $10$  
C) $12$  
D) $15$  
E) $20$  

30. En un pentágono regular $ABCDE$, se trazan las diagonales $AC$ y $BD$ que se cortan en $P$. Calcule la medida del ángulo $\angle APB$.  
A) $36^\circ$  
B) $54^\circ$  
C) $72^\circ$  
D) $90^\circ$  
E) $108^\circ$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Un operario de maestranza en Talara fabrica una arandela de fijación con perfil de hexágono regular de $6\text{ cm}$ de lado a la cual se le perfora en el centro un orificio circular de radio $r = 3\text{ cm}$. Calcule el área metálica remanente de la arandela. ($\text{use } \sqrt{3} \approx 1.732, \pi \approx 3.1416$).  
A) $58.26\text{ cm}^2$  
B) $62.48\text{ cm}^2$  
C) $65.25\text{ cm}^2$  
D) $68.12\text{ cm}^2$  
E) $72.50\text{ cm}^2$  

32. En un pabellón ferial en Arequipa, se colocan baldosas con forma de octógonos regulares y cuadrados intercalados para teselar un piso de $120\text{ m}^2$. Si cada octógono regular tiene lado de $0.5\text{ m}$, calcule el área de cada cuadrado de empalme que complementa el teselado perfecto.  
A) $0.20\text{ m}^2$  
B) $0.25\text{ m}^2$  
C) $0.30\text{ m}^2$  
D) $0.35\text{ m}^2$  
E) $0.50\text{ m}^2$  

33. Una antena de radar meteorológico gira barriendo una región circular de radio $R = 10\text{ m}$. El sensor calibra un sistema de alerta temprana cuando detecta nubes convectivas en los vértices de un hexágono regular inscrito en dicha zona. Determine la distancia en línea recta entre dos vértices no consecutivos separados por un vértice intermedio (diagonal intermedia) del hexágono.  
A) $10\text{ m}$  
B) $10\sqrt{2}\text{ m}$  
C) $10\sqrt{3}\text{ m}$  
D) $15\text{ m}$  
E) $20\text{ m}$  

34. Una cooperativa de apicultores en Oxapampa construye marcos con celdas hexagonales regulares de $4\text{ mm}$ de lado. ¿Cuál es la cantidad de celdas completas que se pueden empaquetar en una lámina rectangular de cera estampada de $20\text{ cm}$ de ancho por $40\text{ cm}$ de largo? ($\text{use } \sqrt{3} \approx 1.732$).  
A) $\approx 1\,850$ celdas  
B) $\approx 1\,924$ celdas  
C) $\approx 2\,100$ celdas  
D) $\approx 2\,350$ celdas  
E) $\approx 2\,500$ celdas  

35. Para la iluminación de una glorieta decagonal regular ($10$ lados) en Tacna, se instalan guirnaldas de luces uniendo cada par de postes que no son vecinos inmediatos (todas las diagonales posibles). Si cada tramo de guirnalda cuesta $S/\, 45$, ¿cuál es el presupuesto total en guirnaldas?  
A) $S/\, 1250$  
B) $S/\, 1420$  
C) $S/\, 1575$  
D) $S/\, 1800$  
E) $S/\, 2025$  

36. En una planta de fundición en Chimbote, se diseña una tuerca gigante de acero con cabeza hexagonal regular que debe soportar una llave de torque de $60\text{ mm}$ de abertura entre caras paralelas opuestas (distancia entre caras = $2a_p$). Calcule la longitud del lado de la cabeza hexagonal de dicha tuerca.  
A) $20\sqrt{3}\text{ mm}$  
B) $30\text{ mm}$  
C) $30\sqrt{3}\text{ mm}$  
D) $40\text{ mm}$  
E) $45\text{ mm}$  

37. Un parque ecológico en Tarapoto tiene forma de polígono regular donde la suma de las medidas de sus ángulos interiores es $1800^\circ$. Se traza un sendero perimétrico de $1.2\text{ km}$ en total. ¿Cuál es la longitud de cada lado del parque?  
A) $80\text{ m}$  
B) $90\text{ m}$  
C) $100\text{ m}$  
D) $110\text{ m}$  
E) $120\text{ m}$  

38. Se diseña un espejo astronómico segmentado compuesto por $18$ espejos planos hexagonales regulares idénticos. Si el radio de la circunferencia circunscrita a cada espejo individual es de $0.5\text{ m}$, calcule el área colectora total de los $18$ segmentos del espejo.  
A) $6.75\sqrt{3}\text{ m}^2$  
B) $11.25\sqrt{3}\text{ m}^2$  
C) $13.5\sqrt{3}\text{ m}^2$  
D) $15\sqrt{3}\text{ m}^2$  
E) $18\sqrt{3}\text{ m}^2$  

39. En un polígono regular de $n$ lados, se observa que al trazar todas las diagonales desde $3$ vértices consecutivos se obtienen $25$ diagonales. Calcule el área de dicho polígono regular si su circunradio mide $10\text{ cm}$.  
A) $200\text{ cm}^2$  
B) $240\text{ cm}^2$  
C) $280\text{ cm}^2$  
D) $300\text{ cm}^2$  
E) $320\text{ cm}^2$  

40. Una señalización de tránsito en forma de triángulo equilátero está inscrita en el mismo círculo metálico que una señal en forma de cuadrado. Si el lado de la señal cuadrada mide $40\text{ cm}$, ¿cuánto mide el lado de la señal triangular?  
A) $20\sqrt{6}\text{ cm}$  
B) $30\sqrt{3}\text{ cm}$  
C) $40\sqrt{3}\text{ cm}$  
D) $20\sqrt{3}\text{ cm}$  
E) $45\text{ cm}$  

41. En un polígono regular de $15$ lados (pentadecágono), ¿cuál es la medida del menor ángulo que forman las diagonales trazadas desde un mismo vértice hacia los extremos de un lado opuesto?  
A) $12^\circ$  
B) $15^\circ$  
C) $18^\circ$  
D) $24^\circ$  
E) $30^\circ$  

42. En la cubierta de un biohuerto en el Cusco, se arma una estructura piramidal cuya base es un dodecágono regular ($12$ lados) inscrito en un círculo de radio $R = 6\text{ m}$. Calcule el área exacta de la base del biohuerto.  
A) $72\text{ m}^2$  
B) $96\text{ m}^2$  
C) $108\text{ m}^2$  
D) $120\text{ m}^2$  
E) $144\text{ m}^2$  

43. Para un proyecto de energía solar en Moquegua, un panel fotovoltaico tiene la forma de un octógono regular obtenido al cortar cuatro esquinas triangulares isósceles de un cuadrado de plancha de aluminio de $2\text{ m}$ de lado. Calcule la longitud de los catetos de cada esquina recortada.  
A) $2 - \sqrt{2}\text{ m}$  
B) $\sqrt{2} - 1\text{ m}$  
C) $\frac{\sqrt{2}}{2}\text{ m}$  
D) $2 - 2\sqrt{2}\text{ m}$  
E) $\frac{2 - \sqrt{2}}{2}\text{ m}$  

44. En un vivero comunal, un reservorio de agua tiene forma de prisma recto cuya base es un hexágono regular de $4\text{ m}$ de lado y altura de $3\text{ m}$. Calcule la capacidad máxima en litros de agua que puede almacenar el reservorio. ($\text{use } \sqrt{3} \approx 1.732, 1\text{ m}^3 = 1000\text{ L}$).  
A) $118\,200\text{ L}$  
B) $124\,704\text{ L}$  
C) $132\,500\text{ L}$  
D) $144\,000\text{ L}$  
E) $156\,800\text{ L}$  

45. Una pieza mecánica de acople de alta precisión es un engranaje con forma de nonágono regular ($9$ lados). Si la distancia entre el centro de giro y cualquiera de sus vértices es de $50\text{ mm}$, calcule el número total de pares de vértices no adyacentes que se pueden conectar para verificar tolerancias dimensionales con calibrador micrométrico.  
A) $20$  
B) $24$  
C) $27$  
D) $30$  
E) $36$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | C | **31** | C |
| **2** | C | **17** | C | **32** | B |
| **3** | B | **18** | B | **33** | C |
| **4** | B | **19** | C | **34** | B |
| **5** | B | **20** | B | **35** | C |
| **6** | C | **21** | C | **36** | A |
| **7** | B | **22** | C | **37** | C |
| **8** | B | **23** | B | **38** | A |
| **9** | B | **24** | B | **39** | D |
| **10** | B | **25** | B | **40** | A |
| **11** | C | **26** | B | **41** | A |
| **12** | B | **27** | C | **42** | C |
| **13** | B | **28** | B | **43** | A |
| **14** | B | **29** | B | **44** | B |
| **15** | C | **30** | C | **45** | C |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde la apotema con el radio o no recuerda las fórmulas angulares básicas. | Practicar con el triángulo rectángulo central: $a_p^2 + (L_n/2)^2 = R^2$ y deducir las fórmulas dibujando los polígonos. |
| **En Proceso (60% - 80% aciertos)** | Resuelve problemas directos de diagonales y ángulos, pero duda en polígonos notables con raíces ($L_8, L_{12}$). | Revisar la tabla de polígonos notables del §2.4 y resolver paso a paso los ejercicios 16 al 30. |
| **Avanzado (> 80% aciertos)** | Domina el cálculo de áreas regulares, teselados de pisos, tolerancias mecánicas y modelamiento en Beca 18. | Resolver los problemas 31 al 45 con límite estricto de 1.5 minutos por problema sin calculadora. |

### Preguntas Guía para la Reflexión:
1. *¿Por qué el hexágono regular es el único polígono regular cuyo lado mide exactamente igual a su circunradio ($L_6 = R$)?*
2. *¿Por qué solo el triángulo equilátero, el cuadrado y el hexágono regular pueden teselar por sí solos el plano sin dejar huecos ni traslaparse?*
3. *¿Cómo influye la relación $\angle_i + \angle_e = 180^\circ$ para simplificar cálculos algebraicos de polígonos con muchos lados?*

---

## 7. Formulario Resumen

| Propiedad / Parámetro | Condición del Polígono | Expresión Matemática Rigurosa |
| :--- | :--- | :--- |
| **Suma Ángulos Interiores** | Polígono convexo de $n$ lados | $S_i = 180^\circ(n - 2)$ |
| **Ángulo Interior** | Polígono regular o equiángulo | $\angle_i = \frac{180^\circ(n - 2)}{n}$ |
| **Suma Ángulos Exteriores** | Cualquier polígono convexo | $S_e = 360^\circ$ |
| **Ángulo Exterior / Central** | Polígono regular | $\angle_e = \angle_c = \frac{360^\circ}{n}$ |
| **Relación Suplementaria** | Ángulo interior y exterior | $\angle_i + \angle_e = 180^\circ$ |
| **Diagonales desde 1 Vértice** | Vértices no adyacentes | $d_1 = n - 3$ |
| **Total de Diagonales** | Segmentos entre vértices no consecutivos | $D = \frac{n(n - 3)}{2}$ |
| **Diagonales de $v$ Vértices** | Primeros $v$ vértices consecutivos | $D_v = v \cdot n - \frac{(v+1)(v+2)}{2}$ |
| **Relación Pitagórica Central** | Radio $R$, apotema $a_p$ y lado $L_n$ | $a_p^2 + \left(\frac{L_n}{2}\right)^2 = R^2$ |
| **Área Poligonal Regular** | Semiperímetro $p$ y apotema $a_p$ | $\text{Área} = p \cdot a_p = \frac{n \cdot L_n \cdot a_p}{2}$ |
| **Lado Triángulo Equilátero** | Circunradio $R$ | $L_3 = R\sqrt{3},\quad a_p = \frac{R}{2}$ |
| **Lado Cuadrado Regular** | Circunradio $R$ | $L_4 = R\sqrt{2},\quad a_p = \frac{R\sqrt{2}}{2}$ |
| **Lado Hexágono Regular** | Circunradio $R$ | $L_6 = R,\quad a_p = \frac{R\sqrt{3}}{2}$ |
| **Área Hexágono Regular** | Lado $L$ o circunradio $R$ | $\text{Área} = \frac{3\sqrt{3}}{2}R^2$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 2 clave(s) corregida(s) y 5 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **22** | C | C | Corregida | Se ajustó la opción C: las prolongaciones de $AB$ y $ED$ difieren en dos giros de $45^\circ$, por lo que forman $45^\circ$. |
| **26** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **33** | C | C | Corregida | Se eliminó la contradicción «opuestos»: la diagonal intermedia de un hexágono de radio $10$ m mide $R\sqrt{3}=10\sqrt{3}$ m (C). |
| **38** | C | A | Corregida | Se ajustó la opción A: cada hexágono mide $\frac{3\sqrt{3}}{2}(0.5)^2$ y los $18$ suman $6.75\sqrt{3}\text{ m}^2$. |
| **39** | D | D | Corregida | Se corrigió el dato a $25$ diagonales: $3n-11=25 \Rightarrow n=12$ y el área es $\frac{12}{2}(10)^2\sin 30^\circ=300\text{ cm}^2$ (D). |

**Claves sin cambios:** 43 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
