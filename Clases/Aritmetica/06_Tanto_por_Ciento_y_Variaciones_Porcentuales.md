# Tema 06: Tanto por Ciento y Variaciones Porcentuales

**Área:** Aritmética / Regularidad, Cantidad y Finanzas
**Nivel:** Preuniversitario / Beca 18 (ENP)
**Indicador Oficial:** *Evalúa la validez de afirmaciones vinculadas a la conveniencia o no de determinados aumentos o descuentos porcentuales sucesivos.*

---

## 1. Motivación y Contexto Real

En el comercio moderno, la gestión financiera personal y el análisis de políticas socioeconómicas en el Perú, el tanto por ciento es el lenguaje universal para cuantificar variaciones relativas. Desde la evaluación de ofertas comerciales en tiendas por departamento ("$40\% + 20\%$ adicional con tarjeta"), pasando por el cálculo del Impuesto General a las Ventas ($\text{IGV} = 18\%$), hasta la variación del rendimiento de cosechas agrícolas en los valles costeros tras obras de tecnificación, comprender los porcentajes evita engaños económicos y permite tomar decisiones financieras óptimas.

En el Examen Nacional de Preselección (ENP) de Beca 18 y en los exámenes de admisión de mayor rigor académico (UNI, San Marcos, PUCP), las preguntas de tanto por ciento ponen a prueba la capacidad de evitar falacias aritméticas comunes (como creer que un descuento del $30\%$ seguido de otro del $20\%$ equivale a un $50\%$), dominar el modelamiento comercial (precio fijado, costo, venta, ganancia bruta, ganancia neta) y calcular variaciones porcentuales en magnitudes geométricas compuestas (áreas y volúmenes).

---

## 2. Fundamentación Teórica Rigurosa

### 2.1 Concepto de Tanto por Ciento
El tanto por ciento de un número es la cantidad de partes que se toman de una unidad dividida en $100$ partes iguales. Matemáticamente, el símbolo $\%$ representa el operador fraccionario $\frac{1}{100}$:

$$P\% = \frac{P}{100}$$

El $P$ por ciento de una cantidad $N$ es:

$$P\% \text{ de } N = \frac{P}{100} \cdot N$$

#### Relación Parte - Todo Porcentual
Para determinar qué porcentaje representa una cantidad $P$ (parte) respecto de una cantidad base $T$ (todo):

$$\text{Porcentaje} = \left(\frac{\text{Parte}}{\text{Todo}}\right) \times 100\% = \left(\frac{P}{T}\right) \times 100\%$$

*Regla práctica para identificar términos:*
* La palabra **"de"**, **"del"**, **"respecto de"** antecede al **Todo** (denominador).
* La palabra **"es"**, **"son"**, **"representa"** antecede a la **Parte** (numerador).

### 2.2 Operaciones con Porcentajes de una Misma Cantidad
Los porcentajes referidos a una misma cantidad base $N$ pueden sumarse y restarse algebraicamente:

$$a\% \cdot N + b\% \cdot N = (a + b)\% \cdot N$$

$$a\% \cdot N - b\% \cdot N = (a - b)\% \cdot N$$

$$N \pm a\% \cdot N = 100\% \cdot N \pm a\% \cdot N = (100 \pm a)\% \cdot N$$

*Toda cantidad $N$ representa el $100\%$ de sí misma ($N = 100\% \cdot N$).*

### 2.3 Descuentos Sucesivos y Descuento Único
Cuando una cantidad experimenta dos o más descuentos de manera secuencial, cada rebaja posterior se aplica sobre el saldo que queda tras la rebaja anterior (no sobre la cantidad inicial).

#### A. Método del Saldo Remanente (Recomendado para cualquier número de descuentos):
Si un precio inicial $P_0$ sufre descuentos sucesivos de $d_1\%$, $d_2\%$ y $d_3\%$, lo que se paga finalmente es:

$$P_{\text{final}} = (100 - d_3)\% \cdot (100 - d_2)\% \cdot (100 - d_1)\% \cdot P_0$$

El **Descuento Único Equivalente ($D_u$)** es la diferencia entre el $100\%$ inicial y el porcentaje final pagado:

$$D_u = 100\% - \left[ \frac{(100 - d_1)(100 - d_2)\dots(100 - d_k)}{100^{k-1}} \right]\%$$

#### B. Fórmula para Dos Descuentos Sucesivos:
Para dos descuentos sucesivos del $d_1\%$ y $d_2\%$, el descuento único equivalente es:

$$D_u = \left( d_1 + d_2 - \frac{d_1 \cdot d_2}{100} \right)\%$$

### 2.4 Aumentos Sucesivos y Aumento Único
De manera análoga, si una cantidad sufre aumentos sucesivos, cada incremento se calcula sobre la nueva cantidad acumulada.

#### A. Método del Monto Acumulado:
Si una cantidad $C_0$ experimenta aumentos sucesivos de $a_1\%$, $a_2\%$ y $a_3\%$:

$$C_{\text{final}} = (100 + a_3)\% \cdot (100 + a_2)\% \cdot (100 + a_1)\% \cdot C_0$$

El **Aumento Único Equivalente ($A_u$)** es:

$$A_u = \left[ \frac{(100 + a_1)(100 + a_2)\dots(100 + a_k)}{100^{k-1}} \right]\% - 100\%$$

#### B. Fórmula para Dos Aumentos Sucesivos:
Para dos aumentos sucesivos del $a_1\%$ y $a_2\%$:

$$A_u = \left( a_1 + a_2 + \frac{a_1 \cdot a_2}{100} \right)\%$$

### 2.5 Aplicaciones Comerciales Fundamentales
En las transacciones comerciales intervienen magnitudes claramente tipificadas por la teoría preuniversitaria:

1. **Precio de Costo ($P_c$):** El valor que el comerciante invirtió en adquirir o fabricar el producto.
2. **Precio de Venta ($P_v$):** El importe monetario que efectivamente paga el comprador al comerciante.
3. **Precio de Lista, Fijado o Marcado ($P_f$):** El precio exhibido en vitrina antes de otorgar cualquier descuento.
4. **Ganancia ($G$) o Pérdida ($P$):**
* Si hay ganancia: $P_v = P_c + G$.
* Si hay pérdida: $P_v = P_c - P$.
5. **Rebaja o Descuento Comercial ($D$):**

$$P_v = P_f - D \iff P_f = P_v + D$$

