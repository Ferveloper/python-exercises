#-*- coding: utf-8 -*
def pintarFila(n):
    print('<table>');
    for i in range(1, n + 1):
        print('<tr><td></td></tr>')
    print('</table>')

rows = input('Introduce el número de filas: ')
pintarFila(rows)