#-*- coding: utf-8 -*-
grades = list()

for i in range(3):
    grades.append(float(input('Introduce la %sª nota: ' %(i+1))))

ave = sum(grades)/len(grades)

if ave < 5:
    result = 'No Apto'
else:
    result = 'Apto'

print 'Resultado: {}'.format(result)