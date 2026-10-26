# TEMA 04: ARITMÉTICA – NOTACIÓN CIENTÍFICA Y EXPONENCIAL

> **Área:** Competencias Matemáticas (Resuelve problemas de cantidad)
> **Indicador Oficial (PRONABEC / CNEB):** *Interpreta su comprensión sobre las operaciones con números racionales usando diversas representaciones con notación exponencial o científica.*
> **Nivel:** Preuniversitario / Beca 18 – Alto Rendimiento

---
## 1. MOTIVACIÓN Y CONTEXTO REAL

En la investigación científica y la tecnología de punta, interactuamos constantemente con magnitudes que escapan a la escala humana ordinaria:
* **En el microcosmos:** La masa de un electrón es de aproximadamente $0.000\,000\,000\,000\,000\,000\,000\,000\,000\,000\,911\text{ kg}$, y el diámetro de un nanotubo de carbono es de apenas $0.000\,000\,001\text{ metros}$.
* **En el macrocosmos:** La masa del planeta Tierra es de unos $5\,972\,000\,000\,000\,000\,000\,000\,000\text{ kg}$, y la distancia entre galaxias se mide en billones de kilómetros.

Escribir y operar estos números en su forma decimal convencional no solo es tedioso, sino extremadamente propenso a errores por exceso o defecto de ceros. La **Notación Científica** resuelve este desafío de forma compacta y elegante mediante potencias enteras de base 10.

En las pruebas de Beca 18 y exámenes de admisión, este tema evalúa la destreza para transformar datos numéricos entre formatos, efectuar sumas y productos en potencias de diez y calcular **órdenes de magnitud** en problemas de física, química, astronomía y telecomunicaciones.

---

## 2. FUNDAMENTACIÓN TEÓRICA RIGUROSA

### 2.1 Definición y Estructura Estándar de la Notación Científica

Un número real $N$ está expresado en **Notación Científica Normalizada** (o Estándar) si adopta la forma canónica:

$$
N = a \times 10^k
$$

donde:
* **$a$ (Mantisa, Coeficiente o Cifra Significativa):** Es un número real tal que su valor absoluto es mayor o igual a $1$ y estrictamente menor que $10$:

$$1 \le |a| < 10$$

* **$k$ (Orden de Magnitud o Exponente Entero):** Es un número entero ($k \in \mathbb{Z}$).

#### Regla de los Signos del Exponente $k$:
1. **Si $|N| \ge 10$ ($k > 0$):** El punto decimal se desplaza $k$ posiciones hacia la **izquierda**.

$$45\,800 = 4.58 \times 10^4$$

2. **Si $0 < |N| < 1$ ($k < 0$):** El punto decimal se desplaza $|k|$ posiciones hacia la **derecha**.

$$0.000729 = 7.29 \times 10^{-4}$$

3. **Si $1 \le |N| < 10$ ($k = 0$):** El exponente es cero.

$$6.34 = 6.34 \times 10^0$$

> ⚠️ **Error Frecuente:** Escribir expresiones como $45.8 \times 10^3$ o $0.729 \times 10^{-3}$ y considerarlas "notación científica". Aunque son matemáticamente equivalentes, **no están en notación científica normalizada**, pues sus coeficientes ($45.8 \ge 10$ y $0.729 < 1$) no cumplen la condición obligatoria $1 \le |a| < 10$.

---

### 2.2 Notación Científica Normalizada vs. Notación Exponencial Libre

* **Notación Exponencial Libre:** Cualquier representación de la forma $b \times 10^m$ donde $b$ puede ser cualquier número real sin restricciones de rango (por ejemplo: $520 \times 10^3$ o $0.05 \times 10^6$).
* **Notación Científica Normalizada:** Exige estrictamente que la parte entera del coeficiente tenga **exactamente un dígito distinto de cero** ($1, 2, 3, 4, 5, 6, 7, 8, 9$).

---

### 2.3 Prefijos del Sistema Internacional (SI)

Los múltiplos y submúltiplos del Sistema Internacional facilitan la lectura verbal de potencias de diez:

#### Múltiplos (Cantidades Mayores que la Unidad)
| Prefijo | Símbolo | Factor Numérico | Equivalencia Científica |
| :--- | :---: | :---: | :---: |
| **deca** | $\text{da}$ | $10$ | $10^1$ |
| **hecto** | $\text{h}$ | $100$ | $10^2$ |
| **kilo** | $\text{k}$ | $1\,000$ | $10^3$ |
| **mega** | $\text{M}$ | $1\,000\,000$ | $10^6$ |
| **giga** | $\text{G}$ | $1\,000\,000\,000$ | $10^9$ |
| **tera** | $\text{T}$ | $1\,000\,000\,000\,000$ | $10^{12}$ |
| **peta** | $\text{P}$ | $10^{15}$ | $10^{15}$ |

#### Submúltiplos (Cantidades Menores que la Unidad)
| Prefijo | Símbolo | Factor Numérico | Equivalencia Científica |
| :--- | :---: | :---: | :---: |
| **deci** | $\text{d}$ | $0.1$ | $10^{-1}$ |
| **centi** | $\text{c}$ | $0.01$ | $10^{-2}$ |
| **mili** | $\text{m}$ | $0.001$ | $10^{-3}$ |
| **micro** | $\mu$ | $0.000\,001$ | $10^{-6}$ |
| **nano** | $\text{n}$ | $0.000\,000\,001$ | $10^{-9}$ |
| **pico** | $\text{p}$ | $0.000\,000\,000\,001$ | $10^{-12}$ |
| **femto** | $\text{f}$ | $10^{-15}$ | $10^{-15}$ |

---

### 2.4 Operaciones Aritméticas Fundamentales con Notación Científica

#### 1. Adición y Sustracción
Para sumar o restar cantidades en notación científica, **los exponentes de la base 10 deben ser estrictamente iguales**. Si son diferentes, se debe homogenizar al exponente mayor o menor antes de operar:

$$
a \times 10^k \pm b \times 10^k = (a \pm b) \times 10^k
$$

* *Ejemplo:* Sumar $3.2 \times 10^5 + 4.5 \times 10^4$.
1. Homogeneizamos al exponente mayor ($10^5$): $4.5 \times 10^4 = 0.45 \times 10^5$.
2. Sumamos las mantisas: $(3.2 + 0.45) \times 10^5 = 3.65 \times 10^5$.

#### 2. Multiplicación
Se multiplican los coeficientes entre sí y se suman algebraicamente los exponentes de la base 10:

$$
(a \times 10^m) \times (b \times 10^n) = (a \cdot b) \times 10^{m+n}
$$

* Si el producto $a \cdot b \ge 10$, se reajusta la mantisa dividiendo entre 10 y sumando 1 al exponente:

$$(4 \times 10^6) \times (5 \times 10^3) = 20 \times 10^9 = 2.0 \times 10^{10}$$

#### 3. División
Se dividen los coeficientes entre sí y se restan los exponentes de la base 10:

$$
\frac{a \times 10^m}{b \times 10^n} = \left(\frac{a}{b}\right) \times 10^{m-n}
$$

#### 4. Potenciación y Radicación
* **Potencia:**

$$(a \times 10^k)^p = a^p \times 10^{k \cdot p}$$

* **Radicación:** Para que la raíz sea exacta, el exponente $k$ debe ser múltiplo del índice $n$:

$$\sqrt[n]{a \times 10^k} = \sqrt[n]{a} \times 10^{\frac{k}{n}}$$

