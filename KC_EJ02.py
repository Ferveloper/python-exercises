n1 = int(input('Introduce el primer numero:'))
n2 = int(input('Introduce el segundo numero:'))

# En una sola cadena
print(str(n1) + ' + ' + str(n2) + ' = ' + str(n1 + n2) + '\n' + str(n1) + ' - ' + str(n2) + ' = ' + str(n1 - n2) + '\n' + str(n1) + ' * ' + str(n2) + ' = ' + str(n1 * n2) + '\n' + str(n1) + ' / ' + str(n2) + ' = ' + str(n1 / n2) + '\n' + str(n1) + ' ** ' + str(n2) + ' = ' + str(n1 ** n2) + '\n' + str(n1) + ' % ' + str(n2) + ' = ' + str(n1 % n2))

print('')

# Formatos mas legibles
print '{} + {} = {}'.format(str(n1), str(n2), str(n1 + n2))
print '{} - {} = {}'.format(str(n1), str(n2), str(n1 - n2))
print '{} * {} = {}'.format(str(n1), str(n2), str(n1 * n2))
print '{} / {} = {}'.format(str(n1), str(n2), str(n1 / n2))
print '{} ** {} = {}'.format(str(n1), str(n2), str(n1 ** n2))
print '{} % {} = {}'.format(str(n1), str(n2), str(n1 % n2))

print('')

print '%s + %s = %s' %(n1, n2, n1 + n2)
print '%s - %s = %s' %(n1, n2, n1 - n2)
print '%s * %s = %s' %(n1, n2, n1 * n2)
print '%s / %s = %s' %(n1, n2, n1 / n2)
print '%s ** %s = %s' %(n1, n2, n1 ** n2)
print '%s %% %s = %s' %(str(n1), str(n2), str(n1 % n2))