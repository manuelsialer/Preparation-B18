# Tema 05: Sistema de Unidades y Conversión (Múltiplos y Submúltiplos de Longitud y Tiempo)

**Área:** Aritmética / Medida y Regularidad
**Nivel:** Preuniversitario / Beca 18 (ENP)
**Objetivo de Aprendizaje:** Comprender la fundamentación metrológica del Sistema Internacional de Unidades (SI), dominar los prefijos de múltiplos y submúltiplos métricos, aplicar factores de conversión unitarios en longitud y tiempo (sistemas decimal y sexagesimal), y resolver situaciones contextualizadas de alta demanda cognitiva.

---

## 1. Motivación y Contexto Real

En la ingeniería civil, la agronomía de precisión, la telemetría satelital y la gestión logística de emergencias en el Perú, el manejo riguroso de las unidades de medida es la línea divisoria entre el éxito operativo y el desastre técnico.

Imaginemos el trazo de una carretera interoceánica en los Andes peruanos: los planos geodésicos manejan coordenadas en metros y kilómetros, los sensores lidar miden deformaciones de talud en milímetros y micrómetros, mientras que las brigadas de rescate durante huaicos cuantifican caudales en litros por segundo ($L/s$) y planifican evacuaciones en horas, minutos y segundos exactos. Un error en la escala de conversión de una sola unidad puede descalibrar una obra multimillonaria o poner en riesgo vidas humanas.

En el Examen Nacional de Preselección (ENP) de Beca 18 y los exámenes de admisión de mayor rigor académico (UNI, San Marcos, PUCP), las preguntas de sistemas de unidades no se limitan a multiplicar por 10 o por 60; exigen conversiones encadenadas, cambios dimensionales compuestos (velocidades, caudales, densidades superficiales) y la correcta articulación entre el sistema sexagesimal de tiempo y la representación decimal de variables continuas.

---

## 2. Fundamentación Teórica Rigurosa

### 2.1 El Sistema Internacional de Unidades (SI)
El Sistema Internacional de Unidades (SI) establece siete magnitudes fundamentales a partir de las cuales se derivan todas las demás. En el ámbito de la aritmética preuniversitaria y la resolución de situaciones del entorno, dos magnitudes resultan esenciales:

1. **Longitud:** Su unidad base en el SI es el **metro** ($\text{m}$), definido a partir de la velocidad de la luz en el vacío ($c = 299\,792\,458\text{ m/s}$).
2. **Tiempo:** Su unidad base en el SI es el **segundo** ($\text{s}$), definido a partir de la frecuencia de transición hiperfina del átomo de cesio-133.

### 2.2 Prefijos Métricos del SI: Múltiplos y Submúltiplos
El SI emplea prefijos decimales estandarizados que se anteponen al nombre o símbolo de la unidad para expresar múltiplos o submúltiplos mediante potencias enteras de base 10:

$$\text{Medida} = \text{Prefijo} \times \text{Unidad Base}$$

#### Tabla Universal de Prefijos del SI
| Tipo | Prefijo | Símbolo | Factor Multiplicador | Notación Exponencial |
| :--- | :--- | :---: | :--- | :---: |
| **Múltiplos** | Tera | $\text{T}$ | $1\,000\,000\,000\,000$ | $10^{12}$ |
| | Giga | $\text{G}$ | $1\,000\,000\,000$ | $10^9$ |
| | Mega | $\text{M}$ | $1\,000\,000$ | $10^6$ |
| | Kilo | $\text{k}$ | $1\,000$ | $10^3$ |
| | Hecto | $\text{h}$ | $100$ | $10^2$ |
| | Deca | $\text{da}$ | $10$ | $10^1$ |
| **Unidad Base** | *(metro / gramo)* | — | $1$ | $10^0$ |
| **Submúltiplos** | Deci | $\text{d}$ | $0{,}1$ | $10^{-1}$ |
| | Centi | $\text{c}$ | $0{,}01$ | $10^{-2}$ |
| | Mili | $\text{m}$ | $0{,}001$ | $10^{-3}$ |
| | Micro | $\mu$ | $0{,}000\,001$ | $10^{-6}$ |
| | Nano | $\text{n}$ | $0{,}000\,000\,001$ | $10^{-9}$ |
| | Pico | $\text{p}$ | $0{,}000\,000\,000\,001$ | $10^{-12}$ |

> [!WARNING]
> **Atención al uso de mayúsculas y minúsculas:**
> * $\text{m}$ minúscula representa el submúltiplo **mili** ($10^{-3}$) o el **metro**.
> * $\text{M}$ mayúscula representa el múltiplo **Mega** ($10^6$).
> * Escribir $15\text{ Mm}$ significa quince megametros ($15 \times 10^6\text{ m}$), mientras que $15\text{ mm}$ significa quince milímetros ($15 \times 10^{-3}\text{ m}$). ¡La diferencia de magnitud es de nueve órdenes de diez ($10^9$)!

### 2.3 Unidades de Longitud y Factores de Conversión
En el sistema métrico decimal, cada orden de longitud lineal difiere del anterior en un factor de 10:

$$1\text{ km} = 10\text{ hm} = 100\text{ dam} = 1\,000\text{ m} = 10\,000\text{ dm} = 100\,000\text{ cm} = 1\,000\,000\text{ mm}$$

#### Método del Factor de Conversión Unitario
Para transformar una medida de una unidad $U_1$ a otra unidad $U_2$, se multiplica la cantidad por una fracción equivalente a la unidad ($1$), donde el numerador y el denominador representan la misma cantidad física pero en distintas unidades:

$$\text{Valor en } U_2 = \text{Valor en } U_1 \times \left(\frac{\text{Equivalencia en } U_2}{\text{Equivalencia en } U_1}\right)$$

*Ejemplo:* Convertir $4{,}8\text{ km}$ a centímetros ($\text{cm}$):

$$4{,}8\text{ km} \times \left(\frac{1\,000\text{ m}}{1\text{ km}}\right) \times \left(\frac{100\text{ cm}}{1\text{ m}}\right) = 4{,}8 \times 100\,000\text{ cm} = 480\,000\text{ cm} = 4{,}8 \times 10^5\text{ cm}$$

### 2.4 Unidades Derivadas de Superficie y Volumen
Las unidades de área y volumen se derivan elevando al cuadrado y al cubo las relaciones lineales de longitud. Este principio es una fuente frecuente de errores en evaluaciones preuniversitarias:

#### A. Superficie (Área):

$$(1\text{ m})^2 = (100\text{ cm})^2 \implies 1\text{ m}^2 = 10\,000\text{ cm}^2 = 10^4\text{ cm}^2$$

$$(1\text{ km})^2 = (1\,000\text{ m})^2 \implies 1\text{ km}^2 = 1\,000\,000\text{ m}^2 = 10^6\text{ m}^2$$

*Unidades Agrarias Especiales:*
* **Hectárea ($\text{ha}$):** $1\text{ ha} = 1\text{ hm}^2 = 10\,000\text{ m}^2$.
* **Área ($\text{a}$):** $1\text{ a} = 1\text{ dam}^2 = 100\text{ m}^2$.
* **Centiarea ($\text{ca}$):** $1\text{ ca} = 1\text{ m}^2$.

#### B. Capacidad y Volumen:
El puente fundamental entre la capacidad métrica (litro) y el volumen geométrico (metro cúbico) es:

$$1\text{ L} = 1\text{ dm}^3 = 1\,000\text{ cm}^3 = 10^{-3}\text{ m}^3$$

$$1\text{ m}^3 = 1\,000\text{ dm}^3 = 1\,000\text{ L} = 10^6\text{ cm}^3 = 10^6\text{ mL}$$

$$1\text{ mL} = 1\text{ cm}^3 = 1\text{ cc}$$

### 2.5 Unidades de Tiempo: Sistema Decimal vs. Sistema Sexagesimal
A diferencia de la longitud, que es estrictamente decimal, el tiempo combina submúltiplos decimales (milisegundos, microsegundos) con un sistema sexagesimal para intervalos humanos (segundos, minutos, horas) y astronómicos (días, años).

#### Equivalencias Fundamentales:

$$1\text{ minuto (min)} = 60\text{ segundos (s)}$$

$$1\text{ hora (h)} = 60\text{ min} = 3\,600\text{ s}$$

$$1\text{ día solar medio (d)} = 24\text{ h} = 1\,440\text{ min} = 86\,400\text{ s}$$

$$1\text{ semana} = 7\text{ días} = 168\text{ h}$$