#### Invariantes y Reglas Convencionales de Examen:
* **Regla 1:** Salvo que el enunciado declare explícitamente lo contrario, la **Ganancia ($G$)** o la **Pérdida ($P$)** se calculan siempre como un porcentaje del **Precio de Costo ($P_c$)**:

$$G = g\% \cdot P_c \quad \mid \quad P = p\% \cdot P_c$$

* **Regla 2:** Si el enunciado indica que la ganancia es un porcentaje del precio de venta, se plantea:

$$G = g\% \cdot P_v \implies P_v = P_c + g\% \cdot P_v \implies (100 - g)\% \cdot P_v = P_c$$

* **Regla 3:** El **Descuento o Rebaja ($D$)** se calcula invariablemente sobre el **Precio Fijado o de Lista ($P_f$)**:

$$D = d\% \cdot P_f \implies P_v = (100 - d)\% \cdot P_f$$

* **Regla 4 (Ganancia Bruta vs. Ganancia Neta):**

$$G_{\text{bruta}} = G_{\text{neta}} + \text{Gastos Operativos}$$

### 2.6 Variaciones Porcentuales en Magnitudes Geométricas
Para determinar cómo varía porcentualmente el área o volumen de una figura cuando sus dimensiones lineales cambian en ciertos porcentajes, se utiliza el **método del producto de factores**:

1. Se ignora toda constante numérica multiplicativa fija (como $\pi$, $\frac{1}{2}$, $\frac{4}{3}$).
2. Se reemplaza cada dimensión por su factor final porcentual respecto al $100\%$.
3. Se calcula el producto final y se compara respecto al $100\%$ base.

*Ejemplo:* Si el radio de un círculo aumenta en $20\%$, ¿en qué porcentaje varía su área?
* Fórmula: $A = \pi \cdot r^2 \implies \text{Dependencia: } r^2$.
* Factor de $r$: $100\% + 20\% = 120\% = \frac{120}{100} = 1{,}2$.
* Factor de área: $(1{,}2)^2 = 1{,}44 = 144\%$.
* Variación porcentual: $144\% - 100\% = +44\%$ (aumenta en $44\%$).

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Fijación de Conceptos)

#### Ejercicio 1: Cálculo Porcentual Directo y Relación Parte-Todo
En un colegio preuniversitario con $1\,200$ estudiantes matriculados, el $65\%$ son varones. De las mujeres, el $25\%$ postula a carreras de Ingeniería. ¿Cuántas mujeres postulan a carreras distintas de Ingeniería y qué porcentaje del total de estudiantes del colegio representan?

**Solución paso a paso:**

**Paso 1:** Determinar la cantidad de mujeres en el colegio:
Si el $65\%$ son varones, el porcentaje de mujeres es:

$$100\% - 65\% = 35\%$$

$$\text{Mujeres} = 35\% \text{ de } 1\,200 = \frac{35}{100} \cdot 1\,200 = 35 \cdot 12 = 420\text{ mujeres}$$

**Paso 2:** Determinar las mujeres que postulan a carreras distintas de Ingeniería:
Si el $25\%$ postula a Ingeniería, el porcentaje que postula a otras carreras es:

$$100\% - 25\% = 75\%$$

$$\text{Otras carreras} = 75\% \text{ de } 420 = \frac{3}{4} \cdot 420 = 3 \cdot 105 = 315\text{ mujeres}$$

**Paso 3:** Calcular qué porcentaje representan respecto al total del colegio ($1\,200$ estudiantes):

$$\text{Porcentaje} = \left(\frac{315}{1\,200}\right) \times 100\% = \frac{315}{12}\% = 26{,}25\%$$

*Respuesta:* Son $315$ mujeres y representan el $26{,}25\%$ del alumnado total.

---

#### Ejercicio 2: Descuento Único Equivalente
Una tienda de tecnología ofrece por "Ciberday" una laptop con una rebaja del $20\%$, y si el pago se realiza con tarjeta de crédito de la tienda, se otorga un descuento adicional del $15\%$ sobre el saldo. ¿A qué descuento único equivalente corresponde dicha promoción comercial?

**Solución paso a paso:**

**Paso 1:** Analizar el saldo remanente que se paga tras cada descuento:
* Con el primer descuento del $20\%$, se paga el $100\% - 20\% = 80\%$ del precio original.
* Con el segundo descuento del $15\%$, se paga el $100\% - 15\% = 85\%$ de lo que quedaba.

**Paso 2:** Calcular el porcentaje final que se paga del precio de lista ($P_0$):

$$P_{\text{final}} = 85\% \text{ del } 80\% \text{ de } P_0 = \frac{85}{100} \cdot \frac{80}{100} \cdot P_0 = \frac{85 \cdot 4}{500} \cdot P_0 = \frac{340}{500} \cdot P_0 = \frac{68}{100} \cdot P_0 = 68\% \cdot P_0$$

**Paso 3:** Determinar el descuento único equivalente ($D_u$):

$$D_u = 100\% - 68\% = 32\%$$

*(Verificación directa por fórmula de dos descuentos):*

$$D_u = 20 + 15 - \frac{20 \cdot 15}{100} = 35 - \frac{300}{100} = 35 - 3 = 32\%$$

*Respuesta:* La promoción equivale a un descuento único del $32\%$.

---

#### Ejercicio 3: Aplicación Comercial Básica con Ganancia
Un comerciante del emporio de Gamarra compra un lote de pantalones de mezclilla a $\text{S/ } 60$ cada uno. ¿A qué precio debe vender cada pantalón para ganar el $25\%$ del costo sabiendo que los gastos de flete representan $\text{S/ } 5$ por unidad?

**Solución paso a paso:**

**Paso 1:** Identificar el costo total unitario ($P_c$):
El costo unitario comprende la adquisición más los gastos de flete asociados a la mercadería:

$$P_c = \text{S/ } 60 + \text{S/ } 5 = \text{S/ } 65$$

**Paso 2:** Calcular la ganancia monetaria requerida ($G$):
La ganancia es el $25\%$ del costo total:

$$G = 25\% \cdot P_c = \frac{1}{4} \cdot 65 = \text{S/ } 16{,}25$$

**Paso 3:** Calcular el precio de venta ($P_v$):

$$P_v = P_c + G = 65 + 16{,}25 = \text{S/ } 81{,}25$$

*Respuesta:* Debe vender cada pantalón a $\text{S/ } 81{,}25$.

---

### Bloque B: Nivel Intermedio (Operatividad y Modelamiento)

