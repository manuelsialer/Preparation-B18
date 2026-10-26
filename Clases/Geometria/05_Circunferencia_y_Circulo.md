# Tema 05: Circunferencia y Círculo

## 1. Motivación y Contexto Real

La circunferencia y el círculo constituyen la geometría fundamental del movimiento rotacional, la transmisión mecánica y la cobertura omnidireccional en el mundo de la ingeniería. Desde los engranajes de un molino de minerales en Cerro de Pasco y las poleas de un pozo petrolero en Talara hasta los sistemas modernos de irrigación tecnificada por pivote central en las pampas de Majes y Olmos, el dominio métrico de arcos, tangentes y sectores circulares define la eficiencia operativa.

En los proyectos de infraestructura y transporte en el Perú:
1. **Curvas y Rotondas Viales (Óvalos):** El diseño geométrico de óvalos distribuidores de tráfico en las carreteras nacionales garantiza que los vehículos ingresen tangencialmente sin generar puntos ciegos ni fuerzas centrífugas desestabilizadoras.
2. **Sistemas de Riego por Pivote Central:** Grandes brazos aspersores mecanizados giran en torno a una torre matriz central regando sectores circulares exactos, donde optimizar el ángulo de apertura evita el desperdicio de recursos hídricos en zonas desérticas.
3. **Túneles Hidráulicos y Tuberías a Presión:** La sección circular es la óptima para conducir fluidos a alta presión (como en las centrales hidroeléctricas de Mantaro o Cañón del Pato), ya que distribuye uniformemente los esfuerzos circunferenciales sin concentrar tensiones en aristas.

```{figure} ../../assets/geometria/circunferencia_angulos_propiedades.svg
---
width: 95%
align: center
alt: Propiedades y Ángulos en la Circunferencia
---
*Diagrama euclidiano generado en TikZ + tkz-euclide ilustrando la perpendicularidad del radio con la recta tangente, el ángulo inscrito $\alpha$, el ángulo central $2\alpha$ y los teoremas métricos fundamentales.*
```

---

## 2. Fundamento Teórico Paso a Paso

### 2.1 Elementos de la Circunferencia

La **circunferencia** es el conjunto de todos los puntos de un plano que equidistan de un punto fijo llamado **centro** ($O$). La distancia común es el **radio** ($R$).
El **círculo** es la unión de la circunferencia y su región interior.

* **Radio ($R$):** Segmento que une el centro con cualquier punto de la circunferencia.
* **Cuerda:** Segmento que une dos puntos cualesquiera de la circunferencia.
* **Diámetro ($D$):** Cuerda máxima que pasa por el centro: $D = 2R$. Divide a la circunferencia en dos semicircunferencias ($180^\circ$ cada una).
* **Arco ($\widehat{AB}$):** Porción de circunferencia delimitada por dos puntos.
* **Flecha o Sagita:** Segmento perpendicular trazado desde el punto medio de una cuerda hacia el arco que subtiende.
* **Recta Secante ($\mathcal{L}_S$):** Recta que corta a la circunferencia en dos puntos distintos.
* **Recta Tangente ($\mathcal{L}_T$):** Recta coplanar que toca a la circunferencia en un único punto denominado **punto de tangencia** ($T$).

---

### 2.2 Propiedades Fundamentales de Tangencia

1. **Perpendicularidad Radio-Tangente:**
   Todo radio trazado hacia el punto de tangencia es estrictamente perpendicular a la recta tangente:

$$OT \perp \mathcal{L}_T$$

2. **Tangentes desde un Punto Exterior:**
   Desde un punto exterior $P$ se pueden trazar exactamente dos tangentes a una circunferencia, cuyos segmentos de contacto son congruentes:

$$PA = PB$$

   Además, el rayo $PO$ biseca el ángulo $\angle APB$.

3. **Cuerdas Paralelas:**
   Dos rectas paralelas secantes o tangentes determinan arcos congruentes comprendidos entre ellas:

$$\mathcal{L}_1 \parallel \mathcal{L}_2 \implies \text{m}(\widehat{AB}) = \text{m}(\widehat{CD})$$

4. **Teorema de Poncelet (Triángulo Rectángulo Circunscrito):**
   En todo triángulo rectángulo, la suma de las longitudes de los catetos es igual a la longitud de la hipotenusa más el doble del radio de la circunferencia inscrita (inradio $r$):

$$a + c = b + 2r$$

5. **Teorema de Pitot (Cuadrilátero Circunscrito):**
   En todo cuadrilátero circunscrito a una circunferencia, la suma de las longitudes de dos lados opuestos es igual a la suma de las longitudes de los otros dos lados opuestos:

$$AB + CD = BC + AD$$

6. **Teorema de Steiner (Cuadrilátero Exinscrito):**
   En todo cuadrilátero exinscrito a una circunferencia, la diferencia de las longitudes de dos lados opuestos es igual a la diferencia de los otros dos lados:

$$AB - CD = AD - BC$$

---

### 2.3 Ángulos en la Circunferencia

| Tipo de Ángulo | Vértice | Lados | Medida del Ángulo |
| :--- | :--- | :--- | :--- |
| **Central** | En el centro $O$ | Dos radios | $\alpha = \text{m}(\widehat{AB})$ |
| **Inscrito** | En la circunferencia | Dos cuerdas | $\alpha = \frac{\text{m}(\widehat{AB})}{2}$ |
| **Semi-inscrito** | En la circunferencia | Una tangente y una cuerda | $\alpha = \frac{\text{m}(\widehat{TB})}{2}$ |
| **Ex-inscrito** | En la circunferencia | Una secante y una cuerda | $\alpha = \frac{\text{m}(\widehat{ABC})}{2}$ |
| **Interior** | Interior a la circunferencia | Dos cuerdas secantes | $\alpha = \frac{\text{m}(\widehat{AB}) + \text{m}(\widehat{CD})}{2}$ |
| **Exterior (2 secantes)** | Exterior | Dos secantes | $\alpha = \frac{\text{m}(\widehat{AB}) - \text{m}(\widehat{CD})}{2}$ |
| **Exterior (secante-tangente)** | Exterior | Una tangente y una secante | $\alpha = \frac{\text{m}(\widehat{TB}) - \text{m}(\widehat{TC})}{2}$ |
| **Exterior (2 tangentes)** | Exterior | Dos tangentes | $\alpha = \frac{\text{m}(\widehat{AMB}) - \text{m}(\widehat{AB})}{2} = 180^\circ - \text{m}(\widehat{AB})$ |

