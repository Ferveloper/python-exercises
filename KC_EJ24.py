#-*- coding: utf-8 -*
people = list()
i = 0;

while True:
    people.append({})
    people[i]['name'] = raw_input('Introduce el nombre de la persona (o escribe "terminar" para finalizar): ')
    
    if (people[i]['name'] == 'terminar'): 
        people.pop()
        break

    people[i]['grades'] = list()
    for j in range(3):
        people[i]['grades'].append(input('Introduce la %sª calificación de %s: ' %(j + 1, people[i]['name'])))
    
    people[i]['average'] = int(round(sum(people[i]['grades']) / len(people[i]['grades']), 0))
    i += 1

# Otra opción es people = sorted(people, key = lambda k : k['average'], reverse = True),
# pero sorted() es más lenta, según la documentación
people.sort(key = lambda k : k['average'], reverse = True)

for i in range(len(people)):
    print(people[i]['name'] + ' : ' + str(people[i]['average']))