# -*- coding: utf-8 -*-
"""Construye el banco del Simulacro 1 — ENP Beca 18 2018 (Editora Delta).

Fuente: temarios/2027/2018+ simulacros.pdf, paginas 7-11 del PDF
(Simulacro 1 del indice, clave oficial en la pagina 11).

Criterio de fidelidad:
  * Razonamiento Matematico (1-30): enunciado y opciones transcritos como
    texto (formulas en LaTeX). Solo se aporta la figura cuando el item la
    necesita: recorte del grafico en 22, 27 y 28, y una version vectorial
    (SVG) del grafico en 16.
  * Comprension Lectora (31-60): texto transcrito y normalizado a partir de
    la capa OCR del PDF; los pasajes se conservan con su redaccion original.
  * La clave oficial se copia tal como esta impresa.
"""
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b18 import bank as b18bank, console, crop as b18crop  # noqa: E402

import fitz  # noqa: E402

console.setup_console()

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'temarios', '2027', '2018+ simulacros.pdf')
OUT_IMG = os.path.join(ROOT, '_static', 'simulacros', 'img', '2018-s1')
OUT_JSON = os.path.join(ROOT, 'scratch', 'exams', 'banks', '2018-s1.json')
PUB_JSON = os.path.join(ROOT, '_static', 'simulacros', 'banks', '2018-s1.json')

# (nombre, pagina 1-based, x0, y0, x1, y1)
# Recortes de Razonamiento Matematico: solo el grafico (o la expresion del
# item 2), nunca el item completo.
RM_CROPS = [
    # Item 22: solo la figura (columna 2).
    ('q22.png', 8, 281, 149, 390, 231),
    # Item 27: solo el grafico del cuadrado y el triangulo.
    ('q27.png', 8, 338, 449, 393, 535),
    # Item 28: solo el grafico de las rectas paralelas.
    ('q28.png', 8, 248, 570, 391, 648),
]

# (nombre, pagina 1-based, x0, y0, x1, y1)
CL_CROPS = [
    # Infografia del TEXTO XI (preguntas 58-60), pagina 11 columna 2.
    ('infografia-xi.png', 11, 235, 35, 414, 293),
]


def crop_rm():
    doc = fitz.open(PDF)
    b18crop.crop_boxes(doc, RM_CROPS, OUT_IMG, zoom=6, verbose=True)
    doc.close()


def crop_cl():
    doc = fitz.open(PDF)
    b18crop.crop_boxes(doc, CL_CROPS, OUT_IMG, zoom=4, verbose=True)
    doc.close()


MATH_RE = re.compile(r'\$([^$]+)\$')


def tex(s):
    """Convierte $...$ (LaTeX) a los delimitadores \\(...\\) que usa el motor.

    El motor carga MathJax v3 con inlineMath = [['\\\\(', '\\\\)']] porque el
    simbolo $ queda reservado para los soles ("S/."); por eso las formulas
    deben escribirse entre \\( y \\).
    """
    return MATH_RE.sub(lambda m: '\\(' + m.group(1) + '\\)', s)


def q(id, stem, options, answer, section, passage=None, images=None):
    d = {'id': id, 'stem': stem, 'options': options, 'answer': answer, 'section': section}
    if passage is not None:
        d['passage'] = passage
    if images:
        d['images'] = images
    return d


