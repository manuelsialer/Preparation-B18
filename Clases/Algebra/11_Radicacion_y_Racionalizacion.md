# Tema 11: Radicación y Racionalización

La radicación en el cuerpo de los números reales $\mathbb{R}$ es la operación matemática inversa de la potenciación que, dados dos números llamados **índice** $n \in \mathbb{N}$ ($n \geq 2$) y **radicando** o cantidad subradical $a$, tiene por objeto hallar un único número real $b$ denominado **raíz enésima**, tal que elevado a la potencia $n$ reproduzca con exactitud al radicando $a$:

$$
\sqrt[n]{a} = b \iff b^n = a
$$

Para garantizar la existencia y unicidad en el campo de los números reales ($\mathbb{R}$):
* Si el índice $n$ es **par**, el radicando debe ser estrictamente no negativo ($a \geq 0$). La raíz aritmética es siempre un número real no negativo: $b \geq 0$. Una de las identidades más cruciales del álgebra formal es:

$$
\sqrt[2k]{x^{2k}} = |x|
$$

* Si el índice $n$ es **impar**, el radicando puede ser cualquier número real ($a \in \mathbb{R}$), y la raíz $b$ conserva unívocamente el mismo signo que el radicando $a$: $\sqrt[3]{-8} = -2$.

La transformación de radicales dobles a radicales simples y la racionalización de denominadores son herramientas determinantes en el examen de preselección Beca 18, permitiendo el cálculo exacto de límites trigonométricos, cálculo de hipotenusas en topografía e ingeniería, simplificación de impedancias eléctricas y resolución analítica de inecuaciones irracionales.

---

## 1. Fundamentos de la Radicación y Valor Absoluto

La radicación en $\mathbb{R}$ exige considerar las condiciones de existencia para índices pares e impares:
* **Índice Par:** $\sqrt[2k]{a}$ existe en $\mathbb{R} \iff a \geq 0$. Su valor es estrictamente no negativo:

$$
\sqrt[2k]{x^{2k}} = |x|
$$

* **Índice Impar:** $\sqrt[2k+1]{a}$ está definida para todo $a \in \mathbb{R}$ y conserva el signo del radicando: $\sqrt[3]{-27} = -3$.

---

## 2. Radicales Dobles y su Transformación a Radicales Simples

Un radical doble es una expresión irracional que contiene en su interior otros radicales ligados por operaciones de adición o sustracción.

### 1.1 Radicales Dobles de la Forma $\sqrt{A \pm \sqrt{B}}$

Sean $A, B \in \mathbb{Q}^+$ con $A > \sqrt{B}$. Se pueden descomponer en la suma o diferencia de dos radicales simples de la forma:

$$
\sqrt{A \pm \sqrt{B}} = \sqrt{x} \pm \sqrt{y}
$$

Para que $x$ e $y$ sean números racionales ($\mathbb{Q}$), es condición indispensable que la cantidad $A^2 - B$ sea un **cuadrado perfecto** ($k^2, k \in \mathbb{Q}$). Se define la constante discriminante $C$:

$$
C = \sqrt{A^2 - B}
$$

A partir de $C$, los valores de los radicales simples se determinan mediante las fórmulas universales:

$$
x = \frac{A + C}{2}, \quad y = \frac{A - C}{2}
$$

Por lo tanto:

$$
\sqrt{A \pm \sqrt{B}} = \sqrt{\frac{A + C}{2}} \pm \sqrt{\frac{A - C}{2}}
$$

### 1.2 Regla Práctica de Transformación (Forma del Doble Producto)

Si el radical interior tiene coeficiente 2:

$$
\sqrt{(a + b) \pm 2\sqrt{ab}} = \sqrt{a} \pm \sqrt{b}, \quad (a > b > 0)
$$

Esta equivalencia se deduce directamente del desarrollo del binomio al cuadrado: $(\sqrt{a} \pm \sqrt{b})^2 = a + b \pm 2\sqrt{ab}$.

* **Estrategia Operativa:** Si el radical interior no posee el coeficiente 2, se introduce o extrae un factor 4 del radicando:

$$
\sqrt{A \pm \sqrt{B}} = \sqrt{A \pm 2\sqrt{\frac{B}{4}}}
$$

O bien, multiplicando y dividiendo por $\sqrt{2}$:

$$
\sqrt{A \pm \sqrt{B}} = \frac{\sqrt{2A \pm 2\sqrt{B}}}{\sqrt{2}}
$$

### 1.3 Radicales Dobles de Tres Términos

Tienen la estructura generada por el trinomio al cuadrado $(\sqrt{x} + \sqrt{y} + \sqrt{z})^2$:

$$
\sqrt{A + \sqrt{B} + \sqrt{C} + \sqrt{D}} = \sqrt{x} + \sqrt{y} + \sqrt{z}
$$

donde:
* $A = x + y + z$
* $\sqrt{B} = 2\sqrt{xy} \implies B = 4xy$
* $\sqrt{C} = 2\sqrt{yz} \implies C = 4yz$
* $\sqrt{D} = 2\sqrt{xz} \implies D = 4xz$

### 1.4 Radicales Dobles Cúbicos $\sqrt[3]{A \pm \sqrt{B}}$

Se descomponen en la forma $x \pm \sqrt{y}$, donde $A^2 - B = C^3$ (con $C \in \mathbb{Q}$). El valor de $x$ se obtiene resolviendo la ecuación cúbica:

$$
4x^3 - 3Cx - A = 0
$$

y la cantidad cuadrática $y$ se calcula como: $y = x^2 - C$.

---

## 3. Teoría de la Racionalización

Racionalizar una fracción consiste en transformar su denominador irracional en una expresión completamente racional (libre de radicales), multiplicando tanto el numerador como el denominador por un factor no nulo denominado **Factor Racionalizante (F.R.)**:

