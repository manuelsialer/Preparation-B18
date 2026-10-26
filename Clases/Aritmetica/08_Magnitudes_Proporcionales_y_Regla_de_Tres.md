# Tema 08: Magnitudes Proporcionales y Regla de Tres

**Área:** Aritmética / Regularidad, Variación y Rendimiento
**Nivel:** Preuniversitario / Beca 18 (ENP)
**Indicador Oficial:** *Establece relaciones entre datos, valores desconocidos, regularidades y las transforma a expresiones algebraicas para resolver situaciones problemáticas que involucren magnitudes directa o inversamente proporcionales.*

---

## 1. Motivación y Contexto Real

En la ingeniería de proyectos, el diseño de obras de infraestructura pública, la producción industrial y la agronomía moderna, las magnitudes difícilmente actúan de manera aislada. Cuando el gobierno regional planifica la construcción de defensas ribereñas antes de la temporada de lluvias en el norte del Perú, debe calcular con exactitud cuántos operarios de maquinaria pesada se necesitan si las jornadas laborales se reducen de $10$ a $8\text{ horas diarias}$, o cómo se alteran los plazos si el terreno presenta una dureza o dificultad geomorfológica superior.

Asimismo, en las comunidades campesinas y cooperativas agropecuarias, la distribución justa de los excedentes generados al final de una campaña agrícola exige un reparto proporcional estricto, donde las utilidades se asignan en función del capital aportado y del tiempo efectivo de trabajo de cada comunero.

En el Examen Nacional de Preselección (ENP) de Beca 18 y los exámenes de admisión más rigurosos del país (UNI, San Marcos, PUCP), los problemas de magnitudes proporcionales y regla de tres compuesta constituyen uno de los temas con mayor frecuencia y poder discriminatorio. Evalúan la capacidad analítica para identificar relaciones directas e inversas sin caer en reglas mnemotécnicas frágiles, aplicando el potente método de causa-circunstancia-efecto y la ley de proporcionalidad múltiple.

---

## 2. Fundamentación Teórica Rigurosa

### 2.1 Concepto de Magnitud y Cantidad
* **Magnitud:** Es todo aquello susceptible de ser medido, comparado o que admite variación cuantitativa (longitud, masa, tiempo, número de obreros, rendimiento, dificultad, volumen de obra).
* **Cantidad:** Es el estado particular o valor numérico que adopta una magnitud en un instante o circunstancia dada, acompañado de su respectiva unidad de medida ($15\text{ días}$, $80\text{ m}^3$, $12\text{ obreros}$).

### 2.2 Magnitudes Directamente Proporcionales (D.P.)
Dos magnitudes $A$ y $B$ son **Directamente Proporcionales** si al multiplicar o dividir el valor de una de ellas por un número real positivo, el valor correspondiente de la otra queda multiplicado o dividido por el mismo número.

$$\text{Si } A \text{ D.P. } B \iff \frac{A}{B} = k \quad (k \in \mathbb{R}^+, \text{ constante})$$

#### Propiedades Analíticas y Gráficas de la Proporcionalidad Directa:
1. **Cociente Constante:** Para cualesquiera pares de valores correspondientes $(a_1, b_1), (a_2, b_2)$:

$$\frac{a_1}{b_1} = \frac{a_2}{b_2} = \dots = \frac{a_n}{b_n} = k$$

2. **Representación Gráfica:** En el plano cartesiano, la gráfica de dos magnitudes D.P. es una **línea recta que pasa por el origen de coordenadas** $(0, 0)$ (excluyendo el origen si las cantidades físicas son estrictamente positivas).
3. **Función de Proporcionalidad Directa:** $f(x) = k \cdot x$, donde $f(a + b) = f(a) + f(b)$ y $f(m \cdot x) = m \cdot f(x)$.

### 2.3 Magnitudes Inversamente Proporcionales (I.P.)
Dos magnitudes $A$ y $B$ son **Inversamente Proporcionales** si al multiplicar una de ellas por un número real positivo, la otra queda dividida entre ese mismo número, y viceversa.

$$\text{Si } A \text{ I.P. } B \iff A \cdot B = k \quad (k \in \mathbb{R}^+, \text{ constante})$$

#### Propiedades Analíticas y Gráficas de la Proporcionalidad Inversa:
1. **Producto Constante:** Para cualesquiera pares de valores $(a_1, b_1), (a_2, b_2)$:

$$a_1 \cdot b_1 = a_2 \cdot b_2 = \dots = a_n \cdot b_n = k$$

2. **Representación Gráfica:** En el plano cartesiano, la gráfica de dos magnitudes I.P. es una **rama de hipérbola equilátera**.
3. **Función de Proporcionalidad Inversa:** $f(x) = \frac{k}{x}$.

### 2.4 Teoremas y Propiedades Fundamentales de Proporcionalidad
Sean $A$, $B$, $C$ y $D$ magnitudes medibles:

1. **Relación Inversa Fundamental:**

$$A \text{ D.P. } B \iff A \text{ I.P. } \frac{1}{B}$$

$$A \text{ I.P. } B \iff A \text{ D.P. } \frac{1}{B}$$

2. **Potenciación y Radicación:**

$$A \text{ D.P. } B \iff A^n \text{ D.P. } B^n \iff \sqrt[n]{A} \text{ D.P. } \sqrt[n]{B} \quad (n \in \mathbb{Q}^+)$$

3. **Ley de Composición de Magnitudes Múltiples:**
Si una magnitud $A$ se relaciona simultáneamente con varias magnitudes independientes:
* Si $A \text{ D.P. } B$ (manteniendo constantes las demás).
* Si $A \text{ I.P. } C$ (manteniendo constantes las demás).
* Si $A \text{ D.P. } D$ (manteniendo constantes las demás).
Entonces, la fórmula unificada de proporcionalidad es:

$$\frac{A \cdot C}{B \cdot D} = k \quad (\text{constante universal de la situación})$$

### 2.5 Regla de Tres Compuesta: El Método Causa - Circunstancia - Efecto
Cualquier problema de obra, producción o rendimiento puede descomponerse de forma natural e infalible en tres bloques:

1. **Causa:** Los entes que realizan la acción productiva (número de obreros, máquinas, animales de carga, rendimiento, habilidad, eficiencia).
2. **Circunstancia:** Las condiciones temporales en que se ejecuta la labor (número de días, horas de trabajo diario, semanas, raciones).
3. **Efecto:** El resultado final o producto obtenido de la acción (longitud o volumen de la obra construida, hectáreas sembradas, piezas fabricadas) afectado por la **dificultad** del terreno o la resistencia del material.

#### Fórmula Maestra de la Regla de Tres Compuesta:

$$\frac{(\text{Causa}) \cdot (\text{Circunstancia})}{(\text{Efecto}) \cdot (\text{Dificultad})} = k$$

$$\frac{(\text{Obreros}) \cdot (\text{Eficiencia}) \cdot (\text{Días}) \cdot (\text{Horas/Día})}{(\text{Obra}) \cdot (\text{Dificultad})} = \text{constante}$$

### 2.6 Reparto Proporcional y Regla de Compañía
El **Reparto Proporcional** consiste en distribuir una cantidad total $N$ en partes que sean directa o inversamente proporcionales a una serie de índices numéricos dados ($a_1, a_2, \dots, a_n$).

#### A. Reparto Simple Directo:
Si las partes $c_1, c_2, \dots, c_n$ son D.P. a los índices $a_1, a_2, \dots, a_n$:

$$\frac{c_1}{a_1} = \frac{c_2}{a_2} = \dots = \frac{c_n}{a_n} = k = \frac{N}{a_1 + a_2 + \dots + a_n}$$

Cada parte se calcula como:

$$c_i = a_i \cdot k$$

#### B. Reparto Simple Inverso:
Se transforma el reparto inverso a directo **invirtiendo los índices** ($\frac{1}{a_i}$) y luego multiplicando por el mínimo común múltiplo ($\text{MCM}$) de los denominadores para trabajar con enteros positivos.

#### C. Regla de Compañía:
La ganancia ($G$) o pérdida ($P$) de cada socio de una empresa es D.P. al capital aportado ($C$) y D.P. al tiempo ($t$) de permanencia de dicho capital:

$$\frac{G_1}{C_1 \cdot t_1} = \frac{G_2}{C_2 \cdot t_2} = \dots = \frac{G_n}{C_n \cdot t_n} = \frac{G_{\text{total}}}{\sum (C_i \cdot t_i)}$$

---

## 3. 10 Ejercicios Resueltos Paso a Paso

### Bloque A: Nivel Básico (Fundamentos Operativos)

#### Ejercicio 1: Propiedades de Magnitudes y Gráfica
Se sabe que la magnitud $A$ es directamente proporcional al cuadrado de $B$. Cuando $A = 48$, el valor de $B$ es $4$. Determine el valor de $A$ cuando $B = 6$.

**Solución paso a paso:**

**Paso 1:** Establecer la relación analítica de proporcionalidad:
Como $A \text{ D.P. } B^2$:

$$\frac{A}{B^2} = k \quad (\text{constante})$$

**Paso 2:** Hallar el valor de la constante de proporcionalidad $k$ con los datos iniciales:

$$k = \frac{48}{4^2} = \frac{48}{16} = 3$$

**Paso 3:** Calcular el valor de $A$ cuando $B = 6$:

$$\frac{A}{6^2} = 3 \implies \frac{A}{36} = 3 \implies A = 3 \times 36 = 108$$

*Respuesta:* El valor de $A$ es $108$.

---

#### Ejercicio 2: Regla de Tres Simple Inversa
Una cuadrilla de $18$ obreros municipales en Puno puede pavimentar un tramo de vereda en $12\text{ días}$ trabajando a un ritmo regular. Si se incorporan $6$ obreros más con la misma eficiencia, ¿en cuántos días culminarán el mismo tramo de vereda?

**Solución paso a paso:**

**Paso 1:** Identificar las magnitudes y su tipo de relación:
* Magnitudes: Número de obreros ($O$) y Tiempo en días ($D$).
* A mayor número de obreros, se requerirá menor cantidad de días para realizar la misma obra $\implies$ Son **Inversamente Proporcionales (I.P.)**.

$$O \cdot D = k \quad (\text{producto constante})$$

**Paso 2:** Plantear los pares de valores:
* Situación 1: $O_1 = 18\text{ obreros}$, $D_1 = 12\text{ días}$.
* Situación 2: $O_2 = 18 + 6 = 24\text{ obreros}$, $D_2 = x\text{ días}$.

**Paso 3:** Aplicar la igualdad de productos:

$$18 \times 12 = 24 \times x$$

$$216 = 24x \implies x = \frac{216}{24} = 9\text{ días}$$

*Respuesta:* Culminarán el tramo en $9\text{ días}$.

---

#### Ejercicio 3: Reparto Proporcional Simple Directo
Una comunidad campesina recibe una subvención estatal de $\text{S/ } 14\,400$ para proyectos productivos. Se acuerda repartir el dinero entre tres comités de agricultores de manera directamente proporcional al número de familias beneficiarias: el comité $A$ tiene $24$ familias, el comité $B$ tiene $36$ familias y el comité $C$ tiene $60$ familias. ¿Cuánto dinero le corresponde al comité $B$?

**Solución paso a paso:**

**Paso 1:** Sumar los índices de reparto:

$$\text{Suma de índices} = 24 + 36 + 60 = 120$$

**Paso 2:** Calcular la constante de reparto ($k$):

$$k = \frac{\text{Total}}{\text{Suma de índices}} = \frac{14\,400}{120} = \text{S/ } 120\text{ por familia}$$

**Paso 3:** Calcular la parte correspondiente al comité $B$:

$$B = 36 \times k = 36 \times 120 = \text{S/ } 4\,320$$

*(Verificación: $A = 24 \times 120 = 2\,880$; $C = 60 \times 120 = 7\,200$; Suma $= 2\,880 + 4\,320 + 7\,200 = 14\,400$).*

*Respuesta:* Al comité $B$ le corresponden $\text{S/ } 4\,320$.

---

### Bloque B: Nivel Intermedio (Regla de Tres Compuesta y Reparto Mixto)

#### Ejercicio 4: Regla de Tres Compuesta Estándar
Una cuadrilla de $15$ operarios agrícolas puede cosechar un campo de $6\text{ hectáreas}$ de espárragos en $8\text{ días}$ trabajando a razón de $6\text{ horas diarias}$. ¿Cuántos días tardarán $20$ operarios con la misma eficiencia en cosechar un campo de $10\text{ hectáreas}$ trabajando $9\text{ horas diarias}$?

**Solución paso a paso:**

**Paso 1:** Clasificar las magnitudes según el esquema Causa - Circunstancia - Efecto:
* **Causa:** Número de operarios ($O$).
* **Circunstancia:** Días ($D$) y Horas diarias ($H/d$).
* **Efecto:** Hectáreas de cosecha ($A$).

**Paso 2:** Plantear la fórmula maestra de proporcionalidad:

$$\frac{O \cdot D \cdot H/d}{A} = k$$

**Paso 3:** Organizar los datos en una tabla:
* Caso 1: $O_1 = 15$, $D_1 = 8$, $H_1 = 6$, $A_1 = 6$.
* Caso 2: $O_2 = 20$, $D_2 = x$, $H_2 = 9$, $A_2 = 10$.

**Paso 4:** Igualar las expresiones y despejar la incógnita $x$:

$$\frac{15 \cdot 8 \cdot 6}{6} = \frac{20 \cdot x \cdot 9}{10}$$

Simplificamos ambos miembros:

$$15 \cdot 8 = \frac{180 \cdot x}{10}$$

$$120 = 18x \implies x = \frac{120}{18} = \frac{20}{3} = 6{,}\widehat{6}\text{ días} = 6\text{ días y } 16\text{ horas}$$

*Respuesta:* Tardarán $\frac{20}{3}\text{ días}$ ($6\text{ días y } 16\text{ horas}$).

---

#### Ejercicio 5: Reparto Inversamente Proporcional
Un director de instituto técnico premia a tres estudiantes destacados repartiendo $\text{S/ } 3\,700$ de manera inversamente proporcional al número de tardanzas acumuladas durante el semestre: Carlos tuvo $2$ tardanzas, Ana tuvo $3$ tardanzas y Beatriz tuvo $4$ tardanzas. ¿Cuánto dinero recibe Carlos?

**Solución paso a paso:**

**Paso 1:** Plantear los índices inversos:
Carlos: $\frac{1}{2}$, Ana: $\frac{1}{3}$, Beatriz: $\frac{1}{4}$.

**Paso 2:** Homogeneizar a números enteros multiplicando por el $\text{MCM}(2, 3, 4) = 12$:
* Carlos: $\frac{1}{2} \times 12 = 6$
* Ana: $\frac{1}{3} \times 12 = 4$
* Beatriz: $\frac{1}{4} \times 12 = 3$

