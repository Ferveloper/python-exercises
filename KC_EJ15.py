#-*- coding: utf-8 -*
people = list()

for i in range(3):
    people.append(list())
    people[i].append(raw_input("Nombre de la persona %s: " %(i + 1)))
    people[i].append(raw_input("Nota 1 de la persona %s: " %(i + 1)))
    people[i].append(raw_input("Nota 2 de la persona %s: " %(i + 1)))
    people[i].append(raw_input("Nota 3 de la persona %s: " %(i + 1)))
    people[i] = tuple(people[i])
    print('--------------------')
    # persona_1 = (nombre_1, nota1_1, nota2_1, nota3_1)

print(people)