$$
\frac{N}{D} = \frac{N \cdot \text{F.R.}}{D \cdot \text{F.R.}} = \frac{N \cdot \text{F.R.}}{\text{Expresión Racional}}
$$

### 2.1 Caso 1: Denominador Monomio con Raíz Enésima

Para fracciones de la forma $\frac{N}{\sqrt[n]{a^k}}$ con $k < n$:

$$
\text{F.R.} = \sqrt[n]{a^{n - k}}
$$

El denominador resultante es: $\sqrt[n]{a^k} \cdot \sqrt[n]{a^{n - k}} = \sqrt[n]{a^n} = a$.

### 2.2 Caso 2: Denominador Binomio de Raíces Cuadradas

Para fracciones con denominadores $\sqrt{a} \pm \sqrt{b}$ o $a \pm \sqrt{b}$:
El Factor Racionalizante es la **expresión conjugada**, aprovechando la diferencia de cuadrados $(x + y)(x - y) = x^2 - y^2$:

* Si el denominador es $(\sqrt{a} + \sqrt{b})$, su $\text{F.R.} = (\sqrt{a} - \sqrt{b})$:

$$
(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = a - b
$$

* Si el denominador es $(\sqrt{a} - \sqrt{b})$, su $\text{F.R.} = (\sqrt{a} + \sqrt{b})$.

### 2.3 Caso 3: Denominador Binomio de Raíces Cúbicas

Para fracciones con denominadores $\sqrt[3]{a} \pm \sqrt[3]{b}$:
El Factor Racionalizante es el trinomio correspondiente a la suma o diferencia de cubos $(x \pm y)(x^2 \mp xy + y^2) = x^3 \pm y^3$:

* Si el denominador es $(\sqrt[3]{a} + \sqrt[3]{b})$, su $\text{F.R.} = \sqrt[3]{a^2} - \sqrt[3]{ab} + \sqrt[3]{b^2}$:

$$
(\sqrt[3]{a} + \sqrt[3]{b})(\sqrt[3]{a^2} - \sqrt[3]{ab} + \sqrt[3]{b^2}) = a + b
$$

* Si el denominador es $(\sqrt[3]{a} - \sqrt[3]{b})$, su $\text{F.R.} = \sqrt[3]{a^2} + \sqrt[3]{ab} + \sqrt[3]{b^2}$:

$$
(\sqrt[3]{a} - \sqrt[3]{b})(\sqrt[3]{a^2} + \sqrt[3]{ab} + \sqrt[3]{b^2}) = a - b
$$

### 2.4 Caso 4: Denominador Trinomio con Raíces Cuadradas

Para expresiones de la forma $\frac{N}{\sqrt{a} + \sqrt{b} + \sqrt{c}}$:
Se agrupan dos términos como uno solo: $[(\sqrt{a} + \sqrt{b}) + \sqrt{c}]$. Se multiplica primero por la conjugada $[(\sqrt{a} + \sqrt{b}) - \sqrt{c}]$, reduciendo el denominador a un binomio irracional, sobre el cual se aplica una segunda racionalización por diferencia de cuadrados.

### 2.5 Caso 5: Denominador Binomio de Orden Superior $\sqrt[n]{a} \pm \sqrt[n]{b}$

Se utilizan los cocientes notables:

$$
\text{F.R.} = \sqrt[n]{a^{n-1}} \mp \sqrt[n]{a^{n-2}b} + \dots \pm \sqrt[n]{b^{n-1}}
$$

---

## 4. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Descomposición de Radical Doble a Simple (Fórmula General)
Transformar a radicales simples:

$$
E = \sqrt{7 + \sqrt{40}}
$$

**Paso 1:** Identificamos los elementos de la forma general $A = 7$ y $B = 40$.

**Paso 2:** Calculamos la constante $C = \sqrt{A^2 - B}$:
$C = \sqrt{7^2 - 40} = \sqrt{49 - 40} = \sqrt{9} = 3$
Como $C = 3 \in \mathbb{Q}$, la transformación a radicales simples racionales es exacta.

**Paso 3:** Calculamos los radicandos simples $x$ e $y$:
$x = \frac{A + C}{2} = \frac{7 + 3}{2} = \frac{10}{2} = 5$
$y = \frac{A - C}{2} = \frac{7 - 3}{2} = \frac{4}{2} = 2$

**Paso 4:** Escribimos la descomposición:
$\sqrt{7 + \sqrt{40}} = \sqrt{x} + \sqrt{y} = \sqrt{5} + \sqrt{2}$

**Respuesta:** El radical doble transformado es $\sqrt{5} + \sqrt{2}$.

---

### Ejercicio 2: Método Práctico del Doble Producto
Descomponer a radicales simples:

$$
M = \sqrt{11 - 2\sqrt{30}}
$$

**Paso 1:** Identificamos la estructura $\sqrt{(a + b) - 2\sqrt{ab}}$.
Buscamos dos números reales $a$ y $b$ ($a > b$) tales que:
$a + b = 11$
$a \cdot b = 30$

**Paso 2:** Determinamos los pares de divisores de 30:
$1 \times 30 \implies 1 + 30 = 31$
$2 \times 15 \implies 2 + 15 = 17$
$3 \times 10 \implies 3 + 10 = 13$
$5 \times 6 \implies 5 + 6 = 11$ (Coincide exactamente).

**Paso 3:** Asignamos $a = 6$ y $b = 5$ (respetando $a > b$):
$\sqrt{11 - 2\sqrt{30}} = \sqrt{6} - \sqrt{5}$

**Respuesta:** La expresión reducida es $\sqrt{6} - \sqrt{5}$.

---

### Ejercicio 3: Acondicionamiento para el Doble Producto
Simplificar la expresión:

$$
K = \sqrt{4 + \sqrt{12}} - \sqrt{3}
$$

**Paso 1:** Extraemos un factor 4 del radical interior $\sqrt{12}$:
$\sqrt{12} = \sqrt{4 \times 3} = 2\sqrt{3}$

**Paso 2:** Reescribimos el radical doble en la forma práctica:
$\sqrt{4 + 2\sqrt{3}}$

**Paso 3:** Buscamos dos números que sumados den 4 y multiplicados den 3:
$a + b = 4$ y $a \cdot b = 3 \implies a = 3$ y $b = 1$.
$\sqrt{4 + 2\sqrt{3}} = \sqrt{3} + \sqrt{1} = \sqrt{3} + 1$

**Paso 4:** Sustituimos en la expresión $K$:
$K = (\sqrt{3} + 1) - \sqrt{3} = 1$

**Respuesta:** El valor simplificado de $K$ es 1.

---

### Ejercicio 4: Racionalización de Denominador Monomio
Racionalizar y simplificar:

$$
F = \frac{12}{\sqrt[5]{8}}
$$

**Paso 1:** Expresamos el radicando en su descomposición factorial en base prima:
$8 = 2^3 \implies \sqrt[5]{8} = \sqrt[5]{2^3}$

**Paso 2:** Determinamos el factor racionalizante:
$\text{F.R.} = \sqrt[5]{2^{5 - 3}} = \sqrt[5]{2^2} = \sqrt[5]{4}$

**Paso 3:** Multiplicamos numerador y denominador por el $\text{F.R.}$:
$F = \frac{12 \cdot \sqrt[5]{4}}{\sqrt[5]{2^3} \cdot \sqrt[5]{2^2}} = \frac{12\sqrt[5]{4}}{\sqrt[5]{2^5}} = \frac{12\sqrt[5]{4}}{2}$

**Paso 4:** Simplificamos la fracción numérica:
$F = 6\sqrt[5]{4}$

**Respuesta:** La expresión racionalizada es $6\sqrt[5]{4}$.

---

### Ejercicio 5: Racionalización por Conjugada Cuadrática
Racionalizar el denominador de la fracción:

$$
P = \frac{14}{\sqrt{11} - 2}
$$

**Paso 1:** Reconocemos el binomio irracional $(\sqrt{11} - 2)$. Su factor racionalizante conjugado es $(\sqrt{11} + 2)$.

**Paso 2:** Multiplicamos numerador y denominador por $(\sqrt{11} + 2)$:
$P = \frac{14(\sqrt{11} + 2)}{(\sqrt{11} - 2)(\sqrt{11} + 2)}$

**Paso 3:** Desarrollamos la diferencia de cuadrados en el denominador:
$(\sqrt{11})^2 - (2)^2 = 11 - 4 = 7$

**Paso 4:** Simplificamos con el numerador:
$P = \frac{14(\sqrt{11} + 2)}{7} = 2(\sqrt{11} + 2) = 2\sqrt{11} + 4$

**Respuesta:** La expresión racionalizada es $2\sqrt{11} + 4$.

---

### Ejercicio 6: Racionalización de Denominador Cúbico
Racionalizar la fracción:

$$
Q = \frac{10}{\sqrt[3]{7} - \sqrt[3]{2}}
$$

**Paso 1:** El denominador es de la forma $A - B$ con $A = \sqrt[3]{7}$ y $B = \sqrt[3]{2}$.
El factor racionalizante es el trinomio correspondiente a la diferencia de cubos:
$\text{F.R.} = A^2 + AB + B^2 = (\sqrt[3]{7})^2 + \sqrt[3]{7}\sqrt[3]{2} + (\sqrt[3]{2})^2 = \sqrt[3]{49} + \sqrt[3]{14} + \sqrt[3]{4}$

**Paso 2:** Multiplicamos numerador y denominador por el $\text{F.R.}$:
$Q = \frac{10(\sqrt[3]{49} + \sqrt[3]{14} + \sqrt[3]{4})}{(\sqrt[3]{7} - \sqrt[3]{2})(\sqrt[3]{49} + \sqrt[3]{14} + \sqrt[3]{4})}$

**Paso 3:** El denominador se reduce a la diferencia de cubos:
$(\sqrt[3]{7})^3 - (\sqrt[3]{2})^3 = 7 - 2 = 5$

**Paso 4:** Simplificamos el factor numérico:
$Q = \frac{10(\sqrt[3]{49} + \sqrt[3]{14} + \sqrt[3]{4})}{5} = 2(\sqrt[3]{49} + \sqrt[3]{14} + \sqrt[3]{4})$

**Respuesta:** La expresión racionalizada es $2(\sqrt[3]{49} + \sqrt[3]{14} + \sqrt[3]{4})$.

---

### Ejercicio 7: Suma Telescópica de Radicales
Calcular el valor numérico de la suma finita:

$$
S = \frac{1}{\sqrt{2} + 1} + \frac{1}{\sqrt{3} + \sqrt{2}} + \frac{1}{\sqrt{4} + \sqrt{3}} + \dots + \frac{1}{\sqrt{100} + \sqrt{99}}
$$

**Paso 1:** Racionalizamos el término general de la suma para $k \in \mathbb{N}$:
$T_k = \frac{1}{\sqrt{k+1} + \sqrt{k}} \cdot \frac{\sqrt{k+1} - \sqrt{k}}{\sqrt{k+1} - \sqrt{k}} = \frac{\sqrt{k+1} - \sqrt{k}}{(k+1) - k} = \sqrt{k+1} - \sqrt{k}$

**Paso 2:** Escribimos los términos sucesivos de la suma:
$T_1 = \sqrt{2} - 1$
$T_2 = \sqrt{3} - \sqrt{2}$
$T_3 = \sqrt{4} - \sqrt{3}$
$\vdots$
$T_{99} = \sqrt{100} - \sqrt{99}$

**Paso 3:** Efectuamos la suma observando la cancelación telescópica de los términos cruzados:
Todos los términos se anulan excepto el último término positivo y el primer término negativo:
$S = \sqrt{100} - 1 = 10 - 1 = 9$

**Respuesta:** El valor numérico de la suma es 9.

---

### Ejercicio 8: Racionalización de Denominador Trinomio
Racionalizar la fracción:

$$
E = \frac{2}{\sqrt{2} + \sqrt{3} + \sqrt{5}}
$$

**Paso 1:** Agrupamos los términos del denominador en dos partes:
$D = (\sqrt{2} + \sqrt{3}) + \sqrt{5}$

**Paso 2:** Multiplicamos por la primera conjugada $[(\sqrt{2} + \sqrt{3}) - \sqrt{5}]$:
$D_1 = [(\sqrt{2} + \sqrt{3}) + \sqrt{5}][(\sqrt{2} + \sqrt{3}) - \sqrt{5}] = (\sqrt{2} + \sqrt{3})^2 - (\sqrt{5})^2$
$D_1 = (2 + 2\sqrt{6} + 3) - 5 = 5 + 2\sqrt{6} - 5 = 2\sqrt{6}$

**Paso 3:** Escribimos la fracción tras la primera etapa:
$E = \frac{2[(\sqrt{2} + \sqrt{3}) - \sqrt{5}]}{2\sqrt{6}} = \frac{\sqrt{2} + \sqrt{3} - \sqrt{5}}{\sqrt{6}}$

**Paso 4:** Multiplicamos numerador y denominador por $\sqrt{6}$:
$E = \frac{(\sqrt{2} + \sqrt{3} - \sqrt{5})\sqrt{6}}{6} = \frac{\sqrt{12} + \sqrt{18} - \sqrt{30}}{6} = \frac{2\sqrt{3} + 3\sqrt{2} - \sqrt{30}}{6}$

**Respuesta:** La expresión racionalizada es $\frac{3\sqrt{2} + 2\sqrt{3} - \sqrt{30}}{6}$.

---

### Ejercicio 9: Radical Doble Cúbico
Descomponer en radical simple la expresión:

$$
R = \sqrt[3]{10 + \sqrt{108}}
$$

**Paso 1:** Identificamos $A = 10$ y $B = 108$.
Calculamos la constante $C = \sqrt[3]{A^2 - B}$:
$C = \sqrt[3]{10^2 - 108} = \sqrt[3]{100 - 108} = \sqrt[3]{-8} = -2$

**Paso 2:** Planteamos la ecuación cúbica para hallar la parte racional $x$:
$4x^3 - 3Cx - A = 0$
Sustituyendo $C = -2$ y $A = 10$:
$4x^3 - 3(-2)x - 10 = 0 \implies 4x^3 + 6x - 10 = 0$
Dividiendo entre 2:
$2x^3 + 3x - 5 = 0$

**Paso 3:** Evaluamos por inspección de divisores de 5:
Para $x = 1$: $2(1)^3 + 3(1) - 5 = 2 + 3 - 5 = 0$ (Verifica exactamente).
Por lo tanto, la solución racional es $x = 1$.

**Paso 4:** Calculamos la cantidad irracional $y = x^2 - C$:
$y = 1^2 - (-2) = 1 + 2 = 3$

**Paso 5:** Escribimos la descomposición $x + \sqrt{y}$:
$\sqrt[3]{10 + \sqrt{108}} = 1 + \sqrt{3}$

**Respuesta:** El radical cúbico transformado es $1 + \sqrt{3}$.

---

### Ejercicio 10: Aplicación Contextualizada (Cálculo de Impedancia en Redes Eléctricas Rurales)
En un proyecto de electrificación rural con paneles solares en una comunidad andina de Puno, la impedancia equivalente de una red eléctrica alterna está expresada por la fracción racionalizada:

$$
Z = \frac{60}{\sqrt{7 + 4\sqrt{3}}}
$$

donde $Z$ está en ohmios ($\Omega$). Determinar el valor exacto de la impedancia en su forma más simple sin radicales en el denominador.

**Paso 1:** Analizamos el denominador como un radical doble:
$D = \sqrt{7 + 4\sqrt{3}}$

**Paso 2:** Acondicionamos el radical interior para que tenga coeficiente 2:
$4\sqrt{3} = 2(2\sqrt{3}) = 2\sqrt{2^2 \times 3} = 2\sqrt{12}$
El denominador se transforma en:
$D = \sqrt{7 + 2\sqrt{12}}$

**Paso 3:** Buscamos dos números que sumados den 7 y multiplicados den 12:
$a + b = 7$ y $a \cdot b = 12 \implies a = 4$ y $b = 3$.
$D = \sqrt{4} + \sqrt{3} = 2 + \sqrt{3}$

**Paso 4:** Sustituimos el denominador simplificado en la impedancia:
$Z = \frac{60}{2 + \sqrt{3}}$

**Paso 5:** Racionalizamos multiplicando por la conjugada $(2 - \sqrt{3})$:
$Z = \frac{60(2 - \sqrt{3})}{(2 + \sqrt{3})(2 - \sqrt{3})} = \frac{60(2 - \sqrt{3})}{2^2 - (\sqrt{3})^2} = \frac{60(2 - \sqrt{3})}{4 - 3} = 60(2 - \sqrt{3}) = 120 - 60\sqrt{3}$

**Respuesta:** La impedancia exacta es $Z = 60(2 - \sqrt{3})\ \Omega \approx 16.08\ \Omega$.

---

## 5. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. Descomponer a radicales simples $\sqrt{5 + 2\sqrt{6}}$:  
A) $\sqrt{3} + \sqrt{2}$  
B) $\sqrt{3} - \sqrt{2}$  
C) $\sqrt{5} + 1$  
D) $\sqrt{6} + 1$  
E) $2 + \sqrt{3}$  