$$1\text{ mes comercial} = 30\text{ días}$$

$$1\text{ año común} = 365\text{ días} \quad \mid \quad 1\text{ año bisiesto} = 366\text{ días} \quad \mid \quad 1\text{ año comercial} = 360\text{ días}$$

#### Conversión entre Horas Decimales y Notación Sexagesimal
La confusión entre la parte decimal de una hora y los minutos sexagesimales es uno de los distractores más comunes en los exámenes.

* **Regla de Conversión Decimal $\to$ Sexagesimal:**
Si tenemos $T = H + D\text{ h}$, donde $H$ es la parte entera en horas y $D$ es la fracción decimal:

$$\text{Minutos} = D \times 60$$

Si de esta multiplicación resulta una nueva fracción decimal $M + d\text{ min}$, los segundos son:

$$\text{Segundos} = d \times 60$$

*Ejemplo:* Convertir $3{,}45\text{ h}$ a horas, minutos y segundos:
1. Parte entera: $3\text{ h}$.
2. Parte decimal: $0{,}45\text{ h} \times 60\frac{\text{min}}{\text{h}} = 27\text{ min}$ (exactos).
3. Por lo tanto: $3{,}45\text{ h} = 3\text{ h } 27\text{ min}$ (¡NO $3\text{ h } 45\text{ min}$!).

*Ejemplo Inverso:* Convertir $2\text{ h } 15\text{ min } 36\text{ s}$ a horas decimales:

$$T = 2 + \frac{15}{60} + \frac{36}{3\,600} = 2 + 0{,}25 + 0{,}01 = 2{,}26\text{ h}$$

### 2.6 Magnitudes Compuestas Clave: Velocidad y Caudal
1. **Velocidad:** Conversión entre $\text{km/h}$ y $\text{m/s}$:

$$1\frac{\text{km}}{\text{h}} = \frac{1\,000\text{ m}}{3\,600\text{ s}} = \frac{5}{18}\frac{\text{m}}{\text{s}}$$

$$\text{Para pasar de km/h a m/s: multiplicar por } \frac{5}{18}$$

$$\text{Para pasar de m/s a km/h: multiplicar por } \frac{18}{5}$$

2. **Caudal ($Q$):** Volumen que fluye por unidad de tiempo:

$$1\frac{\text{m}^3}{\text{s}} = 1\,000\frac{\text{L}}{\text{s}} = 60\,000\frac{\text{L}}{\text{min}} = 3\,600\frac{\text{m}^3}{\text{h}}$$

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Fundamentos Operativos)

#### Ejercicio 1: Conversión Encadenada con Prefijos Métricos
Un cable de fibra óptica instalado entre dos antenas de telecomunicación mide $3{,}75\text{ km}$. Si un tramo de prueba mide $48\,000\text{ cm}$ y otro tramo de empalme mide $850\text{ m}$, ¿cuántos decámetros ($\text{dam}$) le faltan al tendido para completar la distancia total?

**Solución paso a paso:**

**Paso 1:** Identificar la incógnita y unificar a una unidad común:
Conviene convertir todas las magnitudes a la unidad pedida: decámetros ($\text{dam}$), recordando que:

$$1\text{ dam} = 10\text{ m} \implies 1\text{ m} = 0{,}1\text{ dam}$$

$$1\text{ km} = 1\,000\text{ m} = 100\text{ dam}$$

$$1\text{ dam} = 1\,000\text{ cm} \implies 1\text{ cm} = 10^{-3}\text{ dam}$$

**Paso 2:** Convertir la distancia total:

$$D_{\text{total}} = 3{,}75\text{ km} \times \frac{100\text{ dam}}{1\text{ km}} = 375\text{ dam}$$

**Paso 3:** Convertir los tramos ya instalados:
* Tramo 1:

$$T_1 = 48\,000\text{ cm} \times \frac{1\text{ dam}}{1\,000\text{ cm}} = 48\text{ dam}$$

* Tramo 2:

$$T_2 = 850\text{ m} \times \frac{1\text{ dam}}{10\text{ m}} = 85\text{ dam}$$

**Paso 4:** Calcular la distancia instalada y la faltante:

$$D_{\text{instalada}} = T_1 + T_2 = 48\text{ dam} + 85\text{ dam} = 133\text{ dam}$$

$$D_{\text{faltante}} = D_{\text{total}} - D_{\text{instalada}} = 375\text{ dam} - 133\text{ dam} = 242\text{ dam}$$

*Respuesta:* Faltan $242\text{ dam}$ para completar el tendido total.

---

#### Ejercicio 2: Conversión Sexagesimal a Decimal y Suma de Tiempos
Un estudiante de academia dedica tres sesiones de estudio por la tarde: la primera dura $1\text{ h } 45\text{ min } 30\text{ s}$, la segunda dura $2\text{ h } 38\text{ min } 45\text{ s}$ y la tercera dura $55\text{ min } 45\text{ s}$. Exprese el tiempo total de estudio en horas en formato decimal exacto.

**Solución paso a paso:**

**Paso 1:** Sumar los componentes sexagesimales de forma ordenada:

| Sesión de Estudio | Horas | Minutos | Segundos |
| :--- | :---: | :---: | :---: |
| Primera sesión | $1\text{ h}$ | $45\text{ min}$ | $30\text{ s}$ |
| Segunda sesión | $2\text{ h}$ | $38\text{ min}$ | $45\text{ s}$ |
| Tercera sesión | $0\text{ h}$ | $55\text{ min}$ | $45\text{ s}$ |
| **Suma bruta** | **$3\text{ h}$** | **$138\text{ min}$** | **$120\text{ s}$** |

**Paso 2:** Normalizar los segundos a minutos:

$$120\text{ s} = \frac{120}{60}\text{ min} = 2\text{ min } 00\text{ s}$$

Sumamos a los minutos: $138\text{ min} + 2\text{ min} = 140\text{ min}$.

**Paso 3:** Normalizar los minutos a horas:

$$140\text{ min} = 120\text{ min} + 20\text{ min} = 2\text{ h } 20\text{ min}$$

Sumamos a las horas: $3\text{ h} + 2\text{ h} = 5\text{ h}$.
Tiempo total sexagesimal: $5\text{ h } 20\text{ min } 00\text{ s}$.

**Paso 4:** Convertir a horas en forma decimal fraccionaria y periódica:

$$T = 5\text{ h} + \frac{20\text{ min}}{60\frac{\text{min}}{\text{h}}} = 5 + \frac{1}{3}\text{ h} = \frac{16}{3}\text{ h} = 5{,}\widehat{3}\text{ h}$$

*Respuesta:* El tiempo total de estudio es de $\frac{16}{3}\text{ h} = 5{,}\widehat{3}\text{ h}$ (o $5\text{ h } 20\text{ min}$).

---

#### Ejercicio 3: Transformación de Unidades de Velocidad
Un vehículo de transporte interprovincial viaja por la Panamericana Sur a una velocidad constante de $90\text{ km/h}$. Si ingresa a un tramo urbano donde el límite máximo de velocidad es de $22\text{ m/s}$, determine si el conductor está infringiendo el límite y calcule la diferencia en $\text{m/s}$.

**Solución paso a paso:**

**Paso 1:** Convertir la velocidad del vehículo a $\text{m/s}$ usando el factor directo $\frac{5}{18}$:

$$V = 90\frac{\text{km}}{\text{h}} \times \frac{5\text{ m/s}}{18\text{ km/h}} = \left(\frac{90}{18}\right) \times 5 = 5 \times 5 = 25\text{ m/s}$$

**Paso 2:** Comparar con el límite permitido:

$$V_{\text{vehículo}} = 25\text{ m/s}$$

$$V_{\text{límite}} = 22\text{ m/s}$$

Como $25 > 22$, el conductor sí infringe el límite de velocidad.

**Paso 3:** Calcular la diferencia:

$$\Delta V = 25\text{ m/s} - 22\text{ m/s} = 3\text{ m/s}$$

*Respuesta:* El conductor excede el límite permitido por $3\text{ m/s}$ (equivalente a $10{,}8\text{ km/h}$).

---

### Bloque B: Nivel Intermedio (Aplicaciones Compuestas)

#### Ejercicio 4: Conversión de Áreas y Rendimiento Agrario
Una comunidad campesina en el valle del Mantaro posee un terreno de cultivo de forma rectangular cuyas dimensiones son $450\text{ m}$ de largo por $240\text{ m}$ de ancho. Si se destina el $40\%$ del terreno a la siembra de papa nativa y se sabe que cada metro cuadrado produce en promedio $2{,}5\text{ kg}$ de tubérculo, ¿cuántas toneladas métricas ($\text{t}$) de papa se cosecharán? ($1\text{ t} = 1\,000\text{ kg}$).

