# Tema 06: Cuerpos de Revolución (Cilindro, Esfera y Cono)

## 1. Motivación y Contexto Real

Los cuerpos de revolución son sólidos geométricos tridimensionales engendrados por la rotación de una figura plana alrededor de un eje fijo. En la ingeniería de procesos, almacenamiento de fluidos e infraestructura civil peruana, estos cuerpos son indispensables debido a su máxima eficiencia volumétrica: minimizan la cantidad de material de chapa de acero o concreto necesario para contener un determinado volumen y disipan de manera óptima las presiones internas hidrostáticas o neumáticas.

En las aplicaciones prioritarias evaluadas en Beca 18:
1. **Reservorios Cilíndricos de Agua Potable:** Comunidades rurales y programas como *Sierra y Selva Exportadora* instalan tanques cilíndricos de ferrocemento o polietileno (rotoplas) para abastecer de agua potable a la población calculando su capacidad en litros ($1\text{ m}^3 = 1\,000\text{ L}$).
2. **Tolvas Cónicas en Minería y Agricultura:** Las tolvas de descarga para granos de quinua, maíz y concentrados de mineral tienen fondo cónico invertido para permitir que los sólidos fluyan uniformemente por gravedad sin acumular sedimentos en esquinas.
3. **Balones Esféricos de Gas (GLP y GNV):** En plantas de almacenamiento de hidrocarburos (como Melchorita en Cañete o Pisco), los tanques esféricos ("esferas de Hortonsphere") son los únicos capaces de resistir altísimas presiones internas homogéneas con el menor espesor de pared metálica.

