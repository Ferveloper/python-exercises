#-*- coding: utf-8 -*
array = list()
for i in range(10):
    array.append(input('Introduce el %s%s número: ' %(i + 1, 'er' if i == 0 else 'o')))

print(filter(lambda n: n % 2 == 0, array))