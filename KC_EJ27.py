#-*- coding: utf-8 -*
def esPalindromo(string):
    tempString = string.replace(' ','').lower()
    esPalindromo = 'ES'
    for i in range(int(round(len(tempString) / 2, 0))):
        if (tempString[i] != tempString[len(tempString) - 1 - i]):
            esPalindromo = 'NO ES'
            break
    return esPalindromo

text = raw_input('Introduce eun texto: ');
print('El texto ingresado %s palíndromo' %(esPalindromo(text)))