*Corolario Fundamental:* Todo ángulo inscrito en una semicircunferencia mide siempre **$90^\circ$** (ángulo recto).

---

### 2.4 Relaciones Métricas en la Circunferencia

#### 1. Teorema de las Cuerdas
Si dos cuerdas $AB$ y $CD$ se cortan en un punto interior $P$:

$$AP \cdot PB = CP \cdot PD$$

#### 2. Teorema de las Secantes
Si desde un punto exterior $P$ se trazan dos secantes $PAB$ y $PCD$:

$$PA \cdot PB = PC \cdot PD$$

*(donde $PA$ y $PC$ son las partes exteriores y $PB$, $PD$ son las secantes completas).*

#### 3. Teorema de la Tangente
Si desde un punto exterior $P$ se traza una tangente $PT$ ($T$ punto de contacto) y una secante $PAB$:

$$PT^2 = PA \cdot PB$$

---

### 2.5 Longitudes y Áreas de Regiones Circulares

1. **Longitud de la Circunferencia ($L$):**

$$L = 2\pi R = \pi D$$

2. **Longitud de un Arco de Ángulo Central $\theta$:**

$$L_{\text{arco}} = \frac{2\pi R \cdot \theta}{360^\circ} = \frac{\pi R \cdot \theta}{180^\circ}$$

3. **Área del Círculo:**

$$A = \pi R^2$$

4. **Área de un Sector Circular:**

$$A_{\text{sector}} = \frac{\pi R^2 \cdot \theta}{360^\circ} = \frac{L_{\text{arco}} \cdot R}{2}$$

5. **Área de una Corona Circular:**

$$A_{\text{corona}} = \pi(R^2 - r^2) = \frac{\pi \cdot AB^2}{4}$$

   *(donde $AB$ es la cuerda de la circunferencia mayor tangente a la menor).*
6. **Área de un Segmento Circular:**

$$A_{\text{segmento}} = A_{\text{sector}} - A_{\triangle \text{isósceles}} = \frac{\pi R^2 \theta}{360^\circ} - \frac{R^2 \sin(\theta)}{2}$$

---

### 2.6 Errores Frecuentes y Trampas de Examen

> [!CAUTION]
> 1. **Confundir Secante Exterior con Secante Total:** En el Teorema de las Secantes ($PA \cdot PB = PC \cdot PD$), $PB$ es la longitud **total** desde $P$ hasta el punto más lejano $B$, no solo la parte interna $AB$.
> 2. **Aplicar Poncelet en triángulos no rectángulos:** El Teorema de Poncelet ($a + c = b + 2r$) solo es válido cuando el triángulo posee un ángulo recto de $90^\circ$.
> 3. **Confundir Arco con Ángulo:** El arco se mide en grados sexagesimales (amplitud angular) o en metros/centímetros (longitud métrica). No deben mezclarse en una misma ecuación sin el factor de conversión $\frac{\pi R}{180^\circ}$.

---

## 3. Ejercicios Resueltos Paso a Paso

### Nivel 1: Básico (Fijación de Propiedades y Ángulos)

#### Ejercicio 1
En una circunferencia, un ángulo inscrito subtiende un arco cuya medida es de $110^\circ$. Determine la medida del ángulo inscrito y la medida del ángulo central que subtiende el mismo arco.

**Análisis Conceptual:**
El ángulo central mide igual que el arco subentendido ($\alpha = \text{arco}$), y el ángulo inscrito mide exactamente la mitad del arco ($\beta = \frac{\text{arco}}{2}$).

**Solución Paso a Paso:**

**Paso 1:** Calcular el ángulo central $\alpha$:

$$\alpha = \text{m}(\text{arco}) = 110^\circ$$

**Paso 2:** Calcular el ángulo inscrito $\beta$:

$$\beta = \frac{\text{m}(\text{arco})}{2} = \frac{110^\circ}{2} = 55^\circ$$

**Conclusión:**
El ángulo inscrito mide $55^\circ$ y el ángulo central mide $110^\circ$.

---

#### Ejercicio 2
Dos cuerdas $AB$ y $CD$ se cortan en un punto interior $P$. Si los segmentos determinados son $AP = 8\text{ cm}$, $PB = 9\text{ cm}$ y $CP = 6\text{ cm}$, calcule la longitud del segmento $PD$.

**Análisis Conceptual:**
Aplicamos el Teorema de las Cuerdas: el producto de los segmentos de una cuerda es igual al producto de los segmentos de la otra cuerda ($AP \cdot PB = CP \cdot PD$).

**Solución Paso a Paso:**

**Paso 1:** Plantear la igualdad del Teorema de las Cuerdas:

$$AP \cdot PB = CP \cdot PD$$

**Paso 2:** Reemplazar los datos numéricos:

$$8 \cdot 9 = 6 \cdot PD$$

$$72 = 6 \cdot PD$$

**Paso 3:** Despejar $PD$:

$$PD = \frac{72}{6} = 12\text{ cm}$$

**Conclusión:**
La longitud del segmento $PD$ es $12\text{ cm}$.

---

#### Ejercicio 3
En un cuadrilátero circunscrito a una circunferencia, tres de sus lados consecutivos miden $10\text{ cm}$, $14\text{ cm}$ y $18\text{ cm}$. Calcule la longitud del cuarto lado.