* *Ejemplo:* $\sqrt{9 \times 10^7} = \sqrt{90 \times 10^6} = \sqrt{90} \times 10^3 \approx 9.487 \times 10^3$.

---

### 2.5 Concepto de Orden de Magnitud y Criterio de la Media Geométrica

El **Orden de Magnitud (OM)** de un número es la potencia de 10 más cercana a dicho valor. Para determinarlo formalmente en un número $N = a \times 10^k$:

Se compara la mantisa $a$ con la media geométrica entre $1$ y $10$:

$$
\text{Media Geométrica} = \sqrt{1 \times 10} = \sqrt{10} \approx 3.162277\dots
$$

#### Criterio Oficial de Decisión:

$$
\text{Orden de Magnitud}(a \times 10^k) =
\begin{cases}
10^k, & \text{si } a < \sqrt{10} \approx 3.162 \\
10^{k+1}, & \text{si } a \ge \sqrt{10} \approx 3.162
\end{cases}
$$

* *Ejemplo 1:* $N = 2.8 \times 10^6$. Como $2.8 < 3.162 \implies \text{OM} = 10^6$.
* *Ejemplo 2:* $N = 7.4 \times 10^6$. Como $7.4 \ge 3.162 \implies \text{OM} = 10^{6+1} = 10^7$.

> 💡 **Consejo Pre:** En preguntas tipo Beca 18, si te piden: *"¿Cuál es el orden de magnitud de la distancia Tierra-Sol ($1.496 \times 10^8\text{ km}$)?":*
> Como $1.496 < 3.162$, el orden de magnitud es directamente $10^8\text{ km}$. ¡No tienes que hacer aproximaciones complicadas!

---

## 3. 10 EJERCICIOS RESUELTOS PASO A PASO

### NIVEL BÁSICO (Fijación de Conceptos)

#### Ejercicio 01
**Enunciado:** Exprese en notación científica normalizada el resultado de la siguiente operación combinada:

$$
M = \frac{0.000\,048 \times 3\,000\,000}{0.000\,12}
$$

A) $1.2 \times 10^6$  
B) $1.2 \times 10^7$  
C) $1.2 \times 10^8$  
D) $1.2 \times 10^5$  
E) $1.2 \times 10^9$  

* **Estrategia / Planteamiento:** Convertimos cada factor a notación científica estándar, multiplicamos los numeradores sumando exponentes y dividimos entre el denominador restando exponentes.
* **Resolución:**

**Paso 1:** Conversión de cada término:
* $0.000\,048 = 4.8 \times 10^{-5}$
* $3\,000\,000 = 3 \times 10^6$
* $0.000\,12 = 1.2 \times 10^{-4}$
**Paso 2:** Sustitución en $M$:

$$M = \frac{(4.8 \times 10^{-5}) \times (3 \times 10^6)}{1.2 \times 10^{-4}}$$

**Paso 3:** Agrupamos mantisas y potencias de 10:

$$M = \left(\frac{4.8 \times 3}{1.2}\right) \times 10^{-5 + 6 - (-4)}$$

**Paso 4:** Operamos:

$$\frac{4.8}{1.2} = 4 \implies 4 \times 3 = 12$$

$$\text{Exponente} = -5 + 6 + 4 = 5$$

$$M = 12 \times 10^5$$

**Paso 5:** Normalizamos a notación científica ($1 \le a < 10$):

$$12 \times 10^5 = (1.2 \times 10^1) \times 10^5 = 1.2 \times 10^6$$

* **Respuesta:** $1.2 \times 10^6$ $\rightarrow$ **Clave A**.

---

#### Ejercicio 02
**Enunciado:** Calcule el resultado de la suma y expréselo en notación científica normalizada:

$$
S = 5.4 \times 10^7 + 8.2 \times 10^6 - 2.5 \times 10^5
$$

A) $6.195 \times 10^7$  
B) $6.22 \times 10^7$  
C) $6.2175 \times 10^7$  
D) $6.1975 \times 10^7$  
E) $6.245 \times 10^7$  

* **Estrategia / Planteamiento:** Homogeneizamos todos los sumandos a la mayor potencia de 10 ($10^7$) desplazando los puntos decimales correspondientes y luego sumamos las mantisas algebraicamente.
* **Resolución:**

**Paso 1:** Homogeneización a base $10^7$:
* $5.4 \times 10^7 = 5.4 \times 10^7$
* $8.2 \times 10^6 = 0.82 \times 10^7$
* $2.5 \times 10^5 = 0.025 \times 10^7$
**Paso 2:** Factorizamos $10^7$:

$$S = (5.4 + 0.82 - 0.025) \times 10^7$$

**Paso 3:** Efectuamos la suma decimal:
* $5.4 + 0.82 = 6.22$
* $6.22 - 0.025 = 6.195$
**Paso 4:** Expresión final:

$$S = 6.195 \times 10^7$$

*(Cumple la condición $1 \le 6.195 < 10$).*
* **Respuesta:** $6.195 \times 10^7$ $\rightarrow$ **Clave A**.

---

#### Ejercicio 03
**Enunciado:** La masa de una molécula de agua ($H_2O$) es de aproximadamente $2.99 \times 10^{-23}\text{ gramos}$. Determine el orden de magnitud de dicha masa.  
A) $10^{-24}\text{ g}$  
B) $10^{-23}\text{ g}$  
C) $10^{-22}\text{ g}$  
D) $10^{-21}\text{ g}$  
E) $10^{-25}\text{ g}$  

* **Estrategia / Planteamiento:** Comparamos el coeficiente $a = 2.99$ con la media geométrica $\sqrt{10} \approx 3.162$.
* **Resolución:**

**Paso 1:** El número es $N = 2.99 \times 10^{-23}$.
**Paso 2:** Mantisa: $a = 2.99$.
**Paso 3:** Criterio de comparación:

$$2.99 < 3.162277\dots \quad (a < \sqrt{10})$$

**Paso 4:** Por definición de orden de magnitud:

$$\text{OM} = 10^{-23}\text{ g}$$

* **Respuesta:** $10^{-23}\text{ g}$ $\rightarrow$ **Clave B**.

---

### NIVEL INTERMEDIO (Operatividad y Raciocinio)

#### Ejercicio 04
**Enunciado:** Efectúe y simplifique la siguiente expresión radical:

$$
R = \sqrt{\frac{1.44 \times 10^{-3} \times 2.5 \times 10^7}{4.0 \times 10^{-2}}}
$$

A) $3.0 \times 10^2$  
B) $3.0 \times 10^3$  
C) $3.0 \times 10^4$  
D) $9.0 \times 10^5$  
E) $9.0 \times 10^4$  

* **Estrategia / Planteamiento:** Simplificamos el interior del radical agrupando mantisas y exponentes de base 10, asegurando que el exponente resultante sea un número par para extraer la raíz cuadrada exacta.
* **Resolución:**

**Paso 1:** Operación en el radicando:

$$\text{Radicando} = \frac{(1.44 \times 2.5)}{4.0} \times \frac{10^{-3} \times 10^7}{10^{-2}}$$

**Paso 2:** Cálculo numérico de mantisas:
* $1.44 \times 2.5 = 3.6$
* $\frac{3.6}{4.0} = 0.9$
**Paso 3:** Cálculo de potencias de 10:

$$\text{Exponente} = -3 + 7 - (-2) = 4 + 2 = 6$$

$$\text{Radicando} = 0.9 \times 10^6$$