# --------------------------------------------------------------------------
# PASAJES
# --------------------------------------------------------------------------
PASSAGES = [
    {
        'id': 1,
        'title': 'Texto I — El Museo de los Objetos Fantásticos',
        'html': """El Museo de los Objetos Fantásticos está consagrado a las cosas inverosímiles que evoca el habla cotidiana. Por ahora, la pieza del mes es un mini fenómeno meteorológico que todos conocemos bien.

Armar una tormenta en un vaso de agua es fácil: junte agua, cucharita, y bata a velocidades superiores a los 200 kilómetros por hora. Un poco de azúcar no estaría mal. Por lo menos, así conseguimos lo que exhibimos en el Museo de los Objetos Fantásticos: pura tecnología nacional.

¿Cómo, que no puede? ¡Qué curioso! A juzgar por las noticias, hacer tormentas en un vaso de agua es la cosa más común y silvestre del mundo; un arte bien desarrollado en los más diversos países y en las más diversas lenguas. Véase, por ejemplo, a Ignacio Walker, líder de la oposición chilena, hace algunas semanas, explicando que el no asistir a una reunión convocada por el presidente Piñera no era ninguna catástrofe: «Estaremos siempre disponibles para continuar por la vía del diálogo... No vamos a hacer una tormenta en un vaso de agua».

Igualmente, en Alemania, la canciller Angela Merkel reaccionó con tranquilidad a fuertes críticas del ex líder Helmuth Kohl. De acuerdo al periódico Maerkische Allgemeine, «el asunto no pasa de ser una tormenta en un vaso de agua», y Merkel ha demostrado «tener los nervios en orden». Por cierto, los alemanes, como nosotros, hacen sus tormentas en vasos de agua (Sturm im Wasserglas) y los franceses también (tempête dans un verre d'eau).

Los ingleses, en cambio, y como para fortalecer el estereotipo, las hacen en tazas de té: así, poco antes de perder el poder, el ex primer ministro británico Gordon Brown decía —para tranquilizar los ánimos— que las resistencias hacia su liderazgo eran «poco más que una tormenta en una taza de té» (storm in a teacup) y que no les prestaba atención porque estaba ocupado en «las verdaderas tormentas». Intriga a los curadores de nuestro museo saber que los ingleses hablan también de una «tormenta en una tetera» (storm in a teapot). Sin duda, no se puede negar la afición británica por el té.""",
    },
    {
        'id': 2,
        'title': 'Texto II — Menú Perú',
        'html': """La nueva web de cocina de El Comercio presenta una selección de recetas sencillas e innovadoras para festejar este Día del Niño de manera distinta. Menú Perú propone disfrutar junto a los engreídos del hogar de un día diferente y divertido. En esta web encontrará más de 60 recetas ricas y fáciles para incentivar el gusto por la cocina en los niños y compartir en familia. Este domingo, Día del Niño, visite Menú Perú y consulte la lista completa de recetas para mini chefs.""",
    },
    {
        'id': 3,
        'title': 'Texto III — El dibujo y la noción de espacio en el niño',
        'html': """Los dibujos de un niño entre los 4 y 7 años, es decir, durante el primer nivel de representación, señalan un concepto de espacio muy diferente del que tiene un adulto. A primera vista, los objetos en el espacio tienden a estar en un orden un tanto caprichoso. No obstante, una observación más cuidadosa demuestra que el niño concibe el espacio como aquello que lo rodea. En otras palabras, los objetos aparecerán arriba, abajo o uno junto a otro, en la forma en que el niño los comprende. No se ve a sí mismo en el suelo junto a otros objetos que también están en el suelo; desplazando la mirada con él como centro de todo, el niño percibe cada uno de los elementos que lo circundan. No se ha establecido ninguna relación espacial fuera del concepto que tiene el niño de sí mismo. El espacio se concibe, de este modo, como algo que está a su alrededor.

Es muy interesante lo que para el niño de esta etapa significa el espacio, en el que repara en tanto es relacionado primordialmente consigo mismo y su propio cuerpo. A este vínculo entre el propio cuerpo y el espacio circundante se lo denomina espacio corporal. Más adelante, la comprensión de este concepto cambiará en sus dibujos hasta llegar a distinguirse en ellos el espacio de los objetos como algo ya distinto y posicionado en su propio espacio.""",
    },
    {
        'id': 4,
        'title': 'Texto IV — El control de la malaria en la India',
        'html': """Uno de los programas que se va adentrando cada vez más en las remotas zonas rurales es la campaña de erradicación y control de la malaria. En la India, la autora quedó impresionada por el sentimiento de liberación de las fiebres recurrentes que expresaban los pobladores de muchas aldeas como resultado de los programas de control de la malaria. Hay una zona en que el eficaz control de la malaria va teniendo el efecto de estimular a la gente a pedir servicios sanitarios en otros campos. La gente de la aldea comienza a tomar conciencia de su responsabilidad de cooperar con los problemas de control. De otra parte, de la India se informó con respecto al agente de supervisión de la malaria, que la gente presta atención a lo que este hace y se queja a las autoridades sanitarias si deja de visitar la aldea a intervalos regulares.""",
    },
    {
        'id': 5,
        'title': 'Texto V — Los amish y la tecnología',
        'html': """Una de las cosas que más llama la atención sobre los amish es su resistencia al uso de la tecnología. No usan autos, teléfonos (usan una cabina de teléfono comunitario, solo para casos de extrema urgencia), televisores, radio ni agua corriente, entre otras cosas. ¿Cómo es eso? Regla número uno, la comunidad amish no desea tener una relación física permanente innecesaria con el mundo exterior; regla número dos, si algo no es estrictamente necesario, para qué tenerlo o hacerlo.

Las consecuencias de estas reglas pueden ser evidentes, pero igual sorprende mucho ver a estos expertos granjeros manejando sus carretas tiradas a caballo en medio de sus vecinos «normales» que usan Ford, Chrysler o Chevrolet. O verlos trabajar la tierra con un viejo arado arrastrado por un par de mulas, o ver sus granjas sin cables eléctricos.

Para la calefacción en invierno o enfriar los alimentos en verano usan gas natural embotellado. Claro que las heladeras a gas son unos armatostes viejos; sin enchufe no les quedan muchas opciones.

¿Cómo hacen entonces para que las cosas «se muevan»? Como hacían hace mucho tiempo. Sus fuentes de energía son agua (que mueve la rueda del molino), el viento (que mueve las aspas del molino de viento) y el gasoil (acá le llamamos gasolina).

En realidad esto último es un parche que le tuvieron que hacer a la tradición cuando en 1950 las compañías lecheras les exigieron que usaran máquinas de ordeñar, en vez de hacerlo a mano. A pesar de no hacer uso de la tecnología, si los necesitan usan los servicios médicos otorgados por el Estado (pagan impuestos como todos). Es más, algunos bebés pueden llegar a nacer en un hospital si hace falta, pero como no tienen planes de medicina prepaga, tratan de estar en el hospital lo menos posible para evitar gastos desmedidos.

Los amish residen en unas 22 comunidades cerradas en EEUU, así como en Ontario (Canadá).

Las mayores concentraciones de amish en EEUU están en los Condados de Holmes (Ohio) y Condado de Lancaster (Pensilvania). Por cantidad en cada estado, la población amish más grande está en Ohio, y la segunda más grande en Pensilvania. Hay unos 228.000 amish en EEUU y otros 1.500 en Canadá.

Algunos amish del grupo Beachy Amish han emigrado a América Central en un intento de huir de las influencias de la sociedad moderna, fundando un establecimiento importante cerca de San Ignacio, en Belice. Los grupos amish más estrictos son los denominados Nebraska Amish, Troyer Amish y los grupos Swartzentruber Amish. La lengua usada en todos los hogares amish tradicionales y en muchos hogares Beachy es el alemán de Pensilvania; el inglés se utiliza con el mundo exterior.""",
    },
    {
        'id': 6,
        'title': 'Texto VI — Apolo',
        'html': """Apolo es una figura de extraño origen. Su nombre no aparece en las tablillas micénicas, y su etimología es oscura. Probablemente se introdujo en el panteón helénico a mediados del segundo milenio, viniendo de Asia menor. Era acaso en su origen un dios de los rebaños. Todavía en el Himno Homérico a Hermes se menciona que poseía una manada de bovinos. No deja de ser paradójico que este dios, que por su aspecto grácil y sereno parecía encarnar el ideal griego de la pureza y la perfección juvenil, fuera de origen oriental, un asiático adoptado y extraordinariamente bien adaptado.

Es hijo de Zeus y de Leto, que lo dio a luz junto a su hermana Ártemis, en la isla de Delos, una isla santa desde que se ofreció como asilo para ese parto de la amada de Zeus, a la que perseguían los rencores de Hera. Allí, pues, junto a la palmera sagrada, nacieron los dos dioses: Apolo y Ártemis. Luminosos, resplandecientemente rubios, ágiles y montaraces, comparten la afición al arco y las flechas. El arco es un símbolo del poder distante, certero pero silencioso.""",
    },
    {
        'id': 7,
        'title': 'Texto VII — La extinción de los neandertales',
        'html': """La forma en la que se extinguieron los neandertales no se ha precisado aún bien. Se cree que pueden haber existido varios mecanismos que intervinieron en este proceso. Algunos autores han supuesto una extinción por confrontación directa con los Homo sapiens sapiens. Esta es una explicación que responde más bien a analogías literarias o cinematográficas, pero que no se corresponde con las evidencias que existen respecto a que los grupos humanos tipo neandertal convivieron decenas de miles de años en Próximo Oriente con otros de tipo sapiens sapiens. Por otro lado, la sustitución de un grupo por otro en Europa fue un proceso a largo plazo milenario. Y por último no hay pruebas de enfrentamientos violentos generalizados en el Paleolítico.

En otras ocasiones, se ha argumentado que la extinción de los hombres de Neandertal estaría causada por la mayor competencia de los sapiens sapiens, que estaban mejor adaptados para sobrevivir, y el primitivismo típico de los neandertales, una especie previa a la del hombre moderno representado por el nuevo sapiens. Las innovaciones técnicas que aportaron, la mejor organización social y económica que tenían y una elaboración conceptual más desarrollada —reflejada en el arte rupestre— convertiría a los sapiens sapiens en unos competidores imbatibles para los neandertales.

Una última propuesta sobre la desaparición de los neandertales sugiere que se habría dado un proceso de hibridación con los sapiens sapiens. No obstante, hay pocos rasgos anatómicos tipo neandertal entre las poblaciones europeas posteriores, lo contrario de lo que debería esperarse en caso de que estas poblaciones fueran el resultado de una mezcla entre neandertales y sapiens sapiens.""",
    },
    {
        'id': 8,
        'title': 'Texto VIII — La papa',
        'html': """En días pasados, el ministro de Agricultura, como presidente de la Comisión Nacional Multisectorial de las actividades del «Año Internacional de la Papa», dijo que tiene como uno de sus principales proyectos incrementar en el Perú el consumo anual de ese tubérculo de 77 kilogramos a más de 100 per cápita. ¿Sorprende? Seguramente no, porque la papa es un producto originario de nuestro país, del cual nos sentimos muy orgullosos. No obstante, no solo en el Perú se promueve su producción y consumo. Por ejemplo, en naciones europeas como Rusia, Polonia, Irlanda y los Países Bajos, el consumo de papa per cápita oscila entre los 100 y 140 kilos. ¿Cuáles son las razones de esta popularidad? Gracias a la cantidad de calcio, hierro, azufre, potasio y vitamina C que contiene, más aun si se come con cáscara, la papa es una buena fuente de energía, pues proporciona cerca de la mitad de nutrientes necesarios para la ingesta diaria. Por otro lado, si bien el Gobierno promueve la producción y el consumo de papa, debemos indicar que este sigue aumentando en el Perú y en el mundo, pero no en forma saludable, sino sobre todo bajo las presentaciones fast food, lo cual hace que pierda sus nutrientes naturales y se asocie en forma adictiva con el consumo de grasa y bebidas con exceso de carbohidratos. ¿Es esto responsabilidad del Gobierno?

De todo lo anterior se infiere que el consumo de papa debe ser promovido por todos los ciudadanos, sobre todo los padres de familia y los educadores, quienes deben secundar la labor de las autoridades promoviendo su consumo saludable en el hogar y en los centros educativos en desmedro de sus presentaciones fast food, que reducen el potencial alimentario de nuestra planta.""",
    },
    {
        'id': 9,
        'title': 'Texto IX — La Ilíada',
        'html': """Redactada en el siglo VIII a. C., la Ilíada está compuesta por distintos poemas elaborados oralmente en los cuatro o cinco siglos anteriores. Su tema es la guerra de Troya; la expedición de los griegos, mandados por Agamenón contra la ciudad de Troya y su rey Príamo, defendidos por el valiente Héctor, el hijo del rey. Se trata de vengar la afrenta infligida a los griegos por el troyano Paris, otro hijo de Príamo, ya que él raptó a Helena, la joven esposa de Menelao, hermano de Agamenón. En medio de esta lucha sin cuartel, una de las historias más destacables de la obra es la que se refiere a las hazañas del mejor de los griegos, Aquiles, y su enfrentamiento con el valiente Héctor, con lo que se anticipaba la caída de la ciudad asediada.""",
    },
    {
        'id': 10,
        'title': 'Texto X — Los sentidos de los insectos',
        'html': """El mundo de los insectos está formado por patrones de olores y sabores, más que de luz y sonido.

Gusto, tacto y oído son funciones que corresponden a unos insignificantes pelillos que cubren su cuerpo y generalmente se concentran en las patas, en las antenas y en la boca. Aunque los insectos carecen de nariz, su sentido del olfato es mucho más agudo de lo que podemos imaginar.

Huelen principalmente con sus antenas, dotadas además del sentido del tacto, el gusto y/o el oído. Pueden también gustar a través de células quimiosensibles situadas en las patas y en la boca. Su sensibilidad al sonido varía enormemente entre las especies.

Algunos perciben solo vibraciones con ayuda de sus antenas, mientras que otros poseen estructuras más complejas dotadas de membranas vibrantes que estimulan los nervios fonorreceptores de manera parecida a como ocurre en el oído humano. Estas «orejas» de los insectos pueden, sin embargo, detectar una gama de frecuencias mucho más amplia que nuestros oídos.""",
    },
    {
        'id': 11,
        'title': 'Texto XI — Las «chalacasas» de Ventanilla',
        'html': """[[img:infografia-xi.png]]

En menos de un año, podría levantarse en Ventanilla el primer conjunto habitacional hecho completamente de «chalacasas», viviendas prefabricadas hechas a partir de contenedores. El proyecto, una iniciativa municipal que cuenta con amplio respaldo de la población, viene siendo estudiado por diversos especialistas y se espera que para principios del próximo año la primera «Ciudad de Acero» albergue a unas 120 familias en viviendas diseñadas para brindar techo seguro y servicios básicos.""",
    },
]

