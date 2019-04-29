#-*- coding: utf-8 -*
list = {
            'Pedro' : 'pedro.picapiedra@gmail.com',
            'Pablo' : 'pmarmol123@gmail.com',
            'Bob' : 'bob@gmail.com'
        }
name = raw_input('Introduce un nombre:')
if name in list:
    print(list[name])
else:
    print('No se encuentra el nombre en la lista')