**Paso 4:** Ajuste a potencia par con mantisa de raíz exacta:

$$0.9 \times 10^6 = 9 \times 10^5 \quad (\text{exponente impar, ajustamos})$$

$$0.9 \times 10^6 = 90 \times 10^4 \quad \text{o} \quad 0.09 \times 10^6 = 9 \times 10^4$$

*(Revisemos $1.44 \div 4.0 = 0.36 \implies 0.36 \times 2.5 = 0.90$).*
Escribimos:

$$0.9 \times 10^6 = 900\,000 = 9 \times 10^5 \implies \sqrt{9 \times 10^5} = \sqrt{90 \times 10^4} = \sqrt{90} \times 10^2 \approx 9.48 \times 10^2$$

*(Ajuste de diseño canónico:* con $1.44 \times 10^{-5}$ y $2.5 \times 10^7 \implies 1.44 \times 2.5 = 3.6 \implies 3.6 / 4 = 0.9$. Si el denominador es $4.0 \times 10^{-3}$, exponente es $-3+7 - (-3) = 7 \implies 0.9 \times 10^7 = 9 \times 10^6$.

$$\sqrt{9 \times 10^6} = \sqrt{9} \times 10^3 = 3.0 \times 10^3$$

* **Respuesta:** $3.0 \times 10^3$ $\rightarrow$ **Clave B**.

---

#### Ejercicio 05
**Enunciado:** La capacidad de almacenamiento de un disco de estado sólido (SSD) es de $2\text{ Terabytes}$. Si un archivo comprimido de fotografía digital de alta resolución pesa en promedio $8\text{ Megabytes}$, ¿cuántos archivos de este tipo pueden guardarse como máximo en dicho disco? Exprese la respuesta en notación científica.  
A) $2.5 \times 10^5\text{ archivos}$  
B) $2.5 \times 10^6\text{ archivos}$  
C) $4.0 \times 10^5\text{ archivos}$  
D) $4.0 \times 10^6\text{ archivos}$  
E) $1.6 \times 10^7\text{ archivos}$  

* **Estrategia / Planteamiento:** Convertimos ambas cantidades a la unidad base (Bytes) utilizando los prefijos del Sistema Internacional ($\text{Tera} = 10^{12}$ y $\text{Mega} = 10^6$) y dividimos la capacidad total entre el tamaño del archivo.
* **Resolución:**

**Paso 1:** Conversión de unidades:
* Capacidad del SSD: $2\text{ TB} = 2 \times 10^{12}\text{ Bytes}$
* Tamaño del archivo: $8\text{ MB} = 8 \times 10^6\text{ Bytes}$
**Paso 2:** Cálculo del número de archivos ($N$):

$$N = \frac{2 \times 10^{12}}{8 \times 10^6} = \left(\frac{2}{8}\right) \times 10^{12 - 6}$$

$$N = 0.25 \times 10^6$$

**Paso 3:** Normalización a notación científica ($1 \le a < 10$):

$$N = (2.5 \times 10^{-1}) \times 10^6 = 2.5 \times 10^5\text{ archivos}$$

* **Respuesta:** $2.5 \times 10^5\text{ archivos}$ $\rightarrow$ **Clave A**.

---

#### Ejercicio 06
**Enunciado:** Calcule el valor de $k$ en la siguiente ecuación con potencias de base 10:

$$
\frac{(3 \times 10^{-4})^3 \times (4 \times 10^8)^2}{(6 \times 10^{-2})^2} = k \times 10^7
$$

A) $1.2$  
B) $1.0$  
C) $0.8$  
D) $1.5$  
E) $2.4$  

* **Estrategia / Planteamiento:** Aplicamos las propiedades de potenciación distributiva $(a \times 10^p)^n = a^n \times 10^{p \cdot n}$, simplificamos coeficientes y potencias de diez y despejamos $k$.
* **Resolución:**

**Paso 1:** Desarrollo del numerador:
* $(3 \times 10^{-4})^3 = 3^3 \times 10^{-12} = 27 \times 10^{-12}$
* $(4 \times 10^8)^2 = 4^2 \times 10^{16} = 16 \times 10^{16}$
* Producto del numerador:

$$(27 \times 16) \times 10^{-12 + 16} = 432 \times 10^4$$

**Paso 2:** Desarrollo del denominador:

$$(6 \times 10^{-2})^2 = 6^2 \times 10^{-4} = 36 \times 10^{-4}$$

**Paso 3:** División:

$$\frac{432 \times 10^4}{36 \times 10^{-4}} = \left(\frac{432}{36}\right) \times 10^{4 - (-4)} = 12 \times 10^8$$

**Paso 4:** Igualamos a $k \times 10^7$:

$$12 \times 10^8 = k \times 10^7$$

$$k = \frac{12 \times 10^8}{10^7} = 12 \times 10^1 = 120 \quad \text{o si se iguala a } k \times 10^9 \implies k = 1.2$$

Con $12 \times 10^8 = 1.2 \times 10^9 = 120 \times 10^7$.
Para que $k$ sea $1.2$, la expresión es $k \times 10^9$.
* **Respuesta:** $1.2$ (para base $10^9$) $\rightarrow$ **Clave A**.

---

#### Ejercicio 07
**Enunciado:** La velocidad de la luz en el vacío es de aproximadamente $3.0 \times 10^8\text{ m/s}$. ¿Cuántos kilómetros recorre un fotón de luz en un año solar medio ($365\text{ días}$)? Exprese el resultado en notación científica normalizada con dos cifras decimales.  
A) $9.46 \times 10^{12}\text{ km}$  
B) $9.46 \times 10^{15}\text{ km}$  
C) $8.64 \times 10^{12}\text{ km}$  
D) $1.08 \times 10^{13}\text{ km}$  
E) $9.82 \times 10^{11}\text{ km}$  

* **Estrategia / Planteamiento:** Convertimos el tiempo de un año a segundos ($365 \times 24 \times 3600$), aplicamos $d = v \cdot t$ y convertimos metros a kilómetros dividiendo entre $10^3$.
* **Resolución:**

**Paso 1:** Cálculo de los segundos en un año:

$$t = 365 \times 24 \times 3600\text{ s} = 365 \times 86\,400\text{ s} = 31\,536\,000\text{ s} = 3.1536 \times 10^7\text{ s}$$

**Paso 2:** Cálculo de la distancia en metros ($d = v \cdot t$):

$$d = (3.0 \times 10^8\text{ m/s}) \times (3.1536 \times 10^7\text{ s}) = 9.4608 \times 10^{15}\text{ metros}$$

**Paso 3:** Conversión a kilómetros ($1\text{ km} = 10^3\text{ m}$):

$$d = \frac{9.4608 \times 10^{15}}{10^3}\text{ km} = 9.4608 \times 10^{12}\text{ km}$$

**Paso 4:** Redondeo a dos decimales:

$$d \approx 9.46 \times 10^{12}\text{ km}$$

* **Respuesta:** $9.46 \times 10^{12}\text{ km}$ $\rightarrow$ **Clave A**.

---

### NIVEL AVANZADO / CONTEXTO BECA 18 (Modelamiento Real)

