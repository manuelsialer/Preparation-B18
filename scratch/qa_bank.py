import json, io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
b = json.load(open(r'scratch\exams\banks\2023.json', encoding='utf-8'))
# caracteres no esperados (fuera de latin, numeros, puntuacion comun, $ \ )
bad_re = re.compile(r'[^\w\s$\\\-\+\*/=<>(),.;:!?¿¡%°²³¬·•§†‡…‰\[\]{}|]/#@&~^`\'"“”‘’–—•×÷±≤≥≈≠∞√∑∏∫πθαβγδλμφω°´¨`]+')
print('--- stems/opciones con caracteres sospechosos ---')
for q in b['questions']:
    txt = q['stem'] + ' || ' + ' || '.join(q['options'])
    hits = set(bad_re.findall(txt))
    if hits:
        print(q['id'], sorted(hits)[:10])
print()
print('--- preguntas 1-30: muestra de stems ---')
for q in b['questions'][:30]:
    print(q['id'], '|', q['stem'][:160])
    print('    opts:', q['options'])
