# Tema 03: Identidades Trigonométricas Fundamentales

## 1. Motivación y Contexto Real

Las identidades trigonométricas son las herramientas de simplificación analítica que permiten transformar expresiones complejas e inmanejables en fórmulas compactas, evaluables y computables. En la era digital, casi toda la tecnología de telecomunicaciones, compresión de archivos multimedia y procesamiento de señales se fundamenta en estas equivalencias.

En las aplicaciones de ingeniería y ciencia en el Perú:
1. **Telecomunicaciones y Telefonía Móvil:** Toda onda electromagnética (radio, televisión, 4G, 5G) viaja como una superposición de ondas senoidales y cosenoidales. Las identidades trigonométricas permiten demodular y filtrar el ruido de fondo para que las llamadas celulares no se corten en zonas de difícil cobertura.
2. **Ingeniería Sísmica y Resonancia:** En un país altamente sísmico como el Perú, los ingenieros calculan las frecuencias naturales de oscilación de edificios y puentes atirantados utilizando ecuaciones diferenciales trigonométricas, donde las identidades pitagóricas simplifican las matrices de rigidez estructural.
3. **Compresión de Audio y Video (MP3, MP4, JPEG):** Los algoritmos de compresión emplean la Transformada Discreta del Coseno (DCT), la cual convierte millones de muestras de sonido en sumas trigonométricas equivalentes donde los términos despreciables se eliminan sin perder calidad perceptible.