#### Ejercicio 4: Precio Fijado con Descuento y Ganancia Simultáneos
Un importador de instrumentos topográficos fija el precio de un teodolito de modo que, al hacer un descuento del $20\%$ al comprador, aún gana el $30\%$ de lo que le costó. Si el teodolito le costó $\text{S/ } 2\,400$, ¿cuál fue el precio fijado para la venta en vitrina?

**Solución paso a paso:**

**Paso 1:** Identificar datos conocidos:
* Precio de costo: $P_c = \text{S/ } 2\,400$.
* Ganancia: $G = 30\% \cdot P_c = \frac{30}{100} \cdot 2\,400 = \text{S/ } 720$.
* Descuento ofrecido: $D = 20\% \cdot P_f$.

**Paso 2:** Calcular el precio de venta real efectivo ($P_v$):

$$P_v = P_c + G = 2\,400 + 720 = \text{S/ } 3\,120$$

*(Alternativamente: $P_v = 130\% \cdot P_c = 1{,}3 \cdot 2\,400 = \text{S/ } 3\,120$).*

**Paso 3:** Relacionar el precio de venta con el precio fijado ($P_f$):
Como se rebajó el $20\%$ del precio fijado:

$$P_v = (100\% - 20\%) \cdot P_f = 80\% \cdot P_f = 0{,}8 \cdot P_f$$

**Paso 4:** Despejar el precio fijado ($P_f$):

$$0{,}8 \cdot P_f = 3\,120 \implies P_f = \frac{3\,120}{0{,}8} = \frac{31\,200}{8} = \text{S/ } 3\,900$$

*Respuesta:* El precio fijado en vitrina fue de $\text{S/ } 3\,900$.

---

#### Ejercicio 5: Variación Porcentual de Superficie Rectangular
En una parcela experimental de espárragos en Ica, el ancho del terreno de cultivo se incrementa en un $25\%$, pero debido a una servidumbre de paso para un canal de regadío, la longitud del terreno disminuye en un $20\%$. ¿En qué porcentaje varía el área total disponible para el cultivo?

**Solución paso a paso:**

**Paso 1:** Plantear la fórmula del área original ($A_0$):
Sea $L$ la longitud y $W$ el ancho original:

$$A_0 = L \cdot W \quad (100\% \text{ del área})$$

**Paso 2:** Expresar las nuevas dimensiones en forma porcentual:
* Nueva longitud: $L' = L - 20\% \cdot L = 80\% \cdot L = 0{,}8 \cdot L$.
* Nuevo ancho: $W' = W + 25\% \cdot W = 125\% \cdot W = 1{,}25 \cdot W$.