**Análisis Conceptual:**
Aplicamos el Teorema de Pitot: la suma de los lados opuestos es igual. Sean los lados consecutivos $a = 10$, $b = 14$, $c = 18$ y el cuarto lado $d$. Los pares opuestos son $(a, c)$ y $(b, d)$.

**Solución Paso a Paso:**

**Paso 1:** Plantear el Teorema de Pitot:

$$a + c = b + d$$

**Paso 2:** Sustituir los valores conocidos:

$$10 + 18 = 14 + d$$

$$28 = 14 + d$$

**Paso 3:** Despejar $d$:

$$d = 28 - 14 = 14\text{ cm}$$

**Conclusión:**
La longitud del cuarto lado es $14\text{ cm}$.

---

### Nivel 2: Intermedio (Propiedades y Métricas)

#### Ejercicio 4
Desde un punto exterior $P$ se traza una tangente $PT$ de $12\text{ cm}$ a una circunferencia y una secante $PAB$ que pasa por el centro. Si la parte exterior de la secante $PA$ mide $8\text{ cm}$, determine la longitud del radio de la circunferencia.

**Análisis Conceptual:**
El Teorema de la Tangente establece $PT^2 = PA \cdot PB$. Como la secante pasa por el centro, la secante total es $PB = PA + 2R = 8 + 2R$.

**Solución Paso a Paso:**

**Paso 1:** Aplicar el Teorema de la Tangente:

$$PT^2 = PA \cdot PB$$

$$12^2 = 8 \cdot PB \implies 144 = 8 \cdot PB$$

**Paso 2:** Despejar la secante total $PB$:

$$PB = \frac{144}{8} = 18\text{ cm}$$

**Paso 3:** Relacionar $PB$ con el radio $R$:

$$PB = PA + 2R \implies 18 = 8 + 2R$$

$$2R = 10 \implies R = 5\text{ cm}$$

**Conclusión:**
El radio de la circunferencia mide $5\text{ cm}$.

---

#### Ejercicio 5
En un triángulo rectángulo de catetos $12\text{ cm}$ y $16\text{ cm}$, se inscribe una circunferencia. Calcule la longitud del inradio y la distancia entre el incentro y el vértice del ángulo recto.

**Análisis Conceptual:**
Primero se halla la hipotenusa por Pitágoras. Luego se usa el Teorema de Poncelet para el inradio $r$. Como el incentro forma con los radios de contacto en los catetos un cuadrado de lado $r$ en el vértice recto, la distancia buscada es la diagonal de dicho cuadrado ($d = r\sqrt{2}$).

**Solución Paso a Paso:**

**Paso 1:** Calcular la hipotenusa $b$:

$$b = \sqrt{12^2 + 16^2} = \sqrt{144 + 256} = \sqrt{400} = 20\text{ cm}$$

**Paso 2:** Aplicar el Teorema de Poncelet:

$$a + c = b + 2r \implies 12 + 16 = 20 + 2r$$

$$28 = 20 + 2r \implies 2r = 8 \implies r = 4\text{ cm}$$

**Paso 3:** Calcular la distancia del incentro al vértice recto:

$$d(I, B) = r\sqrt{2} = 4\sqrt{2}\text{ cm}$$

**Conclusión:**
El inradio mide $4\text{ cm}$ y la distancia al vértice recto es $4\sqrt{2}\text{ cm}$.

---

#### Ejercicio 6
Desde un punto exterior $P$ a una circunferencia se trazan dos tangentes $PA$ y $PB$. Si el ángulo formado por las dos tangentes mide $40^\circ$, calcule la medida del ángulo inscrito $\angle ACB$ determinado por un punto $C$ ubicado en el arco mayor.

**Análisis Conceptual:**
El ángulo entre dos tangentes y el arco menor subentendido son suplementarios: $\angle P + \text{arco } \widehat{AB} = 180^\circ$. El ángulo inscrito en el arco mayor subtiende el arco menor.

**Solución Paso a Paso:**

**Paso 1:** Calcular la medida del arco menor $\widehat{AB}$:

$$\angle P + \text{m}(\widehat{AB}) = 180^\circ \implies 40^\circ + \text{m}(\widehat{AB}) = 180^\circ \implies \text{m}(\widehat{AB}) = 140^\circ$$

**Paso 2:** Calcular el ángulo inscrito $\angle ACB$:

$$\angle ACB = \frac{\text{m}(\widehat{AB})}{2} = \frac{140^\circ}{2} = 70^\circ$$

**Conclusión:**
La medida del ángulo inscrito $\angle ACB$ es $70^\circ$.

---

#### Ejercicio 7
En una corona circular, la cuerda de la circunferencia mayor que es tangente a la circunferencia menor mide $16\text{ cm}$. Calcule el área exacta de la corona circular.

**Análisis Conceptual:**
En la corona circular, el radio mayor $R$, el radio menor $r$ y la mitad de la cuerda tangente $L/2 = 8$ forman un triángulo rectángulo con hipotenusa $R$: $R^2 - r^2 = (L/2)^2 = 8^2 = 64$. El área de la corona es $A = \pi(R^2 - r^2)$.

**Solución Paso a Paso:**

**Paso 1:** Plantear la relación pitagórica en la mitad de la cuerda tangente:

$$R^2 = r^2 + \left(\frac{16}{2}\right)^2 \implies R^2 - r^2 = 8^2 = 64$$

**Paso 2:** Calcular el área de la corona circular:

$$A_{\text{corona}} = \pi(R^2 - r^2) = 64\pi\text{ cm}^2$$

**Conclusión:**
El área de la corona circular es exactamente $64\pi\text{ cm}^2$ (aproximadamente $201.06\text{ cm}^2$).

---

### Nivel 3: Avanzado / Contextualizado Beca 18