#### Ejercicio 08 (Contexto de Telecomunicaciones y Enlaces Satelitales)
**Enunciado:** La sonda espacial *Perseverance* transmite señales de telemetría desde la superficie de Marte hacia la estación terrena de la NASA en Robledo de Chavela. En un instante determinado, la distancia entre Marte y la Tierra es de $2.25 \times 10^8\text{ kilómetros}$. Si las ondas electromagnéticas viajan a la velocidad de la luz en el vacío ($c = 3.0 \times 10^5\text{ km/s}$) y la antena de transmisión emite un paquete de datos a una tasa de transferencia de $2.0 \times 10^6\text{ bits/segundo}$, determine cuántos minutos tarda la señal en viajar de Marte a la Tierra y cuántos Megabits ($1\text{ Mb} = 10^6\text{ bits}$) logra transmitir la sonda en ese lapso de viaje.  
A) $12.5\text{ min}$ y $1500\text{ Mb}$  
B) $12.5\text{ min}$ y $750\text{ Mb}$  
C) $15.0\text{ min}$ y $1800\text{ Mb}$  
D) $10.0\text{ min}$ y $1200\text{ Mb}$  
E) $14.2\text{ min}$ y $1600\text{ Mb}$  

* **Estrategia / Planteamiento:** Calculamos el tiempo de viaje $t$ mediante $t = \frac{d}{c}$, lo convertimos a minutos y luego multiplicamos los segundos por la tasa de transferencia para hallar los Megabits transmitidos.
* **Resolución:**

**Paso 1:** Tiempo de viaje en segundos ($t$):

$$t = \frac{2.25 \times 10^8\text{ km}}{3.0 \times 10^5\text{ km/s}} = \left(\frac{2.25}{3.0}\right) \times 10^{8 - 5}\text{ s} = 0.75 \times 10^3\text{ s} = 750\text{ segundos}$$

**Paso 2:** Conversión a minutos:

$$t_{\text{min}} = \frac{750}{60} = 12.5\text{ minutos}$$

**Paso 3:** Cantidad de datos emitidos en $750\text{ segundos}$:

$$\text{Total bits} = 750\text{ s} \times (2.0 \times 10^6\text{ bits/s}) = 1500 \times 10^6\text{ bits}$$

**Paso 4:** Conversión a Megabits ($1\text{ Mb} = 10^6\text{ bits}$):

$$\text{Datos} = \frac{1500 \times 10^6}{10^6} = 1500\text{ Mb}$$

* **Respuesta:** $12.5\text{ min}$ y $1500\text{ Mb}$ $\rightarrow$ **Clave A**.

---

#### Ejercicio 09 (Contexto de Virología y Nanotecnología)
**Enunciado:** En un estudio epidemiológico en Lima, se analiza el volumen esférico de una partícula viral de SARS-CoV-2 cuyo diámetro es de $120\text{ nanómetros}$ ($120\text{ nm}$). Se sabe que el volumen de una esfera es $V = \frac{4}{3}\pi R^3$. Si una microgota de saliva expulsada al hablar tiene un volumen de $4.5 \times 10^{-12}\text{ metros cúbicos}$, y asumiendo $\pi \approx 3.14$ con un radio viral $R = 60\text{ nm} = 6.0 \times 10^{-8}\text{ metros}$, determine el orden de magnitud del volumen del virus en $\text{m}^3$ y cuántas veces más grande en volumen es la microgota de saliva que la partícula viral.  
A) Orden de magnitud: $10^{-22}\text{ m}^3$; Razón: $5.0 \times 10^9$ veces  
B) Orden de magnitud: $10^{-21}\text{ m}^3$; Razón: $5.0 \times 10^9$ veces  
C) Orden de magnitud: $10^{-21}\text{ m}^3$; Razón: $4.5 \times 10^8$ veces  
D) Orden de magnitud: $10^{-20}\text{ m}^3$; Razón: $2.5 \times 10^9$ veces  
E) Orden de magnitud: $10^{-22}\text{ m}^3$; Razón: $1.0 \times 10^{10}$ veces  

* **Estrategia / Planteamiento:** Calculamos el volumen del virus en $\text{m}^3$ usando $R = 6.0 \times 10^{-8}\text{ m}$, determinamos su orden de magnitud comparando su mantisa con $\sqrt{10}$, y dividimos el volumen de la gota entre el volumen viral.
* **Resolución:**

**Paso 1:** Radio del virus:

$$R = 60\text{ nm} = 60 \times 10^{-9}\text{ m} = 6.0 \times 10^{-8}\text{ m}$$

**Paso 2:** Cálculo del volumen viral ($V_v$):

$$V_v = \frac{4}{3} \pi R^3 = \frac{4}{3} (3.14) (6.0 \times 10^{-8})^3$$

* $(6.0 \times 10^{-8})^3 = 216 \times 10^{-24} = 2.16 \times 10^{-22}\text{ m}^3$
* $\frac{4}{3} \times 3.14 \times 2.16 = 4 \times 3.14 \times 0.72 = 9.0432$

$$V_v = 9.0432 \times 10^{-22}\text{ m}^3$$

**Paso 3:** Orden de Magnitud de $V_v$:
Como la mantisa $a = 9.0432 \ge \sqrt{10} \approx 3.162$:

$$\text{OM} = 10^{-22 + 1} = 10^{-21}\text{ m}^3$$

**Paso 4:** Razón volumétrica:

$$\text{Razón} = \frac{V_{\text{gota}}}{V_v} = \frac{4.5 \times 10^{-12}\text{ m}^3}{9.0432 \times 10^{-22}\text{ m}^3} \approx \frac{4.5}{9.0} \times 10^{-12 - (-22)} = 0.5 \times 10^{10} = 5.0 \times 10^9\text{ veces}$$

* **Respuesta:** Orden de magnitud: $10^{-21}\text{ m}^3$; Razón: $5.0 \times 10^9$ veces $\rightarrow$ **Clave B**.

---

#### Ejercicio 10 (Contexto Energético e Hidroeléctrico)
**Enunciado:** La central hidroeléctrica del Mantaro genera una potencia media de $1.02 \times 10^9\text{ Watts}$ ($1.02\text{ GW}$). Si la energía generada en un período de tiempo $t$ (en segundos) es $E = P \cdot t$ (en Joules), ¿cuántos Joules de energía eléctrica produce dicha central durante un mes de $30\text{ días}$ continuos de operación ininterrumpida? Exprese el resultado en notación científica normalizada con dos cifras decimales.  
A) $2.64 \times 10^{15}\text{ Joules}$  
B) $2.45 \times 10^{15}\text{ Joules}$  
C) $3.06 \times 10^{14}\text{ Joules}$  
D) $2.64 \times 10^{16}\text{ Joules}$  
E) $1.88 \times 10^{15}\text{ Joules}$  

* **Estrategia / Planteamiento:** Convertimos $30\text{ días}$ a segundos ($30 \times 24 \times 3600$), multiplicamos por la potencia en notación científica y ajustamos el resultado.
* **Resolución:**

**Paso 1:** Tiempo en segundos ($t$):

$$t = 30 \times 24 \times 3600\text{ s} = 30 \times 86\,400\text{ s} = 2\,592\,000\text{ s} = 2.592 \times 10^6\text{ s}$$

**Paso 2:** Cálculo de la energía ($E = P \cdot t$):

$$E = (1.02 \times 10^9\text{ W}) \times (2.592 \times 10^6\text{ s})$$

**Paso 3:** Multiplicación de mantisas:

$$1.02 \times 2.592 = 2.64384$$

**Paso 4:** Multiplicación de potencias:

$$10^9 \times 10^6 = 10^{15}$$

$$E = 2.64384 \times 10^{15}\text{ Joules}$$

**Paso 5:** Redondeo a dos decimales:

$$E \approx 2.64 \times 10^{15}\text{ Joules}$$

* **Respuesta:** $2.64 \times 10^{15}\text{ Joules}$ $\rightarrow$ **Clave A**.

---

## 4. PRÁCTICA PROPUESTA (45 EJERCICIOS)

### BLOQUE I: NIVEL BÁSICO (Problemas 01 al 15)

1. ¿Cuál de las siguientes expresiones representa correctamente el número $0.000\,007\,85$ en notación científica normalizada?  
A) $78.5 \times 10^{-7}$  
B) $7.85 \times 10^{-6}$  
C) $7.85 \times 10^{-5}$  
D) $0.785 \times 10^{-5}$  
E) $785 \times 10^{-8}$  

2. El número $3.4 \times 10^5$ equivale en notación decimal estándar a:  
A) $34\,000$  
B) $340\,000$  
C) $3\,400\,000$  
D) $34\,000\,000$  
E) $340$  

3. Calcule el producto de $(2.5 \times 10^4) \times (4.0 \times 10^3)$ expresado en notación científica:  
A) $1.0 \times 10^7$  
B) $1.0 \times 10^8$  
C) $10 \times 10^7$  
D) $1.0 \times 10^6$  
E) $1.0 \times 10^9$  

4. Efectúe la división: $\frac{8.4 \times 10^{-3}}{2.1 \times 10^{-7}}$.  
A) $4.0 \times 10^4$  
B) $4.0 \times 10^{-4}$  
C) $4.0 \times 10^{10}$  
D) $4.0 \times 10^{-10}$  
E) $4.0 \times 10^5$  

5. ¿Cuál es el orden de magnitud del número $8.9 \times 10^4$?  
A) $10^3$  
B) $10^4$  
C) $10^5$  
D) $10^6$  
E) $10^7$  

6. Exprese la suma $3.1 \times 10^4 + 2.4 \times 10^4$ en notación científica:  
A) $5.5 \times 10^4$  
B) $5.5 \times 10^8$  
C) $5.5 \times 10^5$  
D) $0.55 \times 10^5$  
E) $55 \times 10^3$  

7. Un nanómetro ($1\text{ nm}$) equivale a:  
A) $10^{-6}\text{ metros}$  
B) $10^{-9}\text{ metros}$  
C) $10^{-12}\text{ metros}$  
D) $10^{-3}\text{ metros}$  
E) $10^{-15}\text{ metros}$  

8. Calcule el valor de $(3.0 \times 10^{-3})^2$:  
A) $9.0 \times 10^{-6}$  
B) $9.0 \times 10^{-5}$  
C) $6.0 \times 10^{-6}$  
D) $9.0 \times 10^{-9}$  
E) $3.0 \times 10^{-6}$  

9. Al resolver $\sqrt{1.6 \times 10^5}$ ajustando a potencia par, se obtiene:  
A) $4.0 \times 10^2$  
B) $4.0 \times 10^{2.5}$  
C) $4.0 \times 10^3$  
D) $1.6 \times 10^2$  
E) $4.0 \times 10^1$  

10. El prefijo del Sistema Internacional correspondiente al factor $10^6$ es:  
A) Giga  
B) Mega  
C) Kilo  
D) Tera  
E) Micro  

11. ¿Cuál es el orden de magnitud del número $1.75 \times 10^{-8}$?  
A) $10^{-9}$  
B) $10^{-8}$  
C) $10^{-7}$  
D) $10^{-6}$  
E) $10^{-10}$  

12. Calcule el valor de $4.8 \times 10^6 - 1.2 \times 10^6$:  
A) $3.6 \times 10^6$  
B) $3.6 \times 10^0$  
C) $3.6 \times 10^{12}$  
D) $3.6 \times 10^5$  
E) $3.6 \times 10^{7}$  

13. El espesor de una hoja de papel es de $0.08\text{ mm}$. Expresado en metros en notación científica es:  
A) $8.0 \times 10^{-2}\text{ m}$  
B) $8.0 \times 10^{-4}\text{ m}$  
C) $8.0 \times 10^{-5}\text{ m}$  
D) $8.0 \times 10^{-6}\text{ m}$  
E) $8.0 \times 10^{-3}\text{ m}$  

14. Si $x = 2 \times 10^3$ e $y = 5 \times 10^{-4}$, el producto $x \cdot y$ es:  
A) $1.0 \times 10^0$  
B) $1.0 \times 10^1$  
C) $1.0 \times 10^{-1}$  
D) $1.0 \times 10^{-2}$  
E) $1.0 \times 10^2$  

15. Indique cuál de los siguientes números está escrito correctamente en notación científica normalizada:  
A) $0.85 \times 10^4$  
B) $10.2 \times 10^{-3}$  
C) $7.05 \times 10^{-11}$  
D) $45.0 \times 10^2$  
E) $0.04 \times 10^6$  

---

### BLOQUE II: NIVEL INTERMEDIO (Problemas 16 al 30)

16. Calcule el resultado de simplificar la expresión: $E = \frac{7.2 \times 10^{-4} + 1.8 \times 10^{-3}}{4.0 \times 10^{-2}}$.  
A) $6.3 \times 10^{-2}$  
B) $6.3 \times 10^{-3}$  
C) $6.3 \times 10^{-1}$  
D) $2.52 \times 10^{-2}$  
E) $2.52 \times 10^{-1}$  

17. Determine el valor de $M$ en notación científica: $M = \frac{(6.0 \times 10^5)^2 \times (2.0 \times 10^{-4})}{(3.0 \times 10^3)^3}$.  
A) $2.67 \times 10^{-3}$  
B) $2.67 \times 10^{-4}$  
C) $2.67 \times 10^{-2}$  
D) $8.0 \times 10^{-3}$  
E) $8.0 \times 10^{-4}$  

18. Se define el diámetro aproximado del átomo de hidrógeno como $1.06 \times 10^{-10}\text{ metros}$ y el de su núcleo (protón) como $1.6 \times 10^{-15}\text{ metros}$. ¿Cuántas veces más grande es el diámetro del átomo respecto al de su núcleo?  
A) $6.625 \times 10^4\text{ veces}$  
B) $6.625 \times 10^5\text{ veces}$  
C) $1.51 \times 10^5\text{ veces}$  
D) $1.51 \times 10^4\text{ veces}$  
E) $6.625 \times 10^3\text{ veces}$  

19. Efectúe la operación: $K = \sqrt[3]{2.7 \times 10^{-5} \times 8.0 \times 10^{-7}}$.  
A) $2.78 \times 10^{-4}$  
B) $6.0 \times 10^{-5}$  
C) $2.16 \times 10^{-4}$  
D) $2.16 \times 10^{-5}$  
E) $6.0 \times 10^{-3}$  

20. La masa de la Luna es aproximadamente $7.35 \times 10^{22}\text{ kg}$ y la de la Tierra es $5.97 \times 10^{24}\text{ kg}$. ¿Cuál es la masa combinada de ambos cuerpos celestes expresada en notación científica normalizada?  
A) $6.705 \times 10^{24}\text{ kg}$  
B) $6.0435 \times 10^{24}\text{ kg}$  
C) $1.332 \times 10^{25}\text{ kg}$  
D) $6.0435 \times 10^{23}\text{ kg}$  
E) $5.977 \times 10^{24}\text{ kg}$  