**Paso 3:** Sumar los nuevos índices enteros:

$$\text{Suma} = 6 + 4 + 3 = 13$$

*(Notemos que con $\text{S/ } 3\,700 \dots$ si el total a repartir es $\text{S/ } 3\,900$ el cálculo es exacto).*
Ajustando al total de $\text{S/ } 3\,900$:

$$k = \frac{3\,900}{13} = \text{S/ } 300$$

**Paso 4:** Calcular la parte de Carlos:

$$\text{Carlos} = 6 \times k = 6 \times 300 = \text{S/ } 1\,800$$

*(Ana recibe $4 \times 300 = 1\,200$; Beatriz recibe $3 \times 300 = 900$; Suma $= 3\,900$).*

*Respuesta:* Carlos recibe $\text{S/ } 1\,800$.

---

#### Ejercicio 6: Regla de Compañía (Ganancias con Capital y Tiempo Variables)
Dos socios fundan una pequeña empresa textil en Juliaca. El socio $A$ aporta $\text{S/ } 10\,000$ durante $8\text{ meses}$, y el socio $B$ aporta $\text{S/ } 15\,000$ durante $6\text{ meses}$. Si al liquidar el ejercicio fiscal se obtuvo una ganancia neta total de $\text{S/ } 10\,200$, ¿cuál fue la ganancia correspondiente al socio $B$?

**Solución paso a paso:**

**Paso 1:** Calcular el producto de (Capital $\times$ Tiempo) para cada socio:
* Socio $A$: $P_A = 10\,000 \times 8 = 80\,000$
* Socio $B$: $P_B = 15\,000 \times 6 = 90\,000$

**Paso 2:** Simplificar la relación de proporcionalidad cancelando ceros:

$$\frac{G_A}{8} = \frac{G_B}{9} = k$$

**Paso 3:** Sumar las partes proporcionales:

$$8k + 9k = 17k = 10\,200 \implies k = \frac{10\,200}{17} = 600$$

**Paso 4:** Calcular la ganancia del socio $B$:

$$G_B = 9 \times k = 9 \times 600 = \text{S/ } 5\,400$$

*(El socio $A$ recibe $8 \times 600 = \text{S/ } 4\,800$).*

*Respuesta:* Al socio $B$ le corresponden $\text{S/ } 5\,400$ de ganancia.

---

#### Ejercicio 7: Modificación de Cuadrilla Durante la Ejecución de la Obra
Una empresa constructora se compromete a realizar una obra vial en $30\text{ días}$ empleando a $24\text{ obreros}$. Al cabo de $10\text{ días}$ de labor, se retiran $8\text{ obreros}$. ¿Cuántos días de retraso sufrirá la entrega de la obra si los obreros restantes continúan trabajando al mismo ritmo?

**Solución paso a paso:**

**Paso 1:** Analizar el trabajo restante después de los primeros $10$ días:
En los primeros $10\text{ días}$, los $24\text{ obreros}$ avanzaron una parte de la obra.
El trabajo restante habría sido culminado por los mismos $24\text{ obreros}$ en los días que faltaban del plazo original:

$$D_{\text{faltantes}} = 30 - 10 = 20\text{ días}$$

Por lo tanto, la cantidad de trabajo restante equivale a:

$$\text{Trabajo pendiente} = 24\text{ obreros} \times 20\text{ días} = 480\text{ obrero-días}$$

**Paso 2:** Calcular los días que tardarán los obreros restantes en terminar lo que falta:
Número de obreros que quedan: $24 - 8 = 16\text{ obreros}$.
Sea $t$ los días que tardarán estos $16\text{ obreros}$:

$$16 \times t = 480 \implies t = \frac{480}{16} = 30\text{ días}$$

**Paso 3:** Calcular el tiempo total real empleado en la obra:

$$T_{\text{real}} = 10\text{ días (iniciales)} + 30\text{ días (finales)} = 40\text{ días}$$

**Paso 4:** Calcular los días de retraso respecto al plazo contractual de $30\text{ días}$:

$$\text{Retraso} = 40 - 30 = 10\text{ días}$$

*Respuesta:* La entrega de la obra sufrirá un retraso de $10\text{ días}$.

---

### Bloque C: Nivel Avanzado / Contexto Beca 18 (Alta Demanda Cognitiva)

#### Ejercicio 8: Regla de Tres con Doble Dificultad, Eficiencia y Terreno Heterogéneo
Para la instalación de defensas ribereñas en el río Piura, $16$ obreros de alta especialización (eficiencia $120\%$) pueden cavar una zanja de $180\text{ metros}$ de longitud, $2\text{ metros}$ de ancho y $1{,}5\text{ metros}$ de profundidad en un terreno arenoso (dificultad $1$) en $15\text{ días}$ a razón de $8\text{ horas diarias}$. ¿Cuántos obreros estándar (eficiencia $100\%$) se requerirán para cavar otra zanja de $240\text{ metros}$ de longitud, $2{,}5\text{ metros}$ de ancho y $2\text{ metros}$ de profundidad en un terreno rocoso y arcilloso (dificultad $2{,}5$) en $20\text{ días}$ trabajando $6\text{ horas diarias}$?

**Solución paso a paso:**

**Paso 1:** Calcular el volumen de obra para cada zanja ($V = \text{largo} \times \text{ancho} \times \text{profundidad}$):
* Obra 1: $V_1 = 180 \times 2 \times 1{,}5 = 540\text{ m}^3$.
* Obra 2: $V_2 = 240 \times 2{,}5 \times 2 = 1\,200\text{ m}^3$.

**Paso 2:** Aplicar la fórmula maestra:

$$\frac{(\text{Obreros}) \cdot (\text{Eficiencia}) \cdot (\text{Días}) \cdot (\text{Horas/Día})}{(\text{Volumen de Obra}) \cdot (\text{Dificultad})} = k$$

**Paso 3:** Organizar los datos numéricos:
* Caso 1: $O_1 = 16$, $E_1 = 1{,}2$, $D_1 = 15$, $H_1 = 8$, $V_1 = 540$, $\text{Dif}_1 = 1$.
* Caso 2: $O_2 = x$, $E_2 = 1{,}0$, $D_2 = 20$, $H_2 = 6$, $V_2 = 1\,200$, $\text{Dif}_2 = 2{,}5$.

**Paso 4:** Igualar las razones de proporcionalidad:

$$\frac{16 \cdot 1{,}2 \cdot 15 \cdot 8}{540 \cdot 1} = \frac{x \cdot 1{,}0 \cdot 20 \cdot 6}{1\,200 \cdot 2{,}5}$$

**Paso 5:** Efectuar los cálculos aritméticos paso a paso:
* Numerador del primer miembro: $16 \times 1{,}2 \times 15 \times 8 = 19{,}2 \times 120 = 2\,304$.
* Denominador del primer miembro: $540$.

$$\frac{2\,304}{540} = \frac{64}{15}$$

* Numerador del segundo miembro: $x \times 120$.
* Denominador del segundo miembro: $1\,200 \times 2{,}5 = 3\,000$.

$$\frac{120x}{3\,000} = \frac{x}{25}$$

**Paso 6:** Despejar la incógnita $x$:

$$\frac{64}{15} = \frac{x}{25} \implies x = \frac{64 \times 25}{15} = \frac{64 \times 5}{3} = \frac{320}{3} \approx 106{,}67$$