**Paso 3:** Calcular la nueva área ($A'$):

$$A' = L' \cdot W' = (0{,}8 \cdot L) \cdot (1{,}25 \cdot W) = (0{,}8 \cdot 1{,}25) \cdot (L \cdot W)$$

Efectuando el producto:

$$0{,}8 \times 1{,}25 = \frac{4}{5} \times \frac{5}{4} = 1$$

$$A' = 1 \cdot (L \cdot W) = A_0$$

**Paso 4:** Comparar respecto al área base:

$$A' = 100\% \cdot A_0$$

Variación: $100\% - 100\% = 0\%$.

*Respuesta:* El área del terreno no varía (permanece exactamente constante).

---

#### Ejercicio 6: Ganancia Sobre el Precio de Venta
Una empresa distribuidora de paneles solares en Arequipa vende un inversor híbrido ganando el $20\%$ del precio de venta. Si el equipo le costó a la empresa $\text{S/ } 3\,600$, determine el monto de la ganancia obtenida.

**Solución paso a paso:**

**Paso 1:** Plantear la relación fundamental con la condición del enunciado:

$$P_v = P_c + G$$

Aquí, la condición explícita es: $G = 20\% \cdot P_v$.

**Paso 2:** Sustituir en la ecuación fundamental:

$$P_v = P_c + 0{,}20 \cdot P_v$$

$$P_v - 0{,}20 \cdot P_v = P_c$$

$$0{,}80 \cdot P_v = P_c \iff 80\% \cdot P_v = P_c$$

**Paso 3:** Calcular el precio de venta ($P_v$):

$$P_v = \frac{P_c}{0{,}80} = \frac{3\,600}{0{,}8} = \text{S/ } 4\,500$$

**Paso 4:** Calcular la ganancia monetaria ($G$):

$$G = 20\% \cdot P_v = 0{,}20 \cdot 4\,500 = \text{S/ } 900$$

*(O también: $G = P_v - P_c = 4\,500 - 3\,600 = \text{S/ } 900$).*

*Respuesta:* La ganancia obtenida fue de $\text{S/ } 900$.

---

#### Ejercicio 7: Pérdida y Ganancia Combinada con Precios de Venta Iguales
Un criador de alpacas de Puno vende dos ejemplares reproductores a $\text{S/ } 2\,400$ cada uno. En el primer ejemplar gana el $20\%$ de su costo, mientras que en el segundo pierde el $20\%$ de su respectivo costo. Determine si en el balance global de la transacción el criador ganó o perdió, y cuánto dinero exactamente.

**Solución paso a paso:**

**Paso 1:** Analizar el primer ejemplar ($P_{v1} = 2\,400$, gana $20\%$ de su costo $C_1$):

$$P_{v1} = C_1 + 20\% \cdot C_1 = 120\% \cdot C_1 = 1{,}2 \cdot C_1$$

$$2\,400 = 1{,}2 \cdot C_1 \implies C_1 = \frac{2\,400}{1{,}2} = \text{S/ } 2\,000$$

Ganancia en el primer animal:

$$G_1 = P_{v1} - C_1 = 2\,400 - 2\,000 = +\text{S/ } 400$$

**Paso 2:** Analizar el segundo ejemplar ($P_{v2} = 2\,400$, pierde $20\%$ de su costo $C_2$):

$$P_{v2} = C_2 - 20\% \cdot C_2 = 80\% \cdot C_2 = 0{,}8 \cdot C_2$$

$$2\,400 = 0{,}8 \cdot C_2 \implies C_2 = \frac{2\,400}{0{,}8} = \text{S/ } 3\,000$$

Pérdida en el segundo animal:

$$P_2 = C_2 - P_{v2} = 3\,000 - 2\,400 = -\text{S/ } 600$$

**Paso 3:** Balance económico global:
* Ingreso total recaudado: $P_{v1} + P_{v2} = 2\,400 + 2\,400 = \text{S/ } 4\,800$.
* Costo total invertido: $C_1 + C_2 = 2\,000 + 3\,000 = \text{S/ } 5\,000$.
* Balance neto:

$$\text{Balance} = 4\,800 - 5\,000 = -\text{S/ } 200$$

*Respuesta:* El criador pierde globalmente $\text{S/ } 200$ (equivalente a una pérdida del $4\%$ sobre el costo total invertido).

---

### Bloque C: Nivel Avanzado / Contexto Beca 18 (Alta Demanda Cognitiva)

#### Ejercicio 8: Optimización de Estrategia Comercial y Descuento en Cascada
Una cooperativa cafetalera de Quillabamba (Cusco) exporta sacos de café especial. Desea fijar el precio de lista de un lote para que, luego de ofrecer a los distribuidores un descuento del $15\%$ por volumen y pagar una comisión bancaria internacional del $5\%$ calculada sobre el precio de venta facturado, obtenga una ganancia neta equivalente al $36\%$ de su costo de producción. Si el costo de producción del lote es de $\$ 40\,000$, determine el precio de lista que debe consignar en la proforma.

**Solución paso a paso:**

**Paso 1:** Desglosar las variables del problema:
* Costo de producción: $P_c = \$ 40\,000$.
* Ganancia neta deseada: $G_n = 36\% \cdot P_c = 0{,}36 \cdot 40\,000 = \$ 14\,400$.
* Comisión bancaria (gasto): $\text{Gasto} = 5\% \cdot P_v = 0{,}05 \cdot P_v$.
* Descuento comercial al distribuidor: $D = 15\% \cdot P_f$.

**Paso 2:** Relacionar la ganancia bruta con la ganancia neta y los gastos:

$$G_{\text{bruta}} = G_n + \text{Gasto} = 14\,400 + 0{,}05 \cdot P_v$$

**Paso 3:** Plantear la ecuación del precio de venta ($P_v$):

$$P_v = P_c + G_{\text{bruta}}$$

$$P_v = 40\,000 + (14\,400 + 0{,}05 \cdot P_v)$$

$$P_v - 0{,}05 \cdot P_v = 54\,400$$

$$0{,}95 \cdot P_v = 54\,400 \implies P_v = \frac{54\,400}{0{,}95} = \frac{54\,400}{\frac{19}{20}} = \frac{54\,400 \cdot 20}{19}$$

Dividiendo $54\,400$ entre $19$ ($54\,400 = 19 \times 2\,863{,}157...$):
Comprobamos: $19 \times 3 = 57$, $54\,400 / 19$:

$$54\,400 = 19 \cdot 2\,863{,}1578... \approx 57\,263{,}16$$

Para mantener exactitud fraccionaria:

$$P_v = \frac{1\,088\,000}{19}$$

**Paso 4:** Relacionar el precio de venta con el precio fijado ($P_f$):
Como se ofrece un descuento del $15\%$:

$$P_v = (100\% - 15\%) \cdot P_f = 85\% \cdot P_f = \frac{17}{20} \cdot P_f$$

Igualamos ambas expresiones para despejar $P_f$:

$$\frac{17}{20} \cdot P_f = \frac{1\,088\,000}{19}$$

$$P_f = \frac{1\,088\,000 \cdot 20}{19 \cdot 17}$$

Notemos que $1\,088$ es divisible entre $17$:

$$1\,088 \div 17 = 64 \implies 1\,088\,000 \div 17 = 64\,000$$

Por lo tanto:

$$P_f = \frac{64\,000 \cdot 20}{19} = \frac{1\,280\,000}{19} \approx \text{USD } 67\,368{,}42$$

*Respuesta:* El precio de lista debe ser de $\frac{1\,280\,000}{19} \approx \text{USD } 67\,368{,}42$.

---

#### Ejercicio 9: Variación de Consumo en Tarifas Eléctricas Dinámicas
En una microempresa de metalmecánica en Huancayo, la tarifa de energía eléctrica industrial se incrementa en un $25\%$ por kilovatio-hora ($\text{kWh}$). El administrador decide optimizar los procesos de corte y soldadura para que el gasto mensual total en electricidad disminuya en un $10\%$. ¿En qué porcentaje debe reducirse el consumo de energía eléctrica de la planta?

**Solución paso a paso:**

**Paso 1:** Establecer la relación del gasto total ($G$):
Sea $P$ el precio unitario del $\text{kWh}$ y $C$ la cantidad de $\text{kWh}$ consumidos:

$$G = P \cdot C \quad (100\% \text{ del gasto original})$$

**Paso 2:** Expresar los nuevos valores tras las variaciones:
* Nuevo precio unitario: $P' = P + 25\% \cdot P = 125\% \cdot P = \frac{5}{4} \cdot P$.
* Nuevo gasto mensual deseado: $G' = G - 10\% \cdot G = 90\% \cdot G = \frac{9}{10} \cdot G$.
* Sea $C'$ el nuevo consumo de energía requerido:

$$G' = P' \cdot C'$$

**Paso 3:** Reemplazar y despejar la relación entre $C'$ y $C$:

$$\frac{9}{10} \cdot (P \cdot C) = \left(\frac{5}{4} \cdot P\right) \cdot C'$$

Cancelamos $P$ en ambos miembros:

$$\frac{9}{10} \cdot C = \frac{5}{4} \cdot C'$$

$$C' = \left(\frac{9}{10} \cdot \frac{4}{5}\right) \cdot C = \frac{36}{50} \cdot C = \frac{72}{100} \cdot C = 72\% \cdot C$$

**Paso 4:** Calcular la variación porcentual de reducción:

$$\text{Reducción} = 100\% - 72\% = 28\%$$

*Respuesta:* El consumo de energía eléctrica debe reducirse en un $28\%$.

---

#### Ejercicio 10: Mezcla de Soluciones Químicas y Concentración Porcentual
En el laboratorio de metalurgia de una universidad en Junín se tienen dos recipientes con ácido sulfúrico diluido. El primer recipiente contiene $40\text{ litros}$ al $30\%$ de concentración en volumen, y el segundo contiene $60\text{ litros}$ al $70\%$ de concentración.
1. Si se mezclan ambos recipientes, ¿cuál es la concentración porcentual resultante?
2. ¿Cuántos litros de agua destilada (al $0\%$ de ácido) deben agregarse a dicha mezcla final para rebajar su concentración hasta un $40\%$ exacto?

**Solución paso a paso:**

**Paso 1:** Calcular el volumen de ácido puro en cada recipiente:
* Recipiente 1: $V_{a1} = 30\% \cdot 40\text{ L} = \frac{30}{100} \cdot 40 = 12\text{ litros de ácido puro}$.
* Recipiente 2: $V_{a2} = 70\% \cdot 60\text{ L} = \frac{70}{100} \cdot 60 = 42\text{ litros de ácido puro}$.

**Paso 2:** Determinar la concentración de la primera mezcla:
* Volumen total de ácido puro: $V_a = 12 + 42 = 54\text{ litros}$.
* Volumen total de la mezcla: $V_T = 40 + 60 = 100\text{ litros}$.
* Concentración porcentual ($C_{\text{mezcla}}$):

$$C_{\text{mezcla}} = \left(\frac{54\text{ L}}{100\text{ L}}\right) \times 100\% = 54\%$$

**Paso 3:** Calcular el volumen de agua ($x$) a añadir para rebajar la concentración al $40\%$:
Al añadir agua destilada, el volumen de ácido puro se mantiene constante en $54\text{ litros}$, mientras que el volumen total se incrementa a $100 + x$:

$$\frac{54}{100 + x} = 40\% = \frac{40}{100} = \frac{2}{5}$$

Multiplicamos en aspa:

$$54 \cdot 5 = 2 \cdot (100 + x)$$

$$270 = 200 + 2x$$

$$2x = 70 \implies x = 35\text{ litros}$$

*Respuesta:* La mezcla inicial queda al $54\%$ de concentración, y se deben agregar $35\text{ litros}$ de agua destilada para rebajarla al $40\%$.

---

## 4. Práctica Propuesta (45 Ejercicios con Claves)

### Bloque I: Nivel Básico (Ejercicios 01 al 15)

1. ¿Cuál es el $15\%$ del $20\%$ de $4\,000$?  
A) $100$  
B) $120$  
C) $140$  
D) $150$  
E) $180$  