**Solución paso a paso:**

**Paso 1:** Calcular el área total del terreno en metros cuadrados:

$$\text{Área}_{\text{total}} = 450\text{ m} \times 240\text{ m} = 108\,000\text{ m}^2$$

*(En hectáreas equivale a $\frac{108\,000}{10\,000} = 10{,}8\text{ ha}$).*

**Paso 2:** Calcular el área destinada al cultivo de papa:

$$\text{Área}_{\text{papa}} = 40\% \times 108\,000\text{ m}^2 = \frac{40}{100} \times 108\,000 = 43\,200\text{ m}^2$$

**Paso 3:** Calcular la masa total cosechada en kilogramos:

$$\text{Masa} = 43\,200\text{ m}^2 \times 2{,}5\frac{\text{kg}}{\text{m}^2} = 108\,000\text{ kg}$$

**Paso 4:** Convertir la masa a toneladas métricas ($\text{t}$):

$$\text{Masa en t} = 108\,000\text{ kg} \times \frac{1\text{ t}}{1\,000\text{ kg}} = 108\text{ t}$$

*Respuesta:* Se cosecharán $108\text{ toneladas métricas}$ de papa nativa.

---

#### Ejercicio 5: Caudal, Capacidad y Tiempo de Llenado Compuesto
Un reservorio comunal para riego tecnificado tiene una capacidad de $180\text{ m}^3$. El reservorio se llena mediante dos tuberías simultáneas: la tubería $A$ abastece a razón de $150\text{ L/min}$ y la tubería $B$ aporta $5\text{ L/s}$. Si al iniciar el proceso el reservorio ya contiene el $15\%$ de su capacidad total, ¿cuántas horas y minutos exactos tardará en llenarse completamente?

**Solución paso a paso:**

**Paso 1:** Calcular el volumen necesario por llenar:
* Capacidad total en litros:

$$V_{\text{total}} = 180\text{ m}^3 \times \frac{1\,000\text{ L}}{1\text{ m}^3} = 180\,000\text{ L}$$

* Volumen inicial existente ($15\%$):

$$V_{\text{inicial}} = 0{,}15 \times 180\,000\text{ L} = 27\,000\text{ L}$$

* Volumen que falta llenar:

$$V_{\text{falta}} = 180\,000\text{ L} - 27\,000\text{ L} = 153\,000\text{ L}$$

**Paso 2:** Unificar y sumar los caudales de ambas tuberías:
* Caudal de la tubería $B$:

$$Q_B = 5\frac{\text{L}}{\text{s}} \times \frac{60\text{ s}}{1\text{ min}} = 300\frac{\text{L}}{\text{min}}$$

* Caudal total de llenado combinado:

$$Q_{\text{total}} = Q_A + Q_B = 150\frac{\text{L}}{\text{min}} + 300\frac{\text{L}}{\text{min}} = 450\frac{\text{L}}{\text{min}}$$

**Paso 3:** Calcular el tiempo en minutos:

$$t = \frac{V_{\text{falta}}}{Q_{\text{total}}} = \frac{153\,000\text{ L}}{450\text{ L/min}} = 340\text{ min}$$

**Paso 4:** Convertir el tiempo a horas y minutos exactos:

$$340\text{ min} = 300\text{ min} + 40\text{ min} = 5\text{ h } 40\text{ min}$$

En horas decimales sería: $5 + \frac{40}{60} = 5{,}\widehat{6}\text{ h}$.

*Respuesta:* Tardará exactamente $5\text{ horas y } 40\text{ minutos}$ en llenarse por completo.

---

#### Ejercicio 6: Escala Cartográfica y Tiempo de Recorrido
En una carta geográfica nacional a escala $1:250\,000$, la distancia medida en línea recta entre dos poblados andinos es de $18{,}4\text{ cm}$. Si una brigada médica recorre dicha ruta en un vehículo todoterreno a una velocidad media de $40\text{ km/h}$ y hace dos paradas técnicas de $25\text{ minutos}$ cada una, ¿cuánto tiempo total (en horas y minutos) dura la expedición?

**Solución paso a paso:**

**Paso 1:** Calcular la distancia real sobre el terreno:
La escala $1:250\,000$ indica que $1\text{ cm}$ en el papel equivale a $250\,000\text{ cm}$ en la realidad.

$$D_{\text{real}} = 18{,}4\text{ cm} \times 250\,000 = 4\,600\,000\text{ cm}$$

**Paso 2:** Convertir la distancia real a kilómetros:

$$D_{\text{real}} = 4\,600\,000\text{ cm} \times \frac{1\text{ m}}{100\text{ cm}} \times \frac{1\text{ km}}{1\,000\text{ m}} = \frac{4\,600\,000}{100\,000}\text{ km} = 46\text{ km}$$

**Paso 3:** Calcular el tiempo de movimiento del vehículo:

$$t_{\text{viaje}} = \frac{D}{V} = \frac{46\text{ km}}{40\text{ km/h}} = 1{,}15\text{ h}$$

Convertimos $1{,}15\text{ h}$ a minutos:

$$1{,}15 \times 60\text{ min} = 69\text{ min} = 1\text{ h } 09\text{ min}$$

**Paso 4:** Sumar el tiempo de las paradas técnicas:

$$t_{\text{paradas}} = 2 \times 25\text{ min} = 50\text{ min}$$

$$t_{\text{total}} = 69\text{ min} + 50\text{ min} = 119\text{ min} = 1\text{ h } 59\text{ min}$$

*Respuesta:* La expedición dura en total $1\text{ hora y } 59\text{ minutos}$.

---

#### Ejercicio 7: Microsegundos, Frecuencia y Transferencia de Datos
Un procesador digital envía paquetes de telemetría hacia una antena cada $250\text{ microsegundos}$ ($\mu\text{s}$). Cada paquete tiene un tamaño de $128\text{ bytes}$. ¿Cuántos megabytes ($\text{MB}$) de información se transmiten en un lapso continuo de $2\text{ horas}$? Asuma que $1\text{ MB} = 10^6\text{ bytes}$ (sistema decimal de telecomunicaciones).

**Solución paso a paso:**

**Paso 1:** Convertir el intervalo de transmisión a segundos:

$$\Delta t = 250\ \mu\text{s} = 250 \times 10^{-6}\text{ s} = 2{,}5 \times 10^{-4}\text{ s}$$

**Paso 2:** Calcular la cantidad de segundos en $2\text{ horas}$:

$$T = 2\text{ h} \times \frac{3\,600\text{ s}}{1\text{ h}} = 7\,200\text{ s} = 7{,}2 \times 10^3\text{ s}$$

**Paso 3:** Calcular el número total de paquetes transmitidos ($N$):

$$N = \frac{T}{\Delta t} = \frac{7\,200\text{ s}}{250 \times 10^{-6}\text{ s}} = \frac{7{,}2 \times 10^3}{2{,}5 \times 10^{-4}} = 2{,}88 \times 10^7\text{ paquetes}$$

**Paso 4:** Calcular el total de bytes y convertir a megabytes ($\text{MB}$):

$$\text{Total bytes} = N \times 128\text{ bytes} = 2{,}88 \times 10^7 \times 128 = 368{,}64 \times 10^7\text{ bytes} = 3\,686{,}4 \times 10^6\text{ bytes}$$

Convertimos a $\text{MB}$ ($10^6\text{ bytes}$):

$$\text{Total MB} = \frac{3\,686{,}4 \times 10^6\text{ bytes}}{10^6\text{ bytes/MB}} = 3\,686{,}4\text{ MB}$$

*Respuesta:* Se transmiten $3\,686{,}4\text{ MB}$ de datos.

---

### Bloque C: Nivel Avanzado / Contexto Beca 18 (Alta Demanda Cognitiva)

#### Ejercicio 8: Logística de Evacuación Fluvial y Terrestre por Inundación
Durante una crecida extraordinaria del río Huallaga en Loreto, se debe evacuar a una población aislada. El plan consta de dos etapas:
* **Etapa 1 (Fluvial):** Una lancha recorre $72\text{ km}$ río abajo. La lancha navega a una velocidad propia de $18\text{ km/h}$ y la corriente del río fluye a $2\text{ m/s}$.
* **Etapa 2 (Terrestre):** Al desembarcar, los damnificados abordan camiones que recorren $45\text{ km}$ por trocha a una velocidad de $30\text{ km/h}$.
Si la operación de transbordo entre la lancha y los camiones toma exactamente $42\text{ minutos}$, determine el tiempo total de la evacuación expresado en horas, minutos y segundos exactos.

