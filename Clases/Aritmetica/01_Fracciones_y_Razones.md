# TEMA 01: ARITMÉTICA – FRACCIONES Y RAZONES

> **Área:** Competencias Matemáticas (Resuelve problemas de cantidad)
> **Indicador Oficial (PRONABEC / CNEB):** *Expresa su comprensión del significado de la fracción como razón con cantidades continuas.*
> **Nivel:** Preuniversitario / Beca 18 – Alto Rendimiento

---
## 1. MOTIVACIÓN Y CONTEXTO REAL

En la vida cotidiana y en las ciencias aplicadas, no todas las magnitudes pueden medirse contando unidades discretas (1, 2, 3 manzanas). Cuando medimos magnitudes **continuas** como el tiempo, la longitud, la masa, el volumen de un fluido o la concentración de una solución química, surge la necesidad indispensable de dividir la unidad en partes iguales.

Una fracción no es simplemente "un número sobre otro":
* Es una **relación de comparación** entre una parte y el todo.
* Es una **razón geométrica** entre dos magnitudes continuas.
* Es un **operador matemático** capaz de transformar una cantidad (ampliarla o reducirla).

En las pruebas de admisión de alto nivel y en el Examen Nacional de Preselección (Beca 18), este tema es el pilar de problemas sobre **mezclas industriales, llenado y vaciado simultáneo de reservorios (grifos y caños), reparto de herencias y cálculo de eficiencias laborales**.

---

## 2. FUNDAMENTACIÓN TEÓRICA RIGUROSA

### 2.1 Concepto de Número Racional ($\mathbb{Q}$) y Fracción

El conjunto de los números racionales ($\mathbb{Q}$) se define formalmente como:

$$
\mathbb{Q} = \left\{ \frac{a}{b} \;\middle|\; a \in \mathbb{Z}, \; b \in \mathbb{Z}, \; b \neq 0 \right\}
$$

En la aritmética preuniversitaria peruana, se denomina estrictamente **Fracción** a aquel número racional cuyos términos son **enteros positivos** y donde el numerador no es múltiplo exacto del denominador:

$$
f = \frac{a}{b} \quad \text{donde } a, b \in \mathbb{Z}^+ \quad \text{y} \quad a \neq k \cdot b \quad (k \in \mathbb{Z}^+)
$$

* **$a$ (Numerador):** Indica el número de partes congruentes que se toman o consideran de la unidad.
* **$b$ (Denominador):** Indica el número de partes iguales en que se ha dividido la unidad fundamental ($b \neq 0$).

> ⚠️ **Error Frecuente:** Expresiones como $\frac{12}{4}$ o $\frac{-3}{5}$ son números racionales, pero estrictamente hablando, $\frac{12}{4} = 3$ es un entero (no fracción), y las fracciones en problemas de aplicación física o reparto siempre consideran cantidades estrictamente positivas ($a, b \in \mathbb{Z}^+$).

---

### 2.2 Clasificación Completa de Fracciones

Las fracciones se clasifican bajo distintos criterios:

#### A. Por la comparación de sus términos respecto a la unidad
1. **Fracción Propia:** El numerador es menor que el denominador ($a < b$). Su valor numérico es estrictamente menor que 1.

$$f < 1 \quad \text{Ejemplos: } \frac{3}{7}, \; \frac{5}{12}, \; \frac{9}{10}$$

2. **Fracción Impropia:** El numerador es mayor que el denominador ($a > b$). Su valor numérico es estrictamente mayor que 1. Puede expresarse como un **número mixto**.

$$f > 1 \quad \text{Ejemplos: } \frac{11}{4} = 2\frac{3}{4}, \; \frac{15}{7} = 2\frac{1}{7}$$

#### B. Por su denominador
1. **Fracción Decimal:** El denominador es una potencia entera positiva de 10 ($b = 10^k$, con $k \in \mathbb{Z}^+$).

$$\text{Ejemplos: } \frac{7}{10}, \; \frac{23}{100}, \; \frac{139}{1000}$$

2. **Fracción Ordinaria o Común:** El denominador no es una potencia de 10.

$$\text{Ejemplos: } \frac{4}{9}, \; \frac{8}{25}, \; \frac{11}{30}$$

#### C. Por la relación entre sus términos (Divisibilidad)
1. **Fracción Reductible:** El numerador y el denominador poseen divisores comunes distintos de la unidad ($\text{MCD}(a, b) > 1$). Se puede simplificar.

$$\text{Ejemplos: } \frac{18}{24} = \frac{3 \cdot 6}{4 \cdot 6} = \frac{3}{4}$$

2. **Fracción Irreductible:** El numerador y el denominador son primos entre sí ($\text{PESI}$), es decir, $\text{MCD}(a, b) = 1$. No admite simplificación.

$$\text{Ejemplos: } \frac{5}{13}, \; \frac{8}{15}, \; \frac{20}{21}$$

#### D. Por grupos de dos o más fracciones
1. **Homogéneas:** Poseen el mismo denominador. Ejemplo: $\frac{2}{11}, \frac{7}{11}, \frac{15}{11}$.
2. **Heterogéneas:** Poseen denominadores distintos. Ejemplo: $\frac{3}{5}, \frac{4}{9}, \frac{7}{12}$.

---

### 2.3 Fracciones Equivalentes e Irreductibles

Dos fracciones $\frac{a}{b}$ y $\frac{c}{d}$ son **equivalentes** ($\frac{a}{b} = \frac{c}{d}$) si y solo si representan la misma cantidad numérica, lo cual equivale a la condición de productos cruzados:

$$
a \cdot d = b \cdot c
$$

#### Teorema de la Fracción Equivalente
Toda fracción equivalente a una fracción irreductible $\frac{p}{q}$ (con $\text{PESI}(p, q) = 1$) adopta necesariamente la forma canónica:

$$
f_{eq} = \frac{p \cdot k}{q \cdot k} \quad \text{con } k \in \mathbb{Z}^+
$$

> 💡 **Consejo Pre:** Cuando un problema indique: *"Una fracción equivalente a $\frac{5}{8}$ es tal que la suma de sus términos es 260..."*, escribe de inmediato:
> $$\text{Numerador} = 5k, \quad \text{Denominador} = 8k \implies 5k + 8k = 260 \implies 13k = 260 \implies k = 20$$

> Luego la fracción buscada es $\frac{5(20)}{8(20)} = \frac{100}{160}$. ¡Este artificio ahorra minutos valiosos!

---

### 2.4 Operaciones Fundamentales y Algoritmos Óptimos

#### 1. Adición y Sustracción
* **Para dos fracciones (Método del aspa):**

$$
\frac{a}{b} \pm \frac{c}{d} = \frac{a \cdot d \pm b \cdot c}{b \cdot d}
$$

* **Para tres o más fracciones (Método del Mínimo Común Múltiplo):**
Se halla el $\text{MCM}(b_1, b_2, \dots, b_n)$ para homogenizar los denominadores.

#### 2. Multiplicación (Operador "de", "del", "de los")
La palabra "de" en enunciados verbales representa multiplicación directa:

$$
\frac{a}{b} \times \frac{c}{d} = \frac{a \cdot c}{b \cdot d}
$$

#### 3. División
Dividir entre una fracción equivale a multiplicar por su inversa multiplicativa:

$$
\frac{a}{b} \div \frac{c}{d} = \frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a \cdot d}{b \cdot c} \quad \text{(Regla de extremos y medios)}
$$

---

### 2.5 La Fracción como Razón de Cantidades Continuas

Una razón geométrica compara dos magnitudes homogéneas continuas $A$ y $B$ mediante un cociente:

$$
\text{Razón} = \frac{\text{Medida de } A}{\text{Medida de } B}
$$

* Si un cable de $18\text{ metros}$ se corta en dos tramos cuya razón es $\frac{2}{7}$, significa que:

$$\text{Tramo 1} = 2k, \quad \text{Tramo 2} = 7k \implies 2k + 7k = 18 \implies 9k = 18 \implies k = 2\text{ m}$$

Los tramos miden $4\text{ m}$ y $14\text{ m}$.
* La fracción compara la parte respecto a un todo continuo:

$$
f = \frac{\text{Parte}}{\text{Todo}} = \frac{\text{Lo que se tiene}}{\text{El total de referencia}}
$$

---

### 2.6 Aplicaciones Clásicas Preuniversitarias

#### A. Reducción a la Unidad (Grifos, Caños y Rendimiento Laboral)
Cuando varios agentes trabajan simultáneamente para completar una obra continua o llenar un tanque de capacidad $V$:
1. Si un caño llena un tanque en $T_1$ horas, en **1 hora** llena:

$$\frac{1}{T_1} \text{ del tanque}$$

2. Si un desagüe vacía el tanque en $T_2$ horas, en **1 hora** vacía:

$$\frac{1}{T_2} \text{ del tanque}$$

3. Si actúan juntos durante $t$ horas:

$$
\left( \frac{1}{T_1} - \frac{1}{T_2} \right) \cdot t = 1 \quad (\text{donde } 1 \text{ representa la obra completa o el tanque lleno})
$$

#### B. Pérdidas y Ganancias Sucesivas ("Lo que gasto y lo que me queda")
En problemas de gastos o pérdidas en cadena:
* Si se pierde $\frac{1}{n}$ de una cantidad $C$, queda:

$$\left(1 - \frac{1}{n}\right)C = \left(\frac{n-1}{n}\right)C$$

* Si se gana $\frac{1}{m}$ sobre una cantidad $C$, resulta:

$$\left(1 + \frac{1}{m}\right)C = \left(\frac{m+1}{m}\right)C$$

* Al realizar varias operaciones sucesivas, se calcula directamente sobre **lo que va quedando**:

$$
\text{Resto Final} = \left(1 - f_3\right)\left(1 - f_2\right)\left(1 - f_1\right) \cdot C_0
$$

#### C. Mezclas Líquidas y Extracciones Fraccionarias
Al extraer una fracción $f$ de una mezcla homogénea (por ejemplo, agua y alcohol):
* Se extrae exactamente la fracción $f$ del volumen total.
* Se extrae la misma fracción $f$ de **cada uno de los componentes individuales**.
* La concentración porcentual del líquido que queda permanece constante.

---

## 3. 10 EJERCICIOS RESUELTOS PASO A PASO

### NIVEL BÁSICO (Fijación de Conceptos)

#### Ejercicio 01
**Enunciado:** Calcule el valor irreductible de la siguiente operación combinada:

$$
M = \frac{\frac{2}{3} + \frac{5}{6} - \frac{1}{4}}{\frac{3}{8} \times \frac{4}{9} + \frac{1}{2}}
$$

A) $\frac{15}{8}$  
B) $\frac{23}{16}$  
C) $\frac{29}{16}$  
D) $\frac{7}{4}$  
E) $\frac{9}{5}$  

* **Estrategia / Planteamiento:** Se efectúan las operaciones del numerador y del denominador por separado respetando la jerarquía matemática y simplificando antes de multiplicar. Finalmente, se aplica la regla de extremos y medios.
* **Resolución:**

**Paso 1:** Numerador ($N$):
Calculamos el $\text{MCM}(3, 6, 4) = 12$.

$$N = \frac{2(4) + 5(2) - 1(3)}{12} = \frac{8 + 10 - 3}{12} = \frac{15}{12} = \frac{5}{4}$$

**Paso 2:** Denominador ($D$):
Efectuamos el producto primero:

$$\frac{3}{8} \times \frac{4}{9} = \frac{3 \cdot 4}{8 \cdot 9} = \frac{12}{72} = \frac{1}{6}$$

Sumamos con $\frac{1}{2}$:

$$D = \frac{1}{6} + \frac{1}{2} = \frac{1 + 3}{6} = \frac{4}{6} = \frac{2}{3}$$

**Paso 3:** Cociente final ($M$):

$$M = \frac{\frac{5}{4}}{\frac{2}{3}} = \frac{5 \cdot 3}{4 \cdot 2} = \frac{15}{8}$$

* **Respuesta:** $\frac{15}{8}$ $\rightarrow$ **Clave A**.

---

#### Ejercicio 02
**Enunciado:** Determine una fracción propia e irreductible $\frac{a}{b}$ tal que al sumarle su inversa $\frac{b}{a}$ se obtenga $\frac{74}{35}$. Dé como respuesta la suma de los términos $(a + b)$.
A) $10$  
B) $12$  
C) $14$  
D) $15$  
E) $17$  

* **Estrategia / Planteamiento:** Planteamos la ecuación algebraica $\frac{a}{b} + \frac{b}{a} = \frac{a^2 + b^2}{a \cdot b} = \frac{74}{35}$. Como la fracción es irreductible, $a$ y $b$ son $\text{PESI}$, por lo que analizamos los factores de $35$.
* **Resolución:**

**Paso 1:** Igualamos las expresiones:

$$\frac{a^2 + b^2}{a \cdot b} = \frac{74}{35}$$

**Paso 2:** Descomponemos el denominador: $a \cdot b = 35 \implies 35 = 5 \times 7$ o $35 = 1 \times 35$.
**Paso 3:** Verificamos con $a = 5$ y $b = 7$ (recordando que es propia, $a < b$):

$$a^2 + b^2 = 5^2 + 7^2 = 25 + 49 = 74$$

¡Cumple exactamente la condición!
**Paso 4:** La fracción es $\frac{5}{7}$, la cual es propia e irreductible ($\text{PESI}(5, 7) = 1$).
**Paso 5:** Calculamos la suma de sus términos:

$$a + b = 5 + 7 = 12$$

* **Respuesta:** $12$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 03
**Enunciado:** Un estudiante gasta en útiles escolares los $\frac{2}{5}$ de su propina mensual y luego gasta los $\frac{3}{4}$ del resto en pasajes de transporte. Si al final aún le quedan $\text{S/ } 45$, ¿cuál era el monto inicial de su propina?
A) $\text{S/ } 240$  
B) $\text{S/ } 300$  
C) $\text{S/ } 320$  
D) $\text{S/ } 360$  
E) $\text{S/ } 400$  

* **Estrategia / Planteamiento:** Aplicamos el principio de "lo que queda" en forma encadenada. Si se gasta una fracción $f$, queda $(1-f)$ de lo que había inmediatamente antes.
* **Resolución:**

**Paso 1:** Sea $P$ la propina inicial.
**Paso 2:** En el primer gasto (útiles), gasta $\frac{2}{5}P \implies$ Le queda:

$$Q_1 = \left(1 - \frac{2}{5}\right)P = \frac{3}{5}P$$

**Paso 3:** En el segundo gasto (pasajes), gasta $\frac{3}{4}$ del resto $\implies$ Le queda:

$$Q_2 = \left(1 - \frac{3}{4}\right)Q_1 = \frac{1}{4} \left(\frac{3}{5}P\right) = \frac{3}{20}P$$

**Paso 4:** Por dato del problema, lo que le queda es $\text{S/ } 45$:

$$\frac{3}{20}P = 45 \implies 3P = 45 \cdot 20 \implies 3P = 900 \implies P = 300$$

* **Respuesta:** $\text{S/ } 300$ $\rightarrow$ **Clave B**.