# --------------------------------------------------------------------------
# PREGUNTAS
# --------------------------------------------------------------------------
# (id, enunciado, opciones, clave, figuras)  — enunciados transcritos del
# escaneo; formulas en LaTeX y figuras como recortes (solo el grafico).
RM = [
    (1,
     'A un cine asisten 399 personas entre hombres, mujeres y niños. El número de hombres es el '
     'quíntuplo del número de mujeres y este es el triple del número de niños. ¿Cuántos hombres hay?',
     ['21', '63', '325', '315'], 'D', None),
    (2,
     'Si:\n'
     '$M = 2 - \\dfrac{1}{4} + 4 - \\dfrac{\\sqrt{12}}{\\sqrt{3}} + \\dfrac{8^{2/3}}{2}$\n'
     '$N = 2^{-1} \\cdot 3^{-1}$\n'
     'Calcular: $\\left(M - \\dfrac{3}{4}\\right)\\left(N + \\dfrac{4}{3}\\right)$',
     ['$\\dfrac{3}{2}$', '6,6', '7,5', '$\\dfrac{15}{8}$'], 'C', None),
    (3,
     'Sabiendo que $E = A\\cdot B^2$, ¿cómo varía $E$ si $A$ disminuye 25 % y $B$ disminuye 20 %?',
     ['Disminuye 48 %', 'Disminuye 52 %', 'Disminuye 45 %', 'Disminuye 65 %'], 'B', None),
    (4,
     'Si al comprar tela me hubieran hecho un descuento del 15 % en el precio, hubiera podido '
     'comprar 6 metros más. ¿Cuántos metros de tela compré?',
     ['34', '40', '42', '45'], 'A', None),
    (5,
     'Se colocan en fila 945 000 esferas de 0,8 cm de radio, una al lado de otra. ¿Cuál es la '
     'longitud de esta fila de esferas?',
     ['1512 m', '15,12 km', '151 200 cm', '1 510 000 mm'], 'B', None),
    (6,
     'Una compañía fabrica un producto tipo A cada 12 min, uno tipo B cada 18 min y uno tipo C '
     'cada 60 min. Si a las 3:30 a. m. se empieza a fabricar un producto de cada tipo, ¿a qué hora '
     'volverán a fabricar un producto de cada tipo simultáneamente?',
     ['4:30 a. m.', '6:30 a. m.', '7:30 a. m.', '8:00 a. m.'], 'B', None),
    (7,
     'Un juego consiste en lanzar un dado 2 veces, y se gana si la suma de puntos obtenidos es 11. '
     '¿Cuál es la probabilidad de ganar?',
     ['$\\dfrac{7}{12}$', '$\\dfrac{4}{9}$', '$\\dfrac{1}{4}$', '$\\dfrac{1}{18}$'], 'D', None),
    (8,
     'El promedio aritmético de cinco números es diez. Si consideramos un sexto número, dicho '
     'promedio aumenta en dos unidades. Calcule el sexto número.',
     ['55', '50', '22', '72'], 'C', None),
    (9,
     'En la academia MAPRIS se desea comprar no más de 3 plumones para pizarra entre negros y '
     'rojos. Si se debe comprar al menos uno de cada color, ¿de cuántas maneras se puede efectuar '
     'la compra?',
     ['2', '3', '4', '5'], 'B', None),
    (10,
     '¿Cuál es la probabilidad de que al ordenar en fila a 2 hombres y 2 mujeres, los 2 hombres '
     'estén juntos?',
     ['$\\dfrac{3}{4}$', '$\\dfrac{1}{4}$', '$\\dfrac{1}{3}$', '$\\dfrac{1}{2}$'], 'D', None),
    (11,
     'Reducir:\n'
     '$E = \\sqrt{\\left(\\dfrac{1}{3}\\right)^{-3} + \\left(\\dfrac{2}{5}\\right)^{-2} + '
     '\\left(\\dfrac{4}{11}\\right)^{-1}}$',
     ['36', '9', '6', '27'], 'C', None),
    (12,
     'Si se cumple que:\n$\\begin{cases} x + y = 46 \\\\ xy = 30 \\end{cases}$\nCalcule $x^2 + y^2$.',
     ['2116', '2176', '2056', '2086'], 'C', None),
    (13,
     'Si $x_1$, $x_2$ son las raíces de la ecuación, en variable $x$:\n'
     '$2(x+1)^2 - x = 2x\\left(\\dfrac{x}{2}+5\\right) + 3(x-9) + 7$\n'
     'Halle: $x_1 + x_2$.',
     ['10', '$-10$', '$-5$', '5'], 'A', None),
    (14,
     'Considere el sistema de ecuaciones:\n'
     '$\\begin{cases} \\dfrac{x}{2} + \\dfrac{y}{3} = 5 \\\\ x - y = 1 \\end{cases}$\n'
     'Halle $x/y$.',
     ['$\\dfrac{32}{5}$', '$\\dfrac{27}{32}$', '$\\dfrac{27}{5}$', '$\\dfrac{32}{27}$'], 'D', None),
    (15,
     'Reduzca la siguiente expresión y dé como respuesta el numerador obtenido:\n'
     '$\\dfrac{8-x^2}{x-2} + \\dfrac{3x-10}{x+3} + \\dfrac{x^3+8x}{(x-2)(x+3)}$',
     ['50', '2', '5', '44'], 'D', None),
    (16,
     'En la siguiente figura, se muestra la gráfica de la función $f$.\n'
     'Halle la regla de correspondencia de $f$.',
     ['$f(x) = \\dfrac{2}{3}x + 2$', '$f(x) = -\\dfrac{2}{3}x + 2$',
      '$f(x) = -x + \\dfrac{2}{3}$', '$f(x) = -2x + 3$'], 'B', ['q16.svg']),
    (17,
     'A un paseo van 53 personas entre adultos y niños. Si el precio del pasaje de un adulto es '
     'S/. 10, el de un niño es S/. 7,5 y el costo del paseo es S/. 480, calcule la diferencia '
     'entre la cantidad de adultos y niños.',
     ['11', '12', '13', '14'], 'C', None),
    (18,
     'Dada la igualdad:\n'
     '$\\dfrac{4x-2}{x^2-x-6} = \\dfrac{A}{x+2} - \\dfrac{B}{x-3}$\n'
     'Halle: $A + B$.',
     ['2', '3', '0', '1'], 'C', None),
    (19,
     'Dentro de 33 años, la suma de las edades de un padre y su hijo será 138 años. Si hace 10 '
     'años la diferencia de sus edades era 32 años, halle la edad actual del padre.',
     ['20 años', '72 años', '52 años', '32 años'], 'C', None),
    (20,
     'Si se cumple que: $a + b = 15$, $a^3 + b^3 = 885$.\nHalle: $ab$.',
     ['166', '$\\dfrac{166}{3}$', '$\\dfrac{163}{3}$', '163'], 'B', None),
    (21,
     'Convertir $\\dfrac{9}{\\pi}$ grados sexagesimales a radianes.',
     ['$\\dfrac{1}{10}$ rad', '$\\dfrac{1}{5}$ rad', '$\\dfrac{1}{20}$ rad',
      '$\\dfrac{1}{4}$ rad'], 'C', None),
    (22,
     'En la figura, indicar el valor de $\\dfrac{2(x+y)}{xy}$.',
     ['$3\\sqrt{3}$', '$\\dfrac{3\\sqrt{3}}{5}$', '$\\dfrac{3\\sqrt{3}}{10}$',
      '$\\dfrac{3\\sqrt{3}}{20}$'], 'C', ['q22.png']),
    (23,
     'Un cuadrado y un hexágono regular tienen ambos un perímetro de 24 cm. Calcular la relación '
     'de sus áreas.',
     ['$\\dfrac{\\sqrt{3}}{2}$', '$\\sqrt{3}$', '$\\dfrac{\\sqrt{3}}{3}$',
      '$\\dfrac{\\sqrt{3}}{4}$'], 'A', None),
    (24,
     'En un triángulo rectángulo $ABC$ recto en $B$, la altura relativa a la hipotenusa es 6 y la '
     'proyección del cateto $AB$ sobre la hipotenusa es 3. Calcular la suma de catetos.',
     ['$6\\sqrt{5}$', '$9\\sqrt{5}$', '$12\\sqrt{5}$', '$15\\sqrt{5}$'], 'B', None),
    (25,
     'En un trapecio, las diagonales miden 6 cm y 8 cm, las cuales son perpendiculares entre sí. '
     'Calcular la base menor si la base mayor mide 8 cm.',
     ['4 cm', '2 cm', '3 cm', '5 cm'], 'B', None),
    (26,
     'En un triángulo $ABC$, $AB = 2$ u, $AC = 5$ u, $m\\angle BAC = 60°$. Calcular la medida del '
     'lado $BC$.',
     ['$\\sqrt{18}$', '$\\sqrt{19}$', '$\\sqrt{20}$', '$\\sqrt{21}$'], 'B', None),
    (27,
     'En el gráfico mostrado, $ABCD$ es un cuadrado y $ADE$ es un triángulo equilátero. '
     'Hallar $x$.',
     ['100°', '110°', '120°', '130°'], 'C', ['q27.png']),
    (28,
     'En el gráfico mostrado, $L_1$ y $L_2$ son paralelas. Calcular $x$.',
     ['130°', '70°', '90°', '110°'], 'D', ['q28.png']),
    (29,
     'Se tienen los puntos consecutivos $A$, $B$ y $C$ sobre una recta, desde un punto exterior '
     '$P$ se forma el triángulo equilátero $BPC$. Si $m\\angle PAC = 30°$ y $AC = 20\\sqrt{3}$ u, '
     'hallar el lado $AP$.',
     ['30 u', '20 u', '$15\\sqrt{3}$', '$10\\sqrt{3}$'], 'A', None),
    (30,
     'Se tiene un cilindro inscrito en una esfera. Si la altura del cilindro es igual al radio de '
     'la esfera, y el volumen de la esfera es $288\\pi$ cm³, calcular el volumen comprendido '
     'entre la esfera y el cilindro.',
     ['$154\\pi$', '$144\\pi$', '$126\\pi$', '$130\\pi$'], 'C', None),
]