2. Descomponer a radicales simples $\sqrt{8 - 2\sqrt{15}}$:  
A) $\sqrt{5} - \sqrt{3}$  
B) $\sqrt{5} + \sqrt{3}$  
C) $\sqrt{6} - \sqrt{2}$  
D) $3 - \sqrt{5}$  
E) $\sqrt{7} - 1$  

3. Racionalizar la fracción $\frac{6}{\sqrt{3}}$:  
A) $2\sqrt{3}$  
B) $3\sqrt{3}$  
C) $\sqrt{3}$  
D) $6\sqrt{3}$  
E) $2$  

4. Racionalizar la fracción $\frac{10}{\sqrt{7} - \sqrt{2}}$:  
A) $2(\sqrt{7} + \sqrt{2})$  
B) $\sqrt{7} + \sqrt{2}$  
C) $5(\sqrt{7} + \sqrt{2})$  
D) $2(\sqrt{7} - \sqrt{2})$  
E) $10(\sqrt{7} + \sqrt{2})$  

5. Al transformar $\sqrt{9 + \sqrt{80}}$ a radicales simples se obtiene:  
A) $\sqrt{5} + 2$  
B) $\sqrt{5} - 2$  
C) $\sqrt{6} + \sqrt{3}$  
D) $3 + \sqrt{5}$  
E) $\sqrt{7} + \sqrt{2}$  

