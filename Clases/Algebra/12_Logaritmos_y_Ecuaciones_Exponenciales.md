# Tema 12: Logaritmos y Ecuaciones Exponenciales

El logaritmo de un número real positivo $N$ en una base dada $b$ (real, positiva y diferente de la unidad) es el exponente $x$ al cual debe elevarse la base $b$ para obtener como resultado dicho número $N$:

$$
\log_b(N) = x \iff b^x = N
$$

Para garantizar la existencia formal y la unicidad en el campo de los números reales ($\mathbb{R}$), se establecen de manera obligatoria las **condiciones de existencia del logaritmo** (Conjunto de Valores Admisibles o C.V.A.):

1. El argumento o número debe ser estrictamente positivo: $N > 0$.

2. La base debe ser estrictamente positiva y diferente de uno:

$$
b > 0 \quad \land \quad b \neq 1
$$

En el contexto del examen de preselección Beca 18 y en las aplicaciones científicas y de ingeniería, los logaritmos y las funciones exponenciales son indispensables. Permiten modelar el crecimiento bacteriano y poblacional en biología, la desintegración radiactiva del carbono-14 en arqueología, la escala de Richter para la intensidad sísmica, la escala de decibelios para la acústica ambiental, y el cálculo del interés compuesto continuo en finanzas y economía.

---

## 1. Fundamentos y Relación entre Funciones Exponenciales y Logarítmicas

La función logarítmica $g(x) = \log_b(x)$ es la **función inversa** de la función exponencial $f(x) = b^x$. Geométricamente, sus gráficas en el plano cartesiano $\mathbb{R}^2$ son perfectamente simétricas respecto a la recta diagonal identidad $y = x$:

```{figure} ../../assets/algebra/funciones_exponencial_logaritmica.svg
---
align: center
alt: Gráfica cartesiana de las funciones exponencial y logarítmica como inversas mutuas
---
Simetría respecto a la diagonal principal $y = x$ entre la función exponencial $y = 2^x$ y su inversa la función logarítmica $y = \log_2(x)$.
```

### 1.1 Identidades Fundamentales

De la definición de función inversa se deducen directamente las dos identidades de cancelación fundamentales:

$$

b^{\log_b(N)} = N, \quad \forall N > 0, \ b > 0, \ b \neq 1

$$

$$

\log_b(b^x) = x, \quad \forall x \in \mathbb{R}, \ b > 0, \ b \neq 1

$$

Valores particulares inmediatos:
* $\log_b(1) = 0$ (ya que $b^0 = 1$).
* $\log_b(b) = 1$ (ya que $b^1 = b$).

### 1.2 Sistemas Notables de Logaritmos

1. **Logaritmo Decimal, Vulgar o de Briggs:** Es aquel cuya base es 10. Por convenio internacional se omite escribir la base:

$$

\log_{10}(N) \equiv \log(N)

$$

2. **Logaritmo Natural, Neperiano o Hiperbólico:** Es aquel cuya base es la constante matemática trascendente $e \approx 2.718281828\dots$:

$$

\log_e(N) \equiv \ln(N)

$$

---

## 2. Propiedades Operativas, Cologaritmo y Antilogaritmo

Para bases y argumentos pertenecientes a sus respectivos dominios de existencia:

### 2.1 Teoremas Operativos Fundamentales

1. **Logaritmo de un Producto:**

$$

\log_b(M \cdot N) = \log_b(M) + \log_b(N)

$$

2. **Logaritmo de un Cociente:**

$$

\log_b\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)

$$

3. **Logaritmo de una Potencia (Regla del Sombrero):**

$$

\log_b(N^k) = k \cdot \log_b(N), \quad (\forall k \in \mathbb{R})

$$

4. **Generalización de Exponentes en Base y Argumento:**

$$

\log_{b^m}(N^k) = \frac{k}{m} \log_b(N), \quad (m \neq 0)

$$

5. **Logaritmo de una Raíz:**

$$

\log_b(\sqrt[n]{N}) = \frac{1}{n} \log_b(N)

$$

### 2.2 Teoremas de Transformación de Base

1. **Fórmula del Cambio de Base:** Permite convertir un logaritmo en base $b$ a una nueva base arbitraria $c$ ($c > 0, c \neq 1$):

$$

\log_b(N) = \frac{\log_c(N)}{\log_c(b)}

$$

2. **Regla de la Inversión de Base:**