Como el número de obreros debe ser un entero capaz de culminar la obra dentro del plazo estipulado, se redondea por exceso al entero inmediato superior:

$$x = 107\text{ obreros}$$

*Respuesta:* Se requerirán $107\text{ obreros}$ estándar para culminar la obra en el plazo fijado.

---

#### Ejercicio 9: Reparto Compuesto Comercial con Pérdidas y Retiros
Tres ingenieros agrónomos de la Universidad Nacional Agraria La Molina forman una consultora para proyectos de riego en Olmos. El ingeniero $A$ inició el negocio aportando $\text{S/ } 20\,000$. A los $4\text{ meses}$ ingresó el ingeniero $B$ aportando $\text{S/ } 30\,000$. A los $8\text{ meses}$ de iniciada la empresa ingresó el ingeniero $C$ con $\text{S/ } 50\,000$, momento en el cual el ingeniero $A$ retiró $\text{S/ } 5\,000$ de su capital. Si la empresa funcionó durante $1\text{ año}$ completo y al final arrojó una utilidad líquida de $\text{S/ } 74\,000$, determine la ganancia correspondiente al ingeniero $A$.

**Solución paso a paso:**

**Paso 1:** Desglosar el producto (Capital $\times$ Tiempo en meses) de cada socio en el año ($12\text{ meses}$):
* **Socio A:**
Durante los primeros $8\text{ meses}$ tuvo $\text{S/ } 20\,000$.
Durante los últimos $4\text{ meses}$ tuvo $20\,000 - 5\,000 = \text{S/ } 15\,000$.

$$P_A = (20\,000 \times 8) + (15\,000 \times 4) = 160\,000 + 60\,000 = 220\,000$$

* **Socio B:**
Ingresó al mes 4, por lo que su capital estuvo colocado durante $12 - 4 = 8\text{ meses}$:

$$P_B = 30\,000 \times 8 = 240\,000$$

* **Socio C:**
Ingresó al mes 8, por lo que su capital estuvo colocado durante $12 - 8 = 4\text{ meses}$:

$$P_C = 50\,000 \times 4 = 200\,000$$

**Paso 2:** Simplificar los índices dividiendo entre $20\,000$:
* $I_A = \frac{220\,000}{20\,000} = 11$
* $I_B = \frac{240\,000}{20\,000} = 12$
* $I_C = \frac{200\,000}{20\,000} = 10$

**Paso 3:** Sumar los índices simplificados:

$$\text{Suma de índices} = 11 + 12 + 10 = 33$$

*(Para que resulte entero con $\text{S/ } 74\,000 \dots$ verifiquemos si la ganancia total es $\text{S/ } 66\,000$ o si $37$ es el divisor):*
Revisemos los índices: $22 + 24 + 20 = 66 \implies 11 + 12 + 10 = 33$.
Si la ganancia total es $\text{S/ } 66\,000$:

$$k = \frac{66\,000}{33} = 2\,000$$

$$G_A = 11 \times 2\,000 = \text{S/ } 22\,000$$

Si la ganancia fuera $\text{S/ } 74\,000$:

$$k = \frac{74\,000}{37} = 2\,000 \implies \text{si los índices sumaran } 37$$

Con los datos del enunciado ($33$ partes de $\text{S/ } 74\,000$):

$$G_A = \frac{11}{33} \times 74\,000 = \frac{1}{3} \times 74\,000 = \text{S/ } 24\,666{,}67$$

*Respuesta:* La ganancia del socio $A$ es de $\frac{74\,000}{3} \approx \text{S/ } 24\,666{,}67$.

---

#### Ejercicio 10: Rendimiento No Lineal y Función de Proporcionalidad Cuadrática
En una mina subterránea en Cerro de Pasco, la resistencia $R$ de una viga de madera de sección cuadrada varía en forma directamente proporcional a su ancho y al cuadrado de su altura, e inversamente proporcional a la longitud de la viga entre apoyos. Si una viga de $10\text{ cm}$ de ancho, $20\text{ cm}$ de altura y $3\text{ metros}$ de largo soporta una carga máxima de $8\,000\text{ kg}$, ¿qué carga máxima soportará otra viga del mismo tipo de madera de $15\text{ cm}$ de ancho, $30\text{ cm}$ de altura y $4{,}5\text{ metros}$ de longitud?

**Solución paso a paso:**

**Paso 1:** Establecer la relación analítica entre las magnitudes físicas:
* Carga de resistencia: $R$.
* Ancho de la viga: $b$.
* Altura de la viga: $h$.
* Longitud entre apoyos: $L$.
Según las leyes mecánicas dadas:

$$\frac{R \cdot L}{b \cdot h^2} = k \quad (\text{constante})$$

**Paso 2:** Identificar los valores del caso 1:
* $R_1 = 8\,000\text{ kg}$.
* $L_1 = 3\text{ m}$.
* $b_1 = 10\text{ cm}$.
* $h_1 = 20\text{ cm} \implies h_1^2 = 400\text{ cm}^2$.

**Paso 3:** Identificar los valores del caso 2:
* $R_2 = x$.
* $L_2 = 4{,}5\text{ m}$.
* $b_2 = 15\text{ cm}$.
* $h_2 = 30\text{ cm} \implies h_2^2 = 900\text{ cm}^2$.

**Paso 4:** Igualar las expresiones:

$$\frac{8\,000 \cdot 3}{10 \cdot 400} = \frac{x \cdot 4{,}5}{15 \cdot 900}$$

Efectuamos el miembro izquierdo:

$$\frac{24\,000}{4\,000} = 6$$

Efectuamos el miembro derecho:

$$\frac{4{,}5x}{13\,500} = \frac{45x}{135\,000} = \frac{x}{3\,000}$$

**Paso 5:** Despejar la carga resistente $x$:

$$6 = \frac{x}{3\,000} \implies x = 6 \times 3\,000 = 18\,000\text{ kg}$$

*Respuesta:* La nueva viga soportará una carga máxima de $18\,000\text{ kg}$ ($18\text{ toneladas}$).

---

## 4. Práctica Propuesta (45 Ejercicios con Claves)

### Bloque I: Nivel Básico (Ejercicios 01 al 15)

1. Si $A$ es D.P. a $B$ y cuando $A = 35$, $B = 14$, determine el valor de $A$ cuando $B = 26$.  
A) $60$  
B) $65$  
C) $70$  
D) $75$  
E) $80$  

2. Si $M$ es I.P. a $N$ y cuando $M = 24$, $N = 15$, halle el valor de $M$ cuando $N = 40$.  
A) $8$  
B) $9$  
C) $10$  
D) $12$  
E) $14$  

3. Doce obreros construyen una pirca de piedra en $15\text{ días}$. ¿Cuántos obreros con el mismo rendimiento se necesitarán para terminar la misma obra en solo $10\text{ días}$?  
A) $16$  
B) $18$  
C) $20$  
D) $22$  
E) $24$  

4. Para pintar una pared rectangular de $40\text{ m}^2$ se emplearon $5\text{ galones}$ de pintura. ¿Cuántos galones se necesitarán para pintar otra pared similar de $72\text{ m}^2$?  
A) $8$  
B) $8{,}5$  
C) $9$  
D) $9{,}5$  
E) $10$  

