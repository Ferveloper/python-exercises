#-*- coding: utf-8 -*-
grades = list()

for i in range(3):
    grades.append(float(input('introduce la ' + str(i + 1) + 'ª nota:')))

# Con el operador %
print 'La media es: %s' %(round(sum(grades)/len(grades),1))

# Con el método format
print 'La media es: {}'.format(str(round(sum(grades)/len(grades),1)))