$$

\log_b(a) = \frac{1}{\log_a(b)} \iff \log_b(a) \cdot \log_a(b) = 1

$$

3. **Regla de la Cadena:**

$$

\log_b(a) \cdot \log_c(b) \cdot \log_d(c) = \log_d(a)

$$

4. **Permuta de Base y Argumento en Exponenciales:**

$$

a^{\log_b(c)} = c^{\log_b(a)}

$$

### 2.3 Cologaritmo y Antilogaritmo

1. **Cologaritmo ($\text{colog}$):** Es el logaritmo del inverso multiplicativo del argumento, equivalente al opuesto del logaritmo:

$$

\text{colog}_b(N) = \log_b\left(\frac{1}{N}\right) = -\log_b(N)

$$

2. **Antilogaritmo ($\text{antilog}$):** Es la operación puramente exponencial en la base especificada:

$$

\text{antilog}_b(x) = b^x

$$

3. **Propiedades de Composición y Cancelación:**

$$

\log_b(\text{antilog}_b(x)) = x

$$

$$

\text{antilog}_b(\log_b(N)) = N

$$

---

## 3. Ecuaciones Exponenciales y Logarítmicas

### 3.1 Ecuaciones Exponenciales

Son igualdades algebraicas donde la incógnita se encuentra ubicada en el exponente.

* **Principio de Bases Iguales:** Si las bases son idénticas y no triviales ($a > 0, a \neq 1$):

$$

a^{f(x)} = a^{g(x)} \iff f(x) = g(x)

$$

* **Principio de Analogía o Semejanza Formal:**

$$

[f(x)]^{f(x)} = a^a \implies f(x) = a

$$

* **Método de Cambio de Variable:** Para ecuaciones con sumas o diferencias de potencias de la misma base, se hace $u = a^x$ (con $u > 0$), reduciendo la expresión a una ecuación polinomial.
* **Aplicación de Logaritmos:** Cuando las bases son distintas e irreducibles ($a^x = b$), se toman logaritmos a ambos miembros: $x = \frac{\log(b)}{\log(a)}$.

### 3.2 Ecuaciones Logarítmicas

Son ecuaciones en las cuales la incógnita forma parte del argumento o de la base de un logaritmo.

**Protocolo de Resolución Riguroso:**
1. **Determinar el C.V.A.:** Establecer las desigualdades $N(x) > 0$, $b(x) > 0$ y $b(x) \neq 1$. El C.V.A. es la intersección de todos los intervalos admisibles.
2. **Aplicar propiedades algebraicas:** Transformar sumas y diferencias de logaritmos en logaritmos de productos o cocientes hasta alcanzar la forma canónica $\log_b(f(x)) = \log_b(g(x))$.
3. **Inyectividad:** Por ser la función logarítmica biyectiva:

$$

\log_b(f(x)) = \log_b(g(x)) \iff f(x) = g(x)

$$

4. **Verificación y Descarte de Raíces Extrañas:** Confrontar las soluciones algebraicas obtenidas con el C.V.A. Solo los valores que pertenezcan estrictamente al C.V.A. constituyen el Conjunto Solución (C.S.).

---

## 4. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Aplicación de la Definición e Identidades
Calcular el valor numérico de la expresión:

$$

E = \log_2(32) + \log_3\left(\frac{1}{27}\right) + \log_{\sqrt{5}}(25)

$$

**Paso 1:** Evaluamos cada término individualmente aplicando la definición de logaritmo:
* Primer término: $\log_2(32) = x \iff 2^x = 32 = 2^5 \implies x = 5$.
* Segundo término: $\log_3\left(\frac{1}{27}\right) = y \iff 3^y = \frac{1}{27} = 3^{-3} \implies y = -3$.
* Tercer término: $\log_{\sqrt{5}}(25) = z \iff (\sqrt{5})^z = 25 \iff (5^{1/2})^z = 5^2 \implies \frac{z}{2} = 2 \implies z = 4$.

**Paso 2:** Sumamos los valores obtenidos:
$E = 5 + (-3) + 4 = 6$

**Respuesta:** El valor numérico de $E$ es 6.

---

### Ejercicio 2: Propiedades de la Regla del Sombrero y Radicales
Reducir la expresión:

$$

M = \log_{8}(16) + \log_{27}(81) - \log_{32}(64)

$$