QUESTIONS = []
for qid, stem, opts, ans, figs in RM:
    QUESTIONS.append(q(qid, tex(stem), [tex(o) for o in opts], ans, 'matematica', images=figs))

QUESTIONS += [
    # -------- COMPRENSIÓN LECTORA (31-60) --------
    q(31, 'Señale la serie verdadera:\n'
          'I. Los ingleses son conocidos por su afición al té.\n'
          'II. Ignacio Walker, líder del oficialismo chileno, no ve mayor problema en no haber asistido a una '
          'reunión con el presidente Piñera.\n'
          'III. Helmuth Kohl ha criticado duramente a la canciller alemana Angela Merkel, pero ella mantuvo la calma.',
      ['VVV', 'FFF', 'VFV', 'VFF'], 'C', 'lectura', passage=1),
    q(32, 'Señale la afirmación incorrecta.',
      ['Ignacio Walker fue invitado a una reunión con el presidente Piñera.',
       'La canciller Angela Merkel tiene en poca estima las declaraciones de Helmuth Kohl.',
       'Hubo ciertas resistencias al liderazgo del ministro Gordon Brown.',
       'En más de un país se puede hacer una tormenta en un vaso de agua.'], 'B', 'lectura', passage=1),
    q(33, '¿Cuál es la intención del texto anterior?',
      ['Presentar una nueva web de El Comercio destinada a los niños.',
       'Proponer a los lectores de El Comercio festejar el Día del Niño cocinando en casa.',
       'Incentivar a que los niños cocinen desde pequeños en casa.',
       'Invitar a visitar una nueva web de cocina por el Día del Niño.'], 'A', 'lectura', passage=2),
    q(34, '¿A quién está dirigido el texto anterior?',
      ['A padres de familia.', 'A niños.', 'A empresarios.', 'A cocineros.'], 'D', 'lectura', passage=2),
    q(35, '¿Cuál sería el tono predominante del texto anterior?',
      ['Informativo.', 'Propagandístico.', 'Insunuante.', 'Festivo.'], 'A', 'lectura', passage=2),
    q(36, 'Según el texto es verdadero:\n'
          'I. Un adulto en sus dibujos representa una noción de espacio esencialmente diferente de la que '
          'presenta cualquier niño.\n'
          'II. En el niño de 4 a 7 años, el espacio significa esencialmente espacio corporal y ve los objetos '
          'según su relación consigo mismo.\n'
          'III. Los niños de 4 a 7 años no parecen haber relacionado los objetos entre sí con exclusión de '
          'ellos mismos.',
      ['I y II', 'Solo II', 'II y III', 'Todas'], 'C', 'lectura', passage=3),
    q(37, 'Según el texto sería verdadero:\n'
          'I. El concepto de espacio puede variar a lo largo del aprendizaje de un niño.\n'
          'II. El niño debe pasar por varias etapas en su aprendizaje para poder comprender correctamente el '
          'espacio.\n'
          'III. Por medio del dibujo de un niño, es posible interpretar cuál es su visión del espacio.',
      ['Solo I', 'Solo I y II', 'Solo I y III', 'Solo II y III'], 'C', 'lectura', passage=3),
    q(38, 'La autora trata en este texto de:',
      ['Los procesos de control de la malaria en la India y sus efectos.',
       'La adaptación progresiva de las poblaciones rurales alejadas a los programas de salubridad.',
       'La penetración de los programas de control en las remotas zonas rurales.',
       'Las sugerencias y quejas que presentan los aldeanos a las autoridades sanitarias.'], 'A',
      'lectura', passage=4),
    q(39, 'Lo que impresionó a la autora, en la India, fue:',
      ['La satisfacción de los pobladores por haberse librado de las fiebres que les aquejaban.',
       'La actividad que desplegaba el agente de supervisión de la malaria.',
       'El resultado eficaz de los programas de control de la malaria.',
       'El sentimiento que expresaban los pobladores por la presencia de las fiebres.'], 'A',
      'lectura', passage=4),
    q(40, 'Que los aldeanos se hayan quejado por la ausencia prolongada del agente supervisor de la malaria '
          'significa:',
      ['Esta enfermedad ha recrudecido en los poblados.',
       'Dicho agente gozaba de su simpatía.',
       'Están cultivando su responsabilidad como verdaderos miembros de la aldea.',
       'Ninguna de las anteriores.'], 'D', 'lectura', passage=4),
    q(41, 'Marque la alternativa incorrecta:\n'
          'I. Los amish se resisten a todo contacto con la tecnología.\n'
          'II. Antes de 1950, los amish mantenían un seguimiento fiel de la tradición de no usar tecnología.\n'
          'III. A diferencia de los amish, la gente «normal» usa autos Ford, Chevrolet, entre otros.',
      ['Solo I y III', 'Solo I y II', 'Ninguna', 'Todas'], 'D', 'lectura', passage=5),
    q(42, 'Es correcto:',
      ['Quienes pagan impuestos pueden acceder a los servicios médicos estatales.',
       'Los amish consideran que si algo es necesario, no hay que tenerlo o hacerlo.',
       'Los amish se esfuerzan por economizar, siempre evitan gastos desmedidos.',
       'Todos los pobladores de Ohio son campesinos.'], 'A', 'lectura', passage=5),
    q(43, 'Acerca de la tecnología usada por los amish podría afirmarse:',
      ['Es implementada y modernizada cada vez que se cambian las leyes.',
       'Obedece a un ciego fundamentalismo religioso.',
       'Se basa, predominantemente, en la energía natural.',
       'Les disgusta, salvo el teléfono que usan con agrado.'], 'C', 'lectura', passage=5),
    q(44, '¿Cuál es el tema central del texto anterior?',
      ['El origen de Ártemis y Apolo.',
       'Las características de Apolo.',
       'El curioso origen y características de Apolo.',
       'La influencia de Oriente en la concepción griega de los dioses.'], 'C', 'lectura', passage=6),
    q(45, 'Según el texto es correcto:',
      ['Apolo aparece por primera vez en el panteón helénico a mediados del segundo milenio antes de Cristo.',
       'Apolo poseía una manada de bovinos, según diversas fuentes arcaicas.',
       'Apolo es hijo de Zeus y Leto, aquel lo dio a luz junto a su hermana Ártemis.',
       'El origen del nombre de Apolo no es claro.'], 'D', 'lectura', passage=6),
    q(46, 'El mejor título para el texto anterior es:',
      ['La verdadera causa de la extinción de los neandertales.',
       '¿A dónde se fueron los neandertales?',
       'El Neandertal: origen, evolución y causas probables de su extinción.',
       'Diversas hipótesis para explicar la extinción de los neandertales.'], 'D', 'lectura', passage=7),
    q(47, 'Según el texto anterior es correcto:',
      ['El hombre de Neandertal se extinguió debido a la mayor competencia del sapiens sapiens, el cual tenía '
       'una mejor organización económica y social.',
       'Las poblaciones europeas no presentan ningún rasgo anatómico propio del neandertal.',
       'La sustitución de los neandertales por los sapiens sapiens en Europa fue un proceso abrupto y '
       'repentino.',
       'El que la desaparición del Neandertal se haya dado por una confrontación con los sapiens sapiens es '
       'algo que parece propio de una película antes que algo real.'], 'D', 'lectura', passage=7),
    q(48, 'Señale la idea central del texto anterior:',
      ['Se ha argumentado que la extinción de los neandertales tuvo que ver con su escasa capacidad para '
       'competir con las mayores habilidades de los sapiens sapiens.',
       'Pese a que se han formulado varias respuestas, aún no es claro cómo se extinguió el hombre de '
       'Neandertal.',
       'Se ha propuesto que los neandertales se extinguieron por hibridación con los sapiens sapiens, pero la '
       'idea no parece tener sustento en los rasgos de la población europea actual.',
       'En realidad, la sustitución del neandertal por el sapiens sapiens fue un proceso lento y milenario.'],
      'B', 'lectura', passage=7),
    # El ejemplar impreso omite los enunciados I, II y III de este item
    # (defecto de la fuente original). Se redactan aqui a partir del Texto VII
    # respetando la clave oficial (B: solo II es verdadero).
    q(49, 'Se puede afirmar a partir del texto anterior:\n'
          'I. La confrontación directa con los Homo sapiens sapiens es la causa de la extinción de los '
          'neandertales que mejor se corresponde con las evidencias fósiles.\n'
          'II. Los grupos neandertales convivieron durante decenas de miles de años con grupos de tipo '
          'sapiens sapiens en el Próximo Oriente.\n'
          'III. La hibridación con los sapiens sapiens está respaldada por la gran cantidad de rasgos '
          'anatómicos neandertales que presentan las poblaciones europeas posteriores.',
      ['Solo I', 'Solo II', 'Solo I y II', 'Solo II y III'], 'B', 'lectura', passage=7),
    q(50, '¿Cuál es la síntesis argumentativa del texto?',
      ['La papa con cáscara contiene todos los nutrientes necesarios para la ingesta diaria; no obstante, suele '
       'consumirse más como fast food, lo cual hace que los esfuerzos del Gobierno sean inútiles.',
       'Consumir papa con cáscara asegura cerca de la mitad de nutrientes necesarios para la ingesta diaria; '
       'por ello, se debe promover su consumo, como viene sucediendo en los países desarrollados.',
       'Debido al potencial alimenticio de la papa, reconocida internacionalmente, y al aumento de su consumo '
       'inadecuado, los padres de familia y los educadores deben promover su consumo saludable en los hogares '
       'y escuelas del país.',
       'Comer papa es conveniente, porque asegura el consumo de calcio, hierro, azufre, potasio y vitamina C '
       'necesarios para la ingesta diaria, pero los esfuerzos del Gobierno resultan insuficientes para que '
       'este tubérculo llegue a todos los hogares.'], 'C', 'lectura', passage=8),
    q(51, '¿Qué afirmación refuerza la argumentación del texto?',
      ['El ministro de Agricultura ha resaltado, en el Día Internacional de la Papa, que este tubérculo es '
       'considerado uno de los cuatro alimentos básicos para el mundo.',
       'El exceso de grasa y bebidas con carbohidratos es un factor que aumenta el riesgo de desarrollar '
       'diversas enfermedades cardiovasculares.',
       'Consumir papa silvestre ha permitido que sobreviva un grupo de turistas que se perdieron por dos '
       'semanas.',
       'Los agricultores altoandinos han manifestado que los niños deben preferir las papas nativas, que son '
       'extraordinariamente nutritivas y deliciosas.'], 'B', 'lectura', passage=8),
    q(52, '¿Qué afirmación debilita la argumentación del texto?',
      ['Se ha descubierto que la papa que se produce para los grandes mercados es transgénica, por lo que hay '
       'que tener cuidado al consumirla.',
       'La papa no es tan nutritiva como se dice y, además, bajo cualquier presentación, es una fuente de '
       'carbohidratos que induce a problemas de sobrepeso, así que no es conveniente fomentar su consumo.',
       'El Colegio de Nutricionistas no está autorizado para hacer alguna recomendación, luego de que '
       'declarara a favor de una transnacional que vende productos transgénicos.',
       'Comer cáscara de papa puede ser perjudicial porque, si está mal lavada, puede producir enfermedades '
       'gastrointestinales.'], 'B', 'lectura', passage=8),
    q(53, '¿Cuál es la postura del texto anterior?',
      ['La papa tiene una gran cantidad de hierro, calcio, potasio, vitamina C y por ello su consumo es muy '
       'saludable.',
       'El Perú debe aumentar su consumo de papa de 77 a 100 kg per cápita en los siguientes años.',
       'Los padres de familia y educadores, especialmente, deben promover el consumo de papa provechoso por '
       'sobre las variedades de comida rápida menos nutritivas.',
       'El Perú debería consumir más papa que en la actualidad y superar a otras naciones que han llegado '
       'hasta los 140 kilos por cabeza al año.'], 'C', 'lectura', passage=8),
    q(54, '¿Cuál es una afirmación correcta del texto?',
      ['Héctor y no Paris pagó con su vida la afrenta hecha a los griegos por su hermano.',
       'Aquiles es el más importante de los griegos, a pesar de que el general es Menelao.',
       'En el bando de los griegos podemos contar a Agamenón, Menelao y Aquiles.',
       'Helena fue raptada contra su voluntad, y pidió venganza a su cuñado Agamenón.'], 'C',
      'lectura', passage=9),
    q(55, '¿Cuál es el tema central del texto?',
      ['Un resumen de una obra clásica griega: la Ilíada de Agamenón.',
       'La reseña sucinta del tema de la Ilíada.',
       'La Ilíada y sus personajes célebres, un resumen del final.',
       'Origen de la guerra de Troya y su temática general.'], 'B', 'lectura', passage=9),
    q(56, 'La idea central del texto anterior es:',
      ['La Ilíada es una obra redactada en el siglo VIII a. de C. cuyo tema es la guerra de Troya, cuyos '
       'personajes centrales son Agamenón, Príamo, Héctor y Aquiles.',
       'La Ilíada fue redactada en el siglo VIII y está basada en distintos poemas compuestos oralmente unos '
       'cuatro o cinco siglos antes.',
       'Una de las historias más destacables de la guerra de Troya es la que cuenta las hazañas del griego '
       'Aquiles y su combate con Héctor.',
       'La guerra de Troya cuenta la historia de la Ilíada, en la que Príamo raptó a Helena, mujer de Menelao, '
       'lo que provocó todo el conflicto.'], 'A', 'lectura', passage=9),
    q(57, '¿Cuál de las siguientes es una afirmación correcta según el texto?',
      ['La luz y el sonido no son estímulos captados por los insectos.',
       'Los pelillos en los insectos cumplen algunas funciones olfativas.',
       'Las antenas de los insectos cumplen varias funciones perceptivas.',
       'Los nervios fonocaptadores de los insectos son menos sensibles que los de los humanos.'], 'C',
      'lectura', passage=10),
    q(58, 'Se puede inferir del texto que:',
      ['Existen personas que, ante la carencia de los medios para construirse una vivienda, podrían apoyar '
       'las iniciativas de vivienda de su municipio.',
       'Se desconoce aún si los estudios de los especialistas confirman el amplio apoyo de la población a las '
       '«chalacasas».',
       'El municipio no se ha puesto a considerar lo humillante que puede resultar para un humilde poblador de '
       'Ventanilla el que le ofrezcan vivir en una casa hecha con los restos de un contenedor.',
       'Se necesita alrededor de $4000 para construir una «chalacasa» simple.'], 'A', 'lectura', passage=11),
    q(59, 'La intención central de la infografía es:',
      ['Mostrar las estructuras internas y externas de una «chalacasa», así como el valor de dichas viviendas.',
       'Mostrar las dimensiones y el diseño interior de una «chalacasa», así como sus proporciones en relación '
       'con su potencial habitante y los muebles del hogar.',
       'Convencer al lector de lo económicas que pueden resultar las «chalacasas» frente a otras alternativas '
       'de vivienda de uso popular.',
       'Motivar al lector a adherirse a la propuesta del municipio de Ventanilla.'], 'B', 'lectura', passage=11),
    q(60, '¿Qué se puede inferir de la infografía?\n'
          'I. Una chalacasa, si es habitada por más de una persona, llevará a una situación de hacinamiento.\n'
          'II. La estructura de la pared de una chalacasa es más compleja que la de una pared hecha con '
          'ladrillos.\n'
          'III. Se puede construir una chalacasa de uno o más pisos.\n'
          'IV. Para construir una chalacasa, basta con tener un contenedor en desuso y no menos de $1990.',
      ['I y II', 'Solo I', 'II, III y IV', 'I, II y IV'], 'C', 'lectura', passage=11),
]

BANK = {
    'year': 2018,
    'title': 'Simulacro 1 — ENP Beca 18 2018',
    'duration_min': 120,
    'sections': [
        {'id': 'matematica', 'label': 'Razonamiento Matemático', 'from': 1, 'to': 30},
        {'id': 'lectura', 'label': 'Comprensión Lectora', 'from': 31, 'to': 60},
    ],
    'passages': PASSAGES,
    'questions': QUESTIONS,
}


def main():
    # figuras de RM (solo los graficos) + infografia del TEXTO XI
    crop_rm()
    crop_cl()

    b18bank.write_bank(BANK, OUT_JSON)
    os.makedirs(os.path.dirname(PUB_JSON), exist_ok=True)
    shutil.copyfile(OUT_JSON, PUB_JSON)
    issues = b18bank.validate_bank(BANK, expected=60)
    assert not issues, issues
    print(b18bank.qa_report(BANK))
    print('OK  banco Simulacro 1 -> %s' % PUB_JSON)


if __name__ == '__main__':
    main()