2. ¿Qué porcentaje de $850$ representa el número $153$?  
A) $16\%$  
B) $17\%$  
C) $18\%$  
D) $19\%$  
E) $20\%$  

3. Si el $40\%$ de un número $N$ es igual a $180$, ¿cuál es el $75\%$ de dicho número?  
A) $315$  
B) $330$  
C) $337{,}5$  
D) $345$  
E) $350$  

4. En un almacén de alimentos hay $1\,800$ sacos de arroz. Si se venden $540$ sacos, ¿qué porcentaje de los sacos queda en el almacén?  
A) $65\%$  
B) $70\%$  
C) $72\%$  
D) $75\%$  
E) $80\%$  

5. Dos aumentos sucesivos del $10\%$ y del $30\%$ equivalen a un aumento único de:  
A) $40\%$  
B) $41\%$  
C) $42\%$  
D) $43\%$  
E) $44\%$  

6. Dos descuentos sucesivos del $20\%$ y del $20\%$ equivalen a un descuento único de:  
A) $36\%$  
B) $40\%$  
C) $38\%$  
D) $32\%$  
E) $34\%$  

7. Un comerciante vende una casaca a $\text{S/ } 180$, ganando el $20\%$ del precio de costo. ¿Cuánto le costó la casaca?  
A) $\text{S/ } 140$  
B) $\text{S/ } 144$  
C) $\text{S/ } 150$  
D) $\text{S/ } 155$  
E) $\text{S/ } 160$  

8. Un artículo que costó $\text{S/ } 240$ se vendió con una pérdida del $15\%$ sobre el precio de costo. ¿En cuánto se vendió?  
A) $\text{S/ } 200$  
B) $\text{S/ } 204$  
C) $\text{S/ } 210$  
D) $\text{S/ } 216$  
E) $\text{S/ } 220$  

9. En una reunión social el $60\%$ de los asistentes son mujeres. Si hay $48$ varones, ¿cuántas personas hay en total en la reunión?  
A) $100$  
B) $110$  
C) $120$  
D) $130$  
E) $140$  

10. Si el lado de un cuadrado aumenta en un $30\%$, ¿en qué porcentaje aumenta su área?  
A) $60\%$  
B) $69\%$  
C) $70\%$  
D) $72\%$  
E) $65\%$  

11. Si el precio de un galón de gasolina era de $\text{S/ } 16{,}00$ y sube a $\text{S/ } 18{,}40$, ¿cuál fue el porcentaje de incremento?  
A) $12\%$  
B) $13{,}5\%$  
C) $15\%$  
D) $16\%$  
E) $18\%$  

12. ¿Qué porcentaje del $80\%$ del $50\%$ de un número representa el $20\%$ del $60\%$ de la misma cantidad?  
A) $25\%$  
B) $30\%$  
C) $35\%$  
D) $40\%$  
E) $50\%$  

13. Un televisor tiene un precio fijado de $\text{S/ } 1\,500$. Si al momento de pagar en caja se realiza un descuento del $12\%$, ¿cuánto se paga finalmente por el televisor?  
A) $\text{S/ } 1\,300$  
B) $\text{S/ } 1\,320$  
C) $\text{S/ } 1\,350$  
D) $\text{S/ } 1\,380$  
E) $\text{S/ } 1\,280$  

14. Si al vender un teléfono en $\text{S/ } 840$ se pierde el $30\%$ de su costo, ¿cuál fue el precio de costo?  
A) $\text{S/ } 1\,100$  
B) $\text{S/ } 1\,150$  
C) $\text{S/ } 1\,200$  
D) $\text{S/ } 1\,250$  
E) $\text{S/ } 1\,300$  

15. En un examen de selección de $80$ preguntas, un postulante responde correctamente $68$. ¿Qué porcentaje de preguntas no respondió correctamente?  
A) $12\%$  
B) $15\%$  
C) $16\%$  
D) $18\%$  
E) $20\%$  

---

### Bloque II: Nivel Intermedio (Ejercicios 16 al 30)

16. Un comerciante fija el precio de venta de una refrigeradora en $\text{S/ } 2\,800$. Al momento de venderla hace un descuento del $15\%$ sobre el precio fijado y aun así obtiene una ganancia de $\text{S/ } 380$. ¿Cuánto le costó la refrigeradora al comerciante?  
A) $\text{S/ } 1\,900$  
B) $\text{S/ } 1\,950$  
C) $\text{S/ } 2\,000$  
D) $\text{S/ } 2\,050$  
E) $\text{S/ } 2\,100$  

