#-*- coding: utf-8 -*
numbers = list()

for i in range(3):
    numbers.append(input('Introduce el número %s: ' %(i+1)))

print 'El mayor es %s' %(max(numbers))
print 'El menor es %s' %(min(numbers))