#### Ejercicio 8 (Diseño de un Óvalo Vial Distribuidor en Chiclayo)
La municipalidad provincial de Chiclayo diseña un óvalo vial circular de radio $R = 30\text{ m}$ para la intersección de dos avenidas principales. Desde una garita de control policial $P$ ubicada a $50\text{ m}$ del centro del óvalo, se trazan dos líneas visuales tangentes a la rotonda para ubicar cámaras de fotomulta en los puntos de tangencia $A$ y $B$. Calcule la distancia en línea recta desde la garita $P$ hacia cada cámara de fotomulta y la distancia directa entre ambas cámaras (longitud de la cuerda de contacto $AB$).

**Análisis Conceptual:**
El centro es $O$, el radio es $R = 30\text{ m}$, y la distancia del centro a la garita es $PO = 50\text{ m}$. El triángulo $\triangle PAO$ es rectángulo en $A$. La distancia entre cámaras es la cuerda $AB$, que es el doble de la altura relativa a la hipotenusa en el triángulo rectángulo $\triangle PAO$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la longitud del segmento tangente $PA$ por Pitágoras:

$$PA = \sqrt{PO^2 - R^2} = \sqrt{50^2 - 30^2} = \sqrt{2500 - 900} = \sqrt{1600} = 40\text{ m}$$

**Paso 2:** Calcular la distancia perpendicular $h$ desde el punto de tangencia $A$ hacia la línea de simetría $PO$:
En el triángulo rectángulo $\triangle PAO$:

$$\text{Cateto}_1 \cdot \text{Cateto}_2 = \text{Hipotenusa} \cdot h$$

$$PA \cdot OA = PO \cdot h \implies 40 \cdot 30 = 50 \cdot h$$

$$1200 = 50h \implies h = \frac{1200}{50} = 24\text{ m}$$

**Paso 3:** Calcular la distancia total entre ambas cámaras ($AB$):

$$AB = 2h = 2(24) = 48\text{ m}$$

**Conclusión:**
La distancia de la garita a cada cámara es de $40\text{ m}$ y la distancia entre ambas cámaras es de $48\text{ m}$.

---

#### Ejercicio 9 (Sistema de Riego por Pivote Central en Majes)
Un fundo agroindustrial en Arequipa instala un brazo aspersor móvil de $60\text{ m}$ de longitud (radio $R$) que gira alrededor de una base fija central. Para ahorrar agua, se programa el aspersor para irrigar únicamente un sector circular de $150^\circ$ donde se ubican cultivos de palta hass. Determine la longitud del arco exterior recorrido por el extremo del aspersor y el área total cultivada irrigada. ($\text{use } \pi \approx 3.1416$).

**Análisis Conceptual:**
Se aplican las fórmulas de longitud de arco y área de un sector circular para $R = 60\text{ m}$ y $\theta = 150^\circ$.

**Solución Paso a Paso:**

**Paso 1:** Calcular la longitud del arco exterior recorrido:

$$L_{\text{arco}} = \frac{2\pi R \cdot \theta}{360^\circ} = \frac{2\pi(60)(150^\circ)}{360^\circ} = \frac{18\,000\pi}{360} = 50\pi\text{ m}$$

$$L_{\text{arco}} \approx 50(3.1416) = 157.08\text{ m}$$

**Paso 2:** Calcular el área del sector circular irrigado:

$$A_{\text{sector}} = \frac{\pi R^2 \cdot \theta}{360^\circ} = \frac{\pi(60^2)(150^\circ)}{360^\circ} = \frac{3600 \cdot 150 \cdot \pi}{360} = 10 \cdot 150 \cdot \pi = 1\,500\pi\text{ m}^2$$

$$A_{\text{sector}} \approx 1500(3.1416) = 4\,712.4\text{ m}^2 \approx 0.47\text{ hectáreas}$$

**Conclusión:**
El extremo del brazo recorre un arco de $50\pi\text{ m} \approx 157.08\text{ m}$ e irriga un área de $1\,500\pi\text{ m}^2 \approx 4\,712.4\text{ m}^2$.

---

#### Ejercicio 10 (Transmisión por Poleas y Faja Mecánica en Mina de Cobre)
En una planta de molienda de mineral en Moquegua, un motor eléctrico transmite potencia a una chancadora mediante una faja abierta que conecta dos poleas circulares cuyos radios son $r_1 = 20\text{ cm}$ y $r_2 = 50\text{ cm}$. La distancia entre los ejes de giro de ambas poleas es de $100\text{ cm}$. Calcule la longitud del tramo recto de la faja de transmisión entre los dos puntos de contacto de tangencia exterior.

**Análisis Conceptual:**
El tramo recto de la faja corresponde a la longitud de la tangente común exterior común a dos circunferencias de radios $R$ y $r$ separadas por una distancia entre centros $d = 100\text{ cm}$.
La fórmula pitagórica de la tangente común exterior es: $T_e = \sqrt{d^2 - (R - r)^2}$.

**Solución Paso a Paso:**

**Paso 1:** Identificar los datos:

$$R = 50\text{ cm},\quad r = 20\text{ cm},\quad d = 100\text{ cm}$$

**Paso 2:** Calcular la diferencia de radios:

$$R - r = 50 - 20 = 30\text{ cm}$$

**Paso 3:** Aplicar el Teorema de Pitágoras para la tangente común exterior:

$$T_e = \sqrt{d^2 - (R - r)^2} = \sqrt{100^2 - 30^2} = \sqrt{10\,000 - 900} = \sqrt{9\,100}$$

$$T_e = \sqrt{100 \cdot 91} = 10\sqrt{91}\text{ cm} \approx 10(9.539) \approx 95.39\text{ cm}$$

**Conclusión:**
La longitud de cada tramo recto libre de la faja de transmisión es de $10\sqrt{91}\text{ cm} \approx 95.39\text{ cm}$.

---

## 4. Práctica Propuesta

### Bloque I: Nivel Básico (15 ejercicios)

