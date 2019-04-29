#-*- coding: utf-8 -
def pintarRectangulo(side, char):
    print(char * side)
    for i in range(side - 2):
        print(char + " " * (side - 2) + char);
    print(char * side)

side = input('Introduce el tamaño del lado:')
char = raw_input('Introduce la figura del lado:')
pintarRectangulo(side, char)