**Solución paso a paso:**

**Paso 1:** Analizar la velocidad efectiva en la etapa fluvial:
La lancha viaja río abajo, por lo que la velocidad del río se suma a la velocidad de la lancha:

$$V_{\text{río}} = 2\frac{\text{m}}{\text{s}} \times \frac{18\text{ km/h}}{5\text{ m/s}} = \frac{36}{5}\text{ km/h} = 7{,}2\text{ km/h}$$

$$V_{\text{efectiva}} = V_{\text{lancha}} + V_{\text{río}} = 18\text{ km/h} + 7{,}2\text{ km/h} = 25{,}2\text{ km/h}$$

**Paso 2:** Calcular el tiempo de la etapa fluvial ($t_1$):

$$t_1 = \frac{D_1}{V_{\text{efectiva}}} = \frac{72\text{ km}}{25{,}2\text{ km/h}} = \frac{72}{\frac{252}{10}} = \frac{720}{252}\text{ h}$$

Simplificamos sacando $36$:

$$t_1 = \frac{20}{7}\text{ h} = 2\text{ h } + \frac{6}{7}\text{ h}$$

Convertimos $\frac{6}{7}\text{ h}$ a minutos:

$$\frac{6}{7} \times 60 = \frac{360}{7}\text{ min} = 51\text{ min } + \frac{3}{7}\text{ min}$$

Convertimos $\frac{3}{7}\text{ min}$ a segundos:

$$\frac{3}{7} \times 60 = \frac{180}{7}\text{ s} = 25{,}71\text{ s}$$

**Paso 3:** Calcular el tiempo de la etapa terrestre ($t_2$):

$$t_2 = \frac{D_2}{V_{\text{terrestre}}} = \frac{45\text{ km}}{30\text{ km/h}} = 1{,}5\text{ h} = 1\text{ h } 30\text{ min } 00\text{ s}$$

**Paso 4:** Convertir el tiempo de transbordo a horas fraccionarias:

$$t_{\text{transbordo}} = 42\text{ min} = \frac{42}{60}\text{ h} = \frac{7}{10}\text{ h} = 0{,}7\text{ h}$$

**Paso 5:** Sumar el tiempo total de manera exacta en fracciones de hora:

$$T_{\text{total}} = t_1 + t_2 + t_{\text{transbordo}} = \frac{20}{7} + \frac{3}{2} + \frac{7}{10}$$

El mínimo común múltiplo de los denominadores $(7, 2, 10)$ es $70$:

$$T_{\text{total}} = \frac{20 \times 10 + 3 \times 35 + 7 \times 7}{70} = \frac{200 + 105 + 49}{70} = \frac{354}{70} = \frac{177}{35}\text{ h}$$

Dividimos $177$ entre $35$:

$$177 = 5 \times 35 + 2 \implies T_{\text{total}} = 5\text{ h} + \frac{2}{35}\text{ h}$$

Convertimos $\frac{2}{35}\text{ h}$ a minutos:

$$\frac{2}{35} \times 60 = \frac{120}{35}\text{ min} = \frac{24}{7}\text{ min} = 3\text{ min} + \frac{3}{7}\text{ min}$$

Convertimos $\frac{3}{7}\text{ min}$ a segundos:

$$\frac{3}{7} \times 60 = \frac{180}{7}\text{ s} = 25\frac{5}{7}\text{ s} \approx 25{,}71\text{ s}$$

*Respuesta:* El tiempo total de evacuación es de $5\text{ h } 03\text{ min } 25\frac{5}{7}\text{ s}$ (o aproximadamente $5{,}057\text{ h}$).

---

#### Ejercicio 9: Telemetría Satelital y Tiempo de Propagación de Señales Ópticas
Un satélite de observación de la Tierra orbita a una altitud de $630\text{ km}$ sobre la superficie del territorio peruano. Emite un pulso láser hacia una estación terrena en Huancayo que se encuentra a una distancia oblicua de $1\,050\text{ km}$. La velocidad de propagación de la luz en el medio es $c \approx 3 \times 10^8\text{ m/s}$. Calcule el tiempo que tarda el pulso en llegar a la estación expresado en milisegundos ($\text{ms}$) y en microsegundos ($\mu\text{s}$).

**Solución paso a paso:**

**Paso 1:** Convertir la distancia a metros:

$$D = 1\,050\text{ km} \times \frac{1\,000\text{ m}}{1\text{ km}} = 1\,050\,000\text{ m} = 1{,}05 \times 10^6\text{ m}$$

**Paso 2:** Calcular el tiempo en segundos empleando la fórmula del MRU:

$$t = \frac{D}{c} = \frac{1{,}05 \times 10^6\text{ m}}{3 \times 10^8\text{ m/s}} = \frac{1{,}05}{3} \times 10^{6-8}\text{ s} = 0{,}35 \times 10^{-2}\text{ s} = 3{,}5 \times 10^{-3}\text{ s}$$

**Paso 3:** Convertir a milisegundos ($\text{ms}$):
Como $1\text{ ms} = 10^{-3}\text{ s}$:

$$t = 3{,}5 \times 10^{-3}\text{ s} = 3{,}5\text{ ms}$$

**Paso 4:** Convertir a microsegundos ($\mu\text{s}$):
Como $1\text{ ms} = 1\,000\ \mu\text{s}$:

$$t = 3{,}5\text{ ms} \times \frac{1\,000\ \mu\text{s}}{1\text{ ms}} = 3\,500\ \mu\text{s}$$

*Respuesta:* El pulso tarda $3{,}5\text{ ms}$ o $3\,500\ \mu\text{s}$ en alcanzar la estación terrena.

---

#### Ejercicio 10: Riego por Aspersión y Consumo Hídrico en Hectáreas
Un proyecto agroindustrial en las pampas de Majes (Arequipa) posee un sistema de riego por aspersión que suministra una lámina de agua de $8\text{ mm}$ de altura a un lote de $15\text{ hectáreas}$ de palto. Si el agua se bombea desde una represa mediante una tubería principal de la cual sale un caudal constante de $75\text{ L/s}$, ¿cuántas horas, minutos y segundos tardará en completarse el riego del lote?

**Solución paso a paso:**

**Paso 1:** Unificar las dimensiones del lote y la lámina de agua a metros:
* Área regada:

$$A = 15\text{ ha} \times \frac{10\,000\text{ m}^2}{1\text{ ha}} = 150\,000\text{ m}^2 = 1{,}5 \times 10^5\text{ m}^2$$

* Altura de la lámina de agua:

$$h = 8\text{ mm} \times \frac{1\text{ m}}{1\,000\text{ mm}} = 8 \times 10^{-3}\text{ m}$$

**Paso 2:** Calcular el volumen total de agua requerido en metros cúbicos y en litros:

$$V = A \times h = (150\,000\text{ m}^2) \times (0{,}008\text{ m}) = 1\,200\text{ m}^3$$

Convertimos a litros:

$$V = 1\,200\text{ m}^3 \times \frac{1\,000\text{ L}}{1\text{ m}^3} = 1\,200\,000\text{ L} = 1{,}2 \times 10^6\text{ L}$$

**Paso 3:** Calcular el tiempo total de bombeo en segundos:

$$t = \frac{V}{Q} = \frac{1\,200\,000\text{ L}}{75\text{ L/s}} = 16\,000\text{ s}$$

**Paso 4:** Convertir los segundos al sistema sexagesimal (horas, minutos y segundos):
* Dividimos entre $3\,600$ para obtener las horas:

$$16\,000 \div 3\,600 = 4\text{ con residuo } 1\,600\text{ s} \implies 4\text{ h}$$

* Dividimos el residuo $1\,600\text{ s}$ entre $60$ para obtener los minutos:

$$1\,600 \div 60 = 26\text{ con residuo } 40\text{ s} \implies 26\text{ min}$$

* Segundos restantes:

$$40\text{ s}$$

*Respuesta:* El riego completo tardará exactamente $4\text{ horas, } 26\text{ minutos y } 40\text{ segundos}$ ($4{,}\widehat{4}\text{ h}$).

---

## 4. Práctica Propuesta (45 Ejercicios con Claves)