6. Racionalizar el denominador de $\frac{4}{\sqrt[3]{2}}$:  
A) $2\sqrt[3]{4}$  
B) $\sqrt[3]{4}$  
C) $4\sqrt[3]{4}$  
D) $2\sqrt[3]{2}$  
E) $4\sqrt[3]{2}$  

7. Calcular el valor de $(\sqrt{3} + \sqrt{2})(\sqrt{3} - \sqrt{2})$:  
A) $1$  
B) $5$  
C) $2\sqrt{6}$  
D) $-1$  
E) $6$  

8. Simplificar la expresión $\sqrt{3 + 2\sqrt{2}} - \sqrt{2}$:  
A) $1$  
B) $2$  
C) $\sqrt{2}$  
D) $0$  
E) $-1$  

9. Racionalizar $\frac{12}{\sqrt{5} + 1}$:  
A) $3(\sqrt{5} - 1)$  
B) $2(\sqrt{5} - 1)$  
C) $4(\sqrt{5} - 1)$  
D) $6(\sqrt{5} - 1)$  
E) $\sqrt{5} - 1$  

10. Si $\sqrt{x + 2\sqrt{y}} = \sqrt{7} + \sqrt{3}$, hallar $x + y$:  
A) $31$  
B) $21$  
C) $10$  
D) $25$  
E) $28$  

