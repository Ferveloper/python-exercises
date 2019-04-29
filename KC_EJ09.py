#-*- coding: utf-8 -*
value = float(input('Introduce el valor: '))

fin = False

while fin != True:
    print 'Elige una opción:'
    print '(1) Convertir de EUR a USD'
    print '(2) Convertir de USD a EUR'
    change = input()

    if change == 1:
        print '$%s USD' %(round(value * 1.06, 2))
        fin = True
    elif change == 2:
        print '$%s EUR' %(round(value / 1.06, 2))
        fin = True
    else:
        print 'Opción no válida \n'
