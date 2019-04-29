#-*- coding: utf-8 -*
vowels = ('a', 'e', 'i', 'o', 'u')

letter = raw_input('Introduce una letra: ')

if letter in vowels:
    type = 'vocal'
else:
    type = 'consonante'

print '%s es letra %s' %(letter, type)