11. Descomponer a radicales simples $\sqrt{10 - 2\sqrt{21}}$:  
A) $\sqrt{7} - \sqrt{3}$  
B) $\sqrt{7} + \sqrt{3}$  
C) $\sqrt{6} - 2$  
D) $5 - \sqrt{3}$  
E) $\sqrt{8} - \sqrt{2}$  

12. ¿Cuál es el factor racionalizante de $\frac{1}{\sqrt[7]{x^3}}$?  
A) $\sqrt[7]{x^4}$  
B) $\sqrt[7]{x^3}$  
C) $\sqrt[7]{x^5}$  
D) $x^4$  
E) $\sqrt[7]{x}$  

13. Efectuar: $E = \frac{1}{\sqrt{5} - 2} - \sqrt{5}$:  
A) $2$  
B) $-2$  
C) $2\sqrt{5}$  
D) $1$  
E) $0$  

14. Racionalizar $\frac{9}{\sqrt[3]{3}}$:  
A) $3\sqrt[3]{9}$  
B) $\sqrt[3]{9}$  
C) $3\sqrt[3]{3}$  
D) $9\sqrt[3]{9}$  
E) $27$  

15. El valor de $\sqrt{6 + 2\sqrt{5}} - \sqrt{6 - 2\sqrt{5}}$ es:  
A) $2$  
B) $2\sqrt{5}$  
C) $0$  
D) $4$  
E) $\sqrt{5}$  

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Simplificar la expresión algebraica: $M = \sqrt{12 + \sqrt{140}} - \sqrt{8 - \sqrt{28}}$.  
A) $2\sqrt{2}$  
B) $\sqrt{5} + 1$  
C) $\sqrt{7} + 1$  
D) $2\sqrt{5}$  
E) $2$  

17. Racionalizar y simplificar: $F = \frac{6}{\sqrt{7} + \sqrt{5} + \sqrt{2}}$.  
A) $\frac{\sqrt{70} + \sqrt{14} - \sqrt{10}}{2}$  
B) $\frac{3(\sqrt{7} + \sqrt{5} - \sqrt{2})}{4}$  
C) $\frac{\sqrt{14} + \sqrt{10} - \sqrt{35}}{2}$  
D) $\sqrt{7} - \sqrt{5}$  
E) $\frac{3(2\sqrt{5} + 5\sqrt{2} - \sqrt{70})}{10}$  

18. Hallar el valor de $E = \frac{1}{\sqrt{3} + \sqrt{2}} + \frac{1}{\sqrt{4} + \sqrt{3}} + \frac{1}{\sqrt{5} + \sqrt{4}} + \frac{1}{\sqrt{6} + \sqrt{5}}$:  
A) $\sqrt{6} - \sqrt{2}$  
B) $\sqrt{6} + \sqrt{2}$  
C) $\sqrt{5} - 1$  
D) $2\sqrt{3}$  
E) $1$  

19. Racionalizar el denominador de la fracción con raíces cúbicas: $K = \frac{15}{\sqrt[3]{25} + \sqrt[3]{10} + \sqrt[3]{4}}$.  
A) $5(\sqrt[3]{5} - \sqrt[3]{2})$  
B) $3(\sqrt[3]{5} - \sqrt[3]{2})$  
C) $\sqrt[3]{5} - \sqrt[3]{2}$  
D) $15(\sqrt[3]{5} - \sqrt[3]{2})$  
E) $2(\sqrt[3]{5} - \sqrt[3]{2})$  