**Paso 1:** Expresamos las bases y argumentos como potencias de números primos comunes:
* Para $\log_{8}(16)$: base $8 = 2^3$, argumento $16 = 2^4$.
Aplicando $\log_{b^m}(N^k) = \frac{k}{m} \log_b(N)$:
$\log_{2^3}(2^4) = \frac{4}{3} \log_2(2) = \frac{4}{3}(1) = \frac{4}{3}$

* Para $\log_{27}(81)$: base $27 = 3^3$, argumento $81 = 3^4$:
$\log_{3^3}(3^4) = \frac{4}{3} \log_3(3) = \frac{4}{3}$

* Para $\log_{32}(64)$: base $32 = 2^5$, argumento $64 = 2^6$:
$\log_{2^5}(2^6) = \frac{6}{5} \log_2(2) = \frac{6}{5}$

**Paso 2:** Efectuamos las operaciones algebraicas:
$M = \frac{4}{3} + \frac{4}{3} - \frac{6}{5} = \frac{8}{3} - \frac{6}{5}$

**Paso 3:** Homogeneizamos fracciones con denominador común 15:
$M = \frac{8(5) - 6(3)}{15} = \frac{40 - 18}{15} = \frac{22}{15}$

**Respuesta:** El valor exacto es $\frac{22}{15}$.

---

### Ejercicio 3: Regla de la Cadena y Cambio de Base
Calcular el valor del producto:

$$

P = \log_2(3) \cdot \log_3(5) \cdot \log_5(7) \cdot \log_7(64)

$$

**Paso 1:** Aplicamos la Regla de la Cadena para el producto continuado de logaritmos:
$\log_b(a) \cdot \log_c(b) \cdot \log_d(c) = \log_d(a)$

**Paso 2:** Los argumentos intermedios $3, 5, 7$ se simplifican sucesivamente con sus bases correspondientes:
$P = \log_2(64)$

**Paso 3:** Evaluamos el logaritmo final:
Como $64 = 2^6$:
$P = \log_2(2^6) = 6\log_2(2) = 6(1) = 6$

**Respuesta:** El valor del producto es 6.

---

### Ejercicio 4: Ecuación Logarítmica con Validación de C.V.A.
Resolver la ecuación logarítmica en $\mathbb{R}$:

$$

\log_2(x + 2) + \log_2(x - 1) = 2

$$

**Paso 1:** Determinamos el Conjunto de Valores Admisibles (C.V.A.):
* $x + 2 > 0 \implies x > -2$
* $x - 1 > 0 \implies x > 1$
Intersecando ambas condiciones:
$\text{C.V.A.} = \langle 1, +\infty \rangle$

**Paso 2:** Aplicamos la propiedad del logaritmo de un producto:
$\log_2[(x + 2)(x - 1)] = 2$

**Paso 3:** Aplicamos la definición de logaritmo:
$(x + 2)(x - 1) = 2^2 = 4$
$x^2 + x - 2 = 4 \implies x^2 + x - 6 = 0$

**Paso 4:** Factorizamos por aspa simple:
$(x + 3)(x - 2) = 0 \implies x_1 = -3 \quad \lor \quad x_2 = 2$

**Paso 5:** Verificamos contra el C.V.A. ($x > 1$):
* $x_1 = -3 \notin \text{C.V.A.}$ (Se descarta por generar argumentos negativos: $\log_2(-1)$).
* $x_2 = 2 \in \text{C.V.A.}$ (Solución válida).

**Respuesta:** El conjunto solución es C.S. $= \{2\}$.

---

### Ejercicio 5: Ecuación Exponencial con Cambio de Variable
Resolver en $\mathbb{R}$:

$$

4^x - 3 \cdot 2^{x+1} + 8 = 0

$$

**Paso 1:** Homogeneizamos la base expresando todo en potencias de 2:
$4^x = (2^2)^x = (2^x)^2$
$2^{x+1} = 2^x \cdot 2^1 = 2 \cdot 2^x$

**Paso 2:** Sustituimos en la ecuación:
$(2^x)^2 - 3(2 \cdot 2^x) + 8 = 0$
$(2^x)^2 - 6(2^x) + 8 = 0$

**Paso 3:** Realizamos el cambio de variable auxiliar:
Sea $u = 2^x$, con la restricción obligatoria $u > 0$.
$u^2 - 6u + 8 = 0$

