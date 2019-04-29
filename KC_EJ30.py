#-*- coding: utf-8 -*
DRINKS = {
            1 : 'Fanta',
            2 : 'Pepsi',
            3 : '7Up',
            'price' : 1
            };

COINS = (10, 20, 50, 1)

def selectDrink(drinks):
    while True:
        drink = input('Selecciona tu bebida:\n'\
                      '(1) Fanta\n'\
                      '(2) Pepsi\n'\
                      '(3) 7Up\n')
                      
        if (drink in drinks and drink != 'price'):
            print('%s vale %s€. Inserta a continuación las monedas' %(drinks[drink], drinks['price']))
            return {'name' : drinks[drink], 'price' : drinks['price']};
        else:
            print('Bebida no válida. Prueba de nuevo')

def payDrink(item, coins):
    pending = float(item['price'])
    while True:
        coin = float(input('Importe pendiente: %s€. Inserta importe de moneda. (Sólo válidos 10c, 20c, 50c y 1€)\n'\
                     'Opciones:\n'\
                     '(10)c\n'\
                     '(20)c\n'\
                     '(30)c\n'\
                     '(1)€\n' %(pending)))
        if coin in COINS:
            if (coin == 1):
                pending = round(pending - coin, 2)
            else:
                pending = round(pending - coin / 100, 2)
            if (pending <= 0):
                giveDrink(item['name'], -pending)
                return
        else:
            print('Moneda no válida. Prueba de nuevo.')
        print(pending)  

def giveDrink(i, change):
    print('Recoge tu %s. El cambio es de %s€' %(i, change))

drink = selectDrink(DRINKS)
payDrink(drink, COINS)