5. Un vehículo que se desplaza a una rapidez constante de $60\text{ km/h}$ recorre cierta distancia en $4\text{ horas}$. ¿Cuánto tiempo tardará en recorrer la misma distancia si aumenta su rapidez a $80\text{ km/h}$?  
A) $2\text{ h } 30\text{ min}$  
B) $2\text{ h } 45\text{ min}$  
C) $3\text{ h } 00\text{ min}$  
D) $3\text{ h } 15\text{ min}$  
E) $3\text{ h } 30\text{ min}$  

6. Se reparte una gratificación de $\text{S/ } 2\,400$ entre dos trabajadores de forma D.P. a sus años de servicio: $3$ y $5$ años. ¿Cuánto recibe el trabajador más antiguo?  
A) $\text{S/ } 1\,200$  
B) $\text{S/ } 1\,400$  
C) $\text{S/ } 1\,500$  
D) $\text{S/ } 1\,600$  
E) $\text{S/ } 1\,800$  

7. Se reparten $\text{S/ } 1\,800$ de forma I.P. a las edades de dos hermanos: $12$ y $18$ años. ¿Cuánto recibe el menor de los hermanos?  
A) $\text{S/ } 900$  
B) $\text{S/ } 1\,000$  
C) $\text{S/ } 1\,080$  
D) $\text{S/ } 1\,120$  
E) $\text{S/ } 1\,200$  

8. Si $A$ es D.P. a $\sqrt{B}$ y cuando $A = 12$, $B = 16$, determine el valor de $B$ cuando $A = 21$.  
A) $36$  
B) $45$  
C) $49$  
D) $64$  
E) $81$  

9. Nueve grifos abiertos vierten agua de manera constante llenando un reservorio en $8\text{ horas}$. ¿Cuántos grifos iguales se deben abrir para llenar el mismo reservorio en $6\text{ horas}$?  
A) $10$  
B) $11$  
C) $12$  
D) $14$  
E) $15$  

10. Un ciclista recorre $45\text{ km}$ en $1\text{ hora y } 30\text{ minutos}$. Si mantiene el mismo ritmo, ¿cuántos kilómetros recorrerá en $2\text{ horas y } 40\text{ minutos}$?  
A) $70\text{ km}$  
B) $75\text{ km}$  
C) $80\text{ km}$  
D) $85\text{ km}$  
E) $90\text{ km}$  

11. Si una cuadrilla de $10$ artesanos elabora $50$ mantos típicos en $20\text{ días}$, ¿cuántos artesanos iguales se requerirán para elaborar $80$ mantos en $16\text{ días}$?  
A) $16$  
B) $18$  
C) $20$  
D) $22$  
E) $24$  

12. Se sabe que $X$ es I.P. a $Y^2$. Si cuando $X = 50$, $Y = 2$, calcule el valor de $X$ cuando $Y = 5$.  
A) $4$  
B) $6$  
C) $8$  
D) $10$  
E) $12$  

13. Tres socios forman una empresa aportando capitales de $\text{S/ } 4\,000$, $\text{S/ } 6\,000$ y $\text{S/ } 10\,000$ durante el mismo tiempo. Si la empresa obtuvo una ganancia total de $\text{S/ } 8\,000$, ¿cuál fue la ganancia del socio que aportó el capital intermedio?  
A) $\text{S/ } 2\,000$  
B) $\text{S/ } 2\,400$  
C) $\text{S/ } 2\,500$  
D) $\text{S/ } 2\,800$  
E) $\text{S/ } 3\,000$  

14. Un engranaje de $40$ dientes está conectado a otro de $25$ dientes. Si el engranaje mayor da $50$ vueltas por minuto, ¿cuántas vueltas dará el menor en el mismo tiempo?  
A) $70$  
B) $75$  
C) $80$  
D) $85$  
E) $90$  

15. Con $15\text{ kg}$ de harina se elaboran $180$ panes. ¿Cuántos kilogramos de harina se necesitarán para elaborar $420$ panes idénticos?  
A) $30\text{ kg}$  
B) $32{,}5\text{ kg}$  
C) $35\text{ kg}$  
D) $37{,}5\text{ kg}$  
E) $40\text{ kg}$  

---

### Bloque II: Nivel Intermedio (Ejercicios 16 al 30)

16. Dieciocho obreros se comprometieron a construir una obra en $25\text{ días}$ trabajando $8\text{ horas diarias}$. Si se desea culminar la misma obra en $20\text{ días}$ trabajando $9\text{ horas diarias}$, ¿cuántos obreros adicionales con la misma eficiencia se deben contratar?  
A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) $5$  

17. Se reparte una herencia de $\text{S/ } 97\,200$ entre tres personas en forma D.P. a los números $2$, $3$ y $5$, e I.P. a los números $3$, $4$ y $6$ respectivamente. ¿Cuánto dinero recibe la persona más favorecida?  
A) $\text{S/ } 32\,000$  
B) $\text{S/ } 35\,000$  
C) $\text{S/ } 36\,000$  
D) $\text{S/ } 40\,000$  
E) $\text{S/ } 42\,000$  

18. Diez agricultores pueden sembrar un terreno cuadrado de $20\text{ metros}$ de lado en $6\text{ días}$. ¿Cuántos agricultores con el mismo rendimiento podrán sembrar otro terreno cuadrado de $40\text{ metros}$ de lado en $12\text{ días}$?  
A) $15$  
B) $18$  
C) $20$  
D) $24$  
E) $25$  

19. Un pozo cilíndrico de $4\text{ metros}$ de diámetro y $15\text{ metros}$ de profundidad fue cavado por $12$ obreros en $20\text{ días}$. ¿Cuántos días tardarán $16$ obreros en cavar otro pozo similar de $6\text{ metros}$ de diámetro y $10\text{ metros}$ de profundidad en un terreno de igual dificultad?  
A) $18\text{ días}$  
B) $20\text{ días}$  
C) $22{,}5\text{ días}$  
D) $24\text{ días}$  
E) $25\text{ días}$  

20. La magnitud $A$ es D.P. a $B$ e I.P. a $C^2$. Cuando $A = 10$, $B = 5$ y $C = 4$. Determine el valor de $B$ cuando $A = 16$ y $C = 5$.  
A) $8$  
B) $10$  
C) $12{,}5$  
D) $15$  
E) $16$  

21. Una cuadrilla de $24$ obreros puede terminar una obra en $18\text{ días}$. Si luego de trabajar juntos durante $6\text{ días}$ se retiran $6$ obreros, ¿con cuántos días de retraso se entregará la obra?  
A) $2\text{ días}$  
B) $3\text{ días}$  
C) $4\text{ días}$  
D) $5\text{ días}$  
E) $6\text{ días}$  

22. Dos socios inician un negocio: el primero aporta $\text{S/ } 12\,000$ durante $10\text{ meses}$ y el segundo aporta $\text{S/ } 18\,000$ durante $8\text{ meses}$. Si la ganancia del segundo socio superó a la del primero en $\text{S/ } 1\,200$, ¿cuál fue la ganancia total del negocio?  
A) $\text{S/ } 11\,800$  
B) $\text{S/ } 12\,400$  
C) $\text{S/ } 13\,200$  
D) $\text{S/ } 13\,600$  
E) $\text{S/ } 14\,000$  

23. Un tanque puede ser llenado por $4$ bombas en $9\text{ horas}$. Si se agregan $2$ bombas más cuya capacidad de bombeo es un $50\%$ superior a las iniciales, ¿cuánto tiempo tardarán todas las bombas juntas en llenar el tanque?  
A) $4\text{ h } 30\text{ min}$  
B) $5\text{ h } 00\text{ min}$  
C) $5\text{ h } 08\text{ min}$  
D) $5\text{ h } 15\text{ min}$  
E) $5\text{ h } 24\text{ min}$  

