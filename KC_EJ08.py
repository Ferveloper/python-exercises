#-*- coding: utf-8 -*
number = int(input('Introduce un número: '))

if number == 0:
    result = 'Cero'
else:
    if number > 0:
        result = 'Positivo'
    else:
        result = 'Negativo'
    if number % 2 == 0:
        result += ' par'
    else:
        result += ' impar'

print(result)