**Paso 4:** Factorizamos el trinomio por aspa simple:
$(u - 4)(u - 2) = 0 \implies u_1 = 4 \quad \lor \quad u_2 = 2$
Ambos valores son positivos, por lo que ambos son válidos.

**Paso 5:** Retornamos a la variable original $x$:
* Si $u = 4 \implies 2^x = 4 = 2^2 \implies x_1 = 2$.
* Si $u = 2 \implies 2^x = 2 = 2^1 \implies x_2 = 1$.

**Respuesta:** El conjunto solución es C.S. $= \{1, 2\}$.

---

### Ejercicio 6: Cologaritmos y Antilogaritmos Compuestos
Calcular el valor numérico de:

$$

A = \text{antilog}_2\left[ \log_3\left( \text{antilog}_3(4) \right) + \text{colog}_2\left( \frac{1}{8} \right) \right]

$$

**Paso 1:** Resolvemos de adentro hacia afuera:
* Por cancelación directa: $\log_3(\text{antilog}_3(4)) = 4$.
* Por definición de cologaritmo:
$\text{colog}_2\left(\frac{1}{8}\right) = -\log_2\left(\frac{1}{8}\right) = -\log_2(2^{-3}) = -(-3) = 3$.

**Paso 2:** Sumamos los términos del argumento del antilogaritmo:
Argumento $= 4 + 3 = 7$

**Paso 3:** Aplicamos la definición de antilogaritmo en base 2:
$A = \text{antilog}_2(7) = 2^7 = 128$

**Respuesta:** El valor numérico de $A$ es 128.

---

### Ejercicio 7: Sistema de Ecuaciones Exponenciales
Resolver el sistema de ecuaciones:

$$

\begin{cases} 2^x \cdot 3^y = 18 \\ 2^y \cdot 3^x = 12 \end{cases}

$$

y calcular el valor de $x + y$.

**Paso 1:** Multiplicamos miembro a miembro ambas ecuaciones:
$(2^x \cdot 3^y)(2^y \cdot 3^x) = 18 \times 12$

**Paso 2:** Agrupamos las potencias de igual base en el primer miembro:
$2^{x+y} \cdot 3^{x+y} = 216$
$(2 \cdot 3)^{x+y} = 216$
$6^{x+y} = 216$

**Paso 3:** Descomponemos 216 en base 6:
$216 = 6^3$
$6^{x+y} = 6^3 \implies x + y = 3$

**Respuesta:** El valor de $x + y$ es 3.

---

### Ejercicio 8: Identidad de Permuta de Base y Argumento
Hallar el valor de $x$ en la ecuación:

$$

x^{\log_3(2)} + 2^{\log_3(x)} = 16

$$

**Paso 1:** Aplicamos la propiedad de permuta $a^{\log_b(c)} = c^{\log_b(a)}$ sobre el primer término:
$x^{\log_3(2)} = 2^{\log_3(x)}$

**Paso 2:** Sustituimos en la ecuación original:
$2^{\log_3(x)} + 2^{\log_3(x)} = 16$
$2 \cdot 2^{\log_3(x)} = 16$

**Paso 3:** Dividimos entre 2:
$2^{\log_3(x)} = 8 = 2^3$

**Paso 4:** Igualamos exponentes por bases iguales:
$\log_3(x) = 3$

**Paso 5:** Aplicamos la definición de logaritmo:
$x = 3^3 = 27$
Verificamos C.V.A.: $x = 27 > 0$ (Válido).

**Respuesta:** El valor de $x$ es 27.

---

### Ejercicio 9: Ecuación por Analogía o Semejanza Formal
Resolver en $\mathbb{R}$:

$$

x^x = 256

$$

**Paso 1:** Descomponemos 256 en factores primos:
$256 = 2^8$

**Paso 2:** Buscamos transformar el segundo miembro a la forma $a^a$:
$2^8 = (2^2)^4 = 4^4$

**Paso 3:** Escribimos la igualdad por semejanza formal:
$x^x = 4^4$
Por analogía matemática estricta: $x = 4$.

**Respuesta:** La solución real es $x = 4$.

---

### Ejercicio 10: Aplicación Contextualizada (Crecimiento Poblacional en Piscigranja)
En un centro de acuicultura comunal en la selva central de Oxapampa, la biomasa $B(t)$ de peces en kilogramos en función del tiempo $t$ (en meses) sigue el modelo de crecimiento exponencial:

$$

B(t) = 500 \cdot e^{0.08 t}

$$

¿En cuántos meses la biomasa alcanzará los $2000\text{ kg}$? (Dato: $\ln(2) \approx 0.693$).

**Paso 1:** Planteamos la condición del problema:
$B(t) = 2000$
$500 \cdot e^{0.08 t} = 2000$

**Paso 2:** Dividimos ambos miembros entre 500:
$e^{0.08 t} = \frac{2000}{500} = 4$

**Paso 3:** Tomamos logaritmo natural ($\ln$) a ambos miembros:
$\ln(e^{0.08 t}) = \ln(4)$
$0.08 t = \ln(2^2) = 2\ln(2)$

**Paso 4:** Sustituimos el dato aproximado $\ln(2) \approx 0.693$:
$0.08 t = 2(0.693) = 1.386$

**Paso 5:** Despejamos el tiempo $t$:
$t = \frac{1.386}{0.08} = \frac{138.6}{8} = 17.325\text{ meses}$

**Respuesta:** La biomasa alcanzará los $2000\text{ kg}$ aproximadamente a los $17.3$ meses.

---

## 5. Ejercicios Propuestos para Práctica Autónomo

### Nivel Básico (Ejercicios 1 al 15)

1. Calcular el valor de $\log_3(81)$:
A) $3$
B) $4$
C) $5$
D) $27$
E) $9$

2. Hallar el valor de $\log_{1/2}(16)$:
A) $4$
B) $-4$
C) $2$
D) $-2$
E) $8$

3. Resolver la ecuación exponencial $3^{2x - 1} = 27$:
A) $1$
B) $2$
C) $3$
D) $4$
E) $5$

4. Si $\log_b(64) = 3$, ¿cuál es el valor de la base $b$?
A) $2$
B) $4$
C) $8$
D) $16$
E) $3$

5. Calcular el valor de $E = \log(1000) + \ln(e^4)$:
A) $7$
B) $12$
C) $10$
D) $3$
E) $4$

6. Reducir la suma $\log(2) + \log(5)$:
A) $0$
B) $1$
C) $7$
D) $10$
E) $\log(7)$

7. Calcular el valor del antilogaritmo: $\text{antilog}_3(4)$:
A) $12$
B) $64$
C) $81$
D) $27$
E) $243$

8. Hallar el valor de $\text{colog}_5(125)$:
A) $3$
B) $-3$
C) $1/3$
D) $-1/3$
E) $25$

9. Resolver la ecuación exponencial $2^{x^2 - 5} = 16$:
A) $\pm 3$
B) $\pm 2$
C) $\pm 1$
D) $3$
E) $9$

10. Si $\log(x) = 2$, ¿cuál es el valor de $x$?
A) $20$
B) $100$
C) $10$
D) $1000$
E) $2$

11. Calcular el valor de $7^{\log_7(15)}$:
A) $7$
B) $15$
C) $1$
D) $105$
E) $0$

12. Resolver la ecuación $\log_5(2x - 3) = 1$:
A) $4$
B) $3$
C) $5$
D) $2$
E) $1$

13. ¿Cuál es el producto de $\log_2(5) \cdot \log_5(8)$?
A) $2$
B) $3$
C) $4$
D) $5$
E) $8$

14. Si $\log_2(x) = -3$, hallar $x$:
A) $-8$
B) $1/8$
C) $1/6$
D) $8$
E) $-6$

15. Resolver $5^{x+1} = 1$:
A) $0$
B) $-1$
C) $1$
D) $5$
E) $-5$

---

### Nivel Intermedio (Ejercicios 16 al 35)

16. Resolver en $\mathbb{R}$ la ecuación $\log(x + 3) + \log(x - 3) = \log(16)$ e indicar la solución:
A) $5$
B) $-5$
C) $\pm 5$
D) $4$
E) $25$

17. Resolver la ecuación exponencial $9^x - 10 \cdot 3^x + 9 = 0$ e indicar la suma de sus soluciones:
A) $1$
B) $2$
C) $3$
D) $10$
E) $0$

18. Calcular el valor de $M = \log_4(8) + \log_9(27)$:
A) $2$
B) $3$
C) $5/2$
D) $7/2$
E) $4$

19. Si $\log(2) = a$ y $\log(3) = b$, expresar $\log(72)$ en función de $a$ y $b$:
A) $3a + 2b$
B) $2a + 3b$
C) $a^3 b^2$
D) $6ab$
E) $3a - 2b$