### Bloque I: Nivel Básico (Ejercicios 1 al 15)

1. Una regla graduada de laboratorio mide $30\text{ cm}$. ¿A cuántos micrómetros ($\mu\text{m}$) equivale dicha longitud?
A) $3 \times 10^4\ \mu\text{m}$  
B) $3 \times 10^5\ \mu\text{m}$  
C) $3 \times 10^6\ \mu\text{m}$  
D) $3 \times 10^7\ \mu\text{m}$  
E) $3 \times 10^3\ \mu\text{m}$  

2. Un atleta corre a una rapidez sostenida de $15\text{ m/s}$. ¿Cuál es su rapidez equivalente en kilómetros por hora ($\text{km/h}$)?
A) $45\text{ km/h}$  
B) $50\text{ km/h}$  
C) $54\text{ km/h}$  
D) $60\text{ km/h}$  
E) $48\text{ km/h}$  

3. Un intervalo de tiempo medido por un cronómetro digital marca $2{,}75\text{ horas}$. Al expresarlo en el sistema sexagesimal de horas y minutos, corresponde a:
A) $2\text{ h } 75\text{ min}$  
B) $2\text{ h } 45\text{ min}$  
C) $2\text{ h } 30\text{ min}$  
D) $2\text{ h } 15\text{ min}$  
E) $2\text{ h } 50\text{ min}$  

4. Una cinta métrica registra una longitud de $4{,}2\text{ hectómetros}$ ($\text{hm}$). ¿Cuántos milímetros ($\text{mm}$) representa dicha medida?
A) $42\,000\text{ mm}$  
B) $420\,000\text{ mm}$  
C) $4\,200\,000\text{ mm}$  
D) $4\,200\text{ mm}$  
E) $420\text{ mm}$  

5. ¿Cuántos segundos tiene un día solar completo de 24 horas?
A) $86\,400\text{ s}$  
B) $84\,600\text{ s}$  
C) $1\,440\text{ s}$  
D) $3\,600\text{ s}$  
E) $43\,200\text{ s}$  

6. Un depósito cúbico de agua tiene $1{,}2\text{ m}$ de arista interior. ¿Cuál es su capacidad en litros?
A) $1\,200\text{ L}$  
B) $1\,440\text{ L}$  
C) $1\,728\text{ L}$  
D) $17\,280\text{ L}$  
E) $172{,}8\text{ L}$  

7. Se tienen tres varillas de hierro cuyas longitudes son: $L_1 = 2{,}4\text{ m}$, $L_2 = 180\text{ cm}$ y $L_3 = 650\text{ mm}$. ¿Cuál es la longitud total de las tres varillas unidas en decímetros ($\text{dm}$)?
A) $48{,}5\text{ dm}$  
B) $485\text{ dm}$  
C) $4{,}85\text{ dm}$  
D) $42\text{ dm}$  
E) $50\text{ dm}$  

8. Un automóvil recorre una distancia de $120\text{ km}$ en $1\text{ hora y } 36\text{ minutos}$. ¿Cuál fue su velocidad media en $\text{km/h}$?
A) $70\text{ km/h}$  
B) $75\text{ km/h}$  
C) $80\text{ km/h}$  
D) $85\text{ km/h}$  
E) $65\text{ km/h}$  

9. Exprese el ángulo horario de $3\text{ horas, } 18\text{ minutos y } 36\text{ segundos}$ en horas decimales exactas:
A) $3{,}31\text{ h}$  
B) $3{,}186\text{ h}$  
C) $3{,}305\text{ h}$  
D) $3{,}31\text{ h}$  
E) $3{,}31\text{ h}$  

10. Un terreno rectangular mide $25\text{ m}$ de frente por $40\text{ m}$ de fondo. ¿A cuántas áreas ($\text{a}$) equivale su superficie? ($1\text{ a} = 100\text{ m}^2$).
A) $1\text{ a}$  
B) $10\text{ a}$  
C) $100\text{ a}$  
D) $0{,}1\text{ a}$  
E) $1\,000\text{ a}$  

11. Un disco duro de computadora transfiere datos a una tasa de $150\text{ megabytes por segundo}$ ($150\text{ MB/s}$). ¿Cuántos gigabytes ($\text{GB}$) transfiere en $1\text{ minuto}$? (Considere $1\text{ GB} = 1\,000\text{ MB}$).
A) $6\text{ GB}$  
B) $9\text{ GB}$  
C) $12\text{ GB}$  
D) $15\text{ GB}$  
E) $18\text{ GB}$  

12. ¿A cuántos centímetros cúbicos ($\text{cm}^3$) equivalen $0{,}045\text{ metros cúbicos}$ ($\text{m}^3$)?
A) $450\text{ cm}^3$  
B) $4\,500\text{ cm}^3$  
C) $45\,000\text{ cm}^3$  
D) $450\,000\text{ cm}^3$  
E) $45\text{ cm}^3$  

13. Una bacteria mide aproximadamente $2{,}5\ \mu\text{m}$ de longitud. ¿Cuántas bacterias colocadas una tras otra en línea recta se necesitarían para cubrir una longitud de $1\text{ centímetro}$?
A) $4\,000$  
B) $40\,000$  
C) $400\,000$  
D) $400$  
E) $4 \times 10^6$  

14. Un tanque cilíndrico pierde agua por una fisura a razón de $25\text{ mL por minuto}$. ¿Cuántos litros se habrán perdido al cabo de $2\text{ días}$ continuos?
A) $36\text{ L}$  
B) $48\text{ L}$  
C) $72\text{ L}$  
D) $60\text{ L}$  
E) $84\text{ L}$  

15. Si un rayo de luz viaja a $300\,000\text{ km/s}$, ¿cuántos kilómetros recorre en un lapso de $1\text{ nanosegundo}$ ($1\text{ ns} = 10^{-9}\text{ s}$)?
A) $3 \times 10^{-4}\text{ km}$  
B) $3 \times 10^{-3}\text{ km}$  
C) $3 \times 10^{-1}\text{ km}$  
D) $3 \times 10^{-6}\text{ km}$  
E) $3 \times 10^{-7}\text{ km}$  

---

### Bloque II: Nivel Intermedio (Ejercicios 16 al 30)

16. Un túnel ferroviario en la sierra central tiene una longitud de $3{,}8\text{ km}$. Un tren de $200\text{ m}$ de largo ingresa al túnel a una velocidad constante de $72\text{ km/h}$. ¿Cuántos minutos tarda el tren desde que la locomotora entra al túnel hasta que el último vagón sale completamente de él?
A) $3\text{ min } 15\text{ s}$  
B) $3\text{ min } 20\text{ s}$  
C) $3\text{ min } 30\text{ s}$  
D) $3\text{ min } 45\text{ s}$  
E) $4\text{ min } 00\text{ s}$  

17. Un agricultor divide una parcela de $4{,}5\text{ hectáreas}$ en lotes iguales de $250\text{ m}^2$ para construir módulos hidropónicos. Si destina el $20\%$ del área total a caminos de acceso y canales, ¿cuántos lotes útiles se obtienen?
A) $120$  
B) $135$  
C) $144$  
D) $150$  
E) $160$  

18. Un ciclista recorre tres etapas en una competencia: la primera etapa de $45\text{ km}$ a $30\text{ km/h}$; la segunda de $36\text{ km}$ a $24\text{ km/h}$; y la tercera de $18\text{ km}$ a $18\text{ km/h}$. ¿Cuál fue su velocidad media para todo el recorrido?
A) $23{,}5\text{ km/h}$  
B) $24{,}75\text{ km/h}$  
C) $25{,}0\text{ km/h}$  
D) $24{,}0\text{ km/h}$  
E) $26{,}2\text{ km/h}$  

19. Una piscina municipal de $25\text{ m}$ de largo, $12\text{ m}$ de ancho y $1{,}8\text{ m}$ de profundidad media se vacía mediante un sistema de motobombas que extrae un caudal constante de $45\text{ m}^3\text{/h}$. ¿Cuánto tiempo (en horas y minutos) tarda en vaciarse totalmente?
A) $10\text{ h } 48\text{ min}$  
B) $11\text{ h } 15\text{ min}$  
C) $12\text{ h } 00\text{ min}$  
D) $12\text{ h } 30\text{ min}$  
E) $11\text{ h } 40\text{ min}$  