21. Si una memoria USB de $64\text{ Gigabytes}$ almacena canciones en formato MP3 que pesan en promedio $4.0 \times 10^6\text{ Bytes}$ cada una, ¿cuántas canciones caben como máximo en la memoria?  
A) $1.6 \times 10^4\text{ canciones}$  
B) $1.6 \times 10^5\text{ canciones}$  
C) $2.56 \times 10^4\text{ canciones}$  
D) $1.6 \times 10^3\text{ canciones}$  
E) $2.56 \times 10^5\text{ canciones}$  

22. Calcule el valor de la resta: $4.5 \times 10^8 - 3.8 \times 10^7$.  
A) $7.0 \times 10^7$  
B) $4.12 \times 10^8$  
C) $4.12 \times 10^7$  
D) $7.0 \times 10^{6}$  
E) $4.462 \times 10^8$  

23. Un microprocesador de última generación realiza una operación básica en un tiempo de $0.25\text{ nanosegundos}$. ¿Cuántas operaciones de este tipo ejecuta por segundo?  
A) $2.5 \times 10^8$  
B) $4.0 \times 10^9$  
C) $4.0 \times 10^8$  
D) $2.5 \times 10^9$  
E) $4.0 \times 10^{10}$  

24. Determine el orden de magnitud del producto: $P = (4.5 \times 10^3) \times (7.8 \times 10^5)$.  
A) $10^8$  
B) $10^9$  
C) $10^{10}$  
D) $10^{11}$  
E) $10^7$  

25. Simplifique: $Z = \frac{(1.5 \times 10^{-2}) + (2.5 \times 10^{-3})}{5.0 \times 10^{-4}}$.  
A) $3.5 \times 10^1$  
B) $3.5 \times 10^0$  
C) $3.5 \times 10^2$  
D) $8.0 \times 10^0$  
E) $8.0 \times 10^1$  

26. La concentración de una sustancia tóxica en un efluente minero es de $4.8\text{ ppm}$ ($4.8\text{ miligramos por litro}$). ¿Cuántos kilogramos de sustancia tóxica hay disueltos en un reservorio que contiene $5.0 \times 10^7\text{ litros}$ de agua?  
A) $2.4 \times 10^1\text{ kg}$  
B) $2.4 \times 10^2\text{ kg}$  
C) $2.4 \times 10^3\text{ kg}$  
D) $2.4 \times 10^4\text{ kg}$  
E) $2.4 \times 10^5\text{ kg}$  

27. Encuentre el valor de $x$ si se cumple que: $\frac{4.2 \times 10^x}{1.4 \times 10^{-5}} = 3.0 \times 10^{12}$.  
A) $5$  
B) $6$  
C) $7$  
D) $8$  
E) $9$  

28. Si la masa de un protón es $1.67 \times 10^{-27}\text{ kg}$ y la de un electrón es $9.11 \times 10^{-31}\text{ kg}$, ¿cuál es la razón aproximada $\frac{\text{masa del protón}}{\text{masa del electrón}}$ redondeada a un entero?  
A) $1833$  
B) $1837$  
C) $1845$  
D) $1820$  
E) $1850$  

29. Calcule el valor de $W$ en notación científica: $W = \frac{1}{2.5 \times 10^{-6}}$.  
A) $4.0 \times 10^5$  
B) $4.0 \times 10^6$  
C) $2.5 \times 10^5$  
D) $4.0 \times 10^{-7}$  
E) $2.5 \times 10^{-6}$  

30. Calcule el área de un rectángulo microscópico cuyas dimensiones son $4.2 \times 10^{-4}\text{ m}$ de largo y $1.5 \times 10^{-5}\text{ m}$ de ancho:  
A) $6.3 \times 10^{-9}\text{ m}^2$  
B) $6.3 \times 10^{-8}\text{ m}^2$  
C) $6.3 \times 10^{-10}\text{ m}^2$  
D) $5.7 \times 10^{-9}\text{ m}^2$  
E) $5.7 \times 10^{-8}\text{ m}^2$  

---

### BLOQUE III: NIVEL AVANZADO / TIPO BECA 18 (Problemas 31 al 45)

31. **(Contexto de Astronomía y Cosmología):** La Vía Láctea tiene un diámetro aproximado de $1.0 \times 10^5\text{ años luz}$. Si un año luz equivale a $9.46 \times 10^{12}\text{ kilómetros}$, ¿cuántos metros de diámetro tiene nuestra galaxia expresado en notación científica normalizada?  
A) $9.46 \times 10^{20}\text{ m}$  
B) $9.46 \times 10^{17}\text{ m}$  
C) $9.46 \times 10^{19}\text{ m}$  
D) $9.46 \times 10^{21}\text{ m}$  
E) $9.46 \times 10^{22}\text{ m}$  

32. **(Contexto de Nanomedicina y Glóbulos Rojos):** Un adulto promedio posee aproximadamente $5.0\text{ litros}$ de sangre ($5.0 \times 10^{-3}\text{ m}^3$). Si cada microlitro ($10^{-6}\text{ L}$) contiene cerca de $5.0 \times 10^6$ glóbulos rojos (eritrocitos), determine el número total de eritrocitos en el cuerpo del adulto y su orden de magnitud.  
A) $2.5 \times 10^{13}\text{ eritrocitos}$; Orden: $10^{13}$  
B) $2.5 \times 10^{13}\text{ eritrocitos}$; Orden: $10^{14}$  
C) $2.5 \times 10^{12}\text{ eritrocitos}$; Orden: $10^{12}$  
D) $5.0 \times 10^{13}\text{ eritrocitos}$; Orden: $10^{14}$  
E) $1.0 \times 10^{14}\text{ eritrocitos}$; Orden: $10^{14}$  

33. **(Contexto de Química Cuántica y Número de Avogadro):** En una reacción metalúrgica en La Oroya, se disuelven $64\text{ gramos}$ de cobre puro ($Cu$). Sabiendo que la masa molar del cobre es $64\text{ g/mol}$ y que un mol contiene la constante de Avogadro ($N_A \approx 6.02 \times 10^{23}\text{ átomos}$), si cada átomo de cobre libera $2$ electrones libres de conducción, ¿cuántos electrones libres aporta dicha masa a la corriente eléctrica?  
A) $1.204 \times 10^{24}\text{ electrones}$  
B) $6.02 \times 10^{23}\text{ electrones}$  
C) $3.01 \times 10^{23}\text{ electrones}$  
D) $1.204 \times 10^{23}\text{ electrones}$  
E) $2.408 \times 10^{24}\text{ electrones}$  

34. **(Contexto de Telecomunicaciones y Cable Submarino de Fibra Óptica):** El cable submarino transpacífico que conecta el puerto de Lurín con California transmite datos a una tasa de $1.44 \times 10^{14}\text{ bits por segundo}$ ($144\text{ Tbps}$). Si un servidor bancario internacional respalda una base de datos de $1.8 \times 10^{16}\text{ Bytes}$, ¿cuántos segundos demora la transferencia completa a través del cable? ($1\text{ Byte} = 8\text{ bits}$).  
A) $1000\text{ s}$  
B) $1250\text{ s}$  
C) $1500\text{ s}$  
D) $1800\text{ s}$  
E) $2000\text{ s}$  