20. Si $\log(2) = a$, expresar $\log(5)$ en términos de $a$:
A) $1 - a$
B) $1 + a$
C) $a/2$
D) $2a$
E) $10 - a$

21. Resolver la ecuación con antilogaritmos y cologaritmos: $\log_2\left( \text{antilog}_4\left( \log_2(x) \right) \right) = 4$.  
A) $2$  
B) $4$  
C) $8$  
D) $16$  
E) $1$  

22. Hallar la solución real de la ecuación exponencial: $x^x = 3125$.  
A) $3$  
B) $4$  
C) $5$  
D) $6$  
E) $25$  

23. Resolver el sistema de ecuaciones: $\begin{cases} x + y = 65 \\ \log(x) + \log(y) = 3 \end{cases}$ e indicar el valor del mayor de los dos números:  
A) $40$
B) $50$
C) $45$
D) $60$
E) $55$

24. Un decibelímetro en un taller industrial en Ate mide el nivel de intensidad sonora $\beta$ en decibelios según $\beta = 10 \log\left(\frac{I}{I_0}\right)$. Si la intensidad de una máquina es $I = 10^8 I_0$, ¿cuál es el nivel de ruido en decibelios?
A) $70\text{ dB}$
B) $80\text{ dB}$
C) $90\text{ dB}$
D) $100\text{ dB}$
E) $60\text{ dB}$

25. Resolver en $\mathbb{R}$: $\log_x(2x^2 - 5x + 4) = 2$.  
A) $1$ ó $4$  
B) Solo $4$  
C) Solo $1$  
D) $2$  
E) $\emptyset$  

26. Calcular el valor de: $E = \log_2(6) \cdot \log_6(8) + \log_3(5) \cdot \log_5(9)$.  
A) $3$  
B) $5$  
C) $6$  
D) $4$  
E) $2$  

27. Resolver la ecuación exponencial $2^{x+2} + 2^{x+1} + 2^x = 56$:  
A) $2$  
B) $3$  
C) $4$  
D) $5$  
E) $1$  

28. Si $\log_{12}(3) = a$, expresar $\log_{12}(4)$ en función de $a$:  
A) $1 - a$  
B) $1 + a$  
C) $2a$  
D) $a/2$  
E) $4a$  

29. Determinar el valor de $x$ que satisface: $3^{\log_2(x)} = 27$.  
A) $4$  
B) $8$  
C) $9$  
D) $16$  
E) $3$  

30. Hallar el producto de las soluciones de la ecuación: $x^{\log(x)} = 100x$.  
A) $10$  
B) $100$  
C) $1000$  
D) $1$  
E) $0.1$  

31. Resolver en $\mathbb{R}$ la ecuación: $\log_2(x^2 - 4) - \log_2(x - 2) = 3$.  
A) $6$  
B) $-6$  
C) $4$  
D) $8$  
E) $2$  

32. Si $a^{\log_b(c)} = 5$, ¿cuál es el valor de $c^{\log_b(a)}$?  
A) $1/5$  
B) $5$  
C) $25$  
D) $\sqrt{5}$  
E) $10$  

33. El tiempo de duplicación de una inversión financiera en una cooperativa agraria a una tasa de interés nominal continuo del $7\%$ anual está dado por $t = \frac{\ln(2)}{0.07}$. Si $\ln(2) \approx 0.693$, ¿cuántos años tarda en duplicarse el capital?  
A) $7\text{ años}$  
B) $9.9\text{ años}$  
C) $12\text{ años}$  
D) $14.3\text{ años}$  
E) $8.5\text{ años}$  

34. Si $\log_3(x) + \log_9(x) + \log_{27}(x) = 11$, calcular el valor de $x$:  
A) $729$  
B) $243$  
C) $81$  
D) $2187$  
E) $27$  

35. Resolver la inecuación logarítmica básica: $\log_2(x - 4) < 3$.  
A) $\langle 4, 12 \rangle$  
B) $\langle -\infty, 12 \rangle$  
C) $[4, 12]$  
D) $\langle 0, 12 \rangle$  
E) $\langle 4, 8 \rangle$  

---

### Nivel Avanzado (Ejercicios 36 al 45)