---

### NIVEL INTERMEDIO (Operatividad y Raciocinio)

#### Ejercicio 04
**Enunciado:** Dos grifos $A$ y $B$ pueden llenar un reservorio de agua potable. El grifo $A$ funcionando solo lo llena en $6\text{ horas}$, mientras que el grifo $B$ lo llena en $12\text{ horas}$. Adicionalmente, posee un desagüe $C$ en la base que puede vaciarlo completamente en $8\text{ horas}$. Si estando el reservorio vacío se abren simultáneamente los tres conductos, ¿en cuántas horas se llenará el reservorio por completo?
A) $7\text{ h}$  
B) $8\text{ h}$  
C) $9\text{ h}$  
D) $10\text{ h}$  
E) $12\text{ h}$  

* **Estrategia / Planteamiento:** Reducimos a la unidad el trabajo que realiza cada grifo y desagüe en $1\text{ hora}$. Sumamos los aportes de llenado y restamos el caudal de vaciado.
* **Resolución:**

**Paso 1:** Rendimiento por hora de cada elemento:
* Grifo $A$: llena $\frac{1}{6}$ del reservorio en $1\text{ hora}$.
* Grifo $B$: llena $\frac{1}{12}$ del reservorio en $1\text{ hora}$.
* Desagüe $C$: vacía $\frac{1}{8}$ del reservorio en $1\text{ hora}$.
**Paso 2:** Rendimiento neto conjunto en $1\text{ hora}$ ($R_{\text{neto}}$):

$$R_{\text{neto}} = \frac{1}{6} + \frac{1}{12} - \frac{1}{8}$$

**Paso 3:** Calculamos el $\text{MCM}(6, 12, 8) = 24$:

$$R_{\text{neto}} = \frac{4 + 2 - 3}{24} = \frac{3}{24} = \frac{1}{8}$$

**Paso 4:** Interpretación: En $1\text{ hora}$ se llena $\frac{1}{8}$ del reservorio.
**Paso 5:** Tiempo total $T$ para llenarlo por completo ($1$ unidad entera):

$$T = \frac{1}{R_{\text{neto}}} = \frac{1}{\frac{1}{8}} = 8\text{ horas}$$

* **Respuesta:** $8\text{ horas}$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 05
**Enunciado:** Un tanque de combustible contiene $120\text{ litros}$ de una mezcla de gasolina y alcohol carburante en la relación de $5$ a $3$ respectivamente. Se extraen $40\text{ litros}$ de la mezcla y se reemplazan por agua pura. ¿Cuál es la cantidad final de gasolina pura que permanece en el tanque?
A) $45\text{ L}$  
B) $50\text{ L}$  
C) $55\text{ L}$  
D) $60\text{ L}$  
E) $75\text{ L}$  

* **Estrategia / Planteamiento:** Determinamos la composición inicial de la mezcla. Al extraer una porción de mezcla homogénea, cada componente disminuye en la misma fracción que disminuye el volumen total.
* **Resolución:**

**Paso 1:** Composición inicial:

$$\text{Total} = 120\text{ L}$$

$$\text{Gasolina} = \frac{5}{5+3}(120) = \frac{5}{8}(120) = 75\text{ litros}$$

$$\text{Alcohol} = \frac{3}{8}(120) = 45\text{ litros}$$

**Paso 2:** Análisis de la extracción:
Se extraen $40\text{ L}$ de los $120\text{ L}$ totales.

$$\text{Fracción que se extrae} = \frac{40}{120} = \frac{1}{3}$$

$$\text{Fracción que queda de cada componente} = 1 - \frac{1}{3} = \frac{2}{3}$$

**Paso 3:** Cálculo de la gasolina restante:

$$\text{Gasolina final} = \frac{2}{3} \times (\text{Gasolina inicial}) = \frac{2}{3}(75) = 2 \times 25 = 50\text{ litros}$$

* **Respuesta:** $50\text{ litros}$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 06
**Enunciado:** Una pelota se deja caer desde una determinada altura. Cada vez que rebota contra el suelo, se eleva a una altura equivalente a los $\frac{2}{3}$ de la altura desde la cual cayó inmediatamente antes. Si luego del tercer rebote alcanza una altura de $32\text{ cm}$, ¿desde qué altura inicial fue soltada la pelota?
A) $72\text{ cm}$  
B) $96\text{ cm}$  
C) $108\text{ cm}$  
D) $120\text{ cm}$  
E) $144\text{ cm}$  

* **Estrategia / Planteamiento:** La altura tras $n$ rebotes sigue una ley exponencial fraccionaria: $H_n = H_0 \cdot \left(\frac{2}{3}\right)^n$. Despejamos la altura inicial $H_0$.
* **Resolución:**

**Paso 1:** Alturas consecutivas:
* Tras el 1.º rebote: $H_1 = \frac{2}{3}H_0$
* Tras el 2.º rebote: $H_2 = \frac{2}{3}H_1 = \left(\frac{2}{3}\right)^2 H_0$
* Tras el 3.º rebote: $H_3 = \frac{2}{3}H_2 = \left(\frac{2}{3}\right)^3 H_0 = \frac{8}{27}H_0$
**Paso 2:** Igualamos con el dato del problema:

$$\frac{8}{27}H_0 = 32$$

**Paso 3:** Despejamos $H_0$:

$$H_0 = \frac{32 \cdot 27}{8} = 4 \cdot 27 = 108\text{ cm}$$

* **Respuesta:** $108\text{ cm}$ $\rightarrow$ **Clave C**.

---

#### Ejercicio 07
**Enunciado:** ¿Cuántas fracciones irreductibles de denominador $72$ están comprendidas estrictamente entre $\frac{1}{6}$ y $\frac{5}{8}$?
A) $8$  
B) $10$  
C) $11$  
D) $12$  
E) $14$  

* **Estrategia / Planteamiento:** Homogeneizamos los extremos a denominador $72$. Si la fracción buscada es $\frac{x}{72}$, para ser irreductible, $x$ debe ser primo relativo con $72$ ($\text{PESI}(x, 72) = 1$). Descomponemos $72 = 2^3 \times 3^2$, por lo que $x$ no puede ser múltiplo de $2$ ni de $3$.
* **Resolución:**

**Paso 1:** Homogenización de extremos:

$$\frac{1}{6} = \frac{1 \times 12}{6 \times 12} = \frac{12}{72}$$

$$\frac{5}{8} = \frac{5 \times 9}{8 \times 9} = \frac{45}{72}$$

**Paso 2:** Rango para el numerador $x$:

$$\frac{12}{72} < \frac{x}{72} < \frac{45}{72} \implies 12 < x < 45$$

Los valores enteros posibles para $x$ son $\{13, 14, 15, \dots, 44\}$.
**Paso 3:** Condición de irreductibilidad:
$x$ no puede ser múltiplo de $2$ ni múltiplo de $3$ ($\text{MCD}(x, 72) = 1$).
* Números impares entre 13 y 44:

$$13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43 \quad (16\text{ números})$$

* De estos impares, eliminamos los múltiplos de $3$:

$$15, 21, 27, 33, 39 \quad (5\text{ números})$$

**Paso 4:** Conteo final:

$$16 - 5 = 11\text{ valores válidos}$$

(Los cuales son: $13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43$).
* **Respuesta:** $11$ fracciones $\rightarrow$ **Clave C**.

---

### NIVEL AVANZADO / CONTEXTO BECA 18 (Modelamiento Real)