20. En un plano catastral elaborado a escala $1:5\,000$, un bosque comunal está representado por un trapecio de bases $6\text{ cm}$ y $10\text{ cm}$, con una altura de $4\text{ cm}$. ¿Cuál es el área real del bosque expresada en hectáreas ($\text{ha}$)?
A) $4\text{ ha}$  
B) $8\text{ ha}$  
C) $10\text{ ha}$  
D) $12\text{ ha}$  
E) $16\text{ ha}$  

21. Una impresora 3D industrial utiliza un filamento cilíndrico de $1{,}75\text{ mm}$ de diámetro. Si en una jornada continua consume $80\text{ metros}$ de dicho filamento, ¿cuál es el volumen aproximado de plástico utilizado en centímetros cúbicos ($\text{cm}^3$)? (Considere $\pi \approx 3{,}1416$).
A) $185{,}2\text{ cm}^3$  
B) $192{,}4\text{ cm}^3$  
C) $201{,}8\text{ cm}^3$  
D) $210{,}5\text{ cm}^3$  
E) $198{,}6\text{ cm}^3$  

22. Un satélite meteorológico toma una fotografía de alta resolución cada $18\text{ milisegundos}$ ($\text{ms}$). Si cada imagen tiene un peso digital comprimido de $4{,}5\text{ megabytes}$ ($\text{MB}$), ¿cuántos gigabytes ($\text{GB}$) de almacenamiento ocupa la información recabada en $3\text{ minutos}$ continuos de escaneo? ($1\text{ GB} = 1\,000\text{ MB}$).
A) $35\text{ GB}$  
B) $45\text{ GB}$  
C) $50\text{ GB}$  
D) $40\text{ GB}$  
E) $60\text{ GB}$  

23. Dos trenes $A$ y $B$ parten simultáneamente al encuentro desde dos ciudades distantes $360\text{ km}$ a través de una vía rectilínea. El tren $A$ viaja a $75\text{ km/h}$ y el tren $B$ a $25\text{ m/s}$. ¿Al cabo de cuánto tiempo (en horas y minutos) se produce el cruce?
A) $2\text{ h } 00\text{ min}$  
B) $2\text{ h } 10\text{ min}$  
C) $2\text{ h } 15\text{ min}$  
D) $2\text{ h } 24\text{ min}$  
E) $2\text{ h } 30\text{ min}$  

24. Un automóvil tiene un consumo de combustible de $8{,}5\text{ litros por cada } 100\text{ kilómetros}$. Si el galón peruano equivale a $3{,}785\text{ litros}$, ¿cuántos kilómetros por galón ($\text{km/gal}$) rinde el vehículo?
A) $42{,}3\text{ km/gal}$  
B) $44{,}5\text{ km/gal}$  
C) $46{,}2\text{ km/gal}$  
D) $48{,}1\text{ km/gal}$  
E) $40{,}8\text{ km/gal}$  

25. Un grifo de jardín vierte $0{,}25\text{ litros por segundo}$ en un tanque cúbico abierto de $80\text{ cm}$ de arista interior. Si el fondo del tanque presenta un orificio de drenaje que desaloja $3\text{ litros por minuto}$, ¿cuánto tiempo tardará el tanque en llenarse desde su estado vacío?
A) $32\text{ min } 40\text{ s}$  
B) $38\text{ min } 24\text{ s}$  
C) $42\text{ min } 40\text{ s}$  
D) $45\text{ min } 00\text{ s}$  
E) $35\text{ min } 30\text{ s}$  

26. Se mide el espesor de una pila de $500$ hojas de papel bond idénticas con un micrómetro digital, obteniéndose $4{,}75\text{ cm}$. ¿Cuál es el espesor de una sola hoja expresado en micrómetros ($\mu\text{m}$)?
A) $95\ \mu\text{m}$  
B) $85\ \mu\text{m}$  
C) $90\ \mu\text{m}$  
D) $105\ \mu\text{m}$  
E) $75\ \mu\text{m}$  

27. Un camión cisterna con capacidad de $15\text{ m}^3$ de agua potable abastece bidones familiares de $60\text{ litros}$. Si el tiempo promedio para llenar cada bidón y cambiar de posición al siguiente usuario es de $1\text{ minuto y } 36\text{ segundos}$, ¿cuántas horas continuas de labor ininterrumpida requiere la distribución de toda la carga?
A) $6\text{ h } 15\text{ min}$  
B) $6\text{ h } 40\text{ min}$  
C) $7\text{ h } 00\text{ min}$  
D) $7\text{ h } 20\text{ min}$  
E) $6\text{ h } 00\text{ min}$  

28. Un reloj analógico adelanta $3\text{ minutos cada } 8\text{ horas}$. Si se sincroniza con la hora oficial a las 6:00 a.m. del día lunes, ¿qué hora marcará este reloj a las 6:00 p.m. del día jueves de esa misma semana?
A) 6:27 p.m.  
B) 6:31 p.m.  
C) 6:31 p.m. y $30\text{ s}$  
D) 6:33 p.m.  
E) 6:35 p.m.  

29. Una tubería de desagüe de sección circular tiene un radio interior de $10\text{ cm}$. Si el agua residual fluye a una velocidad de $1{,}5\text{ m/s}$ ocupando la mitad de la sección de la tubería, ¿cuál es el caudal desalojado en litros por segundo ($\text{L/s}$)? (Considere $\pi \approx 3{,}1416$).
A) $21{,}8\text{ L/s}$  
B) $23{,}56\text{ L/s}$  
C) $25{,}12\text{ L/s}$  
D) $27{,}4\text{ L/s}$  
E) $18{,}9\text{ L/s}$  

30. Se vierte mercurio líquido (densidad $\rho = 13{,}6\text{ g/cm}^3$) en un recipiente cilíndrico graduado hasta alcanzar una altura de $15\text{ cm}$. Si el radio de la base interior es de $4\text{ cm}$, determine la masa total de mercurio en kilogramos ($\text{kg}$). (Considere $\pi \approx 3{,}1416$).
A) $9{,}85\text{ kg}$  
B) $10{,}26\text{ kg}$  
C) $10{,}50\text{ kg}$  
D) $11{,}12\text{ kg}$  
E) $8{,}95\text{ kg}$  

---

### Bloque III: Nivel Avanzado / Contexto Beca 18 (Ejercicios 31 al 45)

31. Un canal de regadío trapezoidal en Lambayeque tiene un ancho basal de $1{,}8\text{ m}$, taludes laterales a $45^\circ$ y una profundidad de lámina de agua de $1{,}2\text{ m}$. Si el agua avanza a una velocidad de $0{,}85\text{ m/s}$, ¿cuántos metros cúbicos por hora ($\text{m}^3\text{/h}$) de caudal transporta dicho canal?
A) $10\,450\text{ m}^3\text{/h}$  
B) $11\,016\text{ m}^3\text{/h}$  
C) $11\,250\text{ m}^3\text{/h}$  
D) $12\,100\text{ m}^3\text{/h}$  
E) $9\,860\text{ m}^3\text{/h}$  

32. En un experimento de física nuclear en el reactor RP-10 de Huarangal (Lima), se detecta un flujo de neutrones térmicos que viajan a una velocidad media de $2\,200\text{ m/s}$. ¿Cuántos picosegundos ($\text{ps}$) tarda un neutrón térmico en atravesar una lámina de blindaje de cadmio de $0{,}44\text{ mm}$ de espesor?
A) $2 \times 10^5\text{ ps}$  
B) $2 \times 10^6\text{ ps}$  
C) $2 \times 10^8\text{ ps}$  
D) $2 \times 10^7\text{ ps}$  
E) $2 \times 10^9\text{ ps}$  

33. Un convoy humanitario con ayuda para comunidades afectadas por heladas en Puno debe trasladar $180\text{ toneladas}$ de víveres a través de una ruta de $240\text{ km}$. La ruta comprende un primer tramo de trocha afirmada ($40\%$ del trayecto) donde la velocidad máxima es de $24\text{ km/h}$, y un segundo tramo asfaltado donde la velocidad es de $60\text{ km/h}$. Si el convoy consume combustible a razón de $1{,}2\text{ L/km}$ en trocha y $0{,}75\text{ L/km}$ en asfalto, y realiza una parada técnica de $45\text{ minutos}$ en el empalme, calcule el tiempo total de traslado (en horas y minutos) y el volumen total de combustible consumido en galones ($1\text{ gal} = 3{,}785\text{ L}$).
A) $6\text{ h } 45\text{ min} \;;\; 58{,}9\text{ gal}$  
B) $7\text{ h } 09\text{ min} \;;\; 58{,}9\text{ gal}$  
C) $7\text{ h } 09\text{ min} \;;\; 59{,}0\text{ gal}$  
D) $7\text{ h } 09\text{ min} \;;\; 59{,}0\text{ gal}$  
E) $7\text{ h } 09\text{ min} \;;\; 59{,}0\text{ gal}$  

