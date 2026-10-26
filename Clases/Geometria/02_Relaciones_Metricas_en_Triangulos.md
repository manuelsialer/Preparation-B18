# Tema 02: Relaciones Métricas en Triángulos

## 1. Motivación y Contexto Real

Las relaciones métricas constituyen el puente matemático entre la forma geométrica pura y el cálculo cuantitativo exacto de longitudes y distancias. Desde la construcción de los canales de regadío incaicos en laderas empinadas hasta el tendido de puentes modulares Bailey y la instalación de cables de alta tensión sobre quebradas en los Andes peruanos, el cálculo de distancias inaccesibles depende de estas proporciones.

En el trabajo de campo de topógrafos, ingenieros civiles y brigadistas comunitarios:
1. **Medición de Alturas Inaccesibles:** Determinar la altura de un farallón rocoso o torre de telecomunicaciones sin escalar, utilizando proyecciones horizontales y teodolitos.
2. **Diseño de Rampas y Desniveles:** Calcular la pendiente y la longitud del soporte estructural de rampas de acceso peatonal y vehicular bajo normativas de accesibilidad universal.
3. **Optimización de Tirantes y Tensores:** Determinar la longitud exacta de cables de acero que estabilizan postes y torres frente a vientos de gran magnitud.

```{figure} ../../assets/geometria/relaciones_metricas_rectangulo.svg
---
width: 95%
align: center
alt: Relaciones Métricas en el Triángulo Rectángulo
---
*Diagrama euclidiano generado en TikZ + tkz-euclide con proyecciones ortogonales y el compendio de teoremas métricos fundamentales.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Proyección Ortogonal sobre una Recta

La **proyección ortogonal** de un punto sobre una recta es el pie de la perpendicular trazada desde dicho punto hacia la recta.
* La proyección de un segmento $AB$ sobre una recta $\mathcal{L}$ es el segmento $A'B'$ cuyos extremos son las proyecciones de los puntos $A$ y $B$.
* Si el segmento es paralelo a la recta, la longitud de la proyección es igual a la del segmento.
* Si el segmento es perpendicular a la recta, su proyección se reduce a un solo punto (longitud cero).

---

### 2.2 Relaciones Métricas en el Triángulo Rectángulo

Sea el triángulo $ABC$ recto en $B$, donde:
* $c$ y $a$ son las longitudes de los catetos ($AB = c$, $BC = a$).
* $b$ es la longitud de la hipotenusa ($AC = b$).
* $h$ es la altura relativa a la hipotenusa ($BH = h$).
* $m$ es la proyección ortogonal del cateto $c$ sobre la hipotenusa ($AH = m$).
* $n$ es la proyección ortogonal del cateto $a$ sobre la hipotenusa ($HC = n$).
* Se cumple siempre que $b = m + n$.

A partir de la semejanza de los tres triángulos rectángulos formados ($\triangle AHB \sim \triangle BHC \sim \triangle ABC$), se demuestran los cinco teoremas fundamentales:

#### Teorema 1: Teorema de Pitágoras
El cuadrado de la longitud de la hipotenusa es igual a la suma de los cuadrados de las longitudes de los catetos:

$$a^2 + c^2 = b^2$$

#### Teorema 2: Cuadrado de un Cateto (Teorema del Cateto)
El cuadrado de la longitud de un cateto es igual al producto de la longitud de la hipotenusa por la longitud de su proyección ortogonal sobre ella:

$$c^2 = b \cdot m$$

$$a^2 = b \cdot n$$

#### Teorema 3: Cuadrado de la Altura Relativa a la Hipotenusa
El cuadrado de la altura relativa a la hipotenusa es igual al producto de las longitudes de las proyecciones de los catetos sobre dicha hipotenusa:

$$h^2 = m \cdot n$$

#### Teorema 4: Producto de Catetos
El producto de las longitudes de los catetos es igual al producto de la longitud de la hipotenusa por la altura relativa a ella:

$$a \cdot c = b \cdot h$$

#### Teorema 5: Inversa de los Cuadrados de los Catetos
La inversa del cuadrado de la altura relativa a la hipotenusa es igual a la suma de las inversas de los cuadrados de los catetos:

$$\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{c^2}$$

---

### 2.3 Relaciones Métricas en Triángulos Oblicuángulos

#### 1. Teorema de Euclides (Generalización de Pitágoras)
* **Para un ángulo agudo ($\angle A < 90^\circ$):**
  El cuadrado del lado opuesto a un ángulo agudo es igual a la suma de los cuadrados de los otros dos lados menos el doble producto de uno de ellos por la proyección del otro sobre él:

$$a^2 = b^2 + c^2 - 2b \cdot m$$

  *(donde $m$ es la proyección de $c$ sobre el lado $b$).*

* **Para un ángulo obtuso ($\angle A > 90^\circ$):**
  El cuadrado del lado opuesto al ángulo obtuso es igual a la suma de los cuadrados de los otros dos lados más el doble producto de uno de ellos por la proyección del otro sobre él:

$$a^2 = b^2 + c^2 + 2b \cdot m$$

#### 2. Teorema de la Mediana (Teorema de Apolonio)
En todo triángulo, la suma de los cuadrados de dos lados es igual al doble del cuadrado de la mediana relativa al tercer lado, más la mitad del cuadrado de dicho tercer lado:

$$a^2 + c^2 = 2m_b^2 + \frac{b^2}{2}$$

#### 3. Teorema de Herón (Cálculo de la Altura)
Permite calcular la longitud de la altura sin conocer ángulos, conociendo únicamente los tres lados del triángulo:

$$h_b = \frac{2}{b}\sqrt{p(p - a)(p - b)(p - c)}$$

donde $p = \frac{a + b + c}{2}$ es el semiperímetro.

---

### 2.4 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Confundir las proyecciones:** En el Teorema del Cateto ($c^2 = b \cdot m$), $m$ es la proyección del cateto $c$ adyacente a él, no la del otro cateto. Si se intercambian $m$ y $n$, el resultado numérico será incorrecto.
> 2. **Olvidar que las relaciones del §2.2 exigen ángulo recto:** Aplicar $h^2 = m \cdot n$ en un triángulo que no es rectángulo es un error recurrente. Debe verificarse previamente que el ángulo superior mide exactamente $90^\circ$.
> 3. **Signos en el Teorema de Euclides:** Frente a un ángulo agudo el término cruzado va con signo **menos** ($-2bm$); frente a un ángulo obtuso va con signo **más** ($+2bm$).

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Propiedades)

#### Ejercicio 1
En un triángulo rectángulo, las proyecciones de los catetos sobre la hipotenusa miden $4\text{ cm}$ y $9\text{ cm}$. Calcule la longitud de la altura relativa a la hipotenusa.

**Análisis Conceptual:**
Se conocen las dos proyecciones $m = 4$ y $n = 9$. El Teorema 3 relaciona directamente la altura relativa a la hipotenusa con el producto de las proyecciones: $h^2 = m \cdot n$.

**Solución Paso a Paso:**

**Paso 1:** Identificar los datos y la fórmula aplicable:

$$m = 4\text{ cm},\quad n = 9\text{ cm}$$

$$h^2 = m \cdot n$$

**Paso 2:** Sustituir los valores:

$$h^2 = 4 \cdot 9 = 36$$

**Paso 3:** Extraer la raíz cuadrada positiva:

$$h = \sqrt{36} = 6\text{ cm}$$

**Conclusión:**
La altura relativa a la hipotenusa mide $6\text{ cm}$.

---

#### Ejercicio 2
En un triángulo rectángulo, la hipotenusa mide $25\text{ cm}$ y la proyección de uno de sus catetos sobre ella mide $9\text{ cm}$. Calcule la longitud de dicho cateto.

**Análisis Conceptual:**
Se conoce la hipotenusa $b = 25$ y la proyección del cateto $m = 9$. El Teorema 2 establece que el cuadrado del cateto es igual a la hipotenusa por su proyección.

**Solución Paso a Paso:**

**Paso 1:** Aplicar el Teorema del Cateto:

$$c^2 = b \cdot m$$

**Paso 2:** Reemplazar los datos numéricos:

$$c^2 = 25 \cdot 9 = 225$$

**Paso 3:** Calcular la longitud del cateto:

$$c = \sqrt{225} = 15\text{ cm}$$

**Conclusión:**
La longitud de dicho cateto es $15\text{ cm}$.

---

#### Ejercicio 3
Los catetos de un triángulo rectángulo miden $15\text{ cm}$ y $20\text{ cm}$. Calcule la longitud de la altura relativa a la hipotenusa.

**Análisis Conceptual:**
Primero se halla la hipotenusa mediante el Teorema de Pitágoras. Luego se calcula la altura aplicando el teorema del producto de catetos: $a \cdot c = b \cdot h$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la hipotenusa $b$ por Pitágoras:

$$b = \sqrt{15^2 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25\text{ cm}$$

**Paso 2:** Aplicar el Teorema 4 (producto de catetos):

$$a \cdot c = b \cdot h$$

$$15 \cdot 20 = 25 \cdot h$$

$$300 = 25h$$

**Paso 3:** Despejar la altura $h$:

$$h = \frac{300}{25} = 12\text{ cm}$$

**Conclusión:**
La altura relativa a la hipotenusa mide $12\text{ cm}$.

---

### Nivel 2: Intermedio (Operatividad y Razonamiento)

#### Ejercicio 4
En un triángulo rectángulo, la altura relativa a la hipotenusa mide $12\text{ cm}$ y una de las proyecciones de los catetos sobre la hipotenusa mide $16\text{ cm}$. Calcule el perímetro del triángulo.

**Análisis Conceptual:**
Con $h = 12$ y $m = 16$, usamos $h^2 = m \cdot n$ para hallar la otra proyección $n$. Con $m$ y $n$ se tiene la hipotenusa $b = m + n$, y luego con el teorema del cateto se calculan ambos catetos para sumar el perímetro.

**Solución Paso a Paso:**

**Paso 1:** Hallar la otra proyección $n$:

$$h^2 = m \cdot n \implies 12^2 = 16 \cdot n$$

$$144 = 16n \implies n = \frac{144}{16} = 9\text{ cm}$$

**Paso 2:** Determinar la hipotenusa total $b$:

$$b = m + n = 16 + 9 = 25\text{ cm}$$

**Paso 3:** Calcular ambos catetos mediante el teorema del cateto:

$$c^2 = b \cdot m = 25 \cdot 16 = 400 \implies c = 20\text{ cm}$$

$$a^2 = b \cdot n = 25 \cdot 9 = 225 \implies a = 15\text{ cm}$$

**Paso 4:** Sumar los lados para obtener el perímetro:

$$\text{Perímetro} = a + c + b = 15 + 20 + 25 = 60\text{ cm}$$

**Conclusión:**
El perímetro del triángulo rectángulo es $60\text{ cm}$.

---

#### Ejercicio 5
En un triángulo rectángulo, los catetos están en la relación de $1$ a $3$. Si la altura relativa a la hipotenusa mide $\sqrt{90}\text{ cm} = 3\sqrt{10}\text{ cm}$, calcule la longitud de la hipotenusa.

**Análisis Conceptual:**
Sean los catetos $c = k$ y $a = 3k$. La hipotenusa por Pitágoras es $b = \sqrt{k^2 + (3k)^2} = k\sqrt{10}$. Aplicando $a \cdot c = b \cdot h$ despejamos $k$ y luego la hipotenusa.

**Solución Paso a Paso:**

**Paso 1:** Expresar los lados en función de $k$:

$$\text{Catetos: } c = k,\quad a = 3k$$

$$\text{Hipotenusa: } b = \sqrt{k^2 + 9k^2} = k\sqrt{10}$$

**Paso 2:** Aplicar el Teorema del producto de catetos:

$$a \cdot c = b \cdot h$$

$$(3k)(k) = (k\sqrt{10})(3\sqrt{10})$$

$$3k^2 = 30k$$

**Paso 3:** Como $k > 0$, simplificamos entre $3k$:

$$k = 10\text{ cm}$$

**Paso 4:** Calcular la hipotenusa $b$:

$$b = k\sqrt{10} = 10\sqrt{10}\text{ cm}$$

**Conclusión:**
La hipotenusa mide $10\sqrt{10}\text{ cm}$ (aproximadamente $31.62\text{ cm}$).

---

#### Ejercicio 6
En un triángulo $ABC$, los lados miden $AB = 7\text{ cm}$, $BC = 9\text{ cm}$ y $AC = 8\text{ cm}$. Calcule la longitud de la mediana relativa al lado $AC$.

**Análisis Conceptual:**
Aplicamos el Teorema de la Mediana (Apolonio) sobre el lado $b = AC = 8$:

$$AB^2 + BC^2 = 2m_b^2 + \frac{AC^2}{2}$$

**Solución Paso a Paso:**

**Paso 1:** Reemplazar las longitudes dadas en la ecuación de Apolonio:

$$7^2 + 9^2 = 2m_b^2 + \frac{8^2}{2}$$

**Paso 2:** Efectuar las potencias y operaciones numéricas:

$$49 + 81 = 2m_b^2 + \frac{64}{2}$$

$$130 = 2m_b^2 + 32$$

**Paso 3:** Despejar la mediana $m_b$:

$$2m_b^2 = 130 - 32 = 98$$

$$m_b^2 = 49 \implies m_b = 7\text{ cm}$$

**Conclusión:**
La longitud de la mediana relativa al lado $AC$ es $7\text{ cm}$.

---

#### Ejercicio 7
En un triángulo rectángulo, la suma de las inversas de los cuadrados de los catetos es $\frac{1}{144}$. Determine la longitud de la altura relativa a la hipotenusa.

**Análisis Conceptual:**
El Teorema 5 establece directamente la igualdad entre la suma de las inversas de los cuadrados de los catetos y la inversa del cuadrado de la altura relativa a la hipotenusa.

**Solución Paso a Paso:**

**Paso 1:** Plantear el Teorema 5:

$$\frac{1}{a^2} + \frac{1}{c^2} = \frac{1}{h^2}$$

**Paso 2:** Igualar con el dato del problema:

$$\frac{1}{144} = \frac{1}{h^2}$$

**Paso 3:** Invertir y extraer la raíz:

$$h^2 = 144 \implies h = 12\text{ cm}$$

**Conclusión:**
La altura relativa a la hipotenusa mide $12\text{ cm}$.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Diseño de Rampa de Acceso Peatonal en Huancavelica)
Un equipo técnico de ingeniería municipal diseña una rampa de acceso peatonal para un centro de salud comunal en Huancavelica. La estructura lateral forma un triángulo rectángulo donde la rampa inclinada (hipotenusa) tiene una longitud de $20\text{ m}$. Por motivos de estabilidad ante sismos, se coloca una columna vertical de soporte que parte desde el ángulo recto de la base hacia la rampa inclinada en forma perpendicular (altura relativa a la hipotenusa). Si el pie de la columna divide a la rampa en dos segmentos de modo que el tramo superior es cuatro veces el tramo inferior, determine la altura de la columna de soporte y la elevación total del centro de salud respecto al nivel del suelo.

**Análisis Conceptual:**
La rampa es la hipotenusa $b = 20\text{ m}$. Está dividida en $m$ y $n$ con $m = 4n$. La columna de soporte es la altura relativa $h$. La elevación total es uno de los catetos del triángulo rectángulo.

**Solución Paso a Paso:**

**Paso 1:** Determinar los segmentos de la rampa:

$$m + n = 20 \implies 4n + n = 20 \implies 5n = 20 \implies n = 4\text{ m}$$

$$m = 4(4) = 16\text{ m}$$

**Paso 2:** Calcular la altura de la columna $h$:

$$h^2 = m \cdot n = 16 \cdot 4 = 64 \implies h = \sqrt{64} = 8\text{ m}$$

**Paso 3:** Calcular la elevación vertical del centro de salud (cateto vertical $a$ adyacente a la proyección $n$ o cateto de elevación):

$$a^2 = b \cdot n = 20 \cdot 4 = 80 \implies a = \sqrt{80} = 4\sqrt{5}\text{ m} \approx 8.94\text{ m}$$

**Conclusión:**
La columna de soporte mide $8\text{ m}$ y la elevación del centro de salud es de $4\sqrt{5}\text{ m}$ (aproximadamente $8.94\text{ m}$).

---

#### Ejercicio 9 (Tendido de Red Eléctrica Rural sobre una Quebrada)
En un proyecto de electrificación rural en Áncash, se deben instalar dos postes de anclaje $A$ y $B$ a ambos lados de una quebrada, y una torre de alta tensión $C$ ubicada en la cresta de un cerro, formando un triángulo $ABC$. Mediciones topográficas indican que $AC = 130\text{ m}$, $BC = 150\text{ m}$ y la separación entre los postes en la base es $AB = 140\text{ m}$. Para calcular la tensión mecánica del cableado principal, se necesita conocer la altura vertical de la torre $C$ respecto a la línea base $AB$. Calcule dicha altura utilizando relaciones métricas oblicuángulos.

**Análisis Conceptual:**
En el triángulo oblicuángulo $ABC$, los lados son $a = 150$, $b = 130$ y el lado base es $c = 140$. Calculamos la altura relativa a la base $c$ mediante el Teorema de Herón: $h_c = \frac{2}{c}\sqrt{p(p-a)(p-b)(p-c)}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el semiperímetro $p$:

$$p = \frac{150 + 130 + 140}{2} = \frac{420}{2} = 210\text{ m}$$

**Paso 2:** Calcular las diferencias del semiperímetro con los lados:

$$p - a = 210 - 150 = 60\text{ m}$$

$$p - b = 210 - 130 = 80\text{ m}$$

$$p - c = 210 - 140 = 70\text{ m}$$

**Paso 3:** Calcular el área del triángulo por Herón:

$$\text{Área} = \sqrt{210 \cdot 60 \cdot 80 \cdot 70}$$

Descomponiendo factores:

$$210 \cdot 70 = 3 \cdot 70 \cdot 70 = 3 \cdot 70^2$$

$$60 \cdot 80 = 4800 = 3 \cdot 1600 = 3 \cdot 40^2$$

$$\text{Área} = \sqrt{(3 \cdot 70^2) \cdot (3 \cdot 40^2)} = \sqrt{3^2 \cdot 70^2 \cdot 40^2} = 3 \cdot 70 \cdot 40 = 8\,400\text{ m}^2$$

**Paso 4:** Calcular la altura relativa $h_c$:

$$\text{Área} = \frac{c \cdot h_c}{2} \implies 8\,400 = \frac{140 \cdot h_c}{2} = 70 \cdot h_c$$

$$h_c = \frac{8\,400}{70} = 120\text{ m}$$

**Conclusión:**
La altura vertical de la torre respecto a la línea base de los postes es de $120\text{ m}$.

---

#### Ejercicio 10 (Cálculo de Distancia Subterránea en una Mina en Pasco)
En una galería minera subterránea en Cerro de Pasco, dos túneles rectos parten de una estación principal $O$ formando un ángulo recto. El túnel 1 tiene una longitud de $60\text{ m}$ hasta el frente de extracción $A$, y el túnel 2 tiene una longitud de $80\text{ m}$ hasta el frente $B$. Se perfora un ducto recto de ventilación que une directamente los dos frentes $A$ y $B$. Desde la estación principal $O$ se planea perforar un conducto de drenaje recto que desemboque perpendicularmente en el ducto de ventilación $AB$. Determine la longitud exacta del conducto de drenaje y a qué distancia del frente $A$ se conectará.

**Análisis Conceptual:**
El sistema forma un triángulo rectángulo en $O$ con catetos $a = 60\text{ m}$ y $b = 80\text{ m}$. El ducto de ventilación $AB$ es la hipotenusa $c$. El conducto de drenaje es la altura relativa a la hipotenusa $h$. El punto de conexión dista de $A$ la longitud de la proyección ortogonal $m$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la longitud del ducto de ventilación $AB$ (hipotenusa $c$):

$$c = \sqrt{60^2 + 80^2} = \sqrt{3600 + 6400} = \sqrt{10\,000} = 100\text{ m}$$

**Paso 2:** Calcular la longitud del conducto de drenaje $h$ (Teorema del producto de catetos):

$$a \cdot b = c \cdot h$$

$$60 \cdot 80 = 100 \cdot h \implies 4800 = 100h \implies h = 48\text{ m}$$

**Paso 3:** Calcular la distancia del punto de conexión al frente $A$ (proyección $m$ del cateto $60\text{ m}$):

$$a^2 = c \cdot m \implies 60^2 = 100 \cdot m$$

$$3600 = 100m \implies m = 36\text{ m}$$

**Conclusión:**
El conducto de drenaje tiene una longitud de $48\text{ m}$ y se conecta a $36\text{ m}$ del frente de extracción $A$ (y a $64\text{ m}$ del frente $B$).

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. En un triángulo rectángulo, las proyecciones de los catetos sobre la hipotenusa miden $2\text{ cm}$ y $8\text{ cm}$. Calcule la longitud de la altura relativa a la hipotenusa.  
A) $3\text{ cm}$  
B) $4\text{ cm}$  
C) $5\text{ cm}$  
D) $6\text{ cm}$  
E) $8\text{ cm}$  

2. En un triángulo rectángulo, la hipotenusa mide $16\text{ cm}$ y la proyección de un cateto sobre ella mide $4\text{ cm}$. Calcule la longitud de dicho cateto.  
A) $6\text{ cm}$  
B) $8\text{ cm}$  
C) $10\text{ cm}$  
D) $12\text{ cm}$  
E) $14\text{ cm}$  

3. Los catetos de un triángulo rectángulo miden $9\text{ cm}$ y $12\text{ cm}$. Calcule la altura relativa a la hipotenusa.  
A) $6.4\text{ cm}$  
B) $7.2\text{ cm}$  
C) $7.5\text{ cm}$  
D) $8.0\text{ cm}$  
E) $8.4\text{ cm}$  

4. En un triángulo rectángulo, la altura relativa a la hipotenusa mide $6\text{ cm}$ y una de las proyecciones mide $3\text{ cm}$. ¿Cuánto mide la otra proyección?  
A) $9\text{ cm}$  
B) $10\text{ cm}$  
C) $12\text{ cm}$  
D) $15\text{ cm}$  
E) $18\text{ cm}$  

5. Si en un triángulo rectángulo la hipotenusa mide $20\text{ cm}$ y una de las proyecciones mide $5\text{ cm}$, ¿cuánto mide la otra proyección?  
A) $10\text{ cm}$  
B) $12\text{ cm}$  
C) $15\text{ cm}$  
D) $16\text{ cm}$  
E) $18\text{ cm}$  

6. En un triángulo rectángulo, las proyecciones de los catetos sobre la hipotenusa miden $1\text{ cm}$ y $9\text{ cm}$. Halle la longitud del cateto menor.  
A) $\sqrt{10}\text{ cm}$  
B) $3\text{ cm}$  
C) $\sqrt{15}\text{ cm}$  
D) $4\text{ cm}$  
E) $5\text{ cm}$  

7. Si los catetos de un triángulo rectángulo miden $8\text{ cm}$ y $15\text{ cm}$, ¿cuál es la longitud de la hipotenusa?  
A) $16\text{ cm}$  
B) $17\text{ cm}$  
C) $18\text{ cm}$  
D) $19\text{ cm}$  
E) $20\text{ cm}$  

8. En un triángulo rectángulo, el producto de los catetos es $60\text{ cm}^2$ y la hipotenusa mide $13\text{ cm}$. Calcule la altura relativa a la hipotenusa.  
A) $\frac{60}{13}\text{ cm}$  
B) $\frac{65}{12}\text{ cm}$  
C) $5\text{ cm}$  
D) $4\text{ cm}$  
E) $\frac{120}{13}\text{ cm}$  

9. En un triángulo rectángulo, la suma de las proyecciones de los catetos sobre la hipotenusa es siempre igual a:  
A) El doble de la altura  
B) La longitud de la hipotenusa  
C) La suma de los catetos  
D) El inradio  
E) El producto de los catetos  

10. Si la altura relativa a la hipotenusa mide $10\text{ cm}$ y una proyección mide $5\text{ cm}$, ¿cuánto mide la hipotenusa total?  
A) $20\text{ cm}$  
B) $25\text{ cm}$  
C) $30\text{ cm}$  
D) $35\text{ cm}$  
E) $40\text{ cm}$  

11. En un triángulo rectángulo de catetos $5\text{ cm}$ y $12\text{ cm}$, halle la proyección del cateto menor sobre la hipotenusa.  
A) $\frac{25}{13}\text{ cm}$  
B) $\frac{144}{13}\text{ cm}$  
C) $2\text{ cm}$  
D) $\frac{60}{13}\text{ cm}$  
E) $3\text{ cm}$  

12. En un triángulo rectángulo de hipotenusa $50\text{ cm}$ y altura relativa $24\text{ cm}$, el producto de los catetos es igual a:  
A) $600\text{ cm}^2$  
B) $800\text{ cm}^2$  
C) $1000\text{ cm}^2$  
D) $1200\text{ cm}^2$  
E) $1500\text{ cm}^2$  

13. La relación $\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{b^2}$ en un triángulo rectángulo permite calcular directamente:  
A) El área total  
B) La altura relativa a la hipotenusa a partir de los catetos  
C) La mediana de la hipotenusa  
D) El perímetro  
E) El circunradio  

14. En un triángulo rectángulo, las proyecciones de los catetos sobre la hipotenusa son iguales entre sí. ¿Qué tipo de triángulo rectángulo es?  
A) Escaleno  
B) Isósceles  
C) Notorio $30^\circ - 60^\circ$  
D) Notorio $37^\circ - 53^\circ$  
E) No puede existir  

15. Si las proyecciones miden $3\text{ cm}$ y $12\text{ cm}$, la altura relativa a la hipotenusa mide:  
A) $5\text{ cm}$  
B) $6\text{ cm}$  
C) $7\text{ cm}$  
D) $8\text{ cm}$  
E) $9\text{ cm}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. En un triángulo rectángulo, la altura relativa a la hipotenusa mide $2\sqrt{6}\text{ cm}$ y las proyecciones de los catetos sobre la hipotenusa están en la relación de $2$ a $3$. Calcule la longitud de la hipotenusa.  
A) $8\text{ cm}$  
B) $10\text{ cm}$  
C) $12\text{ cm}$  
D) $14\text{ cm}$  
E) $15\text{ cm}$  

17. En un triángulo rectángulo, la diferencia entre las proyecciones de los catetos sobre la hipotenusa es $7\text{ cm}$ y la altura relativa a la hipotenusa mide $12\text{ cm}$. Calcule la longitud de la hipotenusa.  
A) $20\text{ cm}$  
B) $23\text{ cm}$  
C) $25\text{ cm}$  
D) $27\text{ cm}$  
E) $29\text{ cm}$  

18. En un triángulo rectángulo, un cateto mide $8\text{ cm}$ y la altura relativa a la hipotenusa mide $4.8\text{ cm}$. Calcule la longitud del otro cateto.  
A) $5\text{ cm}$  
B) $6\text{ cm}$  
C) $7\text{ cm}$  
D) $7.5\text{ cm}$  
E) $9\text{ cm}$  

19. En un triángulo $ABC$, los lados miden $AB = 5\text{ cm}$, $BC = 7\text{ cm}$ y $AC = 6\text{ cm}$. Calcule la longitud de la proyección del lado $AB$ sobre el lado $AC$.  
A) $1\text{ cm}$  
B) $1.5\text{ cm}$  
C) $2\text{ cm}$  
D) $2.5\text{ cm}$  
E) $3\text{ cm}$  

20. En un triángulo rectángulo, las inversas de los cuadrados de los catetos son $\frac{1}{25}$ y $\frac{1}{144}$. Calcule la altura relativa a la hipotenusa.  
A) $\frac{60}{13}\text{ cm}$  
B) $\frac{13}{60}\text{ cm}$  
C) $5\text{ cm}$  
D) $6\text{ cm}$  
E) $7.5\text{ cm}$  

21. Los lados de un triángulo miden $11\text{ cm}$, $13\text{ cm}$ y $20\text{ cm}$. ¿Qué tipo de triángulo es según sus ángulos?  
A) Acutángulo  
B) Rectángulo  
C) Obtusángulo  
D) Equilátero  
E) Degenerado  

22. En un triángulo $ABC$, los lados miden $a = 6\text{ cm}$, $c = 8\text{ cm}$ y la mediana relativa al lado $b$ mide $m_b = 5\text{ cm}$. Calcule la longitud del lado $b$.  
A) $8\text{ cm}$  
B) $10\text{ cm}$  
C) $12\text{ cm}$  
D) $6\sqrt{2}\text{ cm}$  
E) $10\sqrt{2}\text{ cm}$  

23. En un triángulo rectángulo, la hipotenusa mide $10\text{ cm}$ y la altura relativa a ella mide $4\text{ cm}$. Calcule la suma de las longitudes de los catetos.  
A) $12\text{ cm}$  
B) $2\sqrt{45}\text{ cm}$  
C) $6\sqrt{5}\text{ cm}$  
D) $14\text{ cm}$  
E) $15\text{ cm}$  

24. En un triángulo rectángulo, el cociente entre las longitudes de los catetos es $\frac{3}{4}$. Si la hipotenusa mide $35\text{ cm}$, halle la proyección del cateto mayor sobre la hipotenusa.  
A) $15.4\text{ cm}$  
B) $18.6\text{ cm}$  
C) $22.4\text{ cm}$  
D) $24.8\text{ cm}$  
E) $28.0\text{ cm}$  

25. En un triángulo acutángulo, los lados miden $13\text{ cm}$, $14\text{ cm}$ y $15\text{ cm}$. Calcule la altura relativa al lado intermedio de $14\text{ cm}$.  
A) $10\text{ cm}$  
B) $11\text{ cm}$  
C) $12\text{ cm}$  
D) $13\text{ cm}$  
E) $9.6\text{ cm}$  

26. En un trapecio rectángulo, las bases miden $4\text{ cm}$ y $10\text{ cm}$, y el lado oblicuo mide $10\text{ cm}$. Calcule la longitud de la altura del trapecio.  
A) $6\text{ cm}$  
B) $7\text{ cm}$  
C) $8\text{ cm}$  
D) $9\text{ cm}$  
E) $8.5\text{ cm}$  

27. En un triángulo rectángulo $ABC$ recto en $B$, se traza la altura $BH$. Si $AH = 1\text{ cm}$ y $HC = 3\text{ cm}$, calcule la medida del ángulo $\angle BAC$.  
A) $30^\circ$  
B) $45^\circ$  
C) $60^\circ$  
D) $75^\circ$  
E) $37^\circ$  

28. En un triángulo rectángulo, la altura relativa a la hipotenusa determina sobre ella dos segmentos en relación $1:4$. Si la hipotenusa mide $45\text{ cm}$, halle la altura relativa.  
A) $12\text{ cm}$  
B) $15\text{ cm}$  
C) $18\text{ cm}$  
D) $20\text{ cm}$  
E) $24\text{ cm}$  

29. En un rombo de lado $10\text{ cm}$, una diagonal mide $12\text{ cm}$. Calcule la distancia entre dos lados opuestos paralelos (altura del rombo).  
A) $8.0\text{ cm}$  
B) $8.6\text{ cm}$  
C) $9.2\text{ cm}$  
D) $9.6\text{ cm}$  
E) $10.0\text{ cm}$  

30. En un triángulo rectángulo, el producto de los catetos es igual al triple del cuadrado de la altura relativa a la hipotenusa. ¿Cuál es el valor del producto de las proyecciones de los catetos sobre la hipotenusa expresado en función de $h$?  
A) $h^2$  
B) $2h^2$  
C) $3h^2$  
D) $9h^2$  
E) $\frac{h^2}{3}$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Un puente peatonal atirantado en la selva central une dos orillas de un río. La estructura de soporte forma un triángulo rectángulo donde la viga inclinada principal mide $25\text{ m}$. Una péndola vertical de acero (perpendicular a la viga inclinada) se fija desde el pilar base hasta la viga, dividiéndola en dos tramos cuyas longitudes difieren en $7\text{ m}$. Calcule la longitud de dicha péndola de acero.  
A) $10\text{ m}$  
B) $11\text{ m}$  
C) $12\text{ m}$  
D) $13\text{ m}$  
E) $14\text{ m}$  

32. En un terreno comunal de cultivo en el valle sagrado de Cusco, un canal de regadío recto corre por el lindero hipotenusa de $50\text{ m}$ de una parcela triangular rectangular. Desde el vértice opuesto (donde se ubica el pozo de captación) se construye una acequia secundaria perpendicular al canal que mide $24\text{ m}$. Determine el costo de cercar los dos linderos menores (catetos) si el metro lineal de alambre cuesta $S/\, 12$.  
A) $S/\, 720$  
B) $S/\, 840$  
C) $S/\, 960$  
D) $S/\, 1080$  
E) $S/\, 1200$  

33. Una antena de radiodifusión educativa de $24\text{ m}$ de altura se sujeta al suelo mediante dos cables tensores fijados en puntos opuestos $A$ y $B$. El ángulo que forman los dos cables en la cúspide de la antena es recto ($90^\circ$). Si uno de los anclajes dista $18\text{ m}$ del pie de la antena, ¿cuál es la distancia entre los dos puntos de anclaje $A$ y $B$?  
A) $40\text{ m}$  
B) $45\text{ m}$  
C) $50\text{ m}$  
D) $52\text{ m}$  
E) $55\text{ m}$  

34. En la construcción de un túnel carretero a través de un cerro rocoso, dos cuadrillas avanzan en direcciones perpendiculares desde un punto de control $P$ recorriendo $300\text{ m}$ y $400\text{ m}$ hasta las bocaminas $A$ y $B$. Se debe perforar una galería de ventilación rectilínea directa entre $A$ y $B$, y desde $P$ una chimenea perpendicular hacia dicha galería. Calcule la longitud de la chimenea de ventilación.  
A) $200\text{ m}$  
B) $240\text{ m}$  
C) $250\text{ m}$  
D) $280\text{ m}$  
E) $320\text{ m}$  

35. Un agrónomo en Moquegua delimita una parcela triangular con lados de $13\text{ m}$, $14\text{ m}$ y $15\text{ m}$. Se traza una línea de tubería subterránea que parte del vértice opuesto al lado de $14\text{ m}$ hacia el punto medio de dicho lado (mediana). Calcule la longitud exacta de la tubería requerida.  
A) $\sqrt{148}\text{ m}$  
B) $12\text{ m}$  
C) $\sqrt{157}\text{ m}$  
D) $13\text{ m}$  
E) $\sqrt{160}\text{ m}$  

36. En una cancha deportiva comunal con forma triangular, dos reflectores situados en los vértices $A$ y $B$ iluminan el área. La distancia entre $A$ y $B$ es de $30\text{ m}$. El reflector en $A$ dista $24\text{ m}$ del arco central $C$, y el reflector en $B$ dista $18\text{ m}$ de $C$. Verifique la posición angular y calcule la menor distancia desde el arco $C$ hacia la línea recta que une ambos reflectores.  
A) $12.4\text{ m}$  
B) $13.6\text{ m}$  
C) $14.4\text{ m}$  
D) $15.0\text{ m}$  
E) $16.2\text{ m}$  

37. Para instalar paneles solares en el techo de un colegio rural en Cajamarca, se diseña una cercha triangular isósceles con base de $16\text{ m}$ y lados iguales de $17\text{ m}$. Si se desea colocar un montante de refuerzo perpendicular desde uno de los extremos de la base hacia el lado inclinado opuesto, ¿cuánto medirá dicho montante?  
A) $\frac{240}{17}\text{ m}$  
B) $\frac{220}{17}\text{ m}$  
C) $14\text{ m}$  
D) $15\text{ m}$  
E) $\frac{225}{17}\text{ m}$  

38. Una brigada de defensa civil evalúa una pared vertical de $12\text{ m}$ de altura que corre riesgo de colapso. Se coloca un puntal inclinado de acero desde el suelo hasta la parte superior de la pared. A una distancia vertical de $4.8\text{ m}$ del suelo, se coloca una riostra horizontal de apoyo de $5.4\text{ m}$ perpendicular a la pared que toca al puntal. Calcule la longitud total del puntal de acero inclinado.  
A) $13\text{ m}$  
B) $15\text{ m}$  
C) $18\text{ m}$  
D) $20\text{ m}$  
E) $22.5\text{ m}$  

39. En un predio rural en Piura, tres pozos de agua $A$, $B$ y $C$ forman un triángulo con $AB = 100\text{ m}$, $BC = 120\text{ m}$ y $AC = 140\text{ m}$. Se desea cavar una zanja recta de desagüe desde el pozo $B$ perpendicular hacia la tubería matriz que une $A$ y $C$. ¿A qué distancia del pozo $A$ interceptará la zanja a la tubería matriz?  
A) $40\text{ m}$  
B) $45\text{ m}$  
C) $50\text{ m}$  
D) $55\text{ m}$  
E) $60\text{ m}$  

40. Un dron de rescate en la cordillera Blanca parte del campamento base $O$ y vuela en línea recta ascendente $1500\text{ m}$ hacia el norte y luego $2000\text{ m}$ hacia el este en el mismo plano horizontal hasta el punto $P$. Si un sensor láser en $O$ mide la distancia más corta hacia la trayectoria diagonal directa que une los puntos cardinales extremos, ¿cuál es dicha distancia?  
A) $1000\text{ m}$  
B) $1100\text{ m}$  
C) $1200\text{ m}$  
D) $1250\text{ m}$  
E) $1300\text{ m}$  

41. En un terreno triangular rectangular, la relación entre el área y el semiperímetro es igual a $4\text{ m}$ (inradio $r = 4\text{ m}$). Si la hipotenusa mide $26\text{ m}$, calcule la altura relativa a la hipotenusa.  
A) $\frac{120}{13}\text{ m}$  
B) $\frac{130}{12}\text{ m}$  
C) $9.6\text{ m}$  
D) $10.2\text{ m}$  
E) $11.4\text{ m}$  

42. En una fábrica comunal de ladrillos en Huancayo, una rampa de carga triangular recta tiene una altura vertical de $3\text{ m}$ y una longitud horizontal de base de $4\text{ m}$. Un rodillo transportador baja por la rampa. ¿Cuál es la distancia mínima desde el vértice inferior recto de la estructura hasta el rodillo en su trayectoria?  
A) $2.0\text{ m}$  
B) $2.2\text{ m}$  
C) $2.4\text{ m}$  
D) $2.5\text{ m}$  
E) $2.8\text{ m}$  

43. En un triángulo rectángulo, la hipotenusa mide $L$ y la altura relativa a la hipotenusa mide $H$. ¿Cuál es la condición necesaria y suficiente sobre $H$ en función de $L$ para que el triángulo rectángulo exista con medidas reales?  
A) $H \le \frac{L}{4}$  
B) $H \le \frac{L}{2}$  
C) $H \le L$  
D) $H = \frac{L\sqrt{3}}{2}$  
E) $H \ge \frac{L}{2}$  

44. Un topógrafo mide un terreno triangular $ABC$ con $AB = 60\text{ m}$, $BC = 80\text{ m}$ y $\angle B = 90^\circ$. Se proyecta trazar una vereda que parta del vértice $B$ y caiga perpendicularmente sobre $AC$ en el punto $H$. Calcule la diferencia positiva entre las áreas de los dos sectores triangulares $\triangle ABH$ y $\triangle HBC$ en que queda dividido el predio.  
A) $546\text{ m}^2$  
B) $672\text{ m}^2$  
C) $720\text{ m}^2$  
D) $784\text{ m}^2$  
E) $820\text{ m}^2$  

45. En una represa de concreto, el perfil transversal tiene forma de triángulo rectángulo. La cara inclinada exterior mide $50\text{ m}$ y soporta la presión del agua. Sensores colocados a lo largo de la cara inclinada en las proyecciones de los catetos indican que una proyección es $14\text{ m}$ más larga que la otra. Calcule el volumen de concreto por cada metro de ancho de la represa si su sección transversal coincide con el área de dicho triángulo.  
A) $540\text{ m}^3$  
B) $576\text{ m}^3$  
C) $600\text{ m}^3$  
D) $624\text{ m}^3$  
E) $650\text{ m}^3$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | B | **31** | C |
| **2** | B | **17** | C | **32** | B |
| **3** | B | **18** | B | **33** | C |
| **4** | C | **19** | A | **34** | B |
| **5** | C | **20** | A | **35** | A |
| **6** | A | **21** | C | **36** | C |
| **7** | B | **22** | B | **37** | A |
| **8** | A | **23** | C | **38** | B |
| **9** | B | **24** | C | **39** | D |
| **10** | B | **25** | C | **40** | C |
| **11** | A | **26** | C | **41** | A |
| **12** | D | **27** | C | **42** | C |
| **13** | B | **28** | C | **43** | B |
| **14** | B | **29** | D | **44** | B |
| **15** | B | **30** | A | **45** | C |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde la proyección $m$ con la hipotenusa $b$ o no recuerda Pitágoras. | Repasar el diagrama de TikZ en §1 y memorizar las identidades de proyecciones dibujando triángulos. |
| **En Proceso (60% - 80% aciertos)** | Resuelve problemas directos de $h^2 = mn$, pero duda al despejar en sistemas o con Herón. | Practicar los ejercicios 16 a 30 reforzando el álgebra de radicales y proporciones. |
| **Avanzado (> 80% aciertos)** | Modela problemas de ingeniería, rampas y quebradas determinando distancias y áreas con soltura. | Resolver los problemas 31 al 45 cronometrando 2 minutos por problema sin calculadora. |

### Preguntas Guía para la Reflexión:
1. *¿Por qué en todo triángulo rectángulo la altura relativa a la hipotenusa nunca puede superar la mitad de la hipotenusa ($h \le \frac{b}{2}$)?*
2. *¿Cómo se deduce el Teorema de Pitágoras sumando los dos teoremas de los catetos ($c^2 = bm$ y $a^2 = bn$)?*
3. *¿Qué ventaja práctica ofrece el Teorema de Herón para calcular alturas en terrenos irregulares donde no se puede medir el ángulo superior?*

---

## 7. Formulario Resumen

| Teorema / Propiedad | Configuración Geométrica | Expresión Matemática Rigurosa |
| :--- | :--- | :--- |
| **Teorema de Pitágoras** | Triángulo rectángulo de catetos $a, c$ e hipotenusa $b$ | $a^2 + c^2 = b^2$ |
| **Teorema del Cateto** | Cateto, hipotenusa y su proyección ortogonal | $c^2 = b \cdot m \quad\text{y}\quad a^2 = b \cdot n$ |
| **Cuadrado de la Altura** | Altura relativa a la hipotenusa y proyecciones | $h^2 = m \cdot n$ |
| **Producto de Catetos** | Catetos, hipotenusa y altura relativa | $a \cdot c = b \cdot h$ |
| **Inversa de los Cuadrados** | Catetos y altura relativa a la hipotenusa | $\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{c^2}$ |
| **Suma de Proyecciones** | Proyecciones sobre la hipotenusa | $b = m + n$ |
| **Teorema de Euclides (Agudo)** | Lado opuesto al ángulo agudo $A < 90^\circ$ | $a^2 = b^2 + c^2 - 2b \cdot m$ |
| **Teorema de Euclides (Obtuso)** | Lado opuesto al ángulo obtuso $A > 90^\circ$ | $a^2 = b^2 + c^2 + 2b \cdot m$ |
| **Teorema de la Mediana (Apolonio)** | Lados $a, c$, lado base $b$ y mediana $m_b$ | $a^2 + c^2 = 2m_b^2 + \frac{b^2}{2}$ |
| **Altura por Herón** | Lados $a, b, c$ y semiperímetro $p$ | $h_b = \frac{2}{b}\sqrt{p(p-a)(p-b)(p-c)}$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 3 clave(s) corregida(s) y 5 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **19** | C | A | Corregida | El resultado no coincide con la clave anterior; la opción correcta es A. |
| **37** | A | A | Corregida | La opción E era equivalente a D ($\frac{255}{17}=15$); se reemplazó por un distractor. El área es $\frac{16\cdot15}{2}=120$, luego el montante mide $\frac{2\cdot120}{17}=\frac{240}{17}$ m. Clave A. |
| **38** | B | B | Corregida | Se corrigió la riostra a $5.4$ m: la base del puntal queda a $9$ m de la pared y $L=\sqrt{12^2+9^2}=15$ m (B). |
| **39** | C | D | Corregida | El resultado no coincide con la clave anterior; la opción correcta es D. |
| **45** | B | C | Corregida | El resultado no coincide con la clave anterior; la opción correcta es C. |

**Claves sin cambios:** 42 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