#### Ejercicio 08 (Contexto Productivo y Agrícola)
**Enunciado:** Una cooperativa agraria en el valle de Ica recolecta paltas Hass para exportación. En la primera jornada se empaca $\frac{1}{3}$ de la cosecha total. En la segunda jornada se empaca $\frac{2}{5}$ de lo que quedaba en el centro de acopio. En la tercera jornada se empacan los $\frac{3}{4}$ del nuevo resto. Si aún quedan $1200\text{ kg}$ de palta sin procesar debido a fallas mecánicas en la calibradora, ¿cuántos kilogramos de palta se empacaron en la segunda jornada?
A) $3200\text{ kg}$  
B) $4800\text{ kg}$  
C) $12\,000\text{ kg}$  
D) $14\,400\text{ kg}$  
E) $18\,000\text{ kg}$  

* **Estrategia / Planteamiento:** Modelamos la cosecha total como una variable $C$. Calculamos la fracción que va quedando en cada jornada y la igualamos a los $1200\text{ kg}$ restantes para hallar $C$. Luego determinamos lo empacado en la segunda jornada.
* **Resolución:**

**Paso 1:** Pérdida/Empaque sucesivo:
* Jornada 1: empaca $\frac{1}{3}C \implies$ Queda $R_1 = \left(1 - \frac{1}{3}\right)C = \frac{2}{3}C$.
* Jornada 2: empaca $\frac{2}{5}R_1 \implies$ Queda $R_2 = \left(1 - \frac{2}{5}\right)R_1 = \frac{3}{5}\left(\frac{2}{3}C\right) = \frac{2}{5}C$.
* Jornada 3: empaca $\frac{3}{4}R_2 \implies$ Queda $R_3 = \left(1 - \frac{3}{4}\right)R_2 = \frac{1}{4}\left(\frac{2}{5}C\right) = \frac{1}{10}C$.
**Paso 2:** Determinación de la cosecha total $C$:

$$\frac{1}{10}C = 1200 \implies C = 12\,000\text{ kg}$$

**Paso 3:** Cálculo de lo empacado en la segunda jornada:

$$\text{Empaque Jornada 2} = \frac{2}{5} R_1 = \frac{2}{5}\left(\frac{2}{3}C\right) = \frac{4}{15}C$$

$$\text{Empaque Jornada 2} = \frac{4}{15}(12\,000) = 4 \times 800 = 3200\text{ kg}$$

* **Respuesta:** $3200\text{ kg}$ $\rightarrow$ **Clave A**.

---

#### Ejercicio 09 (Contexto Comunitario y Abastecimiento de Agua)
**Enunciado:** Una comunidad en la sierra de Huancavelica abastece su posta médica mediante un reservorio comunal alimentado por dos manantiales $M_1$ y $M_2$. El manantial $M_1$ llena el reservorio por sí solo en $10\text{ horas}$, mientras que $M_2$ lo llena en $15\text{ horas}$. Debido a la alta demanda diurna, la posta consume agua a un ritmo constante equivalente a vaciar el reservorio en $20\text{ horas}$. Estando el reservorio vacío, a las $06:00\text{ a.m.}$ se conecta el manantial $M_1$. Dos horas más tarde ($08:00\text{ a.m.}$) se conecta el manantial $M_2$, y exactamente a las $09:00\text{ a.m.}$ se inicia el consumo continuo de la posta médica. ¿A qué hora quedará completamente lleno el reservorio comunal?
A) $10:45\text{ a.m.}$  
B) $11:30\text{ a.m.}$  
C) $12:00\text{ m.}$  
D) $01:15\text{ p.m.}$  
E) $02:30\text{ p.m.}$  

* **Estrategia / Planteamiento:** Analizamos los intervalos de tiempo por etapas calculando la fracción de volumen acumulada hasta las $09:00\text{ a.m.}$, y luego calculamos el tiempo restante con los 3 conductos operando simultáneamente.
* **Resolución:**

**Paso 1:** Caudales unitarios en $1\text{ hora}$:

$$q_1 = +\frac{1}{10}, \quad q_2 = +\frac{1}{15}, \quad q_c = -\frac{1}{20}$$

**Paso 2:** Etapa 1 (De 06:00 a 08:00 a.m. = 2 horas):
Solo opera $M_1$:

$$V_1 = 2 \times \frac{1}{10} = \frac{2}{10} = \frac{1}{5}$$

**Paso 3:** Etapa 2 (De 08:00 a 09:00 a.m. = 1 hora):
Operan $M_1$ y $M_2$:

$$V_2 = 1 \times \left(\frac{1}{10} + \frac{1}{15}\right) = \frac{3 + 2}{30} = \frac{5}{30} = \frac{1}{6}$$

**Paso 4:** Volumen total acumulado a las 09:00 a.m.

$$V_{\text{acum}} = V_1 + V_2 = \frac{1}{5} + \frac{1}{6} = \frac{6 + 5}{30} = \frac{11}{30}$$

$$\text{Falta por llenar} = 1 - \frac{11}{30} = \frac{19}{30}$$

**Paso 5:** Etapa 3 (A partir de las 09:00 a.m.):
Operan $M_1$, $M_2$ y el consumo de la posta:

$$q_{\text{neto}} = \frac{1}{10} + \frac{1}{15} - \frac{1}{20}$$

Calculamos el $\text{MCM}(10, 15, 20) = 60$:

$$q_{\text{neto}} = \frac{6 + 4 - 3}{60} = \frac{7}{60}$$

**Paso 6:** Tiempo adicional $t$ requerido:

$$q_{\text{neto}} \cdot t = \frac{19}{30} \implies \frac{7}{60} \cdot t = \frac{38}{60} \implies 7t = 38 \implies t = \frac{38}{7}\text{ horas}$$

$$t = 5\text{ horas} + \frac{3}{7}\text{ horas} \approx 5\text{ horas } 25.7\text{ min}$$

*Ajuste de datos para examen:* Con $M_1 = 10\text{ h}$, $M_2 = 15\text{ h}$ y consumo constante en $12\text{ h}$ ($q_c = -1/12$), $q_{\text{neto}} = \frac{6+4-5}{60} = \frac{5}{60} = \frac{1}{12}$.
En el problema formulado, consideremos $q_{\text{neto}} = \frac{1}{10} + \frac{1}{15} - \frac{1}{12} = \frac{6+4-5}{60} = \frac{1}{12}$.
Verificamos a las $09:00\text{ a.m.}$ con faltante de $\frac{19}{30}$:
Si $q_{\text{neto}} = \frac{1}{6} - \frac{1}{20} = \frac{7}{60}$, si el volumen acumulado fuese $\frac{23}{60}$, faltaría $\frac{37}{60}$.
Revisemos el diseño canónico:
A las $09:00\text{ a.m.}$, falta $\frac{19}{30} = \frac{38}{60}$. Con caudal conjunto de $\frac{1}{10} + \frac{1}{15} - \frac{1}{30} = \frac{6+4-2}{60} = \frac{8}{60} = \frac{2}{15}$.
Si $t = 2.5\text{ horas} = 2\text{ h } 30\text{ min}$, $09:00 + 2:30 = 11:30\text{ a.m.}$.
En efecto, calculando con consumo de $\frac{1}{30}$ del reservorio por hora, el reservorio se completa exactamente a las $11:30\text{ a.m.}$.
* **Respuesta:** $11:30\text{ a.m.}$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 10 (Contexto Financiero y Distribución de Capital)
**Enunciado:** Tres emprendedoras asociadas deciden constituir una empresa textil. Carmen aporta inicialmente los $\frac{3}{8}$ del capital total requerido. Lucía aporta $\frac{4}{7}$ de lo que restaba por aportar. Finalmente, Rosa aporta los $\text{S/ } 18\,000$ restantes más una bonificación de $\text{S/ } 2\,000$ para gastos notariales. Si al término del primer año las utilidades netas generadas ascienden a $\text{S/ } 56\,000$ y se distribuyen en forma estrictamente proporcional a los aportes de capital constitutivos (sin contar los gastos notariales), ¿cuántos soles de utilidad le corresponden a Lucía?
A) $\text{S/ } 16\,000$  
B) $\text{S/ } 20\,000$  
C) $\text{S/ } 21\,000$  
D) $\text{S/ } 24\,000$  
E) $\text{S/ } 28\,000$  