```{figure} ../../assets/geometria/cuerpos_revolucion_3d.svg
---
width: 95%
align: center
alt: Cuerpos de Revolución - Cilindro, Cono y Esfera
---
*Diagrama tridimensional vectorial generado en TikZ con el Cilindro Recto, Cono Recto y Esfera, ilustrando sus generatrices, alturas, radios y compendio de fórmulas de volumen y capacidad en litros.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 El Cilindro Circular Recto (Cilindro de Revolución)

Se engendra al girar una región rectangular una vuelta completa ($360^\circ$) alrededor de uno de sus lados, que actúa como eje de rotación.
* **Bases:** Dos círculos congruentes y paralelos de radio $r$.
* **Altura ($h$):** Distancia perpendicular entre las bases. Coincide con la generatriz ($g = h$).
* **Radio ($r$):** Radio de las bases circulares.

#### Fórmulas Fundamentales del Cilindro:
1. **Área Lateral ($A_L$):** Corresponde al desarrollo plano del cilindro, el cual es un rectángulo de base $2\pi r$ (longitud de la circunferencia) y altura $h$:

$$A_L = 2\pi r h$$

2. **Área Total ($A_T$):** Suma del área lateral más el área de las dos bases circulares ($2 \cdot \pi r^2$):

$$A_T = A_L + 2A_{\text{base}} = 2\pi r h + 2\pi r^2 = 2\pi r(h + r)$$

3. **Volumen ($V$):** Producto del área de la base por la altura:

$$V = \pi r^2 h$$

---

### 2.2 El Cono Circular Recto (Cono de Revolución)

Se engendra al girar una región triangular rectangular una vuelta completa ($360^\circ$) alrededor de uno de sus catetos.
* **Base:** Un círculo de radio $r$.
* **Vértice o Cúspide ($V$):** Punto superior donde concurren las generatrices.
* **Altura ($h$):** Segmento perpendicular trazado desde el vértice hacia el centro de la base circular.
* **Generatriz ($g$):** Segmento que une el vértice con cualquier punto de la circunferencia de la base. Cumple el Teorema de Pitágoras con el radio y la altura:

$$g^2 = r^2 + h^2 \implies g = \sqrt{r^2 + h^2}$$

#### Fórmulas Fundamentales del Cono:
1. **Área Lateral ($A_L$):** El desarrollo plano de la superficie lateral es un sector circular de radio $g$ y longitud de arco $2\pi r$:

$$A_L = \pi r g$$

2. **Área Total ($A_T$):** Suma del área lateral y el área de la base:

$$A_T = A_L + A_{\text{base}} = \pi r g + \pi r^2 = \pi r(g + r)$$

3. **Volumen ($V$):** Equivale exactamente a la tercera parte del volumen de un cilindro de igual radio y altura:

$$V = \frac{1}{3}\pi r^2 h$$

4. **Ángulo de Desarrollo del Sector Lateral ($\theta$):**

$$\theta = \frac{r}{g} \cdot 360^\circ$$

---

### 2.3 La Esfera y Superficie Esférica

Se engendra al girar una región semicircular una vuelta completa ($360^\circ$) alrededor de su diámetro.
* **Centro ($O$):** Punto equidistante de todos los puntos de la superficie esférica.
* **Radio ($r$):** Segmento que une el centro con cualquier punto de la superficie esférica.
* **Círculo Máximo:** Sección plana obtenida al cortar la esfera por un plano que pasa por su centro (radio $r$, área $\pi r^2$).

#### Fórmulas Fundamentales de la Esfera:
1. **Área de la Superficie Esférica ($A_S$):** Es exactamente cuatro veces el área de su círculo máximo (demostrado por Arquímedes):

$$A_S = 4\pi r^2$$

2. **Volumen de la Esfera ($V$):**

$$V = \frac{4}{3}\pi r^3$$

3. **Semiesfera o Hemisferio:**
   * Volumen: $V_{\text{hem}} = \frac{2}{3}\pi r^3$
   * Área de la superficie curva: $A_{\text{curva}} = 2\pi r^2$
   * Área total (incluyendo la base circular plana): $A_{\text{total}} = 2\pi r^2 + \pi r^2 = 3\pi r^2$

---

### 2.4 Equivalencias de Capacidad y Densidad (Enfoque Beca 18)

En los problemas de contexto real de Beca 18, el volumen geométrico (en metros cúbicos o centímetros cúbicos) debe transformarse en **capacidad hídrica** o **masa**:

| Unidad de Volumen | Unidad de Capacidad | Masa de Agua Pura ($4^\circ\text{C}$) |
| :--- | :--- | :--- |
| **$1\text{ m}^3$** | **$1\,000\text{ litros}$ ($1\text{ kL}$)** | **$1\,000\text{ kg} = 1\text{ tonelada}$** |
| **$1\text{ dm}^3$** | **$1\text{ litro}$** | **$1\text{ kg}$** |
| **$1\text{ cm}^3$** | **$1\text{ mililitro}$ ($1\text{ mL}$)** | **$1\text{ gramo}$** |

$$\text{Capacidad (litros)} = V (\text{m}^3) \times 1\,000$$

---

### 2.5 Relación Histórica de Arquímedes (Cilindro, Semiesfera y Cono)

Arquímedes demostró que si se inscribe una esfera dentro de un cilindro equilátero ($h = 2r$):
1. El área de la esfera es igual al área lateral del cilindro: $A_S = A_{L,\text{cilindro}} = 4\pi r^2$.
2. El volumen de la esfera es exactamente $\frac{2}{3}$ del volumen del cilindro circunscrito:

$$V_{\text{esfera}} = \frac{2}{3} V_{\text{cilindro}} \quad \left(V_{\text{cilindro}} = \pi r^2(2r) = 2\pi r^3 \implies \frac{2}{3}(2\pi r^3) = \frac{4}{3}\pi r^3\right)$$

3. La proporción entre los volúmenes de un cono, una semiesfera y un cilindro de igual radio $r$ y altura $h = r$ es exactamente:

$$V_{\text{cono}} : V_{\text{semiesfera}} : V_{\text{cilindro}} = 1 : 2 : 3$$

---

### 2.6 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Confundir la Generatriz ($g$) con la Altura ($h$) en el Cono:**
>    * La *altura ($h$)* se usa para el **volumen**: $V = \frac{1}{3}\pi r^2 h$.
>    * La *generatriz ($g$)* se usa para el **área lateral**: $A_L = \pi r g$.
>    * Jamás use la generatriz en la fórmula del volumen ni la altura en el área lateral sin previa conversión pitagórica ($g = \sqrt{r^2 + h^2}$).
> 2. **Olvidar la base al calcular el área total del hemisferio:** El área total de una semiesfera cerrada es $3\pi r^2$ ($2\pi r^2$ de la cúpula curva $+ \pi r^2$ de la tapa circular plana). Si el recipiente está abierto por arriba, solo se considera $2\pi r^2$.
> 3. **Error en conversión de unidades volumétricas:**
>    * $1\text{ m}^3 \ne 100\text{ litros}$; la equivalencia correcta es $1\text{ m}^3 = 1\,000\text{ litros}$.
>    * $1\text{ m}^3 = 1\,000\,000\text{ cm}^3 = 10^6\text{ cm}^3$.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Fórmulas y Volúmenes)

#### Ejercicio 1
Un tanque cilíndrico de almacenamiento de agua tiene un radio basal de $3\text{ m}$ y una altura de $7\text{ m}$. Calcule su volumen en metros cúbicos y su capacidad total en litros. ($\text{use } \pi \approx \frac{22}{7}$).

**Análisis Conceptual:**
El volumen de un cilindro es $V = \pi r^2 h$. La capacidad en litros se obtiene multiplicando los metros cúbicos por $1\,000$.

**Solución Paso a Paso:**

**Paso 1:** Aplicar la fórmula del volumen del cilindro:

$$V = \pi r^2 h$$

**Paso 2:** Reemplazar los valores $r = 3\text{ m}$, $h = 7\text{ m}$ y $\pi \approx \frac{22}{7}$:

$$V = \left(\frac{22}{7}\right) \cdot (3^2) \cdot 7 = 22 \cdot 9 = 198\text{ m}^3$$

**Paso 3:** Convertir el volumen a litros:

$$\text{Capacidad} = 198\text{ m}^3 \times 1\,000\frac{\text{L}}{\text{m}^3} = 198\,000\text{ litros}$$

**Conclusión:**
El volumen es $198\text{ m}^3$ y su capacidad total es de $198\,000\text{ litros}$.

---

#### Ejercicio 2
Un cono circular recto tiene un radio de base de $6\text{ cm}$ y una generatriz de $10\text{ cm}$. Calcule su altura, su área lateral y su volumen.

**Análisis Conceptual:**
El radio $r$, la altura $h$ y la generatriz $g$ forman un triángulo rectángulo con hipotenusa $g$. Se halla $h$ por Pitágoras y luego se aplican las fórmulas de área lateral y volumen.

**Solución Paso a Paso:**

**Paso 1:** Calcular la altura $h$ por Pitágoras:

$$h = \sqrt{g^2 - r^2} = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8\text{ cm}$$

**Paso 2:** Calcular el área lateral $A_L$:

$$A_L = \pi r g = \pi(6)(10) = 60\pi\text{ cm}^2$$

**Paso 3:** Calcular el volumen $V$:

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(6^2)(8) = \frac{1}{3}\pi(36)(8) = 12 \cdot 8 \cdot \pi = 96\pi\text{ cm}^3$$

**Conclusión:**
La altura mide $8\text{ cm}$, el área lateral es $60\pi\text{ cm}^2$ y el volumen es $96\pi\text{ cm}^3$.

---

#### Ejercicio 3
Una esfera de jebe tiene un radio de $6\text{ cm}$. Calcule el área de su superficie esférica y su volumen en función de $\pi$.

**Análisis Conceptual:**
Se aplican directamente las fórmulas de la esfera: $A_S = 4\pi r^2$ y $V = \frac{4}{3}\pi r^3$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el área de la superficie esférica:

$$A_S = 4\pi r^2 = 4\pi(6^2) = 4\pi(36) = 144\pi\text{ cm}^2$$

**Paso 2:** Calcular el volumen de la esfera:

$$V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi(6^3) = \frac{4}{3}\pi(216) = 4 \cdot 72 \cdot \pi = 288\pi\text{ cm}^3$$

**Conclusión:**
El área de la superficie esférica es $144\pi\text{ cm}^2$ y su volumen es $288\pi\text{ cm}^3$.

---

### Nivel 2: Intermedio (Razonamiento y Cuerpos Compuestos)

#### Ejercicio 4
El desarrollo de la superficie lateral de un cilindro circular recto es una región cuadrada cuyo lado mide $12\pi\text{ cm}$. Calcule el volumen del cilindro.

**Análisis Conceptual:**
En el desarrollo lateral, la base del rectángulo/cuadrado es la longitud de la circunferencia de la base ($2\pi r$) y la altura es la altura del cilindro ($h$). Como es un cuadrado, $2\pi r = 12\pi$ y $h = 12\pi$.

**Solución Paso a Paso:**

**Paso 1:** Despejar el radio $r$:

$$2\pi r = 12\pi \implies r = \frac{12\pi}{2\pi} = 6\text{ cm}$$

**Paso 2:** Identificar la altura $h$:

$$h = 12\pi\text{ cm}$$

**Paso 3:** Calcular el volumen del cilindro:

$$V = \pi r^2 h = \pi(6^2)(12\pi) = \pi(36)(12\pi) = 432\pi^2\text{ cm}^3$$

**Conclusión:**
El volumen del cilindro es $432\pi^2\text{ cm}^3$.

---

#### Ejercicio 5
Un depósito cilíndrico de radio $r = 10\text{ cm}$ contiene agua hasta cierta altura. Se introduce completamente dentro del depósito una bola esférica de metal de radio $R = 6\text{ cm}$. Calcule cuántos centímetros se eleva el nivel del agua en el depósito cilíndrico.

**Análisis Conceptual:**
Por el Principio de Arquímedes, el volumen de agua desplazado en el cilindro es exactamente igual al volumen de la esfera sumergida: $V_{\text{cilindro desplazado}} = V_{\text{esfera}}$.
El volumen desplazado en el cilindro es $\pi r^2 \Delta h$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el volumen de la esfera sumergida:

$$V_{\text{esfera}} = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi(6^3) = \frac{4}{3}\pi(216) = 288\pi\text{ cm}^3$$

**Paso 2:** Igualar con el volumen desplazado en el cilindro de radio $r = 10\text{ cm}$:

$$V_{\text{desplazado}} = \pi r^2 \cdot \Delta h$$

$$288\pi = \pi(10^2) \cdot \Delta h$$

$$288\pi = 100\pi \cdot \Delta h$$

**Paso 3:** Despejar el incremento de altura $\Delta h$:

$$\Delta h = \frac{288}{100} = 2.88\text{ cm}$$

**Conclusión:**
El nivel del agua en el cilindro se eleva $2.88\text{ cm}$.

---

#### Ejercicio 6
El área total de un cono circular recto es de $96\pi\text{ cm}^2$ y su generatriz mide $10\text{ cm}$. Calcule el volumen de dicho cono.

**Análisis Conceptual:**
El área total es $A_T = \pi r(g + r)$. Con $A_T = 96\pi$ y $g = 10$, formamos una ecuación cuadrática en $r$. Luego calculamos la altura $h$ por Pitágoras y finalmente el volumen.

**Solución Paso a Paso:**

**Paso 1:** Plantear la ecuación con el área total:

$$\pi r(10 + r) = 96\pi \implies r(10 + r) = 96$$

$$r^2 + 10r - 96 = 0$$

**Paso 2:** Factorizar por aspa simple:

$$(r + 16)(r - 6) = 0$$

Como el radio debe ser positivo: $r = 6\text{ cm}$.

**Paso 3:** Calcular la altura $h$ por Pitágoras:

$$h = \sqrt{g^2 - r^2} = \sqrt{10^2 - 6^2} = \sqrt{64} = 8\text{ cm}$$

**Paso 4:** Calcular el volumen:

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(6^2)(8) = \frac{1}{3}\pi(36)(8) = 96\pi\text{ cm}^3$$

**Conclusión:**
El volumen del cono es $96\pi\text{ cm}^3$.

---

#### Ejercicio 7
Se funde una esfera sólida de plomo de radio $R = 9\text{ cm}$ para fabricar cilindros pequeños idénticos de radio $r = 3\text{ cm}$ y altura $h = 4\text{ cm}$. Suponiendo que no hay pérdida de material, ¿cuántos cilindros completos se obtendrán?

**Análisis Conceptual:**
La cantidad de cilindros $N$ es el cociente entre el volumen de la esfera de plomo y el volumen de un cilindro individual: $N = \frac{V_{\text{esfera}}}{V_{\text{cilindro}}}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el volumen de la esfera:

$$V_{\text{esfera}} = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi(9^3) = \frac{4}{3}\pi(729) = 4(243)\pi = 972\pi\text{ cm}^3$$

**Paso 2:** Calcular el volumen de un cilindro:

$$V_{\text{cilindro}} = \pi r^2 h = \pi(3^2)(4) = 36\pi\text{ cm}^3$$

**Paso 3:** Calcular el número de cilindros $N$:

$$N = \frac{972\pi}{36\pi} = 27$$

**Conclusión:**
Se obtendrán exactamente $27$ cilindros completos de plomo.

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Silo Mixto para Granos de Maíz en el Valle del Mantaro)
Una cooperativa agraria en Jauja construye un silo de almacenamiento para granos secos compuesto por un cuerpo cilíndrico superior de $4\text{ m}$ de diámetro y $6\text{ m}$ de altura, rematado en su parte inferior por una tolva cónica de igual diámetro y $3\text{ m}$ de profundidad para descarga por gravedad. Si la densidad a granel del maíz seco es de $750\text{ kg/m}^3$, determine el volumen total del silo y la cantidad máxima de toneladas de maíz que puede almacenar. ($\text{use } \pi \approx 3.1416$).

**Análisis Conceptual:**
El radio común es $r = \frac{D}{2} = 2\text{ m}$. El volumen total es la suma del volumen del cilindro y del cono: $V_{\text{total}} = V_{\text{cilindro}} + V_{\text{cono}} = \pi r^2 h_{\text{cil}} + \frac{1}{3}\pi r^2 h_{\text{cono}}$. La masa se halla multiplicando por la densidad.

**Solución Paso a Paso:**

**Paso 1:** Calcular el volumen del cuerpo cilíndrico:

$$V_{\text{cilindro}} = \pi(2^2)(6) = 24\pi\text{ m}^3$$

**Paso 2:** Calcular el volumen de la tolva cónica inferior:

$$V_{\text{cono}} = \frac{1}{3}\pi(2^2)(3) = \frac{1}{3}\pi(4)(3) = 4\pi\text{ m}^3$$

**Paso 3:** Calcular el volumen total del silo:

$$V_{\text{total}} = 24\pi + 4\pi = 28\pi\text{ m}^3 \approx 28(3.1416) \approx 87.96\text{ m}^3$$

**Paso 4:** Calcular la capacidad de almacenamiento en toneladas de maíz:

$$\text{Masa} = V_{\text{total}} \times 750\frac{\text{kg}}{\text{m}^3} = 87.9648 \times 750 \approx 65\,973.6\text{ kg} \approx 65.97\text{ toneladas}$$

**Conclusión:**
El volumen total del silo es $28\pi\text{ m}^3 \approx 87.96\text{ m}^3$ y puede almacenar un máximo de aproximadamente $66$ toneladas de maíz.

---

#### Ejercicio 9 (Tanque Esférico de Gas Licuado de Petróleo en Pisco)
En la planta fraccionadora de gas en Pisco, se instala un tanque esférico de acero para gas licuado de petróleo (GLP) de $12\text{ m}$ de diámetro exterior. Para prevenir la corrosión salina marina, se debe aplicar una capa de pintura epóxica anticorrosiva en toda la superficie exterior. Si un galón de pintura epóxica rinde $30\text{ m}^2$ y cuesta $S/\, 120$, determine el área exterior a pintar y el costo total de la pintura necesaria. ($\text{use } \pi \approx 3.1416$).

**Análisis Conceptual:**
El radio es $r = \frac{D}{2} = 6\text{ m}$. El área superficial de la esfera es $A_S = 4\pi r^2$. El número de galones requeridos es $\lceil A_S / 30 \rceil$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el área de la superficie esférica:

$$A_S = 4\pi r^2 = 4\pi(6^2) = 4\pi(36) = 144\pi\text{ m}^2$$

$$A_S \approx 144(3.1416) \approx 452.39\text{ m}^2$$

**Paso 2:** Calcular el número de galones necesarios:

$$N_{\text{galones}} = \frac{452.39}{30} \approx 15.08\text{ galones}$$

En la práctica comercial se deben comprar $16$ galones enteros para garantizar la cobertura total.

**Paso 3:** Calcular el presupuesto total:

$$\text{Costo} = 16 \times S/\, 120 = S/\, 1\,920$$

**Conclusión:**
El área de la superficie esférica a pintar es de $452.39\text{ m}^2$ y se requiere una inversión de $S/\, 1\,920$ en pintura epóxica.

---

#### Ejercicio 10 (Abastecimiento de Agua en Cisterna Cilíndrica para Comunidad en Loreto)
En una comunidad ribereña del río Ucayali en Loreto, se instala un reservorio comunal cilíndrico elevado con diámetro interior de $3\text{ m}$ y altura de $4\text{ m}$. Una electrobomba llena el reservorio bombeando agua a un caudal constante de $150\text{ litros por minuto}$. Si la comunidad consume diariamente $15\,000\text{ litros}$ de agua potable, calcule el tiempo exacto en horas y minutos que demora la electrobomba en llenar el reservorio completamente desde vacío y para cuántos días completos de consumo alcanza un reservorio lleno. ($\text{use } \pi \approx 3.1416$).

**Análisis Conceptual:**
El radio es $r = 1.5\text{ m}$ y $h = 4\text{ m}$. El volumen en metros cúbicos se convierte a litros ($1\text{ m}^3 = 1\,000\text{ L}$). El tiempo de llenado es $\text{Volumen} / \text{Caudal}$.

**Solución Paso a Paso:**

**Paso 1:** Calcular el volumen del reservorio:

$$V = \pi r^2 h = \pi(1.5^2)(4) = \pi(2.25)(4) = 9\pi\text{ m}^3$$

$$V \approx 9(3.1416) = 28.2744\text{ m}^3$$

**Paso 2:** Convertir el volumen a litros:

$$\text{Capacidad} = 28.2744 \times 1\,000 = 28\,274.4\text{ litros}$$

**Paso 3:** Calcular el tiempo de llenado con caudal de $150\text{ L/min}$:

$$t = \frac{28\,274.4\text{ L}}{150\text{ L/min}} \approx 188.5\text{ minutos}$$

$$188.5\text{ min} = 3\text{ horas y } 8.5\text{ minutos} \approx 3\text{ h } 8\text{ min } 30\text{ s}$$

**Paso 4:** Calcular los días de autonomía de la comunidad:

$$\text{Días} = \frac{28\,274.4\text{ L}}{15\,000\text{ L/día}} \approx 1.88\text{ días}$$

Alcanza para $1$ día completo y el $88\%$ del segundo día.

**Conclusión:**
La electrobomba demora aproximadamente $3\text{ horas y } 8.5\text{ minutos}$ en llenar el reservorio, el cual almacena $28\,274\text{ litros}$ y abastece a la comunidad durante casi $2$ días completos.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. Un cilindro recto tiene radio de base $4\text{ cm}$ y altura $10\text{ cm}$. Calcule su volumen.  
A) $120\pi\text{ cm}^3$  
B) $140\pi\text{ cm}^3$  
C) $160\pi\text{ cm}^3$  
D) $180\pi\text{ cm}^3$  
E) $200\pi\text{ cm}^3$  

2. Un cono circular recto tiene radio $3\text{ cm}$ y altura $4\text{ cm}$. Calcule la longitud de su generatriz.  
A) $5\text{ cm}$  
B) $6\text{ cm}$  
C) $7\text{ cm}$  
D) $8\text{ cm}$  
E) $9\text{ cm}$  

3. Calcule el volumen de una esfera cuyo radio mide $3\text{ cm}$.  
A) $27\pi\text{ cm}^3$  
B) $36\pi\text{ cm}^3$  
C) $48\pi\text{ cm}^3$  
D) $54\pi\text{ cm}^3$  
E) $72\pi\text{ cm}^3$  

4. ¿Cuántos litros de agua caben exactamente en un volumen de $4.5\text{ m}^3$?  
A) $450\text{ L}$  
B) $4\,500\text{ L}$  
C) $45\,000\text{ L}$  
D) $450\,000\text{ L}$  
E) $45\text{ L}$  

5. El área lateral de un cilindro recto de radio $5\text{ cm}$ y altura $8\text{ cm}$ es:  
A) $40\pi\text{ cm}^2$  
B) $60\pi\text{ cm}^2$  
C) $80\pi\text{ cm}^2$  
D) $100\pi\text{ cm}^2$  
E) $120\pi\text{ cm}^2$  

6. Calcule el volumen de un cono de radio $6\text{ cm}$ y altura $10\text{ cm}$.  
A) $100\pi\text{ cm}^3$  
B) $120\pi\text{ cm}^3$  
C) $150\pi\text{ cm}^3$  
D) $180\pi\text{ cm}^3$  
E) $240\pi\text{ cm}^3$  

7. El área de la superficie de una esfera de radio $5\text{ cm}$ es:  
A) $50\pi\text{ cm}^2$  
B) $75\pi\text{ cm}^2$  
C) $100\pi\text{ cm}^2$  
D) $125\pi\text{ cm}^2$  
E) $150\pi\text{ cm}^2$  

8. Si se duplica la altura de un cilindro manteniendo constante su radio, su volumen:  
A) Se mantiene igual  
B) Se duplica  
C) Se cuadruplica  
D) Se reduce a la mitad  
E) Se multiplica por $8$  

9. La generatriz de un cono circular recto mide $13\text{ cm}$ y el radio de la base mide $5\text{ cm}$. ¿Cuánto mide su altura?  
A) $10\text{ cm}$  
B) $11\text{ cm}$  
C) $12\text{ cm}$  
D) $12.5\text{ cm}$  
E) $13\text{ cm}$  

10. El área lateral de un cono de radio $4\text{ cm}$ y generatriz $9\text{ cm}$ es:  
A) $18\pi\text{ cm}^2$  
B) $24\pi\text{ cm}^2$  
C) $36\pi\text{ cm}^2$  
D) $48\pi\text{ cm}^2$  
E) $72\pi\text{ cm}^2$  

11. ¿Cuál es el volumen de un cilindro equilátero (donde la altura es igual al diámetro de la base, $h = 2r$) de radio $r = 2\text{ cm}$?  
A) $8\pi\text{ cm}^3$  
B) $12\pi\text{ cm}^3$  
C) $16\pi\text{ cm}^3$  
D) $24\pi\text{ cm}^3$  
E) $32\pi\text{ cm}^3$  

12. Un recipiente contiene $2\,500\text{ mL}$ de líquido. ¿A cuántos centímetros cúbicos equivale?  
A) $2.5\text{ cm}^3$  
B) $25\text{ cm}^3$  
C) $250\text{ cm}^3$  
D) $2\,500\text{ cm}^3$  
E) $25\,000\text{ cm}^3$  

13. El área total de un cilindro recto de radio $2\text{ cm}$ y altura $5\text{ cm}$ es:  
A) $14\pi\text{ cm}^2$  
B) $20\pi\text{ cm}^2$  
C) $24\pi\text{ cm}^2$  
D) $28\pi\text{ cm}^2$  
E) $32\pi\text{ cm}^2$  

14. Si el diámetro de una esfera es de $12\text{ cm}$, ¿cuál es su radio?  
A) $3\text{ cm}$  
B) $4\text{ cm}$  
C) $6\text{ cm}$  
D) $8\text{ cm}$  
E) $12\text{ cm}$  

15. El volumen de un cono es de $45\pi\text{ cm}^3$. Si su altura es de $15\text{ cm}$, ¿cuánto mide el radio de su base?  
A) $2\text{ cm}$  
B) $3\text{ cm}$  
C) $4\text{ cm}$  
D) $5\text{ cm}$  
E) $6\text{ cm}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. Si se duplica el radio de la base de un cilindro manteniendo constante su altura, ¿en qué factor se incrementa su volumen?  
A) Se duplica (factor $2$)  
B) Se triplica (factor $3$)  
C) Se cuadruplica (factor $4$)  
D) Se multiplica por $8$  
E) No varía  

17. En un cono equilátero, la generatriz es igual al diámetro de la base ($g = 2r$). Si el radio de la base mide $3\text{ cm}$, calcule el área total del cono.  
A) $18\pi\text{ cm}^2$  
B) $21\pi\text{ cm}^2$  
C) $24\pi\text{ cm}^2$  
D) $27\pi\text{ cm}^2$  
E) $36\pi\text{ cm}^2$  

18. Dos esferas de plomo de radios $3\text{ cm}$ y $4\text{ cm}$ y una tercera esfera se funden para formar una sola esfera de radio $6\text{ cm}$. Calcule el radio de la tercera esfera.  
A) $4.5\text{ cm}$  
B) $5\text{ cm}$  
C) $5.2\text{ cm}$  
D) $5.5\text{ cm}$  
E) $\sqrt[3]{100}\text{ cm}$  

19. Un cono y un cilindro tienen la misma base circular de radio $r$ y el mismo volumen. Si la altura del cilindro es de $6\text{ cm}$, ¿cuál es la altura del cono?  
A) $2\text{ cm}$  
B) $6\text{ cm}$  
C) $12\text{ cm}$  
D) $18\text{ cm}$  
E) $24\text{ cm}$  

20. El área total de una semiesfera sólida (incluyendo su base circular plana) es de $108\pi\text{ cm}^2$. Calcule el volumen de dicha semiesfera.  
A) $120\pi\text{ cm}^3$  
B) $144\pi\text{ cm}^3$  
C) $160\pi\text{ cm}^3$  
D) $180\pi\text{ cm}^3$  
E) $216\pi\text{ cm}^3$  

21. El desarrollo lateral de un cono circular recto es un semicírculo de radio $10\text{ cm}$. Calcule el radio de la base del cono.  
A) $2.5\text{ cm}$  
B) $4\text{ cm}$  
C) $5\text{ cm}$  
D) $6\text{ cm}$  
E) $7.5\text{ cm}$  

22. En un cilindro de revolución, el área lateral es igual al área de una de sus bases. ¿Qué relación guardan la altura $h$ y el radio $r$?  
A) $h = r$  
B) $h = \frac{r}{2}$  
C) $h = 2r$  
D) $h = \frac{r}{4}$  
E) $h = 4r$  

23. Un pozo cilíndrico de $2\text{ m}$ de diámetro y $10\text{ m}$ de profundidad se encuentra lleno de agua hasta el $70\%$ de su capacidad. ¿Cuántos litros de agua contiene? ($\text{use } \pi \approx 3.14$).  
A) $19\,856\text{ L}$  
B) $21\,980\text{ L}$  
C) $24\,560\text{ L}$  
D) $27\,400\text{ L}$  
E) $31\,400\text{ L}$  

24. Una esfera se encuentra inscrita en un cubo de arista $10\text{ cm}$. Calcule el volumen de la región interior al cubo que queda fuera de la esfera.  
A) $1000 - \frac{500\pi}{3}\text{ cm}^3$  
B) $1000 - \frac{250\pi}{3}\text{ cm}^3$  
C) $500 - \frac{100\pi}{3}\text{ cm}^3$  
D) $1000 - 500\pi\text{ cm}^3$  
E) $1000 - 250\pi\text{ cm}^3$  

25. Un cono recto tiene generatriz $g = 15\text{ cm}$ y el ángulo que forma la generatriz con el plano de la base es de $53^\circ$. Calcule el volumen aproximado del cono.  
A) $324\pi\text{ cm}^3$  
B) $360\pi\text{ cm}^3$  
C) $405\pi\text{ cm}^3$  
D) $480\pi\text{ cm}^3$  
E) $540\pi\text{ cm}^3$  

26. Se vierte agua dentro de un vaso cónico invertido de $12\text{ cm}$ de altura y $8\text{ cm}$ de radio superior hasta la mitad de su altura ($6\text{ cm}$). ¿Qué fracción del volumen total del vaso está ocupada por el agua?  
A) $\frac{1}{2}$  
B) $\frac{1}{4}$  
C) $\frac{1}{6}$  
D) $\frac{1}{8}$  
E) $\frac{1}{16}$  

27. En un cilindro de revolución, la diagonal de la sección axial mide $10\text{ cm}$ y forma un ángulo de $37^\circ$ con la base. Calcule el volumen del cilindro.  
A) $48\pi\text{ cm}^3$  
B) $64\pi\text{ cm}^3$  
C) $72\pi\text{ cm}^3$  
D) $96\pi\text{ cm}^3$  
E) $108\pi\text{ cm}^3$  

28. Si el área de una esfera aumenta en un $44\%$, ¿en qué porcentaje aumenta su radio?  
A) $10\%$  
B) $20\%$  
C) $22\%$  
D) $44\%$  
E) $72.8\%$  

29. Calcule la razón entre el volumen de una esfera y el volumen de un cono recto que tiene igual radio y cuya altura es igual al diámetro de la esfera.  
A) $1 : 1$  
B) $2 : 1$  
C) $3 : 2$  
D) $4 : 3$  
E) $3 : 1$  

30. Un tronco de cono circular recto tiene radios de base de $3\text{ cm}$ y $6\text{ cm}$, y una altura de $4\text{ cm}$. Calcule el volumen del tronco de cono.  
A) $68\pi\text{ cm}^3$  
B) $76\pi\text{ cm}^3$  
C) $84\pi\text{ cm}^3$  
D) $92\pi\text{ cm}^3$  
E) $100\pi\text{ cm}^3$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Un reservorio cilíndrico de agua potable abastece a un caserío de $200$ habitantes en Cajamarca. Si cada persona consume en promedio $50\text{ litros}$ diarios de agua y el tanque tiene un diámetro interior de $2\text{ m}$, calcule la altura mínima que debe tener el reservorio para garantizar $2$ días completos de autonomía comunal. ($\text{use } \pi \approx 3.1416$).  
A) $4.85\text{ m}$  
B) $5.50\text{ m}$  
C) $6.37\text{ m}$  
D) $7.12\text{ m}$  
E) $8.00\text{ m}$  

32. En una planta pesquera en Pisco, se diseña una tolva cónica de acero para recepción de harina de pescado. La tolva tiene $2\text{ m}$ de radio superior y una profundidad de $3\text{ m}$. Si la chapa de acero galvanizado cuesta $S/\, 90$ por metro cuadrado, calcule el costo aproximado del material para la superficie lateral cónica. ($\text{use } \pi \approx 3.1416$).  
A) $S/\, 1\,850$  
B) $S/\, 2\,039$  
C) $S/\, 2\,240$  
D) $S/\, 2\,450$  
E) $S/\, 2\,680$  

33. Un camión cisterna transporta combustible en un tanque con forma de cilindro circular recto colocado horizontalmente de $2\text{ m}$ de diámetro y $8\text{ m}$ de longitud. ¿Cuántos galones de petróleo transporta a capacidad máxima si $1\text{ galón} \approx 3.785\text{ litros}$? ($\text{use } \pi \approx 3.1416$).  
A) $\approx 6\,240\text{ gal}$  
B) $\approx 6\,640\text{ gal}$  
C) $\approx 6\,850\text{ gal}$  
D) $\approx 7\,100\text{ gal}$  
E) $\approx 7\,500\text{ gal}$  

34. Una boya marina de señalización en el puerto del Callao está compuesta por una semiesfera inferior de radio $R = 1.2\text{ m}$ unida a un cono superior de igual radio y altura $h = 1.6\text{ m}$. Calcule el volumen total de la boya marina.  
A) $1.644\pi\text{ m}^3$  
B) $1.728\pi\text{ m}^3$  
C) $1.920\pi\text{ m}^3$  
D) $2.140\pi\text{ m}^3$  
E) $2.304\pi\text{ m}^3$  

35. En un vivero comunal en Oxapampa, se utiliza un sistema de calentamiento de agua con un termotanque esférico de cobre de $80\text{ cm}$ de diámetro. Si el agua ingresa a $15^\circ\text{C}$ y se calienta a $65^\circ\text{C}$, ¿cuántas kilocalorías de energía térmica absorbe el tanque lleno? ($\text{use } \pi \approx 3.1416, 1\text{ L} \leftrightarrow 1\text{ kg}$).  
A) $\approx 11\,250\text{ kcal}$  
B) $\approx 12\,450\text{ kcal}$  
C) $\approx 13\,404\text{ kcal}$  
D) $\approx 14\,200\text{ kcal}$  
E) $\approx 15\,100\text{ kcal}$  

36. En una obra de electrificación rural, se excavan hoyos cilíndricos de $0.6\text{ m}$ de diámetro y $2\text{ m}$ de profundidad para plantar postes de concreto. ¿Qué volumen de tierra suelta en metros cúbicos se extrae por cada hoyo excavado? ($\text{use } \pi \approx 3.1416$).  
A) $0.452\text{ m}^3$  
B) $0.565\text{ m}^3$  
C) $0.678\text{ m}^3$  
D) $0.754\text{ m}^3$  
E) $0.840\text{ m}^3$  

37. Se diseñan copas cónicas de vidrio para una empresa vitivinícola en Ica. Cada copa tiene $6\text{ cm}$ de diámetro en la boca y $8\text{ cm}$ de profundidad interior. Si una botella contiene $750\text{ mL}$ de vino y se sirven copas llenas hasta los $\frac{3}{4}$ de su altura, ¿para cuántas copas completas alcanza la botella?  
A) $18\text{ copas}$  
B) $20\text{ copas}$  
C) $23\text{ copas}$  
D) $24\text{ copas}$  
E) $26\text{ copas}$  

38. Una fábrica de envases metálicos en Arequipa elabora latas cilíndricas de leche evaporada de $400\text{ mL}$ ($400\text{ cm}^3$) de capacidad. Si la lata tiene una altura de $10\text{ cm}$, ¿cuál es el diámetro aproximado de la lata? ($\text{use } \pi \approx 3.1416$).  
A) $6.84\text{ cm}$  
B) $7.14\text{ cm}$  
C) $7.45\text{ cm}$  
D) $7.82\text{ cm}$  
E) $8.00\text{ cm}$  

39. En una fábrica de chocolates en Tarapoto, se moldean bombones esféricos macizos de $3\text{ cm}$ de diámetro y se envuelven individualmente en papel platino brillante. Si se elaboran $1\,000$ bombones, ¿cuántos metros cuadrados de papel platino como mínimo se utilizarán sin considerar traslapes? ($\text{use } \pi \approx 3.1416$).  
A) $2.45\text{ m}^2$  
B) $2.83\text{ m}^2$  
C) $3.14\text{ m}^2$  
D) $3.56\text{ m}^2$  
E) $4.12\text{ m}^2$  

40. Un domo hemisférico (semiesférico) de un planetario escolar en Huancayo tiene un diámetro basal de $14\text{ m}$. Se proyecta impermeabilizar el exterior de la cúpula con pintura elastomérica que cuesta $S/\, 25$ por metro cuadrado. ¿Cuál es el presupuesto aproximado de impermeabilización? ($\text{use } \pi \approx \frac{22}{7}$).  
A) $S/\, 6\,850$  
B) $S/\, 7\,400$  
C) $S/\, 7\,700$  
D) $S/\, 8\,250$  
E) $S/\, 8\,800$  

41. Una canaleta colectora de agua de lluvia tiene forma de medio cilindro hueco (semicilindro abierto) de $20\text{ cm}$ de diámetro y $6\text{ m}$ de longitud. ¿Cuál es la capacidad máxima de evacuación en litros de agua de la canaleta? ($\text{use } \pi \approx 3.1416$).  
A) $84.2\text{ L}$  
B) $94.25\text{ L}$  
C) $105.4\text{ L}$  
D) $120.0\text{ L}$  
E) $140.5\text{ L}$  

42. Para alimentar ganado ovino en Puno durante el invierno, se comprime forraje ensilado en pacas cilíndricas de $1.2\text{ m}$ de diámetro y $1.5\text{ m}$ de altura. Si la masa de una paca es de $450\text{ kg}$, ¿cuál es la densidad aparente del forraje compactado?  
A) $225\text{ kg/m}^3$  
B) $265\text{ kg/m}^3$  
C) $295\text{ kg/m}^3$  
D) $320\text{ kg/m}^3$  
E) $350\text{ kg/m}^3$  

43. Una probeta cilíndrica graduada de laboratorio de $4\text{ cm}$ de diámetro contiene agua. Se sumergen en ella $5$ canicas de vidrio esféricas idénticas de $2\text{ cm}$ de diámetro cada una. ¿Cuántos centímetros asciende el nivel del agua en la probeta?  
A) $0.56\text{ cm}$  
B) $0.67\text{ cm}$  
C) $0.78\text{ cm}$  
D) $0.83\text{ cm}$  
E) $1.67\text{ cm}$  

44. Un reloj de arena decorativo está formado por dos conos idénticos unidos por sus vértices. Cada cono tiene $6\text{ cm}$ de altura y radio de base $4\text{ cm}$. Si la arena llena exactamente uno de los conos y fluye hacia el cono inferior a una velocidad constante de $0.5\text{ cm}^3$ por segundo, ¿cuántos minutos y segundos dura la caída completa de la arena? ($\text{use } \pi \approx 3.1416$).  
A) $3\text{ min } 12\text{ s}$  
B) $3\text{ min } 21\text{ s}$  
C) $3\text{ min } 45\text{ s}$  
D) $4\text{ min } 02\text{ s}$  
E) $4\text{ min } 15\text{ s}$  

45. En una planta embotelladora de jugos de fruta en Chanchamayo, se vierte líquido en botellas cilíndricas de $6\text{ cm}$ de diámetro a razón de $200\text{ mL}$ por segundo. ¿Con qué rapidez constante en centímetros por segundo asciende el nivel del líquido dentro de la botella durante el llenado? ($\text{use } \pi \approx 3.1416$).  
A) $5.42\text{ cm/s}$  
B) $6.15\text{ cm/s}$  
C) $7.07\text{ cm/s}$  
D) $8.24\text{ cm/s}$  
E) $9.10\text{ cm/s}$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | C | **16** | C | **31** | C |
| **2** | A | **17** | D | **32** | B |
| **3** | B | **18** | B | **33** | B |
| **4** | B | **19** | D | **34** | C |
| **5** | C | **20** | B | **35** | C |
| **6** | B | **21** | C | **36** | B |
| **7** | C | **22** | B | **37** | C |
| **8** | B | **23** | B | **38** | B |
| **9** | C | **24** | A | **39** | B |
| **10** | C | **25** | A | **40** | C |
| **11** | C | **26** | D | **41** | B |
| **12** | D | **27** | D | **42** | B |
| **13** | D | **28** | B | **43** | E |
| **14** | C | **29** | B | **44** | B |
| **15** | B | **30** | C | **45** | C |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde la generatriz con la altura en conos o yerra en la equivalencia métrica ($1\text{ m}^3 = 1000\text{ L}$). | Memorizar la tabla de equivalencias de capacidad del §2.4 y practicar el Teorema de Pitágoras en conos: $g^2 = r^2 + h^2$. |
| **En Proceso (60% - 80% aciertos)** | Aplica correctamente volúmenes simples, pero duda en sólidos compuestos o cuerpos truncados. | Resolver los ejercicios 16 al 30 separando los cuerpos compuestos en sus componentes cilíndricos, cónicos y esféricos. |
| **Avanzado (> 80% aciertos)** | Modela problemas de tanques GLP, silos mixtos, caudales de bombeo y autonomía de agua con rapidez. | Resolver los problemas 31 al 45 cronometrando 1.5 minutos por pregunta sin calculadora. |

### Preguntas Guía para la Reflexión:
1. *¿Por qué el volumen del cono es exactamente un tercio del volumen del cilindro circunscrito, y cómo se relaciona esto con la pirámide y el prisma?*
2. *¿Por qué un depósito esférico resiste mejor la presión que uno cúbico o cilíndrico con igual cantidad de material?*
3. *¿Por qué en los problemas de física e ingeniería el cálculo de capacidad en litros exige convertir primero las dimensiones lineales a decímetros o metros cúbicos?*

---

## 7. Formulario Resumen

| Sólido de Revolución | Parámetros Geométricos | Fórmulas de Área y Volumen |
| :--- | :--- | :--- |
| **Cilindro Recto** | Radio basal $r$, altura $h$, generatriz $g = h$ | $A_L = 2\pi r h,\quad A_T = 2\pi r(h + r),\quad V = \pi r^2 h$ |
| **Cono Recto** | Radio $r$, altura $h$, generatriz $g = \sqrt{r^2 + h^2}$ | $A_L = \pi r g,\quad A_T = \pi r(g + r),\quad V = \frac{1}{3}\pi r^2 h$ |
| **Ángulo de Desarrollo Cono** | Radio $r$ y generatriz $g$ | $\theta = \frac{r}{g} \cdot 360^\circ$ |
| **Esfera** | Radio $r$, diámetro $D = 2r$ | $A_S = 4\pi r^2 = \pi D^2,\quad V = \frac{4}{3}\pi r^3 = \frac{1}{6}\pi D^3$ |
| **Semiesfera (Hemisferio)** | Radio $r$ | $A_{\text{curva}} = 2\pi r^2,\quad A_T = 3\pi r^2,\quad V = \frac{2}{3}\pi r^3$ |
| **Tronco de Cono Recto** | Radios $R, r$ y altura $h$ | $V = \frac{\pi h}{3}(R^2 + r^2 + R \cdot r)$ |
| **Equivalencia de Capacidad** | Metro cúbico a litros | $1\text{ m}^3 = 1\,000\text{ litros} = 1\,000\,000\text{ cm}^3$ |
| **Equivalencia Pequeña** | Decímetro cúbico y centímetro cúbico | $1\text{ dm}^3 = 1\text{ litro},\quad 1\text{ cm}^3 = 1\text{ mL}$ |
| **Masa de Agua Pura** | Volumen a kilogramos | $1\text{ litro} \leftrightarrow 1\text{ kg},\quad 1\text{ m}^3 \leftrightarrow 1\,000\text{ kg} = 1\text{ tonelada}$ |
| **Relación de Arquímedes** | Cilindro equilátero ($h=2r$), esfera ($r$) y cono | $V_{\text{cono}} : V_{\text{esfera}} : V_{\text{cilindro}} = 1 : 2 : 3$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 1 clave(s) corregida(s) y 3 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **18** | B | B | Corregida | La opción E repetía el valor de B ($\sqrt[3]{125}=5$); se reemplazó por un distractor distinto. Respuesta: $5$ cm (B). |
| **37** | C | C | Corregida | Se ajustó la opción C: la copa servida es un cono de $r=2.25$ cm y $h=6$ cm ($V\approx31.8$ mL) y $750/31.8\approx23$. |
| **43** | D | E | Corregida | Se ajustó la opción E: las $5$ canicas aportan $\frac{20\pi}{3}\approx20.94\text{ cm}^3$ y el nivel sube $20.94/(4\pi)\approx1.67$ cm. |

**Claves sin cambios:** 44 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