36. Resolver en $\mathbb{R}$ la ecuación: $\log_2(x) + \log_4(x) + \log_{16}(x) = 7$.  
A) $16$  
B) $32$  
C) $64$  
D) $8$  
E) $128$  

37. Si $x, y, z$ son términos consecutivos de una progresión geométrica, simplificar: $E = \frac{1}{\log_x(N) + 1} + \frac{1}{\log_z(N) + 1} - \frac{2}{\log_y(N) + 1}$.  
A) $0$  
B) $1$  
C) $-1$  
D) $2$  
E) $\log_y(N)$  

38. Determinar el número de soluciones reales de la ecuación: $|x - 2| = \log_2(x)$.  
A) $1$  
B) $2$  
C) $3$  
D) $0$  
E) Infinitas  

39. Si $\log_a(bc) = 2$, $\log_b(ca) = 3$ y $\log_c(ab) = 4$, calcular el valor numérico de: $S = \frac{1}{\log_a(abc)} + \frac{1}{\log_b(abc)} + \frac{1}{\log_c(abc)}$.  
A) $1$  
B) $2$  
C) $3$  
D) $1/2$  
E) $9$  

40. Resolver la ecuación exponencial: $2^{2x+1} - 5 \cdot 6^x + 3^{2x+1} = 0$ e indicar el producto de sus raíces:  
A) $-1$
B) $0$
C) $1$
D) $2$
E) $-2$

41. **(Reto)** Si $a^2 + b^2 = 7ab$ con $a, b > 0$, demostrar la identidad de los logaritmos y hallar el valor de $k$ en: $\log\left(\frac{a + b}{3}\right) = k(\log(a) + \log(b))$.  
A) $1/2$  
B) $1/3$  
C) $1$  
D) $2$  
E) $1/4$  

42. **(Reto)** Resolver en $\mathbb{R}$ la ecuación con torre de exponentes: $x^{x^{x+1}} = 256$.  
A) $\sqrt{2}$  
B) $2$  
C) $\sqrt[4]{2}$  
D) $4$  
E) $\sqrt[3]{2}$  

43. **(Reto)** Resolver el sistema simétrico de logaritmos: $\begin{cases} \log_y(x) + \log_x(y) = \frac{5}{2} \\ xy = 64 \end{cases}$ con $x > y > 1$, e indicar el valor de $x - y$:  
A) $12$
B) $14$
C) $16$
D) $15$
E) $18$

44. **(Reto)** Calcular el valor exacto de la suma finita: $S = \sum_{k=2}^{100} \frac{1}{\log_k(100!)}$.  
A) $1$  
B) $100$  
C) $0$  
D) $2$  
E) $99$  

45. **(Reto)** Si $\alpha$ y $\beta$ son las soluciones de la ecuación $x^{\log_3(x)} = 9x$, calcular el valor exacto de $\alpha \cdot \beta$:  
A) $3$  
B) $9$  
C) $27$  
D) $1$  
E) $81$  

---

## 6. Claves de Respuestas y Pistas Estratégicas

### Claves de Respuestas

| N° | Clave | N° | Clave | N° | Clave | N° | Clave | N° | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **10** | B | **19** | A | **28** | A | **37** | A |
| **2** | B | **11** | B | **20** | A | **29** | B | **38** | B |
| **3** | B | **12** | A | **21** | B | **30** | B | **39** | A |
| **4** | B | **13** | B | **22** | C | **31** | A | **40** | A |
| **5** | A | **14** | B | **23** | B | **32** | B | **41** | A |
| **6** | B | **15** | B | **24** | B | **33** | B | **42** | B |
| **7** | C | **16** | A | **25** | B | **34** | A | **43** | A |
| **8** | B | **17** | B | **26** | B | **35** | A | **44** | A |
| **9** | A | **18** | B | **27** | B | **36** | A | **45** | A |

---

### Pistas Estratégicas para Ejercicios Reto (41 al 45)