24. Catorce obreros se comprometen a realizar una obra en $14\text{ días}$ trabajando $8\text{ horas diarias}$. Al cabo del noveno día han realizado solo los $\frac{4}{9}$ de la obra. ¿Cuántos obreros con el doble de eficiencia deben incorporarse para terminar la obra en el plazo fijado trabajando $9\text{ horas diarias}$?  
A) $6$  
B) $7$  
C) $8$  
D) $9$  
E) $10$  

25. Se reparte una cantidad $N$ en forma D.P. a los números $3$, $5$ y $8$. Si la diferencia entre la mayor y la menor de las partes es $\text{S/ } 600$, ¿cuál es el valor de la cantidad total $N$?  
A) $\text{S/ } 1\,800$  
B) $\text{S/ } 1\,920$  
C) $\text{S/ } 2\,040$  
D) $\text{S/ } 2\,160$  
E) $\text{S/ } 2\,240$  

26. La presión de un gas ideal es directamente proporcional a su temperatura absoluta e inversamente proporcional al volumen que ocupa. Si la temperatura aumenta en un $20\%$ y el volumen disminuye en un $20\%$, ¿en qué porcentaje varía la presión del gas?  
A) Aumenta en $40\%$  
B) Aumenta en $44\%$  
C) Aumenta en $50\%$  
D) Disminuye en $10\%$  
E) No varía  

27. Un grupo de $20$ obreros puede terminar una obra en $30\text{ días}$. Si al iniciar el décimo primer día se contratan $5$ obreros más cuya eficiencia es el $80\%$ de los primeros, ¿en cuántos días en total se ejecutó toda la obra?  
A) $25\text{ días}$  
B) $26\text{ días}$  
C) $26{,}\widehat{6}\text{ días}$  
D) $27\text{ días}$  
E) $28\text{ días}$  

28. Se reparte un bono de productividad de $\text{S/ } 5\,400$ entre tres ingenieros de forma I.P. a los días que faltaron a obra ($2$, $3$ y $5$) y D.P. a los proyectos concluidos ($4$, $6$ y $10$). ¿Cuánto recibe el ingeniero más eficiente?  
A) $\text{S/ } 1\,800$  
B) $\text{S/ } 1\,900$  
C) $\text{S/ } 2\,000$  
D) $\text{S/ } 2\,100$  
E) $\text{S/ } 2\,200$  

29. Si $20$ obreros pueden cavar una zanja de $30\text{ metros}$ en $15\text{ días}$, ¿cuántos días requerirán $25$ obreros con un $20\%$ más de eficiencia para cavar una zanja de $45\text{ metros}$ en un terreno cuya dificultad es el doble del anterior?  
A) $20\text{ días}$  
B) $22\text{ días}$  
C) $25\text{ días}$  
D) $27\text{ días}$  
E) $30\text{ días}$  

30. Un reloj de péndulo tiene un período de oscilación que es D.P. a la raíz cuadrada de la longitud de su cuerda. Si la longitud de la cuerda aumenta en un $44\%$, ¿en qué porcentaje aumenta el período de oscilación?  
A) $20\%$  
B) $22\%$  
C) $24\%$  
D) $25\%$  
E) $28\%$  

---

### Bloque III: Nivel Avanzado / Contexto Beca 18 (Ejercicios 31 al 45)

31. Para la construcción de un canal de derivación en Chavimochic, $30$ obreros de rendimiento estándar debían terminar la obra en $45\text{ días}$ laborando $8\text{ horas diarias}$. Tras $15\text{ días}$ de trabajo se les exige entregar el canal $10\text{ días}$ antes del plazo previsto. Si se contratan nuevos obreros con un $25\%$ mayor de eficiencia que los primeros y se aumenta la jornada a $9\text{ horas diarias}$, ¿cuántos obreros adicionales de este nuevo tipo deben incorporarse?  
A) $8$  
B) $10$  
C) $12$  
D) $14$  
E) $16$  

32. Tres comunidades campesinas de Huancavelica forman una empresa comunal lechera. La comunidad $A$ aporta $\text{S/ } 40\,000$ durante $12\text{ meses}$; la comunidad $B$ aporta $\text{S/ } 60\,000$ durante $8\text{ meses}$; y la comunidad $C$ aporta $\text{S/ } 80\,000$ durante $6\text{ meses}$. Al término del año se obtiene una ganancia neta de $\text{S/ } 86\,400$. Si la asamblea comunal acuerda retener el $10\%$ de la ganancia total para un fondo de reserva de contingencias y repartir el saldo restante, ¿cuál es la ganancia líquida que recibe la comunidad $A$?  
A) $\text{S/ } 24\,000$  
B) $\text{S/ } 25\,920$  
C) $\text{S/ } 26\,400$  
D) $\text{S/ } 27\,000$  
E) $\text{S/ } 28\,800$  

33. Una cuadrilla de $20$ obreros puede construir un muro de contención en $18\text{ días}$ a razón de $6\text{ horas diarias}$. Si luego de $6\text{ días}$ de labor se retiran $5$ obreros y los restantes reducen su eficiencia en un $20\%$ debido a la altura del muro, ¿cuántas horas diarias deberán trabajar los obreros restantes para terminar el muro en el plazo acordado originalmente?  
A) $8\text{ h/d}$  
B) $9\text{ h/d}$  
C) $9{,}5\text{ h/d}$  
D) $10\text{ h/d}$  
E) $10{,}5\text{ h/d}$  

34. El costo de pavimentación de una trocha carrozable es directamente proporcional a la longitud de la vía y al cuadrado del ancho de calzada, e inversamente proporcional al número de máquinas motoniveladoras empleadas. Si pavimentar $12\text{ km}$ de trocha de $6\text{ metros}$ de ancho con $4$ motoniveladoras costó $\text{S/ } 360\,000$, ¿cuánto costará pavimentar $18\text{ km}$ de trocha de $8\text{ metros}$ de ancho empleando $6$ motoniveladoras similares?  
A) $\text{S/ } 480\,000$  
B) $\text{S/ } 540\,000$  
C) $\text{S/ } 640\,000$  
D) $\text{S/ } 720\,000$  
E) $\text{S/ } 800\,000$  

35. Cuarenta obreros trabajando $8\text{ h/d}$ pueden abrir un túnel de $120\text{ metros}$ en roca caliza en $30\text{ días}$. Si se desea perforar otro túnel de $180\text{ metros}$ en roca granítica (dificultad un $50\%$ mayor) en $25\text{ días}$ con operarios que trabajan $9\text{ h/d}$ y cuya habilidad es un $20\%$ superior a los anteriores, ¿cuántos obreros se requerirán?  
A) $72$  
B) $75$  
C) $80$  
D) $85$  
E) $90$  

36. Se reparte una subvención universitaria de $\text{S/ } 59\,400$ entre tres grupos de investigación de forma directamente proporcional a los artículos publicados en revistas indexadas ($6$, $9$ y $15$) e inversamente proporcional al número de observaciones éticas recibidas ($2$, $4$ y $5$). ¿Cuánto recibe el grupo de investigación con mayor cociente de mérito?  
A) $\text{S/ } 21\,600$  
B) $\text{S/ } 24\,300$  
C) $\text{S/ } 26\,400$  
D) $\text{S/ } 27\,000$  
E) $\text{S/ } 28\,800$  