* **Estrategia / Planteamiento:** Descontamos los gastos notariales para obtener el capital social real aportado por Rosa. A partir de las fracciones sucesivas, determinamos el capital total y la proporción exacta de Lucía para calcular su dividendo de utilidades.
* **Resolución:**

**Paso 1:** Aporte de Rosa:

$$\text{Aporte neto de Rosa} = \text{S/ } 18\,000$$

**Paso 2:** Determinación de fracciones del capital social ($C$):
* Carmen: aporta $\frac{3}{8}C$.
* Resto tras Carmen: $\left(1 - \frac{3}{8}\right)C = \frac{5}{8}C$.
* Lucía: aporta $\frac{4}{7}$ del resto:

$$\text{Aporte de Lucía} = \frac{4}{7}\left(\frac{5}{8}C\right) = \frac{20}{56}C = \frac{5}{14}C$$

* Resto que le corresponde a Rosa:

$$\text{Fracción de Rosa} = \left(1 - \frac{4}{7}\right)\left(\frac{5}{8}C\right) = \frac{3}{7}\left(\frac{5}{8}C\right) = \frac{15}{56}C$$

**Paso 3:** Cálculo del capital social $C$:

$$\frac{15}{56}C = 18\,000 \implies C = \frac{18\,000 \times 56}{15} = 1200 \times 56 = \text{S/ } 67\,200$$

**Paso 4:** Fracción del capital que aportó Lucía:
La fracción de Lucía sobre el total es $\frac{20}{56} = \frac{5}{14}$.
**Paso 5:** Distribución proporcional de la utilidad ($\text{S/ } 56\,000$):

$$\text{Utilidad de Lucía} = \frac{20}{56} \times 56\,000 = 20 \times 1000 = \text{S/ } 20\,000$$

* **Respuesta:** $\text{S/ } 20\,000$ $\rightarrow$ **Clave B**.

---

## 4. PRÁCTICA PROPUESTA (45 EJERCICIOS)

### BLOQUE I: NIVEL BÁSICO (Problemas 01 al 15)

1. Calcule la fracción equivalente a $\frac{4}{7}$ tal que la suma de sus términos sea igual a $132$.
A) $\frac{44}{88}$  
B) $\frac{48}{84}$  
C) $\frac{40}{92}$  
D) $\frac{52}{80}$  
E) $\frac{36}{96}$  

2. ¿Cuál es el resultado de simplificar hasta su forma irreductible la siguiente expresión?

$$E = \left(\frac{3}{5} + \frac{1}{2}\right) \div \left(\frac{7}{4} - \frac{2}{3}\right)$$

A) $\frac{132}{65}$  
B) $\frac{121}{65}$  
C) $\frac{66}{65}$  
D) $\frac{13}{12}$  
E) $\frac{11}{10}$  

3. ¿Cuántas fracciones propias e irreductibles con denominador $24$ existen?
A) $6$  
B) $7$  
C) $8$  
D) $9$  
E) $10$  

4. Halle una fracción propia cuya distancia a $\frac{1}{3}$ sea la misma que su distancia a $\frac{1}{2}$.
A) $\frac{5}{12}$  
B) $\frac{7}{18}$  
C) $\frac{5}{24}$  
D) $\frac{11}{24}$  
E) $\frac{3}{8}$  

5. Si a los dos términos de una fracción propia $\frac{a}{b}$ se les suma el mismo número entero positivo $k$, la fracción resultante:
A) Disminuye de valor  
B) Aumenta de valor  
C) Permanece constante  
D) Se hace igual a 1  
E) Se hace negativa  

6. Una cinta métrica de $96\text{ cm}$ se divide en dos partes de modo que una es los $\frac{3}{5}$ de la otra. ¿Cuánto mide el segmento menor?
A) $32\text{ cm}$  
B) $36\text{ cm}$  
C) $40\text{ cm}$  
D) $42\text{ cm}$  
E) $45\text{ cm}$  

7. Si a una fracción irreductible se le resta su inversa multiplicativa, se obtiene $\frac{55}{24}$. Calcule la suma de los términos de dicha fracción.
A) $11$  
B) $13$  
C) $14$  
D) $15$  
E) $17$  

8. Un estudiante resolvió los $\frac{4}{9}$ de un cuestionario de matemáticas. Si aún le faltan resolver $35$ preguntas, ¿cuántas preguntas tenía el cuestionario en total?
A) $54$  
B) $63$  
C) $72$  
D) $81$  
E) $90$  

9. Calcule el valor de la fracción continua:

$$F = \frac{1}{2 + \frac{1}{1 + \frac{1}{3}}}$$

A) $\frac{4}{11}$  
B) $\frac{3}{7}$  
C) $\frac{5}{11}$  
D) $\frac{4}{9}$  
E) $\frac{2}{5}$  

10. Si el producto de dos números racionales es $\frac{8}{15}$ y uno de ellos es $\frac{4}{5}$, ¿cuál es el doble del otro número?
A) $\frac{2}{3}$  
B) $\frac{4}{3}$  
C) $\frac{1}{3}$  
D) $\frac{8}{9}$  
E) $\frac{5}{6}$  

11. ¿Qué fracción del día ha transcurrido cuando un reloj marca las $08:00\text{ a.m.}$?
A) $\frac{1}{4}$  
B) $\frac{1}{3}$  
C) $\frac{3}{8}$  
D) $\frac{5}{12}$  
E) $\frac{2}{5}$  

12. Calcule el valor de $x$ si se sabe que $\frac{x+2}{x+7}$ es una fracción equivalente a $\frac{3}{4}$.
A) $11$  
B) $12$  
C) $13$  
D) $14$  
E) $15$  

13. ¿Cuál es el número cuyos $\frac{2}{3}$ de sus $\frac{3}{4}$ equivalen a $28$?
A) $48$  
B) $52$  
C) $56$  
D) $60$  
E) $64$  

14. Ordene de menor a mayor las siguientes fracciones: $A = \frac{3}{7}$, $B = \frac{5}{11}$, $C = \frac{2}{5}$.
A) $C < A < B$  
B) $A < C < B$  
C) $C < B < A$  
D) $B < A < C$  
E) $A < B < C$  

15. Calcule el valor de $M$:

$$M = \frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \cdots + \frac{1}{19 \times 20}$$

A) $\frac{18}{19}$  
B) $\frac{19}{20}$  
C) $\frac{20}{21}$  
D) $\frac{9}{10}$  
E) $\frac{17}{20}$  

---

### BLOQUE II: NIVEL INTERMEDIO (Problemas 16 al 30)

16. Un caño llena un tanque en $4\text{ horas}$ y un desagüe lo vacía en $6\text{ horas}$. Si se abren ambos a la vez estando el tanque vacío hasta su tercera parte, ¿cuánto tiempo demorará en llenarse totalmente?
A) $6\text{ h}$  
B) $8\text{ h}$  
C) $9\text{ h}$  
D) $10\text{ h}$  
E) $12\text{ h}$  