17. Tres descuentos sucesivos del $10\%$, $20\%$ y $25\%$ equivalen exactamente a un único descuento de:  
A) $45\%$  
B) $46\%$  
C) $48\%$  
D) $50\%$  
E) $52\%$  

18. Si la base de un triángulo aumenta en un $20\%$ y su altura disminuye en un $30\%$, ¿en qué porcentaje varía su área?  
A) Aumenta en $10\%$  
B) Disminuye en $10\%$  
C) Disminuye en $16\%$  
D) Aumenta en $14\%$  
E) Disminuye en $14\%$  

19. Un estudiante gasta en una librería el $20\%$ de su propina y luego pierde el $30\%$ de lo que le quedaba en el pasaje. Si finalmente le sobran $\text{S/ } 112$, ¿cuál era el monto inicial de su propina?  
A) $\text{S/ } 180$  
B) $\text{S/ } 200$  
C) $\text{S/ } 220$  
D) $\text{S/ } 240$  
E) $\text{S/ } 250$  

20. Si el precio de un bien disminuye en un $20\%$, ¿en qué porcentaje debe incrementarse el nuevo precio para volver exactamente al precio original?  
A) $20\%$  
B) $22{,}5\%$  
C) $25\%$  
D) $27{,}5\%$  
E) $30\%$  

21. Un lote de mercadería se vende con una ganancia del $25\%$ sobre el precio de venta. ¿Qué porcentaje del precio de costo representa dicha ganancia?  
A) $20\%$  
B) $30\%$  
C) $33{,}\widehat{3}\%$  
D) $35\%$  
E) $40\%$  

22. En una empresa de confecciones, el $45\%$ de los trabajadores son varones y el resto mujeres. Si el $20\%$ de los varones y el $30\%$ de las mujeres asisten a una capacitación de seguridad industrial, ¿qué porcentaje de los trabajadores de la empresa no asiste a la capacitación?  
A) $72{,}5\%$  
B) $73{,}5\%$  
C) $74{,}5\%$  
D) $75{,}5\%$  
E) $76{,}5\%$  

23. Si el radio de una esfera aumenta en un $10\%$, ¿en qué porcentaje se incrementa su volumen?  
A) $30\%$  
B) $31\%$  
C) $33{,}1\%$  
D) $35{,}2\%$  
E) $36\%$  

24. Se mezclan $30\text{ litros}$ de alcohol al $80\%$ con $50\text{ litros}$ de alcohol al $60\%$ y $20\text{ litros}$ de agua pura. ¿Cuál es la concentración alcohólica porcentual de la mezcla resultante?  
A) $50\%$  
B) $52\%$  
C) $54\%$  
D) $56\%$  
E) $58\%$  

25. Un minorista vendió dos cocinas de inducción a $\text{S/ } 1\,440$ cada una. En la primera ganó el $20\%$ de su costo y en la segunda perdió el $20\%$ de su costo. ¿Cuál fue el resultado económico de la operación?  
A) Ganó $\text{S/ } 60$  
B) Perdió $\text{S/ } 60$  
C) No ganó ni perdió  
D) Ganó $\text{S/ } 80$  
E) Perdió $\text{S/ } 120$  

26. En una granja avícola en Huaral, el $40\%$ del total de aves son patos y el resto son pollos. Si se venden el $25\%$ de los patos y el $50\%$ de los pollos, ¿qué porcentaje del número original de aves queda en la granja?  
A) $55\%$  
B) $58\%$  
C) $60\%$  
D) $62\%$  
E) $65\%$  

27. Un terreno rectangular sufre una expropiación que reduce su largo en un $15\%$. ¿En qué porcentaje debe ampliarse su ancho para que su área total aumente en un $19\%$?  
A) $35\%$  
B) $38\%$  
C) $40\%$  
D) $42\%$  
E) $45\%$  

28. Si el valor de las acciones de una empresa sube el lunes un $20\%$, baja el martes un $15\%$ y sube el miércoles un $10\%$, ¿cuál fue la variación porcentual acumulada en los tres días respecto a su valor inicial?  
A) $+12{,}2\%$  
B) $+13{,}5\%$  
C) $+14\%$  
D) $+15\%$  
E) $+10{,}8\%$  

29. Para fijar el precio de venta de una laptop que costó $\text{S/ } 3\,000$, un comerciante aumenta el costo en un $40\%$. Si luego ofrece una rebaja del $20\%$ sobre dicho precio fijado, ¿cuál fue su ganancia real en soles?  
A) $\text{S/ } 320$  
B) $\text{S/ } 340$  
C) $\text{S/ } 360$  
D) $\text{S/ } 380$  
E) $\text{S/ } 400$  

30. ¿En qué porcentaje varía el volumen de un cilindro circular recto si su radio se reduce a la mitad y su altura se cuadruplica?  
A) Aumenta en $50\%$  
B) Disminuye en $50\%$  
C) No varía ($0\%$)  
D) Aumenta en $100\%$  
E) Disminuye en $25\%$  

---

### Bloque III: Nivel Avanzado / Contexto Beca 18 (Ejercicios 31 al 45)

31. Una distribuidora de medicamentos en Lima importa un lote de vacunas con un costo de $\$ 80\,000$. Fija el precio de catálogo de modo que, ofreciendo un descuento comercial del $20\%$ a los hospitales del Estado y pagando un $4\%$ de flete logístico sobre el precio de venta facturado, obtenga una ganancia neta equivalente al $20\%$ del costo total. ¿A cuánto asciende el precio de catálogo fijado?  
A) $\$ 118\,000$  
B) $\$ 120\,000$  
C) $\$ 125\,000$  
D) $\$ 130\,000$  
E) $\$ 135\,000$  

32. Si el precio unitario del cobre en la Bolsa de Metales de Londres sube en un $25\%$, ¿en qué porcentaje debe reducir una empresa minera sus costos operativos para que, manteniendo su margen de ganancia absoluto por tonelada, el precio de venta aumente únicamente en un $10\%$? Asuma que el costo operativo original representaba el $60\%$ del precio de venta original.  
A) $15\%$  
B) $16{,}\widehat{6}\%$  
C) $18\%$  
D) $20\%$  
E) $22{,}5\%$  

