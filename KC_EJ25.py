#-*- coding: utf-8 -*

import random

random = random.randint(1, 100)

for i in range(1, 6):
    guess = input('Escribe un número: ')
    if (guess != random and i != 5):
        print('Intenta con un número %s (te quedan %s oportunidad%s)' %('menor' if guess > random else 'mayor', 5 - i, 'es' if i != 4 else ''))
    else:
        break

if guess == random:
    print('¡Bien, lo has adivinado :D! Era el %s' %(random))
else:
    print('Lo siento, has perdido. Era el %s' %(random))