20. Si $\sqrt{14 + 6\sqrt{5}} = a + \sqrt{b}$ con $a, b \in \mathbb{N}$, calcular $a \cdot b$:  
A) $15$  
B) $18$  
C) $20$  
D) $12$  
E) $25$  

21. Descomponer a radicales simples: $P = \sqrt{28 - 10\sqrt{3}}$.  
A) $5 - \sqrt{3}$  
B) $3 - \sqrt{5}$  
C) $5 + \sqrt{3}$  
D) $4 - \sqrt{3}$  
E) $\sqrt{15} - \sqrt{3}$  

22. Calcular el valor de $x$ que satisface la igualdad: $\sqrt{x + \sqrt{48}} = \sqrt{6} + \sqrt{2}$.  
A) $8$  
B) $10$  
C) $12$  
D) $14$  
E) $16$  

23. Racionalizar y efectuar: $E = \frac{2}{\sqrt{6} - 2} - \frac{2}{\sqrt{6} + 2}$.  
A) $4$  
B) $2\sqrt{6}$  
C) $2$  
D) $\sqrt{6}$  
E) $8$  

24. Un terreno agrícola triangular en Tarma tiene lados perpendiculares de longitudes $(\sqrt{7 + 2\sqrt{10}})\text{ m}$ y $(\sqrt{7 - 2\sqrt{10}})\text{ m}$. Calcular el área del terreno en metros cuadrados:  
A) $1\text{ m}^2$  
B) $1.5\text{ m}^2$  
C) $2\text{ m}^2$  
D) $2.5\text{ m}^2$  
E) $3\text{ m}^2$  

25. Simplificar la expresión: $M = \sqrt{1 + 2\sqrt{1 + 2\sqrt{1 + 2\sqrt{16}}}}$.  
A) $3$  
B) $\sqrt{7}$  
C) $\sqrt{5}$  
D) $2$  
E) $\sqrt{11}$  

26. Descomponer en radicales simples $\sqrt{2 + \sqrt{3}}$ multiplicando por $\frac{\sqrt{2}}{\sqrt{2}}$:  
A) $\frac{\sqrt{6} + \sqrt{2}}{2}$  
B) $\frac{\sqrt{6} - \sqrt{2}}{2}$  
C) $\sqrt{3} + 1$  
D) $\frac{\sqrt{3} + 1}{2}$  
E) $\frac{\sqrt{5} + 1}{2}$  

27. Racionalizar $\frac{1}{\sqrt[3]{9} - \sqrt[3]{3} + 1}$:  
A) $\frac{\sqrt[3]{3} + 1}{4}$  
B) $\frac{\sqrt[3]{3} - 1}{2}$  
C) $\frac{\sqrt[3]{9} + 1}{4}$  
D) $\frac{\sqrt[3]{3} + 1}{2}$  
E) $\sqrt[3]{3} + 1$  

28. Calcular el valor de $K = \sqrt{17 - 12\sqrt{2}} + \sqrt{17 + 12\sqrt{2}}$:  
A) $6$  
B) $4\sqrt{2}$  
C) $2\sqrt{17}$  
D) $8$  
E) $4$  

29. Si $x = \frac{\sqrt{5} + 1}{2}$, calcular el valor de $x^2 - x$:  
A) $1$  
B) $2$  
C) $0$  
D) $-1$  
E) $1/2$  

30. Racionalizar la expresión fraccionaria: $\frac{4}{\sqrt{5} + \sqrt{3} - \sqrt{2}}$ e indicar el denominador racional resultante tras la primera etapa:  
A) $2\sqrt{15}$
B) $6 + 2\sqrt{15}$
C) $2\sqrt{6}$
D) $4$
E) $10$

31. Descomponer a radicales simples $\sqrt{11 + 4\sqrt{6}}$:
A) $2\sqrt{2} + \sqrt{3}$
B) $3\sqrt{2} + \sqrt{3}$
C) $\sqrt{7} + \sqrt{4}$
D) $\sqrt{6} + \sqrt{5}$
E) $2\sqrt{3} + \sqrt{2}$

32. Al simplificar $E = \frac{\sqrt{3}}{\sqrt{3} - \sqrt{2}} - \frac{\sqrt{3}}{\sqrt{3} + \sqrt{2}}$, se obtiene:
A) $5$
B) $1$
C) $2\sqrt{6}$
D) $5 - 2\sqrt{6}$
E) $2\sqrt{6} - 5$

33. Descomponer el radical doble cúbico $\sqrt[3]{26 + \sqrt{675}}$ a la forma simple $x + \sqrt{y}$:
A) $2 + \sqrt{3}$
B) $1 + \sqrt{3}$
C) $3 + \sqrt{2}$
D) $2 + \sqrt{5}$
E) $1 + \sqrt{5}$

34. Si $\frac{1}{\sqrt{7 - \sqrt{48}}} = a + \sqrt{b}$, hallar $a + b$:
A) $5$
B) $7$
C) $9$
D) $6$
E) $8$

35. Un soporte metálico para una torre de telecomunicaciones en Ayacucho tiene una longitud dada por $L = \frac{10}{\sqrt{6} + \sqrt{5} - 1}\text{ m}$. El factor racionalizante adecuado para la primera fase es:
A) $(\sqrt{6} + \sqrt{5}) + 1$
B) $(\sqrt{6} - \sqrt{5}) - 1$
C) $\sqrt{6} - \sqrt{5} + 1$
D) $\sqrt{6} + \sqrt{5}$
E) $\sqrt{30} + 1$

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Descomponer en tres radicales simples la expresión: $P = \sqrt{15 + 2\sqrt{15} + 2\sqrt{21} + 2\sqrt{35}}$.  
A) $\sqrt{3} + \sqrt{5} + \sqrt{7}$  
B) $\sqrt{2} + \sqrt{5} + \sqrt{7}$  
C) $\sqrt{3} + \sqrt{4} + \sqrt{7}$  
D) $1 + \sqrt{6} + \sqrt{7}$  
E) $\sqrt{2} + \sqrt{3} + \sqrt{5}$  

