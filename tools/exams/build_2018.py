# -*- coding: utf-8 -*-
"""Construye el banco del Examen Reconstruido 2018 (Editora Delta).

Fuente: temarios/2027/2018+ simulacros.pdf  (examen real del 30-dic-2018,
paginas 3-7 del PDF; escaneo a 3 columnas).

Pipeline:
  1. Recorta las figuras y los recortes de formula/opciones ambiguas a
     _static/simulacros/img/2018/.
  2. Escribe el banco de 60 preguntas (texto + imagenes) con las claves
     oficiales confirmadas (RM 1-30, CL 31-60).
  3. Copia el banco a _static/simulacros/banks/2018.json.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from b18 import bank as b18bank, console, crop as b18crop, pdfio  # noqa: E402

console.setup_console()

PDF = r'temarios\2027\2018+ simulacros.pdf'
OUT_IMG = r'_static\simulacros\img\2018'
OUT_JSON = r'scratch\exams\banks\2018.json'
PUB_JSON = r'_static\simulacros\banks\2018.json'

# --------------------------------------------------------------------------
# 1) RECORTES  (nombre, pagina 1-based, x0,y0,x1,y1)  coords PDF (puntos)
# --------------------------------------------------------------------------
BOXES = [
    # ---- figuras de Geometria / Medida ----
    ('q10a.png', 3,  62, 688, 230, 777),    # grafico "NUMERO DE POSTULANTES" (fondo col1)
    ('q10b.png', 3, 242,  44, 408, 131),    # grafico "NUMERO DE INGRESANTES" (tope col2)
    ('q21.png', 3, 430,  80, 588, 174),     # cuadrado ABCD + triangulo CDE
    ('q22.png', 3, 424, 204, 543, 284),     # figura (hallar x)
    ('q23.png', 3, 436, 296, 526, 351),     # figura (a2+b2)
    ('q24.png', 3, 452, 372, 580, 440),     # figura AB/CD/BD/AD
    ('q28.png', 3, 424, 592, 535, 655),     # figura (calcular x)
    ('q29.png', 3, 420, 686, 529, 752),     # semicircunferencia
    ('q30.png', 3, 398, 786, 588, 820),     # cuadrado + segmento FE
    # ---- recortes de formulas / opciones graficas ----
    ('q07_o.png', 3,  78, 579, 231, 592),   # opciones de Q7
    ('q12_f.png', 3, 240, 252, 412, 338),   # item completo Q12 (expresion + condiciones + opciones)
    ('q13_f.png', 3, 240, 340, 412, 411),   # item completo Q13 (ecuacion + opciones)
    ('q15_f.png', 3, 236, 446, 412, 524),   # item completo Q15 (expresion + opciones)
    ('q18_f.png', 3, 236, 628, 412, 680),   # conjunto + opciones Q18
    ('q20_f.png', 3, 236, 712, 412, 778),   # item completo Q20
    ('q22_o.png', 3, 538, 202, 600, 286),   # opciones de Q22
    ('q29_o.png', 3, 528, 684, 598, 762),   # opciones de Q29
]

def crop():
    b18crop.crop_boxes(pdfio.open_pdf(PDF), BOXES, OUT_IMG, zoom=5)

# --------------------------------------------------------------------------
# 2) PASAJES
# --------------------------------------------------------------------------
PASSAGES = [
    {
        'id': 1,
        'title': 'Filipo y los lacones',
        'html': (
            'En el siglo IV antes de Cristo, Grecia estaba dividida en ciudades con su propio monarca. '
            'El rey de Macedonia, llamado Filipo, tuvo la belicosa —y a la larga buena— idea de unir a todas '
            'en una sola patria. Como ocurre en estos casos, no había manera de conversar amablemente para '
            'lograrlo y la única alternativa era la guerra.\n\n'
            'El futuro padre de Alejandro Magno (quien sin duda lo superó) se lanzó a la lucha desde el norte '
            'de Grecia. Al cabo de un tiempo y de quién sabe cuántos muertos, tenía casi todo bajo su poder y '
            'era llamado rey de Grecia. Pero digo "casi todo" porque le faltaba Esparta, un estado muy famoso '
            'por sus valientes guerreros. Los espartanos vivían en el sur, en una región conocida como Laconia. '
            'Por eso se les llamaba también lacones o laconios. Filipo, al frente de un ejército considerado '
            'invencible, ubicó sus apabullantes tropas en la frontera de Esparta. Y les mandó un mensaje a los '
            'lacones: "Si no se rinden de inmediato, mis tropas entrarán y saquearán sus tierras. Serán '
            'arrasados y perderán todo. ¿Comprenden lo que esto significa?". Los sitiados contestaron dos días '
            'más tarde. Era una carta lacrada. Al abrirla, Filipo leyó la respuesta a su pregunta. Una sola '
            'palabra resumía todo: "Si". Nada más. Lucharon y ganó Filipo, pero los espartanos —los lacones— '
            'demostraron un gran coraje y un estilo claro y breve. Nada más lacónico. Y así nos legaron este adjetivo.'
        ),
    },
    {
        'id': 2,
        'title': 'Las ventajas de la risa',
        'html': (
            'Los expertos dicen que la risa tiene múltiples ventajas:\n\n'
            '— Inmuniza contra la depresión y angustia.\n'
            '— Al reírnos estamos haciendo ejercicio: con cada carcajada se ponen en marcha cerca de 400 '
            'músculos, incluidos algunos del estómago que solo se pueden ejercitar con la risa.\n'
            '— Actúa como un masaje: la columna vertebral y cervicales, que es donde por lo general se acumulan '
            'tensiones, se estiran al reírnos. Además se estimula el bazo y se eliminan las toxinas. Con este '
            'movimiento el diafragma origina un masaje interno que facilita la digestión y ayuda a reducir los '
            'ácidos grasos y las sustancias tóxicas.\n'
            '— Nos limpia: al reírnos se lubrican y limpian los ojos con lágrimas. La carcajada hace vibrar la '
            'cabeza y se despeja la nariz y el oído.\n'
            '— La risa nos da felicidad: además de favorecer en la producción de endorfinas, también hay más '
            'encefalinas en el cerebro, ambos neurotransmisores (formados por cadenas de aminoácidos) que se '
            'encuentran sobre todo en el sistema límbico y cuya función es combatir el dolor.'
        ),
    },
    {
        'id': 3,
        'title': 'La inclusión',
        'html': (
            'Si buscamos en el diccionario de la Real Academia Española (DRAE) el significado de la palabra '
            'inclusión, encontramos "acción y efecto de incluir"; y si buscamos incluir, aparece "poner algo '
            'dentro de otra cosa". ¿Es esa inclusión de la que hablamos cuando decimos que las escuelas y la '
            'sociedad deben ser inclusivas? Nosotros, sinceramente, creemos que no; de hecho, no concebimos que '
            'algunas personas "deban ponerse dentro" de otro grupo que ya está y al cual se deban adaptar. '
            'Partimos de la premisa básica de que todo ser humano merece pleno desarrollo y respeto en su '
            'diferencia. Todos somos diferentes, cada una de las personas es diversamente hábil, nuestras '
            'capacidades son distintas. Respeto por las diferencias, aceptación de la diversidad es otra cosa.\n\n'
            'Durante años, hemos podido observar varios "milagros": personas diagnosticadas como ciegas '
            'incurables que hoy escriben y leen, niños autistas diagnosticados como irrecuperables que hoy viven '
            'como adultos, personas sin manos que tocan la guitarra con los pies o que escriben con la boca. No '
            'hay nada preestablecido; no hay diagnósticos convertidos en "epitafios".'
        ),
    },
    {
        'id': 4,
        'title': 'El voto obligatorio',
        'html': (
            'La escasa conciencia cívica no se ha ido incrementando. Por el contrario, ha crecido la '
            'informalidad y el comportamiento antisistema. En este contexto, el voto obligatorio es una de las '
            'pocas características que nos sigue uniendo y que nos hace partícipes de ciudadanía; y que, conforme '
            'se produzca un proceso de maduración democrática, nos irá enseñando que debemos ser absolutamente '
            'serios y responsables en la toma de nuestras decisiones.\n\n'
            'El voto facultativo nos haría perder el nivel real de la democracia. En este contexto, la '
            'ingobernabilidad es un peligro creciente que afecta el orden interno y la estabilidad que el país '
            'necesita para crecer y desarrollarse. Además de generar precedentes sobre la imposición de hechos '
            'ilegalmente consumados a las autoridades de turno. Así tenemos que estas son elegidas por los '
            'ciudadanos y en algunos casos revocadas por ellos en una comedia democrática cuando estos no han '
            'alcanzado un porcentaje importante de apoyo popular. Por ello, la legitimidad de las autoridades '
            'para generar gobernabilidad y acatamiento es fundamental: un alcalde elegido con el 30% de los votos '
            'sobre una votación en la cual solo el 40% de la población ha concurrido a votar es políticamente '
            'insostenible en el Perú. Esta afirmación no requiere mayor investigación, pues es pan de cada día, '
            'y si lo trasladamos a la elección presidencial o parlamentaria la cosa simplemente se repite.\n\n'
            'Pero la razón principal es "la igualdad ante la ley". El esnobismo hacia el voto voluntario o '
            'facultativo, promovido por algunos sectores, se sustenta fundamentalmente en que una gran parte de '
            'la población no tiene suficiente criterio para decidir libre y conscientemente por quién votar. Es '
            'decir, es un ciudadano de segunda categoría.\n\n'
            'Mientras en el Perú subsistan la mala educación, el analfabetismo, la marginación de sectores tan '
            'amplios de la población, la pobreza y la falta de oportunidades; así como la imposibilidad de '
            'informar adecuadamente a los ciudadanos de sus derechos, deberes y obligaciones, no es posible el '
            'voto facultativo, pues se convierte en un mecanismo desintegrador donde las autoridades carecerán '
            'de legitimidad y en el que el sistema irá cada vez vaciándose de contenido y de dignidad hacia la '
            'persona humana. La tan mentada igualdad, lamentablemente, no existe todavía.'
        ),
    },
    {
        'id': 5,
        'title': 'Discursos afectivos y discursos técnicos',
        'html': (
            'Los discursos afectivos son aquellos que centran su mensaje en la apelación a los sentimientos y '
            'emociones del destinatario (televidente, oyente, lector, consumidor de un bien, potencial elector, '
            'etc.) y, por lo general, su finalidad es persuasiva (convencerlo para que ayude en una campaña '
            'benéfica, para que compre un bien o servicio, para que vote por determinado candidato, para que '
            '"sienta la necesidad" de ver un programa de televisión, etc.). Podemos sostener que "así como la '
            'flauta hace bailar a la serpiente, el que habla desde el discurso afectivo manipula al oyente". '
            'Los discursos técnicos, en cambio, son, por lo general, más "desapasionados". No intentan, por lo '
            'general, "impactar" en las emociones del receptor, o por lo menos, no de manera tan intensa o '
            'explícita como en el caso de los discursos afectivos, y con frecuencia se elaboran en cumplimiento '
            'de una obligación informativa respecto de un superior o de una comunidad de personas que requieren '
            'estar informadas de ciertas decisiones o situaciones de una área o gestión.\n\n'
            'Ahora bien, la diferencia entre ambos discursos se atenúa con frecuencia. Por ejemplo, un discurso '
            'afectivo, para ser más convincente o para llegar a un público más crítico, puede revestirse de '
            'ciertos datos "objetivos" (como los odontólogos "con todas las de la ley" contratados para '
            'publicitar dentífricos, quienes recomiendan a sus pacientes y a su propia familia el usar '
            'determinada marca). Del mismo modo, el informe de un gerente puede presentar, con profusión de '
            'cifras, documentos y testimonios de origen diverso, la eficiencia de su gestión y la de su '
            'departamento, pero sugiriendo, con mayor o menor sutileza, de manera consciente o inconsciente, '
            'ciertas demandas o aspiraciones de su autor o de sus subordinados.'
        ),
    },
    {
        'id': 6,
        'title': 'El acompañamiento al enfermo terminal',
        'html': (
            'Generalmente el diagnóstico de una enfermedad terminal suele llegar luego de que una persona ha '
            'venido lidiando con una enfermedad crónica, después de haber asumido una serie de renuncias como la '
            'inevitable pérdida de la salud, de la estética, de alguna parte del cuerpo o alguna capacidad. Por '
            'ello el diagnóstico de una enfermedad terminal lleva al paciente al mayor de los duelos y lo '
            'contacta con angustias muy profundas.\n\n'
            'Para la familia, esta situación anuncia una despedida que, como cualquier otra, está teñida de dolor '
            'y de nostalgia. No obstante, la forma en que se dé este último acompañamiento dependerá del rol que '
            'ocupa la persona en la familia, cómo ha sido la dinámica familiar antes y durante la enfermedad y '
            'cómo se transmiten las despedidas.\n\n'
            'Al tener cada miembro de la familia angustias y problemas personales que necesitan de apoyo, lo '
            'ideal es que la familia como grupo pueda encontrar espacios para compartir y dejar otros para que '
            'cada cual pueda resolver aspectos que le son propios.\n\n'
            'En el acompañamiento, tanto para el paciente como para la familia, es esencial que se permitan '
            'cerrar las situaciones inconclusas y se den los espacios para las reconciliaciones.\n\n'
            'También es importante estar con el paciente durante su enfermedad, ofreciendo compañía y las '
            'atenciones cotidianas para su cuidado físico. Este espacio, además de aliviar al paciente, ofrecerá '
            'a los familiares la posibilidad de hablar con mayor naturalidad de la situación por la que '
            'atraviesa el paciente.\n\n'
            'En estos casos de crisis familiar, los psicólogos recomiendan que cada miembro, o toda la familia '
            'como grupo, puedan alimentarse de otras fuentes de energía (amigos), compartiendo su experiencia '
            'con otras personas fuera del círculo familiar. Señalan, también, que la negación, la '
            'sobreexposición de la enfermedad, el rencor, la depresión profunda y el aislamiento son actitudes '
            'que no ayudan a sobrellevar la situación, por lo que deben evitarse.\n\n'
            'El acompañamiento psicológico en enfermos terminales es necesario porque ayuda al paciente a '
            'entender y enfrentar su enfermedad. No obstante, también debe trabajarse con la familia para '
            'prepararla ante la inminente pérdida del ser querido y que pueda realizar el duelo. Este trabajo se '
            'realiza con técnicas de intervención que permiten la unidad familiar que, a su vez, permitirá la '
            'adecuada despedida. Y es que en estos casos, la comunicación no fluye porque hay emociones (miedo, '
            'tristeza, ira, negación) que no pueden ser expresadas adecuadamente debido a lo difícil de la '
            'situación. Entonces el psicólogo es el que promueve los espacios para que el paciente y su familia '
            'puedan liberar sus emociones.\n\n'
            '(Adaptado por Jorge Valenzuela de El Comercio).'
        ),
    },
    {
        'id': 7,
        'title': 'Piaget y la noción de tiempo',
        'html': (
            'Piaget hizo innumerables experimentos para establecer si la noción de tiempo subjetivo en el niño '
            'era inmediata o derivada, y si desde el principio se integraba o no con la velocidad, y llegó a la '
            'conclusión de que es el producto de una relación, penosamente adquirida a través de los años, entre '
            'velocidades y espacios. Encontró que el niño, en primer lugar, es capaz de ordenar acontecimientos, '
            'distinguiendo lo que sucedió antes de lo que pasó después, y en una segunda etapa, ya no solo ordena '
            'sucesos sino que también puede clasificar la duración del intervalo entre ellos. Esto no es todavía '
            'la mensurabilidad del tiempo, pero revela que el niño es ya capaz de revisar de memoria la secuencia '
            'de las duraciones. El niño no alcanza la capacidad de estimar el tiempo transcurrido o predecir '
            'grosso modo el que transcurrirá, hasta los cinco o seis años de edad. Esta tercera etapa sería pues, '
            'un proceso de síntesis entre las duraciones y la sucesión o secuencia de los acontecimientos. Antes '
            'de alcanzar estas etapas, cuando el niño está todavía en un nivel preoperacional, no le sirve de '
            'nada que se le permita observar relojes o cualquier otro dispositivo para medir el tiempo.'
        ),
    },
]

# --------------------------------------------------------------------------
# 3) PREGUNTAS
# --------------------------------------------------------------------------
def q(id, stem, options, answer, section, passage=None, images=None):
    d = {'id': id, 'stem': stem, 'options': options, 'answer': answer, 'section': section}
    if passage is not None:
        d['passage'] = passage
    if images:
        d['images'] = images
    return d

QUESTIONS = [
    # -------- RAZONAMIENTO MATEMÁTICO (1-30) --------
    q(1, 'La suma de las cifras del número ab es 16; al invertir el orden de sus cifras el número disminuye en 18. '
         'Hallar el producto de las cifras de dicho número.',
      ['6', '49', '72', '63'], 'D', 'matematica'),
    q(2, 'Si  (35x − 29)/(x² − 3x + 2) = A/(x − 1) + B/(x − 2)  para cualquier valor de x, distinto de 1 y 2, '
         'entonces el valor numérico de A·B es:',
      ['−290', '−200', '−246', '240'], 'C', 'matematica'),
    q(3, 'El promedio de 9 números es 12 y el promedio de 11 números es 16. ¿Cuál es el promedio de todos estos números?',
      ['15,3', '7,3', '13', '14,2'], 'D', 'matematica'),
    q(4, 'Si A y B representan las sumas respectivas de los pares positivos e impares positivos no mayores que 1000. '
         '¿Calcular A − B?',
      ['501', '500', '499', '999'], 'B', 'matematica'),
    q(5, 'En una urna hay 160 bolas; por cada 3 bolas blancas hay 20 negras y 17 rojas. ¿El número de bolas negras es?',
      ['12', '78', '46', '80'], 'D', 'matematica'),
    q(6, 'Cinco personas rinden un examen:\n'
         '· B tiene un punto más que C.\n'
         '· E tiene dos puntos menos que C.\n'
         '· C tiene un punto más que D.\n'
         '· B tiene dos puntos menos que A.\n'
         '· C tiene el mínimo aprobatorio.\n'
         '¿Quiénes aprobaron?',
      ['A, D, B', 'A, D, C', 'B, A, C', 'C, E, D'], 'C', 'matematica'),
    q(7, 'Un cubo y un cilindro tienen los mismos volúmenes. Si el radio de la base del cilindro es la mitad de la '
         'arista del cubo, la altura del cilindro es:',
      ['', '', '', ''], 'B', 'matematica', images=['q07_o.png']),
    q(8, 'Un número entero se representa en base dos como 110a1 y en base ocho como c3, donde a y c son dígitos. '
         'Hallar a + c.',
      ['8', '7', '3', '4'], 'D', 'matematica'),
    q(9, 'Sean A y B conjuntos tales que: A − B = {2, 4, 6, 8} ; A ∪ B = {1, 2, 3, …, 8}. '
         'Hallar la suma de los elementos de B.',
      ['12', '18', '16', '20'], 'C', 'matematica'),
    q(10, '¿Qué porcentaje del total representan los ingresantes?',
      ['60%', '30%', '45%', '55%'], 'D', 'matematica', images=['q10a.png', 'q10b.png']),
    q(11, 'Los números x e y satisfacen el siguiente sistema de ecuaciones:\n'
          '(x + 1)² + (y + 1)² = (10 − x − y)²   … (1)\n'
          'xy + x + y = 11   … (2)\n'
          'Calcular x + y.',
      ['1', '2', '3', '5'], 'D', 'matematica'),
    q(12, 'Calcular el valor de la expresión M, sabiendo que x − y = 2n y que x/(m+n) + y/(m−n) = 2.',
      ['', '', '', ''], 'D', 'matematica', images=['q12_f.png']),
    q(13, 'Dada la ecuación mostrada, hallar la suma de los valores de x que la satisfacen.',
      ['', '', '', ''], 'D', 'matematica', images=['q13_f.png']),
    q(14, 'Hallar la suma de la solución de: 2x⁴ − 5x³ + 5x − 2 = 0',
      ['3/2', '4/3', '2/3', '5/2'], 'D', 'matematica'),
    q(15, 'Al simplificar la expresión, ¿cuál es el resultado?',
      ['', '', '', ''], 'B', 'matematica', images=['q15_f.png']),
    q(16, 'Hallar los valores de x, si: |5x − 3| = |2x + 9|',
      ['4 y −6/7', '4 y 6/7', '−4 y 6/7', '4 y −6'], 'A', 'matematica'),
    q(17, 'Resolver la desigualdad: x² + 2x + 1 > 0',
      ['x > 0', 'x ∈ (−∞, 1) ∪ (1, ∞)', 'x ∈ (−∞, −1) ∪ (−1, ∞)', 'x ∈ ℝ'], 'C', 'matematica'),
    q(18, '¿Cuál de los siguientes intervalos representa la extensión del conjunto A?',
      ['', '', '', ''], 'A', 'matematica', images=['q18_f.png']),
    q(19, 'Si f(a) = a − 2 y F(a, b) = bᵃ + a, halle F(3, f(4)).',
      ['7', '6', '29', '11'], 'D', 'matematica'),
    q(20, 'Si se cumple la igualdad mostrada, determine el valor pedido:',
      ['', '', '', ''], 'B', 'matematica', images=['q20_f.png']),
    q(21, 'En la figura, ABCD es un cuadrado y CDE un triángulo equilátero; hallar "y − x".',
      ['15°', '30°', '45°', '50°'], 'B', 'matematica', images=['q21.png']),
    q(22, 'En la figura, hallar x.',
      ['', '', '', ''], 'D', 'matematica', images=['q22.png', 'q22_o.png']),
    q(23, 'En la figura, hallar: a² + b²',
      ['6', '36', '6√3', '16'], 'B', 'matematica', images=['q23.png']),
    q(24, 'En la figura, calcular la longitud del segmento AB. Si CD = 3, BD = 5 y AD = 1.',
      ['2', '3', '4√2', '4'], 'C', 'matematica', images=['q24.png']),
    q(25, 'La suma de las diagonales de un rombo es 62 cm y su área 336 cm². Calcular la longitud del lado.',
      ['24 cm', '20 cm', '25 cm', '30 cm'], 'C', 'matematica'),
    q(26, 'Cinco ángulos consecutivos en progresión aritmética forman un ángulo llano. Si el mayor es el cuadrado '
          'del menor, calcular la medida del menor ángulo.',
      ['4', '8', '6', '10'], 'B', 'matematica'),
    q(27, 'En un triángulo rectángulo ABC (recto en B) se inscribe el cuadrado PQRS (PS en AC). Si AP = 50 y '
          'SC = 72, calcula el lado del cuadrado.',
      ['40', '50', '60', '70'], 'C', 'matematica'),
    q(28, 'En la figura, calcular "x".',
      ['2', '3', '√3', '2√3'], 'D', 'matematica', images=['q28.png']),
    q(29, 'En la figura se muestra una semicircunferencia de diámetro AB. Si CH = 2BH y BC = 5u, calcular el '
          'radio de dicha circunferencia.',
      ['', '', '', ''], 'A', 'matematica', images=['q29.png', 'q29_o.png']),
    q(30, 'Halle el perímetro del cuadrado, si el segmento FE mide 10 m. M es punto medio de AD.',
      ['60 m', '45 m', '50 m', '64 m'], 'A', 'matematica', images=['q30.png']),

    # -------- COMPRENSIÓN LECTORA (31-60) --------
    q(31, '¿Cuál es el título del texto?',
      ['Las guerras de Filipo en Grecia',
       'Los laconios, un pueblo valiente',
       'Origen y significado del término "lacónico"',
       'Los espartanos vs Filipo de Macedonia'], 'C', 'lectura', passage=1),
    q(32, 'Según el texto es correcto:\n'
          'I. El ejército de Filipo era considerado casi invencible.\n'
          'II. Los lacones y espartanos lucharon apoyándose mutuamente contra Filipo.\n'
          'III. Alejandro Magno, aún no había nacido para estas fechas.',
      ['Solo I', 'Solo II', 'I y II', 'Solo III'], 'D', 'lectura', passage=1),
    q(33, 'Si los lacones no hubiesen contestado el mensaje de Filipo con un simple "Si", entonces:',
      ['Seguramente los macedonios se hubiesen apiadado de ellos.',
       'Probablemente el término "lacónico" no tuviese el significado que se le adjudica hoy en día.',
       'Los muertos por la batalla hubiesen sido menos.',
       'Filipo no se hubiese ensañado con ellos y los hubiera protegido.'], 'B', 'lectura', passage=1),
    q(34, 'La palabra APABULLANTE del texto, se podría reemplazar por:',
      ['Gigante', 'Desconcertante', 'Invencible', 'Ensordecedor'], 'B', 'lectura', passage=1),
    q(35, '¿Cuál es el título del texto?',
      ['Las causas de la risa', 'Los beneficios de la risa', 'Ríase de sus problemas',
       'Los componentes de una buena risa'], 'B', 'lectura', passage=2),
    q(36, 'Es cierto según el texto:\n'
          'I. Combatir el dolor es función del sistema límbico.\n'
          'II. Al reír ponemos en marcha más de 400 músculos del cuerpo.\n'
          'III. Los efectos de la risa pueden despejar nuestras fosas nasales.',
      ['Solo I', 'Solo II', 'Solo III', 'I y III'], 'C', 'lectura', passage=2),
    q(37, 'Del texto se infiere que:\n'
          'I. Los masajes podrían aliviar las tensiones.\n'
          'II. La risa ha sido objeto de estudio.\n'
          'III. Al reír los ojos se limpian.',
      ['Solo II', 'I y III', 'I y II', 'II y III'], 'C', 'lectura', passage=2),
    q(38, 'La palabra "epitafios" puede ser reemplazada por:',
      ['Condenas', 'Imposibles', 'Tumbas', 'Lápidas'], 'A', 'lectura', passage=3),
    q(39, '¿Qué puede considerarse como un milagro de acuerdo al texto?',
      ['Un niño que siempre vivió en la miseria, pero, al crecer, logró amasar una gran fortuna',
       'Un adolescente que formó una pandilla, pero, con los años, se reformó y se convirtió en pastor de una iglesia',
       'Un futbolista que sufre una lesión y, luego de mucha terapia, recupera sus habilidades',
       'Un compositor y director de orquesta que nació sordo'], 'D', 'lectura', passage=3),
    q(40, '¿Cuál es la opinión del autor del texto anterior?',
      ['Todos los seres humanos somos diferentes y, como tales, merecemos pleno desarrollo y respeto en nuestras diferencias.',
       'La definición de inclusión del DRAE está equivocada.',
       'La inclusión no puede consistir en que algunas personas deban ponerse dentro de un grupo que ya existe y adaptarse a este.',
       'La inteligencia es mucho más que el cociente intelectual.'], 'C', 'lectura', passage=3),
    q(41, '¿En qué se está basando el autor del texto?',
      ['No tenemos idea de qué es la inteligencia',
       'En el respeto a las diferencias',
       'No hay nada preestablecido',
       'El concepto de inclusión del DRAE no tiene en cuenta a la escuela o la sociedad'], 'B', 'lectura', passage=3),
    q(42, '¿Cómo podría reforzarse mejor la argumentación?',
      ['La escuela es uno de los primeros espacios en los que se debe practicar la inclusión.',
       'Ha habido gente que no era considerada inteligente, pero logró sorprender a todos.',
       'Los seres humanos somos valiosos por nuestras características diferenciadoras.',
       'Las definiciones del DRAE siempre están en proceso de mejora.'], 'C', 'lectura', passage=3),
    q(43, '¿Cuál de las siguientes afirmaciones debilita la argumentación del texto?\n'
          'I. Muchos diagnósticos de niños con problemas de desarrollo se han confirmado a través de los años.\n'
          'II. Está comprobado que los niños autistas entienden mejor ciertas expresiones faciales que los niños '
          'que no padecen de esta condición.\n'
          'III. La igualdad de oportunidades es una utopía.',
      ['Solo I', 'Solo II', 'Solo III', 'Ninguna'], 'D', 'lectura', passage=3),
    q(44, '¿Qué información sería contraria al texto expuesto?',
      ['No debemos analizar una situación en base a lo que la gente expresa como duda o vacilación.',
       'Todos los países se desarrollaron en base al libre albedrío del voto, vale decir, en la forma individual '
       'y libre de participar o no en comicios electorales.',
       'El voto facultativo nos puede dar mayor libertad también en el terreno espiritual.',
       'En el Perú realmente no existe una baja educación o cultura.'], 'B', 'lectura', passage=4),
    q(45, '¿Cuál es la intención del autor del texto?',
      ['Criticar', 'Ofender', 'Persuadir', 'Evaluar'], 'C', 'lectura', passage=4),
    q(46, '¿Qué quiso decir el autor del texto con la frase: "El voto facultativo nos haría perder el nivel real '
          'de la democracia"?',
      ['El voto voluntario nos hace ser irresponsables al elegir un candidato sin conocerlo previamente.',
       'Los electores no son realmente conscientes del voto y su connotación social, al escoger al candidato con '
       'menos pergaminos académicos.',
       'Elegir sobre votar o no podría hacernos entrar en una coyuntura complicada.',
       'El voto electoral es la única razón por la cual existe la democracia.'], 'C', 'lectura', passage=4),
    q(47, 'Señala un título adecuado al texto propuesto.',
      ['La conveniencia del voto facultativo', 'El desarrollo del voto opcional',
       'El dilema del voto facultativo', 'Razones para no promover el voto facultativo'], 'D', 'lectura', passage=4),
    q(48, '¿Cuál de los siguientes enunciados cuestiona mejor los conceptos planteados por el autor?',
      ['La distinción conceptual entre discursos afectivos y técnicos es inapropiada: en la práctica, no es '
       'posible diferenciarlos.',
       'Los discursos afectivos no utilizan muchos datos objetivos: plantear lo contrario supone incurrir en una '
       'contradicción.',
       'La objetividad de los discursos técnicos es aparente: las intenciones persuasivas quedan encubiertas.',
       'El discurso afectivo, invariablemente, utiliza argumentos subjetivos y objetivos simultáneamente.'],
      'A', 'lectura', passage=5),
    q(49, '¿Qué quiere decir el autor con el enunciado "así como la flauta hace bailar a la serpiente, el que '
          'habla desde el discurso afectivo manipula al oyente"?',
      ['Que el discurso afectivo es capaz de conjurar cualquier peligro a través de la manipulación',
       'Que el discurso afectivo puede resultar cautivador para aquel que lo recibe',
       'Que el discurso afectivo es tan placentero que hasta un ser astuto y peligroso podría ser sojuzgado por él',
       'Que el discurso afectivo es una ilusión que no encuentra sustento en la realidad'], 'D', 'lectura', passage=5),
    q(50, '¿Cuál es la intención del texto anterior?',
      ['Proponer las diferencias entre el discurso afectivo y el técnico, y plantear su punto de convergencia',
       'Comparar los tipos de discursos más usuales en los medios de comunicación: el discurso afectivo y el '
       'discurso técnico',
       'Plantear que el discurso afectivo puede presentar elementos propios del discurso técnico; del mismo modo, '
       'el discurso técnico puede apelar a ciertas emociones propias del afectivo',
       'Explicar las distintas estrategias utilizadas por dos tipos de discursos a través de distintos ejemplos '
       'puntuales'], 'A', 'lectura', passage=5),
    q(51, 'Determine el tema central del texto.',
      ['Importancia de los amigos en pacientes terminales.',
       'El tratamiento psicológico de la familia con enfermos.',
       'Acompañamiento familiar de pacientes terminales.',
       'Los psicólogos clínicos y los pacientes terminales.'], 'C', 'lectura', passage=6),
    q(52, 'Es incompatible, con respecto a los casos de crisis familiar, sostener que:',
      ['el diagnóstico de una enfermedad terminal lleva al paciente al duelo.',
       'los familiares de un enfermo terminal deben hallar espacios para compartir.',
       'la despedida de un enfermo terminal depende de cómo es la relación con él.',
       'los vínculos amicales no son recomendables para sobrellevar la angustia.'], 'D', 'lectura', passage=6),
    q(53, 'El vocablo LIBERAR tiene el sentido contextual de:',
      ['manifestar.', 'promover.', 'incitar.', 'empujar.'], 'A', 'lectura', passage=6),
    q(54, 'Puede deducirse del texto, que en el acompañamiento del paciente terminal:',
      ['este debe entender los problemas familiares.',
       'debe tratar de curarse de su enfermedad.',
       'deben dejarse atrás los odios y rencores.',
       'debe ejercitarse una escasa comunicación.'], 'C', 'lectura', passage=6),
    q(55, 'Si no se diera un adecuado acompañamiento psicológico al paciente terminal, muy probablemente:',
      ['éste podría salir adelante de la enfermedad que padece.',
       'éste no podría comprender su enfermedad y ser valiente.',
       'los psicólogos considerarían que su profesión es inútil.',
       'la ciencia médica daría por terminadas sus sugerencias.'], 'B', 'lectura', passage=6),
    q(56, 'El texto se refiere a los trabajos de Piaget sobre:',
      ['la mensurabilidad del tiempo o determinación de su duración.',
       'el desarrollo de la noción del tiempo subjetivo en el niño.',
       'el ordenamiento de sucesos por intervalos y velocidades.',
       'el uso de los relojes como una forma de medir el tiempo.'], 'B', 'lectura', passage=7),
    q(57, 'El término estimar es equivalente a:',
      ['percibir', 'valorar', 'predecir', 'considerar'], 'A', 'lectura', passage=7),
    q(58, 'Se deduce del texto que la mensurabilidad del tiempo posibilita al niño:',
      ['comprender los conceptos de tiempo y espacio.',
       'dejar de lado el uso de cronómetros.',
       'predecir la duración de un acontecimiento.',
       'clasificar la duración de los intervalos.'], 'C', 'lectura', passage=7),
    q(59, 'Se desprende del texto que la tercera etapa del proceso requiere como condición:',
      ['la posibilidad de ordenar acontecimientos.',
       'síntesis entre orden y duración del tiempo.',
       'diferenciar lo anterior de lo posterior.',
       'clasificar la duración del intervalo entre sucesos.'], 'B', 'lectura', passage=7),
    q(60, 'Señale el enunciado incompatible con el contenido del texto.',
      ['La noción de tiempo subjetivo es adquirida de inmediato.',
       'Para entender los sucesos primero hay que ordenarlos.',
       'Los niños de cuatro años no pueden usar relojes.',
       'El tiempo subjetivo proviene de relacionar velocidad y espacio.'], 'A', 'lectura', passage=7),
]

BANK = {
    'year': 2018,
    'title': 'Examen Reconstruido ENP Beca 18 — 2018',
    'duration_min': 120,
    'sections': [
        {'id': 'matematica', 'label': 'Razonamiento Matemático', 'from': 1, 'to': 30},
        {'id': 'lectura', 'label': 'Comprensión Lectora', 'from': 31, 'to': 60},
    ],
    'passages': PASSAGES,
    'questions': QUESTIONS,
}

def main():
    crop()
    b18bank.write_bank(BANK, OUT_JSON)
    os.makedirs(os.path.dirname(PUB_JSON), exist_ok=True)
    shutil.copyfile(OUT_JSON, PUB_JSON)
    issues = b18bank.validate_bank(BANK, expected=60)
    assert not issues, issues
    print(b18bank.qa_report(BANK))
    print('OK  banco 2018 -> %s' % PUB_JSON)

if __name__ == '__main__':
    main()