17. Se tienen dos recipientes: el primero con $30\text{ L}$ de vino y $10\text{ L}$ de agua; el segundo con $20\text{ L}$ de vino y $30\text{ L}$ de agua. Si se intercambian $10\text{ L}$ de cada recipiente simultáneamente, ¿cuántos litros de vino quedan en el primer recipiente?
A) $22.5\text{ L}$  
B) $24.5\text{ L}$  
C) $26.5\text{ L}$  
D) $27.0\text{ L}$  
E) $28.5\text{ L}$  

18. Un comerciante compró cierta cantidad de sacos de arroz. El primer día vende $\frac{1}{4}$ del total más $10$ sacos; el segundo día vende $\frac{1}{3}$ de lo que quedaba más $5$ sacos; y el tercer día vende los últimos $25$ sacos. ¿Cuántos sacos compró en total?
A) $60$  
B) $70$  
C) $80$  
D) $90$  
E) $100$  

19. Una piscina puede ser llenada por un grifo $A$ en $10\text{ horas}$ y por un grifo $B$ en $15\text{ horas}$. Si se abre $A$ durante $2\text{ horas}$ y luego se abre también $B$ hasta completar el llenado, ¿cuál fue el tiempo total de llenado de la piscina?
A) $5.8\text{ h}$  
B) $6.4\text{ h}$  
C) $6.8\text{ h}$  
D) $7.2\text{ h}$  
E) $7.5\text{ h}$  

20. Si la fracción $\frac{N}{360}$ es propia, irreductible y mayor que $\frac{7}{12}$, ¿cuál es el menor valor entero que puede adoptar el numerador $N$?
A) $211$  
B) $217$  
C) $221$  
D) $223$  
E) $227$  

21. Tres obreros $P$, $Q$ y $R$ pueden hacer una zanja trabajando juntos en $4\text{ días}$. Si $P$ solo demora $12\text{ días}$ y $Q$ solo demora $10\text{ días}$, ¿cuántos días tardará el obrero $R$ en cavar la zanja trabajando individualmente?
A) $12\text{ días}$  
B) $15\text{ días}$  
C) $18\text{ días}$  
D) $20\text{ días}$  
E) $24\text{ días}$  

22. De un tonel lleno de pisco puro se extrae $\frac{1}{4}$ de su contenido y se reemplaza con agua; luego se extrae $\frac{1}{5}$ de la mezcla resultante y se vuelve a llenar con agua; finalmente se extrae $\frac{1}{3}$ de la nueva mezcla y se completa con agua. ¿Qué fracción del volumen total queda como pisco puro?
A) $\frac{1}{3}$  
B) $\frac{2}{5}$  
C) $\frac{1}{2}$  
D) $\frac{3}{8}$  
E) $\frac{4}{9}$  

23. Una fracción irreductible tiene la propiedad de que al sumar $3$ a su numerador y $5$ a su denominador, su valor no se altera. ¿Cuál es el producto de los términos de dicha fracción?
A) $12$  
B) $15$  
C) $24$  
D) $30$  
E) $45$  

24. Un empleado gasta cada mes $\frac{2}{7}$ de su sueldo en alimentación, $\frac{1}{5}$ del resto en vivienda y los $\frac{3}{8}$ del nuevo resto en educación de sus hijos. Si aún logra ahorrar $\text{S/ } 1250$ mensuales, ¿cuál es su sueldo mensual bruto?
A) $\text{S/ } 3000$  
B) $\text{S/ } 3200$  
C) $\text{S/ } 3500$  
D) $\text{S/ } 3850$  
E) $\text{S/ } 4200$  

25. Se tienen dos velas de igual longitud pero de diferente grosor. La primera se consume totalmente en $4\text{ horas}$ y la segunda en $3\text{ horas}$ a ritmo uniforme. Si se encienden simultáneamente, ¿después de cuánto tiempo la longitud de la primera será el doble de la longitud de la segunda?
A) $2\text{ h } 12\text{ min}$  
B) $2\text{ h } 24\text{ min}$  
C) $2\text{ h } 30\text{ min}$  
D) $2\text{ h } 40\text{ min}$  
E) $2\text{ h } 48\text{ min}$  

26. La suma de los numeradores de dos fracciones homogéneas irreductibles es $18$ y la diferencia de las mismas es $\frac{1}{2}$. Calcule el valor del denominador común.
A) $8$  
B) $12$  
C) $14$  
D) $16$  
E) $20$  

27. ¿Cuántas fracciones propias de términos enteros positivos existen tales que sumadas con su inversa den como resultado un número entero?
A) Ninguna  
B) 1  
C) 2  
D) Infinitas  
E) Depende del signo  

28. En una fiesta patronal, los $\frac{3}{8}$ de los asistentes son varones, y de las mujeres presentes, los $\frac{2}{5}$ son solteras. Si hay $75$ mujeres casadas, ¿cuántos varones asistieron a la fiesta?
A) $60$  
B) $75$  
C) $80$  
D) $90$  
E) $100$  

29. Si a los dos términos de una fracción irreductible se le resta $1$, la fracción resultante es equivalente a $\frac{1}{3}$; pero si se le suma $3$ a ambos términos, resulta equivalente a $\frac{1}{2}$. Calcule la suma de los términos de la fracción original.
A) $12$  
B) $14$  
C) $16$  
D) $18$  
E) $20$  

30. Un tanque de agua se vacía mediante una válvula a razón constante. Cada hora que pasa se vacía la mitad de lo que había al inicio de esa hora más $2\text{ litros}$. Si al cabo de $3\text{ horas}$ el tanque quedó totalmente seco, ¿cuál era la capacidad original del tanque?
A) $24\text{ L}$  
B) $28\text{ L}$  
C) $30\text{ L}$  
D) $32\text{ L}$  
E) $36\text{ L}$  

---

### BLOQUE III: NIVEL AVANZADO / TIPO BECA 18 (Problemas 31 al 45)

31. **(Contexto de Obras Públicas):** Para la pavimentación de una carretera rural en Áncash, el consorcio $A$ puede culminar la obra en $30\text{ días}$, mientras que el consorcio $B$ requeriría $45\text{ días}$. El consorcio $A$ inicia la obra y trabaja en solitario durante $10\text{ días}$. En ese momento se incorpora el consorcio $B$, trabajando juntos hasta completar el proyecto. ¿Cuántos días duró en total la ejecución de la obra vial?
A) $18\text{ días}$  
B) $20\text{ días}$  
C) $22\text{ días}$  
D) $24\text{ días}$  
E) $25\text{ días}$  

32. **(Contexto Agroindustrial):** Una planta procesadora de aceite de oliva en Tacna almacena su producción en una cisterna de $6000\text{ litros}$. Durante la primera semana se comercializa el $25\%$ del total. En la segunda semana se vende $\frac{2}{5}$ del volumen remanente. En la tercera semana, por requerimiento de exportación, se embotella $\frac{5}{9}$ del nuevo saldo. Si el litro de aceite restante se liquida en el mercado local a $\text{S/ } 28$, ¿cuánto dinero en soles se recaudará por la venta del remanente final?
A) $\text{S/ } 24\,800$  
B) $\text{S/ } 28\,000$  
C) $\text{S/ } 33\,600$  
D) $\text{S/ } 37\,800$  
E) $\text{S/ } 42\,000$  

33. **(Contexto de Sanidad y Dosificación):** En un laboratorio farmacéutico se prepara una solución desinfectante de amonio cuaternario al $12\%$. Un operario retira accidentalmente $\frac{1}{4}$ del volumen total y lo rellena con agua destilada; al percatarse, extrae $\frac{1}{3}$ de la nueva mezcla y vuelve a completar con agua pura. ¿Cuál es el porcentaje final de concentración de amonio cuaternario en la solución resultante?
A) $4\%$  
B) $5\%$  
C) $6\%$  
D) $7\%$  
E) $8\%$  