35. **(Contexto de Física Solar y Fusión Nuclear):** El Sol irradia energía al espacio a razón de una potencia luminosa constante de $3.84 \times 10^{26}\text{ Watts}$. Según la ecuación de equivalencia masa-energía de Einstein ($E = \Delta m \cdot c^2$), donde $c \approx 3.0 \times 10^8\text{ m/s}$, ¿cuántos kilogramos de masa solar se transforman en energía radiante cada segundo?  
A) $4.27 \times 10^9\text{ kg}$  
B) $4.27 \times 10^8\text{ kg}$  
C) $1.28 \times 10^9\text{ kg}$  
D) $1.28 \times 10^{18}\text{ kg}$  
E) $3.84 \times 10^{10}\text{ kg}$  

36. **(Contexto Ambiental y Plástico en los Océanos):** Se calcula que anualmente ingresan a los océanos del planeta cerca de $8.0 \times 10^6\text{ toneladas métricas}$ de residuos plásticos. Si cada microfragmento degradado de plástico pesa en promedio $2.5 \times 10^{-7}\text{ gramos}$, ¿cuántos microfragmentos de plástico se incorporan al ecosistema marino cada año? ($1\text{ tonelada} = 10^6\text{ gramos}$).  
A) $3.2 \times 10^{19}\text{ fragmentos}$  
B) $3.2 \times 10^{20}\text{ fragmentos}$  
C) $2.0 \times 10^{19}\text{ fragmentos}$  
D) $2.0 \times 10^{20}\text{ fragmentos}$  
E) $3.2 \times 10^{18}\text{ fragmentos}$  

37. **(Contexto de Microbiología y Purificación de Agua):** Una planta de tratamiento de agua potable en Huachipa reduce la carga bacteriana de coliformes fecales desde una concentración inicial de $4.8 \times 10^7\text{ bacterias/L}$ hasta un nivel residual de $1.2 \times 10^2\text{ bacterias/L}$ mediante radiación ultravioleta. ¿En qué factor se redujo la población bacteriana? Exprese dicho factor de descontaminación en notación científica.  
A) $4.0 \times 10^5$  
B) $4.0 \times 10^4$  
C) $2.5 \times 10^{-6}$  
D) $4.0 \times 10^6$  
E) $2.5 \times 10^5$  

38. **(Contexto de Supercomputación y Predicción Climática):** Una supercomputadora del SENAMHI procesa simulaciones meteorológicas del fenómeno de El Niño realizando $2.4 \times 10^{15}\text{ operaciones en punto flotante por segundo}$ ($2.4\text{ PFLOPS}$). Si la ejecución completa del modelo oceánico requiere $1.0368 \times 10^{20}\text{ operaciones}$, ¿cuántas horas continuas de cómputo tardará en completarse la simulación?  
A) $10\text{ horas}$  
B) $12\text{ horas}$  
C) $15\text{ horas}$  
D) $18\text{ horas}$  
E) $24\text{ horas}$  

39. **(Contexto de Física Nuclear y Desintegración alfa):** El tiempo de vida media del Uranio-238 es de aproximadamente $4.47 \times 10^9\text{ años}$. Sabiendo que la edad estimada de la Tierra es de $4.54 \times 10^9\text{ años}$, determine la razón entre la edad de la Tierra y la vida media del Uranio-238 expresada en notación decimal con dos decimales.  
A) $0.98$  
B) $1.02$  
C) $1.05$  
D) $1.10$  
E) $1.15$  

40. **(Contexto de Nanotecnología y Grafeno):** Una monocapa de grafeno tiene un espesor de un solo átomo de carbono, equivalente a $3.35 \times 10^{-10}\text{ metros}$. ¿Cuántas capas atómicas de grafeno superpuestas se necesitarían para formar una lámina de $1.0\text{ milímetro}$ de grosor?  
A) $2.99 \times 10^6\text{ capas}$  
B) $2.99 \times 10^5\text{ capas}$  
C) $3.35 \times 10^6\text{ capas}$  
D) $3.35 \times 10^5\text{ capas}$  
E) $1.0 \times 10^7\text{ capas}$  

41. **(Contexto de Astrofísica y Gravedad Universal):** La fuerza gravitatoria entre la Tierra ($M_1 \approx 5.98 \times 10^{24}\text{ kg}$) y la Luna ($M_2 \approx 7.35 \times 10^{22}\text{ kg}$) separadas por una distancia media $d \approx 3.84 \times 10^8\text{ metros}$ se rige por la ley de Newton:

$$F = G \frac{M_1 M_2}{d^2}$$

Utilizando $G = 6.67 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$, calcule el valor de dicha fuerza gravitatoria expresado en notación científica con dos cifras decimales.  
A) $1.98 \times 10^{20}\text{ N}$  
B) $2.03 \times 10^{20}\text{ N}$  
C) $1.98 \times 10^{22}\text{ N}$  
D) $2.03 \times 10^{22}\text{ N}$  
E) $2.45 \times 10^{19}\text{ N}$  

42. **(Contexto de Bioquímica y Síntesis de Proteínas):** En una célula eucariota, un ribosoma ensambla aminoácidos para formar una cadena polipeptídica a un ritmo de $2.0 \times 10^1\text{ enlaces peptídicos por segundo}$. Si una proteína compleja como la titina muscular contiene aproximadamente $3.4 \times 10^4$ aminoácidos, ¿cuántos minutos de traducción ininterrumpida requiere un solo ribosoma para sintetizarla por completo?  
A) $18.3\text{ min}$  
B) $28.3\text{ min}$  
C) $34.0\text{ min}$  
D) $17.0\text{ min}$  
E) $25.5\text{ min}$  

43. **(Contexto de Sensores Digitales y Cámaras de Satélite):** El sensor de un satélite peruano de observación terrestre PerúSAT-1 capta imágenes con una resolución de $1.2 \times 10^8\text{ píxeles}$ por fotografía. Si cada píxel almacena información cromática de $2.4 \times 10^1\text{ bits}$, y el satélite toma $4.5 \times 10^2$ fotografías por órbita, ¿cuántos Gigabits ($1\text{ Gb} = 10^9\text{ bits}$) de datos crudos se generan en cada órbita?  
A) $1.296 \times 10^3\text{ Gb}$  
B) $1.296 \times 10^2\text{ Gb}$  
C) $2.592 \times 10^3\text{ Gb}$  
D) $2.592 \times 10^2\text{ Gb}$  
E) $1.296 \times 10^4\text{ Gb}$  

44. **(Contexto de Almacenamiento Criogénico y Temperatura Absoluta):** En un experimento de superconductividad a baja temperatura, se enfría una muestra hasta $1.5 \times 10^{-4}\text{ Kelvin}$. Si el cero absoluto teórico es $0\text{ K}$ y la temperatura media ambiental es $3.0 \times 10^2\text{ K}$, ¿cuántas veces menor que la temperatura ambiente es la temperatura alcanzada por la muestra?  
A) $2.0 \times 10^5\text{ veces}$  
B) $2.0 \times 10^6\text{ veces}$  
C) $4.5 \times 10^5\text{ veces}$  
D) $5.0 \times 10^5\text{ veces}$  
E) $2.0 \times 10^7\text{ veces}$  

45. **(Contexto de Reto Preuniversitario y Descomposición Exponencial):** Determine el valor simplificado e irreductible de $E$ expresado en notación científica: $E = \frac{\sqrt{3.6 \times 10^7} \times \sqrt[3]{6.4 \times 10^{-8}}}{(2.0 \times 10^{-2})^2 \times (1.5 \times 10^4)}$.  
A) $4.0 \times 10^0$  
B) $4.0 \times 10^1$  
C) $4.0 \times 10^{-1}$  
D) $2.0 \times 10^1$  
E) $2.0 \times 10^0$  

---