* **Pista 41:** Suma $2ab$ a ambos miembros de la condición inicial: $a^2 + 2ab + b^2 = 9ab \implies (a + b)^2 = 9ab$. Divide entre 9: $\left(\frac{a + b}{3}\right)^2 = ab$. Toma logaritmos a ambos lados y aplica la regla del sombrero: $2\log\left(\frac{a + b}{3}\right) = \log(ab) = \log(a) + \log(b)$. Concluye que $k = 1/2$.
* **Pista 42:** Aplica la ley de potencia de potencia $(A^B)^C = A^{B \cdot C}$: $(x^x)^{x^x} = x^{x \cdot x^x} = x^{x^{x+1}} = 256$. Como $256 = 4^4$, por comparación o cambio de variable $u = x^x$ se tiene $u^u = 4^4 \implies u = 4$. Luego $x^x = 4 = 2^2 \implies x = 2$.
* **Pista 43:** Sea $u = \log_y(x)$. Como $\log_x(y) = 1/u$, la primera ecuación es $u + \frac{1}{u} = \frac{5}{2} \implies 2u^2 - 5u + 2 = 0 \implies u = 2$ ó $u = 1/2$. Como $x > y > 1$, tomamos $u = 2 \implies \log_y(x) = 2 \implies x = y^2$. Sustituyendo en $xy = 64 \implies y^3 = 64 \implies y = 4$ y $x = 16$. La diferencia requerida es $x - y = 16 - 4 = 12$.
* **Pista 44:** Invierte cada término de la suma aplicando la regla de cambio de base: $\frac{1}{\log_k(100!)} = \log_{100!}(k)$. La suma se transforma en una suma de logaritmos de igual base: $\sum_{k=2}^{100} \log_{100!}(k) = \log_{100!}(2 \cdot 3 \cdot 4 \cdots 100) = \log_{100!}(100!) = 1$.
* **Pista 45:** Aplica logaritmo en base 3 a ambos miembros: $\log_3(x^{\log_3(x)}) = \log_3(9x) \implies (\log_3(x))^2 = \log_3(9) + \log_3(x) = 2 + \log_3(x)$. Haciendo $u = \log_3(x)$, se tiene la ecuación cuadrática $u^2 - u - 2 = 0$. Por el Teorema de Cardano-Vieta, la suma de las raíces es $u_1 + u_2 = 1$. Como $u_1 + u_2 = \log_3(\alpha) + \log_3(\beta) = \log_3(\alpha \cdot \beta) = 1 \implies \alpha \cdot \beta = 3^1 = 3$.

---

## 7. Formulario Resumen

| Concepto / Teorema | Expresión Matemática | Restricciones y Propiedades |
| :--- | :--- | :--- |
| **Definición de Logaritmo** | $\log_b(N) = x \iff b^x = N$ | $N > 0, b > 0, b \neq 1$ |
| **Cancelación Exponencial** | $b^{\log_b(N)} = N$ | Válida para todo $N > 0$ |
| **Cancelación Logarítmica** | $\log_b(b^x) = x$ | Válida para todo $x \in \mathbb{R}$ |
| **Logaritmo del Producto** | $\log_b(M \cdot N) = \log_b(M) + \log_b(N)$ | Convierte multiplicación en adición |
| **Logaritmo del Cociente** | $\log_b(M / N) = \log_b(M) - \log_b(N)$ | Convierte división en sustracción |
| **Regla del Sombrero** | $\log_b(N^k) = k \log_b(N)$ | El exponente baja como coeficiente |
| **Exponentes Compuestos** | $\log_{b^m}(N^k) = \frac{k}{m} \log_b(N)$ | Razón de potencias de argumento y base |
| **Cambio de Base** | $\log_b(N) = \frac{\log_c(N)}{\log_c(b)}$ | Permite evaluar en bases decimal y natural |
| **Inversión de Base** | $\log_b(a) \cdot \log_a(b) = 1$ | Producto de logaritmos recíprocos |
| **Regla de la Cadena** | $\log_b(a) \cdot \log_c(b) \cdot \log_d(c) = \log_d(a)$ | Cancelación de argumentos y bases cruzadas |
| **Permuta de Base-Argumento**| $a^{\log_b(c)} = c^{\log_b(a)}$ | Intercambio de extremos en potencias |
| **Cologaritmo** | $\text{colog}_b(N) = -\log_b(N) = \log_b(1/N)$ | Opuesto aditivo del logaritmo |
| **Antilogaritmo** | $\text{antilog}_b(x) = b^x$ | Operación inversa exponencial |
| **Bases Iguales Exponencial**| $a^{f(x)} = a^{g(x)} \iff f(x) = g(x)$ | Válido para $a > 0, a \neq 1$ |
| **Inyectividad Logarítmica** | $\log_b(f(x)) = \log_b(g(x)) \iff f(x) = g(x)$ | Exige verificar contra el C.V.A. |