34. Una represa hidroeléctrica en la cuenca del Mantaro tiene un espejo de agua de $4{,}2\text{ km}^2$. Durante el estiaje, la evaporación superficial reduce la cota a razón de $3{,}5\text{ mm}$ diarios, mientras que las compuertas de fondo evacúan un caudal ecológico constante de $150\text{ L/s}$. Si las precipitaciones y afluentes aportan un caudal promedio de solo $50\text{ L/s}$, ¿cuántos metros cúbicos de agua pierde la represa en un lapso de $30\text{ días}$ comerciales?
A) $699\,600\text{ m}^3$  
B) $700\,200\text{ m}^3$  
C) $712\,800\text{ m}^3$  
D) $725\,400\text{ m}^3$  
E) $685\,000\text{ m}^3$  

35. Un microcontrolador en un sistema de aviónica aeroespacial opera con un ciclo de reloj de $16\text{ nanosegundos}$ ($16\text{ ns}$). Si una rutina de control de navegación requiere procesar $12{,}5 \times 10^6$ ciclos continuos de reloj, ¿cuántos milisegundos ($\text{ms}$) tarda dicha rutina en ejecutarse?
A) $100\text{ ms}$  
B) $150\text{ ms}$  
C) $200\text{ ms}$  
D) $250\text{ ms}$  
E) $300\text{ ms}$  

36. En una planta de tratamiento de aguas residuales en Iquitos, se desinfecta un flujo continuo de agua residual que ingresa a razón de $180\text{ m}^3\text{/h}$ mediante la inyección automatizada de hipoclorito de sodio a una concentración de $4{,}5\text{ mg por cada litro}$. Si la solución comercial concentrada tiene una densidad de $1{,}2\text{ g/cm}^3$ y contiene un $12\%$ de cloro activo en masa, ¿cuántos litros de solución concentrada se consumen al cabo de una semana continua de operación ($7\text{ días}$)?
A) $787{,}5\text{ L}$  
B) $945\text{ L}$  
C) $1\,050\text{ L}$  
D) $1\,125\text{ L}$  
E) $850\text{ L}$  

37. La sonda espacial New Horizons se encuentra a una distancia de la Tierra de $54\text{ Unidades Astronómicas}$ ($\text{UA}$). Si $1\text{ UA} \approx 1{,}496 \times 10^8\text{ km}$ y las ondas de radio viajan a la velocidad de la luz en el vacío ($c \approx 3 \times 10^5\text{ km/s}$), ¿cuánto tiempo tarda una señal de telemetría en llegar a la estación terrena? Exprese el resultado en horas, minutos y segundos exactos.
A) $7\text{ h } 15\text{ min } 34\text{ s}$  
B) $7\text{ h } 28\text{ min } 53\text{ s}$  
C) $7\text{ h } 42\text{ min } 12\text{ s}$  
D) $8\text{ h } 01\text{ min } 25\text{ s}$  
E) $6\text{ h } 58\text{ min } 40\text{ s}$  

38. Una máquina tuneladora en la Línea 2 del Metro de Lima perfora a un ritmo sostenido de $12\text{ milímetros por minuto}$. Si la máquina trabaja en turnos ininterrumpidos durante $25\text{ días}$, ¿cuántos metros lineales de túnel habrá perforado al culminar dicho periodo?
A) $360\text{ m}$  
B) $432\text{ m}$  
C) $504\text{ m}$  
D) $520\text{ m}$  
E) $480\text{ m}$  

39. Un terreno de forma poligonal irregular en Cajamarca tiene un perímetro de $1{,}75\text{ km}$. Se desea cercar con $4$ líneas de alambre de púas sostenidas por postes de eucalipto colocados cada $2{,}5\text{ metros}$. Si cada rollo de alambre de púas tiene una longitud de $400\text{ metros}$ y se desperdicia un $5\%$ en amarres y empalmes, ¿cuántos rollos de alambre y cuántos postes como mínimo se deben comprar?
A) $18\text{ rollos y } 700\text{ postes}$  
B) $19\text{ rollos y } 701\text{ postes}$  
C) $19\text{ rollos y } 700\text{ postes}$  
D) $20\text{ rollos y } 701\text{ postes}$  
E) $18\text{ rollos y } 701\text{ postes}$  

40. Un proyectil balístico experimental lanzado verticalmente hacia arriba alcanza una altitud de apogeo de $45\text{ km}$. Durante los primeros $15\text{ segundos}$ de vuelo asciende con aceleración constante de $40\text{ m/s}^2$ a partir del reposo, momento en el cual se apaga el motor y continúa en ascenso libre frenado por la gravedad ($g = 9{,}8\text{ m/s}^2$). ¿Cuál es la velocidad del proyectil (en $\text{km/h}$) al momento exacto en que se apagan sus motores?
A) $1\,800\text{ km/h}$  
B) $2\,160\text{ km/h}$  
C) $2\,400\text{ km/h}$  
D) $2\,520\text{ km/h}$  
E) $1\,980\text{ km/h}$  

41. Un sistema de purificación por ósmosis inversa procesa agua de mar desalinizada produciendo $250\text{ mililitros por segundo}$ de agua apta para consumo humano. ¿Cuántos metros cúbicos ($\text{m}^3$) de agua pura producirá la planta durante el mes de febrero en un año bisiesto si opera $20\text{ horas}$ diarias?
A) $522\text{ m}^3$  
B) $540\text{ m}^3$  
C) $604{,}8\text{ m}^3$  
D) $580\text{ m}^3$  
E) $626{,}4\text{ m}^3$  

42. Un transformador eléctrico trifásico en una subestación de alta tensión en Huancayo pierde energía en forma de calor a razón de $15\text{ kilovatios}$ ($15\text{ kW} = 15\,000\text{ J/s}$). Para refrigerarlo, se hace circular aceite dieléctrico (calor específico $c_e = 2\,000\text{ J/(kg}\cdot^\circ\text{C)}$ y densidad $\rho = 850\text{ kg/m}^3$). Si el aceite no debe elevar su temperatura en más de $10^\circ\text{C}$, ¿cuál debe ser el caudal mínimo de circulación en litros por minuto ($\text{L/min}$)?
A) $45\text{ L/min}$  
B) $52{,}94\text{ L/min}$  
C) $60\text{ L/min}$  
D) $65{,}5\text{ L/min}$  
E) $48{,}2\text{ L/min}$  

43. Dos satélites geoestacionarios $S_1$ y $S_2$ orbitan sobre el ecuador terrestre separados por una distancia en línea recta de $12\,600\text{ km}$. Una estación terrena ubicada exactamente en el punto medio geodésico recibe señales emitidas por ambos satélites. Si el reloj atómico de $S_1$ presenta un adelanto temporal acumulado de $45\text{ microsegundos}$ respecto a $S_2$, ¿qué distancia espacial habrá recorrido la onda electromagnética de $S_1$ adicional a la de $S_2$ durante ese desfase? ($c = 3 \times 10^8\text{ m/s}$).
A) $13{,}5\text{ km}$  
B) $15\text{ km}$  
C) $12\text{ km}$  
D) $18\text{ km}$  
E) $10{,}5\text{ km}$  

44. Una viga de acero estructural para un puente en la selva central de $18\text{ metros}$ de longitud a $10^\circ\text{C}$ experimenta una dilatación térmica lineal de $\Delta L = \alpha \cdot L_0 \cdot \Delta T$. Si el coeficiente de dilatación del acero es $\alpha = 1{,}2 \times 10^{-5}\ ^\circ\text{C}^{-1}$ y la temperatura máxima al mediodía alcanza los $38^\circ\text{C}$, ¿cuántos milímetros ($\text{mm}$) se expande la viga?
A) $5{,}04\text{ mm}$  
B) $6{,}05\text{ mm}$  
C) $4{,}85\text{ mm}$  
D) $7{,}12\text{ mm}$  
E) $6{,}48\text{ mm}$  