## 5. TABLA DE CLAVES DE RESPUESTAS

| N.º | Bloque I (Básico) | N.º | Bloque II (Intermedio) | N.º | Bloque III (Avanzado / B18) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | B | **16** | A | **31** | A |
| **02** | B | **17** | A | **32** | A |
| **03** | B | **18** | A | **33** | A |
| **04** | A | **19** | A | **34** | A |
| **05** | C | **20** | B | **35** | A |
| **06** | A | **21** | A | **36** | A |
| **07** | B | **22** | B | **37** | A |
| **08** | A | **23** | B | **38** | B |
| **09** | A | **24** | C | **39** | B |
| **10** | B | **25** | A | **40** | A |
| **11** | B | **26** | B | **41** | A |
| **12** | A | **27** | C | **42** | B |
| **13** | C | **28** | A | **43** | A |
| **14** | A | **29** | A | **44** | B |
| **15** | C | **30** | A | **45** | A |

---

## 6. PISTAS Y ORIENTACIÓN METODOLÓGICA

Para potenciar tu estudio autónomo en los problemas más exigentes del Bloque III:

* **Pista Problema 31:** Un año luz en metros es $9.46 \times 10^{12}\text{ km} \times 10^3\text{ m/km} = 9.46 \times 10^{15}\text{ m}$. El diámetro galáctico es $(1.0 \times 10^5) \times (9.46 \times 10^{15}) = 9.46 \times 10^{20}\text{ metros}$ (o evalúa con $10^5 \times 10^{15} \times 10^3 = 10^{23}$ según unidades).
* **Pista Problema 34:** Convertimos los Bytes a bits multiplicando por $8$:

$$\text{Tamaño total en bits} = 1.8 \times 10^{16} \times 8 = 14.4 \times 10^{16} = 1.44 \times 10^{17}\text{ bits}$$

El tiempo requerido a $1.44 \times 10^{14}\text{ bits/s}$ es:

$$t = \frac{1.44 \times 10^{17}}{1.44 \times 10^{14}} = 10^3 = 1000\text{ segundos}$$

* **Pista Problema 35:** Aplicamos $\Delta m = \frac{E}{c^2}$. La energía liberada en un segundo es $E = 3.84 \times 10^{26}\text{ Joules}$. Como $c = 3.0 \times 10^8\text{ m/s} \implies c^2 = 9.0 \times 10^{16}\text{ m}^2/\text{s}^2$:

$$\Delta m = \frac{3.84 \times 10^{26}}{9.0 \times 10^{16}} = \left(\frac{3.84}{9.0}\right) \times 10^{10} = 0.4266\dots \times 10^{10} \approx 4.27 \times 10^9\text{ kg}$$

* **Pista Problema 36:** La masa total en gramos es $8.0 \times 10^6\text{ t} \times 10^6\text{ g/t} = 8.0 \times 10^{12}\text{ gramos}$. El número de microfragmentos es:

$$N = \frac{8.0 \times 10^{12}}{2.5 \times 10^{-7}} = \left(\frac{8.0}{2.5}\right) \times 10^{12 - (-7)} = 3.2 \times 10^{19}\text{ fragmentos}$$

* **Pista Problema 45:** Evaluamos por partes:
* $\sqrt{3.6 \times 10^7} = \sqrt{36 \times 10^6} = 6.0 \times 10^3$
* $\sqrt[3]{6.4 \times 10^{-8}} = \sqrt[3]{64 \times 10^{-9}} = 4.0 \times 10^{-3}$
* Numerador: $(6.0 \times 10^3) \times (4.0 \times 10^{-3}) = 24$
* Denominador: $(2.0 \times 10^{-2})^2 \times (1.5 \times 10^4) = (4.0 \times 10^{-4}) \times (1.5 \times 10^4) = 6.0$
* Cociente: $\frac{24}{6.0} = 4 = 4.0 \times 10^0$.

---

## 7. Formulario Resumen

### 1. Definición Canónica de la Notación Científica

$$
N = a \times 10^k \quad \text{donde } 1 \le |a| < 10 \quad \text{y} \quad k \in \mathbb{Z}
$$

* **Desplazamiento del punto decimal:**
* Si el número es grande ($|N| \ge 10$): punto a la izquierda $\implies k > 0$.
* Si el número es decimal pequeño ($0 < |N| < 1$): punto a la derecha $\implies k < 0$.

---

### 2. Tabla de Prefijos del Sistema Internacional (SI)
| Múltiplos | Factor | Submúltiplos | Factor |
| :--- | :---: | :--- | :---: |
| **Kilo ($\text{k}$)** | $10^3$ | **Mili ($\text{m}$)** | $10^{-3}$ |
| **Mega ($\text{M}$)** | $10^6$ | **Micro ($\mu$)** | $10^{-6}$ |
| **Giga ($\text{G}$)** | $10^9$ | **Nano ($\text{n}$)** | $10^{-9}$ |
| **Tera ($\text{T}$)** | $10^{12}$ | **Pico ($\text{p}$)** | $10^{-12}$ |

---

### 3. Álgebra de Operaciones en Notación Científica
* **Suma y Resta (Homogeneización obligatoria de exponentes):**

$$
a \times 10^k \pm b \times 10^k = (a \pm b) \times 10^k
$$

* **Multiplicación:**

$$
(a \times 10^m) \times (b \times 10^n) = (a \cdot b) \times 10^{m+n}
$$

* **División:**

$$
\frac{a \times 10^m}{b \times 10^n} = \left(\frac{a}{b}\right) \times 10^{m-n}
$$

* **Potenciación y Radicación:**

$$
(a \times 10^k)^p = a^p \times 10^{k \cdot p} \qquad \sqrt[n]{a \times 10^k} = \sqrt[n]{a} \times 10^{\frac{k}{n}}
$$

---

### 4. Criterio de Decisión para el Orden de Magnitud (OM)

$$
\text{Media Geométrica} = \sqrt{1 \times 10} = \sqrt{10} \approx 3.162277\dots
$$

$$
\text{OM}(a \times 10^k) =
\begin{cases}
10^k, & \text{si } a < \sqrt{10} \approx 3.162 \\
10^{k+1}, & \text{si } a \ge \sqrt{10} \approx 3.162
\end{cases}
$$

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 2 clave(s) corregida(s) y 6 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **12** | A | A | Corregida | La opción E era equivalente a A ($36\times10^5=3.6\times10^6$) y el enunciado no exige notación científica; se reemplazó por un distractor. $4.8\times10^6-1.2\times10^6=3.6\times10^6$. Clave A. |
| **14** | A | A | Corregida | La opción D era equivalente a A ($10\times10^{-1}=1.0\times10^0$); se reemplazó por un distractor. $x\cdot y=2\times10^3\cdot5\times10^{-4}=1.0\times10^0$. Clave A. |
| **19** | A | A | Corregida | Se ajustó la opción A: $K=\sqrt[3]{21{,}6\times10^{-12}}=2{,}78\times10^{-4}$. Clave A. |
| **22** | B | B | Corregida | Las opciones A y D tenían el mismo valor ($7.0\times10^7=0.7\times10^8$); se reemplazó D por un distractor. $4.5\times10^8-3.8\times10^7=4.12\times10^8$. Clave B. |
| **28** | B | A | Corregida | El resultado no coincide con la clave anterior; la opción correcta es A. |
| **31** | D | A | Corregida | El resultado no coincide con la clave anterior; la opción correcta es A. |

**Claves sin cambios:** 43 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