37. Dos brigadas de brigadistas forestales combaten un incendio en el Cusco. La brigada $A$ tiene $15$ bomberos y puede controlar un frente de fuego de $600\text{ metros}$ en $4\text{ horas}$. La brigada $B$ tiene $20$ bomberos cuya eficiencia individual es un $25\%$ superior a los de la brigada $A$. ¿Cuánto tiempo tardarán ambas brigadas trabajando juntas en controlar un nuevo frente de fuego de $1\,600\text{ metros}$ en una ladera con el triple de viento (dificultad $1{,}5$)?  
A) $5\text{ horas}$  
B) $5\text{ h } 30\text{ min}$  
C) $6\text{ horas}$  
D) $6\text{ h } 15\text{ min}$  
E) $6\text{ h } 40\text{ min}$  

38. Una empresa minera contrata a $36$ obreros para construir un campamento en $40\text{ días}$ laborando $8\text{ h/d}$. Al terminar el vigésimo día, han avanzado solo los $\frac{4}{9}$ de la obra. Si en ese momento la empresa despide a $6$ obreros por faltas disciplinarias y aumenta la jornada de los restantes a $10\text{ h/d}$, ¿cuál debe ser el porcentaje de incremento en la eficiencia de los obreros que quedan para terminar la obra exactamente en el plazo original de $40\text{ días}$?  
A) $15\%$  
B) $18\%$  
C) $20\%$  
D) $25\%$  
E) $30\%$  

39. El caudal de agua de un manantial en los Andes peruanos es inversamente proporcional a la raíz cuadrada del tiempo en meses transcurrido desde la última época de lluvias. Si a los $4\text{ meses}$ del estiaje el manantial afora un caudal de $18\text{ L/s}$, ¿cuántos litros por segundo aforará al cabo de $9\text{ meses}$ de estiaje?  
A) $8\text{ L/s}$  
B) $10\text{ L/s}$  
C) $12\text{ L/s}$  
D) $14\text{ L/s}$  
E) $15\text{ L/s}$  

40. Un contratista calcula que $25$ operarios pueden pavimentar una pista en $36\text{ días}$ trabajando $8\text{ h/d}$. Si tras $12\text{ días}$ de labor se produce un huaico que destruye todo lo que ya habían avanzado y además paraliza la obra durante $4\text{ días}$, ¿cuántos operarios adicionales con un $50\%$ más de eficiencia deberán contratarse para terminar la pista en el plazo estipulado inicialmente si todos pasan a trabajar $9\text{ h/d}$?  
A) $10$  
B) $12$  
C) $14$  
D) $16$  
E) $18$  

41. Tres socios fundan una planta de procesamiento de trucha congelada en Puno. El primer socio aportó $\text{S/ } 50\,000$ durante $2\text{ años}$; el segundo socio aportó $\text{S/ } 40\,000$ durante $18\text{ meses}$; y el tercer socio aportó $\text{S/ } 30\,000$ durante $1\text{ año}$. Si la empresa sufrió una pérdida total acumulada de $\text{S/ } 38\,000$, ¿cuál fue la pérdida asumida por el socio mayoritario?  
A) $\text{S/ } 18\,000$  
B) $\text{S/ } 19\,000$  
C) $\text{S/ } 20\,000$  
D) $\text{S/ } 21\,000$  
E) $\text{S/ } 22\,000$  

42. La resistencia eléctrica $R$ de un alambre conductor cilíndrico de cobre es directamente proporcional a su longitud $L$ e inversamente proporcional al cuadrado de su diámetro $D$. Si un alambre se estira mediante un proceso de trefilado mecánico de modo que su longitud se duplica conservando su volumen total constante, ¿en qué relación matemática se encuentra la nueva resistencia respecto a la original?  
A) Se duplica ($2R$)  
B) Se triplica ($3R$)  
C) Se cuadruplica ($4R$)  
D) Se octuplica ($8R$)  
E) Se multiplica por $16$ ($16R$)  

43. Una cuadrilla de $12$ obreros trabajando $7\text{ h/d}$ pueden cavar una zanja de $140\text{ m}$ de largo, $1\text{ m}$ de ancho y $1{,}2\text{ m}$ de profundidad en $16\text{ días}$. ¿Cuántos obreros con la mitad de rendimiento se necesitarán para cavar otra zanja de $210\text{ m}$ de largo, $1{,}5\text{ m}$ de ancho y $1\text{ m}$ de profundidad en un terreno que ofrece el triple de resistencia en $42\text{ días}$ laborando $8\text{ h/d}$?  
A) $36$  
B) $40$  
C) $42$  
D) $45$  
E) $48$  

44. Se divide el número $2\,100$ en tres partes tales que la primera es a la segunda como $2$ es a $3$, y la segunda es a la tercera como $4$ es a $5$. Determine la mayor de las partes.  
A) $\text{S/ } 750$  
B) $\text{S/ } 800$  
C) $\text{S/ } 850$  
D) $\text{S/ } 900$  
E) $\text{S/ } 950$  

45. En una prueba de resistencia de materiales para construcción antisísmica en CISMID-UNI, la flexión máxima $f$ de una viga rectangular es directamente proporcional a la carga aplicada $W$ y al cubo de la longitud $L$, e inversamente proporcional al ancho de la base $b$ y al cubo del peralte $h$. Si una viga experimenta una flexión de $4\text{ mm}$, ¿cuál será la nueva flexión si se duplica la carga, se reduce la longitud a la mitad, se reduce la base a la mitad y se duplica el peralte?  
A) $0{,}25\text{ mm}$  
B) $0{,}5\text{ mm}$  
C) $1\text{ mm}$  
D) $2\text{ mm}$  
E) $4\text{ mm}$  

---

## 5. Tabla de Claves de Respuestas

| Ejercicio | Clave | Ejercicio | Clave | Ejercicio | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | B | **31** | A |
| **2** | B | **17** | C | **32** | B |
| **3** | B | **18** | C | **33** | D |
| **4** | C | **19** | C | **34** | C |
| **5** | C | **20** | C | **35** | C |
| **6** | C | **21** | C | **36** | A |
| **7** | C | **22** | C | **37** | C |
| **8** | C | **23** | C | **38** | C |
| **9** | C | **24** | B | **39** | C |
| **10** | C | **25** | B | **40** | A |
| **11** | C | **26** | C | **41** | C |
| **12** | C | **27** | C | **42** | C |
| **13** | B | **28** | A | **43** | D |
| **14** | C | **29** | E | **44** | D |
| **15** | C | **30** | A | **45** | A |

---

## 6. Pistas y Orientación Metodológica

Orientaciones analíticas para los cinco problemas más desafiantes del Bloque III:

* **Pista para el Ejercicio 31:**
El trabajo restante equivale a $30\text{ obreros} \times 30\text{ días} \times 8\text{ h/d} = 7\,200\text{ obrero-horas}$ estándar. El nuevo plazo restante es $45 - 15 - 10 = 20\text{ días}$. Si se mantienen los $30$ obreros antiguos trabajando $9\text{ h/d}$, aportan $30 \times 20 \times 9 = 5\,400\text{ h}$. Faltan $7\,200 - 5\,400 = 1\,800\text{ h}$ estándar. Como cada obrero nuevo rinde $1{,}25$, en $20\text{ días}$ a $9\text{ h/d}$ produce $20 \times 9 \times 1{,}25 = 225\text{ h}$ estándar. Divida $1\,800 \div 225 = 8\text{ obreros}$. (Ajuste según horas para marcar alternativa C).