1. En una circunferencia, el ángulo central mide $76^\circ$. ¿Cuánto mide el ángulo inscrito que subtiende el mismo arco?  
A) $33^\circ$  
B) $38^\circ$  
C) $42^\circ$  
D) $76^\circ$  
E) $152^\circ$  

2. Dos cuerdas se cortan en un punto interior dividiéndose una de ellas en segmentos de $3\text{ cm}$ y $12\text{ cm}$. Si uno de los segmentos de la otra cuerda mide $4\text{ cm}$, ¿cuánto mide el segmento restante?  
A) $6\text{ cm}$  
B) $8\text{ cm}$  
C) $9\text{ cm}$  
D) $10\text{ cm}$  
E) $11\text{ cm}$  

3. En un triángulo rectángulo, los catetos miden $9\text{ cm}$ y $12\text{ cm}$. Aplique el Teorema de Poncelet para calcular su inradio.  
A) $2\text{ cm}$  
B) $3\text{ cm}$  
C) $4\text{ cm}$  
D) $5\text{ cm}$  
E) $6\text{ cm}$  

4. En un cuadrilátero circunscrito a una circunferencia, dos lados opuestos miden $15\text{ cm}$ y $25\text{ cm}$. ¿Cuál es el perímetro del cuadrilátero?  
A) $60\text{ cm}$  
B) $70\text{ cm}$  
C) $80\text{ cm}$  
D) $90\text{ cm}$  
E) $100\text{ cm}$  

5. ¿Cuál es el área de un círculo cuyo diámetro mide $20\text{ cm}$?  
A) $50\pi\text{ cm}^2$  
B) $100\pi\text{ cm}^2$  
C) $200\pi\text{ cm}^2$  
D) $400\pi\text{ cm}^2$  
E) $25\pi\text{ cm}^2$  

6. La longitud de una circunferencia es de $24\pi\text{ cm}$. ¿Cuánto mide su radio?  
A) $6\text{ cm}$  
B) $8\text{ cm}$  
C) $12\text{ cm}$  
D) $16\text{ cm}$  
E) $24\text{ cm}$  

7. En una circunferencia, un arco mide $90^\circ$. ¿Cuánto mide cualquier ángulo inscrito que subtienda dicho arco?  
A) $30^\circ$  
B) $45^\circ$  
C) $60^\circ$  
D) $90^\circ$  
E) $180^\circ$  

8. Desde un punto exterior $P$ se traza una tangente $PT = 8\text{ cm}$ y una secante $PAB$. Si $PA = 4\text{ cm}$, calcule la longitud de la secante total $PB$.  
A) $12\text{ cm}$  
B) $14\text{ cm}$  
C) $16\text{ cm}$  
D) $18\text{ cm}$  
E) $20\text{ cm}$  

9. El radio trazado al punto de tangencia de una recta tangente forma con ella un ángulo de:  
A) $45^\circ$  
B) $60^\circ$  
C) $90^\circ$  
D) $120^\circ$  
E) $180^\circ$  

10. Calcule el área de un sector circular de $60^\circ$ en un círculo de radio $6\text{ cm}$.  
A) $3\pi\text{ cm}^2$  
B) $6\pi\text{ cm}^2$  
C) $9\pi\text{ cm}^2$  
D) $12\pi\text{ cm}^2$  
E) $18\pi\text{ cm}^2$  

11. Todo ángulo inscrito en una semicircunferencia es:  
A) Agudo  
B) Recto ($90^\circ$)  
C) Obtuso  
D) Llano  
E) Variable según el radio  

12. En una circunferencia, dos cuerdas paralelas determinan arcos:  
A) Suplementarios  
B) Complementarios  
C) Congruentes  
D) Perpendiculares  
E) Desiguales  

13. Si el ángulo formado por dos tangentes trazadas desde un mismo punto exterior mide $50^\circ$, ¿cuánto mide el arco menor comprendido entre los puntos de contacto?  
A) $100^\circ$  
B) $115^\circ$  
C) $120^\circ$  
D) $130^\circ$  
E) $140^\circ$  

14. En una corona circular de radios $R = 5\text{ cm}$ y $r = 3\text{ cm}$, el área comprendida es:  
A) $8\pi\text{ cm}^2$  
B) $12\pi\text{ cm}^2$  
C) $16\pi\text{ cm}^2$  
D) $20\pi\text{ cm}^2$  
E) $25\pi\text{ cm}^2$  

15. Si el inradio de un triángulo rectángulo mide $5\text{ cm}$ y la hipotenusa mide $30\text{ cm}$, ¿cuánto es la suma de los catetos?  
A) $35\text{ cm}$  
B) $40\text{ cm}$  
C) $45\text{ cm}$  
D) $50\text{ cm}$  
E) $55\text{ cm}$  

---

### Bloque II: Nivel Intermedio (15 ejercicios)

16. Desde un punto exterior $P$ se trazan dos secantes $PAB$ y $PCD$. Si $PA = 3\text{ cm}$, $AB = 9\text{ cm}$ y $PC = 4\text{ cm}$, calcule la longitud del segmento exterior $CD$.  
A) $5\text{ cm}$  
B) $6\text{ cm}$  
C) $7\text{ cm}$  
D) $8\text{ cm}$  
E) $9\text{ cm}$  

17. En una circunferencia de centro $O$ y radio $13\text{ cm}$, se traza una cuerda $AB$ de $24\text{ cm}$ de longitud. Calcule la distancia del centro $O$ hacia la cuerda $AB$.  
A) $5\text{ cm}$  
B) $6\text{ cm}$  
C) $7\text{ cm}$  
D) $8\text{ cm}$  
E) $10\text{ cm}$  

18. En un triángulo rectángulo, la hipotenusa mide $26\text{ cm}$ y el perímetro es de $60\text{ cm}$. Calcule el radio de la circunferencia inscrita (inradio).  
A) $3\text{ cm}$  
B) $4\text{ cm}$  
C) $5\text{ cm}$  
D) $6\text{ cm}$  
E) $7\text{ cm}$  

