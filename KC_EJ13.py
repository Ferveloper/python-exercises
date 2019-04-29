#-*- coding: utf-8 -*
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

start = input('Valor de inicio: ')
end = input('Valor de fin: ')

if (start < array[0] or end > array[len(array) - 1] or start > end):
    print('El rango debe entre 1 y 20 y el inicio debe ser menor que el final')
else:
    print(array[start:end])