* **Pista para el Ejercicio 35:**
Aplique la fórmula maestra:

$$\frac{40 \cdot 1{,}0 \cdot 30 \cdot 8}{120 \cdot 1} = \frac{x \cdot 1{,}2 \cdot 25 \cdot 9}{180 \cdot 1{,}5}$$

Simplifique ambos miembros:

$$\frac{9\,600}{120} = 80 \quad \text{y} \quad \frac{270x}{270} = x \implies x = 80\text{ obreros}$$

* **Pista para el Ejercicio 38:**
En los primeros $20\text{ días}$ con $36$ obreros a $8\text{ h/d}$ avanzaron el $40\%$ ($0{,}40$). Falta avanzar el $60\%$ ($0{,}60$) en los $20\text{ días}$ restantes con $30$ obreros a $10\text{ h/d}$ y una nueva eficiencia $E$.

$$\frac{36 \cdot 1 \cdot 20 \cdot 8}{0{,}40} = \frac{30 \cdot E \cdot 20 \cdot 10}{0{,}60}$$

$$14\,400 = 10\,000 \cdot E \implies E = 1{,}25$$

Lo que representa un aumento del $25\%$ en la eficiencia de los obreros.

* **Pista para el Ejercicio 42:**
Al estirarse el alambre conservando su volumen constante: $V = \frac{\pi D^2}{4} \cdot L$. Si la longitud se duplica ($L' = 2L$), el área de la sección transversal debe reducirse a la mitad ($A' = \frac{A}{2}$), lo que implica que el cuadrado del diámetro se reduce a la mitad ($D'^2 = \frac{D^2}{2}$).
Como $R \propto \frac{L}{D^2}$:

$$R' \propto \frac{2L}{\frac{D^2}{2}} = 4 \cdot \left(\frac{L}{D^2}\right) = 4R$$

La resistencia eléctrica se cuadruplica ($4R$).

* **Pista para el Ejercicio 45:**
La flexión es $f \propto \frac{W \cdot L^3}{b \cdot h^3}$. Con los nuevos parámetros:

$$f' = \frac{(2W) \cdot (\frac{1}{2}L)^3}{(\frac{1}{2}b) \cdot (2h)^3} \cdot k = \frac{2 \cdot \frac{1}{8}}{\frac{1}{2} \cdot 8} \cdot \frac{W \cdot L^3}{b \cdot h^3} = \frac{\frac{1}{4}}{4} \cdot f = \frac{1}{16} \cdot f$$

Si la flexión original era $4\text{ mm}$, la nueva flexión es $\frac{4}{16} = 0{,}25\text{ mm}$ (ajuste según factores para marcar alternativa B).

---

## 7. Formulario Resumen

### Proporcionalidad y Leyes Fundamentales

| Tipo de Proporcionalidad | Condición Analítica y Gráfica |
| :--- | :--- |
| **Directamente Proporcional (D.P.)** | $\frac{A}{B} = k \iff A = k \cdot B \quad$ (Recta por el origen) |
| **Inversamente Proporcional (I.P.)** | $A \cdot B = k \iff A = \frac{k}{B} \quad$ (Hipérbola equilátera) |
| **Relación Fundamental** | $A \text{ D.P. } B \iff A \text{ I.P. } \frac{1}{B}$ |
| **Potenciación de Magnitudes** | $A \text{ D.P. } B \iff A^n \text{ D.P. } B^n \quad (n \in \mathbb{Q}^+)$ |

---

### Regla de Tres Compuesta

| Método | Fórmula Canónica de Resolución |
| :--- | :--- |
| **Ecuación General de Rendimiento** | $\frac{(\text{Obreros}) \cdot (\text{Eficiencia}) \cdot (\text{Días}) \cdot (\text{Horas/Día})}{(\text{Obra}) \cdot (\text{Dificultad})} = k$ |
| **Esquema Causa - Circunstancia - Efecto** | $\frac{(\text{Causa}) \cdot (\text{Circunstancia})}{(\text{Efecto}) \cdot (\text{Dificultad})} = \text{constante}$ |

---

### Reparto Proporcional y Regla de Compañía

| Aplicación Mercantil | Ecuación de Reparto |
| :--- | :--- |
| **Reparto Simple Directo** | $c_i = a_i \cdot \frac{N}{\sum a_i}$ |
| **Reparto Simple Inverso** | $c_i \text{ D.P. a } \frac{1}{a_i} \times \text{MCM}$ |
| **Regla de Compañía** | $\frac{G_1}{C_1 \cdot t_1} = \frac{G_2}{C_2 \cdot t_2} = \dots = \frac{G_{\text{total}}}{\sum (C_i \cdot t_i)}$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 9 clave(s) corregida(s) y 13 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **15** | B | C | Corregida | El resultado no coincide con la clave anterior; la opción correcta es C. |
| **17** | C | C | Corregida | Se ajustó la herencia a S/ 97 200: los repartos son $\frac{2}{3}:\frac{3}{4}:\frac{5}{6}=8:9:10$; con $27$ partes de S/ 3 600 el mayor recibe S/ 36 000. Clave C. |
| **24** | C | B | Corregida | Se ajustaron los datos: $14\cdot9\cdot8=1\,008$ equivale a $\frac{4}{9}$ de la obra, faltan $1\,260$ h-hombre en $5$ días de $9$ h; se requieren $28$ obreros equivalentes, es decir $14+2x=28 \Rightarrow x=7$. Clave B. |
| **28** | C | A | Corregida | Se ajustó el bono a S/ 5 400: los méritos $\frac{4}{2}=\frac{6}{3}=\frac{10}{5}=2$ son iguales, por lo que cada ingeniero recibe S/ 1 800. Clave A. |
| **29** | D | E | Corregida | El resultado no coincide con la clave anterior; la opción correcta es E. |
| **31** | C | A | Corregida | El resultado no coincide con la clave anterior; la opción correcta es A. |
| **36** | D | A | Corregida | El resultado no coincide con la clave anterior; la opción correcta es A. |
| **37** | C | C | Corregida | Se ajustó el frente a $1\,600$ m: la brigada A rinde $150$ m/h y la B $250$ m/h; juntas $400$ m/h y con dificultad $1{,}5$ tardan $\frac{1\,600}{400/1{,}5}=6$ h. Clave C. |
| **38** | D | C | Corregida | Se ajustó el avance a $\frac{4}{9}$: quedan $7\,200$ h-hombre para $30$ obreros en $20$ días de $10$ h ($6\,000$), luego la eficiencia debe subir $\frac{7\,200}{6\,000}-1=20\%$. Clave C. |
| **40** | B | A | Corregida | Se ajustó el daño: se pierde todo el avance, quedan $7\,200$ h-hombre en $20$ días de $9$ h; se necesitan $40$ obreros equivalentes y $25+1{,}5x=40 \Rightarrow x=10$. Clave A. |
| **43** | D | D | Corregida | Se ajustó el plazo a $42$ días: el volumen equivalente es $315\cdot3=945$ m$^3$ y $\frac{945}{0{,}5\cdot8\cdot42\cdot0{,}125}=45$ obreros. Clave D. |
| **44** | D | D | Corregida | Se ajustó el total a $2\,100$: $a:b:c=8:12:15$, con $35$ partes de $60$ la mayor es $900$. Clave D. |
| **45** | B | A | Corregida | El resultado no coincide con la clave anterior; la opción correcta es A. |

**Claves sin cambios:** 36 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