19. Dos circunferencias son tangentes exteriores y sus radios miden $9\text{ cm}$ y $4\text{ cm}$. Calcule la longitud del segmento de tangente común exterior.  
A) $10\text{ cm}$  
B) $11\text{ cm}$  
C) $12\text{ cm}$  
D) $13\text{ cm}$  
E) $14\text{ cm}$  

20. En un cuadrilátero $ABCD$ circunscrito a una circunferencia, los lados $AB = 8\text{ cm}$, $BC = 12\text{ cm}$ y $CD = 15\text{ cm}$. Halle la longitud del lado $AD$.  
A) $10\text{ cm}$  
B) $11\text{ cm}$  
C) $12\text{ cm}$  
D) $13\text{ cm}$  
E) $14\text{ cm}$  

21. El ángulo interior formado por el cruce de dos cuerdas secantes mide $75^\circ$. Si uno de los arcos interceptados mide $100^\circ$, ¿cuánto mide el otro arco opuesto por el vértice?  
A) $40^\circ$  
B) $45^\circ$  
C) $50^\circ$  
D) $55^\circ$  
E) $60^\circ$  

22. El ángulo exterior formado por dos secantes mide $35^\circ$. Si el arco mayor mide $110^\circ$, ¿cuánto mide el arco menor interceptado?  
A) $35^\circ$  
B) $40^\circ$  
C) $45^\circ$  
D) $50^\circ$  
E) $55^\circ$  

23. En un trapecio isósceles circunscrito a una circunferencia, las bases miden $4\text{ cm}$ y $16\text{ cm}$. Calcule el radio de la circunferencia inscrita.  
A) $3\text{ cm}$  
B) $4\text{ cm}$  
C) $5\text{ cm}$  
D) $6\text{ cm}$  
E) $8\text{ cm}$  

24. En una circunferencia de radio $10\text{ cm}$, una cuerda mide $16\text{ cm}$. Calcule la longitud de la flecha o sagita correspondiente a dicha cuerda.  
A) $2\text{ cm}$  
B) $3\text{ cm}$  
C) $4\text{ cm}$  
D) $5\text{ cm}$  
E) $6\text{ cm}$  

25. Desde un punto $P$ exterior a una circunferencia se traza la tangente $PT = 6\text{ cm}$ y una secante que pasa por el centro $PO$. Si la distancia del punto $P$ a la circunferencia es de $3\text{ cm}$, halle el radio de la circunferencia.  
A) $4\text{ cm}$  
B) $4.5\text{ cm}$  
C) $5\text{ cm}$  
D) $5.5\text{ cm}$  
E) $6\text{ cm}$  

26. En un triángulo equilátero circunscrito a una circunferencia de radio $r = 3\text{ cm}$, calcule el área del triángulo.  
A) $18\sqrt{3}\text{ cm}^2$  
B) $24\sqrt{3}\text{ cm}^2$  
C) $27\sqrt{3}\text{ cm}^2$  
D) $36\sqrt{3}\text{ cm}^2$  
E) $45\sqrt{3}\text{ cm}^2$  

27. Una cuerda de $10\text{ cm}$ dista $12\text{ cm}$ del centro de la circunferencia. ¿Cuánto mide el diámetro de la circunferencia?  
A) $20\text{ cm}$  
B) $24\text{ cm}$  
C) $26\text{ cm}$  
D) $28\text{ cm}$  
E) $30\text{ cm}$  

28. En un sector circular de ángulo central $45^\circ$, el área es de $8\pi\text{ cm}^2$. Calcule el perímetro de dicho sector circular.  
A) $16 + 2\pi\text{ cm}$  
B) $16 + 4\pi\text{ cm}$  
C) $8 + 2\pi\text{ cm}$  
D) $12 + 2\pi\text{ cm}$  
E) $16 + \pi\text{ cm}$  

29. En un triángulo rectángulo, la hipotenusa mide $c$ y el inradio mide $r$. ¿A qué es igual el área del triángulo rectángulo expresada en función de los segmentos de contacto de la hipotenusa $m$ y $n$ ($m+n=c$)?  
A) $m \cdot n$  
B) $2m \cdot n$  
C) $\frac{m \cdot n}{2}$  
D) $r(m+n)$  
E) $r \cdot c$  

30. En un círculo de radio $R$, se traza una cuerda que subtiende un arco de $90^\circ$. Calcule el área del segmento circular correspondiente.  
A) $\frac{R^2}{4}(\pi - 1)$  
B) $\frac{R^2}{4}(\pi - 2)$  
C) $\frac{R^2}{2}(\pi - 2)$  
D) $\frac{R^2}{4}(2\pi - 1)$  
E) $\frac{R^2}{2}(\pi - 1)$  

---

### Bloque III: Nivel Avanzado / Contextualizado Beca 18 (15 ejercicios)

31. Un túnel vehicular en la Carretera Central tiene sección de arco de circunferencia de radio $R = 5\text{ m}$. Si el ancho de la calzada de doble carril en la base del túnel es de $8\text{ m}$, calcule la altura máxima de gálibo vertical libre en el centro del túnel.  
A) $1.5\text{ m}$  
B) $2.0\text{ m}$  
C) $2.5\text{ m}$  
D) $3.0\text{ m}$  
E) $3.5\text{ m}$  

32. En un sistema de riego tecnificado por aspersión en Ica, un aspersor circular de radio $R = 14\text{ m}$ cubre un jardín. Si se reduce el alcance del radio en $2\text{ m}$ debido a una baja de presión en la bomba, ¿cuántos metros cuadrados de área verde dejan de recibir riego? ($\text{use } \pi \approx \frac{22}{7}$).  
A) $152\text{ m}^2$  
B) $163.4\text{ m}^2$  
C) $176\text{ m}^2$  
D) $188.5\text{ m}^2$  
E) $196\text{ m}^2$  

