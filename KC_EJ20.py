#-*- coding: utf-8 -*
number = input('Introduce un número: ')
array = list()
for i in range(number):
    array.append(i + 1)
print('%s = %s' %(' + '.join(str(i) for i in array), sum(array)))