37. Simplificar la siguiente expresión con infinitos radicales anidados: $E = \sqrt{12 + \sqrt{12 + \sqrt{12 + \dots}}}$.  
A) $4$  
B) $3$  
C) $6$  
D) $12$  
E) $\sqrt{12}$  

38. Calcular el valor exacto de la expresión cúbica: $M = \sqrt[3]{20 + 14\sqrt{2}} + \sqrt[3]{20 - 14\sqrt{2}}$.  
A) $4$  
B) $2$  
C) $2\sqrt{2}$  
D) $6$  
E) $3$  

39. Si se racionaliza el denominador de: $F = \frac{1}{\sqrt[4]{8} + \sqrt[4]{4} + \sqrt[4]{2} + 1}$, el resultado equivalente simplificado es:  
A) $\sqrt[4]{2} - 1$
B) $\sqrt[4]{8} - 1$
C) $\sqrt{2} - 1$
D) $\sqrt[4]{4} - 1$
E) $1 - \sqrt[4]{2}$

40. Hallar el valor de $x$ que satisface la ecuación irracional: $\sqrt{x + 2} + \sqrt{x - 3} = 5$.  
A) $7$  
B) $9$  
C) $6$  
D) $8$  
E) $11$  

41. **(Reto)** Simplificar a su mínima expresión: $T = \sqrt{2 + \sqrt{3}} \cdot \sqrt{2 + \sqrt{2 + \sqrt{3}}} \cdot \sqrt{2 - \sqrt{2 + \sqrt{3}}}$.  
A) $1$  
B) $\sqrt{2}$  
C) $\sqrt{3}$  
D) $2$  
E) $1/2$  

42. **(Reto)** Descomponer en cuatro radicales simples la expresión: $\sqrt{10 + \sqrt{24} + \sqrt{40} + \sqrt{60}}$.  
A) $\sqrt{2} + \sqrt{3} + \sqrt{5}$  
B) $1 + \sqrt{2} + \sqrt{3} + \sqrt{5}$  
C) $\sqrt{3} + \sqrt{5} + \sqrt{7}$  
D) $\sqrt{2} + \sqrt{5} + \sqrt{6}$  
E) $2 + \sqrt{3} + \sqrt{5}$  

43. **(Reto)** Racionalizar completamente el denominador de: $K = \frac{1}{\sqrt[3]{4} + \sqrt[3]{2} - 2}$.  
A) $\frac{\sqrt[3]{2} - 1}{2}$  
B) $\frac{3\sqrt[3]{4} + 4\sqrt[3]{2} + 2}{10}$  
C) $\frac{\sqrt[3]{4} + 1}{3}$  
D) $\frac{\sqrt[3]{2} + 1}{2}$  
E) $\frac{\sqrt[3]{4} - \sqrt[3]{2} + 1}{3}$  

44. **(Reto)** Calcular el valor exacto de la fracción racionalizada: $E = \frac{\sqrt{10 + \sqrt{84}} - \sqrt{10 - \sqrt{84}}}{\sqrt{3}}$.  
A) $2\sqrt{3}$  
B) $2$  
C) $\sqrt{3}$  
D) $2/\sqrt{7}$  
E) $\sqrt{6}$  

45. **(Reto)** Si $x = \sqrt[3]{\sqrt{5} + 2} - \sqrt[3]{\sqrt{5} - 2}$, calcular el valor numérico exacto de $x^3 + 3x$:  
A) $4$  
B) $2$  
C) $2\sqrt{5}$  
D) $1$  
E) $8$  

---

## 6. Claves de Respuestas y Pistas Estratégicas

### Claves de Respuestas

| N° | Clave | N° | Clave | N° | Clave | N° | Clave | N° | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | A | **10** | A | **19** | A | **28** | A | **37** | A |
| **2** | A | **11** | A | **20** | A | **29** | A | **38** | A |
| **3** | A | **12** | A | **21** | A | **30** | B | **39** | A |
| **4** | A | **13** | A | **22** | A | **31** | A | **40** | A |
| **5** | A | **14** | A | **23** | A | **32** | C | **41** | A |
| **6** | A | **15** | A | **24** | B | **33** | A | **42** | A |
| **7** | A | **16** | B | **25** | B | **34** | A | **43** | B |
| **8** | A | **17** | E | **26** | A | **35** | A | **44** | B |
| **9** | A | **18** | A | **27** | A | **36** | A | **45** | A |

---

### Pistas Estratégicas para Ejercicios Reto (41 al 45)