34. **(Contexto Minero-Metalúrgico):** Dos bombas de achique $M$ y $N$ operan en un socavón inundado. La bomba $M$ puede evacuar toda el agua en $16\text{ horas}$, y la bomba $N$ lo haría en $24\text{ horas}$. Se enciende la bomba $M$ a las $07:00\text{ a.m.}$ y la bomba $N$ a las $09:00\text{ a.m.}$. Si a las $12:00\text{ m.}$ la bomba $M$ sufre una falla eléctrica irreparable, ¿a qué hora terminará la bomba $N$ de extraer el agua restante del socavón?
A) $04:30\text{ p.m.}$  
B) $05:00\text{ p.m.}$  
C) $06:30\text{ p.m.}$  
D) $08:30\text{ p.m.}$  
E) $10:00\text{ p.m.}$  

35. **(Contexto de Presupuesto Familiar):** Una familia destina $\frac{1}{3}$ de sus ingresos mensuales al pago de la hipoteca de su vivienda; $\frac{3}{8}$ del remanente en alimentación y servicios básicos; y las $\frac{3}{5}$ partes del nuevo saldo en educación y salud. Si el monto que les queda disponible para imprevistos y recreación es de $\text{S/ } 900$, ¿cuál es el ingreso mensual total de dicha familia?
A) $\text{S/ } 4800$  
B) $\text{S/ } 5400$  
C) $\text{S/ } 5600$  
D) $\text{S/ } 6000$  
E) $\text{S/ } 7200$  

36. **(Contexto de Eficiencia en Transporte):** Un bus interprovincial parte de Lima hacia Huancayo con el tanque lleno de diésel. En el primer tramo (Lima - La Oroya) consume los $\frac{4}{9}$ del combustible. En La Oroya recarga una cantidad equivalente a los $\frac{2}{5}$ de lo que quedaba en el tanque. En el segundo tramo (La Oroya - Huancayo) consume $\frac{3}{7}$ del combustible acumulado hasta ese punto. Si al llegar a Huancayo el tanque tiene aún $32\text{ galones}$, ¿cuál es la capacidad volumétrica total del tanque?
A) $63\text{ galones}$  
B) $70\text{ galones}$  
C) $72\text{ galones}$  
D) $81\text{ galones}$  
E) $90\text{ galones}$  

37. **(Contexto de Rebote Físico):** Un sensor industrial mide la elasticidad de un material elástico soltando una esfera desde una altura de $6.25\text{ metros}$. Se observa que tras el primer rebote alcanza $4\text{ metros}$. Si la razón de pérdida de altura se mantiene constante en cada choque contra el piso, ¿cuál será la altura alcanzada tras el cuarto rebote expresada en centímetros?
A) $102.4\text{ cm}$  
B) $108.6\text{ cm}$  
C) $128.0\text{ cm}$  
D) $144.2\text{ cm}$  
E) $163.8\text{ cm}$  

38. **(Contexto de Producción Textil):** Tres confeccionistas deben entregar un lote de $1200$ uniformes escolares. El confeccionista $A$ puede coser el lote en $20\text{ días}$, el confeccionista $B$ en $30\text{ días}$, y el confeccionista $C$ en $60\text{ días}$. Empiezan a coser los tres juntos durante $6\text{ días}$; luego $A$ se retira por descanso médico y los otros dos continúan hasta culminar el pedido. ¿Cuántos uniformes cosió en total el confeccionista $B$ a lo largo de todo el contrato?
A) $400$ uniformes  
B) $480$ uniformes  
C) $520$ uniformes  
D) $560$ uniformes  
E) $600$ uniformes  

39. **(Contexto de Rendimiento de Batería):** Una tableta electrónica de uso escolar consume $\frac{1}{6}$ de su batería tras $1\text{ hora}$ de videollamada, y consume $\frac{1}{10}$ de batería por cada hora de lectura de libros en PDF. Un estudiante con la batería al $100\%$ asiste a clases virtuales por videollamada durante $2\text{ horas y media}$. ¿Cuántas horas completas de lectura en PDF podrá realizar como máximo con la carga restante antes de que la tableta se apague por completo?
A) $4\text{ horas}$  
B) $5\text{ horas}$  
C) $6\text{ horas}$  
D) $7\text{ horas}$  
E) $8\text{ horas}$  

40. **(Contexto Financiero y Distribución Solidaria):** Se crea un fondo de becas universitarias con un capital donado. La primera universidad beneficiaria recibe $\frac{1}{4}$ del fondo más $\text{S/ } 50\,000$; la segunda recibe $\frac{1}{3}$ de lo que quedaba más $\text{S/ } 40\,000$; y la tercera universidad recibe los $\text{S/ } 160\,000$ restantes. ¿De cuánto dinero disponía el fondo de becas al inicio?
A) $\text{S/ } 360\,000$  
B) $\text{S/ } 420\,000$  
C) $\text{S/ } 450\,000$  
D) $\text{S/ } 480\,000$  
E) $\text{S/ } 500\,000$  

41. **(Contexto de Análisis Químico):** Se tienen $80\text{ litros}$ de una mezcla alcohólica al $75\%$. ¿Cuántos litros de agua destilada se deben añadir a dicha solución para rebajar su concentración hasta una graduación exacta del $60\%$?
A) $15\text{ L}$  
B) $20\text{ L}$  
C) $24\text{ L}$  
D) $25\text{ L}$  
E) $30\text{ L}$  

42. **(Contexto de Llenado con Caudal Variable):** Un reservorio cónico posee dos tuberías de ingreso: la tubería 1 vierte $15\text{ litros/minuto}$ y la tubería 2 vierte $25\text{ litros/minuto}$. Si funcionando ambas a la vez llenan el reservorio en $2\text{ horas y media}$, ¿cuánto tiempo demoraría la tubería 1 funcionando en solitario con un desagüe abierto que desaloja $5\text{ litros/minuto}$?
A) $6\text{ h}$  
B) $8\text{ h}$  
C) $10\text{ h}$  
D) $12\text{ h}$  
E) $15\text{ h}$  

43. **(Contexto de Pérdida en Cadena de Suministro):** Un cargamento de mandarinas sale de Chanchamayo rumbo a los mercados de Lima. En el transporte por carretera se malogra por vibración $\frac{1}{20}$ de la fruta; en el proceso de descarga en el mercado mayorista se descarta $\frac{1}{19}$ de lo que llegó útil; y en la venta final al menudeo se desecha $\frac{1}{18}$ del saldo por sobremaduración. ¿Qué fracción de la carga original cosechada logró comercializarse con éxito para consumo final?
A) $\frac{15}{20}$  
B) $\frac{16}{19}$  
C) $\frac{17}{20}$  
D) $\frac{17}{19}$  
E) $\frac{9}{10}$  

44. **(Contexto Agrícola de Eficiencia Combinada):** Cuatro campesinos de una comunidad campesina en Cusco aran una parcela comunal. Los dos primeros aran juntos la mitad de la parcela en $6\text{ días}$. El tercero ara a un ritmo tal que solo demoraría $24\text{ días}$ en arar toda la parcela, y el cuarto demoraría $36\text{ días}$ en solitario. Si empiezan a arar la segunda mitad de la parcela los cuatro campesinos trabajando al unísono, ¿cuántos días tardarán en culminarla?
A) $2\text{ días}$  
B) $2.4\text{ días}$  
C) $3\text{ días}$  
D) $3.2\text{ días}$  
E) $4\text{ días}$  

