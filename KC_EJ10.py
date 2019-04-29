#-*- coding: utf-8 -*
movies = {
'1' : 'Star Wars I: La amenaza fantasma',
'2' : 'Star Wars II: El ataque de los clones',
'3' : 'Star Wars III: La venganza de los Sith',
'4' : 'Star Wars IV: Una nueva esperanza',
'5' : 'Star Wars V: El Imperio contraataca',
'6' : 'Star Wars VI: El retorno del Jedi',
'7' : 'Star Wars VII: El despertar de la Fuerza',
'8' : 'Star Wars VIII: Los últimos Jedi',
'I' : 'Star Wars I: La amenaza fantasma',
'II' : 'Star Wars II: El ataque de los clones',
'III' : 'Star Wars III: La venganza de los Sith',
'IV' : 'Star Wars IV: Una nueva esperanza',
'V' : 'Star Wars V: El Imperio contraataca',
'VI' : 'Star Wars VI: El retorno del Jedi',
'VII' : 'Star Wars VII: El despertar de la Fuerza',
'VIII' : 'Star Wars VIII: Los últimos Jedi'
}

movie = raw_input('Introduce un número del 1 al 8 o del I al VIII: ')

print(movies[movie])