33. Una cooperativa de agricultores de quinua en Ayacucho vende el $35\%$ de su cosecha con una ganancia del $20\%$, el $45\%$ del total con una ganancia del $30\%$, y el resto de la cosecha con una pérdida del $10\%$ debido a problemas de humedad en el transporte. ¿Cuál fue el porcentaje de ganancia promedio que obtuvo la cooperativa sobre el costo de toda la cosecha?  
A) $17{,}5\%$  
B) $18{,}5\%$  
C) $19\%$  
D) $19{,}5\%$  
E) $20\%$  

34. En una prueba hidrostática de tanques de combustible esféricos en Talara, el radio interior de un tanque se deforma elásticamente aumentando en un $2\%$. ¿Cuál es la variación porcentual aproximada que experimenta la superficie externa del tanque y su capacidad volumétrica máxima?  
A) Área $+4\%$ y Volumen $+6\%$  
B) Área $+4{,}04\%$ y Volumen $+6{,}12\%$  
C) Área $+2{,}04\%$ y Volumen $+4{,}08\%$  
D) Área $+4{,}04\%$ y Volumen $+8\%$  
E) Área $+2\%$ y Volumen $+6\%$  

35. Un comerciante compró $800$ cuadernos a $\text{S/ } 5$ cada uno. Decide vender una parte ganando el $30\%$ y el resto ganando el $15\%$. Si la ganancia total obtenida fue de $\text{S/ } 980$, ¿cuántos cuadernos vendió con la mayor ganancia?  
A) $480$  
B) $500$  
C) $520$  
D) $540$  
E) $560$  

36. En una planta de desalinización de agua por ósmosis en Moquegua, el agua marina ingresa con una salinidad del $3{,}5\%$ en masa. Tras el primer ciclo de filtración se descarta una salmuera que contiene el $70\%$ de la sal original en una solución al $7\%$ de salinidad. ¿Qué porcentaje del volumen de agua total ingresado se recuperó como agua desalinizada de alta pureza en este ciclo?  
A) $60\%$  
B) $65\%$  
C) $70\%$  
D) $72\%$  
E) $75\%$  

37. Dos recipientes contienen mezclas de alcohol y agua. En el primer recipiente la razón de alcohol a agua es de $3$ a $2$, mientras que en el segundo es de $1$ a $3$. Si se extraen $20\text{ litros}$ del primero y $40\text{ litros}$ del segundo para formar una nueva mezcla en un tercer recipiente, ¿cuál es la concentración alcohólica porcentual de la mezcla resultante?  
A) $33{,}\widehat{3}\%$  
B) $35\%$  
C) $36{,}\widehat{6}\%$  
D) $38\%$  
E) $40\%$  

38. Para incentivar la adquisición de viviendas de interés social mediante el programa Techo Propio, una entidad financiera ofrece un crédito con una tasa de descuento del $10\%$ sobre el saldo de capital si el beneficiario aporta un bono inicial del $20\%$. Si el costo de la vivienda es de $\text{S/ } 120\,000$ y sobre el monto financiado se aplican gastos administrativos del $3\%$, ¿a cuánto asciende el monto final del préstamo financiado?  
A) $\text{S/ } 86\,400$  
B) $\text{S/ } 88\,992$  
C) $\text{S/ } 89\,200$  
D) $\text{S/ } 90\,150$  
E) $\text{S/ } 92\,000$  

39. En un proceso siderúrgico en Chimbote, se mezclan dos lingotes de bronce (aleación de cobre y estaño). El primer lingote pesa $18\text{ kg}$ y contiene un $80\%$ de cobre; el segundo lingote pesa $32\text{ kg}$ y tiene una pureza de cobre del $65\%$. ¿Cuántos kilogramos de estaño puro deben fundirse con esta masa para que la nueva aleación contenga exactamente un $60\%$ de cobre?  
A) $4\text{ kg}$  
B) $6\text{ kg}$  
C) $8\text{ kg}$  
D) $9\text{ kg}$  
E) $10\text{ kg}$  

40. Si el precio fijado de un producto supera en un $60\%$ a su costo de producción, pero al venderse se otorga dos descuentos sucesivos del $10\%$ y del $20\%$, ¿qué porcentaje del precio de costo se gana o pierde en la transacción?  
A) Se gana el $15{,}2\%$  
B) Se gana el $12\%$  
C) Se pierde el $5\%$  
D) Se gana el $18\%$  
E) Ni se gana ni se pierde  

41. En una campaña médica en la selva central, se detecta que el $12\%$ de la población de una comunidad indígena tiene anemia leve y el $8\%$ tiene anemia moderada o severa. Si tras un programa de suplementación nutricional el $75\%$ de los niños con anemia leve y el $50\%$ de los niños con anemia severa superan la condición, ¿qué porcentaje de la población total de la comunidad continúa presentando algún grado de anemia?  
A) $5\%$  
B) $6\%$  
C) $7\%$  
D) $8\%$  
E) $9\%$  

42. Si el volumen de un cono circular recto disminuye en un $28\%$ debido a que su altura se redujo en un $50\%$, ¿en qué porcentaje aumentó el radio de su base?  
A) $15\%$  
B) $18\%$  
C) $20\%$  
D) $22\%$  
E) $25\%$  

43. Una empresa agroindustrial en Piura proyecta una cosecha de mangos para exportación. Por efectos del Fenómeno de El Niño, la producción recolectada cae en un $20\%$, pero debido a la escasez en los mercados internacionales el precio de venta por kilogramo aumenta en un $35\%$. ¿En qué porcentaje variaron los ingresos brutos totales de la empresa respecto a lo proyectado?  
A) Aumentaron en $8\%$  
B) Aumentaron en $10\%$  
C) Disminuyeron en $5\%$  
D) Aumentaron en $15\%$  
E) No variaron ($0\%$)  

44. Un comerciante tiene un capital de $\text{S/ } 50\,000$. Invierte el $60\%$ en la compra de acciones y el resto en fondos mutuos. Al cabo de un año, las acciones sufrieron una pérdida del $12\%$, mientras que los fondos mutuos generaron una ganancia del $18\%$. ¿Cuál fue la tasa de rentabilidad porcentual global que obtuvo sobre su capital total invertido?  
A) Pérdida del $2\%$  
B) Ganancia del $0\%$ (equilibrio)  
C) Ganancia del $1\%$  
D) Ganancia del $2\%$  
E) Pérdida del $1{,}5\%$  