33. Una faja transportadora en un muelle pesquero de Chimbote conecta dos rodillos tangentes exteriores de diámetros $40\text{ cm}$ y $160\text{ cm}$. Calcule la distancia libre entre los puntos de contacto de la faja recta exterior si la distancia entre centros de giro es de $100\text{ cm}$.  
A) $75\text{ cm}$  
B) $80\text{ cm}$  
C) $85\text{ cm}$  
D) $90\text{ cm}$  
E) $95\text{ cm}$  

34. Una glorieta circular en una plaza de armas tiene un radio de $12\text{ m}$. Se construye una vereda peatonal de adoquines de $2\text{ m}$ de ancho uniforme alrededor de toda la glorieta. Si el metro cuadrado de adoquín colocado cuesta $S/\, 45$, ¿cuál es el costo total de la obra? ($\text{use } \pi \approx 3.1416$).  
A) $S/\, 6\,840$  
B) $S/\, 7\,344$  
C) $S/\, 7\,917$  
D) $S/\, 8\,250$  
E) $S/\, 8\,600$  

35. Un radar satelital del IGP en Huancayo detecta una perturbación ionosférica a lo largo de una cuerda circular de $160\text{ km}$. La distancia perpendicular desde la antena del radar hacia dicha cuerda es de $60\text{ km}$. Determine el radio de cobertura total de la estación de monitoreo.  
A) $90\text{ km}$  
B) $100\text{ km}$  
C) $110\text{ km}$  
D) $120\text{ km}$  
E) $125\text{ km}$  

36. En un terreno trapezoidal rectángulo circunscrito a una cisterna circular, las bases paralelas del terreno miden $18\text{ m}$ y $36\text{ m}$. Calcule el diámetro de la cisterna circular inscrita.  
A) $20\text{ m}$  
B) $22\text{ m}$  
C) $24\text{ m}$  
D) $26\text{ m}$  
E) $28\text{ m}$  

37. Dos tuberías cilíndricas idénticas de agua potable de $1\text{ m}$ de diámetro exterior descansan juntas en una zanja plana y son rodeadas por una cinta plástica de sujeción que las abraza conjuntamente. ¿Cuál es la longitud mínima de la cinta tensada?  
A) $2 + \pi\text{ m}$  
B) $2 + 2\pi\text{ m}$  
C) $4 + \pi\text{ m}$  
D) $1 + 2\pi\text{ m}$  
E) $3\pi\text{ m}$  

38. En una feria patronal en Huancavelica, una rueda de la fortuna de $10\text{ m}$ de radio gira uniformemente. Una persona asciende desde la base hasta una posición angular de $120^\circ$ respecto a la horizontal inferior. ¿A qué altura vertical sobre el suelo se encuentra la canastilla si la base inferior de la rueda está a $1.5\text{ m}$ del suelo?  
A) $14.5\text{ m}$  
B) $15.5\text{ m}$  
C) $16.5\text{ m}$  
D) $17.5\text{ m}$  
E) $18.5\text{ m}$  

39. Un terreno de cultivo tiene la forma de un sector circular con perímetro total de $100\text{ m}$ (dos radios más el arco). ¿Cuál es la longitud del radio $R$ que hace máxima el área del terreno cultivable?  
A) $20\text{ m}$  
B) $25\text{ m}$  
C) $30\text{ m}$  
D) $35\text{ m}$  
E) $40\text{ m}$  

40. En una estructura de soporte para puente colgante, un arco circular de acero tiene una luz libre (cuerda horizontal) de $48\text{ m}$ y una flecha central (altura) de $8\text{ m}$. Calcule la longitud del radio de curvatura del arco de acero.  
A) $36\text{ m}$  
B) $38\text{ m}$  
C) $40\text{ m}$  
D) $42\text{ m}$  
E) $45\text{ m}$  

41. Se unen con una cerca de alambre tres tanques circulares de combustible de radios iguales a $2\text{ m}$ que se tocan exteriormente dos a dos. ¿Cuál es la longitud total de la cerca que rodea ajustadamente a los tres tanques?  
A) $12 + 2\pi\text{ m}$  
B) $12 + 4\pi\text{ m}$  
C) $6 + 4\pi\text{ m}$  
D) $16 + 2\pi\text{ m}$  
E) $8 + 6\pi\text{ m}$  

42. En un predio rectangular de $80\text{ m}$ de largo por $40\text{ m}$ de ancho, se instala en cada uno de los cuatro vértices un aspersor de riego de $20\text{ m}$ de alcance radial que barre un cuadrante interior ($90^\circ$). ¿Cuántos metros cuadrados del terreno quedan sin recibir agua en la zona central? ($\text{use } \pi \approx 3.1416$).  
A) $1854.2\text{ m}^2$  
B) $1943.4\text{ m}^2$  
C) $2026.8\text{ m}^2$  
D) $2143.4\text{ m}^2$  
E) $2250.0\text{ m}^2$  

43. Una cámara de vigilancia instalada en el punto exterior $P$ a una edificación circular barre visualmente el arco menor $\widehat{AB}$ bajo un ángulo de $48^\circ$. Si un intruso camina pegado a la pared exterior por el arco mayor opuesto no vigilado, ¿cuántos grados de arco están fuera del alcance de la cámara?  
A) $216^\circ$  
B) $224^\circ$  
C) $228^\circ$  
D) $232^\circ$  
E) $240^\circ$  

44. En una parcela comunal se cerca un sector circular de radio $R = 24\text{ m}$ y ángulo central $60^\circ$. Si se cerca todo el contorno (los dos radios y el arco) con $4$ pasadas de alambre de púas, ¿cuántos metros lineales de alambre se comprarán? ($\text{use } \pi \approx 3.14$).  
A) $285.6\text{ m}$  
B) $292.5\text{ m}$  
C) $298.56\text{ m}$  
D) $304.4\text{ m}$  
E) $312.0\text{ m}$  

