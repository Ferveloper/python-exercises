#-*- coding: utf-8 -*
people = list()

for i in range(10):
    people.append({'name': '', 'age': 0})
    people[i]['name'] = raw_input('Introduce el nombre de la %sª persona: ' %(i + 1))
    people[i]['age'] = input('Introduce la edad de la %sª persona: ' %(i + 1))

canVote = map(lambda person : person['name'], filter(lambda person : person['age'] >= 18, people))
last = canVote.pop()
canVote = ', '.join(canVote) + ' y ' + last

print('Tienen derecho al voto %s' %(canVote))