45. En un ensayo geomecánico de permeabilidad hidráulica de suelos en el valle de Urubamba, se hace pasar agua a través de una probeta cilíndrica de suelo de $10\text{ cm}$ de diámetro y $15\text{ cm}$ de longitud bajo una carga hidráulica constante. Si se recolectan $785\text{ cm}^3$ de agua en un tiempo de $1\text{ hora y } 40\text{ minutos}$, ¿cuál es la velocidad de descarga aparente del agua a través del suelo expresada en micrómetros por segundo ($\mu\text{m/s}$)? (Considere $\pi \approx 3{,}1416$).
A) $16{,}67\ \mu\text{m/s}$  
B) $18{,}25\ \mu\text{m/s}$  
C) $20{,}0\ \mu\text{m/s}$  
D) $22{,}5\ \mu\text{m/s}$  
E) $15{,}0\ \mu\text{m/s}$  

---

## 5. Tabla de Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | B | **31** | B |
| **2** | C | **17** | C | **32** | C |
| **3** | B | **18** | D | **33** | C |
| **4** | B | **19** | C | **34** | A |
| **5** | A | **20** | A | **35** | C |
| **6** | C | **21** | B | **36** | B |
| **7** | A | **22** | B | **37** | B |
| **8** | B | **23** | D | **38** | B |
| **9** | D | **24** | B | **39** | C |
| **10** | B | **25** | C | **40** | B |
| **11** | B | **26** | A | **41** | E |
| **12** | C | **27** | B | **42** | B |
| **13** | A | **28** | C | **43** | A |
| **14** | C | **29** | B | **44** | B |
| **15** | A | **30** | B | **45** | A |

---

## 6. Pistas y Orientación Metodológica

Orientaciones analíticas para los cinco problemas más desafiantes del Bloque III:

* **Pista para el Ejercicio 33:**
Descomponga el trayecto en dos tramos independientes. En el tramo 1, $D_1 = 0{,}40 \times 240\text{ km} = 96\text{ km}$; calcule el tiempo con $V_1 = 24\text{ km/h}$ y el combustible con $1{,}2\text{ L/km}$. En el tramo 2, $D_2 = 144\text{ km}$; calcule el tiempo con $V_2 = 60\text{ km/h}$ y el combustible con $0{,}75\text{ L/km}$. Sume ambos tiempos junto con la parada de $45\text{ min}$, y convierta la suma total de litros a galones dividiendo entre $3{,}785$.

* **Pista para el Ejercicio 36:**
Calcule el volumen total de agua procesada en una semana: $V = 180\text{ m}^3\text{/h} \times 24\text{ h/d} \times 7\text{ d} \times 1\,000\text{ L/m}^3 = 30\,240\,000\text{ L}$. La masa de cloro requerida es $30\,240\,000\text{ L} \times 4{,}5\text{ mg/L} = 136\,080\,000\text{ mg} = 136{,}08\text{ kg}$. Dado que la solución tiene $12\%$ de cloro activo, la masa total de solución necesaria es $\frac{136{,}08}{0{,}12} = 1\,134\text{ kg}$. Finalmente, divida dicha masa entre la densidad ($\rho = 1{,}2\text{ kg/L}$) para hallar el volumen en litros.

* **Pista para el Ejercicio 40:**
En el movimiento uniformemente variado (MUV), la velocidad final alcanzada desde el reposo se obtiene como $V = a \cdot t = 40\text{ m/s}^2 \times 15\text{ s} = 600\text{ m/s}$. Para transformar esta rapidez a kilómetros por hora, multiplique directamente por el factor de conversión $\frac{18}{5}$, obteniendo $600 \times \frac{18}{5} = 2\,160\text{ km/h}$.

* **Pista para el Ejercicio 42:**
El calor disipado por unidad de tiempo es la potencia calorífica: $P = 15\,000\text{ W} = 15\,000\text{ J/s}$. Aplique la ecuación calorimétrica $P = \dot{m} \cdot c_e \cdot \Delta T$. Despeje el flujo másico: $\dot{m} = \frac{15\,000}{2\,000 \times 10} = 0{,}75\text{ kg/s}$. Con la densidad $\rho = 850\text{ kg/m}^3 = 0{,}85\text{ kg/L}$, el caudal volumétrico es $Q = \frac{\dot{m}}{\rho} = \frac{0{,}75}{0{,}85}\text{ L/s} \approx 0{,}8824\text{ L/s}$. Multiplique por $60\text{ s}$ para obtener litros por minuto.

* **Pista para el Ejercicio 45:**
El área de la sección circular de la probeta es $A = \frac{\pi \cdot D^2}{4} = \frac{\pi \cdot (10\text{ cm})^2}{4} = 25\pi\text{ cm}^2 \approx 78{,}54\text{ cm}^2$. El tiempo en segundos es $t = 1\text{ h } 40\text{ min} = 100\text{ min} = 6\,000\text{ s}$. El caudal es $Q = \frac{785\text{ cm}^3}{6\,000\text{ s}} \approx 0{,}13083\text{ cm}^3\text{/s}$. La velocidad de descarga aparente es $v = \frac{Q}{A} = \frac{785}{6\,000 \times 25\pi} \approx 0{,}0016667\text{ cm/s}$. Finalmente, convierta $\text{cm/s}$ a micrómetros por segundo: $1\text{ cm} = 10\,000\ \mu\text{m}$, lo que resulta en $16{,}67\ \mu\text{m/s}$.

---

## 7. Formulario Resumen

### Prefijos del Sistema Internacional (SI)

| Prefijo | Símbolo | Factor Multiplicador |
| :--- | :---: | :---: |
| **Tera / Giga** | $\text{T / G}$ | $10^{12} \quad / \quad 10^9$ |
| **Mega / Kilo** | $\text{M / k}$ | $10^6 \quad / \quad 10^3$ |
| **Hecto / Deca** | $\text{h / da}$ | $10^2 \quad / \quad 10^1$ |
| **Unidad Base** | — | $10^0 = 1$ |
| **Deci / Centi** | $\text{d / c}$ | $10^{-1} \quad / \quad 10^{-2}$ |
| **Mili / Micro** | $\text{m / } \mu$ | $10^{-3} \quad / \quad 10^{-6}$ |
| **Nano / Pico** | $\text{n / p}$ | $10^{-9} \quad / \quad 10^{-12}$ |

---

### Equivalencias de Longitud, Superficie y Capacidad

| Magnitud | Equivalencias Fundamentales |
| :--- | :--- |
| **Longitud Lineal** | $1\text{ km} = 1\,000\text{ m} = 10^5\text{ cm} = 10^6\text{ mm}$ |
| **Superficie (Área)** | $1\text{ m}^2 = 10^4\text{ cm}^2 = 10^6\text{ mm}^2 \quad \mid \quad 1\text{ km}^2 = 10^6\text{ m}^2$ |
| **Unidades Agrarias** | $1\text{ ha} = 10\,000\text{ m}^2 = 1\text{ hm}^2 \quad \mid \quad 1\text{ a} = 100\text{ m}^2 = 1\text{ dam}^2$ |
| **Capacidad y Volumen** | $1\text{ m}^3 = 1\,000\text{ L} = 10^6\text{ cm}^3 \quad \mid \quad 1\text{ L} = 1\text{ dm}^3 = 1\,000\text{ mL} = 1\,000\text{ cm}^3$ |

---

### Sistema de Tiempo y Magnitudes Derivadas

| Concepto | Relación Matemática |
| :--- | :--- |
| **Equivalencias de Tiempo** | $1\text{ día} = 24\text{ h} = 1\,440\text{ min} = 86\,400\text{ s} \quad \mid \quad 1\text{ h} = 60\text{ min} = 3\,600\text{ s}$ |
| **Año Comercial / Común** | $1\text{ año com.} = 360\text{ días} \quad \mid \quad 1\text{ año común} = 365\text{ días} \quad \mid \quad 1\text{ año bis.} = 366\text{ días}$ |
| **Conversión Decimal a Horas** | $H{,}D\text{ h} \implies \text{Minutos} = D \times 60 \quad (0{,}45\text{ h} = 27\text{ min})$ |
| **Factor de Velocidad** | $1\,\frac{\text{km}}{\text{h}} \times \frac{5}{18} = 1\,\frac{\text{m}}{\text{s}} \qquad \iff \qquad 1\,\frac{\text{m}}{\text{s}} \times \frac{18}{5} = 1\,\frac{\text{km}}{\text{h}}$ |
| **Caudal Volumétrico** | $Q = \frac{V}{t} \quad \left(1\,\frac{\text{m}^3}{\text{s}} = 1\,000\,\frac{\text{L}}{\text{s}} = 3\,600\,\frac{\text{m}^3}{\text{h}}\right)$ |