* **Pista 41:** Multiplica primero los dos últimos factores utilizando la diferencia de cuadrados bajo un mismo radical: $\sqrt{(2 + \sqrt{2+\sqrt{3}})(2 - \sqrt{2+\sqrt{3}})} = \sqrt{2^2 - (2 + \sqrt{3})} = \sqrt{4 - 2 - \sqrt{3}} = \sqrt{2 - \sqrt{3}}$. Luego multiplica este resultado por el primer factor: $\sqrt{2 + \sqrt{3}} \cdot \sqrt{2 - \sqrt{3}} = \sqrt{2^2 - (\sqrt{3})^2} = \sqrt{4 - 3} = 1$.
* **Pista 42:** Expresa cada radical interior con coeficiente 2: $\sqrt{24} = 2\sqrt{6}$, $\sqrt{40} = 2\sqrt{10}$, $\sqrt{60} = 2\sqrt{15}$. Busca tres números $x, y, z$ que sumen 10 y cuyos productos dos a dos sean 6, 10 y 15: los números son 2, 3 y 5.
* **Pista 43:** Haz el cambio de variable auxiliar $u = \sqrt[3]{2} \implies u^3 = 2$. El denominador es $u^2 + u - u^3 = u(u + 1 - u^2)$. Aplica la identidad de suma de cubos multiplicando por expresiones polinomiales adecuadas para eliminar la irracionalidad en el denominador.
* **Pista 44:** Transforma a radicales simples cada término del numerador: $\sqrt{10 \pm \sqrt{84}} = \sqrt{10 \pm 2\sqrt{21}} = \sqrt{7} \pm \sqrt{3}$. Al restar ambos términos: $(\sqrt{7} + \sqrt{3}) - (\sqrt{7} - \sqrt{3}) = 2\sqrt{3}$. Divide entre $\sqrt{7}$ o evalúa directamente la simplificación.
* **Pista 45:** Eleva al cubo la igualdad $x = a - b$ utilizando la identidad de Cauchy: $x^3 = a^3 - b^3 - 3ab(a - b)$. Observa que $a^3 - b^3 = (\sqrt{5} + 2) - (\sqrt{5} - 2) = 4$, y $ab = \sqrt[3]{(\sqrt{5}+2)(\sqrt{5}-2)} = \sqrt[3]{5 - 4} = 1$. Luego: $x^3 = 4 - 3(1)(x) \implies x^3 + 3x = 4$.

---

## 7. Formulario Resumen

| Concepto / Teorema | Expresión Matemática | Notas y Condiciones |
| :--- | :--- | :--- |
| **Radical Simple Par** | $\sqrt[2k]{x^{2k}} = \|x\|$ | Obligatoriedad del valor absoluto en índice par |
| **Radical Doble Canónico** | $\sqrt{A \pm \sqrt{B}} = \sqrt{\frac{A+C}{2}} \pm \sqrt{\frac{A-C}{2}}$ | $C = \sqrt{A^2 - B} \in \mathbb{Q}$ (cuadrado perfecto) |
| **Forma Práctica (Doble)** | $\sqrt{(a + b) \pm 2\sqrt{ab}} = \sqrt{a} \pm \sqrt{b}$ | $a > b > 0$; suma y producto de dos números |
| **Acondicionamiento Factor 2**| $\sqrt{A \pm \sqrt{B}} = \sqrt{A \pm 2\sqrt{B/4}}$ | Extraer factor 4 del radical interior |
| **Radical Doble de Tres Raíces**| $\sqrt{x+y+z + 2\sqrt{xy} + 2\sqrt{yz} + 2\sqrt{xz}}$ | Descomposición en $\sqrt{x} + \sqrt{y} + \sqrt{z}$ |
| **Radical Doble Cúbico** | $\sqrt[3]{A \pm \sqrt{B}} = x \pm \sqrt{y}$ | $C = \sqrt[3]{A^2 - B}$; $4x^3 - 3Cx - A = 0$; $y = x^2 - C$ |
| **Racionalización Monomio** | $\frac{N}{\sqrt[n]{a^k}} \cdot \frac{\sqrt[n]{a^{n-k}}}{\sqrt[n]{a^{n-k}}} = \frac{N\sqrt[n]{a^{n-k}}}{a}$ | El exponente resultante completa el índice $n$ |
| **Conjugada Cuadrática** | $(\sqrt{a} \pm \sqrt{b})(\sqrt{a} \mp \sqrt{b}) = a - b$ | Diferencia de cuadrados |
| **Conjugada Cúbica (Suma)** | $(\sqrt[3]{a} + \sqrt[3]{b})(\sqrt[3]{a^2} - \sqrt[3]{ab} + \sqrt[3]{b^2}) = a + b$ | Suma de cubos |
| **Conjugada Cúbica (Resta)** | $(\sqrt[3]{a} - \sqrt[3]{b})(\sqrt[3]{a^2} + \sqrt[3]{ab} + \sqrt[3]{b^2}) = a - b$ | Diferencia de cubos |
| **Suma Telescópica Radical** | $\frac{1}{\sqrt{k+1} + \sqrt{k}} = \sqrt{k+1} - \sqrt{k}$ | Cancelación sucesiva de términos intermedios |
| **Infinitos Radicales Suma** | $\sqrt{n(n+1) + \sqrt{n(n+1) + \dots}} = n + 1$ | Convergencia a la raíz positiva |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 3 clave(s) corregida(s) y 7 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **17** | E | E | Corregida | Se ajustó la opción E con el valor exacto: al racionalizar dos veces resulta $\frac{3}{10}(2\sqrt{5}+5\sqrt{2}-\sqrt{70})$. Clave E. |
| **25** | A | B | Corregida | Se ajustó el radicando interno: $\sqrt{16}=4$, $1+8=9$, $\sqrt{9}=3$, $1+6=7$ y $M=\sqrt{7}$. Clave B. |
| **31** | A | A | Corregida | La opción C era idéntica a A ($\sqrt{8}=2\sqrt{2}$); se sustituyó por un distractor. Descomposición: $2\sqrt{2}+\sqrt{3}$ (A). |
| **32** | D | C | Corregida | Se ajustó el primer numerador a $\sqrt{3}$: la diferencia de conjugados da $2\sqrt{6}$. Clave C. |
| **36** | A | A | Corregida | Se ajustó el término independiente a $15$: $(\sqrt{3}+\sqrt{5}+\sqrt{7})^2=15+2\sqrt{15}+2\sqrt{21}+2\sqrt{35}$. Clave A. |
| **43** | B | B | Corregida | Se ajustó la opción B: con $u=\sqrt[3]{2}$ se obtiene $K=\frac{3u^2+4u+2}{10}$. Clave B. |
| **44** | A | B | Corregida | Se ajustó el denominador a $\sqrt{3}$: $\sqrt{10\pm\sqrt{84}}=\sqrt{7}\pm\sqrt{3}$, la diferencia es $2\sqrt{3}$ y $E=2$. Clave B. |

**Claves sin cambios:** 42 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