45. En una licitación pública para la pavimentación de una vía rural, una constructora calcula su propuesta económica: Costo de obra $= C$. Para asegurar contingencias y tributos, fija el valor de la oferta de modo que tras otorgar un descuento del $10\%$ a la entidad convocante, aún obtenga una utilidad bruta del $26\%$ sobre el costo de obra. ¿Qué porcentaje del costo de obra representa la diferencia entre el valor fijado en la oferta y el costo original de la obra?  
A) $36\%$  
B) $40\%$  
C) $42\%$  
D) $44\%$  
E) $45\%$  

---

## 5. Tabla de Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | C | **31** | C |
| **2** | C | **17** | B | **32** | B |
| **3** | C | **18** | C | **33** | B |
| **4** | B | **19** | B | **34** | B |
| **5** | D | **20** | C | **35** | C |
| **6** | A | **21** | C | **36** | B |
| **7** | C | **22** | C | **37** | C |
| **8** | B | **23** | C | **38** | B |
| **9** | C | **24** | C | **39** | C |
| **10** | B | **25** | E | **40** | A |
| **11** | C | **26** | C | **41** | C |
| **12** | B | **27** | C | **42** | C |
| **13** | B | **28** | C | **43** | A |
| **14** | C | **29** | C | **44** | B |
| **15** | B | **30** | C | **45** | B |

---

## 6. Pistas y Orientación Metodológica

Orientaciones analíticas para los cinco problemas más desafiantes del Bloque III:

* **Pista para el Ejercicio 31:**
Plantee la cadena de relaciones: $P_v = P_c + G_n + 0{,}04 \cdot P_v \implies 0{,}96 \cdot P_v = 80\,000 + 0{,}20(80\,000) = 96\,000$. Despeje $P_v = \$ 100\,000$. Luego relacione con el catálogo fijado: $P_v = (100\% - 20\%) \cdot P_f \implies 0{,}80 \cdot P_f = 100\,000 \implies P_f = \$ 125\,000$.

* **Pista para el Ejercicio 33:**
Normalice el costo total a $100$ unidades monetarias. El balance de ganancias es:

$$\text{Ganancia total} = 0{,}35(100) \cdot 0{,}20 + 0{,}45(100) \cdot 0{,}30 - 0{,}20(100) \cdot 0{,}10$$

$$\text{Ganancia total} = 7 + 13{,}5 - 2 = 18{,}5$$

Como el costo base fue $100$, el rendimiento promedio es exactamente del $18{,}5\%$.

* **Pista para el Ejercicio 36:**
Sea $100\text{ kg}$ de agua marina con $3{,}5\text{ kg}$ de sal. La salmuera contiene el $70\%$ de esa sal: $0{,}70 \times 3{,}5 = 2{,}45\text{ kg}$ de sal. Como la concentración de la salmuera es al $7\%$, la masa total de salmuera es $\frac{2{,}45}{0{,}07} = 35\text{ kg}$. Por balance de masa total, el agua desalinizada pura recuperada es $100\text{ kg} - 35\text{ kg} = 65\text{ kg}$ ($65\%$).

* **Pista para el Ejercicio 40:**
Sea el costo $P_c = 100$. El precio fijado es $P_f = 160$. Los dos descuentos sucesivos del $10\%$ y $20\%$ dejan como precio de venta:

$$P_v = 0{,}80 \times 0{,}90 \times 160 = 0{,}72 \times 160 = 115{,}2$$

Como el costo inicial fue $100$, la ganancia efectiva es $115{,}2 - 100 = 15{,}2$ sobre el costo ($15{,}2\%$).

* **Pista para el Ejercicio 42:**
El volumen del cono depende de $r^2 \cdot h$. El nuevo volumen es $V' = (1 - 0{,}28)V = 0{,}72V$. La nueva altura es $h' = 0{,}50h$.

$$r'^2 \cdot (0{,}50h) = 0{,}72 \cdot (r^2 \cdot h) \implies r'^2 = \frac{0{,}72}{0{,}50} \cdot r^2 = 1{,}44 \cdot r^2$$

Extrayendo raíz cuadrada: $r' = \sqrt{1{,}44} \cdot r = 1{,}20 \cdot r$, lo que corresponde a un aumento del $20\%$.

---

## 7. Formulario Resumen

### Operaciones Porcentuales y Descuentos Sucesivos

| Concepto | Expresión Matemática |
| :--- | :--- |
| **Operador Porcentual** | $P\% = \frac{P}{100} \implies P\% \text{ de } N = \frac{P}{100} \cdot N$ |
| **Relación Parte - Todo** | $\text{Porcentaje} = \left(\frac{\text{Parte}}{\text{Todo}}\right) \times 100\% = \left(\frac{P}{T}\right) \times 100\%$ |
| **Dos Descuentos Sucesivos** | $D_u = \left(d_1 + d_2 - \frac{d_1 \cdot d_2}{100}\right)\%$ |
| **Dos Aumentos Sucesivos** | $A_u = \left(a_1 + a_2 + \frac{a_1 \cdot a_2}{100}\right)\%$ |
| **Descuentos en Cascada (Saldo)** | $P_{\text{final}} = (100 - d_k)\% \dots (100 - d_1)\% \cdot P_0$ |

---

### Aplicaciones Comerciales

| Magnitud Comercial | Ecuación y Regla Convencional |
| :--- | :--- |
| **Con Ganancia** | $P_v = P_c + G \quad (\text{por defecto: } G = g\% \cdot P_c)$ |
| **Con Pérdida** | $P_v = P_c - P \quad (\text{por defecto: } P = p\% \cdot P_c)$ |
| **Precio Fijado o de Lista** | $P_f = P_v + D \iff P_v = (100 - d)\% \cdot P_f$ |
| **Ganancia Bruta vs. Neta** | $G_{\text{bruta}} = G_{\text{neta}} + \text{Gastos Operativos}$ |
| **Ganancia sobre Venta** | $P_v = P_c + g\% \cdot P_v \implies (100 - g)\% \cdot P_v = P_c$ |

---

### Variaciones Geométricas y Mezclas

| Caso de Aplicación | Algoritmo Óptimo |
| :--- | :--- |
| **Variación de Áreas / Volúmenes** | $A' = (1 \pm \Delta_1)(1 \pm \Delta_2)\dots \cdot A_0 \implies \Delta\% = A' - 100\%$ |
| **Concentración de Mezcla** | $C_m = \left(\frac{V_{a1} \cdot c_1 + V_{a2} \cdot c_2 + \dots}{V_1 + V_2 + \dots}\right)\%$ |
| **Dilución de Solución** | $V_1 \cdot C_1 = V_2 \cdot C_2 \quad (\text{soluto constante})$ |