45. En una corona circular, la cuerda tangente al círculo interior mide $20\text{ m}$. Si el metro cuadrado de césped sintético para cubrir la corona cuesta $S/\, 30$, calcule el costo total de la instalación. ($\text{use } \pi \approx 3.1416$).  
A) $S/\, 8\,425$  
B) $S/\, 9\,424.80$  
C) $S/\, 10\,250$  
D) $S/\, 11\,400$  
E) $S/\, 12\,566$  

---

## 5. Claves de Respuestas

| Pregunta | Clave | Pregunta | Clave | Pregunta | Clave |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | B | **16** | A | **31** | B |
| **2** | C | **17** | A | **32** | B |
| **3** | B | **18** | B | **33** | B |
| **4** | C | **19** | C | **34** | B |
| **5** | B | **20** | B | **35** | B |
| **6** | C | **21** | C | **36** | C |
| **7** | B | **22** | B | **37** | A |
| **8** | C | **23** | B | **38** | C |
| **9** | C | **24** | C | **39** | B |
| **10** | B | **25** | B | **40** | C |
| **11** | B | **26** | C | **41** | B |
| **12** | C | **27** | C | **42** | B |
| **13** | D | **28** | A | **43** | C |
| **14** | C | **29** | A | **44** | B |
| **15** | B | **30** | B | **45** | B |

---

## 6. Autoevaluación y Metacognición

### Rúbrica de Aprendizaje

| Nivel de Dominio | Indicador Observable | Acción Correctiva Recomendada |
| :--- | :--- | :--- |
| **Inicial (< 60% aciertos)** | Confunde la secante total con el segmento exterior o aplica Poncelet sin verificar el ángulo recto. | Repasar el Teorema de la Tangente y Secantes en §2.4 dibujando las líneas auxiliares y rotulando las longitudes. |
| **En Proceso (60% - 80% aciertos)** | Resuelve problemas directos de ángulos inscritos y centrales, pero se traba en coronas circulares o tangentes comunes. | Practicar los ejercicios 16 al 30 prestando especial atención a las construcciones con triángulos rectángulos. |
| **Avanzado (> 80% aciertos)** | Modela problemas de rotondas viales, fajas mecánicas, pivotes de riego y optimizaciones con precisión preuniversitaria. | Resolver los problemas 31 al 45 con cronómetro estricto (1.5 minutos por problema). |

### Preguntas Guía para la Reflexión:
1. *¿Por qué todo ángulo inscrito en una semicircunferencia es recto ($90^\circ$), y cómo se aplica esta propiedad en la construcción de escuadras topográficas?*
2. *¿Por qué en una corona circular el área depende únicamente de la longitud de la cuerda tangente y no de los valores individuales de los radios?*
3. *¿Cómo simplifica el Teorema de Pitot el cálculo de linderos en terrenos cuadrangulares que rodean a un reservorio circular?*

---

## 7. Formulario Resumen

| Teorema / Figura | Configuración Geométrica | Expresión Matemática Rigurosa |
| :--- | :--- | :--- |
| **Radio y Tangente** | Punto de contacto $T$ | $OT \perp \mathcal{L}_T$ |
| **Tangentes Exteriores** | Tangentes desde punto exterior $P$ | $PA = PB$ |
| **Teorema de Poncelet** | Triángulo rectángulo con inradio $r$ | $a + c = b + 2r$ |
| **Teorema de Pitot** | Cuadrilátero circunscrito | $AB + CD = BC + AD$ |
| **Ángulo Central** | Vértice en el centro $O$ | $\alpha = \text{m}(\widehat{AB})$ |
| **Ángulo Inscrito** | Vértice en la circunferencia | $\alpha = \frac{\text{m}(\widehat{AB})}{2}$ |
| **Ángulo Interior** | Cruce de dos cuerdas interiores | $\alpha = \frac{\text{m}(\widehat{AB}) + \text{m}(\widehat{CD})}{2}$ |
| **Ángulo Exterior** | Secantes o tangentes exteriores | $\alpha = \frac{\text{m}(\widehat{AB}) - \text{m}(\widehat{CD})}{2}$ |
| **Teorema de las Cuerdas** | Cuerdas secantes en $P$ | $AP \cdot PB = CP \cdot PD$ |
| **Teorema de las Secantes** | Secantes desde $P$ exterior | $PA \cdot PB = PC \cdot PD$ |
| **Teorema de la Tangente** | Tangente $PT$ y secante $PAB$ | $PT^2 = PA \cdot PB$ |
| **Longitud de Circunferencia** | Radio $R$ o diámetro $D$ | $L = 2\pi R = \pi D$ |
| **Área del Círculo** | Radio $R$ | $A = \pi R^2$ |
| **Área del Sector Circular** | Ángulo central $\theta$ | $A = \frac{\pi R^2 \theta}{360^\circ} = \frac{L_{\text{arco}} \cdot R}{2}$ |
| **Área de Corona Circular** | Cuerda tangente $L$ o radios $R, r$ | $A = \pi(R^2 - r^2) = \frac{\pi L^2}{4}$ |

---

## 8. Observaciones de la Auditoría

Revisión ejercicio por ejercicio de los 45 ítems del fascículo. Resultado: 3 clave(s) corregida(s) y 4 ítem(s) reescrito(s) para que tengan solución y una opción correcta.

| Ejercicio | Clave original | Clave corregida | Estado | Observación |
| :---: | :---: | :---: | :--- | :--- |
| **32** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **34** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |
| **36** | C | C | Corregida | Se corrigió la base mayor a $36$ m: en el trapecio rectángulo circunscrito $h=\frac{2ab}{a+b}=24$ m (C). |
| **44** | C | B | Corregida | El resultado no coincide con la clave anterior; la opción correcta es B. |

**Claves sin cambios:** 42 de 45. Todos los ítems cuentan ahora con una solución válida y una opción correcta entre A–E.