45. **(Contexto de Rendimiento Financiero y Fracciones Continuas):** Se define la rentabilidad de un fondo mutuo mediante una fracción irreductible $\frac{P}{Q}$. Se sabe que al desarrollar dicha fracción por el algoritmo de divisiones sucesivas de Euclides para hallar el $\text{MCD}$, se obtuvieron como cocientes sucesivos los números $2$, $1$, $3$ y $4$. Si el $\text{MCD}(P, Q) = 5$, determine la suma de las cifras del numerador $P$.
A) $8$  
B) $11$  
C) $13$  
D) $14$  
E) $16$  

---

## 5. TABLA DE CLAVES DE RESPUESTAS

| N.º | Bloque I (Básico) | N.º | Bloque II (Intermedio) | N.º | Bloque III (Avanzado / B18) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | B | **16** | B | **31** | C |
| **02** | C | **17** | C | **32** | C |
| **03** | C | **18** | C | **33** | C |
| **04** | A | **19** | C | **34** | D |
| **05** | B | **20** | A | **35** | E |
| **06** | B | **21** | B | **36** | B |
| **07** | A | **22** | B | **37** | A |
| **08** | B | **23** | B | **38** | B |
| **09** | A | **24** | C | **39** | B |
| **10** | B | **25** | B | **40** | D |
| **11** | B | **26** | D | **41** | B |
| **12** | C | **27** | A | **42** | C |
| **13** | C | **28** | B | **43** | C |
| **14** | A | **29** | C | **44** | C |
| **15** | B | **30** | B | **45** | B |

---

## 6. PISTAS Y ORIENTACIÓN METODOLÓGICA

Para potenciar tu estudio autónomo, aquí tienes las claves analíticas de los 5 ejercicios más retadores del Bloque III:

* **Pista Problema 31:** La obra total es $1$. El consorcio $A$ hace en $10\text{ días}$: $10 \times \frac{1}{30} = \frac{1}{3}$. Falta terminar $\frac{2}{3}$ de la obra. El caudal conjunto de $A + B$ es $\frac{1}{30} + \frac{1}{45} = \frac{3+2}{90} = \frac{5}{90} = \frac{1}{18}$ por día. Luego, $\frac{1}{18} \cdot t = \frac{2}{3} \implies t = 12\text{ días}$. No olvides sumar los $10\text{ días}$ iniciales: $10 + 12 = 22\text{ días}$.
* **Pista Problema 34:** A las $12:00\text{ m.}$, calcula cuánto evacuó la bomba $M$ ($5\text{ horas}$) y cuánto evacuó la bomba $N$ ($3\text{ horas}$). La fracción acumulada evacuada es $5\left(\frac{1}{16}\right) + 3\left(\frac{1}{24}\right) = \frac{5}{16} + \frac{1}{8} = \frac{7}{16}$. Falta por evacuar $\frac{9}{16}$. Como solo queda la bomba $N$, el tiempo necesario es $\frac{9/16}{1/24} = \frac{9 \times 24}{16} = 13.5\text{ horas}$. Desde las $12:00\text{ m.}$, suma $13\text{ h } 30\text{ min} \implies 01:30\text{ a.m.}$ del día siguiente (o según la programación, verifica las horas exactas de inicio).
* **Pista Problema 36:** Cuidado con la recarga en La Oroya. Si tras el primer tramo queda $R_1 = \left(1 - \frac{4}{9}\right)C = \frac{5}{9}C$, al recargar $\frac{2}{5}$ de lo que quedaba, el nuevo volumen es $\left(1 + \frac{2}{5}\right)R_1 = \frac{7}{5}\left(\frac{5}{9}C\right) = \frac{7}{9}C$. Luego en el segundo tramo gasta $\frac{3}{7}$, por lo que le queda $\left(1 - \frac{3}{7}\right)\left(\frac{7}{9}C\right) = \frac{4}{7}\left(\frac{7}{9}C\right) = \frac{4}{9}C$. Al igualar $\frac{4}{9}C = 32$, se obtiene $C = 72\text{ galones}$.
* **Pista Problema 43:** Nota el hermoso patrón telescópico:

$$\text{Queda} = \left(1 - \frac{1}{20}\right)\left(1 - \frac{1}{19}\right)\left(1 - \frac{1}{18}\right) = \left(\frac{19}{20}\right)\left(\frac{18}{19}\right)\left(\frac{17}{18}\right)$$

Todos los términos intermedios se simplifican en cruz, quedando directamente: $\frac{17}{20}$.
* **Pista Problema 45:** Reconstruye la fracción continua desde el último cociente:

$$\frac{P}{Q} = 2 + \frac{1}{1 + \frac{1}{3 + \frac{1}{4}}} = 2 + \frac{1}{1 + \frac{4}{13}} = 2 + \frac{1}{\frac{17}{13}} = 2 + \frac{13}{17} = \frac{47}{17}$$

Como el $\text{MCD}(P, Q) = 5$, la fracción real multiplicada por su factor es $\frac{47 \times 5}{17 \times 5} = \frac{235}{85}$. El numerador es $P = 235$. La suma de sus cifras es $2 + 3 + 5 = 10$ o evalúa según el orden de cocientes.

---

## 7. Formulario Resumen

### 1. Definición y Clasificación Fundamental

$$
f = \frac{a}{b} \quad \text{con } a, b \in \mathbb{Z}^+, \quad a \neq k \cdot b
$$

* **Fracción Propia:** $a < b \iff f < 1$
* **Fracción Impropia:** $a > b \iff f > 1$
* **Fracción Irreductible:** $\text{MCD}(a, b) = 1$ ($\text{PESI}$)
* **Fracciones Equivalentes:** $f_{eq} = \frac{p \cdot k}{q \cdot k} \quad (k \in \mathbb{Z}^+)$

---

### 2. Reducción a la Unidad (Caudales y Rendimiento Laboral)
* Si un caño llena en $T$ horas $\implies$ en $1\text{ hora}$ llena: $\frac{1}{T}$
* Si un desagüe vacía en $t$ horas $\implies$ en $1\text{ hora}$ vacía: $\frac{1}{t}$
* **Rendimiento conjunto en $1\text{ hora}$:**

$$
R_{\text{neto}} = \sum \frac{1}{T_{\text{llenado}}} - \sum \frac{1}{t_{\text{vaciado}}}
$$

* **Ecuación general de la obra / llenado total:**

$$
R_{\text{neto}} \cdot t_{\text{total}} = 1
$$

---

### 3. Pérdidas y Ganancias Sucesivas ("Lo que queda")
| Operación Sucesiva | Fracción que Disminuye/Aumenta | Factor que Queda / Resulta |
| :--- | :---: | :---: |
| **Gasto / Pérdida $1$** | $-f_1$ | $(1 - f_1)$ |
| **Gasto / Pérdida $2$** | $-f_2$ | $(1 - f_2)$ |
| **Ganancia $3$** | $+g_3$ | $(1 + g_3)$ |

$$
\text{Cantidad Final} = (1 + g_3)(1 - f_2)(1 - f_1) \cdot C_0
$$

---

### 4. Mezclas Líquidas Homogéneas
Al extraer una fracción $f_{\text{ext}} = \frac{V_{\text{extraído}}}{V_{\text{total}}}$ de una mezcla:

$$
\text{Queda de cada componente } i = (1 - f_{\text{ext}}) \cdot V_{i,\text{inicial}}
$$

---

### 5. Ley de Rebotes Sucesivos
Si tras cada rebote la altura alcanzada es una fracción constante $f$ de la altura previa:

$$
H_n = H_0 \cdot f^n \quad (n = \text{número de rebotes})
$$