```{figure} ../../assets/trigonometria/circulo_trigonometrico_identidades.svg
---
width: 95%
align: center
alt: Circunferencia Trigonométrica e Identidades Fundamentales
---
*Diagrama analítico en TikZ con la circunferencia trigonométrica unitaria ($R=1$), la descomposición en seno y coseno, y el compendio de identidades pitagóricas, cocientes y recíprocas.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Concepto de Identidad Trigonométrica

Una **identidad trigonométrica** es una igualdad algebraica entre razones trigonométricas que se verifica para **todos los valores admisibles** de la variable angular, es decir, para todos aquellos valores donde las razones intervinientes se encuentren bien definidas en el campo real ($\mathbb{R}$).

*Valores no admisibles típicos:*
* $\tan\theta$ y $\sec\theta$ no existen si $\theta = (2k+1)\frac{\pi}{2} = 90^\circ, 270^\circ, \dots$ (denominador $\cos\theta = 0$).
* $\cot\theta$ y $\csc\theta$ no existen si $\theta = k\pi = 0^\circ, 180^\circ, 360^\circ, \dots$ (denominador $\sin\theta = 0$).

---

### 2.2 Las Tres Familias de Identidades Fundamentales

#### 1. Identidades Pitagóricas
Derivan directamente del Teorema de Pitágoras en la circunferencia unitaria ($x^2 + y^2 = 1$):

1. **Fundamental del Seno y Coseno:**

$$\sin^2\theta + \cos^2\theta = 1$$

   *Despejes de alta frecuencia:*

$$\sin^2\theta = 1 - \cos^2\theta = (1 + \cos\theta)(1 - \cos\theta)$$

$$\cos^2\theta = 1 - \sin^2\theta = (1 + \sin\theta)(1 - \sin\theta)$$

2. **De la Tangente y Secante:**
   Dividiendo entre $\cos^2\theta$:

$$1 + \tan^2\theta = \sec^2\theta \implies \sec^2\theta - \tan^2\theta = 1$$

   *Diferencia de cuadrados (propiedad clave en Beca 18):*

$$(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = 1 \iff \sec\theta + \tan\theta = \frac{1}{\sec\theta - \tan\theta}$$

3. **De la Cotangente y Cosecante:**
   Dividiendo entre $\sin^2\theta$:

$$1 + \cot^2\theta = \csc^2\theta \implies \csc^2\theta - \cot^2\theta = 1$$

   *Diferencia de cuadrados:*

$$(\csc\theta + \cot\theta)(\csc\theta - \cot\theta) = 1 \iff \csc\theta + \cot\theta = \frac{1}{\csc\theta - \cot\theta}$$

---

#### 2. Identidades por Cociente
Expresan a la tangente y cotangente en términos exclusivos de senos y cosenos:

$$\tan\theta = \frac{\sin\theta}{\cos\theta} \qquad\qquad \cot\theta = \frac{\cos\theta}{\sin\theta}$$

---

#### 3. Identidades Recíprocas
Relacionan cada razón con su inversa multiplicativa:

$$\sin\theta \cdot \csc\theta = 1 \implies \csc\theta = \frac{1}{\sin\theta}$$

$$\cos\theta \cdot \sec\theta = 1 \implies \sec\theta = \frac{1}{\cos\theta}$$

$$\tan\theta \cdot \cot\theta = 1 \implies \cot\theta = \frac{1}{\tan\theta}$$

---

### 2.3 Identidades Auxiliares de Alto Impacto

Estas identidades se deducen algebraicamente de las fundamentales y ahorran tiempo valioso en exámenes cronometrados:

1. **Suma de Tangente y Cotangente:**

$$\tan\theta + \cot\theta = \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta} = \frac{\sin^2\theta + \cos^2\theta}{\sin\theta \cos\theta} = \frac{1}{\sin\theta \cos\theta} = \sec\theta \csc\theta$$

$$\tan\theta + \cot\theta = \sec\theta \csc\theta$$

2. **Suma de Cuadrados de Secante y Cosecante:**

$$\sec^2\theta + \csc^2\theta = \sec^2\theta \cdot \csc^2\theta$$

3. **Cuartas Potencias:**
   Elevando al cuadrado $\sin^2\theta + \cos^2\theta = 1$:

$$\sin^4\theta + \cos^4\theta = 1 - 2\sin^2\theta \cos^2\theta$$

4. **Sextas Potencias:**
   Elevando al cubo $\sin^2\theta + \cos^2\theta = 1$:

$$\sin^6\theta + \cos^6\theta = 1 - 3\sin^2\theta \cos^2\theta$$

5. **Trinomio al Cuadrado Especial:**

$$(1 \pm \sin\theta \pm \cos\theta)^2 = 2(1 \pm \sin\theta)(1 \pm \cos\theta)$$

---

### 2.4 Estrategias Heurísticas de Simplificación

Para simplificar expresiones o demostrar identidades en exámenes:
1. **Paso a Senos y Cosenos:** Si una expresión contiene mezcla de tangentes, cotangentes, secantes o cosecantes, reescriba todo en función de $\sin\theta$ y $\cos\theta$.
2. **Uso de Productos Notables:** Aplique diferencias de cuadrados ($a^2 - b^2$), binomios al cuadrado ($a \pm b)^2$ y factorización por factor común.
3. **Multiplicación por el Conjugado:** Cuando aparezcan expresiones como $\frac{1}{1 \pm \sin\theta}$ o $\frac{1}{1 \pm \cos\theta}$, multiplique numerador y denominador por el conjugado ($1 \mp \sin\theta$) para formar la identidad pitagórica en el denominador.

---

### 2.5 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Olvidar los cuadrados en la identidad pitagórica:** $\sin\theta + \cos\theta \ne 1$. La relación exige estrictamente los cuadrados: $\sin^2\theta + \cos^2\theta = 1$.
> 2. **Confundir $\sec^2\theta - \tan^2\theta = 1$ con $\tan^2\theta - \sec^2\theta = 1$:** Si los términos están invertidos, el resultado es $-1$, no $1$.
> 3. **Asumir que $\sec\theta + \tan\theta = x$ implica $\sec\theta = x/2$:** No; si $\sec\theta + \tan\theta = x$, entonces $\sec\theta - \tan\theta = \frac{1}{x}$. Sumando ambas: $2\sec\theta = x + \frac{1}{x} \implies \sec\theta = \frac{x^2 + 1}{2x}$.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Identidades Fundamentales)

#### Ejercicio 1
Simplifique la siguiente expresión trigonométrica:

$$E = (\sin\theta + \cos\theta)^2 + (\sin\theta - \cos\theta)^2$$

**Análisis Conceptual:**
Desarrollamos ambos binomios al cuadrado mediante el producto notable $(a \pm b)^2 = a^2 \pm 2ab + b^2$ y agrupamos usando la identidad pitagórica fundamental $\sin^2\theta + \cos^2\theta = 1$.

**Solución Paso a Paso:**

**Paso 1:** Desarrollar el primer binomio al cuadrado:

$$(\sin\theta + \cos\theta)^2 = \sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta$$

**Paso 2:** Desarrollar el segundo binomio al cuadrado:

$$(\sin\theta - \cos\theta)^2 = \sin^2\theta - 2\sin\theta\cos\theta + \cos^2\theta$$

**Paso 3:** Sumar ambas expresiones:

$$E = (\sin^2\theta + \cos^2\theta) + (\sin^2\theta + \cos^2\theta) + (2\sin\theta\cos\theta - 2\sin\theta\cos\theta)$$

$$E = 1 + 1 + 0 = 2$$

**Conclusión:**
La expresión simplificada es idénticamente igual a $2$.

---

#### Ejercicio 2
Simplifique la expresión trigonométrica:

$$K = \frac{\tan\theta + \cot\theta}{\sec\theta}$$

**Análisis Conceptual:**
Expresamos todo en términos de senos y cosenos, o empleamos la identidad auxiliar $\tan\theta + \cot\theta = \sec\theta \csc\theta$.

**Solución Paso a Paso:**

**Paso 1:** Aplicar la identidad auxiliar $\tan\theta + \cot\theta = \sec\theta \csc\theta$:

$$K = \frac{\sec\theta \csc\theta}{\sec\theta}$$

**Paso 2:** Simplificar el factor común $\sec\theta$:

$$K = \csc\theta$$

**Conclusión:**
La expresión simplificada es $K = \csc\theta$.

---

#### Ejercicio 3
Si $\sin\theta + \cos\theta = \frac{4}{3}$, calcule el valor del producto $\sin\theta \cdot \cos\theta$.

**Análisis Conceptual:**
Elevamos ambos miembros de la ecuación al cuadrado para hacer aparecer el término cruzado $2\sin\theta\cos\theta$ y la identidad pitagórica $\sin^2\theta + \cos^2\theta = 1$.

**Solución Paso a Paso:**

**Paso 1:** Elevar al cuadrado ambos miembros:

$$(\sin\theta + \cos\theta)^2 = \left(\frac{4}{3}\right)^2$$

**Paso 2:** Desarrollar el binomio al cuadrado:

$$\sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = \frac{16}{9}$$

**Paso 3:** Reemplazar $\sin^2\theta + \cos^2\theta = 1$:

$$1 + 2\sin\theta\cos\theta = \frac{16}{9}$$

**Paso 4:** Despejar el producto:

$$2\sin\theta\cos\theta = \frac{16}{9} - 1 = \frac{7}{9}$$

$$\sin\theta\cos\theta = \frac{7}{18}$$

**Conclusión:**
El valor del producto $\sin\theta \cdot \cos\theta$ es $\frac{7}{18}$.

---

### Nivel 2: Intermedio (Propiedades y Reducciones)

#### Ejercicio 4
Si $\sec\theta - \tan\theta = \frac{1}{4}$, determine el valor de $\cos\theta$.

**Análisis Conceptual:**
Utilizamos la propiedad de que $\sec\theta + \tan\theta$ y $\sec\theta - \tan\theta$ son inversos multiplicativos porque $\sec^2\theta - \tan^2\theta = 1$. Se forma un sistema simple para hallar $\sec\theta$ y de allí su recíproco $\cos\theta$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la identidad de la diferencia de cuadrados:

$$\sec\theta + \tan\theta = \frac{1}{\sec\theta - \tan\theta} = \frac{1}{1/4} = 4$$

**Paso 2:** Sumar miembro a miembro ambas ecuaciones:

$$(\sec\theta + \tan\theta) + (\sec\theta - \tan\theta) = 4 + \frac{1}{4}$$

$$2\sec\theta = \frac{17}{4} \implies \sec\theta = \frac{17}{8}$$

**Paso 3:** Calcular $\cos\theta$ mediante la razón recíproca:

$$\cos\theta = \frac{1}{\sec\theta} = \frac{8}{17}$$

**Conclusión:**
El valor de $\cos\theta$ es $\frac{8}{17}$.

---

#### Ejercicio 5
Reduzca a su mínima expresión:

$$M = \frac{1}{1 + \sin\theta} + \frac{1}{1 - \sin\theta}$$

**Análisis Conceptual:**
Efectuamos la suma de fracciones heterogéneas encontrando el común denominador $(1 + \sin\theta)(1 - \sin\theta) = 1 - \sin^2\theta = \cos^2\theta$.

**Solución Paso a Paso:**

**Paso 1:** Sumar las fracciones cruzadas:

$$M = \frac{(1 - \sin\theta) + (1 + \sin\theta)}{(1 + \sin\theta)(1 - \sin\theta)}$$

**Paso 2:** Simplificar el numerador:

$$\text{Numerador} = 1 - \sin\theta + 1 + \sin\theta = 2$$

**Paso 3:** Simplificar el denominador usando la identidad pitagórica:

$$\text{Denominador} = 1 - \sin^2\theta = \cos^2\theta$$

**Paso 4:** Reescribir la fracción resultante:

$$M = \frac{2}{\cos^2\theta} = 2\sec^2\theta$$

**Conclusión:**
La mínima expresión es $M = 2\sec^2\theta$.

---

#### Ejercicio 6
Calcule el valor numérico de la expresión:

$$W = 3(\sin^4\theta + \cos^4\theta) - 2(\sin^6\theta + \cos^6\theta)$$

**Análisis Conceptual:**
Aplicamos las identidades auxiliares de cuartas y sextas potencias:
$\sin^4\theta + \cos^4\theta = 1 - 2\sin^2\theta\cos^2\theta$
$\sin^6\theta + \cos^6\theta = 1 - 3\sin^2\theta\cos^2\theta$

**Solución Paso a Paso:**

**Paso 1:** Sustituir las identidades auxiliares:

$$W = 3(1 - 2\sin^2\theta\cos^2\theta) - 2(1 - 3\sin^2\theta\cos^2\theta)$$

**Paso 2:** Aplicar la propiedad distributiva:

$$W = 3 - 6\sin^2\theta\cos^2\theta - 2 + 6\sin^2\theta\cos^2\theta$$

**Paso 3:** Reducir términos semejantes:

$$W = (3 - 2) + (-6\sin^2\theta\cos^2\theta + 6\sin^2\theta\cos^2\theta) = 1 + 0 = 1$$

**Conclusión:**
El valor numérico de la expresión es $1$, constante e independiente del ángulo $\theta$.

---

#### Ejercicio 7
Demuestre y simplifique la expresión:

$$H = \frac{\sin\theta}{1 + \cos\theta} + \frac{1 + \cos\theta}{\sin\theta}$$

**Análisis Conceptual:**
Sumamos las fracciones algebraicamente para generar la identidad pitagórica fundamental en el numerador.

**Solución Paso a Paso:**

**Paso 1:** Efectuar la suma de fracciones:

$$H = \frac{\sin^2\theta + (1 + \cos\theta)^2}{\sin\theta(1 + \cos\theta)}$$

**Paso 2:** Desarrollar el binomio al cuadrado:

$$(1 + \cos\theta)^2 = 1 + 2\cos\theta + \cos^2\theta$$

$$H = \frac{\sin^2\theta + 1 + 2\cos\theta + \cos^2\theta}{\sin\theta(1 + \cos\theta)}$$

**Paso 3:** Agrupar $\sin^2\theta + \cos^2\theta = 1$:

$$H = \frac{(1) + 1 + 2\cos\theta}{\sin\theta(1 + \cos\theta)} = \frac{2 + 2\cos\theta}{\sin\theta(1 + \cos\theta)}$$

**Paso 4:** Factorizar el $2$ en el numerador y simplificar:

$$H = \frac{2(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)} = \frac{2}{\sin\theta} = 2\csc\theta$$

**Conclusión:**
La expresión simplificada es $H = 2\csc\theta$.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Optimización de Energía en Señal de Antena de Telecomunicación)
En una torre de transmisión de microondas de Entel en la sierra de Huancavelica, la potencia de radiación electromagnética instantánea $P(t)$ en vatios está modelada por la expresión:

$$P(t) = P_0 \cdot \left[ (\sec\theta + \tan\theta)^2 + (\sec\theta - \tan\theta)^2 - 2 \right]$$

donde $\theta$ es el desfase de modulación y $P_0 = 50\text{ W}$ es la potencia base. Si se sabe que $\sec\theta \cdot \tan\theta = \sqrt{3}$, calcule el valor exacto de la potencia de transmisión $P(t)$.

**Análisis Conceptual:**
Llamemos $a = \sec\theta$ y $b = \tan\theta$.
La expresión interior es $(a + b)^2 + (a - b)^2 - 2$.
Por la identidad de Legendre: $(a+b)^2 + (a-b)^2 = 2(a^2 + b^2)$.
Por lo tanto: $2(a^2 + b^2) - 2 = 2(\sec^2\theta + \tan^2\theta - 1)$.
Como $\sec^2\theta - 1 = \tan^2\theta$, la expresión se simplifica a $2(2\tan^2\theta) = 4\tan^2\theta$.
También podemos expresarlo con el dato del producto.

**Solución Paso a Paso:**

**Paso 1:** Desarrollar la expresión de Legendre:

$$(\sec\theta + \tan\theta)^2 + (\sec\theta - \tan\theta)^2 = 2(\sec^2\theta + \tan^2\theta)$$

**Paso 2:** Restar el $2$ y aplicar la identidad pitagórica $\sec^2\theta - 1 = \tan^2\theta$:

$$2(\sec^2\theta + \tan^2\theta) - 2 = 2(\sec^2\theta + \tan^2\theta - 1) = 2(\tan^2\theta + \tan^2\theta) = 4\tan^2\theta$$

**Paso 3:** Usar el dato $\sec\theta \cdot \tan\theta = \sqrt{3}$:
Sabemos que $\sec^2\theta = 1 + \tan^2\theta$.
Elevando al cuadrado el dato: $\sec^2\theta \cdot \tan^2\theta = (\sqrt{3})^2 = 3$.

$$(1 + \tan^2\theta)\tan^2\theta = 3 \implies (\tan^2\theta)^2 + \tan^2\theta - 3 = 0$$

Sea $u = \tan^2\theta$:

$$u^2 + u - 3 = 0 \implies u = \frac{-1 + \sqrt{1 - 4(1)(-3)}}{2} = \frac{-1 + \sqrt{13}}{2}$$

**Paso 4:** Calcular la potencia final $P(t) = P_0 \cdot 4u$:

$$P(t) = 50 \cdot 4 \cdot \left(\frac{\sqrt{13} - 1}{2}\right) = 100(\sqrt{13} - 1)\text{ W} \approx 100(3.6055 - 1) \approx 260.55\text{ W}$$

**Conclusión:**
La potencia de radiación de la antena es de $100(\sqrt{13}-1)\text{ W} \approx 260.55\text{ W}$.

---

#### Ejercicio 9 (Filtrado de Ruido Armónico en Subestación Eléctrica del Mantaro)
En el monitoreo de armónicos eléctricos de la central hidroeléctrica del Mantaro, una onda de voltaje parásita $V(\theta)$ viene descrita por la ecuación:

$$V(\theta) = V_{\text{pico}} \cdot \frac{\sin^4\theta - \cos^4\theta}{\sin^2\theta - \cos^2\theta} + V_{\text{pico}} \cdot (\tan\theta \cos\theta)^2$$

con $V_{\text{pico}} = 220\text{ V}$. Reduzca la ecuación a su mínima expresión y determine el valor constante del voltaje RMS efectivo detectado por los filtros de protección.

**Análisis Conceptual:**
El numerador $\sin^4\theta - \cos^4\theta$ es una diferencia de cuadrados: $(\sin^2\theta + \cos^2\theta)(\sin^2\theta - \cos^2\theta)$. Como $\sin^2\theta + \cos^2\theta = 1$, la primera fracción se simplifica a la unidad. En el segundo término, $\tan\theta \cos\theta = \sin\theta$.

**Solución Paso a Paso:**

**Paso 1:** Factorizar el primer término:

$$\sin^4\theta - \cos^4\theta = (\sin^2\theta + \cos^2\theta)(\sin^2\theta - \cos^2\theta) = 1 \cdot (\sin^2\theta - \cos^2\theta)$$

Por lo tanto:

$$\frac{\sin^4\theta - \cos^4\theta}{\sin^2\theta - \cos^2\theta} = 1$$

**Paso 2:** Simplificar el segundo término:

$$\tan\theta \cdot \cos\theta = \frac{\sin\theta}{\cos\theta} \cdot \cos\theta = \sin\theta$$

$$(\tan\theta \cos\theta)^2 = \sin^2\theta$$

**Paso 3:** Reensamblar la expresión de voltaje:

$$V(\theta) = V_{\text{pico}}(1 + \sin^2\theta)$$

Cuando la señal se encuentra en su nodo principal ($\theta = 0$): $V = V_{\text{pico}} = 220\text{ V}$.
El término base filtrado corresponde a $220\text{ V}$.

**Conclusión:**
La expresión se reduce a $V(\theta) = 220(1 + \sin^2\theta)\text{ V}$, donde la componente fundamental constante es de $220\text{ V}$.

---

#### Ejercicio 10 (Diseño de Disipador Sísmico en Edificio Multifamiliar de Lima)
El coeficiente de amortiguamiento dinámico $C(\theta)$ de un disipador viscoso en un edificio de Miraflores cumple la relación trigonométrica:

$$C(\theta) = C_0 \cdot \frac{\sec\theta - \cos\theta}{\csc\theta - \sin\theta}$$

donde $C_0 = 150\text{ kN}\cdot\text{s/m}$. Demuestre que el coeficiente puede expresarse como una sola razón trigonométrica al cubo de $\theta$, y calcule su valor si $\theta = 30^\circ$.

**Análisis Conceptual:**
Transformamos el numerador y denominador a senos y cosenos:
- Numerador: $\sec\theta - \cos\theta = \frac{1}{\cos\theta} - \cos\theta = \frac{1 - \cos^2\theta}{\cos\theta} = \frac{\sin^2\theta}{\cos\theta}$.
- Denominador: $\csc\theta - \sin\theta = \frac{1}{\sin\theta} - \sin\theta = \frac{1 - \sin^2\theta}{\sin\theta} = \frac{\cos^2\theta}{\sin\theta}$.

**Solución Paso a Paso:**

**Paso 1:** Expresar numerador y denominador con fracciones homogéneas:

$$\text{Numerador} = \frac{\sin^2\theta}{\cos\theta}$$

$$\text{Denominador} = \frac{\cos^2\theta}{\sin\theta}$$

**Paso 2:** Dividir mediante producto de extremos y medios:

$$\frac{\frac{\sin^2\theta}{\cos\theta}}{\frac{\cos^2\theta}{\sin\theta}} = \frac{\sin^2\theta \cdot \sin\theta}{\cos\theta \cdot \cos^2\theta} = \frac{\sin^3\theta}{\cos^3\theta} = \tan^3\theta$$

**Paso 3:** Evaluar para $\theta = 30^\circ$ con $\tan(30^\circ) = \frac{\sqrt{3}}{3}$:

$$\tan^3(30^\circ) = \left(\frac{\sqrt{3}}{3}\right)^3 = \frac{3\sqrt{3}}{27} = \frac{\sqrt{3}}{9}$$

**Paso 4:** Calcular el valor numérico de $C(30^\circ)$:

$$C(30^\circ) = 150 \cdot \frac{\sqrt{3}}{9} = \frac{50\sqrt{3}}{3}\text{ kN}\cdot\text{s/m} \approx \frac{50(1.732)}{3} \approx 28.87\text{ kN}\cdot\text{s/m}$$

**Conclusión:**
El coeficiente se reduce a $C(\theta) = C_0 \tan^3\theta$, y para $\theta = 30^\circ$ su valor es de $\frac{50\sqrt{3}}{3}\text{ kN}\cdot\text{s/m} \approx 28.87\text{ kN}\cdot\text{s/m}$.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. Simplifique la expresión: $E = \sin\theta \cdot \csc\theta + \cos\theta \cdot \sec\theta$.  
A) $1$  
B) $2$  
C) $3$  
D) $0$  
E) $\sin\theta\cos\theta$  

2. Reduzca la expresión: $K = \tan\theta \cdot \cos\theta$.  
A) $\sin\theta$  
B) $\cos\theta$  
C) $\sec\theta$  
D) $\csc\theta$  
E) $1$  

3. Simplifique: $M = (1 - \sin^2\theta) \cdot \sec^2\theta$.  
A) $\sin^2\theta$  
B) $\cos^2\theta$  
C) $1$  
D) $2$  
E) $\tan^2\theta$  

4. Calcule el valor de: $P = \sec^2(25^\circ) - \tan^2(25^\circ)$.  
A) $0$  
B) $1$  
C) $2$  
D) $-1$  
E) $\frac{1}{2}$  

5. Si $\sin\theta = \frac{3}{5}$ con $\theta$ agudo, calcule $\cos\theta$ mediante la identidad pitagórica.  
A) $\frac{2}{5}$  
B) $\frac{4}{5}$  
C) $\frac{3}{4}$  
D) $\frac{5}{4}$  
E) $\frac{1}{5}$  

6. Simplifique: $E = \cos\theta \cdot \tan\theta \cdot \csc\theta$.  
A) $\sin\theta$  
B) $\cos\theta$  
C) $1$  
D) $2$  
E) $\cot\theta$  

7. Reduzca la expresión: $W = (1 + \tan^2\theta)\cos^2\theta$.  
A) $1$  
B) $\sin^2\theta$  
C) $\cos^2\theta$  
D) $\tan^2\theta$  
E) $\sec^2\theta$  

8. Calcule el valor de: $Q = \csc^2(40^\circ) - \cot^2(40^\circ)$.  
A) $-1$  
B) $0$  
C) $1$  
D) $2$  
E) $\sqrt{2}$  

9. Si $\tan\theta = \frac{5}{12}$ con $\theta$ agudo, halle $\sec\theta$.  
A) $\frac{12}{13}$  
B) $\frac{13}{12}$  
C) $\frac{13}{5}$  
D) $\frac{5}{13}$  
E) $\frac{17}{12}$  

10. Simplifique: $H = \frac{\sin^2\theta}{1 - \cos\theta} - \cos\theta$.  
A) $0$  
B) $1$  
C) $-1$  
D) $2$  
E) $\sin\theta$  

11. La identidad $\tan\theta + \cot\theta$ es idénticamente igual a:  
A) $\sin\theta\cos\theta$  
B) $\sec\theta\csc\theta$  
C) $\sec^2\theta\csc^2\theta$  
D) $\tan^2\theta$  
E) $1$  

12. Si $\cos\theta = \frac{1}{3}$, calcule $\sin^2\theta$.  
A) $\frac{1}{9}$  
B) $\frac{2}{3}$  
C) $\frac{8}{9}$  
D) $\frac{4}{9}$  
E) $\frac{2\sqrt{2}}{3}$  

13. Reduzca: $E = \cot\theta \cdot \sin\theta$.  
A) $\cos\theta$  
B) $\sec\theta$  
C) $\tan\theta$  
D) $1$  
E) $\csc\theta$  

14. Simplifique: $A = (1 - \cos^2\theta)(1 + \cot^2\theta)$.  
A) $\sin^2\theta$  
B) $\cos^2\theta$  
C) $1$  
D) $2$  
E) $\tan^2\theta$  

15. Calcule el valor de: $M = \sin^2(10^\circ) + \sin^2(80^\circ)$.  
A) $0$  
B) $\frac{1}{2}$  
C) $1$  
D) $2$  
E) $\sqrt{2}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. Si $\sin\theta - \cos\theta = \frac{1}{2}$, determine el valor de $\sin\theta \cdot \cos\theta$.  
A) $\frac{1}{4}$  
B) $\frac{3}{8}$  
C) $\frac{1}{2}$  
D) $\frac{5}{8}$  
E) $\frac{3}{4}$  

17. Simplifique la expresión: $E = \frac{\sin\theta}{1 + \cos\theta} + \frac{\sin\theta}{1 - \cos\theta}$.  
A) $2\sin\theta$  
B) $2\cos\theta$  
C) $2\csc\theta$  
D) $2\sec\theta$  
E) $2\tan\theta$  

18. Si $\sec\theta + \tan\theta = 3$, halle el valor de $\sec\theta - \tan\theta$.  
A) $-3$  
B) $\frac{1}{3}$  
C) $-\frac{1}{3}$  
D) $\frac{2}{3}$  
E) $1$  

19. Reduzca a su mínima expresión: $K = (\sec\theta - \cos\theta)(\csc\theta - \sin\theta)$.  
A) $\sin\theta\cos\theta$  
B) $\tan\theta$  
C) $\cot\theta$  
D) $1$  
E) $\sec\theta\csc\theta$  

20. Si $\tan\theta + \cot\theta = 4$, determine el valor de $\tan^2\theta + \cot^2\theta$.  
A) $12$  
B) $14$  
C) $16$  
D) $18$  
E) $20$  

21. Simplifique: $W = \sin^4\theta - \cos^4\theta + 2\cos^2\theta$.  
A) $0$  
B) $1$  
C) $2$  
D) $\sin^2\theta$  
E) $\cos^2\theta$  

22. Si $\csc\theta - \cot\theta = \frac{1}{5}$, determine el valor de $\csc\theta$.  
A) $\frac{12}{5}$  
B) $\frac{13}{5}$  
C) $\frac{14}{5}$  
D) $3$  
E) $\frac{26}{5}$  

23. Reduzca la expresión: $P = \frac{\tan\theta}{\sec\theta - 1} - \frac{\tan\theta}{\sec\theta + 1}$.  
A) $2\sin\theta$  
B) $2\cos\theta$  
C) $2\cot\theta$  
D) $2\tan\theta$  
E) $2\csc\theta$  

24. Si $\sin^4\theta + \cos^4\theta = \frac{7}{9}$, calcule el valor del producto $\sin\theta \cdot \cos\theta$.  
A) $\frac{1}{3}$  
B) $\frac{1}{2}$  
C) $\frac{2}{3}$  
D) $\frac{1}{4}$  
E) $\frac{\sqrt{2}}{3}$  

25. Simplifique: $M = \frac{1 + \sin\theta}{\cos\theta} + \frac{\cos\theta}{1 + \sin\theta}$.  
A) $2\sin\theta$  
B) $2\cos\theta$  
C) $2\sec\theta$  
D) $2\csc\theta$  
E) $2\tan\theta$  

26. Si $\tan\theta + \cot\theta = 3$, calcule el valor de $\sin^6\theta + \cos^6\theta$.  
A) $\frac{1}{3}$  
B) $\frac{2}{3}$  
C) $\frac{4}{9}$  
D) $\frac{5}{9}$  
E) $\frac{2}{9}$  

27. Reduzca la expresión: $R = \sqrt{\frac{1 + \sin\theta}{1 - \sin\theta}}$ para $\theta$ agudo.  
A) $\sec\theta + \tan\theta$  
B) $\sec\theta - \tan\theta$  
C) $\csc\theta + \cot\theta$  
D) $\csc\theta - \cot\theta$  
E) $\sin\theta + \cos\theta$  

28. Si $\sec\theta = x + \frac{1}{4x}$, determine una expresión equivalente para $\sec\theta + \tan\theta$ para $x > 0$ con $\theta$ en el primer cuadrante.  
A) $x$  
B) $2x$  
C) $4x$  
D) $\frac{1}{2x}$  
E) $\frac{x}{2}$  

29. Simplifique: $E = \frac{\sec^2\theta + \csc^2\theta}{\sec^2\theta \cdot \csc^2\theta}$.  
A) $0$  
B) $1$  
C) $2$  
D) $\sin^2\theta$  
E) $\cos^2\theta$  

30. Calcule el valor de $k$ para que la siguiente igualdad sea una identidad: $\frac{\cos\theta}{1 - \sin\theta} = \frac{1 + \sin\theta}{k}$.  
A) $\sin\theta$  
B) $\cos\theta$  
C) $\tan\theta$  
D) $1$  
E) $\sec\theta$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. En un circuito electrónico RLC para telecomunicaciones, la impedancia reactiva $Z(\theta)$ cumple la relación:  

$$Z(\theta) = Z_0 \cdot \left[ (\sin\theta + \csc\theta)^2 + (\cos\theta + \sec\theta)^2 - (\tan\theta + \cot\theta)^2 \right]$$

Calcule el valor constante del factor multiplicativo entre corchetes independiente de $\theta$.  
A) $3$  
B) $5$  
C) $7$  
D) $9$  
E) $11$  

32. En un sismógrafo digital en Arequipa, la señal de aceleración del suelo $a(t)$ en $\text{m/s}^2$ viene dada por:  

$$a(t) = 4\left(\frac{1 - \tan^2\theta}{1 + \tan^2\theta}\right)$$

Si se sabe que $\theta$ es tal que $\sin\theta = \frac{3}{5}$ con $\theta$ agudo, calcule el valor de la aceleración $a(t)$.  
A) $0.80\text{ m/s}^2$  
B) $1.12\text{ m/s}^2$  
C) $1.44\text{ m/s}^2$  
D) $1.76\text{ m/s}^2$  
E) $2.00\text{ m/s}^2$  

33. Un filtro digital de audio ecualiza una pista musical eliminando ruidos en frecuencias altas mediante el factor de atenuación:  

$$F(\theta) = \frac{\sin^3\theta + \cos^3\theta}{\sin\theta + \cos\theta} + \sin\theta\cos\theta$$

Demuestre el valor exacto de la atenuación $F(\theta)$ para cualquier fase $\theta$.  
A) $0.5$  
B) $1.0$  
C) $1.5$  
D) $2.0$  
E) Depende de $\theta$  

34. Una antena parabólica en un observatorio solar en Moquegua tiene un rendimiento de captación modelado por:  

$$\eta(\theta) = \eta_0 \cdot \left( \frac{\tan\theta + \sec\theta - 1}{\tan\theta - \sec\theta + 1} \right)$$

Simplifique la expresión entre paréntesis a una sola razón trigonométrica o suma elemental.  
A) $\sin\theta + \cos\theta$  
B) $\sec\theta + \tan\theta$  
C) $\csc\theta + \cot\theta$  
D) $\sec\theta - \tan\theta$  
E) $1$  

35. En una línea de alta tensión en el valle de Huallaga, el factor de potencia eléctrica está determinado por $\cos\phi$. Si mediciones con osciloscopio revelan que $\tan\phi + \cot\phi = \frac{25}{12}$, determine el valor del factor de potencia $\cos\phi$ si $\phi < 45^\circ$.  
A) $0.60$  
B) $0.75$  
C) $0.80$  
D) $0.85$  
E) $0.90$  

36. Un motor eléctrico trifásico en una mina de Huancavelica experimenta una corriente de fuga dada por $I = I_0(\sec^4\theta - \tan^4\theta)$. Si el sensor marca $\tan\theta = \frac{3}{4}$, calcule el factor $(\sec^4\theta - \tan^4\theta)$.  
A) $\frac{34}{16}$  
B) $\frac{37}{16}$  
C) $\frac{41}{16}$  
D) $\frac{43}{16}$  
E) $\frac{45}{16}$  

37. En un sistema de control de estabilidad para un vehículo autónomo en pendientes, se calcula el índice de tracción $T = \frac{1 + \sin\theta - \cos\theta}{1 + \sin\theta + \cos\theta}$. Demuestre a qué razón trigonométrica simple de $\frac{\theta}{2}$ o $\theta$ equivale exactamente dicha expresión.  
A) $\sin\theta$  
B) $\cos\theta$  
C) $\tan(\theta/2)$  
D) $\cot(\theta/2)$  
E) $\tan\theta$  

38. La potencia disipada en una resistencia de caldeo por efecto Joule es proporcional a:  

$$E = (\sin\theta + \cos\theta)^4 - (\sin\theta - \cos\theta)^4$$

Simplifique la expresión $E$ a su forma más compacta.  
A) $4\sin\theta\cos\theta$  
B) $8\sin\theta\cos\theta$  
C) $8\sin^2\theta\cos^2\theta$  
D) $4\sin^2\theta\cos^2\theta$  
E) $16\sin\theta\cos\theta$  

39. Si $\sec\theta + \tan\theta = 5$, determine el valor exacto de $\sin\theta$.  
A) $\frac{5}{13}$  
B) $\frac{12}{13}$  
C) $\frac{12}{5}$  
D) $\frac{5}{12}$  
E) $\frac{10}{13}$  

40. En un dron de rescate, la señal de telemetría procesa el cociente:  

$$Q = \frac{\cos^2\theta - \sin^2\theta}{\cot\theta - \tan\theta}$$

Simplifique la señal $Q$ en términos elementales de senos y cosenos.  
A) $\sin\theta\cos\theta$  
B) $\sin^2\theta$  
C) $\cos^2\theta$  
D) $1$  
E) $\tan\theta$  

41. Si se sabe que $\tan\theta + \cot\theta = m$, exprese $\sec^2\theta + \csc^2\theta$ exclusivamente en términos de $m$.  
A) $m$  
B) $m^2$  
C) $2m$  
D) $m^2 - 2$  
E) $m^2 + 2$  

42. Para un sistema óptico con lentes polarizadas en Lima, la intensidad lumínica transmitida es $I = I_0(1 - \sin^6\theta - \cos^6\theta)$. Si $\sin\theta\cos\theta = \frac{1}{3}$, determine la intensidad $I$ en función de $I_0$.  
A) $\frac{1}{3}I_0$  
B) $\frac{2}{3}I_0$  
C) $\frac{1}{2}I_0$  
D) $\frac{3}{4}I_0$  
E) $\frac{5}{6}I_0$  

43. Si $\sin\theta + \cos\theta = \sqrt{2}$, determine el valor del ángulo agudo $\theta$.  
A) $15^\circ$  
B) $30^\circ$  
C) $45^\circ$  
D) $60^\circ$  
E) $75^\circ$  

44. Simplifique la siguiente expresión trigonométrica: $Y = \frac{\sin^3\theta + \cos^3\theta}{1 - \sin\theta\cos\theta} + \frac{\sin^3\theta - \cos^3\theta}{1 + \sin\theta\cos\theta}$.  
A) $2\sin\theta$  
B) $2\cos\theta$  
C) $0$  
D) $2$  
E) $\sin\theta\cos\theta$  

45. En una red de sensores piezoeléctricos, la salida de voltaje viene dada por:  

$$V = V_0 \cdot \left[ \frac{\tan\theta}{1 - \cot\theta} + \frac{\cot\theta}{1 - \tan\theta} \right]$$

Reduzca el factor entre corchetes a una expresión equivalente con razones fundamentales.  
A) $1 + \tan\theta + \cot\theta$  
B) $1 + \sec\theta\csc\theta$  
C) $\sec\theta\csc\theta - 1$  
D) $\tan\theta - \cot\theta$  
E) $1 - \sec\theta\csc\theta$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | B | **31** | B |
| **2** | A | **17** | C | **32** | B |
| **3** | C | **18** | B | **33** | B |
| **4** | B | **19** | A | **34** | B |
| **5** | B | **20** | B | **35** | C |
| **6** | C | **21** | B | **36** | A |
| **7** | A | **22** | B | **37** | C |
| **8** | C | **23** | C | **38** | B |
| **9** | B | **24** | A | **39** | B |
| **10** | B | **25** | C | **40** | A |
| **11** | B | **26** | B | **41** | B |
| **12** | C | **27** | A | **42** | A |
| **13** | A | **28** | B | **43** | C |
| **14** | C | **29** | B | **44** | A |
| **15** | C | **30** | B | **45** | B |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde identidades pitagóricas o intenta simplificar cancelando términos en sumas. | Repasar el paso de toda expresión a senos y cosenos y memorizar $\sin^2\theta + \cos^2\theta = 1$. |
| **En Proceso (60% - 80% aciertos)** | Domina las identidades fundamentales, pero demora en simplificaciones con potencias altas o conjugados. | Practicar el uso sistemático de las identidades auxiliares del §2.3 resolviendo los ejercicios 16 al 30. |
| **Avanzado (> 80% aciertos)** | Resuelve problemas algebraicos complejos, desfasajes y simplificaciones avanzadas con agilidad. | Resolver los problemas 31 al 45 con cronómetro estricto (1.5 minutos por ítem). |

### Preguntas Guía para la Reflexión:
1. *¿Por qué la relación $(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = 1$ es tan útil para resolver ecuaciones no lineales en trigonometría?*
2. *¿Cómo se deduce la identidad auxiliar $\tan\theta + \cot\theta = \sec\theta\csc\theta$ utilizando únicamente razones por cociente?*
3. *¿Por qué en ingeniería de señales el paso a senos y cosenos es el estándar universal antes de aplicar filtros analógicos o digitales?*

---

## 7. Formulario Resumen

| Identidad Trigonométrica | Tipo de Identidad | Expresión Matemática Rigurosa |
| :--- | :--- | :--- |
| **Pitagórica Principal** | Seno y Coseno | $\sin^2\theta + \cos^2\theta = 1$ |
| **Pitagórica Tangente** | Tangente y Secante | $1 + \tan^2\theta = \sec^2\theta \implies \sec^2\theta - \tan^2\theta = 1$ |
| **Pitagórica Cotangente** | Cotangente y Cosecante | $1 + \cot^2\theta = \csc^2\theta \implies \csc^2\theta - \cot^2\theta = 1$ |
| **Inversas de Secante y Tangente** | Diferencia de cuadrados | $\sec\theta + \tan\theta = \frac{1}{\sec\theta - \tan\theta}$ |
| **Inversas de Csc y Cot** | Diferencia de cuadrados | $\csc\theta + \cot\theta = \frac{1}{\csc\theta - \cot\theta}$ |
| **Por Cociente Tangente** | Expresada en senos y cosenos | $\tan\theta = \frac{\sin\theta}{\cos\theta}$ |
| **Por Cociente Cotangente** | Expresada en senos y cosenos | $\cot\theta = \frac{\cos\theta}{\sin\theta}$ |
| **Recíprocas** | Producto igual a 1 | $\sin\theta\csc\theta = 1,\ \cos\theta\sec\theta = 1,\ \tan\theta\cot\theta = 1$ |
| **Auxiliar Suma Tan + Cot** | Producto de secante y cosecante | $\tan\theta + \cot\theta = \sec\theta\csc\theta$ |
| **Auxiliar Suma de Cuadrados** | Secante y cosecante | $\sec^2\theta + \csc^2\theta = \sec^2\theta\csc^2\theta$ |
| **Cuartas Potencias** | Binomio al cuadrado derivado | $\sin^4\theta + \cos^4\theta = 1 - 2\sin^2\theta\cos^2\theta$ |
| **Sextas Potencias** | Binomio al cubo derivado | $\sin^6\theta + \cos^6\theta = 1 - 3\sin^2\theta\cos^2\theta$ |
| **Trinomio al Cuadrado** | Simplificación con signos | $(1 \pm \sin\theta \pm \cos\theta)^2 = 2(1 \pm \sin\theta)(1 \pm \cos\theta)$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 2 clave(s) corregida(s) y 4 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **28** | B | B | Corregida | Se precisó que $\theta$ está en el primer cuadrante, lo que elimina la segunda solución $\frac{1}{2x}$ (D). Respuesta: $2x$ (B). |
| **31** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **36** | C | A | Corregida | Se ajustó la opción A: $\sec^4\theta-\tan^4\theta=1+2\tan^2\theta=1+\frac{18}{16}=\frac{34}{16}$. |
| **39** | B | B | Corregida | Las opciones C ($\frac{24}{26}$) y D repetían el valor de B; se reemplazaron por distractores. De $\sec\theta+\tan\theta=5$ resulta $\cos\theta=\frac{5}{13}$ y $\sin\theta=\frac{12}{13}$. Clave B. |

**Claves sin cambios:** 43 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
